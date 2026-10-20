# DriveCompose Mermaid 数据流程图

依据当前项目的 `pipeline.py`、数据契约、网络模块及仿真代码整理。简化版用于说明整体机制，详细版用于逐步追踪数据、坐标空间、观测保护与在线状态更新。两版均覆盖离线推理与在线仿真；训练流程见 [training.md](training.md)。

## 简化版

读取顺序：左侧离线构建自上而下；固定 `WorldVault` 供右侧在线闭环跨轨迹复用。为保持总览紧凑，观测基线、失败出口、物理描述安装与相机变换在详细版展开。

[Mermaid 源文件](diagrams/data-flow-simple.mmd) · [SVG 矢量预览](diagrams/data-flow-simple.svg) · [PNG 预览](diagrams/data-flow-simple.png)

```mermaid
flowchart LR
  subgraph OFFLINE["离线：从驾驶日志构建固定世界"]
    direction TB
    LOG["多相机驾驶日志<br/>图像、时间戳、标定、可选自车位姿"]
    ENC["Driving Log Encoder<br/>共享特征、几何、实例身份与逐帧状态"]
    DEC["Scene–Asset Decomposer<br/>背景 / 车辆 / 人体 / 天空查询<br/>规范化、跨视图聚合、可见性标记"]
    DIT["分类型潜码编码 + Joint Completion DiT<br/>锁定已观测潜码，补全未知区域，清零自由空间"]
    HEADS["三路解码<br/>背景与天空 / 刚体车辆 / 绑定人体"]
    CHECK["ObservedViewValidator<br/>原视角重渲染，检查观测一致性<br/>仅通过检查的结果进入固定世界"]
    WORLD[("WorldVault：固定可组合高斯世界<br/>背景、天空、规范资产、支撑范围与种子")]
    LOG --> ENC --> DEC --> DIT --> HEADS --> CHECK
    CHECK --> WORLD
  end

  subgraph ONLINE["在线：同一世界上的仿真闭环"]
    direction TB
    STATE["SimulationState：当前状态<br/>自车位姿、活动车辆位姿、人体根位姿与骨架"]
    RENDER["State-driven Renderer<br/>状态装配 + 外接多相机高斯渲染"]
    OBS["CameraObservation<br/>RGB、depth、alpha、coverage"]
    POLICY["驾驶策略 DrivingPolicy【外接】"]
    ENGINE["Simulation Bridge + DynamicsEngine【外接】<br/>结合道路 / 碰撞代理，根据动作与步长<br/>推进自车、其他车辆与人体状态"]
    STATE --> RENDER --> OBS --> POLICY
    POLICY -->|转向、加速度| ENGINE
    ENGINE -->|下一状态；重复闭环| STATE
  end

  OFFLINE -->|WorldVault 固定内容<br/>跨轨迹复用| ONLINE

  classDef input fill:#EFF6FF,stroke:#2563EB,color:#172554;
  classDef process fill:#F8FAFC,stroke:#64748B,color:#0F172A;
  classDef generation fill:#F3E8FF,stroke:#9333EA,color:#3B0764;
  classDef store fill:#ECFDF5,stroke:#059669,color:#064E3B;
  classDef check fill:#FFF7ED,stroke:#EA580C,color:#7C2D12;
  classDef external fill:#FFFFFF,stroke:#475569,stroke-dasharray:5 4,color:#0F172A;
  class LOG,STATE input;
  class ENC,DEC,HEADS,RENDER,OBS process;
  class DIT generation;
  class WORLD store;
  class CHECK check;
  class POLICY,ENGINE external;
```

## 详细版

A–F 为离线世界构建，G 为在线仿真。实线表示主要数据流、顺序关系或状态反馈；虚线表示辅助条件、外部依赖或可选持久化。标有“外接”的节点为项目定义的接口，具体后端由调用方提供。完整流程较长，查看时可打开 SVG 放大。

[Mermaid 源文件](diagrams/data-flow-detailed.mmd) · [SVG 矢量预览](diagrams/data-flow-detailed.svg) · [PNG 预览](diagrams/data-flow-detailed.png)

```mermaid
flowchart TB
  subgraph INPUT["A · 输入与离线构建条件"]
    LOG["DrivingLog.validate<br/>images: T×V×3×H×W；timestamps: T<br/>K、rig_from_camera、可选 world_from_rig"]
    VERS["已加载 Encoder / Codec / Completion<br/>CheckpointRecord.validate<br/>核对特征基、潜码与查询布局版本"]
    CONFIG["构建参数<br/>bounds、背景 / 车辆网格、天空分辨率<br/>steps、seed"]
    TEMPLATE["HumanTemplateProvider【外接】<br/>根据体型码返回规范支撑、权重与 bind pose"]
  end

  subgraph ENCODER["B · Driving Log Encoder：共享恢复"]
    PATCH["Patch 编码 + 像素位置<br/>相机标定与相对时间条件"]
    CONTEXT["图像内 Transformer<br/>跨视图 / 跨时刻摘要交互"]
    GEOM["几何与语义头<br/>光轴深度、置信度、语义"]
    ACTOR["轨迹级身份槽 + 逐帧状态读取<br/>实例分配、车辆尺寸 / 位姿<br/>人体体型、根位姿与关节旋转"]
    POSE["相机世界位姿<br/>使用日志 rig 位姿，或估计 rig 运动<br/>T_world_camera = T_world_rig × T_rig_camera"]
    EVID["SceneEvidence<br/>features: T×V×h×w×F；深度 / 置信度<br/>实例 / 语义、相机位姿、ActorTrack"]
    PATCH --> CONTEXT
    CONTEXT --> GEOM
    CONTEXT --> ACTOR
    CONTEXT --> POSE
    GEOM --> EVID
    ACTOR --> EVID
    POSE --> EVID
  end
  LOG --> PATCH
  VERS -.->|版本一致后构建| PATCH
  LOG -.->|标定与可选 rig 位姿| POSE
  TEMPLATE -.->|人体规范模板与骨架绑定| ACTOR

  subgraph DECOMPOSITION["C · Scene–Asset Decomposer：规范支撑与观测聚合"]
    BGQ["背景查询<br/>可靠深度抬升锚点 + 有限空间网格<br/>世界坐标"]
    VEHQ["车辆查询<br/>逆轨迹变换后的锚点 + 包围体网格<br/>固定车辆局部坐标"]
    HUMQ["人体查询<br/>同一身份模板的完整规范支撑<br/>固定骨架权重与邻域尺度"]
    SKYQ["天空查询<br/>立方体贴图六面单位方向"]
    PLACE["make_blocks → QueryBlock<br/>规范位置、尺度、类型、参考世界位置、分组<br/>跨时刻放置并投影到输入相机取特征"]
    GATE["观测门控与加权聚合<br/>视野、深度残差、置信度、实例 / 语义<br/>可靠射线对自由空间投票；天空仅按旋转投影"]
    BUNDLE["QueryBundle<br/>融合特征: N×(F+1)；layout；场景摘要 context<br/>known / free / unknown 互斥；confidence"]
    EVID --> BGQ
    EVID --> VEHQ
    EVID --> HUMQ
    EVID --> SKYQ
    BGQ --> PLACE
    VEHQ --> PLACE
    HUMQ --> PLACE
    SKYQ --> PLACE
    PLACE --> GATE --> BUNDLE
  end
  CONFIG -.->|支撑范围与查询容量| PLACE
  EVID -.->|特征、深度、标签、相机与资产轨迹| GATE

  subgraph COMPLETION["D · 分类型潜码编码与联合条件补全"]
    CODEC["TypedLatentCodec.encode<br/>四类独立投影 → 共同宽度潜码 z_obs: N×D<br/>仅保留 known 查询的编码"]
    INIT["sample / integrate 初始化<br/>known = z_obs；free = 0<br/>unknown = 固定种子的高斯噪声"]
    COND["补全条件 C<br/>z_obs、known / free、confidence、context<br/>类型、规范坐标、参考世界坐标、尺度、分组"]
    DIT["JointCompletionDiT.forward<br/>组内局部注意力 + 跨组全局记忆<br/>预测未知查询的潜码速度"]
    EULER["Euler 积分：流时间 τ 从 0 到 1<br/>每步恢复 known，并将 free 清零"]
    ZDONE["联合补全潜码 z_complete: N×D"]
    BUNDLE --> CODEC --> INIT --> DIT --> EULER
    BUNDLE --> COND --> DIT
    CODEC --> COND
    EULER -->|未到最后一步| DIT
    EULER -->|完成 steps 步| ZDONE
  end
  CONFIG -.->|seed 与 steps；示例配置为 24 步| INIT

  subgraph DECODE["E · 三路解码与观测保护"]
    BGD["BackgroundDecoder<br/>世界坐标背景高斯 + 天空颜色<br/>sky_valid 取已观测天空方向"]
    VEHD["RigidVehicleDecoder<br/>每查询生成 K 个固定局部高斯<br/>保留 actor_id 与固定尺寸"]
    HUMD["HumanAvatarDecoder<br/>每查询生成 K 个规范人体高斯<br/>子高斯继承模板绑定权重"]
    CAND["export_world → 候选 WorldVault<br/>高斯：中心、协方差、不透明度、方向外观<br/>free 查询的高斯不透明度显式置零"]
    BASE["同一 Codec 解码 z_obs → 观测基线<br/>非 known 查询的高斯不透明度关闭"]
    REF["验证参考<br/>原日志 RGB + 编码器预测深度<br/>原相机位姿与原资产状态"]
    REPLAY["ObservedViewValidator<br/>将候选与观测基线放回原状态、原相机<br/>经 StateComposer 与外接 GaussianRasterizer 重渲染"]
    VALID{"观测约束是否通过？<br/>绝对 RGB / 深度误差、逐视图覆盖率<br/>RGB 退化、新增前景侵入、最差视图约束"}
    FAIL["抛出 ValueError<br/>本次构建不返回 BuildResult"]
    ZDONE --> BGD
    ZDONE --> VEHD
    ZDONE --> HUMD
    BGD --> CAND
    VEHD --> CAND
    HUMD --> CAND
    CODEC --> BASE
    CAND --> REPLAY
    BASE --> REPLAY
    REF --> REPLAY --> VALID
    VALID -->|未通过| FAIL
  end
  LOG -.->|原始 RGB| REF
  EVID -.->|预测深度、相机与资产状态| REF

  subgraph FIXED["F · 固定内容与持久化"]
    WORLD[("通过检查的 WorldVault + ValidationReport<br/>背景、天空 / sky_valid、规范车辆与人体<br/>bounds、build_seed、表示版本；数组只读")]
    NPZ[("可选 NPZ 世界文件<br/>save_world / load_world<br/>数组 + JSON 元数据；allow_pickle=False")]
    VALID -->|通过；写入检查状态与表示版本| WORLD
    WORLD -.->|可选保存；读取后恢复同一契约| NPZ
  end

  subgraph ONLINE["G · 在线仿真：固定世界 + 当前状态"]
    PHYS["PhysicsDescription【外部提供】<br/>道路三角网格、车辆尺寸、人体骨骼半径<br/>共享视觉资产 ID、坐标与尺寸"]
    INSTALL["SimulationBridge 初始化<br/>physics.validate → engine.install_world<br/>reset 只重置仿真状态"]
    STATE["SimulationState s_k<br/>自车世界位姿、活动车辆位姿<br/>人体根位姿 / 骨架姿态、仿真计时"]
    COMPOSE["StateComposer.assemble<br/>按当前状态选择活动资产"]
    BGFIX["背景直接复用<br/>天空与有效域保持固定"]
    RIGID["车辆整体 SE(3) 变换<br/>中心、协方差、局部方向映射同步更新"]
    SKIN["人体按当前骨架蒙皮，再应用根位姿<br/>中心、协方差、局部方向映射同步更新"]
    SCENE["AssembledScene<br/>拼接世界高斯、actor_ranges<br/>附带 sky、sky_valid、bounds"]
    CAM["RenderCamera + 当前自车位姿<br/>T_world_camera = T_world_ego × T_ego_camera<br/>内参 K 与图像分辨率"]
    RASTER["StateDrivenRenderer → GaussianRasterizer【外接】<br/>相机 / 自车支撑范围检查<br/>投影、遮挡合成、天空与逐像素有效域"]
    OBS["多相机 CameraObservation<br/>rgb、depth、alpha、coverage"]
    POLICY["DrivingPolicy.act【外接】"]
    ACTION["DrivingAction<br/>steering、acceleration"]
    DYN["DynamicsEngine.advance(action, dt)【外接】<br/>推进自车、其他车辆与人体交互状态"]
    TRANS["Transition<br/>before、observations、action、after"]
    PHYS --> INSTALL -->|初始状态 reset| STATE
    STATE --> COMPOSE
    COMPOSE --> BGFIX
    COMPOSE --> RIGID
    COMPOSE --> SKIN
    BGFIX --> SCENE
    RIGID --> SCENE
    SKIN --> SCENE
    STATE --> CAM
    CAM --> RASTER
    SCENE --> RASTER --> OBS --> POLICY --> ACTION --> DYN
    DYN -->|engine.state：下一状态 s_k+1| STATE
    DYN -->|step 返回本次转移记录| TRANS
  end
  WORLD -->|安装同一固定世界| INSTALL
  WORLD -->|每步读取固定背景与规范资产| COMPOSE

  classDef input fill:#EFF6FF,stroke:#2563EB,color:#172554;
  classDef process fill:#F8FAFC,stroke:#64748B,color:#0F172A;
  classDef generation fill:#F3E8FF,stroke:#9333EA,color:#3B0764;
  classDef store fill:#ECFDF5,stroke:#059669,color:#064E3B;
  classDef check fill:#FFF7ED,stroke:#EA580C,color:#7C2D12;
  classDef external fill:#FFFFFF,stroke:#475569,stroke-dasharray:5 4,color:#0F172A;
  class LOG,CONFIG,STATE,CAM input;
  class PATCH,CONTEXT,GEOM,ACTOR,POSE,BGQ,VEHQ,HUMQ,SKYQ,PLACE,GATE,CODEC,BGD,VEHD,HUMD,BASE,REF,INSTALL,COMPOSE,BGFIX,RIGID,SKIN,SCENE,OBS,ACTION,TRANS process;
  class INIT,COND,DIT,EULER,ZDONE generation;
  class EVID,BUNDLE,CAND,WORLD,NPZ store;
  class VERS,REPLAY,VALID,FAIL check;
  class TEMPLATE,PHYS,RASTER,POLICY,DYN external;
```

## 图中数据的含义

| 数据 | 内容与坐标 / 张量契约 |
| --- | --- |
| `DrivingLog` | 多相机同步图像 `[T,V,3,H,W]`，时间戳 `[T]`，内参 `[V,3,3]`，安装外参 `[V,4,4]`，可选自车世界位姿 `[T,4,4]`。输入准备为线性 RGB 和针孔模型；畸变、滚动快门与曝光处理属于入口前的数据适配。 |
| `SceneEvidence` | 图像特征 `[T,V,h,w,F]`，光轴深度、置信度、实例与语义标签，相机世界位姿及轨迹级资产状态。法线由编码器头预测，但当前 `encode` 未将其导出到 `SceneEvidence`。 |
| `QueryBlock / QueryBundle` | 背景在世界坐标，车辆在固定局部坐标，人体在规范空间，天空在单位方向域。融合特征 `[N,F+1]` 的最后一维是归一化有符号深度残差；另存查询布局、观测标记、置信度和场景摘要。 |
| `z_obs / z_complete` | 潜码为 `[N,D]`。`known` 为可靠已见表面，`free` 为可靠自由空间，`unknown = ~(known | free)`。已见潜码每步锁定，自由空间每步清零；仅未知潜码随流积分更新。 |
| `GaussianSet` | 中心 `[M,3]`、正定协方差 `[M,3,3]`、不透明度 `[M]`、局部方向外观 `[M,3,4]`，以及观察方向到局部坐标的映射。单个非天空查询产生 K 个高斯。 |
| `WorldVault` | 固定背景、天空与 `sky_valid`、规范车辆和人体、支撑范围、构建种子与元数据。数组复制后设为只读。 |
| `SimulationState` | 本步自车位姿、活动车辆映射、人体根位姿与当前骨架，以及仿真计时；资产是否活动由状态映射显式确定。 |
| `CameraObservation / Transition` | 每相机输出 `rgb / depth / alpha / coverage`。`coverage` 表示支撑有效域。一步仿真返回 `before / observations / action / after`。 |

`T` 是输入时刻数，`V` 是相机数，`h,w` 是特征网格尺寸，`N` 是总查询数，`M` 是某个高斯集合的元素数。`configs/concept.json` 的示例参数为 `F=128`、融合特征宽度 129、`D=128`、`K=4`、采样 24 步；这些容量可通过模块和构建参数调整。构建入口接收参数，当前没有直接读取该 JSON 的总控脚本。

## 关键边界

- **补全与仿真分开执行。** `OfflineWorldBuilder.build` 完成编码、查询分解、潜码采样、解码和观测验证。在线 `observe / step` 读取同一份固定世界与当前状态；新 rollout 调用 `reset` 重置状态。
- **车辆与人体使用不同运动模型。** 车辆的尺寸、局部几何和外观固定，车轮随车体整体运动；人体保持规范形状与绑定，通过骨架蒙皮及根位姿变换运动。中心、协方差和方向映射同步更新。
- **构建检查有两份世界。** 同一个 codec 分别解码完整候选与仅观测基线；基线的非 `known` 高斯关闭不透明度。验证器在原相机、原资产状态下渲染两者，限制绝对误差、相对退化、覆盖率与新增前景侵入。深度参考来自编码器预测。检查不通过时直接抛出异常，源码没有自动修复或重试循环。
- **固定内容与物理描述分别提供。** `PhysicsDescription` 的道路网格和碰撞代理由调用方提供，与视觉资产共享 ID、坐标和尺寸；项目没有把高斯自动转换为道路或碰撞网格的实现。`HumanTemplateProvider`、`GaussianRasterizer`、`DrivingPolicy`、`DynamicsEngine` 需要接入具体后端。图表示当前模块与接口的数据流。
- **天空与持久化有明确约束。** 天空颜色由背景解码分支产生，`sky_valid` 仍取已观测天空查询。`save_world / load_world` 是独立、可选的 NPZ 接口，`build` 本身不自动写文件。

## 源码对应

| 图中阶段 | 源码与关键入口 |
| --- | --- |
| A：输入与版本 | [contracts.py](../src/drivecompose/contracts.py) 的 `DrivingLog`；[pipeline.py](../src/drivecompose/pipeline.py) 的 `CheckpointRecord.validate`、`OfflineWorldBuilder.build` |
| B：共享编码 | [networks/encoder.py](../src/drivecompose/networks/encoder.py) 的 `DrivingLogEncoder.forward / encode`、`HumanTemplateProvider` |
| C：规范支撑与聚合 | [decomposition.py](../src/drivecompose/decomposition.py) 的 `observed_support`、`make_blocks`、`SceneAssetDecomposer.decompose / _aggregate`、`QueryBundle.layout` |
| D：潜码与补全 | [networks/decoders.py](../src/drivecompose/networks/decoders.py) 的 `TypedLatentCodec.encode`；[networks/completion.py](../src/drivecompose/networks/completion.py) 的 `JointCompletionDiT.forward / sample / integrate` |
| E：解码与验证 | [networks/decoders.py](../src/drivecompose/networks/decoders.py) 的 `decode / export_world`；[validation.py](../src/drivecompose/validation.py) 的 `ObservedViewValidator.validate` |
| F：固定世界与存取 | [contracts.py](../src/drivecompose/contracts.py) 的 `WorldVault`；[world.py](../src/drivecompose/world.py) 的 `save_world / load_world` |
| G：在线装配与渲染 | [rendering.py](../src/drivecompose/rendering.py) 的 `StateComposer.assemble`、`StateDrivenRenderer.observe`、`GaussianRasterizer` |
| G：策略与动力学闭环 | [simulation.py](../src/drivecompose/simulation.py) 的 `PhysicsDescription.validate`、`DrivingPolicy`、`DynamicsEngine`、`SimulationBridge.step` |

## 编辑与渲染

直接编辑两个 `.mmd` 文件即可在支持 Mermaid 的编辑器中使用。本文的代码块与 `.mmd` 保持一致；修改源文件后应同步本文，并重新生成预览。当前两张图已通过本机 Mermaid CLI 实际渲染检查，预览使用 [mermaid-config.json](diagrams/mermaid-config.json) 的字体与间距设置。
