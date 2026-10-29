"""通过渲染结果检查补全内容与输入观测的一致性。"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import DrivingLog, HumanState, SimulationState, TokenKind, WorldVault
from .decomposition import SceneEvidence
from .geometry import inverse_se3
from .rendering import GaussianRasterizer, StateComposer


@dataclass(frozen=True)
class ValidationReport:
    accepted: bool
    checked_pixels: int
    checked_geometry_pixels: int
    absolute_rgb_error: float
    absolute_depth_error: float
    minimum_view_coverage: float
    rgb_regression: float
    new_front_intrusion_fraction: float
    maximum_view_rgb_error: float
    maximum_view_front_fraction: float
    notes: tuple[str, ...]


class ObservedViewValidator:
    def __init__(self, rasterizer: GaussianRasterizer, max_rgb_regression=0.03,
                 max_front_fraction=0.01, depth_tolerance=0.15, confidence_threshold=0.8,
                 max_absolute_rgb=0.15, max_absolute_depth=0.75, minimum_coverage=0.9):
        self.rasterizer = rasterizer
        self.max_rgb_regression = max_rgb_regression
        self.max_front_fraction = max_front_fraction
        self.depth_tolerance = depth_tolerance
        self.confidence_threshold = confidence_threshold
        self.max_absolute_rgb = max_absolute_rgb
        self.max_absolute_depth = max_absolute_depth
        self.minimum_coverage = minimum_coverage

    def validate(self, candidate: WorldVault, observed_only: WorldVault,
                 log: DrivingLog, evidence: SceneEvidence) -> ValidationReport:
        total, geometry_total, rgb_change, new_intrusions = 0, 0, 0.0, 0
        rgb_absolute, depth_absolute, valid_depth_total = 0.0, 0.0, 0
        view_rgb, view_front, view_depth, view_coverage = [], [], [], []
        composer = StateComposer()
        _, _, h, w, _ = evidence.features.shape
        for t in range(len(log.timestamps)):
            rigids = {a.actor_id: a.world_from_actor[t] for a in evidence.tracks if a.kind == TokenKind.RIGID}
            humans = {a.actor_id: HumanState(a.world_from_actor[t], a.posed_global[t])
                      for a in evidence.tracks if a.kind == TokenKind.HUMAN}
            ego = evidence.world_from_camera[t, 0] @ inverse_se3(log.rig_from_camera[0])
            state = SimulationState(ego, rigids, humans)
            scenes = [composer.assemble(world, state) for world in (observed_only, candidate)]
            for v in range(log.images.shape[1]):
                # 用特征网格中心对齐渲染监督，避免把插值后的预测当作新增真值。
                ih, iw = log.images.shape[-2:]
                y = np.clip(np.rint((np.arange(h)+0.5)*ih/h-0.5).astype(int), 0, ih-1)
                x = np.clip(np.rint((np.arange(w)+0.5)*iw/w-0.5).astype(int), 0, iw-1)
                renders = [self.rasterizer.render(s, evidence.world_from_camera[t, v], log.intrinsics[v], (ih, iw))
                           for s in scenes]
                rgbs = [r.rgb[y[:, None], x[None]] for r in renders]
                depths = [r.depth[y[:, None], x[None]] for r in renders]
                alphas = [r.alpha[y[:, None], x[None]] for r in renders]
                coverage = renders[1].coverage[y[:, None], x[None]] > 0.5
                if not all(np.isfinite(rgb).all() for rgb in rgbs):
                    raise ValueError("渲染后端返回非有限颜色")
                target = log.images[t, v].transpose(1, 2, 0)[y[:, None], x[None]]
                mask = (evidence.confidence[t, v] >= self.confidence_threshold) & (evidence.semantics[t, v] != 5)
                if not mask.any():
                    view_coverage.append(0.0)
                    continue
                # 每像素限制退化，避免其他像素的改善抵消明显的新遮挡。
                delta = np.maximum(np.abs(rgbs[1]-target).mean(-1)-np.abs(rgbs[0]-target).mean(-1), 0)
                rgb_change += float(delta[mask].sum())
                measured_depth = evidence.depth[t, v]
                geometry_mask = mask & (evidence.semantics[t, v] != 4) & np.isfinite(measured_depth) & (measured_depth > 0)
                valid_depth = geometry_mask & coverage & (alphas[1] > 0.1) & np.isfinite(depths[1]) & (depths[1] > 0)
                front = [(a > 0.1) & (d < measured_depth-self.depth_tolerance) for a, d in zip(alphas, depths)]
                intrusion = int((front[1] & ~front[0] & geometry_mask).sum())
                new_intrusions += intrusion
                rgb_error = np.abs(rgbs[1]-target).mean(-1)
                rgb_absolute += float(rgb_error[mask].sum())
                view_rgb.append(float(rgb_error[mask].mean()))
                view_coverage.append(float(coverage[mask].mean()))
                if geometry_mask.any():
                    view_front.append(intrusion / int(geometry_mask.sum()))
                    view_coverage.append(float(valid_depth.sum() / geometry_mask.sum()))
                    if valid_depth.any():
                        error = np.abs(depths[1][valid_depth]-measured_depth[valid_depth])
                        depth_absolute += float(error.sum())
                        valid_depth_total += int(valid_depth.sum())
                        view_depth.append(float(error.mean()))
                geometry_total += int(geometry_mask.sum())
                total += int(mask.sum())
        regression = rgb_change / max(total, 1)
        fraction = new_intrusions / max(geometry_total, 1)
        rgb_error = rgb_absolute / max(total, 1)
        depth_error = depth_absolute / max(valid_depth_total, 1)
        min_coverage = min(view_coverage, default=0.0)
        max_rgb = max(view_rgb, default=float("inf"))
        max_front = max(view_front, default=float("inf"))
        accepted = (total > 0 and geometry_total > 0 and valid_depth_total > 0
                    and regression <= self.max_rgb_regression and fraction <= self.max_front_fraction
                    and max_rgb <= self.max_absolute_rgb and max(view_depth, default=float("inf")) <= self.max_absolute_depth
                    and max_front <= self.max_front_fraction and min_coverage >= self.minimum_coverage)
        return ValidationReport(accepted, total, geometry_total, rgb_error, depth_error, min_coverage,
                                regression, fraction, max_rgb, max_front,
                                ("使用编码器预测深度检查观测一致性。",))
