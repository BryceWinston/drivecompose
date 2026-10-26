# DriveCompose 当前总览图

2026-10-26 更新。用户明确指定 `repair-attempt.png`（原图已移入项目外归档）后，两版论文共同使用[主推理流程总览图](../../../paper/fig/drivecompose-inference-overview.png)。内置 Image Gen 生成，场景为机制示意，不是实验结果；PNG 是光栅图，不宣称为可编辑矢量。

三部分依次说明结构化编码、联合 DiT 补全和类型高斯解码，重点展示局部注意力与跨组件记忆 CCM。ViT 到 DiT 之间只画抽象特征与潜码；检查、状态复用、仿真及 known/unknown 图例不在本图展示，相关方法定义仍保留在正文和补充材料。两张用户提供的参考图只提供视觉风格。

- [最终完整生成指令](drafts/inference-overview/production-prompt.txt)
- [设计规格与采用记录](drafts/inference-overview/design-spec.json)
- [图注](caption.md)
- [前后对照与替换理由](../../paper-revision-changes.md)
- [候选生成记录](drafts/inference-overview/README.md)

活动图尺寸 2079 × 756，按论文跨栏宽度原比例放置。对应指令 26,503 个非空白字符，绑定模板 15,356 字符，长度检查通过。候选图、中间产物与本轮修改前基线已移入[项目外归档](../../../../_archive/drivecompose/20261026-overview-intermediates)，具体路径及 SHA256 见[归档清单](../../../../_archive/drivecompose/20261026-overview-intermediates/archive-manifest.json)；旧 TikZ、历史 PNG、旧指令及未采用训练图已移入[历史图件归档](../../../../_archive/drivecompose/20261026-tracked-intermediates)，仍可按原路径层级追溯。2026-10-21 的制作记录保留在原文件中，不作为当前图的核验结论。
