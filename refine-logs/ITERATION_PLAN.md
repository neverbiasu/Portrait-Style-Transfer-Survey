# 迭代计划 (ITERATION_PLAN) — 让 review 收敛而非反复

> 核心思想:每次 review 发现的**新 issue 类别**,必须回填为 `RULES.md` 的新规则(规则只增不减)。
> 这样 paper 的质量边界随每次 review **单调提升**,而不是每次从零被打回。

## 循环 (per review round)

```
 round_start
      │
      ├─ 1. 跑 audit.sh ──────────────► 机械违反清单(A1/A5/A6/D3/…)
      │        │
      │        ├─ 有 F 级违反? ── YES ─► 禁止投稿,先修
      │        │
      │        └─ NO
      │
      ├─ 2. 人工过 RULES.md (A2/A3/A4/B2/B3/C1/C3/D1/D2/E2/E3…)
      │
      ├─ 3. 收新 review → 逐条核验(用 bib/tex 证伪幻觉,如 Rev3/4 的 Table III/StyleAligned)
      │        │
      │        └─ 每条新 issue 类别 ─► 回填 RULES.md 新规则 + 写 Changelog
      │
      ├─ 4. 映射到 TODO.md(续号),按 F>M>m 修
      │
      └─ 5. 收敛判据检查
```

## 收敛判据 (Convergence Gate)
投稿/返修提交前必须满足:
- **F 级**:0 违反(否则 desk-reject 风险,尤其编造引文/数字)。
- **M 级**:0 未决(全部 fixed 或 documented-with-rationale)。
- **m 级**:全部已进 TODO 跟踪,有 owner/ETA。
- 新 review 的 **共识项(≥3 reviewer 提)** 自动升最高优先级。

## 角色分工(建议)
- **作者(你)**:执行修改、跑 audit.sh、回填规则。
- **外部 review(人/NotebookLM/多模型)**:每轮独立挑刺 → 喂给步骤 3。
- **规则集**:唯一的"质量真理源",不随情绪/单轮意见漂移。

## 与现有工件的衔接
- `REVIEW_SUMMARY.md`(根目录):4-review 矩阵,作为 RULES v1.0 的种子。
- `TODO.md`:R1–R50,每条对应一条规则违反。
- `refine-logs/RULES.md`:通用规则(只增不减)。
- `refine-logs/BOUNDARIES.md`:硬边界,越界修改回退。
- `refine-logs/audit.sh`:机械守门员,投稿前必跑。

## 首次演示(本轮)
1. 已建 RULES/BOUNDARIES/audit.sh。
2. 下一步:跑 `audit.sh --all`,把剩余机械违反(如 D3 重复句、A5 未引 bib)直接修掉或入 TODO。
3. 人工过 A2/A3 致命项(R25–R27)→ 这是当前阻断点。
