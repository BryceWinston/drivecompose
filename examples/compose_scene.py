"""纯数值示例：一个固定高斯车辆绕竖直轴旋转，检验局部资产复用。"""
from __future__ import annotations

import json
import numpy as np

from drivecompose.contracts import GaussianSet, RigidAsset, SimulationState, WorldVault
from drivecompose.rendering import StateComposer


def main():
    background = GaussianSet(np.array([[0, 0, -1]]), np.eye(3)[None] * 0.1,
                             np.array([1.0]), np.zeros((1, 3, 4)))
    body = GaussianSet(np.array([[-1, 0, 0], [1, 0, 0]]),
                       np.broadcast_to(np.diag([0.4, 0.1, 0.1]), (2, 3, 3)),
                       np.ones(2), np.zeros((2, 3, 4)))
    world = WorldVault(background, np.ones((6, 2, 2, 3)) * 0.4,
                       {"rigid_0": RigidAsset("rigid_0", body, np.array([4, 2, 1.5]))},
                       {}, np.array([[-20, -20, -3], [20, 20, 10]]), 7)
    pose = np.eye(4)
    pose[:3, :3] = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    pose[:3, 3] = [5, 0, 0]
    scene = StateComposer().assemble(world, SimulationState(np.eye(4), {"rigid_0": pose}, {}))
    print(json.dumps({"kind": "synthetic_geometry_demo", "world_rigid_centers": scene.gaussians.means[1:].tolist(),
                      "canonical_rigid_centers": body.means.tolist(), "actor_ranges": scene.actor_ranges}, indent=2))


if __name__ == "__main__":
    main()
