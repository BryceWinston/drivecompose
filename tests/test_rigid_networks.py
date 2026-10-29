"""新刚体接口、权重格式以及恢复—聚合—解码—装配链路的回归检查。"""
import io
import unittest
from dataclasses import replace

import numpy as np

try:
    import torch
except ModuleNotFoundError:
    torch = None

from drivecompose.contracts import QUERY_SCHEMA, DrivingLog, SimulationState, TokenKind
from drivecompose.decomposition import SceneAssetDecomposer, make_blocks
from drivecompose.rendering import StateComposer

if torch is not None:
    from drivecompose.networks.decoders import RigidGaussianDecoder, TypedLatentCodec
    from drivecompose.networks.encoder import DrivingLogEncoder
    from drivecompose.pipeline import CheckpointRecord


@unittest.skipIf(torch is None, "需要 networks 可选依赖 PyTorch")
class RigidNetworkTests(unittest.TestCase):
    def test_new_checkpoint_roundtrip_and_old_keys_rejected(self):
        codec = TypedLatentCodec(feature_dim=5, latent_dim=8, children=2)
        self.assertIsInstance(codec.rigid, RigidGaussianDecoder)
        weights = codec.state_dict()
        self.assertTrue(any(key.startswith("rigid.") for key in weights))
        self.assertFalse(any("vehicle" in key for key in weights))
        stream = io.BytesIO()
        torch.save(weights, stream)
        stream.seek(0)
        restored = TypedLatentCodec(feature_dim=5, latent_dim=8, children=2)
        restored.load_state_dict(torch.load(stream, weights_only=True), strict=True)
        code = torch.randn(2, 8)
        positions, scales, free = torch.zeros(2, 3), torch.ones(2, 3), torch.zeros(2, dtype=torch.bool)
        expected = codec.rigid(code, positions, scales, free)
        actual = restored.rigid(code, positions, scales, free)
        for field in expected:
            torch.testing.assert_close(actual[field], expected[field])
        old_weights = {key.replace("rigid.", "vehicle.", 1): value for key, value in weights.items()}
        with self.assertRaises(RuntimeError):
            restored.load_state_dict(old_weights, strict=True)

    def test_checkpoint_record_requires_current_query_schema(self):
        record = CheckpointRecord("encoder-r2", "codec-r2", "encoder-r2", QUERY_SCHEMA,
                                  "encoder-r2", "codec-r2", QUERY_SCHEMA)
        record.validate()
        for old in (replace(record, query_schema="v1", completion_query_schema="v1"),
                    replace(record, completion_query_schema="v1")):
            with self.subTest(record=old), self.assertRaises(ValueError):
                old.validate()

    def test_rigid_recovery_aggregation_decoding_and_composition(self):
        torch.manual_seed(7)
        encoder = DrivingLogEncoder(width=16, patch_size=8, actor_slots=1, joints=2, heads=4)
        # Force the one identity slot to the rigid category; geometry remains a real forward pass.
        with torch.no_grad():
            for parameter in encoder.actor_kind.parameters():
                parameter.zero_()
            encoder.actor_kind[-1].bias.copy_(torch.tensor([-10., 10., -10.]))
        log = DrivingLog(np.zeros((2, 1, 3, 16, 16), dtype=np.float32), np.array([0., 1.]),
                         np.array([[[10., 0., 7.5], [0., 10., 7.5], [0., 0., 1.]]]),
                         np.eye(4)[None], np.broadcast_to(np.eye(4), (2, 4, 4)).copy())
        evidence = encoder.encode(log)
        self.assertEqual(len(evidence.tracks), 1)
        self.assertEqual(evidence.tracks[0].actor_id, "rigid_000")
        self.assertEqual(evidence.tracks[0].kind, TokenKind.RIGID)
        bounds = np.array([[-3., -3., -3.], [3., 3., 8.]])
        blocks = make_blocks(evidence, bounds, background_shape=(2, 2, 2), rigid_shape=(2, 2, 2), sky_resolution=1)
        bundle = SceneAssetDecomposer().decompose(evidence, blocks)
        layout = {key: torch.tensor(value, dtype=torch.long if key in ("kind", "groups") else torch.float32)
                  for key, value in bundle.layout().items()}
        codec = TypedLatentCodec(feature_dim=17, latent_dim=8, children=2)
        latent = codec.encode(torch.tensor(bundle.features), layout)
        decoded = codec.decode(latent, bundle, layout, torch.tensor(bundle.free))
        world = codec.export_world(decoded, bundle, bounds, seed=7)
        self.assertEqual(set(world.rigids), {"rigid_000"})
        self.assertEqual(world.metadata["rigid_motion"], "rigid")
        loss = sum(value["means"].square().sum() for value in decoded if "means" in value)
        loss.backward()
        self.assertTrue(any(p.grad is not None and torch.isfinite(p.grad).all() for p in codec.rigid.parameters()))
        pose = np.eye(4)
        pose[:3, :3] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        pose[:3, 3] = [1, 2, 0]
        scene = StateComposer().assemble(world, SimulationState(world_from_ego=np.eye(4), rigid_poses={"rigid_000": pose}, human_poses={}))
        start, end = scene.actor_ranges["rigid_000"]
        canonical = world.rigids["rigid_000"].gaussians
        np.testing.assert_allclose(scene.gaussians.means[start:end], canonical.means @ pose[:3, :3].T + pose[:3, 3], atol=1e-6)
        np.testing.assert_allclose(np.linalg.eigvalsh(scene.gaussians.covariance[start:end]), np.linalg.eigvalsh(canonical.covariance), atol=1e-6)


if __name__ == "__main__":
    unittest.main()
