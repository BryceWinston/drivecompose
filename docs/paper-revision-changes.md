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

## 2026-10-28：首页加入用户指定 teaser

基线提交：`e98697e09af130895fe14f70fbc840571da28a0d`。论文源码开始时与 HEAD 一致；上一轮未提交的 `docs/figures/teaser/` 是既有设计产物，本轮直接复用其 Waymo 风格图，不重新生成。修改前真实文本保存在 `paper/build/teaser-insertion/baseline.json`。

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

两版最后一次编译均成功且实际写入新 PDF；日志无编译错误、未定义引用、缺字、overfull 或图注警告。Figure 1 均在首页标题下、摘要前；图框宽 495 pt、高 165 pt。原方法总览为第 2 页 Figure 2，双语流程引用同步。英文共 12 页（之前 11 页），正文结论与参考文献均在第 9 页；正文仍超过 8 页目标，本轮未压缩。中文共 9 页。已查看两版首页、英文流程图及正文末页，无重叠或裁切；最后修正图注锚点后，两版首页渲染与已检查版本逐字节一致。16 项受保护源码/图件哈希未变，四个正文文件只改引用标签。核验记录：`paper/build/teaser-insertion/check.json`。

[英文正式稿](../paper/build/en/main.pdf) · [中文正式稿](../paper/build/zh/main_zh.pdf)。排版与核验完成后，用户授权提交并推送本轮图件、双语源码、正式 PDF 和对应记录。

## 2026-10-28：摘要开头收紧并突出联合补全与资产复用

基线提交：`2f86dc78ec1da7210983446ab853b9947a0ce95a`。两份摘要源码在本轮开始时均与 HEAD 一致；本地既有的三个 pointforward PDF 删除状态不属于本轮改动。真实源码、正式 PDF 哈希与受保护文件清单保存在 `paper/build/abstract-revision/baseline.json`。

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

两版主稿均成功编译并实际写入新 PDF，日志无编译错误、未定义引用、缺字或 overfull 警告。英文仍为 12 页，正文结论及参考文献起始均在第 9 页；中文仍为 9 页，结论在第 6 页、参考文献从第 7 页开始。英文摘要 188 → 177 词，中文 404 → 395 字符；本轮未增加页数，原有英文正文越过第 8 页的状态不变。已目视检查两版首页及正文结论页，无重叠、裁切或缺字，新增 20.5% 正常显示。132 项受保护文件的哈希或既有缺失状态与本轮基线一致，用户已有的三个 PDF 删除状态保留。详细核验见 `paper/build/abstract-revision/check.json`。本轮未提交或推送。


## 2026-10-28：仅微调双语摘要首句（nature-polishing 检查后）

范围：仅英文与中文摘要第一句。基线提交为 `2f86dc78ec1da7210983446ab853b9947a0ce95a`，本轮真实基线为该提交之上的未提交工作区，已保存在 `paper/build/abstract-revision/first-sentence-baseline.json`；先前摘要改动不计入本轮。

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

编译与版面核验：双语候选稿均成功编译，日志无未定义引用、缺字或 overfull 警告；两版首页与结论页目视检查无重叠、裁切或缺字。英文总页数保持 12 页、正文及结论仍结束于第 9 页；中文保持 9 页、结论在第 6 页。原有英文正文超出 8 页的状态不变。英文正式 PDF 已替换并校验哈希。中文正式 PDF 已替换并校验哈希。 两个摘要除首句外逐字不变，受保护文件与本轮基线一致。检查记录见 `paper/build/abstract-revision/first-sentence-check.json`。本轮未提交或推送。


## 2026-10-28：撤回摘要首句试改，恢复上一版

用户认为原首句更清晰，本轮仅撤回上一轮首句替换，中英文摘要恢复至 `first-sentence-baseline.json` 中保存的实际工作区基线；不使用更早 HEAD 覆盖先前摘要修改。基线提交仍为 `2f86dc78ec1da7210983446ab853b9947a0ce95a`；撤回前的实际文本另存于 `paper/build/abstract-revision/first-sentence-revert-baseline.json`。

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

基线 HEAD：`2f86dc78ec1da7210983446ab853b9947a0ce95a`；实际起点是此前已确认但尚未提交的 177 词摘要工作区，不能以 HEAD 中的旧摘要冒充本轮修改前文本。真实双语原文、PDF 哈希与受保护文件状态保存于 `paper/build/abstract-revision/consistency-baseline.json`。

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

两版主稿均重新编译成功并实际写入正式 PDF。日志无编译错误、未定义引用、缺字或 overfull 警告。两版首页及结论页已目视检查，无重叠或裁切，确认新版观测一致性表述及 20.5% 正常显示。英文仍为 12 页，正文结论与参考文献均在第 9 页；中文仍为 9 页，结论在第 6 页、参考文献从第 7 页开始。英文摘要缩为 173 词，未增加页数；原有英文正文超过 8 页的状态不变。132 项受保护文件及既有缺失状态未变，已有改动记录前缀完整保留。详细核验保存于 `paper/build/abstract-revision/consistency-check.json`。按本轮用户授权提交并推送。


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
