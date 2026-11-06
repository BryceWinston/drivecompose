# 作者数据与协议

这里保存支撑论文的长期作者输入，不包含审稿报告、逐轮核验或执行日志。材料属于作者提供的汇总数据；独立原始运行日志核验和新增实验须另有实际证据。

| 文件 | 内容 |
|---|---|
| `author-results.txt` / `author-results.json` | 完整作者文本及结构化结果、条件和后续确认；JSON 中的原文哈希对应同目录文本 |
| `author-ssim-confirmation.json` | Table 1 的最新全图 SSIM 确认及 S11 的方法级汇总口径 |
| `author-baseline-input.json` | 作者填写的基线数值及确认状态 |
| `ablation-results.json` | 组件消融、输入数量敏感性的条件、原始表格和已报告差值 |
| `author-method-config.json` | 作者提供的方法、训练、空间支撑、比较及几何评价配置 |
| `author-protocols.txt` | 统一数据规模、输入、评价与编辑条件 |
| `author-supplement.txt` | 作者补充的复现配置和结果解释 |
| `author-initial-results.txt` / `author-clarifications.txt` | 较早的原始作者输入与澄清，用于保留来源和协议条件 |

结构化结果中的原始表格保持作者输入；后续确认具有更高优先级。当前 Table 1 的全图 SSIM 采用 `author-ssim-confirmation.json` 的 `after` 值：STORM 0.782、DGGT 0.875、StreetForward 0.819、Ours 0.903。S11 只将这四个值作为方法级全图 SSIM 汇总，不将其反推为插值／外推组的新结果。

较早输入不得覆盖后续确认；具体科学主张和当前展示位置见 [EVIDENCE.md](../EVIDENCE.md)，最终呈现以中英文主稿和补充材料为准。
