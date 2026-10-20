"""列向量、米、右手系。T_a_b 把 b 系坐标变到 a 系。"""
from __future__ import annotations

import numpy as np


def check_se3(transform: np.ndarray) -> None:
    t = np.asarray(transform)
    if t.shape[-2:] != (4, 4) or not np.isfinite(t).all():
        raise ValueError("位姿必须是有限的 [...,4,4] 数组")
    if not np.allclose(t[..., 3, :], [0, 0, 0, 1], atol=1e-5):
        raise ValueError("位姿末行必须为 [0,0,0,1]")
    r = t[..., :3, :3]
    if not np.allclose(np.swapaxes(r, -1, -2) @ r, np.eye(3), atol=1e-4):
        raise ValueError("旋转必须正交")
    if not np.allclose(np.linalg.det(r), 1, atol=1e-4):
        raise ValueError("旋转行列式必须为 +1")


def inverse_se3(transform: np.ndarray) -> np.ndarray:
    check_se3(transform)
    out = np.zeros_like(transform)
    rt = np.swapaxes(transform[..., :3, :3], -1, -2)
    out[..., :3, :3] = rt
    out[..., :3, 3] = -(rt @ transform[..., :3, 3, None])[..., 0]
    out[..., 3, 3] = 1
    return out


def transform_points(points: np.ndarray, transform: np.ndarray) -> np.ndarray:
    """单个变换作用于 N 点，或 N 个变换分别作用于 N 点。"""
    return np.einsum("...ij,...j->...i", transform[..., :3, :3], points) + transform[..., :3, 3]


def project_pinhole(points_world: np.ndarray, world_from_camera: np.ndarray,
                    intrinsics: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    camera_points = transform_points(points_world, inverse_se3(world_from_camera))
    z = camera_points[:, 2]
    pixels = camera_points @ intrinsics.T
    uv = pixels[:, :2] / np.where(z > 1e-8, z, 1.0)[:, None]
    return uv, z


def lift_depth(depth: np.ndarray, intrinsics: np.ndarray,
               image_size: tuple[int, int]) -> np.ndarray:
    """输入是特征网格上的光轴深度；内参仍对应原始图像。"""
    h, w = depth.shape
    image_h, image_w = image_size
    u = (np.arange(w) + 0.5) * image_w / w - 0.5
    v = (np.arange(h) + 0.5) * image_h / h - 0.5
    uu, vv = np.meshgrid(u, v)
    rays = np.stack([uu, vv, np.ones_like(uu)], -1) @ np.linalg.inv(intrinsics).T
    return rays * depth[..., None]


def joint_globals(local_transforms: np.ndarray, parents: tuple[int, ...]) -> np.ndarray:
    if local_transforms.shape != (len(parents), 4, 4):
        raise ValueError("关节变换数量与骨架不符")
    check_se3(local_transforms)
    out = np.empty_like(local_transforms)
    for j, parent in enumerate(parents):
        if parent < -1 or parent >= j:
            raise ValueError("骨架须按父节点在前排序")
        out[j] = local_transforms[j] if parent == -1 else out[parent] @ local_transforms[j]
    return out


def skin_transforms(weights: np.ndarray, rest_global: np.ndarray,
                    posed_global: np.ndarray) -> np.ndarray:
    """规范坐标到人体根坐标的逐点仿射；包含 bind pose 的逆。"""
    if weights.shape[1] != len(rest_global) or rest_global.shape != posed_global.shape:
        raise ValueError("绑定维度不一致")
    if np.any(weights < 0) or not np.allclose(weights.sum(-1), 1, atol=1e-5):
        raise ValueError("蒙皮权重必须非负且逐点和为 1")
    transforms = posed_global @ inverse_se3(rest_global)
    return np.einsum("nj,jab->nab", weights, transforms)


def normalize(vectors: np.ndarray) -> np.ndarray:
    return vectors / np.maximum(np.linalg.norm(vectors, axis=-1, keepdims=True), 1e-8)


def cube_directions(resolution: int) -> np.ndarray:
    """面顺序 +X,-X,+Y,-Y,+Z,-Z；行列方向由下面的显式映射定义。"""
    a = 2 * (np.arange(resolution) + 0.5) / resolution - 1
    u, v = np.meshgrid(a, a)
    one = np.ones_like(u)
    faces = [(one, -v, -u), (-one, -v, u), (u, one, v),
             (u, -one, -v), (u, -v, one), (-u, -v, -one)]
    return normalize(np.stack([np.stack(f, -1) for f in faces]))
