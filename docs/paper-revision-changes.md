# 当前改动：压缩 §3.2 与 §3.5

更新：2026-10-25。仅修改中英文主稿 §3.2、§3.5，新增双语补充材料 C/D。图示仅提出建议，本轮未改 Figure 1，也未增加正文图。其他主稿章节（含上一轮 §3.6）保持本轮起点原文。

基线：HEAD `ee5b6cb` 上的本轮未提交工作区。真实原文保存在 `paper/build/revision-baseline.json` 的 `composition_frontend_before`，英文 PDF 哈希、逐页文本和位置测量保存在 `composition_frontend_pdf_before`。Git 未暂存差异还包含此前 §3.6 的改动；本轮范围以此记录及[本轮彩色左右对照](../paper/build/method-revision-diff.html)为准。

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
