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

本轮修改摘要、引言、相关工作、方法、讨论、结论、入口浮动边界与方法总览图。实验及其依赖按原始哈希冻结，来源清单和既有历史报告保持原样。当前矢量图替代了论文中的旧 PNG，旧 PNG 仍作为历史来源核对对象。
