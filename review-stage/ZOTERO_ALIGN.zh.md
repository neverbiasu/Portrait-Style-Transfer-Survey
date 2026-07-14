# Zotero `survey` 收藏 — 引文对齐报告

**日期：** 2026-07-14
**评审人：** 当前模型（本环境未配置 Codex/gemini MCP；以 Zotero 作为事实来源）
**评审方法：** 以 Zotero 为基准的引文审计。将本地 Zotero 库（`~/Zotero/zotero.sqlite`，通过在线备份恢复）中的 `survey` 收藏视为权威参考集，提取其 5 条条目的规范元数据（作者、年份、载体、卷/页、DOI），并与 `references.bib` + `main.tex` 做差异比对。

## Zotero `survey` 收藏（collectionID=24）— 5 条

| # | Zotero 标题 | 规范作者（Zotero） | 载体 / 年份 | DOI |
|---|---|---|---|---|
| 1 | Personalized Image Generation with Deep Generative Models: A Decade Survey | Y. Zhang, Y. Wei, Z. Ji, W. Zuo, L. Zhang, Y. Zheng, M. Liu | Comput. Visual Media 11:1141–1194, 2025 | 10.26599/CVM.2025.9450495 |
| 2 | Style Transfer Review: Traditional Machine Learning to Deep Learning | Y. Xu, M. Xia, K. Hu, S. Zhou, L. Weng | Information 16(2):157, 2025 | 10.3390/info16020157 |
| 3 | Style Transfer: A Decade Survey | T. Zhang, H. Tang | arXiv:2506.19278, 2025 | 10.48550/arXiv.2506.19278 |
| 4 | Image neural style transfer: A review | Q. Cai, M. Ma, C. Wang, H. Li | Comput. Electr. Eng. 108:108723, 2023 | 10.1016/j.compeleceng.2023.108723 |
| 5 | Advances in 3D Neural Stylization: A Survey | Y. Chen, G. Shao, K. C. Shum, B.-S. Hua, S.-K. Yeung | IJCV 133:5026–5061, 2025 | 10.1007/s11263-025-02403-9 |

## 发现（与稿件比对）

| Zotero 条目 | 在 `references.bib`？ | 在 `main.tex` 引用？ | 已采取行动 |
|---|---|---|---|
| 1 Personalized Image Gen. Decade Survey | **缺失** | **缺失** | 新增 `zhang2025personalized`；在方法论段落引用 |
| 2 Style Transfer Review (ML→DL) | **缺失** | **缺失** | 新增 `xu2025stylereview`；在方法论段落引用 |
| 3 Style Transfer: A Decade Survey | **缺失**（R2 缺口） | **缺失** | 新增 `zhang2025decadesurvey`；在方法论段落引用 |
| 4 Image neural style transfer: A review | **缺失**（我们原有 *另一篇* NST 综述：`jing2020neural`） | **缺失** | 新增 `cai2023imagestyle`；在 NST 小节引用 |
| 5 Advances in 3D Neural Stylization | **缺失** | **缺失** | 新增 `chen20253dstylization`；在 3D 感知小节引用 |

**对齐过程中发现的其他规范缺陷：**
- 方法论段落中的载体拼写错误：`ECCCV (5)` → 修正为 `ECCV (5)`。
  （`ECCCV` 并非真实载体；同段前文正确使用了 `ECCV`。）

## 备注 / 非问题项
- 我们原有的 `jing2020neural`（"Neural Style Transfer: A Review"，Jing 等，IEEE TVCG 2020）与 Zotero 第 4 篇是 **确实不同的论文**；两篇现均已引用，原样保留。
- 这些条目在 Zotero 中未固定 BBT 引文键，故以标题/DOI 做匹配。
- `survey` 收藏仅含 5 条。Zotero 中还存在其他明显相关的收藏（如 `portrait_stylization` = 53 条、`new_buds` = 28+6、`diffusion` = 18、`ref` = 19），但按本次要求的 `survey` 目录范围，不在本对齐轮次内。

## 结果
- 5 条规范综述条目已加入 `references.bib`，元数据经 Zotero 核验。
- 向 `main.tex` 新增 4 处定位引用（方法论 ×3、NST ×1、3D ×1）。
- 修正 1 处载体拼写错误。
- 编译干净（pdflatex+bibtex）；未定义引用 = 0；A5（已引但未入 bib）= 0。
- 结论：稿件现已对齐 Zotero `survey` 收藏的参考规范。
