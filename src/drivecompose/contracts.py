"""持久世界数据与每步状态分开定义；持久数组复制后设为只读。"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum
from types import MappingProxyType
from typing import Mapping

import numpy as np

from .geometry import check_se3


QUERY_SCHEMA = "drivecompose-rigid-v2"


def readonly(value, dtype=np.float32) -> np.ndarray:
    out = np.array(value, dtype=dtype, copy=True)
    if not np.isfinite(out).all():
        raise ValueError("数组包含非有限值")
    out.setflags(write=False)
    return out


class TokenKind(IntEnum):
    BACKGROUND = 0
    RIGID = 1                         # 刚体资产类型
    HUMAN = 2
    SKY = 3


@dataclass(frozen=True)
class DrivingLog:
    images: np.ndarray                    # [T,V,3,H,W], RGB in [0,1]
    timestamps: np.ndarray                # [T], seconds
    intrinsics: np.ndarray                # [V,3,3], rectified pinhole
    rig_from_camera: np.ndarray           # [V,4,4]
    world_from_rig: np.ndarray | None = None  # [T,4,4]

    def validate(self) -> None:
        if self.images.ndim != 5 or self.images.shape[2] != 3:
            raise ValueError("图像应为 [T,V,3,H,W]")
        t, v = self.images.shape[:2]
        if min(self.images.shape) < 1 or not np.isfinite(self.images).all():
            raise ValueError("图像不能为空或含非有限值")
        if self.images.min() < 0 or self.images.max() > 1:
            raise ValueError("图像应归一化到 [0,1]")
        if self.timestamps.shape != (t,) or not np.isfinite(self.timestamps).all() or np.any(np.diff(self.timestamps) <= 0):
            raise ValueError("时间戳须严格递增")
        if self.intrinsics.shape != (v, 3, 3) or self.rig_from_camera.shape != (v, 4, 4):
            raise ValueError("标定数量与相机数量不符")
        if not np.isfinite(self.intrinsics).all() or np.any(np.linalg.det(self.intrinsics) <= 0):
            raise ValueError("内参必须有效且可逆")
        check_se3(self.rig_from_camera)
        if self.world_from_rig is not None:
            if self.world_from_rig.shape != (t, 4, 4):
                raise ValueError("自车位姿数量与时间戳不符")
            check_se3(self.world_from_rig)


@dataclass(frozen=True)
class GaussianSet:
    means: np.ndarray                     # [N,3]
    covariance: np.ndarray                # [N,3,3], SPD
    opacity: np.ndarray                   # [N]
    appearance: np.ndarray                # [N,3,4]: base RGB + local directional RGB
    direction_to_local: np.ndarray | None = None  # [N,3,3]

    def __post_init__(self):
        for name in ("means", "covariance", "opacity", "appearance"):
            object.__setattr__(self, name, readonly(getattr(self, name)))
        n = len(self.means)
        shapes = {"means": (n, 3), "covariance": (n, 3, 3), "opacity": (n,), "appearance": (n, 3, 4)}
        for name, shape in shapes.items():
            if getattr(self, name).shape != shape:
                raise ValueError(f"{name} 形状应为 {shape}")
        if np.any((self.opacity < 0) | (self.opacity > 1)):
            raise ValueError("不透明度须在 [0,1]")
        if not np.allclose(self.covariance, self.covariance.swapaxes(-1, -2), atol=1e-6):
            raise ValueError("协方差必须对称")
        if np.any(np.linalg.eigvalsh(self.covariance) <= 0):
            raise ValueError("协方差必须正定")
        axes = np.broadcast_to(np.eye(3), (n, 3, 3)) if self.direction_to_local is None else self.direction_to_local
        if np.shape(axes) != (n, 3, 3) or np.any(np.abs(np.linalg.det(axes)) < 1e-8):
            raise ValueError("外观方向映射必须可逆")
        object.__setattr__(self, "direction_to_local", readonly(axes))


@dataclass(frozen=True)
class RigidAsset:
    """固定规范刚体资产；状态仅控制整体 SE(3) 位姿。"""
    actor_id: str
    gaussians: GaussianSet
    dimensions: np.ndarray                 # [3], length,width,height in actor axes

    def __post_init__(self):
        d = readonly(self.dimensions)
        if d.shape != (3,) or np.any(d <= 0):
            raise ValueError("刚体尺寸应为三个正数")
        object.__setattr__(self, "dimensions", d)


@dataclass(frozen=True)
class HumanAvatarAsset:
    actor_id: str
    gaussians: GaussianSet
    weights: np.ndarray                    # [N,J]
    rest_global: np.ndarray                # [J,4,4], in root coordinates
    parents: tuple[int, ...]

    def __post_init__(self):
        w, rest = readonly(self.weights), readonly(self.rest_global)
        if w.shape != (len(self.gaussians.means), len(self.parents)) or rest.shape != (len(self.parents), 4, 4):
            raise ValueError("人体绑定维度不符")
        if np.any(w < 0) or not np.allclose(w.sum(-1), 1, atol=1e-5):
            raise ValueError("人体绑定权重无效")
        if any(p < -1 or p >= j for j, p in enumerate(self.parents)):
            raise ValueError("骨架拓扑无效")
        if self.parents.count(-1) != 1:
            raise ValueError("人体骨架必须只有一个根节点")
        check_se3(rest)
        object.__setattr__(self, "weights", w)
        object.__setattr__(self, "rest_global", rest)


@dataclass(frozen=True)
class HumanState:
    world_from_root: np.ndarray
    posed_global: np.ndarray               # [J,4,4], current pose in root frame


@dataclass(frozen=True)
class SimulationState:
    world_from_ego: np.ndarray
    rigid_poses: Mapping[str, np.ndarray]
    human_poses: Mapping[str, HumanState]
    elapsed_seconds: float = 0.0            # sim bookkeeping; never controls asset lifetime


@dataclass(frozen=True)
class WorldVault:
    background: GaussianSet
    sky: np.ndarray                        # [6,S,S,3], linear RGB
    rigids: Mapping[str, RigidAsset]
    humans: Mapping[str, HumanAvatarAsset]
    bounds: np.ndarray                     # [2,3], supported world volume
    build_seed: int
    metadata: Mapping[str, str] = field(default_factory=dict)
    sky_valid: np.ndarray | None = None     # [6,S,S], validated sky directions only

    def __post_init__(self):
        sky, bounds = readonly(self.sky), readonly(self.bounds)
        if sky.ndim != 4 or sky.shape[0] != 6 or sky.shape[-1] != 3 or sky.shape[1] != sky.shape[2] or sky.shape[1] < 1:
            raise ValueError("天空应为 [6,S,S,3]")
        if np.any(sky < 0):
            raise ValueError("天空辐射值须非负")
        if bounds.shape != (2, 3) or np.any(bounds[0] >= bounds[1]):
            raise ValueError("世界支撑范围无效")
        ids = list(self.rigids) + list(self.humans)
        if len(set(ids)) != len(ids):
            raise ValueError("刚体与人体 ID 必须互异")
        for key, asset in list(self.rigids.items()) + list(self.humans.items()):
            if key != asset.actor_id:
                raise ValueError("资产键与身份不一致")
        object.__setattr__(self, "sky", sky)
        object.__setattr__(self, "bounds", bounds)
        object.__setattr__(self, "rigids", MappingProxyType(dict(self.rigids)))
        object.__setattr__(self, "humans", MappingProxyType(dict(self.humans)))
        object.__setattr__(self, "metadata", MappingProxyType(dict(self.metadata)))
        valid = np.zeros(sky.shape[:-1], dtype=bool) if self.sky_valid is None else self.sky_valid
        if np.shape(valid) != sky.shape[:-1]:
            raise ValueError("天空有效域形状不符")
        object.__setattr__(self, "sky_valid", readonly(valid, bool))
