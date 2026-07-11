# 文献数据分析 — 151 篇论文（NotebookLM #7）

> 数据源：`Survey/docs/literature_data.json`（151 篇，字段：标题/年份/类别/任务类型/数据集/关键指标/身份保持方法/备注）
> 用途：支撑 *Portrait Style Transfer: A Decade Survey*（TVCG）的论述与表格

## 1. 年份分布（n=127 有年份）

| 年份 | 篇数 | 备注 |
|------|------|------|
| 2014 | 4 | 奠基期 |
| 2015 | 1 | |
| 2016 | 7 | |
| 2017 | 9 | |
| 2018 | 4 | GAN 上升期 |
| 2019 | 8 | |
| 2020 | 3 | |
| 2021 | 15 | 放量 |
| 2022 | 13 | |
| 2023 | 15 | |
| 2024 | 22 | 高峰年 |
| 2025 | 26 | 高峰年（至数据提取日） |

- **2021 年后放量，2024–2025 占 38%（48/127）**，符合领域热度快速上升。

## 2. 类别总分布

| 类别 | 篇数 | 占比 |
|------|------|------|
| Diffusion Models | 55 | 36% |
| GANs | 49 | 32% |
| Feed-Forward Networks | 21 | 14% |
| 未知（非论文） | 12 | 8% |
| Optimization | 8 | 5% |
| 3D/NeRF | 6 | 4% |

## 3. 类别 × 年代（验证五代叙事）

| 年代 | n | 主导机制 |
|------|---|----------|
| 2015–2017 | 17 | Feed-Forward 7, Optimization 5, GANs 4 → **Optimization / Feed-Forward 早期** |
| 2018–2019 | 12 | GANs 7, Feed-Forward 5 → **GAN 时代** |
| 2020–2021 | 18 | GANs 12, Diffusion 1 → **GAN 顶峰，Diffusion 初现** |
| 2022–2023 | 28 | Diffusion 14, GANs 13 → **Diffusion 反超** |
| 2024–2025 | 48 | Diffusion 28, 3D/NeRF 6, GANs 6 → **Diffusion 主导 + 3D/NeRF 兴起** |

→ 与综述主张的 **Optimization → Feed-Forward → GANs → Diffusion → 3D/NeRF 五代主线高度吻合**。数据驱动的有力证据。

## 4. 高频数据集

| 数据集 | 使用篇数 | 领域 |
|--------|----------|------|
| FFHQ | 12 | 人像 |
| CelebA | 5 | 人脸 |
| LSUN | 4 | 场景 |
| AFHQ | 4 | 动物面部 |
| ImageNet | 3 | 通用 |
| MetFaces | 2 | 艺术品人脸 |

FFHQ/CelebA/AFHQ 占绝对主导，符合「Portrait」主题。

## 5. 字段填充率

| 字段 | 填充率 | 说明 |
|------|--------|------|
| 备注 | 99% | 可参考 |
| 年份 | 84% | 可靠 |
| 任务类型 | 84% | 可靠 |
| 身份保持方法 | 64% | 部分可用 |
| 关键指标 | 58% | 部分可用 |
| 数据集 | 49% | 有限 |

24 篇信息极少（≤1 字段有值）的条目基本是非论文 source（综述写作指南、教学 PDF、PDF 未被完整摄入的 arxiv 链接），**不应进入正式表格**。

## 6. 写作建议

1. **Diffusion 已成主流**（55 篇，2024–2025 占 28/48），建议正文强化 Diffusion 章节（Stable Diffusion / LoRA / 身份保持扩散）
2. **3D/NeRF 是前沿小类**（仅 6 篇），放在"Future / Emerging Frontiers"作上升期方向，不必展开过细
3. **Optimization 类偏少**（8 篇）但属奠基期，保留为第 1 代即可
4. **24 篇无年份 / 12 篇未知类别**不应进入正式表格，仅作库内冗余

## 7. 待办

1. 将以上分布与五代叙事直接写进顶层 `main.tex`（内联表格/正文）
2. 把 `main.tex` 现有 `\input{Survey/paper/tabs/tab_chronology}` 等依赖内联化，脱离 Survey/
