import tempfile
import unittest
from pathlib import Path

import numpy as np

from drivecompose.contracts import GaussianSet, HumanAvatarAsset, HumanState, RigidVehicleAsset, SimulationState, WorldVault
from drivecompose.geometry import inverse_se3, joint_globals, project_pinhole, skin_transforms, transform_points
from drivecompose.rendering import StateComposer, evaluate_appearance, transform_gaussians
from drivecompose.world import load_world, save_world


def gaussians(points):
    n = len(points)
    appearance = np.zeros((n, 3, 4))
    appearance[..., 0] = 0.5
    appearance[:, 0, 1] = 0.2
    return GaussianSet(np.array(points), np.broadcast_to(np.diag([0.09, 0.04, 0.01]), (n, 3, 3)),
                       np.ones(n), appearance)


def world_fixture():
    rest = np.broadcast_to(np.eye(4), (2, 4, 4)).copy()
    rest[1, :3, 3] = [1, 0, 0]
    body = gaussians([[1, 1, 0]])
    human = HumanAvatarAsset("human_0", body, np.array([[0, 1]]), rest, (-1, 0))
    vehicle = RigidVehicleAsset("vehicle_0", gaussians([[-1, 0, 0], [1, 0, 0]]), np.array([4, 2, 1.5]))
    return WorldVault(gaussians([[0, 0, -1]]), np.ones((6, 2, 2, 3))*0.5,
                      {"vehicle_0": vehicle}, {"human_0": human}, np.array([[-20,-20,-3],[20,20,10]]), 7,
                      sky_valid=np.ones((6,2,2), bool))


class GeometryAndWorldTests(unittest.TestCase):
    def test_camera_roundtrip_and_projection(self):
        pose = np.eye(4)
        pose[:3, :3] = [[0,-1,0],[1,0,0],[0,0,1]]
        pose[:3, 3] = [3,4,1]
        camera_points = np.array([[0,0,5],[1,2,10]], dtype=float)
        world_points = transform_points(camera_points, pose)
        np.testing.assert_allclose(transform_points(world_points, inverse_se3(pose)), camera_points)
        pixels, depth = project_pinhole(world_points, pose, np.array([[100,0,20],[0,100,30],[0,0,1]]))
        np.testing.assert_allclose(pixels, [[20,30],[30,50]])
        np.testing.assert_allclose(depth, [5,10])

    def test_rigid_transform_preserves_shape_and_local_appearance(self):
        source = gaussians([[-1,0,0],[1,0,0]])
        pose = np.eye(4)
        pose[:3, :3] = [[0,-1,0],[1,0,0],[0,0,1]]
        pose[:3, 3] = [5,2,0]
        moved = transform_gaussians(source, pose)
        self.assertAlmostEqual(np.linalg.norm(moved.means[1]-moved.means[0]), 2)
        np.testing.assert_allclose(np.linalg.eigvalsh(moved.covariance), np.linalg.eigvalsh(source.covariance))
        camera = np.array([3,1,4])
        np.testing.assert_allclose(evaluate_appearance(source, camera),
                                   evaluate_appearance(moved, transform_points(camera, pose)), atol=1e-6)

    def test_bind_pose_and_articulation_use_same_covariance_transform(self):
        world = world_fixture()
        asset = world.humans["human_0"]
        identity = skin_transforms(asset.weights, asset.rest_global, asset.rest_global)
        np.testing.assert_allclose(identity, np.eye(4)[None])
        posed = asset.rest_global.copy()
        posed[1, :3, :3] = [[0,-1,0],[1,0,0],[0,0,1]]
        scene = StateComposer().assemble(world, SimulationState(np.eye(4), {}, {"human_0": HumanState(np.eye(4), posed)}))
        np.testing.assert_allclose(scene.gaussians.means[-1], [0,0,0], atol=1e-6)
        np.testing.assert_allclose(scene.gaussians.covariance[-1], np.diag([0.04,0.09,0.01]), atol=1e-6)

    def test_joint_tree_and_singular_pose_rejection(self):
        local = np.broadcast_to(np.eye(4), (2,4,4)).copy()
        local[1, :3, 3] = [1,0,0]
        np.testing.assert_allclose(joint_globals(local, (-1,0))[1,:3,3], [1,0,0])
        transforms = np.broadcast_to(np.eye(4), (2,4,4)).copy()
        transforms[1,:3,:3] = np.diag([-1,-1,1])
        blended = skin_transforms(np.array([[0.5,0.5]]), np.broadcast_to(np.eye(4), (2,4,4)), transforms)
        with self.assertRaises(ValueError):
            transform_gaussians(gaussians([[0,0,0]]), blended)

    def test_world_is_reused_without_log_time_lifetime(self):
        world = world_fixture()
        original = world.vehicles["vehicle_0"].gaussians.means.copy()
        composer = StateComposer()
        state_a = SimulationState(np.eye(4), {"vehicle_0": np.eye(4)}, {}, 0)
        state_b = SimulationState(np.eye(4), {"vehicle_0": np.eye(4)}, {}, 10000)
        np.testing.assert_array_equal(composer.assemble(world,state_a).gaussians.means,
                                      composer.assemble(world,state_b).gaussians.means)
        np.testing.assert_array_equal(world.vehicles["vehicle_0"].gaussians.means, original)
        with self.assertRaises(ValueError):
            world.vehicles["vehicle_0"].gaussians.means[0,0] = 99
        with self.assertRaises(TypeError):
            world.vehicles["other"] = world.vehicles["vehicle_0"]

    def test_archive_roundtrip_keeps_asset_binding_and_coverage(self):
        source = world_fixture()
        with tempfile.TemporaryDirectory(prefix="drivecompose_test_") as directory:
            path = Path(directory)/"world.npz"
            save_world(source, path)
            loaded = load_world(path)
            np.testing.assert_array_equal(loaded.humans["human_0"].weights, source.humans["human_0"].weights)
            np.testing.assert_array_equal(loaded.sky_valid, source.sky_valid)
            self.assertEqual(loaded.build_seed, 7)
            self.assertFalse(loaded.background.means.flags.writeable)
            with self.assertRaises(FileExistsError):
                save_world(source, path)


if __name__ == "__main__":
    unittest.main()
