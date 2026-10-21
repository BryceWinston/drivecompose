# 来源与项目外归档

2026-10-20 目录整理将历史材料移至 `pre-research/_archive/drivecompose/20261020-cleanup/`，位于 DriveCompose 项目之外。目录整理当时，双语论文入口、正文、实验章节、图件依赖、书目和样式保持原字节。后续非实验改写另见下方记录。

- [原始来源清单](source-manifest.json)：从旧 `paper/archive/` 原样归位，保留迁移时的路径、Git 提交和 SHA-256，不以当前文件覆盖历史记录。
- [归档定位与路径映射](archive-map.json)：项目外归档位置、原包、原始主图以及整理前文档快照的定位。
- [归档说明](../../../_archive/drivecompose/20261020-cleanup/README.md)
- [逐文件移出清单](../../../_archive/drivecompose/20261020-cleanup/moves.json)
- [整理验收记录](../../../_archive/drivecompose/20261020-cleanup/cleanup-report.json)

归档内 `files/` 保留移出文件的原项目相对路径，`before-edit/` 保存本轮更新过的说明文档和校验脚本的原版本，`inventory-before.json` 记录整理前的文件哈希。迁移和语言终校的历史报告不重写，其路径应按历史目录理解。

`tools/check_manuscript.py` 从索引定位外部原包、原始主图和历史文档快照，核对冻结内容及归档完整性。README 与论文定位文档因链接调整而改变；它们的旧版本单独保存，源码与算法文档仍按原哈希检查。归档迁至其他位置时可使用 `--archive-root PATH`，不修改原始来源清单。

## 非实验章节改写（2026-10-20）

- [录用论文结构观察与采用理由](structure-study-20261020.md)
- [本轮改动与最终检查](revision-20261020.md)
- [改写前的完整论文备份](../../../_archive/drivecompose/20261020-paper-revision/before/paper/)

本轮修改摘要、引言、相关工作、方法、讨论、结论、入口浮动边界与方法总览图。实验及其依赖按原始哈希冻结，来源清单和既有历史报告保持原样。当时使用矢量图替代论文中的旧 PNG，旧 PNG 仍作为历史来源核对对象。

## 生成式重建改写与双语核对（2026-10-21）

- [生成式重建改写记录](revision-20261021.md)：新标题、非实验双语正文和 Image Gen 总览图。
- [双语核对与实验历史](bilingual-audit-20261021.md)：非实验译法修正、原始实验差异及 Git 追溯。
- [旧构建文件迁移清单](build-archive-20261021.json)：项目外归档路径与哈希。
- [本轮归档目录](../../../_archive/drivecompose/20261021-bilingual-audit/)：旧版构建产物、修正前新版和源稿、PDF 检查材料。

当前 PDF 统一位于 `paper/build/en/main.pdf` 和 `paper/build/zh/main_zh.pdf`。非实验部分已核对；两版实验在原始压缩包中即不一致，尚未同步，不能将整个 PDF 称为完全对应的双语稿。

## 文献接入与实验迁入（2026-10-21 后续）

- [75 条文献的来源与引用位置](reference-integration-20261021.md)
- [书目接入清单](reference-integration-20261021.json)
- [用户指定实验目录的复制记录](experiment-import-20261021.json)
- [本轮修改前快照与临时材料](../../../_archive/drivecompose/20261021-reference-integration/)

当前书目为 84 条，用户已明确暂不限制篇幅。实验以指定目录的中英文文件分别为准；本轮不统一其内容，由后续实验负责人处理。本轮新修改等待用户确认，尚未提交或推送。

## 英文实验图片恢复（2026-10-21 后续）

- [原因、修复和中英文渲染对照](experiment-figure-fix-20261021.md)
- [PDF 图片资源与图号检查](../../../_archive/drivecompose/20261021-source-experiment-match/build-before/experiment-figure-check.json)
- [修复前文件与渲染快照](../../../_archive/drivecompose/20261021-experiment-figure-fix/)

原始实验文件继续保留；英文通过独立文件加载与中文相同的三张来源图。图件内容对齐不代表两版实验协议已统一。

## 实验全部留空（2026-10-21 最新状态）

- [当前实验留空与备份记录](experiments-empty-20261021.json)
- [修改前源码、PDF、原目录编译和对比材料](../../../_archive/drivecompose/20261021-source-experiment-match/)

按用户最新指令，两版仅保留实验章节标题，先前导入与英文图片补充已撤出当前稿。前文的实验导入和图片恢复条目保留为历史记录；其他章节不变，本轮不提交或推送。
