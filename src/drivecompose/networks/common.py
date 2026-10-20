import torch
from torch import nn


def mlp(in_dim, out_dim, hidden=None):
    hidden = hidden or out_dim
    return nn.Sequential(nn.Linear(in_dim, hidden), nn.GELU(), nn.Linear(hidden, out_dim))


def axis_angle_matrix(vector):
    """Rodrigues，零角度使用 sinc 的连续极限。"""
    x, y, z = vector.unbind(-1)
    zeros = torch.zeros_like(x)
    skew = torch.stack([zeros, -z, y, z, zeros, -x, -y, x, zeros], -1).reshape(*vector.shape[:-1], 3, 3)
    theta = torch.linalg.vector_norm(vector, dim=-1)
    a = torch.sinc(theta / torch.pi)[..., None, None]
    b = (0.5 * torch.sinc(theta / (2 * torch.pi)).square())[..., None, None]
    return torch.eye(3, device=vector.device, dtype=vector.dtype) + a * skew + b * (skew @ skew)


def pose_matrix(raw):
    result = torch.eye(4, device=raw.device, dtype=raw.dtype).expand(*raw.shape[:-1], 4, 4).clone()
    result[..., :3, :3] = axis_angle_matrix(raw[..., :3])
    result[..., :3, 3] = raw[..., 3:6]
    return result


def quaternion_matrix(raw):
    # 保留非零实部以规避原点；归一化后构造正交旋转。
    identity = torch.zeros_like(raw)
    identity[..., 0] = 1
    shifted = raw + identity
    norm = torch.linalg.vector_norm(shifted, dim=-1, keepdim=True)
    q = torch.where(norm < 1e-6, identity, shifted / norm.clamp_min(1e-6))
    w, x, y, z = q.unbind(-1)
    return torch.stack([
        1 - 2 * (y*y + z*z), 2 * (x*y - z*w), 2 * (x*z + y*w),
        2 * (x*y + z*w), 1 - 2 * (x*x + z*z), 2 * (y*z - x*w),
        2 * (x*z - y*w), 2 * (y*z + x*w), 1 - 2 * (x*x + y*y),
    ], -1).reshape(*raw.shape[:-1], 3, 3)
