# DriveCompose 论文定位：近邻检索与证据记录

检索日期：2026-10-19，Asia/Shanghai。范围：可组合驾驶场景、规范资产、生成式三维补全、观测保持和状态驱动渲染。此记录服务于 [CVPR 论文方案](paper-positioning.md)，不是系统综述或绝对新颖性证明。

## 检索方式

使用当前可用网页检索与原始来源浏览。优先会议公开论文、arXiv、作者项目页与官方代码说明；第三方解读、聚合页和社交内容未作为技术判断依据。

本轮主要查询包括：

```text
OmniRe Omni Urban Scene Reconstruction arxiv official project
HUGSIM A Real-Time Photo-Realistic and Closed-Loop Simulator for Autonomous Driving
driving scene completion joint background object latent flow matching 3D Gaussian 2026
driving Gaussian world compositional completion diffusion scene assets 2026
"driving" "completion" "flow matching" "Gaussian"
"driving" "joint" "completion" "canonical"
"scene" "completion" "compositional" "driving" 2026
"Grounded Latents for Entity-Centric 4D Scene Generation" arxiv project
"HorizonForge" driving scene editing github project
"JRM" "Joint Reconstruction Model" arxiv
"GenAssets" latent space official project arxiv
```

按问题 / 表示近邻纳入，不以发表年份作为唯一筛选条件。反复出现的同一论文 arXiv、项目页、会议版本归并为同一记录。语义占据生成、LiDAR 补全和对象联合重建保留为机制近邻，不直接与 RGB 渲染指标混合排名。

## 核验条目

所有条目的访问日期均为 2026-10-19。“原文范围”说明本轮实际获得的材料，避免把摘要层面的信息当作完整实现审计。

| ID | 书目与状态 | 原始来源 / 本轮可读范围 | 与 DriveCompose 的关系 |
| --- | --- | --- | --- |
| L01 | Ziyu Chen et al. **OmniRe: Omni Urban Scene Reconstruction**，ICLR 2025；arXiv:2408.16760 | [作者项目页](https://ziyc.github.io/omnire/)、[arXiv](https://arxiv.org/abs/2408.16760)；项目方法说明与摘要 | 已有背景 / 多类动态对象规范表示、刚体车辆和模板人体关节控制。需要把差异落在生成补全及其证据上。 |
| L02 | Hongyu Zhou et al. **HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving**，2024 年预印本；arXiv:2412.01718 | [作者项目页](https://xdimlab.github.io/HUGSIM/)、[arXiv](https://arxiv.org/abs/2412.01718)；系统架构与摘要 | 高斯闭环仿真、控制驱动状态变化和车辆插入已有先例。 |
| L03 | Yunzhi Yan et al. **StreetCrafter: Street View Synthesis with Controllable Video Diffusion Models**，CVPR 2025；arXiv:2412.13188 | [作者项目页](https://zju3dv.github.io/street_crafter/)、[会议 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yan_StreetCrafter_Street_View_Synthesis_with_Controllable_Video_Diffusion_Models_CVPR_2025_paper.pdf)；项目方法说明、原文检索片段 | 使用 LiDAR 渲染条件控制视频生成，并以生成视图监督动态高斯表示。 |
| L04 | Yifan Wang et al. **HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles**，CVPR 2026；arXiv:2602.21333 | [作者项目页](https://horizonforge.github.io/)、[会议 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf)；项目说明与方法原文片段 | 可编辑 Gaussian / mesh 与视频扩散渲染结合，覆盖 ego / agent 编辑。 |
| L05 | Ziyue Zhu et al. **WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving**，ICLR 2026；arXiv:2509.23402 | [arXiv 全文 HTML](https://arxiv.org/html/2509.23402v1)、[作者项目页](https://wm-research.github.io/worldsplat/)、[官方仓库说明](https://github.com/xiaomi-research/worldsplat/blob/main/README.md)；全文 HTML 与方法说明 | 4D 感知潜空间生成、像素对齐高斯解码与增强视频扩散。全文 3.4 与推理段明确描述渲染后的扩散增强。 |
| L06 | Jinhyung Park et al. **Grounded Latents for Entity-Centric 4D Scene Generation**（LatentWorld），CVPR 2026 | [会议条目](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Grounded_Latents_for_Entity-Centric_4D_Scene_Generation_CVPR_2026_paper.html)、[作者项目页](https://jindapark.github.io/projects/latentworld/)；会议摘要与项目方法说明 | 实体中心 grounded latent、背景区域 latent、语义高斯 / 占据、layout / feature / motion 生成。其输出任务与光度表面重建不同。 |
| L07 | Ze Yang et al. **GenAssets: Generating in-the-wild 3D Assets in Latent Space**，CVPR 2025 | [会议 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_GenAssets_Generating_in-the-wild_3D_Assets_in_Latent_Space_CVPR_2025_paper.pdf)；原文方法检索片段 | 从驾驶场景中学习资产潜空间及生成先验，涉及遮挡感知分解和补全。以会议版本定年；检索出现的 2026 年 arXiv 发布记录不作为另一个新工作。 |
| L08 | Ziwei Liao et al. **Complete Gaussian Splats from a Single Image with Denoising Diffusion Models**，项目论文；本轮未额外核验会议状态 | [作者项目页](https://nianticspatial.github.io/completesplat/)；摘要与任务说明 | 已有从单图通过潜空间扩散补全隐藏高斯场景的机制。 |
| L09 | Qirui Wu et al. **JRM: Joint Reconstruction Model for Multiple Objects without Alignment**，2026；arXiv:2603.25985 | [arXiv](https://arxiv.org/abs/2603.25985)；摘要；另检索到 CVPR 2026 同题条目 | 对同一对象的多份未对齐观测进行潜空间流匹配聚合，覆盖非刚体变化；属于联合重建机制近邻。 |

StreetCrafter 的作者与会议年份同时由作者项目页正文和 BibTeX 核对。本文件保留定位所需书目，未生成独立 BibTeX；方法相关性判断不依赖引用计数。

## 与现有代码之间可定位的候选差异

| 候选主张 | 代码证据 | 最近邻压力 | 尚需证据 |
| --- | --- | --- | --- |
| C001：异构规范空间的联合补全有效 | `decomposition.py:109` 的多类型支撑；`completion.py:49` 的双坐标条件；`CompletionBlock.forward` 的局部注意力与记忆读写 | L01、L05、L06 已覆盖可组合 / 潜码 / 高斯等多个要素；L07–L09 覆盖生成与联合重建机制 | 同预算联合 vs 独立；参考世界坐标作用；新放置状态是否仍可用 |
| C002：补全兼容已观测内容 | `completion.py:79` 的积分覆盖；`decoders.py:18` 的空域不透明度；`pipeline.py:69` 的两份世界；`validation.py` 的重渲染验证 | 硬条件与生成补全不宜作为首次提出；应证明完整约束设计的收益 | 已见退化与未见质量权衡；所有场景拒绝率和有效域；独立几何真值 |
| C003：同一补全内容支持状态干预 | `rendering.py` 的刚体 / 蒙皮装配；`simulation.py` 的状态更新 | L01、L02 已支持规范资产与状态驱动仿真；L04、L05 提供场景编辑 / 新轨迹生成 | 新相机、车辆、人体状态下的真实渲染质量；固定策略 / 物理的应用验证 |

这里的代码定位表示机制存在，不表示相关主张已经被实验支持。候选差异是从现有实现与已读材料推导出的研究定位。

## 来源访问限制与剩余检索项

- 本轮部分 OpenReview PDF 请求遇到浏览器验证页面；部分 CVF 直接 HTML / PDF 请求未返回正文。WorldSplat 改用 arXiv 全文；OmniRe、LatentWorld 等使用作者项目页与已获取的会议 / 摘要记录。
- LatentWorld、JRM、GenAssets 和 CompleteSplat 的差异判断尚不等于完整逐节核验。正式写 Related Work 前应核对它们的观测条件、损失、补全采样和实际评测范围。
- 后续针对 C001–C002 检索 observation-preserving / data-consistent 3D inpainting、mixed canonical / scene-coordinate conditioning、scene–object joint completion，检查最接近机制。
- 不从当前检索推断不存在相同方法，也不将未知机制记为论文“没有”。

## 数据依据

- [Waymo 官方数据说明](https://www.waymo.com/open/about/)支持相机、LiDAR、标定、位姿及实例标注的来源说明；实际使用的 798 / 202 场景数来自用户本轮提供的条件，需要在数据清单中落实。
- [CARLA 官方行人骨架接口说明](https://carla-ue5.readthedocs.io/en/latest/tuto_G_pedestrian_bones/)说明可以读取行人骨架。它不自动保证完整衣物表面、规范高斯目标或与本项目相同拓扑的模板已经可得；若选该合成后端，还需单独验收相应导出链路。
