# 结构优化分析与实践指南设计（中文版）

**日期：** 2026-07-14
**范围：** 针对用户提出的 6 项结构议题，给出"分析 + 已落实改动"的对照。改动均已写入 `main.tex` 并编译通过（undefined=0，A5=0）。

---

## 0. 本次已落实的具体改动（速览）

| 议题 | 动作 | 状态 |
|---|---|---|
| 综述组织图（Taxonomy Tree） | 新增 TikZ 三轴分类树 `fig:pst_taxonomy`（生成范式 / 任务输出 / 控制信号 × Trilemma 透镜） | ✅ 已实现并编译 |
| 时间线图 `timeline.png` | 从 `~/Downloads` 导入 `images/`，新增 `fig:pst_timeline` | ✅ 已纳入，待人工目检 |
| 生成范式组织（NST/GAN/Diffusion/AR） | 用户确认无问题 | ➖ 保持不变 |
| 统一框架 / PST 定义 | 新增 **Definition 1（形式化 PST）**；Trilemma 三轴术语统一 | ✅ 已实现 |
| Trilemma 命名不一致 | 三处不一致命名统一为 *Identity Preservation / Stylization Strength / Computational Efficiency* | ✅ 已修正 |
| 穷尽式方法表 | 分析是否值得借鉴（见 §3） | 🔍 分析给出建议，未盲目加表 |
| 实践指南 | 新增 `§Practical Guidelines: Lessons from a Decade of PST`（G1–G7） | ✅ 已实现 |
| PRISMA 表溢出 | `table` → `table*`，修复 75pt 溢出 | ✅ 已修复 |

当前稿件体量：4 图（teaser / pipeline / timeline / taxonomy）+ 9 表 + Definition 1 文本框。

---

## 1. 时间线图 `timeline.png`：纳入与"是否优化"分析

**现状：** `~/Downloads/timeline.png`（2332×1230，RGBA 位图）已复制到 `images/timeline.png`，作为 `fig:pst_timeline`（2015–2025 PST 里程碑时间线）纳入引言区。编译已验证其能被正确嵌入。

**风险（需人工）：** 本模型无法查看图片内容，因此该图的 **节点准确性、与我们范式划分的一致性、是否覆盖 video/3D/AR 前沿、配色可读性** 必须经由人工目检确认。

**优化建议（分档）：**
- **最低成本：** 人工目检 → 若内容与我们综述一致，直接保留（满足"应该有时间线图"的诉求）。
- **camera-ready 推荐：** 位图在期刊排版中通常不如矢量图（不可编辑、缩放易糊、风格难统一）。建议将其 **重绘为矢量**（TikZ 或 drawio→PDF），与我们新增的 `fig:pst_taxonomy`（已是 TikZ 矢量）风格一致。
- **若内容不符：** 直接替换为自制矢量时间线，节点严格对应 §Technological Evolution 的里程碑叙事。

**结论：** 先纳入以补齐"时间线图"这一最明显缺口；是否进一步矢量优化取决于人工目检结果。

---

## 2. PST 形式化定义 + Trilemma 再斟酌（已落实）

**原稿问题（用户敏锐指出"Trilemma 需要再斟酌"）：** Trilemma 三个轴在全文被 **三种不同方式命名**，造成术语漂移：
- 列举项用 *Editing Fidelity / Inference Speed*；
- 正文用 *stylization strength / computational efficiency*；
- teaser 图注用 *stylization intensity / inference speed*。

**处理：**
1. 统一为 **Identity Preservation / Stylization Strength / Computational Efficiency**，同步修正：列举项、Pareto 形式化变量（$I_m, \mathrm{St}_m, C_m$）、`tab:trilemma_paradigms` 表头与图注、Conclusion 措辞。
2. 新增 **Definition 1（Portrait Style Transfer）**，把"任务"与"约束"分清：
   - PST 是任务：$\mathbf{y}=G(\mathbf{x},\mathbf{s};\theta)$，满足 (i) 身份/拓扑保持、(ii) 目标风格传达、(iii) 仍为可控可信人脸；联合损失 $\mathcal{L}_{\mathrm{PST}}$ + 身份硬约束 $I(\mathbf{y},\mathbf{x})\ge\tau_{\mathrm{id}}$ + 计算预算。
   - Trilemma 是该任务约束面上的 **三元权衡**（身份 ↔ 风格 ↔ 效率），而非独立新框架——延续此前"采用 well-established impossible triangle 并形式化"的措辞，**不夸大原创性**，正合 TVCG/TOG 对"定义清晰 + 框架不夸大"的期待。

---

## 3. 穷尽式方法表是否值得借鉴（对标 *Style Transfer: A Decade Survey* Table 3 / Table 7）

该综述共 **9 表**，其中与"穷尽"相关的是：
- **Table 3**：~55 个 GAN 变体逐年列表；
- **Table 4**：4 大类 16 子类 90+ 扩散方法嵌套分类；
- **Table 7**：~127 个方法按 5 应用域索引；
- 另有 Table 1（编年史总览）、Table 6（5 维评级矩阵）、Table 8（数据集）等。

**我们的现状：** 已有 `tab:method_overview`（客观编年史）、`tab:comparison_matrix`（能力矩阵）、`tab:trilemma_paradigms`（Trilemma 映射）、`tab:datasets_pst`、`tab:research_roadmap` 等——内容已相当充实（用户亦确认"我们内容也挺多了"）。

**借鉴判断：**

| 借鉴项 | 价值 | 建议 |
|---|---|---|
| 年份排序的 **PST 里程碑总览表**（对标 Table 1） | 高 / 低成本 | ✅ 建议补一张（与现有 `tab:method_overview` 互补，后者未按年份排序） |
| 逐范式 **穷尽变体表**（Table 3 / 4，55 / 90 条） | 低 / 易冗长 | ❌ 不建议。我们是 *人像* 综述，已有能力矩阵+编年史，再加会造成重复与篇幅膨胀 |
| **应用域方法索引表**（Table 7，~127 条） | 中 | ◐ 可选补一张"按任务域的方法索引"紧凑表，但不必到 127 条规模 |

**结论：** 采取克制策略——**补一张年份总览表即可**，不盲目追表数量。这既对齐 Decade Survey 最有用的表（Table 1），又避免其"表过多"的膨胀问题。

---

## 4. 实践指南：以"十年领域经验"的口吻设计（已落实）

新增 `§Practical Guidelines: Lessons from a Decade of PST`（Discussion 末尾），刻意区别于已有的 *Dataset Selection Guide*（偏数据清单）与 *Practical Deployment*（偏部署清单），聚焦 **方法论层面的可操作经验**，每条对应 Trilemma 某轴或某范式陷阱：

- **G1 — 按约束选范式，而非追潮流**：以 Trilemma 的绑定轴决定 GAN/Diffusion/AR。
- **G2 — 身份保持作硬约束，而不是事后指标**：在表示层强制，而非风格化后补救。
- **G3 — 在表示层而非像素层解耦风格/内容**：避免 Gram/IN 统计耦合带来的年代久远的伪影。
- **G4 — 先统一评估再宣称 SOTA**：指向 Golden Protocol，绝不单轴报优。
- **G5 — 正视训练数据隐私转向**：用合成三元组（如 OmniStyle-1M）并补真实脸评估。
- **G6 — 延迟是一等需求**：按目标设备选采样器/适配器，而非只报离线最佳。
- **G7 — 视频/3D 中一致性优先于风格**：时间/几何一致性先于纹理细腻度被感知。

设计原则：用"十年经验"的确定性口吻给出 **带观点** 的指引，而非综述式罗列——这正是 5 篇标杆综述中 #5（3D Stylization）"Practical Guidelines"小节的精髓，且更契合我们"领域老手"的定位。

---

## 5. 下一步（可选，待用户决定）

1. **人工目检 `timeline.png`**；如需，重绘为矢量时间线（与 `fig:pst_taxonomy` 同风格）。
2. **补一张年份排序的 PST 里程碑总览表**（低风险、高价值，对标 Decade Survey Table 1）。
3. 视篇幅决定是否加紧凑"任务域方法索引"表（不超过现有 Advanced Tasks 覆盖范围）。
4. 范式组织与统一框架维持现状（用户已确认无问题）。
