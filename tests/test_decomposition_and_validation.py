import unittest
import numpy as np

from drivecompose.contracts import DrivingLog, SimulationState, TokenKind
from drivecompose.decomposition import SceneAssetDecomposer, SceneEvidence, make_blocks
from drivecompose.rendering import CameraObservation, RenderCamera, StateDrivenRenderer
from drivecompose.simulation import DrivingAction, PhysicsDescription, SimulationBridge
from drivecompose.validation import ObservedViewValidator
from test_geometry_and_world import world_fixture


def evidence_fixture(semantics=None):
    semantic = np.zeros((1,1,2,2),dtype=int) if semantics is None else semantics
    return SceneEvidence(np.ones((1,1,2,2,4)), np.full((1,1,2,2),5.0), np.ones((1,1,2,2)),
                         np.zeros((1,1,2,2),int), semantic,
                         np.array([[[4,0,1.5],[0,4,1.5],[0,0,1]]]), np.eye(4)[None,None], (4,4), ())


class DecompositionTests(unittest.TestCase):
    def test_observed_surface_anchors_survive_coarse_completion_grid(self):
        evidence = evidence_fixture()
        blocks = make_blocks(evidence, np.array([[-3,-3,0],[3,3,10]]), (2,2,2), sky_resolution=2)
        bg = blocks[0]
        self.assertTrue(np.any(np.isclose(bg.positions[:,2],5)))
        bundle = SceneAssetDecomposer().decompose(evidence,blocks)
        observed_centers = bg.positions[bundle.known[:len(bg.positions)]]
        self.assertGreater(len(observed_centers),0)
        self.assertTrue(np.allclose(observed_centers[:,2],5))
        self.assertFalse(np.any(bundle.known & bundle.free))

    def test_dynamic_semantics_are_not_silently_added_to_background(self):
        evidence = evidence_fixture(np.full((1,1,2,2),2))
        blocks = make_blocks(evidence,np.array([[-3,-3,0],[3,3,10]]),(2,2,2),sky_resolution=2)
        bundle = SceneAssetDecomposer().decompose(evidence,blocks)
        self.assertFalse(bundle.known[:len(blocks[0].positions)].any())

    def test_sky_aggregation_is_translation_invariant(self):
        e = evidence_fixture(np.full((1,1,2,2),4))
        bounds = np.array([[-3,-3,0],[3,3,10]])
        blocks = make_blocks(e,bounds,(2,2,2),sky_resolution=2)
        first = SceneAssetDecomposer().decompose(e,blocks)
        e.world_from_camera = e.world_from_camera.copy()
        e.world_from_camera[0,0,:3,3] = [100,-20,8]
        second = SceneAssetDecomposer().decompose(e,blocks)
        sky = first.layout()["kind"] == int(TokenKind.SKY)
        np.testing.assert_array_equal(first.known[sky],second.known[sky])
        np.testing.assert_array_equal(first.features[sky],second.features[sky])


class ConstantRasterizer:
    def __init__(self,rgb=0.0): self.rgb = rgb
    def render(self,scene,pose,k,size):
        return CameraObservation(np.full((*size,3),self.rgb),np.full(size,5.0),np.ones(size),np.ones(size))


class ValidationAndSimulationTests(unittest.TestCase):
    def test_equally_bad_baseline_and_candidate_are_rejected(self):
        e = evidence_fixture()
        log = DrivingLog(np.zeros((1,1,3,4,4)),np.array([0]),e.intrinsics,np.eye(4)[None])
        report = ObservedViewValidator(ConstantRasterizer(1.0)).validate(world_fixture(),world_fixture(),log,e)
        self.assertEqual(report.rgb_regression,0)
        self.assertGreater(report.absolute_rgb_error,0.9)
        self.assertFalse(report.accepted)

    def test_camera_offset_outside_world_is_rejected(self):
        camera = RenderCamera(np.eye(3),np.eye(4),(2,2))
        camera.ego_from_camera[0,3] = 30
        with self.assertRaises(ValueError):
            StateDrivenRenderer(ConstantRasterizer()).observe(world_fixture(),
                SimulationState(np.eye(4),{},{}),(camera,))

    def test_sky_pixels_do_not_dilute_front_intrusion_rate(self):
        e = evidence_fixture(np.array([[[[0,4],[4,4]]]]))
        log = DrivingLog(np.zeros((1,1,3,4,4)),np.array([0]),e.intrinsics,np.eye(4)[None])
        class SequenceRasterizer:
            calls = 0
            def render(self,scene,pose,k,size):
                self.calls += 1
                depth = 5.0 if self.calls == 1 else 4.0
                return CameraObservation(np.zeros((*size,3)),np.full(size,depth),np.ones(size),np.ones(size))
        report = ObservedViewValidator(SequenceRasterizer(),max_absolute_depth=2).validate(world_fixture(),world_fixture(),log,e)
        self.assertEqual(report.checked_geometry_pixels,1)
        self.assertEqual(report.new_front_intrusion_fraction,1.0)
        self.assertFalse(report.accepted)

    def test_bridge_advances_state_after_policy_observes(self):
        world = world_fixture()
        class Engine:
            installs = 0
            def install_world(self,w,p): self.installs += 1; self.world = w
            def reset(self,state): self.current = state
            def state(self): return self.current
            def advance(self,action,dt):
                pose = self.current.world_from_ego.copy()
                pose[0,3] += action.acceleration*dt
                self.current = SimulationState(pose,{}, {}, self.current.elapsed_seconds+dt)
        class Policy:
            def act(self,observations):
                assert len(observations)==1
                return DrivingAction(0,1)
        physics = PhysicsDescription(np.array([[0,0,0],[1,0,0],[0,1,0]]),np.array([[0,1,2]]),
                                     {"rigid_0":world.rigids["rigid_0"].dimensions},{"human_0":np.array([0.1,0.1])})
        engine=Engine()
        bridge=SimulationBridge(world,physics,engine,StateDrivenRenderer(ConstantRasterizer()),
                                (RenderCamera(np.eye(3),np.eye(4),(2,2)),))
        bridge.reset(SimulationState(np.eye(4),{},{}))
        transition=bridge.step(Policy(),2)
        self.assertEqual(transition.before.world_from_ego[0,3],0)
        self.assertEqual(transition.after.world_from_ego[0,3],2)
        bridge.reset(SimulationState(np.eye(4),{},{}))
        self.assertEqual(engine.installs,1)
        self.assertIs(engine.world,world)


if __name__ == "__main__":
    unittest.main()
