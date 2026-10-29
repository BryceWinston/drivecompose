"""在线路径只依赖固定资产与当前状态，不调用编码器或生成网络。"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np

from .contracts import GaussianSet, SimulationState, WorldVault
from .geometry import check_se3, normalize, skin_transforms, transform_points


def transform_gaussians(source: GaussianSet, transforms: np.ndarray) -> GaussianSet:
    """支持一个刚体变换或逐高斯仿射；中心、协方差、外观方向共同更新。"""
    linear = transforms[..., :3, :3]
    if np.any(np.linalg.svd(linear, compute_uv=False)[..., -1] < 1e-4):
        raise ValueError("姿态超出支持范围：蒙皮局部变换接近奇异")
    means = transform_points(source.means, transforms)
    covariance = linear @ source.covariance @ np.swapaxes(linear, -1, -2)
    axes = source.direction_to_local @ np.linalg.inv(linear)
    return GaussianSet(means, covariance, source.opacity, source.appearance, axes)


def concatenate_gaussians(sets: list[GaussianSet]) -> GaussianSet:
    if not sets:
        raise ValueError("场景至少需要一个高斯集合")
    return GaussianSet(**{key: np.concatenate([getattr(g, key) for g in sets], axis=0)
                          for key in ("means", "covariance", "opacity", "appearance", "direction_to_local")})


def evaluate_appearance(gaussians: GaussianSet, camera_center: np.ndarray) -> np.ndarray:
    """一阶局部方向外观；它是确定性的外观模型，不执行图像生成。"""
    directions = normalize(camera_center[None] - gaussians.means)
    local = normalize(np.einsum("nij,nj->ni", gaussians.direction_to_local, directions))
    rgb = gaussians.appearance[..., 0] + np.einsum("ncj,nj->nc", gaussians.appearance[..., 1:], local)
    return np.maximum(rgb, 0)


@dataclass(frozen=True)
class AssembledScene:
    gaussians: GaussianSet
    sky: np.ndarray
    actor_ranges: dict[str, tuple[int, int]]
    bounds: np.ndarray
    sky_valid: np.ndarray


class StateComposer:
    def assemble(self, world: WorldVault, state: SimulationState) -> AssembledScene:
        check_se3(state.world_from_ego)
        unknown = (set(state.rigid_poses) - set(world.rigids)) | (set(state.human_poses) - set(world.humans))
        if unknown:
            raise KeyError(f"状态引用未构建的资产：{sorted(unknown)}")
        sets = [world.background]
        ranges = {}
        offset = len(world.background.means)
        # 状态中的资产即为本步活动资产；不根据原始日志时间窗自动消失。
        for actor_id in sorted(state.rigid_poses):
            pose = state.rigid_poses[actor_id]
            check_se3(pose)
            g = transform_gaussians(world.rigids[actor_id].gaussians, pose)
            sets.append(g)
            ranges[actor_id] = (offset, offset + len(g.means))
            offset += len(g.means)
        for actor_id in sorted(state.human_poses):
            asset, pose = world.humans[actor_id], state.human_poses[actor_id]
            check_se3(pose.world_from_root)
            check_se3(pose.posed_global)
            root = asset.parents.index(-1)
            if not np.allclose(pose.posed_global[root], asset.rest_global[root], atol=1e-5):
                raise ValueError("整体人体朝向应由根位姿控制，不得重复写入根关节")
            transforms = skin_transforms(asset.weights, asset.rest_global, pose.posed_global)
            g = transform_gaussians(asset.gaussians, pose.world_from_root @ transforms)
            sets.append(g)
            ranges[actor_id] = (offset, offset + len(g.means))
            offset += len(g.means)
        return AssembledScene(concatenate_gaussians(sets), world.sky, ranges, world.bounds, world.sky_valid)


@dataclass(frozen=True)
class RenderCamera:
    intrinsics: np.ndarray
    ego_from_camera: np.ndarray
    image_size: tuple[int, int]


@dataclass(frozen=True)
class CameraObservation:
    rgb: np.ndarray
    depth: np.ndarray
    alpha: np.ndarray
    coverage: np.ndarray                    # 支撑区域覆盖度，不是正确性概率


class GaussianRasterizer(Protocol):
    def render(self, scene: AssembledScene, world_from_camera: np.ndarray,
               intrinsics: np.ndarray, image_size: tuple[int, int]) -> CameraObservation:
        """处理投影、遮挡、天空及有效域。越出 bounds 的无表面射线不得靠天空补色取得有效 coverage。

        有效天空观测须同时遵守 scene.sky_valid；真实遮挡表面按 bounds 和几何支持判定。
        """
        ...


class StateDrivenRenderer:
    def __init__(self, backend: GaussianRasterizer):
        self.backend = backend
        self.composer = StateComposer()

    def observe(self, world: WorldVault, state: SimulationState,
                cameras: tuple[RenderCamera, ...]) -> tuple[CameraObservation, ...]:
        center = state.world_from_ego[:3, 3]
        if np.any(center < world.bounds[0]) or np.any(center > world.bounds[1]):
            raise ValueError("自车离开世界支撑范围，须另建场景或终止本次 rollout")
        scene = self.composer.assemble(world, state)
        observations = []
        for camera in cameras:
            check_se3(camera.ego_from_camera)
            pose = state.world_from_ego @ camera.ego_from_camera
            if np.any(pose[:3, 3] < world.bounds[0]) or np.any(pose[:3, 3] > world.bounds[1]):
                raise ValueError("相机中心离开世界支撑范围")
            observation = self.backend.render(scene, pose, camera.intrinsics, camera.image_size)
            coverage = observation.coverage
            if coverage.shape != camera.image_size or not np.isfinite(coverage).all() or np.any((coverage < 0) | (coverage > 1)):
                raise ValueError("后端须返回与图像匹配的 [0,1] 有效域")
            observations.append(observation)
        return tuple(observations)
