"""可微训练目标片段。渲染图像、自由空间射线量和接触量由相应后端提供。"""
import torch
from torch.nn import functional as F


def masked_mean(values, mask):
    mask = mask.to(values.dtype)
    return (values * mask).sum() / mask.sum().clamp_min(1)


def reconstruction_losses(rendered_rgb, target_rgb, rendered_depth, target_depth,
                          observed_mask, depth_mask):
    return {
        "rgb_l1": masked_mean((rendered_rgb-target_rgb).abs().mean(-1), observed_mask),
        "depth_l1": masked_mean((rendered_depth-target_depth).abs(), depth_mask),
    }


def representation_losses(decoded, target, surface_mask, empty_mask):
    """同一支撑单元与固定 child 对应关系；无对应数据时改用渲染/集合匹配监督。"""
    return {
        "position": masked_mean((decoded["means"]-target["means"]).abs().mean(-1), surface_mask),
        "empty_opacity": masked_mean(decoded["opacity"].square(), empty_mask),
    }


def observed_anchor_loss(candidate, observed_only, protected):
    return {
        "protected_geometry": masked_mean((candidate["means"]-observed_only["means"]).square().sum(-1), protected),
        "protected_opacity": masked_mean((candidate["opacity"]-observed_only["opacity"]).square(), protected),
    }


def scene_constraint_losses(free_ray_opacity, foot_signed_distance, foot_contact,
                            penetration_depth):
    """SDF 正值在地面上方；contact 只标记当前确实接地的脚点。"""
    zero = foot_signed_distance.sum() * 0
    return {
        "free_space": free_ray_opacity.square().mean() if free_ray_opacity.numel() else zero,
        "ground_penetration": F.relu(-foot_signed_distance).square().mean() if foot_signed_distance.numel() else zero,
        "foot_contact": masked_mean(foot_signed_distance.abs(), foot_contact),
        "actor_penetration": F.relu(penetration_depth).square().mean() if penetration_depth.numel() else zero,
    }


def matched_track_losses(predicted_pose, target_pose, predicted_dimensions, target_dimensions):
    """调用前须在整条轨迹上完成一次集合匹配，不能逐帧重新分配身份。"""
    return {
        "root_translation": (predicted_pose[..., :3, 3]-target_pose[..., :3, 3]).abs().mean(),
        "root_rotation": (predicted_pose[..., :3, :3]-target_pose[..., :3, :3]).square().mean(),
        "dimensions": (predicted_dimensions-target_dimensions).abs().mean(),
    }
