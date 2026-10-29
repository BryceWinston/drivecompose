# 当前论文 PDF

**2026-10-29 最新：三张方法图已插入并完成排版检查。** 两版图1、图2、图3分别位于第2、3、5页；原实验图顺延为图4、图5。63项稿件检查通过。

- [英文当前版](en/main.pdf)：12页；正文与图表止于第9页，参考文献从第9页下部开始。**尚超过CVPR正文8页限制。**
- [中文当前版](zh/main_zh.pdf)：10页；正文止于第8页，参考文献从第8页开始。
- [本轮排版核验](../provenance/three-figure-layout-verification-20261029.json)。
- [实际改动与原因](../../docs/paper-revision-changes.md)。

正文、图注、表格、公式及引用已检查；实验数值未改。两份既有补充材料各3页，已作全页视觉检查，未重新改写。

## 上一轮输出记录（不代表当前页数）


**2026-10-29 当前交付：** 中英文两张消融表已填入作者提供的通用指标结果，每种语言 33 个数值；同步组件与输入数量分析，并按列或同一 T 分组标粗最优值。

- [英文当前版](en/main.pdf)：11 页；两张消融表在第 7、8 页，正文止于第 8 页，参考文献从第 8 页开始。
- [中文当前版](zh/main_zh.pdf)：9 页；两张消融表在第 6、7 页，正文止于第 7 页，参考文献从第 7 页开始。
- [本轮核验](../provenance/ablation-standard-metrics-verification-20261029.json)：54 项现有稿件检查通过，逐格数值、T=8 跨表一致性、双语与修改范围均已核对；英文第 6–8 页、中文第 6–7 页已作视觉检查。
- [前后对照与理由](../../docs/paper-revision-changes.md#2026-10-29回填两组通用指标消融结果)。

本轮仅重新构建中英文主稿；数值来源为作者汇总结果，未独立核验原始运行材料，也未执行训练或评测。其他章节与补充材料保持本轮起点原文。

## 历史记录（以下不作为当前结果状态）

**2026-10-29 当前输出：** 规范空间聚合、潜表示、解码及场景组合统一使用刚体（rigid）分支术语。四份正式 PDF 已重新编译；英文正文仍止于第 8 页，References 从第 9 页开始。52 项稿件检查通过。见 [本轮核验](../provenance/rigid-terminology-20261029.json)。

2026-10-28 最新总览图：按用户要求改为内置 Image Gen 生成的完整 PNG；旧矢量图已停用。输入遮挡、对应资产、场景组合与中央流向经过独立复查。双语论文均直接引用 PNG，见 [当前总览说明](../../docs/figures/overview/README.md)。

2026-10-28 总览图更新：Figure 1 改为矢量 PDF，配套 SVG 与 PNG；输入采用用户提供全景的三个相邻视图，刚体示意采用完整邮政车，末端展示闭环仿真用途。两版图位于第 2 页；英文正文仍止于第 8 页，参考文献从第 9 页开始。图件及解码命名本轮核验见 [记录](../provenance/overview-expansion-20261028.json)。

**当前版本（本段优先于下方历史记录）：** 2026-10-29：中英文消融仅保留组件与输入数量两张表。组件表采用全图 PSNR/SSIM/LPIPS 和动态区域 PSNR/SSIM，输入数量表采用全图 PSNR/SSIM/LPIPS；新指标数值全部留空。旧自定义指标及依赖其结果的摘要、引言和结论表述已删除。当前合同为 paper/provenance/ablation-standard-metrics-20261029.json；历史结果保留溯源。

2026-10-26 推送整合：保留远端 `1e2dd79` 的新标题、双语引言及补充材料，同步本次总览图与图注后重新编译主稿。英文共 11 页，正文与结论在第 9 页结束，References 也从第 9 页开始，尚未满足 8 页正文目标；远端合并前 PDF 的正文也结束于第 9 页。中文共 9 页。图件均在第 2 页；52 项稿件检查通过。以下记录中的“正文 8 页”描述此前版本，当前以本段和[最终核验](overview-replacement-check.json)为准。

2026-10-26：中英文 Figure 1 最终采用用户明确指定的 `repair-attempt.png`（原图已归档），按字节原样替换；双语图注已作局部语言清理，并按用户截图要求删除与流程无关的尾句；方法开头保持不变。两版编译成功；英文 11 页，正文与结论止于第 8 页、References 从第 9 页开始；中文 9 页。两版图件均在第 2 页。52 项结构检查通过，内嵌图像与确认图像像素一致，见[本轮核验记录](overview-replacement-check.json)。以下消融记录为此前已完成工作，本轮未修改实验。

中英文已写入用户于 2026-10-23 提供的组件消融及输入数量敏感性结果，两张表共 29 个数值及 1 个未报告指标，组件消融保留 Ours、w/o GCM、w/o CCM，取消 A+数字编号，并同步结果分析。三路相机、24 步补全和 [0,1] 线性 RGB 尺度已明确；消融定性图（原图 3）及其引用已删除。

- [英文当前版](en/main.pdf)
- [中文当前版](zh/main_zh.pdf)
- [表格预览（已归档）](../../../_archive/drivecompose/20261026-tracked-intermediates/paper/build/ablation-tables-preview.png)

当前编译状态以各语言目录的 `compile-result.json` 为准；逐格数值、T=8 跨表一致性及双语检查见 [核验记录](verification.json)，数据来源见 [消融结果记录](../provenance/ablation-results-20261023.json)。`ablation-framework-check.json` 是 2026-10-21 空表阶段的历史检查，现已移入项目外归档。修改前稿件、PDF 和本轮临时检查文件存入项目外 `pre-research/_archive/drivecompose/20261023-ablation-results/`。

2026-10-23 按用户要求移除无世界坐标和软观测对照。此次修改前的稿件、PDF 与检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-ablation-simplification/。

2026-10-23 表格重排：两表采用单行表头与统一栏宽；输入敏感性按 T 分组。w/o GCM 的 Obs-Reg 改为横线，不纳入最优值比较。此次修改前文件与检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-ablation-table-design/。

2026-10-23 删除图 3：中英文同步移除消融与复用占位图及正文引用，表格保持不变。修改前版本与本轮检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-remove-figure3/。

2026-10-26：本轮候选、临时编译文件、页面预览和修改前备份已移至[项目外归档](../../../_archive/drivecompose/20261026-overview-intermediates)。正式 PDF、编译结果与最终核验记录保留；移动前后正式 PDF、活动图片和论文源码哈希一致。

2026-10-26：进一步移出 30 个此前已提交的过程文件，包括历史图件和未采用草稿、表格预览、修订差异页与基线、四份编译文本日志；见[归档清单](../../../_archive/drivecompose/20261026-tracked-intermediates/archive-manifest.json)。四份正式 PDF 和各自的 `compile-result.json` 保留。
