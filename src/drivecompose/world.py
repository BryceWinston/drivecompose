"""固定世界的显式 NPZ 存储；不序列化网络、历史状态或 Python pickle。"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .contracts import GaussianSet, HumanAvatarAsset, RigidVehicleAsset, WorldVault


FIELDS = ("means", "covariance", "opacity", "appearance", "direction_to_local")


def save_world(world: WorldVault, path: str | Path) -> None:
    path = Path(path)
    if path.suffix != ".npz":
        raise ValueError("世界文件扩展名须为 .npz")
    if path.exists():
        raise FileExistsError(path)
    arrays = {"sky": world.sky, "sky_valid": world.sky_valid, "bounds": world.bounds}
    entries = []
    for index, (kind, asset) in enumerate(
            [("vehicle", v) for v in world.vehicles.values()] + [("human", h) for h in world.humans.values()]):
        prefix = f"asset_{index}"
        for field in FIELDS:
            arrays[f"{prefix}_{field}"] = getattr(asset.gaussians, field)
        entry = {"kind": kind, "actor_id": asset.actor_id, "prefix": prefix}
        if kind == "vehicle":
            arrays[f"{prefix}_dimensions"] = asset.dimensions
        else:
            arrays[f"{prefix}_weights"] = asset.weights
            arrays[f"{prefix}_rest_global"] = asset.rest_global
            entry["parents"] = list(asset.parents)
        entries.append(entry)
    for field in FIELDS:
        arrays[f"background_{field}"] = getattr(world.background, field)
    manifest = {"schema": 1, "seed": world.build_seed, "metadata": dict(world.metadata), "assets": entries}
    arrays["manifest"] = np.array(json.dumps(manifest, ensure_ascii=False))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        np.savez_compressed(stream, **arrays)


def load_world(path: str | Path) -> WorldVault:
    with np.load(path, allow_pickle=False) as data:
        manifest = json.loads(str(data["manifest"]))
        if manifest["schema"] != 1:
            raise ValueError("不支持的世界格式")
        def gaussians(prefix):
            return GaussianSet(**{field: data[f"{prefix}_{field}"] for field in FIELDS})
        vehicles, humans = {}, {}
        for entry in manifest["assets"]:
            key, prefix = entry["actor_id"], entry["prefix"]
            if key in vehicles or key in humans:
                raise ValueError("世界文件含重复资产身份")
            if entry["kind"] == "vehicle":
                vehicles[key] = RigidVehicleAsset(key, gaussians(prefix), data[f"{prefix}_dimensions"])
            elif entry["kind"] == "human":
                humans[key] = HumanAvatarAsset(key, gaussians(prefix), data[f"{prefix}_weights"],
                                               data[f"{prefix}_rest_global"], tuple(entry["parents"]))
            else:
                raise ValueError("世界文件含未知资产类型")
        return WorldVault(gaussians("background"), data["sky"], vehicles, humans,
                          data["bounds"], manifest["seed"], manifest["metadata"], data["sky_valid"])
