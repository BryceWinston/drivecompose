# DriveCompose 的论文立意与叙事改进建议

## 2026 年 11 月 5 日 CVPR 录用论文叙事对照

**当前稿件的主线已经成立：相机或参与者状态变化暴露未观测表面，联合补全构建可组合内容，固定资产随后支持状态驱动复用。优先改进的是设计理由和证据的呈现位置。** 引言应把共享场景上下文与保留组件运动绑定连接起来，方法应让读者看清局部注意力与跨组件交换的分工，实验应将已有结果提炼为明确的技术判断。

本轮只提出意见和候选表达，未修改中英文论文、图表、实验值或正式 PDF。审阅对象为 2026-11-05 当前工作树，包含作者已有的未提交修改。以下判断以当前源文和最新证据记录为准；后面的 2026-10-21 审查保留为历史，不代表当前仍存在相同缺口。

### 调研样本及可借鉴之处

选取与本文任务或设计最相关的六篇 CVPR 主会录用论文，核验 CVF 发表记录，并读取项目已保存、带 CVF 录用版本水印的 PDF。重点对照摘要、引言、相关方法和分析段落。下表是对这些样本的写作判断，不是 CVPR 官方写作规则，也不用于推断录用原因。

| 论文及原始来源 | 本轮重点位置，页码从 PDF 首页计 | 叙事方式 | 对 DriveCompose 的具体启发 |
| --- | --- | --- | --- |
| [DGGT，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.pdf) | 第 1–2 页摘要、引言；第 8 页分析与结论 | 用相机位姿由输入转为输出这一设计选择贯穿问题和系统能力；寿命参数与细化模块分别对应不同的结果现象。 | 为整体框架建立一个能被复述的设计判断。保留 DriveCompose 的标定输入和多步补全设定，明确自己的改变发生在补全内容的组织和交互方式上。 |
| [HorizonForge，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf) | 第 1–3 页摘要、引言、概述；第 7–8 页 §4.2 | 引言同时建立真实感与控制需求；方法中的表示选择、时序建模分别由消融回答。引言还直接提炼实验形成的设计认识。 | 将“共享组件上下文在哪些条件下更有用”写成发现；用固定资产复用及其成本解释输出表示的用途。 |
| [StreetCrafter，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Yan_StreetCrafter_Street_View_Synthesis_with_Controllable_Video_Diffusion_Models_CVPR_2025_paper.pdf) | 第 1–3 页摘要、引言、方法概述；第 8 页分析与结论 | 先指出偏离轨迹后的观测不足和生成模型控制不足，再解释几何条件为何适合作为像素级控制信号；蒸馏由渲染延迟这一新需求引出。 | 用用途和约束引出设计。说明规范表示如何保留绑定、组件交换如何提供补全上下文，再介绍实现。 |
| [ReconDreamer，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.pdf) | 第 1–2 页摘要、引言；第 5 页 §3.3；第 8 页结论 | 将一般的新轨迹问题收窄到较大偏移下的伪影与恢复困难，随后解释渐进更新如何回应这一条件。 | 保留 DriveCompose 的具体操作入口；在既定实验范围内说明缺少哪些观测、采用哪种补全，以及如何检验。 |
| [VGGT，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf) | 第 1–2 页摘要、引言；第 4 页 §3.2；第 7 页 §4.5 | 多项输出由统一的前馈几何估计问题统领；注意力设计先交代作用，多任务消融进一步说明哪些输出对学习更有帮助。 | GCM、CCM、codec 和运动绑定应服从同一个输入到输出的解释。消融应报告作用差异，不能只说所有组件都有效。 |
| [Fast3R，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf) | 第 1–3 页摘要、引言、模型定义；第 6 页效率与位姿结果 | 从成对处理的计算负担和上下文限制引出多视图联合处理；贡献中既有模型，也有随视图数量变化的实证规律。 | 第三条贡献可直接写稀疏输入与低可见率下的收益规律。技术名词后面应接信息如何交换、由此解决什么问题。 |

这些论文的开篇和贡献形式并不一致：VGGT 很快进入方法能力，Fast3R 用较多篇幅解释近邻瓶颈，HorizonForge 强调编辑任务与评测。适合沿用的是“具体障碍 → 有理由的技术选择 → 对应证据”的联系，不需要统一段数、贡献数量或宣传性措辞。

### 当前已经写好的内容

- **摘要及引言的具体入口应保留。** 相机移动、车辆转向和人体换姿使隐藏表面成为可理解的问题，不需要再补一段泛泛的自动驾驶背景。
- **引言对前馈恢复的判断已经克制、准确。** “整个输入序列都未观测到的表面需要生成先验”清楚地区分了聚合证据与推断缺失内容，不应改成现有方法都无法补全或编辑。
- **方法的主要结构可以沿用。** 输入条件、世界背景与规范资产、观测聚合、联合补全、状态装配和训练已经闭合。双坐标用途、观测潜码恢复及逐查询解码都有解释，不需要重写整个方法节。
- **实验的关键区别应原样保留。** 主重建与消融的输入不同；规则 C 与 F 单列；真实编辑的结构完整性与四项联合质量分开；参数保持与渲染变化分开。这些条件决定结果如何理解。
- **输入数量敏感性已有好的结果句。** §4.5 已明确指出 T=2 时收益最大，适合用作整篇论文提炼发现的依据。讨论中的具体人体失败条件也应保留。

### 优先修改一 引言明确设计问题

位置：[英文引言第 8 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/1_introduction.tex:8)，对应中文引言第三段。当前前两句分别介绍生成式重建和可组合重建，后两句分别说明绑定和上下文；两种能力与本文联合补全之间的联系还可以更直接。局部替换最后两句即可，前两句及引文保持。

**原文：**

> Completing these component representations lets generated surfaces retain their actors' motion bindings. The visible background and other actors provide scene context for completing a partially observed component.

**建议表达：**

> A partially observed component can draw on the visible background and other actors for completion. The challenge is to share this scene context while retaining the component identities and motion bindings needed for subsequent edits.

**中文对应：**

> 部分可见的组件可以利用可见背景与其他参与者进行补全。关键在于共享这些场景上下文，同时保留后续编辑所需的组件身份与运动绑定。

这样，下一段的联合补全和跨组件记忆就有了明确的任务来源。该表达只连接已有方法事实，不声称独立补全必然失败，也不把局部注意力与记忆结构各自包装成独立贡献。写法参考 StreetCrafter 对条件信号用途的解释，以及 Fast3R 从上下文问题引出交互设计的方式。

### 优先修改二 方法说明局部与跨组件交互的分工

位置：[方法第 88 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/3_method.tex:88)，§3.3 的跨组件记忆段。当前段落已经给出输入、分组和公式；需要补的是读取公式前的设计目的。无需重写前端或增加一个新模块。

**原文：**

> Local self-attention processes these groups separately. Cross-component memory (CCM) then exchanges context across groups:

**建议表达：**

> Local self-attention models structure within each group. Cross-component memory (CCM) exchanges intermediate features across groups, providing scene context during completion while keeping component codes separate:

**中文对应：**

> 局部自注意力建模各组内部的结构。跨组件记忆交换组间的中间特征，在保持组件潜码分离的同时，为补全过程提供场景上下文：

原有读入、写回公式和后续变量说明保持。这一改动突出“局部结构建模”和“补全过程中的组间信息交换”两种作用，参考 VGGT 对注意力设计的解释方式。这里的“分离”指组件归属和表示组织，不意味着统计独立。

尤其要保留实验中的事实：**w/o CCM 仍具有相同的全局日志条件。** 因而本文比较的是跨组件中间特征交换的增量作用，不能将其写成“有全局信息”相对“完全没有全局信息”的优势。

### 优先修改三 消融先写发现 再给比较条件

位置：[实验第 123 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/4_experiments.tex:123)，§4.5 的 Completion components 段。当前前半段连续交代控制组、冻结条件、预算、训练与采样，主要结果位于段落后半。可把原有结果句提前，让读者先知道本段回答什么问题，再读控制条件。

**原文中的结果句：**

> At $T=8$, exchanging component context adds 0.627/0.934 dB full-image/dynamic PSNR (Table~\ref{tab:ablation-components}).

**建议用作段首：**

> At $T=8$, cross-component exchange improves full-image and dynamic-region PSNR by 0.627 and 0.934 dB, respectively (Table~\ref{tab:ablation-components}).

**中文对应：**

> 在 $T=8$ 时，跨组件交互使全图和动态区域 PSNR 分别提高 0.627 和 0.934 dB。

随后保留现有 w/o GCM 与 w/o CCM 定义、相同参数和全局日志条件、Stages 3–4 重训、共享恢复与 codec、数据预算、Euler 步数及种子统计。图 6 的具体视觉分析保持。此处的收益来自结果位置变化，不需要替换全部句式。

[第 153 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/4_experiments.tex:153) 的输入数量敏感性段已经写出稀疏输入下收益最大，建议保留。两段合起来应让读者记住：跨组件交换产生可测增益，而且这种增益随可用观测减少而增大。后一个判断限于本稿 T=2/4/8 的受控设置，不能改成任意稀疏条件下的普遍保证。

### 优先修改四 给核心隐藏表面证据一个正文落点

当前引言和贡献提到匹配机制与可见率评价，结论也概括隐藏几何和外观改善；主文 §4.5 对这部分只给出附录指引。核心数值均已在附录 H，无需恢复刚迁出的整张表。

位置：[实验第 123 行末句](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/4_experiments.tex:123)，证据见[附录 H 第 174–241 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/supplementary/evaluation.tex:174)。建议以一句关键结果替换笼统的附录指引。

**原文：**

> Appendix H reports paired hidden-surface mechanism comparisons and visibility-stratified results.

**建议表达：**

> On 100 synthetic test scenes, hidden-region PSNR exceeds a task-adapted object-coupling control by 0.67 dB; Appendix H reports the matched comparison and visibility analysis.

**中文对应：**

> 在 100 个合成测试场景上，隐藏区域 PSNR 比任务适配的对象耦合对照高 0.67 dB；匹配比较与可见率分析见附录 H。

这里的对照是通过共享恢复模块、codec、查询布局、输入、训练数据和 24 步采样接口实现的机制适配，数值为 23.18 对 22.51 dB。不能写成超过 JRM 原论文的公开成绩。可见率结果仍留在附录：低覆盖背景、车辆和人体分别提高 1.02、1.28、1.54 dB，充分观测区域仅提高 0.03–0.04 dB。这些结果为“收益集中于观测不足区域”提供解释。

若英文页数紧张，优先保留上述一句关键比较，不在正文同时展开隐藏机制表、可见率表和读取诊断。HorizonForge 将实验转换为设计认识、VGGT 在消融中指出不同任务的作用差异，都说明这种短结果句比泛泛的“更多实验见附录”更有信息。

### 后续同步一 第三条贡献写出发现

位置：[引言第 19 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/1_introduction.tex:19)。当前“通过什么评价验证什么”仍偏向实验安排；Fast3R 的贡献给出了随视图数量变化的规律，HorizonForge 也在引言明确提炼设计认识。DriveCompose 已有相应结果，可以直接陈述。

**原文：**

> We establish the contribution of shared scene context through matched completion mechanisms and visibility-stratified evaluations, and demonstrate state-driven reuse with real actor edits.

**建议表达：**

> We show that cross-component exchange provides its largest gains with sparse inputs and in poorly observed regions, through matched completion controls and visibility-stratified evaluation.

**中文对应：**

> 匹配补全对照与可见率分组评价表明，跨组件交互在稀疏输入和低观测覆盖区域中收益最大。

稀疏输入的证据来自 Waymo 的 T=2/4/8；低覆盖区域的证据来自合成可见率分组，二者不得混为同一组实验。真实编辑仍支撑第一条贡献中的资产复用能力，§4.4 和附录 I 的结果完整保留。三条贡献分别承担框架、关键机制、实证认识三个任务即可，数量无需调整。

### 后续同步二 摘要结果句与核心主张对应

位置：[摘要第 2 行最后两句](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/0_abstract.tex:2)。前面的具体问题、规范聚合和绑定解释可以保留；末尾目前只概括重建更好、能够编辑，没有选出直接支撑联合补全的关键证据。

**原文：**

> Experiments on Waymo show higher reconstruction accuracy and better off-trajectory rendering quality than feed-forward reconstruction baselines. Actor editing experiments further demonstrate that completed vehicles and humans can be reused across motion and pose changes.

**建议表达：**

> Experiments on Waymo show improved reconstruction and off-trajectory rendering quality over the feed-forward baselines. On 100 synthetic scenes, hidden-region PSNR exceeds a task-adapted object-coupling control by 0.67 dB. Across 360 actor edits in twenty real scenes, 82.78% pass all four quality criteria, covering structure, new-surface texture, appearance identity, and local geometry.

**中文对应：**

> Waymo 实验表明，相比前馈基线，DriveCompose 提高了重建与轨迹外渲染质量。在 100 个合成场景上，隐藏区域 PSNR 比任务适配的对象耦合对照高 0.67 dB。在二十个真实场景的 360 次参与者编辑中，82.78% 同时通过结构、新可见表面纹理、外观身份和局部几何四项质量检查。

选择这两项核心结果，是因为它们分别回答联合补全是否改善隐藏内容，以及完成的资产是否支持编辑后的质量要求。Waymo 全图和动态区域 PSNR 仍在正文报告，不需要把所有主表数字放进摘要。360 次编辑来自二十个场景与九组种子，不能表述为 360 个独立场景；82.78% 是四项联合通过率，92.78% 是结构完整性通过率。

### 后续同步三 结论收束到已建立的认识

位置：[结论第 4 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/6_conclusion.tex:4)。现有内容准确，但最后一句罗列 Waymo、配对指标和评价类型，信息已在实验中给出。若实施前面的修改，可用同一条技术认识收束，避免再列一次实验清单。

**原文：**

> DriveCompose jointly completes world-space background and canonical actor latents, preserving component identity and motion bindings for state-driven reuse. Shared scene context improves hidden geometry and appearance over task-adapted scene-latent and object-coupling controls. Fixed Gaussian assets support camera shifts, vehicle rotation, and human pose edits. Waymo reconstruction, paired surface metrics, and multidimensional real-edit ratings establish completion quality and state-driven reuse.

**候选表达：**

> DriveCompose jointly completes background and canonical actor representations, preserving their identities and motion bindings for reuse. Matched completion comparisons and visibility analyses show that sharing component context improves hidden-surface reconstruction, with larger benefits in poorly observed regions. The resulting Gaussian assets support camera shifts, vehicle rotations, and human pose edits without regenerating the scene.

**中文对应：**

> DriveCompose 联合补全背景与规范参与者表示，保留其身份和运动绑定以支持复用。匹配补全比较与可见率分析表明，共享组件上下文改善了隐藏表面重建，收益在低观测覆盖区域中更大。得到的高斯资产无需重新生成场景，即可用于相机平移、车辆旋转和人体换姿。

这属于候选段落级收束，优先级低于前四项；不应仅为换一种表达而执行。固定照明、有限覆盖和人体形变范围等具体边界继续在讨论中说明，不将已测试编辑扩大为任意姿态、完整闭环仿真或物理正确性。

### 相关工作与术语处理

当前 Related work 的四组已经覆盖恢复、可组合表示、补全和图像/视频生成，第三、四组也明确了本文的补全单位与持久三维内容。**这轮没有充分理由重排该节或再增加一批引文。** DGGT 本身也具有高斯级编辑能力，StreetCrafter 还可以蒸馏为动态三维表示；不能用“近邻只能生成视频、均不能编辑”来建立差异。差异应落在输入设定、生成/补全对象、规范车辆与人体绑定、跨组件交互，以及本文实际测试的复用范围。

| 稳定术语 | 本轮采用的含义 | 表达要求 |
| --- | --- | --- |
| Joint completion | 在共享条件模型中补全背景与规范参与者潜码 | 不等同于所有组件被合并成没有归属的单一场景潜码。 |
| Cross-component memory（CCM） | 局部组之间读入与写回中间特征的记忆机制 | 与全局日志条件分开描述，后者在 w/o CCM 中仍保留。 |
| Canonical asset | 保留组件身份、局部几何和刚体/骨架绑定的资产 | 不与逐帧高斯图或重新生成的视频混称。 |
| State-driven reuse | 固定已完成内容，改变相机与资产放置/关节状态后装配渲染 | 不扩展为行为策略、动力学预测或闭环效果。 |
| Off-trajectory distribution quality | 相对原轨迹参考总体的 FID/FVD | 不表述为新视角成对 GT 精度，也不单独证明隐藏几何正确。 |
| Structural integrity / joint quality acceptance | 92.78% 的结构通过率 / 82.78% 的四项联合通过率 | 结果名称、检查条件和分母保持区分。 |

### 修改顺序与证据核对

建议顺序为：先改引言的两句连接和方法的两句设计解释，再调整消融结果句的位置并补正文关键结果，最后决定是否同步贡献、摘要和结论。章节、图表、协议和结果均可沿用，无需新增实验才能完成这些文字改进。全部为建议，实际采用后还需同步中文并检查英文正文篇幅。

| 可用于文字的判断 | 当前证据位置 | 适用范围 |
| --- | --- | --- |
| Waymo 重建优于当前前馈基线 | 主文表 1；全图/动态 PSNR 相对 DGGT 分别 +1.154/+2.340 dB | 作者提供结果，共享条件重建协议。 |
| CCM 具有增量作用 | 主文表 3，T=8；全图/动态 PSNR +0.627/+0.934 dB | 共享恢复与 codec；w/o CCM 保留全局日志条件。 |
| 观测更稀疏时收益更大 | 主文表 4，T=2/4/8；PSNR 增益为 1.104/0.738/0.627 dB | 同时间跨度、目标视图和固定 checkpoint；每种输入重建证据与查询。 |
| 隐藏表面补全优于匹配机制对照 | 附录 H；23.18 对 22.51/22.24 dB | 100 个合成测试场景，任务适配的对象耦合/场景潜码对照；不作为原论文公开成绩比较。 |
| 收益集中于低覆盖区域 | 附录 H 可见率表；低覆盖 +1.02/+1.28/+1.54 dB，充分观测 +0.03–0.04 dB | 与零输入覆盖的隐藏区域评价区分，低覆盖组允许最多 20% 输入覆盖。 |
| 同一资产支持测试范围内的真实编辑 | 主文 §4.4，附录 I；298/360 四项联合通过，334/360 结构通过 | 二十个场景，九组种子；人体大关节弯折、自遮挡和宽松衣物边界失败保留。 |
| 参数保持与渲染影响需要区分 | 主文 §4.4，附录 J；参数差为零，输入视角 PSNR −0.029 dB、深度 MAE +2 mm | 固定原相机与参与者状态，相对 observed-only 参考。 |

数值从当前主稿、补充和作者证据记录转录，并核对上述差值与通过率；本轮未开展新的训练、评测或原始运行审计。此前作者确认原始材料已具备的状态保持，不将旧缺口记录重新判为当前材料缺失。

本轮基线、六篇 PDF 的来源及哈希、逐页文本和阅读记录保存在项目外归档 [`20261105-cvpr-narrative-review`](../../_archive/drivecompose/20261105-cvpr-narrative-review/)。基线 HEAD 为 `5b46f9eb8e131314430a2f2fa5193dadd16dc296`，审阅实际采用未提交工作树。中英文论文和正式 PDF 的未改动核验随同归档。

## 2026 年 10 月 21 日历史审查

以下保留当时的原始分析与候选方案。当前题名、证据状态、章节位置和修改建议以上方 2026-11-05 审查及现行稿件为准。

题名更新（2026-10-26）：当前采用 **DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion**，中文为 **DriveCompose：通过联合补全实现驾驶场景的可组合生成式重建**。下文保留 2026-10-21 审查时的候选标题及比较理由。

审查日期：2026 年 10 月 21 日。对象为当前中英文稿、项目方法与训练文档、主张证据表，以及 DGGT 原文。目标沿用项目的 CVPR 定位。本报告提出修改方案，没有改写论文、修改实验数值或运行训练。

本轮进一步明确的定位是：**以真实图像证据为条件，在背景和规范资产组成的结构化潜空间中进行生成式重建，得到可编辑、可复用的驾驶场景。** 相对 DGGT 一类逐帧像素对齐高斯恢复，这里同时改变了重建变量的组织方式和未观测内容的推断方式。局部—全局交互、观测锚定和状态装配服务于这一整体框架。论文不宜仅围绕观测锁定或某个补全模块组织。

DGGT 的主要推进可以概括为免位姿、可泛化的动态驾驶场景前馈重建，将相机恢复、动态处理和渲染串成完整方案。全文解释实现这一能力所需的组件，包含成熟组件及其训练方式；主题集中不等于只写局部创新。

DPT 与 DiT 不在同一功能层级。DPT 承担稠密解码，DiT 在本项目中参数化条件流的速度场，之后仍需类型专属高斯解码。实际链路为图像与标定、视觉恢复、规范查询与证据聚合、结构潜码、条件流补全、背景与资产解码、按状态装配。当前代码没有把 ViT 的图像 token 直接交给 DiT，也不是一次前向就得到最终世界。

进一步核验发现，WorldSplat 已将潜空间生成与像素对齐高斯解码结合，LatentWorld 已在实体中心潜空间生成语义占据场景。因此“生成式”和“可组合表示”应分开比较，并在驾驶日志条件下的 RGB 几何/外观重建、规范车辆与人体、原始三维内容的跨状态复用上界定本文方案。没有进行绝对首创性判定。[WorldSplat](https://wm-research.github.io/worldsplat/)、[LatentWorld](https://jindapark.github.io/projects/latentworld/)

DGGT 公开代码核验于提交 `a3276d2bbe4cbb03bcc117830b1836110a27adeb`，其 [GaussianHead](https://github.com/xiaomi-research/dggt/blob/a3276d2bbe4cbb03bcc117830b1836110a27adeb/dggt/heads/dpt_head.py#L309) 采用 DPT 风格多尺度稠密解码。本文对应实现见 [构建入口](E:/Users/changan/Desktop/论文/pre-research/drivecompose/src/drivecompose/pipeline.py:52)、[条件流模块](E:/Users/changan/Desktop/论文/pre-research/drivecompose/src/drivecompose/networks/completion.py:40) 和 [类型解码器](E:/Users/changan/Desktop/论文/pre-research/drivecompose/src/drivecompose/networks/decoders.py:44)。

当前稿件的主要问题是叙事重心失衡。它对联合补全、潜码锁定和构建检查解释得很细，却把恢复前端、完整训练目标和可控场景的实际形成过程压缩得过短。读者能够记住若干机制名称，却不容易判断整个方法怎样工作、凭什么能训练，以及最终解决了什么实际困难。

用户所说的“过于创新偏执”，在这份稿件中更准确地表现为：用机制差异组织整篇论文，支撑方法理解的内容则因不被列为创新而退到了背景。建议把论文中心放回“从不完整驾驶观测构建可控三维场景”，让核心技术沿解决问题的过程出现。

**DGGT 提供的写作参照**

DGGT 的标题为 *DGGT: Feedforward 4D Reconstruction of Dynamic Driving Scenes using Unposed Images*。它交代计算方式、重建任务、驾驶场景和输入条件，没有把寿命参数、运动头及扩散细化全部放进标题。其摘要将相机位姿从输入条件转为预测输出，作为贯穿方法的明确选择。[CVF 官方条目](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DGGT_Feedforward_4D_Reconstruction_of_Dynamic_Driving_Scenes_using_Unposed_CVPR_2026_paper.html)

DGGT 引言由驾驶日志的重建用途进入，随后收紧到逐场景优化、标定依赖和短窗口这些障碍。方法先解释场景如何恢复，再处理动态聚合和时间插值，最后处理渲染伪影；同时交代预训练组件、冻结选择和训练目标。这个顺序让新增模块有前因，也让常规组件有明确位置。[arXiv v1，§1、§3](https://arxiv.org/html/2512.03004v1)

从写作上看，值得借鉴的是“任务承诺—具体障碍—设计选择—实现与验证”的对应关系。借用成熟组件完全可以坦率说明；读者需要知道它们如何组成解决方案。没有必要要求每段方法说明都同时证明一个独立创新点。

视觉表达也有分工。DGGT 图 1 展示输入、可见输出、场景编辑和速度质量比较，图 2 再展开网络。项目页同样先让读者看见重建与编辑的结果，再解释细化过程。[DGGT 项目页](https://xiaomi-research.github.io/dggt/)

这不意味着照搬其技术承诺。DriveCompose 当前输入包含标定，离线补全需要多步积分；因此不能借用免位姿、单次前向或高速等标签。DGGT 的图像细化结果也不能直接作为持久三维资产完成度的证据。建议学习其论证顺序，用 DriveCompose 自己的输入、输出和证据确定标题与结论。

**当前稿件哪些地方值得保留**

引言开头的道路遮挡、车辆转向和人体姿态例子很有效。它们让“未见表面”成为一个具体问题，应保留并贯穿图示和实验。规范坐标与参考世界坐标的区分，以及已见高斯参数不变仍可能发生新增遮挡的解释，也具有实质内容。问题在于这些内容目前过早、过密地展开，挤占了整体方案与学习过程的说明。

项目已经有一套较完整的方法规格、几何约定和接口设计，足以支撑有内容的改稿。现有材料不能支撑性能提升结论；这项边界已经在 [EVIDENCE.md](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/EVIDENCE.md) 明确记录。写作时应利用已有细节补全解释，把尚未落实的研究内容留在工作清单中。

**需要优先处理的问题**

以下为本轮审查编号。Blocking 表示阻断当前完整方法或效果主张成立，不表示需要停止撰写已有部分。

| 编号与级别 | 位置与观察 | 对论文的影响 | 可验收的修改 |
| --- | --- | --- | --- |
| N1，Major，Blocking 否 | [引言第 10、12、14 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/1_introduction.tex:10) 连续展开双坐标、潜码约束、验收条件和状态变换 | 读者尚未形成整体任务图景，就进入实现约束；引言承担了过多方法说明 | 用一段完整流程概述接住研究问题，再用两段解释主要困难和选择；具体检查量移到方法 |
| N2，Major，Blocking 是，针对完整系统可复现性 | [方法第 18–19 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/3_method.tex:18) 用一段承载深度、法线、语义、身份、轨迹、关节和人体形状恢复 | 后续规范化与硬锚定依赖这些输出；不知道它们如何可靠获得，就无法评估整条链路 | 补充骨干与初始化、图像特征交互、身份槽和逐帧状态关系、监督来源、训练冻结关系；实际缺失的提供器单列 |
| N3，Major，Blocking 是，针对可训练性 | [方法第 113–117 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/3_method.tex:113) 概括恢复、codec 与补全训练；[证据表 G002、G003、G005](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/EVIDENCE.md) 仍列完整目标、人体模板和训练器缺口 | “使用完整目标”没有回答目标从哪里来、如何覆盖未知查询；公式完整不等于训练方案已闭合 | 为每阶段列实际数据、监督目标、可训练参数、冻结模块和输出；落实固定布局目标构造与人体模板；区分方法规格和已执行训练 |
| N4，Major，Blocking 是，针对效果主张 | [英文实验第 16、48、58 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/4_experiments.tex:16) 是 40 序列、单 FRONT 相机的基线评测并保留 MOSAIC 空行；[中文实验第 10、28 行起](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/zh/4_experiments_zh.tex:10) 使用另一套协议和 PointForward 来源数值 | 两版不是同一份实验叙事，也没有验证当前 DriveCompose 的中心主张 | 追溯英文基线原始日志，保留可复用部分；把中文来源表图作为参考资料；形成一套实际执行的 DriveCompose 协议并同步双语 |
| N5，Major，Blocking 否 | [贡献第 18–20 行](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/1_introduction.tex:18) 并列联合补全、观测约束、固定世界变换 | 方法机制、系统能力和成熟表示处于同一层级，容易迫使作者为每项分别寻找新颖性 | 按整体框架、关键补全设计和实证发现组织；状态驱动复用作为框架输出及应用验证，不单凭标准变换建立新颖性 |
| n1，Minor | [标题](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/main.tex:16) 堆叠 Observation-Anchored、Joint、Composable、Gaussian、Worlds | 标题先要求读者理解术语组合，任务入口较弱 | 改成任务、对象与关键条件明确的标题，机制名称留给摘要和方法 |
| n2，Minor | [相关工作](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/2_related_work.tex:5) 多段后半重复介绍本方法 | 与引言争夺功能，缺少充分解释相关技术关系的空间 | 按既有能力、尚未解决的具体需求、本方法采用或改变的部分来写；补齐实际使用组件的来源 |
| n3，Minor | [图 1](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/drivecompose-overview-vector.tex) 主要是 token、注意力、恢复与检查框 | 当前图能说明控制流，但不能直观说明新视角和新状态下究竟改善了什么 | 将结果预览与架构分开；缺真实结果时保留清楚标注的示意，后续用可追溯渲染替换结果位置 |

N2、N3 中有两类不同的缺口。已存在于文档或代码中的内容需要写清楚，例如轨迹级身份、逐时刻状态、类别支撑和冻结顺序；完整目标数据、实际模板提供器、训练记录及真实后端则需要项目工作。不能靠增加一段文字把后一类缺口变成已完成模块。

**标题建议**

优先采用以下工作标题：

**DriveCompose: Generative Reconstruction of Compositional Driving Scenes**

中文可用“DriveCompose：可组合驾驶场景的生成式重建”。Generative Reconstruction 表达以观测为条件、用生成先验处理未见内容的学习方式；Compositional 表达背景与规范资产组成的输出结构。标题覆盖整个框架，正文充分解释恢复、表示、生成、解码和控制。希望直接强调使用能力时，可用 `DriveCompose: Generative Reconstruction of Editable Driving Scenes from Images`。编辑能力应具体落到相机变化、车辆刚体运动和人体关节状态，不延伸为已经具备完整行为生成或物理仿真能力。

如果后续实验证据主要集中在补全模块，可收紧为：

**DriveCompose: Generative Completion of Compositional Driving Scenes**

中文可用“DriveCompose：可组合驾驶场景的生成式补全”。这个标题适合将恢复前端作为固定条件的研究。两种标题对应不同证据范围，不能在方法仍只验证模块时，仅为了气势选择完整系统标题。

不建议继续给当前长标题增加限定词，也不建议为了贴近 DGGT 加上 Feedforward 或 Pose-Free。Gaussian 可以出现在摘要首个方法句中；是否放进标题取决于表示本身是否承担中心贡献。

**推荐的研究主线**

建议用下面的问题统领论文：

> 如何把沿既有轨迹采集的不完整驾驶观测，构造成能在新相机位置和新交通参与者状态下重复使用的三维场景？

这条主线有四个自然环节。跨帧观测首先需要按身份和运动整理，得到稳定的背景和规范资产；已有观测没有覆盖的部分需要生成先验；生成内容必须与已有观测兼容；完成的内容需要随明确状态变化正确装配。联合条件和观测约束由这些需求引出。

“联合”仍是值得验证的技术假设，但不能预先决定整篇论文必须证明它是最独特的一环。只有同预算独立补全的对照能够说明跨组信息有多少额外价值。如果收益很小，应保留可信的完整方案，同时收紧这项机制的权重；不能换一组名字继续强化同一主张。

可控性也需要具体界定。OmniRe 已有刚体车辆、模板人体及关节控制，HUGSIM 已有控制命令驱动的闭环状态更新。它们说明场景分解和控制接口是可复用的研究基础。DriveCompose 的实证重点应落在补全后的场景在新状态下是否更可用，以及付出了什么构建成本。[OmniRe](https://ziyc.github.io/omnire/)、[HUGSIM](https://xdimlab.github.io/HUGSIM/)

**引言如何重排**

| 段落 | 要完成的论证 | 当前材料如何使用 |
| --- | --- | --- |
| 第 1 段 | 从驾驶日志复用需求进入，说明新视角与新状态会暴露未见表面 | 保留当前开头的道路、车辆和人体例子；补一句这些变化为何使原轨迹重建不足 |
| 第 2 段 | 说明已有方法提供了什么基础，剩余困难是什么 | 合并当前结构化重建与生成方法概述；避免断言所有既有方法都无法处理同一问题 |
| 第 3 段 | 用普通技术语言讲完整方案 | 图像和标定进入，恢复几何与身份运动，在规范空间聚合，补全缺失表面，再组成可控场景 |
| 第 4 段 | 解释为何采用规范空间及跨组件条件 | 先解释运动观测为什么需要对齐，再介绍双坐标和联合信息；用一个道路与车辆关系的例子说明动机 |
| 第 5 段 | 解释补全与观测保持之间的冲突 | 保留新增遮挡的例子；用两句交代硬约束和原视角检查，把具体指标移入方法 |
| 第 6 段 | 概括实际发现并收束贡献 | 有结果后填写新状态质量、观测保持与成本；当前用内部待补项管理，不向摘要填入虚构提升 |

不必强制六段；重点是每段承担不同任务。尤其应把引言中的固定逐查询解码、误差聚合、覆盖率、协方差和外观方向等细节移到方法相应位置，腾出解释整体方案的空间。

贡献可以先按两项方法贡献组织：一项是从部分日志构建可控场景的完整框架，一项是异构规范表示中的补全及观测保持设计。第三项若采用，应是有证据的发现或评测结果，不再单列“协方差随状态正确变换”。框架贡献仍需与最近邻比较，并由完整运行及任务效果证明价值。

**方法中应当补写什么**

建议采用以下阅读顺序，允许复用现有公式和符号。

| 小节 | 正文必须讲清楚 | 适合放补充材料 |
| --- | --- | --- |
| 问题与场景表示 | 输入和已知条件、最终输出、背景/车辆/人体采用何种表示、状态控制哪些量；用简洁的高斯渲染关系连接表示与图像 | 完整字段表、文件序列化、全部坐标变换细节 |
| 场景恢复与规范化 | 骨干和预训练来源或从头训练设定；跨视图/时间处理；身份和逐帧状态；为什么必须按运动对齐；人体模板的实际来源 | 每层宽度、完整头结构、槽数量、阈值表 |
| 从观测构建补全变量 | 已见、未知、自由空间如何由深度和实例证据得到；规范查询如何对应同一实体；双坐标分别解决什么问题 | 全部边界分支和容差实现 |
| 条件补全与场景解码 | 先定义条件生成任务，再解释局部/全局交互、flow、硬约束和类型解码；说明这些选择解决的具体困难 | 通用 attention 推导、采样实现细节、额外消融 |
| 可控渲染与构建检查 | 一个场景如何切换到新状态；新增遮挡为什么需要渲染检查；拒绝后的实际行为及成本 | 检查器全部阈值、异常与持久化策略 |
| 训练与推理 | 逐阶段的数据、目标、训练/冻结范围；完整潜目标的构造；训练与测试时的步骤 | 最终权重、batch、优化器、训练时长和硬件细节，正文保留关键设置 |

当前前端的一段文字应扩展成能独立读懂的小节。它的输出并不天然可信：深度、实例关联或人体规范姿态一旦出错，硬锁定会保留错误观测。正文需要说明置信度如何得到及如何影响证据采纳；实验需要区分真实前端与理想输入条件。

训练目标的来源尤其需要落实。完整资产样本可以支持单资产先验，但不能自动提供道路与多个演员之间的联合条件分布。若主张场景级联合补全，需要说明完整场景、组合数据或部分观测训练如何提供跨组件关系。现有“完整场景或资产目标”不足以回答这点。

这也不是要求所有生成模型都必须取得完整三维真值。CompleteSplat 通过图像投影监督学习表示，说明监督路线可以不同；如果 DriveCompose 改走类似路线，应重新给出与自身变量一致的训练定义，不能只保留当前需要有效完整潜目标的公式。[CompleteSplat 方法说明](https://nianticspatial.github.io/completesplat/)

**图表与实验应服务于同一条主线**

当前图 1 应承担架构图功能。另设一个结果预览，展示同一日志如何得到分离的背景、车辆和人体，以及同一补全结果在新相机、车辆转向或人体姿态下的表现。观察区域与新增区域的颜色应一致。没有真实输出时，示意只能解释目标，不能作为能力证据。

方法图需要把“共享恢复”展开到足以理解依赖关系，把“固定世界”画成能辨认的组成对象。双坐标和新增遮挡这两个难点各用一个局部例子即可，不必把检查器全部指标塞进主图。先让读者看到数据和场景的变化，再阅读模块名称。

实验建议按以下顺序组织，而不是先把消融表填满：

1. **完整方案是否改善新视角表现。** 保留可追溯且协议匹配的重建基线，增加本文结果；区分已见区域与新暴露区域，展示相同场景、相同视角的图像。
2. **补全场景是否支持明确状态变化。** 在固定输入和同一构建结果下改变相机、车辆和人体状态，检验内容质量与身份一致性。人体支持尚未落实时，不把人体演示当作已完成能力。
3. **改善来自哪些设计。** 先做无补全、独立补全、联合补全的清楚对照，再分析双坐标及观测约束；参数、条件信息、训练与推理预算需要对齐。
4. **代价和失败发生在哪里。** 报告原视角退化、覆盖率、全部场景的拒绝/失败率，以及前端、采样、检查、装配和渲染的分项成本。重复使用的收益用不同轨迹数量下的总成本表示。

现有英文实验中的短期时间外推涉及未来运动预测，而当前 DriveCompose 主要接收外部状态做装配。若保留这项任务，需要明确未来状态由谁提供，并向方法提供可比信息；给本文真实未来状态、让基线自行外推，会混淆比较对象。

英文稿当前将 DGGT 的扩散细化关闭。作为原始三维渲染对照，这一设置可以单独报告；若讨论最终图像质量，还应在条件允许时列出完整 DGGT 分支并计入细化成本。两种结果回答的问题不同，不应把关闭模块的结果概括为整个方法的能力上限。[当前基线设置](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/sec/4_experiments.tex:19)

真实离轨视角没有配对图像时，保留分布指标和定性比较，但不能据 FID/FVD 得出隐藏几何正确的结论。几何或新状态的配对评价应使用真实存在的留出观测、额外采集或受控合成参考。既有英文实验已经说明无配对真值，这一点应保留。

**对旧修改方向的调整与执行次序**

[上一轮审查](E:/Users/changan/Desktop/论文/pre-research/drivecompose/paper/provenance/nonexperimental-review-20261020.md) 将“确定两项真正独立的技术贡献”放在第一步。关于来源、训练目标和可比性的检查仍然有效，但本轮建议改变修改顺序。先恢复任务和完整方法的可理解性，再依据证据决定哪些设计值得作为核心贡献。

实际可以依次完成：确定一个任务句和工作标题；按读者理解顺序重排摘要与引言；补齐恢复、表示和训练的必要说明；落实完整目标、模板与后端缺口；建立一份双语一致的实验协议；用真实结果重写贡献、摘要结尾和结论。前四步中的写作工作无需等待全部实验完成，但不能将待实现内容改写成已验证事实。

当前英文 PDF 总计 8 页，参考文献已经从第 7 页开始。可以重新分配篇幅给方法解释和结果，而不需要缩小字体。篇幅应由必要内容决定，达到 8 页主文不是修改目标。

**来源与本轮核验范围**

DGGT 采用 Chen 等人的 arXiv:2512.03004v1，2025-12-02，题名见上文；官方 CVF 条目另确认其 CVPR 2026 收录。CVF 终稿 PDF 在本轮浏览访问返回 403，因此详细方法及页码以已下载的 arXiv v1 为准，不混用版本。该版本共 15 页；人工查看第 1–4 页的排版、图 1 和图 2，读取正文及附录相关段落。DriveCompose 查看两版源文件，并查看英文 PDF 第 1–2 页。

外部来源访问日期均为 2026-10-21。定向检索式为 `DGGT Feedforward 4D Reconstruction Dynamic Driving Scenes Unposed Images paper`；采用 arXiv、CVF、作者项目页，补查 OmniRe、HUGSIM 和 CompleteSplat 以核对能力边界。二手页面和匿名旧版本未作为方法依据。本轮没有开展穷尽最近邻检索、训练或性能复现。

本轮下载、文本抽取和页面预览保存在项目外 [审查材料目录](E:/Users/changan/Desktop/论文/pre-research/_archive/drivecompose/20261021-dggt-review)。原稿、代码、原始实验表和既有未跟踪文件均未改动。
