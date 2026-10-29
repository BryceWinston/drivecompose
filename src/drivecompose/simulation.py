"""Simulation Bridge：策略动作经动力学更新后才影响下一步观测。"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np

from .contracts import SimulationState, WorldVault
from .rendering import CameraObservation, RenderCamera, StateDrivenRenderer


@dataclass(frozen=True)
class DrivingAction:
    steering: float
    acceleration: float


@dataclass(frozen=True)
class PhysicsDescription:
    """碰撞代理与视觉资产共用 actor 原点、尺寸、骨架和每步位姿。"""
    road_vertices: np.ndarray
    road_triangles: np.ndarray
    rigid_dimensions: dict[str, np.ndarray]
    human_bone_radii: dict[str, np.ndarray]

    def validate(self, world: WorldVault):
        if set(self.rigid_dimensions) != set(world.rigids) or set(self.human_bone_radii) != set(world.humans):
            raise ValueError("物理资产与视觉资产 ID 不一致")
        for key, asset in world.rigids.items():
            if not np.allclose(self.rigid_dimensions[key], asset.dimensions):
                raise ValueError("刚体碰撞尺寸与视觉资产尺寸不一致")
        for key, asset in world.humans.items():
            radii = self.human_bone_radii[key]
            if np.shape(radii) != (len(asset.parents),) or np.any(np.asarray(radii) <= 0):
                raise ValueError("人体碰撞半径与骨架不一致")
        vertices, faces = np.asarray(self.road_vertices), np.asarray(self.road_triangles)
        if vertices.ndim != 2 or vertices.shape[1] != 3 or not np.isfinite(vertices).all():
            raise ValueError("道路顶点应为 [N,3]")
        if faces.ndim != 2 or faces.shape[1] != 3 or not np.issubdtype(faces.dtype, np.integer):
            raise ValueError("道路三角形应为整数 [F,3]")
        if faces.size and (faces.min() < 0 or faces.max() >= len(vertices)):
            raise ValueError("道路面索引越界")


class DrivingPolicy(Protocol):
    def act(self, observations: tuple[CameraObservation, ...]) -> DrivingAction: ...


class DynamicsEngine(Protocol):
    def install_world(self, world: WorldVault, physics: PhysicsDescription) -> None: ...
    def reset(self, initial_state: SimulationState) -> None: ...
    def state(self) -> SimulationState: ...
    def advance(self, action: DrivingAction, dt: float) -> None:
        """推进自车、其他车辆和人体的交互状态；不能直接拿动作当下一步位姿。"""
        ...


@dataclass(frozen=True)
class Transition:
    before: SimulationState
    observations: tuple[CameraObservation, ...]
    action: DrivingAction
    after: SimulationState


class SimulationBridge:
    def __init__(self, world: WorldVault, physics: PhysicsDescription, engine: DynamicsEngine,
                 renderer: StateDrivenRenderer, cameras: tuple[RenderCamera, ...]):
        physics.validate(world)
        self.world, self.engine, self.renderer, self.cameras = world, engine, renderer, cameras
        engine.install_world(world, physics)

    def reset(self, initial_state: SimulationState) -> None:
        self.engine.reset(initial_state)

    def step(self, policy: DrivingPolicy, dt: float) -> Transition:
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError("仿真步长须为有限正数")
        before = self.engine.state()
        observations = self.renderer.observe(self.world, before, self.cameras)
        action = policy.act(observations)
        self.engine.advance(action, dt)
        return Transition(before, observations, action, self.engine.state())
