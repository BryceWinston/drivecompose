# DriveCompose CVPR 风格总览图

本目录交付 2026-10-20 的科研总览图。科学依据为项目当前数据契约、查询分解、联合补全、解码、观测验证及在线组装实现。

用户反馈布局紧凑、颜色偏淡后，新增 [V2：四篇项目图风格参考下的重新生成版](revision-v2-reference/README.md)，采用三阶段布局、鲜明配色和更大的场景表现；下列原生矢量图保留为前版。

- [总览图 PNG](drivecompose-overview-native.png)：3600 × 1680，供预览和评议。
- [总览图 SVG](drivecompose-overview-native.svg)：2400 × 1120 原生矢量画布，文本、形状和连线可编辑。
- [矢量绘图源码](draw_overview.py) · [渲染与边界检查](render_overview.mjs) · [检查记录](render-qa.json)
- [近期论文参考与设计原则](references.md)
- [科学拓扑与设计规格](design-spec.json)
- [英文图注](caption.md) · [科学与视觉自审](review.md)
- [完整视觉草稿提示词](production-prompt-v6-correction.txt)

采用五个阅读区域：多相机观测、规范查询、观测锚定联合补全、固定高斯世界、状态驱动复用。联合补全作为主焦点，展开局部注意力、全局记忆及已见 / 空域约束。图内英文方便后续论文排版。

本轮依次应用 `design-scientific-figure` 的科学语义和构图流程、`nature-academic-search` 的来源核验，并尝试 Image Gen 与已授权的 `gpt-image` 回退。保留了三轮光栅草稿，但它们存在箭头方向、接受顺序或文字错误，均未选为交付图。最终按同一科学规格重新绘制原生 SVG，并由 Edge 渲染 PNG；没有通过脚本修改生图模型的 PNG。

视觉草稿提示词按 Sivia overview 模板检查：模板为 15,356 个非空白字符，最后一版完整提示词为 23,960 个非空白字符。提示词与请求元数据保留用于过程追溯。

PNG 已实际查看，SVG 文本边界和文本间重叠检查通过。原生图含 51 个文本对象，无嵌入位图。最小字号为 34 SVG px，按 178 mm 双栏宽度折算约 7.15 pt。正式论文中应保持双栏宽度，或根据最终模板重新检查字号。

图中驾驶画面、空间支撑和高斯均为机制示意。当前交付为方法图设计稿，尚未替换为真实 Waymo / 模型结果，也未创建 PPT 或 draw.io 重建件。

重新生成：先运行 `python draw_overview.py`，再运行 `node render_overview.mjs`。后者支持用 `OVERVIEW_PUPPETEER_PATH` 和 `OVERVIEW_BROWSER_PATH` 指定本机渲染依赖。
