# 论文书目维护

英文与中文主稿共用 [main.bib](main.bib)，补充材料使用 [references.bib](supplementary/references.bib)。同一工作使用稳定的引用键；补充书目仅保留实际引用的条目。

新增或更正文献时核对原文、作者顺序、题名、年份、版本、会议和页码；使用作者公开页面、正式录用论文与会议页面等原始来源。预印本的引用不等于已确认正式发表。

JRM 的 `wu2026jrm` 使用 [CVPR 2026 正式记录](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_JRM_Joint_Reconstruction_Model_for_Multiple_Objects_without_Alignment_CVPR_2026_paper.html)。机制比较中应区分引用工作的原生机制与本任务的适配对照，避免把适配结果写成原论文直接实验。

作者提供的[参考文献资料](../docs/DriveCompose_75篇顶会参考文献.docx)属于长期输入。正文的实际引用集合以当前书目与源文为准，不用较早接入数量代替当前条目统计。

提交前使用 `python -B paper/tools/check_manuscript.py --staged` 核对重复引用键、未定义引用及当前资源；逐条检索、下载与核验过程保存在仓库外。
