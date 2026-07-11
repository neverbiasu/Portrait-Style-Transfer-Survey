# Kill Argument Report — Portrait Style Transfer: A Decade Survey (2015–2025)

**日期**: 2026-07-10
**评审方式**: 模拟执行（Codex MCP 不可用，Agent 直接读取源码按 kill-argument 方法论完成）
**结论**: **WARN** — ≥2 个 `partially_answered` 级别为 major，0 个 `still_unresolved` 致命

> ⚠️ 注：本 session 已补入 4 篇缺失论文（InterFaceGAN / pSp/e4e / FRESCO / MangaGAN）。以下攻击备忘录基于补前状态，裁决基于当前源码。

## 1. 总体评估

| 指标 | 评价 |
|------|------|
| 论文水准 | TVCG 级别，结构扎实。**无致命缺陷** |
| 亮点 | "Portrait Editing Trilemma" 框架有实用价值，Limitations 部分诚实 |
| 核心风险 | abstract 的 "comprehensive, mechanism-based taxonomy" 主张被两点削弱 |

| 风险 | 严重程度 |
|------|----------|
| abstract "five paradigms" vs body "four families" 分类法不一致 | major（visible inconsistency） |
| 覆盖完整性依赖单一 curated notebook（cross-check 即发现缺口） | major |
| GANs vs Diffusion "Structure Masters / Texture Masters" 二分法过度简化 | major |

## 2. 攻击备忘录（原文，~170 词，模拟）

This survey's headline contribution—a comprehensive, mechanism-based taxonomy of a decade of portrait style transfer—does not survive contact with its own text. The abstract advertises coverage across "five paradigms: Optimization, Feed-Forward Networks, GANs, Diffusion Models, and 3D/NeRF systems," yet the body organizes the entire Methods section into only "four foundational method families" (NST, GANs, Diffusion, AR), demoting 3D/NeRF and Optimization to footnotes and silently introducing AR as a fifth family the abstract never names. The taxonomy is therefore not the clean five-way map the title sells. Worse, the "comprehensive" claim is belied by the corpus itself: the authors' own managed literature (a single curated notebook) omitted foundational PST works—InterFaceGAN (GAN disentanglement), pSp/e4e (StyleGAN inversion), and FRESCO (video)—that any competent survey must cover, a gap exposed by a trivial cross-check. A taxonomy assembled from one author's reading list, then mismatched between abstract and body, cannot anchor a "comprehensive" survey; the contribution collapses to a competent but partial opinion piece.

## 3. 逐点裁决

| # | 攻击点 | 裁决 | 严重程度 | 证据 |
|---|--------|------|----------|------|
| P_1 | abstract "five paradigms" vs body "four families" taxonomy 不一致 | partially_answered | major | Abstract L17,L23 列 five paradigms；§3 L199 写 "four foundational method families: NST, GANs, Diffusion, AR"；3D/NeRF 仅在 Advanced Tasks §3D（L311）以前沿出现；Optimization 归入 NST §3.1 |
| P_2 | "comprehensive" survey 遗漏 InterFaceGAN / pSp/e4e / FRESCO 等奠基工作 | answered_by_current_text（本 session 已修复） | critical（原级） | 当前 `references.bib` 已含 4 条，已在对应段落 `\cite` |
| P_3 | "Structure Masters"(GANs) = identity / "Texture Masters"(Diffusion) = diversity 二分法过度简化 | partially_answered | major | Abstract L23 + Conclusion L517 推 clean dichotomy；但 §3.3 L255-257 承认 diffusion "re-introduced identity loss challenges"，§3.2 L238 指出 GAN domain lock-in |
| P_4 | "Golden Protocol" 是 recommendation 而非 executed benchmark | partially_answered | minor | §5 L197 明确 "do not provide a single merged score table"；Limitations L565 承认 heterogeneity。但对综述可接受 |
| P_5 | 检索偏差 — corpus = 单一 curated notebook，非 field-wide systematic | partially_answered | major | 检索方法 L60 写了 venue/keywords，但实际 corpus 是 NotebookLM #7（151 源，27 篇非论文）。"over 115 publications"（abstract）vs "~90 distinct methods"（L55）vs 151 managed sources 三个数字不一致 |

### 3.1 若 unresolved 的修复建议

| # | 建议修复 |
|---|----------|
| P_1 | 统一措辞：abstract 改为 "four core families + emerging frontiers (3D/NeRF, video, AR)"，或 body 改名匹配 |
| P_3 | 软化： "GANs historically prioritized identity-bound structure; diffusion prioritized open-vocabulary diversity — with modern hybrids blurring the boundary"，并 inline cite identity-focused diffusion（IP-Adapter, InstantID）|
| P_4 | Contribution #3 从 "Proposing a Golden Protocol" → "Proposing (and calling for adoption of) a Golden Protocol" |
| P_5 | 显式声明 coverage scope；统一 115 / 90 / 151 三个数字 |

## 4. 总结

| 指标 | 数值 |
|------|------|
| 总攻击点 | 5 |
| answered_by_current_text | 1（P_2，已修复） |
| partially_answered | 4（P_1, P_3, P_4, P_5） |
| still_unresolved | 0 |

## 5. 行动项（按优先级）

1. **统一分类法措辞**: abstract "five paradigms" → "four core + frontiers" ——P_1，最显眼
2. **软化 "comprehensive / Structure-vs-Texture Masters" 措辞**: 补充 diffusion identity preservation caveat——P_3, P_5
3. **统一覆盖数字**: 115 / 90 / 151 → 一个数字——P_5
4. **Golden Protocol 措辞微调**: 避免 overclaim——P_4
