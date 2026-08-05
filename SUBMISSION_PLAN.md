# 投稿写作日程

> 论文：Portrait Style Transfer: A Decade Survey
> 当前状态：18 页，0 overfull，0 undefined，62 项 TODO 已完成 52 项
> 最新提交：fae1344 (fix Colab notebook URL)
> 日期：2026-08-05

---

## 阶段概览

| 阶段 | 目标 | 截止 | 状态 |
|------|------|------|------|
| 0. 预备 | 远程仓库、画廊跑通、Progress 系统就位 | 2026-08-05 | ✅ 已完成 |
| 1. 收尾 | 剩余 TODO（T7–T11, G4–G5）、最终审校 | 2026-08-19 | 🔄 进行中 |
| 2. 预印本 | arXiv 提交 + 社区反馈 | 2026-08-26 | ⏳ 待开始 |
| 3. 投稿 | 目标会议/期刊投稿 | 2026-10–11 | ⏳ 待定 |
| 4. 审稿回复 | Major Revision 回复 | 2026-12–2027-01 | ⏳ 待定 |
| 5. 录用 | Camera-ready | 2027-03–06 | ⏳ 待定 |

---

## 阶段 1：收尾（2026-08-05 → 2026-08-19）

### 画廊（G4–G5）
| 项 | 任务 | 依赖 | 预计耗时 |
|----|------|------|----------|
| G4 | Colab 跑 Wikimedia 风格图 | GitHub 远程已就绪 ✅ | 2–3h（Colab T4） |
| G5 | 下载 PNG → images/ → 重编译 | G4 完成 | 30min |

### 剩余 TODO（T7–T11）
| 项 | 任务 | 优先级 | 预计耗时 |
|----|------|--------|----------|
| T7 | 人工目检 timeline.png / 必要时矢量重绘 | P1 | 1–2h |
| T8 | 补年份排序 PST 里程碑总览表 | P1 | 1h |
| T9 | Table IV 补具体方法示例 | P2 | 30min |
| T10 | 附录方法全表（~90 方法精简版） | P3 | 1h |
| T11 | 表编号与引用一致性复核（audit.sh） | P3 | 30min |

### 最终审校
| 项 | 任务 | 预计耗时 |
|----|------|----------|
| R1 | 4 轮审稿意见逐条核对（REVIEW_SUMMARY.md） | 2h |
| R2 | 编译 + PDF 终检 | 30min |
| R3 | 更新 HANDOFF.md + TODO.md | 30min |

---

## 阶段 2：预印本（2026-08-26 前）

| 任务 | 说明 |
|------|------|
| arXiv 提交 | 提交至 arXiv，标题：Portrait Style Transfer: A Decade Survey |
| 补充 Artifact 链接 | 在 paper 中加入 GitHub repo 链接 + Colab badge |
| 社区反馈 | 发布到 Twitter/X + LinkedIn + Reddit r/MachineLearning |

---

## 阶段 3：投稿（2026-10–11）

### 目标 venue（按优先级）
| Venue | 类型 | 截稿日期 | 轮次 |
|-------|------|----------|------|
| **TVCG** (IEEE) | 期刊 | 滚动投稿 | 2–3 月 |
| **ACM Computing Surveys** | 期刊 | 滚动投稿 | 2–3 月 |
| **ICCV 2027** | 会议 | 2027-02 末 | 4–6 月 |
| **CVPR 2027** | 会议 | 2026-11 末 | 3–5 月 |
| **ECCV 2026** | 会议 | 已过 | — |

> 建议：先投 TVCG（滚动审稿，速度快），同时准备 ICCV 2027 版本。

---

## 阶段 4–5：审稿与录用（2026-12 → 2027-06）

| 里程碑 | 时间 |
|--------|------|
| 投稿截止 | 按 venue 而定 |
| 第一轮审稿意见 | 投稿后 2–4 月 |
| Major Revision 回复 | 1 个月内 |
| 最终录用 | 2027-03–06 |
| Camera-ready | 录用后 1–2 月 |

---

## 风险与缓解

| 风险 | 缓解 |
|------|------|
| Colab 画廊跑不通（依赖下载失败） | 保留本地 MPS 验证结果作为 fallback；Limitations 中说明 |
| 审稿要求补充实验 | Golden Protocol 已设计为可扩展，社区可复现 |
| 截稿日期紧迫 | 阶段 1 预留 2 周缓冲；TODO 优先级已标注 |

---

## 关键链接

- GitHub 仓库：https://github.com/neverbiasu/Portrait-Style-Transfer-Survey
- Colab Notebook：`gallery/PST_Gallery.ipynb`（需先 clone 仓库）
- Progress 文件：`PROGRESS.md`
- 审稿总结：`REVIEW_SUMMARY.md`
- TODO 清单：`TODO.md`