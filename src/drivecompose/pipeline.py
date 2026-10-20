"""离线构建入口：场景恢复、联合补全、资产解码与观测验证。"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import torch

from .contracts import DrivingLog, WorldVault
from .decomposition import SceneAssetDecomposer, make_blocks
from .networks.completion import JointCompletionDiT
from .networks.decoders import TypedLatentCodec
from .networks.encoder import DrivingLogEncoder, HumanTemplateProvider
from .validation import ObservedViewValidator, ValidationReport


@dataclass(frozen=True)
class CheckpointRecord:
    encoder_revision: str
    codec_revision: str
    codec_encoder_revision: str
    query_schema: str
    completion_encoder_revision: str
    completion_codec_revision: str
    completion_query_schema: str

    def validate(self):
        if not all(vars(self).values()):
            raise ValueError("必须记录实际加载的整组表示版本")
        if self.encoder_revision != self.codec_encoder_revision or self.encoder_revision != self.completion_encoder_revision:
            raise ValueError("编码器特征基与 codec / 补全网络不匹配")
        if self.codec_revision != self.completion_codec_revision or self.query_schema != self.completion_query_schema:
            raise ValueError("潜码或查询布局版本不匹配，须重新编码目标并适配先验")


@dataclass(frozen=True)
class BuildResult:
    world: WorldVault
    validation: ValidationReport


class OfflineWorldBuilder:
    def __init__(self, encoder: DrivingLogEncoder, codec: TypedLatentCodec,
                 completion: JointCompletionDiT, checkpoints: CheckpointRecord,
                 validator: ObservedViewValidator, templates: HumanTemplateProvider | None = None):
        checkpoints.validate()
        self.encoder, self.codec, self.completion = encoder, codec, completion
        self.checkpoints, self.validator, self.templates = checkpoints, validator, templates
        self.decomposer = SceneAssetDecomposer()

    @torch.no_grad()
    def build(self, log: DrivingLog, bounds: np.ndarray, seed=0, steps=24,
              background_shape=(20, 12, 6), vehicle_shape=(8, 4, 4), sky_resolution=4) -> BuildResult:
        self.codec.eval(); self.completion.eval()
        if next(self.codec.parameters()).device != next(self.completion.parameters()).device:
            raise ValueError("codec 与补全网络须位于同一设备")
        evidence = self.encoder.encode(log, self.templates)
        blocks = make_blocks(evidence, bounds, background_shape, vehicle_shape, sky_resolution)
        bundle = self.decomposer.decompose(evidence, blocks)
        device = next(self.codec.parameters()).device
        tensor = lambda a, dtype=torch.float32: torch.as_tensor(np.array(a), dtype=dtype, device=device)
        layout = {k: tensor(v, torch.long if k in ("kind", "groups") else torch.float32)
                  for k, v in bundle.layout().items()}
        known, free = tensor(bundle.known, torch.bool), tensor(bundle.free, torch.bool)
        observed = self.codec.encode(tensor(bundle.features), layout)
        observed = torch.where(known[:, None], observed, torch.zeros_like(observed))
        completed = self.completion.sample(observed, known, free, tensor(bundle.confidence),
                                           layout, tensor(bundle.context), steps, seed)
        candidate = self.codec.export_world(self.codec.decode(completed, bundle, layout, free), bundle, bounds, seed)
        baseline = self.codec.export_world(self.codec.decode(observed, bundle, layout, ~known), bundle, bounds, seed)
        report = self.validator.validate(candidate, baseline, log, evidence)
        if not report.accepted:
            raise ValueError(f"构建结果未通过观测约束：{report}")
        metadata = dict(candidate.metadata)
        metadata.update({"status": "observation_checked_candidate",
                         "encoder_revision": self.checkpoints.encoder_revision,
                         "codec_revision": self.checkpoints.codec_revision,
                         "query_schema": self.checkpoints.query_schema})
        checked = WorldVault(candidate.background, candidate.sky, candidate.vehicles, candidate.humans,
                             candidate.bounds, seed, metadata, candidate.sky_valid)
        return BuildResult(checked, report)
