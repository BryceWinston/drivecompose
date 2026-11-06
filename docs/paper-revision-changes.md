## 2026-11-06 当前源文件重编、临时文件归档与提交

本轮执行作者“重新编译，并清理临时文件，然后提交并推送”的要求。真实起点为 `5b46f9eb8e131314430a2f2fa5193dadd16dc296` 之后的未提交工作区；[工作区状态与逐文件哈希](../../_archive/drivecompose/20261106-recompile-cleanup/workspace-before.json)和必要文件原件已保存，既有论文与图件修订不计作本轮新增写作。

| 位置／原状态 | 本轮结果 | 原因 |
|---|---|---|
| 四份正式 PDF 及其编译记录 | 按当前源文件真实重编，经检查后替换正式路径 | 保证提交的成品对应当前论文和已采用图件 |
| 未采用图稿、原稿副本、对比预览、自动备份、缓存和旧检查输出 | 29 份既有文件及本轮新检查输出分别归档，逐文件 SHA-256 核对 | 保留可恢复原件，移出当前论文无须加载的文件 |
| 历史过程记录中的候选文件链接 | 91 处 Markdown 链接指向归档原件；图件布局索引增加本轮归档根 | 保持来源、候选及实际原稿可追溯，不改写历史 JSON 中的事实 |
| draw.io 自动备份 | 新增 `*.drawio.bkp` 忽略规则，沿用 `*.dtmp` 规则 | 避免自动保存文件再次进入待提交清单 |

四次编译均成功并生成本轮新 PDF。英文／中文主稿共 11／10 页，完整总结逐段匹配且正文结束标签位于第 8／7 页，全部主文图表位于预算内；英文／中文补充共 12／10 页，表 S1–S25 完整。全部 43 页已渲染复核，另用 Poppler 检查两版正文末页，未见裁切或重叠。最终日志没有新增警告、缺字、未定义引用或溢出；中文仅浮动页提示和补充材料的 lineno hook 提示均有旧编译日志可核对。

所有 TeX、书目、样式源文件与活动图件保持本轮真实基线；未改文字、图注、实验值、字号、边距或行距。保留当前 Teaser 的 draw.io／PDF、已采用的加框图 3 PDF／SVG／PPTX、图 6 及六张结果原图；其余候选可从归档恢复。

历史证据审计仍为 80 项中 76 项通过。4 项失败为 `figure1_approved_pixels_exact`、`figure2_approved_pixels_exact`、`mechanism_author_selected_image_exact` 和 `figure3_approved_pixels_exact`，与本轮开始时保存的检查结果完全相同；不将历史审计报告为全量通过。当前编译、资源依赖、正文终止位置和 PDF 核验另行通过并记录。

[逐文件迁移与 SHA-256](../../_archive/drivecompose/20261106-recompile-cleanup/archive-manifest.json)、[完整重编与清理验收](../paper/provenance/recompile-cleanup-20261106.json)及[当前四份正式输出](../paper/build/CURRENT-OUTPUTS.md)已更新。编译候选、辅助文件、旧成品、日志、43 页渲染和专项脚本均放在仓库外同一归档目录。

---

## 2026-11-06 确认的简化版 Teaser 已替换中英文主稿

按作者“用这版替换”，将 revision 4 候选逐字节复制至正式 `paper/fig/fig01-teaser.pdf`，并同步可编辑 draw.io 与预览 PNG。真实基线是本轮开始时的未提交工作区，旧正式 PDF 哈希为 `7fe29dcf…`；最初原稿及替换前正式图、主稿、编译记录均已保留在 `../../_archive/drivecompose/20261106-teaser-context-adoption/baseline/`。

| 位置 | 原正式版 | 本轮采用版 | 原因 |
|---|---|---|---|
| 输入及画面 | 1350×690画布、折线共享输入 | 1440×690画布、框外柔和分流箭头 | 采用作者已确认的加宽和箭头样式 |
| 主场景注释 | Background、Vehicle、Human 三个标签及连接 | 删除三处文字与对应箭头 | 采用作者最新确认的简化版 |
| context 表示 | Shared scene context 与向量偏向场景右侧 | 标题和九个色块共同居中于主场景上方 | 减少视觉干扰并统一对齐 |
| 论文入口 | 中英文均引用 `fig/fig01-teaser.pdf` | 路径及图注源文保持，正式图内容更新 | 两版共用同一确认图，无需修改技术正文 |

两版已真实重编并写回正式输出：英文11页、完整正文止于第8页；中文10页、正文止于第7页。图表页码映射保持。宽高比例改变引起首页及后续自然重排；不声称所有后续页像素不变。全部43份 TeX／书目／样式源文件、其余图件、确认候选、最初原稿和两版补充材料保持原哈希。

新图在两版首页中的14个位图解码像素均与确认版一致，Form 边界匹配1038×498 pt。已检查中英文首页、全稿缩略图、正文结束标签和独立 Poppler 首页渲染，没有新增裁切或重叠。英文最终日志无警告；中文沿用第6页仅含浮动体的既有提示，无新增编译警告。80项既有检查中76项通过，4项历史图源失败与修改前一致，无新增失败；不将其报告为全量通过。

[正式图](../paper/fig/fig01-teaser.pdf)、[可编辑文件](../paper/fig/fig01-teaser.drawio)、[英文主稿](../paper/build/en/main.pdf)、[中文主稿](../paper/build/zh/main_zh.pdf)、[两版首页预览](../../_archive/drivecompose/20261106-teaser-context-adoption/layout-preview.png)与[采用及验收记录](../paper/provenance/teaser-style-adoption-20261106.json)。所有中间产物位于外部归档；未提交或推送。

---

## 2026-11-06 候选 Teaser：删除三个组件标签与箭头，居中 context 表示

本轮按作者要求，只修改独立候选。实际基线为上一轮77对象预览，原生文件 SHA-256 为 `9c7550c2…`；该轮 PDF、PNG、draw.io、对照和来源记录已完整保存在 `../../_archive/drivecompose/20261106-teaser-context-centered/baseline/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 主场景组件注释 | Background、Vehicle、Human 三个彩色标签及三条双向连接 | 删除三个文字、三条连线及对应隐形标签框 | 按作者要求简化主场景上方的注释 |
| Shared scene context 与向量 | 二者中心位于 x766.72，偏向主场景右侧 | 作为整体左移56.58单位，共同对齐主场景水平中心 x710.14 | 建立居中的上下关系；标题、九个色块的相对位置、尺寸、颜色与高度保持 |

本轮移除9个原生对象、平移11个原生对象；当前68个对象，包括14张独立图片。其余57个对象的内容、样式和几何保持，父组的子对象数量正常更新。PDF 仅删除 Background、Vehicle、Human 三个词，其余文字、页面尺寸以及14张图片的解码像素和位置一致；PNG 在局部注释区域外逐像素相同。原始审计为0条硬性问题、1条原子场景图尺寸提示；原生窗口、局部前后对照和最终 PDF 已复核。

[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.pdf)、[PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.png)、[可编辑文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.drawio)和[正式版／候选对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-comparison.png)已更新；[本轮局部前后对照](../../_archive/drivecompose/20261106-teaser-context-centered/local-before-after.png)展示实际删除和居中变化。[来源记录](../paper/provenance/teaser-style-preview-20261106.json)已更新为 revision 4。正式图、最初原稿和两版主稿保持原哈希，未重编论文；未提交或推送。

---

## 2026-11-06 候选 Teaser：Background 居中落点与 context 向量连接

本轮只修改独立候选。实际基线为上一轮保留箭头、去除圆点的77对象版本，原生文件 SHA-256 为 `40efb5a9…`；其 PDF、PNG、draw.io 和来源记录已完整保存在 `../../_archive/drivecompose/20261106-teaser-background-center-vector/baseline/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| Background 双向连接 | 落在标签右上角，绿色曲线较短 | 落在标签上边中点 (589.16, 346.8)，保留一个柔和弯曲及两端箭头 | 让箭头对应整个 Background 标签，并增加曲线舒展空间 |
| context 向量落点 | 三条连接依附包含标题的隐形外框 | 将隐形连接范围收紧到九个色块外侧，统一留3单位空隙；绿色到左侧中线，蓝色到底边中心，紫色保留横向落点后贴合底边 | 使箭头明确连接向量而非标题，并避免压住色块 |

只改3个原生对象；其余74个对象一致。文字、字体、所有标签位置、14张图片和左侧框外箭头保持。蓝色连接对象未改，其向量端随隐形锚框自动贴合。PDF 文字清单、页面尺寸与14个位图解码像素相同；PNG 在 context 连线区域以外逐像素一致。原始审计仍为4条已核对的图片白底覆盖误报，无新增发现；新原生窗口、局部前后对照与最终 PDF 已复核。

[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.pdf)、[PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.png)、[可编辑文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.drawio)与[正式版／候选对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-comparison.png)已更新；[本轮局部前后对照](../../_archive/drivecompose/20261106-teaser-background-center-vector/local-before-after.png)展示实际落点变化。[既有来源记录](../paper/provenance/teaser-style-preview-20261106.json)已回填为 revision 3。正式图、最初原稿和两版主稿保持原哈希，未重编论文；未提交或推送。

---

## 2026-11-06 候选 Teaser：灰色曲线恢复箭头，背景连线改为柔和单弯

本轮按作者两张局部截图，仅修改独立候选。真实起点为上一轮加宽候选，原生文件 SHA-256 为 `29c1e5b7…`；原候选 PDF / PNG / draw.io 已完整保存在 `../../_archive/drivecompose/20261106-teaser-arrowhead-softcurve/baseline/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 输入共享连接 | 两条无头灰色曲线和三个圆点端口 | 删除三个圆点，改为两条带小实心三角端头的灰色曲线；尖端仍在框外 x362，距框左边 x372 为10单位 | 按作者要求使用箭头，同时保留此前“不要进入框内”的约束 |
| Background 双向连接 | 两个控制点的弯曲路径 | 一个控制点的柔和单弯，保留绿色、线宽和两端箭头 | 与现有行人连接的曲线语法一致，避免局部反复拐弯 |

只改三条线并删除三个圆点；其余74个对象逐项一致，全部文字、字体、配色、Human 位置、相机对齐、1440×690画布和14张图片均保持。导出 PDF 文字、页面尺寸与14个位图的解码像素保持；原生 PNG 在两处修改区以外逐像素相同（含10px导出边缘保护）。原始审计仍为4条已核对的原图白底矩形误报，无新增问题；新原生窗口、绿色曲线近景和最终PDF已复核。

[候选PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.pdf)、[PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.png)、[可编辑文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.drawio)和[正式版／候选对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-comparison.png)已更新；[本轮局部前后对照](../../_archive/drivecompose/20261106-teaser-arrowhead-softcurve/local-before-after.png)可直接检查圆点与箭头、两种曲线。正式图、最初原稿与两版主稿保持，未重编论文。完整对象核验与哈希回填[既有来源记录](../paper/provenance/teaser-style-preview-20261106.json)，中间产物在本轮归档；未提交或推送。

---

## 2026-11-06 Teaser 局部样式候选：加宽画布、框外共享连接与人体标签对齐

作者要求“做一版我看下效果，保留当前版本”，随后明确否定“输入箭头加长并进入框内”，说明可以加宽整个画面、换用其他共享输入符号，并将 Human 放在人头上方。本轮以当前已入稿的 `fig01-teaser.drawio` / PDF 为真实基线，另存独立候选；没有替换正式图或重编论文。

| 位置 / Location | 当前正式版 / Before | 候选版 / After | 理由 / Reason |
|---|---|---|---|
| 左侧共享输入 / shared input | 硬折线一分二和短三角箭头，端点靠近框边 | 两条浅灰无箭头曲线连接圆点端口，全部停在框外；上下外框恢复完整左边线 | 撤掉被作者否定的“箭头进入框内”；用更轻的连接明确相同输入供两条路径共享 |
| 画布 / canvas | 1350×690 | 1440×690，主图区域整体右移90单位，图片与文字尺寸保持 | 加宽的是整幅画面，为左侧连接预留真实空间 |
| 共享上下文 / shared context | 上下文卡片和三个彩色标签框，关系线弧度较散 | 居中的标题＋原九个token，彩色无框标签，保留三条双向连接 | 降低边框数量，统一注释与表示的视觉层级 |
| 相机条件 / camera condition | 图标／文字组合偏向竖箭头右侧 | 收紧文字框，图标与文字作为整体与竖箭头、渲染模块同轴 | 消除文本框尾部空白导致的偏心 |
| 人体标签 / human annotation | Human 在人头右上方 | 标签中心与主图人头对齐，上方留12单位净距 | 按作者最新截图建立直接的对象对应，保留原人体画面 |

[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.pdf)、[可编辑 draw.io](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.drawio)、[预览 PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-preview.png)和[当前／候选对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-style-comparison.png)已保存。当前正式 `fig01-teaser.pdf` / `.drawio`、既有原稿、此前确认候选以及两版主稿共9项文件保持原哈希；正式 PDF 仍为 `7fe29dcf…`，正式 draw.io 仍为 `2c3b2fc8…`。

候选保留全部文字、字体、组件配色与14张独立图片。14个PDF位图的解码像素与基线完全一致；除整个主图区平移90单位外，场景内部相对位置和图片尺寸未变。当前候选为80个对象，其中66个原生／组对象及14个位图。已检查原生窗口、实际导出PDF及灰度论文宽度预览；共享输入端口最右边为x364.5，外框左边为x372，连接没有进入框内；相机共同中轴为x1020，Human与人头中心为x853.3038。自动审计的4条图像矩形覆盖提示均核对为原图白底，实际路线包络内源像素最低253，无墙体／人体覆盖；保留原始审计计数，不冒称原始报告为零。

本轮为有上下文的局部自审和候选交付，不重新批准整幅图的出版设计。作者否定的最初“箭头伸入框内”尝试只留在归档 `rejected-arrow-extension/` 中，不作为交付版本。真实基线、原生操作、反馈修订与核验在 `../../_archive/drivecompose/20261106-teaser-style-preview/`；[来源与验收](../paper/provenance/teaser-style-preview-20261106.json)记录精确哈希及范围。未提交或推送。

---

## 2026-11-06 参考 CVPR 录用论文调整英文图表位置

本轮按作者指定的英文主稿执行，修改范围为 `paper/sec/3_method.tex` 与 `paper/sec/4_experiments.tex` 的浮动选项、图块位置及一个局部浮动边界。基线提交为 `5b46f9eb8e131314430a2f2fa5193dadd16dc296`，实际原文来自本轮修改前的未提交工作区快照；既有改动完整保留。纯排版调整不涉及中英文语义变更，中文源文及输出保持。

调研以 CVF 正式录用版为准，复用已有归档 PDF，核验日期为 2026-11-06。查看以下六篇论文前 8 页的布局与图表页码。这是目的性排版样本，不将其解释为录用率或官方强制摆法。

| 录用论文 | 年份 | 与本轮有关的可核验版式观察 |
|---|---|---|
| [StreetCrafter](https://openaccess.thecvf.com/content/CVPR2025/papers/Yan_StreetCrafter_Street_View_Synthesis_with_Controllable_Video_Diffusion_Models_CVPR_2025_paper.pdf) | 2025 | 第 3 页跨栏总览位于页顶；第 6 页两幅定性图上下排列，并在同页下方配主表。 |
| [ReconDreamer](https://openaccess.thecvf.com/content/CVPR2025/papers/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.pdf) | 2025 | 第 3 页总览位于页顶；第 4 页方法局部图采用单栏。页顶总览下仍承接相关工作尾段，说明无需强制在章节边界换页。 |
| [VGGT](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf) | 2025 | 第 3 页跨栏架构图在方法节附近；第 7 页将单栏表、定性图与各项分析交错组织。 |
| [Fast3R](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf) | 2025 | 第 3 页跨栏架构图位于页顶；第 6 页将跨栏主表与单栏分任务表组合；第 7–8 页消融图表保持单栏。 |
| [D4RT](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.pdf) | 2026 | 第 2 页跨栏方法总览；第 8 页消融图及表 7 在左栏，表 8–9 在右栏，与消融文字共享末页。 |
| [Native3D](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiang_Native_and_Compact_Structured_Latents_for_3D_Generation_CVPR_2026_paper.pdf) | 2026 | 第 3 页两幅方法图使用单栏；第 8 页定量表主要排列于左侧，右侧保留定性图和分析。 |

本稿第 3 页总览图、第 6 页重建图、第 7 页轨迹外图已经与相应内容相邻，继续保留。对末页采用定量表在左、定性图在右的组织方式，并将机制图放入所属小节。

| 位置 | 本轮真实基线 | 调整后 | 原因 |
|---|---|---|---|
| 图 3 / §3.3 | 第 4 页右栏顶部；其后先接 §3.2 尾文；`figure[t]` | 第 4 页 §3.3 的 Latent encoding 之后；`figure[!htbp]` | 避免方法细节图出现在所属小节之前 |
| 表 4 / Input-timestamp sensitivity | 第 8 页右栏顶部，与分析分栏 | 第 8 页左栏，紧接对应分析 | 保持两张定量消融表及解释的连续阅读 |
| 图 6 / Completion component ablations | 第 8 页左栏中部；源文为“表 3 → 图 6 → 输入分析 → 表 4” | 第 8 页右栏顶部；源文为“表 3 → 输入分析 → 表 4 → 图 6” | 让定性证据独立成列，给两张定量表留出连续空间 |
| 实验末尾浮动边界 | `\FloatBarrier` 将 Discussion 推到右栏 | 移除这一个局部边界，保留 `main.tex` 正文末尾的边界 | 让 Discussion 使用左栏余量；图表仍在使用说明和参考文献之前 |

正文、公式、引用、所有表格单元格、图注、图号、图件路径、显示尺寸、标题及模板保持；六张图的原始 PDF 没有编辑。原组件分析跨第 7–8 页的自然分页仍保留，不宣称已消除全部段落分页。

英文正式稿已由现有 Tectonic 入口真实编译并替换，11 页总 PDF，全部技术正文、完整结论和六图四表均在前 8 页。29 项本轮检查通过，最终日志没有未定义引用、缺字、溢出或浮动超页警告；第 1、2、3、5、6、7 页与实际基线逐像素一致。全部 11 页缩略图及第 4／8 页详细图已复核，并以 Poppler 独立渲染第 4／8 页。既有检查器 80 项仍为 76 项通过，原有 4 项历史图源核对失败与基线相同，无新增失败。

[英文正式稿](../paper/build/en/main.pdf)、[第 4／8 页前后对照](../../_archive/drivecompose/20261106-cvpr-float-layout/layout-comparison.png)、[只含本轮改动的逐行差异](../../_archive/drivecompose/20261106-cvpr-float-layout/layout-only.diff)、[完整来源与验收](../paper/provenance/figure-table-layout-20261106.json)。基线、候选、日志、页图和所有中间文件均在项目外 `../../_archive/drivecompose/20261106-cvpr-float-layout/`。

---

## 2026-11-06 确认的加框版图 3 已替换中英文主稿

按作者确认，将中英文方法源文中图 3 的插图路径由 `fig/fig03-joint-completion.pdf` 切换为 `fig/fig03-joint-completion-core-boxed.pdf`。只改两处路径，原中英文图注、图号、单栏宽度、技术正文和公式保持；原图及所有候选继续保留。

两版均已真实重编并替换正式输出：[英文主稿](../paper/build/en/main.pdf)、[中文主稿](../paper/build/zh/main_zh.pdf)。图 3 仍在两版第 4 页，约 83.34 × 50.14 mm；相比原图同宽放置约减少 3.46 mm 高度。英文／中文仍共 11／10 页，完整正文止于第 8／7 页。

已检查图 3、前后页、完整总结页及中文第 6 页的既有结果浮动页。批准图中的 83 条矢量绘制、24 个原生文字和 16 处矢量渐变均在两版编译 PDF 中匹配；图注源文和渲染文字均保持。Poppler 复核没有新增裁切、重叠或浮动异常，无新增最终编译警告。全量检查器 80 项中既有历史图源失败由 5 项减为 4 项，没有新增失败；旧图源问题未在本轮扩展处理。

[中英文第 4 页排版预览](../../_archive/drivecompose/20261106-figure3-boxed-adoption/layout-preview.png)与[本轮采用、编译及验收](../paper/provenance/figure3-boxed-adoption-20261106.json)可直接核对。两版补充材料及其他图件未改，未重编补充材料。编译中间文件和真实修改前基线保存在外部归档。

---

## 2026-11-06 图 3 加框与连线留白候选（保留当前版）

按作者标出的连线问题，将三组左上特征用一层细浅蓝灰框归为同一集合，替代两侧括号。另存[加框候选 PDF](../paper/fig/fig03-joint-completion-core-boxed.pdf)、[SVG](../paper/fig/fig03-joint-completion-core-boxed.svg)、[可编辑 PPTX](../paper/fig/fig03-joint-completion-core-boxed.pptx)与[预览](../paper/fig/fig03-joint-completion-core-boxed.png)。[同尺度前后对照](../../_archive/drivecompose/20261106-figure3-boxed-candidate/comparison.png)左侧为保留的当前版，右侧为本轮候选。

| 位置 | 当前版（保留） | 加框候选 | 原因 |
|---|---|---|---|
| 左上特征边界 | 左右两根括号 | 一层白底细浅色框，不加标题 | 明确三组特征属于同一集合，给连线提供清楚边界 |
| 红框所指更新线 | 从括号下方伸出，经过两次直角转折 | 从框右下侧出线，以一条平滑曲线进入投影框顶部中心 | 消除悬空起点与阶梯折线，清楚衔接约束更新 |
| 箭头交接 | 多处贴近边框 | 主要箭头起止处统一留 10 个原生单位白隙 | 按作者补充要求保持端点清爽 |
| 掩码速度公式 | 紧邻原竖直线 | 仅右移 65 个原生单位，字形、字号、内容不变 | 与新曲线分开，避免挤靠 |

特征色块、组内注意力小箭头、记忆内容、投影与状态条保持。99 个原生对象，含 24 个文本、68 个可编辑路径、7 个椭圆；13 个逻辑分组及独立外框，无图片。六处科学图形区域的实际 PDF 渲染逐像素一致，全部文字内容、字体、字号及颜色保持。新版沿用此前可编辑源的数学上标间距；与旧 PDF 的极小上标位置差异已记在验收中。

已通过独立文件构建和 WPS 新副本导出核对，随后检查 Poppler、SVG、单栏彩色／灰度和并排预览。当前版四个交付文件及全部原图 3、图注源文哈希保持；本轮没有替换论文选图、修改图注或重编正文。[设计、精确修改清单与验收](../paper/provenance/figure3-boxed-candidate-20261106.json)可追溯。本轮为局部自审，连接线仍为可编辑自由曲线，移动模块后需调整端点。

---

## 2026-11-05 确认版 Teaser 替换入中英文论文

作者明确要求“用这版替换论文中的 teaser”。本轮真实起点为未提交工作区；原正式图、两版主稿、源码及选择记录保存在 `../../_archive/drivecompose/20261105-teaser-adoption/baseline/`，HEAD 为 `5b46f9e`，没有把 HEAD 当作本轮正文基线。

| 位置 / Location | 修改前 / Before | 修改后 / After | 原因 / Reason |
|---|---|---|---|
| 首页图 1 / title teaser | 主稿仍加载之前的紧凑框版 `fig01-teaser.pdf`，不是已确认候选 | 以已确认的 `fig01-teaser-balanced.pdf` 原字节替换正式 `fig01-teaser.pdf` | 让论文实际采用作者确认的布局和已修正的空间位置、人体未观测面 |
| 可编辑源 / editable source | 最新改动保存在独立候选 draw.io | 同步为正式 `fig01-teaser.drawio` 和当前预览 | 正式 PDF 与可编辑稿、预览对应；原稿另存保留 |
| 英文工具说明 / English usage statement | “OpenAI Codex was used solely for language polishing…” | 去掉 solely，并加入 “OpenAI Image Gen was used to revise a schematic scene illustration in Figure 1.” | 真实记录已采用的生成式示意图修订；中文既有说明已覆盖，保持原文 |

中英文入口的图路径、图宽与图注保持原样，技术正文、公式、实验值和其余图件保持。使用项目原有 Tectonic 构建入口真实重编两版主稿，先在本轮归档中核验，再替换原正式路径。英文／中文共 11／10 页，完整正文分别止于第 8／7 页；已查看两版首页、正文末页和全页缩略图。两版首页均检出新标题，1981×794 局部示意图的解码像素与确认图逐字节一致；无缺字、未定义引用或新增编译警告。中文原有第 6 页仅浮动图警告与基线相同。

[英文主稿](../paper/build/en/main.pdf)、[中文主稿](../paper/build/zh/main_zh.pdf)、[正式 Teaser](../paper/fig/fig01-teaser.pdf)及[可编辑源](../paper/fig/fig01-teaser.drawio)已更新。[最初原稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)和原始 draw.io 继续保持原始字节，确认候选也保持。两版补充材料未改、未重编。采用、哈希、编译及图像核验均回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)，中间文件保存在本轮归档。未提交或推送。

---

## 2026-11-05 图 3 核心机制矢量重建，删除 CCM 标题并统一 N

按作者“改成矢量图，且不要 CCM 标题”及随后“S 换成 N”的要求，基于已选光栅预览重建[矢量 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.pdf)、[SVG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.svg)、[可编辑 PPTX](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.pptx)及[PDF 渲染预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-vector.png)。原稿、全部此前候选和中英文图注保持；本轮没有替换论文选图或重编正文。

| 位置 | 上一版预览 | 本轮矢量版 |
|---|---|---|
| 表现形式 | 1536 × 1024 的光栅图 | 100 个原生文字／几何对象，14 个逻辑分组，无图片；SVG、PPTX 与矢量 PDF |
| 顶部标题 | CCM | 删除，并裁去顶部仅含标题的 100 单位画布；其余对象保持原相对位置 |
| 迭代与终态 | ×S，z 的 S 上标 | ×N，z 的 N 上标 |
| 科学结构 | 组件局部特征、共享记忆读写、掩码速度及投影更新 | 保持，数学符号用原生文字项重建 |

本轮通过独立原生 OOXML 文件构建，再由本机 WPS Presentation 后台打开同一 PPTX 并导出，未声称使用 Microsoft PowerPoint。最终 PDF 有 83 条矢量绘制记录、24 个原生文本对象、零位图，字体已嵌入。SVG 有独立文字、曲线、色块和斜线；不是把整张 PNG 包进 SVG。PPTX 的 69 个自定义路径、7 个椭圆和 24 个文字对象可分别编辑。

已查看 WPS 导出、实际 PDF 的 Poppler 全图、SVG 的 CairoSVG 渲染，以及 83.34 mm 单栏彩色／灰度预览；修正上标间距后重新导出并核验。连接线为可编辑自由曲线，移动模块后需手动调整端点；数学式由独立文本项构成。图 3 原稿、此前候选与图注源文哈希保持；同期另一任务修改的图 1 与使用说明保留，未回退或计入本轮修改。本轮为有前文背景的自审。[来源、对象清单与验收](../paper/provenance/figure3-core-vector-20261105.json)可追溯。

---

## 2026-11-05 重生成 Teaser 新视角缺失场景，修正空间位置和人体未观测面

真实起点为本轮保存的 revision 7 候选，见 `../../_archive/drivecompose/20261105-teaser-unseen-regeneration/baseline/`。本轮只替换上排右侧独立示意图片 `scene-unseen`，不改论文文字、标题、布局或其他图件。

| 位置 / Location | 修改前 / Before | 修改后 / After | 原因 / Reason |
|---|---|---|---|
| 新视角三维场景 / changed-view scene | 车体、墙体和路面未知区域浅白相连，边界不清 | 用蓝灰已观测表面和白色缺口、浅灰虚线轮廓区分未知面 | 改善未知区域与白底的区分，保留 observation-only reconstruction 暴露缺失面的科学含义 |
| 空间关系 / spatial arrangement | 首次生成移动了相对位置，墙柱落在错误一端；作者指出不正确，未插入候选图 | 以现有右下第一张相机变化图作位置模板：墙柱在左端、车在右且朝左、行人在左后侧斑马线上 | 上下两条路线对应同一场景和同一目标视角，只比较是否补全 |
| 人体表面 / human surfaces | 第二次生成把紫色已观测面与白色未知面画反 | 依参考图逐肢体对应：金色表示的前侧未知面改为白色缺失，保留右后侧的紫色已观测部分 | 未观测面必须来自同一参考视角的完成区域；不是任意左右分半 |

最终用内置 Image Gen 生成独立示意资产，非实验输出。六张输入照片及其余 80 个原生/图片对象逐项保持；所有对象几何不变，导出图在替换图片附近以外逐像素一致（含 10 px 导出/滤波边缘保护），最终 PDF 的文字和 14 张独立图片数量保持。已有 6 条关于中部原图白底矩形的自动审计误报保持记录，无新增问题；原生窗口和最终 PDF 已目视检查。

[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[可编辑稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)、[本轮局部前后对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-unseen-comparison.png)、[最初原稿／当前稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)已更新。[独立新资产](../paper/fig/source/fig01-scene-unseen-regenerated.png)保存在项目中。原始 PDF 和 draw.io 均保持原始字节；原局部图、被否定的尝试、最终两步提示词及核验记录均保存在本轮归档目录，并回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。主选图及主稿编译产物未替换，未提交或推送。

---

## 2026-11-05 图 3 核心机制重绘预览

按作者“只突出核心机制，布局简洁紧凑，保留原稿，图注不变，先看看效果”的要求，另存[核心机制预览 PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-core-preview.png)。保留全部原图和此前矢量候选；当前论文选图及中英文图注未改，未重编论文。

| 位置 | 上一候选 | 本轮预览 |
|---|---|---|
| 记忆交换主体 | M / M′、U 和较多独立中间状态 | 一组组件特征、一组共享记忆，用方向相反的读／写箭头呈现交换 |
| 更新机制 | 独立速度头、加法节点、展开 Euler 算术和中间状态 | 未知掩码速度边、紧凑 Π 算子及一条 ×S 回路 |
| 约束效果 | 大幅状态条与末端符号 | 成对的小状态条：观测格、自由空间零值保持，未知格变化 |

本轮使用内置 Image Gen 生成光栅视觉草稿；没有声称交付可编辑矢量源或最终出版图。参考作者提供的另一篇论文示意图，仅借鉴信息取舍、短标签、特征图形与更新回路，未沿用其采样／投影的科学拓扑。首稿的重复 M 和灰色输入箭头落点已通过 Image Gen 修正，随后检查整图、单栏和灰度预览。

[完整最终提示词](../../_archive/drivecompose/20261105-figure3-core-preview/prompt.txt)与[设计、来源和验收](../paper/provenance/figure3-core-mechanism-preview-20261105.json)可追溯。提示词按绑定机制模板检查；原稿、此前候选、正式稿件与图注共 71 项文件哈希保持。本轮为有前文背景的自审，预览供作者判断构图效果。

---

## 2026-11-05 Teaser 标题改为「问题—作用」的直接对照

作者指出上一版两条标题不合适。本轮按英文科研图标题作局部润色，保留 Previous methods / Ours、现有科学含义及所有图形；用具体动词交代状态变化暴露什么问题、联合补全支持什么用途。

| 位置 | 修改前 | 修改后 | 理由与来源 |
|---|---|---|---|
| (a) | Previous methods: observation-only reconstruction | Previous methods: state changes expose missing surfaces | 从重复模块名称改为明确的可见问题；与现有图注中视角和 actor changes expose missing surfaces 一致（paper/main.tex:30） |
| (b) | Ours: joint completion for state-driven asset reuse | Ours: joint completion enables asset reuse across states | 从名词串改为机制与用途的关系；由现有图注及状态驱动装配定义支持（paper/main.tex:30；paper/sec/3_method.tex:143） |

[PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[可编辑稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)、[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)及[原稿／新稿对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)已更新。仅两处 label 值改变；所有几何和样式、其余 79 个对象、14 张图片、已删除标注及箭头留白保持。原生渲染在两条标题之外逐像素相同；最终 PDF 文字差异也严格对应两条标题，无新增裁切或溢出。

[最初原稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)继续保持原始字节。真实起点、措辞依据和核验保存在 `../../_archive/drivecompose/20261105-teaser-heading-refinement/`，回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。未修改论文源文、主选图或编译产物，未提交或推送。

---

## 2026-11-05 删除 Teaser 红框说明，a/b 改为 Previous methods / Ours 加简短介绍

本轮仅按作者图 1 红框删除文字，并参考作者图 2 的命名方式重写两条分区标题，不移植参考图中的速度、模型或任务结论。

| 位置 | 修改前 | 修改后／原因 |
|---|---|---|
| 输入旁 | Multi-view sequence、Time、Example frames | 删除这三处指定文字；六张照片、时间标签与轴保持 |
| 上下分块说明 | Aggregated observed surfaces、Unseen regions exposed、Joint completion、Asset reuse | 删除四处分块小标题 |
| 右侧三种状态 | Camera view、Vehicle rotation、Human pose | 删除三处指定文字，三个原图保持 |
| 底部车辆与图例 | After aggregating all inputs、After joint completion、Observed、Completed，以及两个图例色块 | 删除四处文字及整套图例；两车及中间箭头保持 |
| (a) 标题 | (a) Observation-only reconstruction | (a) Previous methods: observation-only reconstruction |
| (b) 标题 | (b) DriveCompose | (b) Ours: joint completion for state-driven asset reuse |

共删除 14 个文本对象和 2 个图例色块，重写 2 个标题。标题保持原字体、字号和位置，仅扩大文本框以容纳单行介绍。其余 79 个对象逐项相同；14 张原始图像和所有箭头保持，指定区域外的原生渲染逐像素一致。最终 PDF 的文字差异严格对应删除清单及两条新标题，未出现新增溢出或裁切。

[新版 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[源文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)、[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)及[前后对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)已更新。[最初原稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)继续保持原始字节。实际起点与证据在 `../../_archive/drivecompose/20261105-teaser-label-removal/`，验收回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。未改正文、主选图或编译产物，未提交或推送。

---

## 2026-11-05 图 3 候选的全图联动修改

按作者“修改”的要求，已将上轮三项全图建议落实到独立[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)和[PNG](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.png)。[同尺度全图对照](../../_archive/drivecompose/20261105-figure3-global-revision/comparison.png)保留相同的原英文图注。

| 位置 | 修改前 | 修改后 |
|---|---|---|
| 全图与中间连线 | 964.08 × 620 pt；模块间跨度 404.93 pt | 820 × 570 pt；跨度 335.70 pt，联动重排记忆、U 与采样链 |
| 两侧特征三行 | 行中心和 token 尺寸略有差异 | 三行严格对齐，统一 35.41 pt 方形 token |
| M / M′ | token 和容器大小不一致 | 均为 194 × 46 pt 条带，token 均为 28 × 28 pt |
| 算子与输出 | 两根匿名黑线；Velocity head；Completed | Attn 的 r / w 下标；v 的 θ 下标；保留 z 的 S 上标 |
| 投影与最终输出框 | 宽 164.30 / 217.42 pt | 宽 92 / 80 pt，保留原投影公式和最终状态 |

**原稿、图注和正式论文保持。** 本轮保留修改前候选，未更改 LaTeX 选图或重编论文，也未向图中补回一般解释性备注。原生画布面积减少 21.80%；按同一 83.34 mm 单栏宽放置时，内容相应放大，图高由 53.60 mm 变为 57.93 mm。

最终 PDF 含 112 个矢量对象、34 个原生文本对象、无位图面板。保留的 28 个原文字形、字体、字号和颜色均核对；70 项原有文件（含原图注与主稿）哈希保持。已查看新的 Poppler 全图、同尺度对照和单栏彩色／灰度预览，修正 M′ 标签图层遮挡；未观察到新增裁切、遮挡或含糊交叉。本轮为有前文背景的自审，未声称独立盲审或取得匹配 draw.io / PPTX 源稿。[参数与验收](../paper/provenance/figure3-global-revision-candidate-20261105.json)可追溯。

---

## 2026-11-05 四根指定横向箭头两端留白

按作者截图，仅调整上排三根流程箭头和下排补全至复用的箭头，不移动框、图像或标题。坐标单位为原生 1350×690 画布单位，箭头垂直中心线保持。

| 箭头 | 修改前起止 x | 修改后起止 x | 两侧白隙 |
|---|---|---|---|
| 观测重建框 → 聚合场景 | 520 → 550 | 528 → 550 | 与两侧对象边界各距 8 |
| 聚合场景 → 状态渲染框 | 811 → 850 | 811 → 842 | 各距 8 |
| 状态渲染框 → 未见区域场景 | 1010 → 1042 | 1018 → 1042 | 各距 8 |
| 联合补全场景 → 复用分组括号 | 899.36 → 980.32 | 899.36 → 965.60 | 各距 14.72 |

[PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[可编辑稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)及[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)已更新，箭头线宽、箭头头部大小及方向保持。其余 93 个对象逐项相同，四处箭头区域以外的原生渲染逐像素一致；最终 PDF 全部文字及 14 张图片保持。没有新增文字溢出或路由问题。

[最初原稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)保持原始字节，[并排对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)已同步。实际基线和验证位于 `../../_archive/drivecompose/20261105-teaser-arrow-clearance/`；结果回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。未改主选图、正文或编译产物，未提交或推送。

---

## 2026-11-05 修正 Teaser 下方为「一个大标题＋两个小标题」

作者明确指出，上下分区都应有一个大标题和两个分块小标题。此前把 (b) 大标题当作左侧分块标题，遗漏了独立的左侧小标题；本轮按真实层级修正。

| 层级／位置 | 修改前 | 修改后 | 与上方对应 |
|---|---|---|---|
| 第一行：下方大标题 | `(b) Joint completion and reuse` | `(b) DriveCompose` | 同 (a) 的 x300、宽520、字号22.5；y251 对应 y23 |
| 第二行：左块小标题 | 缺失 | 新增 `Joint completion` | 同 Aggregated observed surfaces 的 x548、宽260、字号19；y281 对应 y53 |
| 第二行：右块小标题 | `Same assets, new states` | `Asset reuse` | 同 Unseen regions exposed 的 x1045、宽280、字号19；y281 对应 y53 |

[修改稿 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[源文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)和[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)已更新。此次只更新两个原生文本对象，并新增一个原生小标题；其余 94 个既有对象逐项保持，标题区之外的原生导出逐像素一致。14 张图片、所有箭头、此前确定的下半部分缩放与内容位置均保持。最终 PDF 的文字差异严格对应三处标题，未发现新增文字溢出或裁切。

[最初原稿 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)保持首轮修改前的原始字节；[原稿／新稿对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)已同步更新。本轮真实起点与核验在 `../../_archive/drivecompose/20261105-teaser-three-heading-hierarchy/`，当前结果回填[既有来源记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。未改主选图、论文正文或编译产物，未提交或推送。

---

## 2026-11-05 Teaser 小标题重写并按上下两行对齐，独立保留最初原稿

根据作者指出的小标题层级，本轮仅修改 balanced 候选中的两个文本对象。与本轮真实起点相比，其余 94 个对象逐项一致；标题区域之外的原生导出逐像素相同。原图和箭头未再缩放或移动。

| 位置 | 修改前 | 修改后 | 对齐依据 |
|---|---|---|---|
| 下方分区小标题 | `(b) DriveCompose: joint completion and asset reuse` | `(b) Joint completion and reuse` | 与 (a) 同为 x300、宽520、字号22.5；y251 对应上方 y23，加上分区间距228 |
| 右侧复用小标题 | `Reuse the same assets`，y287、字号20.7 | `Same assets, new states` | 与上方 Unseen 小标题同为 x1045、宽280、字号19；y281 对应上方 y53，加上分区间距228 |

作者要求保留的**最初原稿**已从首轮修改前的真实备份逐字节复制为[原稿 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.pdf)，SHA-256 为 `6183604dca2eae5cfa7a65e7e65c64599ee84be00640159bc7f0b3ac487326a5`，不是将中间修改版当作原稿。既有原稿 draw.io 也保持。[并排对照](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-comparison.png)使用同等显示宽度的两个实际 PDF 渲染。

[修改稿 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[修改稿源文件](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)和[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)已更新。最终 PDF 文字差异严格对应上述两处名称；14 张图片和其余文字保持，未发现新增溢出、裁切或路由问题。当前主选图及论文正文未改，未重编论文，未提交或推送。来源及验证更新到[既有记录](../paper/provenance/teaser-coordinated-preview-20261105.json)；本轮真实起点与过程位于 `../../_archive/drivecompose/20261105-teaser-subtitle-alignment/`。

---

## 2026-11-05 收紧图 3 候选左侧模块空白

本轮继续编辑独立候选，图注、原稿及正式论文保持。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 左侧模块外框 | 361.18 × 250.70 pt | 261.18 × 238.70 pt，面积减少 31.15% | 回收符号替换文字后留下的空白 |
| 符号与 token 间距 | 87.82 pt | 32.82 pt | 收紧横向间距，保留原字号和 token 大小 |
| 三行、括号及关联连线 | 沿用上一候选位置 | 后两行上移 6／12 pt；括号缩短，输出与反馈端点随边框调整 | 保持清楚的分组及端点连接 |

所有字形、字号、颜色、公式和连接关系保持。113 个矢量对象、30 个文本对象保留；局部模块及关联连线之外在 72／144 dpi 下逐像素一致。68 项原有文件哈希保持，包含中英文图注与正式论文 PDF。没有重编或替换论文。

[当前候选](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)、[同尺度局部前后对照](../../_archive/drivecompose/20261105-figure3-symbol-compact/comparison.png)及[参数／验收](../paper/provenance/figure3-symbol-compact-candidate-20261105.json)可核对。真实基线与脚本保存在 `../../_archive/drivecompose/20261105-figure3-symbol-compact/`，原稿继续保留。

---

## 2026-11-05 Teaser 下半部分缩小，标题独占一行

按作者截图，在现有 balanced 候选上局部调整；原文件及来源记录保存在 `../../_archive/drivecompose/20261105-teaser-title-row/baseline/`。本轮继续更新[候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[可编辑源稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)及[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 下半部分图文内容 | 主场景、共享单元、复用示例和对照沿用上一版尺寸 | 整体缩至 92%，水平居中，内容从 y287 开始 | 给标题腾出独立横行 |
| (b) 标题 | 与右侧 Reuse 标题处在同一行 | 独占首行；与 (a) 同为 x300、22.5 字号，距各自上框线 9 单位 | 对齐上下标题层级 |
| 下方入口与复用连接 | 中心线 y440 | 随内容移动至 y460.88，保留分区入口缺口和原连接关系 | 避免缩放后箭头错位 |

上方区域原生导出逐像素一致；全部文字、14 张图片资源、96 个对象及原有语义关系保持。图件已原生重新导出并核对 PDF 文字、图片数量和边界。当前选图 `fig01-teaser.pdf`、正文与主稿 PDF 未由本轮修改。来源和验收更新至[既有记录](../paper/provenance/teaser-coordinated-preview-20261105.json)。

---

## 2026-11-05 图 3 候选区域符号化，保留原图注

作者明确要求不改图注，并将截图中的四处文字改成符号。本轮只更新独立候选，保留原稿和当前论文选择。

| 位置 | 前一候选 | 本轮候选 | 原因 |
|---|---|---|---|
| 局部注意力标题 | `Local attention` | Attn 的 g 下标 | 以分组注意力算子替代长文字，g 对应正文的局部组索引 |
| 三行类型标签 | `Background / Rigid / Human` | X 的 b／r／h 下标 | 使用对应分量的特征符号 |
| 候选图注 | 曾提议增补分组和状态说明 | 恢复原中英文图注，预览两栏相同 | 按作者要求撤回图注改动 |

保留上一候选中的 Π 算子。113 个矢量对象及其余 22 个候选文本对象逐项保持；四处标签区域之外在 72／144 dpi 下逐像素一致。66 项原有源文、图件及 PDF 哈希保持，未重编或替换论文。原图 SHA-256 仍为 `6978ecdd8aaadf84fbac991163a7b60a5a119ce4e10b81e981eaa97f3a819ffd`。

[候选图](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)、[相同图注的并排预览](../../_archive/drivecompose/20261105-figure3-symbol-candidate/comparison.png)和[来源／验收](../paper/provenance/figure3-symbol-candidate-20261105.json)可核对。前一候选和撤回的图注位于 `../../_archive/drivecompose/20261105-figure3-symbol-candidate/baseline/`；正式中英文图注源文未改动。

---

## 2026-11-05 Teaser 连线与协调性修订候选

作者在上一版预览后指出布局不协调、箭头混乱，并授权按只读审查结果改一版看效果。本轮保留当前选图 `fig01-teaser.pdf`（SHA-256 `9b6c15f90670f6386ececf763b865685633b2a9dab8ee8acbeff9ca946f93847`），从匹配的原稿 draw.io 制作[独立候选 PDF](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.pdf)、[可编辑源稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.drawio)及[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-balanced.png)。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 共享输入 | 输入括号、分流竖线及框边密集平行；箭头横穿边框 | 一条分流线，两个分区入口各留缺口 | 消除重复骨架，让入口统一 |
| 右侧复用 | 长竖线加三根输出小箭头 | 一根主箭头接浅灰分组括号；三图共用一条垂直对齐线 | 表达并列复用结果，降低连接线重量 |
| 中央共享关系 | 三条饱和彩色回路环绕场景 | 原生共享单元移至上方，三条局部细双向连接 | 保留跨组件共享关系，并让场景轮廓清楚 |
| 上排、标题与底部 | 虚实流程混用，相机条件悬空；标题在底部，车辆说明分散 | 主流程实线；相机短竖箭头；a/b 标题左上；两车及说明对齐 | 区分数据流和条件输入，减少跳跃阅读 |

原始六张输入照片字节保持，八个图像裁剪经逐像素核验；没有新生成或改画场景。重复的 Joint completion 标题并入完整 b 标题，Also 说明并入既有三种状态标签；全部科学条件与聚合所有输入后的对照保留。画布 1350×690。96 个对象中，82 个原生构件或组合对象、14 个独立图片；中央场景及上下文组成一个可展开编辑的语义组。

完成 draw.io 实际模型审计、应用截图、原生文件重新导出，以及最终 PDF 的 Poppler/PyMuPDF 渲染复核。自动审计的六项命中均来自中央底图的白色矩形边界，已用实际像素及完整渲染确认连接线位于留白，不遮挡三维主体；逐项证据与原始输出保留，未将原始计数改成零。文字溢出和实际路由问题已修正；本轮为已知主张下的局部自审，不冒充独立盲审或完整投稿审查。

正式选图、原稿及其他 draw.io 变体保持；未改论文正文或重编论文，未提交或推送。完整记录见[本轮来源与验收](../paper/provenance/teaser-coordinated-preview-20261105.json)，过程位于 `../../_archive/drivecompose/20261105-teaser-coordinated/`。

---

## 2026-11-05 图 3 的独立算子标注候选（未替换论文）

作者要求保留原稿，本轮仅另存候选 PDF／PNG 及图注，当前论文与图件选择不变。

| 位置 | 原稿 | 候选稿 | 原因 |
|---|---|---|---|
| 投影模块标签 | `Projection` | Π 及斜体 m,f 下标 | 与正文约束投影算子一致，避免与相机投影混淆 |
| 图注 | 简述 CCM 读写和未知码更新 | 增补局部组示例、实心点／斜线／零的含义，以及观测恢复和自由空间归零 | 将一般解释置于图注，保持图内简化机制结构 |

原图 SHA-256 保持 `6978ecdd8aaadf84fbac991163a7b60a5a119ce4e10b81e981eaa97f3a819ffd`。其余 24 个原文本对象与 113 个矢量对象逐项相同；投影模块标签区之外在 72／144 dpi 下逐像素一致。当前两版主稿和方法图注源文均未修改，未重编。图注候选尚未写入论文。

[候选图](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig03-joint-completion-revised.pdf)、[中英文图注](../../_archive/drivecompose/20261106-recompile-cleanup/files/docs/figures/fig03-joint-completion-revised-caption.txt)和[等尺寸并排预览](../../_archive/drivecompose/20261105-figure3-operator-candidate/comparison.png)可审阅；[来源与验收](../paper/provenance/figure3-operator-candidate-20261105.json)记录字体、像素核验与原稿保护。所有中间产物在 `../../_archive/drivecompose/20261105-figure3-operator-candidate/`。

---

## 2026-11-05 收紧图 3 删除文字后的空白

按作者要求只收紧图 3 布局，保留上一轮已删除的图例和六处文字。真实基线为上一轮未提交版本，图 3 SHA-256 为 `11067cccfea969be42d62b4c18c7fde29c4d9ea6eb90dd0fc70cc4cbefc77135`；原件、复现脚本、候选、编译与页图保存在 `../../_archive/drivecompose/20261105-figure3-compact/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 上下两段流程之间 | 删除说明后留有较大间隔 | 下方采样链与橙色循环整体上移 100 pt；更新公式上移 60 pt | 收紧主要空白，同时保留公式与下方模块间距 |
| 速度头及关联连线 | 沿用旧位置 | 速度头上移 12 pt；只缩短三条受影响连线 | 保持端点连接和清楚的箭头方向 |
| 顶部与底部画布 | 高 760 pt | 顶部裁去 40 pt，底部随采样链上移裁去 100 pt；最终高 620 pt，宽度保持 964.08 pt | 图高减少 18.42%，保持字号和模块大小 |

全部 25 个文本对象的字形、字体、字号、颜色，以及 113 个矢量对象的样式保持；除三条连线长度调整外，图形尺寸保持。公式、符号、剩余标签、模块关系及图注无改动。上方模块保留原坐标与样式，仅随画布原点变化整体显示；栅格预览有极少量边缘取样差异，已在验收记录中注明，不宣称逐像素相同。更新公式与连线相隔约 8.50 pt，与下方投影框相隔约 13.94 pt，箭头端点未侵入模块。

仅替换图 3 后，两版初次编译的全文词项计数均与基线相同。收尾检查发现另一任务同期更新了图 1 PDF，已保留该文件及其记录，再用当前图件完整重编。最终英文／中文共 11／10 页，完整正文仍止于第 8／7 页，图 3 均在第 4 页；最终全文词项差异仅为参考文献中的页码回引数字，未改正文源文或科学数值。独立图与两版第 4 页经 Poppler 复核，无裁切、重叠、缺字、未定义引用或溢出。

原保护清单中 57 项文件保持原哈希，图 1 为已保留的同期独立改动；最终重编前后 58 项当前输入哈希均稳定。80 项检查仍为 75 项通过，5 项历史图源失败保持，本轮未新增失败。详见[本轮来源与验收](../paper/provenance/figure3-compact-layout-20261105.json)。

---

## 2026-11-05 Teaser PDF 收紧留白并加上下分区框

本轮以作者指定的当前 `fig01-teaser.pdf` 为真实基线，不采用独立 draw.io 修订稿。基线提交为 `5b46f9e`，实际起点为既有未提交工作区；原 PDF SHA-256 为 `6183604dca2eae5cfa7a65e7e65c64599ee84be00640159bc7f0b3ac487326a5`。原版与本轮必要记录已备份到 `../../_archive/drivecompose/20261105-teaser-compact-framing/baseline/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 上下两条路径 | 仅中间一条分隔线 | 两个左右边界相同的灰蓝细框，框间距 12 pt | 明确观测路径和补全／复用路径的范围 |
| 上排两个操作框 | 高 89.28 pt | 高 66 pt，原蓝色及文字字号保持 | 收紧框内空白 |
| 底部车辆对照 | 图片下方另放整行说明，图例占对照区右侧 | 说明分两行放在车辆旁，图例移至中央场景的右上空白 | 回收纵向空间，保留原有全部文字 |
| 整图 | 1350 × 708.72 pt | 1350 × 640 pt，高度减少约 9.7% | 压缩空白，保留主场景及图片比例 |

已更新[正式图件](../paper/fig/fig01-teaser.pdf)，[调整后预览](../paper/fig/fig01-teaser-preview.png)可直接查看。15 张原始图片资源和全部文字词项均与基线一致；图片只裁外沿空白，不重采样或改画。主场景原有烘焙标注沿用，不将其声称为全原生矢量。PyMuPDF 与 Poppler 实际渲染复核通过，未发现缺字、文字相交、裁切或连线遮挡；本轮是指定布局的自审回归，不替代完整科学叙事审阅。

独立 draw.io 变体及其他图件未由本轮修改；本轮未改论文源文或重编主稿，未提交或推送。完整来源与验收见[记录](../paper/provenance/teaser-compact-framing-20261105.json)。期间观察到其他图件／编译产物由并行工作更新，按外部变更记入验收，不覆盖、不算作本轮贡献。

---

## 2026-11-05 删除图 3 的六处指定文字

按作者补充的五张截图，仅删除当前图 3 的六处指定文字。真实起点为上一轮已去除图例的未提交版本，基线图件 SHA-256 为 `2a19c18a3f83b040f5dd928204a917647c62bbe97e8d4bb55dea37b472ad7a0e`；基线、中间产物与截图在 `../../_archive/drivecompose/20261105-figure3-remove-labels/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 图上方 | `Cross-component context`、`Shared memory` | 删除这两处标题，保留 M、M′ 和 C、τ | 按截图删除 |
| 图中部 | `Fixed query layout`、`Constrained update` | 删除这两处说明，连线及其他对象位置保持 | 按截图删除 |
| 更新公式右侧 | `(unknown only)` | 删除括号说明，保留 Δτ u ⊙ vθ | 按截图删除 |
| 完成输出上方 | `after S` | 删除此处文字，保留输出的 S 上标及 `S steps` | 按截图删除 |

删除六个完整原生文本对象，其余 25 个文本对象的内容流逐字节保持，113 个矢量绘制对象的全部属性相同。页面尺寸不变；72／144 dpi 下，六处目标文字区域之外的像素完全一致。中英文主稿全文文本差异均严格对应以上六处文字，没有其他新增或删除词项。

两版主稿已重编并保存到正式路径；英文／中文共 11／10 页，正文仍止于第 8／7 页，图 3 均在第 4 页。独立图和两版第 4 页经 Poppler 复核，无新增重叠、裁切或编译警告。58 项正文源文、其他图件和补充材料文件哈希保持。80 项既有检查仍为 75 项通过，5 项历史图源失败与基线相同；本轮未新增失败。详细证据见[本轮验收](../paper/provenance/figure3-label-removal-20261105.json)。

---

## 2026-11-05 删除图 3 底部图例

作者指定删除截图中的底部备注。本轮起点为 `5b46f9e` 之上的既有未提交工作区；真实修改前文件、差异、页图与编译中间产物保存在 `../../_archive/drivecompose/20261105-figure3-remove-legend/`。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 两版主稿图 3 底部 | `Observed / fixed`、`Unknown / updated`、`Free / zero`，含三个符号和浅色外框 | 删除上述图例、符号及外框 | 按作者截图指定范围删除 |
| 图 3 页面底部 | 高 845.04 pt，包含图例条带 | 高 760 pt；宽度和其余对象位置保持 | 去除删除图例后的多余空白 |

直接删除当前原生矢量 PDF 的图例内容流，保留区域在 72 与 144 dpi 渲染下逐像素一致；其余文字完全相同。图注、中英文正文源文、公式、数据、其他图件和补充 PDF 的 56 项文件哈希保持。英文／中文主稿重编并保存至正式路径，共 11／10 页，正文仍止于第 8／7 页，图 3 均位于第 4 页。Poppler 页图复核无新增裁切或重叠，编译无缺字、未定义引用或溢出。

80 项既有检查中 75 项通过，5 项历史图源检查失败与修改前相同；本轮未新增失败。当前匹配的 draw.io 源稿未在检出中找到，本轮直接编辑现用矢量 PDF，历史 draw.io 变体保持。详见[本轮来源与验收](../paper/provenance/figure3-legend-removal-20261105.json)。

---

## 2026-11-05 Teaser 按已讨论建议另存修改稿

作者授权“按这些建议改一版 draw.io，保留原稿，改好后给我看预览”。本轮真实基线为当前[原稿 draw.io](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.drawio)，SHA-256 为 `05fe93a91a09496c72b3be1c2038d1ae17fc2a4b4f41122f129767bd3dba8324`；仅制作独立[修改稿](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-revised.drawio)与[预览](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-revised.png)，未改论文文字或当前 PDF 选图。

| 位置 | 本轮原稿 | 修改后 | 原因 |
|---|---|---|---|
| 上方观测路径 | 两个大蓝色流程框；未见面接近白底 | 浅灰紧凑节点，未见车身增加原生灰斜线；相机图标改原生形状 | 减少操作框的视觉重量，让缺失表面可见 |
| 输入 | 两列视角未标明；小字号时间标签 | 添加 View 1 / View 2，统一时间标签字号与矩阵间距 | 明确视角／时间两个维度，保留六张原始输入照片 |
| 中央和底部补全说明 | 主场景标签约 5.56 pt，底部重复完整车辆 | 机制标签约 8.07 pt；底部保留“全部输入聚合后”条件，改为同位置车尾局部对照 | 提高可读性，并保留能解释补全增量的必要信息 |
| 右侧复用 | 三张小全景，状态名称在细小侧注中 | 相机全景、车辆转动近景、人体两姿态近景；独立动作箭头与随姿态变化的金色上臂标记 | 让复用与表面运动在画面中可观察 |
| 图例与冗余注释 | Observed 仅蓝灰单色；重复 Also 注释 | 三类观测组件色加金色完成标记；删除重复注释 | 区分组件身份与完成状态，回收空间 |

[并排前后预览](../../_archive/drivecompose/20261105-teaser-revised/before-after-comparison.png)包含本轮真实基线。新文件 109 个对象，其中 94 个原生构件与 15 个独立位图；六张照片原始字节保持，五个裁剪保留源像素。标签最小字号按当前跨栏宽约为 8.07 pt。draw.io 实际重新打开、原生结构审计及独立阅读均完成，0 个硬错误；大幅底图提示经目视确认为单张连续三维示意场景。

原稿、原版／调整版图一 PDF 和两版论文入口文件均通过起止哈希一致检查。未改科学主张、实验结果或图注，未替换正式论文图件，未编译、提交或推送。完整来源和过程见[验收记录](../paper/provenance/teaser-revision-20261105.json)及既有项目外归档 `../../_archive/drivecompose/20261105-teaser-revised/`。

---

## 2026-11-05 原稿 PPT 转入 draw.io（保持原稿布局）

作者补充原稿 `E:/Users/changan/Downloads/feishu/fig01-teaser.pptx`，并明确要求先按原稿转换，不采用调整稿。已交付[原稿 draw.io](../../_archive/drivecompose/20261106-recompile-cleanup/files/paper/fig/fig01-teaser-original.drawio)。源稿 SHA-256：`610b31c35ba550a9b0319982e24ba47d9d261d76854525631445a58d7119f4b5`。

| 项目 | 原稿 | draw.io 结果 |
|---|---|---|
| 版式与内容 | 一页 1350×708.75，36 个形状、17 条连接线、15 张图片 | 原有 68 个对象全部对应；原位置、尺寸和文字保持，不套用调整稿 |
| 主场景标注 | Background、Vehicle、Human、共享上下文与彩色曲线烘焙在主场景图中 | 仅去除底图中的标注，以 26 个独立原生对象按原位复建；场景保持光栅图片 |
| 图片 | 15 张独立图像 | 14 张原字节保留，1 张主场景为去标注派生底图；所有图片内嵌，无外链依赖；真实输入照片不作生成式修改 |
| 可编辑性 | PPT 原生对象及图片 | 29 个文本、23 条线、28 个形状、15 张图片；仅白色画布背景锁定，其余 94 个对象可编辑及移动，无分组 |
| 原始文件 | 原稿 PPT、原版 PDF、调整版 PDF | 三者哈希不变，当前论文图件路径和正文不变 |

最终文件已在独立 draw.io Desktop 会话实际重新打开并查看，原生审计 0 个硬错误；单张主场景占页 17.9% 的提示已核对。导出了全彩预览、标题隐藏灰度副本及跨栏尺度预览。此次为原稿转换自审，出版尺度的小字号继承原稿，不宣称完成版式优化或独立盲审。

完整[来源与验收记录](../paper/provenance/teaser-original-drawio-20261105.json)包含原稿映射、图片处理说明、逐项哈希和原生打开证据；[过程归档](../../_archive/drivecompose/20261105-teaser-drawio/)保留原始素材、提示词和预览。主稿未重编，未提交或推送。

---

## 2026-11-05 单栏组件消融图与对应分析入稿

按作者要求参考 HUGS（CVPR 2024，§4.4／Fig. 9）、DeSiRe-GS（CVPR 2025，§5.4／Fig. 6）和 Street Gaussians（ECCV 2024，§5.3／Fig. 5）的消融写法，在现有组件定义与表 3 结论后补两句具体视觉分析，并加入单栏图 6。真实起点为已有未提交改动的工作区，HEAD 为 `5b46f9eb8e131314430a2f2fa5193dadd16dc296`；[基线与完整差异](../../_archive/drivecompose/20261105-component-ablation-insertion/)保存本轮实际修改前文件，未把已有改动归入本轮。

### 正文实际前后对照

英文 §4.5“Completion components”，原文：

```latex
At $T=8$, exchanging component context adds 0.627/0.934 dB full-image/dynamic PSNR (Table~\ref{tab:ablation-components}). Appendix H reports paired hidden-surface mechanism comparisons and visibility-stratified results.
```

修改后：

```latex
At $T=8$, exchanging component context adds 0.627/0.934 dB full-image/dynamic PSNR (Table~\ref{tab:ablation-components}). Figure~\ref{fig:component-ablation} shows cleaner traffic-signal contours and sharper foliage detail with the full model. Pedestrian silhouettes and vehicle windows have fewer distortions and ghosting artifacts. Appendix H reports paired hidden-surface mechanism comparisons and visibility-stratified results.
```

中文对应原文：

```latex
在 $T=8$ 时，交换组件上下文使全图／动态 PSNR 分别提高 0.627／0.934 dB（表~\ref{tab:ablation-components}）。隐藏表面配对机制比较与可见率分组结果见附录 H。
```

修改后：

```latex
在 $T=8$ 时，交换组件上下文使全图／动态 PSNR 分别提高 0.627／0.934 dB（表~\ref{tab:ablation-components}）。图~\ref{fig:component-ablation} 中，完整模型的信号灯杆轮廓更清晰，树冠纹理更鲜明。行人轮廓与车窗区域的局部形变和重影也更少。隐藏表面配对机制比较与可见率分组结果见附录 H。
```

修改理由：原段已说明删减版本和指标收益，缺少结果图及可定位的视觉解释。新增文字直接描述灯杆轮廓、树冠纹理、行人和车窗区域的差异，不添加泛泛的有效性宣言、假想质疑或新的机制结论。英文新增文字按 humanizer 检查；中文仅按 lieflat 白名单核查，未触发额外改写。

### 图件与图注

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| §4.5，表 3 后 | 没有定性组件消融图 | [图 6](../paper/fig/fig06-component-ablation.pdf)，单栏 83.34×54.44 mm；Ours、w/o CCM、w/o GCM；标签 9 pt | 与组件表同页展示局部轮廓和纹理差异 |
| 英文图注 | 无 | **Completion component ablations.** Rows show two scenes; columns are Ours, w/o CCM, and w/o GCM. Colored boxes mark the regions enlarged below each view. | 简洁交代样例、版本与放大关系 |
| 中文图注 | 无 | **补全组件消融。** 每行一个场景，各列依次为 Ours、w/o CCM 和 w/o GCM。彩色框标记各图下方对应的放大区域。 | 与英文对应 |
| 检查器 | 沿用“消融图已删除”的旧约定 | 核对当前单栏图、正文引用、PDF／SVG 哈希与六张原图 | 与本轮作者授权同步，保留旧占位图禁用检查 |

六张原图逐字节保存在 `paper/fig/source/component-ablation/`，图中全景与局部均保持原生像素；没有调色、锐化或生成式处理。图注不额外假定尚未提供的输入数量或种子。已有表 3／4、实验设置、摘要、引言、方法、讨论、结论、图 1–5 与两版补充材料的源文件及资产均保持本轮起点；主稿重编自然包含工作区已有的图一更新。

### 验证与输出

- 两版主稿真实重编成功；英文／中文总页数 11／10，完整结论与正文结束标签在第 8／7 页。图 6 与组件表分别同在第 8／7 页，单栏标签实际约 9 pt。
- 42 项专项检查通过，含两张表逐字一致、原图与 18 张内嵌图像像素一致、改动范围、完整结论、列顺序、字号及编译产物核验。无缺字、未定义引用或溢出。
- 现有稿件检查器 80 项中 75 项通过；5 项旧图来源检查在本轮修改前已经失败，本轮没有新增失败。完整名称与真实结果保存在[专项验收](../../_archive/drivecompose/20261105-component-ablation-insertion/verification.json)，未声称全部既有检查通过。中文保留第 6 页仅含浮动图的既有提示。
- 正式稿：[英文](../paper/build/en/main.pdf)、[中文](../paper/build/zh/main_zh.pdf)。[图件、来源与本轮记录](../paper/provenance/component-ablation-figure-20261105.json)；[可编辑 SVG](../paper/fig/fig06-component-ablation.svg)。未提交或推送。

---

## 2026-11-05 原版与调整稿分开保留（当前选择）

按作者“原版先保留，方便我对比”的要求，将 `paper/fig/fig01-teaser.pdf` 恢复为最初原版，SHA-256 为 `6183604dca2eae5cfa7a65e7e65c64599ee84be00640159bc7f0b3ac487326a5`。最新调整稿另存为 `paper/fig/fig01-teaser-layout.pdf`，SHA-256 为 `d51b5eccbdf24ac23724ea143fc5a536e7b9efe661801589332c7450ff1c2383`。两份文件均逐字节核对，后续编译默认仍采用原版，调整稿留待作者比较选择。

同尺度[原版／调整稿并排预览](../../_archive/drivecompose/20261105-teaser-version-comparison/fig01-teaser-comparison.png)已生成；首轮调整 PDF 也继续保留在既有归档中。当前[版本选择记录](../paper/provenance/teaser-layout-20261105.json)已同步，LaTeX 和已编译论文 PDF 未改。

---

## 2026-11-05 按作者反馈重新校正子图尺度与连线（调整稿，现已另存）

作者指出首轮重排中的左右分叉线、长标题等细节仍未处理好。本轮以首轮实际输出为基线，SHA-256 为 `7f2a9d1d6cb688e60f2d8e16424246d6d1a9cb039d5c80bf54c5785666d9cc84`；没有将 HEAD 或最初原图冒充本轮基线。[原文件、三张作者反馈截图和说明备份](../../_archive/drivecompose/20261105-teaser-layout-refinement/)保留。下方首轮的版面自审结论由本轮复核接续。

| 位置 | 首轮状态 | 本轮处理 | 原因 |
|---|---|---|---|
| 共享输入出口 | 输入括线与分支竖线并排，另有中央短横线，两个分支端点不一致 | 一条输入分组括线同时作为两条路径的起点；两条水平箭头均约 50 pt，去掉中央短横线 | 让连线明确对应整组输入，避免重复竖线和悬空线段 |
| 右侧复用 | 一条短横线接三叉竖线，三枚箭头轴段过短，原点离场景主体较远 | 从主场景可见道路端点附近发出一条约 49 pt 的完整箭头，连接明确括起的三个状态示例 | 表达同一场景组件的三种复用，避免细碎分叉和看不清的箭头 |
| `(b)` 长标题 | `(b) DriveCompose: joint completion and asset reuse`，约 516 pt 宽 | `(b) DriveCompose: joint completion`，约 359 pt；资产复用由右侧原有标题说明 | 标题控制在主场景区域内，取消重复信息 |
| 上方标题 | `(a)` 标题与 Aggregated observed surfaces 的字行相邻，信息偏长 | `(a) Observation-only`；`Aggregated surfaces`，完整 reconstruction 名称保留在操作框 | 增加标题之间的真实空隙，并保持上方路径的观测限定 |
| 图例 | 位于主场景底部、靠近右侧连线和车辆对照 | 放入主场景右上方原有空白区域 | 使图例直接服务主场景，避免与连接线和辅助图竞争；核对底层区域没有原有非白内容 |
| 辅助车辆对照 | 图像与长说明、图例混排 | 说明置于两车上方，两车字段同尺寸、同基线，独立保留一条完整比较箭头 | 将辅助证据与主图、状态复用分组分开阅读 |

### 按可见主体校正尺寸

首轮主要按整张图片外框统一，图片内部空白差异仍使实际主体大小不一。本轮只通过 PDF 裁剪窗口移除外侧空白，在源图允许范围内保留约 8 个像素的边缘留白，不改图像字节、不重采样。下表为可见主体宽度，单位为图源 pt；辅助照片和原生标签仍分别处理。

| 子图 | 首轮主体宽度 | 本轮主体宽度 | 排布 |
|---|---:|---:|---|
| 两幅上方场景 | 约 252.5／258.0 | 约 258.1／258.3 | 相同 265×160 pt 字段，保持比例并垂直居中 |
| 联合补全主场景 | 约 538.8 | 约 574.4 | 占主要视觉面积，约为一个状态场景的 2.26 倍宽 |
| 三个状态示例 | 约 239.9／227.0／227.0 | 约 254.0／253.6／253.6 | 相同 260×114 pt 字段，中心距 125 pt，标签共同对齐 |
| 两辆辅助车辆 | 约 90.7／90.7 | 约 94.3／94.3 | 同尺寸裁剪字段、同一水平比较轴 |
| 六张输入帧 | 90 pt 图宽 | 100 pt 图宽 | 保留两视角×三时刻，统一行距和边框 |

最终仍为 1350×708.72 pt，15 张原始图像的像素签名逐项相同。原生文字无重叠或裁切、字体均嵌入；三幅复用图的可见宽度差小于 0.35 pt。已经查看 Poppler 实际渲染、495 pt 插入宽度预览和隐藏分区标题后的灰度图。本轮为针对作者反馈的排版自审，没有把源图中的光栅标注或表面语义问题称为新完成的矢量审查。

当前[图一 PDF](../paper/fig/fig01-teaser.pdf)已替换为本轮结果；[来源与验收](../paper/provenance/teaser-layout-20261105.json)已更新，旧记录原件保存于本轮基线。完整[重排脚本](../../_archive/drivecompose/20261105-teaser-layout-refinement/reflow_teaser.py)、[最终预览](../../_archive/drivecompose/20261105-teaser-layout-refinement/final-preview.png)与逐对象规范可复核。正文、图注、实验结果、其他图件和现有论文 PDF 保持；未重编主稿、未提交或推送。

---

## 2026-11-05 首轮 teaser 版式调整（已由上方复核接续）

按作者要求直接更新 `paper/fig/fig01-teaser.pdf`。真实基线为 HEAD `5b46f9e` 下的当前工作副本，原 PDF 的 SHA-256 为 `6183604dca2eae5cfa7a65e7e65c64599ee84be00640159bc7f0b3ac487326a5`；原文件及本轮修改前的说明已保存于[本轮基线](../../_archive/drivecompose/20261105-teaser-layout/baseline/)。既有未提交工作保留。

| 位置 | 原状态 | 本轮修改 | 原因 |
|---|---|---|---|
| 上方流程框和场景 | 两个深蓝框约 220×90／138×90 pt，场景宽约 255／240 pt | 流程框统一为浅蓝、约 190×66／185×66 pt；场景宽增至 300／278 pt | 减轻流程框视觉重量，让观测与缺失场景更突出 |
| 上下分区标题 | `(a)`、`(b)` 在各自区域底部，另有重复的 Joint completion 标题 | 分区标题放到同一左对齐锚点；Joint completion 并入 `(b)` 标题 | 进入每个区域时即可识别其作用，减少重复层级 |
| 右侧状态示例 | 图像、标签位置分散，字号 15 pt | 三图宽度统一 267 pt、行距 125 pt；标签共用左边界与基线，字号 21.8 pt | 建立一致的阅读节奏与对应关系 |
| 图例与前后对照 | 图例 13.56 pt，状态文字 15 pt，跨栏后约 4.97／5.50 pt；对照使用较重虚线外框 | 图例、状态与对照文字改为 21.8 pt，跨栏后约 8 pt；外框改为浅色分隔线 | 提高关键文字可读性，减轻底部边框的干扰 |

页面保持 1350×708.72 pt，原始 15 张图像像素逐项核对一致，全部原标签信息保留。保留原始实线／虚线流程关系；仅裁掉上方观测场景右边缘的一条导出残留细线。原生文字无重叠或裁切，两套字体已嵌入；已查看 PyMuPDF、Poppler 渲染，以及按 495 pt 插入宽度的缩小预览和隐藏分区标题后的灰度图。本轮为排版范围自审，未重绘场景、未解决原图表面标记的历史语义问题。

本轮只更新图一及相应记录；未修改 LaTeX、图注、实验数据，未重编或替换两版主稿 PDF，未提交或推送。新图会被后续正常编译采用。完整[来源与验收](../paper/provenance/teaser-layout-20261105.json)、[重排脚本](../../_archive/drivecompose/20261105-teaser-layout/reflow_teaser.py)、[最终预览](../../_archive/drivecompose/20261105-teaser-layout/final-preview.png)保留可追溯。

---

## 2026-11-04 拉取最新文件并审阅新 teaser

按作者要求，分支从 `edcd19c` 快进到 `5b46f9e`，接入远端统一图件目录和五份最终 PDF。本地未提交的核心消融、补充材料、检查脚本及四份正式 PDF 已逐项备份并恢复；两版实验源文只叠加远端的图件路径改名。双方文档新增记录合并保留，四份编译结果 JSON 与被保留 PDF 的 SHA-256 相符，没有用另一机器的旧编译记录覆盖本机输出。没有新增提交或推送。

本轮审阅的是当前 `paper/fig/fig01-teaser.pdf`，保留共享多视角输入和几何示意风格。具体问题为：上方缺失区域过浅、补全表面的跨状态对应不明确；大流程框及车辆前后条带重复占位；实际跨栏图例和状态标签仅约 4.97／5.50 pt。建议先统一未知／补全标记，再压缩重复内容、放大状态示例及文字。当前图件、图注和正文科学内容未被本轮修改，未重新生图或编译。

详细“位置 → 当前问题 → 改法 → 验收”、新构图建议及中英文图注候选见[图件索引](figures/README.md)，完整证据与同步状态见[本轮记录](../paper/provenance/teaser-latest-review-20261104.json)。拉取前真实原件、恢复补丁、逐文字号、原图及缩小灰度预览保存在[本轮归档](../../_archive/drivecompose/20261104-teaser-latest-review/)。此前录用论文参考拆解继续作为历史依据，没有重复开展文献检索。

---

## 2026-11-04 正文消融收拢为两组核心实验

作者确认按录用论文的主文篇幅收拢消融。本轮实际起点为干净工作区 HEAD `edcd19c6c8b63d5ae8b242044fedf2f83838762b`，真实原件已逐文件保存于[本轮基线](../../_archive/drivecompose/20261104-core-ablation-revision/baseline/)。本轮只修改中英文实验正文、必要的相关工作交叉引用、补充材料中的编辑表位置，以及相应检查与项目记录。

中英文主稿及两版补充材料均已编译、核验并更新至原正式路径。英文／中文主稿共 11／10 页，完整正文止于第 8／7 页；英文／中文补充材料共 12／10 页。75 项既有稿件检查及 107 项本轮源文、数据保留与编译核验通过；四份最终日志无未定义引用、缺字或溢出。补充表编号连续为 S1–S25。受影响正文与补充页已渲染复核。

### 位置与取舍

| 位置 | 原文／原状态 | 修改后 | 原因 |
|---|---|---|---|
| 主稿 §4.5 | 组件、隐藏机制、可见率、编辑后表面、自由空间五项展开，三张受控表 | 组件贡献、输入数量两段，两张表 | 集中回答补全与组件交换的作用及输入稀疏性 |
| 组件表 | 全图三项＋动态 PSNR／SSIM | 全图三项＋动态 PSNR；动态 SSIM 原值和 SD 在附录 G 保留 | 精简单栏表宽，保留完整记录 |
| 输入数量 | 正文只概述增益，均值与 SD 在附录 G | 均值表进入主文表 4，附录完整 SD 保持 | 让第二组核心消融可直接阅读 |
| 隐藏机制、可见率 | 正文重复展示附录 H 已有结果 | 撤下正文表和展开，正文一处指向附录 H | 保留近邻机制证据，释放正文篇幅 |
| 编辑后表面 | 原主文表 5 | 表体逐字迁入附录 I，编号 S19，§4.4 引用配对比较 | 资产复用证据保持完整 |
| 自由空间 | §4.5 展开 C／F 与射线损失数值 | 既有附录 D／J 保持；观测保持标签移至 §4.4 | 避免非核心展开与失效引用 |
| 指标实现 | 颜色域、SSIM 和 LPIPS 生产配置未独立核验 | 继续在实验方案与来源记录中列为待核验 | 不以公共默认设置冒充实际评价器 |

### 实际中英文前后对照

组件表图注原文：

```tex
\caption{\textbf{Component ablations on Waymo.} $T=8$, with shared recovery, codec, and target views. Full SDs are in Appendix G.}
\caption{\textbf{Waymo 组件消融。}$T=8$，恢复模块、codec 与目标视图相同。完整 SD 见附录 G。}
```

修改后：

```tex
\caption{\textbf{Component ablations on Waymo.} $T=8$ timestamps (24 images), with shared recovery, codec, and target views. Full metrics and SDs are in Appendix G.}
\caption{\textbf{Waymo 组件消融。}$T=8$ 个时刻（24 张图像），恢复模块、codec 与目标视图相同。完整指标与 SD 见附录 G。}
```

原组件段落中输入数量只用一处结果概述；附录 G 已有六行完整均值与 SD。本轮新增正文段落如下，数值均取自原作者记录：

```tex
Fixed checkpoints use nested $T=2,4,8$ inputs (6/12/24 images) over the same time span and target views. At each input count, evidence and queries are reconstructed from the supplied inputs. CCM adds 1.104, 0.738, and 0.627 dB PSNR and reduces LPIPS by 0.041, 0.028, and 0.018 (Table~\ref{tab:ablation-inputs}), with the largest benefit at the sparsest input setting. Appendix G gives the input lists and seed statistics.

固定 checkpoint，在相同时间跨度与目标视图上使用 $T=2,4,8$ 嵌套输入（6／12／24 张图像），每档均从所给输入重新构建证据与查询。CCM 的 PSNR 增益分别为 1.104、0.738 和 0.627 dB，LPIPS 分别降低 0.041、0.028 和 0.018（表~\ref{tab:ablation-inputs}），输入最稀疏时收益最大。输入清单与种子统计见附录 G。
```

相关工作最后一句原指向 `Sec.~\ref{sec:hidden-completion}`／`第~\ref{sec:hidden-completion} 节`，本轮仅改为 `Appendix H`／`附录 H`；其余内容保持。方法中的观测保持引用继续有效，标签移至保留的 §4.4 观测保持段。

完整逐行差异见[本轮差异](../../_archive/drivecompose/20261104-core-ablation-revision/source-changes.diff)，原始均值及展示选择见[本轮记录](../paper/provenance/core-ablation-revision-20261104.json)。摘要、引言、方法、讨论、总结、书目、所有活动图件及模板逐文件保持；没有执行训练或评价，也没有改变任何实验结果值。

---

## 2026-11-04 补齐仓库内的论文编译依赖

原问题：上一轮将“不推 PPT 等大文件”扩大为“不上传任何 PDF”，提交 `42ea76f6ef0b49afe0e57c0b7fa712a58bf0d885` 中的 LaTeX 已引用统一命名的五份 PDF，Git 却没有这些文件，新检出无法直接编译。按作者本轮要求，修正版本控制范围，保留 PPT 和论文成品输出在本机。

真实基线为 `42ea76f` 后的工作区；此前四份未提交的论文 PDF 不属于本轮改动。[基线及文件哈希](../../_archive/drivecompose/20261104-self-contained-build/baseline.json)已保存。

| 位置 | 原文／原状态 | 修改后 | 原因 |
|---|---|---|---|
| `.gitignore` | `paper/fig/fig*.pdf` | 删除该忽略规则，保留 PPT 和中间文件忽略规则 | 五份图件 PDF 是源码依赖 |
| `paper/fig/fig01-*.pdf` 至 `fig05-*.pdf` | 仅本机存在 | 纳入 Git，文件字节及哈希不变 | 同事拉取后即可读取全部插图 |
| `paper/README.md`、图件索引 | “新检出编译前需另行补齐五份图件 PDF” | “五份图件 PDF 纳入 Git，拉取后无需另行复制”，列出四份论文的编译命令 | 仓库内容与协作说明一致 |
| 编译说明中的历史审计 | 与编译命令放在同一代码块 | 从编译命令块移出，说明审计依赖历史归档但编译不依赖 | 避免将审计材料误认为编译依赖 |

英文、中文的 LaTeX、图注、实验值、书目、样式和字体配置均保持原字节。仅使用待提交 Git 树 `93c931519f8807ea0793468e2b6a8bf775e88226` 导出的独立快照，排除已有论文输出 PDF，用 Tectonic 在全新目录编译四份论文，全部成功；主稿为 11／10 页，补充为 12／10 页。43 页逐页提取文本相同，Poppler 72 dpi 逐像素比对全部一致，已目视复核主稿五张图、正文末页与补充首末页；最终日志无未定义引用、缺字或溢出。

验收不依赖本机未提交的 PPT、论文 PDF 或仓库外历史素材。此次没有重跑依赖旧外部归档的历史证据审计。完整检查结果已并入[布局记录](../paper/provenance/figure-layout.json)，原始日志、页图和对比在[构建验收归档](../../_archive/drivecompose/20261104-self-contained-build/)。后续只补记这些说明与验收信息，编译所用源码和图件不再变动。下方保留上一阶段的实际提交范围，当前以本节为准。

---

## 2026-11-04 提交图件整理的源码与文本

按作者本轮推送要求，以已同步的 `edcd19c6c8b63d5ae8b242044fedf2f83838762b` 为提交基线，提交统一图件路径、命名、来源说明、检查脚本与已归档旧文件的删除记录。保留此前合并的同事修订，不改学术正文、实验数值或图注。

最终 PPT、五份图件 PDF、四份本机重编的论文 PDF 及图片均不新增上传；新增最终图件 PDF 忽略规则，图件索引明确说明新检出在编译前需要另行补齐图件。编译结果 JSON 与布局记录用于记录本机验收，不能代替未上传的最终 PDF。下方“未提交或推送”描述保留为各阶段的当时状态。

本次检查提交差异、冲突和上传对象范围；四份 PDF 的编译与版面验收沿用上一阶段结果，本阶段未改论文内容，也未重复编译。

---

## 2026-11-04 拉取同事更新并保留本地图件整理

按作者要求执行 `git pull --ff-only origin main`，分支由 `2c6bab6151e40d58f67d17e94a943fe5306b7288` 快进至 `edcd19c6c8b63d5ae8b242044fedf2f83838762b`。本轮真实基线含上一轮未提交的目录整理；[本地原件、状态与哈希](../../_archive/drivecompose/20261104-sync-collaborator/baseline.json)在拉取前保存，远端 47 个更新文件也在恢复本地修改前逐文件保存于同一归档的 `remote/`。

同事的补充材料修订、JRM 正式会议引文、技术审查、LLM 使用说明和图件选择全部接入。逐文件核对 38 个 LaTeX／书目文件，当前内容等于远端原文，仅将主稿的 10 处插图路径映射为本机统一文件名；未改写同事的学术内容或实验数值。

| 冲突位置 | 拉取后的原文件／远端修改 | 合并结果 | 依据 |
|---|---|---|---|
| 两版总览引用及图 2 | `fig/drivecompose-inference-overview.pdf` | `fig/fig02-overview.pdf`，采用远端 PDF 原件 | PDF SHA-256 保持同事来源记录中的 `51fa1721…`；本机原生可编辑 PPT 原字节保留 |
| 两版机制图引用及图 3 | `fig/drivecompose-joint-completion.pdf`，修正后的 draw.io 矢量图 | `fig/fig03-joint-completion.pdf`，替代上一轮 PNG 封装版 | PDF SHA-256 保持 `93a923a7…`；检查确认无内嵌位图，保留原矢量内容 |
| 机制图可编辑原件及过程材料 | `docs/figures/joint-completion-vector/` | 原件保存在[同步归档](../../_archive/drivecompose/20261104-sync-collaborator/remote/docs/figures/joint-completion-vector/)，当前入口加入[图件索引](figures/README.md) | `.drawio` 原生源稿完整保留；工作区图目录继续只放最终 PDF 与已有 PPT |
| 修改记录与输出索引 | 远端新增修订记录，本地也新增整理记录 | 两边记录合并保留，当前同步记录置顶 | 不用一方全文覆盖另一方的新增内容 |
| 检查脚本与忽略规则 | 远端新增 PDF／原生源稿哈希检查及 `*.dtmp` 规则 | 保留远端检查，并读取统一布局与归档路径；忽略规则取并集 | 当前路径与历史证据分别核对 |
| PDF 临时保存及编译结果 | Git 对两张 ASCII PDF 提示换行转换，四份编译结果随版本不同 | 从拉取前逐字节备份恢复最终图件，新增 PDF／PPTX 二进制属性，重新编译四份正式 PDF | 避免 Windows 换行转换改变 PDF 字节；不选择任意一方旧编译输出充作新结果 |

恢复本地修改时的 16 个冲突已解决。两份本机 PPT 哈希不变，图目录仍为 5 份 PDF 与 2 份 PPT；新的 draw.io 源稿可从索引进入归档。所有原有 stash 保留，本轮临时 stash 在核验后清除，原件另有仓库外备份。

四份 PDF 已在本机重编并核对输出哈希：英文／中文主稿为 11／10 页，完整总结与正文结束标签仍在第 8／7 页；英文／中文补充为 12／10 页。最终日志无未定义引用、缺字或溢出；新矢量图、主稿受影响页与正文末页、补充首末页均已渲染复核。当前机器缺少旧 `20261020-cleanup` 归档，因此不将同事机器上记录的 73 项历史检查称为本轮重跑结果。

完整文件、来源和验收见[布局记录](../paper/provenance/figure-layout.json)。本轮只拉取和恢复合并，未新增提交或推送；本地图件整理继续保留为未提交修改。

---

## 2026-11-04 统一图件目录、格式与命名

本轮范围是文件整理与图件格式，不改学术正文。真实基线为提交 `2c6bab6151e40d58f67d17e94a943fe5306b7288` 之后的工作区，已有四份未提交 PDF 修改一并保留；本轮不把这些既有修改计作新成果。[基线及文件哈希](../../_archive/drivecompose/20261104-figure-cleanup/baseline.json)、源码与当前主稿 PDF 快照保存在同一归档的 `before/`。摘要、贡献、标题、公式、图注和实验数值保持原文。

原问题：活动图件散落在 `paper/fig/`、`assets/` 与两个 `*-editable/output/` 目录；文件名混用 `DriveCompose`、`placeholder`、`refined`、`merged` 和 `Shift`。旧候选、逐面板 PNG、预览、提示词及构建依赖与正式图件混存，难以判断哪个文件应当继续编辑。

| 位置（英文／中文同步） | 真实基线原文／原文件 | 修改后 | 原因与核验 |
|---|---|---|---|
| 首页 Figure 1 引用：`main.tex` / `main_zh.tex` | `fig/drivecompose-concept-merged.pdf` | `fig/fig01-teaser.pdf`；可编辑源稿为同名 PPTX | 按图号命名，集中最终源稿及导出；作者 PPT 字节不变 |
| 方法总览引用：两版入口 | `fig/overview-editable/output/DriveCompose.pdf` | `fig/fig02-overview.pdf`；可编辑源稿为同名 PPTX | 消除多层输出目录与版本词；原生 PowerPoint 导出保留文字、线条及图片 |
| 方法机制图引用：`sec/3_method.tex` / `zh/3_method_zh.tex` | `fig/drivecompose-joint-completion.png` | `fig/fig03-joint-completion.pdf` | PNG 无损封装；1374 × 1145 内嵌像素与原件一致 |
| 动态重建结果引用：两版实验节 | `fig/experiment1-dynamic-reconstruction.png` | `fig/fig04-dynamic-reconstruction.pdf` | PNG 无损封装；2424 × 1693 内嵌像素与原件一致，保留透明通道 |
| 轨迹外渲染引用：两版实验节 | `fig/assets/Shift.pdf` | `fig/fig05-off-trajectory-rendering.pdf` | 名称对应任务；原 PDF 逐字节不变 |
| 正式图件存放 | 根目录 PNG、`assets/`、`overview-editable/`、`teaser-editable/` 及 `docs/figures/` 多处分散 | `paper/fig/` 仅保留 5 份 PDF 和 2 份 PPTX | 两个 PPT 均含原生可编辑文本与形状，图片已内嵌，不依赖被归档的零散素材 |
| 旧候选、素材及过程文件 | 保留在活动图目录与多个 build 目录 | 移至仓库外 `../_archive/drivecompose/20261104-figure-cleanup/files/<原路径>` | 9,439 个已归档文件，共约 1.68 GiB，逐文件 SHA-256 核对一致；可重建的依赖缓存路径不作为恢复原件 |
| 图件说明与工具引用 | 多个分散说明页，检查脚本硬编码旧 PNG 名称 | 单一 [图件索引](figures/README.md) 与 [布局记录](../paper/provenance/figure-layout.json)；检查脚本使用新路径并能解析归档旧图 | 当前入口统一；历史来源 JSON 保留原文，通过原路径映射读取证据 |

图 1 的当前 PPT 保存时间晚于旧主稿编译记录。本轮保留作者最后保存的文件，直接用 PowerPoint 原生导出 PDF，没有用旧构建脚本重建或修改 PPT。首页图 PDF 从 6,503,246 字节降为 448,038 字节；文字和线条恢复为可提取的矢量内容。图 2 同样从最终 PPT 原生导出。图 3–5 未提供当前采用图件的原生可编辑 PPT，不把位图装入 PPT 冒充可编辑源稿。

双语 LaTeX 仅修改 10 处图文件引用；与真实基线逐文件对照，替换这些路径后，其余内容完全一致。当前依赖、PPT 原件、两张 PNG 的内嵌像素、图 5 原件哈希与五张 PDF 的独立渲染均已核对。完整历史稿件检查仍依赖本机未提供的 2026-10-20 外部归档，不据此声称旧 70 项检查已重新通过。

双语主稿本轮重编成功，英文共 11 页、完整正文及总结止于第 8 页；中文共 10 页、完整正文及总结止于第 7 页。逐段匹配完整总结，并与正文结束标签互相核对；两版受影响页已渲染复核，无新增重叠或裁切，最终日志无缺字、溢出或未定义引用。编译新生成的 14 个辅助文件也已移至归档的 `after-build/`；`paper/build/` 只保留四份正式 PDF、四份编译结果 JSON 和当前输出索引。补充材料源文与正式 PDF 保持原字节。本轮未提交或推送，大文件留在本地。


---

## 2026-11-04 更新后归档临时文件并整合远端

本轮仅处理作者要求的归档、提交与推送。实际起点为 `a0ccb6b509f7b6454313f4108b956741b5ca4fd3` 之后的未提交工作区；[真实工作区基线](../../_archive/drivecompose/20261104-pre-push-sync/workspace-before.json)及当时已修改文件的原件已保存。远端新增 `2c6bab6` 文本提交，本轮将尚未发布的本地修订接到该提交之后，保留全部 71 份远端新增文本和两侧修订历史。

| 原位置／状态 | 本轮处理 | 原因 |
|---|---|---|
| draw.io 的 `.$figure3-drawio.drawio.dtmp` 与 Python 缓存 | 移入仓库外，新增 `*.dtmp` 忽略规则 | 移出自动保存和缓存；当前已采用的 draw.io 源文件及 PDF／SVG／PNG 保留 |
| 未采用的 `figure1-comparison-draft.png` 及其提示词、规格、生成记录 | 四份文件按原层级归档，更新说明中的链接 | 保留完整原件，避免将草稿作为活动图件提交 |
| 旧 `paper/build/verification.json` 与本轮新检查输出 | 分别归档，不把检查中间输出留在仓库 | 原检查与本轮 73 项检查均可追溯 |
| 两侧图件引用、输出说明和修订记录的合并冲突 | 保留本机当前已核验图件和对应编译记录，合并两侧新增历史 | 不用异机旧输出记录覆盖当前正式 PDF；[逐文件处理依据](../../_archive/drivecompose/20261104-pre-push-sync/resolution-report.json)已保存 |

共归档 7 份既有临时文件及 1 份本轮检查输出，逐文件 SHA-256 核对一致。除明确更新的说明和忽略规则外，191 份本机文件恢复并保持原始字节，包括全部论文源文、当前活动图件、四份正式 PDF 及编译记录；Git 检出造成的换行转换也已按真实基线恢复。本轮未改论文文字、数值、图表内容或排版，未重新编译；已核对四份 PDF 及入口源文件与现有成功编译记录的哈希，73 项稿件检查通过。

远端只提交了文本：其 PPT teaser 记录所指的 PPT 及 SHA-256 为 `5f1e29a61e407e9e4c597e579b1eb8b7eeb2f58d21560b430562908b58e59d3e` 的导出没有同步到本机。本次保留当前本机 `drivecompose-concept-merged.pdf`（SHA-256 `3031f2f09069d714ed267cb0390d6ea978e23304b7c7a23d5f5e0225773b1a40`），将异机记录及其适用状态写入图件和输出说明，未据文字记录替换图件。

完整原路径、归档路径和哈希见[归档清单](../../_archive/drivecompose/20261104-pre-push-sync/archive-manifest.json)，核验与保留项见[本轮仓库记录](../paper/provenance/pre-push-sync-20261104.json)。

---

## 2026-11-04 图一录用论文对照与构图草稿

按作者要求优化首页对比表达，检查 ReconDreamer、StreetCrafter、GenAssets、HorizonForge 的实际首页 Figure 1。原图把失败流程与完整 teaser 上下拼接，输入、标签和信息重复；本轮用内置 Image Gen 生成[共享输入、两行三列的对照草稿](../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-comparison-draft.png)，放大车辆旋转和人体换姿的对应区域。保持概念示意身份，没有制作具名基线结果、修改实验值或替换活动图一。

完整“原问题 → 实际改动 → 原因”、论文原图画法与来源见[图件记录](figures/teaser/README.md)。[最终提示词](../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-comparison-prompt.txt)、[设计规格](../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-design-spec.json)和[生成记录](../../_archive/drivecompose/20261104-pre-push-sync/files/docs/figures/teaser/figure1-generation-record.json)随草稿归档；首轮草稿、基线及参考页图仍在项目外[原过程归档](../../_archive/drivecompose/20261104-figure1-optimization/)。本轮没有编译主稿；其他同期论文修订原样保留。

---

## 2026-11-04 补充材料局部修订与 JRM 正式引文

按作者本轮授权，主稿仅更新 JRM 引文，舍弃图 5 参照列更名。其余修改集中在中英文补充材料，采用[作者补充原文](../paper/provenance/author-supplement-20261104.txt)的数值与结论，沿用现有章节和行文方式。

实际基线 HEAD 为 `a0ccb6b509f7b6454313f4108b956741b5ca4fd3`，并非仅以 HEAD 代替工作区原文。[本轮真实基线](../../_archive/drivecompose/20261104-supplementary-author-revision/baseline/)、[完整逐行差异](../../_archive/drivecompose/20261104-supplementary-author-revision/source-changes.diff)及[验收记录](../paper/provenance/supplementary-author-revision-20261104.json)已保留。

本轮期间另有图 2/3 矢量替换及使用说明更新，发生在六份主稿 TeX 文件中。这些同期工作保留原样，单独保存于[同期差异](../../_archive/drivecompose/20261104-supplementary-author-revision/concurrent-source-changes.diff)，不计入本轮修改。正式 PDF 采用编译时的稳定工作区，编译期间输入没有变化。

四份 PDF 均重编成功。英文主稿 11 页、完整技术正文止于第 8 页；中文主稿 10 页、正文止于第 7 页。英文/中文补充材料分别为 12/10 页。73 项既有检查和 27 项本轮检查通过；补充表 S1–S24 顺序连续、全部表格数字保持，最终日志无未定义引用、缺字或溢出。补充材料全部页图及主稿受影响页已复核。

### 修改位置与理由

| 文件 | 修改理由 |
|---|---|

| `paper/main.bib` | 主稿只更新 JRM 的正式会议书目信息，保留引用键和其他条目。 |

| `paper/supplementary/composition.tex` | 在现有蒙皮公式旁补权重非负、归一化和静止状态恒等性质。 |

| `paper/supplementary/composition_zh.tex` | 同步英文蒙皮定义，公式编号保持。 |

| `paper/supplementary/evaluation.tex` | 补每学习版本 108,000 张输出、稀疏输入和可见率分组增益、真实共有支撑比较及高斯计数关系；就地标明结构完整性统计，精简重复解释。 |

| `paper/supplementary/evaluation_zh.tex` | 同步英文新增数值结论及局部精简，保留所有表格数值和评价口径。 |

| `paper/supplementary/frontend.tex` | 将 0.10 m 明确为支撑邻域边长；中文现文已有该定义，保持原文。 |

| `paper/supplementary/references.bib` | 补充材料使用相同的 JRM 正式条目。 |

| `paper/supplementary/training.tex` | 补明 100/20 个合成场景和 20 个真实场景的评价用途，明确 16 个记忆 token 为可学习参数。 |

| `paper/supplementary/training_zh.tex` | 同步英文数据用途与记忆 token 定义。 |


### 实际原文与修改后


#### paper/main.bib

主稿只更新 JRM 的正式会议书目信息，保留引用键和其他条目。


原文（本轮基线第 458 行）

```latex
@article{wu2026jrm,
```


修改后（当前第 458 行）

```latex
@inproceedings{wu2026jrm,
```


原文（本轮基线第 461 行）

```latex
  journal={arXiv preprint arXiv:2603.25985},
```


修改后（当前第 461 行）

```latex
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
```


原文（本轮基线第 463 行）

```latex
  url={https://arxiv.org/abs/2603.25985},
```


修改后（当前第 463 行）

```latex
  pages={307--316},
  url={https://openaccess.thecvf.com/content/CVPR2026/html/Wu_JRM_Joint_Reconstruction_Model_for_Multiple_Objects_without_Alignment_CVPR_2026_paper.html},
```


#### paper/supplementary/composition.tex

在现有蒙皮公式旁补权重非负、归一化和静止状态恒等性质。


原文（本轮基线第 15 行）

```latex
For humans, the weighted skinning transform is $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$, where $\mathbf B_j$ and $\mathbf P_j$ are rest and current global joints in the root frame. The transformed center is $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$. The combined local linear map $\mathbf J_i$ gives covariance $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$. Its inverse $\mathbf J_i^{-1}$ maps viewing directions into the canonical frame; the direction is normalized before appearance evaluation. The inverse is evaluated for nonsingular skinning transforms. The root pose controls overall placement, while the root joint retains its rest transform.
```


修改后（当前第 15 行）

```latex
For humans, the weighted skinning transform is $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$, where $\mathbf B_j$ and $\mathbf P_j$ are rest and current global joints in the root frame. Weights satisfy $w_{ij}\geq0$ and $\sum_j w_{ij}=1$, giving $\mathbf A_i=\mathbf I$ in the rest state $\mathbf P_j=\mathbf B_j$. The transformed center is $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$. The combined local linear map $\mathbf J_i$ gives covariance $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$. Its inverse $\mathbf J_i^{-1}$ maps viewing directions into the canonical frame; the direction is normalized before appearance evaluation. The inverse is evaluated for nonsingular skinning transforms. The root pose controls overall placement, while the root joint retains its rest transform.
```


#### paper/supplementary/composition_zh.tex

同步英文蒙皮定义，公式编号保持。


原文（本轮基线第 15 行）

```latex
人体使用加权蒙皮变换 $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$，其中 $\mathbf B_j$ 和 $\mathbf P_j$ 是根坐标系中的静止与当前全局关节矩阵。变换后的中心为 $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$。组合局部线性映射 $\mathbf J_i$ 将协方差变换为 $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$，其逆 $\mathbf J_i^{-1}$ 将观察方向映回规范坐标，并在外观求值前归一化。上述逆映射使用非奇异蒙皮变换。根位姿控制整体放置，根关节保持静止变换。
```


修改后（当前第 15 行）

```latex
人体使用加权蒙皮变换 $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$，其中 $\mathbf B_j$ 和 $\mathbf P_j$ 是根坐标系中的静止与当前全局关节矩阵。权重满足 $w_{ij}\geq0$、$\sum_j w_{ij}=1$，因此静止状态 $\mathbf P_j=\mathbf B_j$ 下有 $\mathbf A_i=\mathbf I$。变换后的中心为 $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$。组合局部线性映射 $\mathbf J_i$ 将协方差变换为 $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$，其逆 $\mathbf J_i^{-1}$ 将观察方向映回规范坐标，并在外观求值前归一化。上述逆映射使用非奇异蒙皮变换。根位姿控制整体放置，根关节保持静止变换。
```


#### paper/supplementary/evaluation.tex

补每学习版本 108,000 张输出、稀疏输入和可见率分组增益、真实共有支撑比较及高斯计数关系；就地标明结构完整性统计，精简重复解释。


原文（本轮基线第 169 行）

```latex
% 原位置无此段。
```


修改后（当前第 169 行）

```latex

At $T=2,4,8$, CCM increases full-image PSNR by 1.104, 0.738, and 0.627 dB and reduces LPIPS by 0.041, 0.028, and 0.018 (Table~\ref{tab:seed-inputs}). The largest gains occur with the sparsest input.
```


原文（本轮基线第 222 行）

```latex
Independent reference geometry establishes correspondences between recorded and off-trajectory views. Dynamic actors are transformed with shared states. The reference evaluator removes occlusion-ambiguous correspondences for every method; finite outputs and rendering coverage determine method validity. Test LiDAR is used only by the evaluator. Linear-RGB MAE is measured on both each method's valid subset and their intersection, which covers 58.7\% of the reference set (Table~\ref{tab:reprojection}). Ours achieves 0.019 common-support MAE and 92.4\% overall coverage.
```


修改后（当前第 224 行）

```latex
Independent reference geometry establishes correspondences between recorded and off-trajectory views. Dynamic actors are transformed with shared states. The reference evaluator removes occlusion-ambiguous correspondences for every method; finite outputs and rendering coverage determine method validity. Test LiDAR is used only by the evaluator. Linear-RGB MAE is measured on both each method's valid subset and their intersection, which covers 58.7\% of the reference set (Table~\ref{tab:reprojection}). CCM reduces common-support MAE from 0.028 to 0.019 and raises overall coverage from 86.9\% to 92.4\% relative to w/o CCM.
```


原文（本轮基线第 227 行）

```latex
Table~\ref{tab:hidden-regions} uses the same 100 synthetic test scenes and 12,000 shifted target images per seed combination. Over the stronger object-coupling control, CCM adds 0.67 dB PSNR, reduces LPIPS by 0.020, and increases coverage and F-score by 2.6 and 3.6 percentage points. Surface evaluation uses original metric coordinates, 65,536 area-uniform samples from each mesh, and a shared 2 cm point-to-triangle threshold.
```


修改后（当前第 229 行）

```latex
Table~\ref{tab:hidden-regions} uses the same 100 synthetic test scenes and 12,000 shifted target images per seed combination. Each learned variant produces 108,000 outputs across nine seed combinations; scene-wise scores include all views, frames, and seeds. Over the object-coupling control, CCM adds 0.67 dB PSNR, reduces LPIPS by 0.020, and increases coverage and F-score by 2.6 and 3.6 percentage points. The PSNR gain over the scene-latent control is 0.94 dB. Surface evaluation uses original metric coordinates, 65,536 area-uniform samples from each mesh, and a shared 2 cm point-to-triangle threshold.
```


原文（本轮基线第 233 行）

```latex
Common-support error and coverage separate correspondence accuracy from the extent of reconstructed content.
```


修改后（当前第 235 行）

```latex
% 此重复句已删除，定义和数值保留在相邻段落及表格。
```


原文（本轮基线第 239 行）

```latex
% 原位置无此段。
```


修改后（当前第 240 行）

```latex

CCM adds 1.02, 1.28, and 1.54 dB for severely missing background, vehicle, and human regions (Table~\ref{tab:visibility}). Well-observed regions gain 0.04, 0.04, and 0.03 dB, concentrating the benefit where input coverage is limited.
```


原文（本轮基线第 345 行）

```latex
The three training seeds $\{0,1,2\}$ and three generation seeds $\{7,17,27\}$ yield 360 edits on the same twenty real scenes (Table~\ref{tab:edit-seeds}). Vehicles succeed in 177/180 edits (98.33\%), humans in 157/180 (87.22\%), and the aggregate in 334/360 (92.78\%). The sample SD of the three training-seed mean success rates is 0.48 percentage points. Scene-cluster bootstrap sampling retains all eighteen edits for a selected scene, giving a 95\% interval of 85.28--99.17\%. The 26 failures are concentrated in four scenes with 9, 8, 6, and 3 failures. The clustered interval describes scene variation; training-seed SD is reported separately.
```


修改后（当前第 348 行）

```latex
The three training seeds $\{0,1,2\}$ and three generation seeds $\{7,17,27\}$ yield 360 edits on the same twenty real scenes (Table~\ref{tab:edit-seeds}). Vehicles succeed in 177/180 edits (98.33\%), humans in 157/180 (87.22\%), and the aggregate in 334/360 (92.78\%). The sample SD of the three training-seed mean structural-integrity rates is 0.48 percentage points. Scene-cluster bootstrap sampling retains all eighteen edits for a selected scene, giving a 95\% structural-integrity interval of 85.28--99.17\%. The 26 failures are concentrated in four scenes with 9, 8, 6, and 3 failures.
```


原文（本轮基线第 352 行）

```latex
Table~\ref{tab:real-edit-quality} scores the original 360 actor edits from twenty scenes and nine seed combinations; camera shifts add no actor-edit trials. Joint acceptance is the per-edit intersection of the four criteria. Of 334 structurally intact edits, 36 fail at least one added quality check, leaving 298 joint passes (82.78\%). The 62 joint failures comprise 26 structural failures and these 36 additional failures. The 0.48-point training-seed SD and 85.28--99.17\% scene-cluster interval above describe structural integrity. Canonical linear-RGB MAE 0.014 measures previously observed human texture; new-surface ratings measure visual quality and identity consistency.
```


修改后（当前第 355 行）

```latex
Table~\ref{tab:real-edit-quality} scores 360 actor edits from twenty scenes and nine seed combinations; camera shifts add no actor-edit trials. Joint acceptance is the per-edit intersection of the four criteria, yielding 298 passes (82.78\%). The 62 failures comprise 26 structural failures and 36 structurally intact edits that fail at least one other quality check.
```


原文（本轮基线第 357 行）

```latex
The 360-edit quality evaluation uses fixed target-state and view lists. A separate expanded protocol applies vehicle yaw changes of $30^\circ$, $60^\circ$, and $90^\circ$, and human maximum non-root joint rotation differences of $15^\circ$, $30^\circ$, and $45^\circ$ at fixed root placement. Across the same scene/seed combinations, this state grid defines 1,080 actor edits and 3,240 images from three predefined target views per edit. Its sample count is separate from the 360-edit quality evaluation. Each seed reuses one completed asset across all states, with the five-pixel criterion defined at $240\times160$ resolution.
```


修改后（当前第 360 行）

```latex
The 360-edit quality evaluation uses fixed target-state and view lists. The expanded protocol applies vehicle yaw changes of $30^\circ$, $60^\circ$, and $90^\circ$, and human maximum non-root joint rotation differences of $15^\circ$, $30^\circ$, and $45^\circ$ at fixed root placement. Twenty scenes and nine seed combinations yield $20\times9\times(3+3)=1,080$ actor edits. Three predefined target views per edit give 3,240 images. Each seed reuses one completed asset across all states, with the five-pixel criterion defined at $240\times160$ resolution.
```


原文（本轮基线第 381 行）

```latex
For Ours, 0.18\% added occlusion corresponds to 3,636 rays and 0.07\% strict violation to 1,414. The stricter violation set can be a subset of the added-occlusion set. Relative to the pre-completion scene, input-view PSNR decreases by 0.029 dB and depth MAE increases by 2 mm. Removing the free-ray loss raises the two ray rates to 1.34\% and 0.91\%, showing its effect on rendering beyond query-level parameter preservation.
```


修改后（当前第 384 行）

```latex
For Ours, 0.18\% added occlusion corresponds to 3,636 rays and 0.07\% strict violation to 1,414. Relative to the pre-completion scene, input-view PSNR decreases by 0.029 dB and depth MAE increases by 2 mm. Removing the free-ray loss raises the two ray rates to 1.34\% and 0.91\%, showing its effect on rendering beyond query-level parameter preservation.
```


原文（本轮基线第 427 行）

```latex
% 原位置无此段。
```


修改后（当前第 430 行）

```latex
Let $Q=Q_b+\sum_a Q_a^{\mathrm{vehicle}}+\sum_h Q_h^{\mathrm{human}}$ count non-sky queries. Decoding produces $4Q$ candidate Gaussians, which bound the non-transparent output count. The mean of 1.4 million therefore corresponds to at least 350,000 non-sky queries per scene on average. Sky uses the separate cubemap head.

```


#### paper/supplementary/evaluation_zh.tex

同步英文新增数值结论及局部精简，保留所有表格数值和评价口径。


原文（本轮基线第 174 行）

```latex
% 原位置无此段。
```


修改后（当前第 174 行）

```latex

在 $T=2,4,8$ 时，CCM 分别将全图 PSNR 提高 1.104、0.738 和 0.627 dB，LPIPS 降低 0.041、0.028 和 0.018（表~\ref{tab:seed-inputs}）。输入最稀疏时收益最大。
```


原文（本轮基线第 227 行）

```latex
独立参考几何建立记录视图与离轨视图的对应，动态参与者按共享状态变换。参考评价器统一排除遮挡不确定的对应，各方法的有效性由有限输出和渲染覆盖确定。测试 LiDAR 专用于评价器。线性 RGB MAE 同时在各自有效区域及其交集上计算，共有区域占参考集合的 58.7\%（表~\ref{tab:reprojection}）。Ours 的共有区域 MAE 为 0.019，总覆盖率为 92.4\%。
```


修改后（当前第 229 行）

```latex
独立参考几何建立记录视图与离轨视图的对应，动态参与者按共享状态变换。参考评价器统一排除遮挡不确定的对应，各方法的有效性由有限输出和渲染覆盖确定。测试 LiDAR 专用于评价器。线性 RGB MAE 同时在各自有效区域及其交集上计算，共有区域占参考集合的 58.7\%（表~\ref{tab:reprojection}）。相对 w/o CCM，CCM 将共有区域 MAE 从 0.028 降至 0.019，总覆盖率从 86.9\% 提高至 92.4\%。
```


原文（本轮基线第 232 行）

```latex
表~\ref{tab:hidden-regions} 使用相同的 100 个合成测试场景，每组种子含 12,000 张偏移目标图像。相对较强的对象耦合对照，CCM 将 PSNR 提高 0.67 dB、LPIPS 降低 0.020，覆盖率与 F-score 分别提高 2.6 和 3.6 个百分点。表面评价在原始米制坐标中进行，预测与参考网格各取 65,536 个面积均匀采样点，采用相同的 2 cm 点到三角网格距离阈值。
```


修改后（当前第 234 行）

```latex
表~\ref{tab:hidden-regions} 使用相同的 100 个合成测试场景，每组种子含 12,000 张偏移目标图像。每个学习版本的九组种子共生成 108,000 张输出，场景统计保留全部视角、帧和种子结果。相对对象耦合对照，CCM 将 PSNR 提高 0.67 dB、LPIPS 降低 0.020，覆盖率与 F-score 分别提高 2.6 和 3.6 个百分点；相对场景潜码对照，PSNR 提高 0.94 dB。表面评价在原始米制坐标中进行，预测与参考网格各取 65,536 个面积均匀采样点，采用相同的 2 cm 点到三角网格距离阈值。
```


原文（本轮基线第 238 行）

```latex
表~\ref{tab:reprojection} 的共有支持集误差与覆盖率分别描述对应精度和重建内容范围。
```


修改后（当前第 240 行）

```latex
% 此重复句已删除，定义和数值保留在相邻段落及表格。
```


原文（本轮基线第 244 行）

```latex
% 原位置无此段。
```


修改后（当前第 245 行）

```latex

CCM 在严重缺失的背景、车辆和人体区域分别增加 1.02、1.28 和 1.54 dB（表~\ref{tab:visibility}），充分观测区域分别增加 0.04、0.04 和 0.03 dB，收益主要集中在输入覆盖不足的区域。
```


原文（本轮基线第 350 行）

```latex
三个训练种子 $\{0,1,2\}$ 与三个生成种子 $\{7,17,27\}$ 在相同二十个真实场景上形成 360 次编辑（表~\ref{tab:edit-seeds}）。车辆成功 177/180 次（98.33\%），人体 157/180 次（87.22\%），总体 334/360 次（92.78\%）。三个训练种子均值的样本 SD 为 0.48 个百分点。场景聚类 bootstrap 每次保留被抽中场景的全部十八次编辑，95\% 区间为 85.28--99.17\%。26 次失败集中在四个场景，分别为 9、8、6 和 3 次。聚类区间描述场景差异，训练种子 SD 单独报告。
```


修改后（当前第 353 行）

```latex
三个训练种子 $\{0,1,2\}$ 与三个生成种子 $\{7,17,27\}$ 在相同二十个真实场景上形成 360 次编辑（表~\ref{tab:edit-seeds}）。车辆成功 177/180 次（98.33\%），人体 157/180 次（87.22\%），总体 334/360 次（92.78\%）。三个训练种子结构完整性均值的样本 SD 为 0.48 个百分点。场景聚类 bootstrap 每次保留被抽中场景的全部十八次编辑，结构完整性的 95\% 区间为 85.28--99.17\%。26 次失败集中在四个场景，分别为 9、8、6 和 3 次。
```


原文（本轮基线第 357 行）

```latex
表~\ref{tab:real-edit-quality} 评价原有二十个场景、九组种子的 360 次演员编辑，相机平移不增加演员编辑分母。联合通过按逐例交集计算。334 次结构完整编辑中，36 次未通过至少一项新增质量检查，四项联合通过 298 次（82.78\%）。62 次联合失败由 26 次结构失败与另外 36 次质量失败组成。前述 0.48 个百分点训练种子 SD 和 85.28--99.17\% 场景聚类区间均描述结构完整性。规范对应线性 RGB MAE 0.014 衡量人体原已见纹理保持，新增表面评价衡量视觉质量与身份一致性。
```


修改后（当前第 360 行）

```latex
表~\ref{tab:real-edit-quality} 评价二十个场景、九组种子的 360 次演员编辑，相机平移不增加演员编辑分母。联合通过按四项判据的逐例交集计算，共通过 298 次（82.78\%）。62 次失败包括 26 次结构失败，以及 36 次结构完整但未通过至少一项其他质量检查的编辑。
```


原文（本轮基线第 362 行）

```latex
360 次编辑质量评价使用固定目标状态与视角清单。扩展协议设置车辆偏航角变化 $30^\circ$、$60^\circ$、$90^\circ$，人体最大非根关节旋转差 $15^\circ$、$30^\circ$、$45^\circ$，根放置固定。在相同场景／种子组合上，该状态网格定义 1,080 次演员编辑，每次三个预定义目标视角，共 3,240 幅图像，分母与原 360 次编辑质量评价分开。每个种子在全部状态中复用同一完成资产，五像素判据在 $240\times160$ 分辨率下计算。
```


修改后（当前第 365 行）

```latex
360 次编辑质量评价使用固定目标状态与视角清单。扩展协议设置车辆偏航角变化 $30^\circ$、$60^\circ$、$90^\circ$，人体最大非根关节旋转差 $15^\circ$、$30^\circ$、$45^\circ$，根放置固定。二十个场景与九组种子共形成 $20\times9\times(3+3)=1,080$ 次演员编辑，每次三个预定义目标视角，共 3,240 幅图像。每个种子在全部状态中复用同一完成资产，五像素判据在 $240\times160$ 分辨率下计算。
```


原文（本轮基线第 386 行）

```latex
Ours 的 0.18\% 新增遮挡对应 3,636 条射线，0.07\% 严格违规对应 1,414 条；更严格的违规集合可以是新增遮挡集合的子集。相对补全前，输入视角 PSNR 下降 0.029 dB，深度 MAE 增加 2 mm。去掉自由射线损失后，两类射线比例升至 1.34\% 和 0.91\%，说明该损失约束了查询级参数保持之外的渲染影响。
```


修改后（当前第 389 行）

```latex
Ours 的 0.18\% 新增遮挡对应 3,636 条射线，0.07\% 严格违规对应 1,414 条。相对补全前，输入视角 PSNR 下降 0.029 dB，深度 MAE 增加 2 mm。去掉自由射线损失后，两类射线比例升至 1.34\% 和 0.91\%，说明该损失约束了查询级参数保持之外的渲染影响。
```


原文（本轮基线第 432 行）

```latex
% 原位置无此段。
```


修改后（当前第 435 行）

```latex
令 $Q=Q_b+\sum_a Q_a^{\mathrm{vehicle}}+\sum_h Q_h^{\mathrm{human}}$ 为非天空查询总数。解码生成 $4Q$ 个候选高斯，非透明输出数量以此为上界，因此平均 140 万非透明高斯对应每场景平均至少 350,000 个非天空查询。天空由独立 cubemap 头输出。

```


#### paper/supplementary/frontend.tex

将 0.10 m 明确为支撑邻域边长；中文现文已有该定义，保持原文。


原文（本轮基线第 21 行）

```latex
The background base grid spans $[-20,80]\times[-30,30]\times[-3,15]$ m with $20\times12\times6$ cells, giving $5\times5\times3$ m cell scales. Up to 2,048 observed anchors add 0.20 m support cells. Each vehicle uses an $8\times4\times4$ grid inside its actual bounding box, with cell sides $(L/8,W/4,H/4)$ and up to 512 observed anchors of side 0.20 m. Human queries lie on the canonical template with 0.10 m support neighborhoods. Sky has six cubemap faces with $4\times4$ direction queries per face. Background attention groups use 4 m spatial bins; this grouping scale is independent of the support-cell scales.
```


修改后（当前第 21 行）

```latex
The background base grid spans $[-20,80]\times[-30,30]\times[-3,15]$ m with $20\times12\times6$ cells, giving $5\times5\times3$ m cell scales. Up to 2,048 observed anchors add 0.20 m support cells. Each vehicle uses an $8\times4\times4$ grid inside its actual bounding box, with cell sides $(L/8,W/4,H/4)$ and up to 512 observed anchors of side 0.20 m. Human queries lie on the canonical template with support neighborhoods of side 0.10 m. Sky has six cubemap faces with $4\times4$ direction queries per face. Background attention groups use 4 m spatial bins; this grouping scale is independent of the support-cell scales.
```


#### paper/supplementary/references.bib

补充材料使用相同的 JRM 正式条目。


原文（本轮基线第 27 行）

```latex
@article{wu2026jrm,
```


修改后（当前第 27 行）

```latex
@inproceedings{wu2026jrm,
```


原文（本轮基线第 30 行）

```latex
  journal={arXiv preprint arXiv:2603.25985},
```


修改后（当前第 30 行）

```latex
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
```


原文（本轮基线第 32 行）

```latex
  url={https://arxiv.org/abs/2603.25985},
```


修改后（当前第 32 行）

```latex
  pages={307--316},
  url={https://openaccess.thecvf.com/content/CVPR2026/html/Wu_JRM_Joint_Reconstruction_Model_for_Multiple_Objects_without_Alignment_CVPR_2026_paper.html},
```


#### paper/supplementary/training.tex

补明 100/20 个合成场景和 20 个真实场景的评价用途，明确 16 个记忆 token 为可学习参数。


原文（本轮基线第 8 行）

```latex
% 原位置无此段。
```


修改后（当前第 8 行）

```latex

The synthetic test split supplies 100 scenes for paired hidden-surface evaluation and 20 scenes for asset editing. Fixed-asset reuse is also evaluated on 20 real scenes (Appendices H and I).
```


原文（本轮基线第 59 行）

```latex
Completion network & Width 128; 4 layers; 4 heads; 16 memory tokens \\
```


修改后（当前第 61 行）

```latex
Completion network & Width 128; 4 layers; 4 heads; 16 learnable memory tokens \\
```


#### paper/supplementary/training_zh.tex

同步英文数据用途与记忆 token 定义。


原文（本轮基线第 8 行）

```latex
% 原位置无此段。
```


修改后（当前第 8 行）

```latex

合成测试划分中，100 个场景用于隐藏表面的配对评价，20 个场景用于资产编辑；另在 20 个真实场景上评价固定资产复用（附录 H 和 I）。
```


原文（本轮基线第 59 行）

```latex
补全网络 & 宽度 128，4 层，4 头，16 个记忆 token \\
```


修改后（当前第 61 行）

```latex
补全网络 & 宽度 128，4 层，4 头，16 个可学习记忆 token \\
```

---

## 2026-11-04 总览 PDF 与机制矢量图入稿

本轮按作者“替换到中英文论文并重新编译检查排版”的要求，接入指定总览 PDF 和修订后的 draw.io 机制 PDF。真实起点为 HEAD `a0ccb6b509f7b6454313f4108b956741b5ca4fd3` 之后的未提交工作区；已有改动不计入本轮贡献。插图引用和使用说明原文取自[本轮实际基线](../../_archive/drivecompose/20261104-overview-mechanism-replacement/baseline/)，完整哈希与范围见[基线清单](../../_archive/drivecompose/20261104-overview-mechanism-replacement/baseline-manifest.json)。

### 插图引用与连线

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| `paper/main.tex`、`paper/main_zh.tex` 的图 2 | `\includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}` | `\includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.pdf}` | 直接采用作者指定的最新 PDF，保留原文件的矢量对象与图片 |
| `paper/sec/3_method.tex`、`paper/zh/3_method_zh.tex` 的图 3 | `\includegraphics[width=\linewidth]{fig/drivecompose-joint-completion.png}` | `\includegraphics[width=\linewidth]{fig/drivecompose-joint-completion.pdf}` | 接入已修正箭头及反馈路径的机制矢量图 |
| 三组局部注意力 | 中间 token 上方两个箭头拥挤，曲率不统一 | 平滑公共弧线及三个均匀箭头 | 解决作者指出的箭头外观问题 |
| 迭代反馈 | 反馈线在 `S steps` 文字处断开 | 一条完整反馈连接，文字放在线外 | 保持状态迭代路径连续、可编辑 |

插图宽度、图注、编号和引用标签保持。两版图 2 仍位于第 3 页、图 3 位于第 4 页。机制 PDF 无内嵌光栅图，实际单栏宽度约 83.34 mm，正文标签约 8.16–8.33 pt；总览 PDF 逐字节采用作者文件，原有照片像素保留。总览局部小字仍偏小，`Depth+ ID` 按实际放置尺寸约 4.39 pt，未擅自重画源图。

### 使用说明的中英同步

为准确说明当前图件的制作方式，仅替换两版使用说明中的相关一句，其余说明保持。

英文原文：

> OpenAI Image Gen was used for the conceptual scene and method illustrations in Figs.~\ref{fig:teaser}--\ref{fig:joint-completion}.

英文修改后：

> OpenAI Image Gen assisted the conceptual scene and method-illustration designs. The overview uses the author-supplied PDF, and the joint-completion diagram was rebuilt as editable vectors in draw.io.

中文原文：

> OpenAI Image Gen 用于图~\ref{fig:teaser}--\ref{fig:joint-completion} 的概念场景与方法插图。

中文修改后：

> OpenAI Image Gen 辅助概念场景与方法插图设计。总览图采用作者提供的 PDF，联合补全机制图通过 draw.io 重建为可编辑矢量图。

### 编译与最终输出

两份主稿通过已有 `paper/tools/build.py` 及 Tectonic 重编。最初正式英文 PDF 被占用，已在项目外编译候选、完成校验后按字节一致地原子替换正式路径；编译记录同时保留实际候选路径及正式安装结果。英文共 11 页，完整结论及 `sec:main-text-end` 均在第 8 页；中文共 10 页，完整正文止于第 7 页。结论全文匹配、图表页码、引用、溢出、图件哈希和页面渲染均已检查，未见缺字、未定义引用、裁切或重叠；中文保留原有第 6 页仅含浮动图的提示。

73 项稿件结构检查及 21 项本轮核验通过。检查器改为从当前图件清单读取 PDF 选择并核对两个 PDF 和 draw.io 源文件的哈希，历史 PNG 来源检查仍保留。未修改科研叙述、公式、实验数值、图注或格式参数；同期其他会话的补充材料修改原样保留。本轮仅重新编译主稿，不声称重编补充。完整来源和最终输出见[验收记录](../paper/provenance/figure-replacement-20261104.json)，页图与候选统一在[项目外工作目录](../../_archive/drivecompose/20261104-overview-mechanism-replacement/)。

---

## 2026-11-04 将作者指定 PPT 替换为首页 teaser

本轮问题与范围：作者指定 `paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx` 直接替换论文 teaser；原 Figure 1 仍是早期概念图。本轮只接入现有图稿并重编主稿，PPT 内容、两版图注、正文与版式参数保持。

按此前要求先同步远端，HEAD 从 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe` 快进至 `a0ccb6b509f7b6454313f4108b956741b5ca4fd3`。保留本地未提交工作，并在远端移动后的总览图位置继续使用此前的 `DriveCompose.pdf`；这项为已有成果的保留，不计作新图设计。图替换的真实基线是同步并恢复本地修改后的工作区，见[基线清单](../paper/build/teaser-paper-integration/integration-baseline.json)与[原文件快照](../paper/build/teaser-paper-integration/before-integration/)。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 双语首页 Figure 1 的图件 | 原 `drivecompose-concept-merged.pdf`，SHA-256 `3031f2f09069d714ed267cb0390d6ea978e23304b7c7a23d5f5e0225773b1a40` | 同一路径改为指定 PPT 的完整页面，SHA-256 `5f1e29a61e407e9e4c597e579b1eb8b7eeb2f58d21560b430562908b58e59d3e` | 将作者确认的图稿实际接入论文 |
| 图幅与图内内容 | 720 × 378 pt；早期概念场景 | 图幅仍为 720 × 378 pt；共享输入、上下方法对比、联合补全及三种状态复用均来自作者现有 PPT | 保留原有排版尺寸，不另行设计 |
| 英文图注开头 | “From observations to reusable completed assets.” | 原文保留，整条图注逐字不变 | 本轮仅替换图件 |
| 中文图注开头 | “从观测到可复用的完成资产。” | 原文保留，整条图注逐字不变 | 与英文同一修改范围 |
| 英文／中文完整正文结束页 | 第 8／7 页 | 第 8／7 页 | 核对总结全文及结束标签，确认换图未造成超页 |

来源 PPT SHA-256 为 `eda0c26a9fa6b493bc441dd16eb6c406b2137c8de5616786d712544f5b734008`；导出前后哈希相同，作者最新保存的排版与文字保留。采用完整单页 5400 × 2835 像素渲染后封装为 PDF，非原生矢量导出；两版最终 PDF 的内嵌图像与该导出逐像素一致。P2–P6 继续作为概念示意，不作为实验结果。

英文与中文主稿均重新编译成功，总页数分别为 11／10 页；完整总结与正文结束标签分别在第 8／7 页。已渲染复核两版首页和正文末页，无新增重叠或裁切；编译日志无未定义引用、缺字或溢出错误。当前 [英文主稿](../paper/build/en/main.pdf)、[中文主稿](../paper/build/zh/main_zh.pdf)及[采用与核验记录](../paper/provenance/teaser-ppt-replacement-20261104.json)可检查。补充材料未修改，未新建提交或推送。

---

## 2026-11-04 提交前归档临时图稿

按作者“将临时文件移出仓库并提交和推送”的要求，仅整理文件及归档入口。起点为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe` 之后的未提交工作区；已有论文修订属于本次整理前的成果。实际起点的文件哈希和 Git 状态见[工作区基线](../../_archive/drivecompose/20261104-pre-push-cleanup/workspace-before.json)，本轮修改的两份说明文件原文也已单独保存。

| 位置／原状态 | 整理后 | 原因 |
|---|---|---|
| `docs/figures/joint-completion-vector/` 中未采用的 draw.io／PowerPoint 候选、导出与核验 | 移至仓库外，原目录仅保留当前选择和归档入口说明 | 保留可恢复的原件，移出已退出论文的候选 |
| `simplification/` 中生成草稿、提示词、规格与审查记录 | 按原层级归档；正式 `paper/fig/drivecompose-joint-completion.png` 保留 | 草稿 PNG 与活动图重复，过程材料可由清单追溯 |
| `paper/fig/drivecompose-joint-completion.pdf` | 移至仓库外 | 两版主稿均使用作者选定 PNG，此 PDF 为未采用的矢量候选 |

共迁移 16 个文件，逐文件核对 SHA-256；正式图件、四份主稿／补充 PDF、论文源文、实验值和证据记录保留。本轮未改中英文论文文字或排版。完整原路径与新路径见[迁移清单](../../_archive/drivecompose/20261104-pre-push-cleanup/archive-manifest.json)，整理与检查结果见[仓库记录](../paper/provenance/pre-push-cleanup-20261104.json)。

---

## 2026-11-04 修正正文超页：总结全文收回第 8 页

作者指出的问题属实：上一版英文 PDF 中，第六章标题在第 8 页，但结尾四行续到了第 9 页。此前记录将标题所在页误当作正文终止页，所称“正文 8 页”不成立。本轮以完整总结段落的 PDF 文本匹配、最后一句的实际位置及 `sec:main-text-end` 标签共同验收，不再用标题页代替正文结束页。

真实基线为实验集中组织后的未提交工作区，HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。原英文 PDF SHA-256 为 `7989fbe80ff430c4ff8d652c31e085f24b2fc6c03b58ef6aa8a0c0873b38988a`；[本轮实际基线](../../_archive/drivecompose/20261104-page-layout-fix/baseline/)、[英文逐行差异](../../_archive/drivecompose/20261104-page-layout-fix/en-source-changes.diff)和[中文逐行差异](../../_archive/drivecompose/20261104-page-layout-fix/zh-source-changes.diff)已保留。

### 正文终止位置前后对照

| 检查对象 | 修改前 | 修改后 | 依据 |
|---|---|---|---|
| 英文第六章标题 | 第 8 页 | 第 8 页 | 标题页只能说明起点 |
| 英文总结最后一句 | 第 9 页 | 第 8 页 | 将源文完整段落匹配到 PDF，逐行复核末句 |
| 英文正文结束标签 | 第 9 页 | 第 8 页 | `sec:main-text-end` 的编译结果 |
| 英文第 9 页开头 | 总结续行，然后是使用说明 | 从 LLM Usage Statement 开始 | 已渲染并目视复核 |
| 中文正文结束 | 第 7 页 | 第 7 页 | 同样核对全文与结束标签 |

英文完整总结原文逐字保留，最后一句仍为：

> Waymo reconstruction, paired surface metrics, and multidimensional real-edit ratings establish completion quality and state-driven reuse.

[CVPR 2027 作者指南](https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines)于 2026-11-04 复核：正文含图表最多 8 页，引用与必需的 LLM 使用说明另计。新英文 PDF 共 11 页，技术内容完整止于第 8 页，第 9–11 页为使用说明与引用；中文共 10 页，正文完整止于第 7 页。

### 三处局部去重及中英对应

没有压缩总结、删去实验结果或改变图表内容。只处理实验中重复的说明，保持 4.5 集中消融的组织。

英文表 3 图注原文：

```latex
\caption{\textbf{Component ablations on Waymo.} $T=8$, with shared recovery, codec, and target views. Means cover three training and three generation seeds; full SDs are in Appendix G.}
```

修改后：

```latex
\caption{\textbf{Component ablations on Waymo.} $T=8$, with shared recovery, codec, and target views. Full SDs are in Appendix G.}
```

原因：三个训练种子、三个生成种子及所有输出平均的协议已在紧邻正文完整说明；图注保留 T=8、共享组件和完整 SD 的附录定位。

英文编辑后补全段落原文：

```latex
\paragraph{Completion after editing.}
On twenty identity-disjoint synthetic scenes, each containing one vehicle and one human, we apply a 1 m camera shift, $30^\circ$ vehicle rotation, and human pose change to fixed completed assets. Joint completion gives the best PSNR, LPIPS, and surface coverage for newly visible vehicle and human surfaces (Table~\ref{tab:asset-reuse}), evaluated at 2 cm vehicle and 1 cm human thresholds.
```

修改后：

```latex
\paragraph{Completion after editing.}
We apply the edits in Sec.~\ref{sec:ablation-reuse} to twenty identity-disjoint synthetic scenes, each containing one vehicle and one human. Joint completion gives the best PSNR, LPIPS, and surface coverage for newly visible surfaces (Table~\ref{tab:asset-reuse}).
```

原因：相机平移 1 m、车辆旋转 30 度及人体换姿已在 4.4 给出，当前直接引用该节；车辆 2 cm／人体 1 cm 的覆盖率阈值在表 5 图注及表头保留。20 个身份隔离场景和每场景车辆／人体构成保留，结果含义不变。

中文表 3 图注原文：

```latex
\caption{\textbf{Waymo 组件消融。}$T=8$，恢复模块、codec 与目标视图相同。报告三个训练种子和三个生成种子的均值；完整 SD 见补充材料附录 G。}
```

修改后：

```latex
\caption{\textbf{Waymo 组件消融。}$T=8$，恢复模块、codec 与目标视图相同。完整 SD 见附录 G。}
```

原因：三个训练种子、三个生成种子及所有输出平均的协议已在紧邻正文完整说明；图注保留 T=8、共享组件和完整 SD 的附录定位。

中文编辑后补全段落原文：

```latex
\paragraph{编辑后的补全。}
在 20 个身份隔离合成场景上，每个场景各含一辆车和一个人体，相机平移 1 m、车辆旋转 $30^\circ$ 及人体换姿均复用固定完成资产。联合补全在新增可见车辆与人体表面的 PSNR、LPIPS 和覆盖率上均取得最优结果（表~\ref{tab:asset-reuse}），车辆／人体评价阈值为 2／1 cm。
```

修改后：

```latex
\paragraph{编辑后的补全。}
在 20 个身份隔离合成场景上执行第~\ref{sec:ablation-reuse} 节的相同编辑，每个场景各含一辆车和一个人体。联合补全在新增可见表面的 PSNR、LPIPS 和覆盖率上均取得最优结果（表~\ref{tab:asset-reuse}）。
```

原因：相机平移 1 m、车辆旋转 30 度及人体换姿已在 4.4 给出，当前直接引用该节；车辆 2 cm／人体 1 cm 的覆盖率阈值在表 5 图注及表头保留。20 个身份隔离场景和每场景车辆／人体构成保留，结果含义不变。

可见率段落原文首句：

- EN: `CCM benefits severely missing regions more than well-observed ones.`
- ZH: `CCM 对严重缺失区域的收益高于充分可见区域。`

修改后删除这两个重复概括句。后文仍完整保留 100 个合成场景、充分可见与严重缺失的分组阈值、三类资产各自的增益及读取范围干预的补充定位；这组实测比较已经直接说明同一发现。

### 保留项与验收

- 题名、确认摘要、引言、相关工作、方法、讨论及两版总结源文件全部保持。所有公式、五张表主体、实验数值、引用键、图片及显示尺寸保持；补充材料源文和两份 PDF 保持。编辑条件从正文重复列举改为明确交叉引用，没有迁入补充材料。
- 没有改页边距、字体、行距、表格字级、图大小或模板；没有新增负间距、强制分页或浮动规则。篇幅收益来自上述三处文本去重。
- 专项检查先对旧 PDF 验证，准确识别总结跨第 8–9 页；再对新 PDF 匹配完整总结，确认全文及末尾标签均为第 8 页。21 项专项检查和 70 项现有结构检查通过。最终编译日志无未定义引用、缺字、重复标签或 overfull。
- 已看英文第 8、9 页高清渲染及中文第 7 页；同时检查两版全部正文缩略图。英文总结完整收在第 8 页，第 9 页不再出现总结续行。没有正文图表漂到第 9 页。
- 上轮 `experiment-consolidation-20261103.json` 已补充勘误，改正实际正文终止页及错误的页数检查状态，并标记由[本轮验收](../paper/provenance/page-layout-fix-20261104.json)替代；不将其旧页数结论继续当作当前状态。

---

## 2026-11-03 实验组织：将受控比较集中到消融实验

本轮问题有明确位置：原 4.4“隐藏表面补全”含 w/o GCM、w/o CCM 和替代机制比较，4.5 再解释组件消融，4.6“资产复用”又加入相同组件比较、自由射线损失移除和 CCM 成本。读者需要跨三个小节拼接设计证据。按作者“消融实验不要写得到处都是”的要求，合并这些受控比较；其他准确段落原样保留。沿用 `ml-paper-writing` 与已确认的 `cvpr-paper-standard`。

真实基线为作者指定 PNG 入稿后的未提交工作区，HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，不是本轮原文。两版实验源文、正式 PDF 及记录的真实起点保存在[本轮基线](../../_archive/drivecompose/20261103-experiment-consolidation/baseline/)；[英文逐行差异](../../_archive/drivecompose/20261103-experiment-consolidation/en-source-changes.diff)和[中文逐行差异](../../_archive/drivecompose/20261103-experiment-consolidation/zh-source-changes.diff)仅比较本轮起点与当前实验文件。

### 对照的录用论文与实际采用之处

| 样本与复核位置 | 实际观察 | 本稿采用 |
|---|---|---|
| [VGGT，CVPR 2025，第 7 页 / 4.5 节](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf) | 骨干与多任务设计比较集中在 Ablation Studies，以短段题说明设计问题 | 一个消融小节，下设按问题命名的段首标题 |
| [Fast3R，CVPR 2025，第 7–8 页 / 第 5 节](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf) | 主要任务比较与视图数量、模型和局部头等设计干预分开组织 | 主任务先建立效果，随后集中解释组件和机制 |
| [HorizonForge，CVPR 2026，第 7–8 页 / 4.2–4.3 节](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf) | 条件表示和扩散模型比较归入同一消融节，用户评价另节呈现 | 完整方法的真实编辑质量与合成配对组件消融分别叙述 |

这些是样本的组织方式，不是 CVPR 对章节数量的规定；未模仿样本中无证据的宣传语或改变本稿实验条件。

### 章节与表格位置前后对照

| 原位置 / 标题 | 当前位置 / 标题 | 原因 |
|---|---|---|
| 4.1 Experimental setup / 实验设置 | 4.1，正文原样保留 | 现有协议已清楚，无需重写 |
| 4.2 Dynamic scene reconstruction / 动态场景重建 | 4.2，正文原样保留 | 负责完整方法的 Waymo 重建比较 |
| 4.3 Off-trajectory rendering / 轨迹外渲染 | 4.3，正文原样保留 | 负责完整方法的轨迹外分布质量比较 |
| 4.6 State-driven asset reuse / 状态驱动资产复用 | 4.4，同名；只保留完整方法的真实编辑、观测保持和绝对效率 | 组件删减与损失移除集中到后面的消融 |
| 4.5 Ablation studies / 消融实验 | 4.5，先定义控制变体，再依次解释 Waymo 组件、隐藏表面、可见率、编辑后补全及自由空间约束 | 一处建立完整的设计证据链 |
| 独立 4.4 Hidden-surface completion / 隐藏表面补全 | 4.5 内段首标题，原分析及指标保留 | 本质是相同重建接口下的机制对照 |
| 原表 4：组件消融 | 当前表 3，位于 4.5 的首项比较 | 先说明核心设计在 Waymo 上的效果 |
| 原表 3：隐藏区域机制比较 | 当前表 4，接续解释隐藏表面的收益 | 顺着“有效→作用在哪里”推进 |
| 原表 5：编辑后的新增表面比较 | 当前表 5，移入 4.5 | 其行是组件控制，属于消融证据 |

三张消融表的表格主体（含数值、变体和标粗）逐字保留。表 3 图注补出 Waymo，表 5 图注明确是补全消融；表 1–2、两张实验结果图及既有采样和评价段落原样保留。相关工作和方法中的稳定交叉引用标签保留，自动解析至新的 4.5 节。

### 协议限定：保留真实基线，只明确适用范围

英文原文（原 4.5）：

```latex
Ablations use one 29-timestamp window per test sequence, three cameras, nested $T=2,4,8$ inputs, and seven shared targets (Appendix G).
```

修改后（当前 4.5）：

```latex
Waymo ablations use one 29-timestamp window per test sequence, three cameras, nested $T=2,4,8$ inputs, and seven shared targets (Appendix G).
```

中文原文（原 4.5）：

```latex
每条测试序列取一个 29 时刻窗口，使用三相机、$T=2,4,8$ 嵌套输入与七个共享目标（附录 G）。
```

修改后（当前 4.5）：

```latex
Waymo 组件消融从每条测试序列取一个 29 时刻窗口，使用三相机、$T=2,4,8$ 嵌套输入与七个共享目标（附录 G）。
```

原因：29 时刻、嵌套 T=2/4/8 和七个目标属于 Waymo 组件实验；100 个合成隐藏表面场景与 20 个身份隔离合成编辑场景继续在各自段落说明，不让读者误认为所有消融采用同一组数据。主比较的 20 帧片段、12 张上下文图和 C 主协议均保留。

### 资产复用与组件对照分开，但不删除编辑证据

英文原文（原 4.6 同时混写两种比较）：

```latex
\paragraph{Asset edits.}
We test fixed-asset reuse on twenty real and twenty identity-disjoint synthetic scenes, each containing one vehicle and one human. A 1 m camera shift, $30^\circ$ vehicle rotation, and human pose change reuse fixed completed assets. Joint completion gives the best PSNR, LPIPS, and surface coverage for newly visible vehicle and human surfaces in the synthetic scenes (Table~\ref{tab:asset-reuse}), evaluated at 2 cm vehicle and 1 cm human thresholds.
```

修改后（4.4 完整方法的真实编辑）：

```latex
\paragraph{Asset edits.}
We test fixed-asset reuse on twenty real scenes, each containing one vehicle and one human. A 1 m camera shift, $30^\circ$ vehicle rotation, and human pose change reuse fixed completed assets. Nine training/generation-seed combinations yield 360 actor edits. The five-pixel structural-integrity criterion passes 334/360 (92.78\%); 298/360 (82.78\%) jointly pass structure, newly visible texture, appearance identity, and local geometry checks. Appendix I reports the four-of-five rating rule, failure breakdown, and seed statistics.
```

迁入 4.5 的合成配对比较：

```latex
\paragraph{Completion after editing.}
On twenty identity-disjoint synthetic scenes, each containing one vehicle and one human, we apply a 1 m camera shift, $30^\circ$ vehicle rotation, and human pose change to fixed completed assets. Joint completion gives the best PSNR, LPIPS, and surface coverage for newly visible vehicle and human surfaces (Table~\ref{tab:asset-reuse}), evaluated at 2 cm vehicle and 1 cm human thresholds.
```

中文原文（原 4.6 同时混写两种比较）：

```latex
\paragraph{资产编辑。}
我们在 20 个真实和 20 个身份隔离合成场景上测试固定资产复用，每个场景各含一辆车和一个人体。相机平移 1 m、车辆旋转 $30^\circ$ 及人体换姿均复用固定完成资产。联合补全在合成场景新增可见车辆与人体表面的 PSNR、LPIPS 和覆盖率上均取得最优结果（表~\ref{tab:asset-reuse}），车辆／人体评价阈值为 2／1 cm。
```

修改后（4.4 完整方法的真实编辑）：

```latex
\paragraph{资产编辑。}
我们在 20 个真实场景上测试固定资产复用，每个场景各含一辆车和一个人体。相机平移 1 m、车辆旋转 $30^\circ$ 及人体换姿均复用固定完成资产。九组训练／生成种子共形成 360 次参与者编辑。五像素结构完整性判据通过 334／360 次（92.78\%）；结构、新增表面纹理、外观身份与局部几何四项联合通过 298／360 次（82.78\%）。五人中至少四人同意的评判规则、失败分解与种子统计见附录 I。
```

迁入 4.5 的合成配对比较：

```latex
\paragraph{编辑后的补全。}
在 20 个身份隔离合成场景上，每个场景各含一辆车和一个人体，相机平移 1 m、车辆旋转 $30^\circ$ 及人体换姿均复用固定完成资产。联合补全在新增可见车辆与人体表面的 PSNR、LPIPS 和覆盖率上均取得最优结果（表~\ref{tab:asset-reuse}），车辆／人体评价阈值为 2／1 cm。
```

原因：真实编辑的结构完整性和四项联合质量回答完整资产是否可复用；合成配对测试回答去掉组件后新可见表面如何变化。两类证据、各自场景数量、状态变化、阈值和统计均保留。中文把 actor edits 的“演员编辑”改为“参与者编辑”，与道路参与者术语一致。

### 自由射线损失与 CCM 成本：文字保留，位置集中

| 语言 / 项目 | 原文和原位置 | 当前表达和位置 | 原因 |
|---|---|---|---|
| EN / ray loss | 4.6 Observation preservation: “On 2,020,000 fixed rays, added-occlusion and strict free-ray violation rates are 0.18\% and 0.07\%; removing the free-ray loss raises them to 1.34\% and 0.91\%.” | 4.5 Free-space constraints，原句后明确指向 Appendix J | 损失移除属于设计干预；完整方法的参数保持、输入视角退化和纹理 MAE 仍在 4.4 |
| ZH / 射线损失 | 4.6 观测保持：“在 2,020,000 条固定射线上，新增遮挡及严格自由射线违规率为 0.18\% 和 0.07\%；移除自由射线损失后增至 1.34\% 和 0.91\%。” | 4.5 自由空间约束，原数值和比较保留，注明附录 J | 与 C/F 标记干预集中，区分两种实验及其原补充定位 |
| EN / CCM time | 4.6 Efficiency: “CCM adds 5.1\% construction time.” | 4.5 Completion components: “CCM adds 5.1\% construction time (Appendix K).” | 将增量代价放在相应组件收益旁；完整方法绝对速度留在 4.4 |
| ZH / CCM 时间 | 4.6 效率：“CCM 增加 5.1\% 构建时间。” | 4.5 补全组件：“CCM 增加 5.1\% 构建时间（附录 K）。” | 同英文同步 |

### 排版调整与核验

- 英文消融标题始于第 7 页，三张受控表集中在第 8 页，按正文首次引用次序为表 3、4、5。英文技术正文和全部表图仍止于第 8 页，共 11 页，References 从第 9 页开始。
- 中文在消融之前增加浮动边界，使第 6 页的两张主结果图先排完；第 7 页从“4.5 消融实验”开始，三张受控表也在同页，不再被整页结果图打断。中文正文仍止于第 7 页，共 10 页，References 从第 8 页开始。没有改变字体、页边距、表格字级或图片尺寸。
- 双语五个表格主体、引用键、标签、所有数值种类和其实验条件均已核对；设置和主结果的源文原样保留。31 项本轮源文／编译／位置核验通过，70 项既有稿件结构检查通过。最终日志没有未定义引用、缺字、重复标签或 overfull；英文 7–8 页、中文 5–7 页已逐页视觉检查。
- 题名、确认摘要、引言、相关工作、方法、讨论和结论源文件保留。作者指定 PNG 及两版 PDF 内嵌像素一致。两份补充源文和 PDF 哈希均保持，机制图仍不放入补充材料。
- 未运行新实验，未更改结果或新增科学主张；本轮只重新组织已有、作者确认的实验。核验记录见 [experiment-consolidation-20261103.json](../paper/provenance/experiment-consolidation-20261103.json)。

---

## 2026-11-03 机制图定稿：采用作者指定 PNG

按作者最新明确选择，中英文主稿图3采用 exec-3c098566-0ff6-4440-970a-2499b09464ee.png 原图，替代此前 draw.io 矢量候选。文件1374×1145，复制到正式图件路径后 SHA-256 与作者源文件一致；两份主稿 PDF 的内嵌图像像素逐像素一致，插入宽度83.34 mm，均位于第4页。

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 中英文方法图引用 | fig/drivecompose-joint-completion.pdf | fig/drivecompose-joint-completion.png | 执行作者选定的原图，不使用矢量候选 |
| 中英文使用说明 | 声称联合补全机制图用draw.io矢量重绘 | 说明最终概念与方法插图来自Image Gen，去掉矢量入稿表述 | 与实际最终图件一致 |
| 补充材料 | 原附录L含放大机制图，前一步已删除 | 维持删除，主稿也不再指向放大图 | 遵从作者不在补充中放机制图的要求 |

本次切换的真实起点为已完成矢量候选但尚未最终交付的未提交工作区；必要源文件及两份主稿保存在 ../../_archive/drivecompose/20261103-figure3-simplification/author-png-selection/baseline/，未以更早HEAD冒充本轮原文。此前未采用的矢量候选与来源保留为过程记录。

两份主稿已重新编译并检查第4页：英文总11页、技术正文止于第8页；中文总10页、正文止于第7页。70项结构检查通过。补充材料保持已删除机制图的英文11页／中文10页版本，表S1–S24完整；这次PNG切换未改补充源文。当前选择和哈希见 paper/provenance/mechanism-image-replacement-20261103.json。

---

## 2026-11-03 图表摆放与阅读顺序优化

按作者“图表的摆放位置也需要对照中稿论文”的要求，检查双语主稿和补充材料的图表位置、首次引用、相应任务段落、单双栏选择和末页留白。应用 `cvpr-paper-standard` 的图表标准，并沿用既有 Tectonic／PDF 后端。保留上轮定下的题名、摘要、标题层级、正文、图注和实验数据，仅调整浮动声明位置、容器与排队方式。

本轮真实基线为标题和编号审查后的未提交工作区，HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。[修改前源文与四份 PDF](../../_archive/drivecompose/20261103-figure-table-layout/baseline/)、[本轮逐行差异](../../_archive/drivecompose/20261103-figure-table-layout/source-changes.diff)均单独保存，没有以累计 HEAD 差异代替本轮起点。

### 对照论文与采用的摆放方式

| 来源及实际复核页 | 页面组织 | 对应处理 |
|---|---|---|
| [VGGT，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf)，PDF 第 3 页，复用已核对页图 | 跨栏架构图位于方法开头页上部，下面进入方法定义 | 提前声明总览图，让英文图 2 出现在第 3 页方法开头页，而不是等到第 4 页 |
| [Fast3R，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf)，放大复核 PDF 第 6 页 | 宽表与单栏表混排，相关结果可以集中呈现，并保留相邻讨论 | 保留结果表的成组布局；按实际自然宽度选择单栏或跨栏，让短表随正文流动 |
| [HorizonForge，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf)，放大复核 PDF 第 7 页 | 定量表、定性对比与结果分析在相邻区域构成一组证据 | 让英文重建结果图与 §4.2 同页，离轨图与 §4.3 同页，避免结果图在讨论结束后滞后两页 |

这些是录用样本的布局观察，不规定每页只能放一张图或每张表必须单独占栏。图注位于图下、表注位于表上，字号和版心沿用[当前官方模板](https://github.com/cvpr-org/author-kit/blob/main/sec/2_formatting.tex)。没有修改图片显示宽度、正文字号、行距或页边距。

### 主稿图件的实际前后位置

页码是各自 PDF 内的顺序。表中的引用距离来自 PDF 超链接指向的图件标签；同页顶部图件与下方文字记为相隔 0 页。

| 图件 | 英文原页 → 新页 | 中文原页 → 新页 | 原问题与处理 |
|---|---:|---:|---|
| 图 1：首页概念图 | 1 → 1 | 1 → 1 | 沿用作者确认的标题下位置及完整内容 |
| 图 2：方法总览 | 4 → 3 | 3 → 3 | 英文首次引用在第 2 页，原来要到第 4 页才看到图；提前声明后在方法开头页上部展示 |
| 图 3：联合补全细节 | 4 → 4 | 4 → 4 | 保留在机制说明附近，图件宽度和标签可读性保持 |
| 图 4：动态重建对比 | 7 → 6 | 6 → 6 | 英文调整为与 §4.2 及表 1 同页；中文保留在第 5 页说明之后的相邻结果页 |
| 图 5：离轨渲染对比 | 8 → 7 | 6 → 6 | 英文调整为与 §4.3、表 2 同页；中文按自身正文密度摆放，避免试排时出现图先于说明一页的情况 |

双语主稿的全部主图均处于首次引用的同页或次页。英文全部图表的最大首次引用距离从 2 页降至 1 页；中文主稿最大图表距离仍为 2 页，其中表 4 延续跨页的消融讨论。主稿图件同页／相邻页是本轮阅读目标，不是官方录用条件。

### 表格与补充材料的实际调整

| 位置 | 修改前 | 修改后 | 原因及保留项 |
|---|---|---|---|
| 英文实验图 4、5 | 在具体讨论段落之后才声明，跨栏队列分别推迟到第 7、8 页 | 在实验开头提前声明，实际落在第 6、7 页 | 图件本身和正文顺序保持，改变 LaTeX 的排队时点 |
| 主稿结果表 | 多张短表只允许页顶浮动 | 允许正常的行间、页顶、页底或浮动页位置 | 表 1、2、3 分别随重建、离轨和隐藏表面讨论出现；表 4、5 随消融和资产复用讨论摆放，数据与图注保持 |
| 补充表 S12、S15 | 表格自然宽度能放入单栏，却占用跨栏浮动队列 | 改为单栏表 | 英文自然宽度约 224、222 pt，均小于约 236 pt 的单栏；没有缩小表格或字体 |
| 补充 F–K 表格 | 一些表格在长段说明后才进入浮动队列 | 在所属节开头按原编号顺序声明 | 缩短排队等待，原段落任务、顺序和科学含义保持 |
| 补充表 S23、S24 | 两个独立小表纵向分开，留有较多空白 | 同一跨栏浮动组内并排，各保留独立表注、标签和编号 | 保留原字号、列内容和原有间距；两张表的单元内容逐字一致 |
| 补充 L 放大图与参考文献 | 英文图在第 13 页，参考文献另占第 14 页；中文图在第 11 页，参考文献另占第 12 页 | 用标准跨栏页首块承载原尺寸图片，英文图与参考文献同在第 12 页，中文同在第 11 页 | 消除整块图片在浮动页居中的留白，并利用图后剩余栏位；图注和图片显示宽度保持 |

英文补充的最大首次引用距离从 3 页降至 1 页；中文补充的协议概览仍会提前引用后续成组表格，最大距离为 3 页，与本轮基线一致。两版均保留表 S1–S24 的可见顺序。中文按自身篇幅独立设置结果图位置，不强制复制英文页码。

### 源文保护、检查与交付

- 逐文档展开 `input` 后，移除浮动容器的正文与公式顺序完全一致；全部表格单元、图注、引用键、标题、图片路径及显示宽度核对一致。确认摘要和既有图片资产保持字节一致。
- 总览图的声明现在位于主入口中，以便提前进入队列；其展示位置仍围绕方法节。相应更新稿件检查器的源文件定位规则，保留图片及标签唯一性、作者确认图片哈希检查，并新增最终 PDF 中总览图与方法开头页的距离检查。
- 69 项稿件结构检查与本轮 81 项源文／图表位置检查通过；四份 PDF 已重新编译。已核对主稿全部技术页和补充全部页的缩略图，并放大复核受影响页面。没有发现缺字、未定义引用、溢出或内容重叠。
- 英文主稿 11 页、技术正文与全部正文图表止于第 8 页；中文主稿 10 页、正文止于第 7 页。英文补充 14→12 页，中文补充 12→11 页，页数减少来自摆放变化，没有删除科学内容。

[本轮验收及逐图引用距离](../paper/provenance/figure-table-layout-20261103.json)、[当前正式 PDF](../paper/build/CURRENT-OUTPUTS.md)。基线、源文差异、来源页图、最终页面图和编译辅助文件统一放在项目外 `_archive/drivecompose/20261103-figure-table-layout/`。

---

## 2026-11-03 章节标题、层级与编号专项审查

按作者“编号、标题都需要对照中稿论文的写法，仔细审查”的要求，检查双语主稿和补充材料的章节、小节、段首标题、图表与公式编号、正文交叉引用及最终页面。复用 `ml-paper-writing` 和已确认的 `cvpr-paper-standard`。论文题名、确认版摘要、上一轮叙述正文和实验数据保持；本轮修改标题、层级、引用目标及局部浮动／断行设置。

本轮真实起点是四节叙述优化后的未提交工作区，HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。[本轮基线](../../_archive/drivecompose/20261103-heading-numbering-audit/baseline/)保存修改前的双语源文和四份 PDF，[逐行差异](../../_archive/drivecompose/20261103-heading-numbering-audit/source-changes.diff)只比较本轮起点与实际结果。

### 对照依据与取舍

- [VGGT，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf)：方法按问题定义、主干和预测头组织，具体说明使用不编号段首标题。复核其 PDF 第 2–8 页标题，放大检查第 3 页。
- [Fast3R，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf)：在同一架构小节内以段首标题说明编码器、融合与解码，避免把每个短操作都独立编号。复核其 PDF 第 2–8 页标题，放大检查第 4 页。
- [HorizonForge，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf)：方法小节按主要任务组织，较多预备知识另设三级标题。复核其 PDF 第 2–8 页标题，放大检查第 3 页。本文没有增加三级编号的必要。

样本的章节数、大小写和相关工作位置各有差异，不能作为统一录用条件。本文采用两级编号，短操作用不编号的段首标题；章节和小节沿用官方模板的句首大写、专名与缩写规则。`Related work`、`Method`、`Experiments`、`Discussion`、`Conclusion` 等清楚的主标题保持。

### 实际问题与中英修改对照

| 位置 | 修改前 | 修改后 | 理由 |
|---|---|---|---|
| 方法 3.1 | Problem formulation and compositional representation／问题定义与可组合表示 | Problem formulation／问题定义 | 输入、输出与表示均属于问题定义；缩短双主题标题 |
| 方法 3.3–3.5 | 编码、联合补全和解码分别编号，其中编码仅一段 | 统一为 3.3 Joint latent completion／联合潜空间补全；内部以潜码编码、跨组件记忆、流训练与采样、分类型解码作段首标题 | 保持原有技术顺序，围绕中心机制组织层级；没有删除或迁移正文 |
| 方法原 3.6 | Scene composition／场景组合，紧接 State-driven rendering／状态驱动渲染 | 3.4 State-driven scene composition／状态驱动场景组合；删除重复段首标题 | 上下两层标题原来指向同一段内容，合并后直接说明任务 |
| 方法原 3.7 | Training procedure／训练流程 | 标题保持，自动顺延为 3.5 | 训练承担独立小节任务；同步更新所有自动引用 |
| 实验原 4.3 | Off-trajectory rendering and missing surfaces／轨迹外渲染与缺失表面 | 4.3 Off-trajectory rendering／轨迹外渲染；4.4 Hidden-surface completion／隐藏表面补全 | Waymo 分布评价与合成配对几何评价分别组织，清楚呈现两套数据及指标 |
| 相关工作引用 | 机制适配比较引用原 4.3 混合小节 | 改为引用独立的 4.4 隐藏表面补全 | 将读者直接引向场景潜码／对象耦合对照及其条件 |
| 实验原 4.4 | Ablations and component context／消融与组件上下文 | 4.5 Ablation studies／消融实验 | 标题覆盖模块、输入数量、可见率及自由空间规则四类分析 |
| 消融段首 | Where CCM helps／CCM 在哪里有效 | Visibility-stratified analysis／可见率分组分析 | 直接点明按可见率分组的评价方式 |
| 消融段首 | Protocol／协议；Completion and context／补全与上下文；Free-space rule／自由空间规则 | Evaluation protocol／评价协议；Completion components／补全组件；Free-space labeling rules／自由空间标记规则 | 明确标题所指对象，规则用复数对应 C／F |
| 实验原 4.5 | State-driven reuse and observation preservation／状态复用与观测保持 | 4.6 State-driven asset reuse／状态驱动资产复用 | 以资产复用统领编辑、观测检查和摊销代价，保留内部结果及限定 |
| 相关工作段首 | Compositional scenes and controllable assets／可组合场景与可控资产 | Compositional scene representations／可组合场景表示 | 以表示路线归组，该段仍保留控制与绑定关系 |
| 相关工作段首 | Generative driving scenes and videos／驾驶场景与视频生成 | Driving-scene generation／驾驶场景生成 | 使用任务名称，覆盖该段图像、视频及混合生成方法 |
| 附录 F | Conditional reconstruction and comparison protocol／条件重建与比较协议 | Reconstruction protocols and baselines／重建协议与基线 | 概括该节的比较协议、训练资源、状态适配与深度评价 |
| 附录 G | Ablations, seed statistics, and evaluation denominators／消融、种子统计与评价分母 | Ablation protocols and seed statistics／消融协议与种子统计 | 精简并列项；分母定义仍完整保留 |
| 附录 H | Off-trajectory, hidden-region, and context diagnostics／离轨、隐藏区域与上下文诊断 | Off-trajectory rendering and completion analysis／轨迹外渲染与补全分析 | 用任务与分析对象概括该节内容 |
| 附录 I、J | State-driven reuse of completed assets／完成资产的状态驱动复用；Parameter and observation-rendering preservation／参数与观测渲染保持 | State-driven asset reuse／状态驱动资产复用；Observation consistency／观测一致性 | 与正文任务名称对应；参数保持与渲染误差仍分别报告 |

### 编号和版面修正

- 主文原来先引用离轨结果表 3，再引用隐藏区域表 2。将离轨表及对应图的环境移至该任务段落后，隐藏区域表仍随补全段落；现在离轨表为表 2，隐藏区域表为表 3，全文首次引用及可见表序均为 1–5。表格数据与图表标题保持。
- 补充原来固定表格跳过未排出的浮动表格，导致 S17／S18 早于 S15／S16、S23／S24 早于 S22。六张原固定表格改用普通浮动，在附录 L 放大图之前排完剩余表格；最终两版 S1–S24 均按可见顺序连续排列。没有缩字号或修改表格间距。
- 方法 3.3 的编码、补全、解码标签均指向同一小节，内部内容仍可通过原标签定位；场景组合 3.6→3.4、训练 3.7→3.5，消融 4.4→4.5、复用 4.5→4.6。正文引用使用标签自动更新，机制比较改用新标签 `sec:hidden-completion`。
- 保留主文连续公式编号 (1)–(11)、图 1–5、附录 A–L 和补充 S 前缀；保留无需修改的图表标题。检查段首标题与二级标题的任务是否重复、是否出现跨页孤立标题，以及标题和正文是否对应。
- 英文阶段范围 “Stages 3–4” 曾在页边界断出孤立的 “4.”，已对该范围作不换行处理，数字与科学含义保持。

### 最终主文层级

```text
1. Introduction
2. Related work
3. Method
   3.1. Problem formulation
   3.2. Visual recovery and canonical aggregation
   3.3. Joint latent completion
   3.4. State-driven scene composition
   3.5. Training procedure
4. Experiments
   4.1. Experimental setup
   4.2. Dynamic scene reconstruction
   4.3. Off-trajectory rendering
   4.4. Hidden-surface completion
   4.5. Ablation studies
   4.6. State-driven asset reuse
5. Discussion
6. Conclusion
```

### 核验与文件

本轮八份既有论文源文之外的源文件保持字节一致，图表内容与图注、行间公式、实验数值和引用键保持。英文仍为 11 页、技术正文止于第 8 页；中文 10 页、正文止于第 7 页。英文补充 14 页，中文补充 12 页；英文补充相对本轮起点增加 1 页，用于恢复表格顺序，正文篇幅不变。69 项稿件结构检查与本轮 141 项编号／源文／PDF 检查全部通过；最终技术页缩略图、全部补充页缩略图及受影响重点页已复核。完整结果见[验收记录](../paper/provenance/heading-numbering-audit-20261103.json)，正式文件入口见[当前 PDF](../paper/build/CURRENT-OUTPUTS.md)。

---

## 2026-11-03 引言、相关工作、方法与实验的双语叙述优化

按作者“继续以相同方式优化引言和相关工作和方法还有实验，对照中稿论文怎么写”的要求，沿用已确认摘要的主线，修改四节的中英文叙述。由 `ml-paper-writing` 统筹并应用已确认的 CVPR 标准；英文用 humanizer 检查，中文仅对本轮改动段落按 lieflat 白名单终校。科学正文改动限于八份章节源文件，已确认摘要保持字节一致。

本轮起点为已有未提交修改的工作区，Git HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。[真实修改前基线](../../_archive/drivecompose/20261103-main-sections-polish/baseline/)保存本轮八份源文及双语 PDF；[完整逐行差异](../../_archive/drivecompose/20261103-main-sections-polish/source-changes.diff)只包含本轮改动，不能用累计 HEAD 差异代替。诊断与结果分配见[本轮工作记录](../../_archive/drivecompose/20261103-main-sections-polish/revision-plan.json)。

### 对照论文与采用的写法

| 录用论文及原文范围 | 观察到的组织方式 | 本轮对应处理 |
|---|---|---|
| [VGGT，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf)，PDF 2–5、7 页 | 先定义输入、输出与坐标，再说明信息交互设计；消融对应具体架构选择 | 保留原方法顺序，解释规范／世界坐标、统一潜码维度及记忆读写的用途；实验区分整体效果与机制证据 |
| [Fast3R，CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Fast3R_Towards_3D_Reconstruction_of_1000_Images_in_One_Forward_CVPR_2025_paper.pdf)，PDF 2–3、7 页 | 从具体处理瓶颈引出联合建模，并检验更多上下文带来的变化 | 合并引言两段重复流程，将跨组件信息与未知表面补全连接；解释输入数量与可见率下的收益差异 |
| [HorizonForge，CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_HorizonForge_Driving_Scene_Editing_with_Any_Trajectories_and_Any_Vehicles_CVPR_2026_paper.pdf)，PDF 2–3、6–7 页 | 按重建、生成及其结合组织相关方法；编辑目标对应表示与评价 | 沿用四条既有技术路线，前置其方法关系；把固定资产编辑与新显露表面评价联系起来 |

采用上述论证方式，不复制论文措辞，不把其宣传性表述、任务条件或排版压缩方式移入本文。

### 代表性前后对照

| 位置 | 本轮原文或原问题 | 修改后 | 原因 |
|---|---|---|---|
| 引言结果预览（英文） | Under shared camera and actor states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering. | Experiments on Waymo show higher reconstruction accuracy and better off-trajectory rendering quality than the feed-forward baselines. | 在引言集中陈述 Waymo 的比较结论；编辑百分比仍保留在 §4.5 与附录 I |
| 引言结果预览（中文） | 在 Waymo 的统一相机与参与者状态条件下，DriveCompose 改善了重建与轨迹外渲染。隐藏表面测试中，异构联合补全优于任务适配的场景级潜码生成和跨对象耦合对照。真实编辑跨状态复用固定资产，结构完整性成功率为 92.78\%，四项质量联合通过率为 82.78\%（第~\ref{sec:experiments} 节）。 | Waymo 实验表明，相比前馈重建基线，DriveCompose 获得了更高的重建精度和更好的轨迹外渲染质量。合成配对测试将联合补全与场景级生成、跨对象耦合进行比较，真实参与者编辑则验证同一组补全资产的复用（第~\ref{sec:experiments} 节）。 | 与英文的比较对象、任务和主张强度同步 |
| 相关工作近邻对照（英文） | We compare their task-adapted mechanisms through a shared reconstruction interface (Sec.~\ref{sec:spatial_evaluation}). | Our matched comparisons adapt scene-level generation and cross-object coupling to the same reconstruction interface (Sec.~\ref{sec:spatial_evaluation}). | 明确比较场景级生成与跨对象耦合两个适配机制，消除 their 可能包含 GenAssets 的歧义 |
| 相关工作近邻对照（中文） | 我们在共享重建接口下比较相应任务适配机制（第~\ref{sec:spatial_evaluation} 节）。 | 匹配比较将场景级生成与跨对象耦合适配到相同重建接口（第~\ref{sec:spatial_evaluation} 节）。 | 以机制关系组织近邻比较，不把适配成绩归于原生方法 |
| 方法双坐标作用（英文） | The fixed layout stores canonical coordinates for component identity and first-input world coordinates $\mathbf q_i^w$ (including human skinning) for relating components to their surroundings. | The layout retains canonical coordinates to identify component surfaces and first-input world coordinates $\mathbf q_i^w$, including human skinning, to locate them relative to the background and other actors. | 说明规范坐标标识组件表面、参考世界坐标联系背景与其他参与者；计算及变量保持 |
| 方法双坐标作用（中文） | 固定布局以规范坐标标识组件内容，以第一帧世界坐标 $\mathbf q_i^w$（包括人体蒙皮）联系组件与周围场景。 | 布局保留规范坐标以标识组件表面，并以首个输入时刻的世界坐标 $\mathbf q_i^w$（包括人体蒙皮）确定其相对背景与其他参与者的位置。 | 补足两种坐标描述的用途，保留人体蒙皮条件 |
| 方法 CCM 读写（英文） | 原文给出 memory-exchange 公式和 query/key/value 次序，随后直接进入前馈更新。 | Memory first reads all local groups, then supplies the updated scene context to each group's tokens. | 把公式的两步注意力与“汇集局部特征、回写场景上下文”对应，不修改公式 |
| 方法 CCM 读写（中文） | 原文给出注意力参数次序，随后直接进入残差前馈更新。 | 记忆先读取全部局部组，再将更新后的场景上下文传回各组的 token。$\mathbf U$ 后接残差前馈更新。流时间调制局部归一化，记忆由可学习 token 与日志摘要初始化。 | 与英文相同的机制解释，不增加新的网络组件或能力 |
| Waymo 离轨结果（英文） | Figure~\ref{fig:waymo-left-shift} compares shifted renders against an original-trajectory reference. | DriveCompose achieves the lowest FID and FVD at all three Waymo offsets, improving both image and video distribution quality (Table~\ref{tab:spatial_current}). | 原文此处仅交代图示；新增对现有三个偏移下 FID/FVD 的解读，主表数值不变 |
| Waymo 离轨结果（中文） | 图~\ref{fig:waymo-left-shift} 展示偏移渲染及原轨迹参考。 | DriveCompose 在 Waymo 的三种偏移下均取得最低 FID 和 FVD，改善了图像与视频的分布质量（表~\ref{tab:spatial_current}）。图~\ref{fig:waymo-left-shift} 展示偏移渲染及原轨迹参考。 | 将实测优势落到 Waymo，随后以独立段落进入合成隐藏区域评价 |
| 输入稀疏度消融（英文） | At $T=2,4,8$, PSNR gains are 1.104, 0.738, and 0.627 dB (Appendix G). | PSNR gains are 1.104, 0.738, and 0.627 dB at $T=2,4,8$, with the largest benefit at the sparsest input setting (Appendix G). | 保留全部增益，说明最稀疏输入下上下文收益最大；可见率分组仍按原阈值定义 |
| 输入稀疏度消融（中文） | $T=2,4,8$ 时的 PSNR 增益为 1.104、0.738 和 0.627 dB（附录 G）。 | $T=2,4,8$ 时的 PSNR 增益为 1.104、0.738 和 0.627 dB，输入最稀疏时收益最大（附录 G）。 | 与英文一致，从数值复述推进到已有比较所支持的发现 |

### 内容保留与删减位置

- 引言合并原第 4、5 段重复概述，不改变研究问题、输入、表示或生成机制。第三项贡献聚焦共享场景上下文的机制认识与真实资产复用；自由空间规则的原有分析仍在 §4.4 和附录 D。
- 引言不再重复 92.78%／82.78% 编辑成绩；§4.5 与附录 I 中的 334/360 结构判据、298/360 四项联合质量、场景数和种子条件全部保留。本轮没有把材料重新迁入补充。
- 相关工作保留四个主题和全部原引用，明确场景级生成与跨对象耦合是适配机制对照。保留本文与生成视图／视频精修方法在固定三维内容复用上的具体关系。
- 方法只修改解释性文字；输入标定、给定状态、目标数据用途、查询布局、三种掩码、绑定、采样、目标有效性、四阶段训练及全部数值保持。
- 实验保留全部表格、图件、协议、成绩、种子 SD、覆盖阈值和计时条件；保留输入视角 PSNR 下降 0.029 dB、深度 MAE 增加 2 mm 等限定结果，区分参数保持与渲染变化。新增文字解释既有比较，没有新训练或新增测量。
- 英文改动段落完成一轮 humanizer 复读；中文按 lieflat 白名单检查，技术清单、公式引导和领域术语按科研语体保留，不机械改动句长、条目数或未命中表达。

### 核验与交付

双语主稿已重新编译。英文共 11 页，技术正文、讨论、结论及全部正文图表止于第 8 页，参考文献从第 9 页开始；中文共 10 页，正文止于第 7 页。69 项稿件结构检查与本轮 70 项源文／PDF 检查全部通过：双语各 9 个方法行间公式环境、全部图表环境、引用键和方法／实验数值保持不变，八份章节以外的既有论文源文件及已确认摘要保持字节一致。

已检查最终两版全部技术页缩略图，并放大复核英文第 4、5、8 页和中文第 2、3、4、5、7 页；首轮另已放大复核英文第 2、3、5–8 页。首轮发现英文第 5 页页首孤立的 “memory:”，将前句收紧为 “Cross-component memory (CCM) then exchanges context across groups:”，同步中文后再次编译，最终第 4／5 页断句已检查。日志保留浮动页提示，未发现未定义引用、缺字、溢出或页面内容重叠；字体、版心和间距未调整。

下表用于比较叙述文字量：排除图表、公式、标题、引文键和 LaTeX 控制后，英文按含字母或数字的空格分词计数，中文仅计汉字；不作为会议官方词数。

| 章节 | 英文修改前 → 后 | 中文汉字修改前 → 后 |
|---|---:|---:|
| 引言 | 441 → 378 | 842 → 718 |
| 相关工作 | 285 → 293 | 480 → 476 |
| 方法 | 1059 → 1087 | 1833 → 1901 |
| 实验 | 819 → 907 | 1281 → 1418 |

结构检查、源文件保护、逐节文字量和双语 PDF 核验见[本轮验收记录](../paper/provenance/main-sections-polish-20261103.json)。正式文件及页数见[当前 PDF](../paper/build/CURRENT-OUTPUTS.md)。基线、检索与阅读材料、差异、编译辅助文件及页图均保存在项目外 `_archive/drivecompose/20261103-main-sections-polish/`。

---

## 2026-11-03 采用作者确认的中英文摘要

按作者“就用这一版，更新论文中英文摘要”的指令，逐字采用本轮对话最后确认的双语文本，不再改写。英文摘要以视点和姿态变化暴露未知表面切入，串联共享场景上下文、联合补全与绑定资产复用，效果陈述落在 Waymo 的重建和轨迹外渲染，不列具体提升数值。

本轮开始时工作区已有未提交修改。Git HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，本轮真实基线是[修改前摘要、记录和 PDF](../../_archive/drivecompose/20261103-abstract-adoption/baseline/)，不能用 HEAD 差异代替本轮前后对照。[本轮摘要逐行差异](../../_archive/drivecompose/20261103-abstract-adoption/abstracts.diff)只包含这次替换。

### 代表性前后对照与理由

| 位置 | 原文 | 修改后 | 理由 |
|---|---|---|---|
| 英文开头 | “Reconstructing complete and controllable 3D scenes from partial observations is essential …” | “Moving the camera or changing actor poses exposes surfaces …” | 从具体可见性问题切入，直接引出补全与运动控制需求 |
| 中文开头 | “从局部观测中重建完整、可控的三维场景，是……重要基础” | “相机视点与参与者姿态的变化会显露……从未观测到的表面” | 与英文问题表述同步，删除泛化的重要性开场 |
| 英文效果陈述 | “Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering.” | “Experiments on Waymo show higher reconstruction accuracy and better off-trajectory rendering quality than feed-forward reconstruction baselines.” | 明确 Waymo、比较对象和两项效果，不报告具体幅度 |
| 中文效果陈述 | “在 Waymo 的统一状态条件下，DriveCompose 改善了重建与轨迹外渲染。” | “Waymo 实验表明，相比前馈重建基线，DriveCompose 获得了更高的重建精度和更好的轨迹外渲染质量。” | 与英文比较范围及主张强度一致 |
| 摘要结果细节 | 0.67 dB、2.6 个百分点、360 次编辑、92.78%／82.78% 及检查项目 | 用 Waymo 上的比较结论及参与者编辑复用结果收束 | 按作者要求精简摘要；上述数值和评价条件原已存在于实验及补充材料，本轮保留原文，没有重新迁移或删除正文证据 |
| 方法细节 | 摘要中的潜码硬恢复与自由射线约束说明 | 摘要集中解释跨组件上下文、几何与外观补全、刚体／骨架绑定和状态复用 | 聚焦主要设计直觉；方法节与相应证据保留原文 |

### 英文摘要全文对照

修改前：

Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for compositional generative reconstruction from driving image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for actors, then encoded into component-specific latents. A conditional flow model uses cross-component memory to exchange scene context and jointly complete missing codes. Type-specific decoders convert the completed latents into Gaussian components with rigid and skeletal bindings, allowing the same assets to be composed and rendered under different camera and actor states. Hard latent restoration preserves observed Gaussian parameters, and free-ray constraints control the rendering effects of added content. Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering. In paired hidden-region tests, cross-component completion exceeds the strongest task-adapted mechanism control by 0.67 dB PSNR and 2.6 percentage points of surface coverage. Across 360 actor edits in 20 real scenes and nine seed combinations, structural integrity succeeds in 92.78\% of edits; 82.78\% jointly pass structure, newly visible texture, appearance identity, and local geometry checks.

修改后（作者确认文本）：

Moving the camera or changing actor poses exposes surfaces that were never observed in the input driving images. Reconstructing scenes for simulation and editing therefore requires completing these surfaces while retaining control over actor motion. We present DriveCompose, a framework for compositional generative reconstruction from calibrated driving image sequences. Visual evidence is aggregated in world coordinates for the background and canonical frames for vehicles and humans. A conditional flow model uses cross-component memory to share scene context and jointly complete missing geometry and appearance in the component latents. The completed latents are decoded into Gaussian components with rigid and skeletal bindings, allowing generated surfaces to move with their corresponding actors. The same background and actor assets can then be assembled and rendered under new camera viewpoints and actor states. Experiments on Waymo show higher reconstruction accuracy and better off-trajectory rendering quality than feed-forward reconstruction baselines. Actor editing experiments further demonstrate that completed vehicles and humans can be reused across motion and pose changes.

### 中文摘要全文对照

修改前：

从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景。视觉特征在背景的世界坐标系和参与者各自的规范坐标系中聚合，再编码为对应组件的潜表示。条件流模型通过跨组件记忆交换场景上下文，联合补全缺失潜码。分类型解码器将补全潜码转换为具有刚体和骨架绑定的高斯组件，使同一组资产能够在不同相机与参与者状态下组合和渲染场景。潜码硬恢复保持已见高斯参数，自由射线约束控制新增内容对渲染的影响。在 Waymo 的统一状态条件下，DriveCompose 改善了重建与轨迹外渲染。配对隐藏区域测试中，跨组件补全相对最强任务适配机制对照将 PSNR 提高 0.67 dB、表面覆盖率提高 2.6 个百分点。20 个真实场景、九组种子的 360 次演员编辑中，结构完整性成功率为 92.78\%；结构、新增表面纹理、外观身份与局部几何四项联合通过率为 82.78\%。

修改后（作者确认文本）：

相机视点与参与者姿态的变化会显露输入驾驶图像中从未观测到的表面。面向仿真与编辑的场景重建需要补全这些表面，同时保留对参与者运动的控制。我们提出 DriveCompose，从有标定的驾驶图像序列中生成式重建可组合场景。视觉证据分别在背景的世界坐标系和车辆、人体的规范坐标系中聚合。条件流模型通过跨组件记忆共享场景上下文，在组件潜表示中联合补全缺失的几何与外观。补全后的潜表示被解码为具有刚体和骨架绑定的高斯组件，使生成表面随对应参与者运动。同一组背景与参与者资产随后可在新的相机视点和参与者状态下装配与渲染。Waymo 实验表明，相比前馈重建基线，DriveCompose 获得了更高的重建精度和更好的轨迹外渲染质量。参与者编辑实验进一步验证了补全车辆与人体在运动和姿态变化下的复用能力。

### 本轮范围与核验

科学正文仅替换 `paper/sec/0_abstract.tex` 与 `paper/zh/0_abstract_zh.tex`。标题、其他章节、实验数值、图表、公式、书目、模板及补充材料保持本轮基线。重新编译两份主稿，检查结果见[采用与核验记录](../paper/provenance/abstract-adoption-20261103.json)，正式文件见[当前 PDF](../paper/build/CURRENT-OUTPUTS.md)。

验收结果：两份源文与作者确认文本逐字一致；英文摘要 163 词。中英文主稿均编译成功，分别共 11／10 页，技术正文分别止于第 8／7 页；两份摘要完整出现在首页。检查覆盖全部技术正文缩略图，以及双语首页和结论页的高清页图，无缺字、溢出、裁切或重叠。编译日志仅有图表专页提示，无未定义引用或缺字警告。新生成的日志、辅助文件、页图和本轮基线归入项目外 `../_archive/drivecompose/20261103-abstract-adoption/`，正式路径仅保留当前 PDF 与构建记录。

---

## 2026-11-02 统一证据修订与语言终校

本轮基线为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，开始时工作区干净。[实际源文件和 PDF 基线](../../_archive/drivecompose/20261102-review-evidence-revision/baseline/)与[完整逐行差异](../../_archive/drivecompose/20261102-review-evidence-revision/source-changes.diff)仅记录本轮改动。采用最新统一作者文本，前一份 600 场景、512×512 与另一套网格／绑定设置未用于稿件。

### 具体修改与理由

| 位置 | 原文或原问题 | 修改后 | 理由 |
|---|---|---|---|
| 摘要与引言 | “Real-scene edits achieve 92.78% success”；“真实场景编辑……92.78% 成功率” | “structural integrity succeeds in 92.78%”；“结构完整性成功率为 92.78%”，并加入四项联合质量 82.78% | 将结构判据和纹理／身份／几何质量分别归因，明确 360 次、二十个场景、九组种子 |
| 相关工作、§4.3 与补充 H | 仅有 w/o GCM、w/o CCM 和 Ours 的隐藏表面结果 | 增加 Scene latent／场景潜码与 Object coupling／对象耦合的任务适配对照；明确共享模块、输入、监督和采样 | 将异构联合补全的增量直接定位到可比机制，不归为原生 CompleteSplat／JRM 成绩 |
| 主稿新表 2、补充表 S15 | 原隐藏结果 23.18 dB 主要与内部变体比较 | 对最强新增对照提高 0.67 dB PSNR、2.6 个百分点覆盖率、3.6 个百分点 F-score；LPIPS 减少 0.020 | 主张与相同 100 场景、C 规则和九组种子的证据一致 |
| §3.2／§4.4、补充 D 表 S6–S7 | 足迹仅报告掩码误标 | 增加隐藏区域下游指标及薄结构、边界、人体切片，报告 F 的质量与代价 | 将 1,355 个净误标减少与 1.2 个百分点表面覆盖增益分开，不推断错误集合对应关系 |
| 主表协议 | 原数据规模与中心射线结果 | 保留 740/58/202、10,000/1,000/1,000 等划分及 240×160；C 为主协议，F 单列 | 不把原表数值移用于另一套规则或数据配置 |
| §4.5、补充 I 表 S19–S21 | 总成功率与原种子区间 | 保留 334/360 结构结果，新增 298/360 联合质量；62 次联合失败分为 26 次结构失败与另外 36 次质量失败 | 原 0.48 个百分点 SD 和 85.28%–99.17% 区间仅对应结构；联合通过按逐例交集 |
| 观测保持 | MAE 0.014 与资产编辑段并列 | 移到主稿观测保持段；补充明确其为已见人体纹理指标 | 避免用已见区域误差代表新增表面纹理质量 |
| 补充 D、表 S3 | 仅给基础网格维数 | 补充背景米制范围、5×5×3 m 单元、2,048／512 锚点上限、0.20 m 去重、4 m 注意力分组和 0.10 m 人体邻域 | 区分网格、锚点、注意力分组及人体体型尺度；保留查询先绑定、子高斯继承 |
| 引言与实验重复文字 | 引言重复逐模块流程；正文重复附录 F/G/H 已有完整数值 | 局部删减重复说明；完整插值／外推、输入敏感性、读取干预和失败统计保留在原附录 | 为新增证据腾出版面，不改变原有数值及协议 |
| 原资产编辑表 | 车辆与人体分成六行 | 同一变体一行，车辆与人体指标并列，全部十八个结果保留 | 紧凑原生表格，维持可读字号，正文止于第 8 页 |
| 补充材料页内留白 | 固定表格之间弹性空白被拉大 | 使用 raggedbottom 保留自然段表间距 | 不修改字体、版心或基线行距 |
| 英文声明分页 | 新内容使声明段在第 8／9 页之间拆开 | 使用 Needspace 将声明标题及段落保持在同页 | 技术正文仍在第 8 页结束，声明仍位于参考文献之前 |
| 稿件检查器 | 图 2 仍比较早期 PNG 哈希；把后续资产表的标准覆盖率误判为旧自定义消融指标 | 图 2 读取最新已有作者批准记录；旧指标禁用检查明确限制到对应消融范围 | 纠正过期校验依据，仍保留完整图像哈希与旧指标检测 |

### 保留项与展示决定

标题、既有图 1–5、主书目、原主重建／离轨／组件消融数值及公式保持；图像文件未改。用户明确要求本轮不放新增结果图，新增结论以文字和表格呈现。正文没有声称展示尚未提供的编辑渲染或局部放大图。

### 摘要全文前后对照

**英文摘要原文。**

> Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for compositional generative reconstruction from driving image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for actors, then encoded into component-specific latents. A conditional flow model uses cross-component memory to exchange scene context and jointly complete missing codes. Type-specific decoders convert the completed latents into Gaussian components with rigid and skeletal bindings, allowing the same assets to be composed and rendered under different camera and actor states. Hard latent restoration preserves observed Gaussian parameters, and free-ray constraints control the rendering effects of added content. Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering over state-adapted baselines; cross-component memory adds 0.627 dB full-image PSNR. Real-scene edits achieve 92.78\% success across nine training/generation-seed combinations, demonstrating reuse of fixed completed assets.

**英文摘要修改后。**

> Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for compositional generative reconstruction from driving image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for actors, then encoded into component-specific latents. A conditional flow model uses cross-component memory to exchange scene context and jointly complete missing codes. Type-specific decoders convert the completed latents into Gaussian components with rigid and skeletal bindings, allowing the same assets to be composed and rendered under different camera and actor states. Hard latent restoration preserves observed Gaussian parameters, and free-ray constraints control the rendering effects of added content. Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering. In paired hidden-region tests, cross-component completion exceeds the strongest task-adapted mechanism control by 0.67 dB PSNR and 2.6 percentage points of surface coverage. Across 360 actor edits in 20 real scenes and nine seed combinations, structural integrity succeeds in 92.78\% of edits; 82.78\% jointly pass structure, newly visible texture, appearance identity, and local geometry checks.

**中文摘要原文。**

> 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景。视觉特征在背景的世界坐标系和参与者各自的规范坐标系中聚合，再编码为对应组件的潜表示。条件流模型通过跨组件记忆交换场景上下文，联合补全缺失潜码。分类型解码器将补全潜码转换为具有刚体和骨架绑定的高斯组件，使同一组资产能够在不同相机与参与者状态下组合和渲染场景。潜码硬恢复保持已见高斯参数，自由射线约束控制新增内容对渲染的影响。在 Waymo 的统一状态条件下，DriveCompose 的重建与轨迹外渲染优于状态适配后的基线，跨组件记忆使全图 PSNR 提高 0.627 dB。真实场景编辑在九组训练／生成种子下取得 92.78\% 成功率，固定完成资产可跨状态复用。

**中文摘要修改后。**

> 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景。视觉特征在背景的世界坐标系和参与者各自的规范坐标系中聚合，再编码为对应组件的潜表示。条件流模型通过跨组件记忆交换场景上下文，联合补全缺失潜码。分类型解码器将补全潜码转换为具有刚体和骨架绑定的高斯组件，使同一组资产能够在不同相机与参与者状态下组合和渲染场景。潜码硬恢复保持已见高斯参数，自由射线约束控制新增内容对渲染的影响。在 Waymo 的统一状态条件下，DriveCompose 改善了重建与轨迹外渲染。配对隐藏区域测试中，跨组件补全相对最强任务适配机制对照将 PSNR 提高 0.67 dB、表面覆盖率提高 2.6 个百分点。20 个真实场景、九组种子的 360 次演员编辑中，结构完整性成功率为 92.78\%；结构、新增表面纹理、外观身份与局部几何四项联合通过率为 82.78\%。

### 科学与语言复查

英文新改与受影响段落按 humanizer 检查，中文只选 lieflat-less-ai-tone 检查明确触发项。删除重复段尾判断和修订过程口吻，保留参数、协议、公式、引用与主张强度；把 newly visible 的条件统一为输入不可见，涵盖遮挡和视野外表面。论文不出现 R1-M1 等审稿编号或“为回应质疑”的段落。

原件缺口只记录在 [EVIDENCE](../paper/EVIDENCE.md) 和 [来源记录](../paper/provenance/review-evidence-revision-20261102.json)。当前没有编造两种新增机制对照的参数量、成本、运行 ID 或数据资源全集。本轮未重新训练或评测。

### 交付与验收

- 英文主稿 11 页，技术正文、结论和全部正文表图止于第 8 页；中文主稿 10 页，正文止于第 7 页。英文摘要 183 词。
- 双语独立补充材料页数以[最终验收](../paper/provenance/review-evidence-revision-20261102-verification.json)为准。
- 稿件结构检查 69 项通过；数值转录、原表保留、分母算术、双语公式、正式样式、实际编译和页数的定向检查 74 项通过。
- 四份正式 PDF 均为本轮编译输出；最终日志无溢出、缺字、未定义引用或重复标签。全稿页图与新增／受影响表格已目视检查。基线、构建脚本、预览和差异保存在项目外归档。

---
## 2026-11-02：先固定空间设定，再单独生成 P2 素材

用户要求 P2/P3 分开生成，先预设观测方位与物体相对位置，并结合整张 teaser 只生成 P2。本轮从已有未提交工作区开始，基线提交仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。本改动记录的真实基线保存在 `paper/build/teaser-p2-standalone/before/paper-revision-changes.md`，SHA256 为 `1ca5f973a4cdc7cb3265700a62614baabb986425f7ed798af8da48e36602b522`。此前合并 P2/P3 的试稿保留为历史候选，本轮不据其重新安排空间。

具体问题：合并生成的双图没有固定的坐标场景，容易把相机变化画成物体移动；图内标题、箭头和图例也无法直接作为现有 P2 框内的独立素材使用。

| 位置 | 既有试稿 | 本轮修改 | 原因及改善 |
| --- | --- | --- | --- |
| 素材单元 / Asset unit | 单张 PNG 包含 P2/P3、标题、相机箭头和图例 | 独立无字 P2 场景，约 2.35:1，匹配既有 P2 框比例 | 图内只保留场景表达，标题和流程元素由整张 teaser 的原生 PPT 对象承担。 |
| 空间依据 / Spatial specification | 主要由提示词描述相对位置并逐轮修正 | 先保存世界坐标、观察相机、物体锚点和未知面归属；由同一坐标生成几何底图，再交给 imagegen 风格化 | 使后续各槽位可以共享同一场景，而不独立编造物体位置 / Reuse a fixed world instead of restaging each panel. |
| 观察与采集 / Viewing and acquisition | 输入相机符号和场景观察角度混在插图中 | 采集相机固定在车前 +X、近侧 -Y；P2 使用外部后侧相机 (-8,-14,7)，图内不再重复相机符号 | 解释为何 P2 可从外部看见未被输入观测到的车尾缺口。 |
| 未知区域 / Unknown surfaces | 车辆后部一个局部 U，空间位置随重绘调整 | 整个车尾面 Uv、被车辆遮挡的车后地面 Ug 固定在坐标中；远侧 +Y 面在 P2 中隐藏 | 未知面在相机变化前已经确定；后续车辆与背景的联合补全可使用相同区域。 |
| 后续对应 / Future correspondence | 通过图像重绘近似保持两图关系 | P3 只改外部相机；P4 沿用 P2 视角并补面；P5 裁同一资产；P6a 沿用 P3 相机看补全场景 | 固定不同面板之间的共有条件 / Fix the common scene across the teaser. 本轮只生成 P2。 |

空间设定属于受控概念场景，不来自 Waymo 标定。几何底图由原生 SVG 投影构建，进行了 54 条地面采样视线的遮挡检查及车尾/远侧面的朝向检查；它只核验设计条件，不是论文实验，也不证明生成位图满足精确标定投影。对生成结果目检了车辆方向、行人和背景位置、两处未知面以及无字单图格式。

交付：[独立 P2 PNG](figures/teaser/p2-standalone.png)，1921×819；[空间设定](figures/teaser/p2-spatial-plan.md)、[数值场景约定](figures/teaser/p2-scene-contract.json)、[生成提示词](figures/teaser/p2-standalone-prompt.txt)、[来源记录](figures/teaser/p2-standalone-generation-record.json)。使用内置 image_gen，根据几何底图和用户风格参考生成一次。现有 PPT SHA256 仍为 `60ecadfa10823080aa648e29f8609db9df5995534db743f635f7cdf8a51917fe`；主稿、PDF、实验数值未改，没有编译论文。

## 2026-11-02：试生成 P2/P3 的抽象几何概念素材

用户提供学术图示风格参考，明确要求使用 imagegen 先试做 P2/P3，采用抽象信息表达，避免模仿真实纹理。本轮基线提交为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`；从已有未提交工作区开始。改动记录的真实基线已保存于 `paper/build/teaser-p2-p3-concept/before/paper-revision-changes.md`，SHA256 为 `b13b3eba00e0852c9f9a56abb92758fcfd96c12fd379d71ea556a01748ea710a`。仅新增试稿、提示词及生成记录，不替换现有 PPT 或论文图件。

具体问题：P2/P3 当前仍为灰色占位，尚未形成能在缩略尺寸下读懂的“汇总观测后仍有未知表面 → 改变视角暴露同一缺口”的图形。用用户参考图的简化几何体、平面配色和细轮廓来表达这组关系。

| 位置 | 当前占位内容 | 候选素材表达 | 原因及改善 |
| --- | --- | --- | --- |
| P2 / Aggregated observations | `All input frames aggregated / Unobserved surfaces remain` / 汇总全部输入帧后仍有未观测表面 | 灰蓝色车辆表面、简化行人和背景，单侧日志相机符号，以及远端未知区域 U 的虚线提示 | 用观察方向和缺失位置表达覆盖不足，避免真实街景纹理分散注意。 |
| P3 / Unseen surfaces exposed | `New camera view s1 / Unobserved surfaces exposed` / 新相机视角下暴露未观测表面 | 相同概念场景换视角；未知表面 U 以白色、虚线与稀疏斜线突出 | 保持问题路径的含义；两图均未画入完成后的表面。 |
| 风格 / Visual style | 未填入场景素材 | 少量几何体、灰蓝车辆、淡紫人物、浅青路面、浅灰背景，白色底 | 保留驾驶场景语义，以形状和颜色承担信息。 |

使用内置 image_gen 生成初稿后进行一次对应关系修正：初稿主要改变车辆朝向，背景与行人位置几乎未变；修正稿调整背景、行人和斑马线随视角的投影关系，并把日志相机放在同一观测侧。该图为生成式概念试稿，U 不代表从 Waymo 图像测出的真实可见性掩码，未进行标定三维投影核验。尚未生成 P4/P5/P6。

候选：[P2/P3 PNG](figures/teaser/p2-p3-abstract.png)，2094×751；[初始提示词](figures/teaser/p2-p3-abstract-prompt.txt)、[对应关系修正提示词](figures/teaser/p2-p3-abstract-refinement-prompt.txt)；[生成与来源记录](figures/teaser/p2-p3-abstract-generation-record.json)。用户参考图已按原字节保存于素材参考目录。现有 PPT SHA256 仍为 `60ecadfa10823080aa648e29f8609db9df5995534db743f635f7cdf8a51917fe`；原 PDF、LaTeX、正文、实验数值保持原样，没有编译论文。

## 2026-11-02：将共享输入改为相机 × 时间序列矩阵

用户要求左侧体现多帧、多时刻的输入，并相应调整排版。本轮从上一轮未提交工作区开始，真实基线 PPT、构建源、素材说明和本改动记录已保存于 `paper/build/teaser-temporal-input/before/`，哈希见其上一层 `baseline.json`。基线提交仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`；基线 PPT SHA256 为 `910e81c5ffc06160c5e56c74acecf84ddcdb98584d4425cfec356f7b88c2c8ac`。

具体问题：上一版一列三张照片与 I1/I2/I3 编号只表明多个观测，没有表达相机视角和时间的关系。保持共享输入及上下方法对比，把输入内部组织为两维。

| 位置 | 真实基线 | 本轮修改 | 原因及改善 |
| --- | --- | --- | --- |
| 输入标题 / Input title | `Multi-view observations` / 多视图观测 | `Multi-view sequence` / 多视图序列 | 让标题直接包含序列含义。 |
| 输入照片 / Input images | 三张不同相机或时刻的照片纵向排列，标 I1/I2/I3 | 两列相机 Front-left / Front，三行时刻 t₀ / t₁ / t₂；使用同一片段 frame 000 / 010 / 020 对应的六张原始图 | 同行显示相机维度，同列显示时间推进 / Columns denote cameras and rows denote time. 删除独立图片编号。 |
| 时间线索 / Temporal cues | 没有时间轴；脚注为 `Partial surface coverage` / 部分表面覆盖 | 向下的 `Time` 箭头、时刻标签与两列底部省略号；脚注 `Example frames` / 示例帧 | 表达持续的输入序列，六张仅是展示示例，不限定帧数或相机数。 |
| 整组连接 / Shared-input connection | 括线覆盖三张纵向照片，进入同一个分叉 | 括线覆盖完整相机-时间矩阵，并调整出线位置 | 两条方法路径仍使用同一输入序列；不重复绘制输入。 |
| 聚合占位文字 / Aggregation placeholder | `All views aggregated` / 汇总全部视图 | `All input frames aggregated` / 汇总全部输入帧 | 与时间序列输入的表述一致。 |
| 候选图注 / Candidate caption | `Given the same multi-view inputs` / 给定相同的多视图输入 | `Given the same multi-view image sequence` / 给定相同的多视图图像序列 | 仅同步输入定义，保留方法、补全与复用含义。 |

素材核验：六张图来自 scene 186 的同一 case，使用 `waymo-186/source/f{000,010,020}_{FRONT_LEFT,FRONT}.jpg`。`manifest.json` 对应时戳为 `1553735853362214`、`1553735854362103`、`1553735855362157` μs；t 的下标表示选中的示例时刻，不声称这三个采样是连续帧，也不推定帧率。六张源图均为 1920×1280，使用完整的 3:2 原生图片框展示。PPT 备注和素材说明已同步来源与映射。

下方中央大图、补全小对照、右侧状态展示以及 (a)/(b) 编号保留。原论文 PDF、LaTeX、双语正文、实验数值保持原样；只在候选图注中同步序列定义。交付前完成单页包结构、布局和字体检查，并重新导入渲染检查。

## 2026-11-02：合并 teaser 的重复输入，以共享输入分叉表达对比

用户指出输入相同、只有后续处理不同。本轮基线为上一轮未提交的占位 PPT、构建源、素材说明及本记录，已保存于 `paper/build/teaser-shared-input/before/`，哈希见其上一层 `baseline.json`。基线提交仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，基线 PPT SHA256 为 `3f0fdc58beef29e791240acab67491407f8428f5fd5533b9ca0ab4e8bc975cea`。

具体问题：上一轮通过重复同一组三张输入保证共有条件，却留下两组相同内容与 `Same inputs as (a)` 的重复说明。输入是两条方法路径共同的起点，应在图面上直接共享。

| 位置 | 真实基线 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| 输入图与标题 / Input stack | 上下各一组 `Multi-view observations`，各三张 I1/I2/I3 | 左侧一组 `Multi-view observations`，I1/I2/I3 各出现一次 | 删除重复照片与标题 / Show the common inputs once. |
| 输入连接 / Input connection | 两组输入分别连接上下路径 | 整组照片以括线汇总，连接一个分叉，再进入 (a)/(b) | 后续处理的分歧直接可见 / Fork the common inputs into the two processing routes. 分叉不代表共享推断出的三维场景或掩码。 |
| 输入脚注 / Input footer | `Same inputs as (a)` / 与 (a) 相同的输入 | 删除；共享输入下保留 `Partial surface coverage` / 部分表面覆盖 | 共享关系已由图形表达，删除文字复述。 |
| 分隔线与路径标题 / Divider and route captions | 分隔线横跨整幅图；路径标题横跨输入区域 | 分隔线从共享输入与分叉之后开始，(a)/(b) 标题只对应右侧处理区域 | 避免把共享输入划入某一方法 / Keep the shared input outside the two method panels. |

其余场景、局部补全、状态展示的占位位置与对应要求保留。PPT 备注及素材说明已同步。原 PDF、论文 LaTeX、双语正文、实验数值与候选图注保持原样；没有编译论文。交付文件完成包结构与布局检查，并重新导入渲染检查。

## 2026-11-02：按上下方法对比修正 teaser 编号与共有条件

用户指出前版 `(a)(b)(c)(d)` 编号与上下对比意图冲突，并要求从严格审稿人角度检查排版。本轮基线提交仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，实际基线为上一轮未提交的 PPT、构建源、素材说明和本改动记录，已保存于 `paper/build/teaser-layout-review/before/`；各项哈希见该目录上一层 `baseline.json`。基线 PPT SHA256 为 `7b7fcfc73163d3607e60210083e600975ffbbad7c9cb02bae08daf984f112181`。本轮只微调现有占位 PPT 与相关说明，保留上下布局和下方中央大图。

原问题：前版将上方整条路径与下方三个流程阶段放在同一编号层级；上排两张加省略号、下排三张，且显示宽高比不同；上排一个失败状态与下排三项用途之间缺少固定状态的配对。它们妨碍读者把差异归因于是否联合补全。

| 位置 | 真实基线 | 本轮修改 | 原因及改善 |
| --- | --- | --- | --- |
| 面板编号 / Panel hierarchy | 上排 `(a) Observation-only: regions unseen in all inputs remain incomplete.`；下排 `(b) Driving observations`、`(c) Joint completion`、`(d) Reuse the same assets` | 上排 `(a) Observation-only reconstruction`；下排 `(b) DriveCompose: joint completion and asset reuse`；内部阶段无字母编号 | 两个字母对应两种方法路径 / Two panel letters denote the two method routes. 删除的上排解释仍在 P2/P3 占位文字及候选图注中。 |
| 共有输入 / Common input | 上排两张加省略号；下排三张；上下相同源图的框比例不同 | 两排均从同一数组读取 I1/I2/I3，顺序相同、裁切比例均为 2:1 | 显示相同输入条件 / Show identical illustrative input conditions. 上排采用缩略图以保留原行高。 |
| 下排输入脚注 / Input footer | `Partial coverage across all inputs` / 所有输入的覆盖仍不完整 | `Same inputs as (a)` / 与 (a) 相同的输入 | 用于确认上下对比的共有条件；覆盖条件由 P2/P5 承担。 |
| 对应场景 / Scene correspondence | P4 为 `One coherent scene illustration` / 一个连贯的场景示意 | P4 为 `Same scene and assets as (a)` / 与 (a) 相同的场景和资产；备注要求 P2/P4 同相机、同裁切、同参考状态 | 防止中央大图成为与上排无关的另一场景。 |
| 配对状态 / Matched state | P3 为泛指新状态；P6a 为 `Same assets / New camera view` | 两处均标明 `New camera view s1`，固定相同相机、场景与参与者姿态；P6b/P6c 是额外复用示例 | 将一个明确状态用于失败/补全的配对展示 / Match one camera state across routes. 未把全部三张下排画面误标成三组对照。 |
| 资产复用连接 / Reuse connections | 中央场景到右侧一条箭头，落在中间输出附近 | 同一场景分支至三个状态输出 | 表明三张来自同一批构建内容 / Three outputs reuse the same constructed content. |
| 小字与候选图注 / Labels and candidate caption | 长的上排总结句、右侧多行标签；图注使用 Top/Bottom 泛指 | 路径名简化；右侧缩短为相机视图、车辆旋转、人体姿态；双语图注明确 (a)/(b)、同输入、配对相机状态与额外复用 | 降低缩印后的文字负担，图注指代与图中两条路径一致。 |

尚需在填素材时落实的图形条件：同一 U 在上排缺失、下排补全；P2/P4 为同一参考状态的观测/补全版本，P3/P6a 为同一新相机下的版本；中央场景显示跨组件的上下文交换与相应补全部位，避免仅凭 `Joint completion` 标签或车辆局部小图宣称联合机制。SIDE_LEFT 已可见后门，不能任意将后门当作全部输入中的未知区域。这些条件已写入 [排版审查与素材要求](../paper/fig/teaser-editable/README.md) 和 PPT 备注，灰框继续保留为占位。

标题、摘要、贡献、实验数值、LaTeX 与原图 PDF 保留原样。本轮单页 PPT 的包结构、尺寸、文字几何与字体检查通过，最终修正稿无几何警告；交付文件经重新导入并渲染目检。实际前后变化以本轮保存的工作区基线为准，不把此前改动计入本轮。

## 2026-11-02：保留原 teaser 布局，制作单页可编辑占位 PPT

用户明确要求沿用 `paper/fig/drivecompose-concept-merged.pdf` 的简洁上下结构，仅微调内部内容。本轮基线提交为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区开始；此前生成图及其他论文修改不计为本轮。改动记录的真实基线保存在 `paper/build/teaser-layout/before/paper-revision-changes.md`，SHA256 为 `378149128f72205329f052f65e319337c5cc6708e0301127d50a4ef169678984`。参考 PDF SHA256 为 `3031f2f09069d714ed267cb0390d6ea978e23304b7c7a23d5f5e0225773b1a40`。

具体问题：原图没有明确“先汇总多个视图，再判断剩余未知表面”的关系；上下输入风格不同；底部小图的 `Observed surfaces` 容易被理解成单张观测中的可见部分。本轮在原布局内修复这些关系，交付可编辑占位，不改正式论文图件。此前尝试的四栏结构已按用户要求舍弃。

| 位置 | 原文 / 原图 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| 上方输入 / Top input | `Driving images` / 驾驶图像 | `Multi-view observations` / 多视图观测 | 明确输入包含多个视图；上下采用同一组真实输入示例。 |
| 上方重建场景 / Aggregated scene | `Observed surfaces` / 观测表面 | `Aggregated observed surfaces` / 汇总后的观测表面 | 缺口指汇总所有输入后仍未观测到的表面。 |
| 上方说明 / Observation-only claim | `Observation-only reconstruction: unseen regions remain incomplete.` / 仅观测重建：未见区域仍不完整 | `Observation-only: regions unseen in all inputs remain incomplete.` / 仅基于观测：所有输入均未见的区域仍不完整 | 补上跨视图联合覆盖的条件，避免单张遮挡等同于全部未知。 |
| 底部小对照 / Completion inset | `Observed surfaces` → `Completed surfaces` / 观测表面→补全表面 | `After aggregating all inputs` → `After joint completion` / 汇总全部输入后→联合补全后 | 同一资产、同一视角、同一未知区域前后对应；沿用现有小图位置。 |
| 右侧说明 / State reuse | `Complete once; compose across states.` / 一次补全，跨状态组合 | `Same completed assets across states` / 跨状态复用同一批补全资产 | 直接说明复用对象；三个状态占位要求使用同一次补全结果。 |
| 面板编号 / Panel labels | 上下重复使用 `(a)` | `(a)`–`(d)` 各使用一次 | 消除图注指代歧义。 |

中文为图中文字的对应释义。原有中央大场景、背景/车辆/人体标注、共享场景上下文与右侧三项状态展示均保留。P2/P3/P4/P5/P6 为有明确内容要求的空占位；真实输入已嵌入。SIDE_LEFT 输入可见车辆后门，故未预先把后门指定为所有视图共同未知区域。生成式资产素材的身份和不同 track ID 的边界已记入素材说明，避免将其当作真实配对结果。

交付：[单页 PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx)；[素材要求与双语候选图注](../paper/fig/teaser-editable/README.md)。原 PDF、LaTeX、标题、摘要、贡献与实验数值均保持原样；没有编译论文。导出文件的包结构、单页数量、尺寸、文字几何和字体检查通过；最终文件另行导入渲染目检。PPT 中的灰框为有意保留的素材占位，未冒充完成的实验画面。

## 2026-11-02：生成联合补全概念型 teaser 候选

用户认可概念图方向，并明确要求使用 imagegen 生成。本轮基线提交为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区开始。此前方法总览图、方法节及其他改动不计入本轮。改动记录的真实工作区基线保存在 `paper/build/teaser-conceptual/before/paper-revision-changes.md`，哈希及生成来源见 [生成记录](figures/teaser/conceptual-generation-record.json)。本轮只新增候选图、生成指令和双语候选图注，没有替换论文图件或修改 LaTeX。

具体问题：旧 teaser 采用照片式生成画面与仿重建边缘，上下重复输入，联合机制和同一补全部位跨状态复用不够突出。按用户认可的方向重绘为概念示意，输入画面也统一为示意，不标作真实数据帧。

| 位置 | 原文／原图 | 候选图 | 原因及改善 |
| --- | --- | --- | --- |
| 共享输入 / Shared input | `Driving images` 与 `Driving observations` 分属上下两组 | 一组 `(a) Input observations` / 输入观测，分叉至两条路径 | 对照使用共同输入，减少重复与场景风格差异。 |
| 联合机制 / Joint completion | `Joint completion` 主要标在大型街景上 | 背景、规范车辆、规范人体分别可见，并与 `Shared scene context` / 共享场景上下文连接 | 让跨组件交换上下文的含义可以从图形读出。 |
| 跨状态复用 / Asset reuse | `Complete once; compose across states.` / 一次补全，跨状态组合 | `Completion retains motion bindings` / 补全保留运动绑定；相同后车门与上臂区域在状态变化后保持对应 | 用具体表面与动作解释复用，删除重复口号。 |
| 图像身份 / Image provenance | 照片式场景、散点边缘及概念声明同时存在 | 统一简化绘图风格，保留 `Conceptual illustration` / 概念示意 | 图像形式与来源说明一致；上方路径仍是概念对照，不冒充具名基线输出。 |

候选文件：[PNG](figures/teaser/drivecompose-teaser-conceptual.png)，2098 × 749；[双语图注](figures/teaser/conceptual-caption.txt)。使用内置 image_gen，进行了两次局部对应修正：统一上下规范车辆朝向，将人体补全标记统一到同侧上臂。已目检标注、缺失／补全区域对应、组件连接及输出构图。标题、摘要、贡献、实验数值、双语主稿和正式 PDF 均保持原样；本轮未编译，未执行真实重建或实验验证。

## 2026-11-01：将用户指定的新 PDF 接入双语方法总览图

本轮基线提交为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区开始。用户更新的源 PDF、既有图件编辑记录及其他素材不计为本轮新制作。修改前的两版方法节、说明、改动记录和正式 PDF 已保存于 `paper/build/overview-replacement/before/`；各项实际基线哈希见同目录上一层 `baseline.json`。

具体问题：双语论文仍引用上一版 PNG，未使用本轮用户指定的最新 PDF。仅更换图件引用，按完整页和原跨栏宽度放置。

| 位置 | 原文／修改前 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| English §3, Figure 2 / 英文方法节总览图 | `\includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}` | `\includegraphics[width=\textwidth]{fig/overview-editable/output/DriveCompose.pdf}` | 接入用户指定的新图，并保留 PDF 文字和线条的矢量内容。 |
| 中文第 3 节，图 2 / Chinese method overview | `\includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}` | `\includegraphics[width=\textwidth]{fig/overview-editable/output/DriveCompose.pdf}` | 与英文同步使用同一份用户图件。 |
| 图件说明 / Figure documentation | 当前图件入口为旧 PNG | `paper/README.md` 和总览图说明改为当前 PDF 入口，旧记录标为历史 | 使图件说明与实际 LaTeX 引用一致。 |

学术内容：无文字、数字、引用键、公式或图注修改。标题、摘要、贡献与实验结果均保留。纯图件替换：源 PDF 为单页 1800×1050 pt，与旧 PNG 同为 12:7 比例；源文件 SHA256 `347a71f6d6d8b8f25b98e1ef77b9921a6db9dc891ede1474b415604e16b4b6f6`，替换与编译过程中保持原字节。旧 PNG 不再由两版主稿引用，未删除。

验证：既有 `paper/tools/build.py` 完成两版正式 PDF 编译，退出码均为 0，且均实际更新。英文总览图在第 4 页，中文在第 3 页；两页已渲染目检，图面完整、无新增重叠或裁切。英文总计 11 页，结论在第 8 页，参考文献从第 9 页开始；中文总计 10 页。最终 LaTeX 日志没有未定义引用、缺字或 overfull 报告；仍有原有的纯浮动页提示。Poppler 对源图及嵌入后页面均提示 Symbol / ArialUnicode 显示字体回退，实际渲染的图中文字、符号和箭头已目检。核验摘要见 `paper/build/overview-replacement/verification.json`。

## 2026-10-30：删除停用的 pointforward 图件目录

按用户明确要求删除本地及 Git 上的 `paper/fig/pointforward/`。本轮基线为 `156726d45cb5ee3317c96c1d8e99a4d0ac074c7f`；开始时目录为空，Shift.pdf、Waymo.pdf、nuScenes.pdf 已在本地删除但尚未提交。本轮实际移除空目录，并将三项删除登记、提交和推送。README、检查器与本轮前实际工作区日志保存于 `paper/fig/overview-editable/.build/remove-pointforward/before/`。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| `fig/pointforward/` | Git 跟踪三份旧 PDF，本地仅剩空目录 | 移除本地目录及三项 Git 跟踪 | 用户明确要求删除停用副本；历史版本仍由 Git 保留。 |
| `paper/README.md` | 宣称三份旧副本原样保留 | 指向当前 `fig/assets/Shift.pdf`，记录旧副本已删除 | 与现有双语图引用一致。 |
| `check_manuscript.py` | 冻结文件列表仍强制读取三份旧 PDF | 仅移除这三项过时的在库要求 | 避免检查器要求恢复已停用的副本；其他检查和历史来源清单不改。 |

已核对双语主稿及补充材料无旧目录引用；当前图件 `fig/assets/Shift.pdf` 和两份正式主稿 PDF 哈希保持。检查器语法解析通过；未重编译未改动的稿件，也未将缺少本机历史归档的通用检查器报告为通过。此前未提交的 230 行图件编辑记录和其他本地素材不计入本轮提交。

## 2026-10-30：用用户提供的 PDF 替换论文总览图并整合远端修订

本轮实际起点为 `79bdd94948d4dbea340f4c4098b33aaec201c435` 上的未提交工作区；真实图件、双语 PDF、说明和记录保存于 `paper/fig/overview-editable/.build/pdf-replacement/before/`，基线哈希见同目录 `baseline.json`。仅将用户明确指定的 `output/DriveCompose.pdf` 转为论文活动 PNG，并执行提交、推送和重新拉取。源 PDF SHA256 为 `034178db3de2dd608f0397b909783f47250eea832a0de15eed3955b1cde44aec`。

| 位置 | 修改前 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| `drivecompose-inference-overview.png`／总览图 | 1764×892 PNG，SHA256 `63c62037e5699b421e3fe864b1dbe6e83fc1b4e5680fd56902b8ca754fc97579` | 用户所选 PDF 单页原比例渲染为 6000×3500 PNG，SHA256 `afabc000279b8d239487401a9506c0fffa5d10f3ea44990f7de20261e4aa8a14` | 保留 PDF 完整图面与文本，不重新生图或改画；双语共用原活动路径。 |
| Source and provenance／来源 | 活动文件指向前版机制图 | 提交用户 PDF 原字节、渲染命令、PNG/PDF 哈希及本轮来源记录 | 使论文使用的图可追溯到用户确认的导出文件。 |
| Abstract merge／双语摘要合并 | 本地 `79bdd94` 的已确认开头、解码句与远端新版完整段落冲突 | 保留本地 “Reconstructing complete and controllable 3D scenes …”／“从局部观测中重建完整、可控的三维场景……”以及解码复用句，其余采用远端更新的机制、约束及作者结果 | 保留已确认措辞与远端新证据；不从旧摘要覆盖新的结果段。三方真实文本保存于本轮 `merge-conflicts.json`。 |
| English column flow／英文换栏 | 摘要后无条件 `\par\vfill\newpage` | 仅摘要仍在第一栏时换栏：`\par` 后检测 `\if@firstcolumn` | 远端摘要变长后已跨到右栏，避免旧换栏把引言推到下一页；保留图注后的 8 pt 与 Abstract 标题下 6 pt 间距，不改字号、行距或页边距。 |

原本本地与远端各有一个未合并提交。本轮保留远端 `498f5e89f2685c0c84e9088154b8032fe99705f3` 的正文、方法、实验、官方样式及补充材料，处理摘要和入口冲突后重新编译双语主稿。远端已有的实验更新不计为本轮新增结果；图注和章节中的图引用继承远端结构。

最终英文主稿 11 页，技术正文结束标记在第 8 页；中文主稿 10 页，正文结束标记在第 7 页。总览图分别在英文第 4 页、中文第 3 页。两版编译退出码均为 0，且正式 PDF 本轮实际更新；内嵌图像解码像素与新 PNG 一致。已检查两版首页、总览页和正文末页，无新增图面遮挡或裁切。日志中的提示仅为浮动页；无未定义引用、缺字或溢出记录。通用稿件检查器因本机缺少历史项目外归档，在执行检查前退出；未将其报告为通过。本轮独立编译、像素及页码记录见 `paper/provenance/overview-pdf-replacement-20261030.json`。

此前未提交的 230 行图件编辑记录、三份 pointforward PDF 的删除及其他本地素材暂存保护，合并提交与同步完成后恢复，不包含在本轮新增提交中。

## 2026-10-30：以规范查询为中心重绘 Canonical aggregation

本轮按用户澄清仅重绘 Canonical aggregation 内部，不再调整 Structured latents。真实未提交基线保存为 `paper/fig/overview-editable/.build/before-canonical-query-aggregation.pptx`，SHA256 为 `228a210a36b24a3cd27a16e48ce6c8fc155c4008cd96fd44d91d1f0a5e51b224`；生成脚本及替换说明保留同轮基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

保存前检测到 A10 车辆素材在另一轮中更新，因此把本轮内部重绘重放到最新 PPT。合并基线保存为 `.build/before-canonical-query-aggregation-merged.pptx`，SHA256 `4ecbc80663563664076ed2883d128b1571e2ce88fbcdebd7b7a07775a9efb735`；保留其车辆图片、裁剪和位置等更新，不计为本轮改动。

具体问题：原图以两个带散点的矩形汇入第三个矩形，仅用 `Align · filter · fuse` 概括过程，未显示运动对齐的参照、无效观测的剔除或权重的作用。论文中这一步以固定规范查询为参照，将查询置于各时刻组件状态并投影，聚合同实例、可见且深度一致的图像证据。技术依据为 `paper/sec/3_method.tex` 的 Canonical feature aggregation、查询放置公式与聚合公式，并与 `docs/representations.md`、`docs/algorithm.md` 对照。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| Alignment reference／对齐参照 | 两个特征矩形，没有固定参照点 | 顶部规范查询 `qᵢ`；`Pose + project`／按状态放置并投影，以紫色虚线连到两张观测平面的不同采样位置 | 明确同一规范查询在不同时间／视角中的对应关系；没有用统一逆刚体变换替代人体的正向蒙皮投影。 |
| Valid evidence／有效观测 | 很小的灰色散点与叉，缺少筛选含义 | `Depth + ID`／深度与实例筛选；有效路径旁为勾，灰色候选块划叉且没有输出路径 | 让可见性、深度一致和同实例条件可读，显示筛选对特征流的作用。 |
| Weighted aggregation／加权聚合 | 两条灰色箭头直接连接输出矩形 | 蓝色实线经 `w₁`、`w₂` 汇入 `Σ`，输出 `hᵢ`／规范特征 | 显示置信度与深度残差决定权重，多个观测融合到同一查询。图中 Σ 表示带归一化权重的聚合；残差通道在备注中说明。 |
| Visual hierarchy／视觉层级 | 三个平面内重复蓝／橙／绿散点 | 稀疏的大色块；橙色贯穿同一查询，紫色虚线为投影、蓝色实线为特征流 | 区分几何投影与证据流，减少格子和重复元素。主要内部文字 32 px，查询 34 px，融合符号 36 px；保留原 42 px 模块标题及紫色分组框。 |
| Editable reconstruction／可编辑复现 | 原生简化示意 | 先用内置 imagegen 生成设计参考，再用 43 个 PPT 原生形状与文本复现，替换原 26 个内部形状 | 查询、特征平面、筛选符号、权重、线条及输出均可单独编辑；参考 PNG 未作为整块截图嵌入。 |

imagegen 设计参考保存为 `paper/fig/overview-editable/assets/canonical-aggregation-concept.png`（1485×1059），完整提示词为 `canonical-aggregation-concept-prompt.txt`，来源和哈希为 `canonical-aggregation-design.json`。两个观测与一次拒绝仅为机制示意，不规定实际视角数，也不作为测量结果。背景、刚体、人体采用各自的查询放置规则；未观测内容的生成仍由后续联合补全表达。

已查看最终整页渲染，并提高关键标注字号、调整底部说明与边框间距；PPTX 包结构、画布、字体及重新导入检查通过。逐对象核验确认目标模块之外的对象文字、视觉样式与几何保持，10 张既有图片的字节、裁剪和变换保持；最终包含 392 个原生形状。生成脚本、替换说明及幻灯片机制备注同步更新。最终 PPT SHA256 为 `6c398107dfd9895efafaa9446d07d10267bf19cb2ae7c467b60f184797a8e909`。未改论文正文、公式或实验值，无 LaTeX 编译。

## 2026-10-30：简化背景标签并重排结构潜码三行

本轮仅调整用户指出的解码背景标签和右上 Structured latents 排版。真实未提交基线保存在 `paper/fig/overview-editable/.build/before-latent-row-layout.pptx`，SHA256 为 `e19deb313eeb8a143add63d2af431f2d8ed51bf344c09c25ef9f31886db978dc`；该起点包含 A03/A10 车辆及 A09 背景等已有素材，全部继承。生成脚本与替换说明保存对应基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| Decoder background caption／背景解码标签 | `Background + sky`／背景与天空，28 px | `Background`／背景，30 px，与 Rigid、Human 同字号 | 按用户要求仅突出背景类别，减少文字。背景语义仍涵盖天空。 |
| Structured latent labels／结构潜码标签 | `Background · world`、`Rigid · canonical`、`Human · canonical`，居中放在 token 上方 | 左列为 Background／Rigid／Human，34 px 加粗；第二行为 world／canonical，28 px | 将类别与坐标说明分成两个层级；三行共享同一左边界，避免文字与 token 上下挤在一起。 |
| Token sequences／潜码序列 | 五个 44×44 token，间距 18 px，位于标签下方 | 五个 42×42 token，间距 12 px，统一置于右列，省略号对齐 | 形成稳定的左右阅读顺序，保持三类序列的对应。token 数量仍为机制示意，未改模型维度。 |
| Rounded bands／圆角底板 | 580×115，中心与输入箭头相差 7.5 px | 580×110，中心分别位于 y=260／390／520，与输入箭头对齐 | 统一上下留白和行间距；保留原蓝／橙／绿配色与圆角样式。 |

已查看整页渲染，未见新增重叠或裁切；PPTX 包结构、画布、字体及重新导入检查通过。逐对象核验确认仅修改目标的 25 个原生形状，增加 3 个坐标说明文本；其余对象内容、位置及 10 张已有图片的字节、裁剪与变换保持。生成脚本和替换说明同步更新。最终 PPT SHA256 为 `228a210a36b24a3cd27a16e48ce6c8fc155c4008cd96fd44d91d1f0a5e51b224`。未修改论文正文、方法或实验值，无 LaTeX 编译。

## 2026-10-30：将 A10 改为朝左前方的三分之四视角

本轮仅按用户参考调整 A10 车辆朝向。真实未提交基线为 `.build/before-A10-direction.pptx`，SHA256 `e19deb313eeb8a143add63d2af431f2d8ed51bf344c09c25ef9f31886db978dc`；原 A10 素材保存为 `.build/A10-before-direction.png`，原提示词、素材表、替换说明及编辑脚本同时留有基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A10 vehicle orientation／车辆朝向 | 朝右、接近纯侧面 | 朝左前方的前侧三分之四视角，能看到前脸、前挡风玻璃、侧面及车顶 | 对应用户参考中 Canonical rigid 小车的展示角度，完整资产的体积更易辨认。 |
| Image placement／图片适配 | 1774×887 图像，110×55 显示 | 1536×1024 RGBA，在原 110×55 位置内居中显示为 82.5×55，左上角 (713.75,1035) | 保持新图纵横比与原有周边间距，避免沿旧比例拉伸。 |

使用内置 imagegen 编辑上一版完整车，参考图仅用于朝向与视角；白色车体、红蓝条纹与邮政车识别元素延续。选定原字节输出保存为 `assets/A10-canonical-vehicle.png`；当前完整提示词、生成源和旧版历史均保存在 `assets/A10-canonical-vehicle-prompt.txt`。参考图另存 `.build/A10-direction-reference.png`。生成素材仍用于方法示意。

保存时检测到另一轮已更新背景标签及右上潜码行排版，因此在最新文件上重放 A10 图片替换。合并基线保存为 `.build/before-A10-direction-merged.pptx`，SHA256 `228a210a36b24a3cd27a16e48ce6c8fc155c4008cd96fd44d91d1f0a5e51b224`，这些既有改动全部保留。

已查看合并后的整页渲染并通过包结构、字体、画布和重新导入检查。逐对象核验确认最新基线的 375 个原生对象和其余 9 张图片及位置保持，仅 A10 图片来源及其等比适配范围改变；总图片数保持 10。最终 SHA256 `4ecbc80663563664076ed2883d128b1571e2ce88fbcdebd7b7a07775a9efb735`。素材清单、替换说明及构建使用的说明同步更新，未修改论文正文。

## 2026-10-30：嵌入 A03 观测车辆并生成 A10 规范车辆示意

本轮按用户确定的素材方案仅替换 A03 与 A10。起始未提交基线为 `.build/before-A03-A10-vehicles.pptx`，SHA256 `6b52ec0a4728c5bcb5985d041316bf67286ed21531bf3ee7967a8b8af824c181`；脚本、素材映射及说明均保留同轮基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。A03 先保存到正式 PPT；生成 A10 期间 A09 背景已由另一轮写入，因此 A10 基于最新文件修改，合并基线为 `.build/before-A10-vehicles-merged.pptx`，SHA256 `c961416db4b2fa435a58f35f1e259080057b14d645f5b022493052cf5f67f190`，保留 A09 并不计入本轮改动。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A03 Rigid pose／观测车辆姿态 | 灰色 A03 占位框与编号 | V01 f000 FRONT_LEFT 半截邮政车原始透明抠图 | 与输入照片对应，保留实际观测的截断车身；1076×689 RGBA 原字节嵌入，按原 100×65 逻辑像素框等比适配。 |
| A10 Rigid asset／规范刚体资产 | 灰色 A10 占位框与编号 | 完整白色邮政车透明 PNG，车头朝右、车轮摆正，补齐后车体与轮胎 | 以观测外观为依据展示规范完整资产，保留白色车身、红蓝条纹、邮政标识及方盒车体；原 110×55 框等比适配。 |
| Asset provenance／素材来源 | 两处为待填占位 | A03 原始观测；A10 内置 imagegen 参考编辑的机制示意 | 原图和生成图分别记录，来源与说明写入备注；不将 A10 当作模型实际解码或重建结果。 |

A10 主参考为 `assets/waymo-186/vehicles/V01_postal_front_PARTIAL_f000_FRONT_LEFT.png`，V02 仅用于辅助车身比例和后部结构；两者记录的 track ID 不同，未断言跨相机实例身份已经核验。选定输出 `assets/A10-canonical-vehicle.png` 为 1774×887 RGBA，提示词与生成源见 `assets/A10-canonical-vehicle-prompt.txt`，项目素材按生成原字节保存。另一次边缘清理变体增加了白色碎片，未采用；选定首版已按实际白底图面尺寸检查。

PPTX 包结构、字体、画布及重新导入检查通过。逐对象核验确认各阶段仅删除目标灰框及编号，新增对应图片，其余原生对象、已有图片及其位置均保持；最终包含 372 个原生形状和 10 张图片。最终 SHA256 `e19deb313eeb8a143add63d2af431f2d8ed51bf344c09c25ef9f31886db978dc`。生成脚本、素材清单和替换说明同步更新；已查看整页渲染，无新增重叠。未修改论文正文、实验值或正式图引用。

## 2026-10-30：为 A09 生成去动态目标的静态背景补全示意

本轮按用户要求制作 A09。真实未提交基线保存在 `.build/before-A09-background.pptx`，SHA256 为 `59ce1c2452ba4433c267eda327b4bc082ea2174e521f90d74796a69a803a3853`；该实际起点已包含本轮生成期间保存的车辆图等既有编辑，全部继承，不计入本轮。生成脚本、素材映射和替换说明保存对应同轮基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A09 Background + sky／背景与天空 | 浅灰 A09 占位 | 与 A01 同一左前视角场景的静态背景补全图 | 输入与背景示意保持场景对应。移除邮政车、其他车辆、行人及自行车，补齐其遮挡的道路、人行道和背景。 |
| Static scene appearance／静态场景外观 | 原图动态目标遮挡街景 | imagegen 编辑后保留可辨认的桥梁、树木、路牌、围挡及路口结构 | 以原视角和场景内容为依据补全；不将生成结果声称为像素完全不变的编辑。 |
| Embedded picture／PPT 图片 | 200×56 逻辑像素占位框与编号 | 嵌入完整 1536×1024 PNG，以原框显示可编辑横幅裁剪：左右不裁、上 22%、下 36% | 清除编辑占位标记，保留之后重新取景的能力；原图单独保存。 |
| Provenance／来源记录 | A09 待填素材 | `assets/A09-static-background.png`、`A09-static-background-prompt.txt`、`A09-static-background-provenance.json` | 记录生成提示词、两张参考图哈希、输出哈希及显示裁剪。素材状态为 `embedded-illustration`。 |

采用内置 `image_gen` 编辑：主图为 `assets/waymo-186/source/f000_FRONT_LEFT.jpg`（与 A01 相同），辅助静态场景参考为 `backgrounds/B02_source_plate_f060_FRONT_LEFT.jpg`。A09 是去动态目标与遮挡补全的机制示意，不是实际高斯解码结果或真值；来源及边界写入幻灯片备注。原始输入相机照片及现有 Waymo 素材未改。

PPTX 包结构、字体、画布与重新导入检查通过，已查看整页渲染，未见新增遮挡或越界。其余对象沿用本轮真实基线，未改论文正文、实验值或正式图引用，无 LaTeX 编译。

## 2026-10-30：生成 A11 规范人体示意并将结构潜码改为纯 token 表达

本轮依据用户对 A11 及 A05–A07 的明确要求修改同一页 PPT。真实未提交基线保存在 `.build/before-A11-token-only.pptx`，SHA256 为 `2e9afa406c784b3102a69e3ff9db4706f49a87281131df8dc7d6434fab9e5e49`；生成脚本、素材映射和替换说明保留对应同轮基线。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A11 Human asset／规范人体资产 | A11 灰色占位框 | 基于 P01 f020/f022 生成的透明底规范静止 A-pose 人物示意；深色夹克、蓝裤、黑鞋及体型与参考保持联系 | 区分 A04 当前帧的迈步姿态与解码后可复用资产的规范展示姿态。保留原 48×78 逻辑像素位置，按比例适配。 |
| A05/A06/A07 in Structured latents／结构潜码中的三张图片 | 背景、车辆、人体图片占位，及车辆坐标轴／人体骨架 | 删除三张图片占位及相邻几何图标；保留 `Background · world`、`Rigid · canonical`、`Human · canonical` | 该阶段处理潜码，完整资产图像留在解码端展示，避免与补全后资产混淆。 |
| Latent token rows／三类潜码行 | 每行五个 26×26 token，靠右放置 | 保留每行五个 token，改为 44×44 并统一居中；省略号同步对齐 | 利用删除图像后的空间，明确三条潜码序列的对应。token 数量为机制示意，未改变实际潜维度或查询数。 |
| Asset inventory／素材映射 | A05–A07 继续列为待填图片，A11 为占位 | A05–A07 停止作为图片素材使用，A11 记录实际 PNG 来源和 `embedded-illustration` 状态 | 后续只需准备解码侧资产，无需为潜码行重复生成人物、车辆或背景。 |

A11 使用内置 `image_gen` 参考编辑，原图为 `assets/A11-canonical-human.png`（893×1761 RGBA），完整提示词及来源记录为 `assets/A11-canonical-human-prompt.txt`。这是一张规范资产的机制示意图，不是实际模型解码渲染，也不包含三维几何或蒙皮权重；相关来源写入幻灯片备注。

已通过 PPTX 结构、字体、画布及重新导入检查，并查看整页渲染。A04 真实人物图、输入照片、A13 相机、原配色及其余方法模块保持。论文正文、实验值与正式图引用未改，无 LaTeX 编译。

## 2026-10-30：将选定人物原图放入 A04 并对应行走姿态示意

本轮仅替换 A04 及其相邻姿态示意。真实未提交基线为 `.build/before-A04-human.pptx`，SHA256 `a437abdb723dc8a733e0220cc65a31263e210e59e17bbc10d6c76f9563200fd0`；生成脚本、素材表和替换说明均保存了对应同轮基线。该基线已经包含输入照片与 A13 相机，本轮不覆盖或计入这些既有修改。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A04 Human pose／当前帧人体姿态 | 灰色 A04 占位框与编号 | 直接嵌入 `assets/waymo-186/people/P01_dark_jacket_f020_FRONT_LEFT.png` 的原始 RGBA 人物抠图，216×426 像素 | 按用户选定的深色夹克人物放入，保留迈步姿态；按原 50×82 逻辑像素框保持比例显示。未生成、锐化或重新着色人物。 |
| Adjacent skeleton／相邻骨架 | 通用直立姿态图标 | 原生可编辑的迈步骨架示意 | 与人物动作方向和双腿展开关系对应。该骨架为手工示意，未声称是该帧的三维姿态估计结果。 |
| A11 Canonical asset／规范人体资产的语义 | 用户询问其是否等同“处理好的 pose” | 明确为规范坐标中的带衣人体高斯资产，以模板 rest pose 展示，保留蒙皮绑定；当前帧动作留给后续状态驱动 | 依据当前方法的 Human queries、Gaussian decoding 和 Scene composition；避免把资产仅理解为一张换姿势的人像。本轮 A11 素材未生成、占位未改。 |

同一身份可由 f020 和 f022 的 Waymo track ID `219ff131-95cb-46c2-8deb-2024687ba1d4` 关联。已查看整页渲染并通过 PPTX 结构、画布、字体和重新导入检查；来源及骨架示意身份写入幻灯片备注，保留原输入照片备注。A07 未改，论文正文、实验值及正式图引用未改，无 LaTeX 编译。

## 2026-10-30：生成 A13 相机简笔线稿并嵌入状态模块

本轮仅制作并替换 A13 素材。真实未提交基线保存在 `paper/fig/overview-editable/.build/before-A13-camera.pptx`，SHA256 为 `e855e8350f21a44558fb1820b2e807fc9f915ca85c7a0e9c6f821d1e7c59123c`；脚本、素材清单及替换说明均在 `.build/` 留有同轮基线。仓库基线提交为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| A13 Camera／状态相机 | 浅灰图片占位框及 `A13` 编号 | 透明底深蓝相机轮廓，镜头带一圈蓝线；删除灰框和编号 | 按用户要求采用简笔线稿，与右侧坐标轴、人体骨架的平面线条呼应。 |
| Image placement／图片位置 | 左上角 (543, 812)，尺寸 42×45 逻辑像素 | 同位置同尺寸，原比例适应，不拉伸 | 保留状态模块中三个元素的间距，缩小预览后加粗了相机轮廓以保证辨识度。 |
| Asset and source／素材及生成源 | A13 仅记录推荐像素尺寸 | `assets/A13-camera.png`，1429×1100 RGBA；提示词为 `assets/A13-camera-prompt.txt`；素材清单增加来源与嵌入状态 | 原图保留 Alpha 通道，另存于项目中，PPT 内亦嵌入实际 PNG。 |

使用内置 `image_gen` 生成，并依据用户线条参考调整；早期写实草图未用于正式 PPT。相机是图片组件，旁边坐标轴与骨架继续为原生可编辑形状。PPTX 结构、画布、字体和重新导入检查通过，已查看整页渲染并核对位置。图标只表示相机状态，不作为实验结果；未改论文正文、方法或数值，无 LaTeX 编译。

## 2026-10-30：将输入占位替换为 Waymo 多相机原图

本轮只修改总览图输入区。真实基线为开始时的未提交 PPT，保存在 `paper/fig/overview-editable/.build/before-input-views.pptx`，SHA256 为 `e855e8350f21a44558fb1820b2e807fc9f915ca85c7a0e9c6f821d1e7c59123c`；生成脚本、素材映射和替换说明也分别保存到同一 `.build/` 目录。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`。前轮标题栏、训练状态符号、Logo 和配色均继承。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| Multi-view images／多视图输入 | A01、A02 两个灰色横向占位框 | 同一 Waymo 帧的三张跨相机原图；左前视图放大居中，下方两张补充邮政车后部与过街行人 | 同时呈现真实人车与跨视角观测，避免窄横条裁掉主要主体。 |
| Input set／输入集合 | 两个显式素材编号 | 仅保留 Multi-view images 总标题，图面无相机名称，底部增加省略号 | 三张照片作为多路输入示例，避免暗示输入固定为三路相机。 |
| Encoder connection／编码器连线 | 从 A02 右侧直接连到 E | 新增直角括线汇合多视图，再通过原加粗箭头连到 E | 表达整个多视图集合共同输入编码器。 |

素材来自 case `1024360143612057520_3580_000_3600_000`、processed scene 186、第 0 帧（时间戳 `1553735853362214`）：A01 为 FRONT_LEFT，A02 为 SIDE_LEFT，新增 A16 为 FRONT，避免复用原 A03 车辆编号。图片在 PPT 中保持独立、完整原始 JPEG 嵌入及可调整裁剪；仅调整取景，没有生成、补绘、调色或移除人车。相机身份保存在备注和 `assets/waymo-186/input-views/selection.json`，不显示在论文图中。另保存三张无缩放 PNG 裁剪素材，方便复用。

保存前检测到另一轮 A13 相机素材已写入同一 PPT，因此改为在最新文件上重放本轮输入区修改。该合并基线保存在 `.build/before-input-views-with-camera.pptx`，SHA256 为 `24e254c7ea446988dc438b043411f572362a222d4899e2a1c3f3fff045386285`。A13 的图片、来源记录和生成脚本更新均保留，不计为本轮改动。最终合并 PPT 的 SHA256 为 `a437abdb723dc8a733e0220cc65a31263e210e59e17bbc10d6c76f9563200fd0`。

已查看整页渲染并核对间距、主体可见性和直线连接；包结构、单页画布、字体与重新导入检查通过。逐对象对照确认其余模块文字、位置、样式、Logo 及 A13 相机图片内容保留。论文正文、结果图和实验数值未改。

## 2026-10-30：结合训练阶段增加标题栏、分组和状态符号

本轮按用户澄清借鉴参考图的模块结构与符号设计，保留蓝／橙／绿分支和紫色机制模块。真实基线是本轮开始时的未提交 PPT，保存为 `paper/fig/overview-editable/.build/before-semantic-style.pptx`，SHA256 为 `a1217ea992130dd0dac0a4a2e21d32b261e8cddaf151848686998460f6c02b0e`；生成脚本保存为 `.build/build-before-semantic-style.mjs`。仓库基线提交仍为 `79bdd94948d4dbea340f4c4098b33aaec201c435`，不将其冒充 PPT 原文来源。

技术依据为当前 `paper/sec/3_method.tex` 的 Training procedure 及训练阶段表，并与 `docs/training.md` 核对：Prior 与 Adaptation 阶段冻结 recovery 和整个 codec，仅训练／适配 GCM。因此没有把火焰泛化为所有模块的微调，也没有把雪花解释为视觉恢复模块从未训练。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| Canonical aggregation／规范聚合 | 标题位于实线圆角框内部 | 跨越分组顶边的淡紫标题栏，外围改为圆角虚线 | 借鉴参考图的标题与分组层次；延续原配色。 |
| Joint latent completion／联合潜码补全 | 框内标题，外围为实线圆角框 | 跨边框标题栏及圆角虚线分组，标题左侧增加火焰 | 让整个 GCM 对应可训练／可适配状态，避免只给 CCM 单独标火。 |
| Recovery and codec／恢复模块与编解码器 | 无训练状态符号 | 视觉编码器、三个潜码编码器及三个高斯解码器旁各增加原生雪花 | 对应 Prior／Adaptation 阶段的冻结状态；解码器图标放入侧边留白，避开相邻模块。 |
| Training legend／训练图例 | 无 | `Prior / adaptation`／先验训练与适配；雪花 `Frozen`／冻结；火焰 `Train / adapt`／训练或适配 | 明确图标适用阶段，保留方法表中的训练与适配区别。 |
| Geometry connector／几何输入连线 | 箭头指向原分组顶边 y=210 | 指向新标题栏顶边 y=185 | 保持连线竖直，并避免穿过标题文字。 |

雪花、火焰、标题栏和图例均为 PPT 原生可编辑对象，未新增栅格素材。已通过 PPTX 结构、画布、字体与重新导入检查，并查看整页渲染，修正了解码器雪花与邻接轮廓的间距。论文正文、训练表、实验值及正式论文图引用未改，无 LaTeX 编译。

## 2026-10-30：按用户反馈保留与 Logo 呼应的原配色

用户提供蓝、青绿、奶油色及淡紫参考图后，本轮在 `.build/` 内生成了配色与标题色带试稿；用户随后明确认为原配色更好，且能与中央标题／Logo 呼应。因此不将参考配色试稿写入正式文件，并将生成脚本恢复到本轮真实基线。正式 PPT 和预览保留原有蓝、橙、绿分支及紫色机制模块。

真实基线保存在 `paper/fig/overview-editable/.build/before-reference-palette.pptx`、`before-reference-palette.png` 和 `build-before-reference-palette.mjs`。本轮最终 PPT SHA256 为 `a1217ea992130dd0dac0a4a2e21d32b261e8cddaf151848686998460f6c02b0e`，与该基线完全一致；参考色试稿不计为最终改进。

| 位置 | 参考配色试稿（英文／中文） | 最终保留（英文／中文） | 原因 |
| --- | --- | --- | --- |
| Background／背景分支 | 蓝 `#89B0E7` | 蓝 `#168CE3` | 与 Logo 蓝色组件呼应，保留原辨识度。 |
| Rigid／刚体分支 | 青绿 `#0CC6C8` | 橙 `#F39A2C` | 与 Logo 橙色组件呼应。 |
| Human／人体分支 | 粉色 `#FD75A0` | 绿 `#0AB88C` | 与 Logo 绿色组件呼应。 |
| Completion／补全模块 | 淡紫容器、紫色标题色带和阴影 | 紫色 `#9458DE` 描边与原浅底色 | 与 Compose 紫色字标呼应，保留原有图面层次。 |

已完成的七个原生梯形编解码器、加粗箭头、潜码分组框、字号和间距均保留。通过文件哈希核验恢复结果；无论文正文或 LaTeX 修改。

## 2026-10-30：用梯形区分编解码网络与圆角模块

本轮修改同一份可编辑 PowerPoint。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`；真实基线为本轮未提交的 PPT，保存在 `paper/fig/overview-editable/.build/before-network-shapes.pptx`，生成脚本保存在 `.build/build-before-network-shapes.mjs`。直接导入基线并编辑现有对象，未重建整页。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| E、E_b/E_r/E_h／视觉及组件编码器 | 与普通模块相同的圆角矩形 | 原生梯形，沿右向数据流从宽端收窄至潜码端 | 用轮廓区分编码网络与分组容器；形状表达转换角色，不表示具体层数或通道数。 |
| D_b/D_r/D_h／组件解码器 | 与普通模块相同的圆角矩形 | 原生梯形，沿左向数据流从潜码端向输出端展开 | 对应潜码到场景组件的重建。上下排数据流相反，因此图面上的梯形都为左宽右窄；并非机械地将解码器水平翻转。 |
| Subscripts／六个组件下标 | 原圆角框内的位置 | 各向左及向上移动 3 px，字号保留 | 为梯形斜边留出间距，保留 E/D 与下标的对应。 |
| Geometry branch／编码器顶部支线 | 起点 y=300 | 起点 y=314，与梯形顶边相接 | 衔接新的轮廓，继续使用水平／垂直连线。 |

聚合、补全、局部注意力及潜码分组保留圆角框，特征保留叠片，token 保留方块；前轮加粗箭头、颜色、字号和 Logo 均保留。PPTX 结构、字体、单页画布及重新导入检查通过；已对照整页渲染检查文字、斜边和连线。未改论文正文或实验内容，无 LaTeX 编译。

## 2026-10-30：加粗总览图箭头并恢复潜码分组框

本轮仅调整 `paper/fig/overview-editable/output/DriveCompose-overview-refined.pptx` 的箭头及用户圈出的潜码分组框。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`；真实基线是本轮开始时的未提交 PPT，保存在 `.build/before-arrows-frames.pptx`，对应脚本为 `.build/build-before-arrows-frames.mjs`。前轮配色、字号、标签精简及 Logo 不计入本轮修改。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| Main flow arrows／主流程箭头 | 默认线宽 2.2 px，箭头尖端长 9 px、宽 8 px | 默认线宽 3.8 px；较细流程线至少 3.2 px；对应尖端长 13.5 px、宽 12.6 px | 提高缩放后的方向辨识度，延续水平／垂直布线。坐标轴及骨架线保留原尺寸。 |
| Initial latents／初始潜码 | 无可见外层分组框，三行 token 裸排 | 蓝色虚线圆角外框，三行分别增加同色虚线圆角框 | 按圈选参考恢复清晰的整体及行级分组。 |
| Completed latents／完成潜码 | 三行 token 裸排 | 蓝、橙、绿三行分别增加同色实线圆角框，并将连线端点对齐边框 | 与初始潜码形成对应，保留完整／待补全状态的实线与虚线区别。 |

验证：PPTX 包结构、2400×1400 单页画布、字体及重新导入检查通过；已查看整页渲染，未见新增重叠或裁切。主稿正文、图面文字、Logo 和图片占位内容未改，无 LaTeX 修改或编译。

## 2026-10-30：提高总览图饱和度、放大字号、精简标签并加入 Logo

本轮按用户对 PPT 的批注修改同一个交付文件 `paper/fig/overview-editable/output/DriveCompose-overview-refined.pptx`。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`；真实基线是上一轮未提交 PPT，已保存到 `.build/before-vibrant.pptx`，对应脚本保存为 `.build/build-before-vibrant.mjs`。不将前轮网格简化和 CCM 机制校正计入本轮。

| 位置 | 修改前（英文／中文） | 修改后（英文／中文） | 原因及改善 |
| --- | --- | --- | --- |
| 中央标识 | `DriveCompose overview`／DriveCompose 总览，36 px 灰色文本 | imagegen 透明底 `DriveCompose` Logo；删除 overview | 按选中元素批注执行。三块蓝、橙、绿组件围出道路，字标使用深蓝与紫色；作为独立图片组件插入，非可逐字编辑文本。 |
| 组件配色 | 蓝 `#659BC5`、橙 `#CF995D`、绿 `#76A18C`、紫 `#9685B3`，token 再叠低透明度 | 蓝 `#168CE3`、橙 `#F39A2C`、绿 `#0AB88C`、紫 `#9458DE`，token 80% 不透明度 | 提高主体对比和饱和度，容器仍使用浅色底，保持三类组件对应关系。 |
| 字号 | 多数说明约 19–29 px，主标题约 34 px | 主标题约 40–42 px；主要标签约 30–34 px，CCM 46 px | 提高整图缩放后的可读性。图片框的素材编号属于编辑标记，小框仍采用较小字号。 |
| 输入和编码 | `Driving images` + `Multi-view log`；`Visual encoder`；`Visual features` | `Multi-view images`／多视图图像；`Encoder`／编码器；`Features`／特征 | 合并重复输入说明，保留过程名称。 |
| 规范聚合 | `Same component across views`、`Aligned canonical feature` 两处说明 | 删除两处文字；保留 `Canonical aggregation` 与 `Align · filter · fuse` | 对应点和汇聚图形承担说明，减少标题已经覆盖的重复文字。 |
| 结构化潜码 | `Background (world space)`；`Rigid/Human (canonical space)` | `Background · world`；`Rigid/Human · canonical` | 保留空间语义，缩短标签以支持较大字号。 |
| 初始化及完成模块 | `Initialized latent codes`；`Observed + unknown (noise)`；`Updated tokens`；`Shared memory`；`read/write`；`τ (flow time)` | `Initial latents`／初始潜码；删除五组辅助说明；保留 `CCM`、`Local attention` 和 `τ` | 总览保留模块和必要变量。读写方向由箭头、未知项由虚线 token 与噪声输入表达；被删说明仍在当前方法正文，不声称新迁移了内容。 |
| 解码及输出 | `Gaussian decoders`；`Canonical rigid/human`；`Composed Gaussian scene`；`Rendering` | `Decoders`；`Rigid/Human`；`Gaussian scene`；`Render` | 规范坐标已经在结构化潜码行说明，场景类别已经明确；减少重复修饰。 |
| 形状及间距 | 编解码器为梯形，特征为直角／斜平面，token 为直角方块；正文较小 | 统一原生圆角编码器、解码器、特征片、token 及组件框；为增大的标签腾出间距 | 按用户要求统一轮廓，保留2400×1400画布及水平／垂直主连线。 |

Logo 使用内置 `image_gen` 生成，原始透明 PNG 位于 `paper/fig/overview-editable/assets/drivecompose-logo.png`，完整提示词位于同目录 `drivecompose-logo-prompt.txt`。图像为 2172×724 RGBA，Alpha 通道包含完全透明和不透明像素；PPT 中使用原生图片裁切来适配中央位置，原始 PNG 未改写。生成图只用作方法标识。

验证：PPTX 包结构、画布、字体及重新导入检查通过；整页渲染检查后调整了解码器标题、Compose 框以及人体标签的间距。主稿文字、实验数值及正式论文图像引用未变，无 LaTeX 修改或编译。图面为英文，表内给出中文语义对照。

## 2026-10-29：按 VGGT 图示参考精简可编辑总览图

范围为单页 PowerPoint `paper/fig/overview-editable/output/DriveCompose-overview-refined.pptx`，基于本轮开始时的未提交 `DriveCompose-overview-spaced.pptx`。仓库 HEAD 为 `79bdd94948d4dbea340f4c4098b33aaec201c435`，它不是本轮 PPT 的原文来源。真实基线脚本与素材清单分别保存为 `.build/build-before-refinement.mjs`、`.build/asset-map-before-refinement.csv`；上一轮 PPT 和预览原样保留。本轮不计入此前画布放大、间距调整或占位框搭建。

参考：[VGGT 作者版论文 Fig. 2（第 3 页）](https://www.robots.ox.ac.uk/~vgg/publications/2025/Wang25/wang25.pdf)，2026-10-29 检索并实际渲染查看。参考图中的色块对应 token 分组，主体使用常规衬线文字、灰色连线和少量模块容器。本轮借鉴其视觉层级，不复用其方法结构、实验图像或声称采用其精确字体。技术依据为当前 `paper/sec/3_method.tex` 的视觉编码、规范聚合及联合补全段落。

| 位置 | 本轮真实基线（英文／中文说明） | 修改后（英文／中文说明） | 原因及改善 |
| --- | --- | --- | --- |
| Visual features／视觉特征 | 三面密集网格立方体，并带橙色小格 | 三张有偏移的平面叠片，无内部网格 | 保留多张特征图的含义，减少无信息小格及将其误解为空间体素的可能。 |
| Canonical aggregation／规范聚合 | 三片 8×6 网格；`Multi-view features (same object)` | 三片简化平面，仅保留三个对应点及一个灰色被筛除观测；`Same component across views`／跨视图的同一组件 | 让颜色承担对应关系，让筛选有可见对象；component 与背景、刚体和人体的统一表述相符。点仅为机制示意，不表示实验样本数量。 |
| CCM／跨组件记忆 | 紫色网格立方体，单独的 `CCM` 标签 | 扁平模块，内部为 `CCM` 与 `Shared memory`／共享记忆，三条水平读写通道 | 正文明确 CCM 是共享记忆读写机制，网格立方体没有解释该机制且易被误解为空间结构。 |
| 组件更新 | Background/Rigid/Human component 内还重复绘制 token | `Local attention` 下的 Background/Rigid/Human 模块 | 对应正文先组内注意力、再读写共享记忆的顺序。左右的 token 行继续表示更新前后的特征。 |
| Flow time／流时间 | τ 的箭头直达 CCM 附近 | `τ (flow time)` 从外部进入整个联合补全模块 | 正文将流时间用于局部归一化调制；总览图不将它专属绑定给 CCM。 |
| Initialized latent codes／初始化潜码 | 仅颜色与实心／虚线 token | 补充 `Observed + unknown (noise)`／观测码与噪声初始化的未知码 | 说明噪声作用于未知码；未新增实验或方法步骤。 |
| 标题与线框 | 多处粗体衬线字；中央 64 px 粗斜体标题；多层虚线框和高饱和边框 | 常规衬线字为主；中央 36 px 正体标题；删去潜码外围的重复边框，保留两个核心机制的浅色容器 | 减少视觉竞争，保留蓝／橙／绿的组件对应关系和紫色的联合处理模块。 |
| 图片占位 | 灰色虚线框内两行：编号名称、显示尺寸 | 浅灰实线框内保留编号名称，小图框仅保留编号；尺寸留在 `asset-map.csv` | 减少最终图面上的编辑信息，图片替换能力保留。 |
| 编解码符号 | Unicode 下标 b 被显示为类似 β 的字形 | E/D 与单独的小号斜体 b/r/h 文本 | 避免背景下标的字形歧义，仍可原生编辑。 |

纯视觉调整与局部机制澄清均已体现在上表。标题、摘要、正文、实验数字、引用键和中英文 LaTeX 未改；未替换主稿中的正式总览图，未运行 LaTeX 编译。此文件仅有英文图面，无新中文图面需同步；上表提供中文语义对照。

验证：PPTX 包结构、单页 2400×1400 画布、字体和重新导入检查通过；查看整页渲染，未见新增文字遮挡或越界。该检查不是 PowerPoint 桌面实机验证。图片占位仍待作者实际素材替换，不能作为实验结果图。

## 2026-10-30：提交前清理与归档

按用户要求，将页面预览、修订基线与脚本、LaTeX 辅助文件及 Python 缓存共 225 个文件（179.40 MiB）移至[项目外归档](../../_archive/drivecompose/20261030-pre-push-cleanup/)。移动前后逐文件 SHA-256 一致。正式源稿、四份 PDF、编译结果、来源核验及可编辑图源保留在项目内，四份 PDF 哈希与最终验收记录相同。`paper/.gitignore` 增加审图和修订临时目录规则，`paper/build/CURRENT-OUTPUTS.md` 更新到当前页数；下方历史修订差异链接同步到归档位置。详见[清理记录](../paper/provenance/pre-push-cleanup-20261030.json)。

---

## 2026-10-30：删除符号备注与外部对照行，图五标注改为 GT

本轮按作者最新三项要求做局部修改，采用 nature-polishing 并沿用 CVPR 规范。实际起点为未提交工作区，HEAD 为 `a12af3c150f4f44a8a2a86beed54d315a4bce886`；[本轮基线快照](../../_archive/drivecompose/20261030-display-cleanup/baseline/)保留修改前源文件和 PDF。[本轮完整差异](../../_archive/drivecompose/20261030-display-cleanup/source-changes.diff)只比较该快照与本轮最终文件。

### 位置、实际前后变化与理由

| 位置 | 修改前 | 修改后 | 原因 |
|---|---|---|---|
| 主稿表 1、表 2，图 4、图 5 及补充各基线表 | `STORM† / DGGT† / StreetForward†`，并附适配符号备注 | `STORM / DGGT / StreetForward`，删除相应备注 | 按要求简化方法名及图表阅读信息 |
| 实验比较协议及补充 F | `A shared state adapter ($^\dagger$)`；`Methods marked $^\dagger$ use a common deterministic adapter.` | `A shared state adapter`；`The baselines use a common deterministic state adapter.` | 去掉符号指代，直接描述适配过程 |
| 表 4 车辆组 | `GenAssets-RGB-MV & 23.37 & 0.194 & 94.7\%` | 删除该行；车辆与人体均展示 w/o GCM、w/o CCM、Ours | 按要求调整比较范围，其余数值保持原值 |
| 摘要、引言、实验 4.5、补充 I | 多视图 GenAssets 比较，以及 0.81 dB／1.4 个百分点的衍生结论 | 删除该项比较，保留匹配消融与固定资产复用的论述 | 表格与跨节主张一致 |
| 图 5 图内第一列 | `Recorded-view reference` | `GT` | 按要求统一标签；使用与其他列相同的嵌入字体、字号和基线 |
| 补充 H–I 的四张小表 | 可见率表跨栏，读取诊断与编辑统计延后浮动 | 可见率表单栏，四张表随对应段落放置 | 避免删文后表格积压成单独页面；字体、边距和行距不变 |

**图 5 图注（中英对应）。**

- 英文原文：`\caption{\textbf{Off-trajectory rendering with a 2 m leftward shift.} The first column is the recorded-view reference, followed by STORM$^\dagger$, DGGT$^\dagger$, StreetForward$^\dagger$, and Ours. The reference records the original trajectory.}`
- 英文修改后：`\caption{\textbf{Off-trajectory rendering with a 2 m leftward shift.} Columns show GT, STORM, DGGT, StreetForward, and Ours. GT is the original-trajectory image.}`
- 中文原文：`\caption{\textbf{相机左移 2 m 的离轨渲染。}首列为原轨迹记录参考图，随后为 STORM$^\dagger$、DGGT$^\dagger$、StreetForward$^\dagger$ 与 Ours。首列记录原始轨迹。}`
- 中文修改后：`\caption{\textbf{相机左移 2 m 的离轨渲染。}各列依次为 GT、STORM、DGGT、StreetForward 与 Ours。GT 为原轨迹记录图像。}`

图注用一句话说明 GT 对应原轨迹记录图像，保持原有相机设置。图内仅替换矢量标签，全部结果图像流与基线一致。

**引言结果句（中英对应）。**

- 英文原文：Under shared camera and actor states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering. Paired synthetic tests show better newly visible surfaces than independent completion and a multiview GenAssets variant; real edits reuse the same completed assets across actor states (Sec.~\ref{sec:experiments}).
- 英文修改后：Under shared camera and actor states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering. Paired synthetic tests show better newly visible surfaces than independent completion; real edits reuse the same completed assets across actor states (Sec.~\ref{sec:experiments}).
- 中文原文：在 Waymo 的统一相机与参与者状态条件下，DriveCompose 改善了重建与轨迹外渲染。配对合成测试中，新增可见表面优于独立补全和多视图 GenAssets 变体；真实编辑在不同参与者状态下复用同一份完成资产（第~\ref{sec:experiments} 节）。
- 中文修改后：在 Waymo 的统一相机与参与者状态条件下，DriveCompose 改善了重建与轨迹外渲染。配对合成测试中，新增可见表面优于独立补全；真实编辑在不同参与者状态下复用同一份完成资产（第~\ref{sec:experiments} 节）。

**摘要全文对照。** 仅删除外部车辆比较句，其余表述沿用上一轮。

英文原文：

> Driving simulation and scene editing require reconstructed scenes that support camera and actor motion beyond recorded configurations. Such changes expose unseen surfaces whose geometry and appearance must be completed in the corresponding background, vehicle, or human representation. We present DriveCompose, a framework for compositional generative reconstruction from driving image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for actors, then encoded into component-specific latents. A conditional flow model uses cross-component memory to exchange scene context and jointly complete missing codes. Type-specific Gaussian decoders retain rigid and skeletal bindings, allowing the same completed assets to follow new camera and actor states. Hard latent restoration preserves observed Gaussian parameters, and free-ray constraints control the rendering effects of added content. Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering over state-adapted baselines; cross-component memory adds 0.627 dB full-image PSNR. On newly visible vehicle surfaces, it exceeds a multiview GenAssets variant by 0.81 dB. Real-scene edits achieve 92.78\% success across nine training/generation-seed combinations, demonstrating reuse of fixed completed assets.

英文修改后：

> Driving simulation and scene editing require reconstructed scenes that support camera and actor motion beyond recorded configurations. Such changes expose unseen surfaces whose geometry and appearance must be completed in the corresponding background, vehicle, or human representation. We present DriveCompose, a framework for compositional generative reconstruction from driving image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for actors, then encoded into component-specific latents. A conditional flow model uses cross-component memory to exchange scene context and jointly complete missing codes. Type-specific Gaussian decoders retain rigid and skeletal bindings, allowing the same completed assets to follow new camera and actor states. Hard latent restoration preserves observed Gaussian parameters, and free-ray constraints control the rendering effects of added content. Under shared states on Waymo, DriveCompose improves reconstruction and off-trajectory rendering over state-adapted baselines; cross-component memory adds 0.627 dB full-image PSNR. Real-scene edits achieve 92.78\% success across nine training/generation-seed combinations, demonstrating reuse of fixed completed assets.

中文原文：

> 驾驶仿真与场景编辑需要重建场景支持相机和参与者偏离记录状态后的运动。这些变化会暴露未见表面，其几何与外观需要在对应的背景、车辆或人体表示中完成补全。我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景。视觉特征在背景的世界坐标系和参与者各自的规范坐标系中聚合，再编码为对应组件的潜表示。条件流模型通过跨组件记忆交换场景上下文，联合补全缺失潜码。分类型高斯解码器保留刚体与骨架绑定，使同一份完成资产随新的相机和参与者状态组合。潜码硬恢复保持已见高斯参数，自由射线约束控制新增内容对渲染的影响。在 Waymo 的统一状态条件下，DriveCompose 的重建与轨迹外渲染优于状态适配后的基线，跨组件记忆使全图 PSNR 提高 0.627 dB。在车辆新增可见表面上，它比多视图 GenAssets 变体提高 0.81 dB。真实场景编辑在九组训练／生成种子下取得 92.78\% 成功率，固定完成资产可跨状态复用。

中文修改后：

> 驾驶仿真与场景编辑需要重建场景支持相机和参与者偏离记录状态后的运动。这些变化会暴露未见表面，其几何与外观需要在对应的背景、车辆或人体表示中完成补全。我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景。视觉特征在背景的世界坐标系和参与者各自的规范坐标系中聚合，再编码为对应组件的潜表示。条件流模型通过跨组件记忆交换场景上下文，联合补全缺失潜码。分类型高斯解码器保留刚体与骨架绑定，使同一份完成资产随新的相机和参与者状态组合。潜码硬恢复保持已见高斯参数，自由射线约束控制新增内容对渲染的影响。在 Waymo 的统一状态条件下，DriveCompose 的重建与轨迹外渲染优于状态适配后的基线，跨组件记忆使全图 PSNR 提高 0.627 dB。真实场景编辑在九组训练／生成种子下取得 92.78\% 成功率，固定完成资产可跨状态复用。

### 验收

- 项目检查 72 项通过；本轮定向检查 38 项通过，包含正文／PDF 残留、表格数字、图像流、稳定方法文本、引用、编译时间及页数。
- 英文摘要 163 词；英文技术正文第 8 页结束，中文正文第 7 页结束。主稿总页数分别为 11／10，含声明与参考文献；独立补充分别为 11／9 页。
- 四份最终编译日志无溢出、缺字或未定义引用。已渲染检查主稿及补充图表，重点复核图 5、删行后的表 4 和补充末尾表格。
- 方法、公式、主书目和保留表格结果保持不变。原始作者结果保留在既有记录中，本轮修改只改变论文展示范围及相关语言。
- [本轮来源记录](../paper/provenance/display-cleanup-20261030.json)；[定向验收](../paper/provenance/display-cleanup-20261030-verification.json)。

---

## 2026-10-30：作者补充结果入稿、自然表达终校与 CVPR 2027 样式

本轮依据本聊天中作者对 R1-M1 至 R1-m2 的完整补充，修改英文主稿、中文对照及独立双语补充材料。主流程为 ml-paper-writing，规范层为 cvpr-paper-standard；英文执行 humanizer，中文执行 lieflat-less-ai-tone 的定点终校。科学内容与语言终校分别记录。

本轮从已有未提交工作区开始，HEAD 为 `a12af3c150f4f44a8a2a86beed54d315a4bce886`，实际原文基线以[本轮快照](../../_archive/drivecompose/20261030-author-results-revision/baseline/)为准。[完整逐行差异](../../_archive/drivecompose/20261030-author-results-revision/source-changes.diff)仅比较本轮起点与最终文件，之前各轮的改动保留。新增方法、资源和结果登记于[作者输入记录](../paper/provenance/author-results-followup-20261030.json)。

### 修改位置与证据安排

| 位置 | 原问题 | 本轮修改与作用 |
|---|---|---|
| 摘要、引言、结论 | 新增外部对照及真实编辑统计尚未进入主线 | 用已给出的 0.81 dB 外部车辆比较及九组种子 92.78% 编辑结果表达完成资产的质量与复用 |
| 方法 3.3、3.7；补充 B | 完整网格到目标潜码的路径与训练配置省略 | 明确固定查询布局、确定性表面采样、完整视图特征、129/135/128 维接口、无表面目标、网络规模及四阶段损失和预算 |
| 方法 3.2；补充 D | 中心射线与整个支撑单元的范围容易混淆 | 主实验准确描述中心射线标签；独立报告完整足迹规则及 1,374→19 的误标审计，性能表与掩码审计保持对应 |
| 实验 4.1；补充 F | 原文只说合成数据向基线开放 | 写明实际随机初始化重训、逐方法数据和原生目标、Ours 的额外监督、训练成本、身份归属与规范化适配及适配损失 |
| 实验 4.3；补充 H | 几何表面及重投影有效域定义简略 | 完整写入渲染—TSDF—网格—BVH 流程，保留米制距离；新增共有支持集 MAE 0.022/0.028/0.019 与 58.7% 分母 |
| 实验 4.5、表 4；补充 I | 外部车辆资产对照缺行，单组编辑统计未展示种子和类型差异 | 增加本地 GenAssets-RGB-MV 行，明确为本文适配版本；保留原单组结果，再报告车辆/人体和全部九组统计及场景聚类区间 |
| 表 1；补充 F | 深度表头未标对齐方式 | 表头标为逐帧尺度对齐深度，并给出尺度计算和未对齐指标 |
| 讨论与全篇终校 | 重复提醒、预设反驳与技术内容交织 | 直接陈述方法和结果，保留实际失败条件、比较条件及统计含义；删除重复的预先辩解 |

### 代表性原文与修改后

**目标构造，方法 3.7。**

- 英文原文：`query complete meshes for surface and empty-space targets, and encode them as $\mathbf z_1$ with the fixed codec.`
- 英文修改后：`Complete meshes supply surface samples within each cell. Multiview rendering and the frozen visual encoder produce $\mathbf h_i^{\rm full}$, which the shared type-specific encoder maps to $\mathbf z_{1,i}=E_{k_i}([\mathbf h_i^{\rm full};\mathbf q_i;\boldsymbol\delta_i])$.`
- 中文原文：`查询完整网格的表面与空域，再经固定 codec 得到 $\mathbf z_1$。`
- 中文修改后：`完整网格提供各单元内的表面样本，多视图渲染与冻结视觉编码器得到 $\mathbf h_i^{\rm full}$，再由共享的类型专属编码器映射为 $\mathbf z_{1,i}=E_{k_i}([\mathbf h_i^{\rm full};\mathbf q_i;\boldsymbol\delta_i])$。`
- 原因：补齐从几何监督到共享视觉特征和潜码的实际计算路径。采样细节与全部配置进入附录 B。

**比较数据，实验 4.1。**

- 英文原文：`Synthetic data are available to retrained baselines, and weights remain fixed at test time.`
- 英文修改后：`are retrained from random initialization on the same real logs, synthetic scenes, and complete assets. Each uses its native supervision; Ours also uses cell-empty and template-binding targets.`（主语为 STORM、DGGT 与 StreetForward。）
- 中文原文：`重训练基线可使用合成数据，测试时权重固定。`
- 中文修改后：`均随机初始化，在相同真实日志、合成场景和完整资产上重训。各方法使用自身监督目标，Ours 另用单元空域及模板绑定监督。`（主语同上。）
- 原因：把数据开放意向替换为作者给出的实际训练过程，保留影响比较解释的监督条件。

**重投影结果，实验 4.3。**

- 英文原文：`Error must be read together with coverage (Appendix H).`
- 英文修改后：`On real scenes, Ours reduces common-support RGB reprojection MAE from 0.028 to 0.019 versus w/o CCM and raises coverage from 86.9\% to 92.4\%.`
- 中文原文：`需结合覆盖率解读误差（附录 H）。`
- 中文修改后：`真实场景中，Ours 相对 w/o CCM 将共有支持集 RGB 重投影 MAE 从 0.028 降至 0.019，覆盖率从 86.9\% 增至 92.4\%。`
- 原因：直接给出共有区域的精度与覆盖结果，完整定义和原有自身有效域结果保留在附录 H。

**真实编辑，实验 4.5。**

- 英文原文：`Across 40 real actor edits with training seed 0 and generation seed 7, failures decrease from 16 (w/o GCM) to 7 (w/o CCM) and 3 (Ours), giving 92.5\% success.`
- 英文修改后：`Across nine training/generation-seed combinations, real edits succeed for 177/180 vehicles and 157/180 humans, yielding 92.78\% overall success.`
- 中文原文：`固定训练种子 0、生成种子 7，在 40 次真实参与者编辑中，失败数由 w/o GCM 的 16 次、w/o CCM 的 7 次降至 Ours 的 3 次，成功率为 92.5\%。`
- 中文修改后：`九组训练／生成种子下，真实车辆编辑成功 177／180 次，人体为 157／180 次，总成功率 92.78\%；场景聚类 bootstrap 的 95\% 区间为 85.28--99.17\%。`
- 原因：正文采用作者给出的完整九组统计，原有单组 40 次编辑及各方法结果保留于附录 I，连同盲评规则、类型分组和失败情形一起呈现。

### 表达与格式

终校直接说明输入、运算、约束和已有结果，保留固定照明、给定状态、实际监督和困难编辑条件。英文删去重复的 staged run-up 与 not-X 对照，中文按对应规则作最小修改；[逐处终校记录](../../_archive/drivecompose/20261030-author-results-revision/language-pass.json)保留原因。中文摘要末尾压缩短句，避免孤立短行；补充放大图标题与图保持在同一浮动块。

主稿及补充材料采用从[CVPR 2027 官方作者指南](https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines)下载的 author-kit-CVPR2027-v1-latex 样式，两个 cvpr.sty 与官方下载文件逐字节一致。新样式取消标题区与页眉的 Paper ID；正文页边距、字号和全局行距保持官方设置。图像、固定标题、图 1 前置、方法总览及单栏细节的已有安排沿用本轮基线。

### 最终验收

四份最终 PDF 均重新编译。英文主稿 11 页，其中技术正文及五图四表止于第 8 页，声明及参考文献自第 9 页开始；中文主稿 10 页，正文止于第 7 页。英文／中文补充材料为 12／10 页。项目 72 项检查及本轮 106 项核验通过，最终日志无溢出、缺字或未定义引用。逐页渲染覆盖四份 PDF，目视检查了整体布局，并复查新增公式、表格与末页。

完整结果见[本轮核验](../paper/provenance/author-results-followup-20261030-verification.json)。本轮中间脚本、渲染图与实际起点快照均在项目外 `_archive/drivecompose/20261030-author-results-revision/`，正式 PDF 沿用原路径。

---

## 2026-10-30：图 1 前置至摘要之前（当前首页布局）

按用户要求，仅调整中英文首页布局。图 1 从摘要之后的跨栏浮动图，改为标题区内的固定图，显示顺序为标题、作者占位、图 1、摘要。保留原图、尺寸、图注、编号与科学正文；去掉图注后手动增加的空白，避免英文摘要末行续到第二页。

| 文件 | 原位置 | 新位置 | 原因 |
|---|---|---|---|
| main.tex | Abstract 之后的 figure*，显示于后续页面 | 标题下、Abstract 之前的 minipage | 英文图 1 前置且不再受浮动影响 |
| main_zh.tex | 摘要之后的 figure* | 标题下、摘要之前的 minipage | 中文对照同步 |

调整前快照保存在 pre-research/_archive/drivecompose/20261030-pre-push-cleanup/paper/build/revision-20261030/teaser-before-abstract-baseline/，逐行对照见[本次布局差异](../../_archive/drivecompose/20261030-pre-push-cleanup/paper/build/revision-20261030/teaser-before-abstract.diff)。两版已编译并目视检查：首页图 1 均位于摘要之前，摘要完整留在首页，英文正文仍止于第 8 页；日志无溢出、缺字或未定义引用。本次没有修改图像或实验值；验收见[布局记录](../paper/provenance/teaser-before-abstract-20261030.json)。

---

## 2026-10-30 后续图件调整（当前布局）

用户要求将原总览图加回方法处，并缩小细节图。本次只改双语图件位置、大小、图注和必要引用，保留实验数值与科学正文。

| 位置 | 调整前 | 调整后 | 原因 |
|---|---|---|---|
| 方法总览 / DriveCompose overview | 位于补充 L，正文 overview 标签指向概念图 | 原图恢复到方法开头，正文图 2；英文实测第 4 页 | 按用户要求在方法处提供完整流程 |
| 联合补全细节 / Joint latent completion | 0.86 倍正文宽的跨栏图 | 单栏图 3，宽约 83.3 mm；补充 L 保留 0.86 倍正文宽的放大图 | 缩小细节图，同时保留完整可读版本 |
| 后续图号 | 动态结果图 3、离轨结果图 4 | 动态结果图 4、离轨结果图 5 | 自动顺延并同步中英文引用；资产换姿结果图仍未加入 |
| 声明与检查 | 说明补充总览，检查旧图序 | 声明补充放大图，检查 overview 在方法与 detail 在补充 | 与实际 PDF 一致 |

调整前快照位于 pre-research/_archive/drivecompose/20261030-pre-push-cleanup/paper/build/revision-20261030/layout-followup-baseline/。源 PNG 的字节和实验图像素均未更改；未改正文几何、字号或行距。最终英文主稿正文及五图四表止于第 8 页，总计 11 页；中文主稿 10 页。英文／中文补充为 8／7 页。四份 PDF 编译成功，71 项稿件检查与 53 项本轮核验通过。方法总览、单栏细节及补充放大图已目视检查，详见[验证记录](../paper/provenance/review-revision-20261030-verification.json)。

---

## 2026-10-30：审稿问题修正、作者结果回填与八页正文
基线提交为 a12af3c150f4f44a8a2a86beed54d315a4bce886。修订开始时除上一轮只读审图缓存外工作区干净。原始源稿、四份 PDF 和离轨图保存在 pre-research/_archive/drivecompose/20261030-pre-push-cleanup/paper/build/revision-20261030/baseline/。本轮未提交、推送或运行训练/评测。
新增事实与结果来自[作者原始要求](../paper/provenance/review-revision-20261030-author-source.txt)，采用作者汇总证据等级；未将转录和算术核对描述为原始运行核验。[机器可读来源](../paper/provenance/review-revision-20261030.json)保留全部 16 张原始表。
### 范围与取舍
| 位置 | 实际改动 | 原因及去向 |
|---|---|---|
| 双语摘要、方法与引言 | 明确统一状态、有限支撑完整目标、有效目标规则及参数保持边界；闭环改为应用方向 | 对应 R-M1、R-M2、R-M3、R-M5；标题保留 |
| 双语实验 | 保留原主表均值，主比较基线标明统一状态适配；加入资产编辑、隐藏区域、CCM 分组、观测保持及效率结论 | 用户新增汇总；未补造近邻排名 |
| 双语补充 A/B/F–K | 补齐来源、监督、插值／外推、完整 SD、失败分母、上下文诊断、射线阈值及计时明细 | 正文保留核心条件，完整表格可定位 |
| 原图 1/2 | 用原概念对照图的观测缺失面板与原 teaser 组合为一张 PDF | 复用原图像，无生成新实验图，保留示意身份 |
| 原图 3/4 | 原展开总览迁入附录 L；CCM 机制图保留为正文图 2 | 去除重复概念说明，保留机制与完整流程 |
| 动态／离轨结果 | 顺延为图 3/4；离轨首列 GT 改为 Recorded-view reference | PDF 原图像流逐个哈希一致，仅编辑标题文本 |
| 图 5 | 按用户后续明确指令暂不放入 | 不以示意图替代真实换姿结果，定量表保留 |
| 引言、相关工作、方法、结论 | 删除重复流程说明和重复自我比较，精简长句 | 技术核心、九个公式块和 52 条书目保留；训练表迁入 B，输入敏感性表迁入 G |
| LLM Usage Statement | 置于正文之后、参考文献之前 | 披露本会话及项目记录中的 Codex、Image Gen 用途 |
| 校验入口 | 更新旧图序及消融表位置假设，继续检查原均值及跨表 T=8 一致性 | 新布局下 67 项稿件检查；新增作者表数值、算术、像素与页界审计另存验证 JSON |

### 代表性中英前后对照

**摘要中的观测保持**

区分高斯参数的结构保证与新增遮挡造成的经验渲染变化。

英文原文

> Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces.

英文修改后

> Hard latent restoration preserves observed Gaussian parameters, while free-ray constraints limit rendering changes caused by added content.

中文原文

> 补全过程受输入观测约束，以保持已观测表面的几何与外观。

中文修改后

> 潜码硬恢复保持已见高斯参数，自由射线约束限制新增内容引起的渲染变化。

**完整目标与损失选择器**

解释为何 s_i=0 不能使流插值中的无效目标变得有效；完整规则仍使用原公式。

英文原文

> Complete scene or asset examples supply $\mathbf z_1$ at the unknown queries, while $s_i$ selects their contribution to the training loss (Sec.~\ref{sec:training}).

英文修改后

> Every unknown query must have a valid target because Eq.~\ref{eq:flow-path} uses $\mathbf z_{1,i}$ even when $s_i=0$. Samples failing this condition are excluded from prior learning; $s_i$ only selects loss terms among valid targets (Sec.~\ref{sec:training}).

中文原文

> 完整场景或资产样本为未知查询提供目标潜码 $\mathbf z_1$，$s_i$ 则选择其对训练损失的贡献（第~\ref{sec:training} 节）。

中文修改后

> 每个未知查询都必须具有有效目标，因为即使 $s_i=0$，式~\ref{eq:flow-path} 仍使用 $\mathbf z_{1,i}$。不满足这一条件的样本不参与先验学习；$s_i$ 仅在有效目标中选择损失项（第~\ref{sec:training} 节）。

**离轨图参考身份**

原轨迹参考与偏移相机不配对，标签和图注同时更正，保留全部实验像素。

英文原文

> Columns, from left to right, show the reference image (GT), STORM, DGGT, StreetForward, and DriveCompose (Ours).

英文修改后

> The first column is the recorded-view reference, followed by STORM$^\dagger$, DGGT$^\dagger$, StreetForward$^\dagger$, and Ours. The reference is captured on the original trajectory, not at the shifted camera.

中文原文

>   \caption{\textbf{动态场景重建的定性对比。}每行展示一个样例，从左至右依次为真实图像、DGGT、STORM、StreetForward 和 DriveCompose（Ours）。样例覆盖行人、交通车辆与城市背景，用于比较参与者轮廓、车辆边界以及道路和建筑结构。}

中文修改后

> 首列为原轨迹记录参考图，随后为 STORM$^\dagger$、DGGT$^\dagger$、StreetForward$^\dagger$ 与 Ours。首列不与平移后的相机配对。

完整逐行对照见 [source-changes.diff](../../_archive/drivecompose/20261030-pre-push-cleanup/paper/build/revision-20261030/source-changes.diff)。

### 验证与边界

正文页数按结论全文末尾 sec:main-text-end 和全部正文图表标签检查，避免仅看标题漏判续页。编译与数值、像素核验详情见[验证记录](../paper/provenance/review-revision-20261030-verification.json)。最终英文主稿 11 页，全部技术正文及四图四表止于第 8 页，LLM Usage Statement 与参考文献从第 9 页开始；中文主稿 10 页，正文止于第 7 页。英文补充 8 页，中文补充 7 页。四份 PDF 编译成功，日志无未定义引用、缺字或溢出。67 项既有稿件检查和 53 项本轮来源/算术/页界/图像核验通过；逐页缩略图及关键页高清检查通过。未改变主文字号、页边距或行距。

作者侧仍待追溯的材料包括原始运行、checkpoint、数据清单和未提供的训练超参数；R-M6 协议定位已由作者补充并写入双语正文和补充 H：可见率分组共享 100 个合成场景，读取范围在 202 个 Waymo 窗口上对同一 Ours checkpoint 施加推理遮罩；记录见[补充来源](../paper/provenance/review-revision-20261030-clarification.txt)。论文文字依据本轮作者汇总，不据缺少原始材料推断实验未实施。

---

## 2026-10-29：补回图注与 Abstract 之间的空白

本轮从 `a12af3c150f4f44a8a2a86beed54d315a4bce886` 上已完成标题下间距修正的未提交工作区开始。真实原文和测量保存在 `paper/build/abstract-revision/teaser-caption-spacing-baseline.json`。仅改英文入口一行，不计入此前的摘要选取或排版修改。

| 位置 | 原文／修改前 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| teaser 图注后、两栏标题前 | `\end{minipage}\par` 后无额外空白；图注至 Abstract 实测约 1.80 pt | 加入 `\vspace{8pt}`；实测约 9.77 pt | 按用户反馈补回图注与标题之间的分隔，避免紧贴；不恢复此前 Abstract 标题下方的大空白。 |

Abstract 标题与首行的实测间距保持约 7.56 pt。英文摘要仍完整位于左栏，引言从右栏开始。中英文摘要源文件和中文 PDF 哈希与本轮基线一致，中文未重新编译。字体、字号、正文行距、页边距和图片大小未变。

**验证：** `tools/build.py --language en` 编译成功，退出码 0，正式英文 PDF 本轮实际更新，SHA256 为 `e5e5f86cc81c0d55db254007882b116e99304c099a63c1a7ae2afcf1e3c55f78`。已渲染检查第 1、2 页，未见新增重叠或裁切；最终日志未报告警告、未定义引用、缺字或溢出。PDF 仍为 12 页，正文与参考文献分界在第 10 页。本轮核验见 `paper/build/abstract-revision/teaser-caption-spacing-check.json`。

## 2026-10-29：修正 Abstract 标题下方空白

本轮基于 `a12af3c150f4f44a8a2a86beed54d315a4bce886` 上已完成摘要选取及孤词修复的未提交工作区，只调整英文入口的首页排版。真实原文与摘要源文件、PDF 哈希保存在 `paper/build/abstract-revision/abstract-heading-baseline.json`，不将此前摘要文字修改计入本轮。

| 位置 | 原文／原布局 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| 英文 Abstract 标题后 | 继承 `cvpr.sty` 中的 `\vspace*{12pt}`，标题与首行实际空白约 21.99 pt | 在英文 `main.tex` 中局部替换为 `\vspace*{6pt}`，实际空白约 7.56 pt | 收紧截图指出的标题下方大空白，保留清楚的标题与正文分隔；共享 CVPR 样式、字号、正文行距和页边距不变。 |
| 英文摘要结束后 | 直接进入后续浮动图及引言，让页面分配剩余高度 | `\par\vfill\newpage`，把本栏剩余弹性空白放在摘要末尾，并切换到右栏开始引言 | 明确保持首页左栏摘要、右栏引言的布局，避免剩余高度集中出现在标题与正文之间；双栏模式下这里切换一栏，没有新增物理页面。 |

本轮没有学术内容修改。中英文摘要源文件与本轮真实基线的 SHA256 相同，中文 PDF 哈希也相同；中文未重新编译。

**验证：** 通过现有 `tools/build.py --language en` 成功更新正式英文 `paper/build/en/main.pdf`，退出码 0，`pdf_written_this_run=true`。最终 PDF SHA256 为 `353aeccdf4f0a703630b97d7e6739f2677ff51c55e417f3df767e26ca2fca964`。已重新渲染并查看第 1、2 页，摘要完整位于左栏，标题下方间距正常，引言从右栏顶部开始，图件没有新增重叠或裁切。最终日志未报告警告、未定义引用、缺字或溢出。总页数仍为 12，正文与参考文献分界仍在第 10 页。测量及哈希核验保存在 `paper/build/abstract-revision/abstract-heading-check.json`。

## 2026-10-29：修复首页摘要末行跨栏

本轮从 `a12af3c150f4f44a8a2a86beed54d315a4bce886` 上已完成逐句选取的未提交工作区开始。真实修改前主文件、英文摘要及 PDF 哈希保存在 `paper/build/abstract-revision/layout-baseline.json`，中文摘要的单词同步前原文也保存在同一基线；不把先前摘要选取算作本轮修改。

| 位置 | 原文 | 修改后 | 原因及改善 |
| --- | --- | --- | --- |
| 英文入口 teaser 图注后 | `\end{minipage}\par` 后另有 `\vspace{\baselineskip}` | 仅保留 `\end{minipage}\par` | 删除自定义的额外一行空白，保持模板字号、页边距和行距；配合下面的去重后，摘要完整留在左栏。 |
| 英文摘要末句 | allowing the same completed assets to be composed and rendered | allowing the same assets to be composed and rendered | 用户授权调整一个词，删除重复的 completed；同句前文 completed latents 已说明资产来自补全潜码。摘要由 142 词变为 141 词，没有改变机制或能力主张。 |
| 对应中文末句 | 使同一组补全资产能够在不同相机与参与者状态下组合和渲染场景。 | 使同一组资产能够在不同相机与参与者状态下组合和渲染场景。 | 与英文同步去掉重复限定，保留同一组资产复用、组合和渲染的含义；中文未重新编译。 |

仅删除额外空白不足以消除跨栏。曾检查的局部分行与纵向对齐设置没有保留；最终没有新增 looseness、tolerance、raggedbottom 或 flushbottom 设置，没有缩小图件或改写其余稳定句子。

**验证：** 现有 `tools/build.py --language en` 成功更新正式英文 `paper/build/en/main.pdf`，退出码 0 且 `pdf_written_this_run=true`，SHA256 为 `6e2422ba3611eb1ef4f035a478528a038f7354cc045acf012e56cfff00dc9d93`。最终日志未报告警告、未定义引用、缺字或溢出。已渲染并检查首页和第二页，首页摘要末句完整位于左栏，引言标题位于右栏顶部；原先右栏顶部孤立的 states. 已消除。PDF 仍为 12 页，正文与参考文献分界仍在第 10 页。内置编译预览仍受 20 MiB 限制，不影响本地正式构建结果；未重新编译中文。

## 2026-10-29：逐句确认摘要选取

本轮基线为拉取后的 `a12af3c150f4f44a8a2a86beed54d315a4bce886`。动笔前两份摘要没有未提交修改；真实原文另存于 `paper/build/abstract-revision/agreed-selection-baseline.json`。仅修改英文摘要与对应中文摘要，并更新本记录；不改引言、贡献、方法或实验。

### 局部修改与理由

| 位置 | 原文 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 英文摘要开头 | Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, rigid asset, or human. | Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. | 用户选用拉取前的简洁背景句，随后直接引入框架；删除的状态变化动机在当前引言第一段已有解释，本轮未执行内容迁移。 |
| 中文摘要开头 | 驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、刚体或人体。 | 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。 | 同步英文背景句，保留局部观测、完整性、可控性与应用目的。 |
| 英文摘要结尾 | Type-specific decoders convert the completed latents into Gaussian components whose rigid and skeletal bindings support composition under different camera and actor states. | Type-specific decoders convert the completed latents into Gaussian components with rigid and skeletal bindings, allowing the same completed assets to be composed and rendered under different camera and actor states. | 保留解码与绑定机制，并明确同一组补全资产跨状态复用、组合与渲染；未新增实验效果。 |
| 中文摘要结尾 | 分类型解码器将补全潜码转换为高斯组件，其刚体与骨架绑定支持在不同相机和参与者状态下组合场景。 | 分类型解码器将补全潜码转换为具有刚体和骨架绑定的高斯组件，使同一组补全资产能够在不同相机与参与者状态下组合和渲染场景。 | 同步英文的机制与复用能力。 |

**明确保留项：** 框架介绍；世界/规范坐标系中的视觉特征聚合与组件特定潜表示；当前条件生成模型与 flow matching / cross-component memory 句；当前短观测约束句；当前 Waymo 结果句。不恢复历史 20.5% RGB MAE 消融数字，不改当前指标合同。

术语沿用：rigid assets（刚体资产）、canonical frames（规范坐标系）、component-specific latent representations（组件特定的潜表示）、cross-component memory（跨组件记忆）、rigid and skeletal bindings（刚体与骨架绑定）。用户逐句确认的措辞优先，不因技能的通用句长建议另行拆句。

### 英文全文前后对照

原文：

> Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, rigid asset, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for rigid assets and humans, then encoded into component-specific latent representations. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Type-specific decoders convert the completed latents into Gaussian components whose rigid and skeletal bindings support composition under different camera and actor states.

修改后：

> Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for rigid assets and humans, then encoded into component-specific latent representations. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Type-specific decoders convert the completed latents into Gaussian components with rigid and skeletal bindings, allowing the same completed assets to be composed and rendered under different camera and actor states.

### 中文全文前后对照

原文：

> 驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、刚体或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。视觉特征在背景的世界坐标系与刚体、人体各自的规范坐标系中聚合，再编码为对应组件的潜表示。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。分类型解码器将补全潜码转换为高斯组件，其刚体与骨架绑定支持在不同相机和参与者状态下组合场景。

修改后：

> 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。视觉特征在背景的世界坐标系与刚体、人体各自的规范坐标系中聚合，再编码为对应组件的潜表示。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。分类型解码器将补全潜码转换为具有刚体和骨架绑定的高斯组件，使同一组补全资产能够在不同相机与参与者状态下组合和渲染场景。

### 检查

英文按空白分词由 162 词变为 142 词，低于仓库 150–250 词的目标范围。本轮按用户逐项选定内容落地，不为达到目标机械补句。数字、引用、公式及实验条件未变。已调用内置 compile_latex_document：首次自动选择 main_zh.tex，随后显式指定 main.tex；两次均返回 compile-failed / The LaTeX preview exceeds the 20 MiB limit。无法据此确认本轮编译成功，也未完成新预览的页面与正文终止页核验。本轮保留当前编辑器，没有切换标签或另行导出 PDF。git diff --check 通过；已按真实基线核对双语仅开头与结尾有改动。

后续英文构建：用户要求仅编译英文，已通过现有 tools/build.py --language en 成功更新 paper/build/en/main.pdf；编译退出码 0，pdf_written_this_run=true，SHA256 为 b66a1af95f6d7f9930e5eb4c8adbe11b4a126d6b683ce1cd77e767c2d33869f5。最终 main.log 未发现编译警告、未定义引用、缺字或 Overfull/Underfull。PDF 共 12 页，结论与参考文献分界在第 10 页。已检查首页和第二页：摘要末词 states. 单独延续至右栏顶部；本轮按编译范围保留已确认措辞和现有排版，未修改源文。中文未重新编译。

## 2026-10-29：归档临时文件并整合远端更新

本轮用于清理、提交和推送。清理后的本地基线为 `fae4966`，远端为 `4403f99`；两边完整历史均保留。

| 冲突位置 | 本地当前内容 | 远端内容 | 合并结果及原因 |
| --- | --- | --- | --- |
| 双语摘要与引言结果句 | 当前刚体/潜表示叙述，已删除旧自定义指标结论 | 摘要含 RGB MAE 降低 20.5%，引言仍描述该旧指标 | 采用本地当前主张与指标合同，避免恢复已弃用结论；远端引言第二、三段的兼容修改由 Git 保留。 |
| 双语入口 | 三张方法图，概念对照使用 `fig:teaser` | 新增标题区 teaser，也使用 `fig:teaser` | 两组图均保留；标题区图改为唯一标签 `fig:title-teaser`，原概念对照引用不变。 |
| 方法节开头 | 与三图一致的当前完整流程说明 | 仅将旧流程图引用改为 `fig:overview` | 保留本地当前说明，其引用已经是 `fig:overview`。 |
| 本文件 | 本地方法、引文及消融记录 | 远端 teaser、摘要和引言记录 | 合并两组记录，保留各轮来源。 |

临时脚本、构建快照、审图页图、候选/重复图片与缓存迁入项目外 `_archive/drivecompose/20261029-pre-push-cleanup/`。迁移按 SHA256 核对，历史来源 JSON 原文保留，通过[迁移记录](../paper/provenance/pre-push-cleanup-20261029.json)解析旧路径。正式图片像素、当前实验值和代码实现不因合并改变。

14 项代码测试通过；3 项 PyTorch 可选网络测试因缺少依赖跳过。63 项稿件检查通过。两版主稿重新编译成功，日志无未定义引用、缺字、重复标签或溢出；已查看全部页面缩略图及高清首页。英文总计 12 页，正文和参考文献分界在第 10 页；中文共 11 页，分界在第 8 页。英文仍超出当前正文页数目标，本轮不扩大到内容压缩。

## 2026-10-29：三图入稿与整篇排版检查

用户授权将三张 Image Gen 预览图放入论文。以本轮开始时的未提交工作区为基线，完成中英文图件、图注及引用的必要修改，并重新编译正式 PDF。基线提交为 `e98697e09af130895fe14f70fbc840571da28a0d`，真实修改前文件保存在 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/three-figure-layout/baseline/`，不将此前工作区改动计入本轮。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 主文件图1 | 一张完整流程图，图注按 (a)(b)(c) 三阶段解释 | 图1替换为上下对照图；英文题注 “From observed surfaces to compositional scene assets.”，中文“从观测表面到可组合场景资产” | 匹配用户选定的新图1及概念对照内容 |
| 引言流程引用 | `Figure~\ref{fig:teaser} follows the reconstruction pipeline.`／“图~\ref{fig:teaser} 展示完整重建流程。” | `Figure~\ref{fig:overview} follows the reconstruction pipeline.`／“图~\ref{fig:overview} 展示完整重建流程。” | 完整框架现为图2；引言首段另引用图1说明未见区域 |
| 方法 §3.5 | GCM 起始句只解释结构，无机制图 | 起始句加入图3引用，并在对应位置声明联合补全图 | 连接 CCM 与约束采样正文和图3 |
| 实验图号 | 动态重建图2、视图外推图3 | 自动顺延为图4、图5 | 三张方法图占用前三号；实验图文件、图注、数值及分析原文不变 |
| 中文图件浮动 | 首轮图1与图2同时挤在第2页 | 每页最多一张页顶跨栏图，图1/2分置第2/3页 | 保持图文阅读节奏；未缩正文或修改模板几何 |

两版图1、图2宽 174.63 mm；图3宽 150.18 mm、高 134.22 mm，以跨栏方式居中，保留细节可读尺度。三张图均为用户选定 PNG 的原字节副本，无代码重绘。场景与资产插图的机制示意身份写入图注。

**最终排版结果：** 英文总计 12 页，正文与图表止于第 9 页，参考文献从第 9 页下部开始；中文总计 10 页，正文止于第 8 页，参考文献从第 8 页开始。两版前三图都在第 2、3、5 页。两份既有补充材料各 3 页，已检查，未改写。

**检查：** 正式 PDF 编译成功；最终日志没有 Overfull/Underfull、缺字、未定义引用或警告。逐页渲染检查未发现裁切、图文重叠、缺图或意外空白页。程序检查页外文字与文字覆盖图片均为 0；63 项现有稿件检查通过，52 条书目、9 个双语方法公式块保持一致。实验源文件、书目、共享 preamble 和字体设置与本轮基线逐字节一致。

**未解决的篇幅问题：** 英文技术正文占 9 页，尚未符合 [CVPR 2027 的 8 页正文限制](https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines)。新增图件后的实质篇幅需要在后续内容压缩中处理；本轮未通过删减方法、实验、缩字号、改页边距或负间距规避限制。不将当前稿宣称为可直接提交版。

完整本轮差异见 [source-changes.diff](../../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/three-figure-layout/source-changes.diff)，检查数据见 [核验记录](../paper/provenance/three-figure-layout-verification-20261029.json)，所有页图见 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/three-figure-layout/final/review/`。


# 当前改动：压缩 §3.2 与 §3.5

更新：2026-10-25。仅修改中英文主稿 §3.2、§3.5，新增双语补充材料 C/D。图示仅提出建议，本轮未改 Figure 1，也未增加正文图。其他主稿章节（含上一轮 §3.6）保持本轮起点原文。

基线：HEAD `ee5b6cb` 上的本轮未提交工作区。真实原文保存在 `paper/build/revision-baseline.json` 的 `composition_frontend_before`，英文 PDF 哈希、逐页文本和位置测量保存在 `composition_frontend_pdf_before`。Git 未暂存差异还包含此前 §3.6 的改动；本轮范围以此记录及[本轮彩色左右对照](../../_archive/drivecompose/20261026-tracked-intermediates/paper/build/method-revision-diff.html)为准。

## 1. 代表性前后对照与理由

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| §3.2 共享编码 | 两段逐项解释 patch/三种嵌入、两级 Transformer、预测头和身份槽实现 | 一段交代预测内容、持久身份与逐帧状态的分离；结构细节见附录 D | 正文保留聚合需要什么信息，前端实现完整保留在 D |
| §3.2 自由空间 | 保守判定文字后列出原公式 (6)，另复述筛选排除深度/身份冲突 | 保留整单元位于观测表面之前的条件、三种互斥掩码和天空例外；不等式见 D 的 (S12) | 精确公式有明确去向；删去的复述已由前文有效性条件说明，原句也保留在 D |
| §3.5 状态驱动渲染 | 标准刚体公式 (13)、完整蒙皮/协方差/外观方向变换、外部动力学递推 (15) | 用一句话说明刚体放置与人体蒙皮，保留装配渲染关系和固定场景复用 | 变换展开及后端细节完整保留在 C；正文集中解释场景内容与状态的关系 |
| §3.5 观测检查 | 已见码固定后仍可能发生新遮挡；候选/observed-only 双渲染；正退化与各接受条件 | **整段及公式原样保留**，只自动重编号 | 这是约束机制的核心逻辑，不为了节省篇幅弱化它 |

**英文编码段修改后（中文逐句同步）：**

> The Driving Log Encoder uses transformer features to predict camera-axis depth, normals, confidence, semantics, and instance assignments from the calibrated image log. Trajectory-level identity slots separate persistent identity, dimensions, and human shape from frame-dependent root poses and joint rotations. Architectural details and state parameterization are given in Appendix D of the supplementary material.

此展示省略引用标记便于阅读，源文保留 ViT/Transformer 引用；附录 D 的两条书目从主书目逐字提取。

**装配段新增的替代说明：**

> Vehicles are placed by rigid transforms and humans by skinning; standard transformations and backend details are given in Appendix C of the supplementary material.

> 车辆通过刚体变换放置，人体通过蒙皮变换放置；标准变换和后端细节见补充材料附录 C。

完整原文和修改后见下方全文对照。C/D 保留原节完整说明以便独立阅读；核心定义在正文中同时保留。没有增加新机制、新实验或新能力主张。

## 2. 公式与跨文档依赖

| 内容 | 修改前主稿编号 | 当前去向 |
| --- | --- | --- |
| 查询运动放置 | (3) | 主稿 (3)，原式保留；D 中另有 (S9) |
| 聚合权重及特征 | (4)–(5) | 主稿 (4)–(5)，原式保留 |
| 自由空间单元判定 | (6) | D 中 (S12) |
| 刚体中心/协方差 | (13) | C 中 (S5) |
| 装配渲染 | (14) | 主稿 (12)，原关系保留；C 中 (S6) |
| 外部策略与动力学递推 | (15) | C 中 (S7) |
| 观测正退化 | (16) | 主稿 (13)，原式保留；C 中 (S8) |

主稿 flow 路径/目标自动变为 (9)/(10)，同步修正了补充 B 中对主稿的两个显式引用；除此之外 B 的内容未改。主稿实验里的 Obs-Reg 通过已有标签自动指向 (13)，未改实验源文。补充 A 及其表格数据不变。

## 3. 英文篇幅变化

| 项目 | 本轮前 | 本轮后 | 变化 |
| --- | ---: | ---: | ---: |
| §3.2 | 约 0.72 页 | 约 0.60 页 | −0.12 |
| §3.5 | 约 0.51 页 | 约 0.36 页 | −0.15 |
| Method 整体 | 约 2.97 页 | 约 2.69 页 | −0.28 |
| 正文流式占用 | 约 8.64 页 | 约 8.41 页 | −0.24 |
| 正文结束位置 | 第 9 页右栏 | 第 9 页左栏 | 仍超 8 页 |
| 英文主稿总页数（含参考文献） | 12 | 11 | −1 |
| 英文补充材料总页数 | 2 | 3 | +1 |

仍用双栏、每栏 648 pt 的页当量口径；不同小节边界及图表浮动使局部节省与整稿收益不完全相等。不能把 PDF 总页数减少 1 页说成正文节省 1 页。表 4、局限与结论仍在第 9 页，距离正文 8 页约有 0.41 页内容空间及排版余量需要处理，本轮未继续删减。

## 4. 图示建议（未修改论文图件）

检查了现有 Figure 1：它已经覆盖视觉恢复、联合补全、解码与复用。建议保留总体图的任务，优先增强两个具体机制的可读性：

1. **§3.2 规范聚合：** 用同一辆车的两帧位姿与同一规范查询，画出查询随资产放置、投影取样、按深度/身份筛选，再聚合回同一规范查询。用三类标记说明 observed/free/unknown，突出 free 需要整个单元位于可靠观测表面前方，而非“没看到就是自由空间”。可作为 Figure 1(a) 的局部放大或替换其笼统的聚合方框。
2. **§3.5 新遮挡与检查：** 对照“仅已见内容”和“加上生成表面后的候选”，让读者看到同一原始相机下新增表面如何挡住已见内容，再指向正退化检查与接受/拒绝。该示意解释检查动机，不能画成已经验证的闭环或任意新状态安全性。

第一项优先；第二项可做紧凑 inset。两者都应替换对应的解释负担，避免再增加一张重复总览的大图。刚体矩阵和两级 Transformer 框图更适合补充材料，不应占用核心机制的图示预算。具体构图草案已记入工作流，尚未插图或删改配套正文。

## 5. 核验与保留项

- 两版主稿和两版补充材料均重新编译成功；最终日志无未定义引用、缺字或 Overfull 警告。
- 逐页检查英文受影响第 3–9 页、中文目标第 3–4 页，以及两版补充材料全部 3 页；行号、公式和图表无覆盖或裁切。
- §3.1、§3.3、§3.4、§3.6 及其他主稿章节逐字比对保持原样；§3.2 查询支撑定义、运动放置与聚合公式保留，§3.5 检查段落完整保留。
- 附录 C/D 与本轮对应原节逐字核对通过，仅 section 标题和标签改变；补充 B 仅更新主稿公式号。
- 未改模板字号、页边距、行距和图件；未提交或推送 GitHub。

## 6. 两节中英文全文前后对照

### English §3.2

**修改前**

```latex
\subsection{Visual recovery and canonical aggregation}
\label{sec:queries}

\paragraph{Shared visual encoding.}

The Driving Log Encoder uses patch tokenization~\cite{dosovitskiy2021vit} and transformer attention~\cite{vaswani2017attention}, with image-position, camera-calibration, and time embeddings. Within-image attention extracts spatial features. A second transformer processes pooled image summaries across views and timestamps, and returns the resulting context to the patch features. Geometry heads predict camera-axis depth, normals, confidence, semantics, and instance assignments. The confidence determines which predictions can contribute surface evidence.

Learned actor queries attend to all image tokens to form trajectory-level identity slots. Each slot then reads the features at an individual timestamp to estimate its state. This separates persistent identity, dimensions, and human shape from frame-dependent root poses and joint rotations. Root poses are predicted in the rig frame and mapped to world coordinates with $\mathbf T^w_r(t)$. A human shape code selects an identity-specific template with fixed canonical support, skeleton topology, and binding. Slot capacity bounds the number of represented actors.

\paragraph{Query supports.}

A query stores canonical position $\mathbf q_i$, cell scale $\boldsymbol\delta_i$, type $k_i$, local attention group $g_i$, and reference-world coordinate $\mathbf q_i^w$. Reliable depth samples provide surface anchors. Background anchors are combined with a finite world grid; vehicle anchors are motion-normalized and combined with a grid in the local bounding volume. Human queries lie on the canonical template surface. Sky queries are unit directions grouped by cubemap face. These supports provide explicit locations for both observed and missing content.

The layout remains fixed during completion. We obtain $\mathbf q_i^w$ by placing the query in the first input configuration, including skinning for humans. Canonical coordinates identify the content within its component; reference-world coordinates let the generator relate that component to its surroundings.

\paragraph{Motion-aware evidence aggregation.}

For each observation, we place the canonical query at the corresponding actor state:

\begin{equation}
\mathbf p_i(t)=
\begin{cases}
\mathbf q_i,& k_i=\mathrm{background},\\
\operatorname{xyz}(\mathbf T^w_a(t)\bar{\mathbf q}_i),& k_i=\mathrm{vehicle},\\
\operatorname{xyz}(\mathbf T^w_h(t)\mathbf A_i(t)\bar{\mathbf q}_i),& k_i=\mathrm{human}.
\end{cases}
\label{eq:query-placement}
\end{equation}

Here $\bar{\mathbf q}_i$ is homogeneous, $\operatorname{xyz}$ extracts Euclidean coordinates, and $\mathbf A_i(t)$ is the weighted skinning transform. Projection into a camera gives depth $z_{i,t,v}$ and sampled feature, depth, and confidence $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$. With tolerance $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$, define $r=(d-z)/\eta$. A surface observation must lie inside the image, have valid depth and sufficient confidence, match the query's instance, and satisfy $|r|\leq1$. Background queries additionally require static-background semantics. Let $a_{i,t,v}$ denote this validity test. We aggregate

\begin{align}
w_{i,t,v}&=a_{i,t,v}c_{i,t,v}\exp(-r_{i,t,v}^2/2),\\
\mathbf h_i&=\frac{\sum_{t,v}w_{i,t,v}[\boldsymbol\phi_{i,t,v};r_{i,t,v}]}
{\max(\varepsilon,\sum_{t,v}w_{i,t,v})}.
\label{eq:aggregation}
\end{align}

The query confidence is the maximum over accepted observations. The test excludes observations whose depth or instance identity disagrees with the query. A reliable ray votes for free space only when the entire support cell is in front of the measured surface:

\begin{equation}
z_{i,t,v}+\tfrac12\|\boldsymbol\delta_i\|_2<d_{i,t,v}-\eta.
\label{eq:free-space}
\end{equation}

Positive accumulated observation weight marks a query as observed. Otherwise, sufficient free-space votes mark it free, and the remainder is unknown. The masks $m_i$, $f_i$, and $u_i$ are mutually exclusive and satisfy $m_i+f_i+u_i=1$. Sky projection uses camera rotation alone, reliable sky semantics, and zero depth residual; sky queries receive no free-space votes.
```

**修改后**

```latex
\subsection{Visual recovery and canonical aggregation}
\label{sec:queries}

\paragraph{Shared visual encoding.}

The Driving Log Encoder uses transformer features~\cite{dosovitskiy2021vit,vaswani2017attention} to predict camera-axis depth, normals, confidence, semantics, and instance assignments from the calibrated image log. Trajectory-level identity slots separate persistent identity, dimensions, and human shape from frame-dependent root poses and joint rotations. Architectural details and state parameterization are given in Appendix D of the supplementary material.

\paragraph{Query supports.}

A query stores canonical position $\mathbf q_i$, cell scale $\boldsymbol\delta_i$, type $k_i$, local attention group $g_i$, and reference-world coordinate $\mathbf q_i^w$. Reliable depth samples provide surface anchors. Background anchors are combined with a finite world grid; vehicle anchors are motion-normalized and combined with a grid in the local bounding volume. Human queries lie on the canonical template surface. Sky queries are unit directions grouped by cubemap face. These supports provide explicit locations for both observed and missing content.

The layout remains fixed during completion. We obtain $\mathbf q_i^w$ by placing the query in the first input configuration, including skinning for humans. Canonical coordinates identify the content within its component; reference-world coordinates let the generator relate that component to its surroundings.

\paragraph{Motion-aware evidence aggregation.}

For each observation, we place the canonical query at the corresponding actor state:

\begin{equation}
\mathbf p_i(t)=
\begin{cases}
\mathbf q_i,& k_i=\mathrm{background},\\
\operatorname{xyz}(\mathbf T^w_a(t)\bar{\mathbf q}_i),& k_i=\mathrm{vehicle},\\
\operatorname{xyz}(\mathbf T^w_h(t)\mathbf A_i(t)\bar{\mathbf q}_i),& k_i=\mathrm{human}.
\end{cases}
\label{eq:query-placement}
\end{equation}

Here $\bar{\mathbf q}_i$ is homogeneous, $\operatorname{xyz}$ extracts Euclidean coordinates, and $\mathbf A_i(t)$ is the weighted skinning transform. Projection into a camera gives depth $z_{i,t,v}$ and sampled feature, depth, and confidence $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$. With tolerance $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$, define $r=(d-z)/\eta$. A surface observation must lie inside the image, have valid depth and sufficient confidence, match the query's instance, and satisfy $|r|\leq1$. Background queries additionally require static-background semantics. Let $a_{i,t,v}$ denote this validity test. We aggregate

\begin{align}
w_{i,t,v}&=a_{i,t,v}c_{i,t,v}\exp(-r_{i,t,v}^2/2),\\
\mathbf h_i&=\frac{\sum_{t,v}w_{i,t,v}[\boldsymbol\phi_{i,t,v};r_{i,t,v}]}
{\max(\varepsilon,\sum_{t,v}w_{i,t,v})}.
\label{eq:aggregation}
\end{align}

The query confidence is the maximum over accepted observations. A reliable ray votes for free space only when the entire support cell is in front of the measured surface; the criterion is detailed in Appendix D of the supplementary material.

Positive accumulated observation weight marks a query as observed. Otherwise, sufficient free-space votes mark it free, and the remainder is unknown. The masks $m_i$, $f_i$, and $u_i$ are mutually exclusive and satisfy $m_i+f_i+u_i=1$. Sky projection uses camera rotation alone, reliable sky semantics, and zero depth residual; sky queries receive no free-space votes.
```

### English §3.5

**修改前**

```latex
\subsection{Scene composition and observation consistency}
\label{sec:composition}

\paragraph{State-driven rendering.}

At online step $k$, state $s_k$ specifies the ego pose, active assets, vehicle transforms, and human root and joint poses. A vehicle's Gaussian center and covariance transform as

\begin{equation}
\boldsymbol\mu^w=\mathbf R\boldsymbol\mu^a+\mathbf t,
\qquad
\boldsymbol\Sigma^w=\mathbf R\boldsymbol\Sigma^a\mathbf R^\top.
\label{eq:rigid}
\end{equation}

For humans, the weighted skinning transform is $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$, where $\mathbf B_j$ and $\mathbf P_j$ are rest and current global joints in the root frame. The transformed center is $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$. The combined local linear map $\mathbf J_i$ gives covariance $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$. Its inverse $\mathbf J_i^{-1}$ maps viewing directions into the canonical frame; the direction is normalized before appearance evaluation. Nearly singular skinning transforms are rejected. The root pose controls overall placement, while the root joint retains its rest transform.

The renderer composites the background, active assets, and valid sky. External policy and dynamics can advance the state:

\begin{align}
o_k&=\mathcal R(\operatorname{Compose}(\mathcal W,s_k),\mathcal C_k),\\
s_{k+1}&=F_{\rm dyn}(s_k,\pi(o_k),\Delta t).
\label{eq:simulation}
\end{align}

Resetting or branching a trajectory changes state while preserving $\mathcal W$ and its seed. Finite support and supported sky directions determine coverage. Road meshes and collision proxies share the visual assets' coordinates and are maintained by the physical backend.

\paragraph{Checking a constructed scene.}

Fixed observed codes preserve decoded parameters, but a newly generated surface can still occlude them. Before accepting a scene, we render the completed candidate and an observed-only reference at the original cameras and actor states. The reference disables all non-observed queries. Let $e_{\rm cand}(p)$ and $e_{\rm obs}(p)$ be their mean absolute RGB errors at pixel $p$. We measure local degradation with

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

Averaging this quantity over reliable non-ego pixels prevents improvements in one region from cancelling degradation elsewhere. Acceptance also bounds absolute RGB and valid-depth errors, minimum coverage, and foreground intrusion, using aggregate and worst-view checks. An intrusion is a newly rendered surface in front of the predicted reference depth that is absent from the observed-only render; its rate is normalized over reliable non-sky geometry pixels. Predicted depth provides an observation-consistency reference. Independent geometry evaluation requires a separate reference. A rejected candidate is not exported for reuse.
```

**修改后**

```latex
\subsection{Scene composition and observation consistency}
\label{sec:composition}

\paragraph{State-driven rendering.}

At online step $k$, state $s_k$ specifies the ego pose, active assets, vehicle transforms, and human root and joint poses. Vehicles are placed by rigid transforms and humans by skinning; standard transformations and backend details are given in Appendix C of the supplementary material. The renderer composites the background, active assets, and valid sky:

\begin{equation}
o_k=\mathcal R(\operatorname{Compose}(\mathcal W,s_k),\mathcal C_k).
\label{eq:simulation}
\end{equation}

Resetting or branching a trajectory changes state while preserving $\mathcal W$ and its seed. Finite support and supported sky directions determine coverage.

\paragraph{Checking a constructed scene.}

Fixed observed codes preserve decoded parameters, but a newly generated surface can still occlude them. Before accepting a scene, we render the completed candidate and an observed-only reference at the original cameras and actor states. The reference disables all non-observed queries. Let $e_{\rm cand}(p)$ and $e_{\rm obs}(p)$ be their mean absolute RGB errors at pixel $p$. We measure local degradation with

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

Averaging this quantity over reliable non-ego pixels prevents improvements in one region from cancelling degradation elsewhere. Acceptance also bounds absolute RGB and valid-depth errors, minimum coverage, and foreground intrusion, using aggregate and worst-view checks. An intrusion is a newly rendered surface in front of the predicted reference depth that is absent from the observed-only render; its rate is normalized over reliable non-sky geometry pixels. Predicted depth provides an observation-consistency reference. Independent geometry evaluation requires a separate reference. A rejected candidate is not exported for reuse.
```

### 中文 §3.2

**修改前**

```latex
\subsection{视觉恢复与规范聚合}
\label{sec:queries}

\paragraph{共享视觉编码。}

Driving Log Encoder 使用图像 patch 划分~\cite{dosovitskiy2021vit}与 Transformer 注意力~\cite{vaswani2017attention}，并加入图像位置、相机标定和时间编码。图像内部注意力提取空间特征，第二个 Transformer 在不同视角与时刻的池化图像摘要之间交互，再将上下文送回 patch 特征。几何头预测相机光轴深度、法线、置信度、语义和实例归属。置信度决定哪些预测可以提供表面证据。

可学习的资产查询读取全部图像 token，形成轨迹级身份槽；每个槽再读取单个时刻的特征以估计状态。由此，持久身份、尺寸和人体体型与逐帧变化的根位姿、关节旋转分开表示。根位姿先在支架坐标中预测，再通过 $\mathbf T^w_r(t)$ 映射到世界坐标。人体体型码选择对应身份的模板，模板包含固定规范支撑、骨架拓扑和绑定。身份槽容量限定可表示的资产数量。

\paragraph{查询支撑。}

每个查询存储规范位置 $\mathbf q_i$、单元尺度 $\boldsymbol\delta_i$、类型 $k_i$、局部注意力组 $g_i$ 和参考世界坐标 $\mathbf q_i^w$。可靠深度样本提供表面锚点。背景锚点与有限世界网格结合；车辆锚点经运动规范化后，与局部包围体中的网格结合。人体查询位于规范模板表面，天空查询为按立方体贴图面分组的单位方向。这些支撑为已见与缺失内容提供明确位置。

补全过程中布局保持固定。我们将查询放到第一帧的配置中以得到 $\mathbf q_i^w$，其中人体包含蒙皮变换。规范坐标标识组件内部的内容，参考世界坐标则使生成器能够联系该组件与周围场景。

\paragraph{运动感知证据聚合。}

对于每份观测，我们将规范查询放到对应的资产状态：

\begin{equation}
\mathbf p_i(t)=
\begin{cases}
\mathbf q_i,& k_i=\mathrm{background},\\
\operatorname{xyz}(\mathbf T^w_a(t)\bar{\mathbf q}_i),& k_i=\mathrm{vehicle},\\
\operatorname{xyz}(\mathbf T^w_h(t)\mathbf A_i(t)\bar{\mathbf q}_i),& k_i=\mathrm{human}.
\end{cases}
\label{eq:query-placement}
\end{equation}

其中，$\bar{\mathbf q}_i$ 为齐次坐标，$\operatorname{xyz}$ 提取欧氏坐标，$\mathbf A_i(t)$ 为加权蒙皮变换。投影到相机后，得到深度 $z_{i,t,v}$ 以及采样特征、深度和置信度 $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$。给定容差 $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$，定义 $r=(d-z)/\eta$。表面观测需位于图像内、深度有效、置信度足够，与查询的实例身份一致，并满足 $|r|\leq1$。背景查询还要求静态背景语义。令 $a_{i,t,v}$ 表示这一有效性判断，则聚合为

\begin{align}
w_{i,t,v}&=a_{i,t,v}c_{i,t,v}\exp(-r_{i,t,v}^2/2),\\
\mathbf h_i&=\frac{\sum_{t,v}w_{i,t,v}[\boldsymbol\phi_{i,t,v};r_{i,t,v}]}
{\max(\varepsilon,\sum_{t,v}w_{i,t,v})}.
\label{eq:aggregation}
\end{align}

查询置信度取被接受观测中的最大值。该筛选排除深度或实例身份与查询不一致的观测。仅当整个支撑单元都位于观测表面之前时，可靠射线才提供自由空间票：

\begin{equation}
z_{i,t,v}+\tfrac12\|\boldsymbol\delta_i\|_2<d_{i,t,v}-\eta.
\label{eq:free-space}
\end{equation}

有效观测权重之和大于零时，查询被标为已见。否则，足够的自由空间票将其标为自由空间，其余查询为未知。掩码 $m_i$、$f_i$ 和 $u_i$ 互斥，满足 $m_i+f_i+u_i=1$。天空投影仅使用相机旋转，采用可靠天空语义和零深度残差，不接收自由空间票。
```

**修改后**

```latex
\subsection{视觉恢复与规范聚合}
\label{sec:queries}

\paragraph{共享视觉编码。}

Driving Log Encoder 使用 Transformer 特征~\cite{dosovitskiy2021vit,vaswani2017attention}，从有标定的图像日志预测相机光轴深度、法线、置信度、语义和实例归属。轨迹级身份槽将持久身份、尺寸和人体体型与逐帧变化的根位姿、关节旋转分开表示。网络结构与状态参数化细节见补充材料附录 D。

\paragraph{查询支撑。}

每个查询存储规范位置 $\mathbf q_i$、单元尺度 $\boldsymbol\delta_i$、类型 $k_i$、局部注意力组 $g_i$ 和参考世界坐标 $\mathbf q_i^w$。可靠深度样本提供表面锚点。背景锚点与有限世界网格结合；车辆锚点经运动规范化后，与局部包围体中的网格结合。人体查询位于规范模板表面，天空查询为按立方体贴图面分组的单位方向。这些支撑为已见与缺失内容提供明确位置。

补全过程中布局保持固定。我们将查询放到第一帧的配置中以得到 $\mathbf q_i^w$，其中人体包含蒙皮变换。规范坐标标识组件内部的内容，参考世界坐标则使生成器能够联系该组件与周围场景。

\paragraph{运动感知证据聚合。}

对于每份观测，我们将规范查询放到对应的资产状态：

\begin{equation}
\mathbf p_i(t)=
\begin{cases}
\mathbf q_i,& k_i=\mathrm{background},\\
\operatorname{xyz}(\mathbf T^w_a(t)\bar{\mathbf q}_i),& k_i=\mathrm{vehicle},\\
\operatorname{xyz}(\mathbf T^w_h(t)\mathbf A_i(t)\bar{\mathbf q}_i),& k_i=\mathrm{human}.
\end{cases}
\label{eq:query-placement}
\end{equation}

其中，$\bar{\mathbf q}_i$ 为齐次坐标，$\operatorname{xyz}$ 提取欧氏坐标，$\mathbf A_i(t)$ 为加权蒙皮变换。投影到相机后，得到深度 $z_{i,t,v}$ 以及采样特征、深度和置信度 $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$。给定容差 $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$，定义 $r=(d-z)/\eta$。表面观测需位于图像内、深度有效、置信度足够，与查询的实例身份一致，并满足 $|r|\leq1$。背景查询还要求静态背景语义。令 $a_{i,t,v}$ 表示这一有效性判断，则聚合为

\begin{align}
w_{i,t,v}&=a_{i,t,v}c_{i,t,v}\exp(-r_{i,t,v}^2/2),\\
\mathbf h_i&=\frac{\sum_{t,v}w_{i,t,v}[\boldsymbol\phi_{i,t,v};r_{i,t,v}]}
{\max(\varepsilon,\sum_{t,v}w_{i,t,v})}.
\label{eq:aggregation}
\end{align}

查询置信度取被接受观测中的最大值。仅当整个支撑单元都位于观测表面之前时，可靠射线才提供自由空间票；具体判定式见补充材料附录 D。

有效观测权重之和大于零时，查询被标为已见。否则，足够的自由空间票将其标为自由空间，其余查询为未知。掩码 $m_i$、$f_i$ 和 $u_i$ 互斥，满足 $m_i+f_i+u_i=1$。天空投影仅使用相机旋转，采用可靠天空语义和零深度残差，不接收自由空间票。
```

### 中文 §3.5

**修改前**

```latex
\subsection{场景装配与观测一致性}
\label{sec:composition}

\paragraph{状态驱动渲染。}

在线步 $k$ 的状态 $s_k$ 指定自车位姿、活动资产、车辆变换，以及人体根位姿与关节姿态。车辆的高斯中心和协方差变换为

\begin{equation}
\boldsymbol\mu^w=\mathbf R\boldsymbol\mu^a+\mathbf t,
\qquad
\boldsymbol\Sigma^w=\mathbf R\boldsymbol\Sigma^a\mathbf R^\top.
\label{eq:rigid}
\end{equation}

人体使用加权蒙皮变换 $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$，其中 $\mathbf B_j$ 和 $\mathbf P_j$ 是根坐标系中的静止与当前全局关节矩阵。变换后的中心为 $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$。组合局部线性映射 $\mathbf J_i$ 将协方差变换为 $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$，其逆 $\mathbf J_i^{-1}$ 将观察方向映回规范坐标，并在外观求值前归一化。接近奇异的蒙皮变换被拒绝。根位姿控制整体放置，根关节保持静止变换。

渲染器合成背景、活动资产和有效天空。外部策略与动力学可推进状态：

\begin{align}
o_k&=\mathcal R(\operatorname{Compose}(\mathcal W,s_k),\mathcal C_k),\\
s_{k+1}&=F_{\rm dyn}(s_k,\pi(o_k),\Delta t).
\label{eq:simulation}
\end{align}

重置或分支轨迹改变状态，同时保留 $\mathcal W$ 及其种子。有限空间支撑和有效天空方向决定覆盖范围。道路网格与碰撞代理采用和视觉资产一致的坐标，由物理后端维护。

\paragraph{构建场景的检查。}

固定已见潜码能够保持解码参数，但新增表面仍可能遮挡这些内容。接受场景之前，我们在原始相机和资产状态下渲染补全候选及仅由已见查询构成的观测参考；参考渲染关闭全部非已见查询。令 $e_{\rm cand}(p)$ 和 $e_{\rm obs}(p)$ 为像素 $p$ 处两者的平均绝对 RGB 误差，局部退化定义为

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

在可靠的非自车像素上平均这一量，避免某一区域的改善抵消其他区域的退化。接受条件还限制绝对 RGB 误差、有效深度误差和前景侵入率，并要求最低覆盖率；这些条件同时检查聚合结果和最差视图。前景侵入指新增渲染表面位于预测参考深度之前，且未出现在观测参考渲染中；其比例按可靠的非天空几何像素归一化。预测深度提供观测一致性参照，独立几何评测需要另一份参考。被拒绝的候选不导出复用。
```

**修改后**

```latex
\subsection{场景装配与观测一致性}
\label{sec:composition}

\paragraph{状态驱动渲染。}

在线步 $k$ 的状态 $s_k$ 指定自车位姿、活动资产、车辆变换，以及人体根位姿与关节姿态。车辆通过刚体变换放置，人体通过蒙皮变换放置；标准变换和后端细节见补充材料附录 C。渲染器合成背景、活动资产和有效天空：

\begin{equation}
o_k=\mathcal R(\operatorname{Compose}(\mathcal W,s_k),\mathcal C_k).
\label{eq:simulation}
\end{equation}

重置或分支轨迹改变状态，同时保留 $\mathcal W$ 及其种子。有限空间支撑和有效天空方向决定覆盖范围。

\paragraph{构建场景的检查。}

固定已见潜码能够保持解码参数，但新增表面仍可能遮挡这些内容。接受场景之前，我们在原始相机和资产状态下渲染补全候选及仅由已见查询构成的观测参考；参考渲染关闭全部非已见查询。令 $e_{\rm cand}(p)$ 和 $e_{\rm obs}(p)$ 为像素 $p$ 处两者的平均绝对 RGB 误差，局部退化定义为

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

在可靠的非自车像素上平均这一量，避免某一区域的改善抵消其他区域的退化。接受条件还限制绝对 RGB 误差、有效深度误差和前景侵入率，并要求最低覆盖率；这些条件同时检查聚合结果和最差视图。前景侵入指新增渲染表面位于预测参考深度之前，且未出现在观测参考渲染中；其比例按可靠的非天空几何像素归一化。预测深度提供观测一致性参照，独立几何评测需要另一份参考。被拒绝的候选不导出复用。
```

---

# 历史记录：仅压缩 §3.6 训练流程

更新：2026-10-25。范围：中英文主稿 §3.6，以及独立补充材料 B；其他论文章节保持本轮起点原文。英文是唯一篇幅验收对象。

真实基线：HEAD `ee5b6cb` 之上的本轮未提交工作区，完整源文保存在 `paper/build/revision-baseline.json` 的 `training_migration_before`；本轮前 PDF 的哈希及逐页文本保存在 `training_migration_pdf_before`。不将此前的引言、摘要和跨数据集迁移算作本轮改动。

## 1. 原问题 → 局部修改 → 保留位置

| 位置 | 原问题/修改前 | 修改后 | 原因及保留情况 |
| --- | --- | --- | --- |
| 开头 | 四句概述各模块作用，随后四阶段再展开 | 保留首句，增加补充材料 B 指引 | 让正文快速进入训练逻辑；完整概述保留在 B |
| Stage 1 | 罗列轨迹匹配、车辆/人体监督及置信度校准 | 保留监督对象、监督来源及其建立坐标/身份一致性的作用 | 细节全部原样保留在 B 的 Stage 1 |
| Stage 2 | 同布局目标构造后继续展开集合匹配、RGB/深度公式与掩码解释 | 保留冻结恢复模块、训练编解码器、同布局目标对应和监督类别 | 原公式 (17)–(18) 移为 B 中 (S1)–(S2)，集合匹配与掩码说明一并保留 |
| Stage 3 | 核心目标有效性条件之外，还列举掩码模式与恢复误差扰动 | 保留冻结范围、flow 目标、每个未知查询必须有有效目标、同一 codec/查询定义 | 完整场景/资产的作用、拒绝无效目标、掩码与扰动细节均保留在 B；主稿核心公式 (10)–(11) 不动 |
| Stage 4 | 梯度路径之后，展开自由射线、接地、穿透损失与符号定义 | 保留仅更新补全网络、真实日志监督、几何约束、可交替完整目标及各损失适用条件、已见锚点保持 | 原公式 (19)–(20) 移为 (S3)–(S4)，混合目标 L4 及所有符号说明保留在 B |
| Inference | 场景导出流程之后说明模块版本登记 | 场景编码、补全、解码、检查及固定内容复用句子原样保留 | 版本登记移入 B，不改变推理流程 |

补充材料 B 保留原 §3.6 的完整学术文字，便于独立阅读。只调整 section 标题、标签，并将对主稿 flow 公式的引用写为“主稿式 (10)/(11)”；不把主稿编号误链接成补充材料公式。两版原有补充材料 A 和表 S1 内容均未改。

当前正文未提供具体数值化损失权重、优化器配置或各阶段训练预算，本轮没有补造这些内容；迁移的是已有损失定义、条件扰动与版本配置说明。详细训练参数仍需作者的实际配置来源。

## 2. 英文篇幅变化

| 项目 | 本轮修改前 | 修改后 |
| --- | ---: | ---: |
| §3.6 占用估计 | 约 0.90 页 | 约 0.46 页 |
| Method 整体占用估计 | 约 3.40 页 | 约 2.97 页 |
| 正文流式占用估计 | 约 9.07 页 | 约 8.64 页 |
| 正文结束位置 | 第 10 页左栏 | 第 9 页右栏 |
| 含参考文献的英文主稿总页数 | 12 | 12 |
| 英文补充材料总页数 | 1 | 2 |

§3.6 约节省 0.44 页，正文整体约节省 0.43 页。正文结束页提前不等于节省了整整一页；图表与段落重排会影响实际收益。页当量沿用每页两栏、每栏 648 pt 的估计口径，不能替代正式验收。当前正文仍越过第 8 页，下一步尚需约 0.64 页内容空间，另留排版余量；本轮按范围停止，不修改其他章节。

## 3. 编译与版面检查

- 中英文主稿、两版补充材料均重新编译成功；最终日志无未定义引用、缺字或 Overfull 警告。
- 检查英文第 5–9 页（训练流程、重排后的图表、正文结尾）、中文第 4–5 页及两版补充材料全部页面。
- 修复独立补充材料在当前 TeX 版本下的双栏行号错位：采用 lineno 原有列标记包装方式，将列号写在列内容之前。仅补充项目加载 `lineno-fix.tex`，不改正文、模板字号、页边距或行距；最终行号均位于外侧，不覆盖文字。
- 主稿 §3.1–3.5、标题、摘要、引言/贡献、相关工作、实验、局限、结论均与本轮基线逐字一致；补充 A 及表格数值不变。
- 原 §3.6 的完整内容在 B 中逐字核对通过（仅标题/标签和主稿公式引用方式变化）；不是删除后仅留下迁移声明。
- 未提交或推送 GitHub。

## 4. 英文 §3.6 全文前后对照

### 修改前

```latex
\subsection{Training procedure}
\label{sec:training}

Learning is divided into four stages so that the completion target has a stable meaning. Recovery determines the evidence and support, the codec defines its latent coordinates, and the completion network learns a distribution over the missing codes. The last stage adapts this distribution to real observations without changing the representation it predicts.

\paragraph{Stage 1: visual recovery.}

We supervise the image encoder, geometry heads, identity slots, and state heads using geometry, semantics, instance assignments, and actor annotations. One trajectory-level matching assigns slots to target identities and is reused at every timestamp. Root translation, rotation, and fixed dimensions constrain vehicle states; humans additionally require identity-consistent shape, template binding, and joint supervision. Confidence is trained or calibrated against geometric reliability, using depth, occlusion, and reprojection information. These targets establish the coordinate and identity consistency required by aggregation.

\paragraph{Stage 2: latent representation fitting.}

We freeze recovery and train the type-specific encoders and decoders. For each sample, partial input establishes the query layout once. More complete observations are then aggregated on exactly the same positions, types, order, and ownership. This correspondence is required for latent completion: separately rebuilding a complete-scene layout would change the variables being predicted. RGB, depth, and silhouette supervision train the decoded scene, with empty-space opacity and Gaussian-scale regularization. Gaussian-set targets can also be matched as sets; direct coordinate supervision is used only when child correspondences are available.

For rendered image $\widehat{\mathbf I}$ and depth $\widehat d$, the observation terms used in representation fitting and later adaptation are masked L1 errors:

\begin{align}
\mathcal L_{\rm rgb}&=\langle\|\widehat{\mathbf I}-\mathbf I\|_1/3\rangle_{\Omega_I},\\
\mathcal L_{\rm depth}&=\langle|\widehat d-d|\rangle_{\Omega_d}.
\label{eq:reconstruction-loss}
\end{align}

The notation $\langle\ell\rangle_{\Omega}$ denotes a mean over valid elements of mask $\Omega$. The depth target $d$ and its validity mask are supplied by the available supervision; they do not make the observation check an independent accuracy measurement.

\paragraph{Stage 3: completion-prior learning.}

We freeze recovery and the entire codec, encode complete targets as $\mathbf z_1$, and optimize the completion transformer with Eq.~\ref{eq:flow-loss}. Complete scene or asset examples must provide a valid target for every unknown query in Eq.~\ref{eq:flow-path}; partial real logs alone do not meet this condition. Complete scenes provide cross-component context, while complete assets supply within-object content. A validity test rejects targets with unsupported unknown queries.

Conditioning masks simulate contiguous unseen surfaces, background holes, long occlusions, short tracks, and uneven camera coverage. Perturbations to recovered poses, instance assignments, and confidence expose the generator to imperfect evidence. Target codes and input codes retain the same codec and query definition throughout this stage.

\paragraph{Stage 4: adaptation through rendering.}

Keeping recovery and the codec frozen, we differentiate through flow integration, decoding, and rendering to update only the completion network. Partial real logs supervise the rendered observations. Known-free rays and geometric backend samples constrain added content:

\begin{align}
\mathcal L_{\rm scene}={}&\lambda_e\langle a_r^2\rangle
+\lambda_g\langle[-d_f]_+^2\rangle\nonumber\\
&+\lambda_c\langle|d_f|\rangle_{\Omega_c}
+\lambda_p\langle[d_p]_+^2\rangle,\\
\mathcal L_{\rm adapt}={}&\lambda_r\mathcal L_{\rm rgb}
+\lambda_d\mathcal L_{\rm depth}+\mathcal L_{\rm scene}.
\label{eq:adaptation}
\end{align}

Here $a_r$ is accumulated opacity along a known-free ray, $d_f$ is foot signed distance positive above ground, $\Omega_c$ selects contacting feet, and $d_p$ is penetration depth positive inside another actor. We use $[x]_+=\max(x,0)$; unmasked means run over supplied samples. The coefficients $\lambda$ weight the active constraints. Free-ray opacity constrains the rendered effects of added content beyond the query-level free-space mask.

Complete-target samples can be interleaved with real-log adaptation to retain the learned prior, yielding $\mathcal L_4=\lambda_f\mathcal L_{\rm flow}+\mathcal L_{\rm adapt}$, with each term applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration.

\paragraph{Inference.}

A log is encoded once, its support and evidence are fixed, and the completion model integrates the unknown codes. We then decode and check the scene before exporting its fixed content. Runtime rendering uses only this content and the requested states. Recovery, codec, completion, and query-definition versions are recorded together, since changing any of the first two changes the latent distribution on which completion was learned.
```

### 修改后

```latex
\subsection{Training procedure}
\label{sec:training}

Learning is divided into four stages so that the completion target has a stable meaning. Detailed supervision, losses, and conditioning perturbations are provided in Appendix B of the supplementary material.

\paragraph{Stage 1: visual recovery.}

We supervise the image encoder, geometry heads, identity slots, and state heads using geometry, semantics, instance assignments, and actor annotations. These targets establish the coordinate and identity consistency required by aggregation.

\paragraph{Stage 2: latent representation fitting.}

We freeze recovery and train the type-specific encoders and decoders. For each sample, partial input establishes the query layout once. More complete observations are then aggregated on exactly the same positions, types, order, and ownership. This correspondence is required for latent completion: separately rebuilding a complete-scene layout would change the variables being predicted. RGB, depth, and silhouette supervision train the decoded scene, with empty-space opacity and Gaussian-scale regularization.

\paragraph{Stage 3: completion-prior learning.}

We freeze recovery and the entire codec, encode complete targets as $\mathbf z_1$, and optimize the completion transformer with Eq.~\ref{eq:flow-loss}. Complete scene or asset examples must provide a valid target for every unknown query in Eq.~\ref{eq:flow-path}; partial real logs alone do not meet this condition. Target codes and input codes retain the same codec and query definition throughout this stage.

\paragraph{Stage 4: adaptation through rendering.}

Keeping recovery and the codec frozen, we differentiate through flow integration, decoding, and rendering to update only the completion network. Partial real logs supervise the rendered observations. Known-free rays and geometric backend samples constrain added content. Complete-target samples can be interleaved with real-log adaptation to retain the learned prior, with each loss term applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration.

\paragraph{Inference.}

A log is encoded once, its support and evidence are fixed, and the completion model integrates the unknown codes. We then decode and check the scene before exporting its fixed content. Runtime rendering uses only this content and the requested states.
```

## 5. 中文 §3.6 全文前后对照

### 修改前

```latex
\subsection{训练过程}
\label{sec:training}

学习分为四个阶段，使补全目标具有稳定含义。恢复模块确定证据与支撑，编解码器定义潜空间坐标，补全网络学习缺失潜码的分布。最后一个阶段将该分布适配到真实观测，同时保持其预测的表示不变。

\paragraph{阶段一：视觉恢复。}

我们利用几何、语义、实例归属和资产标注监督图像编码器、几何头、身份槽及状态头。在整条轨迹上执行一次匹配，将槽分配给目标身份，并在所有时刻复用这一匹配。根平移、旋转和固定尺寸约束车辆状态；人体还需要身份一致的体型、模板绑定和关节监督。置信度根据几何可靠性训练或校准，依据包括深度、遮挡和重投影信息。这些目标建立聚合所需的坐标与身份一致性。

\paragraph{阶段二：潜表示拟合。}

冻结恢复模块，训练类型专属编码器和解码器。每个样本先由部分输入建立一次查询布局，再将更完整的观测聚合到完全相同的位置、类型、顺序和归属上。这种对应关系是潜码补全的前提；若为完整场景另建布局，就会改变待预测变量。RGB、深度和轮廓监督训练解码场景，并结合空域不透明度与高斯尺度正则。高斯集合目标也可以采用集合匹配；仅在子高斯对应已知时使用直接坐标监督。

对于渲染图像 $\widehat{\mathbf I}$ 和深度 $\widehat d$，表示拟合及后续适配使用的观测项为带掩码的 L1 误差：

\begin{align}
\mathcal L_{\rm rgb}&=\langle\|\widehat{\mathbf I}-\mathbf I\|_1/3\rangle_{\Omega_I},\\
\mathcal L_{\rm depth}&=\langle|\widehat d-d|\rangle_{\Omega_d}.
\label{eq:reconstruction-loss}
\end{align}

符号 $\langle\ell\rangle_{\Omega}$ 表示在掩码 $\Omega$ 的有效元素上取平均。深度目标 $d$ 及其有效掩码由可用监督提供；它们不使观测检查成为独立的精度测量。

\paragraph{阶段三：补全先验学习。}

冻结恢复模块和整个编解码器，将完整目标编码为 $\mathbf z_1$，并以式~\ref{eq:flow-loss} 优化补全 Transformer。完整场景或资产样本必须为式~\ref{eq:flow-path} 中的每个未知查询提供有效目标，单独的部分真实日志不满足这一条件。完整场景提供跨组件上下文，完整资产提供对象内部内容；任一未知查询缺少有效目标潜码时，有效性检查会拒绝该样本。

条件掩码模拟连续未见表面、背景空洞、长时间遮挡、短轨迹和不均匀相机覆盖。对恢复位姿、实例归属和置信度施加扰动，使生成器接触不完美证据。该阶段中，目标潜码和输入潜码始终使用相同的编解码器与查询定义。

\paragraph{阶段四：通过渲染适配。}

保持恢复模块与编解码器冻结，通过流积分、解码和渲染反向传播，仅更新补全网络。部分真实日志监督渲染观测，已知自由射线和几何后端样本约束新增内容：

\begin{align}
\mathcal L_{\rm scene}={}&\lambda_e\langle a_r^2\rangle
+\lambda_g\langle[-d_f]_+^2\rangle\nonumber\\
&+\lambda_c\langle|d_f|\rangle_{\Omega_c}
+\lambda_p\langle[d_p]_+^2\rangle,\\
\mathcal L_{\rm adapt}={}&\lambda_r\mathcal L_{\rm rgb}
+\lambda_d\mathcal L_{\rm depth}+\mathcal L_{\rm scene}.
\label{eq:adaptation}
\end{align}

其中，$a_r$ 为已知自由射线上的累积不透明度，$d_f$ 为脚点有符号距离且地面上方为正，$\Omega_c$ 选择接地脚点，$d_p$ 为穿透深度且另一资产内部为正。采用 $[x]_+=\max(x,0)$；无掩码的平均在提供的样本上计算。系数 $\lambda$ 为有效约束赋权。自由射线不透明度在查询级空域掩码之外，进一步约束新增内容的渲染影响。

完整目标样本可与真实日志适配交替使用以保留先验，得到 $\mathcal L_4=\lambda_f\mathcal L_{\rm flow}+\mathcal L_{\rm adapt}$，各项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。

\paragraph{推理。}

日志只编码一次，随后固定支撑与证据，由补全模型积分未知潜码。解码并检查场景后，导出固定内容；运行时渲染仅使用这些内容和指定状态。恢复模块、编解码器、补全网络与查询定义的版本一并记录，因为前两者的变化会改变补全网络学习的潜分布。
```

### 修改后

```latex
\subsection{训练过程}
\label{sec:training}

学习分为四个阶段，使补全目标具有稳定含义。详细监督、损失和条件扰动见补充材料附录 B。

\paragraph{阶段一：视觉恢复。}

我们利用几何、语义、实例归属和资产标注监督图像编码器、几何头、身份槽及状态头。这些目标建立聚合所需的坐标与身份一致性。

\paragraph{阶段二：潜表示拟合。}

冻结恢复模块，训练类型专属编码器和解码器。每个样本先由部分输入建立一次查询布局，再将更完整的观测聚合到完全相同的位置、类型、顺序和归属上。这种对应关系是潜码补全的前提；若为完整场景另建布局，就会改变待预测变量。RGB、深度和轮廓监督训练解码场景，并结合空域不透明度与高斯尺度正则。

\paragraph{阶段三：补全先验学习。}

冻结恢复模块和整个编解码器，将完整目标编码为 $\mathbf z_1$，并以式~\ref{eq:flow-loss} 优化补全 Transformer。完整场景或资产样本必须为式~\ref{eq:flow-path} 中的每个未知查询提供有效目标，单独的部分真实日志不满足这一条件。该阶段中，目标潜码和输入潜码始终使用相同的编解码器与查询定义。

\paragraph{阶段四：通过渲染适配。}

保持恢复模块与编解码器冻结，通过流积分、解码和渲染反向传播，仅更新补全网络。部分真实日志监督渲染观测，已知自由射线和几何后端样本约束新增内容。完整目标样本可与真实日志适配交替使用以保留先验，各损失项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。

\paragraph{推理。}

日志只编码一次，随后固定支撑与证据，由补全模型积分未知潜码。解码并检查场景后，导出固定内容；运行时渲染仅使用这些内容和指定状态。
```

迁移后的完整说明：[英文补充材料 B 源文](../paper/supplementary/training.tex) · [中文补充材料 B 源文](../paper/supplementary/training_zh.tex)。

---

# 历史记录：跨数据集实验迁入补充材料

更新：2026-10-25。用户授权将原英文 4.4 移入 CVPR 格式补充材料，同步调整中英文摘要及实验概述，并提供 8 页压缩方案；本轮没有执行 Method、Related Work、引言或图件的压缩。

按用户补充要求，8 页限制及压缩方案只按英文主稿验收；中文仅同步内容，补充材料独立计页。

真实起点：本轮开始时的未提交工作区，已保存到 `paper/build/revision-baseline.json` 的 `supplement_migration_before` 字段。此前引言/贡献/摘要的改动不算作本轮新增。

## 1. 内容从哪里到哪里

| 修改前 | 修改后 | 理由及保留情况 |
| --- | --- | --- |
| 英文主稿 4.4 Cross-Dataset Generalization：两段结果分析及表 3 | 独立英文补充材料 A，表 S1 | 两段学术文字原样迁移；仅标题由 subsection 改为 section，表浮动位置由 `[t]` 改为 `[!htbp]`，让独立短文先出现说明再出现表格 |
| 中文正文没有对应跨数据集小节或主结果表 | 中文补充材料 A，表 S1 | 从英文实际结果补齐中文；没有声称从不存在的中文小节中移除了内容 |
| 摘要同时突出 Waymo 外推及 nuScenes 迁移 | 两版只删去 nuScenes 结果半句 | 保留 Waymo FID 和 CCM 消融；其余摘要原文保持不变 |
| 英文实验概述列四个方向，包含跨数据集迁移 | 三个主方向，并指向补充材料 | 正文聚焦动态重建、轨迹外合成与消融 |
| 中文实验节没有概述 | 补上对应的三方向概述及补充材料入口 | 与英文主线同步；仅增加必要标签 `sec:ablations` 作为现有协议小节的别名，不改实验内容 |

[英文补充材料源文](../paper/supplementary/cross_dataset.tex) · [中文补充材料源文](../paper/supplementary/cross_dataset_zh.tex)。项目入口为 `paper/supplementary/main.tex` 和 `main_zh.tex`，独立编译；使用主稿相同的 CVPR review 样式、10 pt 双栏、Letter 纸型和匿名标记，补充参考文献单独编号。

表格逐项保留如下，没有改变指标、比较对象、粗体或结果值：

| 方法 | 迁移前 PSNR / SSIM | 补充材料 PSNR / SSIM |
| --- | --- | --- |
| STORM | 17.77 / 0.669 | 17.77 / 0.669 |
| DGGT | 25.31 / 0.794 | 25.31 / 0.794 |
| StreetForward | 23.17 / 0.712 | 23.17 / 0.712 |
| Ours | 26.47 / 0.803 | 26.47 / 0.803 |

## 2. 摘要的准确前后对照

### 英文

**修改前**

> On Waymo, DriveCompose reduces FID from 83.72 to 37.43 relative to STORM for ±2 m camera shifts, and reaches 26.47 dB PSNR in zero-shot transfer to nuScenes.

**修改后**

> On Waymo, DriveCompose reduces FID from 83.72 to 37.43 relative to STORM for ±2 m camera shifts.

### 中文

**修改前**

> 在 Waymo 的 ±2 m 相机偏移下，DriveCompose 相较于 STORM 将 FID 从 83.72 降至 37.43；零样本迁移至 nuScenes 时达到 26.47 dB PSNR。

**修改后**

> 在 Waymo 的 ±2 m 相机偏移下，DriveCompose 相较于 STORM 将 FID 从 83.72 降至 37.43。

英文摘要按同一空白分词方式由约 169 词变为 **159 词**，仍为 8 句，满足既定 150–250 词目标。前两句动机、方法命名、联合补全直觉、CCM 结果及最后一句均未重写。

## 3. 实验概述的前后对照

**英文修改前**

> We evaluate our method along four axes: (i) dynamic scene reconstruction quality on Waymo Open Dataset (§ 4.2); (ii) off-trajectory view synthesis under lateral camera shifts (§ 4.3); (iii) cross-dataset transfer from Waymo to nuScenes (§ 4.4); and (iv) ablations of the main design choices (§ 4.5).

**英文修改后**

> We evaluate our method along three axes: (i) dynamic scene reconstruction quality on Waymo Open Dataset (§ 4.2); (ii) off-trajectory view synthesis under lateral camera shifts (§ 4.3); and (iii) ablations of the main design choices (§ 4.4). Additional cross-dataset generalization results are provided in the supplementary material.

**中文修改前：** 无实验概述，直接进入“动态场景重建”。

**中文修改后**

> 我们从三个方面评价方法：（i）Waymo Open Dataset 上的动态场景重建质量（第 4.1 节）；（ii）横向相机偏移下的轨迹外视图合成（第 4.2 节）；（iii）主要设计的消融分析（第 4.3 节）。跨数据集泛化结果见补充材料。

这里用编译后的章节号展示；源码使用标签自动更新。中文主实验尚未与英文全部结构同步，故节号仍不同，本轮没有顺带补写无关章节。

英文正文的原 4.5/4.6/4.7 自动变为 4.4/4.5/4.6；原组件消融表 4 与输入敏感性表 5 自动变为表 3 与表 4。补充材料的迁移表独立编号为 S1，不占用主稿表号。

## 4. 编译、页数与保留项

| 材料 | 编译结果 | 当前页数 |
| --- | --- | ---: |
| 英文主稿 `paper/build/en/main.pdf` | XeLaTeX 成功 | 12 |
| 中文主稿 `paper/build/zh/main_zh.pdf` | XeLaTeX 成功 | 10 |
| 英文补充材料 `paper/build/supp-en/main.pdf` | XeLaTeX 成功；桌面内置编译器也验证通过 | 1 |
| 中文补充材料 `paper/build/supp-zh/main_zh.pdf` | XeLaTeX 成功 | 1 |

- 两版补充材料的表格主体与原英文表完全相同；引用的三条 BibTeX 记录从主书目提取，内容一致。
- Method 和引言两版源文与本轮起点完全一致；其余实验段落、实验值及图件保留。英文原 `raggedbottom` 命令保留，仅调整已不适用的注释。
- 最终构建无未定义引用、缺字或溢出；已检查两版摘要、实验概述及英文受影响图表页，并查看两版补充材料全部页面。
- 英文结论由第 10 页开始提前至第 9 页开始，但约 8 行仍续至第 10 页。以当前栏高估算，正文约 9.07 页当量；**本轮尚未压到 8 页**。
- 8 页方案已写入[工作流第 2 节](paper-revision-workflow.md#2-当前基线与压到-8-页的具体方案)。Method 约 3.40 页，优先将训练及外围实现压缩/迁移，目标约 2.45 页。其余候选项先讨论后按授权落实。
- 本轮未提交或推送 GitHub；保留用户已有图件移动和其他未提交改动。

---

# 历史记录：引言、贡献与摘要轮次 A–D

以下为此前的前后对照及理由，保留真实历史。其“当前”表示对应轮次；本轮引言与贡献仍沿用 D，摘要与跨数据集内容以本文上方的新记录为准。此前的主稿表号、节号按当时编译版本展示。


更新：2026-10-25。用户反馈上一版贡献表述不佳后，本轮仅调整两项贡献。摘要、引言其他段落、标题、方法、实验及图表均保持本轮起点原样。前一轮摘要修改及其证据记录继续保留。

## 如何阅读对照

- **首轮前 A**：Git 提交 `ee5b6cb` 中尚未润色的引言。
- **第一轮后 B**：初次引言微调完成，贡献和摘要尚未修改。
- **本轮前 C**：上一版已修改贡献及摘要的未提交工作区，用户反馈贡献表述不佳。本轮开始前已保存四份源文件到 `paper/build/revision-baseline.json` 的 `contribution_revision_before` 字段。
- **当前 D**：相对 C，只改两项贡献；两版摘要全文、引言六个主体段落、组织说明、引用与排版命令保持原样，仅随删除的消融结果句去掉其交叉引用。

“本轮贡献对照”展示 C → D；后面的英文与中文引言全文展示 A → D，包含所有保留段落。引用命令转换为当前编译编号，仅为便于阅读。英文和中文小节编号可能不同。

源文件：[英文引言](../paper/sec/1_introduction.tex)、[中文引言](../paper/zh/1_introduction_zh.tex)、[英文摘要](../paper/sec/0_abstract.tex)、[中文摘要](../paper/zh/0_abstract_zh.tex)。

## 为什么修正上一版贡献

上一版第一条用“a generative reconstruction formulation”开头，再展开身份、坐标系和运动绑定，重复了引言已经讲清的表示细节。第二条将注意力、记忆、三种观测约束及一个具体消融结果放在一起，贡献的中心被细节分散。

本轮保留“联合补全”与“跨组件上下文及观测约束”两条原有主线，分别回答：**框架提供什么能力，以及什么机制支撑这项能力。** 使用明确主语和动作，第一条点名 DriveCompose，第二条先说明跨组件记忆的作用，再说明潜空间与渲染视角的观测约束。

- 第一条不再重复列举身份、坐标系和绑定；这些技术含义继续保留在引言第 3–4 段和方法中，贡献中凝练为同一补全内容的状态复用。
- 第二条删除八时间戳和 20.5% 的消融结果句，使贡献集中陈述机制。结果继续保留在两版摘要与实验中，没有删除或改变证据。
- 不增加贡献项、不改研究问题、不声称“首次”，也不为追求措辞变化重写引言其他段落。

## 本轮贡献对照：C → D

### 英文两项贡献

| 项目 | 本轮前 C | 本轮后 D |
| --- | --- | --- |
| 贡献 1 | A generative reconstruction formulation that jointly completes a world-space background and canonical vehicle and human assets as a compositional Gaussian scene. Generated surfaces inherit their component's identity, coordinate frame, and motion binding for reuse under new camera and actor states. | We introduce DriveCompose, a generative reconstruction framework that jointly completes background and canonical actor assets from driving observations. The resulting compositional Gaussian scene can be rendered under new camera and actor states using the same completed content. |
| 贡献 2 | A structured conditional flow model that combines attention within each component with cross-component memory, while observed-code constraints, free-space suppression, and input-view checks anchor completion to recorded evidence. In the eight-timestamp ablation, cross-component memory reduces unseen-surface RGB error by 20.5% relative to isolated per-component memories (Sec. 4.6). | We develop a structured conditional flow model that shares scene context across background and assets through cross-component memory. Observed-code and free-space constraints guide latent completion, while input-view checks validate the assembled scene against the recorded observations. |


### 中文两项贡献

| 项目 | 本轮前 C | 本轮后 D |
| --- | --- | --- |
| 贡献 1 | 提出生成式重建形式，联合补全世界空间背景与规范车辆、人体资产，构建可组合高斯场景。生成表面继承所属组件的身份、坐标系与运动绑定，以支持新相机和参与者状态下的复用。 | 提出生成式重建框架 DriveCompose，从驾驶观测中联合补全背景与规范参与者资产。所得可组合高斯场景可在新的相机和参与者状态下渲染，复用同一份补全内容。 |
| 贡献 2 | 提出结构化条件流模型，结合组件内注意力与跨组件记忆，并通过已见潜码约束、自由空间抑制和输入视角检查，使补全过程遵循已记录的观测。在使用八个输入时间戳的消融中，跨组件记忆相较于各组件独立记忆，将未见表面的 RGB 误差降低了 20.5%（第 4.4 节）。 | 设计结构化条件流模型，通过跨组件记忆在背景与资产之间共享场景上下文。已见潜码与自由空间约束引导潜空间补全，输入视角检查则验证装配后的场景与已记录观测的一致性。 |


## 完整引言如何推进

| 部分 | 读者应获得的信息 | 本轮处理 |
| --- | --- | --- |
| 第 1 段：背景与任务 | 新相机/参与者状态暴露未见表面，重建需同时考虑补全和身份归属 | 沿用首轮文本 |
| 第 2 段：恢复方法的缺口 | 从已有观测恢复内容，并不自动提供之后暴露的表面 | 沿用首轮文本 |
| 第 3 段：表示与生成的结合 | 承认可组合表示和生成模型的进展，明确生成表面仍需归属、坐标系和运动规则 | 沿用首轮文本 |
| 第 4 段：关键见解 | 在组件的控制坐标系中补全，使生成内容可随组件状态变化保持归属 | 沿用首轮文本 |
| 第 5 段：实现核心见解 | 前端恢复证据，组件内注意力处理局部支撑，共享记忆交换上下文，再解码高斯 | 沿用首轮文本 |
| 第 6 段：观测保持与复用 | 约束已见潜码和自由空间，并检查新增内容的遮挡；构建后由状态驱动渲染 | 沿用首轮文本 |
| 两项贡献 | 分别概括联合补全框架的输出能力，以及共享上下文和观测约束的机制 | 本轮局部修改 |
| 组织说明 | 指向相关工作、方法、实验、局限性与结论 | 沿用首轮文本 |

## 英文 Introduction 全文对照：A → D

下表按原文顺序保留全文，每一行是一段或一项贡献；没有仅摘录改动句。第一轮前没有组织说明，对应空项用“原文无此段”标出。

| 部分 | 首轮修改前 A | 当前 D |
| --- | --- | --- |
| 背景与任务 | Driving datasets record scenes along captured trajectories [1, 31]. Driving simulation and scene editing require a reconstruction that remains usable when the recorded configuration changes. Moving a camera reveals a road patch hidden behind a vehicle. Turning that vehicle exposes its unseen side, and changing a pedestrian's pose brings previously occluded body surfaces into view. These operations require geometry and appearance beyond the recorded images, together with a representation that keeps the content attached to the same scene and actor identities. | Driving datasets record scenes along captured trajectories [1, 31]. Driving simulation and scene editing require a reconstruction that remains usable when the recorded configuration changes. Moving a camera, turning a vehicle, or changing a pedestrian's pose exposes previously unobserved surfaces. These operations require geometry and appearance beyond the recorded images, together with a representation that keeps the content attached to the same scene and actor identities. |
| 前馈恢复 | Recent feed-forward methods recover driving scenes directly from temporal observations. STORM aggregates dynamic Gaussians through estimated scene flow, and DGGT jointly recovers camera parameters and dynamic scene content from unposed images [3, 45]. StreetForward and PointForward further study temporal processing and the organization of reconstructed evidence [6, 48]. For an asset that will later be moved or articulated, however, observations across time must also be gathered into a stable local representation, and the surfaces exposed by the new state must be supplied. | Recent feed-forward methods recover driving scenes and motion directly from temporal observations [3, 6, 45, 48]. Recovering observed content alone does not supply the unseen surfaces exposed by later actor motion. |
| 可组合表示与生成 | Compositional representations address the first requirement. Street Gaussians separates vehicles from the background; OmniRe includes canonical models for rigid and articulated actors; HUGSIM connects scene content to control-driven state updates [5, 43, 49]. Generative models address missing content through asset priors, Gaussian completion, or generated views [17, 44, 47, 51]. Combining them requires a generator that assigns content to the background and to individual assets. A generated surface must have an owner, a coordinate frame, and a motion rule before it can become part of an editable scene. | Compositional representations separate background and actors and provide canonical models for independent motion and control [5, 43, 49]. Generative models address missing content through asset priors, Gaussian completion, or generated views [17, 44, 47, 51]. Combining them requires a generator that assigns content to the background and to individual assets. A generated surface must have an owner, a coordinate frame, and a motion rule before it can become part of an editable scene. |
| 关键见解 | We formulate driving-scene reconstruction as conditional generation of a compositional scene. Our representation follows the units that will be manipulated: a world-space background, rigid vehicles in local coordinates, and humans on canonical surfaces with skeleton bindings. Image evidence is first aggregated on these supports. A generative model then completes their missing latent content under the observed scene conditions. Each completed surface is decoded in the coordinate frame used to control its component. | We formulate driving-scene reconstruction as conditional generation of a compositional scene. Our representation follows the units that will be manipulated: a world-space background, rigid vehicles in local coordinates, and humans on canonical surfaces with skeleton bindings. Completing surfaces in their component's control frame lets the same generated content retain its identity under later state changes (Sec. 3.1). Image evidence is first aggregated on these supports. A generative model then completes their missing latent content under the observed scene conditions. |
| 方法概述 | DriveCompose implements this formulation with a visual recovery front end, structured latent codes, and a conditional flow model (Fig. 1). The front end estimates geometry, trajectory-level identities, and time-varying states. Canonical aggregation combines observations of the same content across views and time. Within the completion model, local attention follows each component's support, while shared memory exchanges context between background and assets. Each query carries both its canonical coordinate and its placement in a reference world configuration: the former identifies persistent content, and the latter expresses its spatial relation to the scene. Type-specific decoders convert the completed codes into Gaussian components. | DriveCompose implements this formulation with a visual recovery front end, structured latent codes, and a conditional flow model [18] (Fig. 1). The front end estimates geometry, trajectory-level identities, and time-varying states. Within the completion model, local attention follows each component's support, while shared memory exchanges context between background and assets. Type-specific decoders convert the completed codes into Gaussian components. |
| 观测保持与复用 | Generation must also respect the images from which the scene was recovered. We retain reliable observed codes and suppress known free space throughout sampling. Newly generated content can nevertheless occlude an observed surface, so we check the assembled candidate in the original views as well. After construction, the background and canonical assets remain fixed. Camera placement, vehicle transforms, and human joint poses determine their subsequent rendering. Learning follows this separation: we fit recovery and the latent representation before training the completion prior, then adapt generation through differentiable rendering while keeping the representation fixed. | Generation must also respect the images from which the scene was recovered. We retain reliable observed codes and suppress known free space throughout sampling. Newly generated content can nevertheless occlude an observed surface, so we check the assembled candidate in the original views as well. After construction, the background and canonical assets remain fixed. Camera placement, vehicle transforms, and human joint poses determine their subsequent rendering (Sec. 3.5). |
| 贡献导语 | Our contributions are: | Our contributions are: |
| 贡献 1 | A generative reconstruction framework that organizes driving observations into a compositional Gaussian scene, with world-space background and persistent canonical assets for state-driven reuse. | We introduce DriveCompose, a generative reconstruction framework that jointly completes background and canonical actor assets from driving observations. The resulting compositional Gaussian scene can be rendered under new camera and actor states using the same completed content. |
| 贡献 2 | A structured completion model that combines category-specific supports and scene-wide context with observed-code constraints, free-space suppression, and rendered observation checks. | We develop a structured conditional flow model that shares scene context across background and assets through cross-component memory. Observed-code and free-space constraints guide latent completion, while input-view checks validate the assembled scene against the recorded observations. |
| 论文组织 | 原文无此段。 | Section 2 reviews related work, Section 3 presents the method, and Section 4 reports experiments. Sections 5 and 6 discuss limitations and conclude. |

## 中文引言全文对照：A → D

| 部分 | 首轮修改前 A | 当前 D |
| --- | --- | --- |
| 背景与任务 | 驾驶数据集沿采集轨迹记录场景 [1, 31]。驾驶仿真和场景编辑要求重建结果在原始配置改变后仍然可用。移动相机会露出被车辆遮挡的道路，转动车辆会暴露未见的侧面，改变行人姿态则会使此前被遮挡的身体表面进入视野。这些操作既需要原始图像之外的几何与外观，也需要一种表示，使内容始终归属于同一个场景和资产身份。 | 驾驶数据集沿采集轨迹记录场景 [1, 31]。驾驶仿真和场景编辑要求重建结果在原始配置改变后仍然可用。移动相机、转动车辆或改变行人姿态，都会暴露此前未观测的表面。这些操作既需要原始图像之外的几何与外观，也需要一种表示，使内容始终归属于同一个场景和资产身份。 |
| 前馈恢复 | 近期前馈方法直接从时序观测恢复驾驶场景。STORM 通过估计场景流聚合动态高斯，DGGT 从无位姿图像联合恢复相机参数与动态场景内容 [3, 45]。StreetForward 和 PointForward 进一步研究时序处理及重建证据的组织方式 [6, 48]。对于后续需要移动或驱动的资产，还需将不同时刻的观测汇入稳定的局部表示，并为新状态暴露的表面提供内容。 | 近期前馈方法直接从时序观测恢复驾驶场景与运动 [3, 6, 45, 48]。仅恢复已观测内容，无法为后续资产运动暴露的未见表面提供内容。 |
| 可组合表示与生成 | 可组合表示解决了前一项需求。Street Gaussians 将车辆与背景分离，OmniRe 为刚体和关节对象建立规范模型，HUGSIM 将场景内容接入控制驱动的状态更新 [5, 43, 49]。生成模型则通过资产先验、高斯补全或生成视图处理缺失内容 [17, 44, 47, 51]。结合这些能力，需要生成器明确区分属于背景和各个资产的内容。生成的表面必须具有明确的归属、坐标系和运动规则，才能成为可编辑场景的一部分。 | 可组合表示将背景与参与者分离，并通过规范模型支持独立运动和控制 [5, 43, 49]。生成模型则通过资产先验、高斯补全或生成视图处理缺失内容 [17, 44, 47, 51]。结合这些能力，需要生成器明确区分属于背景和各个资产的内容。生成的表面必须具有明确的归属、坐标系和运动规则，才能成为可编辑场景的一部分。 |
| 关键见解 | 我们将驾驶场景重建建模为可组合场景的条件生成。表示的组织单位对应后续操作的对象：世界空间中的背景、局部坐标中的刚体车辆，以及带骨架绑定的规范人体表面。图像证据先在这些支撑上聚合，生成模型再根据已观测场景条件补全缺失潜码。每个补全表面都在所属组件的控制坐标系中解码。 | 我们将驾驶场景重建建模为可组合场景的条件生成。表示的组织单位对应后续操作的对象：世界空间中的背景、局部坐标中的刚体车辆，以及带骨架绑定的规范人体表面。在组件的控制坐标系中补全表面，使同一份生成内容在后续状态变化时仍保持身份归属（第 3.1 节）。图像证据先在这些支撑上聚合，生成模型再根据已观测场景条件补全缺失潜码。 |
| 方法概述 | DriveCompose 通过视觉恢复前端、结构化潜码和条件流模型实现这一形式（图 1）。前端估计几何、轨迹级身份和随时间变化的状态，规范聚合将不同视角、不同时刻对同一内容的观测汇集起来。在补全模型中，局部注意力沿各组件的支撑组织，共享记忆在背景与资产之间交换上下文。每个查询同时携带规范坐标及其在参考世界配置中的位置：前者标识持久内容，后者表达与场景的空间关系。类型专属解码器将完成的潜码转化为高斯组件。 | DriveCompose 通过视觉恢复前端、结构化潜码和条件流模型 [18] 实现这一形式（图 1）。前端估计几何、轨迹级身份和随时间变化的状态。在补全模型中，局部注意力沿各组件的支撑组织，共享记忆在背景与资产之间交换上下文。类型专属解码器将完成的潜码转化为高斯组件。 |
| 观测保持与复用 | 生成还需要遵循场景恢复所依据的图像。我们在采样过程中保留可靠的已见潜码，并抑制已知自由空间。新增内容仍可能遮挡已观测表面，因此还需在原始视角下检查装配后的候选场景。构建完成后，背景与规范资产保持固定，后续渲染由相机位置、车辆变换和人体关节姿态决定。学习过程遵循这一分工：先拟合恢复模块和潜表示，再训练补全先验，最后保持表示固定，通过可微渲染适配生成模型。 | 生成还需要遵循场景恢复所依据的图像。我们在采样过程中保留可靠的已见潜码，并抑制已知自由空间。新增内容仍可能遮挡已观测表面，因此还需在原始视角下检查装配后的候选场景。构建完成后，背景与规范资产保持固定，后续渲染由相机位置、车辆变换和人体关节姿态决定（第 3.5 节）。 |
| 贡献导语 | 本文的贡献包括： | 本文的贡献包括： |
| 贡献 1 | 提出生成式重建框架，将驾驶观测组织为可组合高斯场景，以世界空间背景和持久规范资产支持状态驱动复用。 | 提出生成式重建框架 DriveCompose，从驾驶观测中联合补全背景与规范参与者资产。所得可组合高斯场景可在新的相机和参与者状态下渲染，复用同一份补全内容。 |
| 贡献 2 | 建立结构化补全模型，将类别专属支撑和场景上下文与已见潜码约束、自由空间抑制及渲染观测检查结合。 | 设计结构化条件流模型，通过跨组件记忆在背景与资产之间共享场景上下文。已见潜码与自由空间约束引导潜空间补全，输入视角检查则验证装配后的场景与已记录观测的一致性。 |
| 论文组织 | 原文无此段。 | 第 2 节回顾相关工作，第 3 节介绍方法，第 4 节报告实验，第 5 和第 6 节分别讨论局限性并总结全文。 |

## 前一轮摘要记录：本轮全文保留

| 位置 | 原文状态 | 本轮改动及理由 |
| --- | --- | --- |
| 开头两句 | 新状态暴露未见表面，重建需要补全与稳定身份 | 原文保留，问题已经具体 |
| 方法命名句 | 从有标定图像序列重建可组合场景 | 原文保留，输入与方法定位清楚 |
| 方法中段 | 依次介绍编码器、聚合、潜表示、条件流、约束和解码 | 收束为“联合补全与控制坐标系的直觉”和“局部注意力/跨组件记忆及观测约束”两句 |
| 训练过程句 | 按四阶段复述训练流程 | 从摘要删除，原方法第 3.6 节仍保留；训练阶段不是摘要所需的主要论证 |
| 结果 | 原摘要没有数据集结果和关键数字 | 新增 Waymo 的 ±2 m 外推、nuScenes 零样本迁移，以及八个输入时间戳下的 CCM 消融结果 |
| 结尾 | 状态装配与持久输出分两句说明 | 合并为同一补全内容在不同状态下渲染，无需重新采样；保留原来有价值的机制含义 |

英文当前约 **169 词、8 句**（按空白分词，`±2 m` 计两个词），句长依次约为 16、23、16、27、24、27、17、19 词。对应 2 句问题、3 句方法、2 句结果、1 句意义，符合本轮 150–250 词目标。计数工具不同会有少量差异；没有为了凑句长修改保留句。

### 英文摘要修改前 B（全文）

Reusing a driving scene under new camera and actor states exposes surfaces that were never recorded. Reconstructing such a scene requires recovering the observed content, completing missing geometry and appearance, and retaining a stable identity for each movable component. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. A shared visual encoder estimates geometry, actor identities, and motion. We aggregate this evidence into world-space background queries and canonical vehicle and human queries, then encode them in a structured latent representation. A conditional flow model completes unknown codes while exchanging context across scene components. Observed codes and known free space constrain this generation process. Type-specific decoders produce Gaussian background and assets, which are checked against the input views before use. Learning proceeds from visual recovery and latent representation fitting to completion-prior training and adaptation with rendered observations. The reconstructed scene is subsequently composed under explicit camera, rigid-body, and skeletal states. This formulation gives generation a persistent three-dimensional output: the same completed content can be rendered along different trajectories without resampling its geometry or appearance.

### 当前英文摘要 C = D（全文）

Reusing a driving scene under new camera and actor states exposes surfaces that were never recorded. Reconstructing such a scene requires recovering the observed content, completing missing geometry and appearance, and retaining a stable identity for each movable component. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. It jointly completes a world-space background and canonical vehicle and human assets, so generated surfaces inherit the coordinate frames and motion bindings used for later scene editing. A conditional flow model combines local attention with cross-component memory, while observed codes, known free space, and input-view checks constrain the completed Gaussian scene. On Waymo, DriveCompose reduces FID from 83.72 to 37.43 relative to STORM for ±2 m camera shifts, and reaches 26.47 dB PSNR in zero-shot transfer to nuScenes. Cross-component memory lowers unseen-surface RGB error by 20.5% relative to isolated per-component memories with eight input timestamps. The resulting scene can be rendered under different camera and actor states without resampling its completed geometry or appearance.

### 中文摘要修改前 B（全文）

在新的相机和交通参与者状态下复用驾驶场景，会暴露原始日志未曾记录的表面。重建这样的场景，需要恢复已观测内容、补全缺失的几何与外观，并为各个可移动组件保持稳定的身份。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。共享视觉编码器估计几何、资产身份和运动；我们将这些证据聚合到世界空间的背景查询及车辆、人体的规范查询，并编码为结构化潜表示。条件流模型在场景组件之间交换上下文，补全未知潜码，生成过程受已见潜码和已知自由空间约束。类型专属解码器输出高斯背景与资产，随后在输入视角下检查重建结果。学习过程依次包括视觉恢复、潜表示拟合、补全先验训练和基于渲染观测的适配。重建场景通过显式的相机、刚体和骨架状态进行装配。这一形式为生成过程提供了持久的三维输出：同一份补全内容可以沿不同轨迹渲染，无需重新采样几何或外观。

### 当前中文摘要 C = D（全文）

在新的相机和交通参与者状态下复用驾驶场景，会暴露原始日志未曾记录的表面。重建这样的场景，需要恢复已观测内容、补全缺失的几何与外观，并为各个可移动组件保持稳定的身份。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。该框架联合补全世界空间背景与规范车辆、人体资产，使生成表面继承后续场景编辑所用的坐标系与运动绑定。条件流模型结合局部注意力与跨组件记忆，已见潜码、已知自由空间和输入视角检查共同约束补全后的高斯场景。在 Waymo 的 ±2 m 相机偏移下，DriveCompose 相较于 STORM 将 FID 从 83.72 降至 37.43；零样本迁移至 nuScenes 时达到 26.47 dB PSNR。在使用八个输入时间戳时，跨组件记忆相较于各组件独立记忆，将未见表面的 RGB 误差降低了 20.5%。所得场景可在不同相机和参与者状态下渲染，无需重新采样已补全的几何或外观。

## 主张与全文证据的对应

| 摘要/贡献中的内容 | 已有来源 | 表述边界 |
| --- | --- | --- |
| 新状态暴露未见表面，内容需要身份与控制关系 | 引言第 1、3 段；Related Work 的可组合场景与生成补全部分；对应原有文献 | 任务与表示需求，没有断言所有已有方法都无此能力 |
| 背景与规范车辆/人体联合补全，生成内容继承身份、坐标与绑定 | 方法 3.1–3.4；结构化潜表示、类型解码及人车绑定 | 方法机制，有明确设计依据；不是独立的编辑质量排名 |
| 局部注意力与跨组件记忆 | 方法 3.4；英文表 4、中文组件消融表 | 未把标准注意力或条件流的使用本身写成首创 |
| 已见潜码、自由空间、输入视角检查 | 方法 3.3–3.5 的逐查询解码、投影采样与原视角检查 | 描述约束机制，不声称像素绝对不变或所有候选均通过 |
| Waymo ±2 m FID：STORM 83.72 → Ours 37.43 | 英文表 2，`tab:spatial_current` | 左、右偏移分别评价后的平均；该列 STORM 是所列基线中最低 FID。不是左偏 2 m 单独得分，不是 FVD |
| nuScenes：26.47 dB PSNR | 英文表 3，`tab:generalization` | Waymo 训练检查点直接迁移，参数固定；不是在 nuScenes 上重新训练 |
| 未见表面 RGB 误差降低 20.5% | 英文表 4、两版组件消融：w/o CCM 的 New-MAE 0.078，Ours 0.062；(0.078−0.062)/0.078 ≈ 20.5% | 八个输入时间戳、三相机；与各组件独立记忆比较。数值来自作者既有汇总，本轮只复核算术，不声称重新运行实验或核验原始日志 |
| 构建后的场景可按状态渲染，无需重新采样内容 | 方法 3.5 状态装配及 3.6 推理流程 | 表示和运行方式的能力；不将外推指标扩大为任意人体动作的质量或闭环策略效果 |

现有中文实验尚未同步英文主结果表和 nuScenes 迁移小节。本轮两版摘要采用英文主稿中的同一组已提供数值；这处已有的实验双语差异留待实验章节同步处理，不假称整篇两版已经完全一致。本轮没有顺带改写实验。

## 首轮 A → B 的修改理由（保留记录）

| 位置 | 首轮改动 | 理由与保留内容 |
| --- | --- | --- |
| 第 1 段 | 三个展开案例合并为一句 | 都解释“新状态暴露未见表面”；保留相机、车辆、人体三个对象 |
| 第 2 段 | 四篇逐项介绍改为类别概括，并直说缺口 | 原引用保留，逐篇机制仍在 Related Work；缺口限定为仅恢复已观测内容 |
| 第 3 段 | 可组合表示逐篇介绍改为共性 | 保留对前人能力的肯定，删除依赖上段措辞的指代 |
| 第 4 段 | 解码说明改为控制坐标系为何有用，并提前 | 让关键见解先于聚合和补全操作；表示细节仍在方法 3.1 |
| 第 5 段 | 删除重复聚合与双坐标解释 | 第 4 段已说聚合，方法 3.2/3.4 已有双坐标机制；保留局部注意力、共享记忆及解码 |
| 第 6 段 | 删除四阶段训练复述 | 该段集中说明观测保持与复用；训练完整保留在方法 3.6 |
| 结尾 | 增加组织说明 | 按用户要求提供章节导航；首轮两项贡献文字未改 |
| 引用/排版 | Flow Matching 基础引用、自身方法交叉引用、英文贡献前 Needspace | 引用来源明确；避免贡献导语独留上一页。本轮沿用这些改动 |

## 验证与保留项

- 本轮脚本逐项确认：中英文引言的贡献列表之前及之后均与本轮基线完全一致。
- 两版摘要全文与本轮基线 C 一致；实验数值、表格和图件未改，标题未改。
- 中英文贡献和摘要的科学含义、关键数字、比较对象和八时间戳条件对应；文献键未改，保留的交叉引用均可解析。
- 英文摘要与引言的 prose-quality 检查通过；结果只是辅助检查，已结合全文人工复读机制与证据关系。
- 两版 XeLaTeX 构建退出码均为 0；无未定义引用、缺字、Overfull 等编译问题；已渲染查看两版受影响的前两页，英文贡献导语与列表位于同页。
- 正式输出仍为 `paper/build/en/main.pdf`（12 页）与 `paper/build/zh/main_zh.pdf`（10 页）。英文局限性、结论仍在第 10 页，尚未达到 8 页正文目标。
- 本轮没有提交或推送 GitHub；保留用户已有的图件移动及其他未提交内容。

## 2026-10-25：3.6 训练与推理 PPT 草图（未替换正文）

基线：`c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb`。本轮只绘制原生可编辑的双语 PPT，未改 LaTeX、摘要或正式 PDF，未提交或推送。

- 当前问题：3.6 各段反复说明模块冻结与更新关系；推理段重复前文的构建和复用链路。
- 草图方案：用四阶段训练表对照可训练模块与监督目标；用连线展示恢复、补全、解码、原视角检查、接受及状态驱动渲染。
- 保留条件：共享查询布局、完整未知查询目标、适配仅更新 GCM、检查后才能复用；短版文字另保留先验回放和观测锚点机制。
- 篇幅取舍：图按英文双栏通栏宽度约占 0.29 页，尚未计图注与配套文字；相比当前约 0.46 页的 3.6，不保证显著省页。纯文字略写或并入已有总览图可能更省。尚未进行主稿插图与编译测量。
- 双语渲染和原生对象边界检查通过，每页 20 个原生对象、0 个图片对象。

[可编辑 PPT](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/training-inference.pptx) · [英文预览](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/training-inference-en.png) · [中文预览](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/training-inference-zh.png) · [拟替换短文、原因及篇幅评估](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/README.md)。短文只是草案，未写入正文。

## 2026-10-25：训练与推理图的 imagegen 视觉草案

按用户要求使用内置 image_gen，将文字表格改为四阶段视觉卡片与推理流程。当前工具不暴露模型选择，未核实为 image-2.5。原 PPT 保留，主稿及正式 PDF 未改。

- 原来：训练阶段依赖长句和重复 Train/Frozen 单元格；现在：用模块颜色、冻结锁标记、查询网格和连线呈现。
- 原来：推理以文字框为主；现在：以示意输入、潜码、固定场景图形区分一次构建与状态复用。
- 检查并修正：完整监督目标与预测输出分开；适配仅回传更新 GCM；渲染步骤明确标注；街景均为生成式示意，不是实验结果。
- 这是位图视觉草案，不是更新后的原生 PPT；未据此宣称主稿节省页数。

[图稿](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/training-inference-illustrated.png) · [完整生成与修正提示词](../../_archive/drivecompose/20261026-tracked-intermediates/paper/fig/training-inference/imagegen-prompt.txt)。


## 2026-10-25：3.6 紧凑训练表试排（已应用）

基线提交：`c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb`。本轮开始时两版方法源文件与该提交一致；真实工作区基线另保存在 `paper/build/training-table/before-en.tex`、`before-zh.tex`。此前图稿、对照日志及用户图件移动不计入本轮修改。

范围：仅替换两版 3.6；补充 B 已含原详细内容，无需重复迁移。摘要、引言、3.1–3.5、实验源文和数值均不变。新增表格使后续表号自动递增，交叉引用已重新编译。

### 修改依据与去向

| 位置 | 原问题 | 局部替换 | 内容去向 |
| --- | --- | --- | --- |
| 四阶段段落 | 反复说明更新和冻结关系 | 单栏四行训练表，列明 R/C/G 状态和监督 | 监督细节已在补充 B，正文保留关键条件 |
| 阶段二 | 查询布局对应关系展开较长 | 一句保留位置、类型、顺序、归属完全共享 | 另建布局会改变预测变量的解释仍在补充 B |
| 阶段三 | 冻结关系与表格重复 | 正文保留每个未知查询有完整有效目标及 flow-loss 引用 | 不改变完整目标要求 |
| 阶段四 | 模块状态、反传路径、监督说明混在长段内 | 表格说明状态和约束，短文保留反传路径、先验交替和观测锚点 | 自由射线和几何约束细节仍在补充 B |
| 推理 | 与 3.4–3.5 重复展开 | 一句保留日志一次编码、固定支撑证据、检查后复用并引用 3.5 | 完整流程也保留在补充 B |

### 英文实测

| 项目 | 修改前 | 修改后 |
| --- | --- | --- |
| 主稿总页数（含参考文献） | 11 | 11 |
| 正文结束 | 第 9 页左栏，距页顶 599.63 pt | 第 9 页左栏，距页顶 294.34 pt |
| 正文页当量 | 8.407 | 8.172 |

净减少约 **0.236 页**，约占本轮前超出 8 页空间的 58%。页当量按两栏各 648 pt、正文顶部 72 pt 计算，包含实际浮动重排影响；不是严格投稿页数。正文仍延续到第 9 页，尚未达到 8 页目标。

### 检查

两版 latexmk/XeLaTeX 成功退出；英文 11 页、中文 9 页。无 Overfull、未定义引用或缺字警告。已目视检查英文训练表、重排后的第 6–9 页，以及中文训练表页。未修改模板字号、页边距或全局行距；训练表采用常规 small 字号和 booktabs，未使用缩放或负间距。补充材料未改，无需重编译。


### 英文 3.6 完整前后对照

修改前：

```latex
\subsection{Training procedure}
\label{sec:training}

Learning is divided into four stages so that the completion target has a stable meaning. Detailed supervision, losses, and conditioning perturbations are provided in Appendix B of the supplementary material.

\paragraph{Stage 1: visual recovery.}

We supervise the image encoder, geometry heads, identity slots, and state heads using geometry, semantics, instance assignments, and actor annotations. These targets establish the coordinate and identity consistency required by aggregation.

\paragraph{Stage 2: latent representation fitting.}

We freeze recovery and train the type-specific encoders and decoders. For each sample, partial input establishes the query layout once. More complete observations are then aggregated on exactly the same positions, types, order, and ownership. This correspondence is required for latent completion: separately rebuilding a complete-scene layout would change the variables being predicted. RGB, depth, and silhouette supervision train the decoded scene, with empty-space opacity and Gaussian-scale regularization.

\paragraph{Stage 3: completion-prior learning.}

We freeze recovery and the entire codec, encode complete targets as $\mathbf z_1$, and optimize the completion transformer with Eq.~\ref{eq:flow-loss}. Complete scene or asset examples must provide a valid target for every unknown query in Eq.~\ref{eq:flow-path}; partial real logs alone do not meet this condition. Target codes and input codes retain the same codec and query definition throughout this stage.

\paragraph{Stage 4: adaptation through rendering.}

Keeping recovery and the codec frozen, we differentiate through flow integration, decoding, and rendering to update only the completion network. Partial real logs supervise the rendered observations. Known-free rays and geometric backend samples constrain added content. Complete-target samples can be interleaved with real-log adaptation to retain the learned prior, with each loss term applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration.

\paragraph{Inference.}

A log is encoded once, its support and evidence are fixed, and the completion model integrates the unknown codes. We then decode and check the scene before exporting its fixed content. Runtime rendering uses only this content and the requested states.
```

修改后：

```latex
\subsection{Training procedure}
\label{sec:training}

Learning is divided into four stages so that the completion target has a stable meaning (Table~\ref{tab:training}).

\begin{table}[t]
\centering
\small
\caption{Training schedule. R: recovery; C: codec; G: GCM. T: trained; F: frozen; --: unused.}
\label{tab:training}
\begin{tabular}{@{}lccc p{0.43\linewidth}@{}}
\toprule
Stage & R & C & G & Supervision \\
\midrule
Recovery & T & -- & -- & Geometry, semantics, identity, states \\
Codec & F & T & -- & Partial / complete observations \\
Prior & F & F & T & Complete targets \\
Adaptation & F & F & T & Real-log rendering and scene constraints \\
\bottomrule
\end{tabular}
\end{table}

For codec fitting, partial input and more complete observations share the same query positions, types, order, and ownership. With recovery and the entire codec frozen, complete scene or asset examples provide a valid target for every unknown query to train the GCM with Eq.~\ref{eq:flow-loss}. Real-log adaptation differentiates through flow integration, decoding, and rendering to update only the GCM. Complete-target samples can be interleaved to retain the prior, with each loss applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration. Detailed supervision, losses, and conditioning perturbations are provided in Appendix B of the supplementary material.

At inference, a log is encoded once; its support and evidence remain fixed during completion, and the decoded scene is checked before reuse under requested states (Section~\ref{sec:composition}).
```


### 中文 3.6 完整前后对照

修改前：

```latex
\subsection{训练过程}
\label{sec:training}

学习分为四个阶段，使补全目标具有稳定含义。详细监督、损失和条件扰动见补充材料附录 B。

\paragraph{阶段一：视觉恢复。}

我们利用几何、语义、实例归属和资产标注监督图像编码器、几何头、身份槽及状态头。这些目标建立聚合所需的坐标与身份一致性。

\paragraph{阶段二：潜表示拟合。}

冻结恢复模块，训练类型专属编码器和解码器。每个样本先由部分输入建立一次查询布局，再将更完整的观测聚合到完全相同的位置、类型、顺序和归属上。这种对应关系是潜码补全的前提；若为完整场景另建布局，就会改变待预测变量。RGB、深度和轮廓监督训练解码场景，并结合空域不透明度与高斯尺度正则。

\paragraph{阶段三：补全先验学习。}

冻结恢复模块和整个编解码器，将完整目标编码为 $\mathbf z_1$，并以式~\ref{eq:flow-loss} 优化补全 Transformer。完整场景或资产样本必须为式~\ref{eq:flow-path} 中的每个未知查询提供有效目标，单独的部分真实日志不满足这一条件。该阶段中，目标潜码和输入潜码始终使用相同的编解码器与查询定义。

\paragraph{阶段四：通过渲染适配。}

保持恢复模块与编解码器冻结，通过流积分、解码和渲染反向传播，仅更新补全网络。部分真实日志监督渲染观测，已知自由射线和几何后端样本约束新增内容。完整目标样本可与真实日志适配交替使用以保留先验，各损失项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。

\paragraph{推理。}

日志只编码一次，随后固定支撑与证据，由补全模型积分未知潜码。解码并检查场景后，导出固定内容；运行时渲染仅使用这些内容和指定状态。
```

修改后：

```latex
\subsection{训练流程}
\label{sec:training}

学习分为四个阶段，使补全目标保持稳定的含义（表~\ref{tab:training}）。

\begin{table}[t]
\centering
\small
\caption{训练阶段。R：恢复模块；C：编解码器；G：GCM。T：训练；F：冻结；--：未使用。}
\label{tab:training}
\begin{tabular}{@{}lccc p{0.43\linewidth}@{}}
\toprule
阶段 & R & C & G & 监督 \\
\midrule
视觉恢复 & T & -- & -- & 几何、语义、身份、状态 \\
表示拟合 & F & T & -- & 部分与完整观测 \\
补全先验 & F & F & T & 完整目标 \\
渲染适配 & F & F & T & 真实日志渲染与场景约束 \\
\bottomrule
\end{tabular}
\end{table}

编解码器拟合时，部分输入与更完整观测共享相同的查询位置、类型、顺序和归属。随后冻结恢复模块与整个编解码器，使用为每个未知查询提供有效目标的完整场景或资产样本，以式~\ref{eq:flow-loss} 训练 GCM。真实日志适配通过流积分、解码和渲染反向传播，仅更新 GCM。完整目标样本可交替使用以保留先验，各损失项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。详细监督、损失和条件扰动见补充材料附录 B。

推理时，日志只编码一次，补全过程中支撑与证据保持固定；解码后的场景通过检查后，按指定状态复用（第~\ref{sec:composition} 节）。
```


## 2026-10-25：方法概述、3.1 与 3.3 的内容整理（已应用）

本轮基于未提交工作区：包括上一轮已经完成的 3.6 训练表。Git HEAD 为 `c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb`，但本轮对照以 `paper/build/method-compression/baseline.json` 保存的实际源文件为准，不能拿 HEAD 代替本轮基线。主稿基线亦保存在同目录的 before-en.tex / before-zh.tex。

### 范围、理由与去向

| 位置 | 原问题 | 实际处理 | 保留与去向 |
| --- | --- | --- | --- |
| 方法概述 | 六句逐节导航重复 Figure 1 和正文结构 | 保留首句组织原则与总览图引用，删除重复导航 | 无技术内容丢失 |
| 3.1 输入 | 在问题定义前展开相机变换和图像预处理 | 主稿保留日志、标定和位姿来源 | 原完整输入段落迁入补充 D 的 Input conventions and preprocessing |
| 3.1 高斯属性 | 主稿逐项解释标准高斯属性 | 保留 Gaussian splatting 引用，缩成组件渲染说明 | 中心、协方差、不透明度和方向外观定义移入补充 E |
| 3.3 解码 | 参数化公式和外观实现打断机制说明 | 主稿概括每查询 K 个子高斯、支撑限制、运动绑定与自由空间约束 | 原解码段落完整保存在新增补充 E；中心公式变为 S13 |
| 3.3 观测保持 | 核心性质已经清楚 | 原句逐字保留，并独立成段 | 未改已见潜码不变→高斯参数不变的条件与结论 |

未改 3.2、3.4、3.5、3.6 的源文；摘要、引言、实验源文与数值未改。主稿删除一条参数化公式，后续公式自动减一；补充 B 对主稿 flow loss / flow path 的数字引用同步由 10 / 9 更新为 9 / 8。这是必要跨文件依赖更新。

### 英文实际篇幅与编译

| 项目 | 本轮前 | 本轮后 |
| --- | --- | --- |
| Method 页当量（标题至 Experiments 标题） | 2.528 | 2.403 |
| 正文页当量 | 8.172 | 8.074 |
| 正文最后一行位置 | 第 9 页左栏，距页顶 294.34 pt | 第 9 页左栏，距页顶 167.81 pt |
| 英文主稿总页数 | 11 | 11 |
| 英文补充总页数 | 3 | 4 |

Method 减少约 0.125 页；整稿因分页和浮动重排，净减少约 0.098 页。第 9 页仍有约 8 行结论，尚未满足 8 页正文目标。页当量按双栏每栏 648 pt、正文顶部 72 pt 计，不等于正式投稿页数。

中英文主稿及补充材料均经 latexmk/XeLaTeX 成功编译，输出分别为 11 / 9 / 4 / 3 页。未发现 Overfull、缺字或未定义引用。已核对公式编号，目视检查主稿受影响的方法页和结论页，以及双语补充 D/E。模板字体、边距、行距未调整。未提交或推送。

### 本轮实际双语差异

#### sec/3_method.tex

```diff
--- 本轮修改前/sec/3_method.tex
+++ 本轮修改后/sec/3_method.tex
@@ -1,11 +1,11 @@
 \section{Method}\label{sec:method}

-DriveCompose reconstructs a driving scene in the units that will later be controlled. We first recover visual evidence and aggregate it on background and canonical asset supports (Secs.~\ref{sec:representation}--\ref{sec:queries}). A typed codec defines the latent variables and their Gaussian decoding (Sec.~\ref{sec:codec}). Conditional flow completes missing content in this representation (Sec.~\ref{sec:completion}), after which the scene is composed and checked in the observed views (Sec.~\ref{sec:composition}). Section~\ref{sec:training} describes how these modules are learned. Figure~\ref{fig:teaser} shows the complete construction and reuse path.
+DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:teaser} shows the complete construction and reuse path.

 \subsection{Problem formulation and compositional representation}
 \label{sec:representation}

-The input is a synchronized log of images $\mathbf I_{t,v}$, timestamps, intrinsics $\mathbf K_v$, and camera-to-rig calibration $\mathbf T^r_{c_v}$. Rig poses $\mathbf T^w_r(t)$ are provided or estimated relative to the first frame, giving camera poses $\mathbf T^w_{c_v}(t)=\mathbf T^w_r(t)\mathbf T^r_{c_v}$. Transforms act on column vectors and distances are in meters. Images follow a rectified pinhole model and linear RGB; distortion, rolling shutter, and exposure differences are handled before evidence aggregation.
+The input is a synchronized image log $\mathbf I_{t,v}$ with timestamps, camera intrinsics, and camera-to-rig calibration. Rig poses are provided or estimated relative to the first frame. Coordinate conventions and image preprocessing are detailed in Appendix D of the supplementary material.

 The output is a compositional Gaussian scene

@@ -15,7 +15,7 @@
 \label{eq:world}
 \end{equation}

-where $\mathcal G_b$ is the world-space background, $C_{\rm sky}$ a sky cubemap, $V_{\rm sky}$ its supported directions, $\mathcal A_a$ the canonical asset for identity $a$, $\mathcal B$ the finite spatial support, and $\xi$ the sampling seed. A Gaussian stores its center $\boldsymbol\mu$, covariance $\boldsymbol\Sigma$, opacity $\alpha$, and directional appearance, and is rendered by Gaussian splatting~\cite{kerbl2023gaussians}. Vehicles retain local geometry and dimensions. Humans additionally retain a rest skeleton and skinning weights. Scene state controls the placement and articulation of these fixed components.
+where $\mathcal G_b$ is the world-space background, $C_{\rm sky}$ a sky cubemap, $V_{\rm sky}$ its supported directions, $\mathcal A_a$ the canonical asset for identity $a$, $\mathcal B$ the finite spatial support, and $\xi$ the sampling seed. The components are rendered by Gaussian splatting~\cite{kerbl2023gaussians}. Vehicles retain local geometry and dimensions. Humans additionally retain a rest skeleton and skinning weights. Scene state controls the placement and articulation of these fixed components.

 We model missing content through conditional generation. Let $\mathcal Q$ be the recovered query layout and $C$ its observed evidence. The completion model samples unknown codes $\mathbf z_u$, while the codec $D_\psi$ decodes the assembled codes into scene content:

@@ -73,17 +73,9 @@

 Type-specific encoders map $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$ to codes $\mathbf z_i\in\mathbb R^D$. Each query keeps its type, ownership, and coordinate frame even though all codes have the same dimension. Visibility masks and confidence are supplied separately to the completion model. Partial and complete observations therefore use the same intrinsic encoding map. Before conditioning, unobserved codes are set to zero; the observed subset is denoted $\mathbf z^{\rm obs}$.

-Background, vehicle, and human decoders independently map each query to $K$ child Gaussians. For child $k$ of query $i$, the center is confined to its support cell:
+Background, vehicle, and human decoders independently map each query to $K$ child Gaussians confined to its support cell. Human children inherit the query's skinning weights; vehicle children share their asset's rigid transform. Opacity is multiplied by $1-f_i$, so free queries cannot produce visible Gaussians. A separate sky head predicts cubemap colors within the observation-supported domain $V_{\rm sky}$. Gaussian and appearance parameterizations are detailed in Appendix E of the supplementary material.

-\begin{equation}
-\boldsymbol\mu_{i,k}=\mathbf q_i+
-\tfrac12\boldsymbol\delta_i\odot\tanh(\mathbf b_{i,k}).
-\label{eq:child-center}
-\end{equation}
-
-Positive scales and normalized rotations determine positive-definite covariance. Opacity is multiplied by $1-f_i$, so free queries cannot produce visible Gaussians. Human children inherit the skinning weights of their support query; vehicle children share their asset's rigid transform. A separate sky head predicts cubemap colors, with the observation-supported domain retained in $V_{\rm sky}$.
-
-Appearance uses a constant RGB term and three local directional coefficients per channel, evaluated as $c(d)=\max(0,c_0+C_{\rm app}\hat d_{\rm local})$. Decoding is per query: once the codec is frozen, an unchanged observed code produces unchanged Gaussian parameters. The completion network can exchange context across queries without changing this decoding property.
+Decoding is per query: once the codec is frozen, an unchanged observed code produces unchanged Gaussian parameters. The completion network can exchange context across queries without changing this decoding property.

 \subsection{Conditional generative reconstruction}
 \label{sec:completion}
```

#### zh/3_method_zh.tex

```diff
--- 本轮修改前/zh/3_method_zh.tex
+++ 本轮修改后/zh/3_method_zh.tex
@@ -1,11 +1,11 @@
 \section{方法}\label{sec:method}

-DriveCompose 按照后续控制的单位重建驾驶场景。我们首先恢复视觉证据，并在背景与规范资产支撑上聚合（第~\ref{sec:representation}--\ref{sec:queries} 节）；类型专属编解码器定义潜变量及其高斯解码（第~\ref{sec:codec} 节）。条件流在该表示中补全缺失内容（第~\ref{sec:completion} 节），随后装配场景并在观测视角下检查（第~\ref{sec:composition} 节）。第~\ref{sec:training} 节说明各模块的学习过程。图~\ref{fig:teaser} 展示完整的构建与复用链路。
+DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:teaser} 展示完整的构建与复用链路。

 \subsection{问题定义与可组合表示}
 \label{sec:representation}

-输入是同步图像 $\mathbf I_{t,v}$、时间戳、内参 $\mathbf K_v$ 及相机到传感器支架的标定 $\mathbf T^r_{c_v}$。支架位姿 $\mathbf T^w_r(t)$ 由日志提供，或以第一帧为参考估计；相机位姿为 $\mathbf T^w_{c_v}(t)=\mathbf T^w_r(t)\mathbf T^r_{c_v}$。变换作用于列向量，距离单位为米。图像采用校正后的针孔模型与线性 RGB；畸变、滚动快门和曝光差异在证据聚合之前处理。
+输入是同步图像日志 $\mathbf I_{t,v}$、时间戳、相机内参及相机到传感器支架的标定。支架位姿由日志提供，或以第一帧为参考估计。坐标约定与图像预处理见补充材料附录 D。

 输出为可组合高斯场景

@@ -15,7 +15,7 @@
 \label{eq:world}
 \end{equation}

-其中，$\mathcal G_b$ 是世界空间背景，$C_{\rm sky}$ 是天空立方体贴图，$V_{\rm sky}$ 表示其有效方向，$\mathcal A_a$ 是身份 $a$ 对应的规范资产，$\mathcal B$ 是有限空间支撑，$\xi$ 是采样种子。每个高斯存储中心 $\boldsymbol\mu$、协方差 $\boldsymbol\Sigma$、不透明度 $\alpha$ 和方向外观，并通过高斯泼溅渲染~\cite{kerbl2023gaussians}。车辆保留局部几何与固定尺寸，人体另存静止骨架和蒙皮权重。场景状态控制这些固定组件的放置与关节运动。
+其中，$\mathcal G_b$ 是世界空间背景，$C_{\rm sky}$ 是天空立方体贴图，$V_{\rm sky}$ 表示其有效方向，$\mathcal A_a$ 是身份 $a$ 对应的规范资产，$\mathcal B$ 是有限空间支撑，$\xi$ 是采样种子。这些组件通过高斯泼溅渲染~\cite{kerbl2023gaussians}。车辆保留局部几何与固定尺寸，人体另存静止骨架和蒙皮权重。场景状态控制这些固定组件的放置与关节运动。

 我们通过条件生成建模缺失内容。令 $\mathcal Q$ 为恢复得到的查询布局，$C$ 为其观测证据。补全模型采样未知潜码 $\mathbf z_u$，编解码器 $D_\psi$ 将组合后的潜码解码为场景内容：

@@ -73,17 +73,9 @@

 类型专属编码器将 $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$ 映射为潜码 $\mathbf z_i\in\mathbb R^D$。各潜码维度相同，但查询仍保留类型、归属和坐标系。可见性掩码与置信度单独提供给补全模型，使部分观测与完整观测使用同一潜码编码映射。作为条件输入之前，未观测潜码置零；已见子集记为 $\mathbf z^{\rm obs}$。

-背景、车辆和人体解码器分别将每个查询独立映射为 $K$ 个子高斯。查询 $i$ 的子高斯 $k$ 的中心被限制在其支撑单元内：
+背景、车辆和人体解码器分别将每个查询独立映射为限制在其支撑单元内的 $K$ 个子高斯。人体子高斯继承查询的蒙皮权重；车辆子高斯共用所属资产的刚体变换。不透明度乘以 $1-f_i$，使自由空间查询不能产生可见高斯。独立天空头在观测支持的方向域 $V_{\rm sky}$ 内预测立方体贴图颜色。高斯与外观参数化详见补充材料附录 E。

-\begin{equation}
-\boldsymbol\mu_{i,k}=\mathbf q_i+
-\tfrac12\boldsymbol\delta_i\odot\tanh(\mathbf b_{i,k}).
-\label{eq:child-center}
-\end{equation}
-
-正尺度与归一化旋转确定正定协方差。不透明度乘以 $1-f_i$，使自由空间查询不能产生可见高斯。人体子高斯继承支撑查询的蒙皮权重；车辆子高斯共用所属资产的刚体变换。独立天空头预测立方体贴图颜色，并在 $V_{\rm sky}$ 中保留观测支持的方向域。
-
-外观为每个颜色通道存储常数 RGB 项和三个局部方向系数，按 $c(d)=\max(0,c_0+C_{\rm app}\hat d_{\rm local})$ 求值。解码逐查询执行：编解码器冻结后，不变的已见潜码产生不变的高斯参数。补全网络可以在查询之间交换上下文，同时保留这一解码性质。
+解码逐查询执行：编解码器冻结后，不变的已见潜码产生不变的高斯参数。补全网络可以在查询之间交换上下文，同时保留这一解码性质。

 \subsection{条件生成式重建}
 \label{sec:completion}
```

#### supplementary/frontend.tex

```diff
--- 本轮修改前/supplementary/frontend.tex
+++ 本轮修改后/supplementary/frontend.tex
@@ -1,5 +1,9 @@
 \section{Visual recovery and aggregation details}
 \label{sec:supp-queries}
+
+\paragraph{Input conventions and preprocessing.}
+
+The input is a synchronized log of images $\mathbf I_{t,v}$, timestamps, intrinsics $\mathbf K_v$, and camera-to-rig calibration $\mathbf T^r_{c_v}$. Rig poses $\mathbf T^w_r(t)$ are provided or estimated relative to the first frame, giving camera poses $\mathbf T^w_{c_v}(t)=\mathbf T^w_r(t)\mathbf T^r_{c_v}$. Transforms act on column vectors and distances are in meters. Images follow a rectified pinhole model and linear RGB; distortion, rolling shutter, and exposure differences are handled before evidence aggregation.

 \paragraph{Shared visual encoding.}

```

#### supplementary/frontend_zh.tex

```diff
--- 本轮修改前/supplementary/frontend_zh.tex
+++ 本轮修改后/supplementary/frontend_zh.tex
@@ -1,5 +1,9 @@
 \section{视觉恢复与聚合细节}
 \label{sec:supp-queries}
+
+\paragraph{输入约定与预处理。}
+
+输入是同步图像 $\mathbf I_{t,v}$、时间戳、内参 $\mathbf K_v$ 及相机到传感器支架的标定 $\mathbf T^r_{c_v}$。支架位姿 $\mathbf T^w_r(t)$ 由日志提供，或以第一帧为参考估计；相机位姿为 $\mathbf T^w_{c_v}(t)=\mathbf T^w_r(t)\mathbf T^r_{c_v}$。变换作用于列向量，距离单位为米。图像采用校正后的针孔模型与线性 RGB；畸变、滚动快门和曝光差异在证据聚合之前处理。

 \paragraph{共享视觉编码。}

```

补充 E 完整内容：[英文](../paper/supplementary/codec.tex) · [中文](../paper/supplementary/codec_zh.tex)。


## 2026-10-25：合并消融协议与分析，英文正文收进 8 页

本轮基线为上一轮未提交工作区（已完成方法概述及 3.1/3.3 压缩）；源文件快照保存于 `paper/build/ablation-merge/before-en.tex` 和 `before-zh.tex`。Git HEAD `c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb` 不代表本轮原文。

### 实际调整与原因

- 英文 4.4 Ablation protocol 与 4.5 Ablation studies 合并为 4.4 Ablation studies；原 4.6 State-driven reuse 自动变为 4.5。三个旧 section label 全保留，指向合并后小节。
- 中文对应的 4.3 消融实验协议与 4.4 消融分析合并为 4.3 消融分析；原状态复用变为 4.4。中文前部原有章节差异未在本轮扩展修改。
- 两个表注删除与 Protocol / Metrics 重复的 GCM/CCM 展开、相机数、24 步、RGB 尺度等说明。组件表仍明确 T=8、24 张图像、共享模块和评价掩码、接受筛选前的质量与全申请世界 Pass；输入表仍明确固定权重与目标、共同未见区域及 T=8 对应关系。
- 完整协议、时间戳、种子、评价定义、全部结果分析和表格数值原样保留。本轮未将实验内容移至补充材料。

### 验证

脚本核对：除上述标题、label 位置和两个表注外，两版实验源文完全一致（忽略空白）。因此数字、协议和结果解释均未改。

两版 latexmk/XeLaTeX 成功编译，无 Overfull、缺字或未定义引用。目视检查英文第 6–9 页及中文受影响页面；正文图表、局限性和结论均在英文第 8 页结束，第 9 页从 References 开始。英文总页数仍为 11，中文总页数仍为 9。未修改字号、边距、行距、图表尺寸或浮动参数；未提交或推送。

这是当前模板下的正文篇幅检查通过，不代替最终投稿模板、匿名性和其他投稿要求核查。

### en：实际前后对照

```diff
--- before/sec/4_experiments.tex
+++ after/sec/4_experiments.tex
@@ -129,9 +129,10 @@
 % Keep natural paragraph spacing around the remaining experiment tables.
 \raggedbottom
-\subsection{Ablation protocol}
+\subsection{Ablation studies}
 \label{sec:ablation-protocol}
 \label{sec:ablations}
-
-\paragraph{Inputs and controls.}
+\label{sec:ablation-studies}
+
+\paragraph{Protocol.}
 Paired evaluation of hidden surfaces is defined on independent complete-reference scenes; Waymo logs provide recorded-view evaluation.
 Each 29-timestamp window uses three synchronized cameras: front, front-left, and front-right.
@@ -154,7 +155,4 @@
 Metrics are averaged within each scene and then across scenes and training seeds.

-\subsection{Ablation studies}
-\label{sec:ablation-studies}
-
 \paragraph{Completion and scene context.}
 Table~\ref{tab:ablation-components} compares the full model with two controls.
@@ -169,5 +167,5 @@
 \begin{table}[t]
   \centering
-  \caption{\textbf{Component ablations.} GCM and CCM denote the generative completion and cross-component memory modules. All variants use $T=8$ and three cameras (24 input images), a shared recovery module and codec, and the same evaluation masks. Completion uses 24 steps when enabled. New-MAE and Obs-Reg use $[0,1]$ linear RGB. Quality is measured before acceptance filtering; Pass includes all requested worlds. A dash denotes an unreported metric. Bold marks the best reported value in each column.}
+  \caption{\textbf{Component ablations.} All variants use $T=8$ (24 images), shared recovery and codec, and common evaluation masks. Quality is measured before acceptance filtering; Pass includes all requested worlds. A dash denotes an unreported metric; bold marks the best reported value in each column.}
   \label{tab:ablation-components}
   \small
@@ -197,5 +195,5 @@
 \begin{table}[t]
   \centering
-  \caption{\textbf{Input-timestamp sensitivity.} Each group fixes $T$ and compares the variant w/o CCM with the full model. Three cameras give 6/12/24 images at $T=2,4,8$. The time span, checkpoints, targets, and 24 completion steps are shared. MAE uses $[0,1]$ linear RGB; New-MAE uses the common unseen region. Results at $T=8$ match Table~\ref{tab:ablation-components}. Bold marks the better value within each group.}
+  \caption{\textbf{Input-timestamp sensitivity.} At each $T$, we compare w/o CCM with the full model using fixed checkpoints and target views. New-MAE uses the common unseen region. Results at $T=8$ match Table~\ref{tab:ablation-components}; bold marks the better value within each group.}
   \label{tab:ablation-inputs}
   \small
```

### zh：实际前后对照

```diff
--- before/zh/4_experiments_zh.tex
+++ after/zh/4_experiments_zh.tex
@@ -36,9 +36,10 @@
 \end{figure*}

-\subsection{消融实验协议}
+\subsection{消融分析}
 \label{sec:ablation-protocol}
 \label{sec:ablations}
+\label{sec:ablation-studies}

-\paragraph{输入与固定条件。}
+\paragraph{实验协议。}
 隐藏表面的配对评价定义在具有独立完整参考的场景上；Waymo 日志用于记录视角评价。
 每个窗口含 29 个时间戳，使用前向、左前和右前三路同步相机。
@@ -61,7 +62,4 @@
 先在场景内平均，再对场景及训练种子汇总。

-\subsection{消融分析}
-\label{sec:ablation-studies}
-
 \paragraph{补全与场景上下文。}
 表~\ref{tab:ablation-components} 将完整版本 Ours 与两个对照比较。
@@ -76,5 +74,5 @@
 \begin{table}[t]
   \centering
-  \caption{\textbf{组件消融。}GCM 和 CCM 分别为生成式补全模块与跨组件记忆模块。所有版本采用 $T=8$、三路相机（24 张输入图像）、相同的恢复模块与编解码器及统一评价掩码。启用补全时采用 24 步。New-MAE 和 Obs-Reg 使用 $[0,1]$ 线性 RGB 尺度。质量在接受筛选前计算，Pass 包含全部申请世界。横线表示该指标未报告；粗体表示各列已报告的最优值。}
+  \caption{\textbf{组件消融。}所有版本采用 $T=8$（24 张图像）、相同的恢复模块与编解码器及统一评价掩码。质量在接受筛选前计算，Pass 包含全部申请世界。横线表示该指标未报告；粗体表示各列已报告的最优值。}
   \label{tab:ablation-components}
   \small
@@ -104,5 +102,5 @@
 \begin{table}[t]
   \centering
-  \caption{\textbf{输入时刻数量敏感性。}每组固定 $T$，比较 w/o CCM 与完整模型。三路相机在 $T=2,4,8$ 时提供 6/12/24 张图像，共享时间跨度、模型权重、目标图像和 24 步补全设置。MAE 使用 $[0,1]$ 线性 RGB 尺度；New-MAE 使用共同未见区域。$T=8$ 的结果与表~\ref{tab:ablation-components} 一致。粗体表示每组内的较优值。}
+  \caption{\textbf{输入时刻数量敏感性。}每档 $T$ 比较 w/o CCM 与完整模型，权重和目标视图固定。New-MAE 使用共同未见区域。$T=8$ 的结果与表~\ref{tab:ablation-components} 一致；粗体表示每组内的较优值。}
   \label{tab:ablation-inputs}
   \small
```

英文正文最后一行位置与页当量：`{"body_page": 8, "column": "R", "last_line": "pletion.", "bottom_pt": 706.7688842, "equivalent": 7.989790805709877, "pages": 11}`。修改前为 8.074 页当量；该估算不代替逐页验收。


## 2026-10-25：摘要主线整理（双语已应用）

本轮基于未提交工作区，实际摘要基线保存在 `paper/build/abstract-revision/before-en.tex` 与 `before-zh.tex`。Git HEAD 为 `c08c4b1ce9da0ec92d93b6b4678de2d19b59aebb`，不作为本轮原文替代。修改范围仅为两版摘要、编译输出和本记录；标题、引言、方法与实验源文不变。

### 原问题 → 修改 → 理由

| 位置 | 原内容 | 修改后 | 理由 |
| --- | --- | --- | --- |
| 开头 | 从新状态暴露未见表面开始，随后列出三个重建要求 | 先交代驾驶仿真与编辑为何需要可复用场景，再说明未见表面和组件归属 | 让用途与核心障碍先于任务拆解 |
| 方法 | 局部注意力、CCM、已见潜码、自由空间和检查并列 | 直接说明在后续控制的坐标系中补全，再概括跨组件上下文与观测约束 | 用设计直觉代替模块清单；细节保留方法正文 |
| 实验 | FID 83.72→37.43、±2m、20.5%、八时间戳和具体对照 | 一句概述 Waymo 重建与视图外推，以及消融支持的跨组件上下文作用 | 减少实验配置打断叙事；数值完整保留实验节 |
| 结尾 | 新状态下无需重采样 | 明确内容构建与状态驱动渲染分离，再回到同一份内容的复用 | 与前面的设计直觉形成完整论证 |

### 主张依据

- 动机及组件归属：当前引言前四段；方法 3.1 的可组合表示。
- 坐标系内联合补全：方法 3.2–3.4 的规范查询、潜表示和条件流。
- 跨组件上下文与观测约束：方法 3.4–3.5；不声称严格几何一致性保证。
- Waymo 重建与轨迹外合成改善：当前实验表 2、3；比较范围限定为所比较基线。
- 未见表面补全中跨组件上下文的收益：实验表 4、5；不将完整参考场景消融泛称为 Waymo 隐藏表面真值评价。
- 同一内容的状态复用：方法表示与渲染机制；未声称新增状态编辑结果或闭环实验验证。

### 检查

英文 176 词（连字符复合词按一个词计），符合本项目 150–250 词目标。两版编译成功，无 Overfull、缺字或未定义引用；已查看双语首页及英文第 8 页。英文正文及图表仍在第 8 页结束，References 从第 9 页开始；总页数英文 11、中文 9。语言检查仅提示分号密度，实际只有结果句中的一个分号，经上下文复核保留。未为消除启发式提示而替换稳定表述。未提交或推送。

### en 全文前后对照

修改前：

```latex
\begin{abstract}
Reusing a driving scene under new camera and actor states exposes surfaces that were never recorded. Reconstructing such a scene requires recovering the observed content, completing missing geometry and appearance, and retaining a stable identity for each movable component. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. It jointly completes a world-space background and canonical vehicle and human assets, so generated surfaces inherit the coordinate frames and motion bindings used for later scene editing. A conditional flow model combines local attention with cross-component memory, while observed codes, known free space, and input-view checks constrain the completed Gaussian scene. On Waymo, DriveCompose reduces FID from 83.72 to 37.43 relative to STORM for $\pm2\,\mathrm{m}$ camera shifts. Cross-component memory lowers unseen-surface RGB error by 20.5\% relative to isolated per-component memories with eight input timestamps. The resulting scene can be rendered under different camera and actor states without resampling its completed geometry or appearance.
\end{abstract}
```

修改后：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Such changes expose unobserved surfaces, whose geometry and appearance must be completed while remaining attached to the scene components that control their motion. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. Its key idea is to complete missing content in the coordinate frames where that content will later be controlled. Image evidence is organized into a world-space background and canonical vehicle and human assets, and a conditional flow model jointly completes their latent representations using context shared across components. Observed evidence constrains generation, and the assembled scene is checked against the input views before reuse. Experiments on Waymo show improved dynamic scene reconstruction and off-trajectory view synthesis over the compared baselines; ablations demonstrate the benefit of cross-component context for completing unseen surfaces. The resulting Gaussian scene separates content construction from state-driven rendering, allowing the same completed geometry and appearance to be reused under new camera and actor states.
\end{abstract}
```

### zh 全文前后对照

修改前：

```latex
\begin{abstract}
在新的相机和交通参与者状态下复用驾驶场景，会暴露原始日志未曾记录的表面。重建这样的场景，需要恢复已观测内容、补全缺失的几何与外观，并为各个可移动组件保持稳定的身份。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。该框架联合补全世界空间背景与规范车辆、人体资产，使生成表面继承后续场景编辑所用的坐标系与运动绑定。条件流模型结合局部注意力与跨组件记忆，已见潜码、已知自由空间和输入视角检查共同约束补全后的高斯场景。在 Waymo 的 $\pm2\,\mathrm{m}$ 相机偏移下，DriveCompose 相较于 STORM 将 FID 从 83.72 降至 37.43。在使用八个输入时间戳时，跨组件记忆相较于各组件独立记忆，将未见表面的 RGB 误差降低了 20.5\%。所得场景可在不同相机和参与者状态下渲染，无需重新采样已补全的几何或外观。
\end{abstract}
```

修改后：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。这些变化会暴露未观测表面，既需要补全其几何与外观，也需要让补全内容保持归属于控制其运动的场景组件。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。其核心思路是在内容后续受控的坐标系中补全缺失部分。图像证据被组织为世界空间背景与规范车辆、人体资产，条件流模型利用组件间共享的上下文，联合补全其潜表示。观测证据约束生成过程，装配后的场景在复用前接受输入视角检查。Waymo 实验表明，该方法在动态场景重建和轨迹外视图合成中优于所比较的基线；消融实验验证了跨组件上下文对未见表面补全的作用。所得高斯场景将内容构建与状态驱动渲染分开，使同一份补全后的几何与外观能够在新的相机和参与者状态下复用。
\end{abstract}
```


## 2026-10-25：摘要局部语言微调与提交

本轮真实基线保存在 `paper/build/abstract-revision/before-polish-en.tex` 与 `before-polish-zh.tex`，继承上一轮未提交摘要。保留开头 require、方法引入句、核心见解及其余段落；只修改长从句及结果句。

- 长从句：从组件控制表面运动的绕行表述，改为补全过程保持与场景及参与者的归属关系。
- 结果句：拆分 Waymo 比较与消融发现；使用明确主语和 evaluated baselines，避免混淆评价来源。

### en 全文对照

修改前：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Such changes expose unobserved surfaces, whose geometry and appearance must be completed while remaining attached to the scene components that control their motion. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. Its key idea is to complete missing content in the coordinate frames where that content will later be controlled. Image evidence is organized into a world-space background and canonical vehicle and human assets, and a conditional flow model jointly completes their latent representations using context shared across components. Observed evidence constrains generation, and the assembled scene is checked against the input views before reuse. Experiments on Waymo show improved dynamic scene reconstruction and off-trajectory view synthesis over the compared baselines; ablations demonstrate the benefit of cross-component context for completing unseen surfaces. The resulting Gaussian scene separates content construction from state-driven rendering, allowing the same completed geometry and appearance to be reused under new camera and actor states.
\end{abstract}
```

修改后：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Such changes expose unobserved surfaces, whose geometry and appearance must be completed in a way that preserves their association with the scene and its actors. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. Its key idea is to complete missing content in the coordinate frames where that content will later be controlled. Image evidence is organized into a world-space background and canonical vehicle and human assets, and a conditional flow model jointly completes their latent representations using context shared across components. Observed evidence constrains generation, and the assembled scene is checked against the input views before reuse. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. The resulting Gaussian scene separates content construction from state-driven rendering, allowing the same completed geometry and appearance to be reused under new camera and actor states.
\end{abstract}
```

### zh 全文对照

修改前：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。这些变化会暴露未观测表面，既需要补全其几何与外观，也需要让补全内容保持归属于控制其运动的场景组件。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。其核心思路是在内容后续受控的坐标系中补全缺失部分。图像证据被组织为世界空间背景与规范车辆、人体资产，条件流模型利用组件间共享的上下文，联合补全其潜表示。观测证据约束生成过程，装配后的场景在复用前接受输入视角检查。Waymo 实验表明，该方法在动态场景重建和轨迹外视图合成中优于所比较的基线；消融实验验证了跨组件上下文对未见表面补全的作用。所得高斯场景将内容构建与状态驱动渲染分开，使同一份补全后的几何与外观能够在新的相机和参与者状态下复用。
\end{abstract}
```

修改后：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。这些变化会暴露未观测表面，需要在补全其几何与外观的同时，保持它们与场景及参与者的归属关系。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。其核心思路是在内容后续受控的坐标系中补全缺失部分。图像证据被组织为世界空间背景与规范车辆、人体资产，条件流模型利用组件间共享的上下文，联合补全其潜表示。观测证据约束生成过程，装配后的场景在复用前接受输入视角检查。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。所得高斯场景将内容构建与状态驱动渲染分开，使同一份补全后的几何与外观能够在新的相机和参与者状态下复用。
\end{abstract}
```

验证：两版编译成功，英文正文仍在第 8 页结束，参考文献从第 9 页开始。正文其他源文件本轮未改。按用户授权，本次提交汇总此前已完成的摘要、方法压缩、消融合并、双语补充与正式 PDF；不包含构建缓存、预览和用户原有图件移动。

## 2026-10-25：摘要控制坐标与联合补全关系澄清

基线提交：`d360908c7ec585a79aadf09017b4abcc0e3e23aa`。两份摘要在修改前均与 HEAD 一致；仅按用户确认版本替换第四、五句与最后一句，其他正文、实验与补充材料源文件不变。

### paper/sec/0_abstract.tex

- 原文：Its key idea is to complete missing content in the coordinate frames where that content will later be controlled.
- 修改后：Our key idea is to jointly complete scene components in the coordinate frames used for their subsequent control.
- 原因：将控制坐标中的补全与跨组件联合补全统一为核心思路，去掉对归属关系的重复解释。

- 原文：Image evidence is organized into a world-space background and canonical vehicle and human assets, and a conditional flow model jointly completes their latent representations using context shared across components.
- 修改后：Features recovered from the input images are aggregated onto a world-space background and canonical vehicle and human supports, and a conditional flow model uses cross-component memory to infer their missing latent content from shared scene context.
- 原因：明确输入图像特征、组件支撑和共享场景上下文的关系，消除 image evidence 的粒度歧义。

- 原文：The resulting Gaussian scene separates content construction from state-driven rendering, allowing the same completed geometry and appearance to be reused under new camera and actor states.
- 修改后：The resulting Gaussian scene separates content construction from state-driven rendering, keeping the completed background and canonical assets fixed during subsequent camera and actor control.
- 原因：以固定背景与规范资产、改变控制状态解释内容复用，减少与前文的重复。

### paper/zh/0_abstract_zh.tex

- 原文：其核心思路是在内容后续受控的坐标系中补全缺失部分。
- 修改后：其核心思路是在各组件后续受控的坐标系中联合补全场景。
- 原因：将控制坐标中的补全与跨组件联合补全统一为核心思路，去掉对归属关系的重复解释。

- 原文：图像证据被组织为世界空间背景与规范车辆、人体资产，条件流模型利用组件间共享的上下文，联合补全其潜表示。
- 修改后：从输入图像恢复的特征被聚合到世界空间背景与规范车辆、人体支撑上，条件流模型通过跨组件记忆共享场景上下文，据此推断各组件缺失的潜表示。
- 原因：明确输入图像特征、组件支撑和共享场景上下文的关系，消除 image evidence 的粒度歧义。

- 原文：所得高斯场景将内容构建与状态驱动渲染分开，使同一份补全后的几何与外观能够在新的相机和参与者状态下复用。
- 修改后：所得高斯场景将内容构建与状态驱动渲染分开，在后续相机和参与者控制过程中保持补全后的背景与规范资产固定。
- 原因：以固定背景与规范资产、改变控制状态解释内容复用，减少与前文的重复。

验证：中英文主稿均实际编译成功，最终 TeX 日志无未定义引用、缺字或 overfull 警告。英文总计 11 页，正文及结论结束于第 8 页，参考文献从第 9 页开始；中文总计 9 页。已检查两版摘要首页和英文第 8 页渲染。中文正式 PDF 被阅读器占用时先在临时目录构建，替换正式文件后随本轮摘要提交。

## 2026-10-26：摘要术语与衔接澄清

基线提交：`f38a81537d0c4dd4d0ca55fcea92e21f7fb30907`。修改前两份摘要均与 HEAD 一致。本轮按用户逐项讨论后确认的完整双语版本更新，仅涉及摘要；标题、引言、方法及实验源文件不变。

修改理由：明确相机与参与者运动及其暴露的未见表面，消除代词歧义；删除摘要中的标定限定；用具体坐标系及运动关系解释组件表示；将条件流明确为通过流匹配训练的条件生成模型；用输入观测约束和原视角渲染说明一致性检查；统一组合术语，删除容易误解为对象静止的固定表述，精简末句。标定、潜码硬约束和自由空间约束仍由方法部分说明。

### paper/sec/0_abstract.tex

修改前：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Such changes expose unobserved surfaces, whose geometry and appearance must be completed in a way that preserves their association with the scene and its actors. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from calibrated image sequences. Our key idea is to jointly complete scene components in the coordinate frames used for their subsequent control. Features recovered from the input images are aggregated onto a world-space background and canonical vehicle and human supports, and a conditional flow model uses cross-component memory to infer their missing latent content from shared scene context. Observed evidence constrains generation, and the assembled scene is checked against the input views before reuse. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. The resulting Gaussian scene separates content construction from state-driven rendering, keeping the completed background and canonical assets fixed during subsequent camera and actor control.
\end{abstract}
```

修改后：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, vehicle, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We also render the composed scene from the original camera viewpoints to check its consistency with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. The completed components form a Gaussian scene that supports rendering under different camera and actor states.
\end{abstract}
```

### paper/zh/0_abstract_zh.tex

修改前：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。这些变化会暴露未观测表面，需要在补全其几何与外观的同时，保持它们与场景及参与者的归属关系。我们提出 DriveCompose，从有标定的图像序列中生成式地重建可组合驾驶场景。其核心思路是在各组件后续受控的坐标系中联合补全场景。从输入图像恢复的特征被聚合到世界空间背景与规范车辆、人体支撑上，条件流模型通过跨组件记忆共享场景上下文，据此推断各组件缺失的潜表示。观测证据约束生成过程，装配后的场景在复用前接受输入视角检查。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。所得高斯场景将内容构建与状态驱动渲染分开，在后续相机和参与者控制过程中保持补全后的背景与规范资产固定。
\end{abstract}
```

修改后：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、车辆或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还从原始相机视角渲染组合后的场景，检查补全结果是否与输入图像一致。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。补全后的组件构成高斯场景，支持在不同相机和参与者状态下渲染。
\end{abstract}
```

验证：双语主稿编译成功，英文摘要 188 词；英文总计 11 页，正文和结论在第 8 页结束，参考文献从第 9 页开始；中文总计 9 页。最终 TeX 日志无未定义引用、缺字或 overfull 警告；两版摘要首页及英文第 8 页渲染检查通过。

## 2026-10-26：引言论证与核心贡献整理

基线提交：`d741912c7a666308c5363cfb79a6c51b11b76e2b`。两版引言修改前均与 HEAD 一致，以下原文取自本轮真实基线。按用户逐段确认内容整合六段引言，补充已有实验概述，并重新聚焦两项贡献。仅修改双语引言与本记录；摘要、方法、实验、图件和补充材料源文件保持原样。

- **第一段**：原始配置、仍然可用、身份归属等抽象表达影响阅读。 → 按用户确认版本，以具体控制需求开篇，说明观测范围与未见表面，并将身份归属落到表面随对象运动。
- **第二、三段**：观测恢复局限句拗口，重建、控制与生成的能力边界混在一起。 → 分开说明多帧恢复的能力、完全未观测表面的直接约束缺失，以及可控场景对联合补全的要求。不将所有前馈方法概括为不具备生成先验，也不宣称所有生成方法缺乏可控性。
- **第四段**：控制坐标系、组织单位等概括未解释为什么有效。 → 先交代背景、车身与人体的具体表示，再解释补全表面为何能随对象运动，承接前文的控制需求。保留对既有可组合表示的归因。
- **第五段**：原段按前端、潜码、条件流与解码器列模块，核心机制不突出。 → 将组件内部局部建模与跨组件记忆的信息汇集和回传作为中心；首次说明潜码编码几何与外观。前端和解码仅承担输入输出说明。
- **第六段**：自由空间、装配、固定资产的表述影响理解。 → 保留新增表面可能遮挡已观测区域这一检查理由，明确记录视角和对象状态下的渲染比较。采样约束细节仍在方法中，没有删除技术条件或改写实验。
- **新增实验概述**：引言缺少方法有效性与核心机制的实证收束。 → 引用当前动态重建、视图外推和消融节，说明相对已评估基线的结果以及稀疏观测下更大的绝对误差收益。不添加数值、显著性或新状态质量结论。
- **贡献列表**：原条目将框架、流模型、约束与检查堆在一起。 → 第一项明确生成内容直接进入带身份和运动绑定的组件表示并可复用；第二项明确局部注意力与跨组件记忆组成的联合补全机制。观测检查作为框架机制保留在正文，不单列为独立创新。

删减说明：删除重复的框架导航和抽象表述；前端输出、自由空间与潜码约束等已有细节仍保留在方法，并未新迁入补充材料。标题和最新摘要保持原样；不改字号、边距、行距或浮动设置。自身方法与结果段以内部节号支持主张，不为满足引用数量将本文设计错误归因于外部论文。

### paper/sec/1_introduction.tex：全文前后对照

修改前：

```latex
\section{Introduction}
\label{sec:introduction}

Driving datasets record scenes along captured trajectories~\cite{sun2020waymo,caesar2020nuscenes}. Driving simulation and scene editing require a reconstruction that remains usable when the recorded configuration changes. Moving a camera, turning a vehicle, or changing a pedestrian's pose exposes previously unobserved surfaces. These operations require geometry and appearance beyond the recorded images, together with a representation that keeps the content attached to the same scene and actor identities.

Recent feed-forward methods recover driving scenes and motion directly from temporal observations~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}. Recovering observed content alone does not supply the unseen surfaces exposed by later actor motion.

Compositional representations separate background and actors and provide canonical models for independent motion and control~\cite{yan2024street,chen2025omnire,zhou2024hugsim}. Generative models address missing content through asset priors, Gaussian completion, or generated views~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}. Combining them requires a generator that assigns content to the background and to individual assets. A generated surface must have an owner, a coordinate frame, and a motion rule before it can become part of an editable scene.

We formulate driving-scene reconstruction as conditional generation of a compositional scene. Our representation follows the units that will be manipulated: a world-space background, rigid vehicles in local coordinates, and humans on canonical surfaces with skeleton bindings. Completing surfaces in their component's control frame lets the same generated content retain its identity under later state changes (Sec.~\ref{sec:representation}). Image evidence is first aggregated on these supports. A generative model then completes their missing latent content under the observed scene conditions.

DriveCompose implements this formulation with a visual recovery front end, structured latent codes, and a conditional flow model~\cite{lipman2022flowmatching} (Fig.~\ref{fig:teaser}). The front end estimates geometry, trajectory-level identities, and time-varying states. Within the completion model, local attention follows each component's support, while shared memory exchanges context between background and assets. Type-specific decoders convert the completed codes into Gaussian components.

Generation must also respect the images from which the scene was recovered. We retain reliable observed codes and suppress known free space throughout sampling. Newly generated content can nevertheless occlude an observed surface, so we check the assembled candidate in the original views as well. After construction, the background and canonical assets remain fixed. Camera placement, vehicle transforms, and human joint poses determine their subsequent rendering (Sec.~\ref{sec:composition}).

\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework that jointly completes background and canonical actor assets from driving observations. The resulting compositional Gaussian scene can be rendered under new camera and actor states using the same completed content.
\item We develop a structured conditional flow model that shares scene context across background and assets through cross-component memory. Observed-code and free-space constraints guide latent completion, while input-view checks validate the assembled scene against the recorded observations.
\end{itemize}

Section~\ref{sec:related} reviews related work, Section~\ref{sec:method} presents the method, and Section~\ref{sec:experiments} reports experiments. Sections~\ref{sec:discussion} and~\ref{sec:conclusion} discuss limitations and conclude.
```

修改后：

```latex
\section{Introduction}
\label{sec:introduction}

Driving simulation and scene editing require 3D scenes that support changes in camera viewpoint, vehicle motion, and human pose~\cite{yang2023unisim,zhou2024hugsim}. However, driving images reveal only the surfaces visible from the recorded viewpoints and actor configurations~\cite{sun2020waymo,caesar2020nuscenes}. Moving a camera, turning a vehicle, or changing a pedestrian's pose exposes previously unobserved regions. Reconstructing scenes for these operations therefore requires completing the missing geometry and appearance while ensuring that completed vehicle and human surfaces move with their respective actors.

Recent feed-forward methods predict driving-scene geometry and Gaussians from multiple images, using motion and visibility modeling to align dynamic observations~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}. Surfaces unseen throughout the sequence lack direct image constraints and require inference from learned priors.

Generative methods infer unseen content through asset priors, Gaussian completion, or generated views~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}. Compositional representations support independent vehicle motion and human pose control~\cite{yan2024street,chen2025omnire,zhou2024hugsim}. Editable scenes require completion to preserve these motion relationships while drawing on the surrounding scene.

We introduce DriveCompose for joint reconstruction and completion of controllable driving scenes. The background uses world coordinates, vehicles their own coordinate frames, and humans a reference pose with skeletal bindings~\cite{yan2024street,chen2025omnire}. Completing these representations lets generated surfaces follow actor motion and pose changes (Sec.~\ref{sec:representation}).

As shown in Fig.~\ref{fig:teaser}, recovered geometry and motion align image features with component representations. Local attention models each component's structure, while cross-component memory gathers and redistributes scene context. The model generates missing geometry and appearance codes through flow matching~\cite{lipman2022flowmatching}, and component-specific decoders produce a Gaussian scene~\cite{kerbl2023gaussians}.

Completion retains reliably observed surfaces and generates missing geometry and appearance. New surfaces may occlude visible regions, so we compare renderings with input images at the recorded camera and actor states. Accepted scenes reuse this content under new states (Sec.~\ref{sec:composition}).

Waymo experiments show improved dynamic reconstruction and off-trajectory view synthesis over the evaluated baselines (Sec.~\ref{sec:experiments}). Ablations show lower unseen-surface error with cross-component memory, with larger absolute gains under sparser observations (Sec.~\ref{sec:ablations}).

\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework that jointly completes background and canonical actor representations from driving images. Generated surfaces retain their component ownership and motion bindings, enabling reuse of the completed Gaussian scene under new camera and actor states.
\item We develop a structured flow-matching model that combines local component attention with cross-component memory, allowing each component to use scene context to complete missing content while retaining its spatial organization.
\end{itemize}

Section~\ref{sec:related} reviews related work, Section~\ref{sec:method} presents the method, and Section~\ref{sec:experiments} reports experiments. Sections~\ref{sec:discussion} and~\ref{sec:conclusion} discuss limitations and conclude.
```

### paper/zh/1_introduction_zh.tex：全文前后对照

修改前：

```latex
\section{引言}
\label{sec:introduction}

驾驶数据集沿采集轨迹记录场景~\cite{sun2020waymo,caesar2020nuscenes}。驾驶仿真和场景编辑要求重建结果在原始配置改变后仍然可用。移动相机、转动车辆或改变行人姿态，都会暴露此前未观测的表面。这些操作既需要原始图像之外的几何与外观，也需要一种表示，使内容始终归属于同一个场景和资产身份。

近期前馈方法直接从时序观测恢复驾驶场景与运动~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}。仅恢复已观测内容，无法为后续资产运动暴露的未见表面提供内容。

可组合表示将背景与参与者分离，并通过规范模型支持独立运动和控制~\cite{yan2024street,chen2025omnire,zhou2024hugsim}。生成模型则通过资产先验、高斯补全或生成视图处理缺失内容~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}。结合这些能力，需要生成器明确区分属于背景和各个资产的内容。生成的表面必须具有明确的归属、坐标系和运动规则，才能成为可编辑场景的一部分。

我们将驾驶场景重建建模为可组合场景的条件生成。表示的组织单位对应后续操作的对象：世界空间中的背景、局部坐标中的刚体车辆，以及带骨架绑定的规范人体表面。在组件的控制坐标系中补全表面，使同一份生成内容在后续状态变化时仍保持身份归属（第~\ref{sec:representation} 节）。图像证据先在这些支撑上聚合，生成模型再根据已观测场景条件补全缺失潜码。

DriveCompose 通过视觉恢复前端、结构化潜码和条件流模型~\cite{lipman2022flowmatching} 实现这一形式（图~\ref{fig:teaser}）。前端估计几何、轨迹级身份和随时间变化的状态。在补全模型中，局部注意力沿各组件的支撑组织，共享记忆在背景与资产之间交换上下文。类型专属解码器将完成的潜码转化为高斯组件。

生成还需要遵循场景恢复所依据的图像。我们在采样过程中保留可靠的已见潜码，并抑制已知自由空间。新增内容仍可能遮挡已观测表面，因此还需在原始视角下检查装配后的候选场景。构建完成后，背景与规范资产保持固定，后续渲染由相机位置、车辆变换和人体关节姿态决定（第~\ref{sec:composition} 节）。

本文的贡献包括：
\begin{itemize}
\item 提出生成式重建框架 DriveCompose，从驾驶观测中联合补全背景与规范参与者资产。所得可组合高斯场景可在新的相机和参与者状态下渲染，复用同一份补全内容。
\item 设计结构化条件流模型，通过跨组件记忆在背景与资产之间共享场景上下文。已见潜码与自由空间约束引导潜空间补全，输入视角检查则验证装配后的场景与已记录观测的一致性。
\end{itemize}

第~\ref{sec:related} 节回顾相关工作，第~\ref{sec:method} 节介绍方法，第~\ref{sec:experiments} 节报告实验，第~\ref{sec:discussion} 和第~\ref{sec:conclusion} 节分别讨论局限性并总结全文。
```

修改后：

```latex
\section{引言}
\label{sec:introduction}

驾驶仿真与场景编辑需要能够支持相机移动、车辆运动和人体姿态变化的三维场景~\cite{yang2023unisim,zhou2024hugsim}。然而，驾驶日志中的图像只提供采集视角和当时参与者状态下的可见表面~\cite{sun2020waymo,caesar2020nuscenes}。移动相机、转动车辆或改变行人姿态，都会暴露此前未观测的区域。因此，场景重建需要补全这些区域的几何与外观，并使补全后的车辆和人体表面能够随所属对象运动。

近期前馈方法从多帧图像中预测驾驶场景的几何与高斯，并利用运动和可见性建模对齐动态观测~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}。整个序列都未观测的表面缺少直接图像约束，需要利用学习到的先验推断。

生成式重建通过资产先验、高斯补全或生成视图推断未观测内容~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}。可组合表示支持车辆独立运动和人体姿态控制~\cite{yan2024street,chen2025omnire,zhou2024hugsim}。可编辑场景要求补全保留这些运动关系，同时利用周围场景的信息。

我们提出 DriveCompose，联合重建并补全可控驾驶场景。我们在世界坐标系中表示背景，在车辆自身的坐标系中表示车身，并在参考姿态下表示人体、保留其骨架绑定~\cite{yan2024street,chen2025omnire}。补全直接在这些表示中进行，使生成的车辆和人体表面能够随所属对象运动或改变姿态（第~\ref{sec:representation} 节）。

图~\ref{fig:teaser} 展示整体流程。恢复的几何与运动用于将图像特征对齐到组件表示中。局部注意力建模组件结构，跨组件记忆汇集并回传场景上下文。流匹配生成缺失的几何与外观潜码~\cite{lipman2022flowmatching}，类型专属解码器将其转化为高斯~\cite{kerbl2023gaussians}。

补全保留可靠观测确定的表面，生成缺失的几何与外观。新增表面可能遮挡原本可见的区域，因此我们在记录的相机和参与者状态下，将渲染视图与输入图像比较检查。通过检查的场景可在新的状态下复用这些内容（第~\ref{sec:composition} 节）。

在 Waymo 上，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线（第~\ref{sec:experiments} 节）。组件消融表明，跨组件记忆能够降低未观测表面的补全误差，且在输入观测较少时带来更大的绝对误差降低（第~\ref{sec:ablations} 节）。

本文的贡献包括：
\begin{itemize}
\item 提出生成式重建框架 DriveCompose，从驾驶图像中联合补全背景与规范参与者表示。生成表面保留组件归属与运动绑定，使补全后的高斯场景能够在新的相机和参与者状态下复用。
\item 设计结合组件内部局部注意力与跨组件记忆的结构化流匹配模型，使各组件在保留自身空间结构的同时，利用场景上下文补全缺失内容。
\end{itemize}

第~\ref{sec:related} 节回顾相关工作，第~\ref{sec:method} 节介绍方法，第~\ref{sec:experiments} 节报告实验，第~\ref{sec:discussion} 节和第~\ref{sec:conclusion} 节分别讨论局限性并总结全文。
```

篇幅处理：首轮整合后结论延至英文第 9 页；随后只在引言中删除第三、四、五段重复的联合补全与上下文用途说明，压缩检查流程及贡献的重复措辞，保留坐标表示、局部/跨组件机制、检查理由和实验概述。没有改动其他章节或排版参数。

最终核验：两版均实际编译成功，英文总计 11 页，正文与结论结束于第 8 页，参考文献从第 9 页开始；中文总计 9 页。两版最终 TeX 日志无未定义引用、缺字或 overfull 警告。各有 16 个有效文献键与 9 个有效内部引用目标；已检查英文引言两页、中文引言首页及英文第 8 页渲染。Git 差异确认除双语引言外，其余 LaTeX、书目和样式源文件均未修改。双语措辞清理按 anti-defensive-writing 与 humanizer 的已读取规则执行，没有新增或独立核验实验结果，也没有进行外部文献检索。

## 2026-10-26：确认引言、三项贡献与新标题并推送

基线 HEAD：`d741912c7a666308c5363cfb79a6c51b11b76e2b`。本轮开始时双语引言已有上轮未提交的压缩修改，以下“修改前”保存本轮真实工作区内容及哈希，而非将 HEAD 冒充本轮起点。按用户后续要求恢复已逐段认可的完整解释，只合入已确认的局部去重，不再为页数整体压缩。

本轮确认：第三段保留设计需求、删除重复提出方案的末句；第四段末句删除“交换信息”的同义复述；第五段解码句用“各组件”承接；第六段末句明确复用同一份内容。贡献改为生成式重建框架、条件流匹配的跨组件潜空间补全、实验评估三项，第一项以闭环仿真为应用目标，未添加闭环策略实测或效率结论。第二段将“只能增加可见覆盖”写为对观测覆盖的正面说明，避免将生成能力的边界归给所有前馈方法。

### paper/sec/1_introduction.tex

工作区原文 SHA-256：`015543f2be39c71964ada43420ad7392b7e477782dadafd1cc8b20193f4e5b3c`。

修改前：

```latex
\section{Introduction}
\label{sec:introduction}

Driving simulation and scene editing require 3D scenes that support changes in camera viewpoint, vehicle motion, and human pose~\cite{yang2023unisim,zhou2024hugsim}. However, driving images reveal only the surfaces visible from the recorded viewpoints and actor configurations~\cite{sun2020waymo,caesar2020nuscenes}. Moving a camera, turning a vehicle, or changing a pedestrian's pose exposes previously unobserved regions. Reconstructing scenes for these operations therefore requires completing the missing geometry and appearance while ensuring that completed vehicle and human surfaces move with their respective actors.

Recent feed-forward methods predict driving-scene geometry and Gaussians from multiple images, using motion and visibility modeling to align dynamic observations~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}. Surfaces unseen throughout the sequence lack direct image constraints and require inference from learned priors.

Generative methods infer unseen content through asset priors, Gaussian completion, or generated views~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}. Compositional representations support independent vehicle motion and human pose control~\cite{yan2024street,chen2025omnire,zhou2024hugsim}. Editable scenes require completion to preserve these motion relationships while drawing on the surrounding scene.

We introduce DriveCompose for joint reconstruction and completion of controllable driving scenes. The background uses world coordinates, vehicles their own coordinate frames, and humans a reference pose with skeletal bindings~\cite{yan2024street,chen2025omnire}. Completing these representations lets generated surfaces follow actor motion and pose changes (Sec.~\ref{sec:representation}).

As shown in Fig.~\ref{fig:teaser}, recovered geometry and motion align image features with component representations. Local attention models each component's structure, while cross-component memory gathers and redistributes scene context. The model generates missing geometry and appearance codes through flow matching~\cite{lipman2022flowmatching}, and component-specific decoders produce a Gaussian scene~\cite{kerbl2023gaussians}.

Completion retains reliably observed surfaces and generates missing geometry and appearance. New surfaces may occlude visible regions, so we compare renderings with input images at the recorded camera and actor states. Accepted scenes reuse this content under new states (Sec.~\ref{sec:composition}).

Waymo experiments show improved dynamic reconstruction and off-trajectory view synthesis over the evaluated baselines (Sec.~\ref{sec:experiments}). Ablations show lower unseen-surface error with cross-component memory, with larger absolute gains under sparser observations (Sec.~\ref{sec:ablations}).

\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework that jointly completes background and canonical actor representations from driving images. Generated surfaces retain their component ownership and motion bindings, enabling reuse of the completed Gaussian scene under new camera and actor states.
\item We develop a structured flow-matching model that combines local component attention with cross-component memory, allowing each component to use scene context to complete missing content while retaining its spatial organization.
\end{itemize}

Section~\ref{sec:related} reviews related work, Section~\ref{sec:method} presents the method, and Section~\ref{sec:experiments} reports experiments. Sections~\ref{sec:discussion} and~\ref{sec:conclusion} discuss limitations and conclude.
```

修改后：

```latex
\section{Introduction}
\label{sec:introduction}

Driving simulation and scene editing require 3D scenes that support changes in camera viewpoint, vehicle motion, and human pose~\cite{yang2023unisim,zhou2024hugsim}. However, driving images reveal only the surfaces visible from the recorded viewpoints and actor configurations~\cite{sun2020waymo,caesar2020nuscenes}. Moving a camera, turning a vehicle, or changing a pedestrian's pose exposes previously unobserved regions. Reconstructing scenes for these operations therefore requires completing the missing geometry and appearance while ensuring that completed vehicle and human surfaces move with their respective actors.

Recent feed-forward methods fuse multiple images to directly predict driving-scene geometry and Gaussian representations~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}. Motion estimation and visibility modeling further help align dynamic objects and integrate observations over time. Multi-frame aggregation increases coverage of surfaces visible in the input sequence. When a new viewpoint or actor motion reveals surfaces unseen throughout the sequence, reconstruction must infer their geometry and appearance from generative priors.

Generative reconstruction uses asset priors, Gaussian completion, or generated views to infer unobserved content~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}. Meanwhile, compositional reconstruction represents the background and moving actors separately to support vehicle motion and human pose control~\cite{yan2024street,chen2025omnire,zhou2024hugsim}. Applying generative completion to such scenes requires generated surfaces to move with their actors, while allowing each actor's completion to use information from the surrounding scene.

To this end, we introduce DriveCompose, which reconstructs driving image sequences into a generatively completed 3D scene with independently controllable actors. We represent the background in world coordinates, vehicle surfaces in each vehicle's own coordinate frame, and human surfaces in a reference pose with skeletal bindings~\cite{yan2024street,chen2025omnire}. Completion operates directly on these representations, allowing generated vehicle and human surfaces to follow their actors' motion and pose changes (Sec.~\ref{sec:representation}). The model jointly completes missing background and actor content using shared scene context.

As illustrated in Fig.~\ref{fig:teaser}, DriveCompose first recovers scene geometry and actor motion from the image sequence and aligns multi-frame image features with the background, vehicle, and human representations. The completion model captures local structure within each component, while cross-component memory gathers information from the background and actors and distributes the shared context back to each component. Missing regions of a vehicle or human can therefore be completed using information from the surrounding scene. The model learns to generate missing latent codes through flow matching~\cite{lipman2022flowmatching}, and component-specific decoders convert the completed representations into a Gaussian scene~\cite{kerbl2023gaussians}.

During completion, we retain surfaces established by reliable observations and generate the missing geometry and appearance. Newly generated surfaces may occlude previously visible regions, so we render the completed scene at the recorded camera viewpoints and actor states and compare it with the input images to check for inconsistencies introduced by completion. Scenes that pass this check can reuse the same completed content for rendering under different camera viewpoints and actor states (Sec.~\ref{sec:composition}).

On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines (Sec.~\ref{sec:experiments}). Component ablations further show that cross-component information sharing reduces unseen-surface completion error, with larger absolute error reductions under sparser observations (Sec.~\ref{sec:ablations}).

\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework for closed-loop driving simulation. It recovers and completes backgrounds, vehicles, and humans from image sequences to construct compositional Gaussian scene assets. The resulting scene reuses the same completed assets for composition and rendering as camera poses, vehicle poses, and human poses change.
\item We develop a cross-component latent completion model based on conditional flow matching. Local attention models spatial relationships within each component, while cross-component memory aggregates background and actor features to provide scene context for generating each component's missing content.
\item We evaluate the framework and its key mechanisms through dynamic reconstruction, off-trajectory view synthesis, and component ablations. Experiments show that DriveCompose outperforms the evaluated baselines on reconstruction and view synthesis; cross-component information sharing reduces unseen-surface completion error, with larger absolute reductions under sparse observations.
\end{itemize}

Section~\ref{sec:related} reviews related work, Section~\ref{sec:method} presents the method, and Section~\ref{sec:experiments} reports experiments. Sections~\ref{sec:discussion} and~\ref{sec:conclusion} discuss limitations and conclude.
```

### paper/zh/1_introduction_zh.tex

工作区原文 SHA-256：`2d02dde40ee4d2fa4cb41ed4eb5c8b5d2d9406378ff0ebac851d117183c24189`。

修改前：

```latex
\section{引言}
\label{sec:introduction}

驾驶仿真与场景编辑需要能够支持相机移动、车辆运动和人体姿态变化的三维场景~\cite{yang2023unisim,zhou2024hugsim}。然而，驾驶日志中的图像只提供采集视角和当时参与者状态下的可见表面~\cite{sun2020waymo,caesar2020nuscenes}。移动相机、转动车辆或改变行人姿态，都会暴露此前未观测的区域。因此，场景重建需要补全这些区域的几何与外观，并使补全后的车辆和人体表面能够随所属对象运动。

近期前馈方法从多帧图像中预测驾驶场景的几何与高斯，并利用运动和可见性建模对齐动态观测~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}。整个序列都未观测的表面缺少直接图像约束，需要利用学习到的先验推断。

生成式重建通过资产先验、高斯补全或生成视图推断未观测内容~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}。可组合表示支持车辆独立运动和人体姿态控制~\cite{yan2024street,chen2025omnire,zhou2024hugsim}。可编辑场景要求补全保留这些运动关系，同时利用周围场景的信息。

我们提出 DriveCompose，联合重建并补全可控驾驶场景。我们在世界坐标系中表示背景，在车辆自身的坐标系中表示车身，并在参考姿态下表示人体、保留其骨架绑定~\cite{yan2024street,chen2025omnire}。补全直接在这些表示中进行，使生成的车辆和人体表面能够随所属对象运动或改变姿态（第~\ref{sec:representation} 节）。

图~\ref{fig:teaser} 展示整体流程。恢复的几何与运动用于将图像特征对齐到组件表示中。局部注意力建模组件结构，跨组件记忆汇集并回传场景上下文。流匹配生成缺失的几何与外观潜码~\cite{lipman2022flowmatching}，类型专属解码器将其转化为高斯~\cite{kerbl2023gaussians}。

补全保留可靠观测确定的表面，生成缺失的几何与外观。新增表面可能遮挡原本可见的区域，因此我们在记录的相机和参与者状态下，将渲染视图与输入图像比较检查。通过检查的场景可在新的状态下复用这些内容（第~\ref{sec:composition} 节）。

在 Waymo 上，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线（第~\ref{sec:experiments} 节）。组件消融表明，跨组件记忆能够降低未观测表面的补全误差，且在输入观测较少时带来更大的绝对误差降低（第~\ref{sec:ablations} 节）。

本文的贡献包括：
\begin{itemize}
\item 提出生成式重建框架 DriveCompose，从驾驶图像中联合补全背景与规范参与者表示。生成表面保留组件归属与运动绑定，使补全后的高斯场景能够在新的相机和参与者状态下复用。
\item 设计结合组件内部局部注意力与跨组件记忆的结构化流匹配模型，使各组件在保留自身空间结构的同时，利用场景上下文补全缺失内容。
\end{itemize}

第~\ref{sec:related} 节回顾相关工作，第~\ref{sec:method} 节介绍方法，第~\ref{sec:experiments} 节报告实验，第~\ref{sec:discussion} 节和第~\ref{sec:conclusion} 节分别讨论局限性并总结全文。
```

修改后：

```latex
\section{引言}
\label{sec:introduction}

驾驶仿真与场景编辑需要能够支持相机移动、车辆运动和人体姿态变化的三维场景~\cite{yang2023unisim,zhou2024hugsim}。然而，驾驶日志中的图像只提供采集视角和当时参与者状态下的可见表面~\cite{sun2020waymo,caesar2020nuscenes}。移动相机、转动车辆或改变行人姿态，都会暴露此前未观测的区域。因此，场景重建需要补全这些区域的几何与外观，并使补全后的车辆和人体表面能够随所属对象运动。

近期前馈方法通过融合多帧图像，直接预测驾驶场景的三维几何与高斯表示~\cite{yang2025storm,chen2025dggt,yu2026streetforward,chi2026pointforward}。运动估计与可见性建模进一步帮助这些方法对齐动态对象，并整合不同时刻的观测。多帧融合增加了对输入序列中可见表面的覆盖。当新视角或对象运动暴露出整个序列都未曾拍摄的表面时，重建需要借助生成先验推断其几何与外观。

生成式重建通过资产先验、高斯补全或生成视图推断未观测内容~\cite{yang2025genassets,liao2025complete,streetcrafter,zhu2025worldsplat}。与此同时，可组合重建将背景与运动对象分开表示，支持车辆移动和人体姿态控制~\cite{yan2024street,chen2025omnire,zhou2024hugsim}。将生成补全用于这类场景，需要使补出的表面随所属对象运动，同时让每个对象能够利用周围场景的信息完成补全。

为此，我们提出 DriveCompose，从驾驶图像序列中构建可独立控制、并经过生成补全的三维场景。我们在世界坐标系中表示背景，在车辆自身的坐标系中表示车身，并在参考姿态下表示人体、保留其骨架绑定~\cite{yan2024street,chen2025omnire}。补全直接在这些表示中进行，使生成的车辆和人体表面能够随所属对象运动或改变姿态（第~\ref{sec:representation} 节）。在此基础上，模型通过共享场景上下文，联合补全背景与各对象的缺失内容。

如图~\ref{fig:teaser} 所示，DriveCompose 首先从图像序列中恢复场景几何与参与者运动，将多帧图像特征对齐到背景、车辆和人体各自的表示中。补全模型在每个组件内部建模局部结构，并通过跨组件记忆汇集背景与各对象的信息，再将共享上下文传回各组件。这样，车辆或人体的缺失部分可以结合周围场景的信息进行补全。模型通过流匹配学习生成缺失潜码~\cite{lipman2022flowmatching}，再由各组件的解码器将补全后的表示转化为高斯场景~\cite{kerbl2023gaussians}。

补全时，我们保留由可靠观测确定的表面，并生成缺失部分的几何与外观。新增表面可能遮挡原本可见的区域，因此我们在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较，检查补全是否引入观测不一致。通过检查的场景可复用同一份补全内容，在不同相机视角和参与者状态下渲染（第~\ref{sec:composition} 节）。

在 Waymo 上，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线（第~\ref{sec:experiments} 节）。组件消融进一步表明，跨组件信息共享能够降低未观测表面的补全误差，且在输入观测较少时带来更大的绝对误差降幅（第~\ref{sec:ablations} 节）。

本文的贡献包括：
\begin{itemize}
\item 提出面向闭环驾驶仿真的生成式重建框架 DriveCompose。从图像序列中恢复并补全背景、车辆与人体，构建可组合的高斯场景资产。所得场景可在相机位姿、车辆位姿和人体姿态变化时，复用同一组补全资产进行组合与渲染。
\item 设计基于条件流匹配的跨组件潜空间补全模型。通过局部注意力建模各组件内部的空间关系，通过跨组件记忆汇集背景与参与者的特征，为各组件的缺失内容生成提供场景上下文。
\item 通过动态重建、轨迹外视图合成与组件消融评估框架及其关键机制。实验表明，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线；跨组件信息共享降低了未观测表面的补全误差，并在观测稀疏时带来更大的绝对误差降幅。
\end{itemize}

第~\ref{sec:related} 节回顾相关工作，第~\ref{sec:method} 节介绍方法，第~\ref{sec:experiments} 节报告实验，第~\ref{sec:discussion} 节和第~\ref{sec:conclusion} 节分别讨论局限性并总结全文。
```

### 标题同步

- 英文：`DriveCompose: Generative Reconstruction of Compositional Driving Scenes via Joint Completion` → `DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion`。
- 中文对应：`DriveCompose：通过联合补全实现可组合驾驶场景的生成式重建` → `DriveCompose：通过联合补全实现驾驶场景的可组合生成式重建`。
- 同步两版主稿、两版补充材料及当前标题说明；已有历史对照、来源记录中的旧题名保留其历史含义。
- 摘要、方法、实验与补充材料正文保持原样；当前稿的闭环仿真是应用定位，证据范围仍为已有重建、视图外推与消融结果。

最终构建与交付检查：英文主稿 11 页，中文主稿 9 页，英文补充材料 4 页，中文补充材料 3 页，四份 PDF 均由本轮实际写出。主稿最终日志无未定义引用、缺字或 overfull 警告；补充材料仅保留既有 lineno hook 警告。双语标题、引言三项贡献、引用目标和渲染页面均已核对。

篇幅状态：按用户要求恢复解释完整的引言并采用三项贡献后，英文正文与结论结束于第 9 页，参考文献也从第 9 页开始；尚不满足正文 8 页目标。本轮不再整体压缩已认可的文字，也未改动字体、边距、行距、图表或其他章节。此状态已在推送前向用户说明。


## 2026-10-26：总览图仅保留主推理流程（候选，未插入论文）

范围：只生成新的候选图，不改中英文 LaTeX、实验数值或正式 PDF。当前 HEAD 为 `d741912c7a666308c5363cfb79a6c51b11b76e2b`；实际图像基线是未提交的 `docs/figures/overview/drafts/20261023-reference-style/candidate-v5.png`，SHA256 为 `55b02eb44ad8c2404e691e3348f2da84b013108fb037693db81025af2e7a1188`，没有把 HEAD 当作旧图原文。

| 位置 | 旧候选实际内容 | 本轮候选 | 原因 |
| --- | --- | --- | --- |
| 右侧与下方 | `Observation check`、`Fixed world W`、`State-driven reuse`、`Compose + render` | 从图中移除；结束于 `Background + sky / Vehicle / Human` | 用户要求仅展示主题推理，减少拥挤 |
| 图例与采样区 | `Observed / Unknown / Generated / Free`、`Noise on unknown`、`Constrained flow sampling` 等备注 | 不再单独展示 | 减少次要说明，使联合 DiT 成为视觉中心；方法正文不变 |
| ViT 到 DiT 之间 | 背景、车辆和人体的空间示意 | `Visual features` 与 `Structured latents` 均使用抽象 token | 避免把中间表示误认为图片 |
| 中央联合模块 | 局部注意力与记忆混在完整系统流程中 | 独立突出 `Joint completion DiT`，三路局部潜码与一个 `CCM / Shared memory` 交互 | 对齐当前方法节的联合补全核心设计 |

交付：[候选图](../../_archive/drivecompose/20261026-overview-intermediates/docs/figures/overview/drafts/inference-overview/candidate.png)、[完整指令与核对记录](figures/overview/drafts/inference-overview/README.md)。输入和输出场景保留机制示意身份。自审确认 ViT 至 DiT 区域没有实图，E 收缩、D 展开；主链路及类型对应可辨。待用户确认图像，未将其标为论文定稿，未触发主稿编译。

### 同日续修：修复六项图示问题

用户明确要求“全部修复”。本轮实际基线是上轮生成后未提交的 [candidate.png 修改前图像](../../_archive/drivecompose/20261026-overview-intermediates/docs/figures/overview/drafts/inference-overview/baseline/candidate.png)，SHA256 为 `35085490d036fbbf87fcf13caa55d458eeb5bf78380bf5c44fc815193934cb89`；HEAD 仍为 `d741912c7a666308c5363cfb79a6c51b11b76e2b`。使用该真实基线作以下对照，不将更早版本或用户其他修改算作本轮成果。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| DiT → Completed latents | 三条线从 CCM 边框直接延伸到外部潜码 | 取消 CCM 到模型外框的线段，三条输出箭头从 DiT 外框独立端口引出 | 对应更新后的组件表示由整个补全模块输出，避免把共享记忆本身画成解码输入 |
| Local attention ↔ CCM | 每行有两条双向线 | 每行保留一条双向线，共三条 | 删除重复，明确每个局部分组与同一记忆交互 |
| Local attention 边界 | 内部虚线框及左上弯折细线 | 全部清除，保留标题、三行 token、外层实线框 | 消除无算法含义的生图残留和多余分组边界 |
| 分区与输入 | 左侧约占四成，三张输入图，中央范围较小 | 两张输入图；三个主色区域实际约 33%／46%／21%，结构潜码放入中央入口区 | 联合 DiT 区域成为主视觉中心，保留可读间距；实际比例未机械写成指令目标 30%／48%／22% |
| Background + sky 输出 | 完整道路示意中有交通参与者 | 静态道路、建筑、植被与天空，无可见车辆或人体；车辆与人体仍保留在独立输出行 | 保持静态背景与动态资产的分解含义 |
| 中央第一行英文标签 | `Background`（背景） | `Background region`（背景局部区域） | 对应背景按空间邻域分组；`Vehicle i`、`Human j` 保持实例分组含义 |

保留：ViT 至 DiT 之间全部为抽象 token；E 左宽右窄、D 左窄右宽；不恢复 check、reuse、仿真或 known/unknown 等备注。标题、摘要、正文、公式、实验及正式 PDF 本轮均未改动。

验证：对 2079 × 756 的实际输出逐项自审，六项修复均可见；三区背景色区间读取自 y=726 的图像扫描线。主稿引用仍为原 `drivecompose-overview-20261021.png`，本候选未插入论文、未触发编译。场景插画继续作为机制示意，不作为实验结果。最终仍待用户确认视觉方案。

交付：[六项修复后的候选图](../../_archive/drivecompose/20261026-overview-intermediates/docs/figures/overview/drafts/inference-overview/candidate.png) · [完整生成指令](figures/overview/drafts/inference-overview/production-prompt.txt) · [逐项核验记录](figures/overview/drafts/inference-overview/design-spec.json)。

## 2026-10-26：将确认的总览图替换到中英文论文

本轮基线提交：`d741912c7a666308c5363cfb79a6c51b11b76e2b`。真实工作区起点已保存在 `paper/build/overview-replacement-baseline/`，包含两份入口、方法开头、旧图注、旧图与 PDF；不把先前已完成的候选生成或用户其他修改计入本轮。

范围：替换两版 Figure 1 图片引用及图注，修正双语方法开头的一句图示范围说明，同步活动图文档及检查脚本路径。标题、摘要、引言、贡献、实验数值、其余方法内容、公式和补充材料保持不变。

### 图片与排版

- `fig/drivecompose-overview-20261021.png` → `fig/drivecompose-inference-overview.png`。新图与确认候选逐字节一致，两版 PDF 内嵌图片像素也与该图一致。
- 保留原跨栏 `figure*`、`width=\textwidth`、编号和 `fig:teaser` 标签；按原比例放置，不修改模板边距、字号或行距。
- 图的展示范围由构建、检查和复用收窄为结构化编码、联合 DiT/CCM 与高斯解码，因此图注不再指称已经从图中删除的检查与复用部分。这些方法内容仍在正文中。

### 双语图注前后对照

英文 Figure 1：

修改前：

```latex
\caption{\textbf{DriveCompose overview.} (a) Calibrated images provide geometry, identity, and motion evidence, which is aggregated on background and canonical asset supports and encoded into structured latents. (b) A scene-conditioned flow transformer completes unknown codes while retaining observed content and suppressing free space. (c) Typed decoders produce Gaussian components. A check in the original views precedes scene reuse; camera and actor states then control composition and rendering. Scene depictions are schematic, not experimental outputs.}
```

修改后：

```latex
\caption{\textbf{DriveCompose overview.} (a) A shared ViT extracts visual evidence, which is aggregated on background and canonical asset supports and encoded into structured latents. (b) Joint completion combines local attention with cross-component memory (CCM) to exchange context across components. (c) Type-specific decoders produce the Gaussian background, canonical vehicle and human assets, and a sky map. Scene depictions are schematic, not experimental outputs.}
```

中文 Figure 1：

修改前：

```latex
\caption{\textbf{DriveCompose 总览。}（a）从有标定图像恢复几何、身份与运动证据，在背景和规范资产支撑上聚合并编码为结构化潜码。（b）场景条件流 Transformer 补全未知潜码，同时保留已见内容并抑制自由空间。（c）类型解码器输出高斯组件，在原始视角下检查后复用场景；相机与资产状态控制后续装配和渲染。图中场景为机制示意，不是实验输出。}
```

修改后：

```latex
\caption{\textbf{DriveCompose 总览。}（a）共享 ViT 提取视觉证据，在背景与规范资产支撑上聚合并编码为结构化潜码。（b）联合补全结合局部注意力与跨组件记忆（CCM），在组件间交换上下文。（c）类型专属解码器输出高斯背景、规范车辆与人体资产，以及天空贴图。图中场景为机制示意，不是实验输出。}
```

原因：按实际图件解释三个面板，明确 ViT、CCM 与类型解码的对应关系，保留机制示意身份；没有把插画写成实验输出。

### 方法开头的必要依赖修改

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 英文 §3 开头 | DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:teaser} shows the complete construction and reuse path. | DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:teaser} shows the main reconstruction pipeline. | 新图只展示主要重建流程，修正已失效的完整复用链路指称 |
| 中文 §3 开头 | DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:teaser} 展示完整的构建与复用链路。 | DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:teaser} 展示主要重建流程。 | 新图只展示主要重建流程，修正已失效的完整复用链路指称 |

### 验证与交付

- 现有 Tectonic 构建入口完成双语编译。旧英文 PDF 曾被 WPS 占用，先编译到临时目录；用户关闭 WPS 后替换正式文件并核对 SHA256。没有终止 WPS 进程或丢弃用户批注。
- 两版编译退出码均为 0；英文总计 11 页、中文总计 9 页。Figure 1 均在第 2 页；英文正文与结论仍在第 8 页结束，References 从第 9 页开始。
- 52 项稿件检查通过；日志无未定义引用、缺字或 overfull；两版图件页和英文正文末页已目视检查，无重叠或裁切。46 个受保护源码文件哈希保持不变。
- [英文正式稿](../paper/build/en/main.pdf) · [中文正式稿](../paper/build/zh/main_zh.pdf) · [本轮核验记录](../paper/build/overview-replacement-check.json)。

## 2026-10-26：按用户指定文件替换总览图

用户终止继续校正图形，明确指定 `docs/figures/overview/drafts/inference-overview/work/repair-attempt.png`。本轮只复制该文件并重编译，不对其内容或布局再作修改。HEAD 为 `d741912c7a666308c5363cfb79a6c51b11b76e2b`；真实未提交工作区基线及两版 PDF 保存在 `paper/build/latent-alignment-baseline/before-user-selection/`。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 两版 Figure 1 活动图 | 对齐候选，SHA256 `50b7c0b615c45f446c03441ab3a09397f7710847096b53c25a1a85a5e327bacf` | 用户指定图，SHA256 `79eb11de6e2257b089647fe5d314e93414b85381eb276fe3656937ad06c1701c` | 按用户最终选择替换 |
| `candidate.png` 和生成指令 | 后续局部对齐候选及指令 | 指定图原文件及其 `repair-attempt-prompt.txt` | 当前候选、溯源与论文图像一致 |
| 中英文图注、方法开头和其他源码 | 替换前现有内容 | 本次图片替换保持不变 | 该步仅更换已有图片，不改学术文本 |

验证：两版编译退出码 0；内嵌图片逐像素等于指定文件，38 个受保护源码文件哈希不变，52 项稿件检查通过。Figure 1 均在第 2 页；英文共 11 页，正文止于第 8 页、参考文献从第 9 页开始；中文共 9 页。已查看两版图件页和英文正文末页，无新增重叠或裁切。

[英文正式稿](../paper/build/en/main.pdf) · [中文正式稿](../paper/build/zh/main_zh.pdf) · [核验记录](../paper/build/overview-replacement-check.json)。

## 2026-10-26：本轮新增图注的语言清理

按用户“修改过的文本内容需要去 AI 味”要求，使用 humanizer 检查此次总览图替换改动过的双语图注及方法开头。范围限于已有修改，未扩展到整篇论文。HEAD 仍为 `d741912c7a666308c5363cfb79a6c51b11b76e2b`；真实基线、两版 PDF 和局部差异保存于 `paper/build/overview-replacement/humanizer-baseline/`。

具体问题与处理：

| 位置 | 原文 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 英文图注（b） | Joint completion combines local attention with cross-component memory (CCM) to exchange context across components. | Joint completion applies local attention within groups and shares context through cross-component memory (CCM). | 将泛化的“结合模块”改为具体分工，删除 cross-component / across components 的重复；分组自注意力和共享记忆已有 §3.4 及源码依据 |
| 中文图注（b） | 联合补全结合局部注意力与跨组件记忆（CCM），在组件间交换上下文。 | 联合补全在各组内执行局部注意力，并通过跨组件记忆（CCM）共享上下文。 | 同步英文，直接说明两个模块的作用 |
| 中文图注（a） | 共享 ViT 提取视觉证据，在背景与规范资产支撑上聚合并编码为结构化潜码。 | 共享 ViT 提取的视觉证据在背景与规范资产支撑上聚合，再编码为结构化潜码。 | 明确聚合和编码的对象是视觉证据，避免后半句仍以 ViT 为主语；英文对应句已明确，保持原样 |

保留：中英文方法开头、英文（a）、双语（c）及“机制示意、不是实验输出”的身份说明。未改变标题、摘要、贡献、公式、数值、引用、实验及用户指定图片；不因普通被动句、三类真实组件或必要限定而机械改写。

### 双语图注完整前后对照

English 修改前：

```latex
\caption{\textbf{DriveCompose overview.} (a) A shared ViT extracts visual evidence, which is aggregated on background and canonical asset supports and encoded into structured latents. (b) Joint completion combines local attention with cross-component memory (CCM) to exchange context across components. (c) Type-specific decoders produce the Gaussian background, canonical vehicle and human assets, and a sky map. Scene depictions are schematic, not experimental outputs.}
```

修改后：

```latex
\caption{\textbf{DriveCompose overview.} (a) A shared ViT extracts visual evidence, which is aggregated on background and canonical asset supports and encoded into structured latents. (b) Joint completion applies local attention within groups and shares context through cross-component memory (CCM). (c) Type-specific decoders produce the Gaussian background, canonical vehicle and human assets, and a sky map. Scene depictions are schematic, not experimental outputs.}
```

中文 修改前：

```latex
\caption{\textbf{DriveCompose 总览。}（a）共享 ViT 提取视觉证据，在背景与规范资产支撑上聚合并编码为结构化潜码。（b）联合补全结合局部注意力与跨组件记忆（CCM），在组件间交换上下文。（c）类型专属解码器输出高斯背景、规范车辆与人体资产，以及天空贴图。图中场景为机制示意，不是实验输出。}
```

修改后：

```latex
\caption{\textbf{DriveCompose 总览。}（a）共享 ViT 提取的视觉证据在背景与规范资产支撑上聚合，再编码为结构化潜码。（b）联合补全在各组内执行局部注意力，并通过跨组件记忆（CCM）共享上下文。（c）类型专属解码器输出高斯背景、规范车辆与人体资产，以及天空贴图。图中场景为机制示意，不是实验输出。}
```

对应技术依据：`paper/sec/3_method.tex` 的 Local self-attention / CCM 段，`src/drivecompose/networks/completion.py` 的局部分组注意力与 memory read/write。此轮仅使图注直接表达现有机制，没有增加实验或能力主张。

### 同轮按用户截图删除无关尾句

用户随后明确要求去掉图注中与流程内容无关的说明。此次删除覆盖前述“保留身份说明”的决定；真实删除前基线与局部差异位于 `paper/build/overview-replacement/humanizer-baseline/before-disclaimer-removal/`，HEAD 不变。

| 位置 | 原文 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 中文图注尾句 | 图中场景为机制示意，不是实验输出。 | 删除 | 用户明确要求图注只解释图中流程，移除附加说明 |
| 英文图注尾句 | Scene depictions are schematic, not experimental outputs. | 删除 | 与中文同步 |

此次删除保留刚完成的（a）主语澄清及（b）模块分工表述；三个面板的流程解释、图片、编号和正文其他内容不变。同步 `docs/figures/overview/caption.md`。

最终验证：本轮两版主稿重新编译成功；52 项稿件检查通过，日志无未定义引用、缺字或 overfull。36 个未授权改动的源码文件及指定图片共 37 项哈希不变，两份入口除图注外内容与语言清理前基线一致。图件均在第 2 页；英文共 11 页、正文在第 8 页结束、参考文献从第 9 页开始，中文共 9 页。已查看最终两版图件页和英文正文末页，无新增重叠或裁切。指定图片在两版 PDF 中逐像素一致。

[英文正式稿](../paper/build/en/main.pdf) · [中文正式稿](../paper/build/zh/main_zh.pdf) · [最终核验记录](../paper/build/overview-replacement-check.json)。

## 2026-10-26：移出中间产物，保留待确认修改

按用户要求，将本轮候选图、布局参考、重复图片、基线备份、临时 PDF、页面预览及编译辅助文件移至项目外。仅移动本轮未跟踪或已忽略的辅助文件，未移动已跟踪论文源码或正式 PDF。前文记录中的旧临时路径均按原目录层级保存在归档根目录下。

归档：[20261026-overview-intermediates](../../_archive/drivecompose/20261026-overview-intermediates)；[完整路径与哈希清单](../../_archive/drivecompose/20261026-overview-intermediates/archive-manifest.json)。

| 位置 | 清理前 | 清理后 | 原因 |
| --- | --- | --- | --- |
| 图件工作目录 | 候选副本、布局参考、逐轮指令与修改前图像 | 中间文件移入项目外；项目内保留正式图、最终指令及设计记录 | 清除重复和过程文件，保留必要溯源 |
| 构建工作目录 | 多轮基线、临时 PDF、渲染预览与辅助文件 | 移入项目外，保留正式双语 PDF、编译结果及最终核验记录 | 减少待提交文件，正式交付不变 |
| 文档链接和核验路径 | 指向项目内临时目录 | 更新为归档位置 | 保持可追溯和可恢复 |

本次只整理文件和更新记录；没有重新生成图片、修改论文正文或重新编译。暂不暂存、提交或推送，待用户确认清理后的统计。

## 2026-10-26：继续移出已提交的中间产物

按用户要求检查全部已跟踪文件，确认 30 个历史过程文件已不被当前论文编译依赖，移入[项目外归档](../../_archive/drivecompose/20261026-tracked-intermediates)。此轮开始时 HEAD 为 `d741912c7a666308c5363cfb79a6c51b11b76e2b`，部分编译日志已有未提交更新，因此归档保存本轮真实工作区字节；[清单](../../_archive/drivecompose/20261026-tracked-intermediates/archive-manifest.json)记录逐文件哈希，说明和校验脚本的修改前版本保存在归档 `records-before-cleanup/`。

| 类别 | 数量 | 处理与原因 |
| --- | ---: | --- |
| 编译日志、历史检查、表格预览、修订差异页和基线 | 8 | 可重建或阶段性过程材料，移出构建目录 |
| 旧总览图的设计、指令、绘图脚本和风格候选 | 12 | 当前已有明确采用版本，历史制作文件归档 |
| 旧总览图 PNG、TikZ 源码及输入插画素材 | 4 | 当前主稿不再引用；旧图哈希校验改为读取归档副本 |
| 未采用的训练/推理图 PPTX、PNG、指令和说明 | 6 | 目录明确为未应用草稿，移出活动图目录 |

当前总览图、实验图、四份正式 PDF、正文与补充材料源码、书目、算法实现、文档仍使用的流程图及原始来源材料保留。更新归档链接和旧图校验路径；`.gitignore` 补充 `.brf` 与编译文本日志规则，避免再次误加入 Git。没有改论文表述或重新编译，删除状态仅表示文件移出仓库工作区，原字节可从项目外归档恢复；不暂存、不提交、不推送，待用户确认。

验证：30 个归档文件逐一核对 SHA256，大小合计 11.91 MiB；四份正式 PDF、活动图片及其余受保护内容哈希不变，当前 LaTeX 无归档图件依赖，52 项稿件检查全部通过。清理后共 21 个已跟踪文件修改、30 个移出导致的删除状态和 5 个新增文件，合计 56 个待确认项；暂存区为空。

## 2026-10-26：提交前整合远端更新

用户授权提交并推送。远端新增 `1e2dd79`（标题与双语引言更新），本地确认修改先保存为 `f0a79bb`，随后重放到远端版本之上。保留远端标题、双语引言及补充材料，保留本次选定总览图、图注、方法开头和归档清理。两侧改动记录完整保留；更新过的历史日志移至项目外，未恢复到仓库。整合前两侧文件与重新编译产物保存在 `../_archive/drivecompose/20261026-push-integration/`。

中英文主稿重新编译成功，52 项检查通过；PDF 中总览图像素与用户指定图一致。英文共 11 页，正文与结论止于第 9 页，References 从第 9 页开始，超过 8 页正文目标；远端整合前版本也止于第 9 页。本轮未压缩或重写远端引言。已检查英文首页、两版图件页及英文第 8、9 页，无重叠或裁切。四份正式 PDF 保留，临时编译文件继续存放在项目外。

## 2026-10-27：同步实验二新图的双语图注与描述

基线提交：`e05587775d9a3b01e0365dc15b30ea1820daac47`（实验二图更换）。修改前两份实验源文件与 HEAD 一致。本轮仅同步图 3 的场景数量、行列含义与方法列表：新图为三行场景，五列从左至右为 GT、STORM、DGGT、StreetForward、Ours。保留原有向左偏移 2 m 的实验条件，未改实验数值、协议或实验一图注。

### paper/sec/4_experiments.tex

- 位置：正文描述
- 原文：Figure~\ref{fig:waymo-left-shift} presents qualitative view-extrapolation results on Waymo with the camera shifted $2\,\mathrm{m}$ to the left, illustrating vehicle shape, road layout, and occlusion boundaries across five scenes.
- 修改后：Figure~\ref{fig:waymo-left-shift} presents qualitative view-extrapolation results on Waymo with the camera shifted $2\,\mathrm{m}$ to the left, illustrating vehicle shape, road layout, and occlusion boundaries across three scenes.
- 原因：正文中的场景数量由五组同步为三组。

- 位置：图注
- 原文：Each column shows one scene. Rows, from top to bottom, show the reference image (GT), STORM, DGGT, and DriveCompose (Ours).
- 修改后：Each row shows one scene. Columns, from left to right, show the reference image (GT), STORM, DGGT, StreetForward, and DriveCompose (Ours).
- 原因：将每列场景改为每行场景，方法顺序改为从左至右并补入 StreetForward。

### paper/zh/4_experiments_zh.tex

- 位置：正文描述
- 原文：图~\ref{fig:waymo-left-shift} 展示 Waymo 数据集上相机向左偏移 $2\,\mathrm{m}$ 的定性视图外推结果，通过五组场景比较车辆外形、道路布局与遮挡边界。
- 修改后：图~\ref{fig:waymo-left-shift} 展示 Waymo 数据集上相机向左偏移 $2\,\mathrm{m}$ 的定性视图外推结果，通过三组场景比较车辆外形、道路布局与遮挡边界。
- 原因：正文中的场景数量由五组同步为三组。

- 位置：图注
- 原文：每列展示一个场景，从上至下依次为参考图像（GT）、STORM、DGGT 和 DriveCompose（Ours）。
- 修改后：每行展示一个场景，各列从左至右依次为参考图像（GT）、STORM、DGGT、StreetForward 和 DriveCompose（Ours）。
- 原因：将每列场景改为每行场景，方法顺序改为从左至右并补入 StreetForward。

图件 `paper/fig/assets/Shift.pdf` 保持原字节，SHA-256：`6d29c5b316b5e9fb2977549105eb716bb71b46ef10cff29f1a25b9f0cc5b3eb4`。

验证：中英文主稿均重新编译成功，图 3 分别位于英文第 8 页、中文第 6 页。实际 PDF 已包含每行场景、从左至右五列方法的新图注，并补入 StreetForward。最终 TeX 日志无未定义引用、缺字或 overfull 警告；两版图件页渲染无重叠或裁切。英文仍为 11 页、正文结论在第 9 页，中文仍为 9 页。图件原始字节不变，实验一描述及所有数值保持不变。按用户授权提交并推送双语说明与正式构建产物。

## 2026-10-28：主流程叙述、全文语言清理与全量引文核验

本轮基线是开始工作时的实际工作区，HEAD 为 `e98697e09af130895fe14f70fbc840571da28a0d`。工作区已有未提交修改；以下原文均从 [本轮基线快照](../../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/revision-20261028/baseline.zip) 读取，不把 HEAD 或用户既有修改冒充本轮原文。

主流程：多视角图像序列 → 视觉编码 → 规范空间特征聚合 → 潜表示编码 → 联合潜空间补全 → 分类型高斯解码 → 场景组合。标题不变，原有实验数值不变。

完整逐行差异见 [本轮独立 diff](../../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/revision-20261028/manuscript-changes.diff)。该差异与基线快照比较，区别于包含既有用户修改的 Git HEAD 差异。

参考文献 52 条均找到原始来源，修正 DriveDreamer 作者姓名顺序、补齐 Waymo 两位作者、补齐 LatentWorld 正式页码及链接。详见 [全量引用核验](../paper/REFERENCES.md)。

### 改动范围和理由

| 位置 | 原问题及处理 |
| --- | --- |
| 摘要 | 删除原视角检查句，明确视觉特征聚合、潜表示及分类型解码之间的关系。保留已有结果结论。 |
| 引言 | 用视觉编码—规范聚合—潜编码—联合补全—高斯解码—场景组合解释完整技术链，替换接受检查段。删除末尾机械式章节导航。 |
| 相关工作 | 比较焦点落在完成位置、组件坐标系和运动绑定；删去“重要比较对象”和检查装配结果的叙述。 |
| 方法 | 拆开视觉编码与规范聚合、潜编码与高斯解码，按数据流排列。移除检查器模块，补足编码输入、跨组件信息交换和刚体/骨架组合原理。可见性判定的完整条件保留在附录 D，正文保留加权聚合公式和三类掩码。 |
| 实验 | 将 Obs-Reg 定义移到实验指标处，保留 Pass 定义、分母、筛选口径、全部比较值和实际残余伪影描述。中文补齐英文已有的实验设置、定量比较与两张主结果表，数值逐格一致。 |
| 讨论 | 按表示的适用条件组织讨论，去除围绕检查器的辩解；保留固定照明、恢复误差、人体模板及物理仿真的实际边界。 |
| 结论 | 围绕完整方法链及已有 Waymo/消融证据收束，删去重复的模块属性描述。 |
| 总览图注 | 删除 schematic illustrations / 机制示意 尾注，补上场景组合的具体动作。图仍为方法总览，没有改写为实验结果。图片文件未在本轮改动。 |
| 补充材料训练 | 删除目标拒绝、导出和版本登记等工程叙述，用共享布局、完整目标与渲染监督解释训练机制；损失公式保持不变。 |
| 补充材料组合 | 移除重复的完整检查流程，保留刚体/蒙皮、协方差、观察方向与状态推进公式。Obs-Reg 的唯一活动定义位于主稿实验。 |
| 补充材料聚合 | 承接正文简化的完整投影、深度残差和有效观测条件，使聚合权重仍可追溯。 |

### 中英文原文与修改后逐项对照

以下按实际差异给出上下文；大段移动也会显示为删除和插入。正文删除的检查流程没有迁入其他论文章节；可复核旧文保存在基线快照，原实现代码未改。聚合判定条件则实际保留在附录 D。

#### 摘要

删除原视角检查句，明确视觉特征聚合、潜表示及分类型解码之间的关系。保留已有结果结论。

**英文：** [paper/sec/0_abstract.tex](../paper/sec/0_abstract.tex)

原文：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, vehicle, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We also render the composed scene from the original camera viewpoints to check its consistency with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. The completed components form a Gaussian scene that supports rendering under different camera and actor states.
\end{abstract}

```

修改后：

```latex
\begin{abstract}
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, vehicle, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. Visual features are aggregated in world coordinates for the background and canonical frames for vehicles and humans, then encoded into component-specific latent representations. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. Type-specific decoders convert the completed latents into Gaussian components whose rigid and skeletal bindings support composition under different camera and actor states.
\end{abstract}

```

**中文：** [paper/zh/0_abstract_zh.tex](../paper/zh/0_abstract_zh.tex)

原文：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、车辆或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还从原始相机视角渲染组合后的场景，检查补全结果是否与输入图像一致。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。补全后的组件构成高斯场景，支持在不同相机和参与者状态下渲染。
\end{abstract}

```

修改后：

```latex
\begin{abstract}
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、车辆或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。视觉特征在背景的世界坐标系与车辆、人体各自的规范坐标系中聚合，再编码为对应组件的潜表示。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。分类型解码器将补全潜码转换为高斯组件，其刚体与骨架绑定支持在不同相机和参与者状态下组合场景。
\end{abstract}

```

#### 引言

用视觉编码—规范聚合—潜编码—联合补全—高斯解码—场景组合解释完整技术链，替换接受检查段。删除末尾机械式章节导航。

**英文：** [paper/sec/1_introduction.tex](../paper/sec/1_introduction.tex)

原文：

```latex
As illustrated in Fig.~\ref{fig:teaser}, DriveCompose first recovers scene geometry and actor motion from the image sequence and aligns multi-frame image features with the background, vehicle, and human representations. The completion model captures local structure within each component, while cross-component memory gathers information from the background and actors and distributes the shared context back to each component. Missing regions of a vehicle or human can therefore be completed using information from the surrounding scene. The model learns to generate missing latent codes through flow matching~\cite{lipman2022flowmatching}, and component-specific decoders convert the completed representations into a Gaussian scene~\cite{kerbl2023gaussians}.

During completion, we retain surfaces established by reliable observations and generate the missing geometry and appearance. Newly generated surfaces may occlude previously visible regions, so we render the completed scene at the recorded camera viewpoints and actor states and compare it with the input images to check for inconsistencies introduced by completion. Scenes that pass this check can reuse the same completed content for rendering under different camera viewpoints and actor states (Sec.~\ref{sec:composition}).
```

修改后：

```latex
Figure~\ref{fig:teaser} follows the reconstruction pipeline. A visual encoder extracts image features and estimates scene geometry and actor motion. Motion-aware aggregation aligns features across views and time in the background and canonical asset frames, and type-specific encoders map them into a shared latent dimension. Local attention captures structure within each component. Cross-component memory gathers background and actor features and returns the shared scene context to each component, allowing missing surfaces to be inferred from both local observations and their surroundings. The model learns this joint completion through flow matching~\cite{lipman2022flowmatching} while retaining observed latent codes.

Type-specific Gaussian decoders turn the completed codes into a background, canonical vehicles, and articulated humans~\cite{kerbl2023gaussians}. Vehicle geometry follows rigid poses, and human geometry follows skeletal motion through its skinning weights. Scene composition places these components in world coordinates for the requested camera and actor states, reusing the same completed content across state changes (Sec.~\ref{sec:composition}).
```

原文：

```latex
\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework for closed-loop driving simulation. It recovers and completes backgrounds, vehicles, and humans from image sequences to construct compositional Gaussian scene assets. The resulting scene reuses the same completed assets for composition and rendering as camera poses, vehicle poses, and human poses change.
\item We develop a cross-component latent completion model based on conditional flow matching. Local attention models spatial relationships within each component, while cross-component memory aggregates background and actor features to provide scene context for generating each component's missing content.
\item We evaluate the framework and its key mechanisms through dynamic reconstruction, off-trajectory view synthesis, and component ablations. Experiments show that DriveCompose outperforms the evaluated baselines on reconstruction and view synthesis; cross-component information sharing reduces unseen-surface completion error, with larger absolute reductions under sparse observations.
\end{itemize}

Section~\ref{sec:related} reviews related work, Section~\ref{sec:method} presents the method, and Section~\ref{sec:experiments} reports experiments. Sections~\ref{sec:discussion} and~\ref{sec:conclusion} discuss limitations and conclude.

```

修改后：

```latex
\Needspace{6\baselineskip}
Our contributions are:
\begin{itemize}
\item We introduce DriveCompose, a generative reconstruction framework for closed-loop driving simulation. It recovers and completes backgrounds, vehicles, and humans from image sequences to construct compositional Gaussian scene assets. The resulting scene reuses the same completed assets for composition and rendering as camera poses, vehicle poses, and human poses change.
\item We develop a cross-component latent completion model based on conditional flow matching. Local attention models spatial relationships within each component, while cross-component memory aggregates background and actor features to provide scene context for generating each component's missing content.
\item We evaluate the framework and its key mechanisms through dynamic reconstruction, off-trajectory view synthesis, and component ablations. Experiments show that DriveCompose outperforms the evaluated baselines on reconstruction and view synthesis; cross-component information sharing reduces unseen-surface completion error, with larger absolute reductions under sparse observations.
\end{itemize}

```

**中文：** [paper/zh/1_introduction_zh.tex](../paper/zh/1_introduction_zh.tex)

原文：

```latex
如图~\ref{fig:teaser} 所示，DriveCompose 首先从图像序列中恢复场景几何与参与者运动，将多帧图像特征对齐到背景、车辆和人体各自的表示中。补全模型在每个组件内部建模局部结构，并通过跨组件记忆汇集背景与各对象的信息，再将共享上下文传回各组件。这样，车辆或人体的缺失部分可以结合周围场景的信息进行补全。模型通过流匹配学习生成缺失潜码~\cite{lipman2022flowmatching}，再由各组件的解码器将补全后的表示转化为高斯场景~\cite{kerbl2023gaussians}。

补全时，我们保留由可靠观测确定的表面，并生成缺失部分的几何与外观。新增表面可能遮挡原本可见的区域，因此我们在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较，检查补全是否引入观测不一致。通过检查的场景可复用同一份补全内容，在不同相机视角和参与者状态下渲染（第~\ref{sec:composition} 节）。
```

修改后：

```latex
图~\ref{fig:teaser} 展示完整重建流程。视觉编码器提取图像特征，并估计场景几何与参与者运动。运动感知聚合将跨视角、跨时刻特征对齐到背景和规范资产坐标系，类型专属编码器再将其映射为维度统一的潜码。局部注意力建模各组件内部的结构，跨组件记忆汇集背景与参与者特征，并将共享场景上下文传回各组件，使缺失表面能够同时依据局部观测与周围场景推断。模型通过流匹配学习联合补全~\cite{lipman2022flowmatching}，并在补全过程中保留已见潜码。

分类型高斯解码器将补全潜码转换为背景、规范车辆和关节化人体~\cite{kerbl2023gaussians}。车辆几何随刚体位姿移动，人体几何通过蒙皮权重随骨架运动。场景组合按照指定的相机与参与者状态，将这些组件放置到世界坐标系，在状态变化时复用同一份补全内容（第~\ref{sec:composition} 节）。
```

原文：

```latex
本文的贡献包括：
\begin{itemize}
\item 提出面向闭环驾驶仿真的生成式重建框架 DriveCompose。从图像序列中恢复并补全背景、车辆与人体，构建可组合的高斯场景资产。所得场景可在相机位姿、车辆位姿和人体姿态变化时，复用同一组补全资产进行组合与渲染。
\item 设计基于条件流匹配的跨组件潜空间补全模型。通过局部注意力建模各组件内部的空间关系，通过跨组件记忆汇集背景与参与者的特征，为各组件的缺失内容生成提供场景上下文。
\item 通过动态重建、轨迹外视图合成与组件消融评估框架及其关键机制。实验表明，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线；跨组件信息共享降低了未观测表面的补全误差，并在观测稀疏时带来更大的绝对误差降幅。
\end{itemize}

第~\ref{sec:related} 节回顾相关工作，第~\ref{sec:method} 节介绍方法，第~\ref{sec:experiments} 节报告实验，第~\ref{sec:discussion} 节和第~\ref{sec:conclusion} 节分别讨论局限性并总结全文。

```

修改后：

```latex
本文的贡献包括：
\begin{itemize}
\item 提出面向闭环驾驶仿真的生成式重建框架 DriveCompose。从图像序列中恢复并补全背景、车辆与人体，构建可组合的高斯场景资产。所得场景可在相机位姿、车辆位姿和人体姿态变化时，复用同一组补全资产进行组合与渲染。
\item 设计基于条件流匹配的跨组件潜空间补全模型。通过局部注意力建模各组件内部的空间关系，通过跨组件记忆汇集背景与参与者的特征，为各组件的缺失内容生成提供场景上下文。
\item 通过动态重建、轨迹外视图合成与组件消融评估框架及其关键机制。实验表明，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线；跨组件信息共享降低了未观测表面的补全误差，并在观测稀疏时带来更大的绝对误差降幅。
\end{itemize}

```

#### 相关工作

比较焦点落在完成位置、组件坐标系和运动绑定；删去“重要比较对象”和检查装配结果的叙述。

**英文：** [paper/sec/2_related_work.tex](../paper/sec/2_related_work.tex)

原文：

```latex
\paragraph{Generative reconstruction and completion.}
Image-conditioned 3D generation uses generated views~\cite{liu2023zero123,shi2024mvdream,gao2024cat3d} or structured latents encoding geometry and appearance~\cite{xiang2025trellis,xiang2026trellis2}. GenAssets learns driving-asset priors, CompleteSplat completes hidden Gaussian content, and JRM aggregates unaligned object observations through latent flow matching~\cite{yang2025genassets,liao2025complete,wu2026jrm}. LatentWorld organizes semantic occupancy generation around entity and background latents~\cite{park2026latentworld}, making structured scene generation an important point of comparison. DriveCompose targets RGB-renderable reconstruction conditioned on driving logs: a shared completion model exchanges context across world-space background and canonical vehicle and human codes. Observed codes and known free space constrain sampling, and original-view rendering checks the assembled result before reuse.
```

修改后：

```latex
\paragraph{Generative reconstruction and completion.}
Image-conditioned 3D generation uses generated views~\cite{liu2023zero123,shi2024mvdream,gao2024cat3d} or structured latents encoding geometry and appearance~\cite{xiang2025trellis,xiang2026trellis2}. GenAssets learns driving-asset priors, CompleteSplat completes hidden Gaussian content, and JRM aggregates unaligned object observations through latent flow matching~\cite{yang2025genassets,liao2025complete,wu2026jrm}. LatentWorld organizes semantic occupancy generation around entity and background latents~\cite{park2026latentworld}. DriveCompose targets RGB-renderable reconstruction conditioned on driving logs: a shared completion model exchanges context across world-space background and canonical vehicle and human codes. Observed codes and known free space condition the completion, and type-specific decoders preserve each component's spatial frame and motion binding.
```

**中文：** [paper/zh/2_related_work_zh.tex](../paper/zh/2_related_work_zh.tex)

原文：

```latex
\paragraph{生成式重建与补全。}
图像条件三维生成可通过生成视图~\cite{liu2023zero123,shi2024mvdream,gao2024cat3d}或编码几何与外观的结构化潜变量实现~\cite{xiang2025trellis,xiang2026trellis2}。GenAssets 学习驾驶资产先验，CompleteSplat 补全隐藏的高斯内容，JRM 通过潜空间流匹配聚合未对齐的对象观测~\cite{yang2025genassets,liao2025complete,wu2026jrm}。LatentWorld 围绕实体和背景潜变量组织语义占据生成~\cite{park2026latentworld}，是结构化场景生成的重要比较对象。DriveCompose 面向以驾驶日志为条件、可供 RGB 渲染的重建：共享补全模型在世界空间背景与规范车辆、人体潜码之间交换上下文。已见潜码和已知自由空间约束采样，原始视角渲染在复用前检查装配结果。
```

修改后：

```latex
\paragraph{生成式重建与补全。}
图像条件三维生成可通过生成视图~\cite{liu2023zero123,shi2024mvdream,gao2024cat3d}或编码几何与外观的结构化潜变量实现~\cite{xiang2025trellis,xiang2026trellis2}。GenAssets 学习驾驶资产先验，CompleteSplat 补全隐藏的高斯内容，JRM 通过潜空间流匹配聚合未对齐的对象观测~\cite{yang2025genassets,liao2025complete,wu2026jrm}。LatentWorld 围绕实体和背景潜变量组织语义占据生成~\cite{park2026latentworld}。DriveCompose 面向以驾驶日志为条件、可供 RGB 渲染的重建：共享补全模型在世界空间背景与规范车辆、人体潜码之间交换上下文。已见潜码和已知自由空间为补全提供条件，分类型解码器保留各组件的空间坐标系与运动绑定。
```

#### 方法

拆开视觉编码与规范聚合、潜编码与高斯解码，按数据流排列。移除检查器模块，补足编码输入、跨组件信息交换和刚体/骨架组合原理。可见性判定的完整条件保留在附录 D，正文保留加权聚合公式和三类掩码。

**英文：** [paper/sec/3_method.tex](../paper/sec/3_method.tex)

原文：

```latex
DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:teaser} shows the main reconstruction pipeline.
```

修改后：

```latex
DriveCompose converts multi-view image sequences into a compositional Gaussian scene through visual encoding, canonical feature aggregation, latent encoding, joint latent completion, type-specific Gaussian decoding, and scene composition (Fig.~\ref{fig:teaser}). Canonical aggregation aligns observations of each component across time; joint completion uses the surrounding scene to infer its missing geometry and appearance.
```

原文：

```latex
The decoder also carries forward the fixed support, identity, binding, and sky-validity metadata in Eq.~\ref{eq:world}. The layout is established from the input log; generation fills its unknown content. Simulation time changes the state of the decoded scene, while flow time indexes the construction of its latent codes.

\subsection{Visual recovery and canonical aggregation}
\label{sec:queries}

\paragraph{Shared visual encoding.}

The Driving Log Encoder uses transformer features~\cite{dosovitskiy2021vit,vaswani2017attention} to predict camera-axis depth, normals, confidence, semantics, and instance assignments from the calibrated image log. Trajectory-level identity slots separate persistent identity, dimensions, and human shape from frame-dependent root poses and joint rotations. Architectural details and state parameterization are given in Appendix D of the supplementary material.

\paragraph{Query supports.}
```

修改后：

```latex
The query layout assigns each latent code to a spatial location and scene component. Completion fills the unknown codes within this layout, and decoding preserves their component identities and motion bindings.

\subsection{Visual encoding}
\label{sec:visual-encoding}

The Driving Log Encoder extracts patch features from each image and exchanges pooled context across cameras and timestamps~\cite{dosovitskiy2021vit,vaswani2017attention}. Geometry heads predict camera-axis depth, normals, confidence, semantics, and instance assignments. These predictions connect the image features to 3D surfaces and their owning components. Trajectory-level identity slots separate persistent identity, dimensions, and human shape from frame-dependent root poses and joint rotations. Architectural details and state parameterization are given in Appendix D of the supplementary material.

\subsection{Canonical feature aggregation}
\label{sec:queries}

\paragraph{Spatial supports.}
```

原文：

```latex
Here $\bar{\mathbf q}_i$ is homogeneous, $\operatorname{xyz}$ extracts Euclidean coordinates, and $\mathbf A_i(t)$ is the weighted skinning transform. Projection into a camera gives depth $z_{i,t,v}$ and sampled feature, depth, and confidence $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$. With tolerance $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$, define $r=(d-z)/\eta$. A surface observation must lie inside the image, have valid depth and sufficient confidence, match the query's instance, and satisfy $|r|\leq1$. Background queries additionally require static-background semantics. Let $a_{i,t,v}$ denote this validity test. We aggregate
```

修改后：

```latex
Here $\bar{\mathbf q}_i$ is homogeneous, $\operatorname{xyz}$ extracts Euclidean coordinates, and $\mathbf A_i(t)$ is the weighted skinning transform. Projection gives query depth $z_{i,t,v}$ and samples image features $\boldsymbol\phi_{i,t,v}$, depth $d_{i,t,v}$, and confidence $c_{i,t,v}$. We weight observations by confidence and normalized depth residual $r=(d-z)/(\eta_{\rm abs}+\eta_{\rm rel}d)$. The indicator $a_{i,t,v}$ selects visible, depth-consistent observations of the same instance (Appendix D):
```

原文：

```latex
The query confidence is the maximum over accepted observations. A reliable ray votes for free space only when the entire support cell is in front of the measured surface; the criterion is detailed in Appendix D of the supplementary material.

Positive accumulated observation weight marks a query as observed. Otherwise, sufficient free-space votes mark it free, and the remainder is unknown. The masks $m_i$, $f_i$, and $u_i$ are mutually exclusive and satisfy $m_i+f_i+u_i=1$. Sky projection uses camera rotation alone, reliable sky semantics, and zero depth residual; sky queries receive no free-space votes.

\subsection{Structured latent representation and decoding}
\label{sec:codec}

Type-specific encoders map $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$ to codes $\mathbf z_i\in\mathbb R^D$. Each query keeps its type, ownership, and coordinate frame even though all codes have the same dimension. Visibility masks and confidence are supplied separately to the completion model. Partial and complete observations therefore use the same intrinsic encoding map. Before conditioning, unobserved codes are set to zero; the observed subset is denoted $\mathbf z^{\rm obs}$.

Background, rigid, and human Gaussian decoders independently map each query to $K$ child Gaussians confined to its support cell. Human children inherit the query's skinning weights; vehicle children share their asset's rigid transform. Opacity is multiplied by $1-f_i$, so free queries cannot produce visible Gaussians. A separate sky head predicts cubemap colors within the observation-supported domain $V_{\rm sky}$. Gaussian and appearance parameterizations are detailed in Appendix E of the supplementary material.

Decoding is per query: once the codec is frozen, an unchanged observed code produces unchanged Gaussian parameters. The completion network can exchange context across queries without changing this decoding property.

\subsection{Conditional generative reconstruction}
\label{sec:completion}
```

修改后：

```latex
The masks $m_i$, $f_i$, and $u_i$ distinguish observed surfaces, known free space, and unknown content, with $m_i+f_i+u_i=1$. Confidence is the maximum over valid observations; free space is inferred from reliable depth rays. Sky features are aggregated by viewing direction using camera rotation and sky semantics. Appendix D gives the visibility and free-space criteria.

\subsection{Latent representation encoding}
\label{sec:codec}

Type-specific encoders compress the aggregated feature and its spatial support, $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$, into a latent code $\mathbf z_i\in\mathbb R^D$. The shared latent dimension lets the completion model exchange information across background, vehicle, and human representations. Each query keeps its type, ownership, and coordinate frame even though all codes have the same dimension. Visibility masks and confidence are supplied separately to the completion model. Partial and complete observations therefore use the same intrinsic encoding map. Before conditioning, unobserved codes are set to zero; the observed subset is denoted $\mathbf z^{\rm obs}$.

\subsection{Joint latent-space completion}
\label{sec:completion}
```

原文：

```latex
All unknown queries interpolated in Eq.~\ref{eq:flow-path} require valid target codes, even if $s_i$ excludes some of them from the loss. This requirement determines how complete targets are constructed in Sec.~\ref{sec:training}.
```

修改后：

```latex
Complete scene or asset examples supply $\mathbf z_1$ at the unknown queries, while $s_i$ selects their contribution to the training loss (Sec.~\ref{sec:training}).
```

原文：

```latex
\subsection{Scene composition and observation consistency}
\label{sec:composition}
```

修改后：

```latex
\subsection{Type-specific Gaussian decoding}
\label{sec:decoding}

Background, rigid, and human Gaussian decoders independently map each query to $K$ child Gaussians confined to its support cell. Human children inherit the query's skinning weights; vehicle children share their asset's rigid transform. Opacity is multiplied by $1-f_i$, so free queries cannot produce visible Gaussians. A separate sky head predicts cubemap colors within the observation-supported domain $V_{\rm sky}$. Gaussian and appearance parameterizations are detailed in Appendix E of the supplementary material.

Each query is decoded independently. Freezing the codec and retaining observed codes therefore preserves the Gaussian parameters of observed surfaces.

\subsection{Scene composition}
\label{sec:composition}
```

原文：

```latex
At online step $k$, state $s_k$ specifies the ego pose, active assets, vehicle transforms, and human root and joint poses. Vehicles are placed by rigid transforms and humans by skinning; standard transformations and backend details are given in Appendix C of the supplementary material. The renderer composites the background, active assets, and valid sky:
```

修改后：

```latex
At time step $k$, state $s_k$ specifies the ego pose, active assets, vehicle transforms, and human root and joint poses. Vehicle poses transform canonical Gaussian centers and covariances rigidly. Human joint poses deform them through the stored skinning weights, so completed surfaces move with the corresponding body parts. Appendix C gives the transformations. The renderer composites the background, active assets, and valid sky:
```

原文：

```latex
Resetting or branching a trajectory changes state while preserving $\mathcal W$ and its seed. Finite support and supported sky directions determine coverage.

\paragraph{Checking a constructed scene.}

Fixed observed codes preserve decoded parameters, but a newly generated surface can still occlude them. Before accepting a scene, we render the completed candidate and an observed-only reference at the original cameras and actor states. The reference disables all non-observed queries. Let $e_{\rm cand}(p)$ and $e_{\rm obs}(p)$ be their mean absolute RGB errors at pixel $p$. We measure local degradation with

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

Averaging this quantity over reliable non-ego pixels prevents improvements in one region from cancelling degradation elsewhere. Acceptance also bounds absolute RGB and valid-depth errors, minimum coverage, and foreground intrusion, using aggregate and worst-view checks. An intrusion is a newly rendered surface in front of the predicted reference depth that is absent from the observed-only render; its rate is normalized over reliable non-sky geometry pixels. Predicted depth provides an observation-consistency reference. Independent geometry evaluation requires a separate reference. A rejected candidate is not exported for reuse.
```

修改后：

```latex
Changing the camera selects a new view of the composed scene; changing an actor state moves its completed canonical asset. The background and canonical content remain fixed across these operations, allowing the same reconstruction to be reused along different trajectories.
```

原文：

```latex
Learning is divided into four stages so that the completion target has a stable meaning (Table~\ref{tab:training}).
```

修改后：

```latex
We train visual recovery, the latent codec, and the completion model in sequence, then adapt completion through rendered observations (Table~\ref{tab:training}). Freezing the codec during completion training keeps its target latent space fixed.
```

原文：

```latex
For codec fitting, partial input and more complete observations share the same query positions, types, order, and ownership. With recovery and the entire codec frozen, complete scene or asset examples provide a valid target for every unknown query to train the GCM with Eq.~\ref{eq:flow-loss}. Real-log adaptation differentiates through flow integration, decoding, and rendering to update only the GCM. Complete-target samples can be interleaved to retain the prior, with each loss applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration. Detailed supervision, losses, and conditioning perturbations are provided in Appendix B of the supplementary material.

At inference, a log is encoded once; its support and evidence remain fixed during completion, and the decoded scene is checked before reuse under requested states (Section~\ref{sec:composition}).

```

修改后：

```latex
For codec fitting, partial input and more complete observations share the same query positions, types, order, and ownership. With recovery and the entire codec frozen, complete scene or asset examples provide a valid target for every unknown query to train the GCM with Eq.~\ref{eq:flow-loss}. Real-log adaptation differentiates through flow integration, decoding, and rendering to update only the GCM. Complete-target samples can be interleaved to retain the prior, with each loss applied only to samples carrying its required targets. Observed anchors are enforced by frozen decoding and hard code restoration. Detailed supervision, losses, and conditioning perturbations are provided in Appendix B of the supplementary material.

```

**中文：** [paper/zh/3_method_zh.tex](../paper/zh/3_method_zh.tex)

原文：

```latex
DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:teaser} 展示主要重建流程。
```

修改后：

```latex
DriveCompose 从多视角图像序列出发，依次经过视觉编码、规范空间特征聚合、潜表示编码、联合潜空间补全、分类型高斯解码与场景组合，得到可组合高斯场景（图~\ref{fig:teaser}）。规范聚合将各组件在不同时刻的观测对齐，联合补全则利用周围场景推断其缺失的几何与外观。
```

原文：

```latex
解码器同时保留式~\ref{eq:world} 中固定的支撑、身份、绑定和天空有效域元数据。布局由输入日志建立，生成过程填充其中的未知内容。仿真时间改变解码场景的状态，流时间则描述潜码的构建过程。

\subsection{视觉恢复与规范聚合}
\label{sec:queries}

\paragraph{共享视觉编码。}

Driving Log Encoder 使用 Transformer 特征~\cite{dosovitskiy2021vit,vaswani2017attention}，从有标定的图像日志预测相机光轴深度、法线、置信度、语义和实例归属。轨迹级身份槽将持久身份、尺寸和人体体型与逐帧变化的根位姿、关节旋转分开表示。网络结构与状态参数化细节见补充材料附录 D。

\paragraph{查询支撑。}
```

修改后：

```latex
查询布局为每个潜码指定空间位置和所属组件。补全在这一布局中生成未知潜码，解码后仍保留其组件身份与运动绑定。

\subsection{视觉编码}
\label{sec:visual-encoding}

Driving Log Encoder 从各图像提取 patch 特征，并在相机与时间戳之间交换池化上下文~\cite{dosovitskiy2021vit,vaswani2017attention}。几何预测头输出相机光轴深度、法线、置信度、语义和实例归属，将图像特征关联到三维表面及其所属组件。轨迹级身份槽将持久身份、尺寸和人体体型与逐帧变化的根位姿、关节旋转分开表示。网络结构与状态参数化细节见补充材料附录 D。

\subsection{规范空间特征聚合}
\label{sec:queries}

\paragraph{空间支撑。}
```

原文：

```latex
其中，$\bar{\mathbf q}_i$ 为齐次坐标，$\operatorname{xyz}$ 提取欧氏坐标，$\mathbf A_i(t)$ 为加权蒙皮变换。投影到相机后，得到深度 $z_{i,t,v}$ 以及采样特征、深度和置信度 $(\boldsymbol\phi_{i,t,v},d_{i,t,v},c_{i,t,v})$。给定容差 $\eta=\eta_{\rm abs}+\eta_{\rm rel}d$，定义 $r=(d-z)/\eta$。表面观测需位于图像内、深度有效、置信度足够，与查询的实例身份一致，并满足 $|r|\leq1$。背景查询还要求静态背景语义。令 $a_{i,t,v}$ 表示这一有效性判断，则聚合为
```

修改后：

```latex
其中，$\bar{\mathbf q}_i$ 为齐次坐标，$\operatorname{xyz}$ 提取欧氏坐标，$\mathbf A_i(t)$ 为加权蒙皮变换。投影得到查询深度 $z_{i,t,v}$，并采样图像特征 $\boldsymbol\phi_{i,t,v}$、深度 $d_{i,t,v}$ 和置信度 $c_{i,t,v}$，按置信度及归一化深度残差 $r=(d-z)/(\eta_{\rm abs}+\eta_{\rm rel}d)$ 为观测赋权。指示量 $a_{i,t,v}$ 选择同一实例中可见且深度一致的观测（附录 D）：
```

原文：

```latex
查询置信度取被接受观测中的最大值。仅当整个支撑单元都位于观测表面之前时，可靠射线才提供自由空间票；具体判定式见补充材料附录 D。

有效观测权重之和大于零时，查询被标为已见。否则，足够的自由空间票将其标为自由空间，其余查询为未知。掩码 $m_i$、$f_i$ 和 $u_i$ 互斥，满足 $m_i+f_i+u_i=1$。天空投影仅使用相机旋转，采用可靠天空语义和零深度残差，不接收自由空间票。

\subsection{结构化潜表示与解码}
\label{sec:codec}

类型专属编码器将 $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$ 映射为潜码 $\mathbf z_i\in\mathbb R^D$。各潜码维度相同，但查询仍保留类型、归属和坐标系。可见性掩码与置信度单独提供给补全模型，使部分观测与完整观测使用同一潜码编码映射。作为条件输入之前，未观测潜码置零；已见子集记为 $\mathbf z^{\rm obs}$。

背景、刚体和人体高斯解码器分别将每个查询独立映射为限制在其支撑单元内的 $K$ 个子高斯。人体子高斯继承查询的蒙皮权重；车辆子高斯共用所属资产的刚体变换。不透明度乘以 $1-f_i$，使自由空间查询不能产生可见高斯。独立天空头在观测支持的方向域 $V_{\rm sky}$ 内预测立方体贴图颜色。高斯与外观参数化详见补充材料附录 E。

解码逐查询执行：编解码器冻结后，不变的已见潜码产生不变的高斯参数。补全网络可以在查询之间交换上下文，同时保留这一解码性质。

\subsection{条件生成式重建}
\label{sec:completion}
```

修改后：

```latex
掩码 $m_i$、$f_i$ 和 $u_i$ 区分已见表面、已知自由空间和未知内容，满足 $m_i+f_i+u_i=1$。置信度取有效观测的最大值，自由空间由可靠深度射线确定。天空特征依据相机旋转和天空语义，按观察方向聚合。可见性与自由空间判定式见附录 D。

\subsection{潜表示编码}
\label{sec:codec}

类型专属编码器将聚合特征及其空间支撑 $[\mathbf h_i;\mathbf q_i;\boldsymbol\delta_i]$ 压缩为潜码 $\mathbf z_i\in\mathbb R^D$。统一的潜码维度使补全模型能够在背景、车辆和人体表示之间交换信息。各潜码维度相同，但查询仍保留类型、归属和坐标系。可见性掩码与置信度单独提供给补全模型，使部分观测与完整观测使用同一潜码编码映射。作为条件输入之前，未观测潜码置零；已见子集记为 $\mathbf z^{\rm obs}$。

\subsection{联合潜空间补全}
\label{sec:completion}
```

原文：

```latex
式~\ref{eq:flow-path} 中所有参与插值的未知查询都需要有效目标潜码，即使 $s_i$ 将其中一部分排除在损失之外。该要求决定了第~\ref{sec:training} 节中完整目标的构造方式。
```

修改后：

```latex
完整场景或资产样本为未知查询提供目标潜码 $\mathbf z_1$，$s_i$ 则选择其对训练损失的贡献（第~\ref{sec:training} 节）。
```

原文：

```latex
\subsection{场景装配与观测一致性}
\label{sec:composition}
```

修改后：

```latex
\subsection{分类型高斯解码}
\label{sec:decoding}

背景、刚体和人体高斯解码器分别将每个查询独立映射为限制在其支撑单元内的 $K$ 个子高斯。人体子高斯继承查询的蒙皮权重；车辆子高斯共用所属资产的刚体变换。不透明度乘以 $1-f_i$，使自由空间查询不能产生可见高斯。独立天空头在观测支持的方向域 $V_{\rm sky}$ 内预测立方体贴图颜色。高斯与外观参数化详见补充材料附录 E。

各查询独立解码。冻结编解码器并保留已见潜码，使已观测表面的高斯参数保持不变。

\subsection{场景组合}
\label{sec:composition}
```

原文：

```latex
在线步 $k$ 的状态 $s_k$ 指定自车位姿、活动资产、车辆变换，以及人体根位姿与关节姿态。车辆通过刚体变换放置，人体通过蒙皮变换放置；标准变换和后端细节见补充材料附录 C。渲染器合成背景、活动资产和有效天空：
```

修改后：

```latex
时刻 $k$ 的状态 $s_k$ 指定自车位姿、活动资产、车辆变换，以及人体根位姿与关节姿态。车辆位姿对规范高斯的中心和协方差施加刚体变换，人体关节姿态通过存储的蒙皮权重使高斯变形，补全表面因此随相应身体部位运动。具体变换见补充材料附录 C。渲染器合成背景、活动资产和有效天空：
```

原文：

```latex
重置或分支轨迹改变状态，同时保留 $\mathcal W$ 及其种子。有限空间支撑和有效天空方向决定覆盖范围。

\paragraph{构建场景的检查。}

固定已见潜码能够保持解码参数，但新增表面仍可能遮挡这些内容。接受场景之前，我们在原始相机和资产状态下渲染补全候选及仅由已见查询构成的观测参考；参考渲染关闭全部非已见查询。令 $e_{\rm cand}(p)$ 和 $e_{\rm obs}(p)$ 为像素 $p$ 处两者的平均绝对 RGB 误差，局部退化定义为

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

在可靠的非自车像素上平均这一量，避免某一区域的改善抵消其他区域的退化。接受条件还限制绝对 RGB 误差、有效深度误差和前景侵入率，并要求最低覆盖率；这些条件同时检查聚合结果和最差视图。前景侵入指新增渲染表面位于预测参考深度之前，且未出现在观测参考渲染中；其比例按可靠的非天空几何像素归一化。预测深度提供观测一致性参照，独立几何评测需要另一份参考。被拒绝的候选不导出复用。
```

修改后：

```latex
改变相机得到组合场景的新视角，改变参与者状态则移动其已补全的规范资产。背景与规范内容在这些操作中保持固定，使同一重建结果可以沿不同轨迹复用。
```

原文：

```latex
学习分为四个阶段，使补全目标保持稳定的含义（表~\ref{tab:training}）。
```

修改后：

```latex
我们依次训练视觉恢复模块、潜表示编解码器和补全模型，再通过渲染观测适配补全模型（表~\ref{tab:training}）。补全训练期间冻结编解码器，使目标潜空间保持固定。
```

原文：

```latex
编解码器拟合时，部分输入与更完整观测共享相同的查询位置、类型、顺序和归属。随后冻结恢复模块与整个编解码器，使用为每个未知查询提供有效目标的完整场景或资产样本，以式~\ref{eq:flow-loss} 训练 GCM。真实日志适配通过流积分、解码和渲染反向传播，仅更新 GCM。完整目标样本可交替使用以保留先验，各损失项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。详细监督、损失和条件扰动见补充材料附录 B。

推理时，日志只编码一次，补全过程中支撑与证据保持固定；解码后的场景通过检查后，按指定状态复用（第~\ref{sec:composition} 节）。

```

修改后：

```latex
编解码器拟合时，部分输入与更完整观测共享相同的查询位置、类型、顺序和归属。随后冻结恢复模块与整个编解码器，使用为每个未知查询提供有效目标的完整场景或资产样本，以式~\ref{eq:flow-loss} 训练 GCM。真实日志适配通过流积分、解码和渲染反向传播，仅更新 GCM。完整目标样本可交替使用以保留先验，各损失项仅作用于具备所需目标的样本。已见锚点由冻结解码和潜码硬恢复维持。详细监督、损失和条件扰动见补充材料附录 B。

```

#### 实验

将 Obs-Reg 定义移到实验指标处，保留 Pass 定义、分母、筛选口径、全部比较值和实际残余伪影描述。中文补齐英文已有的实验设置、定量比较与两张主结果表，数值逐格一致。

**英文：** [paper/sec/4_experiments.tex](../paper/sec/4_experiments.tex)

原文：

```latex
\paragraph{Qualitative comparison.}
Figure~\ref{fig:dynamic-reconstruction} shows that DriveCompose retains the pedestrian silhouette in the first row and the rear profile of the central vehicle in the second row, while preserving the surrounding street layout. The baseline renderings exhibit displaced or repeated actor contours in the upper rows and blurred or distorted road structure in the lower rows. DriveCompose more closely follows these reference structures in the displayed examples, with residual artifacts around the pedestrians in the third row and the parked pickup in the last row.
% Table 1 results supplied by the author on 2026-10-22.
\begin{table}[!htbp]
\centering
\footnotesize
\setlength{\tabcolsep}{1.3pt}
\renewcommand{\arraystretch}{1.08}
\setlength{\belowcaptionskip}{5pt}
\caption{Dynamic scene reconstruction on Waymo. Image quality is reported over the full image and annotated regions; depth is evaluated at valid LiDAR samples.}
\label{tab:regions_current}
\begin{tabular}{@{}lcccccc@{}}
\toprule
& \multicolumn{2}{c}{Full image} & \multicolumn{2}{c}{\shortstack{Dynamic Region}} & \multicolumn{2}{c}{Depth} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
Method & PSNR $\uparrow$ & SSIM $\uparrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ & AbsRel $\downarrow$ & $\delta_1$ $\uparrow$ \\
\midrule
STORM & 26.380 & 0.826 & 22.100 & 0.624 & 0.178 & 0.741 \\
DGGT & 27.410 & 0.794 & 22.710 & 0.651 & 0.249 & 0.668 \\
StreetForward & 27.010 & 0.818 & 20.919 & 0.592 & 0.197 & 0.759 \\
\midrule
Ours & \textbf{28.564} & \textbf{0.901} & \textbf{25.050} & \textbf{0.862} & \textbf{0.095} & \textbf{0.877} \\
\bottomrule
\end{tabular}
\end{table}
```

修改后：

```latex
\paragraph{Qualitative comparison.}
Figure~\ref{fig:dynamic-reconstruction} shows that DriveCompose retains the pedestrian silhouette in the first row and the rear profile of the central vehicle in the second row, while preserving the surrounding street layout. The baseline renderings exhibit displaced or repeated actor contours in the upper rows and blurred or distorted road structure in the lower rows. DriveCompose recovers these reference structures more closely. Residual artifacts occur around the pedestrians in the third row and the parked pickup in the last row.
% Table 1 results supplied by the author on 2026-10-22.
\begin{table}[!htbp]
\centering
\footnotesize
\setlength{\tabcolsep}{1.3pt}
\renewcommand{\arraystretch}{1.08}
\setlength{\belowcaptionskip}{5pt}
\caption{Dynamic scene reconstruction on Waymo. Image quality is reported over the full image and annotated regions; depth is evaluated at valid LiDAR samples.}
\label{tab:regions_current}
\begin{tabular}{@{}lcccccc@{}}
\toprule
& \multicolumn{2}{c}{Full image} & \multicolumn{2}{c}{\shortstack{Dynamic Region}} & \multicolumn{2}{c}{Depth} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
Method & PSNR $\uparrow$ & SSIM $\uparrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ & AbsRel $\downarrow$ & $\delta_1$ $\uparrow$ \\
\midrule
STORM & 26.380 & 0.826 & 22.100 & 0.624 & 0.178 & 0.741 \\
DGGT & 27.410 & 0.794 & 22.710 & 0.651 & 0.249 & 0.668 \\
StreetForward & 27.010 & 0.818 & 20.919 & 0.592 & 0.197 & 0.759 \\
\midrule
Ours & \textbf{28.564} & \textbf{0.901} & \textbf{25.050} & \textbf{0.862} & \textbf{0.095} & \textbf{0.877} \\
\bottomrule
\end{tabular}
\end{table}
```

原文：

```latex
\paragraph{Metrics.}
New-MAE measures linear-RGB error on independently identified surfaces unseen in every input; NVS-MAE covers all held-out target pixels.
Both MAE metrics and Obs-Reg use linear RGB on a $[0,1]$ scale.
Across input settings, New-MAE uses the common region unseen even under $\mathcal T_8$.
Obs-Reg averages the positive input-view regression in Eq.~\ref{eq:regression}.
Cov.\ is the non-sky target fraction with support coverage $>0.5$, opacity $>0.1$, and finite positive depth.
Uncovered pixels receive the same zero-RGB fill for error measurement.
Pass is the fraction of all requested worlds accepted by the fixed checker, including construction failures in its denominator.
Image metrics include every renderable candidate, including rejected worlds; non-renderable counts are recorded separately.
Metrics are averaged within each scene and then across scenes and training seeds.
```

修改后：

```latex
\paragraph{Metrics.}
New-MAE measures linear-RGB error on independently identified surfaces unseen in every input; NVS-MAE covers all held-out target pixels.
Both MAE metrics and Obs-Reg use linear RGB on a $[0,1]$ scale.
Across input settings, New-MAE uses the common region unseen even under $\mathcal T_8$.
Obs-Reg measures the increase in input-view RGB error after completion. For completed and observed-query renders with per-pixel errors $e_{\rm cand}(p)$ and $e_{\rm obs}(p)$, it averages
\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}
\label{eq:regression}
\end{equation}
over reliable non-ego pixels.
Cov.\ is the non-sky target fraction with support coverage $>0.5$, opacity $>0.1$, and finite positive depth.
Uncovered pixels receive the same zero-RGB fill for error measurement.
Pass is the fraction of requested scenes meeting fixed bounds on RGB and depth error, coverage, and foreground intrusion, evaluated both across views and in the worst view. Foreground intrusion measures added surfaces in front of reference depth over reliable non-sky pixels. Construction failures remain in the denominator.
Image metrics cover all renderable scenes before threshold filtering; non-renderable counts are recorded separately.
Metrics are averaged within each scene and then across scenes and training seeds.
```

原文：

```latex
\paragraph{Input sparsity.}
Table~\ref{tab:ablation-inputs} reuses checkpoints of the full model and the variant w/o CCM at $T=2,4,8$, with 6/12/24 input images.
The time span, target views, and common unseen-region mask remain fixed; evidence and queries are rebuilt from each input subset.
No model is retrained for this comparison.
For the full model, increasing $T$ from 2 to 8 reduces NVS-MAE from 0.043 to 0.026 and New-MAE from 0.092 to 0.062, while increasing coverage from 91.7\% to 96.3\%.
The full model outperforms the variant w/o CCM on all three metrics at every input count.
The absolute New-MAE reduction from CCM is 0.027, 0.020, and 0.016 at $T=2,4,8$, respectively, while the corresponding coverage gains are 3.2, 2.3, and 1.8 percentage points.
The larger absolute gains at lower input counts indicate that cross-component context is especially useful when observations are sparse.
```

修改后：

```latex
\paragraph{Input sparsity.}
Table~\ref{tab:ablation-inputs} reuses checkpoints of the full model and the variant w/o CCM at $T=2,4,8$, with 6/12/24 input images.
The time span, target views, and common unseen-region mask remain fixed; evidence and queries are rebuilt from each input subset.
No model is retrained for this comparison.
For the full model, increasing $T$ from 2 to 8 reduces NVS-MAE from 0.043 to 0.026 and New-MAE from 0.092 to 0.062, while increasing coverage from 91.7\% to 96.3\%.
The full model outperforms the variant w/o CCM on all three metrics at every input count.
The absolute New-MAE reduction from CCM is 0.027, 0.020, and 0.016 at $T=2,4,8$, respectively, while the corresponding coverage gains are 3.2, 2.3, and 1.8 percentage points.
Cross-component context therefore contributes more when each component has fewer observations.
```

**中文：** [paper/zh/4_experiments_zh.tex](../paper/zh/4_experiments_zh.tex)

原文：

```latex
（此处原无内容）
```

修改后：

```latex
\subsection{实验设置}
\label{sec:experimental_setup}

\paragraph{数据集与协议。}
我们使用 Waymo Open Dataset 的 798 条训练序列和 202 条验证序列。遵循 STORM，将每条验证序列划分为不重叠的 2 秒片段，每段包含以 10\,Hz 采样的 20 帧~\cite{yang2025storm}。FRONT、FRONT\_LEFT 和 FRONT\_RIGHT 相机在从零计数的帧索引 $\{0,5,10,15\}$ 提供观测，其余 16 帧用于评价，其中 12 帧对应时间插值，4 帧位于最后一次观测之后。评价时将预测与参考图像缩放至 $240\times160$ 像素~\cite{huang2026instantnurec}。

\paragraph{基线。}
我们比较 STORM、DGGT 和 StreetForward~\cite{yang2025storm,chen2025dggt,yu2026streetforward}。各方法使用相同输入时刻和目标视图，并采用各自的预处理。相机参数、额外几何输入与渲染适配器随实现设置记录。空间外推遵循 PointForward，比较扩散细化前的高斯渲染~\cite{chi2026pointforward}。

\paragraph{指标。}
我们在完整图像与共享标注区域上报告 PSNR 和 SSIM。深度评价在有效 LiDAR 投影点上计算逐帧尺度对齐后的 AbsRel 和 $\delta_1$~\cite{huang2026instantnurec}。分数先在片段内按帧平均，再在序列内按片段平均，最后对各序列等权汇总。新轨迹渲染使用固定真实图像与视频参考集合计算 FID 和 FVD。

\paragraph{实现细节。}
DriveCompose 从运动对齐的观测中重建各类型参与者资产，并与静态背景组合。重建耗时包括预处理、资产生成和场景组合；渲染耗时单独测量，资产复用通过重复场景查询评价。
```

原文：

```latex
图~\ref{fig:dynamic-reconstruction} 展示第一个主实验的五组场景重建对比，比较参与者轮廓、车辆边界和街道结构。
```

修改后：

```latex
我们在记录相机轨迹上的未观测时刻评价重建。表~\ref{tab:regions_current} 报告完整图像、动态区域及深度质量，图~\ref{fig:dynamic-reconstruction} 比较五个样例的渲染外观。

\paragraph{定量比较。}
DriveCompose 在表~\ref{tab:regions_current} 的六项指标上均取得最优结果。完整图像和动态区域 PSNR 分别比各自最强基线高 1.154 和 2.340 dB，对应 SSIM 达到 0.901 和 0.862；深度 AbsRel 降至 0.095，$\delta_1$ 达到 0.877。
```

原文：

```latex
\paragraph{定性比较。}
图~\ref{fig:dynamic-reconstruction} 中，DriveCompose 保留了第一行的行人轮廓和第二行中央车辆的尾部外形，同时恢复周围街道布局。基线渲染在上方样例中出现参与者轮廓偏移或重复，在下方样例中出现道路结构模糊或畸变。DriveCompose 在这些展示样例中更接近参考结构，第三行行人周围及最后一行停放的皮卡附近仍有残余伪影。
```

修改后：

```latex
\paragraph{定性比较。}
图~\ref{fig:dynamic-reconstruction} 中，DriveCompose 保留了第一行的行人轮廓和第二行中央车辆的尾部外形，同时恢复周围街道布局。基线渲染在上方样例中出现参与者轮廓偏移或重复，在下方样例中出现道路结构模糊或畸变。DriveCompose 更准确地恢复了这些参考结构。残余伪影集中在第三行行人周围及最后一行停放的皮卡附近。

\begin{table}[!htbp]
\centering
\footnotesize
\setlength{\tabcolsep}{1.3pt}
\renewcommand{\arraystretch}{1.08}
\setlength{\belowcaptionskip}{5pt}
\caption{Waymo 动态场景重建。图像质量在完整图像和标注区域上统计，深度在有效 LiDAR 投影点上评价。}
\label{tab:regions_current}
\begin{tabular}{@{}lcccccc@{}}
\toprule
& \multicolumn{2}{c}{完整图像} & \multicolumn{2}{c}{\shortstack{动态区域}} & \multicolumn{2}{c}{深度} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
方法 & PSNR $\uparrow$ & SSIM $\uparrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ & AbsRel $\downarrow$ & $\delta_1$ $\uparrow$ \\
\midrule
STORM & 26.380 & 0.826 & 22.100 & 0.624 & 0.178 & 0.741 \\
DGGT & 27.410 & 0.794 & 22.710 & 0.651 & 0.249 & 0.668 \\
StreetForward & 27.010 & 0.818 & 20.919 & 0.592 & 0.197 & 0.759 \\
\midrule
Ours & \textbf{28.564} & \textbf{0.901} & \textbf{25.050} & \textbf{0.862} & \textbf{0.095} & \textbf{0.877} \\
\bottomrule
\end{tabular}
\end{table}
```

原文：

```latex
图~\ref{fig:waymo-left-shift} 展示 Waymo 数据集上相机向左偏移 $2\,\mathrm{m}$ 的定性视图外推结果，通过三组场景比较车辆外形、道路布局与遮挡边界。
```

修改后：

```latex
我们在相机横向偏移 $\pm1$、$\pm2$ 和 $\pm4$ 米时评价轨迹外渲染，并保持相机朝向、内参和时间戳固定~\cite{zhu2025worldsplat,chi2026pointforward}。

表~\ref{tab:spatial_current} 报告各偏移幅度下分别评价左移和右移后平均的 FID 与 FVD，各方法使用相同的真实参考集合。图~\ref{fig:waymo-left-shift} 展示 Waymo 数据集上相机向左偏移 $2\,\mathrm{m}$ 的三组场景，比较车辆外形、道路布局与遮挡边界。
```

原文：

```latex
（此处原无内容）
```

修改后：

```latex
\begin{table}[t]
\centering
\footnotesize
\setlength{\tabcolsep}{2.5pt}
\renewcommand{\arraystretch}{1.08}
\caption{横向相机偏移下的新视角合成。FID 与 FVD 为各偏移幅度下左移和右移结果的平均，数值越低越好。}
\label{tab:spatial_current}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}l|rr|rr|rr@{}}
\toprule
方法
& \multicolumn{2}{c|}{偏移 $\pm 1$ m}
& \multicolumn{2}{c|}{偏移 $\pm 2$ m}
& \multicolumn{2}{c}{偏移 $\pm 4$ m} \\
\cmidrule(lr){2-3}
\cmidrule(lr){4-5}
\cmidrule(lr){6-7}
& FID $\downarrow$ & FVD $\downarrow$
& FID $\downarrow$ & FVD $\downarrow$
& FID $\downarrow$ & FVD $\downarrow$ \\
\midrule
STORM
& 61.97 & 722.27
& 83.72 & 1029.36
& 132.57 & 1704.16 \\
DGGT
& 73.99 & 984.00
& 93.36 & 1197.03
& 128.01 & 1661.70 \\
StreetForward
& 84.30 & 878.95
& 103.31 & 1095.02
& 123.58 & 1578.63 \\
\midrule
Ours
& \textbf{28.52} & \textbf{544.27}
& \textbf{37.43} & \textbf{673.17}
& \textbf{58.19} & \textbf{817.13} \\
\bottomrule
\end{tabular}%
}
\end{table}
```

原文：

```latex
\paragraph{指标。}
New-MAE 在独立判定为所有输入均不可见的表面上计算线性 RGB 误差；NVS-MAE 覆盖全部留出目标像素。
两项 MAE 指标和 Obs-Reg 均采用 $[0,1]$ 线性 RGB 尺度。
跨输入档位比较时，New-MAE 使用相对 $\mathcal T_8$ 仍不可见的共同区域。
Obs-Reg 对原始输入视角中式~\ref{eq:regression} 的正退化取平均。
Cov.\ 为目标非天空区域中支撑覆盖度 $>0.5$、不透明度 $>0.1$ 且深度有限为正的像素比例。
未覆盖像素统一填零 RGB 后计入误差。
Pass 为固定检查器接受的世界占全部申请世界的比例，构建失败保留在分母中。
图像指标纳入全部可渲染候选，包括被拒绝的世界；不可渲染数量单独记录。
先在场景内平均，再对场景及训练种子汇总。
```

修改后：

```latex
\paragraph{指标。}
New-MAE 在独立判定为所有输入均不可见的表面上计算线性 RGB 误差；NVS-MAE 覆盖全部留出目标像素。
两项 MAE 指标和 Obs-Reg 均采用 $[0,1]$ 线性 RGB 尺度。
跨输入档位比较时，New-MAE 使用相对 $\mathcal T_8$ 仍不可见的共同区域。
Obs-Reg 衡量补全后输入视角 RGB 误差的增量。令补全场景与已见查询渲染的逐像素误差分别为 $e_{\rm cand}(p)$ 和 $e_{\rm obs}(p)$，在可靠的非自车像素上平均
\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}
Cov.\ 为目标非天空区域中支撑覆盖度 $>0.5$、不透明度 $>0.1$ 且深度有限为正的像素比例。
未覆盖像素统一填零 RGB 后计入误差。
Pass 为满足固定 RGB 与深度误差、覆盖率和前景侵入阈值的场景比例，同时按跨视图汇总与最差视图评价。前景侵入衡量可靠非天空像素中新增加在参考深度之前的表面。构建失败保留在分母中。
图像指标统计阈值筛选前的全部可渲染场景，不可渲染数量单独记录。
先在场景内平均，再对场景及训练种子汇总。
```

原文：

```latex
\paragraph{输入稀疏度。}
表~\ref{tab:ablation-inputs} 复用 Ours 和 w/o CCM 的权重，在 $T=2,4,8$ 下分别输入 6/12/24 张图像。
时间跨度、目标视图和共同未见区域掩码固定，证据与查询由各档输入重新构建。
这项比较不重新训练模型。
对 Ours，将 $T$ 从 2 增至 8 后，NVS-MAE 从 0.043 降至 0.026，New-MAE 从 0.092 降至 0.062，覆盖率从 91.7\% 提高至 96.3\%。
在每档输入下，Ours 的三项指标均优于 w/o CCM。
在 $T=2,4,8$ 时，CCM 带来的 New-MAE 绝对降幅分别为 0.027、0.020 和 0.016，覆盖率增益分别为 3.2、2.3 和 1.8 个百分点。
输入较少时更大的绝对收益表明，跨组件上下文在观测稀疏时更有帮助。
```

修改后：

```latex
\paragraph{输入稀疏度。}
表~\ref{tab:ablation-inputs} 复用 Ours 和 w/o CCM 的权重，在 $T=2,4,8$ 下分别输入 6/12/24 张图像。
时间跨度、目标视图和共同未见区域掩码固定，证据与查询由各档输入重新构建。
这项比较不重新训练模型。
对 Ours，将 $T$ 从 2 增至 8 后，NVS-MAE 从 0.043 降至 0.026，New-MAE 从 0.092 降至 0.062，覆盖率从 91.7\% 提高至 96.3\%。
在每档输入下，Ours 的三项指标均优于 w/o CCM。
在 $T=2,4,8$ 时，CCM 带来的 New-MAE 绝对降幅分别为 0.027、0.020 和 0.016，覆盖率增益分别为 3.2、2.3 和 1.8 个百分点。
各组件观测较少时，跨组件上下文的贡献更大。
```

#### 讨论

按表示的适用条件组织讨论，去除围绕检查器的辩解；保留固定照明、恢复误差、人体模板及物理仿真的实际边界。

**英文：** [paper/sec/5_discussion.tex](../paper/sec/5_discussion.tex)

原文：

```latex
\section{Limitations}
\label{sec:discussion}

DriveCompose represents a finite region under fixed illumination. Errors in recovered depth, identity, or canonical pose can enter the observed anchors and constrain later completion incorrectly. Vehicles are rigid, and humans retain fixed clothing volume and skeleton binding; poses outside the template's support can expose missing geometry. Reference-world coordinates provide context at construction, while contact and collision validity after an edit depend on the physical backend. The observation check assesses agreement with recorded evidence. Geometry outside that evidence and appearance under changed illumination require separate supervision or modeling.

```

修改后：

```latex
\section{Discussion}
\label{sec:discussion}

DriveCompose separates canonical scene content from camera and actor states. Its representation covers a finite region under fixed illumination, with rigid vehicles and humans bound to a fixed skeleton and clothing volume. Depth, identity, and canonical-pose estimates determine the observed anchors used by completion, so recovery errors propagate into the reconstructed geometry. Human articulation follows the template's geometric support, and contact and collision behavior are handled by the physical simulator. Relighting and changes in clothing geometry require corresponding appearance and deformation models.

```

**中文：** [paper/zh/5_discussion_zh.tex](../paper/zh/5_discussion_zh.tex)

原文：

```latex
\section{局限}
\label{sec:discussion}

DriveCompose 表示固定照明下的有限区域。恢复深度、身份或规范姿态中的错误可能进入已见锚点，并对后续补全施加错误约束。车辆采用刚体模型，人体保留固定衣物体积和骨架绑定；超出模板支撑范围的姿态可能暴露缺失几何。参考世界坐标提供构建时的上下文，编辑后的接触与碰撞有效性则依赖物理后端。观测检查衡量与已记录证据的一致性，证据之外的几何和照明变化下的外观需要额外监督或建模。

```

修改后：

```latex
\section{讨论}
\label{sec:discussion}

DriveCompose 将规范场景内容与相机、参与者状态分开表示。当前表示覆盖固定照明下的有限区域，车辆采用刚体模型，人体绑定固定骨架和衣物体积。深度、身份与规范姿态估计决定补全使用的已见锚点，因此恢复误差会传递到重建几何。人体关节运动遵循模板的几何支撑，接触与碰撞行为由物理仿真器处理。重光照与衣物几何变化需要相应的外观和形变模型。

```

#### 结论

围绕完整方法链及已有 Waymo/消融证据收束，删去重复的模块属性描述。

**英文：** [paper/sec/6_conclusion.tex](../paper/sec/6_conclusion.tex)

原文：

```latex
We presented DriveCompose, a generative reconstruction framework for compositional driving scenes. Its structured latent representation gathers image evidence into background and canonical assets, giving missing content a defined location, identity, and motion model before generation. Conditional completion uses scene context while retaining observed evidence, and typed decoding produces the components of a reusable Gaussian scene. Separating content construction from state-driven composition allows subsequent camera and actor changes to reuse the same completion.

```

修改后：

```latex
We presented DriveCompose, which reconstructs compositional driving scenes through canonical feature aggregation, latent encoding, and joint completion. Local attention and cross-component memory combine component structure with scene context. Type-specific Gaussian decoders retain identity and motion bindings, allowing completed assets to be composed under changing camera and actor states. On Waymo, DriveCompose improves dynamic reconstruction and off-trajectory view synthesis. Ablations show that cross-component context improves unseen-surface completion.

```

**中文：** [paper/zh/6_conclusion_zh.tex](../paper/zh/6_conclusion_zh.tex)

原文：

```latex
本文提出 DriveCompose，用于可组合驾驶场景的生成式重建。结构化潜表示将图像证据汇入背景与规范资产，使缺失内容在生成之前就具有明确的位置、身份和运动模型。条件补全利用场景上下文并保留已观测证据，类型解码输出可复用高斯场景的组成部分。内容构建与状态驱动装配相分离，使后续相机和资产状态变化能够使用同一次补全结果。

```

修改后：

```latex
本文提出 DriveCompose，通过规范特征聚合、潜表示编码与联合补全重建可组合驾驶场景。局部注意力和跨组件记忆结合组件结构与场景上下文，分类型高斯解码保留身份与运动绑定，使补全资产能够在不同相机和参与者状态下组合。在 Waymo 上，DriveCompose 改善了动态重建与轨迹外视图合成。消融实验表明，跨组件上下文改善了未见表面补全。

```

#### 总览图注

删除 schematic illustrations / 机制示意 尾注，补上场景组合的具体动作。图仍为方法总览，没有改写为实验结果。图片文件未在本轮改动。

**英文：** [paper/main.tex](../paper/main.tex)

原文：

```latex
% !TEX program = xelatex
% DriveCompose manuscript for CVPR 2027; inherited CVPR style files.
\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}
\input{preamble}
\input{fontsetup}
\usepackage{tikz}
\usepackage{needspace}
\usetikzlibrary{arrows.meta,patterns}
\definecolor{cvprblue}{rgb}{0.21,0.49,0.74}
\usepackage[pagebackref,breaklinks,colorlinks,allcolors=cvprblue]{hyperref}
\usepackage{url}
\usepackage{multirow}
\usepackage{float}
\usepackage{colortbl}
\usepackage{graphicx}
\usepackage{booktabs}
\def\paperID{*****}
\def\confName{CVPR}
\def\confYear{2027}
\title{DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion}
\author{Anonymous CVPR Submission}
\begin{document}
\maketitle
\input{sec/0_abstract}
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}
  \caption{\textbf{DriveCompose overview.} (a) Visual encoding, motion-aware canonical aggregation, and type-specific latent encoding convert image logs into structured latents. (b) Group-local attention and CCM read/write update component tokens for conditional-flow completion. (c) Query-wise Gaussian decoding produces background and sky, canonical rigid assets, and canonical human assets. Rigid assets retain their rigid binding; humans inherit skinning weights and a rest skeleton. Scene and asset images are schematic illustrations.}
  \label{fig:teaser}
\end{figure*}
\def\CVPRMAIN{}
\input{sec/1_introduction}
\input{sec/2_related_work}
\input{sec/3_method}
% Ablation results supplied by the author on 2026-10-23.
\input{sec/4_experiments}
\input{sec/5_discussion}
\input{sec/6_conclusion}
\FloatBarrier
{\small
\bibliographystyle{ieeenat_fullname}
\bibliography{main}
}
\end{document}

```

修改后：

```latex
% !TEX program = xelatex
% DriveCompose manuscript for CVPR 2027; inherited CVPR style files.
\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}
\input{preamble}
\input{fontsetup}
\usepackage{tikz}
\usepackage{needspace}
\usetikzlibrary{arrows.meta,patterns}
\definecolor{cvprblue}{rgb}{0.21,0.49,0.74}
\usepackage[pagebackref,breaklinks,colorlinks,allcolors=cvprblue]{hyperref}
\usepackage{url}
\usepackage{multirow}
\usepackage{float}
\usepackage{colortbl}
\usepackage{graphicx}
\usepackage{booktabs}
\def\paperID{*****}
\def\confName{CVPR}
\def\confYear{2027}
\title{DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion}
\author{Anonymous CVPR Submission}
\begin{document}
\maketitle
\input{sec/0_abstract}
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}
  \caption{\textbf{DriveCompose overview.} (a) Visual encoding, motion-aware canonical aggregation, and type-specific latent encoding convert image logs into structured latents. (b) Group-local attention and CCM read/write update component tokens for conditional-flow completion. (c) Query-wise Gaussian decoding produces background and sky, canonical rigid assets, and canonical human assets. Rigid assets retain their rigid binding; humans inherit skinning weights and a rest skeleton. Rigid transforms and skeletal motion place the decoded assets in the background to form the composed scene.}
  \label{fig:teaser}
\end{figure*}
\def\CVPRMAIN{}
\input{sec/1_introduction}
\input{sec/2_related_work}
\input{sec/3_method}
% Ablation results supplied by the author on 2026-10-23.
\input{sec/4_experiments}
\input{sec/5_discussion}
\input{sec/6_conclusion}
\FloatBarrier
{\small
\bibliographystyle{ieeenat_fullname}
\bibliography{main}
}
\end{document}

```

**中文：** [paper/main_zh.tex](../paper/main_zh.tex)

原文：

```latex
% !TEX program = xelatex
% DriveCompose 中文对照稿；会议年份统一为 CVPR 2027。
\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}
\input{preamble}
\input{fontsetup}
\usepackage{tikz}
\usepackage{needspace}
\usetikzlibrary{arrows.meta,patterns}
\usepackage{iftex}
\ifXeTeX
  \usepackage{fontspec}
  \usepackage{xeCJK}
  \setCJKmainfont{FandolSong-Regular.otf}[BoldFont=FandolSong-Bold.otf,ItalicFont=FandolKai-Regular.otf]
  \setCJKsansfont{FandolHei-Regular.otf}[BoldFont=FandolHei-Bold.otf]
  \setCJKmonofont{FandolFang-Regular.otf}
\else
  \PackageError{DriveCompose}{The Chinese counterpart requires XeLaTeX}{Compile main_zh.tex with XeLaTeX or Tectonic.}
\fi
\definecolor{cvprblue}{rgb}{0.21,0.49,0.74}
\usepackage[pagebackref,breaklinks,colorlinks,allcolors=cvprblue]{hyperref}
\usepackage{url}
\usepackage{multirow}
\def\paperID{*****}
\def\confName{CVPR}
\def\confYear{2027}
\title{DriveCompose：通过联合补全实现驾驶场景的可组合生成式重建}
\author{Anonymous CVPR Submission}
\begin{document}
\maketitle
\input{zh/0_abstract_zh}
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}
  \caption{\textbf{DriveCompose 总览。}（a）视觉编码、运动感知的规范聚合与类型专属潜码编码将图像日志转换为结构化潜码。（b）组内局部注意力与 CCM 读写更新组件 token，用于条件流补全。（c）逐查询高斯解码生成背景与天空、规范刚体资产和规范人体资产。刚体资产保留刚体绑定，人体资产继承蒙皮权重与静止骨架。场景及资产图像均为机制示意。}
  \label{fig:teaser}
\end{figure*}
\def\CVPRMAIN{}
\input{zh/1_introduction_zh}
\input{zh/2_related_work_zh}
\input{zh/3_method_zh}
% 已写入用户于 2026-10-23 提供的消融结果。
\input{zh/4_experiments_zh}
\Needspace{13\baselineskip}
\input{zh/5_discussion_zh}
\Needspace{14\baselineskip}
\input{zh/6_conclusion_zh}
\FloatBarrier
{\small
\bibliographystyle{ieeenat_fullname}
\bibliography{main}
}
\end{document}

```

修改后：

```latex
% !TEX program = xelatex
% DriveCompose 中文对照稿；会议年份统一为 CVPR 2027。
\documentclass[10pt,twocolumn,letterpaper]{article}
\usepackage[review]{cvpr}
\input{preamble}
\input{fontsetup}
\usepackage{tikz}
\usepackage{needspace}
\usetikzlibrary{arrows.meta,patterns}
\usepackage{iftex}
\ifXeTeX
  \usepackage{fontspec}
  \usepackage{xeCJK}
  \setCJKmainfont{FandolSong-Regular.otf}[BoldFont=FandolSong-Bold.otf,ItalicFont=FandolKai-Regular.otf]
  \setCJKsansfont{FandolHei-Regular.otf}[BoldFont=FandolHei-Bold.otf]
  \setCJKmonofont{FandolFang-Regular.otf}
\else
  \PackageError{DriveCompose}{The Chinese counterpart requires XeLaTeX}{Compile main_zh.tex with XeLaTeX or Tectonic.}
\fi
\definecolor{cvprblue}{rgb}{0.21,0.49,0.74}
\usepackage[pagebackref,breaklinks,colorlinks,allcolors=cvprblue]{hyperref}
\usepackage{url}
\usepackage{multirow}
\def\paperID{*****}
\def\confName{CVPR}
\def\confYear{2027}
\title{DriveCompose：通过联合补全实现驾驶场景的可组合生成式重建}
\author{Anonymous CVPR Submission}
\begin{document}
\maketitle
\input{zh/0_abstract_zh}
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{fig/drivecompose-inference-overview.png}
  \caption{\textbf{DriveCompose 总览。}（a）视觉编码、运动感知的规范聚合与类型专属潜码编码将图像日志转换为结构化潜码。（b）组内局部注意力与 CCM 读写更新组件 token，用于条件流补全。（c）逐查询高斯解码生成背景与天空、规范刚体资产和规范人体资产。刚体资产保留刚体绑定，人体资产继承蒙皮权重与静止骨架。刚体变换与骨架运动将解码资产放置到背景中，完成场景组合。}
  \label{fig:teaser}
\end{figure*}
\def\CVPRMAIN{}
\input{zh/1_introduction_zh}
\input{zh/2_related_work_zh}
\input{zh/3_method_zh}
% 已写入用户于 2026-10-23 提供的消融结果。
\input{zh/4_experiments_zh}
\Needspace{13\baselineskip}
\input{zh/5_discussion_zh}
\Needspace{14\baselineskip}
\input{zh/6_conclusion_zh}
\FloatBarrier
{\small
\bibliographystyle{ieeenat_fullname}
\bibliography{main}
}
\end{document}

```

#### 补充材料训练

删除目标拒绝、导出和版本登记等工程叙述，用共享布局、完整目标与渲染监督解释训练机制；损失公式保持不变。

**英文：** [paper/supplementary/training.tex](../paper/supplementary/training.tex)

原文：

```latex
We freeze recovery and train the type-specific encoders and decoders. For each sample, partial input establishes the query layout once. More complete observations are then aggregated on exactly the same positions, types, order, and ownership. This correspondence is required for latent completion: separately rebuilding a complete-scene layout would change the variables being predicted. RGB, depth, and silhouette supervision train the decoded scene, with empty-space opacity and Gaussian-scale regularization. Gaussian-set targets can also be matched as sets; direct coordinate supervision is used only when child correspondences are available.
```

修改后：

```latex
We freeze recovery and train the type-specific encoders and decoders. For each sample, partial input establishes the query layout once. More complete observations are then aggregated on exactly the same positions, types, order, and ownership. This shared layout aligns partial evidence and complete targets query by query. RGB, depth, and silhouette supervision train the decoded scene, with empty-space opacity and Gaussian-scale regularization. Gaussian-set targets can also be matched as sets; direct coordinate supervision is used only when child correspondences are available.
```

原文：

```latex
The notation $\langle\ell\rangle_{\Omega}$ denotes a mean over valid elements of mask $\Omega$. The depth target $d$ and its validity mask are supplied by the available supervision; they do not make the observation check an independent accuracy measurement.
```

修改后：

```latex
The notation $\langle\ell\rangle_{\Omega}$ denotes a mean over valid elements of mask $\Omega$. The depth target $d$ and its validity mask are supplied by the available supervision.
```

原文：

```latex
We freeze recovery and the entire codec, encode complete targets as $\mathbf z_1$, and optimize the completion transformer with Eq.~(9) of the main paper. Complete scene or asset examples must provide a valid target for every unknown query in Eq.~(8) of the main paper; partial real logs alone do not meet this condition. Complete scenes provide cross-component context, while complete assets supply within-object content. A validity test rejects targets with unsupported unknown queries.
```

修改后：

```latex
We freeze recovery and the entire codec, encode complete targets as $\mathbf z_1$, and optimize the completion transformer with Eq.~(9) of the main paper. Complete scene or asset examples provide target codes for the unknown queries in Eq.~(8) of the main paper. Complete scenes provide cross-component context, while complete assets supply within-object geometry and appearance.
```

原文：

```latex
A log is encoded once, its support and evidence are fixed, and the completion model integrates the unknown codes. We then decode and check the scene before exporting its fixed content. Runtime rendering uses only this content and the requested states. Recovery, codec, completion, and query-definition versions are recorded together, since changing any of the first two changes the latent distribution on which completion was learned.

```

修改后：

```latex
A log is encoded once, its support and evidence are fixed, and the completion model integrates the unknown codes. Type-specific decoders produce the background and canonical assets. Rendering composes these fixed components under the requested camera and actor states.

```

**中文：** [paper/supplementary/training_zh.tex](../paper/supplementary/training_zh.tex)

原文：

```latex
冻结恢复模块，训练类型专属编码器和解码器。每个样本先由部分输入建立一次查询布局，再将更完整的观测聚合到完全相同的位置、类型、顺序和归属上。这种对应关系是潜码补全的前提；若为完整场景另建布局，就会改变待预测变量。RGB、深度和轮廓监督训练解码场景，并结合空域不透明度与高斯尺度正则。高斯集合目标也可以采用集合匹配；仅在子高斯对应已知时使用直接坐标监督。
```

修改后：

```latex
冻结恢复模块，训练类型专属编码器和解码器。每个样本先由部分输入建立一次查询布局，再将更完整的观测聚合到完全相同的位置、类型、顺序和归属上。共享布局使部分观测与完整目标逐查询对应。RGB、深度和轮廓监督训练解码场景，并结合空域不透明度与高斯尺度正则。高斯集合目标也可以采用集合匹配；仅在子高斯对应已知时使用直接坐标监督。
```

原文：

```latex
符号 $\langle\ell\rangle_{\Omega}$ 表示在掩码 $\Omega$ 的有效元素上取平均。深度目标 $d$ 及其有效掩码由可用监督提供；它们不使观测检查成为独立的精度测量。
```

修改后：

```latex
符号 $\langle\ell\rangle_{\Omega}$ 表示在掩码 $\Omega$ 的有效元素上取平均。深度目标 $d$ 及其有效掩码由可用监督提供。
```

原文：

```latex
冻结恢复模块和整个编解码器，将完整目标编码为 $\mathbf z_1$，并以主稿式~(9) 优化补全 Transformer。完整场景或资产样本必须为主稿式~(8) 中的每个未知查询提供有效目标，单独的部分真实日志不满足这一条件。完整场景提供跨组件上下文，完整资产提供对象内部内容；任一未知查询缺少有效目标潜码时，有效性检查会拒绝该样本。
```

修改后：

```latex
冻结恢复模块和整个编解码器，将完整目标编码为 $\mathbf z_1$，并以主稿式~(9) 优化补全 Transformer。完整场景或资产样本为主稿式~(8) 中的未知查询提供目标潜码。完整场景提供跨组件上下文，完整资产提供对象内部的几何与外观。
```

原文：

```latex
日志只编码一次，随后固定支撑与证据，由补全模型积分未知潜码。解码并检查场景后，导出固定内容；运行时渲染仅使用这些内容和指定状态。恢复模块、编解码器、补全网络与查询定义的版本一并记录，因为前两者的变化会改变补全网络学习的潜分布。

```

修改后：

```latex
日志只编码一次，随后固定支撑与证据，由补全模型积分未知潜码。分类型解码器生成背景与规范资产，渲染时按指定相机与参与者状态组合这些固定组件。

```

#### 补充材料组合

移除重复的完整检查流程，保留刚体/蒙皮、协方差、观察方向与状态推进公式。Obs-Reg 的唯一活动定义位于主稿实验。

**英文：** [paper/supplementary/composition.tex](../paper/supplementary/composition.tex)

原文：

```latex
\section{Scene composition and checking details}
\label{sec:supp-composition}
```

修改后：

```latex
\section{Scene composition details}
\label{sec:supp-composition}
```

原文：

```latex
For humans, the weighted skinning transform is $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$, where $\mathbf B_j$ and $\mathbf P_j$ are rest and current global joints in the root frame. The transformed center is $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$. The combined local linear map $\mathbf J_i$ gives covariance $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$. Its inverse $\mathbf J_i^{-1}$ maps viewing directions into the canonical frame; the direction is normalized before appearance evaluation. Nearly singular skinning transforms are rejected. The root pose controls overall placement, while the root joint retains its rest transform.
```

修改后：

```latex
For humans, the weighted skinning transform is $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$, where $\mathbf B_j$ and $\mathbf P_j$ are rest and current global joints in the root frame. The transformed center is $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$. The combined local linear map $\mathbf J_i$ gives covariance $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$. Its inverse $\mathbf J_i^{-1}$ maps viewing directions into the canonical frame; the direction is normalized before appearance evaluation. The inverse is evaluated for nonsingular skinning transforms. The root pose controls overall placement, while the root joint retains its rest transform.
```

原文：

```latex
Resetting or branching a trajectory changes state while preserving $\mathcal W$ and its seed. Finite support and supported sky directions determine coverage. Road meshes and collision proxies share the visual assets' coordinates and are maintained by the physical backend.

\paragraph{Checking a constructed scene.}

Fixed observed codes preserve decoded parameters, but a newly generated surface can still occlude them. Before accepting a scene, we render the completed candidate and an observed-only reference at the original cameras and actor states. The reference disables all non-observed queries. Let $e_{\rm cand}(p)$ and $e_{\rm obs}(p)$ be their mean absolute RGB errors at pixel $p$. We measure local degradation with

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

Averaging this quantity over reliable non-ego pixels prevents improvements in one region from cancelling degradation elsewhere. Acceptance also bounds absolute RGB and valid-depth errors, minimum coverage, and foreground intrusion, using aggregate and worst-view checks. An intrusion is a newly rendered surface in front of the predicted reference depth that is absent from the observed-only render; its rate is normalized over reliable non-sky geometry pixels. Predicted depth provides an observation-consistency reference. Independent geometry evaluation requires a separate reference. A rejected candidate is not exported for reuse.


```

修改后：

```latex
Camera and actor state changes reuse the same background and canonical assets. Road meshes and collision proxies use the same coordinates as the visual components, allowing their motion to be driven by a physical simulator.

```

**中文：** [paper/supplementary/composition_zh.tex](../paper/supplementary/composition_zh.tex)

原文：

```latex
\section{场景装配与检查细节}
\label{sec:supp-composition}
```

修改后：

```latex
\section{场景组合细节}
\label{sec:supp-composition}
```

原文：

```latex
人体使用加权蒙皮变换 $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$，其中 $\mathbf B_j$ 和 $\mathbf P_j$ 是根坐标系中的静止与当前全局关节矩阵。变换后的中心为 $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$。组合局部线性映射 $\mathbf J_i$ 将协方差变换为 $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$，其逆 $\mathbf J_i^{-1}$ 将观察方向映回规范坐标，并在外观求值前归一化。接近奇异的蒙皮变换被拒绝。根位姿控制整体放置，根关节保持静止变换。
```

修改后：

```latex
人体使用加权蒙皮变换 $\mathbf A_i=\sum_j w_{ij}\mathbf P_j\mathbf B_j^{-1}$，其中 $\mathbf B_j$ 和 $\mathbf P_j$ 是根坐标系中的静止与当前全局关节矩阵。变换后的中心为 $\bar{\boldsymbol\mu}_i^w=\mathbf T^w_h\mathbf A_i\bar{\boldsymbol\mu}_i^h$。组合局部线性映射 $\mathbf J_i$ 将协方差变换为 $\mathbf J_i\boldsymbol\Sigma_i\mathbf J_i^\top$，其逆 $\mathbf J_i^{-1}$ 将观察方向映回规范坐标，并在外观求值前归一化。上述逆映射使用非奇异蒙皮变换。根位姿控制整体放置，根关节保持静止变换。
```

原文：

```latex
重置或分支轨迹改变状态，同时保留 $\mathcal W$ 及其种子。有限空间支撑和有效天空方向决定覆盖范围。道路网格与碰撞代理采用和视觉资产一致的坐标，由物理后端维护。

\paragraph{构建场景的检查。}

固定已见潜码能够保持解码参数，但新增表面仍可能遮挡这些内容。接受场景之前，我们在原始相机和资产状态下渲染补全候选及仅由已见查询构成的观测参考；参考渲染关闭全部非已见查询。令 $e_{\rm cand}(p)$ 和 $e_{\rm obs}(p)$ 为像素 $p$ 处两者的平均绝对 RGB 误差，局部退化定义为

\begin{equation}
\Delta e(p)=\max\{e_{\rm cand}(p)-e_{\rm obs}(p),0\}.
\label{eq:regression}
\end{equation}

在可靠的非自车像素上平均这一量，避免某一区域的改善抵消其他区域的退化。接受条件还限制绝对 RGB 误差、有效深度误差和前景侵入率，并要求最低覆盖率；这些条件同时检查聚合结果和最差视图。前景侵入指新增渲染表面位于预测参考深度之前，且未出现在观测参考渲染中；其比例按可靠的非天空几何像素归一化。预测深度提供观测一致性参照，独立几何评测需要另一份参考。被拒绝的候选不导出复用。


```

修改后：

```latex
相机与参与者状态变化时复用同一背景和规范资产。道路网格、碰撞代理与视觉组件采用相同坐标，可由物理仿真器驱动其运动。

```

#### 补充材料聚合

承接正文简化的完整投影、深度残差和有效观测条件，使聚合权重仍可追溯。

### 验证与交付

- 英文主稿：正文、图表、讨论及完整结论在第 8 页内，参考文献从第 9 页开始，总计 11 页。
- 中文主稿：10 页；中英文补充材料各 3 页。
- 四份 PDF 均重新编译；最终日志无未定义引用、缺字或 overfull 溢出。
- 双语引用集合、显示公式与结果表数值一致；英文原表全部结果数值未改。
- 页面对照检查覆盖正文、总览图、方法公式、结果图表、参考文献与补充材料。
- [最终核验记录](../paper/provenance/revision-verification-20261028.json)、[英文主稿](../paper/build/en/main.pdf)、[中文主稿](../paper/build/zh/main_zh.pdf)。


## 2026-10-28：总览图展开、参考场景替换与刚体解码命名

本轮范围：Figure 1、对应图注、解码模块术语、项目图示文档及源码类名。最初基线为 HEAD `e98697e09af130895fe14f70fbc840571da28a0d`，修改前图件和相关文件保存在项目外 `_archive/drivecompose/20261028-overview-expansion/baseline/`。工作期间出现的并行稿件修订原样保留，不计入本轮；最终图件接入前的主文件原文记录在该归档的 work/integration-baseline.json。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| Figure 1 编码区 | ViT、Canonical aggregation 和 E_b/E_v/E_h 的简略模块 | 展示多视角原图、时空特征、对齐/筛选/融合、类型潜码编码 E_b/E_r/E_h | 区分三种操作各自的作用 |
| Figure 1 联合补全 | Local attention 框同时包住 CCM，输出端口内部来源不清 | 组内注意力；组件 token 与旧记忆进入 Read，更新记忆与组件 token 进入 Write，残差合成 U，再经过 Flow update | 明确局部与跨组件交互，输出由更新组件表示产生 |
| Figure 1 输出 | 泛化街景、车辆和人体示意；背景残留交通参与者 | 使用用户给定全景的三个相邻视图，输出对应的空背景、完整邮政车及人体规范资产；补充刚体/蒙皮绑定、状态装配与闭环用途 | 建立场景一致的输入—表示—复用叙事 |
| 论文主稿与补充材料 | Background, vehicle, and human decoders；背景、车辆和人体解码器 | Background, rigid, and human Gaussian decoders；背景、刚体和人体高斯解码器 | 以运动模型命名解码器，当前车辆仍为刚体实例 |
| 项目实现与文档 | RigidVehicleDecoder / Rigid Vehicle Decoder | RigidGaussianDecoder / Rigid Gaussian Decoder | 统一刚体高斯解码命名；保留 vehicle 权重键与车辆数据类型 |
| 论文图件格式 | 一张整图 PNG | SVG 原生文字/模块/连线 + 光栅素材，论文插入矢量 PDF，PNG 用于预览 | 固定精确连线与文字，支持后续局部编辑 |

输入保留用户提供全景的原像素；背景、完整车辆与人体资产是 Image Gen 生成的表示示意，未作为真实模型预测或实验结果。DGGT 参考只用于横向分区、分支组织与图形语言。最终科学结构通过 [build_figure.py](../../_archive/drivecompose/20261028-imagegen-return/retired-native/build_figure.py) 重建；未复制其 pose-free 或渲染细化机制。

验证：13 项既有单元测试通过；归一化 AST 对比确认解码器仅重命名和文档更新，计算行为及 checkpoint 键不变。双语主稿编译成功，图均在第 2 页；英文正文止于第 8 页，References 从第 9 页开始。独立知情审查及局部回归确认核心路径、完整车辆和人体绑定；原文字交叉已修复。[核验记录](../paper/provenance/overview-expansion-20261028.json)。


## 2026-10-28：按用户要求改为整图 Image Gen，并重查输入输出

- **原问题**：上一版使用 SVG 重建，违背用户明确选择的生图路线；输入缺少共同场景线索，输出像独立素材，组合场景表达不足。
- **本轮修改**：通过内置 Image Gen 重绘整张图，突出同一街口的部分可见观测；空背景、完整邮政车与规范人体均回到同一场景语境；三类资产及场景状态汇入 Compose & render，输出组合街景并标注闭环用途。
- **技术回归**：修正几何/运动来源箭头；删除原始潜码绕过交互的旁路；用三类局部组件共同范围框明确更新输出。独立审查确认输入输出叙事及最后局部修改通过。
- **文件对照**：`main.tex` / `main_zh.tex` 中 `drivecompose-inference-overview.pdf` 改为同名 `.png`；PNG 与 Image Gen 返回文件逐字节一致。旧 SVG、图件 PDF 和构建脚本已归档，正式论文不再引用它们。未修改本轮范围外的并行正文、引用或实验。
- **来源边界**：整图依据用户提供场景生成；输入像素不再宣称与原图逐像素一致，输出为机制示意而非实测模型结果。当前记录见 [Image Gen 来源与审核](figures/overview/imagegen-provenance.json)。

本轮 PNG 接入后，双语主稿重新编译成功，图均在第 2 页；英文仍为 8 页正文、References 从第 9 页开始。最终日志无未定义引用/文献、缺字或 Overfull 报告。已查看两版实际 Figure 1 所在页面，见 [本轮核验](../paper/provenance/overview-imagegen-20261028.json)。


## 2026-10-29：刚体分支术语与实现核验

基线提交：`e98697e09af130895fe14f70fbc840571da28a0d`；本轮从已有未提交工作区接续，真实基线与逐行差异位于 [归档](../../_archive/drivecompose/20261029-rigid-terminology/changes.diff)。

核验结论：车辆解码已经调用 `RigidGaussianDecoder`；聚合使用共享整体位姿，装配前验证 SE(3)，规范高斯与尺寸固定。人体分支单独使用骨架蒙皮。此次修正遗漏的术语，不更改网络计算、实验数值、引用、数据类别、序列化字段或 checkpoint 键。当前总览 PNG 已使用 Rigid 标签，保留原图。

| 位置 | 原文 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 主文及补充的查询放置公式 | `k_i=\mathrm{vehicle}` | `k_i=\mathrm{rigid}` | 按运动模型命名分支，与解码器一致。 |
| 规范空间聚合 | vehicle anchors are motion-normalized／车辆锚点经运动规范化后 | rigid anchors are aligned by inverse SE(3) transforms／刚体锚点经逆 SE(3) 变换对齐后 | 明确刚体规范对齐机制。 |
| 解码 | vehicle children／车辆子高斯 | rigid children／刚体子高斯 | 与 RigidGaussianDecoder 和整体位姿绑定一致。 |
| 潜表示 | background, vehicle, and human representations／背景、车辆和人体表示 | background, rigid, and human representations／背景、刚体和人体表示 | 聚合、编码、补全与解码统一术语。 |

修改范围：摘要、引言中本方法的表示说明、相关工作末段的本方法说明、方法正文、补充前端/解码/训练/组合，及对应技术文档、Mermaid 图和代码注释。实验中的真实车辆实例、外部工作的车辆能力、数据标签与历史溯源记录保持其原义。主文首次定义说明车辆是当前刚体资产实例，不将术语统一解读为新增类别的实测验证。

本轮验证：13 项现有单元测试、双帧刚体聚合检查和 52 项稿件检查均通过。AST 对照确认三份 Python 源文件仅改注释/文档字符串。未执行 PyTorch 网络前向（当前环境无 PyTorch）。四份正式 PDF 均重新编译并检查受影响页面；英文正文止于第 8 页，References 从第 9 页开始。三张技术 Mermaid 图的 SVG/PNG 已重新生成，活动总览 PNG 保持不变。

迁移校验原先把未单独归档的源码直接当作历史快照，既有修改和本轮修改都会使该项失败。已从清单记录的原始提交恢复 9 份文件到归档，逐一匹配原 SHA256，并仅更新历史副本索引；当前源码及原始清单不回退、不修改。核验记录见 [刚体术语核验](../paper/provenance/rigid-terminology-20261029.json)。


## 2026-10-29：消融改为通用指标，新结果留空

用户明确要求保留组件消融和输入数量两张表，中英文同步删除旧自定义指标，新指标结果留空。基线提交为 `e98697e09af130895fe14f70fbc840571da28a0d`，本轮从已有未提交工作区接续；真实基线与逐行差异在 [本轮归档](../../_archive/drivecompose/20261029-standard-ablation/changes.diff)，不把此前修改算入本轮。

| 位置 | 修改前 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 组件表（双语 Table 4） | New-MAE / Obs-Reg / Cov. / Pass，三行既有汇总 | Full image：PSNR / SSIM / LPIPS；Dynamic regions：PSNR / SSIM，保留 w/o GCM、w/o CCM、Ours，15 格留空 | 通用指标评价最终重建与动态目标，旧汇总不能换算 |
| 输入数量表（双语 Table 5） | NVS-MAE / New-MAE / Cov.，六行既有汇总 | PSNR / SSIM / LPIPS，T=2/4/8、每档两版本，18 格留空 | 同一 checkpoint 和目标集合下评价输入敏感性 |
| 指标定义 | 自定义误差增量公式、隐藏面掩码、覆盖及多阈值接受标准 | 留出全图三项指标、动态区域 PSNR/SSIM；共同预处理、分辨率与标注掩码 | 删除不再使用的定义及相关公式 |
| 组件/输入分析 | “CCM reduces New-MAE from 0.078 … to 0.062 …”；“CCM 将 New-MAE 从 … 0.078 降至 … 0.062 …” | “These comparisons assess the contributions …”；“这两项对照分别评价……贡献。” | 只说明对照目的，不沿用旧数值证明新指标收益 |
| 摘要 | “Ablations show that sharing context across components improves completion of unseen surfaces.”；“消融实验表明，组件间共享上下文能够改善未见表面的补全。” | 删除该句，保留其他方法与主实验表述 | 当前消融结果留空，该胜出结论暂缺新指标依据 |
| 引言与结论 | “with larger absolute error reductions under sparser observations”；“在输入观测较少时带来更大的绝对误差降幅”等 | 删除依赖旧指标的结果句/分句 | 同步全篇证据状态，保留机制介绍及其他主结果 |

消融使用 Waymo 留出配对图像，保留两表共用的 29 时间戳、三路相机、嵌套输入和 24 步补全设计；未改主实验的 20 帧协议。移除原隐藏面完整参考线的指标依赖。组件对照与输入敏感性的训练/测试区别保持明确。状态驱动复用段落及其余实验内容逐字核对未变。

历史原始数值仍保存在 `paper/provenance/ablation-results-20261023.json` 及修改前备份，未覆盖或转换。新的指标合同为 [ablation-standard-metrics-20261029.json](../paper/provenance/ablation-standard-metrics-20261029.json)。实验方案、证据表及稿件检查脚本同步当前状态。

验证：54 项稿件检查通过；两版各 33 个新结果格为空，双语公式一致；其他主实验及方法/讨论未改。中英文主稿均重新编译成功，最终日志无未定义引用、缺字或 Overfull；组件表和输入表的实际页面已检查。英文 11 页，技术正文止于第 8 页；中文 9 页。参考文献分别从英文第 8 页、中文第 7 页开始。中文原 PDF 的占用通过归档旧文件并安装已验证候选解决。未执行训练或评测。详见 [核验记录](../paper/provenance/ablation-standard-metrics-verification-20261029.json)。


## 2026-10-29：刚体代码接口统一（替代本日上一轮兼容约定）

用户明确要求代码也统一为 rigid，删除旧接口和 checkpoint 兼容。本轮仅改代码、配置、测试、示例和接口文档，未改 LaTeX。基于已有未提交工作区继续修改；本轮 [真实差异](../../_archive/drivecompose/20261029-rigid-api/changes.diff) 与基线保存在项目外归档。

| 原接口 | 新接口 |
| --- | --- |
| `RigidVehicleAsset` / `TokenKind.VEHICLE` | `RigidAsset` / `TokenKind.RIGID` |
| `vehicles` / `vehicle_poses` / `vehicle_dimensions` | `rigids` / `rigid_poses` / `rigid_dimensions` |
| `codec.vehicle` / `vehicle.*` 权重 | `codec.rigid` / `rigid.*` 权重 |
| `vehicle_shape` / `vehicle_grid` / `vehicle_motion` | `rigid_shape` / `rigid_grid` / `rigid_motion` |

世界文件改为 schema 2、资产 kind=rigid；CheckpointRecord 仅接受 drivecompose-rigid-v2 查询规范。没有旧名称别名、旧键转换或自动迁移。仓库（含隐藏和忽略文件，不含 Git 对象库）未发现 .pt/.pth/.ckpt/.safetensors checkpoint 文件，因此未执行权重文件删除。历史证据和项目外源码备份不参与运行。

17 项测试全部通过，无跳过，涵盖真实 CPU PyTorch 前向/反向、新权重保存加载、旧权重拒绝、旧世界格式拒绝及刚体装配链路。src、configs 和 examples 内 vehicle 文本为零；纯数值示例输出 rigid 字段。核验与隔离测试环境位于 [本轮归档](../../_archive/drivecompose/20261029-rigid-api/verification.json)。

## 2026-10-29：回填两组通用指标消融结果

基线提交：`e98697e09af130895fe14f70fbc840571da28a0d`。本轮继承已有未提交工作区，真实修改前源稿、PDF 及哈希保存在 [本轮基线](../../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/ablation-results-revision/baseline-manifest.json)，不将 HEAD 到工作区的全部差异算作本轮。论文范围仅为中英文 §4.4 的两张消融表及两处结果分析；[逐行差异](../../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/ablation-results-revision/changes.diff)。

| 位置（中英文对应） | 原文/原值 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 组件表 Ours | 五个空格 | 28.913 / 0.911 / 0.129 / 25.617 / 0.873 | 写入作者汇总值，指标依次为全图 PSNR/SSIM/LPIPS、动态区域 PSNR/SSIM |
| 组件表 w/o GCM | 五个空格 | 27.137 / 0.867 / 0.183 / 23.431 / 0.811 | 保留原值及三位小数 |
| 输入表 T=2 Ours | 三个空格 | 26.341 / 0.851 / 0.213 | 写入全图 PSNR/SSIM/LPIPS；其余各行见下方完整对照 |
| 最优值样式 | 无数值、无标粗 | 组件表按列、输入表按各 T 分组标粗 Ours | PSNR/SSIM 越高越好，LPIPS 越低越好；没有跨 T 混比 |

### 结果分析的真实前后对照

**EN：组件分析**

**原文：**

```latex
These comparisons assess the contributions of generative completion and cross-component context to full-image and dynamic-region reconstruction.
```

**修改后：**

```latex
Ours achieves the best scores on all five metrics.
Compared with w/o GCM, it raises full-image and dynamic-region PSNR by 1.776 and 2.186 dB, respectively.
Relative to w/o CCM, the corresponding gains are 0.627 and 0.934 dB, while full-image LPIPS decreases from 0.147 to 0.129.
```

原因：原句只介绍对照目的，现用收到的五项指标及 PSNR/LPIPS 差值报告结果。

**EN：输入数量分析**

**原文：**

```latex
Full-image PSNR, SSIM, and LPIPS measure sensitivity to input sparsity under the same target-view evaluation protocol.
```

**修改后：**

```latex
Both variants improve across all three metrics as $T$ increases.
Ours outperforms w/o CCM at every input setting, with PSNR gains of 1.104, 0.738, and 0.627 dB at $T=2,4,8$, respectively.
The LPIPS reduction also increases as inputs become sparser, from 0.018 at $T=8$ to 0.041 at $T=2$.
```

原因：原句只介绍评价用途，现说明各档输入的趋势及相同 T 内的比较；差值由本次汇总值直接相减。

**ZH：组件分析**

**原文：**

```latex
这两项对照分别评价生成式补全和跨组件上下文对全图及动态区域重建的贡献。
```

**修改后：**

```latex
Ours 在全部五项指标上取得最优结果。
相比 w/o GCM，全图和动态区域 PSNR 分别提高 1.776 和 2.186 dB。
相比 w/o CCM，对应增益分别为 0.627 和 0.934 dB，全图 LPIPS 从 0.147 降至 0.129。
```

原因：原句只介绍对照目的，现用收到的五项指标及 PSNR/LPIPS 差值报告结果。

**ZH：输入数量分析**

**原文：**

```latex
全图 PSNR、SSIM 和 LPIPS 用于在相同目标视图评价协议下衡量输入稀疏度的影响。
```

**修改后：**

```latex
随着 $T$ 增大，两个版本的三项指标均得到改善。
Ours 在每档输入设置下均优于 w/o CCM，在 $T=2,4,8$ 时的 PSNR 增益分别为 1.104、0.738 和 0.627 dB。
LPIPS 降幅也随输入变稀疏而增大，从 $T=8$ 时的 0.018 增至 $T=2$ 时的 0.041。
```

原因：原句只介绍评价用途，现说明各档输入的趋势及相同 T 内的比较；差值由本次汇总值直接相减。

### 两张表完整前后对照（双语）

**EN `tab:ablation-components`**

**原文**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Component ablations.} All variants use $T=8$ (24 images), shared recovery and codec, and the same target views and dynamic-region masks. Full-image quality is evaluated with PSNR, SSIM, and LPIPS; dynamic-region quality with PSNR and SSIM.}
  \label{tab:ablation-components}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lccccc@{}}
    \toprule
    \multirow{2}{*}{Variant} & \multicolumn{3}{c}{Full image} & \multicolumn{2}{c}{Dynamic regions} \\
    \cmidrule(lr){2-4}\cmidrule(lr){5-6}
      & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ \\
    \midrule
    w/o GCM & & & & & \\
    w/o CCM & & & & & \\
    \midrule
    Ours & & & & & \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**修改后**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Component ablations.} All variants use $T=8$ (24 images), shared recovery and codec, and the same target views and dynamic-region masks. Full-image quality is evaluated with PSNR, SSIM, and LPIPS; dynamic-region quality with PSNR and SSIM.}
  \label{tab:ablation-components}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lccccc@{}}
    \toprule
    \multirow{2}{*}{Variant} & \multicolumn{3}{c}{Full image} & \multicolumn{2}{c}{Dynamic regions} \\
    \cmidrule(lr){2-4}\cmidrule(lr){5-6}
      & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ \\
    \midrule
    w/o GCM & 27.137 & 0.867 & 0.183 & 23.431 & 0.811 \\
    w/o CCM & 28.286 & 0.893 & 0.147 & 24.683 & 0.849 \\
    \midrule
    Ours & \textbf{28.913} & \textbf{0.911} & \textbf{0.129} & \textbf{25.617} & \textbf{0.873} \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**EN `tab:ablation-inputs`**

**原文**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Input-timestamp sensitivity.} At each $T$, we compare w/o CCM with the full model using fixed checkpoints, time span, and target views. All metrics are evaluated on full images. The $T=8$ setting is shared with Table~\ref{tab:ablation-components}.}
  \label{tab:ablation-inputs}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}clccc@{}}
    \toprule
    $T$ & Variant & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ \\
    \midrule
    \multirow{2}{*}{2} & w/o CCM & & & \\
      & Ours & & & \\
    \midrule
    \multirow{2}{*}{4} & w/o CCM & & & \\
      & Ours & & & \\
    \midrule
    \multirow{2}{*}{8} & w/o CCM & & & \\
      & Ours & & & \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**修改后**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{Input-timestamp sensitivity.} At each $T$, we compare w/o CCM with the full model using fixed checkpoints, time span, and target views. All metrics are evaluated on full images. The $T=8$ setting is shared with Table~\ref{tab:ablation-components}.}
  \label{tab:ablation-inputs}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}clccc@{}}
    \toprule
    $T$ & Variant & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ \\
    \midrule
    \multirow{2}{*}{2} & w/o CCM & 25.237 & 0.817 & 0.254 \\
      & Ours & \textbf{26.341} & \textbf{0.851} & \textbf{0.213} \\
    \midrule
    \multirow{2}{*}{4} & w/o CCM & 27.126 & 0.869 & 0.187 \\
      & Ours & \textbf{27.864} & \textbf{0.891} & \textbf{0.159} \\
    \midrule
    \multirow{2}{*}{8} & w/o CCM & 28.286 & 0.893 & 0.147 \\
      & Ours & \textbf{28.913} & \textbf{0.911} & \textbf{0.129} \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**ZH `tab:ablation-components`**

**原文**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{组件消融。}所有版本采用 $T=8$（24 张图像）、相同的恢复模块与编解码器，以及统一的目标视图和动态区域掩码。全图采用 PSNR、SSIM 和 LPIPS，动态区域采用 PSNR 和 SSIM。}
  \label{tab:ablation-components}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lccccc@{}}
    \toprule
    \multirow{2}{*}{变体} & \multicolumn{3}{c}{全图} & \multicolumn{2}{c}{动态区域} \\
    \cmidrule(lr){2-4}\cmidrule(lr){5-6}
      & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ \\
    \midrule
    w/o GCM & & & & & \\
    w/o CCM & & & & & \\
    \midrule
    Ours & & & & & \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**修改后**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{组件消融。}所有版本采用 $T=8$（24 张图像）、相同的恢复模块与编解码器，以及统一的目标视图和动态区域掩码。全图采用 PSNR、SSIM 和 LPIPS，动态区域采用 PSNR 和 SSIM。}
  \label{tab:ablation-components}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}lccccc@{}}
    \toprule
    \multirow{2}{*}{变体} & \multicolumn{3}{c}{全图} & \multicolumn{2}{c}{动态区域} \\
    \cmidrule(lr){2-4}\cmidrule(lr){5-6}
      & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ & PSNR $\uparrow$ & SSIM $\uparrow$ \\
    \midrule
    w/o GCM & 27.137 & 0.867 & 0.183 & 23.431 & 0.811 \\
    w/o CCM & 28.286 & 0.893 & 0.147 & 24.683 & 0.849 \\
    \midrule
    Ours & \textbf{28.913} & \textbf{0.911} & \textbf{0.129} & \textbf{25.617} & \textbf{0.873} \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**ZH `tab:ablation-inputs`**

**原文**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{输入时刻数量敏感性。}每档 $T$ 比较 w/o CCM 与完整模型，权重、时间跨度和目标视图固定。所有指标均在完整图像上计算。$T=8$ 的设置与表~\ref{tab:ablation-components} 相同。}
  \label{tab:ablation-inputs}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}clccc@{}}
    \toprule
    $T$ & 变体 & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ \\
    \midrule
    \multirow{2}{*}{2} & w/o CCM & & & \\
      & Ours & & & \\
    \midrule
    \multirow{2}{*}{4} & w/o CCM & & & \\
      & Ours & & & \\
    \midrule
    \multirow{2}{*}{8} & w/o CCM & & & \\
      & Ours & & & \\
    \bottomrule
  \end{tabular*}
\end{table}
```

**修改后**

```latex
\begin{table}[t]
  \centering
  \caption{\textbf{输入时刻数量敏感性。}每档 $T$ 比较 w/o CCM 与完整模型，权重、时间跨度和目标视图固定。所有指标均在完整图像上计算。$T=8$ 的设置与表~\ref{tab:ablation-components} 相同。}
  \label{tab:ablation-inputs}
  \small
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.12}
  \begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}clccc@{}}
    \toprule
    $T$ & 变体 & PSNR $\uparrow$ & SSIM $\uparrow$ & LPIPS $\downarrow$ \\
    \midrule
    \multirow{2}{*}{2} & w/o CCM & 25.237 & 0.817 & 0.254 \\
      & Ours & \textbf{26.341} & \textbf{0.851} & \textbf{0.213} \\
    \midrule
    \multirow{2}{*}{4} & w/o CCM & 27.126 & 0.869 & 0.187 \\
      & Ours & \textbf{27.864} & \textbf{0.891} & \textbf{0.159} \\
    \midrule
    \multirow{2}{*}{8} & w/o CCM & 28.286 & 0.893 & 0.147 \\
      & Ours & \textbf{28.913} & \textbf{0.911} & \textbf{0.129} \\
    \bottomrule
  \end{tabular*}
\end{table}
```

### 保留项、来源与检查范围

- 摘要、引言与贡献、方法、其他主实验、状态复用、讨论、结论、引用和补充材料保持本轮起点原文。两张表的既有协议与图注保持原样。
- 33 个结果值均直接来自用户本次表格，不换算旧自定义指标，不补造方差、显著性或运行记录。PSNR/LPIPS 差值是本轮新增算术计算。
- 仅结果标粗涉及排版，未改字体、行距、表格间距或页边距。
- 同步当前来源合同、证据状态和维护说明。稿件检查脚本按当前指标合同选择标准指标检查，避免填入数值后误走旧 MAE 的 RGB 尺度检查。
- 本轮未执行训练/评测，未提交或推送。

核验：54 项现有稿件检查通过；每种语言 33 个数值逐格匹配来源合同，T=8 跨表一致，14 个最优值按正确比较范围标粗。两个主稿均成功重新编译，最终日志无未定义引用、缺字或 Overfull。实际查看英文第 6–8 页、中文第 6–7 页，表格无重叠或裁切。英文 11 页，正文与结论止于第 8 页，References 从第 8 页开始；中文 9 页，正文止于第 7 页，References 从第 7 页开始。两张消融表分别位于英文第 7/8 页、中文第 6/7 页。所有其他 LaTeX 源文件及实验章节范围外的内容与本轮基线一致。[完整核验记录](../paper/provenance/ablation-standard-metrics-verification-20261029.json)。

## 2026-10-28：首页加入用户指定 teaser

基线提交：`e98697e09af130895fe14f70fbc840571da28a0d`。论文源码开始时与 HEAD 一致；上一轮未提交的 `docs/figures/teaser/` 是既有设计产物，本轮直接复用其 Waymo 风格图，不重新生成。修改前真实文本保存在 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/teaser-insertion/baseline.json`。

具体问题：当前首页没有任务/能力 teaser，原 Figure 1 实际是网络流程图。按用户要求，将选定图片放在标题下、摘要前；用户不强制跨栏，试排后因图内三段横向内容较多，采用正文宽度以保留可读性。原流程图完整保留为 Figure 2，实验图依次顺延为 Figure 3、4。

### 排版与图片

- 之前：`\maketitle` 后直接加载摘要，方法总览以 `figure*` 浮动放置。
- 之后：在标题块后追加独立图框及图注，随后仍按原方式加载双栏摘要；teaser 为 Figure 1，固定出现在首页。
- 沿用样式的标题、匿名作者区、正文列宽、字体、边距和行距；未修改 `cvpr.sty`。图框采用完整正文宽度，未用负间距。
- `paper/fig/drivecompose-teaser.png` 与用户刚确认的设计图片逐字节相同；原流程图和实验图不变。保留图内概念示意说明，图注也明确为概念图。

### 新增双语图注

- 英文位置：`paper/main.tex` 的标题区。
- 原文：无 teaser 图注。
- 修改后：`\caption{\textbf{DriveCompose concept.} DriveCompose jointly completes background, vehicle, and human content from driving images to form a compositional Gaussian scene. The same assets are reused under changes in camera viewpoint, vehicle pose, and human articulation. Gold marks completed regions.}`
- 原因：分别说明联合补全、同一资产的状态复用及金色标注的含义，与概念图对应。

- 中文位置：`paper/main_zh.tex` 的标题区。
- 原文：无 teaser 图注。
- 修改后：`\caption{\textbf{DriveCompose 概念示意。}从驾驶图像中联合补全背景、车辆与人体的内容，构建可组合高斯场景。同一组资产可在相机视角、车辆位姿和人体姿态变化时复用。金色标注表示补全区域。}`
- 原因：分别说明联合补全、同一资产的状态复用及金色标注的含义，与概念图对应。

### 正文引用的最小调整

- 位置：`paper/sec/1_introduction.tex`
- 原文：`As illustrated in Fig.~\ref{fig:teaser}`
- 修改后：`As illustrated in Fig.~\ref{fig:overview}`
- 原因：该句解释网络流程，继续指向原流程图（现 Figure 2），避免误指新增的任务概览图。正文其他字句不变。

- 位置：`paper/zh/1_introduction_zh.tex`
- 原文：`如图~\ref{fig:teaser} 所示`
- 修改后：`如图~\ref{fig:overview} 所示`
- 原因：该句解释网络流程，继续指向原流程图（现 Figure 2），避免误指新增的任务概览图。正文其他字句不变。

- 位置：`paper/sec/3_method.tex`
- 原文：`DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:teaser} shows the main reconstruction pipeline.`
- 修改后：`DriveCompose reconstructs a driving scene in the units that will later be controlled. Figure~\ref{fig:overview} shows the main reconstruction pipeline.`
- 原因：该句解释网络流程，继续指向原流程图（现 Figure 2），避免误指新增的任务概览图。正文其他字句不变。

- 位置：`paper/zh/3_method_zh.tex`
- 原文：`DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:teaser} 展示主要重建流程。`
- 修改后：`DriveCompose 按照后续控制的单位重建驾驶场景。图~\ref{fig:overview} 展示主要重建流程。`
- 原因：该句解释网络流程，继续指向原流程图（现 Figure 2），避免误指新增的任务概览图。正文其他字句不变。

### 明确保留项

标题、双语摘要、引言与贡献的所有论述、方法机制与公式、实验条件与数值、书目、补充材料均保留。本轮四个章节文件仅替换图引用标签；其他修改仅限双语入口、新图文件和设计/对照记录。

### 验证

两版最后一次编译均成功且实际写入新 PDF；日志无编译错误、未定义引用、缺字、overfull 或图注警告。Figure 1 均在首页标题下、摘要前；图框宽 495 pt、高 165 pt。原方法总览为第 2 页 Figure 2，双语流程引用同步。英文共 12 页（之前 11 页），正文结论与参考文献均在第 9 页；正文仍超过 8 页目标，本轮未压缩。中文共 9 页。已查看两版首页、英文流程图及正文末页，无重叠或裁切；最后修正图注锚点后，两版首页渲染与已检查版本逐字节一致。16 项受保护源码/图件哈希未变，四个正文文件只改引用标签。核验记录：`../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/teaser-insertion/check.json`。

[英文正式稿](../paper/build/en/main.pdf) · [中文正式稿](../paper/build/zh/main_zh.pdf)。排版与核验完成后，用户授权提交并推送本轮图件、双语源码、正式 PDF 和对应记录。

## 2026-10-28：摘要开头收紧并突出联合补全与资产复用

基线提交：`2f86dc78ec1da7210983446ab853b9947a0ce95a`。两份摘要源码在本轮开始时均与 HEAD 一致；本地既有的三个 pointforward PDF 删除状态不属于本轮改动。真实源码、正式 PDF 哈希与受保护文件清单保存在 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/baseline.json`。

范围：仅修改中英文摘要及本轮改动/编译记录，沿用现有段落结构。按用户给出的开头风格，将背景需求与局部观测痛点收进第一句，第二句即引入方法；并落实上一轮确认的联合补全、观测检查、消融数字和复用结尾调整。

英文词数：188 → 177（减少 11 词）。中文正文字符数（含英文、数字、空格和标点，不含 LaTeX 环境）：404 → 395。未调整字体、行距、边距或图件尺寸。

### 局部前后对照

#### 开头：背景、痛点与方法引入

English 修改前：

```text
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, vehicle, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences.
```

English 修改后：

```text
Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences.
```

中文 修改前：

```text
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、车辆或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。
```

中文 修改后：

```text
从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。
```

原因：将前三句收为两句：从局部观测重建完整、可控场景的需求直接引出 DriveCompose。删除开头重复展开的动作与未见表面说明；相机、车辆与人体的具体示例仍在引言首段，归属和运动关系仍由摘要的表示句说明。

#### 联合补全句

English 修改前：

```text
A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations.
```

English 修改后：

```text
A conditional flow-matching model jointly completes missing background and actor content in these representations, using cross-component memory to share scene context.
```

中文 修改前：

```text
通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。
```

中文 修改后：

```text
基于条件流匹配的生成模型在这些表示中联合补全背景与参与者的缺失内容，并通过跨组件记忆共享场景上下文。
```

原因：用背景与参与者的缺失内容替代摘要中未展开的潜码细节；保留条件流匹配、跨组件记忆、场景上下文与在上述表示中补全的关系。

#### 观测检查句

English 修改前：

```text
We also render the composed scene from the original camera viewpoints to check its consistency with the input images.
```

English 修改后：

```text
We render the completed scene at the recorded camera viewpoints and actor states to check its consistency with the input images.
```

中文 修改前：

```text
我们还从原始相机视角渲染组合后的场景，检查补全结果是否与输入图像一致。
```

中文 修改后：

```text
我们还在记录的相机视角和参与者状态下渲染补全后的场景，检查其与输入图像的一致性。
```

原因：补齐记录时的参与者状态，使检查条件与方法 3.5 一致；保持与输入图像比较的含义。

#### 组件消融结果句

English 修改前：

```text
Ablations show that sharing context across components improves completion of unseen surfaces.
```

English 修改后：

```text
Compared with the variant without cross-component memory, our model reduces mean absolute RGB error on unseen surfaces by 20.5% in component ablations.
```

中文 修改前：

```text
消融实验表明，组件间共享上下文能够改善未见表面的补全。
```

中文 修改后：

```text
组件消融实验表明，相比不使用跨组件记忆的变体，我们的方法将未观测表面的 RGB 平均绝对误差降低了 20.5%。
```

原因：将定性收益换成直接支撑跨组件记忆的量化结论。20.5% 为 T=8 组件消融中 New-MAE 从 0.078 降至 0.062 的相对降幅；对照为 w/o CCM，不能写成所有设置或所有基线的统一收益。

#### 结尾：资产复用

English 修改前：

```text
The completed components form a Gaussian scene that supports rendering under different camera and actor states.
```

English 修改后：

```text
The resulting Gaussian scene supports composition and rendering with the same completed assets under changes in camera viewpoint, vehicle pose, and human articulation.
```

中文 修改前：

```text
补全后的组件构成高斯场景，支持在不同相机和参与者状态下渲染。
```

中文 修改后：

```text
补全后的高斯场景可复用同一组资产，在不同相机视角、车辆位姿和人体姿态下组合与渲染。
```

原因：以同一组补全资产的组合与渲染收尾，明确相机视角、车辆位姿和人体姿态三类状态变化；比泛指不同状态渲染更准确地交代可组合重建的用途。

### 中英文摘要全文对照

English 修改前：

```text
Driving simulation and scene editing require reconstructed scenes that remain usable when cameras and actors move beyond their recorded configurations. Camera or actor motion exposes previously unseen surfaces, requiring their geometry and appearance to be completed and assigned to the corresponding background, vehicle, or human. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional generative model trained with flow matching uses cross-component memory to share scene context and jointly complete the missing codes in these representations. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We also render the composed scene from the original camera viewpoints to check its consistency with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Ablations show that sharing context across components improves completion of unseen surfaces. The completed components form a Gaussian scene that supports rendering under different camera and actor states.
```

English 修改后：

```text
Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional flow-matching model jointly completes missing background and actor content in these representations, using cross-component memory to share scene context. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We render the completed scene at the recorded camera viewpoints and actor states to check its consistency with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Compared with the variant without cross-component memory, our model reduces mean absolute RGB error on unseen surfaces by 20.5% in component ablations. The resulting Gaussian scene supports composition and rendering with the same completed assets under changes in camera viewpoint, vehicle pose, and human articulation.
```

中文 修改前：

```text
驾驶仿真与场景编辑需要重建场景在相机和参与者偏离记录状态后仍可使用。相机移动或参与者运动会暴露此前未被拍摄的表面，因此需要补全这些表面的几何与外观，并使补全内容保持归属于相应的背景、车辆或人体。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。通过流匹配训练的条件生成模型利用跨组件记忆共享场景上下文，联合补全这些表示中的缺失潜码。补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还从原始相机视角渲染组合后的场景，检查补全结果是否与输入图像一致。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。消融实验表明，组件间共享上下文能够改善未见表面的补全。补全后的组件构成高斯场景，支持在不同相机和参与者状态下渲染。
```

中文 修改后：

```text
从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。基于条件流匹配的生成模型在这些表示中联合补全背景与参与者的缺失内容，并通过跨组件记忆共享场景上下文。补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还在记录的相机视角和参与者状态下渲染补全后的场景，检查其与输入图像的一致性。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。组件消融实验表明，相比不使用跨组件记忆的变体，我们的方法将未观测表面的 RGB 平均绝对误差降低了 20.5%。补全后的高斯场景可复用同一组资产，在不同相机视角、车辆位姿和人体姿态下组合与渲染。
```

### 主张依据与保留项

- 第一背景句概括引言首段的应用需求与局部可见性问题；条件流匹配和联合补全对应方法 3.1/3.4，运动与姿态关系对应 3.1/3.5。
- 观测检查使用原始相机及参与者状态，对应方法 3.5；结尾描述同一资产的状态复用机制。
- 消融数字来自 `paper/sec/4_experiments.tex` 的组件表及 `paper/provenance/ablation-results-20261023.json`：T=8，三路相机、24 张输入图像，New-MAE 0.078 → 0.062，相对降幅四舍五入为 20.5%。未增加统计显著性或闭环效果结论。
- 标题、规范表示句、观测保持句、Waymo 重建与视图合成结论保留；引言、贡献、方法、实验设置与数值、正文图件和补充材料不改。

### 编译与篇幅核验

两版主稿均成功编译并实际写入新 PDF，日志无编译错误、未定义引用、缺字或 overfull 警告。英文仍为 12 页，正文结论及参考文献起始均在第 9 页；中文仍为 9 页，结论在第 6 页、参考文献从第 7 页开始。英文摘要 188 → 177 词，中文 404 → 395 字符；本轮未增加页数，原有英文正文越过第 8 页的状态不变。已目视检查两版首页及正文结论页，无重叠、裁切或缺字，新增 20.5% 正常显示。132 项受保护文件的哈希或既有缺失状态与本轮基线一致，用户已有的三个 PDF 删除状态保留。详细核验见 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/check.json`。本轮未提交或推送。


## 2026-10-28：仅微调双语摘要首句（nature-polishing 检查后）

范围：仅英文与中文摘要第一句。基线提交为 `2f86dc78ec1da7210983446ab853b9947a0ce95a`，本轮真实基线为该提交之上的未提交工作区，已保存在 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/first-sentence-baseline.json`；先前摘要改动不计入本轮。

具体问题：原首句说明完整、可控场景的重要性，但没有直接说明状态变化为何同时要求未见表面补全与参与者运动一致性。将泛化的重要性陈述替换为具体任务需求，不调整摘要顺序。

### 英文摘要首句

原文：

> Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing.

修改后：

> Driving simulation and scene editing require completing unseen surfaces exposed by camera or actor motion, while ensuring that completed actor surfaces follow vehicle motion and human articulation.

### 中文摘要首句

原文：

> 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。

修改后：

> 驾驶仿真与场景编辑需要补全相机或参与者运动时暴露的未观测表面，并使补全的参与者表面随车辆运动或人体姿态变化。

原因：首句直接说明相机或参与者运动会暴露未观测表面，并要求补全的参与者表面随车辆运动或人体姿态变化；第三句继续解释规范表示如何满足这一需求。依据为当前引言第一段及方法 3.1/3.5，未增加新的实测能力主张。

保留项：两个摘要从第二句至结尾逐字保持；标题、引言、方法、实验设置与数值、20.5% 消融结论、图表及补充材料均不修改。英文摘要由 177 词变为 186 词，仍为 9 句。无排版参数改动。

编译与版面核验：双语候选稿均成功编译，日志无未定义引用、缺字或 overfull 警告；两版首页与结论页目视检查无重叠、裁切或缺字。英文总页数保持 12 页、正文及结论仍结束于第 9 页；中文保持 9 页、结论在第 6 页。原有英文正文超出 8 页的状态不变。英文正式 PDF 已替换并校验哈希。中文正式 PDF 已替换并校验哈希。 两个摘要除首句外逐字不变，受保护文件与本轮基线一致。检查记录见 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/first-sentence-check.json`。本轮未提交或推送。


## 2026-10-28：撤回摘要首句试改，恢复上一版

用户认为原首句更清晰，本轮仅撤回上一轮首句替换，中英文摘要恢复至 `first-sentence-baseline.json` 中保存的实际工作区基线；不使用更早 HEAD 覆盖先前摘要修改。基线提交仍为 `2f86dc78ec1da7210983446ab853b9947a0ce95a`；撤回前的实际文本另存于 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/first-sentence-revert-baseline.json`。

英文，撤回前：

> Driving simulation and scene editing require completing unseen surfaces exposed by camera or actor motion, while ensuring that completed actor surfaces follow vehicle motion and human articulation.

恢复后：

> Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing.

中文，撤回前：

> 驾驶仿真与场景编辑需要补全相机或参与者运动时暴露的未观测表面，并使补全的参与者表面随车辆运动或人体姿态变化。

恢复后：

> 从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。

原因：原句先概括局部观测到完整、可控三维场景的任务，阅读负担更低；试改首句提前堆叠运动细节，并与第三句的车辆运动和人体姿态说明重复，未获得明确改善，因此撤回。其余摘要内容逐字不变，英文恢复为 177 词。

撤回编译核验：双语重新编译成功，日志无未定义引用、缺字或 overfull 警告；两版首页已目视检查。英文 12 页、中文 9 页，与撤回前相同；英文正文原有第 9 页结束状态不变。两版正式 PDF 均已更新并核验哈希。 双语摘要与上一轮试改前的实际工作区基线逐字一致，其他受保护文件未变；本轮未提交或推送。

## 2026-10-29：合并摘要观测一致性表述并准备发布

基线 HEAD：`2f86dc78ec1da7210983446ab853b9947a0ce95a`；实际起点是此前已确认但尚未提交的 177 词摘要工作区，不能以 HEAD 中的旧摘要冒充本轮修改前文本。真实双语原文、PDF 哈希与受保护文件状态保存于 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/consistency-baseline.json`。

用户确认将观测保持与渲染检查合并为一句，按此前展示的完整中英文摘要落地，编译检查后提交并推送。具体问题是分开叙述容易被读成重复的一致性要求，而中途提出遮挡又增加歧义；本轮以共同目的串联补全时保留表面、补全后在记录状态下渲染并比较两个步骤。

本轮英文摘要 177 → 173 词，9 → 8 句；中文正文字符数（含空格、英文、数字及标点，不含 LaTeX 环境）395 → 394。

### 局部前后对照

English 修改前：

```text
Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We render the completed scene at the recorded camera viewpoints and actor states to check its consistency with the input images.
```

English 修改后：

```text
To maintain consistency with input observations, we preserve observed surface geometry and appearance during completion, then render the completed scene at recorded camera viewpoints and actor states for comparison with the input images.
```

中文 修改前：

```text
补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还在记录的相机视角和参与者状态下渲染补全后的场景，检查其与输入图像的一致性。
```

中文 修改后：

```text
为保持与输入观测的一致性，我们在补全时保留已观测表面的几何与外观，并在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较。
```

原因：将共同目的放在句首，明确先在补全中保留已有几何与外观，再在记录的相机视角与参与者状态下渲染核对输入图像；两个步骤的对象与次序清楚。表述对应方法 3.4 的观测约束及 3.5 的原始状态渲染检查，未新增方法、指标或实验结论。

### 完整摘要前后对照

English 修改前：

```text
Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional flow-matching model jointly completes missing background and actor content in these representations, using cross-component memory to share scene context. Completion is constrained by the input observations to preserve the geometry and appearance of observed surfaces. We render the completed scene at the recorded camera viewpoints and actor states to check its consistency with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Compared with the variant without cross-component memory, our model reduces mean absolute RGB error on unseen surfaces by 20.5% in component ablations. The resulting Gaussian scene supports composition and rendering with the same completed assets under changes in camera viewpoint, vehicle pose, and human articulation.
```

English 修改后：

```text
Reconstructing complete and controllable 3D scenes from partial observations is essential for autonomous driving simulation and scene editing. We present DriveCompose, a framework for generative reconstruction of compositional driving scenes from image sequences. We represent the background in world coordinates and vehicles and humans in their respective canonical frames, allowing completed surfaces to follow vehicle motion and human articulation. A conditional flow-matching model jointly completes missing background and actor content in these representations, using cross-component memory to share scene context. To maintain consistency with input observations, we preserve observed surface geometry and appearance during completion, then render the completed scene at recorded camera viewpoints and actor states for comparison with the input images. On Waymo, DriveCompose improves dynamic scene reconstruction and off-trajectory view synthesis over the evaluated baselines. Compared with the variant without cross-component memory, our model reduces mean absolute RGB error on unseen surfaces by 20.5% in component ablations. The resulting Gaussian scene supports composition and rendering with the same completed assets under changes in camera viewpoint, vehicle pose, and human articulation.
```

中文 修改前：

```text
从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。基于条件流匹配的生成模型在这些表示中联合补全背景与参与者的缺失内容，并通过跨组件记忆共享场景上下文。补全过程受输入观测约束，以保持已观测表面的几何与外观。我们还在记录的相机视角和参与者状态下渲染补全后的场景，检查其与输入图像的一致性。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。组件消融实验表明，相比不使用跨组件记忆的变体，我们的方法将未观测表面的 RGB 平均绝对误差降低了 20.5%。补全后的高斯场景可复用同一组资产，在不同相机视角、车辆位姿和人体姿态下组合与渲染。
```

中文 修改后：

```text
从局部观测中重建完整、可控的三维场景，是自动驾驶仿真与场景编辑的重要基础。我们提出 DriveCompose，从图像序列中生成式地重建可组合驾驶场景。我们在世界坐标系中表示背景，在车辆和人体各自的规范坐标系中表示其内容，使补全表面能够随所属车辆运动或人体姿态变化。基于条件流匹配的生成模型在这些表示中联合补全背景与参与者的缺失内容，并通过跨组件记忆共享场景上下文。为保持与输入观测的一致性，我们在补全时保留已观测表面的几何与外观，并在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较。在 Waymo 上，DriveCompose 的动态场景重建和轨迹外视图合成效果优于所评估的基线。组件消融实验表明，相比不使用跨组件记忆的变体，我们的方法将未观测表面的 RGB 平均绝对误差降低了 20.5%。补全后的高斯场景可复用同一组资产，在不同相机视角、车辆位姿和人体姿态下组合与渲染。
```

### 范围与核验

本轮源码只替换两版摘要的上述观测一致性表述，其他句子与本轮实际基线逐字一致。发布包含此前已确认的摘要优化、双语正式 PDF 和可追溯记录；本地既有的三个 pointforward PDF 删除状态不纳入本次提交。

两版主稿均重新编译成功并实际写入正式 PDF。日志无编译错误、未定义引用、缺字或 overfull 警告。两版首页及结论页已目视检查，无重叠或裁切，确认新版观测一致性表述及 20.5% 正常显示。英文仍为 12 页，正文结论与参考文献均在第 9 页；中文仍为 9 页，结论在第 6 页、参考文献从第 7 页开始。英文摘要缩为 173 词，未增加页数；原有英文正文超过 8 页的状态不变。132 项受保护文件及既有缺失状态未变，已有改动记录前缀完整保留。详细核验保存于 `../_archive/drivecompose/20261029-pre-push-cleanup/files/paper/build/abstract-revision/consistency-check.json`。按本轮用户授权提交并推送。


## 2026-10-29：从领域读者视角局部微调引言

基线提交：`0381af6362fc941420fa23d467dc99d68dc7d0c8`。本轮两版引言与 HEAD 一致，已有工作区的 pointforward 图件删除与摘要预览文件不属于本轮修改。范围仅为两版引言的四处问题、对应记录与重新编译的主稿输出；标题、摘要、其他章节、书目、数值与图表位置保持原样。未提交或推送。

沿用已有应用需求、观测缺失、生成与控制、表示与联合补全、观测检查、实验及贡献的叙事顺序。未发现需要整段重写或重新分类文献的依据。采用 nature-polishing 的 algorithmic / intro / en / generic 路由，并进行非防御性写作和 humanizer 局部复读。

英文按同一计数规则由 633 词变为 624 词（去除章节标题和 LaTeX 引用命令，保留正文及贡献、组织说明）。

### 第二段末句：先明确推断需求，再引出生成式方法

英文原文：

```latex
When a new viewpoint or actor motion reveals surfaces unseen throughout the sequence, reconstruction must infer their geometry and appearance from generative priors.
```

英文修改后：

```latex
When a new viewpoint or actor motion reveals surfaces unseen throughout the sequence, reconstruction must infer their geometry and appearance.
```

中文原文：

```latex
当新视角或对象运动暴露出整个序列都未曾拍摄的表面时，重建需要借助生成先验推断其几何与外观。
```

中文修改后：

```latex
当新视角或对象运动暴露出整个序列都未曾拍摄的表面时，重建需要推断其几何与外观。
```

原因：原句把未观测表面需要推断，进一步限定为必须来自生成先验。删除这一限定，下一段仍完整介绍生成式路线及引用；不新增对已有方法的能力判断。

### 第三段末尾：说明跨组件信息为何参与补全

英文原文：

```latex
Applying generative completion to such scenes requires generated surfaces to move with their actors, while allowing each actor's completion to use information from the surrounding scene.
```

英文修改后：

```latex
Applying generative completion to such scenes requires generated surfaces to move with their actors. When an actor is only partially observed, information from the background and other actors can provide additional context for inferring its missing content.
```

中文原文：

```latex
将生成补全用于这类场景，需要使补出的表面随所属对象运动，同时让每个对象能够利用周围场景的信息完成补全。
```

中文修改后：

```latex
将生成补全用于这类场景，需要使补出的表面随所属对象运动。当对象仅被部分观测时，背景与其他对象的信息可为推断其缺失内容提供补充上下文。
```

原因：保留补出表面随对象运动的控制要求，将信息共享的条件具体写为对象仅被部分观测，并明确上下文来自背景与其他对象。设计依据是方法 3.2 的观测聚合与 3.4 的跨组件特征交换；实验 4.4 的 CCM 消融和输入稀疏性结果支持其补全价值。没有声称所有前人方法均不使用上下文，也没有将场景上下文写成保证恢复真实隐藏表面的充分条件。

### 第四段首句：中文明确独立控制的对象

英文对应句已明确控制对象，原样保留。

中文原文：

```latex
为此，我们提出 DriveCompose，从驾驶图像序列中构建可独立控制、并经过生成补全的三维场景。
```

中文修改后：

```latex
为此，我们提出 DriveCompose，从驾驶图像序列中构建经过生成补全、并支持参与者独立控制的三维场景。
```

原因：原句“可独立控制”修饰整个场景，独立于什么不清楚。改为参与者独立控制，与英文 independently controllable actors 对齐；英文此句不改。

### 第三项贡献：删除重复实验结果

英文原文：

```latex
\item We evaluate the framework and its key mechanisms through dynamic reconstruction, off-trajectory view synthesis, and component ablations. Experiments show that DriveCompose outperforms the evaluated baselines on reconstruction and view synthesis; cross-component information sharing reduces unseen-surface completion error, with larger absolute reductions under sparse observations.
```

英文修改后：

```latex
\item We evaluate the framework through dynamic reconstruction and off-trajectory view synthesis, and use component ablations to quantify the reduction in unseen-surface completion error from cross-component information sharing.
```

中文原文：

```latex
\item 通过动态重建、轨迹外视图合成与组件消融评估框架及其关键机制。实验表明，DriveCompose 在动态场景重建和轨迹外视图合成中优于所评估的基线；跨组件信息共享降低了未观测表面的补全误差，并在观测稀疏时带来更大的绝对误差降幅。
```

中文修改后：

```latex
\item 通过动态重建与轨迹外视图合成评估框架，并通过组件消融量化跨组件信息共享带来的未观测表面补全误差降幅。
```

原因：保留动态重建和视图外推的评估范围，并明确消融量化跨组件信息共享带来的补全误差降幅；删除紧邻第七段已完整说明的基线比较与稀疏条件复述。结果、比较范围和观测稀疏条件均仍在引言第七段及实验正文，不是迁入补充材料，也没有删除不利结果。

### 保留项与证据边界

第一段的问题条件与操作后果、第四段的坐标表示与运动绑定、第五段的局部结构和跨组件信息交换、第六段的观测检查、第七段的实验结论、前两项贡献及论文组织均保留。第一项贡献的闭环驾驶仿真沿用应用定位，现有实验结论仍限定在重建、视图外推和组件消融。未将方法接口当作闭环性能实测。

本轮未新增文献或实验主张；依据当前方法、实验表格及作者确认的 `paper/provenance/ablation-results-20261023.json`，未独立核验原始训练日志。

### 编译与核验

双语主稿重新编译成功，正式 PDF 均由本轮实际写入。日志无编译错误、未定义引用、缺字或 overfull 警告；英文第 1–3 页、中文第 1–2 页和两版结论页已目视核对，无新增重叠或裁切。PDF 中已核对第三段新增解释和第三项贡献的新表述。

英文仍为 12 页，正文结论和参考文献均在第 9 页；中文仍为 9 页，结论在第 6 页。原有英文正文超过 8 页、图 2 占据第 2 页顶部并使贡献列表跨页的排版状态不变，本轮未调整图表声明位置或版式参数。

引言引用键及顺序完全保留，正文按同一规则由 633 词变为 624 词。逐文件哈希核对确认：本轮范围以外的已跟踪文件及既有缺失状态未变，标题、摘要、方法、实验和书目保持原样。源稿差异已打开供审阅。未执行 Git 提交或推送。


## 2026-10-29：引言与摘要表述对齐并发布

基线 HEAD：`0381af6362fc941420fa23d467dc99d68dc7d0c8`；实际起点是上一轮尚未提交的 624 词引言工作区。以下原文直接取自修改前工作区，不能用 HEAD 中更早的引言替代。发布包括上一轮局部微调和本轮摘要对齐。

本轮范围：中英文引言的框架定位、条件流匹配、观测一致性以及 New-MAE 指标表述。标题、双语摘要、方法、实验数值、图表、limitations 和 conclusion 保持原样。当前打开的中文引言文件原位更新，使用内置编译器检查，保持当前编辑器。

### 框架定位

英文原文：

```latex
To this end, we introduce DriveCompose, which reconstructs driving image sequences into a generatively completed 3D scene with independently controllable actors.
```

英文修改后：

```latex
To this end, we introduce DriveCompose, a framework that generatively reconstructs compositional driving scenes from image sequences while supporting independent actor control.
```

中文原文：

```latex
为此，我们提出 DriveCompose，从驾驶图像序列中构建经过生成补全、并支持参与者独立控制的三维场景。
```

中文修改后：

```latex
为此，我们提出 DriveCompose，从驾驶图像序列中生成式地重建可组合场景，并支持参与者的独立控制。
```

原因：将 generatively completed 3D scene 改为直接描述可组合驾驶场景的生成式重建，与摘要的框架定位一致；保留参与者独立控制。

### 条件流匹配

英文原文：

```latex
The model learns to generate missing latent codes through flow matching~\cite{lipman2022flowmatching}, and component-specific decoders convert the completed representations into a Gaussian scene~\cite{kerbl2023gaussians}.
```

英文修改后：

```latex
The model learns to generate missing latent codes through conditional flow matching~\cite{lipman2022flowmatching}, and component-specific decoders convert the completed representations into a Gaussian scene~\cite{kerbl2023gaussians}.
```

中文原文：

```latex
模型通过流匹配学习生成缺失潜码~\cite{lipman2022flowmatching}，再由各组件的解码器将补全后的表示转化为高斯场景~\cite{kerbl2023gaussians}。
```

中文修改后：

```latex
模型通过条件流匹配学习生成缺失潜码~\cite{lipman2022flowmatching}，再由各组件的解码器将补全后的表示转化为高斯场景~\cite{kerbl2023gaussians}。
```

原因：flow matching 统一为 conditional flow matching，与摘要、方法和第二项贡献一致，引用键不变。

### 观测一致性

英文原文：

```latex
During completion, we retain surfaces established by reliable observations and generate the missing geometry and appearance. Newly generated surfaces may occlude previously visible regions, so we render the completed scene at the recorded camera viewpoints and actor states and compare it with the input images to check for inconsistencies introduced by completion.
```

英文修改后：

```latex
To maintain consistency with input observations, we preserve the geometry and appearance of reliably observed surfaces during completion. We then render the completed scene at the recorded camera viewpoints and actor states and compare it with the input images to check for inconsistencies introduced by completion.
```

中文原文：

```latex
补全时，我们保留由可靠观测确定的表面，并生成缺失部分的几何与外观。新增表面可能遮挡原本可见的区域，因此我们在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较，检查补全是否引入观测不一致。
```

中文修改后：

```latex
为保持与输入观测的一致性，我们在补全时保留由可靠观测确定的表面几何与外观。随后，我们在记录的相机视角和参与者状态下渲染补全后的场景，与输入图像比较，检查补全是否引入观测不一致。
```

原因：沿用摘要的共同目的与先后步骤：补全时保留可靠观测确定的几何与外观，随后在记录的相机视角和参与者状态下渲染比较。删除引言中易使读者误解为任意遮挡都属于错误的遮挡引子；该技术原因仍完整保留在方法 3.5，没有迁移或删除方法内容。可靠观测条件和通过检查后复用均保留。

### 结果概述的误差定义

英文原文：

```latex
Component ablations further show that cross-component information sharing reduces unseen-surface completion error, with larger absolute error reductions under sparser observations (Sec.~\ref{sec:ablations}).
```

英文修改后：

```latex
Component ablations further show that cross-component information sharing reduces mean absolute RGB error on unseen surfaces, with larger absolute error reductions under sparser observations (Sec.~\ref{sec:ablations}).
```

中文原文：

```latex
组件消融进一步表明，跨组件信息共享能够降低未观测表面的补全误差，且在输入观测较少时带来更大的绝对误差降幅（第~\ref{sec:ablations} 节）。
```

中文修改后：

```latex
组件消融进一步表明，跨组件信息共享能够降低未观测表面的 RGB 平均绝对误差，且在输入观测较少时带来更大的绝对误差降幅（第~\ref{sec:ablations} 节）。
```

原因：将泛称的补全误差限定为摘要及 New-MAE 指标实际衡量的未观测表面 RGB 平均绝对误差，避免被理解为几何误差；稀疏观测下绝对降幅较大这一条件保留，未新增数值。

### 第三项贡献的指标对应

英文原文：

```latex
\item We evaluate the framework through dynamic reconstruction and off-trajectory view synthesis, and use component ablations to quantify the reduction in unseen-surface completion error from cross-component information sharing.
```

英文修改后：

```latex
\item We evaluate the framework through dynamic reconstruction and off-trajectory view synthesis, and use component ablations to quantify the reduction in mean absolute RGB error on unseen surfaces from cross-component information sharing.
```

中文原文：

```latex
\item 通过动态重建与轨迹外视图合成评估框架，并通过组件消融量化跨组件信息共享带来的未观测表面补全误差降幅。
```

中文修改后：

```latex
\item 通过动态重建与轨迹外视图合成评估框架，并通过组件消融量化跨组件信息共享带来的未观测表面 RGB 平均绝对误差降幅。
```

原因：依照同一 New-MAE 定义同步贡献，保留消融量化跨组件信息共享作用的结论。

### 检查与发布范围

当前打开的 `paper/zh/1_introduction_zh.tex` 已原位保存，并由内置 `compile_latex_document` 以 `paper/main_zh.tex` 为入口成功编译。中英文引言的引用键与原有顺序一致，摘要、方法、实验、limitations 和 conclusion 的文件哈希与本轮实际基线一致。

依照当前编辑器要求，本轮没有另行生成或导出独立 PDF，也未切换编辑器标签。发布仅包含两版引言源码及本对照记录；上一轮工作区中的独立 PDF 和编译记录修改、既有 pointforward 图件删除、临时预览文件均不纳入本次提交。limitations 和 conclusion 本轮仅审读，意见在会话中交付。

## 2026-11-02：P3 新视角概念素材的几何设计

范围：回答“这样的话 P3 怎么绘制”，将已有 P2 空间约定具体化为独立 P3 几何预览。当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`；本轮开始时工作区已有未提交修改。对照记录的真实基线已保存到 `paper/build/teaser-p3-design/before/paper-revision-changes.md`，SHA256 为 `1a75fc51a4d08c55e4321c2011f4349f5699170cc47526d80378746b38d54045`，不以 HEAD 代替工作区基线。

| 位置 | 真实基线或原有设定 | 本轮具体化 | 原因 |
| --- | --- | --- | --- |
| P3 占位 | `New camera view s1` / `Unobserved surfaces exposed`（新相机视图 s1 / 未观测表面暴露） | 独立几何预览把车辆 +Y 远侧画成未知范围；PPT 占位文字未改 | P2 已显示车尾和地面缺口，P3 需要突出此前隐藏的另一侧缺失 |
| P2/P3 对应 | 场景约定要求 `no object translation or rotation between P2/P3`（对象不平移或旋转） | 从同一个世界定义分别投影，固定车辆、人物关节、立面及 Uv/Ug；只改变相机 | 避免只旋转车辆或单独挪动行人造成空间矛盾 |
| 背景立面 | `one observed facade plane`（单片已观测立面） | P3 从背向观察时仅显示浅色位置轮廓 | 避免虚构完整建筑背面，并减少前景立面对车辆缺失区域的遮挡 |
| P3 与 P6a | `reuse the P3 camera and the completed P4 scene`（复用 P3 相机与 P4 补全场景） | 设计说明要求 P6a 在同视角、同状态显示对应补全区域 | 将真正的方法对比落在上下配对，而不是把 P2/P3 当成方法优劣对比 |

新增 [P3 设计说明](figures/teaser/p3-design.md)、[P2/P3 对照预览](../paper/build/teaser-p3-design/p2-p3-design-comparison.png)、[P3 无字几何预览](../paper/build/teaser-p3-design/p3-geometry-preview.png) 及投影脚本。英文图注候选 `A new camera view exposes missing surfaces in the aggregated reconstruction.` 对应“新相机视角暴露了聚合重建中的缺失表面”；仅记录候选，没有修改论文图注。

检查：已运行几何构建并目检对照图；同一场景采用相同正交比例和世界空间取景中心，远侧由隐藏变为可见，P3 没有复制近侧车窗或加入补全内容。P2 成品、场景约定 JSON 和当前 PPT 的 SHA256 与本轮开始时一致。本轮未调用 ImageGen，输出为设计预览；未修改 LaTeX、正式 PDF 或 PPT。

## 2026-11-02：按用户要求交付独立无文字 P3 素材

原问题 → 修改后 → 原因：上一轮提供的是带说明的 P2/P3 构图对照，未交付用户需要的独立 P3 生图素材；本轮用内置 ImageGen 独立生成 [p3-standalone.png](figures/teaser/p3-standalone.png)，只包含无文字场景，满足直接放入 teaser 的素材需求。场景依照 P3 几何底图，配色与笔触参照既有 P2；由新视角显示车辆另一侧未知区域，车顶保留已观测灰蓝色，未复制车窗或加入补全色。

当前 HEAD 仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`；记录的工作区真实基线保存至 `paper/build/teaser-p3-standalone/before/`，日志基线 SHA256 为 `c2ec8090466c3bbf987037eaf0fa9b2dba7839430438c2bd2a4077ed84a3c010`。独立 PNG 为 1922×818、RGB，已目检无标题、标签、文字、箭头、图框或水印。新增[提示词](figures/teaser/p3-standalone-prompt.txt)与[生成记录](figures/teaser/p3-standalone-generation-record.json)，同步设计说明中的生成状态。既有 P2、PPT、论文源码和正式 PDF 未修改。

## 2026-11-03：独立无文字 P4 补全场景素材

按用户“接下来试着生成 P4 的素材”的要求，用内置 ImageGen 以既有 P2 为编辑目标，生成 [p4-standalone.png](figures/teaser/p4-standalone.png)。沿用 P2 的观察相机、场景位置与配色，仅把固定未知范围具体化为补全表面；不采用 P3 的另一侧视角。

| 位置 | P2 实际基线 | P4 素材 | 原因 |
| --- | --- | --- | --- |
| 车尾 Uv / vehicle rear | 白底、灰色斜线和虚线边界 | 原四边形内填入浅金色，使用实线边界 | 表示已补全的车辆表面 |
| 地面 Ug / background road patch | 车尾左下方的白底斜线缺失范围 | 同一位置填入浅金色，与路面齐平 | 同时展示背景与车辆的补全 |
| 已观测内容 / observed content | 灰蓝车身及车顶、车窗和轮胎、紫色人物、灰色立面、浅青路面 | 视觉上保留原相机、布局、姿态及颜色 | 使上下路径可以追踪相同场景与表面，避免为 P4 新增人体缺口或移动对象 |

本轮 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，工作区已有未提交修改。真实记录基线保存于 `paper/build/teaser-p4-standalone/before/paper-revision-changes.md`，SHA256 为 `53e421f216193b3d0929fddd6ffbdef49c76923b3c2503a091529b47aa3b1013`。新增[提示词](figures/teaser/p4-standalone-prompt.txt)和[生成记录](figures/teaser/p4-standalone-generation-record.json)。

检查：PNG 为 1920×819、RGB；已目检无文字、箭头、标签、图框或水印，两个原缺失区域均已填入金色，未添加新对象或人体补全标记。P2、空间约定 JSON 与当前 PPT 的哈希均与既有记录一致；未修改论文源码、正式 PDF 或 PPT。该素材保持概念示意身份，组件和共享场景上下文的原生标注由已有 PPT 布局承载。

## 2026-11-03：P4 补入共享场景上下文的交互含义

用户指出 P4 必须结合其实际含义。具体问题：上一版只有金色补全表面，没有在素材内表达背景、车辆、人体通过共同上下文交换信息，容易被理解为分别完成后的简单装配。本轮以既有 P4 为编辑目标，使用内置 ImageGen 生成独立无文字候选 [p4-joint-context.png](figures/teaser/p4-joint-context.png)，保留上一版供比较。

| 位置 | 上一版实际状态 | 本轮修改 | 原因 |
| --- | --- | --- | --- |
| Shared scene context / 共享场景上下文 | 图像内无共同上下文载体 | 场景下方增加一个包含青、蓝、紫混合色块的共同上下文条 | 明确三类组件共用同一上下文，避免看成三个互不关联的流程 |
| Background / 背景 | 仅见灰色立面和金色地面补全部位 | 青色双向连接在背景锚点与上下文条之间交互 | 将背景本身纳入联合机制 |
| Vehicle、Human / 车辆与人体 | 两个对象之间无信息交互示意 | 蓝色与紫色双向连接分别接到同一上下文条 | 表达共同上下文的读取与返回；不为人体临时制造缺口 |
| 原补全部位 | 车尾与地面均为金色 | 两处标记保留；场景整体缩放，为下方上下文条留白 | 同时保留补全结果和联合机制的因果解释，保持场景对应 |

技术依据为当前 `paper/sec/3_method.tex` 的 CCM 读写机制（第 93–103 行）及 `docs/algorithm.md` 的局部组与全局记忆交互说明（第 31–33 行）。混合色块仅为共享表示的概念标记，不表示特定记忆维数或实测特征。

本轮 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续；记录基线位于 `paper/build/teaser-p4-joint-context/before/paper-revision-changes.md`，SHA256 为 `d05598c4d87e5b1fd1ab447322fffc0f8df351a0f5cbc8d5ac4c00724dfe848c`。保存[提示词](figures/teaser/p4-joint-context-prompt.txt)、[生成记录](figures/teaser/p4-joint-context-generation-record.json)及用户提供的语义布局参考。PNG 为 1922×818、RGB，已目检无文字，三条双向连接均指向同一个上下文条，金色区域与既有位置对应。既有 P2/P3/P4 素材、PPT、论文源码和正式 PDF 均未修改。

## 2026-11-03：P4 图内补充必要文字标签

用户明确要求这块图内加入文字。原问题：无文字版本的三类对象及底部色块条主要依赖颜色识别，共享上下文的含义仍需外部说明。本轮用内置 ImageGen 在已有图上局部补充四个标签，生成 [p4-joint-context-labeled.png](figures/teaser/p4-joint-context-labeled.png)，保留无文字版本。

| 位置 | 原图 | 修改后 | 原因 |
| --- | --- | --- | --- |
| 背景锚点 | 青色圆点，无文字 | `Background`（背景）青色标签 | 明确背景也参与共享上下文交互 |
| 车辆与人体锚点 | 蓝色、紫色圆点，无文字 | `Vehicle`（车辆）、`Human`（人体）对应色标签 | 将对象归属与两条交互连接对应 |
| 共享条 | 仅有混合色块 | 框内色块上方标 `Shared scene context`（共享场景上下文） | 说明三类组件连接的是同一共享表示 |
| 容器与连接 | 上下文框高度只容纳色块 | 框向上扩展，蓝色箭头末端随边界调整 | 避免文字与箭头重叠；三条双向交互和金色补全区域保留 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。真实工作区日志基线位于 `paper/build/teaser-p4-labeled/before/paper-revision-changes.md`，SHA256 为 `d961d733fbe53283b8871c503624f1d8f6419135e3368a6c13cdafb19f69e04f`。新增[提示词](figures/teaser/p4-joint-context-labeled-prompt.txt)与[生成记录](figures/teaser/p4-joint-context-labeled-generation-record.json)。已目检四处标签拼写、对象指向、字号可读性、箭头与文字间距；PNG 为 1921×819、RGB。原无文字 P4 的哈希保持一致；未修改 PPT、论文源码或正式 PDF。

## 2026-11-03：将 P2/P3/P4 放入现有 teaser PPT

用户要求先查看三张素材在整体排版中的效果，再考虑生成 P5a/P5b。具体范围：导入当前单页 PPT，在已有图框内替换 P2/P3/P4，清除已被图像包含的占位标注，保留其他对象与现有布局。没有生成 P5/P6，也未改写论文图注或正文。

| 位置 | 真实基线 | 修改后 | 原因 |
| --- | --- | --- | --- |
| P2 | `P2`、`All input frames aggregated / Unobserved surfaces remain`（汇总全部输入后仍有未观测表面）及虚线框 | `p2-standalone.png`，保持原 377×160 图框，等比完整显示 | 直接查看聚合观测的示意素材在上排的辨识度 |
| P3 | `P3`、`New camera view s1 / Unobserved surfaces exposed`（新相机视图 s1 暴露未观测表面）及虚线框 | `p3-standalone.png`，保持原 350×149 图框，等比完整显示 | 与 P2 连续表达相机改变后的缺失暴露 |
| P4 | `P4 Jointly completed scene`、两段说明、四个原生标签和对应连接 | `p4-joint-context-labeled.png`，在原 850×360 区域等比放置；移除其内部全部 17 个占位对象 | 新素材已包含组件名、共享上下文及三条双向交互，避免重复标签和连接覆盖图像 |
| 图面小字 | `Conceptual placeholders`（概念占位） | `Conceptual illustrations`（概念示意） | P2/P3/P4 已经是概念图素材；P5/P6 仍保留各自占位 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，本轮从已有未提交工作区继续。实际 PPT 基线 SHA256 为 `60ecadfa10823080aa648e29f8609db9df5995534db743f635f7cdf8a51917fe`，已连同原 README 与本记录保存到 `paper/fig/teaser-editable/.build/inserted-concepts/before/`；本记录的真实基线 SHA256 为 `a3b14ec410aaa55d30a6bb2d28e0c038cb376ca81fdc04a8d0922ee1d3a2982c`。未把旧 HEAD 当作本轮原图。

使用 `@oai/artifact-tool` 导入并局部修改，删除 23 个目标占位对象，添加 3 张独立图片。程序核对 79 个不相关对象的位置和文字与导入基线一致；共享输入、方法框、外部箭头、P5/P6 均保持完整。README 同步说明当前填入状态，以及 P4 内部文字/连接属于位图、外部流程元素仍为原生可编辑对象。素材路径和 SHA256 加入幻灯片备注；已有来源记录与双语候选图注保留。

交付更新后的 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx) 和 [整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)。导出后已通过包结构、单页数量、1800×945 画布、参考字体与几何检查，并重新导入最终 PPT 渲染预览。当前文件有 73 个原生形状和 10 张独立图片；PPT SHA256 为 `424f0cd2697e0b98c7ec7ad8d2737e56efb57e714525c1d59e0c793da8b31420`。检查记录位于 `.build/inserted-concepts/validation.json`，目标删除/保留清单位于 `insertion-record.json`。论文 LaTeX、正式 PDF 及原始 PNG/JPEG 素材未修改。

## 2026-11-03：分别绘制 P5a/P5b 并放入 teaser

用户要求绘制 P5a 和 P5b。本轮使用内置 ImageGen 分两次生成独立素材：P5a 从已有 P2 中提取同视角车辆，表示全部输入聚合后仍未观测到的车尾；P5b 直接以 P5a 为编辑目标，将同一车尾面补全并标为金色。已保留纯白背景、相同观察方向、车身轮廓、车窗与两只可见轮胎，未加入道路、人物、额外缺口或图内文字。

| 位置 | 真实基线 | 本轮修改 | 原因 |
| --- | --- | --- | --- |
| P5a | `P5a`、`Asset with unknown U`（具有未知区域 U 的资产）和占位框 | [车辆聚合后素材](figures/teaser/p5a-vehicle-observed.png)，车尾为白底灰色斜线与虚线轮廓 | 明确该区域在汇总所有输入后仍未知，与 P2 的相同车尾对应 |
| P5b | `P5b`、`Same asset, completed U`（同一资产的 U 已补全）和占位框 | [车辆补全后素材](figures/teaser/p5b-vehicle-completed.png)，同一车尾面为浅金色实面 | 将变化集中于同一表面，已观测部分保持对应 |
| 小图尺寸 | 两图框均高 76 px，顶部 y=792 | 两图框高 96 px，顶部 y=772；底部仍为 y=868 | 只提取车辆后，原扁图框使车尾过小；局部加高改善缩小显示的辨识度 |
| 小对照外框与箭头 | 外框 y=780、高 123；箭头 y=831 | 外框 y=764、高 139，底边不变；箭头 y=820 | 为加高的小图留白并使比较箭头与两图居中 |
| 前后说明与图例 | `After aggregating all inputs` / `After joint completion`（全部输入聚合后 / 联合补全后），Observed / Completed | 原文、原位置、原字号保留 | 避免改变已明确的多帧聚合含义或重复在图内加字 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。本轮实际 PPT 基线 SHA256 为 `424f0cd2697e0b98c7ec7ad8d2737e56efb57e714525c1d59e0c793da8b31420`；原 PPT、README 和本记录已保存到 `paper/fig/teaser-editable/.build/inserted-assets-p5/before/`。日志基线 SHA256 为 `33830c248ba74150cab33edd30399c39562dd95acaa9cfb81d1c9c4ab9706032`。

分别保存 [P5a 提示词](figures/teaser/p5a-vehicle-observed-prompt.txt)、[P5b 提示词](figures/teaser/p5b-vehicle-completed-prompt.txt)和[成对生成记录](figures/teaser/p5-generation-record.json)。两张 RGB PNG 分别为 1586×992 与 1585×992；已目检车尾位置、配色、相同观察方向与图像完整性，未作逐像素配准或实测可见性声明。它们是概念示意，不是 Waymo 的实验重建输出。

使用 `@oai/artifact-tool` 导入当前 PPT，删除 6 个 P5 目标占位对象，增加两张独立图片；除指定的局部外框和比较箭头外，核对 75 个不相关对象的文字和位置未变。P2/P3/P4、共享输入与 P6 占位保留；README 和素材来源备注同步。更新后的 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx) 已通过结构、单页、画布、参考字体及几何检查，并重新导入最终文件渲染[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)。最终 PPT 包含 67 个原生形状与 12 张图片，SHA256 为 `fd87d56e814a2c7c850a1177eb1ab6081d4462bf12844b085afd6ff2b9a4d128`。验证及局部差异记录位于 `.build/inserted-assets-p5/`；未修改论文正文、正式 PDF 或原有 PNG/JPEG 素材。

## 2026-11-03：依次生成 P6a/P6b/P6c 并填满状态复用栏

按用户要求，通过三次独立、顺序执行的内置 ImageGen 调用生成三个场景素材。生成前沿用 P2/P3 的空间约定，并为车辆偏航和人体抬臂分别建立几何底图；不将一张图的状态改动累加到下一张图。P6a 与 P3 成对，P6b/P6c 则各自以 P4 参考状态为基准。

| 位置 | 真实基线 | 本轮修改 | 原因 |
| --- | --- | --- | --- |
| P6a | `P6a`、`New camera view s1 / Same completed content`（新相机视图 s1 / 同一补全内容）和占位框 | [新视角补全素材](figures/teaser/p6a-new-camera.png)：保持 P3 相机与人物姿态，将同一远侧车身、车尾和地面缺口补为金色表面 | 与上排 P3 构成同视角的缺失/补全对照 |
| P6b | `P6b`、`Same assets / Vehicle rotation`（同一资产 / 车辆旋转）和占位框 | [车辆旋转素材](figures/teaser/p6b-vehicle-rotation.png)：以 P4 相机为基准，车辆绕原地中心沿 +Z 偏航 45°，金色车尾随车刚体变换 | 显示补全表面随所属车辆复用；地面补全部位、背景和人物保持固定 |
| P6c | `P6c`、`Same assets / Human pose change`（同一资产 / 人体姿态改变）和占位框 | [人体换姿素材](figures/teaser/p6c-human-pose.png)：恢复 P4 原车辆朝向，只将同根位置处的人物改为抬臂姿态 | 单独表达人体关节控制，避免同时变化车辆或相机 |
| 外部状态标签 | `Camera view s1`、`Vehicle rotation`、`Human pose` | 原文字、字号与位置保留 | 素材本身无字，由既有原生标签说明唯一状态变化 |

本轮 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。真实 PPT 基线 SHA256 为 `fd87d56e814a2c7c850a1177eb1ab6081d4462bf12844b085afd6ff2b9a4d128`；原 PPT、README 和本记录保存于 `paper/fig/teaser-editable/.build/inserted-assets-p6/before/`。日志基线 SHA256 为 `b119a94449525b964495524bbd313ba2bd69dd76cec8cc12b1fdfe6eed431f30`。

保存 [P6a 提示词](figures/teaser/p6a-new-camera-prompt.txt)、[P6b 提示词](figures/teaser/p6b-vehicle-rotation-prompt.txt)、[P6c 提示词](figures/teaser/p6c-human-pose-prompt.txt)、[生成记录](figures/teaser/p6-generation-record.json)与[状态约定](figures/teaser/p6-state-contract.json)。P6a 为 1922×818，P6b/P6c 均为 1920×819，全部 RGB PNG。几何底图固定 P6b/P6c 的相机、道路、立面和根位置，分别只改变车辆偏航或人物关节；最终生成图经目检，不声明逐像素配准或实测角度精度。

已在当前 PPT 的原 360×153 图框内等比放入三张素材，删除 9 个原占位对象，保持 70 个不相关对象的位置和文字不变。所有 P2–P6 概念素材现已填满，P6 外部状态标签、输入序列、P4 交互标注、P5 比较及图例均保留。README 和备注同步完整状态及素材来源。最终 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx) 通过包结构、单页画布、参考字体、几何与重导入检查，并重新渲染[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)；含 58 个原生形状和 15 张独立图片，SHA256 为 `b7b2f31d38a2b21ad4a7802df776bf416a09df92caa18db49067f17440f76314`。核验与局部对象清单位于 `.build/inserted-assets-p6/`。本轮没有修改论文 LaTeX、正式 PDF 或已有图像素材；新增场景保持概念示意身份，不描述为实验结果。

## 2026-11-03：P2 三维几何表达、人物方向与连续背景缺失修订

用户指出原素材造型不协调，且单个斜线面不能表达资产几何补全。本轮实际查看 DiffComplete、PartCrafter 的 Figure 1，以及 GenAssets 的 Figures 1–2，提炼形状边界、统一材质和组件层次的做法；来源与设计判断见 [P2 分析说明](figures/teaser/p2-geometry-design.md)。随后用内置 ImageGen 生成新的独立 [P2 素材](figures/teaser/p2-geometry-concept.png)。整体上下排版未改。

| 位置 | 真实基线 / before | 修改后 / after | 原因 |
| --- | --- | --- | --- |
| 车辆形态与缺失 | 原 P2 为方盒车，整个车尾面白底斜线 / cuboid van with a hatched rear face | 简化厢式车的局部三维壳，车顶、后角和侧后边界共同出现覆盖缺失 / partial vehicle geometry with a spatially extended missing rear region | 表达几何结构的缺失，避免被读为缺少纹理 |
| 人物朝向 | 中间造型修订素材中的人物右向侧身，近似沿条纹方向迈步 / right-facing stride approximately along a zebra bar | 转为向画面左上、斑马线远端行走的背面斜视 / rear three-quarter walking pose toward the far end of the crosswalk | 按用户最新纠正保持输入中的过街运动方向 |
| 车后背景 | 中间提示词要求 “Keep just ONE separate small irregular white missing ROAD patch”，实际显示大面积完整青色道路加孤立小洞 | 车后左侧连续背景几何整块缺失，留白连接到场景左边界，孤立方洞和该区车道标记移除 / broad contiguous unobserved background behind the van | 用户指出该区域在输入序列中始终被遮挡，不能表达成只有一小块没有观测到 |

本轮 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，继承已有未提交工作区。用户指出两处问题时的真实 PNG 基线保存于 `paper/build/teaser-p2-geometry-style/before/p2-geometry-concept.png`，SHA256 为 `cb4ea3878fcbf27bc0f8621a41aab3cd5115f792d725208686601c8bafe20061`；日志真实基线保存在同一 `before/`，SHA256 为 `02cb22f6b69f7940404e5161887eb12b4fcbeaa0fe5a8932af257e981418890b`。旧 P2 和原空间约定保持原文件，新的宽范围覆盖设定不沿用旧小方块的数值可见性声明。

保存[初始提示词](figures/teaser/p2-geometry-concept-prompt.txt)、[边界修订提示词](figures/teaser/p2-geometry-concept-refinement-prompt.txt)、[最终人物与背景修订提示词](figures/teaser/p2-geometry-occlusion-prompt.txt)和[生成记录](figures/teaser/p2-geometry-generation-record.json)。最终 PNG 为 1921×819、RGB，已检查可解码性与视觉内容，无文字、箭头、标签或水印；SHA256 为 `f367fa6a8835a7a08527fa77c0738a290f5f4a1a1099f9a6d7a650402aea53fe`。当前只交付 P2 独立修订素材，未替换 PPT；现有 PPT 哈希仍为 `b7b2f31d38a2b21ad4a7802df776bf416a09df92caa18db49067f17440f76314`，P3–P6、论文源码及正式 PDF 均未修改。素材保持概念示意身份。

## 2026-11-03：将已确认 P2 覆盖回原 PPT，并生成新版 P3 候选

按用户要求，把已确认的 [P2 三维几何素材](figures/teaser/p2-geometry-concept.png) 换入当前 PPT。首次覆盖因文件占用失败；用户关闭进程后，文件哈希由 `b7b2f31d38a2b21ad4a7802df776bf416a09df92caa18db49067f17440f76314` 变为 `9b65793bdc8a0fbb49d9fe3f28c4f65e3c5a2064e07fcd06d2401a411179c16e`。为保留关闭前保存的用户修改，重新以这份最新文件为真实基线执行 P2 局部替换，而不是用此前候选覆盖用户的新状态。两份基线均保存在 `paper/fig/teaser-editable/.build/replaced-p2-geometry/before/`；最新基线为 `DriveCompose-teaser-after-close.pptx`。

| 位置 | 实际基线 / before | 本轮修改 / after | 原因 |
| --- | --- | --- | --- |
| PPT 中 P2 图片 | `p2-standalone.png`：方盒车、斜线车尾与小路面缺口 | 换入用户确认的 `p2-geometry-concept.png`：局部三维车壳、沿过街方向行走的人物、车后连续背景缺失 | 落实已确认的新造型和几何语义 |
| P2 图框与其他元素 | 图框为 left 721.86、top 86、width 375.29、height 160；用户关闭前保存的其余元素 | 图框不变，71 个不相关元素的可见文字与位置保留；补充 P2 素材来源备注 | 只替换 P2，保留用户当前排版与已保存修改 |
| P3 远侧表达 | 旧 P3 为完整方盒上的斜线面；新版首稿仍错误生成完整侧门和车轮 | 独立生成 [P3 候选](figures/teaser/p3-geometry-concept.png)，将前景远侧车身和车轮留空，观测到的另一侧车壳退到后方，车后背景保留大范围缺失 | 表达新相机暴露三维缺失，而非镜像 P2 或更换纹理；先供用户查看，未放入 PPT |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。日志真实基线保存于上述 `before/paper-revision-changes.md`，SHA256 为 `597e48f499b24b6ccc6a68dae8a07ccbf69c6d85de7c0e697ae7c7107a2fd21a`；原 P3 设计基线也已保存。README、P2 的采纳状态与 [P3 设计说明](figures/teaser/p3-design.md)同步本轮实际状态。

原 [PPT 路径](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx)已成功覆盖，SHA256 为 `3d90daabc82b09fe2dcb022e7418268c3899a425b73f27c8abaa6f86f9263bef`；含 57 个原生形状、15 张图片，与用户关闭后基线数量一致。包结构、单页尺寸、参考字体、布局与重导入检查通过，已从最终文件重新渲染[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)并目检。临时另存到 output 的备用交付副本在原路径覆盖成功后已移除；该副本的哈希经核对确认为本轮创建的文件。核验与局部差异记录位于 `.build/replaced-p2-geometry/after-close/`。

P3 用两次独立 ImageGen 调用完成初稿与针对性修订；保存[初始提示词](figures/teaser/p3-geometry-concept-prompt.txt)、[修订提示词](figures/teaser/p3-geometry-concept-refinement-prompt.txt)和[生成记录](figures/teaser/p3-geometry-generation-record.json)。最终候选为 1921×819、RGB，SHA256 为 `73623551bd3889432d524624956592306b99fca9d5e788ed5dc4bd424b8bbb00`；已检查可解码性与无文字、箭头、补全色等内容。它是参考图引导的概念素材，未声称来自同一显式网格的精确重投影或真实实验输出。PPT 中 P3–P6 保留旧素材，论文 LaTeX 与正式 PDF 未修改。

## 2026-11-03：重绘 P3 为几何覆盖示意，并补入人体正面未知

用户指出上一版把对侧外车门和轮毂当作从车内看到的结构。该剖视设定已退回；本轮先建立共同的简化世界与两台示意相机，再用内置 ImageGen 生成[新的 P3](figures/teaser/p3-geometry-concept.png)。用户认可车辆与背景后，又指出输入没有覆盖人体正面，因此最后一次生图只针对人物的观测覆盖修改，不通过转身或换动作回避缺失。

| 位置 | 真实基线 / before | 当前素材 / after | 原因 |
| --- | --- | --- | --- |
| 车辆内部 | 从大开口看见完整对侧外门把手、轮毂 / a cutaway showing exterior textures as an interior | 不展示内部；只保留当前可见的已观测外部片段，未知部分用粗略虚线包络表示 / outward observed fragments plus coarse unknown support | 区分未观测几何、实际车内结构与自由空间，不虚构可信内壁 |
| 未知支撑与立面背面 | 完整白车身、精确轮拱暗示形状已知；立面背面是一堵厚白墙 | 近白色、无材质阴影的稀疏虚线支撑；逆面立面减为轻轮廓 | 表达覆盖诊断，不预先画出完成后的精确资产形状 |
| 人体正面 | 车辆／背景修订后，人物仍为完整紫色，暗示正面已有观测 | 头、躯干及部分肢体的正面标为浅色未知，侧后缘保留少量紫色；步态和世界方向视觉保留 | 输入主要来自背面／后斜侧；模板人形和姿态支撑不能被误当作正面观测 |

当前 HEAD 仍为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。本轮从真实未提交工作区继续；旧 P3、设计说明、生成记录与日志基线保存在 `paper/build/teaser-p3-coverage/before/`。旧剖视 PNG 的 SHA256 为 `73623551bd3889432d524624956592306b99fca9d5e788ed5dc4bd424b8bbb00`；用户认可车辆／背景、提出人体问题时的素材保存为 `before/p3-before-human-coverage.png`，SHA256 为 `d1d877ac574a15c8a3959504a39659d98e35193204d68c6278fdf9ed9dc00bf9`。日志基线 SHA256 为 `84025d124de2c738d8bccff88c6ec79e294cac164bd3b4d080e043ccc4c13688`。

新增共同世界设定、两个相机的方位底图与构建脚本，位于 `paper/build/teaser-p3-coverage/`；底图只作为空间关系与覆盖可视化的约束。略去背向观测片段是本示意图的绘图约定，不是假定高斯渲染具有背面剔除。最终生成像素不声称来自同一显式网格的精确重投影，也不对应 Waymo 标定掩码或实测渲染结果。

保存[覆盖提示词](figures/teaser/p3-coverage-prompt.txt)、[包络修订提示词](figures/teaser/p3-coverage-refinement-prompt.txt)、[人体正面修订提示词](figures/teaser/p3-human-coverage-prompt.txt)、[完整生成记录](figures/teaser/p3-coverage-generation-record.json)及[设计说明](figures/teaser/p3-design.md)。旧剖视生成记录已标为弃用，并指向所保存的真实旧 PNG。当前 PNG 为 1920×819、RGB，完整性检查通过；SHA256 为 `b4fb4a233c74d41663ad517d2b3e7a61dbf12ee505e89ac51799bfa9f2ce0dff`。已目检无标题、标签、箭头、内部结构或金色补全内容；人体局部修改的周边有少量栅格差异，不声称逐像素不变。

本轮交付独立 P3 候选，未替换 PPT。原 PPT SHA256 仍为 `3d90daabc82b09fe2dcb022e7418268c3899a425b73f27c8abaa6f86f9263bef`；P2、P4–P6、论文源码与正式 PDF 未修改。README 同步当前候选身份与人体正面的观测边界。

## 2026-11-03：放入已确认 P3，按新版几何语义重绘 P4 候选

按用户要求将已确认的 [P3 几何覆盖素材](figures/teaser/p3-geometry-concept.png)放回原 PPT，同时继续完善 P4。P3 保留原图框及外部文字；P4 本轮交付[独立新候选](figures/teaser/p4-joint-completion.png)，未替换 PPT 中的旧 P4。

| 位置 | 真实基线 / before | 修改后 / after | 原因 |
| --- | --- | --- | --- |
| PPT 中 P3 | `p3-standalone.png`：方盒上的斜线面、完整图标人物 | `p3-geometry-concept.png`：车辆未知支撑、连续背景缺失与未观测人体正面 | 落实用户已确认的空间表达，避免车内剖视与完整正面观测的歧义 |
| P3 图框及其他元素 | left 1427、top 92.02、width 350、height 148.96 | 图框不变，71 个不相关元素保留，可见文字未修改 | 保留用户当前排版和先前修改 |
| P4 车辆 | 方盒车与单个金色车尾平面 | 沿用新版 P2 的厢式车，金色连接车尾、圆角、短车顶续接及后下部结构 | 表达连贯三维结构的补全，而非给现成面片换色 |
| P4 背景 | 完整地台中的小金色方块 | 车后左侧大范围道路连续延伸并标为金色，与已观测青色路面齐平衔接 | 对应已确认 P2 的大范围背景缺失 |
| P4 人体与联合上下文 | 图标人物；三个组件连到同一共享条带 | 保留 P2 的三维人形、朝向与步态；四个标签和三条双向分支保留 | 人体正面补全在当前相机下主要背向，不通过转身或把已观测背部涂金强行显示；继续突出共同上下文 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`。真实 PPT 基线 SHA256 为 `3d90daabc82b09fe2dcb022e7418268c3899a425b73f27c8abaa6f86f9263bef`，原 PPT、预览、README、P3 说明与记录、日志保存于 `paper/fig/teaser-editable/.build/replaced-p3-coverage/before/`。日志基线 SHA256 为 `642623424ac5b6358f8f882f1f9c5fe5a61a7a72f76c9e72850cbba83be8bbc4`。旧 P4 同时保存于 `paper/build/teaser-p4-completion/before/`，原文件未覆盖。

原 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx)已覆盖成功，SHA256 为 `a6ba173b0aab2950e1a0aefa764e4f12b7230ba4f417b522015cb87773d60e61`；57 个原生形状、15 张图片的数量保持不变。包结构、单页尺寸、参考字体、布局及重导入检查通过，已从最终文件重新渲染并目检[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)。局部差异与核验记录位于 `.build/replaced-p3-coverage/`，P2/P4/P5/P6 图片和外部原生排版未改。

P4 使用一次内置 ImageGen 调用生成新候选，参考分别承担：P2 的相机、造型与姿态，旧 P4 的四个标签与三条上下文分支，P3 的未知内容定义。保存[提示词](figures/teaser/p4-joint-completion-prompt.txt)、[设计说明](figures/teaser/p4-joint-completion-design.md)和[生成记录](figures/teaser/p4-joint-completion-generation-record.json)。PNG 为 1920×819、RGB，完整性检查通过；SHA256 为 `a516ba726f37fd1dda14224c926e4abaa5c1fd9a31d6f1ebf8b2c66b86a2219f`。已目检四个标签各出现一次、三条双向分支通向同一个共享上下文、无车内剖视或额外主标题。图面为生成式概念示意，不声明精确几何掩码、逐像素对应或真实实验结果。

README 与 P3 采纳状态已同步。P4 候选暂不放入 PPT，论文源码、正式 PDF、P5 与 P6 均未修改。

## 2026-11-03：P4 补入缺失墙体

用户指出背景墙仍需补全。本轮仅针对 [P4 独立候选](figures/teaser/p4-joint-completion.png)的墙体作局部 ImageGen 修订，延续已确认的相机、车辆、人物和共享上下文布局。

| 位置 | 真实基线 / before | 修改后 / after | 原因 |
| --- | --- | --- | --- |
| 背景墙 | 灰色墙体的左边界仍是阶梯状断口，背景补全只体现在金色路面 / incomplete gray facade fragment | 沿原立面补入金色完整墙段，连接顶部压沿、竖直端部与地面 / connected gold facade continuation with coping and end thickness | 背景几何同时包括道路和立面；补全后的场景不应留下原有墙体缺口 |
| 已观测墙面与图内文字 | 灰色窗墙、Background 标签及三条共享上下文分支 | 灰色窗墙保留，四个标签和三条双向分支视觉保留 / observed window wall and label topology retained | 保留观测与补全的来源区分，避免整墙涂金或改变联合补全机制 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。补墙前 PNG、设计说明、生成记录及日志已保存至 `paper/build/teaser-p4-completion/wall-before/`。真实 PNG 基线 SHA256 为 `a516ba726f37fd1dda14224c926e4abaa5c1fd9a31d6f1ebf8b2c66b86a2219f`，日志基线 SHA256 为 `694af85f3f0d9be3045a617cdb51260362533995b9511614f3a438bc0635f3ec`。

保存[墙体修订提示词](figures/teaser/p4-wall-completion-prompt.txt)，并更新同一份[生成记录](figures/teaser/p4-joint-completion-generation-record.json)和[设计说明](figures/teaser/p4-joint-completion-design.md)。采用一次内置 ImageGen 局部编辑；生成原件保留在默认输出位置，选定结果复制回项目同一素材路径。当前 PNG 为 1920×819、RGB，完整性检查通过，SHA256 为 `289324ea596082ecc52e36f5d433d8cd3ef2630f2b9e3f5859bcfb634ed0cce4`。已目检金色墙段与灰墙衔接、标签文字及共享上下文拓扑；场景主体视觉保留，不声称栅格逐像素不变。

本轮没有改动 PPT；其 SHA256 仍为 `a6ba173b0aab2950e1a0aefa764e4f12b7230ba4f417b522015cb87773d60e61`。P2/P3 素材哈希保持不变，论文源码和正式 PDF 未修改。P4 仍为独立概念候选，新增墙段的形状与范围用于说明机制，不是标定后的实验输出。

## 2026-11-03：放入已确认 P4，生成新版 P5a/P5b 几何对照

按用户要求将包含墙体补全的 [P4](figures/teaser/p4-joint-completion.png) 放回原 PPT，然后分别生成新版 [P5a](figures/teaser/p5a-geometry-observed.png) 和 [P5b](figures/teaser/p5b-geometry-completed.png) 独立候选。上下排版、共享输入和外部原生文字均保留；P5 两张候选尚未替换到 PPT。

| 位置 | 真实基线 / before | 本轮修改 / after | 原因 |
| --- | --- | --- | --- |
| PPT 的 P4 | `p4-joint-context-labeled.png`：方盒车、完整地台上的小金色方块 | `p4-joint-completion.png`：圆角厢式车，金色车尾后角、连续道路及墙体补全 / connected vehicle and background geometry | 落实用户确认的新版造型与背景几何含义 |
| P4 图框与其余元素 | left 462.8、top 392、width 844.4、height 360；71 个不相关元素 | 外框保留；71 个不相关元素的位置与可见文字保留 / original placement and unrelated elements retained | 仅替换已确认的素材，延续当前排版 |
| P5a | 方盒车尾的白底斜线四边形 / hatched planar rear cap | 新版厢式车的后部几何缺失，留白加稀疏虚线 / missing rear geometry with coarse unknown support | 说明汇总全部输入后仍有未恢复结构，不预先假定后门完整形状 |
| P5b | 同一四边形变金色 / gold planar cap | 相同观察方向，补入金色车尾、圆角、短顶部过渡及保险杠 / connected completed rear structure | 体现三维几何的补入，与新版 P4 对应 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。真实 PPT 基线 SHA256 为 `a6ba173b0aab2950e1a0aefa764e4f12b7230ba4f417b522015cb87773d60e61`；原 PPT、预览、README、P4 说明及生成记录、日志保存于 `paper/fig/teaser-editable/.build/replaced-p4-completion/before/`。日志基线 SHA256 为 `5379769cca22148e4fc5c5068c5a735eb044766bebd51575efc901dbf85fa39e`。旧 P5a/P5b 与生成记录另存至 `paper/build/teaser-p5-geometry/before/`，原文件保持不变。

使用 `@oai/artifact-tool` 对原 PPT 作 P4 图片局部替换，包结构、单页尺寸、Times New Roman 参考字体、布局与重导入检查通过。原 [PPT 路径](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx)已覆盖，SHA256 为 `82f5778291c994d0c2c440d37f95a0caaf84509b3a5db5d6cd35ce358221ab2d`；含 57 个原生形状和 15 张图片。已从最终文件重新导入、渲染并目检[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)。验证和局部差异记录位于 `.build/replaced-p4-completion/`；P4 素材本身没有再次生成或修改。

P5 使用两次独立、顺序执行的内置 ImageGen 调用。P5a 以新版 P2 为车辆、相机和未知范围参考；P5b 以新 P5a 为编辑目标，以 P4 的金色车尾为造型参考。保存 [P5a 提示词](figures/teaser/p5a-geometry-observed-prompt.txt)、[P5b 提示词](figures/teaser/p5b-geometry-completed-prompt.txt)、[设计说明](figures/teaser/p5-geometry-design.md)和[生成记录](figures/teaser/p5-geometry-generation-record.json)。两张 RGB PNG 分别为 1586×992、1585×992，完整性检查通过；SHA256 分别为 `e8d63747d479fc1dd22c1f01ab2555bbb4aedc15e9510327f437ad47387ccdac`、`c9bf798bc88f36ef6040182031e3607d2c44fa2e17cda8409be5c9cb11c7fa66`。已目检视角、车身与轮胎的视觉对应、缺失和补全范围；不声明逐像素配准或实测遮挡范围。

README 与 P4 采纳状态已同步。P5 新候选尚未放入 PPT；PPT 中 P5/P6 仍是早期素材。论文源码、正式 PDF、P2/P3/P6 及旧 P5 图片未修改。全部生成面板保持概念示意身份。

## 2026-11-03：将已确认的 P5a/P5b 放回原 PPT

按用户确认，将新版 [P5a](figures/teaser/p5a-geometry-observed.png) 和 [P5b](figures/teaser/p5b-geometry-completed.png) 替换到原 PPT。本轮只放入已生成素材，没有再次生图或改变整体布局。

| 位置 | 真实基线 / before | 修改后 / after | 原因 |
| --- | --- | --- | --- |
| P5a 图片 | `p5a-vehicle-observed.png`：方盒车的斜线后面 / hatched planar rear cap | `p5a-geometry-observed.png`：新版车辆的缺失后部几何，留白及稀疏虚线 / missing rear geometry with coarse support | 放入用户确认的观测聚合示意，与新版 P2/P4 车辆一致 |
| P5b 图片 | `p5b-vehicle-completed.png`：同一平面变金色 / gold planar rear cap | `p5b-geometry-completed.png`：连续金色车尾、圆角、短顶部过渡和保险杠 / connected completed rear geometry | 放入用户确认的三维几何补全对照 |
| 图框与外部说明 | P5a left 552.76、top 772、width 153.48、height 96；P5b left 899.31、top 772、width 153.39、height 96；原生说明、箭头及图例 | 图框尺寸及位置不变，70 个不相关元素的可见文字与位置保留 / original frames, captions, arrow and legend retained | 将修改限制为两张图片，延续当前排版 |

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。本轮真实 PPT 基线 SHA256 为 `82f5778291c994d0c2c440d37f95a0caaf84509b3a5db5d6cd35ce358221ab2d`。原 PPT、预览、README、P5 设计说明与生成记录、日志保存于 `paper/fig/teaser-editable/.build/replaced-p5-geometry/before/`；日志基线 SHA256 为 `5e4f25c417441e76860bf32cbe8c1af7753e3c48ea18afa59213d8af1190aa94`。

使用 `@oai/artifact-tool` 导入并局部替换两张图片，原 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx) 已覆盖，SHA256 为 `03d251bf0646e33ba1a3e8a7e7cb5a6e2f8be2a843dfb99d578e8cf9283adfc0`；含 57 个原生形状及 15 张图片。包结构、单页尺寸、参考字体、布局和重导入检查通过，最终文件已重新渲染为[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)并目检。嵌入媒体哈希对照确认只更换 P5a/P5b，其余媒体完全保留。局部差异、验证与媒体对照保存在 `.build/replaced-p5-geometry/`。

README 和 P5 设计、生成记录已同步采纳状态。P2/P3/P4/P6 素材、论文源码和正式 PDF 未修改；P6 保留现有早期素材。

## 2026-11-03：新版 P6a/P6b/P6c 生成并放回原 PPT

按用户要求继续完成右侧三张复用图，沿用新版 P3/P4 的场景身份、圆角车辆、三维人形和连续背景补全。分别生成 [P6a](figures/teaser/p6a-geometry-new-camera.png)、[P6b](figures/teaser/p6b-geometry-vehicle-rotation.png)、[P6c](figures/teaser/p6c-geometry-human-pose.png)，并在核对后放入原 PPT。

| 位置 | 真实基线 / before | 修改后 / after | 原因 |
| --- | --- | --- | --- |
| P6a 新视角 | 旧方盒车、完整紫色图标人，前景墙保持空轮廓，小路块补全 / cuboid scene with incomplete reverse facade | 对应 P3 相机，金色补入新显露车身、人体正面、连续车后道路及实体墙背面；保留灰蓝观测车顶 / same new camera with completed actor and background geometry | 与新版 P3 的未知范围和人体正面缺少输入的设定一致 |
| P6b 车辆旋转 | 方盒车转向、背景小金色路块 / earlier box-shaped vehicle yaw | 新版圆角厢式车绕固定中心转向，金色后部随车旋转；完整墙体、道路和行人保持原状态 / attached rear geometry under a vehicle-only yaw | 展示同一资产及其补全结构在新刚体状态下复用 |
| P6c 人体姿态 | 图标人物举臂，背景与车辆为旧样式 / icon-style articulation scene | 保留 P4 未旋转车辆与完整背景，同一人形仅抬起双臂，行走腿姿、根位置和朝向保留 / arm articulation with original vehicle state | 避免累加 P6b 车辆旋转，也不通过转身或给已观测背部涂金强行展示补全 |
| 三个图框及外部说明 | 既有三个约 360×153 图框，Camera view / Vehicle rotation / Human pose 原生标签 | 保留原外框、标签和流程箭头；69 个不相关元素的位置与可见文字不变 / existing layout and labels retained | 局部更新素材，延续当前上下对比结构 |

本轮实际使用四次内置 ImageGen 调用：P6a 初稿及一次覆盖颜色修订、P6b 和 P6c 各一次。P6a 初稿错误地把新显露长侧车身画成灰蓝色，已局部改为金色；该首版保存在 `paper/build/teaser-p6-geometry/p6a-before-coverage-color.png`，未放入 PPT。P6b 参考既有几何导图的转向，忽略其旧造型和背景；约 45° 是目标状态，不作为生成像素实测角度。P6c 独立以 P4 为参考，未继承 P6b 的旋转。

当前 HEAD 为 `09ec7adb91eca760fe8c2682d91b40a479f2bcfe`，从已有未提交工作区继续。真实 PPT 基线 SHA256 为 `03d251bf0646e33ba1a3e8a7e7cb5a6e2f8be2a843dfb99d578e8cf9283adfc0`。原 PPT、预览、README 及日志保存于 `paper/fig/teaser-editable/.build/replaced-p6-geometry/before/`，日志基线 SHA256 为 `a97766f5e215946692dd45bb95ce1408155f7d512be523ae7ee20dc230c0890b`；旧 P6 素材与状态、生成记录保存于 `paper/build/teaser-p6-geometry/before/`，原文件保留。

三张 RGB PNG 均为 1920×819，完整性检查通过；SHA256 分别为 `5112531097b6fa94e3bcb743aa509ce37df2a01a502294d3f47b5e8e9bd448f7`、`8ec47ffe8b3c227489c3e5c67fd7dab64c46ea0accb84ff3801dae210c9ee507`、`15d94de9a7df59641bdaea0657ac5c9dce106e46c15250a03536d8e45e824c91`。保存 [P6a 提示词](figures/teaser/p6a-geometry-new-camera-prompt.txt)、[P6a 修订提示词](figures/teaser/p6a-geometry-coverage-refinement-prompt.txt)、[P6b 提示词](figures/teaser/p6b-geometry-vehicle-rotation-prompt.txt)、[P6c 提示词](figures/teaser/p6c-geometry-human-pose-prompt.txt)、[设计说明](figures/teaser/p6-geometry-design.md)、[状态约定](figures/teaser/p6-geometry-state-contract.json)和[生成记录](figures/teaser/p6-geometry-generation-record.json)。已目检姿态、颜色归属、自然遮挡及图内无文字和箭头；生成像素不声明精确配准、标定掩码或实验输出。

使用 `@oai/artifact-tool` 仅替换三个图片对象。原 [PPT](../paper/fig/teaser-editable/output/DriveCompose-teaser-placeholder.pptx) 已覆盖，SHA256 为 `a49b1ce1a17846250b0aea52b1f10aee5bfb2a34f903e003565c526ff0a1ba61`；含 57 个原生形状和 15 张图片。包结构、单页尺寸、参考字体、布局及重导入检查通过，已从最终文件重新渲染并目检[整图预览](../paper/fig/teaser-editable/output/DriveCompose-teaser-preview.png)。嵌入媒体哈希对照确认只更换 P6a/P6b/P6c；其余媒体保持不变。构建、验证及媒体对照位于 `.build/replaced-p6-geometry/`。

README 已同步。P2/P3/P4/P5 图片、论文 LaTeX 和正式 PDF 均未修改；本轮范围止于 P6 素材及对应 PPT 图片替换。
