# 边界声明 (BOUNDARIES) — 人像风格迁移综述

> 目的:明确"论文是什么 / 不声称什么 / 收什么方法",作为一切修改的**硬边界**。越界的修改一律回退。

## 1. 论文本质
- 这是一篇 **survey(综述)**,不是方法论文。
- 核心贡献(之一)是 **Trilemma 分析框架**(Identity Preservation / Editing Fidelity / Inference Speed)用作统一透镜 + **Golden Protocol** 评估提案。
- 时间窗:**2015–2025** 人像风格迁移(PST)。

## 2. 明确声称 (In-Scope Claims)
- 我们**覆盖**优化式(NST)/前馈/GAN/扩散/自回归/Flow/3D-NeRF 多范式的 PST 方法。
- 我们**提出** Trilemma 作为分析透镜(若坚持原创须明写 "We coin";否则删误导引文 — 见 R25)。
- 我们**提议** Golden Protocol(若未执行须降级为 "Proposed Guideline" — 见 R35)。

## 3. 明确不声称 (Out-of-Scope / Forbidden Claims) ⛔
- ⛔ 不声称提出新模型/新方法(这是综述)。
- ⛔ 不声称 Trilemma 已被前人形式化(4 篇脚注引文均不支持 → 必须原创声明或删除)。
- ⛔ 不声称已完成 Golden Protocol 的基准评测(除非真跑)。
- ⛔ 不声称覆盖**通用**风格迁移(非人像 NST 仅作背景基线引用,不重复其综述)。
- ⛔ 不在"peer-reviewed 计数"中混入 arXiv 预印本(R27)。
- ⛔ 不出现**无法溯源的量化数字**(ArtFID 等必须有原表出处,R26)。

## 4. 方法纳入/排除决策规则 (Inclusion Rule)
纳入一个方法,当且仅当:
1. **人像相关**:针对人像,或在其原论文中以人像为主要演示;且
2. **在窗内**:发表于/预印于 2015–2025,或为奠基性 seminal(如 AdaIN、StyleGAN);且
3. **范式相关**:落入本文某一范式分类。

排除:
- 纯通用 NST(无肖像专用贡献)→ 仅背景引用。
- 非风格迁移的人像生成(如单纯人脸生成、ID 识别)→ 不纳入。
- 与本文范式无关的通用扩散/AR 生成综述内容 → 不纳入。

## 5. 修改纪律 (Edit Discipline)
- 任何修改不得破坏 `main.tex` 可编译(改完必跑 `latexmk -pdf` 或等价)。
- 任何新增引文必须同步 `references.bib` 且通过 A1/A5。
- 任何新增数字必须附可溯源 `\cite`(A2)。
- 删内容须确认非唯一支撑某 claim,否则补替代。
- 跨 3+ reviewer 共识项(R1/R3/R5/R7)为最高优先级,不得搁置。

## 6. 收敛判据 (Convergence Gate — 见 ITERATION_PLAN.md)
- 投稿前必须满足:**0 个 F 级规则违反 + 0 个 M 级未决 + 所有 m 级已建 TODO 跟踪**。
- 任一 F 级违反 = 禁止投稿。
