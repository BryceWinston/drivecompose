## 2026-11-06 图件归档与当前保留项

按作者重新编译、清理和提交的要求，未采用候选、原稿副本、对比预览、自动备份及旧检查／缓存已移至[仓库外归档](../../../_archive/drivecompose/20261106-recompile-cleanup/)。原文件逐字节保留，旧路径见[迁移清单](../../../_archive/drivecompose/20261106-recompile-cleanup/archive-manifest.json)，相关 Markdown 链接已指向归档原件；下方过程记录中以代码形式列出的旧路径按清单解析。

六份活动插图 PDF、当前 Teaser 的 draw.io 和预览、当前加框机制图的 SVG／PPTX 和预览、图 6 的 SVG 及六张结果原图继续保留。两版主稿图 3 仍引用 `paper/fig/fig03-joint-completion-core-boxed.pdf`；归档的 `fig03-joint-completion.pdf` 是此前版本，不是当前正文依赖。本轮未重绘或替换活动图件，四份论文已按当前源文件重编；[完整验收](../../paper/provenance/recompile-cleanup-20261106.json)。

---

## 2026-11-06 简化版 Teaser 正式采用

[正式图1](../../paper/fig/fig01-teaser.pdf)、[可编辑 draw.io](../../paper/fig/fig01-teaser.drawio)与[预览](../../paper/fig/fig01-teaser-preview.png)已同步为作者确认的 revision 4：1440×690画布、框外柔和分流箭头、删除 Background／Vehicle／Human 三个标签及对应连线、context 标题和向量居中于主场景上方。当前共有54个原生／组对象与14张独立位图。

中英文主稿已重编入稿，11／10页，完整正文止于第8／7页；源文及其余图件保持。最初原稿和替换前正式版均保留。[当前采用与验收](../../paper/provenance/teaser-style-adoption-20261106.json)、[两版首页预览](../../../_archive/drivecompose/20261106-teaser-context-adoption/layout-preview.png)与[修改对照](../paper-revision-changes.md)可核对。下方日期条目保留历史过程。

---

## 2026-11-06 确认的加框版图 3 已替换中英文主稿

按作者确认，将中英文方法源文中图 3 的插图路径由 `fig/fig03-joint-completion.pdf` 切换为 `fig/fig03-joint-completion-core-boxed.pdf`。只改两处路径，原中英文图注、图号、单栏宽度、技术正文和公式保持；原图及所有候选继续保留。

两版均已真实重编并替换正式输出：[英文主稿](../../paper/build/en/main.pdf)、[中文主稿](../../paper/build/zh/main_zh.pdf)。图 3 仍在两版第 4 页，约 83.34 × 50.14 mm；相比原图同宽放置约减少 3.46 mm 高度。英文／中文仍共 11／10 页，完整正文止于第 8／7 页。

已检查图 3、前后页、完整总结页及中文第 6 页的既有结果浮动页。批准图中的 83 条矢量绘制、24 个原生文字和 16 处矢量渐变均在两版编译 PDF 中匹配；图注源文和渲染文字均保持。Poppler 复核没有新增裁切、重叠或浮动异常，无新增最终编译警告。全量检查器 80 项中既有历史图源失败由 5 项减为 4 项，没有新增失败；旧图源问题未在本轮扩展处理。

[中英文第 4 页排版预览](../../../_archive/drivecompose/20261106-figure3-boxed-adoption/layout-preview.png)与[本轮采用、编译及验收](../../paper/provenance/figure3-boxed-adoption-20261106.json)可直接核对。两版补充材料及其他图件未改，未重编补充材料。编译中间文件和真实修改前基线保存在外部归档。

---

## 2026-11-06 图 3 加框与连线留白候选（保留当前版）

按作者标出的连线问题，将三组左上特征用一层细浅蓝灰框归为同一集合，替代两侧括号。另存[加框候选 PDF](../../paper/fig/fig03-joint-completion-core-boxed.pdf)、[SVG](../../paper/fig/fig03-joint-completion-core-boxed.svg)、[可编辑 PPTX](../../paper/fig/fig03-joint-completion-core-boxed.pptx)与[预览](../../paper/fig/fig03-joint-completion-core-boxed.png)。[同尺度前后对照](../../../_archive/drivecompose/20261106-figure3-boxed-candidate/comparison.png)左侧为保留的当前版，右侧为本轮候选。

| 位置 | 当前版（保留） | 加框候选 | 原因 |
|---|---|---|---|
| 左上特征边界 | 左右两根括号 | 一层白底细浅色框，不加标题 | 明确三组特征属于同一集合，给连线提供清楚边界 |
| 红框所指更新线 | 从括号下方伸出，经过两次直角转折 | 从框右下侧出线，以一条平滑曲线进入投影框顶部中心 | 消除悬空起点与阶梯折线，清楚衔接约束更新 |
| 箭头交接 | 多处贴近边框 | 主要箭头起止处统一留 10 个原生单位白隙 | 按作者补充要求保持端点清爽 |
| 掩码速度公式 | 紧邻原竖直线 | 仅右移 65 个原生单位，字形、字号、内容不变 | 与新曲线分开，避免挤靠 |

特征色块、组内注意力小箭头、记忆内容、投影与状态条保持。99 个原生对象，含 24 个文本、68 个可编辑路径、7 个椭圆；13 个逻辑分组及独立外框，无图片。六处科学图形区域的实际 PDF 渲染逐像素一致，全部文字内容、字体、字号及颜色保持。新版沿用此前可编辑源的数学上标间距；与旧 PDF 的极小上标位置差异已记在验收中。

已通过独立文件构建和 WPS 新副本导出核对，随后检查 Poppler、SVG、单栏彩色／灰度和并排预览。当前版四个交付文件及全部原图 3、图注源文哈希保持；本轮没有替换论文选图、修改图注或重编正文。[设计、精确修改清单与验收](../../paper/provenance/figure3-boxed-candidate-20261106.json)可追溯。本轮为局部自审，连接线仍为可编辑自由曲线，移动模块后需调整端点。

---

## 2026-11-05 确认版 Teaser 正式采用

作者确认的 [Teaser PDF](../../paper/fig/fig01-teaser.pdf)已替换中英文首页，匹配的[可编辑 draw.io](../../paper/fig/fig01-teaser.drawio)及[预览](../../paper/fig/fig01-teaser-preview.png)同时保存。独立候选的布局、标题、箭头留白及已纠正的场景空间关系与人体未观测面均原样采用。

中英文主稿真实重编后为 11／10 页，完整正文仍止于第 8／7 页；新局部图像的嵌入像素与确认图一致。原始 PDF 和 draw.io 继续保留，PPT 历史来源不被冒充为当前可编辑稿。图注及技术正文保持，仅英文工具说明补记本次 Image Gen 示意图修订。[采用、来源和核验](../../paper/provenance/teaser-coordinated-preview-20261105.json)及[修改对照](../paper-revision-changes.md)可追溯。

---

## 2026-11-05 图 3 核心机制矢量重建，删除 CCM 标题并统一 N

按作者“改成矢量图，且不要 CCM 标题”及随后“S 换成 N”的要求，基于已选光栅预览重建[矢量 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.pdf)、[SVG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.svg)、[可编辑 PPTX](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.pptx)及[PDF 渲染预览](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.png)。原稿、全部此前候选和中英文图注保持；本轮没有替换论文选图或重编正文。

| 位置 | 上一版预览 | 本轮矢量版 |
|---|---|---|
| 表现形式 | 1536 × 1024 的光栅图 | 100 个原生文字／几何对象，14 个逻辑分组，无图片；SVG、PPTX 与矢量 PDF |
| 顶部标题 | CCM | 删除，并裁去顶部仅含标题的 100 单位画布；其余对象保持原相对位置 |
| 迭代与终态 | ×S，z 的 S 上标 | ×N，z 的 N 上标 |
| 科学结构 | 组件局部特征、共享记忆读写、掩码速度及投影更新 | 保持，数学符号用原生文字项重建 |

本轮通过独立原生 OOXML 文件构建，再由本机 WPS Presentation 后台打开同一 PPTX 并导出，未声称使用 Microsoft PowerPoint。最终 PDF 有 83 条矢量绘制记录、24 个原生文本对象、零位图，字体已嵌入。SVG 有独立文字、曲线、色块和斜线；不是把整张 PNG 包进 SVG。PPTX 的 69 个自定义路径、7 个椭圆和 24 个文字对象可分别编辑。

已查看 WPS 导出、实际 PDF 的 Poppler 全图、SVG 的 CairoSVG 渲染，以及 83.34 mm 单栏彩色／灰度预览；修正上标间距后重新导出并核验。连接线为可编辑自由曲线，移动模块后需手动调整端点；数学式由独立文本项构成。图 3 原稿、此前候选与图注源文哈希保持；同期另一任务修改的图 1 与使用说明保留，未回退或计入本轮修改。本轮为有前文背景的自审。[来源、对象清单与验收](../../paper/provenance/figure3-core-vector-20261105.json)可追溯。

---

## 2026-11-05 图 3 核心机制重绘预览

按作者“只突出核心机制，布局简洁紧凑，保留原稿，图注不变，先看看效果”的要求，另存[核心机制预览 PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-preview.png)。保留全部原图和此前矢量候选；当前论文选图及中英文图注未改，未重编论文。

| 位置 | 上一候选 | 本轮预览 |
|---|---|---|
| 记忆交换主体 | M / M′、U 和较多独立中间状态 | 一组组件特征、一组共享记忆，用方向相反的读／写箭头呈现交换 |
| 更新机制 | 独立速度头、加法节点、展开 Euler 算术和中间状态 | 未知掩码速度边、紧凑 Π 算子及一条 ×S 回路 |
| 约束效果 | 大幅状态条与末端符号 | 成对的小状态条：观测格、自由空间零值保持，未知格变化 |

本轮使用内置 Image Gen 生成光栅视觉草稿；没有声称交付可编辑矢量源或最终出版图。参考作者提供的另一篇论文示意图，仅借鉴信息取舍、短标签、特征图形与更新回路，未沿用其采样／投影的科学拓扑。首稿的重复 M 和灰色输入箭头落点已通过 Image Gen 修正，随后检查整图、单栏和灰度预览。

[完整最终提示词](../../../_archive/drivecompose/20261105-figure3-core-preview/prompt.txt)与[设计、来源和验收](../../paper/provenance/figure3-core-mechanism-preview-20261105.json)可追溯。提示词按绑定机制模板检查；原稿、此前候选、正式稿件与图注共 71 项文件哈希保持。本轮为有前文背景的自审，预览供作者判断构图效果。

---

## 2026-11-05 图 3 候选的全图联动修改

按作者“修改”的要求，已将上轮三项全图建议落实到独立[候选 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)和[PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.png)。[同尺度全图对照](../../../_archive/drivecompose/20261105-figure3-global-revision/comparison.png)保留相同的原英文图注。

| 位置 | 修改前 | 修改后 |
|---|---|---|
| 全图与中间连线 | 964.08 × 620 pt；模块间跨度 404.93 pt | 820 × 570 pt；跨度 335.70 pt，联动重排记忆、U 与采样链 |
| 两侧特征三行 | 行中心和 token 尺寸略有差异 | 三行严格对齐，统一 35.41 pt 方形 token |
| M / M′ | token 和容器大小不一致 | 均为 194 × 46 pt 条带，token 均为 28 × 28 pt |
| 算子与输出 | 两根匿名黑线；Velocity head；Completed | Attn 的 r / w 下标；v 的 θ 下标；保留 z 的 S 上标 |
| 投影与最终输出框 | 宽 164.30 / 217.42 pt | 宽 92 / 80 pt，保留原投影公式和最终状态 |

**原稿、图注和正式论文保持。** 本轮保留修改前候选，未更改 LaTeX 选图或重编论文，也未向图中补回一般解释性备注。原生画布面积减少 21.80%；按同一 83.34 mm 单栏宽放置时，内容相应放大，图高由 53.60 mm 变为 57.93 mm。

最终 PDF 含 112 个矢量对象、34 个原生文本对象、无位图面板。保留的 28 个原文字形、字体、字号和颜色均核对；70 项原有文件（含原图注与主稿）哈希保持。已查看新的 Poppler 全图、同尺度对照和单栏彩色／灰度预览，修正 M′ 标签图层遮挡；未观察到新增裁切、遮挡或含糊交叉。本轮为有前文背景的自审，未声称独立盲审或取得匹配 draw.io / PPTX 源稿。[参数与验收](../../paper/provenance/figure3-global-revision-candidate-20261105.json)可追溯。

---

## 2026-11-05 收紧图 3 候选局部模块的空白

按作者截图，继续收紧[候选 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)和[候选 PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.png)的左侧局部注意力模块。外框宽度由 361.18 pt 减至 261.18 pt，缩小 27.69%；高度由 250.70 pt 减至 238.70 pt，局部面积减少 31.15%。符号到 token 的横向间距由 87.82 pt 收至 32.82 pt，减少 62.63%。

token 尺寸、符号字号、公式、配色及连接关系保持。三行稍作靠拢，括号与外框相应缩短；只调整受影响的输出与反馈连线端点。图注、原稿和当前论文保持，未重编或替换主稿。[等比例局部对照](../../../_archive/drivecompose/20261105-figure3-symbol-compact/comparison.png)可直接比较。

仍为 113 个矢量对象、30 个原生文本对象、无位图面板；局部模块及关联连线之外在 72／144 dpi 下逐像素一致。68 项原有文件（含原图注）哈希保持，前一候选保存在本轮归档。详细参数、哈希与验收见[本轮记录](../../paper/provenance/figure3-symbol-compact-candidate-20261105.json)。

---

## 2026-11-05 图 3 候选区域符号化，图注沿用原文

按作者要求更新独立[候选 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)和[PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.png)：`Local attention` 改为 Attn 的 g 下标，`Background / Rigid / Human` 分别改为 X 的 b／r／h 下标。保留上一候选中的 Π 算子，其他公式、形状、连线、位置和尺寸保持。

**图注不改。** 前一轮扩写图注的提案已撤回并存档；候选配套文本恢复为原中英文图注。[并排预览](../../../_archive/drivecompose/20261105-figure3-symbol-candidate/comparison.png)两栏采用相同的原英文图注。正式论文与原图不变，未重编或替换。

四处标签区域之外在 72／144 dpi 下逐像素一致，113 个矢量对象及其余 22 个候选文本对象保持；当前候选共有 30 个原生文本对象、无位图面板。66 项原有源文、图件及 PDF 哈希保持。原稿、上一候选及撤回的图注均已保存，详见[本轮来源与验收](../../paper/provenance/figure3-symbol-candidate-20261105.json)。

---

## 2026-11-05 图 3 的独立算子标注候选（保留原稿）

按作者“改一版看看效果，保留原稿”的要求，另存[候选图 3 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)与[PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.png)。仅把原 `Projection` 标签替换为原生数学算子 Π 及斜体 m,f 下标；模块边框、公式、连线、位置、尺寸和其他标签保持。算子框之外在 72／144 dpi 下逐像素一致。

[中英文候选图注](../../../_archive/drivecompose/20261106-recompile-cleanup/files/docs/figures/fig03-joint-completion-revised-caption.txt)解释局部组示例、三类状态及约束恢复，未向图内补回解释性备注。[原稿／候选等尺寸并排预览](../../../_archive/drivecompose/20261105-figure3-operator-candidate/comparison.png)按 83.34 mm 单栏宽度展示，文字解释放在图下。

原 `fig03-joint-completion.pdf`、两版主稿 PDF 和中英文方法源文全部保持原哈希；当前论文仍用原图与原图注，本轮未重编论文。63 项既有源文、图件和 PDF 文件保持。候选为 113 个矢量对象、26 个原生文本对象，无位图面板。原件、脚本和渲染位于外部归档，完整证据见[候选验收](../../paper/provenance/figure3-operator-candidate-20261105.json)。

---

## 2026-11-05 收紧图 3 删除文字后的空白

[当前图 3 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion.pdf)已收紧上下流程的间距：下方采样链和循环上移，公式及速度头相应靠拢，缩短受影响的连接线，并裁去顶部和底部多余画布。宽度不变，图高由 760 pt 减至 620 pt，减少 18.42%。

全部剩余文字、公式、符号、字号、配色、模块尺寸和连接关系保持，仍为原生矢量 PDF。两版主稿已同步重编，并保留另一任务同期更新的图 1；图 3 均在第 4 页，英文／中文正文仍止于第 8／7 页。独立图件和两版论文页经 Poppler 复核，无新增裁切或重叠。[布局操作与验收](../../paper/provenance/figure3-compact-layout-20261105.json)及外部归档中的复现脚本可追溯。

---

## 2026-11-05 删除图 3 的六处指定文字

[当前图 3](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion.pdf)已继续删除五张截图标出的六处文字：`Cross-component context`、`Shared memory`、`Fixed query layout`、`Constrained update`、`(unknown only)` 和 `after S`。保留其余公式、符号、文字、形状和连线，页面尺寸保持。

六处区域之外在 72／144 dpi 下逐像素一致，其余文本对象和矢量对象保持。两版主稿均已重编并保存，图 3 均位于第 4 页；英文／中文正文仍止于第 8／7 页。[本轮操作与验收](../../paper/provenance/figure3-label-removal-20261105.json)可追溯，前后图和截图留在外部归档。

---

## 2026-11-05 删除图 3 底部图例

[当前图 3 PDF](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion.pdf)已删除作者截图中的 `Observed / fixed`、`Unknown / updated`、`Free / zero` 三项图例、对应符号和外框，并收紧底部画布。保留区域在 72／144 dpi 下逐像素一致，仍为原生矢量内容。

中英文主稿同步重编；图 3 均位于第 4 页，正文仍止于第 8／7 页。其余正文源文、图件与补充材料保持。匹配的 draw.io 源稿未在本机检出中找到，本轮直接修改现用 PDF；[本轮验收](../../paper/provenance/figure3-legend-removal-20261105.json)记录精确操作与源稿状态，历史变体未修改。

---

## 2026-11-05 按 CVPR 范例建议完成独立修改稿

已按作者授权另存[修改稿 draw.io](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-revised.drawio)和[预览 PNG](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-revised.png)，[原稿与修改稿并排预览](../../../_archive/drivecompose/20261105-teaser-revised/before-after-comparison.png)可直接比较。保留共享输入与上下对照，压缩淡化上方流程框；补未见面的原生斜线、视角列标签和相机符号；底部改为同位置车尾局部对照；右侧改为相机全景、车辆近景、人体两姿态近景，并添加可编辑的动作及金色上臂表面标记。

当前共有 109 个对象，其中 94 个原生构件、15 个独立图片。图内保留标签最小有效字号约 8.07 pt，区域标题约 9.53 pt，按 174.625 mm 跨栏宽计算。六张输入照片字节不变，五个局部裁剪逐像素核对；新文件由 draw.io Desktop 重新打开，结构审计 0 个硬错误。独立灰度阅读与揭示主张后的彩色比对已记录；上方浅色场景外轮廓仍可作为后续可选微调。

[修改与验收记录](../../paper/provenance/teaser-revision-20261105.json)和[实际前后对照](../paper-revision-changes.md)可追溯。原稿 draw.io、原版／调整版 PDF 及两版论文入口文件哈希均保持；论文继续使用原选图，本轮未替换或重编论文。

---

## 2026-11-05 原稿 teaser 的 CVPR 范例调研与改进建议

本轮核对六篇 CVPR 2025–2026 主会录用论文的 Fig. 1，审阅当前原稿 draw.io，并完成两轮隐藏标题灰度图的独立阅读测试。结论、范例来源、实际尺寸和对象级建议见[调研与改进报告](teaser-cvpr-review.md)，[六篇对照图](../../../_archive/drivecompose/20261105-teaser-cvpr-review/cvpr-teaser-reference-sheet.png)可并排查看。优先建议是强化补全前后对照、扩大车辆和人体动作、明确补全表面的状态对应并提高小字可读性。底部对照的信息价值应先迁入主视觉再合并，不能直接删去。

本轮仅提出意见，当前 draw.io、现用图一 PDF 和论文未修改。[来源与检查记录](../../paper/provenance/teaser-cvpr-review-20261105.json)保存本轮起止哈希和审阅证据。

---

## 2026-11-05 原稿 PPT 转为可编辑 draw.io

按作者最新要求，以本机提供的 `fig01-teaser.pptx` 为唯一版式来源，直接转换为[原稿 draw.io](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.drawio)，保持原稿布局，未套用调整稿。68 个 PPT 对象全部对应，源稿的文字及非连接线对象位置、尺寸逐项相同。原 PPT、原版 PDF 与调整版 PDF 的 SHA-256 均未变化；论文仍引用原版 PDF。

最终含 95 个独立对象：29 个文本、23 条线或连接线、28 个形状（含一个锁定白色画布背景）、15 张内嵌图片，其余 94 个对象可编辑、移动。14 张图片保留原始字节；主场景底图仅通过 Image Gen 去除原有烘焙标注，再按原稿位置用原生标签、框、锚点、曲线和共享上下文色块复建。六张真实输入照片未作生成式修改。

已用 draw.io Desktop 重新打开最终文件，核对所有内嵌图片和原生对象，并导出[预览](../../../_archive/drivecompose/20261105-teaser-drawio/fig01-teaser-original-preview.png)。原生结构审计为 0 个硬错误；主场景大图的尺寸提示已核对为单张连续场景。此次验收限于忠实转换与可编辑性，原稿字号和构图不作美化。[完整来源、逐对象清单和验收](../../paper/provenance/teaser-original-drawio-20261105.json)可追溯。

---

## 2026-11-05 单栏组件消融图与对应分析入稿

新增 [图 6 PDF](../../paper/fig/fig06-component-ablation.pdf) 和 [SVG](../../paper/fig/fig06-component-ablation.svg)，使用六张作者提供的真实消融结果，按两场景、三方法排布；列顺序为 Ours、w/o CCM、w/o GCM。单栏尺寸 83.34×54.44 mm，Times New Roman 标签 9 pt。全景保留原幅，宽框和方框对应下方同坐标裁剪；原生图像像素和色彩不变。

[源图目录](../../paper/fig/source/component-ablation/)与[生成脚本](../../paper/tools/make_component_ablation.py)随工程保留。两版主稿的图 6 分别位于英文第 8 页、中文第 7 页。18 张内嵌图像与原图及裁剪逐像素一致；[来源与验收](../../paper/provenance/component-ablation-figure-20261105.json)可追溯。本轮未修改图 1–5。

---

# 论文图件

## 2026-11-05 原版与调整稿分开保留（当前选择）

按作者要求，原路径恢复为最初原版，最新调整稿另存，供直接比较：

- [原版 PDF（当前论文图一）](../../paper/fig/fig01-teaser.pdf)
- [调整稿 PDF（供比较）](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-layout.pdf)
- [同尺度并排预览](../../../_archive/drivecompose/20261105-teaser-version-comparison/fig01-teaser-comparison.png)

两份 PDF 均核对了原始文件哈希，首轮调整版本继续留在既有归档中。LaTeX 仍引用原版路径，本轮不重编论文。当前选择及调整稿的历史验收分开记录在[版本与来源](../../paper/provenance/teaser-layout-20261105.json)中。

---

## 2026-11-05 子图尺度与连线复核（调整稿，现已另存）

根据作者指出的左右分叉线和长标题，再次更新[活动图一 PDF](../../paper/fig/fig01-teaser.pdf)。本轮按实际可见主体校正各图大小：主场景约为一个状态场景的 2.26 倍宽，三幅状态图可见宽度差小于 0.35 pt，输入帧与辅助车辆分别共用尺寸和间距。图像本身保持原字节，通过 PDF 裁剪窗口去除外侧空白，并保留边缘余量。

输入括线与分支合并，去掉中央短横线；右侧三叉小箭头改为一条完整箭头接三个状态的分组括线。`(b)` 缩短为 `DriveCompose: joint completion`，资产复用由右侧标题说明；图例移到主场景空白角，辅助车辆标题置于图像上方。已查看 Poppler、实际跨栏尺寸及灰度预览，原生文字无重叠或裁切。上一轮版面自审由本轮反馈复核接续。

前后尺寸与具体理由见[修改对照](../paper-revision-changes.md)，当前哈希及验收见[来源记录](../../paper/provenance/teaser-layout-20261105.json)。[本轮归档](../../../_archive/drivecompose/20261105-teaser-layout-refinement/)保存首轮 PDF、作者截图、重排脚本和预览。仅更新独立图一与记录；主稿 PDF 未重编。

---

## 2026-11-05 首轮重排（已由上方版本替代）

作者本轮指定的[图一 PDF](../../paper/fig/fig01-teaser.pdf)已在原路径更新。保留其上下对照、共享输入、全部 15 张原始图像及标签信息，缩小并淡化上方流程框，放大相邻场景，统一分区标题、右侧三行状态示例、字号和间距。图例与状态标签按 495 pt 跨栏宽度约为 8 pt；画布尺寸保持。文字、箭头、图例和分隔线为原生 PDF 对象，场景中的嵌入标注沿用原图像。

该修改针对现有活动 PDF，与下方独立矢量候选是不同产物。当前检出没有与活动图一匹配的 PPTX；本轮没有声称同步修改 PPT。两版主稿 PDF 未重编。原件、复现脚本、版面规范和预览均存放在[本轮归档](../../../_archive/drivecompose/20261105-teaser-layout/)，实际前后对照见[修改记录](../paper-revision-changes.md)，当前活动哈希及验收见[版式记录](../../paper/provenance/teaser-layout-20261105.json)。

---

## 2026-11-05 候选稿的矢量重建

按作者“绘制为矢量图”的要求，将上一轮几何候选重建为独立矢量版，保留构图和文字，不替换当前论文图一：

- [SVG 矢量源图](../../../_archive/drivecompose/20261105-teaser-vector/deliverables/fig01-teaser.svg)
- [矢量 PDF](../../../_archive/drivecompose/20261105-teaser-vector/deliverables/fig01-teaser.pdf)
- [可编辑 PPTX](../../../_archive/drivecompose/20261105-teaser-vector/deliverables/fig01-teaser.pptx)
- [WPS 实际导出预览](../../../_archive/drivecompose/20261105-teaser-vector/deliverables/fig01-teaser.png)

| 上一轮状态 | 本轮产物 | 核验 |
|---|---|---|
| 整张生成式 PNG | 542 个原生文字／矢量形状，13 个逻辑分组，含 348 个自定义路径 | 检查实际 PPTX 包结构及稳定对象名；SVG 含原生文本、路径和渐变 |
| 生成式输入缩略图 | 4 张从当前图一原 PDF 提取的真实输入图像，分别嵌入 | SVG 和 PPTX 保留原图字节；图框、时间／视角标签独立 |
| 场景、车辆、人体和补全斜线不可分开编辑 | 按道路、墙面、车身、车顶、车轮、人物肢体、标记和引线等重建 | 场景中没有整面板截图或自动描摹像素块 |
| 只有光栅预览 | WPS 从与最终文件字节相同的 PPTX 重新导出 PDF 和 PNG | 最终 PDF 仅含 4 张照片、355 条矢量绘制记录，文字可提取且两套 Times New Roman 字体已嵌入 |

原候选的柔和光影以矢量色面和渐变近似。连线为可编辑自由路径，移动分组后需要手动调整端点；这是一张二维矢量插图，不是可旋转的三维模型。当前本机接口实际连接 WPS Presentation，未使用 Microsoft PowerPoint。完整导出已查看；独立盲审和标题隐藏副本的目标应用审阅未完成，不宣称最终出版审查通过。过程、修正与源稿保护核验见[重建记录](../../../_archive/drivecompose/20261105-teaser-vector/verification.json)和[编辑说明](../../../_archive/drivecompose/20261105-teaser-vector/deliverables/README.txt)。未改正文、图注、当前活动图或提交／推送。

---

## 2026-11-04 待确认的 teaser 候选

按作者“改一版出来待我确认”的要求，基于最新几何 teaser 生成[候选预览](../../../_archive/drivecompose/20261104-teaser-revision-preview/candidate.png)。保留共享输入和几何画风，将输入缩为两时刻×两视角的示例矩阵；删大蓝框和重复车辆前后条带；给缺失区域加灰色斜线、补全区域加金色标记；将车辆与人体状态改为近景，并局部修正车辆转向，使其与主场景方向明显不同。等宽插入时候选约高 71.6 mm，原图约 91.7 mm；这是候选比例计算，尚未重排论文。

候选由内置 Image Gen 生成，1959 × 803，属于概念构图预览。查看了原分辨率、缩小图和灰度图；输入缩略图不声称保持实测原始像素，正式原生重建可从已提取的原始帧无损回填。本轮未写入正式图件、论文、图注或 PPT。当前 `fig01-teaser.pdf` 和两版主稿保持原字节，候选等待用户确认。

[完整最终修正提示词](../../../_archive/drivecompose/20261104-teaser-revision-preview/refinement-prompt.txt)含 26,040 个非空白字符，超过绑定模板的 15,356 个，且低于工具总字符上限；原始全图提示词、首稿、规格及核验见[生成记录](../../../_archive/drivecompose/20261104-teaser-revision-preview/generation-record.json)。未提交或推送。

---

## 2026-11-04 最新 teaser 审阅与优化建议

本次按作者要求拉取远端，分支从 `edcd19c` 快进到 `5b46f9e`，当前采用的图一是 [fig01-teaser.pdf](../../paper/fig/fig01-teaser.pdf)，不是上一轮的写实对齐草稿。新图保留共享多视角序列，主体为统一的三维几何示意，原生 PDF 文字和线条可提取。本轮只审阅和给出改法，没有重新生图、改动图一或修改论文图注。

采用 `audit-scientific-figure` 检查当前原图、全图灰度与跨栏尺寸预览，再由 `design-scientific-figure` 将问题整理为设计建议。属于已知论文内容的自审，不声称独立盲审或完成了 PPT 原生对象验收。[本轮同步与审阅记录](../../paper/provenance/teaser-latest-review-20261104.json)、[新图渲染](../../../_archive/drivecompose/20261104-teaser-latest-review/latest-teaser.png)、[缩小预览](../../../_archive/drivecompose/20261104-teaser-latest-review/latest-teaser-publication-preview.png)及[逐文字号](../../../_archive/drivecompose/20261104-teaser-latest-review/latest-teaser-text-metrics.json)可核对。

**建议保留：** 共享输入；明确的时间／视角两个维度；背景、车辆、人体的几何载体；补全后复用同一资产的主线；当前淡色几何画风。优化从这些已有内容接续，不套回旧的写实草稿。

### 优先修正的三项

| 优先项与位置 | 当前原图可见问题 | 具体改法 | 验收方式 |
|---|---|---|---|
| 1. 上方 `Unseen regions exposed` 及右侧三种复用 | 未观测表面主要以白面／浅色轮廓表示，缩小或转灰度后融入底色。右上复用图的人体存在相邻紫／金轮廓，大面积金色也缺少与中央补全区域的对应提示。现图不能单凭投影视角证明标记错误，但读者难判断表面归属是否保持。 | 给缺失区域使用统一灰色边界或稀疏斜线；金色仅作为补全标记，随所属背景、刚体和人体传播。选一个车身区域、一个人体区域，用同一边界／小锚点贯穿中央图和新状态图。若需要旧姿态轮廓，改为明确的细灰虚线，不用两个人体主色叠放。 | 灰度及跨栏尺寸下能找到未观测表面；相机移动只改变可见性，车转动和人体换姿时对应补全区域随资产变化。 |
| 2. 上方两个大蓝框、下方车辆前后小条带 | 上方流程框比局部几何变化更醒目；中央大图已展示车辆补全，下方又重复一次，右侧三张复用图被挤小。上下比较的终点也没有直接对齐。 | 保留上下问题／方法两条叙事，将 `Observation-only reconstruction` 和 `State-driven rendering` 压为短行标签或小操作节点；删去下方重复车辆条带，图例移入主图留白；将释放的空间用于右侧三种状态。右侧相机图保留全场景，车辆与人体两图裁为对应对象的近景。 | 首眼看到缺失表面→联合补全→状态复用；车辆旋转和人体姿态不再需要放大整页辨认。 |
| 3. 图例和状态标签 | 按当前跨栏宽度，`Observed / Completed` 约 4.97 pt，右侧 `Camera view / Vehicle rotation / Human pose` 约 5.50 pt；核心说明依赖过小文字。 | 主标签以约 9 pt、次要标签至少约 8 pt 作为项目工作目标，统一层级；删 `Also: rotation and articulation`，它重复右侧已有标签；删／压缩重复的 `(a)/(b)` 长标题。输入可改为 2 时刻×2 视角的示例矩阵，保留时间与视角维度，`Example frames` 的语义移入图注。 | 按最终插入宽度重新计算字号，直接看整页能读出图例、状态及补全含义；不通过缩字挤内容。 |

这些字号是当前 PDF 原生字体大小乘以 `495 / 1350` 得到的实测值，不是估计截图 DPI。当前原图为 1350 × 708.72 pt，跨栏约 174.6 × 91.7 mm。建议通过去重把宽高比从约 1.90:1 调整至约 2.4–2.6:1，作为待排版验证的目标：相同宽度下图高约 67–73 mm，减少约 21%–27%。这不是已执行的首页重排结果，也不要求一律达到某个比例。

### 下一版建议构图

左侧继续只保留一组多视角序列；上方为紧凑的“观测覆盖→状态变化→缺失显露”对比条；下方保留较大的联合补全几何场景，右侧排列相机、车辆、人体三种复用。共享上下文只用一条局部关联和短标签，已有大场景承担补全解释，不再另加一条完整车辆前后对比。

所有新状态图都从同一套几何和补全区域定义出发。保持相机、车辆、人体干预的条件清楚，避免因视角变化导致金色显示面积变化时被误读为重新生成。画面只说明补全与绑定，不新增闭环、未来预测、360° 覆盖或实验性能结论。

### 图注建议（未写入论文）

当前两版图注将全部 scene and asset images 概括为示意，而当前来源记录区分 Waymo 输入帧与概念几何。建议明确这一界限，并使图注只解释本图可见内容。

English:

> **Completing scene components for reuse.** Example multi-view frames reveal only partial surfaces (a). Joint completion fills missing background and actor content, which is reused under camera shifts, vehicle rotation, and human pose changes (b). Gold marks completed regions. Input frames are from Waymo; the 3D scenes and assets are schematic.

中文：

> **补全场景组件以供复用。** 示例多视角帧只能提供部分表面（a）。联合补全填充背景与参与者的缺失内容，补全后的组件在相机移动、车辆转动和人体换姿时复用（b）。金色表示补全区域。输入帧来自 Waymo，三维场景与资产为概念示意。

本轮保留全部本地未提交的消融、补充材料与已编译 PDF，恢复后仅接入远端图件路径映射并合并双方记录。主稿 PDF 因被其他程序占用而保持原文件，本轮审阅直接渲染新 `fig01-teaser.pdf`，没有将旧主稿首页冒充新图的编译结果。备份、局部恢复补丁及核验统一存放在[本轮归档](../../../_archive/drivecompose/20261104-teaser-latest-review/)。当前检出没有可编辑 PPT 原件，本轮未操作 PowerPoint。

---

全部正式图件统一放在 [`paper/fig/`](../../paper/fig/)，按论文图号使用 `figNN-英文短名`；同一图的 PPTX 与 PDF 使用相同文件名。

下表五份图件 PDF 是论文编译依赖，随源码纳入 Git；拉取后无需另行复制图件。可编辑 PPT、论文编译输出、历史素材和仓库外归档不随本次提交上传；这些文件不参与论文编译。当前编译结果 JSON 和哈希记录对应本机最终文件。

| 图号 | 内容 | PDF | 可编辑源稿 |
|---|---|---|---|
| 1 | 观测、联合补全与资产复用 teaser | [当前 fig01-teaser.pdf](../../paper/fig/fig01-teaser.pdf) | [正式 draw.io](../../paper/fig/fig01-teaser.drawio)，文字与箭头原生可编辑；14 个场景/输入位图独立保留 |
| 2 | 方法总览 | [fig02-overview.pdf](../../paper/fig/fig02-overview.pdf) | [fig02-overview.pptx](../../paper/fig/fig02-overview.pptx) |
| 3 | 联合补全机制 | [fig03-joint-completion.pdf](../../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion.pdf) | 当前为直接编辑的原生矢量 PDF；[来源状态](../../paper/provenance/figure3-compact-layout-20261105.json) |
| 4 | 动态重建结果 | [fig04-dynamic-reconstruction.pdf](../../paper/fig/fig04-dynamic-reconstruction.pdf) | 未提供原生 PPT 源稿 |
| 5 | 轨迹外渲染结果 | [fig05-off-trajectory-rendering.pdf](../../paper/fig/fig05-off-trajectory-rendering.pdf) | 原件为 PDF，未提供 PPT 源稿 |

图 1 当前正式路径采用作者确认的 `fig01-teaser-style-preview.pdf` revision 4，并同步匹配的 draw.io 源与预览。最初原稿保留为 `fig01-teaser-original.pdf` 和 `.drawio`，替换前正式版保存在本轮外部归档。当前图共有 54 个原生或组对象与 14 个独立图片；新视角缺失场景为独立的 Image Gen 机制示意，其余 13 张原图保持，六张 Waymo 输入照片未修改。图 2 PDF 采用作者指定原件。图 1 的输入缩略图来自 Waymo，场景与资产面板为概念示意；图 2、3 为机制说明。图 4、5 保留原实验图内容。

图 3 采用同事本次同步的修正后矢量 PDF，原生可编辑 draw.io 源稿保存在同步归档中。图 4 的 PNG 无损封装为 PDF，未裁切、重绘或重采样，内嵌像素与原件一致。图 5 只改路径与名称，PDF 字节不变。

旧候选、分图素材、提示词、预览、构建脚本及历史快照移至[仓库外归档](../../../_archive/drivecompose/20261104-figure-cleanup/)。可重建的 `node_modules` 依赖路径不作为恢复原件。归档中 `files/` 保留原项目相对路径；`before/` 保存本轮修改前的说明、源码与主稿 PDF。

图 1 当前哈希及入稿验收见[2026-11-06 确认版记录](../../paper/provenance/teaser-style-adoption-20261106.json)；其余图件哈希与旧路径见[图件布局记录](../../paper/provenance/figure-layout.json)，逐文件归档及核验见[归档清单](../../../_archive/drivecompose/20261104-figure-cleanup/archive-manifest.json)，本轮修改理由见[改动对照](../paper-revision-changes.md)。后续修改直接更新同名最终文件；临时输出放在仓库外，避免在图目录积累日期版或预览副本。
