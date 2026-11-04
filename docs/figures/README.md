# 论文图件

全部正式图件统一放在 [`paper/fig/`](../../paper/fig/)，按论文图号使用 `figNN-英文短名`；同一图的 PPTX 与 PDF 使用相同文件名。

下表五份图件 PDF 是论文编译依赖，随源码纳入 Git；拉取后无需另行复制图件。可编辑 PPT、论文编译输出、历史素材和仓库外归档不随本次提交上传；这些文件不参与论文编译。当前编译结果 JSON 和哈希记录对应本机最终文件。

| 图号 | 内容 | PDF | 可编辑源稿 |
|---|---|---|---|
| 1 | 观测、联合补全与资产复用 teaser | [fig01-teaser.pdf](../../paper/fig/fig01-teaser.pdf) | [fig01-teaser.pptx](../../paper/fig/fig01-teaser.pptx) |
| 2 | 方法总览 | [fig02-overview.pdf](../../paper/fig/fig02-overview.pdf) | [fig02-overview.pptx](../../paper/fig/fig02-overview.pptx) |
| 3 | 联合补全机制 | [fig03-joint-completion.pdf](../../paper/fig/fig03-joint-completion.pdf) | [draw.io 源稿](../../../_archive/drivecompose/20261104-sync-collaborator/remote/docs/figures/joint-completion-vector/figure3-drawio.drawio) |
| 4 | 动态重建结果 | [fig04-dynamic-reconstruction.pdf](../../paper/fig/fig04-dynamic-reconstruction.pdf) | 未提供原生 PPT 源稿 |
| 5 | 轨迹外渲染结果 | [fig05-off-trajectory-rendering.pdf](../../paper/fig/fig05-off-trajectory-rendering.pdf) | 原件为 PDF，未提供 PPT 源稿 |

图 1、2 保留本机作者最后保存的 PPT，PPT 内容与文件哈希未变。图 1 PDF 为本机原生导出；图 2 PDF 采用同事本次同步的作者指定原件。原生文本、箭头和形状仍可编辑，场景子图保留为嵌入图片。图 1 的输入缩略图来自 Waymo，场景与资产面板为概念示意；图 2、3 为机制说明。图 4、5 保留原实验图内容。

图 3 采用同事本次同步的修正后矢量 PDF，原生可编辑 draw.io 源稿保存在同步归档中。图 4 的 PNG 无损封装为 PDF，未裁切、重绘或重采样，内嵌像素与原件一致。图 5 只改路径与名称，PDF 字节不变。

旧候选、分图素材、提示词、预览、构建脚本及历史快照移至[仓库外归档](../../../_archive/drivecompose/20261104-figure-cleanup/)。可重建的 `node_modules` 依赖路径不作为恢复原件。归档中 `files/` 保留原项目相对路径；`before/` 保存本轮修改前的说明、源码与主稿 PDF。

当前文件哈希与旧路径见[图件布局记录](../../paper/provenance/figure-layout.json)，逐文件归档及核验见[归档清单](../../../_archive/drivecompose/20261104-figure-cleanup/archive-manifest.json)，本轮修改理由见[改动对照](../paper-revision-changes.md)。后续修改直接更新同名最终文件；临时输出放在仓库外，避免在图目录积累日期版或预览副本。
