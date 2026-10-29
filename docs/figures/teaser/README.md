# DriveCompose teaser 设计研究与概念样例

日期：2026-10-28。范围：参考图研究、teaser 叙事与 Image Gen 概念图；随后按用户要求插入双语主稿标题下、摘要前。样例为生成式示意，不作为实验结果。

本轮场景样例：[drivecompose-teaser-waymo-concept.png](../../../paper/fig/drivecompose-teaser.png)，2172 × 724，宽高比 3:1。以用户提供的路口参考图调整场景、车辆与行人，并保留原有三栏版式。完整指令见 [waymo-production-prompt.txt](waymo-production-prompt.txt)，生成记录见 [waymo-generation-record.json](waymo-generation-record.json)。

上一轮布局样例：[drivecompose-teaser-concept.png](../../../../_archive/drivecompose/20261029-pre-push-cleanup/files/docs/figures/teaser/drivecompose-teaser-concept.png)，同为 2172 × 724。保留作布局与版本对照，生成信息见 [generation-record.json](generation-record.json)。

## 用户指定场景的样例调整（2026-10-28）

用户随后提供路口近景与多相机拼接图，要求按此示例制作 Waymo 风格的 teaser。参考原件保存在 references/user-intersection-closeup.png 与 references/user-intersection-panorama.webp。以路口、邮政车、深色外套行人、施工建筑与吊机、路面和自然曝光为视觉依据；沿用上一张概念图的三栏结构。新样例另存，保留原样例。

本轮只调整场景与对象身份。下方补全示意同步换成邮政车，右侧重复使用相同车辆与行人展示相机、车辆位姿和人体姿态变化。拼接图中的黑边与接缝属于图像覆盖，不作为三维场景的一部分。用户图片用于视觉参考，生成画面仍为概念示意。

## 图中需要让读者看懂的事

从有限驾驶观测出发，在背景、车辆与人体的结构化表示中联合补全缺失内容，再复用同一组补全资产，在不同相机与参与者状态下组合、渲染。

三个视觉问题分别是：输入缺少什么表面？补全如何覆盖背景与不同对象？补出的表面在对象运动后是否仍属于同一资产？Teaser 重点是展示这三个问题的关系，局部注意力、CCM 和条件流匹配的结构细节由现有方法总览图解释。

## 原论文参考与迁移建议

以下按用户提供的五张图顺序排列。会议身份只列本轮有来源支持的条目；其余采用所读取的预印本版本，不统一称为已录用顶会论文。图形分析基于所附实际图片、原文 Figure 1 与图注。

| 参考 | 图的叙事与视觉选择 | 对 DriveCompose 的具体启发 |
| --- | --- | --- |
| [Instant NuRec，Figure 1](https://arxiv.org/html/2607.14203v1#S0.F1) | 输入图像堆叠 → 大幅三维场景 → 多个渲染视角；场景中的彩色位置标记对应右侧同色结果边框。 | 用一个大场景建立三维印象，用统一标记建立场景与结果的对应。速度是该论文的卖点，本图无需移植时间数字。 |
| [StreetForward，Figure 1](https://arxiv.org/html/2603.19552v1) | 道路示意图把输入位置、时间插值和空间外推区别开；结果旁有深度、法线、动态与运动图。 | 展示明确的变化变量：相机、车辆、人体分开展示。辅助预测图不必全部复制进我们的 teaser。 |
| [Envision4D，Figure 1](https://arxiv.org/html/2606.10656v1#S0.F1) | 中央三维场景占最大面积，左右为输入和两类外推结果；相机轨迹用颜色区分。 | 保留清楚的横向阅读路径和主次比例。我们右侧突出状态驱动复用，不能把外部给定状态画成未来预测。 |
| [DGGT，Figure 1；CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.pdf) | 从输入、三维与几何输出过渡到 Add Car / Remove Cyclist，以具体操作表达用途。[作者页](https://xiaomi-research.github.io/dggt/)也说明场景编辑。 | 右侧使用具体可见的动作：新相机视角、车辆转动、人体姿态。选择能暴露未见表面的动作，令应用与补全相联系。 |
| [Drive2Gauss，Figure 1](https://arxiv.org/html/2610.26585v1#S1.F1) | 上下两条路径共用输入/输出类型，突出 RGB 生成后优化与多模态生成后前馈解码的路线差异。 | 借鉴“让贡献差异可见”的原则。我们的参考方法覆盖多类路线，宜用观测表面与补全表面的局部示意，不画笼统的“所有旧方法均失败”。 |

另外检查了两篇更贴近资产与可组合场景的工作：

- [GenAssets，CVPR 2025，Figure 1](https://research-assets.waabi.ai/GenAssets/paper.pdf)：把资产多面重建、车辆 U-turn 和可扩展生成放在同一 teaser 中；[作者页](https://waabi.ai/research/genassets)确认会议与研究定位。对我们最有用的是通过转动资产展示完整表面的用途。我们的展示范围应与实际取得的状态渲染对应，不直接继承其 360° 或生成类别主张。
- [OmniRe，ICLR 2025，Figure 1](https://arxiv.org/html/2408.16760v2)：通过从真实街景中抽离车辆与行人的图形呈现场景分解，并以车辆编辑、人体动作展示用途。[会议论文](https://proceedings.iclr.cc/paper_files/paper/2025/file/d4938496368e1c5806138bea8837595c-Paper-Conference.pdf)。对我们最有用的是明确“同一场景由哪些对象组成”；在此基础上再增加缺失表面补全，突出 DriveCompose 的主题。

## 建议版式

横向白底，约 3:1，按跨栏宽度设计；最终字号与实际两栏版面一起核验。

- 左侧约 17%：三张同一日志的图像，标注 Driving observations / Partial surface coverage。
- 中间约 52%：一幅占主导的斜俯视高斯场景，清楚标出 Background / Vehicle / Human。用一条轻量的共享上下文连接表示跨组件联合补全；下方仅保留一个局部表面补全前后的示意。
- 右侧约 27%：三个同场景的小视图，分别对应 New camera view / Vehicle rotation / Human articulation。保留相同对象外观，让读者能追踪资产。
- 其余空间用于留白和细箭头。图内不再展开编码器、潜码、注意力与解码器。

颜色分别承担两种任务，避免混用：背景/车辆/人体使用青、蓝、紫的细轮廓；所有新增表面统一以金色斜线覆盖标记，配 Observed / Completed 图例。金色是补全区域的标注，不是对象材质变色。

## 与当前论文证据的关系

当前方法支持在背景世界坐标、车辆自身坐标与带骨架绑定的人体参考姿态中建模，并通过 CCM 汇集场景上下文。Waymo 视图外推结果和 CCM 消融可支撑已有实验主张。当前状态复用段落给出了相机移动、车辆转动与人体换姿态的干预设置；此概念图不补造这些干预的真实结果，也不画成已验证的闭环策略反馈。正式结果型 teaser 需用同场景的真实输入、三维可视化和相应状态渲染替换示意画面。

2026-10-28 按用户要求插入：新图复制为 paper/fig/drivecompose-teaser.png，使用 fig:teaser，作为标题下、摘要前的 Figure 1。原网络总览保留为 Figure 2，标签改为 fig:overview，引言和方法对流程图的引用相应调整。未更改图像像素、摘要、正文论述或实验结果。用户允许按可读性决定宽度；此横图采用正文宽度，避免单栏缩放进一步缩小标注。两版图注均以概念示意定位，图内原有说明保留。

## 正文图注

中文：DriveCompose 概念示意。从驾驶图像中联合补全背景、车辆与人体的内容，构建可组合高斯场景。同一组资产可在相机视角、车辆位姿和人体姿态变化时复用。金色标注表示补全区域。

English: DriveCompose concept. DriveCompose jointly completes background, vehicle, and human content from driving images to form a compositional Gaussian scene. The same assets are reused under changes in camera viewpoint, vehicle pose, and human articulation. Gold marks completed regions.

## 生成与复核记录

使用内置 image-gen；初始完整指令见 production-prompt.txt。初稿右侧的车辆转动与人体换姿态不够明显，因此只针对右侧两处状态示例发出局部修改请求，指令见 refinement-prompt.txt。未调用外部 CLI 或 API，也未替换论文图件。图中保留“Concept illustration — not experimental results”。

技能：本机现有技能及扩展目录未定位到用户指定的 CCF-A SKILL.md；未声称执行 CCF-A 审查。实际采用 oral-paper-skill 的原图核验、贡献差异与主张–证据对应原则，以及 imagegen 技能。agent-reach 的 Exa 调用不可用，检索回退至网页工具并以论文/作者网站为依据。

## 正式图的素材准备

选择包含可辨认车辆与行人的同一段日志，保持对象身份、外观与补全种子一致。输入侧保留 2–3 帧；中央提供相同视角下的 observed-only 与 completed 资产或场景可视化；右侧分别改变相机、车辆位姿、人体姿态，每次只改变一个因素。

金色区域应由真实补全查询/高斯的标记及可见性确定，并随车辆刚体变换或人体蒙皮传播。这样，图中的颜色直接对应补全内容，能够检验其在新状态下的归属；不要凭画面观感手工把完整侧面都标成生成区域。

本轮基线提交为 e98697e。用户已授权将图件研究文件、首页插入修改、正式 PDF 和核验记录一并提交并推送。双语差异及编译检查见 docs/paper-revision-changes.md。

2026-10-29 合并：标题下 teaser 保留为 Figure 1，标签为 `fig:title-teaser`。概念对照、整体框架及联合补全机制分别顺延为 Figure 2、3、4。候选和重复图片副本已移至项目外归档；正式图、生成记录和用户参考原件保留。
