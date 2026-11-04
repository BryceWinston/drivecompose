# DriveCompose teaser 设计研究与概念样例

## 异机图 1 采用记录（2026-11-04；原件未同步）

按用户“这个作为 teaser 替换上去就行”的要求，该次异机替换使用 [drivecompose-concept-merged.pdf](../../../paper/fig/drivecompose-concept-merged.pdf)，来源为作者最新保存的 [可编辑 PPT](../../../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx)。完整单页渲染为 5400 × 2835 像素，再封装至原有 720 × 378 pt 图幅；没有重绘、裁切或修改 PPT 内的内容。两版图注与正文保持当前版本。输入缩略图来自 Waymo，P2–P6 为概念示意。

两版已重新编译并检查首页与正文末页；英文完整正文止于第 8 页，中文止于第 7 页。源文件哈希、内嵌像素核对与编译结果见[采用记录](../../../paper/provenance/teaser-ppt-replacement-20261104.json)。该记录仅描述异机编译。对应 PPT 及 SHA-256 为 `5f1e29a61e407e9e4c597e579b1eb8b7eeb2f58d21560b430562908b58e59d3e` 的导出未随纯文本提交提供；本次同步保留本机现有图件，其 SHA-256 为 `3031f2f09069d714ed267cb0390d6ea978e23304b7c7a23d5f5e0225773b1a40`。

## 2026-11-04 首页对比图优化

针对当前活动图一 `paper/fig/drivecompose-concept-merged.pdf`，完成录用论文原图核验和一张新的对齐对比草稿。实际起点为当时未提交工作区，文件哈希和 Git 状态见[本轮基线](../../../../_archive/drivecompose/20261104-figure1-optimization/baseline.json)。本轮由 `design-scientific-figure` 主导设计、`nature-academic-search` 核验参考，图内字号和图注参考项目已确认的 `cvpr-paper-standard`。没有启动第二套论文写作或演示制作流程。

**已归档草稿：** [figure1-comparison-draft.png](../../../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-comparison-draft.png)，2172 × 724，内置 Image Gen 生成，仍是概念示意。共享一组驾驶观测，上下对照 Observation-only / DriveCompose，右侧按 Camera shift / Vehicle rotation / Human articulation 三列逐列对应。车辆与人体用近景，灰斜线表示缺失、金色斜线表示补全。未替换论文活动图一，未修改正文或图注。

### 已录用论文的原图如何组织

核验日期：2026-11-04。下表分析的是各论文实际 Figure 1，而非只依据摘要或项目宣传图。[四篇原图联系图](../../../../_archive/drivecompose/20261104-figure1-optimization/references/accepted-figure1-comparison.png)由源 PDF 第 1 页裁切渲染，保留源图布局，用于个人设计研究。只迁移画法原则，不转用源图像素、数值或科学结论。

| 已录用来源与定位 | 原图实际画法 | 本图采用的原则 |
|---|---|---|
| [ReconDreamer，CVPR 2025，p.1 Fig.1](https://openaccess.thecvf.com/content/CVPR2025/papers/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.pdf) | 方法按行、相同视点位移按列，上方轨迹示意定义变化条件；从原视角到更大的横向位移，直接看画面差别。已下载并核验 CVF 正式版本。 | 共享列条件，固定同列目标状态；把对比放在视觉中心。DriveCompose 按三种不同干预分列，不复制原图的位移数值。 |
| [StreetCrafter，CVPR 2025，p.1 Fig.1](https://openaccess.thecvf.com/content/CVPR2025/papers/Yan_StreetCrafter_Street_View_Synthesis_with_Controllable_Video_Diffusion_Models_CVPR_2025_paper.pdf) | 上方紧凑输入与生成路径，下方分别展示同场景方法对照和编辑；相同位置的局部框突出道路细节差异。 | 先选能暴露差异的局部，统一对应位置。草稿直接放大车辆和人体，避免输出太小后再加一圈小框。 |
| [GenAssets，CVPR 2025，p.1 Fig.1](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_GenAssets_Generating_in-the-wild_3D_Assets_in_Latent_Space_CVPR_2025_paper.pdf) | 输入街景与多角度资产形成对应；转向序列显示资产在新状态下的用途，右侧展示生成资产的覆盖。 | 用同一车辆的转动说明未见表面为何重要。没有继承该论文的 360°、类别覆盖或规模主张。 |
| [HorizonForge，CVPR 2026，p.1 Fig.1](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.html) | 原序列与操作后序列成对排列，操作文字直接指向相机转动或车辆插入；时间对应明确。 | 将可见操作作为列标题，同列保持状态和构图对应，不再靠长段流程文字解释结果。 |

另检查了 UrbanCAD（CVPR 2025）首页编辑矩阵。OmniRe 和 DGGT 的所读版本首页没有放 Figure 1，未将它们作为“首页对比图”的主要样本。上述选择是与本任务相关的案例分析，不是对所有录用论文的统计规律。

### 原图问题 → 新草稿改动 → 作用

| 原图可见问题 | 本轮改动 | 对阅读的作用 |
|---|---|---|
| 上方失败流程与下方完整 teaser 采用不同构图，输入重复 | 两行共用左侧两张观测；行高、表示尺度和结果列统一 | 读者直接比较相同输入下的两种构建条件 |
| 上半没有与下半三种状态一一对应的画面 | 相机移动、车辆转动、人体换姿分别成列，上下配对 | 明确每次干预暴露哪一类未观测表面 |
| 大蓝色流程框、中心全景与下方车辆小插图争夺空间 | 删除大流程框及重复小插图，结果区约占六成宽度 | 让旋转车辆与换姿人体成为视觉中心，方法细节回现有图二／三 |
| 合并图比例 720:378，首页占高较大 | 新草稿比例为 3:1 | 等宽放置的图像高度减少约 36.5%；该值为几何计算，不是本轮重排 PDF 的实测 |
| 旧图两套面板字母与不一致字号 | 使用共享列标题、两行条件名和一个图例 | 减少标签重复，保留表面缺失／补全的语义 |

旧的主要图中文字为 `Driving images → Observation-only reconstruction → Observed surfaces → State-driven rendering → Unseen regions exposed`，下面另起 `Driving observations / Joint completion / Reuse the same assets`。新图将它们整理为共享 `Driving observations`，两行 `Observation-only / DriveCompose`，三列 `Camera shift / Vehicle rotation / Human articulation`。变化只服务于同条件对比，未增添实验结论。

### 产物、来源与复核

- [完整最终提示词](../../../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-comparison-prompt.txt)：最终局部修正调用的全文，26,642 个非空白字符；绑定模板为 15,356 个，长度检查通过。原始全图生成提示词保留在归档。
- [设计规格](../../../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-design-spec.json)：主张、来源、节点／关系、配对条件、组件绑定、字号、颜色及不可误读的边界。
- [生成与复核记录](../../../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-generation-record.json)：两次实际出图、局部修正、最终像素尺寸、SHA-256、采样密度和证据范围。
- [本轮过程归档](../../../../_archive/drivecompose/20261104-figure1-optimization/)：旧图、旧首页、参考 PDF 页图、首次草稿、提示词和缩小／灰度审阅图。生成原件另由 Image Gen 保留。

已查看全图、缩小预览及隐藏标题和一项次要注释的灰度副本；属于知情自审，不声称独立盲审。布局方向可供审阅。车辆与人体的配对修正减少了目标状态差异，但生成画面不是严格像素配准的实验比较。灰度下仅靠斜线颜色区分缺失／补全的效果弱于彩色，最终排版时需保留可读图例。约 173 mm 宽时源图采样密度约 319 dpi；该值只说明分辨率，不证明全部烘焙文字达到精确字号。

本轮没有改写正式 PDF。任务期间检测到其他图件／补充修订引起的 PDF 更新，未覆盖这些同期工作；当前活动图一以及两个主入口相对本轮起点保持。可编辑重建与正式入稿不在本轮已执行的范围内。

---

## 历史设计记录：2026-10-28

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
