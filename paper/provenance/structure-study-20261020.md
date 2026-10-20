# DriveCompose 非实验章节的参考研究与改写依据

日期：2026-10-20。范围：双语摘要、引言、相关工作、方法、讨论、结论和方法总览图。实验正文、实验图表、数值及共享书目保持原字节。本记录沿用现有项目，不另建研究流程。

## 参考材料与检查范围

选取四篇 CVPR 主会录用论文，关注结构如何服务技术论证，不把排版习惯解释为录用原因。使用已保存的 CVF 原始 PDF，核对本地来源哈希；抽取各篇前 8 页结构，人工查看 VGGT 第 1、3 页，Fast3R 第 3、4 页，D4RT 第 2、3 页，Native 3D 第 3、5 页。访问 CVF HTML 详情页时返回 403，未用二手摘要替代已有原始 PDF，也未声称检查了它们全部页面。

| 参考论文 | 章节组织与内容构成 | 本项目采用的做法 |
| --- | --- | --- |
| VGGT，CVPR 2025 | 引言与相关工作之后进入方法；方法先定义任务和符号，再讲特征骨干与预测头。输入、输出和坐标约定先于网络细节。 | 将日志、相机、米制坐标、世界表示放在方法开头；恢复前端作为支撑环节，不与联合补全争夺层级。 |
| Fast3R，CVPR 2025 | 模型章节区分问题定义、训练目标、架构与内存实现；主实验与消融分别成节。标准组件围绕计算过程解释。 | 损失变量在定义后使用；训练按恢复、codec、补全先验和真实观测适配交代，避免模块清单式标题。其实验分节仅作观察，本轮不套到冻结章节。 |
| D4RT，CVPR 2026 | 方法先于相关工作，按整体框架、架构、训练与推理展开；先给短概览，再解释表示和查询如何工作。 | 方法开头用一个自然段说明构建、检查和复用的顺序。本项目的近邻关系无需先读完整方法，继续将相关工作前置。 |
| Native and Compact Structured Latents for 3D Generation，CVPR 2026 | 方法按表示、压缩与生成展开；表示和 VAE 下再分持续展开的子问题，采用第三级编号。 | 按“表示—聚合—联合补全—解码检查—训练—复用”组织六个二级节。短主题使用行内粗体段标题，不为一小段增设 3.x.x。 |

这些样本都用默认模板的编号标题、双栏正文、编号公式和跨栏或单栏图。大小写风格并不完全一致；本稿按已确认标准统一为句首大写。没有复制终稿的作者、水印、连续出版页码，或手工压缩字体与页边距。

## 当前稿件的具体改法

- 摘要保持单段，交代缺失表面、双坐标查询、局部/全局交换、硬约束、接受检查与固定世界复用；实验结论留待真实证据补齐，不添加提升数字。
- 引言从相机和资产状态变化暴露隐藏表面的具体问题起笔，再比较结构化重建与生成方法，说明双坐标的作用。用新增表面遮挡已见背景的例子区分参数保持与图像一致性，最后给出三项技术贡献。
- 相关工作按可组合重建、前馈恢复、生成式补全三条路线展开，比较生成单位、持久内容和后续状态变换。保留已有书目，不将这些写作参考强塞进技术引用。
- 方法采用 3.1 至 3.6 编号：问题定义与世界表示、规范查询与证据聚合、观测锚定联合补全、解码与观测检查、训练阶段与目标、状态驱动装配与复用。核心注意力交换、条件流和有效软约束有计算定义，标准变换压缩为必要公式。
- 小节内的共享恢复、局部/全局交换、条件流、按类型解码、渲染检查及训练阶段采用模板 paragraph 的行内粗体标题。两种语言的层级、标签和数学表达对应。
- 讨论集中保留有限覆盖、固定照明、恢复误差、人体模板与新状态有效域；结论围绕同一场景跨轨迹复用收束，删除模块复述和宣传式评价。
- 图 1 改为原生 TikZ 矢量图。按刊印宽度设计字与箭头，区分观测、未知、自由空间和补全内容，明确拒绝分支以及外部状态的输入位置。
- 以模板字号、几何和标题间距排版；不增设编号图表，不改实验内的浮动设置。在实验输入之后设置浮动边界，避免讨论和结论被前文浮动图拆开。

## 证据与边界

本次改写依据现有代码与方法文档。局部/全局记忆交换公式对应 completion 网络；适配损失对应 training.py 的射线、地面、接触与穿透项。已见潜码硬恢复且逐查询 codec 冻结时，已见高斯参数差异项恒为零，因此不作为有效适配损失；这项修正及未定权重单列于 EVIDENCE.md。未改实现、训练配置或任何实验结果。

篇幅按编译后面积检查，不靠补写空泛文字凑满八页。实验仍冻结，两版实验本身的历史内容和差异不属于本轮完成项。当前使用继承样式并将年份统一为 2027；官方 2027 年度模板仍需后续核验，不能把本次内容与排版修正表述为投稿终检完成。

## 原始来源

- [vggt.pdf：CVF 原始 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf)；本地 `_archive/cvpr-paper-standard-20261020/sources/papers/vggt.pdf`；SHA-256 `b2e33f1040badf274373ad810c6ac0c272597195427ac6a0f171d5933b639a0e`。
- [fast3r.pdf：CVF 原始 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf)；本地 `_archive/cvpr-paper-standard-20261020/sources/papers/fast3r.pdf`；SHA-256 `3deb2db40328f9875b80acf91442c28afaa369340fdafd95e0fbaa40ea837058`。
- [d4rt.pdf：CVF 原始 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.pdf)；本地 `_archive/cvpr-paper-standard-20261020/sources/papers/d4rt.pdf`；SHA-256 `b88222682a2007f797d83bd891165a9dbb997cc5a7d3ab5a0d426e767861c5be`。
- [native3d.pdf：CVF 原始 PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_Native_and_Compact_Structured_Latents_for_3D_Generation_CVPR_2026_paper.pdf)；本地 `_archive/cvpr-paper-standard-20261020/sources/papers/native3d.pdf`；SHA-256 `de9996f3e05b3621c4617786011495e1e600d0ef7058adb06329b537c39e59d8`。

页面预览、首轮排版和图审记录保存在项目外 `_archive/drivecompose/20261020-paper-revision/`，不进入正文或补充材料。
