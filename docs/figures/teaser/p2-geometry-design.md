# P2：部分三维几何的概念表达

本轮只修改 P2 独立素材。当前文件为 [p2-geometry-concept.png](p2-geometry-concept.png)，保留无文字、白底、约 2.35:1 的格式。整体 teaser 排版沿用现有上下方法对比。

## 看过的原图与采用的做法

以下区分原图观察与本项目的设计判断；它们不是统一的“顶会风格”标准。

| 原论文与已查看图件 | 原图中的具体做法 | 对 P2 的设计启发 |
| --- | --- | --- |
| [DiffComplete，NeurIPS 2023，Figure 1](https://proceedings.neurips.cc/paper_files/paper/2023/file/ef7bd1f9cbf8a5ab7ddcaccd50699c90-Paper-Conference.pdf) | 将不完整扫描与完整形状成对展示；缺失出现在实际三维轮廓和表面覆盖中，采用简洁的单色着色 | 缺失应改变可见几何的边界，不能只把一个完整车尾面涂白；保留可识别的车身形态 |
| [PartCrafter，NeurIPS 2025，Figure 1](https://proceedings.neurips.cc/paper_files/paper/2025/file/32cc61322f1e2f56f989d29ccc7cfbb7-Paper-Conference.pdf) | 以统一三维材质和组件颜色展示可分解结构 | 颜色服务于背景、车辆、人体的角色；减少不承担信息的描边和纹理 |
| [GenAssets，CVPR 2025，Figures 1–2](https://research-assets.waabi.ai/GenAssets/paper.pdf) | Figure 1 展示多视角资产；Figure 2 将背景模型、独立资产和装配后的场景区分开 | 车辆需要在不同视角保持身份，背景只提供关系和位置线索，不能抢占主体 |

检索核验日期：2026-11-03。实际查看了三篇论文的 Figure 1，以及 GenAssets 的 Figure 2；没有根据摘要推断其画法。原论文图件仅用于分析，未直接拼入 P2。

## 本轮变化

| 位置 | 实际基线 | 本轮 P2 | 目的 |
| --- | --- | --- | --- |
| 车辆形态 | 原 P2 是灰蓝长方体，白色斜线集中在车尾平面 | 简化厢式车保留驾驶室、车顶曲面和轮拱；车尾及相邻转角结构缺失，观测边界跨越车顶和侧后部 | 表达 partial 3D geometry，而不是缺纹理或单块面片 |
| 人物朝向 | 第一张造型修订中，人物右向侧身，步幅近似沿斑马线条纹延展方向 | 人物转向斑马线远端、画面左上方，呈背面斜视，跨条纹行走 | 与输入的过街运动方向对应 |
| 车后背景 | 中间修订稿曾写入 “Keep just ONE separate small irregular white missing ROAD patch”，并恢复了车后的大面积青色路面 | 用户指出该区域持续被遮挡；当前删除车后左侧连续的大面积背景几何，留白一直连接到场景左边界，移除孤立小方洞和该区车道标记 | 表达跨输入序列仍未观测的背景范围，避免把未知区域缩成装饰性小孔 |
| 表现形式 | 粗地台、平面立牌、方盒车和图标式人物 | 薄的道路片段、局部立面、统一哑光三维形态和克制配色 | 保留抽象性，改善造型与视觉协调 |

## 当前空间约定

- 车辆朝向保持右上，车尾在左下；人物仍在车前方右侧的过街区域。
- 人物朝 +Y，即沿过街走向朝远侧路缘；在此示意相机中投影为左上，不能沿斑马线条纹方向走。
- 车后左侧大面积背景为联合观测仍未覆盖的区域。留白表示没有重建几何，不表示物理坑洞。
- 车辆缺失几何与背景缺失几何分别属于车辆和背景；后续车辆变换不能带走背景缺口。
- 当前不完整车身不绘制厚的切割面、机械内部或破损碎片。金色继续留给后续补全几何。
- 这是新的概念覆盖设定，替代旧 P2 中“整个车尾平面 + 单个小路面方块”的表达。旧 JSON 的数值可见性检查不自动适用于本张生成图；本轮不声称来自 Waymo 的标定掩码。
- 当前人体仍处于同一斑马线区域，但生成修改并非逐像素配准。后续 P3 应只改变观察相机，P4 则在同一场景与状态中加入缺失几何。

## 交付与检查

使用内置 ImageGen 生成并进行两次针对性修订。当前 PNG 为 1921×819、RGB，已检查文件完整性及无标题、标注、箭头、图框和水印。用户确认 P2 后，已将其放入原 PPT 的原图框；关闭进程前保存的用户修改一并保留。P3 已另行生成[新几何候选](p3-geometry-concept.png)，供审阅；当前 PPT 中 P3–P6 仍保留早期素材。

[初始提示词](p2-geometry-concept-prompt.txt)、[边界修订提示词](p2-geometry-concept-refinement-prompt.txt)、[本轮朝向与背景修订提示词](p2-geometry-occlusion-prompt.txt)、[生成记录](p2-geometry-generation-record.json)。

用户指出问题时的真实素材基线保存在 [before/p2-geometry-concept.png](../../../paper/build/teaser-p2-geometry-style/before/p2-geometry-concept.png)。
