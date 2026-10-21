# 引用核验记录

当前更新（2026-10-21）：已接入用户提供的 75 条文献，与原书目去重后共 84 条。75 条均在中英文正文中引用，来源与逐条使用位置见 [接入记录](provenance/reference-integration-20261021.md) 和 [机器可读清单](provenance/reference-integration-20261021.json)。正式 ICLR 来源修正了 STORM 的作者顺序，并将 Flow Matching 更新为 ICLR 2023；下方保留前期核验记录，不再代表这两项的最新版本。

日期：2026-10-20，Asia/Shanghai。工作流：citation-verification。复用项目已有近邻记录，本轮只核验改稿所用条目，不开展新的全面文献综述。

采用作者项目页、arXiv 记录和会议原文。下表的“已核验”指题名、作者、年份及所写的机制概述得到相应来源支持，不表示对原论文全部实验、代码或优劣结论完成审计。完整精确比较仍以项目近邻记录中的剩余核验项为准。

| 引用键 | 书目与状态 | 原始来源 / 实际读取范围 |
| --- | --- | --- |
| `yan2024street` | Street Gaussians，ECCV 2024，已核验 | [作者项目页](https://zju3dv.github.io/street_gaussians/)，题名、作者、表示概述与书目 |
| `chen2025omnire` | OmniRe，ICLR 2025，已核验 | [作者项目页](https://ziyc.github.io/omnire/)、[arXiv v2](https://arxiv.org/abs/2408.16760v2)，作者、会议状态与规范资产概述 |
| `zhou2024hugsim` | HUGSIM，arXiv 2024，已核验该预印本 | [arXiv](https://arxiv.org/abs/2412.01718)，作者、日期与闭环状态更新摘要；不外推其他出版状态 |
| `yang2025storm` | STORM，ICLR 2025，已核验 | [会议 PDF](https://openreview.net/pdf?id=M2NFWRPMUd)、[arXiv](https://arxiv.org/abs/2501.00602)，首屏作者顺序、会议标记与摘要 |
| `chen2025dggt` | DGGT，CVPR 2026，已核验 | [会议 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.pdf)、[作者项目页](https://xiaomi-research.github.io/dggt/)，题名、作者顺序与摘要；保留旧引用键 |
| `yu2026streetforward` | StreetForward，arXiv 2026，已核验 | [arXiv](https://arxiv.org/abs/2603.19552)，书目与前馈时序重建摘要 |
| `chi2026pointforward` | PointForward，arXiv 2026，已核验 | [arXiv](https://arxiv.org/abs/2605.11594)，书目与点对齐/对象接口摘要；本轮没有重新验证被冻结实验中的每个数值 |
| `huang2026instantnurec` | Instant NuRec，arXiv 2026，已核验 | [arXiv](https://arxiv.org/abs/2607.14203)，作者列表与题名；将旧条目的单独机构作者补为具体作者，保留 NVIDIA 来源信息于此 |
| `streetcrafter` | StreetCrafter，CVPR 2025，已核验 | [作者项目页及 BibTeX](https://zju3dv.github.io/street_crafter/)，作者、会议年份、LiDAR 条件和生成视图监督路径 |
| `wang2026horizonforge` | HorizonForge，CVPR 2026，已核验作者声明 | [arXiv v2](https://arxiv.org/abs/2602.21333v2)、[作者项目页](https://horizonforge.github.io/)，作者与 Gaussian–mesh/video diffusion 摘要；CVF HTML 返回 403，会议状态据 arXiv 的 Accepted by CVPR 2026 声明 |
| `zhu2025worldsplat` | WorldSplat，arXiv 2025，已核验该版本 | [arXiv v2](https://arxiv.org/abs/2509.23402v2)，作者、日期、Gaussian 生成与视频精修摘要；补齐原工程缺失的键，不在本条目假定会议状态 |
| `yang2025genassets` | GenAssets，CVPR 2025，已核验 | [会议 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_GenAssets_Generating_in-the-wild_3D_Assets_in_Latent_Space_CVPR_2025_paper.pdf)、[作者机构页](https://waabi.ai/research/genassets)，作者、年份、潜空间资产生成摘要；2026 年 arXiv 上线不另计一篇 |
| `liao2025complete` | Complete Gaussian Splats，arXiv 2025，已核验 | [作者项目页及 BibTeX](https://nianticspatial.github.io/completesplat/)、[arXiv](https://arxiv.org/abs/2508.21542)，书目与单图潜空间补全机制概述 |
| `wu2026jrm` | JRM，arXiv 2026，已核验该版本 | [arXiv](https://arxiv.org/abs/2603.25985)，书目与多份未对齐观测潜空间聚合摘要 |
| `park2026latentworld` | Grounded Latents，CVPR 2026，已核验作者资料 | [作者项目页及 BibTeX](https://jindapark.github.io/projects/latentworld/)，书目与语义占据/实体中心表示概述 |
| `lipman2022flowmatching` | Flow Matching for Generative Modeling，arXiv 2022，已核验该版本 | [arXiv v2](https://arxiv.org/abs/2210.02747v2)，作者、初始年份与速度场回归摘要；条目明确引用预印本版本 |

活动书目共 16 条：16 条书目核验，0 个未解析引用键。旧 `main.bib` 中未使用、不完整或同文不同键的条目从活动集合移除，完整原文保留在项目外归档的 [MOSAIC 原始压缩包](../../_archive/drivecompose/20261020-cleanup/files/paper/archive/MOSAIC-original.zip)。这不代表对原 40 条全部完成核验。

检索式包括 STORM / DGGT / Instant NuRec / StreetForward 的完整题名，以及 GenAssets、Complete Gaussian Splats、Grounded Latents、Flow Matching 的完整题名。工具为现有网页搜索与原始页面读取；未使用聚合解读作为技术论断来源。OpenReview 的一个 Flow Matching 页面出现浏览器校验，改用 arXiv 原始记录。

模板来源另核对 [cvpr-org/author-kit](https://github.com/cvpr-org/author-kit) 和其 [main.tex](https://raw.githubusercontent.com/cvpr-org/author-kit/main/main.tex)：访问时主文件仍标记 2026，故本轮只统一目标年份，不宣称已采用官方 2027 最终模板。

## 2026-10-21 新增基础来源

- `kerbl2023gaussians`：Kerbl, Kopanas, Leimkühler, Drettakis. 3D Gaussian Splatting for Real-Time Radiance Field Rendering. ACM TOG 42(4), 2023。作者页及其 BibTeX 核验，支持高斯表示与泼溅基础来源。https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/
- `peebles2023dit`：William Peebles, Saining Xie. Scalable Diffusion Models with Transformers. ICCV 2023。作者项目页确认题名、作者与 ICCV 2023 Oral；CVF 直接页面访问 403，改用作者页。支持 DiT 风格生成骨干的来源，不表示本文复制其全部结构或训练协议。https://www.wpeebles.com/DiT

访问日期 2026-10-21。DGGT 作为写作与图形语言参考使用 arXiv:2512.03004v1，详细读取范围与本地 PDF 哈希见本轮改写记录。
