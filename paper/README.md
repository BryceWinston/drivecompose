# DriveCompose 双语论文工程

目标会议：CVPR 2027。更新日期：2026-10-21。

本工程由用户提供的 MOSAIC 压缩包迁移而来。当前题名为 **DriveCompose: Generative Reconstruction of Compositional Driving Scenes**。非实验正文按生成式重建框架组织，覆盖视觉恢复、规范聚合、结构潜表示、条件流、类型解码、状态装配与四阶段训练。

非实验正文及图注已完成一轮中英文自然表达终校；修改前的版本保存在项目外的 [语言终校前备份](../../_archive/drivecompose/20261020-cleanup/files/paper/archive/language-before-20261020.zip)。

**实验按用户指定目录原样迁入，由后续实验负责人修改。** 来源为 `E:/Users/changan/Downloads/edge/MOSAIC__Motion_Aware_Multi_Object_Feed_Forward_4D_Reconstruction_for_Driving_Scenes`。2026-10-21 分别复制中英文实验 TeX，内容与复制前相同，三张依赖图也与来源一致。两种语言仍保留来源各自的协议、数值和表图，本轮不翻译或统一实验。来源和逐字节核对见 [迁入清单](provenance/experiment-import-20261021.json)；历史差异见 [双语核对记录](provenance/bilingual-audit-20261021.md)。

## 文件入口

- `main.tex`：英文入口；`sec/`：英文各章节。
- `main_zh.tex`：中文入口；`zh/`：中文各章节，采用与英文相同的方法符号与结构。
- `main.bib`：两版共用的 84 条当前引用。用户 DOCX 的 75 条全部纳入，9 条与原书目重复、新增 66 条；文档之外的 9 条项目近邻工作保留。逐条引用位置见 [引用接入记录](provenance/reference-integration-20261021.md)。
- `fig/drivecompose-overview-20261021.png`：两版共用的 Image Gen 总览图，参考 DGGT 的分区与中间表示视觉语言；场景全部为机制示意。旧 TikZ 与旧 PNG 保留，不再进入当前正文。
- [总览图说明](../docs/figures/overview/README.md)：当前光栅总览图的设计、图注与审核记录；前版制作过程在项目外归档。
- [结构参考与改写依据](provenance/structure-study-20261020.md)：四篇录用论文的章节观察和本轮采用的安排。
- `fig/pointforward/`：原实验章节依赖的三张来源图，原样保留。
- `sec/4_experiments.tex` / `zh/4_experiments_zh.tex`：按用户最新要求，仅保留实验章节标题；原实验内容及英文图片补充文件已备份到项目外。
- `provenance/source-manifest.json`：原始来源哈希及实验冻结清单，内容保持迁移时的版本。
- [归档索引](provenance/README.md)：MOSAIC 原包、迁移报告、终校备份与历史编译检查记录。
- `EVIDENCE.md`：主张、代码依据与材料缺口；`REFERENCES.md`：引用核验记录。
- `build/en/main.pdf` / `build/zh/main_zh.pdf`：当前实验留空版，已替换原文件名。旧版构建文件已移至 [项目外归档](../../_archive/drivecompose/20261021-bilingual-audit/build-old/)；原 `revision-20261021` 的内容已迁入 `build/` 主目录，并在这里重新编译。

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

`tools/check_manuscript.py` 核对两版实验留空、原实验备份与依赖图的哈希、外部归档完整性、会议年份、正文命名、引用、图片/输入依赖及中英文方法公式。归档位置由 `provenance/archive-map.json` 指定；若归档另存他处，使用 `python tools/check_manuscript.py --archive-root "归档目录"`。缺少归档时检查会报错，论文编译本身不依赖外部归档。

来源清单保留旧路径和原哈希，当前文档链接的改动另行记录。校验时，已更新的两份设计文档与其整理前快照核对，其余设计与实现文件仍与原清单核对；检查结果分别列出历史证据完整性和当前文档变化。编译日志、`build/verification.json` 及 `build/pdf-qa.json` 保存在当前 `build/` 目录。

## 模板状态

两版 `confYear` 均为 2027，保留匿名 review 模式和待填写的论文 ID。2026-10-20 检查时，[CVPR 官方 author-kit 的 main.tex](https://raw.githubusercontent.com/cvpr-org/author-kit/main/main.tex) 仍标记 2026。本次保留压缩包内的原样式，不将修改年份表述为已经采用官方 2027 模板；正式投稿时再核对对应届次模板与要求。

2026-10-20 非实验改写：中英文按同一层级重整摘要至结论，方法保留六个编号二级节，短主题采用行内粗体标题。实验源文件及依赖图冻结；实验之后的浮动边界只用于避免讨论、结论被浮动图拆开。详见本轮结构记录及 `build/revision-check.json`。

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

## 实验全部留空（2026-10-21 最新要求）

按用户“实验部分全部留空”的指令，中英文实验仅保留章节标题和 `sec:experiments` 标签。实验文字、表格、图片、引用及额外图片段落均不再进入 PDF；其他章节、方法公式、书目和总览图未改动。此前的实验导入与图片恢复记录是历史记录，以 [本次状态](provenance/experiments-empty-20261021.json) 为准。原始内容、移出文件和修改前 PDF 保存在项目外 `pre-research/_archive/drivecompose/20261021-source-experiment-match/`。

本次两版编译均成功；阅读器关闭后，已将实验留空版替换至 `build/en/main.pdf` 与 `build/zh/main_zh.pdf`。编译记录的 `pdf` 字段指向当前输出，`compiler_pdf` 保存编译器原始输出位置。临时文件名已移至项目外归档。
