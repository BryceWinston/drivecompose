# 当前论文 PDF

中英文已写入用户于 2026-10-23 提供的组件消融及输入数量敏感性结果，两张表共 29 个数值及 1 个未报告指标，组件消融保留 Ours、w/o GCM、w/o CCM，取消 A+数字编号，并同步结果分析。三路相机、24 步补全和 [0,1] 线性 RGB 尺度已明确；消融定性图（原图 3）及其引用已删除。

- [英文当前版](en/main.pdf)
- [中文当前版](zh/main_zh.pdf)
- [表格当前预览](ablation-tables-preview.png)

当前编译状态以各语言目录的 `compile-result.json` 为准；逐格数值、T=8 跨表一致性及双语检查见 [核验记录](verification.json)，数据来源见 [消融结果记录](../provenance/ablation-results-20261023.json)。`ablation-framework-check.json` 是 2026-10-21 空表阶段的历史检查。修改前稿件、PDF 和本轮临时检查文件存入项目外 `pre-research/_archive/drivecompose/20261023-ablation-results/`。

2026-10-23 按用户要求移除无世界坐标和软观测对照。此次修改前的稿件、PDF 与检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-ablation-simplification/。

2026-10-23 表格重排：两表采用单行表头与统一栏宽；输入敏感性按 T 分组。w/o GCM 的 Obs-Reg 改为横线，不纳入最优值比较。此次修改前文件与检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-ablation-table-design/。

2026-10-23 删除图 3：中英文同步移除消融与复用占位图及正文引用，表格保持不变。修改前版本与本轮检查材料保存在项目外 pre-research/_archive/drivecompose/20261023-remove-figure3/。
