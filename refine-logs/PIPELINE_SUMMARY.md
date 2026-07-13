# Pipeline Summary

**Problem**: 每次 review 都打出一大堆同类问题,paper 不收敛。根因 = 没有"质量边界 + 可复用规则 + 迭代回路"。
**Final Method Thesis**: 不重写 paper,而是建一套**只增不减的规则集(RULES)+ 硬边界(BOUNDARIES)+ 自动守门(audit.sh)+ 迭代回路(ITERATION_PLAN)**,把每轮 review 的新 issue 类别回填为规则,使质量随轮次单调提升。
**Final Verdict**: READY (as a process) / paper still REVISE
**Date**: 2026-07-13

## Deliverables (refine-logs/)
- Rules: `refine-logs/RULES.md` (A1–E5, 每条带 WHY+机械 CHECK)
- Boundaries: `refine-logs/BOUNDARIES.md` (in-scope / forbidden / inclusion-rule / convergence-gate)
- Iteration plan: `refine-logs/ITERATION_PLAN.md` (per-round loop + 收敛判据)
- Auditor: `refine-logs/audit.sh` (POSIX/macOS, 跑全部或单规则)
- Review source: `REVIEW_SUMMARY.md` (根目录, 4-review 矩阵 → RULES v1.0 种子)

## Contribution Snapshot
- Dominant contribution: **可迭代的质量守门系统**(规则只增不减 + 机械审计)
- Optional supporting: BOUNDARIES 收敛判据(0 F / 0 M 未决)
- Explicitly rejected complexity: 不为 survey 编造实验;不盲目接纳 reviewer 幻觉(已证伪 R3/R4 共 3 条)

## First Audit Run (已演示, `audit.sh --all`)
| 规则 | 结果 | 对应 TODO |
|------|------|-----------|
| A1 cite 解析 | OK | — |
| A5 未引 bib | 10 条 | R29 |
| A6 "and others" | 15 处 | R38 |
| A7/B1 预印本 | 28 条(`peer-reviewed` est≈105 ≠ "115+") | R27 |
| B3 绝对词 | unbiased(L276)/SOTA(L206)/optimal/perfect/state-of-the-art | R36,R42 |
| **C3 覆盖** | **PhotoMaker/PULID/… 14 项全 0 hits** | **R28(最大缺口)** |
| E4 可用性声明 | hits=2 (边界通过) | R47 |
| D3 重复行 | 仅捕获注释分隔行(需 refinement,见下) | R48 待人工确认 |

## Main Risks
- Risk: 规则本身有误报(如 D3 捕获注释行、C2 用错术语 "Flow Mapping" vs 正文 "Flow Matching") → Mitigation: 每轮 refinement audit.sh,把误报模式修进脚本。
- Risk: 机械审计查不出 A2/A3(数字溯源、概念引文) → Mitigation: 致命项仍须人工逐条核验(这正是 R25–R27 阻断点)。
- Risk: 规则只增不减导致膨胀 → Mitigation: 合并同类,Changelog 记录。

## Next Action
1. 修 audit.sh 误报(D3 排除注释/C2 用正文术语)。
2. 人工过 A2/A3 致命三项 → R25/R26/R27(当前阻断投稿)。
3. 用 C3 结果驱动 R28:补 14 篇 2024-25 SOTA 进正文。
4. 每收到新 review,先核验(证伪幻觉)→ 回填 RULES 新规则 → 重跑 audit → 收敛。
