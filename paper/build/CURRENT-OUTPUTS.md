# 当前论文 PDF

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
