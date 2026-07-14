# Handoff

> 论文已从 `Awesome-Portraits-Style-Transfer`（原 awesome-list 仓库）分拆到此目录 `Portrait-Style-Transfer-Survey`。

---

## 仓库状态

- **位置**：`/Users/nev4rb14su/workspace/Portrait-Style-Transfer-Survey/`
- **Git**：22 commits，纯论文历史，**无 remote**（纯本地，未上 GitHub）
- **远程选项**：后续需要时 `git remote add origin <url> && git push -u origin main`
- **编译**：18 页，0 overfull，0 undefined（最后一次完整编译结果）
- **Bib**：131 条参考文献（106 个 `\cite{}` 在正文）
- **.gitignore**：已添加 LaTeX build 产物（`.aux`, `.bbl`, `.log`, `main.pdf` 等）

## 目录结构

```
Portrait-Style-Transfer-Survey/
├── main.tex              # 论文正文 (681 行)
├── references.bib        # 参考文献 (131 条)
├── images/
│   ├── overview.png      # Fig.1 - Trilemma 概念图
│   ├── timeline.png      # Fig.2 - 时间线
│   └── pipeline.png      # Fig.3 - StyleGAN 工作流
├── Survey/paper/tabs/    # 孤儿文件（已不被引用，未来可清理）
├── TODO.md               # 24 项 TODO 清单（全部完成）
├── CONTENT_MAP.zh.md     # 中文内容对应表（用于审校对齐）
├── MEMORY.zh.md           # 工作记忆/逻辑线索
├── KILL_ARGUMENT.zh.md    # 对抗审查
├── LITERATURE_ANALYSIS.zh.md  # 文献分析
├── REVIEW_SKILL_ANALYSIS.zh.md  # 审稿技能分析
└── main.pdf              # 最新编译 PDF
```

## 已完成的 TODO（全部 24 项）

| # | 问题 | 状态 |
|---|------|------|
| 1 | Fig.1 视觉结果占位符 | ✅ 图注已修正 |
| 2 | 缺方法对比表 | ✅ 新增 Table VIII (14 方法 × 7 维) |
| 3 | ArtFID 矛盾结论 | ✅ |
| 4 | 分类体系不一致 | ✅ 统一四范式 + 递进逻辑 |
| 5 | 缺 NPR/基础文献 | ✅ 补 8 篇 |
| 6 | 数学形式化不完整 | ✅ 补扩散 SDE/DDIM/CFG/PTI/光流 |
| 7 | 缺 PRISMA 漏斗 | ✅ 四阶段 + venue 分解 |
| 8 | 数字对不上 | ✅ scope 声明统一 |
| 9 | 统一框架弱 | ✅ Eq.(14) 三分量 + Trilemma 帕累托 |
| 10 | Killer Failures / Texture Swimming | ✅ 术语替换 + glossary |
| 11 | 评估节偏处方 | ✅ 分析式改写 + metric_usage 表 |
| 12 | 评估重复 | ✅ Sec V vs VII-B/VII-C 去重 |
| 13 | 参考文献质量 | ✅ |
| 14 | 未来日期引用 | ✅ 标注为预印本 |
| 15 | 公式记号粗糙 | ✅ 补 W_K/W_V/Q_f/Q_c 维度 |
| 16 | 权重伪精确 | ✅ 改为定性描述 + 引用原论文 |
| 17 | 缺 StyleGAN2/3 引用 | ✅ |
| 18 | 分类轴不明显 | ✅ Sec IV 导语加递进段落 |
| 19 | 表格缺脚注来源 | ✅ |
| 20 | 堆砌辞藻 | ✅ |
| 21 | abstract 五范式说法 | ✅ |
| 22 | 二分法 | ✅ 加 caveat |
| 23 | Golden Protocol 措辞 | ✅ |
| 24 | 覆盖范围不一致 | ✅ |

## 论文结构速览

| 节 | 标题 | 主要内容 | 表 | 图 | 公式 |
|----|------|---------|----|----|------|
| I | Introduction | 技术演进 + Trilemma + PRISMA 漏斗 | — | 2 | 1 |
| II | Theoretical Foundations | AdaIN / 损失函数 / VAE / GAN(PTI) / FlowMatch / Diffusion(SDE/DDIM/CFG) / 统一框架 | 3 | — | 14 |
| III | Methods | NST → GAN → Diffusion → AR 四范式 | 1 | 1 | — |
| IV | Advanced Tasks | 视频光流 / 局部编辑 / 3D-aware | — | — | 2 |
| V | Evaluation | Golden Protocol / ID / ArtFID / CLIP / User Study / MLLM | 1 | — | — |
| VI | Datasets & Ethics | FFHQ / CelebA-HQ / OmniStyle-1M / EU AI Act | 1 | — | — |
| VII | Discussion | Trilemma 实践 / 创新方向 / 伦理 | — | — | — |
| VIII | Conclusion | 回顾 / 开放挑战 4 项 / 部署 / 局限 | 1 | — | — |

## 已知问题/遗留项

1. **Survey/ 目录**：`Survey/paper/tabs/*.tex` 5 个文件不在 main.tex 中引用，安全可删（`rm -rf Survey/`）
2. **Fig.1**：仍为示意图，有足够时间可替换为真实风格化输出画廊（原 TODO #1 只修了图注，未补真实结果）
3. **编译**：若环境缺少 LaTeX 包（如 `\usepackage{tikz}` 等），需安装相应包
4. **Contact**：这个 session 用的是 neverbiasu 的工作站，后续 session 确保在 `Portrait-Style-Transfer-Survey/` 下启动

## 下一步建议

下一步自然动作：
- 用 `CONTENT_MAP.zh.md` 逐节审校，确保内容覆盖完整
- 或进入写作阶段，用 `CONTENT_MAP.zh.md` 指导新增/删节
- 或新建 GitHub remote，推送到远端备份
