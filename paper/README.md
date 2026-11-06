# DriveCompose 双语论文工程

固定题名：**DriveCompose: Compositional Generative Reconstruction of Driving Scenes via Joint Completion**。

## 文件入口

| 材料 | 英文入口 | 中文入口 |
|---|---|---|
| 主稿 | `main.tex`、`sec/` | `main_zh.tex`、`zh/` |
| 补充材料 | `supplementary/main.tex` | `supplementary/main_zh.tex` |

主稿共用 `main.bib`，补充材料使用 `supplementary/references.bib`。已采用图件及必要素材见[图件说明](../docs/figures/README.md)；作者原始数据和后续确认见[数据说明](data/README.md)与[证据位置](EVIDENCE.md)。协作与提交规则以根目录 [AGENTS.md](../AGENTS.md) 为准。

## 编译

使用已有 Tectonic 运行时，在仓库根目录执行：

```powershell
python -B paper/tools/build.py --material all
```

`--language en` 或 `--language zh` 选择语言；`--material main` 或 `--material supplementary` 选择材料。默认编译目录位于仓库外；`--out-root` 可指定另一个仓库外目录。编译日志、辅助文件和结果 JSON 仅写入该目录。成功后只复制正式 PDF；`--no-install` 用于只编译候选。

使用 XeLaTeX／latexmk 时，从主稿或补充项目目录构建，把 `-outdir` 指向仓库外目录；检查页面后只复制正式 PDF 到下列约定位置。正文、样式、书目与正式图件均包含在工程中。

## 正式成品

- [英文主稿](build/en/main.pdf)
- [中文主稿](build/zh/main_zh.pdf)
- [英文补充材料](build/supp-en/main.pdf)
- [中文补充材料](build/supp-zh/main_zh.pdf)

`build/` 仅保留这四份成品。重新生成后核对完整结论所在页、全部图表、引用、缺字、裁切与重叠；标题页或总页数不能代替正文终止位置。

## 提交前检查

```powershell
python -B paper/tools/check_manuscript.py --staged
```

该工具检查当前依赖、书目与交叉引用、双语方法公式、作者输入及当前 SSIM 确认，同时检查工作区和 Git 暂存区。报告默认保存在仓库外；它不代替实验复现、统计核验或 PDF 视觉检查。

图 6 可从六张结果原图重建：在 `paper/` 下执行 `python -B tools/make_component_ablation.py`。预览和生成清单通过参数写到仓库外。
