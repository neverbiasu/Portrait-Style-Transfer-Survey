# Skill 适用性分析 — 「Research Review via Codex MCP」

> 目标：用该 skill 评审当前论文 *Portrait Style Transfer: A Decade Survey*（TVCG 综述）
> 结论：**不能直接使用**。原因分「环境/工具链不满足」与「内容模板错位」两类。

## 1. 环境 / 工具链硬伤

| 必要条件 | 当前环境 | 结论 |
|----------|----------|------|
| `mcp__codex__codex` 工具 | ❌ 未配置任何 MCP server | 无法调用 |
| `codex` CLI | ❌ 不在 PATH | 无法调用 |
| 外部对话式 LLM | ❌ 仅有 websearch/webfetch | 不能做多轮评审对话 |
| `shared-references/review-tracing.md` | ❌ 不存在 | Review Tracing 无落地处 |
| `.aris/traces/` | ❌ 不存在 | 同上 |
| `gpt-5.4` 模型 | ⚠️ 非 OpenAI 公开标准模型名 | 存疑 (可能为虚构) |

## 2. 内容模板错位（核心问题）

该 skill 为**原创 ML 研究**设计，对**综述论文**基本错位：

| 维度 | Skill 原生问题 | 对综述是否适用 |
|------|---------------|---------------|
| 实验 | "Missing experiments that would strengthen the story" | ❌ 综述无实验 |
| Claim 映射 | "results-to-claims matrix for possible experimental outcomes" | ❌ 综述无实验结果 |
| GPU 资源 | "minimal additional experiment package (highest acceptance lift per GPU week)" | ❌ 综述不消耗 GPU |
| Venue 模板 | "mock NeurIPS review with scores / confidence" | ❌ 目标是 IEEE TVCG（期刊），非 NeurIPS/ICML（会议） |

## 3. 综述该审的维度

| # | 维度 | 说明 |
|---|------|------|
| 1 | 覆盖完整性 | 关键子方向/代表工作是否遗漏 |
| 2 | 分类法合理性 | 五代演化、Structure vs Texture Masters 是否自洽 |
| 3 | 引用准确性与公平性 | 是否偏向/误引 |
| 4 | 趋势分析 | 数据驱动（如本项目 151 篇统计）是否站得住 |
| 5 | 叙述结构 | Trilemma 框架是否成立 |
| 6 | 写作与图表 | overview/timeline/pipeline 清晰度 |

## 4. 若仍要执行的适配路径

1. **换工具**：在 opencode 中用可用入口（API key 或 MCP）替代 Codex；或由 Agent 直接做结构化自评
2. **换评审标准**：将 skill 的「实验/claim 矩阵/GPU-week」框架替换为「综述评审框架」（覆盖/分类法/引用/趋势/结构）
3. **换 venue 模板**：用 TVCG 期刊评审要点，而非 NeurIPS 打分表
4. **自建 trace 落地**：在项目内建 `reviews/` 目录

## 5. 建议

保留 skill 的「多轮批判性评审 + 文档化收敛」骨架，但把评审标准重写为综述标准。具体执行方式已走 kill-argument 替代方案（见 `KILL_ARGUMENT.zh.md`）。
