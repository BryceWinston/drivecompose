# DriveCompose 当前论文方法图

## 当前版本：2026-10-29，合并首页 teaser

首页 teaser 保留为图 1；三张已确认方法图分别为：

1. [概念对照](../../../paper/fig/drivecompose-concept-comparison.png)：图 2，两版第 2 页。
2. [整体框架](../../../paper/fig/drivecompose-inference-overview.png)：图 3，英文第 4 页、中文第 3 页。
3. [联合补全机制](../../../paper/fig/drivecompose-joint-completion.png)：图 4，英文第 6 页、中文第 5 页。

活动 PNG 与选定预览逐字节一致。完整提示词和生成记录见[项目外三图预览记录](../../../../_archive/drivecompose/20261029-pre-push-cleanup/files/docs/figures/overview/drafts/three-figure-preview/README.md)。当前图注位于主文件及方法节；插图为机制示意。合并后页码及核验见[归档与合并记录](../../../paper/provenance/pre-push-cleanup-20261029.json)。英文正文现止于第 10 页；原[三图入稿核验](../../../paper/provenance/three-figure-layout-verification-20261029.json)保留为合并前记录。

## 历史版本：2026-10-28，整图 Image Gen

用户明确要求“总览图调用生图，不用 SVG”后，当前 Figure 1 已改为内置 **Image Gen** 生成的[完整 PNG](../../../paper/fig/drivecompose-inference-overview.png)。尺寸 2163 × 727；该文件与 Image Gen 返回的图片按字节一致，没有通过 SVG 或代码重画。双语论文直接引用 PNG。

输入区突出用户提供街口中的多视角观测及遮挡；输出区依次展示同一场景的空背景、完整邮政车刚体资产和规范人体，再汇入 Compose & render，形成组合场景，并简要说明闭环仿真用途。背景与规范资产的坐标/角色分开，背景不包含交通参与者。所有生成的场景及资产均为机制示意，不作为实测重建或仿真结果；生成输入画面也不宣称逐像素保留原图。

独立知情审查与局部回归确认：视觉特征 → 几何/运动 → 规范聚合；三类局部组件与 CCM 交换后共同输出更新组件；Flow update 位于完成潜码之前；三类高斯组件与状态输入进入装配渲染。原始潜码旁路及“只有人体输出更新结果”的歧义已修正。

- [完整生成/修正指令](drafts/inference-overview/production-prompt.txt)，24,739 个非空白字符；绑定模板 15,356 个，长度检查通过。
- [来源与审核记录](imagegen-provenance.json)。
- [图注](caption.md)。
- [修改对照](../../paper-revision-changes.md)。

上一版 SVG/PDF 与矢量构建脚本已停用并移入[历史归档](../../../../_archive/drivecompose/20261028-imagegen-return/retired-native/)，不再作为当前总览图。此前 asset-provenance.json 仅说明被撤回的矢量版本，当前以 imagegen-provenance.json 为准。

## 历史记录（2026-10-26）


2026-10-26 更新。用户明确指定 `repair-attempt.png`（原图已移入项目外归档）后，两版论文共同使用[主推理流程总览图](../../../paper/fig/drivecompose-inference-overview.png)。内置 Image Gen 生成，场景为机制示意，不是实验结果；PNG 是光栅图，不宣称为可编辑矢量。

三部分依次说明结构化编码、联合 DiT 补全和类型高斯解码，重点展示局部注意力与跨组件记忆 CCM。ViT 到 DiT 之间只画抽象特征与潜码；检查、状态复用、仿真及 known/unknown 图例不在本图展示，相关方法定义仍保留在正文和补充材料。两张用户提供的参考图只提供视觉风格。

- [最终完整生成指令](drafts/inference-overview/production-prompt.txt)
- [设计规格与采用记录](drafts/inference-overview/design-spec.json)
- [图注](caption.md)
- [前后对照与替换理由](../../paper-revision-changes.md)
- [候选生成记录](drafts/inference-overview/README.md)

活动图尺寸 2079 × 756，按论文跨栏宽度原比例放置。对应指令 26,503 个非空白字符，绑定模板 15,356 字符，长度检查通过。候选图、中间产物与本轮修改前基线已移入[项目外归档](../../../../_archive/drivecompose/20261026-overview-intermediates)，具体路径及 SHA256 见[归档清单](../../../../_archive/drivecompose/20261026-overview-intermediates/archive-manifest.json)；旧 TikZ、历史 PNG、旧指令及未采用训练图已移入[历史图件归档](../../../../_archive/drivecompose/20261026-tracked-intermediates)，仍可按原路径层级追溯。2026-10-21 的制作记录保留在原文件中，不作为当前图的核验结论。

2026-10-29 清理：三图预览、未采用候选、旧版矢量图的组件素材与提示词已移至[项目外归档](../../../../_archive/drivecompose/20261029-pre-push-cleanup/)。正式三图仍位于 `paper/fig/`。历史来源记录中的原路径按[迁移清单](../../../paper/provenance/pre-push-cleanup-20261029.json)解析。
