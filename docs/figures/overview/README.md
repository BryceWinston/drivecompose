# DriveCompose 当前总览图

2026-10-21 更新。两版论文共同使用 [总览图](../../../paper/fig/drivecompose-overview-20261021.png)。内置 Image Gen 生成，场景为机制示意，不是实验结果；PNG 是光栅图，不宣称为可编辑矢量。

三部分依次说明视觉恢复与规范聚合、结构潜码上的条件生成、类型解码与状态驱动复用。DGGT 图 2 提供分区、视觉密度及中间表示的参考；其方法、结果和原始图像未移入本图。采样内部过程归入 Conditional flow，检查内部比较在正文第 3.5 节展开。

- [最终完整生成指令](production-prompt-20261021-v4.txt)
- [设计规格](design-spec-20261021.json)
- [图注](caption.md)
- [改写与核验记录](../../../paper/provenance/revision-20261021.md)

最终指令 23,277 个非空白字符，绑定模板 15,356 字符，长度检查通过。候选与生成失败记录保存在项目外 `_archive/drivecompose/20261021-generative-rewrite/`。旧 TikZ 和历史 PNG 保留作为可追溯来源，当前正文不引用。
