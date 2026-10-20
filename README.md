# DriveCompose

**Composable Gaussian Worlds from Driving Logs · 从驾驶日志构建可组合高斯世界**

DriveCompose 从多相机驾驶日志恢复背景、刚体车辆和可驱动人体，通过离线补全构建供多条仿真轨迹复用的固定高斯世界。

项目包含算法设计、数据契约、数值实现和神经网络模块。

## 主流程

1. **Driving Log Encoder** 共享编码多相机与多时刻图像，恢复几何、实例身份、相机位姿和资产状态。
2. **Scene–Asset Decomposer** 将背景放在世界坐标，将车辆和人体放入各自的规范空间。
3. **Joint Completion DiT** 根据观测、场景结构和可见性，联合补全背景空洞和资产未见表面。
4. **Background Decoder / Rigid Vehicle Decoder / Human Avatar Decoder** 输出背景与天空、刚体车辆、骨架绑定人体。
5. **Composable Gaussian World** 以 `WorldVault` 数据契约保存构建后的固定内容。
6. **State-driven Renderer** 根据当前仿真状态组装与渲染；**Simulation Bridge** 连接策略动作和下一步状态。

车辆的局部几何、尺寸和外观固定，运行时只接受整体 SE(3) 变换，车轮随车体整体运动。人体的规范形状和绑定固定，当前骨架姿态控制世界空间中的人体表面。

## 阅读顺序

- [完整架构与流程图](docs/architecture.md)
- [Mermaid 数据流程图：简化版与详细版](docs/data-flow.md)
- [CVPR 论文定位、总览图与消融实验方案](docs/paper-positioning.md)
- [CVPR 风格方法总览图与近期论文视觉参考](docs/figures/overview-cvpr-20261020/README.md)
- [表示、坐标和张量契约](docs/representations.md)
- [分解与补全的算法细节](docs/algorithm.md)
- [分阶段训练与损失](docs/training.md)
- [评估与消融计划](docs/evaluation_plan.md)
- [设计选择](docs/decisions.md)

`src/drivecompose/` 中的数值核心使用 NumPy；`networks/`、`training.py` 与 `pipeline.py` 使用 PyTorch。

## 文件入口

```text
src/drivecompose/
  contracts.py          数据契约与固定世界
  geometry.py           坐标、投影、骨架变换
  decomposition.py      查询支撑、规范化、可见性聚合
  networks/encoder.py   共享编码与轨迹级身份槽
  networks/completion.py 联合条件补全
  networks/decoders.py  潜码编码与三路解码
  training.py           可微损失片段
  pipeline.py           离线构建及观测验证
  rendering.py          状态装配与渲染接口
  simulation.py         策略与动力学接口
  world.py              NPZ 世界存取
```

## 数值检查

在项目目录中，使用已安装 NumPy 的 Python：

```powershell
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/compose_scene.py
```

神经网络模块的依赖通过 `pip install -e ".[networks]"` 安装。`configs/concept.json` 定义场景范围、网络结构、采样参数和观测验证阈值。

## 场景与世界复用

场景采用有限世界范围、固定光照、刚体车辆和受支持骨架姿态。补全根据观测生成世界表示，构建后的背景与规范资产保持固定；不同轨迹共享资产身份、几何和背景，在线按当前状态装配与渲染。

道路网格、碰撞代理与高斯视觉表示分别维护，并共享资产坐标和状态。高斯渲染质量、几何真实性、碰撞有效性和策略表现需要分别评估。
