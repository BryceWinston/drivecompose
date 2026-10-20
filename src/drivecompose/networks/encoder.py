"""Driving Log Encoder：共享图像干，视图上下文、实例槽与每帧状态分开读取。"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
import torch
from torch import nn
from torch.nn import functional as F

from ..contracts import DrivingLog, TokenKind
from ..decomposition import ActorTrack, SceneEvidence
from ..geometry import joint_globals
from .common import axis_angle_matrix, mlp, pose_matrix


@dataclass
class HumanTemplate:
    parents: tuple[int, ...]
    rest_local: np.ndarray               # [J,4,4], identity-specific skeleton
    support: np.ndarray                  # [Q,3], canonical clothed-surface support
    weights: np.ndarray                  # [Q,J]


class HumanTemplateProvider(Protocol):
    def make(self, shape_code: np.ndarray) -> HumanTemplate:
        """根据固定体型码提供同拓扑的规范人体模板。"""
        ...


class DrivingLogEncoder(nn.Module):
    def __init__(self, width=128, patch_size=16, actor_slots=24, joints=17, heads=4):
        super().__init__()
        self.width, self.patch_size, self.joints = width, patch_size, joints
        self.patch = nn.Conv2d(3, width, patch_size, stride=patch_size)
        self.calibration = mlp(21, width)  # rig_from_camera 16 + normalized K 4 + seconds 1
        self.pixel_position = mlp(2, width)
        self.image_block = nn.TransformerEncoderLayer(width, heads, width * 4, dropout=0, batch_first=True)
        self.view_blocks = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(width, heads, width * 4, dropout=0, batch_first=True), 2)
        self.actor_queries = nn.Parameter(torch.randn(actor_slots, width) * 0.02)
        self.actor_attention = nn.MultiheadAttention(width, heads, dropout=0, batch_first=True)
        self.state_attention = nn.MultiheadAttention(width, heads, dropout=0, batch_first=True)
        self.geometry = nn.Linear(width, 11)  # depth1, normal3, confidence1, semantic6
        self.rig_pose = mlp(width, 6)
        self.actor_kind = mlp(width, 3)       # inactive, vehicle, human
        self.actor_dimensions = mlp(width, 3)
        self.actor_shape = mlp(width, 10)
        self.actor_pose = mlp(width, 6)
        self.actor_joints = mlp(width, joints * 3)
        self.background_key = nn.Parameter(torch.randn(1, width) * 0.02)

    def forward(self, images, timestamps, intrinsics, rig_from_camera, world_from_rig=None):
        # 输入为单条多相机日志。
        t, v, _, image_h, image_w = images.shape
        if image_h % self.patch_size or image_w % self.patch_size:
            raise ValueError("输入尺寸须整除 patch_size，预处理时同步更新内参")
        maps = self.patch(images.reshape(t * v, 3, image_h, image_w))
        _, d, h, w = maps.shape
        tokens = maps.flatten(2).transpose(1, 2)
        yy, xx = torch.meshgrid(torch.linspace(-1, 1, h, device=images.device),
                                torch.linspace(-1, 1, w, device=images.device), indexing="ij")
        tokens = tokens + self.pixel_position(torch.stack([xx, yy], -1).reshape(1, -1, 2))
        k = torch.stack([intrinsics[:, 0, 0] / image_w, intrinsics[:, 1, 1] / image_h,
                         intrinsics[:, 0, 2] / image_w, intrinsics[:, 1, 2] / image_h], -1)
        calibration = torch.cat([rig_from_camera.reshape(v, 16), k], -1)
        calibration = calibration.unsqueeze(0).expand(t, v, 20)
        seconds = (timestamps - timestamps[0])[:, None, None].expand(t, v, 1)
        tokens = tokens + self.calibration(torch.cat([calibration, seconds], -1)).reshape(t*v, 1, d)
        tokens = self.image_block(tokens)
        summary = self.view_blocks(tokens.mean(1).reshape(1, t*v, d)).reshape(t*v, d)
        tokens = tokens + summary[:, None]
        feature = tokens.reshape(t, v, h, w, d)
        geometry = self.geometry(feature)
        predicted_rig = pose_matrix(self.rig_pose(summary.reshape(t, v, d).mean(1)))
        if world_from_rig is None:
            world_from_rig = torch.linalg.inv(predicted_rig[0]) @ predicted_rig
        # 每条轨迹一个身份槽；逐帧状态由同一身份槽读取。
        actors, _ = self.actor_attention(self.actor_queries[None], tokens.reshape(1, -1, d),
                                         tokens.reshape(1, -1, d), need_weights=False)
        states, _ = self.state_attention(actors.expand(t, -1, -1), feature.reshape(t, -1, d),
                                         feature.reshape(t, -1, d), need_weights=False)
        keys = torch.cat([self.background_key[None], actors], 1)[0]
        instance_logits = torch.einsum("tvhwd,ad->tvhwa", F.normalize(feature, dim=-1),
                                       F.normalize(keys, dim=-1)) * (d ** 0.5)
        return {
            "features": feature, "depth": F.softplus(geometry[..., 0]) + 0.1,
            "normals_camera": F.normalize(geometry[..., 1:4], dim=-1),
            "confidence": geometry[..., 4].sigmoid(), "semantic_logits": geometry[..., 5:11],
            "world_from_rig": world_from_rig,
            "instance_logits": instance_logits, "actor_kind_logits": self.actor_kind(actors[0]),
            "actor_dimensions": F.softplus(self.actor_dimensions(actors[0])) + 0.2,
            "actor_shape": self.actor_shape(actors[0]), "actor_identity": actors[0],
            "actor_poses": world_from_rig[:, None] @ pose_matrix(self.actor_pose(states)),
            "joint_rotations": axis_angle_matrix(self.actor_joints(states).reshape(t, -1, self.joints, 3)),
        }

    @torch.no_grad()
    def encode(self, log: DrivingLog, templates: HumanTemplateProvider | None = None,
               actor_threshold=0.6) -> SceneEvidence:
        """构建时的 numpy 导出边界；训练直接使用 forward 保留梯度。"""
        log.validate()
        self.eval()
        device = next(self.parameters()).device
        tensor = lambda x: torch.as_tensor(np.array(x), device=device, dtype=torch.float32)
        out = self.forward(tensor(log.images), tensor(log.timestamps), tensor(log.intrinsics),
                           tensor(log.rig_from_camera), None if log.world_from_rig is None else tensor(log.world_from_rig))
        raw = {k: v.detach().cpu().numpy() for k, v in out.items()}
        probabilities = out["actor_kind_logits"].softmax(-1).cpu().numpy()
        labels = raw["instance_logits"].argmax(-1)
        tracks = []
        for slot, scores in enumerate(probabilities):
            kind = int(scores.argmax())
            if kind == 0 or scores[kind] < actor_threshold:
                labels[labels == slot + 1] = 0
                continue
            if kind == 1:
                track = ActorTrack(f"vehicle_{slot:03d}", TokenKind.VEHICLE, slot+1,
                                   raw["actor_poses"][:, slot], raw["actor_dimensions"][slot])
            else:
                if templates is None:
                    raise ValueError("检测到人体：须提供与关节头匹配的规范模板后端")
                template = templates.make(raw["actor_shape"][slot])
                if len(template.parents) != self.joints:
                    raise ValueError("人体模板与关节头拓扑不匹配")
                roots = [j for j, p in enumerate(template.parents) if p == -1]
                if len(roots) != 1:
                    raise ValueError("人体模板必须只有一个根节点")
                rest = joint_globals(template.rest_local, template.parents)
                posed = []
                for rotation in raw["joint_rotations"][:, slot]:
                    local = template.rest_local.copy()
                    local[:, :3, :3] = template.rest_local[:, :3, :3] @ rotation
                    local[roots[0]] = template.rest_local[roots[0]]
                    posed.append(joint_globals(local, template.parents))
                track = ActorTrack(f"human_{slot:03d}", TokenKind.HUMAN, slot+1,
                                   raw["actor_poses"][:, slot], raw["actor_dimensions"][slot],
                                   template.support, template.weights, rest, np.stack(posed), template.parents)
            tracks.append(track)
        cameras = raw["world_from_rig"][:, None] @ log.rig_from_camera[None]
        return SceneEvidence(raw["features"], raw["depth"], raw["confidence"], labels,
                             raw["semantic_logits"].argmax(-1), log.intrinsics, cameras,
                             log.images.shape[-2:], tuple(tracks))
