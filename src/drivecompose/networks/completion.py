"""Joint Completion DiT：只在未知查询上积分，已观测码与自由空间在每步重置。"""
from __future__ import annotations

import torch
from torch import nn

from .common import mlp


class CompletionBlock(nn.Module):
    def __init__(self, width, heads):
        super().__init__()
        self.local = nn.MultiheadAttention(width, heads, dropout=0, batch_first=True)
        self.read = nn.MultiheadAttention(width, heads, dropout=0, batch_first=True)
        self.write = nn.MultiheadAttention(width, heads, dropout=0, batch_first=True)
        self.norm = nn.LayerNorm(width)
        self.condition = mlp(width, width * 2)
        self.feedforward = mlp(width, width, width * 4)

    def forward(self, tokens, memory, time_embedding, groups):
        scale, shift = self.condition(time_embedding).chunk(2, -1)
        normalized = self.norm(tokens) * (1 + scale) + shift
        local = torch.zeros_like(tokens)
        for group in groups.unique():
            indices = (groups == group).nonzero(as_tuple=True)[0]
            q = normalized[indices][None]
            update, _ = self.local(q, q, q, need_weights=False)
            local = local.index_copy(0, indices, update[0])
        tokens = tokens + local
        summary, _ = self.read(memory[None], tokens[None], tokens[None], need_weights=False)
        memory = memory + summary[0]
        context, _ = self.write(self.norm(tokens)[None], memory[None], memory[None], need_weights=False)
        tokens = tokens + context[0]
        return tokens + self.feedforward(self.norm(tokens)), memory


class JointCompletionDiT(nn.Module):
    def __init__(self, latent_dim=128, context_dim=129, width=128, heads=4, layers=4, memory_tokens=16):
        super().__init__()
        self.input = nn.Linear(2 * latent_dim + 3, width)
        self.kind = nn.Embedding(4, width)
        self.geometry = mlp(9, width)  # canonical xyz + reference-world xyz + cell scale
        self.time = mlp(3, width)
        self.context = nn.Linear(context_dim, width)
        self.memory = nn.Parameter(torch.randn(memory_tokens, width) * 0.02)
        self.blocks = nn.ModuleList([CompletionBlock(width, heads) for _ in range(layers)])
        self.output = nn.Linear(width, latent_dim)

    def forward(self, noisy, time, observed, known, free, confidence, layout, context):
        if torch.any(known & free):
            raise ValueError("已观测表面与自由空间标签互斥")
        flags = torch.stack([known.to(noisy.dtype), free.to(noisy.dtype), confidence], -1)
        x = self.input(torch.cat([noisy, observed * known[:, None], flags], -1))
        geometry = torch.cat([layout["positions"], layout["world_reference"], layout["scales"]], -1)
        x = x + self.kind(layout["kind"]) + self.geometry(geometry)
        tau = torch.as_tensor(time, dtype=noisy.dtype, device=noisy.device).reshape(1)
        embedding = self.time(torch.cat([tau, (torch.pi*tau).sin(), (torch.pi*tau).cos()]))
        memory = torch.cat([self.memory, self.context(context)], 0)
        for block in self.blocks:
            x, memory = block(x, memory, embedding, layout["groups"])
        unknown = ~(known | free)
        return self.output(x) * unknown[:, None]

    def flow_loss(self, clean, observed, known, free, confidence, layout, context, target_valid, supervised=None):
        """所有待插值未知维度须有完整目标；supervised 仅表示额外的损失筛选。"""
        unknown = ~(known | free)
        if target_valid.shape != known.shape or not bool(target_valid[unknown].all()) or not bool(torch.isfinite(clean).all()):
            raise ValueError("Flow Matching 需要所有未知查询的有效完整目标；不完整真实日志应走观测约束训练")
        noise = torch.randn_like(clean)
        time = torch.rand((), device=clean.device)
        interpolated = (1-time) * noise + time * clean
        interpolated = torch.where(known[:, None], observed, interpolated)
        interpolated = torch.where(free[:, None], torch.zeros_like(interpolated), interpolated)
        prediction = self(interpolated, time, observed, known, free, confidence, layout, context)
        mask = unknown if supervised is None else unknown & supervised
        error = (prediction - (clean-noise)).square().mean(-1)
        return (error * mask).sum() / mask.sum().clamp_min(1)

    def integrate(self, observed, known, free, confidence, layout, context, steps=24, seed=0):
        """可微积分，供冻结 codec 后的渲染约束适配使用。"""
        if steps < 1:
            raise ValueError("采样步数须为正")
        generator = torch.Generator(device=observed.device).manual_seed(seed)
        x = torch.randn(observed.shape, generator=generator, device=observed.device, dtype=observed.dtype)
        x = torch.where(known[:, None], observed, x)
        x = torch.where(free[:, None], torch.zeros_like(x), x)
        for step in range(steps):
            time = step / steps  # t=0 noise -> t=1 data
            velocity = self(x, time, observed, known, free, confidence, layout, context)
            x = x + velocity / steps
            x = torch.where(known[:, None], observed, x)
            x = torch.where(free[:, None], torch.zeros_like(x), x)
        return x

    @torch.no_grad()
    def sample(self, observed, known, free, confidence, layout, context, steps=24, seed=0):
        self.eval()
        return self.integrate(observed, known, free, confidence, layout, context, steps, seed)
