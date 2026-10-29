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

## 2026-10-29：前馈高斯消融指标调研

本轮由 `nature-academic-search` 执行，回答“现有消融指标是否通用，以及相关论文通常如何设计消融”。访问日期为 2026-10-29（Asia/Shanghai）。这是代表性原文核验，不是穷尽式系统综述；未修改论文、实验协议或已有结果数值。

### 检索与纳入范围

检索使用网页搜索及 CVF、arXiv 全文和作者项目页。实际查询包括：

```text
pixelSplat MVSplat ablation PSNR SSIM LPIPS table
feed forward gaussian splatting ablation study DepthSplat NoPoSplat 2025 2026
site.openaccess.thecvf.com pixelSplat 2024 paper ablation
MVSplat ECCV 2024 paper ablation table 3 cost volume
NoPoSplat No Pose No Problem ICLR 2025 ablation
STORM Spatio Temporal Reconstruction Model ablation PSNR SSIM table 2025
"pixelSplat" "Table 2" "Ablation"
"ReconSplat" "ablation"
"DGGT" site:openaccess.thecvf.com/content/CVPR2026
```

从现有 `paper/main.bib` 取得 DGGT、StreetForward、PointForward、Instant NuRec 的论文地址，直接打开全文核对。纳入静态前馈重建、动态驾驶重建与生成式外推三类；不把逐场景优化工作或第三方解读当作前馈消融的主要证据。同一工作不同入口合并，以下注明实际核验版本和位置。

### 原文证据矩阵

| ID | 论文与版本 | 消融位置、对象 | 实际报告的指标 | 直接来源 |
| --- | --- | --- | --- | --- |
| ABL01 | David Charatan et al., pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction，CVPR 2024 | 会议版表 2；移除极线编码器、深度编码、概率采样，加入深度正则 | PSNR、SSIM、LPIPS | [会议 PDF 的可检索表格](https://openaccess.thecvf.com/content/CVPR2024/papers/Charatan_pixelSplat_3D_Gaussian_Splats_from_Image_Pairs_for_Scalable_Generalizable_CVPR_2024_paper.pdf)；[早期 arXiv v2 §5.3](https://arxiv.org/html/2312.12337v2) 辅助核验机制，数值不混用 |
| ABL02 | Yuedong Chen et al., MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images，ECCV 2024；arXiv v2 | §4.3、表 3、图 6；cost volume、跨视图注意力、U-Net、depth refinement | PSNR、SSIM、LPIPS；附录表 B/C 加时间，比较骨干及每像素高斯数 | [全文](https://arxiv.org/html/2403.14627v2) |
| ABL03 | Haofei Xu et al., DepthSplat: Connecting Gaussian Splatting and Depth，CVPR 2025；arXiv v3 | §4.2、表 2；移除单目特征或 cost volume，更换预训练特征；表 1 比较骨干与尺度 | 图像 PSNR、SSIM、LPIPS；深度 AbsRel、δ₁；模型规模实验另报参数和耗时 | [全文](https://arxiv.org/html/2410.13862v3) |
| ABL04 | Botao Ye et al., No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images（NoPoSplat），ICLR 2025；本轮核对 arXiv v1 | §4.2、表 5；内参编码、RGB shortcut、canonical / transform-then-fuse、2/3 输入视图 | PSNR、SSIM、LPIPS | [全文及对应版本表 5](https://arxiv.org/html/2410.24207v1) |
| ABL05 | Jiawei Yang et al., STORM: Spatio-Temporal Reconstruction Model for Large-Scale Outdoor Scenes，ICLR 2025；本轮核对 arXiv v1 | 附录 B.2、图 B.1–B.2；速度正则系数、motion token 数、训练/测试输入时刻数 | 图 B.1 明确使用 Dynamic PSNR、EPE3D、Acc₅；输入变化区分固定模型直接测试和按输入数重训 | [全文](https://arxiv.org/html/2501.00602v1)；[会议版入口](https://proceedings.iclr.cc/paper_files/paper/2025/file/7dee643a6c5abcdafee51496420c84dc-Paper-Conference.pdf) |
| ABL06 | Xiaoxue Chen et al., DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images，CVPR 2026；本轮消融定位为 arXiv v1 | §4.3、表 4：lifespan、diffusion refinement；表 3：4/8/16 输入视图 | 组件消融为 PSNR、SSIM、LPIPS；输入数量表分别报输入重建和 NVS 的 PSNR、SSIM、D-RMSE | [全文](https://arxiv.org/html/2512.03004v1)；[会议条目](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.html) |
| ABL07 | Zhongrui Yu et al., StreetForward: Perceiving Dynamic Street with Feedforward Causal Attention，2026；本轮依据 arXiv v1，不推断进一步发表状态 | §6.3、表 6；因果注意力、horizon、刚性正则、反向速度、前后向一致性、不透明度正则 | Dynamic Only 和 Full Image 分别报 PSNR、SSIM | [全文](https://arxiv.org/html/2603.19552v1) |
| ABL08 | Cheng Chi et al., PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations，2026；本轮依据 arXiv v1 | §4.4、表 5；加权融合、深度感知融合、lifespan、LiDAR depth | 组件消融用 PSNR、SSIM；另一个实验的表 4 用 FID 比较横向相机偏移，不能把它写成组件消融指标 | [全文](https://arxiv.org/html/2605.11594v1) |
| ABL09 | NVIDIA, Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation，2026；arXiv v1 | §5.3、表 2，内部验证数据；单阶段训练、天空 MLP、去 LPIPS/depth loss、去 frustum-ownership merging | PSNR、SSIM、AbsRel、δ₁ | [全文](https://arxiv.org/html/2607.14203v1) |
| ABL10 | Giuseppe Stracquadanio et al., ReconSplat: Generalizable 3D Scene Reconstruction Beyond Observed Views，作者项目页标注 ECCV 2026；arXiv v1 | §4.4、表 6；3DGS latent 条件、生成深度先验、多分辨率噪声、输入上采样微调 | PSNR、SSIM、LPIPS、FID；表 5 输入数量另含 DISTS；表 7 时序设计另用 MEt3R | [全文](https://arxiv.org/html/2608.28895v1)；[作者页](https://visinf.github.io/reconsplat/) |

上述表格只描述所列原文实验，不比较跨论文绝对分数。各论文的数据、分辨率、采样、监督、输出阶段可能不同。尤其生成式方法的最终图像可能经过二维扩散细化，不能自动视为原始高斯渲染结果。

### 可归纳的做法

1. **模块消融沿用最终任务指标。** 通常逐项移除模块、替换为合理简化实现或移除损失，以 PSNR/SSIM/LPIPS 或 PSNR/SSIM 验证它对最终渲染的贡献。没有必要为每个模块另造一个主指标。
2. **评价区域与评价指标分开。** 驾驶任务常将同一指标分别用于全图和动态区域；这能防止大面积背景淹没车辆等目标的变化。区域掩码需要对变体一致。未见区域也可单列，但其可见性定义仍然是任务协议，换成 PSNR 不会自动成为统一基准。
3. **几何或运动机制增加相应标准指标。** 深度使用 AbsRel、δ₁ 或 D-RMSE；真实预测 scene flow 的工作可以报告 EPE3D、Acc₅。DriveCompose 的外部给定资产状态不等于模型估计 scene flow，不应为了通用而添加不对应输出的运动指标。
4. **输入数量和模块消融分开解释。** 固定 checkpoint 改变输入数是敏感性/适应性实验；改变训练架构通常需要重训。STORM 明确区分两种设置。训练预算、数据曝光、测试场景、checkpoint 选择规则要对齐，不能假定被检索论文全部采用完全相同的最优实践。
5. **生成质量与配对重建互补。** ReconSplat 表 6 在重建指标之外报告 FID；PointForward 的真实离轨实验用 FID。有配对参考的外推可报告 PSNR/SSIM/LPIPS，无配对参考的离轨不能与原相机图像算这些分数。FID 本身不证明场景条件正确或几何完整。

### 当前稿件的具体问题

依据 `paper/zh/4_experiments_zh.tex` 消融小节及英文对应段落：

| 当前项 | 判断 | 建议去向 |
| --- | --- | --- |
| NVS-MAE | MAE 是通用误差，但本轮核验的前馈 RGB 消融更常用 PSNR/SSIM/LPIPS | 主表改用三项常用图像指标，从原始预测和真值重新计算 |
| New-MAE | MAE 本身通用；“所有输入不可见表面”的定义及共同掩码是本文专门协议 | 有独立参考和可靠可见性时，作为未见区域补充分析；可报该区域 PSNR，明确其仍是区域化协议 |
| Obs-Reg | 本文逐像素截断增量定义，适合观测保持诊断 | 主文如需展示观测保持，可像 DGGT 一样另报输入视图重建质量；原增量分析留补充材料 |
| Cov. | 支撑度、不透明度及正深度多阈值定义，不能等同几何覆盖率或完整度 | 保留为实现诊断；不充当重建质量的主证据 |
| Pass | 依赖本方法检查器及多种接受阈值，不能独立代表最终图像或几何质量 | 放运行/失败记录；主表质量使用筛选前输出并明确失败数量 |

未从这次有限检索推断“这些名称在所有论文中从未出现”。例如 Instant NuRec 的 LiDAR 表 3 也有 `Cov.`，方向和定义都与本文像素覆盖比例不同，名称相同不构成协议相同。

### 对 DriveCompose 的建议结构（待执行，不代表已有新结果）

- **组件主表：** 保留 `w/o GCM`、`w/o CCM`、`Ours` 三行；优先列 `Full-image PSNR↑ / SSIM↑ / LPIPS↓`，再加 `Dynamic PSNR↑ / SSIM↑`。更紧凑的版本可沿当前主结果只报全图/动态 PSNR、SSIM，但本文包含生成补全，建议保留全图 LPIPS。
- **输入数量表：** 保留 T=2/4/8、每档 Ours 与 w/o CCM，列同一套 PSNR/SSIM/LPIPS。三路相机对应 6/12/24 张图；保持目标集合和时间跨度一致，固定 checkpoint，标注为输入敏感性。
- **几何补充表：** 若主张涉及补全几何，沿当前主结果报 AbsRel、δ₁，有需要再加米制 D-RMSE。尺度对齐后的深度指标不能独自支持绝对尺度正确的主张。
- **生成补全证据：** 在留出且有配对 GT 的外推视图报告 PSNR/SSIM/LPIPS；在无配对 GT 的真实离轨设置保留单独的 FID 实验。若继续采用现稿已有 FVD，需冻结视频长度、帧率、参考集及样本数，并明确它不是本轮多数前馈组件消融的必选指标。标准图像指标与定性遮挡恢复样例共同说明 GCM 的作用。
- **已见保持与未见细节：** 若需要，单列输入视图重建质量，以及可靠参考下未见区域的 PSNR/深度误差。动态/未见区域 SSIM 和 LPIPS 必须说明窗口、裁剪或特征图聚合办法，不能简单置黑背景后当作普通区域指标。

主实验当前采用 20 帧窗口和固定四个输入时刻，消融采用 29 时间戳与 T=2/4/8。建议组件主表尽量复用主实验协议；如另保留完整参考补全测试集，需明确为独立实验，不将其数值和 Waymo 主表直接比较。输入敏感性可以继续采用独立固定窗口，但应解释目标集合。

更换指标需要原始预测/GT 或可重跑 checkpoint。现有 MAE 汇总无法唯一换算 PSNR，不能通过改表头复用数值；SSIM/LPIPS 同样需实际计算。原始汇总及来源记录保留。涉及重新训练的完整协议后续由实验设计流程接手，本轮仅给出文献支持的改版建议。

### 访问边界

- pixelSplat 与 DGGT 的 CVF PDF 直接打开返回 HTTP 403。pixelSplat 会议表 2 可由搜索返回的原始 PDF 索引读取，并用 arXiv v2 核对对应机制；DGGT 消融细节明确依据可读 arXiv v1，会议条目仅核验发表身份，未宣称逐项核过会议终版。
- latentSplat 的作者站访问超时，且第三方检索所给 arXiv:2403.14774 实际对应另一篇论文，已排除该错误入口，没有将其作为原文证据。相关生成式比较由已读 ReconSplat 原文承担。
- 本轮已核对表格/段落，不是官方评测代码的逐行实现审计；没有生成新的实验结果、改动既有 claim ledger 或推断新增指标优劣。


## 2026-10-29：统一生成式重建架构与模块选型调研（待作者确认）

### 任务与边界

本轮问题是网络主干如何统一重建与生成，以及 ViT、DiT、三维表示和高斯解码器怎样形成可训练的接口。用户已明确：允许少步去噪，不做逐场景优化；暂不以算力和时间预算约束选型。沿用多相机驾驶日志、背景/刚体/人体可组合高斯世界的项目目标。本节是研究建议，没有改变当前架构、代码、稿件或实验协议。

主技能为 nature-academic-search。核验日期为 2026-10-29（Asia/Shanghai）；检索与阅读来自论文全文、作者官方说明及官方 GitHub 源码。没有运行这些外部模型，没有核验论文报告分数，也不以跨论文分数直接排名。

### 核心判断：区分三种表示角色

1. **观测条件 C**：来自 ViT 或三维视觉编码器的干净特征。通过归一化、可学习投影、空间条件和注意力接入 DiT，不要求服从标准高斯分布。
2. **生成变量 Z_tau**：接受噪声扰动并沿采样轨迹更新的对象。必须定义清楚训练目标 Z_0、噪声过程、尺度及输出参数化。它可以是图像、可解码三维特征或高斯参数，不能只写成含义不明的“场景 token”。
3. **高斯读出 D(Z_0)**：将采样结果转换为可渲染世界。只有 D 与 Z 的语义、坐标和分布共同训练匹配，输出才成立。

因此，“DiT 不能使用 ViT 特征”需要区分：ViT 特征可以作为条件；它不能未经适配就替换预训练视频模型的 VAE 生成变量。维度投影解决张量接口，不自动解决空间关系、预训练分布或三维可解码性。

现有六段链路不因模块多就必然冗余。建议改变的是推理分工：观测编码器形成条件，生成器直接推断整体场景表示，解码器统一输出可组合世界。更充分观测对应更强的重建约束，稀疏观测对应更多先验推断；不必先交付一份被锁定的重建结果再调用修补器。

### 代表性机制证据

| ID | 原始材料与核验范围 | 已核实的接口事实 | 对选型的作用 |
| --- | --- | --- | --- |
| ARC01 | [Atlas 官方技术介绍](https://www.worldlabs.ai/blog/atlas)，Model Architecture / Explicit 3D Outputs | 多模态自回归扩散 Transformer，使用空间上下文；介绍包含 RGB/深度与显式三维输出转换 | 用来确定统一空间建模方向；该介绍不能证明“普通 ViT 一次接 DiT 就直接出高斯” |
| ARC02 | [TRELLIS 官方 pipeline](https://github.com/microsoft/TRELLIS/blob/193e0502b5cb3eb5997ec457d5340e95d09b158e/trellis/pipelines/trellis_image_to_3d.py)、[稀疏交叉注意力块](https://github.com/microsoft/TRELLIS/blob/193e0502b5cb3eb5997ec457d5340e95d09b158e/trellis/modules/sparse/transformer/modulated.py) | DINO 特征经归一化成为 cond，稀疏噪声潜码 x 单独进入流模型，通过 cross-attention 接收 cond | 直接证实条件特征和生成变量不需要是同一种表示 |
| ARC03 | [RAE 原文](https://arxiv.org/html/2510.11690v1)，§4–6 | 表征编码器特征可以成为扩散数据空间，但需适配高维去噪及解码鲁棒性 | 不能把高维特征简单压到旧视频潜空间后，假定原先先验仍有效；这是图像领域证据 |
| ARC04 | [Gen3R 原文](https://arxiv.org/html/2601.04090v1)，§3.1–3.3 | 用训练过的几何适配器连接 VGGT 特征与视频潜空间，再共同生成几何和外观 | 是“接口需要学习”的直接例子；保留视频 latent 和多个解码任务，不是最精简的资产世界主干 |
| ARC05 | [OneWorld 原文](https://arxiv.org/html/2603.16099v1)，§3；[官方仓库](https://github.com/SensenGao/OneWorld/tree/ebd6f316ce8fe1da74650a9a5d5738e2ec85994a) | 在兼顾几何和外观的三维特征空间生成，并训练解码器适应采样特征；公开实现已有适配主干和四步推理 | 最适合作为本轮首选架构参考；它仍是以视图组织的表示，并未直接提供驾驶资产的规范解耦 |
| ARC06 | [Free-Range Gaussians 原文](https://arxiv.org/html/2604.04874v1)，§3.1–3.6 | DINOv2-B 特征、RGB和射线经投影后与噪声高斯 token 共同处理，直接生成高斯参数 | 原生高斯路线证明可以取消三维 codec；原文用对象级三维高斯训练目标，50步且包含渲染梯度引导，不能直接作为本任务少步纯前馈成品 |
| ARC07 | [PixWorld 原文](https://arxiv.org/html/2607.05373v1)，§3 / 附录 B、E；[官方 README](https://github.com/SensenGao/PixWorld/blob/c967d20307bd5b41d3b9234b8db42d67b4f28134/README.md) | 原文将干净/带噪视图共同输入双流主干，在渲染图像上定义生成监督；公开版另以 Wan2.2 改造并提供四步权重 | 无三维潜码路线的强对照；公开版不是原文从头训练模型，官方明确不能继承论文数值 |
| ARC08 | [TokenGS 原文](https://arxiv.org/html/2604.15239v1)，§3.2；[官方 2026.6 更新](https://github.com/nv-tlabs/TokenGS/blob/main/release_2026.6.md) | 可学习高斯查询读取图像/场景特征；更新版提供固定场景 latent bottleneck | 高斯查询解码的实现起点；这些 latent 未被该发布自动证明适合扩散，模型本身也不是生成器 |
| ARC09 | [Can3Tok 原文](https://arxiv.org/html/2508.01464v1)，§3 / §4.6 / 附录9 | 编码三维高斯集合为结构化潜码，强调尺度处理；其图像到三维演示使用潜码回归 | 可借鉴场景三维 tokenizer；不能把其图像分支说成已验证的图像条件 DiT |
| ARC10 | [PRoPE 作者页](https://www.liruilong.cn/prope/)、[论文](https://arxiv.org/abs/2507.10496) | 相机内外参可作为注意力级相对位置条件 | 多相机对齐应保留几何信息，不能只平均图像特征或使用一个全局向量 |
| ARC11 | [DINOv3 官方说明](https://ai.meta.com/blog/dinov3-self-supervised-vision-model/)、[官方模型入口](https://github.com/facebookresearch/dinov3) | 提供稠密视觉特征与预训练骨干 | 是编码器升级候选；没有本轮证据证明直接替换已适配 DINOv2 后的整个生成链会提高质量 |
| ARC12 | [OmniRe 作者页](https://ziyc.github.io/omnire/)、[gsplat 文档](https://docs.gsplat.studio/main/apis/rasterization.html) | 前者提供多类规范资产运动表示参考，后者提供可微高斯渲染接口 | 对应资产输出契约与训练渲染，不作为额外的在线重建优化器 |

### 首选架构：统一三维表示空间中的条件生成

建议采用 OneWorld 类三维表示路线，并为 DriveCompose 设计资产读出：

```text
观测图像 + 标定 + 时间
        ↓
统一视觉/空间编码器
（预训练 ViT + 多视图几何交互 + RGB 外观保留）
        ↓
干净观测条件 C ──────────────────┐
                                ↓
噪声三维表示 Z_tau ──→ 适配过的条件 DiT ──→ 完整场景表示 Z_hat
                                                ↓
                                  类型化高斯查询解码器
                                                ↓
                               背景 / 规范刚体 / 绑定人体
```

推理时不先运行显式的逐点查询构造、硬观测聚合和单独潜码重编码。跨视角交互融入空间编码器；三维表示本身由训练确定，DiT 直接预测它。高斯查询放在末端，承担从场景特征读出三维基元的职责。

这仍有编码、生成、解码三种计算职责，并不通过改名消除它们。统一性体现在同一条件生成模型共同解释已见和未见内容，同一场景表示支持高斯输出，而不是依次交付“重建世界”和“补全世界”。

**训练侧必须补上的接口：**

- 使用同一个、经过三维渲染训练的编码器/解码器定义目标表示。完整或更充分的训练观测用于目标编码；推理可用观测单独用于条件编码，禁止把目标图像通过全局上下文泄漏到条件。
- 场景编码目标属于训练数据路径；推理无需先得到“完整目标潜码”。但观测条件本身仍须编码，不能据此声称取消所有三维编码。
- 学习潜码统计量，明确 token 布局、坐标、身份与尺度。让解码器同时接触编码得到的潜码和生成器实际采样得到的潜码，降低分布失配。
- 原模型的视图特征并不天然等于可编辑的规范资产。身份关联、规范内容与运动状态解耦需要新的监督和结构设计，这是 DriveCompose 改造的关键研究部分。

### 每个模块的选型建议

| 模块 | 建议首选 | 为什么适合当前任务 | 备选与限制 |
| --- | --- | --- | --- |
| 图像 ViT | 首个整链原型沿用 Pi3X 配套的 DINOv2 ViT-L/14-reg | 与空间主干和已适配权重的特征基匹配；不额外挂第二个 ViT | DINOv3 ViT-L/16 作为同协议替换实验，需重新适配 patch 网格、空间主干与生成分布 |
| 多视图空间编码 | Pi3X 风格几何交互 + OneWorld 外观分支 | 图像具备相机标定；保留几何和细节，比只有语义 ViT 特征更接近可解码的三维表示 | VGGT 可作几何对照；完整静态几何模型不能未经改造直接承担动态驾驶日志的规范资产恢复 |
| 相机/时间条件 | 使用配套相机注入；新增部分采用射线与相对位姿条件，PRoPE 作对照 | 输入相机之间的关系是可组合重建的重要约束 | 不将新 PRoPE 编码直接替换已训练 checkpoint 的接口而不再训练；时间/运动条件是本项目扩展 |
| ViT/空间特征—DiT 接口 | 干净条件与带噪目标分离；通道归一化/数据统计 + 学习投影 + 相机条件 | 同时解决数值尺度与条件注入，保持条件/目标角色清楚 | 单个 Linear 只负责宽度，不足以证明预训练视频分布兼容；不先全局平均丢掉局部条件 |
| DiT | 以 OneWorld 已适配的 WanPi3Flow 为基座，借鉴其高维 x0 预测和宽输出头 | 已有从三维特征到生成主干的具体适配路径 | 不能换成未经三维适配的原版 Wan/SD3 权重；改变生成 token 的布局和语义后须重新训练/适配 |
| 三维生成表示 | 保留可解码的几何—外观联合特征；先沿用基座表示，再验证资产结构化版本 | 相比直接扩散所有高斯参数，避免首先依赖大量规范三维高斯真值，并能复用三维视觉先验 | TokenGS latent bottleneck、Can3Tok、TRELLIS SLAT 是不同表示，不可按相同维数直接互换 |
| 高斯解码 | TokenGS 式 query decoder 作为可组合改造起点；按背景、刚体、人体分别读出 | 高斯数量不必随图像数增长，输出可处于世界/规范坐标，符合资产重用目标 | 从 OneWorld 特征到该查询解码器需要重新训练；不能把两个模型的解码器权重直接拼接 |
| 人体/刚体运动 | 保留刚体 SE(3) 与人体模板绑定的输出契约 | 身份内容和运动可独立控制；不强迫 DiT 预测物理下一状态 | OmniRe 是表示参考，不将其逐场景拟合流程放进推理主链；人体模板拓扑仍要统一 |
| 渲染 | gsplat | 训练期建立 RGB/深度/轮廓约束，推理期生成观测 | 深度类型、坐标和遮挡口径需统一；渲染器不是三维真实性证明 |
| 少步推理 | 先验证普通条件生成，再做 4/8/16 步质量—代价比较或蒸馏 | 减少步数必须靠训练/蒸馏与实测，不靠直接缩短采样循环 | OneWorld/PixWorld 已有四步发布可作参考；不能把其步数或质量直接迁移到改造后的 DriveCompose |

这张表区分了**第一整链原型可复用的配套基座**和**DriveCompose 必须训练的结构改造**。首选不是把各论文最好看的模块和权重直接拼起来。若保留当前可组合目标，公开模型中尚未在本轮核验到“多相机驾驶日志 → 少步生成 → 背景、刚体、人体规范资产”完整现成链路。

### 公开实现核验中影响判断的细节

**OneWorld：**
- 本轮读取官方提交 `ebd6f316ce8fe1da74650a9a5d5738e2ec85994a`（2026-10-20），晚于部分网页索引仍显示“待发布”的状态。
- [rae/model.py](https://github.com/SensenGao/OneWorld/blob/ebd6f316ce8fe1da74650a9a5d5738e2ec85994a/oneworld/rae/model.py) 定义几何 1024 通道与外观 32 通道的联合表示；[wan_flow.py](https://github.com/SensenGao/OneWorld/blob/ebd6f316ce8fe1da74650a9a5d5738e2ec85994a/oneworld/rae/wan_flow.py) 使用独立输入映射、相机条件和高维输出头。因此它不是原版 Wan 直接消费 ViT 特征。
- [infer.py](https://github.com/SensenGao/OneWorld/blob/ebd6f316ce8fe1da74650a9a5d5738e2ec85994a/infer/infer.py) 的发布入口固定八个相机视图，四步采样的中间步有“解码—渲染—重新编码”反馈，相关函数在 inference_mode 下运行，没有基于场景损失的反向优化。
- 所以该发布满足“不做逐场景优化”，但其运行量不等于四次 DiT 加一次末端解码。若目标要求每次构建只解码一次，需设计新的蒸馏/采样方案，不能直接删掉反馈后沿用其质量结论。
- 本轮没有下载或运行权重。Hugging Face 模型页通过网页工具读取失败；权重发布状态依据官方仓库说明，不能写成已经实测可运行。

**PixWorld：**
- 本轮读取官方提交 `c967d20307bd5b41d3b9234b8db42d67b4f28134`。README 明确发布版是 Wan2.2-TI2V-5B 改造，论文数值不描述该版本。
- [infer/diffusion/dmd_sampling.py](https://github.com/SensenGao/PixWorld/blob/c967d20307bd5b41d3b9234b8db42d67b4f28134/infer/diffusion/dmd_sampling.py) 默认四步过程由三个多视图步骤和末端三维步骤组成；[gs_lift.py](https://github.com/SensenGao/PixWorld/blob/c967d20307bd5b41d3b9234b8db42d67b4f28134/infer/models/gs_lift.py) 含独立高斯读出分支。不能把“无 VAE”解读为“没有任何特征编码/解码模块”。

**TokenGS / Pi3X：**
- 官方 TokenGS 更新页有带/不带 test-time tuning 的不同结果；本任务只采用不调优的推理方式。本轮核对了 `tokengs/models/enc_dec.py` 中的查询自注意力/交叉注意力与 latent bottleneck；它不等于已训练的生成先验。
- 官方 Pi3X 的 `pi3/models/pi3x.py` 使用 `dinov2_vitl14_reg`，支持相机相关条件；与输出特征配套使用，不默认另接 DINOv3。
- 这两个仓库的文件已读取；后续读取最新 commit 接口时发生传输错误，因此本节对它们使用访问日期和文件路径，不虚构固定 SHA。

### 两条备选路线的取舍

| 路线 | 优点 | 当前不作为首选的原因 | 何时转向 |
| --- | --- | --- | --- |
| 原生高斯去噪，参考 Free-Range Gaussians | 取消独立三维 codec，生成变量与最终三维参数直接对应 | 大场景规模、规范资产目标构建和异质参数分布需要解决；原文对象实验含推理梯度引导 | 已有高质量、足量且坐标一致的场景/资产高斯训练库，并验证去掉梯度引导后仍保持观测 |
| 像素空间生成，参考 PixWorld | 以真实图像直接定义生成监督；不需要预先训练三维 latent encoder | 现成输出仍按视图/像素组织，独立资产身份和规范空间需新增设计；需要选择生成视图布局 | 目标优先是整体场景 NVS/生成，资产独立编辑可后置；用作无三维 codec 的强对照 |

### 最小验证：决定是否接受该架构

以下是待批准后执行的判断实验，不是本轮已完成结果。

1. **先验与读出上限**：只训练/核验统一表示到高斯的重建路径。它若不能保留输入细节和规范资产身份，先修表示与解码，不把问题交给 DiT。
2. **接口对照**：在同一生成目标与同一解码器下比较普通 ViT 条件、空间/外观联合条件、额外潜压缩条件；保持图像输入、训练曝光与预算可比。
3. **生成与重建共存**：比较输入视图和留出视图的 PSNR/SSIM/LPIPS、动态区域与几何误差；稀疏输入时还检查多个采样的可见区域稳定性和未见区域合理性。
4. **可组合性**：固定一次输出改变资产状态，检查内容身份、残留背景影像、遮挡、人体绑定和新视角质量。普通 NVS 得分不能替代这一验证。
5. **推理合同**：逐项统计 DiT 次数、编码/解码/渲染次数、运行时间和显存，确认没有测试场景反向优化。4/8/16 步必须和质量一起报告。
6. **决策规则**：只有联合编码对可见重建与未见预测有可重复收益，且资产解耦成立，才采用主方案。若三维 latent 的重建上限成为瓶颈，转向像素空间对照；若已具备优质三维目标且 codec 明显损失细节，优先验证原生高斯路线。数值阈值在实际基线与评价协议固定后预注册，不填造阈值或结果。

### 检索记录与交接

主要查询：Atlas unified reconstruction generation；ViT DiT conditioning DINO/TRELLIS；Diffusion Transformers with Representation Autoencoders；Gen3R / OneWorld / PixWorld architecture；Free-Range Gaussians conditioning and inference；TokenGS latent bottleneck and decoder；PRoPE camera conditioning；DINOv3 official backbone；Pi3X optional camera conditions；gsplat rasterization。

纳入依据：能定位条件接口、生成变量、解码器、训练监督或推理限制；重复的项目页/论文/仓库合并记录。普通视频生成性能榜、第三方解读和二手摘要不用于关键技术判断。该集合是针对本次架构决策的代表性检索，不是系统综述或新颖性证明。

交接结论：**优先研究“几何—外观联合三维编码 + 适配后的条件 DiT + 可组合高斯查询读出”，以 OneWorld 的配套编码/生成适配为原型参考，以 TokenGS 的查询读出为资产化改造参考。** 新资产布局、动态运动条件、读出解码和少步采样需要联合适配；现有实验结果不能直接继承到新链路。等待作者确认后再更新正式架构与实现。
