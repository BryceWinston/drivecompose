# Teaser 可编辑概念图（素材已全部填入）

2026-11-04 论文采用：用户指定的现有 `output/DriveCompose-teaser-placeholder.pptx` 已原样接入两版首页 Figure 1。PPT SHA-256 为 `eda0c26a9fa6b493bc441dd16eb6c406b2137c8de5616786d712544f5b734008`，本次没有保存或修改 PPT。完整单页以 5400 × 2835 像素导出，封装为 `../drivecompose-concept-merged.pdf`（720 × 378 pt）；两版沿用已有图注与正文。导出时保留作者最新保存的排版和文字调整，不由早期构建脚本覆盖。采用与核验见 [来源记录](../../provenance/teaser-ppt-replacement-20261104.json)。

交付文件：`output/DriveCompose-teaser-placeholder.pptx`，单页；整图预览为 `output/DriveCompose-teaser-preview.png`。比例沿用原图 720:378；左侧为共享的多视图图像序列，按相机列、时间行排列，分叉至上方观测重建与下方 DriveCompose。下方保留中央大场景、补全小对照和右侧三种状态展示。外部标题、模块、流程箭头、共享输入和状态标签为原生可编辑对象；P2/P3/P4/P5a/P5b/P6a/P6b/P6c 是可独立替换的图片，P4 内部的四个标签和三条交互连接包含在素材中。

当前已填入 `docs/figures/teaser/p2-geometry-concept.png`、`p3-geometry-concept.png`、`p4-joint-completion.png`、`p5a-geometry-observed.png`、`p5b-geometry-completed.png`、`p6a-geometry-new-camera.png`、`p6b-geometry-vehicle-rotation.png` 和 `p6c-geometry-human-pose.png`。全部目标占位框、编号和说明已移除；P4 同时移除了原生占位标签与连接，避免重复。P5b 以新版 P5a 为编辑目标，在相应未知区域补入连续后部几何；原生的前后说明、比较箭头与图例保留。两个 P5 图框均保持现有 96 px 高度、底边及说明位置。

2026-11-03：用户确认的新版 P2、P3、P4、P5a/P5b 均已替换到原位置；P6a/P6b/P6c 本轮也已按同一造型和几何语义更新并放入。P2 的人物沿斑马线过街，车后背景为连续的大面积未重建区域；P3 取消车内剖视，以粗略虚线包络表示未知，并将缺少输入支持的人体正面标为未观测。P4 采用 P2 的造型、相机与姿态，金色补入连续的车辆后部结构、大范围车后道路和缺失墙段，保留三个组件与一个共享上下文之间的双向联系。更新版已覆盖回原路径。

新版 P5a/P5b 使用 `docs/figures/teaser/p5a-geometry-observed.png`、`p5b-geometry-completed.png`。两张图沿用新版车辆和同一观察方向；P5a 显示观测聚合后仍缺失的后部几何，P5b 在相应未知区域补入金色车尾、圆角、顶部续接和保险杠。设计、提示词与生成记录见 `docs/figures/teaser/p5-geometry-design.md` 及 `p5-geometry-generation-record.json`。本轮仅替换两张图片，70 个不相关元素、现有图框及外部文字保留。

P6 三张图分别、依次生成：P6a 与 P3 使用同一相机 s1，金色补入新显露的长侧车身、人体正面、连续车后道路及墙体背面；P6b 和 P6c 各自从 P4 参考状态 s0 出发，只改变车辆绕固定中心的偏航（目标约 45°），或只将人体双臂抬起并保留行走腿姿。它们不是从 P6a 连续累加状态。P6 保持原图框和外部状态标签，69 个不相关元素保留。状态设定见 `docs/figures/teaser/p6-geometry-state-contract.json`；生成来源与检查见 `p6-geometry-generation-record.json`，设计及全部提示词见 `p6-geometry-design.md`。

新版 P6 的替换脚本为 `.build/replace-p6-geometry.mjs`，插入前基线、验证及媒体对照位于 `.build/replaced-p6-geometry/`。早期 P6 素材和旧状态记录保持原路径，另保存于 `paper/build/teaser-p6-geometry/before/`。

图的核心关系：**多时刻、多视图汇总仍有未观测表面 → 利用共享场景上下文联合补全 → 同一批补全资产在不同状态下复用。**

## 上下对比的排版审查

本图采用两条方法路径：(a) Observation-only reconstruction；(b) DriveCompose。共享的 `Multi-view sequence` 在左侧只出现一次，不参与方法编号；右侧的处理、表示和复用阶段使用无编号标题。上下两行可以占用不同面积，但必须让共有条件与对应对象在图面上可辨认。分隔线从共享输入和分叉之后开始。

| 缺陷 | 对阅读的影响 | 本轮处理或素材要求 |
| --- | --- | --- |
| 上排整条路径标为 (a)，下排三个阶段标为 (b)(c)(d) | 编号混合了方法对比和流程阶段，容易被读成四个并列面板 | 改为两条路径 (a)/(b)，内部阶段使用无编号标题。 |
| 输入曾重复展示，合并后仍像三张独立照片 | 共有输入已明确，但没有表达时间序列与相机视角的两个维度 | 只展示一个相机 × 时间矩阵，列为 Front-left / Front，行为 t₀ / t₁ / t₂；时间箭头和省略号表示序列延续。整组以括线连接同一个分叉。 |
| 上排一个变化后场景，下排三种用途 | 无法判断失败与成功是否发生在同一状态 | P3/P6a 明确使用同一相机状态 s1；P6b/P6c 承担额外复用展示，不作为额外配对比较。 |
| 上下中央场景缺少明确对应 | 大图容易成为与上排无关的漂亮街景 | P2/P4 保持同一场景、参考状态 s0 和相机观察方向；P4 将场景整体缩放，为共享上下文标注留白。 |
| 未知区域与输入联合覆盖没有几何联系 | 人为缺口可能被误读成方法失败，补全则缺乏来源 | U 来自受控示意中的联合可见性；相同 U 在上排缺失、下排补全，并随状态变换保持表面对应。 |
| 联合补全只靠标题和上下文标签 | 容易只读成车辆局部补洞，跨组件机制没有体现 | 中央素材需表达背景与资产之间的信息交换及相关补全部位；P5 只解释覆盖与补全的局部前后关系。 |
| 信息在多个标签、脚注中重复 | 缩至论文栏宽时，小字和细纹会抢占主体辨识空间 | 删除长的上排总结句、缩短右侧标签；来源说明统一留在候选图注。占位编号在换入素材时移除。 |

下排保留较大的中央场景，用于说明本方法的组件与机制；这部分面积差异可以保留。后续应在论文实际插图宽度下检查补全标记和小对照，而不以 PPT 放大预览代替可读性检查。

## 素材与剩余占位要求

| 编号 | 放置内容 | 必须保持的对应关系 |
| --- | --- | --- |
| P1 | 同一片段的 Front-left / Front 相机，在帧 000 / 010 / 020 的六张示例图 | 相机按列、时间按行，原始图像使用 3:2 显示框。整组序列只出现一次，共同供给 (a)/(b)。六张示例不限定输入帧数或相机数。 |
| P2 | 汇总全部输入后的局部三维场景 | 选定具体未知表面 U，必须是所有输入联合覆盖后仍未观测到的区域。不能把单张图中的遮挡或图外区域直接当作 U。 |
| P3 | P2 场景在相机状态 s1 下暴露 U | 与 P6a 使用相同相机、裁切、资产和人体姿态；缺口与 P2 的 U 一致。 |
| P4 | 一个完整的联合补全场景，包含背景、车辆、人体 | 与 P2 保持同一场景、相机和参考状态 s0；显示三类内容的上下文关系。金色只落在选定的补全部位。 |
| P5a / P5b | 同一资产、同一视角，汇总全部观测后 / 联合补全后 | 轮廓、位置和已观测部分对应；同一 U 从未知变为补全。这个小对照承担“先汇总，再补全”的解释。 |
| P6a / P6b / P6c | 相机状态 s1 的配对展示，以及车辆旋转、人体姿态变化的额外复用示例 | 使用同一批资产和同一次补全样本；每张只改变标签所指状态。三条分支来自同一构建场景。 |

## 素材核对

- 当前输入使用 `overview-editable/assets/waymo-186/source/` 中帧 000、010、020 的 `FRONT_LEFT` 与 `FRONT` 原始 JPEG，共六张；均为 1920×1280，使用原生 3:2 图框完整显示，源图字节未重绘。
- 素材库中的 SIDE_LEFT f000 已能看到邮政车后门，它不属于本轮矩阵展示的两列相机示例。未知区域应由完整输入协议下的联合可见性确定，不能因某张 FRONT_LEFT 中看不到后门，就把整扇后门标作全部输入的未知区域。
- V01 与 V02 的记录 track ID 不同；当前资料未确认两者为同一实例。不能直接把两组裁切作为同一车辆的多视图证据。
- `A09-static-background.png`、`A10-canonical-vehicle.png`、`A11-canonical-human.png` 是生成式方法示意素材，可参考外观与构图。A11 对应 P01 深色外套人物，应保持人物身份一致。
- 图像裁切及预测 alpha 不等于三维可见性掩码。实际方法的 observed / free / unknown 三种状态不可混同；表面示意只画其中相关的表面区域。
- P6 当前使用受控的概念示意展示相机、车辆和人体状态变化，不作为实验结果图；后续若替换为真实渲染，应保留对应来源和条件。

时间对应来自同一目录的 `manifest.json`：t₀ 为 frame 000 / `1553735853362214` μs，t₁ 为 frame 010 / `1553735854362103` μs，t₂ 为 frame 020 / `1553735855362157` μs。图中 t 下标是所展示时刻的编号，不把这些采样帧写成连续帧，也不推定帧率。

## 图注候选

**From observations to reusable completed assets.** Given the same multi-view image sequence, (a) observation-only reconstruction leaves surfaces unseen across all inputs incomplete, while (b) DriveCompose jointly completes the background and canonical vehicle and human assets using shared scene context. The two routes are shown under the same changed camera state s1, exposing missing surfaces in (a) and the corresponding completed content in (b). Additional examples illustrate reuse under vehicle rotation and human articulation. Gold marks completed surfaces. Input images are from Waymo; the remaining panels are conceptual illustrations.

**从观测到可复用的补全资产。** 给定相同的多视图图像序列，(a) 仅基于观测的重建仍缺少所有输入中均未观测到的表面；(b) DriveCompose 利用共享场景上下文联合补全背景、规范车辆与人体资产。两条路径采用相同的变化后相机状态 s1，分别展示缺失表面的暴露及对应补全内容。其他示例展示车辆旋转与人体关节运动下的资产复用。金色表示补全表面。输入图像来自 Waymo，其余面板为概念示意。

上述图注对应当前全部素材已填入的概念示意版本。图面显示 `Conceptual illustrations`；若后续改用真实结果，应按具体面板更新来源说明。

详细占位要求、来源路径和双语候选图注也在幻灯片备注中。以上为素材制作记录；2026-11-04 已按用户指定将整页接入论文，候选图注未替换现有论文图注。

素材从现有 PPT 导入后局部替换，P2/P3/P4 的早期填入脚本为 `.build/insert-concept-assets.mjs`，P5 为 `.build/insert-p5-assets.mjs`，P6 为 `.build/insert-p6-assets.mjs`；各轮基线、素材哈希和删除对象记录分别位于 `.build/inserted-concepts/`、`.build/inserted-assets-p5/` 和 `.build/inserted-assets-p6/`。新版 P2 的局部替换脚本为 `.build/replace-p2-geometry.mjs`，关闭进程后的真实基线及核验位于 `.build/replaced-p2-geometry/after-close/`；新版 P3 为 `.build/replace-p3-coverage.mjs`，基线及核验位于 `.build/replaced-p3-coverage/`；新版 P4 为 `.build/replace-p4-completion.mjs`，基线及核验位于 `.build/replaced-p4-completion/`；新版 P5 为 `.build/replace-p5-geometry.mjs`，基线及核验位于 `.build/replaced-p5-geometry/`。原始占位构建脚本仍保留；再次运行会生成早期占位基线，不能据此覆盖当前交付文件。
