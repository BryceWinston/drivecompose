# DriveCompose 双语论文工程

**当前版本：** 2026-10-29：两张消融表已写入作者提供的 33 个通用指标结果，双语分析与来源记录同步。54 项稿件检查及双语编译通过；英文正文止于第 8 页。当前 PDF 及核验入口见 [CURRENT-OUTPUTS.md](build/CURRENT-OUTPUTS.md)。

**2026-10-28 修订记录：** 按用户指定主流程完成中英文正文及补充材料修订。视觉编码、规范空间特征聚合、潜表示编码、联合潜空间补全、分类型高斯解码与场景组合分节解释，观测检查从方法主线移除；Obs-Reg 与 Pass 在实验中保留必要定义。中文同步补齐英文已有的实验设置和主结果表。52 条参考文献均完成真实性核验，3 条书目信息修正或补全。英文完整正文在第 8 页内，参考文献从第 9 页开始。

## 独立补充材料（2026-10-25）

原英文 4.4 跨数据集泛化及表 3 已完整迁入 `supplementary/cross_dataset.tex`，并补齐中文 `cross_dataset_zh.tex`。两版补充材料均采用与主稿相同的 CVPR 双栏样式，编号为附录 A、表 S1。`supplementary/` 是独立可编译项目，复用主稿的 `cvpr.sty`、`fontsetup.tex`、`ieeenat_fullname.bst`，`references.bib` 仅包含本补充材料实际引用的三条主书目记录。

在 `paper/supplementary/` 下执行：

```powershell
latexmk -xelatex -interaction=nonstopmode -halt-on-error '-outdir=../build/supp-en' main.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error '-outdir=../build/supp-zh' main_zh.tex
```

正式输出为 `build/supp-en/main.pdf`、`build/supp-zh/main_zh.pdf`；主稿仍使用 `build/en/main.pdf`、`build/zh/main_zh.pdf`。后续更新模板或这些参考文献时须同时核对两个项目。主稿的 8 页压缩目前仅形成[具体方案](../docs/paper-revision-workflow.md)，尚未执行 Method 等章节的压缩。

目标会议：CVPR 2027。更新日期：2026-10-23。

本工程由用户提供的 MOSAIC 压缩包迁移而来。当前题名为 **DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion**，中文题名为 **DriveCompose：通过联合补全实现驾驶场景的可组合生成式重建**。非实验正文按生成式重建框架组织，覆盖视觉恢复、规范聚合、结构潜表示、条件流、类型解码、状态装配与四阶段训练。

非实验正文及图注已完成一轮中英文自然表达终校；修改前的版本保存在项目外的 [语言终校前备份](../../_archive/drivecompose/20261020-cleanup/files/paper/archive/language-before-20261020.zip)。

**当前消融状态：已写入用户提供的两组结果及中英文分析。** 两张表包含 29 个结果数值及 1 个未报告指标，覆盖 Ours、w/o GCM、w/o CCM 组件消融及 Ours、w/o CCM 在 2/4/8 时刻下的输入数量敏感性；明确三路相机、24 步补全及 $[0,1]$ 线性 RGB 尺度。两表的 T=8 数值一致，消融定性图（原图 3）及其引用已删除。数据及来源见 [消融结果记录](provenance/ablation-results-20261023.json)，既有协议见 [最终消融方案](../docs/evaluation_plan.md)。本次按用户汇总结果回填，没有重新执行实验或独立核验原始日志。非消融内容不在本次修改范围内；此前空结果框架和实验迁入记录保留为历史。

## 文件入口

- `main.tex`：英文入口；`sec/`：英文各章节。
- `main_zh.tex`：中文入口；`zh/`：中文各章节，采用与英文相同的方法符号与结构。
- `main.bib`：两版共用的 84 条当前引用。用户 DOCX 的 75 条全部纳入，9 条与原书目重复、新增 66 条；文档之外的 9 条项目近邻工作保留。逐条引用位置见 [引用接入记录](provenance/reference-integration-20261021.md)。
- `fig/drivecompose-inference-overview.png`：两版共用的 Image Gen 总览图，展示结构化编码、联合 DiT 与高斯解码；ViT 到 DiT 之间使用抽象潜码，场景全部为机制示意。旧 TikZ、历史 PNG 和未采用草稿已移至[项目外归档](../../_archive/drivecompose/20261026-tracked-intermediates)。
- [总览图说明](../docs/figures/overview/README.md)：当前光栅总览图的设计、图注与审核记录；前版制作过程在项目外归档。
- [结构参考与改写依据](provenance/structure-study-20261020.md)：四篇录用论文的章节观察和本轮采用的安排。
- `fig/pointforward/`：原实验章节依赖的三张来源图，原样保留。
- `sec/4_experiments.tex` / `zh/4_experiments_zh.tex`：同步消融协议、结果表与分析；原消融定性图已删除。
- `provenance/source-manifest.json`：原始来源哈希及实验冻结清单，内容保持迁移时的版本。
- [归档索引](provenance/README.md)：MOSAIC 原包、迁移报告、终校备份与历史编译检查记录。
- `EVIDENCE.md`：主张、代码依据与材料缺口；`REFERENCES.md`：引用核验记录。
- `build/en/main.pdf` / `build/zh/main_zh.pdf`：中英文唯一当前构建路径；两版均已重新编译。实际构建状态以各目录的 `compile-result.json` 为准。临时合并目录和旧输出已移至项目外归档，见 [构建目录整理记录](provenance/build-directory-cleanup-20261021.json)。

## 编译与检查

推荐 XeLaTeX；`fontsetup.tex` 为两版加载 Times 兼容的 TeX Gyre Termes，中文采用 Fandol 宋体/黑体/楷体。字体通过 TeX 文件名读取，避免依赖本机系统字体配置。两版均使用共享 BibTeX 文件和原 CVPR 样式。

以英文为例，在本目录执行：

```powershell
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

中文将 `main` 替换为 `main_zh`。也可用 Tectonic 的内置 BibTeX 流程，分别指定输出目录：

```powershell
New-Item -ItemType Directory -Force build/en, build/zh
tectonic -X compile --keep-logs --keep-intermediates --outdir build/en main.tex
tectonic -X compile --keep-logs --keep-intermediates --outdir build/zh main_zh.tex
python tools/check_manuscript.py
```

本机可直接执行 `python tools/build.py`。脚本依次查找环境变量 `CODEX_TECTONIC_PATH`、PATH 和 Windows 上已安装的 Codex 所带 Tectonic，并将中英文 PDF 和日志分别保存在 `build/en/`、`build/zh/`。字体配置由 `tools/fontconfig.conf` 提供；已有 `FONTCONFIG_FILE` 时沿用该设置。`compile-result.json` 记录本次执行时间、退出码、PDF 哈希及是否实际写入新输出，避免将历史 PDF 误认为本次编译结果。

这一本地构建入口可在应用内置编译接口尚未完成沙箱初始化时使用；它不改变应用设置，也不替代内置预览的初始化步骤。

`tools/check_manuscript.py` 优先读取 `provenance/ablation-standard-metrics-20261029.json`，逐格核对两张消融表的版本、输入数量与作者提供的 33 个结果值，检查通用指标、旧指标删除、T=8 跨表一致性及双语公式。新指标数值来自作者于 2026-10-29 提供的汇总结果，旧自定义指标仅保留历史溯源。原实验归档、依赖图哈希、会议年份、引用和方法公式检查继续保留。归档位置由 `provenance/archive-map.json` 指定；缺少归档时检查会报错，论文编译不依赖外部归档。

来源清单保留旧路径和原哈希，当前文档链接的改动另行记录。校验时，已更新的两份设计文档与其整理前快照核对，其余设计与实现文件仍与原清单核对；检查结果分别列出历史证据完整性和当前文档变化。当前构建目录保留主稿及补充材料的双语正式 PDF、`compile-result.json`、`build/verification.json` 和总览图最终核验记录。历史检查、预览、基线快照及编译文本日志已归档。历史检查与编译中间文件移至项目外，旧路径及归档位置见 [整理记录](provenance/build-directory-cleanup-20261021.json)。

## 模板状态

两版 `confYear` 均为 2027，保留匿名 review 模式和待填写的论文 ID。2026-10-20 检查时，[CVPR 官方 author-kit 的 main.tex](https://raw.githubusercontent.com/cvpr-org/author-kit/main/main.tex) 仍标记 2026。本次保留压缩包内的原样式，不将修改年份表述为已经采用官方 2027 模板；正式投稿时再核对对应届次模板与要求。

2026-10-20 非实验改写：中英文按同一层级重整摘要至结论，方法保留六个编号二级节，短主题采用行内粗体标题。实验源文件及依赖图冻结；实验之后的浮动边界只用于避免讨论、结论被浮动图拆开。详见本轮结构记录；当时的 `build/revision-check.json` 现按 [整理记录](provenance/build-directory-cleanup-20261021.json) 归档。

## 2026-10-21 生成式重建改写

本轮采用 DGGT 的任务动机、整体设计、表示与模块解释、训练过程的叙述顺序，未复制原句或实验结论。中英文非实验正文和图注同步；实验正文与依赖图按字节冻结。完整记录见 [改写记录](provenance/revision-20261021.md)。

重新构建本轮输出：

```powershell
python tools/build.py
python tools/check_manuscript.py
```

当前统一使用默认 `build/en/`、`build/zh/` 路径。`--out-root` 仅在需要单独的临时输出时使用，历史版本保存在项目外归档。

## 2026-10-21 文献接入与实验迁入

75 条文献均在中英文正文中实际引用，相关工作按七个主题组织；引言加入驾驶数据来源，方法加入图像 patch 与注意力的基础引用。新增内容完成双语对应和自然表达检查，完整方法、公式及技术细节保留。按用户要求暂不约束篇幅，也不通过排版压缩页数。

本轮修改以已推送的 `a2cdacc` 为基线，留在工作区等待用户确认，再提交和推送。修改前的构建产物、源稿、文献页面与临时检查材料保存在项目外 `pre-research/_archive/drivecompose/20261021-reference-integration/`。

## 英文实验图片恢复（2026-10-21 历史步骤，现已撤销）

原英文实验文件只有数值表格，没有图环境或图片加载命令；中文实验文件则直接加载了三张来源图。现通过独立的图片补充文件为英文加入相同图件，并保留 PointForward 来源和图中“Ours”的归属说明。实验原文与数值未修改。修复及渲染对照见 [检查记录](provenance/experiment-figure-fix-20261021.md)。

## 实验全部留空（2026-10-21 历史步骤，已由消融框架替代）

按用户“实验部分全部留空”的指令，中英文实验仅保留章节标题和 `sec:experiments` 标签。实验文字、表格、图片、引用及额外图片段落均不再进入 PDF；其他章节、方法公式、书目和总览图未改动。此前的实验导入与图片恢复记录是历史记录，以 [本次状态](provenance/experiments-empty-20261021.json) 为准。原始内容、移出文件和修改前 PDF 保存在项目外 `pre-research/_archive/drivecompose/20261021-source-experiment-match/`。

本次两版编译均成功；阅读器关闭后，已将实验留空版替换至 `build/en/main.pdf` 与 `build/zh/main_zh.pdf`。编译记录的 `pdf` 字段指向当前输出，`compiler_pdf` 保存编译器原始输出位置。临时文件名已移至项目外归档。

## 消融设置与空结果框架（2026-10-21 历史步骤）

按最终方案写入中英文实验章节：完整方法及 A1/A2/A3/A7 对照、嵌套输入与固定目标、指标和重复规则。表 1 为五行组件对照，表 2 为 A0/A2 在 2/4/8 时刻下的六行对照；图 2 保留两行机制裁剪和一行状态复用，共 16 个空图片槽。数值格、实际图片和结果分析均留空，不包含性能结论。

旧留空版本及修改前 PDF 已备份至项目外 `pre-research/_archive/drivecompose/20261021-ablation-manuscript/`。核验脚本按新状态检查空结果格、空图片槽、双语实验公式和引用依赖，历史归档哈希检查继续保留。正式训练和真实渲染尚未执行。

## 消融结果回填（2026-10-23 历史步骤）

按用户提供的数值同步填写中英文两张消融表，按各指标实际最优值标粗；输入敏感性表只在相同 T 下比较。分析覆盖生成补全的覆盖率收益、跨组件潜码交换、显式世界坐标条件、硬/软观测约束的质量权衡，以及输入减少时跨组件交换的绝对收益变化。汇总值不附加未提供的方差或显著性结论。修改前源稿和 PDF 备份至项目外 `pre-research/_archive/drivecompose/20261023-ablation-results/`。

## 消融条目精简（2026-10-23 历史步骤）

按用户要求删除无世界坐标和软观测两组对照及其表格行、图示列与分析，正文、图注和两张表均改用 Full、No completion、Independent 名称，取消 A+数字编号。组件表保留三行，按保留版本重新标粗最优值；输入数量敏感性表保留六行及原数值。两版共用相同消融设置，各含 30 个结果数值和 12 个空图片槽。修改前文件保存在项目外 pre-research/_archive/drivecompose/20261023-ablation-simplification/。

## 消融表格重排（2026-10-23）

组件变体统一为 w/o GCM、w/o CCM 和 Ours；GCM 与 CCM 在方法节分别定义为生成式补全模块（Generative Completion Module）与跨组件记忆模块（Cross-Component Memory）。按用户要求将 w/o GCM 的 Obs-Reg 改为横线（未报告），删除对应零退化描述，最优值比较排除该单元格。两张表均使用等宽单栏布局、单行表头（指标名、单位与方向同行）；组件表分隔消融版本与完整模型，输入敏感性表按 T=2/4/8 分组并合并重复 T。其余 29 个数值保持不变。调研依据及布局取舍见 provenance/ablation-table-design-20261023.json；修改前文件与渲染检查位于项目外 pre-research/_archive/drivecompose/20261023-ablation-table-design/。

## 删除图 3（2026-10-23 当前状态）

按用户要求，中英文稿删除消融与复用占位图（原图 3）及其正文引用。消融表格、数值、单行表头和组件命名保持不变。修改前文件保存在项目外 pre-research/_archive/drivecompose/20261023-remove-figure3/。
