# 总览图风格候选，待用户确认

用户于 2026-10-23 提供两张参考图，要求先生成候选、不写入论文，潜码保持抽象表示，并核对 E/D 形状与箭头。

- 当前候选：[candidate-v5.png](candidate-v5.png)
- 完整生图指令：[production-prompt-v5.txt](production-prompt-v5.txt)
- 后端：内置 Image Gen；光栅候选，不是可编辑矢量成品。
- 指令非空白字符 17,286，绑定 overview-template.txt 为 15,356，长度核验通过。
- 两张用户参考图保存在同目录。借用图形风格，不借用其方法或结果。
- 论文当前仍引用 `paper/fig/drivecompose-overview-20261021.png`。本候选未写入论文，未触发编译。

## 核验状态

潜码为抽象 token；主要编码器为左宽右窄，主要解码器为左窄右宽；运行时 W 与状态分别进入渲染器。场景为生成式机制插画，不是模型实验结果。

**箭头核验未通过，不作为方法定稿：**

1. 右侧人体输出到候选场景汇合线仍有缺失。
2. Recorded views 到 Observation check 的路径存在方向/端点歧义。
3. shared memory 的 write 文字与对应箭头尚未完全对齐。

五次生成/局部修订保留了参考风格，但未稳定修正全部细线。先请用户确认视觉方向，下一步应在获准的制作方式中精确修正这些连接，不能把风格确认视为科学拓扑通过。

中间候选与指令已移至项目外 `pre-research/_archive/drivecompose/20261023-overview-redraw/reference-style-iterations/`。同时存在其他任务对论文的修改；本任务未覆盖或回退这些修改。
