# DriveCompose 双语论文工程

目标会议：CVPR 2027。更新日期：2026-10-21。

本工程由用户提供的 MOSAIC 压缩包迁移而来。当前题名为 **DriveCompose: Generative Reconstruction of Compositional Driving Scenes**。非实验正文按生成式重建框架组织，覆盖视觉恢复、规范聚合、结构潜表示、条件流、类型解码、状态装配与四阶段训练。

非实验正文及图注已完成一轮中英文自然表达终校；修改前的版本保存在项目外的 [语言终校前备份](../../_archive/drivecompose/20261020-cleanup/files/paper/archive/language-before-20261020.zip)。

**实验章节尚未双语同步。** 2026-10-21 逐节核对并追溯 Git 历史后确认：原始 MOSAIC 压缩包、首次加入论文的 `f2fa6f3`、上次提交 `b677a00` 和当前工作区的两份实验文件分别字节一致，但两种语言原本就是不同内容。英文采用 40 序列、单 FRONT 相机的本地基线评测，中文采用旧三相机协议和 PointForward 来源表图。按已有“实验暂不改”要求保留，不能将整份 PDF 称为已双语对齐或完成实验核验。详见 [双语核对与实验历史](provenance/bilingual-audit-20261021.md)。

## 文件入口

- `main.tex`：英文入口；`sec/`：英文各章节。
- `main_zh.tex`：中文入口；`zh/`：中文各章节，采用与英文相同的方法符号与结构。
- `main.bib`：两版共用的 18 条当前引用；旧版完整 40 条书目保存在原始压缩包中。
- `fig/drivecompose-overview-20261021.png`：两版共用的 Image Gen 总览图，参考 DGGT 的分区与中间表示视觉语言；场景全部为机制示意。旧 TikZ 与旧 PNG 保留，不再进入当前正文。
- [总览图说明](../docs/figures/overview/README.md)：当前光栅总览图的设计、图注与审核记录；前版制作过程在项目外归档。
- [结构参考与改写依据](provenance/structure-study-20261020.md)：四篇录用论文的章节观察和本轮采用的安排。
- `fig/pointforward/`：原实验章节依赖的三张来源图，原样保留。
- `provenance/source-manifest.json`：原始来源哈希及实验冻结清单，内容保持迁移时的版本。
- [归档索引](provenance/README.md)：MOSAIC 原包、迁移报告、终校备份与历史编译检查记录。
- `EVIDENCE.md`：主张、代码依据与材料缺口；`REFERENCES.md`：引用核验记录。
- `build/en/main.pdf` / `build/zh/main_zh.pdf`：当前中英文编译产物。旧版构建文件已移至 [项目外归档](../../_archive/drivecompose/20261021-bilingual-audit/build-old/)；原 `revision-20261021` 的内容已迁入 `build/` 主目录，并在这里重新编译。

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

`tools/check_manuscript.py` 核对实验和依赖图的冻结哈希、外部归档完整性、会议年份、正文命名、引用、图片/输入依赖及中英文方法公式。归档位置由 `provenance/archive-map.json` 指定；若归档另存他处，使用 `python tools/check_manuscript.py --archive-root "归档目录"`。缺少归档时检查会报错，论文编译本身不依赖外部归档。

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
