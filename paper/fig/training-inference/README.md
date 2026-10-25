# Training and inference figure draft

2026-10-25; manuscript baseline: `c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb`.

`training-inference.pptx` contains two editable slides: English and Chinese. Native tables show the four training stages; attached connectors show inference. PNGs are previews, not the editable source. This is a method schematic, not experimental evidence. No manuscript text or PDF was changed in this round.

## Proposed replacement text (not applied)

The current Section 3.6 repeats module-freezing relationships across four paragraphs. Its inference paragraph also repeats the construction/reuse relationship from Sections 3.4–3.5. The figure consolidates those relationships, while the following draft retains conditions that should not disappear into a diagram.

**English:** Learning is divided into four stages so that the completion target has a stable meaning (Fig. X). Recovery and codec fitting establish coordinate-consistent representations, with partial and more complete observations sharing the same query layout. With recovery and the codec frozen, the GCM learns from complete scene or asset examples that provide a valid target for every unknown query. Real-log adaptation updates only the GCM through integration, decoding, and rendering; complete-target samples may be interleaved to retain the prior. Observed anchors are enforced by frozen decoding and hard code restoration. Training details are provided in Appendix B of the supplementary material.

**中文：** 学习分为四个阶段，使补全目标保持稳定的含义（图 X）。视觉恢复与编解码器拟合建立坐标一致的表示，部分输入与更完整观测共享同一查询布局。随后冻结恢复模块和编解码器，使用为每个未知查询提供有效目标的完整场景或资产样本训练 GCM。真实日志适配通过流积分、解码和渲染，仅更新 GCM；可交替使用完整目标样本以保留已学先验。冻结解码器并硬恢复观测潜码，以维持观测锚点。详细训练设置见补充材料附录 B。

**Proposed caption:** Training and inference in DriveCompose. Green cells indicate updated modules and gray cells indicate frozen modules. Inference constructs and checks a scene once, then reuses its accepted content under new camera and actor states.

**图注草案：** DriveCompose 的训练与推理流程。绿色单元格表示更新参数的模块，灰色表示冻结模块。推理阶段一次构建并检查场景，随后在新的相机和资产状态下复用通过检查的内容。

## Changes proposed, not yet made

| Current presentation | Proposed presentation | Reason / retained content |
| --- | --- | --- |
| Four separate paragraphs repeat train/freeze relationships | One native table | Makes parameter updates and target requirements directly comparable |
| Stage 2 explains matching layouts in several sentences | Table plus one sentence | Same-layout requirement remains explicit; detailed correspondence stays in Appendix B |
| Stage 4 mixes optimization path, constraints, replay and anchors | Optimization path in table; replay and anchors in prose | Preserve meaningful training conditions; loss details remain in Appendix B |
| Inference paragraph lists construction and reuse | Connected flow with original-view check before acceptance | Keeps acceptance gate and separates construction from runtime state changes |

## Space and validation

- Canvas: 960 × 360 pt. At 6.875-inch full text width, figure height is about 186 pt, approximately 0.29 of a 9-inch text page, excluding caption and float spacing. Minimum nominal font size is 17 pt, about 8.8 pt after that reduction.
- Current Section 3.6 is estimated at 0.46 page equivalent. Figure plus prose and caption may save only modest space, or none, depending on float placement. No compiled page reduction is claimed. Text-only shortening, or merging this flow into an existing overview figure, is likely more economical if page count is the primary objective.
- Both slides were rendered through native COM and visually inspected. Exact presentation path was used to avoid relying on the active window. Native text/table-cell heights and slide boundaries passed the saved audit; no embedded screenshot is used as the figure.
- Draft intentionally omits detailed losses and configurations already in Appendix B. Before adoption, verify the short prose and caption together with the figure in the actual two-column layout.
