# DriveCompose 主张与证据

更新：2026-10-20。沿用项目 `docs/paper-positioning.md` 的 C001–C003，不另建研究状态机。

当前材料支持方法结构与实现机制的描述；未提供训练权重、完整训练记录或 DriveCompose 性能结果。正文不据此声称优于基线、统计显著或已经完成闭环实验。

| ID | 当前正文对应内容 | 原始依据（相对 `drivecompose/`） | 证据状态与待补条件 |
| --- | --- | --- | --- |
| C001 | 异构规范查询上的背景—资产联合补全 | `decomposition.py` 的 `make_blocks`、`QueryBundle.layout`；`networks/completion.py` 的 `CompletionBlock`、`JointCompletionDiT`；`docs/algorithm.md` | 查询分组、双坐标条件和局部/全局交换机制可定位。联合补全收益仍需同预算独立补全对照 |
| C002 | 已见潜码锁定、自由空间清零与不透明度抑制、原视角接受检查 | `completion.py` 的 `integrate`；`decoders.py` 的 `GaussianDecoder.forward`；`pipeline.py` 的两份世界；`validation.py` 的 `validate` | 保护机制可定位。固定逐查询 codec 下的参数不变不等于新增遮挡被消除；需要原视角重渲染与全部场景通过/拒绝率 |
| C003 | 固定世界按外部状态装配并跨轨迹复用 | `contracts.py` 的 `WorldVault`；`rendering.py` 的 `StateComposer`、`transform_gaussians`；`simulation.py` 的 `SimulationBridge` | 只读资产、刚体/蒙皮、协方差与外观方向变换及状态桥可定位。新状态质量、效率和策略效果仍需实测 |
| D001 | 图像、尺度与相机位姿契约 | `contracts.py` 的 `DrivingLog`；`docs/representations.md`；`networks/encoder.py` | 米制、相机安装标定与 rig 世界运动分开；输入要求预先校正针孔图像与统一颜色 |
| D002 | 固定布局目标与四阶段学习过程 | `training.md`；`completion.py` 的 `flow_loss`、`integrate`；`training.py`；`pipeline.py` 的 `CheckpointRecord` | 方法规格、目标有效性检查和损失片段存在；不等同于完整训练器及四阶段训练已执行 |

以上源码均位于 `src/drivecompose/`，迁移时的完整文件哈希记在 [来源清单](provenance/source-manifest.json)。目录整理前的文档快照和外部原件位置见 [归档索引](provenance/README.md)。现有数值测试的存在只作为实现检查线索，本轮不把它们改写为研究结果。

## 材料缺口

| 编号 | 尚需材料 | 受影响内容 |
| --- | --- | --- |
| G001 | Waymo 数据适配、固定场景与身份清单、相机/颜色/尺度协议 | 恢复和训练输入；两版实验后续统一 |
| G002 | 完整场景/资产目标来源、同查询布局目标构造器、未知查询 `target_valid` | 条件流先验训练；真实部分日志不能自动提供完整隐藏表面 |
| G003 | 同拓扑人体模板、身份体型与骨架绑定提供器 | 人体查询构造和新姿态有效域 |
| G004 | 可微高斯渲染、有效域输出、道路/碰撞代理与动力学实现 | 观测检查、渲染适配、真实闭环应用 |
| G005 | 完整训练器、checkpoint、运行配置与日志、机制消融和独立测试 | C001–C003 的经验结论与效率 |
| G006 | 原英文实验数值对应的原始日志、代码版本、场景清单；中文引用数值与来源协议核对 | 用户暂时冻结的实验章节；本轮不改、不补数值 |
| G007 | 正式结果图、原视角及新状态的真实渲染样例 | 当前原生矢量总览图只作机制说明，不能当作 Waymo 或模型渲染结果 |
| G008 | 官方 CVPR 2027 最终 author-kit 与当届要求 | 当前两版年份为 2027，样式沿用原工程；未完成正式投稿核查 |
| G009 | 实际训练采用的各项损失权重、采样数量、阶段预算与检查阈值来源 | 当前配置未提供全套最终训练设置；方法保留符号权重，不补造数值 |

正文中的训练流程是方法规格；既有实现中的后端协议与损失接口不应被解释为这些外部模块或真实训练已经全部落实。经验结论待 G001–G006 补齐后回写，并同步中英文。实验文件本轮受用户冻结要求保护。

## 本轮方法表述修正

2026-10-20：按 `networks/completion.py` 明确局部查询到全局记忆的读写；按 `training.py` 区分自由射线不透明度、地下脚点、接触与穿透四项有效软约束。固定逐查询 codec 与每步潜码硬恢复使已见高斯参数保持不变；此时对这些参数再加差异惩罚恒为零，本轮从适配目标中去掉该无效项。代码中的相关 helper 保持原样。新增内容导致的遮挡仍由渲染误差、射线约束和原视角接受检查处理。

这属于方法说明与既有计算接口的对齐，不是新的实验发现。双语公式同步，实验章节未修改。结构参考与采用理由见 [本轮参考研究](provenance/structure-study-20261020.md)。
