# DriveCompose 图 3：PPT 与 draw.io 矢量重建

对应当前英文论文第 4 页 Figure 3（Joint latent completion）。原稿和论文插图保持原样。

## 文件

- `figure3-powerpoint.pptx`：1 页，471 个原生可编辑对象，8 个区域组；文本、公式项、token、斜线纹理、箭头和边框均可编辑。
- `figure3-drawio.drawio`：1 页，471 个原生图元与 8 个区域组；在可见 draw.io 画布通过 graph API 构建后保存。
- `figure3-drawio.svg`：draw.io 原生图形渲染器导出的矢量图，无嵌入图片；用 HTML `foreignObject` 保留富文本标签，建议在浏览器查看，编辑优先使用 `.drawio`。
- 两个同名 PNG 为实际应用渲染；`figure3-comparison.png` 用于并排比较。
- `reconstruction_spec.json` 保存逐对象几何与来源；`verification.json` 保存结构核验结果。

## 编辑和验证

PPTX 使用原生 OOXML 构建。本机的 PowerPoint COM 注册指向 WPS，因此实际渲染已用 WPS Presentation 验证；未使用 Microsoft PowerPoint。字体为 Times New Roman，未嵌入字体。公式是可编辑富文本，不是 Office 公式对象。自定义曲线和路径为可编辑矢量；移动分组后应检查连线，尤其是补全出口的跨线断口。

两版均无图片对象、无位图嵌入。图中文字已与重建清单逐项核对，连接端点引用完整。draw.io 最终结构审查为 0 hard / 0 warning。各区域和整图已对照原图及实际渲染自审；不声称独立盲审。按放大图查看字体与线条，未对原单栏 86mm 排版重新认证。

与原图的局部差异：原有虚线补全出口在穿过实线速度回路处留出 16px 断口，以表达非连接交叉；少量字号和文本框作适配，保留原文字、布局、面板范围与配色。没有替换论文中的原始图 3。

构建脚本、阶段文件和审查中间产物保存在 `pre-research/_archive/drivecompose/20261030-figure3-vector-work/`。
