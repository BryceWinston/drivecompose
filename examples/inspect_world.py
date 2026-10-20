"""读取已有世界文件的结构，不创建或补造观测。"""
import argparse
import json

from drivecompose.world import load_world


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("world", help="已有的 .npz 世界文件")
    args = parser.parse_args()
    world = load_world(args.world)
    print(json.dumps({"background_gaussians": len(world.background.means), "vehicles": list(world.vehicles),
                      "humans": list(world.humans), "metadata": dict(world.metadata)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
