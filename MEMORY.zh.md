# MEMORY — Portrait Style Transfer 十年综述项目

> Agent 接手时优先阅读此文件。记录项目事实、关键决策与工具链配置。

## 1. 项目概况

| 项 | 值 |
|---|-----|
| 项目 | Portrait Style Transfer: A Decade Survey (2015–2025)，人像风格迁移十年综述 |
| 目标期刊 | IEEE TVCG（IEEEtran 文档类） |
| 作者 | Feichi Chen（陈非池） |
| 来源压缩包 | `Portrait Style Transfer Survey(v1.5).zip`（仓库根） |

## 2. 仓库文件结构

| 文件/目录 | 说明 | 状态 |
|-----------|------|------|
| `main.tex` | **唯一论文文件**，最新版 | ✅ 所有改动以此为准 |
| `references.bib` | 参考文献（118 条，已补入 4 条缺口） | ✅ 编译 0 undefined citation |
| `images/` | `overview.png` / `timeline.png` / `pipeline.png` | ✅ 已从 Downloads 替换（2026-04-17 版） |
| `TODO.md` | 写作任务清单 | 来自 zip |
| `Survey/`（workspace 根） | 旧工作副本，已归档 | ⛔ 不再更新 |
| `content/` | `cover.png` | 不相关 |

## 3. 关键决策记录

1. **顶层 `main.tex` 是唯一论文文件**。Survey/ 归档不更新。
2. **文献数据直接写进 `main.tex`**（内联表格/正文），不进 Survey/paper/tabs/。
3. **同步策略**：
   - Overleaf: `69d90168a7f91dccb290bfc7`，git 同步需会员（暂不做）
   - Prism: OpenAI 网页端产品，不好配 git（暂走网页手动）
4. **3 张图**已替换为 Download 同名文件（April 2026 版）。

## 4. 文献管理（NotebookLM）

| 项 | 值 |
|---|-----|
| 账号 | `neverbiasu@gmail.com` |
| 登录态 | `/Users/nev4rb14su/.notebooklm/profiles/default/storage_state.json` |
| CLI 库 | `notebooklm-py`（v0.7.3） |
| 工具 venv | workspace 根 `.venv_nlm/`（`source .venv_nlm/bin/activate`） |
| 目标 notebook | #7「Domain Generalizable Portrait Style Transfer」 |
| Notebook ID | `d547d711-9291-4b6b-bd82-ecd265b0ec2e` |
| 总 source | 155（151 篇唯一论文 + 4 个重复 URL） |
| 数据文件 | `Survey/docs/literature_data.json` / `.csv`（151 条，字段：标题/年份/类别/任务类型/数据集/关键指标/身份保持方法/备注） |

### 4.1 提取踩坑记录

| 问题 | 原因 | 修复 |
|------|------|------|
| 列左移 | Markdown 表格批量提问，NotebookLM 省略标题列 | 改为「逐篇字段块」格式（`=== 论文N ===` + `字段: 值`） |
| 类别未归一 | NotebookLM 随意生成类别 | 严格限制到 5 类（Diffusion / GANs / Feed-Forward / Optimization / 3D-NeRF） |
| 流中断 | NotebookLM 服务端 180s 无响应 | 脚本自动跳过，续跑补齐 |

## 5. 查漏补缺审计结果

| 步骤 | 结果 |
|------|------|
| NotebookLM 论文数 | 151 |
| `references.bib` 原数 | 114 |
| 匹配命中 | 117（含重复匹配） |
| 排除（非论文/冗余） | 27 个非论文 source + 24 篇无年份 + 12 篇未知类别 |
| **真实缺口**（已全部补入） | **4 篇** |

### 5.1 补入的 4 篇论文

| 论文 | 引用 key | 发表 | 对应章节 |
|------|----------|------|----------|
| Encoding in Style (pSp/e4e) — Richardson et al. | `richardson2021encoding` | CVPR 2021 | §GANs W+ 编码器 |
| FRESCO — Yang et al. | `yang2024fresco` | CVPR 2024 | §Video Portrait Stylization |
| InterFaceGAN — Shen et al. | `shen2020interfacegan` | TPAMI 2020 | §Disentangle (StyleGAN W/W+ 解耦) |
| MangaGAN — Su et al. | `su2021mangagan` | AAAI 2021 | §Local Editing (跨域 cartoon/manga) |

`references.bib` 当前总计：118 条。编译验证通过（0 undefined citation）。

## 6. 待办 & 已知限制

| # | 事项 | 优先级 | 状态 |
|---|------|--------|------|
| 1 | `Survey/paper/tabs/` 依赖内联化（main.tex 仍 `\input` 旧 tab 文件） | medium | ⬜ 暂不需（用户确认） |
| 2 | Overleaf git 同步（需会员） | low | ⬜ 暂不做 |
| 3 | Prism 同步 | low | ⬜ 走网页手动 |
