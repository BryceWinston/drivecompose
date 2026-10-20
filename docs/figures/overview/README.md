# DriveCompose 当前总览图

当前中英文入口共同引用 [原生 TikZ 图源](../../../paper/fig/drivecompose-overview-vector.tex)。图随论文编译为矢量文字和图元，没有嵌入生成图片；画布为 495 × 225 pt，普通标签 8.3 pt，阶段标题 9.5 pt。

图的主张：已见规范查询通过硬约束保持，未知查询在场景上下文中联合补全；候选通过原视角检查后进入固定世界，外部状态驱动后续装配和渲染。图中的相机平面、查询色块与高斯标记均为机制示意，没有实验图像或量化结果。

- [同步图注](caption.md)
- [当前设计规格](design-spec.json)
- [结构参考](../../../paper/provenance/structure-study-20261020.md)
- [本轮备份与图审记录](../../../../_archive/drivecompose/20261020-paper-revision/)

图分三阶段：规范证据、联合补全、检查与复用。虚线只表示下一步流积分；实线传递数据。观测图像与仅观测渲染作为检查参照；拒绝候选在 discard 支路终止，不进入固定世界。外部状态和固定内容分别输入渲染器。

旧 [PNG 设计稿](../../../paper/fig/drivecompose-overview.png) 保持原字节用于来源核对，当前论文不引用它。`production-prompt-final.txt` 属于该历史光栅稿。旧 README、规格及图注的改写前版本保存在本轮项目外备份，早期生成记录仍在 [整理归档](../../../../_archive/drivecompose/20261020-cleanup/README.md)。
