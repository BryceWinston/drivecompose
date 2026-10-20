"""Scene–Asset Decomposer：规范查询先放到各时刻，再按可见性读取图像特征。"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import TokenKind
from .geometry import cube_directions, inverse_se3, lift_depth, project_pinhole, skin_transforms, transform_points


@dataclass
class ActorTrack:
    actor_id: str
    kind: TokenKind
    instance_label: int                  # 图像 instance map 中稳定的正整数
    world_from_actor: np.ndarray         # [T,4,4]
    dimensions: np.ndarray              # [3], 固定身份尺寸
    human_support: np.ndarray | None = None  # [Q,3], 规范人体表面/邻域
    skin_weights: np.ndarray | None = None   # [Q,J]
    rest_global: np.ndarray | None = None    # [J,4,4]
    posed_global: np.ndarray | None = None   # [T,J,4,4]
    parents: tuple[int, ...] = ()


@dataclass
class SceneEvidence:
    features: np.ndarray                 # [T,V,h,w,F]
    depth: np.ndarray                    # [T,V,h,w], camera z in meters
    confidence: np.ndarray               # [T,V,h,w], trained geometric confidence
    instance: np.ndarray                 # [T,V,h,w], 0=background
    semantics: np.ndarray                # 0 road,1 static,2 vehicle,3 human,4 sky,5 ego
    intrinsics: np.ndarray               # [V,3,3], original image coordinates
    world_from_camera: np.ndarray        # [T,V,4,4]
    image_size: tuple[int, int]
    tracks: tuple[ActorTrack, ...]


@dataclass
class QueryBlock:
    kind: TokenKind
    actor_id: str | None
    positions: np.ndarray                # [Q,3], local coordinates; sky = unit direction
    scales: np.ndarray                   # [Q,3], support-cell size in meters
    world_reference: np.ndarray          # [Q,3], sky = world unit direction
    groups: np.ndarray                   # [Q], local attention neighborhoods
    track: ActorTrack | None = None


@dataclass
class QueryBundle:
    blocks: tuple[QueryBlock, ...]
    features: np.ndarray                 # [N,F+1], fused features + signed depth residual
    known: np.ndarray                    # [N], high-confidence observed support
    free: np.ndarray                     # [N], observed free-space support
    confidence: np.ndarray               # [N]
    context: np.ndarray                  # [T*V,F+1]

    def layout(self) -> dict[str, np.ndarray]:
        groups, offset = [], 0
        for b in self.blocks:
            g = b.groups - b.groups.min()
            groups.append(g + offset)
            offset += int(g.max()) + 1
        return {
            "kind": np.concatenate([np.full(len(b.positions), int(b.kind)) for b in self.blocks]),
            "positions": np.concatenate([b.positions for b in self.blocks]),
            "scales": np.concatenate([b.scales for b in self.blocks]),
            "world_reference": np.concatenate([b.world_reference for b in self.blocks]),
            "groups": np.concatenate(groups),
        }


def grid_support(lower: np.ndarray, upper: np.ndarray,
                 shape: tuple[int, int, int]) -> tuple[np.ndarray, np.ndarray]:
    if min(shape) < 1 or np.any(upper <= lower):
        raise ValueError("查询支撑网格无效")
    step = (upper - lower) / np.asarray(shape)
    axes = [lower[j] + (np.arange(shape[j]) + 0.5) * step[j] for j in range(3)]
    points = np.stack(np.meshgrid(*axes, indexing="ij"), -1).reshape(-1, 3)
    return points.astype(np.float32), np.broadcast_to(step, points.shape).copy()


def observed_support(e: SceneEvidence, lower: np.ndarray, upper: np.ndarray,
                     track: ActorTrack | None = None, max_points=2048, voxel_size=0.20) -> np.ndarray:
    samples = []
    for t in range(e.depth.shape[0]):
        for v in range(e.depth.shape[1]):
            valid = np.isfinite(e.depth[t, v]) & (e.depth[t, v] > 0) & (e.confidence[t, v] >= 0.8)
            if track is None:
                valid &= (e.instance[t, v] == 0) & (e.semantics[t, v] <= 1)
            else:
                valid &= e.instance[t, v] == track.instance_label
            camera = lift_depth(e.depth[t, v], e.intrinsics[v], e.image_size)
            points = transform_points(camera[valid], e.world_from_camera[t, v])
            if track is not None:
                points = transform_points(points, inverse_se3(track.world_from_actor[t]))
            points = points[np.all((points >= lower) & (points <= upper), axis=-1)]
            samples.append(points)
    points = np.concatenate(samples)
    if not len(points):
        return np.empty((0, 3), dtype=np.float32)
    _, indices = np.unique(np.floor(points / voxel_size).astype(int), axis=0, return_index=True)
    if len(indices) > max_points:
        indices = indices[np.linspace(0, len(indices)-1, max_points).astype(int)]
    return points[indices].astype(np.float32)


def make_blocks(evidence: SceneEvidence, bounds: np.ndarray,
                background_shape=(20, 12, 6), vehicle_shape=(8, 4, 4), sky_resolution=4) -> tuple[QueryBlock, ...]:
    points, scales = grid_support(bounds[0], bounds[1], background_shape)
    anchors = observed_support(evidence, bounds[0], bounds[1])
    points = np.concatenate([anchors, points])
    scales = np.concatenate([np.full_like(anchors, 0.20), scales])
    cells = np.floor((points - bounds[0]) / 4).astype(int)
    _, groups = np.unique(cells, axis=0, return_inverse=True)
    blocks = [QueryBlock(TokenKind.BACKGROUND, None, points, scales, points.copy(), groups)]
    for track in evidence.tracks:
        if track.kind == TokenKind.VEHICLE:
            p, s = grid_support(-track.dimensions / 2, track.dimensions / 2, vehicle_shape)
            anchors = observed_support(evidence, -track.dimensions/2, track.dimensions/2, track, max_points=512)
            p = np.concatenate([anchors, p])
            s = np.concatenate([np.full_like(anchors, 0.20), s])
            reference = transform_points(p, track.world_from_actor[0])
        elif track.kind == TokenKind.HUMAN:
            if any(x is None for x in (track.human_support, track.skin_weights, track.rest_global, track.posed_global)):
                raise ValueError("人体轨迹必须有规范支撑和骨架绑定")
            p = track.human_support
            s = np.full_like(p, 0.10)  # 只是支撑邻域，不是人体体型或高斯大小
            transforms = skin_transforms(track.skin_weights, track.rest_global, track.posed_global[0])
            reference = transform_points(p, track.world_from_actor[0] @ transforms)
        else:
            raise ValueError("资产只支持刚体车辆和骨架人体")
        blocks.append(QueryBlock(track.kind, track.actor_id, p, s, reference, np.zeros(len(p), dtype=int), track))
    directions = cube_directions(sky_resolution).reshape(-1, 3)
    blocks.append(QueryBlock(TokenKind.SKY, None, directions, np.ones_like(directions), directions.copy(),
                             np.repeat(np.arange(6), sky_resolution ** 2)))
    return tuple(blocks)


class SceneAssetDecomposer:
    def __init__(self, depth_tolerance=0.15, relative_tolerance=0.02,
                 confidence_threshold=0.8, free_votes=2):
        self.depth_tolerance = depth_tolerance
        self.relative_tolerance = relative_tolerance
        self.confidence_threshold = confidence_threshold
        self.free_votes = free_votes

    def decompose(self, evidence: SceneEvidence, blocks: tuple[QueryBlock, ...]) -> QueryBundle:
        fused, known, free, confidence = [], [], [], []
        for block in blocks:
            f, k, empty, c = self._aggregate(evidence, block)
            fused.append(f); known.append(k); free.append(empty); confidence.append(c)
        context = evidence.features.mean(axis=(2, 3)).reshape(-1, evidence.features.shape[-1])
        context = np.pad(context, ((0, 0), (0, 1)))
        return QueryBundle(blocks, np.concatenate(fused), np.concatenate(known), np.concatenate(free),
                           np.concatenate(confidence), context.astype(np.float32))

    def _aggregate(self, e: SceneEvidence, block: QueryBlock):
        t_count, v_count, h, w, channels = e.features.shape
        n = len(block.positions)
        total = np.zeros((n, channels + 1), dtype=np.float32)
        mass = np.zeros(n)
        free_count = np.zeros(n, dtype=int)
        max_confidence = np.zeros(n)
        for t in range(t_count):
            if block.kind == TokenKind.VEHICLE:
                points = transform_points(block.positions, block.track.world_from_actor[t])
            elif block.kind == TokenKind.HUMAN:
                transforms = skin_transforms(block.track.skin_weights, block.track.rest_global, block.track.posed_global[t])
                points = transform_points(block.positions, block.track.world_from_actor[t] @ transforms)
            else:
                points = block.positions
            for v in range(v_count):
                pose = e.world_from_camera[t, v]
                if block.kind == TokenKind.SKY:
                    # 天空位于无穷远：仅应用相机旋转，不应用平移。
                    camera_points = points @ pose[:3, :3]
                    z = camera_points[:, 2]
                    pixel = camera_points @ e.intrinsics[v].T
                    uv = pixel[:, :2] / np.where(z > 1e-8, z, 1)[:, None]
                else:
                    uv, z = project_pinhole(points, pose, e.intrinsics[v])
                image_h, image_w = e.image_size
                x = np.floor((uv[:, 0] + 0.5) * w / image_w).astype(int)
                y = np.floor((uv[:, 1] + 0.5) * h / image_h).astype(int)
                inside = (z > 1e-6) & (x >= 0) & (x < w) & (y >= 0) & (y < h)
                x, y = np.clip(x, 0, w - 1), np.clip(y, 0, h - 1)
                sem = e.semantics[t, v, y, x]
                conf = e.confidence[t, v, y, x]
                if block.kind == TokenKind.SKY:
                    seen = inside & (sem == 4) & (conf >= self.confidence_threshold)
                    residual = np.zeros(n)
                    weight = seen.astype(float) * conf
                else:
                    depth = e.depth[t, v, y, x]
                    tolerance = self.depth_tolerance + self.relative_tolerance * np.maximum(depth, 0)
                    reliable = inside & np.isfinite(depth) & (depth > 0) & (conf >= self.confidence_threshold) & (sem != 4) & (sem != 5)
                    expected = 0 if block.track is None else block.track.instance_label
                    belongs = e.instance[t, v, y, x] == expected
                    if block.track is None:
                        belongs &= (sem == 0) | (sem == 1)
                    residual = np.where(reliable, (depth - z) / tolerance, 0)
                    seen = reliable & belongs & (np.abs(residual) <= 1)
                    weight = seen * conf * np.exp(-0.5 * residual ** 2)
                    free_count += reliable & (z + np.linalg.norm(block.scales, axis=-1) / 2 < depth - tolerance)
                observations = np.concatenate([e.features[t, v, y, x], residual[:, None]], -1)
                total += (weight[:, None] * observations).astype(np.float32)
                mass += weight
                max_confidence = np.maximum(max_confidence, np.where(seen, conf, 0))
        observed = mass > 0
        empty = (free_count >= self.free_votes) & ~observed
        total /= np.maximum(mass[:, None], 1e-8)
        return total, observed, empty, max_confidence.astype(np.float32)
