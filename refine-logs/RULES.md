# 审核规则集 (RULES) — 人像风格迁移综述

> 目的:将历次 review 的 50+ 散点问题,提炼为**可复用的不变量规则**,使未来 review 不再反复踩同类坑。
> 用法:每次投稿/返修前跑 `audit.sh` + 人工过本表;新发现的 issue 类别**必须**回填为新规则(规则只增不减 = 逐渐迭代)。
> 严重度:F=致命(阻断投稿) M=主要(major revision 范围) m=次要。

## A. 引文完整性 (Citation Integrity)

- **A1 [F]** 正文中每个 `\cite{key}` 必须在 `references.bib` 存在对应条目。
  - WHY: 编造/缺失条目是最易被 desk-reject 的硬伤。
  - CHECK: `audit.sh --cite-keys`
- **A2 [F]** 正文每个**量化/指标数字**(ArtFID、FID、LPIPS、MS-SSIM、步数、ms…)若带 `\cite`,必须能在所引论文的**具体表/图 + 明确实验条件**中溯源;无法溯源即视为编造。
  - WHY: R26 — AdaIN 31.85(StyleInV)、InstantStyle 42.48 / StyleID 38.57 错引视频论文,均为查无。
  - CHECK: 人工逐条核对(无自动),`audit.sh --numbers` 仅列出所有"数字+\cite"位置供人工验。
- **A3 [F]** 用引文**支撑一个概念性论断**(如"框架""分类法""Trilemma/Impossible Triangle")时,所引论文必须**确实讨论该概念**。
  - WHY: R25 — Trilemma 脚注 4 篇(wang2024instantstyle 等)无一讨论三角困境,属引文灌水。
  - CHECK: 人工读所引 abstract。
- **A4 [F]** 一个方法的指标**不得**引自另一篇方法的论文。
  - WHY: R26 — StyleID 的 ArtFID 被挂到 StyleMaster(视频论文),且 bib 无 StyleID 独立条目。
  - CHECK: 人工确认方法名与引用论文匹配。
- **A5 [M]** `references.bib` 中**不得有未正文引用的条目**(引而不用)。
  - WHY: R29 — 10 条未被引用(artflow/jojogan/MUNIT/NeRF-Art 等)。
  - CHECK: `audit.sh --unused-bib`
- **A6 [m]** 作者字段不得写 "and others";TVCG/TOG 要求列全至第 6 位 + et al.
  - WHY: R38。
  - CHECK: `audit.sh --and-others`
- **A7 [M]** 预印本(arXiv 等)必须在 bib 与正文**明确标注 preprint**,且**不计入** peer-reviewed 统计。
  - WHY: R27/R30 — 28 篇 arXiv 预印本被算进 "115+ peer-reviewed"。
  - CHECK: `audit.sh --preprint-label`

## B. 事实与统计 (Factual & Statistical Integrity)

- **B1 [F]** peer-reviewed 计数**必须扣除** arXiv 预印本;建议分层报告(peer-reviewed + screened preprints = total)。
  - WHY: R27。
  - CHECK: `audit.sh --count` 输出 bib 中 preprint 数供手算核对。
- **B2 [M]** 数据集表(Table VI)每行**许可协议 + 引用来源**必须与官方一致(FFHQ 非 CC BY-NC-SA;Danbooru 非 BSD;WikiArt 区分 Saleh2015/Nichol2016;AAHQ 需补条目)。
  - WHY: R34。
  - CHECK: 人工核对每行。
- **B3 [m]** 禁用无条件的绝对化形容词:"unbiased""theoretically optimal""SOTA""state-of-the-art" 须附证据或 caveat。
  - WHY: R36(NST "theoretically unbiased" 假)、R42("SOTA" 偏见)。
  - CHECK: `audit.sh --absolutes` 列出候选词。
- **B4 [m]** 年代一致性:方法不得被引为早于其真实发表年;未来会议录用(如 ICLR2026)须标 "to appear"/preprint。
  - WHY: FlowAlign "ICLR2026"、FlowEdit "ICCV2025" 时间倒置。
  - CHECK: 人工核对。
- **B5 [M]** 摘要中的数字(publications / methods / sources)必须与正文口径**可调和**,并各自注明 scope。
  - WHY: R24/R27。
  - CHECK: 人工。

## C. 覆盖与分类 (Coverage & Taxonomy)

- **C1 [M]** 分类词汇在 abstract / intro / body **全文一致**(一套范式名)。
  - WHY: 旧 #4(五范式 vs 四族)。
  - CHECK: 人工。
- **C2 [M]** 每个在正文引入的范式(含 Flow Matching)必须同时出现在**统一框架表 + 能力矩阵**;不得有孤儿概念。
  - WHY: R33(Flow Matching 排除于 III/IV)。
  - CHECK: `audit.sh --orphan-paradigm`
- **C3 [M]** 综述须覆盖其自身时间窗(2015-2025)内**每范式近 24 个月的代表 SOTA**:至少含 PhotoMaker/PULID/LivePortrait/ConsistentID/MagicAnimate/AnimateAnyone/AnimateDiff/GaussianHair/3DGS-Avatar/DragGAN/Barbershop。
  - WHY: R28。
  - CHECK: `audit.sh --coverage` 列出必含方法名命中情况。
- **C4 [m]** 分类轴须正交可比;不得把"算法/损失"(NST)与"架构"(GAN/Diff/AR)并列混层。
  - WHY: R39。
  - CHECK: 人工。

## D. 结构与方法 (Structure & Methodology)

- **D1 [M]** 任何自称"contribution"的协议/框架(如 Golden Protocol)**必须被执行**,否则降级为 "Proposed Guideline"/"future work"。
  - WHY: R35。
  - CHECK: 人工。
- **D2 [M]** 声称 PRISMA/文献筛选,必须有真实漏斗(数据库 + 检索式 + 日期 + 纳排标准)。
  - WHY: R30(漏斗仅 3 行)。
  - CHECK: 人工。
- **D3 [m]** 正文不得有**逐字重复**的句子/段落。
  - WHY: R48(OmniStyle-1M 整句重复两次)。
  - CHECK: `audit.sh --dup-lines`
- **D4 [m]** 核心框架(Trilemma)必须作为**分析透镜**在方法各章复用,而非仅陈述一次。
  - WHY: 旧 m11。
  - CHECK: 人工。

## E. 呈现与伦理 (Presentation & Ethics)

- **E1 [m]** 表格须有单位/脚注/来源;速度数字须标注硬件(GPU/显存)。
  - WHY: R40/R19/R41(VToonify "RT" 混乱)。
  - CHECK: 人工。
- **E2 [m]** 伦理段须**直接关联**本综述主题,不得是通用法律复述(EU AI Act/GDPR 堆砌)。
  - WHY: R43。
  - CHECK: 人工。
- **E3 [m]** 须在 related work 明确**本综述与已有/同期综述的差异**(Fan TVCG24、Garcia CGF24、Zhang2025 decade survey 等)。
  - WHY: R45。
  - CHECK: 人工。
- **E4 [m]** 须有 Code/Data Availability 声明。
  - WHY: R47。
  - CHECK: `audit.sh --availability`
- **E5 [m]** 须有正式 Appendix(PRISMA 图 / 完整方法清单 / benchmark 代码)。
  - WHY: R46。
  - CHECK: 人工。

## 规则变更日志 (Changelog — 只增不减)
- 2026-07-13 v1.0:由 4-review 矩阵(28 去重项)初始化 A1–E5。
