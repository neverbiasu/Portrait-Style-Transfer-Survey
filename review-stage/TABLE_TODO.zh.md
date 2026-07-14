# 表格相关 TODO（Table TODO）

> 范围：仅针对"表（table）"的改进项。图/定义/实践指南等见 `STRUCTURE_PLAN.zh.md` 与提交历史。

## Archived（已实现 / 已归档）

- [x] **Table III (`tab:unified_paradigms`) 重设计**：原表只有 NST/GAN/Diffusion/AR 四行 + Control/Prior/Constraint 三列，**无任何具体方法**。已新增第 5 列 *Representative methods*，逐范式补入被引具体方法（Gatys NST / AdaIN / Johnson FST；StyleGAN / BlendGAN / DualStyleGAN；LDM-SD / IP-Adapter / InstantID；StyleTokenizer / EditAR / VAR）；并改用 `tabularx` 消除 280pt 溢出。（commit `451cb0a`）
- [x] **PRISMA 表 (`tab:prisma`)**：由 `table` 改 `table*`，修复 75pt 单列溢出。（commit `daf4f9e`）
- [x] **Trilemma 三轴术语统一**：原稿在三处命名不一致（Editing Fidelity / Stylization Intensity / Inference Speed），已统一为 *Identity Preservation / Stylization Strength / Computational Efficiency*，同步修正 `tab:trilemma_paradigms` 表头与图注。（commit `daf4f9e`）
- [x] **新增 3 篇前沿引用并落到正文**：`shiri2019`（身份恢复逆问题，Identity Loss 小节）、`zhang2026telestyle`（内容保持，Video 小节）、`he2026stylegallery`（免训练语义感知个性化，Adapter 段落）。（commit `451cb0a` + 本次）
- [x] **现有 9 张表**：PRISMA 漏斗、术语表、统一框架、Trilemma 映射、能力矩阵、方法编年史、指标使用、数据集、研究路线图——结构完整。

## Pending（待做）

- [ ] **人工目检 `images/timeline.png`**：确认节点/年份/范式覆盖是否准确（模型无法看图，需人工）。若不准，重绘为矢量时间线（与 `fig:pst_taxonomy` 同 TikZ 风格）。
- [ ] **补一张"年份排序的 PST 里程碑总览表"**（对标 Decade Survey Table 1）：与现有 `tab:method_overview` 互补（后者未按年份排序），低成本高价值。
- [ ] **可选：Table IV (`tab:trilemma_paradigms`) 补具体方法示例**：目前仅范式级评级（★▲●），可加每行代表方法使读者更易落地。
- [ ] **可选：紧凑"按任务域的方法索引"表**（video / local / 3D 等，对标 Decade Survey Table 7，但压缩规模，不追 127 条）。
- [ ] **可选：附录穷尽方法列表**：对标 Decade Survey 附录；我们已在 `app:checklist` 说明 ~90 方法由策展 BibTeX 维护，可补一张精简全表。
- [ ] **复核表编号与正文引用一致性**（当前 Table I–IX），确保无悬空引用。
