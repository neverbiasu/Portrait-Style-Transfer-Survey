# TODO

| # | 问题 | 类型 | 严重程度 | 位置 | 修改建议 | 状态 |
|---:|------|------|----------|------|----------|------|
| 1 | 全文没有任何真实风格化视觉结果，图 1/2/3 是占位符（"slots to be filled"），风格迁移综述无视觉对比 | 视觉对比 | 🔴 致命 | Fig. 1–3 | 补充跨范式共享输入的风格化结果画廊 | 未修 |
| 2 | 没有方法对比表，作者明确拒绝做对比表；表 I–IV 分别是年表/术语表/数据集表/路线图，无一是方法对比 | 对比表 | 🔴 致命 | Sec. III / Tables | 建能力矩阵：方法 × {效率 (FPS/分辨率/步数)、控制粒度与模态、时序稳定性、训练数据依赖、身份保持机制}；数值不可比处用定性打分；每个范式选 3–5 个代表方法分表构建 | 未修 |
| 3 | ArtFID 自相矛盾：定义"越低越好"，却说 AdaIN=31.85"差距更大"、InstantStyle=42.48"显著更优"——按其定义 31.85 才是最好，叙述反了 | 事实/数学错误 | 🔴 致命 | Sec. III | 逐一核对原论文引用具体表格，修正数值与结论 | ✅ 已修 |
| 4 | ⚡ 分类体系不一致：摘要/引言说"五范式（优化/前馈/GAN/扩散/3D-NeRF）"，第 III 节却说"四大族（NST/GAN/扩散/AR）" | 结构/逻辑 | 🔴 阻断 | Abstract vs Sec. III/IV | 统一一套范式并全文贯彻；加一个非架构维度（粒度或控制模态） | ✅ 已修 |
| 5 | 缺失基础图形学/NPR 文献：Kyprianidis TVCG'13、Selim SIGGRAPH'16、Ruder 视频时序、Hertzmann Image Analogies、Winnemöller、APDrawingGAN、Jing NST 综述 TVCG'19、GAN inversion 综述 TPAMI'22 | 文献覆盖 | 🔴 主要 | 全文 / References | 补齐，建立与深度学习方法之间的方法论联系；明确本综述相对已有综述的增量 | ✅ 已修 |
| 6 | ⚡ 数学形式化不完整：(a) 视频时序一致性未做数学建模；(b) 扩散模型反向 SDE/DDIM/score function/CFG 缺形式化；(c) PTI 缺数学表述 | 数学严谨性 | 🔴 主要 | Sec. II / IV-A | 补光流 warping loss / 时序 VGG loss、扩散 SDE/DDIM/CFG 公式、PTI 二阶段优化 | ✅ 已修 |
| 7 | 缺乏与已有综述的差异化说明，且无 PRISMA 式筛选流程；无各会议计数/纳排流程 | 新颖性/方法学 | 🟠 主要 | Sec. I-C | 加"本综述有何不同"段落 + 文献筛选流程图与计数 | ✅ 已修 |
| 8 | 数字对不上：摘要"115+ 篇" vs 实际 106 条参考文献 vs "~90 种方法" vs 151 条 managed sources | 一致性 | 🟠 主要 | Abstract / Refs | 核对并明确统计口径；统一四个数字的 scope 说明 | ✅ 已修 |
| 9 | ⚡ 统一框架薄弱：仅 Eq. (2) 加权损失和，未将四范式统一到共同数学形式；Trilemma 只是概念修辞 | 技术深度 | 🟠 主要 | Sec. II / III | 提出"控制信号→生成先验→约束"分解；补 Trilemma 定性 Pareto 映射 | ✅ 已修 |
| 10 | ⚡ 过度造词/营销腔：Killer Failures、Texture Swimming 未正式定义；GAN=结构/扩散=纹理二分过于简化 | 写作风格 | 🟠 主要 | 全文 | 替换 Killer Failures 为技术术语; Texture Swimming 纳入 Table II; 二分法加 caveat | ✅ 已修 |
| 11 | 评估章节偏"处方式"而非"分析式"：缺各方法实际指标对照表、缺 ArtFID 局限分析、用户研究设计讨论浅、MLLM-as-judge 一笔带过 | 综述定位 | 🟠 中等 | Sec. V | 加 metric usage 表; 扩展 ArtFID bias、用户研究方法论、MLLM 偏差与校准 | ✅ 已修 |
| 12 | 评估内容重复：Sec. V 与 Sec. VII-B 大量重叠 | 组织 | 🟡 次要 | Sec. V / VII-B | 合并去重 | ✅ 已修 |
| 13 | 参考文献质量差：作者字段损坏、裸 "et al."、年份不一致、arXiv 与正式出版区分不清晰、中文姓名缩写不一致 | 引用格式 | 🟡 次要 | References | 全面校对；统一标注 arXiv 预印本状态；统一人名缩写规范 | ✅ 已修 |
| 14 | 未来日期引用：FlowAlign "ICLR 2026"、FlowEdit "ICCV 2025" 超出综述范围 | 引用 | 🟡 次要 | References | 明确标注为预印本，在正文说明纳入理由 | ✅ 已修 |
| 15 | 公式记号粗糙：Eq. (5) e_c 同时作 key/value 无维度交代；Eq. (6) Q_f/Q_c 首次使用未定义 | 记号 | 🟡 次要 | Eq. (5)(6) | 补投影矩阵与维度，首次使用即定义 | 未修 |
| 16 | 权重取值含糊："λ_id≈0.5–1.0""λ_geo≈0.1–0.5" 伪精确、缺具体出处 | 严谨性 | 🟡 次要 | Sec. II-B | 用各方法真实设置表支撑，或删去伪精确值 | 未修 |
| 17 | 缺 StyleGAN2/StyleGAN3 引用，却大量依赖 StyleGAN 家族 | 引用 | 🟡 次要 | Sec. II-E | 补齐 | ✅ 已修 |
| 18 | 局部 vs 全局编辑未作为一级分类轴，埋在"高级任务"里；Sec. IV 内部逻辑联系不够紧密 | 分类 | 🟡 次要 | Sec. IV | 提为独立分类维度；强化"从 2D 到 spatiotemporal"递进逻辑 | 未修 |
| 19 | 表格缺单位/脚注，内联指标（DualStyleGAN FS2K、偏好）缺具体来源表与协议说明 | 图表 | 🟡 次要 | Tables / Sec. III | 补来源与 caption | ✅ 已修 |
| 20 | 行文偶有堆砌辞藻（"navigational constraints""pendulum swing"等） | 文字 | 🟡 次要 | 全文 | 收敛到技术语体 | ✅ 已修 |
| 21 | abstract "five paradigms" → "four core families + emerging frontiers" | 结构/逻辑 | ✅ | Abstract | 已与 body 一致 | ✅ 已修 |
| 22 | "Structure Masters / Texture Masters" 二分法已在 abstract + conclusion 加 caveat | 写作风格 | ✅ | Abstract / Conclusion | 已加 inline caveat + identity-focused diffusion cite | ✅ 已修 |
| 23 | "Proposing a Golden Protocol" → "Proposing (and calling for adoption of) a Golden Protocol" | 结构/逻辑 | ✅ | Contributions | 措辞已修正 | ✅ 已修 |
| 24 | "over 115 publications" vs "~90 distinct methods" vs 151 managed sources 三个覆盖数字不一致 | 一致性 | 🟠 主要 | Abstract / Sec. I-C | 统一 scope 声明，明确各数字计算口径 | ✅ 已修 |

## 评审意见（参考）

| # | 维度 | 评价 |
|---|------|------|
| R1 | 论文概要 | 系统综述 2015–2025 十年人像风格迁移，覆盖 ~115 篇文献 / ~90 种方法。提出"人像编辑三难困境"(Identity Preservation / Editing Fidelity / Inference Speed) 作为统一分析框架，以及 Multi-Pillar Golden Protocol。主题有实效性，覆盖广泛，但距离 TVCG 标准在若干关键维度仍有差距 |
| R2 | 技术深度与数学严谨性 | 优点：关键公式统一了不同范式优化目标。不足：(a) 扩散模型 SDE/DDIM 采样过程缺形式化推导；(b) GAN latent inversion (W/W+) 讨论简略，缺 PTI 数学表述；(c) Trilemma 未形式化为可量化 Pareto frontier；(d) 视频时域一致性缺光流 warping loss 等公式 |
| R3 | 分类体系与全面对比 | 优点：按生成机制分类具有逻辑一致性。关键缺失：未提供任何结构化方法对比表，仅 Table I 年表信息密度不足 |
| R4 | 评估方法论 | 优点：Golden Protocol Multi-Pillar 方向正确。不足：缺用户研究设计方法论讨论、ArtFID 等指标局限分析、MLLM-as-judge 仅一笔带过、缺标准评估基准对比表 |
| R5 | 开放挑战与未来方向 | 优点：识别了 3D/NeRF/3DGS、视频一致性、伦理等前沿方向。不足：缺与经典图形学变形方法 (ARAP/MLS) 的联系、交互编辑未讨论蒸馏/量化/edge 部署、方法论融合展望不够深入 |
| R6 | 最终建议 | Major Revision（大修） |
