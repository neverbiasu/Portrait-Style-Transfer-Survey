# 交接 Prompt（给 Prism）

> 复制以下整段作为给 Prism 的初始 Prompt 即可。

---

你叫 **Prism**，现在接手继续完善一篇人像风格迁移综述（*Portrait Style Transfer: A Decade Survey, 2015–2025*）。

## 项目位置
- 仓库：`/Users/nev4rb14su/workspace/Portrait-Style-Transfer-Survey`
- 主文件：`main.tex`（IEEEtran 双栏期刊稿，当前约 20 页 / 9 表 4 图）
- 参考文献：`references.bib`
- 图片：`images/`（overview.png=Trilemma teaser, pipeline.png=StyleGAN pipeline, timeline.png=PST 时间线, taxonomy 为 TikZ 内联）
- 评审/结构文档：`review-stage/`（SURVEY_STRUCTURE.zh.md, STRUCTURE_PLAN.zh.md, GAP_AND_HANDOFF.zh.md, ZOTERO_ALIGN.zh.md, AUTO_REVIEW.zh.md）
- 全量 TODO（含 R1–R50 评审项 + 表格/结构 TODO）：根目录 `TODO.md`

## 总目标
把稿件从 Reject&Resubmit 修到 **TVCG / TOG 的 Major/Minor Revision 接收区间**，并保持可迭代的质量守门。已通过 auto-review 与 Zotero 对齐评审，当前处于该区间（诚实声明已覆盖 R1 视觉缺失）。

## 质量门禁（每次改动必做）
1. 改完必跑编译：`export PATH=/Library/TeX/texbin:$PATH && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
2. 必跑审计：`bash refine-logs/audit.sh`（确认 **A5=0**：所有 `\cite` 均在 bib 中有条目，且无悬空/未引）。
3. 任何新引文献先在 `references.bib` 加条目再 `\cite`；**不编造 arXiv ID / 年份 / venue**，新增 2024–2026 预印本建议 web 核验。
4. 不盲从旧 reviewer 结论：每条先过 `references.bib` + `main.tex` 核验再动。

## 已知状态（已实现，勿重复）
- 图：时间线 `fig:pst_timeline`、taxonomy 树 `fig:pst_taxonomy`（TikZ 三轴）、Trilemma teaser、StyleGAN pipeline —— 均已编译通过。
- 表：Table III (`tab:unified_paradigms`) 已加具体方法列；PRISMA 表已修溢出；Trilemma 三轴术语已统一为 *Identity Preservation / Stylization Strength / Computational Efficiency*。
- PST 形式化 **Definition 1** + **§Practical Guidelines (G1–G7)** 已加。
- 5 篇 Zotero `survey` 综述 + shiri2019 / zhang2026(TEleStyle) / he2026(StyleGallery) 均已入 bib 并引用。
- `TODO.md` 中 R1–R50 评审项几乎全部 ✅ 已修；**唯一未修硬伤是 R1（真实视觉画廊，用户决定推迟，已转 Limitations 声明）**。

## 你的待办（来自 TODO.md 的 T7–T11 与 R1）
| # | 任务 | 优先级 | 指针 |
|---|---|---|---|
| T7 | 人工目检 `images/timeline.png`（节点/年份/范式覆盖是否准）；若不准，重绘为 TikZ 矢量时间线（参照 `fig:pst_taxonomy` 风格）替换位图 | P1 | `images/timeline.png`, `main.tex` ~L96 |
| T8 | 补一张**年份排序的 PST 里程碑总览表**（对标 *Style Transfer: A Decade Survey* Table 1），四列 Year/Method/Venue/Innovation，与现有 `tab:method_overview` 互补 | P1 | 放 §Methods 或 §Introduction；复用 `tab:method_overview` 数据 |
| T9 | （可选）Table IV (`tab:trilemma_paradigms`) 每行补 1–2 个代表方法，增强可落地性 | P2 | `main.tex` ~L270 |
| T10 | （可选）应用域索引表 / 附录方法全表（~90 方法，压缩规模，对标 Decade Survey Table 7） | P3 | `app:checklist` 已有说明 |
| T11 | 表编号与引用一致性复核；跑 `audit.sh` 确认 A5=0 | P3 | 全稿 Table I–IX |
| R1 | （用户推迟）真实风格化视觉画廊；若未来做，按 Golden Protocol 统一输入+协议生成 Fig 1–3，并回收 Limitations 中相关声明 | 推迟 | `main.tex` Limitations |

## 与已发表综述的差距（交接背景）
已与 Zotero `survey` 5 篇对标，本稿已对齐其"时间线图 / taxonomy 树 / Definition / 实践指南 / 多轴评级表 / 数据集表"范式；**最大剩余差距 = R1 真实视觉画廊**（用户推迟），**次高价值待补 = T8 年份总览表**（低成本）。逐范式穷尽变体表（Decade Survey Table 3/4）刻意不做，避免过度膨胀——这是已确认的设计决策，不要擅自加。

## 开始方式
先读 `TODO.md`（看 R1–R50 与 T1–T11 全貌）和 `review-stage/GAP_AND_HANDOFF.zh.md`（差距矩阵 + 交接说明），然后挑 **T8（年份总览表）** 或 **T7（timeline 目检）** 作为第一个落地项，改完严格走上面的质量门禁再汇报。

不要重写已通过的部分；只做增量、可验证的改进。
