# 与已发表综述的差距分析 & 最新 TODO 交接（Prism）

**日期：** 2026-07-14
**对标对象：** Zotero `survey` 收藏 5 篇（详见 `SURVEY_STRUCTURE.zh.md`）
**目的：** 复盘本稿相对 5 篇已发表综述的结构差距，固化已实现项，列出剩余 TODO 交接给 **Prism** 继续推进。

---

## 1. 对标对象

| # | 综述 | 载体 / 年 | 关键结构特征 |
|---|---|---|---|
| 1 | Personalized Image Generation: A Decade Survey | CVM 2025 | 统一框架 + **taxonomy 树图** + 增长时间线图 |
| 2 | Style Transfer Review (ML→DL) | MDPI 2025 | 时代演进弧线（前深度学习→深度学习） |
| 3 | Style Transfer: A Decade Survey | arXiv 2025 | **时间线图** + 6 表（含逐年总览表、逐范式变体表、评级矩阵、应用索引）+ 附录穷尽列表 |
| 4 | Image neural style transfer: A review | Elsevier 2023 | 前 CNN / CNN 二值时代划分 + 每法优缺点 |
| 5 | Advances in 3D Neural Stylization | IJCV 2025 | **Definition 1** + **实践指南小节** + 真实 benchmark + 应用小节 + 5 轴挑战 |

---

## 2. 差距矩阵（本稿 vs 5 篇最佳实践）

| 结构范式 | 5 篇最佳实践 | 本稿现状 | 状态 |
|---|---|---|---|
| 时间线图（2015–2025） | #1/#3 有 | `fig:pst_timeline`（已纳入，待目检） | ✅ 补齐 |
| 综述组织 taxonomy 树 | #1/#5 有 | `fig:pst_taxonomy`（TikZ 三轴） | ✅ 补齐 |
| 年份排序总览表 | #3 Table 1 | 缺（现有 `tab:method_overview` 未按年份） | ⬜ 待补 |
| 逐范式穷尽变体表 | #3 Table 3/4 (~55/~90) | 刻意不做（避免膨胀，内容已足） | ✅ 决策 |
| 应用域索引表 | #3 Table 7 (~127) | 可选（现有 Advanced Tasks 节覆盖） | ◐ 可选 |
| 多轴评级/基准表 | #3 Table 6 / #5 | `tab:comparison_matrix` + `tab:trilemma_paradigms` | ✅ |
| 形式化 Definition | #5 Definition 1 | `Definition 1 (PST)` | ✅ |
| 实践指南小节 | #5 §3.7 | `§Practical Guidelines: Lessons from a Decade` (G1–G7) | ✅ |
| 严格范式组织 | 全部 | NST/GAN/Diffusion/AR 四族 | ✅ |
| 数据集表 | #5 / #3 | `tab:datasets_pst` | ✅ |
| 附录穷尽方法列表 | #3 | `app:checklist` 说明 + 策展 BibTeX（未出全表） | ◐ 可选 |
| **真实视觉画廊** | 所有综述均有 | **缺（R1，用户推迟，转 Limitations）** | ⚠️ 最大剩余硬伤 |
| 统一框架/形式化透镜 | #1 / 本稿 | Portrait Editing Trilemma | ✅ 差异化 |

---

## 3. 本稿相对 5 篇的差异化优势（应保留并强调）

1. **人像专属聚焦**：以身份保持为硬约束，而非众多综述的"风格迁移之一例"。
2. **Portrait Editing Trilemma** 统一分析透镜，贯穿全文（定义→范式→评估→路线图）。
3. **Golden Protocol** 评估提案（多柱基准 + 统一协议倡议），是 5 篇均未提出的原创贡献。
4. **10 年经验实践指南**（G1–G7），以领域老手口吻给出可操作、带观点的指引。

---

## 4. 剩余差距（按优先级）

1. **真实风格化视觉画廊（R1）** — 最高优先但用户决定推迟；以 Golden Protocol（统一输入/协议重跑）留作未来工作。若补，接收概率显著提升。
2. **年份排序 PST 里程碑总览表** — 高价值、低成本，对标 #3 Table 1。
3. **`timeline.png` 人工目检 / 矢量重绘** — 内容需人工确认。
4. **Table IV 补具体方法示例**（可选）。
5. **应用域索引表 / 附录方法全表**（可选，避免过度膨胀）。
6. **引文时效性** — 持续纳入 2025–2026 前沿（已加 TeleStyle、StyleGallery 等）。

---

## 5. 最新 TODO 交接给 Prism

> Owner: **Prism** ｜ 交接人：current agent ｜ 状态基线：编译通过（undefined=0, A5=0）

- [ ] **P1** — 补"年份排序的 PST 里程碑总览表"（对标 #3 Table 1），置于 §Methods 或 §Introduction；引用 `tab:method_overview` 已有数据，重排为 Year / Method / Venue / Innovation 四列。
- [ ] **P1** — 人工目检 `images/timeline.png`；若节点/配色与正文里程碑不符，重绘为 TikZ 矢量时间线（参照 `fig:pst_taxonomy` 风格），替换位图。
- [ ] **P2** — 评估是否补"真实视觉画廊"（R1）：若决定做，按 Golden Protocol 统一输入+协议生成 Fig 1–3，并在 Limitations 中回收该声明。
- [ ] **P2** — （可选）Table IV (`tab:trilemma_paradigms`) 每行补 1–2 个代表方法，增强可落地性。
- [ ] **P3** — （可选）补"按任务域的方法索引"紧凑表 或 附录方法全表（~90 方法）。
- [ ] **P3** — 复核 Table I–IX 编号与正文引用一致性；运行 `refine-logs/audit.sh` 确认 A5=0。
- [ ] **P3** — 持续跟踪 2026 新预印本（arXiv/cs.CV），将重要方法并入对应范式小节与 `tab:method_overview`。

**交接说明：** 本稿结构已对齐 5 篇标杆综述的"图/表/定义/实践指南"范式；最大待决项为 R1 真实视觉画廊（用户已推迟）与年份总览表（低成本高价值）。所有新增图/表/定义/指南均已编译验证，详见 `STRUCTURE_PLAN.zh.md`、`TABLE_TODO.zh.md` 与提交历史（`daf4f9e`, `451cb0a` 及本次）。
