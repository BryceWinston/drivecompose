"""分类型潜码编码与背景、刚体、人体三路解码。"""
from __future__ import annotations

import numpy as np
import torch
from torch import nn

from ..contracts import GaussianSet, HumanAvatarAsset, RigidAsset, TokenKind, WorldVault
from .common import mlp, quaternion_matrix


class GaussianDecoder(nn.Module):
    def __init__(self, latent_dim, children=4):
        super().__init__()
        self.children = children
        self.parameters_head = mlp(latent_dim, children * 23)

    def forward(self, code, positions, scales, free):
        n = len(code)
        p = self.parameters_head(code).reshape(n, self.children, 23)
        means = positions[:, None] + 0.5 * scales[:, None] * p[..., :3].tanh()
        rotation = quaternion_matrix(p[..., 3:7])
        std = (scales[:, None] * p[..., 7:10].sigmoid() * 0.35).clamp_min(1e-3)
        covariance = rotation @ torch.diag_embed(std.square()) @ rotation.transpose(-1, -2)
        opacity = p[..., 10].sigmoid() * (~free)[:, None]
        appearance = torch.cat([p[..., 11:14].sigmoid()[..., None],
                                0.25*p[..., 14:23].tanh().reshape(n, self.children, 3, 3)], -1)
        return {"means": means.reshape(-1, 3), "covariance": covariance.reshape(-1, 3, 3),
                "opacity": opacity.reshape(-1), "appearance": appearance.reshape(-1, 3, 4)}


class BackgroundDecoder(nn.Module):
    def __init__(self, latent_dim, children=4):
        super().__init__()
        self.gaussians = GaussianDecoder(latent_dim, children)
        self.sky = mlp(latent_dim, 3)


class RigidGaussianDecoder(GaussianDecoder):
    """刚体高斯解码器：输出固定规范资产；整体 SE(3) 位姿由场景状态提供。"""


class HumanAvatarDecoder(GaussianDecoder):
    """输出规范高斯，沿用同一身份模板上的邻接骨架权重。"""


class TypedLatentCodec(nn.Module):
    def __init__(self, feature_dim=129, latent_dim=128, children=4):
        super().__init__()
        self.latent_dim = latent_dim
        self.encoders = nn.ModuleList([nn.Sequential(mlp(feature_dim+6, latent_dim),
                                                     nn.LayerNorm(latent_dim)) for _ in range(4)])
        self.background = BackgroundDecoder(latent_dim, children)
        self.rigid = RigidGaussianDecoder(latent_dim, children)
        self.human = HumanAvatarDecoder(latent_dim, children)

    def encode(self, features, layout):
        raw = torch.cat([features, layout["positions"], layout["scales"]], -1)
        # 可见性标记属于条件，不进入本征目标编码，避免完整/部分目标定义漂移。
        out = features.new_zeros(len(features), self.latent_dim)
        for kind, encoder in enumerate(self.encoders):
            ids = (layout["kind"] == kind).nonzero(as_tuple=True)[0]
            out = out.index_copy(0, ids, encoder(raw[ids]))
        return out

    def decode(self, code, bundle, layout, free):
        """可微输出；训练器把这些张量交给可微渲染后端，不能先导出 numpy。"""
        decoded, cursor = [], 0
        for block in bundle.blocks:
            count = len(block.positions)
            section = slice(cursor, cursor+count)
            if block.kind == TokenKind.SKY:
                value = {"sky": self.background.sky(code[section]).sigmoid()}
            else:
                decoder = {TokenKind.BACKGROUND: self.background.gaussians,
                           TokenKind.RIGID: self.rigid, TokenKind.HUMAN: self.human}[block.kind]
                value = decoder(code[section], layout["positions"][section], layout["scales"][section], free[section])
            decoded.append(value)
            cursor += count
        return decoded

    @torch.no_grad()
    def export_world(self, decoded, bundle, bounds, seed):
        background, sky, sky_valid, rigids, humans = None, None, None, {}, {}
        cursor = 0
        for block, tensors in zip(bundle.blocks, decoded):
            section = slice(cursor, cursor+len(block.positions))
            cursor += len(block.positions)
            arrays = {k: v.detach().cpu().numpy() for k, v in tensors.items()}
            if block.kind == TokenKind.SKY:
                size = int(round((len(block.positions)/6) ** 0.5))
                sky = arrays["sky"].reshape(6, size, size, 3)
                sky_valid = bundle.known[section].reshape(6, size, size)
                continue
            gaussians = GaussianSet(**arrays)
            if block.kind == TokenKind.BACKGROUND:
                background = gaussians
            elif block.kind == TokenKind.RIGID:
                rigids[block.actor_id] = RigidAsset(block.actor_id, gaussians, block.track.dimensions)
            else:
                weights = np.repeat(block.track.skin_weights, self.human.children, axis=0)
                humans[block.actor_id] = HumanAvatarAsset(block.actor_id, gaussians, weights,
                                                         block.track.rest_global, block.track.parents)
        if background is None or sky is None:
            raise ValueError("缺少背景或天空查询")
        return WorldVault(background, sky, rigids, humans, bounds, seed,
                          {"status": "candidate", "lighting": "fixed", "rigid_motion": "rigid"}, sky_valid)
