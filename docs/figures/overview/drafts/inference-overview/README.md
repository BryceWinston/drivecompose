# 主推理流程总览图（已采用）

> 2026-10-28 最新更新：用户要求整图生图后，当前正式图已切回 Image Gen PNG。本目录 production-prompt.txt 是最新实际提交的完整修正指令，见[当前总览说明](../../README.md)。以下旧确认记录属于历史版本。

当前采用用户明确指定的 [repair-attempt.png（归档原图）](../../../../../../_archive/drivecompose/20261026-overview-intermediates/docs/figures/overview/drafts/inference-overview/work/repair-attempt.png)，已按字节原样复制到论文活动图；候选副本已移出项目归档。后续对齐候选不再采用。当前 SHA256：`79eb11de6e2257b089647fe5d314e93414b85381eb276fe3656937ad06c1701c`。以下六项修复及分区比例是此前候选的历史记录，不能作为当前指定图片的几何验收结论。

[论文活动图](../../../../../paper/fig/drivecompose-inference-overview.png) · [完整生成指令](production-prompt.txt) · [设计及核对记录](design-spec.json)

2026-10-26 按用户反馈精简，并按“全部修复”要求完成六项局部修正。保留“图像 → ViT → 规范聚合与类型编码 → 联合 DiT → 类型解码 → 高斯组件”，重点展示局部注意力与跨组件记忆 CCM。

| 旧候选的具体问题 | 本候选调整 |
| --- | --- |
| Completed latents 的连线看起来由 CCM 直接输出 | 删除 CCM 到外框的线段，三路输出均从 DiT 外框端口引出 |
| 每行两条双向箭头重复 | 每行只保留一条双向交换线，共三条 |
| Local attention 虚线框与左上弯折残线 | 删除内层虚线框与残线，保留标题、token 和外层 DiT 边界 |
| 左侧约占四成，中央不够突出 | 输入图改为两张，结构化潜码移入蓝色区入口；实际三区约为 33%／46%／21%，中央成为最宽区域 |
| 背景输出带交通参与者 | 更换为无可见车辆或人体的静态道路、建筑、植被和天空组件 |
| Background 未指明局部分组 | 改为 Background region，保留 Vehicle i 与 Human j |

图像为内置 Image Gen 生成的光栅图，尺寸 2079 × 756。输入及高斯组件均为机制示意，不作实验结果。编码器沿主流向收缩，解码器沿主流向展开；六项修复已按实际渲染图自审，用户随后确认替换到论文。分区比例按图像底部的背景色区间测量，不将指令中的目标比例当作实际结果。

继续保留前轮已确认的范围：不展示 check、reuse、仿真、known/unknown/free 图例或采样备注；ViT 至 DiT 区域只有抽象特征与潜码。正文、公式、代码和实验没有随图示省略而改变。

联合补全在本图中作为完整推理过程的组合模块呈现，内部仅展开局部注意力和 CCM；数值积分、掩码条件和观测检查继续由正文定义，不代表从方法中删除。

当前生成指令恢复为指定图片对应的 `work/repair-attempt-prompt.txt`，共 26,503 个非空白字符；绑定模板为 15,356 个。此次仅复制已有图像，不重新生成。原始用户样式参考保留在[项目外历史候选目录](../../../../../../_archive/drivecompose/20261026-tracked-intermediates/docs/figures/overview/drafts/20261023-reference-style)。

2026-10-26 用户要求“替换掉论文中的总览图”后，已将本图按字节原样复制到论文活动图路径，并同步双语图注与方法开头的图示范围说明。两版主稿编译成功，Figure 1 均在第 2 页；英文正文保持 8 页，参考文献从第 9 页开始。[本轮修改前图像](../../../../../../_archive/drivecompose/20261026-overview-intermediates/docs/figures/overview/drafts/inference-overview/baseline/candidate.png)、指令、设计基线和论文修改前基线均已移入项目外归档，保留原目录层级。前后对照与理由统一记录在 `docs/paper-revision-changes.md`。

2026-10-26 清理：项目内保留当前生成指令、设计说明和本记录，正式图片仅保留在论文活动图路径。候选、布局参考、各轮备份及预览见[项目外归档](../../../../../../_archive/drivecompose/20261026-overview-intermediates)，文件对应和 SHA256 见[归档清单](../../../../../../_archive/drivecompose/20261026-overview-intermediates/archive-manifest.json)。

推送整合更新：保留远端新标题与引言后，英文正文结束于第 9 页；前述 8 页检查对应整合前版本。活动图及图注保持用户确认版本，详见当前构建记录。
