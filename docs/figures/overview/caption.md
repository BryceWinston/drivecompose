# 总览图图注

English: \textbf{DriveCompose overview.} (a) Visual encoding, motion-aware canonical aggregation, and type-specific latent encoding convert image logs into structured latents. (b) Group-local attention and CCM read/write update component tokens for conditional-flow completion. (c) Query-wise Gaussian decoding produces background and sky, canonical rigid assets, and canonical human assets. Rigid assets retain their rigid binding; humans inherit skinning weights and a rest skeleton. State-driven composition and rendering reuse these assets for closed-loop simulation.

中文: \textbf{DriveCompose 总览。}（a）视觉编码、运动感知的规范聚合与类型专属潜码编码将图像日志转换为结构化潜码。（b）组内局部注意力与 CCM 读写更新组件 token，用于条件流补全。（c）逐查询高斯解码生成背景与天空、规范刚体资产和规范人体资产。刚体资产保留刚体绑定，人体资产继承蒙皮权重与静止骨架。刚体变换与骨架运动将解码资产放置到背景中，完成场景组合。 状态驱动的装配与渲染复用这些资产，为闭环仿真提供观测。
