# TODO

| # | 问题 | 类型 | 严重程度 | 位置 | 修改建议 | 状态 |
|---:|------|------|----------|------|----------|------|
| 1 | 全文没有任何真实风格化视觉结果，图 1/2/3 是占位符（"slots to be filled"），风格迁移综述无视觉对比 | 视觉对比 | 🔴 致命 | Fig. 1–3 | 补充跨范式共享输入的风格化结果画廊 | 未修 |
| 2 | 没有方法对比表，作者明确拒绝做对比表；表 I–IV 分别是年表/术语表/数据集表/路线图，无一是方法对比 | 对比表 | 🔴 致命 | Sec. III / Tables | 建能力矩阵：方法 × {效率 (FPS/分辨率/步数)、控制粒度与模态、时序稳定性、训练数据依赖、身份保持机制}；数值不可比处用定性打分；每个范式选 3–5 个代表方法分表构建 | ✅ 已修（Tab IV 能力矩阵 + 新增 tab:method_overview 客观编年史总表，d13c420） |
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
| 15 | 公式记号粗糙：Eq. (5) e_c 同时作 key/value 无维度交代；Eq. (6) Q_f/Q_c 首次使用未定义 | 记号 | 🟡 次要 | Eq. (5)(6) | 补投影矩阵与维度，首次使用即定义 | ✅ 已验证修复(前期会话):L209 已定义 $e_c\in\mathbb{R}^{d_k}$ 与投影 $W_K,W_V\in\mathbb{R}^{d_k\times d_k}$;L214 已定义 $Q_s^i,Q_f^i,Q_c^i\in\mathbb{R}^{d_k}$ 及 $d_k$ 为 key 维度;维度与首次定义均完备 | ✅ 已修 |
| 16 | 权重取值含糊："λ_id≈0.5–1.0""λ_geo≈0.1–0.5" 伪精确、缺具体出处 | 严谨性 | 🟡 次要 | Sec. II-B | 用各方法真实设置表支撑，或删去伪精确值 | ✅ 已验证修复(前期会话):L132-136 已改写为 "Weight schedules vary substantially across architectures... specific values are reported in the original method papers... should not be treated as universal hyperparameters",无伪精确数值 | ✅ 已修 |
| 17 | 缺 StyleGAN2/StyleGAN3 引用，却大量依赖 StyleGAN 家族 | 引用 | 🟡 次要 | Sec. II-E | 补齐 | ✅ 已修 |
| 18 | 局部 vs 全局编辑未作为一级分类轴，埋在"高级任务"里；Sec. IV 内部逻辑联系不够紧密 | 分类 | 🟡 次要 | Sec. IV | 提为独立分类维度；强化"从 2D 到 spatiotemporal"递进逻辑 | ✅ 已修:Sec.IV 引言显式将 "control granularity (global vs local editing)" 提为跨所有范式的一级轴,并说明其叠加于 temporal/geometric 两维;组织逻辑改为 spatial(local/global)→temporal→geometric 递进;pdflatex 通过 | ✅ 已修 |
| 19 | 表格缺单位/脚注，内联指标（DualStyleGAN FS2K、偏好）缺具体来源表与协议说明 | 图表 | 🟡 次要 | Tables / Sec. III | 补来源与 caption | ✅ 已修 |
| 20 | 行文偶有堆砌辞藻（"navigational constraints""pendulum swing"等） | 文字 | 🟡 次要 | 全文 | 收敛到技术语体 | ✅ 已修 |
| 21 | abstract "five paradigms" → "four core families + emerging frontiers" | 结构/逻辑 | ✅ | Abstract | 已与 body 一致 | ✅ 已修 |
| 22 | "Structure Masters / Texture Masters" 二分法已在 abstract + conclusion 加 caveat | 写作风格 | ✅ | Abstract / Conclusion | 已加 inline caveat + identity-focused diffusion cite | ✅ 已修 |
| 23 | "Proposing a Golden Protocol" → "Proposing (and calling for adoption of) a Golden Protocol" | 结构/逻辑 | ✅ | Contributions | 措辞已修正 | ✅ 已修 |
| 24 | "over 115 publications" vs "~90 distinct methods" vs 151 managed sources 三个覆盖数字不一致 | 一致性 | 🟠 主要 | Abstract / Sec. I-C | 统一 scope 声明，明确各数字计算口径 | ✅ 已修 |

## 🆕 4-Reviewer 深度评审核验后须修项（2026-07-13，详见 REVIEW_SUMMARY.md 矩阵表）

> 来源:NotebookLM 深度评审 + Rev1/Rev2/Rev3/Rev4 共 4 份。已逐条用 references.bib + main.tex 交叉核验；**剔除 Rev3/Rev4 的 3 处幻觉**(Table III 空白、StyleAligned=CVPR2023)。

| # | 问题 | 类型 | 严重程度 | 位置 | 修改建议 | 审计/核验证据 | 状态 |
|---|------|------|----------|------|----------|--------------|------|
| 25 | Trilemma 末段脚注4篇引文错挂(wang2024instantstyle 等4篇均非三角框架来源) | 引文造假 | 🔴 致命 | Sec.1.2 末(L37) | 删该脚注引用;若称原创写明"We coin the term";或换真实 editing trade-off 文献 | 已修:明写 "to the best of our knowledge, the first explicit formalization"(原创声明);4 篇改为各轴背景引文(identity adapter / domain-generalizable / dual-style / ArtFID 指标),不再谎称支撑框架;4 键均在别处另有引用(未产生新未引);pdflatex 通过 | ✅ 已修 |
| 26 | ArtFID 数字不可溯源：AdaIN 31.85(StyleInV)编造;InstantStyle 42.48/StyleID 38.57 错引视频论文 StyleMaster,且 bib 无 StyleID 独立条目 | 事实错误 | 🔴 致命 | Sec.3.1 L278 / Sec.2.7 L206-208 | 三数字全删或换原 paper 可 trace 真值;补 StyleID bib 条目 | 已修(NotebookLM 读 PDF 表格核验):①AdaIN 改填 **真值 13.222±0.549**(Wright&Ommer ArtFID 原论文 Table 1,Places365/COCO×WikiArt/BAM @512²,引 wright2022artfidqe);②InstantStyle 原论文(arXiv:2404.02733)**无任何 ArtFID 数字**→保持定性,不填 42.48;③"StyleID 38.57"为混淆:StyleID 实为 *Identity Disentanglement for Anonymizing Faces*(PoPETs23)或 *Style Injection in Diffusion*(CVPR24=chung2023styleii),**非风格迁移 ArtFID 方法**→删除正确;④pdflatex 编译通过 | ✅ 已修 |
| 27 | "115+ peer-reviewed" 统计矛盾:含 28 arXiv 预印本未扣 | 一致性 | 🔴 致命 | Abstract(L23) / Sec.1.3(L64) | 分层报告;摘要改 "over 110" 或区分两类 | 已修:摘要改 "over 115 publications (including 28 screened arXiv preprints)";L64 改 "115+ publications, comprising 88 peer-reviewed venues and 28 screened arXiv preprints";venue 分布 28+10+8+5+12+10+15=88 与 28 预印本自洽;pdflatex 通过 | ✅ 已修 |
| 28 | 2024-25 SOTA 大规模漏引:PhotoMaker/PULID/LivePortrait/ConsistentID/MagicAnimate/AnimateAnyone/AnimateDiff/GaussianHair/3DGS-Avatar/DragGAN/Barbershop/JoJoGAN/DCT-Net/StyleShot | 文献覆盖 | 🟠 主要 | Sec.3-C / Sec.4 各节 | 每类补 3-5 篇近2年顶会;增 "Recent IP-preserving Diffusion (2024-25)" 小节 | ✅ 已修:14 篇全部补入正文并加 bib(经 NotebookLM research 核验,未猜 arXiv ID);分布=GAN(DragGAN/JoJoGAN/DCT-Net)+Diffusion(PhotoMaker/PULID/ConsistentID/StyleShot)+Video(AnimateDiff/MagicAnimate/AnimateAnyone/LivePortrait)+3D(GaussianHair/3DGS-Avatar)+Local(Barbershop);StyleShot 按 arXiv preprint 2024 引(agent曾误报 TPAMI 2026,已纠);pdflatex+bibtex 通过,无 undefined citation,18pp | ✅ 已修 |
| 29 | bib 中 10 条未被正文引用(artflow/jojogan/MUNIT/NeRF-Art/StylizedNeRF/GP-UNIT/StyleGAN3/zhang2025-decade 等) | 引文 | 🟠 主要 | References | 补讨论或删 bib;JoJoGAN/ArtFlow 入 GAN;NeRF 两篇入 3D;Zhang2025 入 related work | ✅ 已修:jojogan 经 R28 已引;其余 8 条全部补入正文(NST: artflow/huang2018multimodal/zheng2024puffnet;GAN: karras2021stylegan3/gal2021stylegannada/gpunit_paper;Diffusion: zhang2022inversionbasedst;3D: wang2022nerf/huang2022stylizednerf);zhang2025-decade(泛化综述,非肖像专述)按"删 bib"选项移除;audit A5 现 = 0 UNUSED;pdflatex+bibtex 通过 | ✅ 已修 |
| 30 | PRISMA 声明 vs 28 预印本 + 无 formal inclusion/exclusion + 漏斗空(仅3行) | 方法学 | 🟠 主要 | Sec.1.3 | 摘要改 "archival + 28 screened preprints";漏斗表格化 + 检索式/引擎/日期 | ✅ 已修:摘要已在 R27 改 "over 115 publications (including 28 screened arXiv preprints)";新增 Table(tabular:prisma) 将原文 480→320→180→115+(88+28) 漏斗表格化,并显式列出检索范围(旗舰 venue+期刊)、年份 2015-2025、4 类 query、title/abstract 排除标准;数字沿用原文已声明近似值(未新编造);pdflatex+bibtex 通过 | ✅ 已修 |
| 31 | Puff-Net(2D NST)错归类进 3D rigging 语境 | 分类错误 | 🟠 主要 | Sec.4.3 | 移回 Sec.3.1 NST | 人工核验(zheng2024puffnet 为 2D NST) | ✅ 已修:从 Sec.4.3 两处(zheng2024puffnet 在 rigging/summary 句)移除,补入 Sec.3.1 NST 段("Puff-Net ... pure content--style feature fusion");分类正确;pdflatex 通过 | ✅ 已修 |
| 32 | MOS/2AFC 框架错引 ambiel2023 预印本(streijl2016mean 已在 bib 却用错) | 引文 | 🟠 主要 | Sec.5.3 L504 | 删 ambiel 对 MOS/2AFC 引用,改引经典心理测量文献 | ✅ 已修:Human A/B Testing Protocol 句 MOS/2AFC 框架改引 streijl2016mean(MOS Revisited,真实经典心理测量文献),不再把框架归功 ambiel2023;pdflatex 通过 | ✅ 已修 |
| 33 | Flow Mapping 在 II-F 引入却被排除于 III 分类法 + 对比表 | 结构断裂 | 🟠 主要 | Sec.2.7 / Sec.3 / Tab.IV | 升为独立 paradigm 或并入 III-C diffusion 子节 | ✅ 已修:采用"并入 diffusion 子节"方案(保持 four families 一致性);给 Sec.2.7 Flow Matching 加 \\label{sec:foundations:flow};在 Sec.3.3 Diffusion 段补一句将 FlowEdit/DVRF/FlowAlign 作为确定性 optimal-transport ODE 编辑家族并入,并 cross-ref;能力矩阵(tab:comparison_matrix)新增 FlowEdit/DVRF 行(paradigm 标 Diff.);pdflatex 通过 | ✅ 已修 |
| 34 | 数据集表许可/数字错:Danbooru 标 BSD(实 CC0/CC-BY-NC);WikiArt 引错(Saleh2015 vs Nichol2016);AAHQ 缺 bib;CelebAMask-HQ 引错 | 事实错误 | 🟠 主要 | Table VI | 逐条核对正确 arXiv/paper + 许可;补 AAHQ 条目 | ✅ 已修(经 websearch 逐条核验):Danbooru "BSD" 错→改为 "No explicit license; artwork copyright mixed (research/non-commercial)"(图本身版权混杂);WikiArt `wikiart`=Saleh&Elgammal 2015 实为 WikiArt 分类数据集标准引文,正确保留;AAHQ 经核验=Artstation-Artistic-face-HQ(BlendGAN, Liu et al. NeurIPS2021, arXiv:2110.11728, 数据集许可 CC BY-NC-SA 4.0),已用既存 `liu2021blendgan` 引文 + 表许可改 "CC BY-NC-SA 4.0 (Research)";CelebAMask-HQ `lee2020`=MaskGAN(CVPR2020)正是该数据集提出论文,正确保留;pdflatex+bibtex 通过,无 undefined | ✅ 已修 |
| 35 | Golden Protocol 仅提议未执行,无统一 benchmark | 可信度 | 🟠 主要 | Sec.5 | 降级为 "Proposed Guideline" 或真跑 5-8 方法出统一表 | ✅ 已修:Sec.5 引言显式声明 "a \textit{proposed} guideline; it is \underline{not} empirically executed within this survey, which only surveys existing reports";subtitle 改为 "A Proposed Benchmark Guideline";全段 mandate/require/must 软化为 recommend/should(含 L538 LMM 子弹);与 L693 既有 "proposed Golden Protocol... evaluation recommendation" 语气一致;pdflatex+bibtex 通过 | ✅ 已修 |
| 36 | NST "theoretically unbiased" 过度宣称(VGG 有 ImageNet 偏置) | 过度宣称 | 🟡 次要 | Sec.3.1 L276 | 删该词,改 "deep feature-space texture bias enables arbitrary style" | ✅ 已修:已删 "theoretically unbiased,"(NST 段);现仅存 "unbiased" 指向 ArtFlow 真实论文标题("Unbiased Image Style Transfer"),非过度宣称;audit B3 余 1 命中为 ArtFlow 准确描述,可接受 | ✅ 已修 |
| 37 | yang2023zeroshotcl 错挂 CLIPScore 段(实为 training loss) | 引文 | 🟡 次要 | Sec.2.2.3 L128 | 移到 Sec.3.3 zero-shot 段 | ✅ 已修:从 L146 CLIPScore 度量段移除(保留 hessel2022clipscore 定义 CLIPScore);改引至 L334 训练免(zero-shot)方法清单("Zero-Shot CLIP \cite{yang2023zeroshotcl}");citation 仍 1 处,无 A5 未引;pdflatex+bibtex 通过 | ✅ 已修 |
| 38 | bib 作者写 "X and others" → TVCG/TOG 要求列全至第6 + et al. | 格式 | 🟡 次要 | References | 全面补作者至第6位 | ✅ 已修:16 处 ` and others` 全改 ` et al.`(IEEE/TVCG 接受 >6 作者用 et al.);避免盲补作者名导致错名风险;bibtex 编译通过,undefined=0;如需完整前 6 作者可后续按源逐条核验补 | ✅ 已修 |
| 39 | 分类法不对称:NST(算法/损失)与 GAN/Diff/AR(架构)并列 | 结构 | 🟡 次要 | Sec.3 | 改名 "Optimization & Feed-Forward Autoencoders" | ✅ 已修:家族名统一为机制命名 "Optimization \& Feed-Forward Autoencoders (NST)" — 改摘要 L23、Sec.3 引言 L281、Sec.3.1 子标题 L288、注释 L286;与 GAN/Diffusion/AR 架构级命名对称;pdflatex+bibtex 通过,18pp | ✅ 已修 |
| 40 | 速度列无硬件标注(GPU/显存) | 图表 | 🟡 次要 | Tab.IV | 补 GPU 类型/显存 | ✅ 已修:Tab.IV caption 显式说明速度数字在各源论文硬件(GPU/分辨率/batch/backbone)下异质报告、不可直接比较、仅示意相对数量级;避免编造统一硬件基准(超出综述范围);与 R41(real-time 标注)一致;pdflatex 通过 | ✅ 已修 |
| 41 | VToonify 表 IV "RT" 与 22ms/8B 混乱 | 图表 | 🟡 次要 | Tab.IV | 统一速度标注,注明 real-time 基准 | ✅ 已修:VToonify 速度格 "$\bigstar$~RT" 改 "$\bigstar$~real-time",与表内其他条目(~130ms/~0.6s/~sec)标注风格一致,消除歧义;pdflatex 通过 | ✅ 已修 |
| 42 | One-Step 节标注 "SOTA" 带偏见 | 写作 | 🟡 次要 | Sec.3.5 | 改中性表述 | audit B3 命中 L206 'SOTA' | ✅ 已修:OmniStyle-1M 段 "six state-of-the-art (SOTA) transfer models" 改中性 "six strong transfer models";pdflatex 通过 | ✅ 已修 |
| 43 | 伦理段过度膨胀(EU AI Act+GDPR 复述,与 PST 关联松) | 组织 | 🟡 次要 | Sec.9? | 减为 1-2 段 cross-link Sec.5/6 | ✅ 已修:伦理子节由 ~2 段含 EU AI Act/GDPR 复述,压缩为 1 段,聚焦 PST 直接相关两项义务(透明水印/生物特征隐私),并 cross-link 至 Sec.6 数据集隐私 与 Sec.5 Golden Protocol 披露要求;pdflatex 通过 | ✅ 已修 |
| 44 | 缺独立 Benchmark 对比章 + PRISMA 流程图 | 组织 | 🟠 主要 | Sec.5/7 | 增 benchmark 对比章 + 流程图 | ✅ 已修(诚实scope说明):PRISMA 漏斗已在 R30 表格化(Tab.prisma);新增 Sec.5 末 "Benchmark Scope and Limitations" 子节,明确本综述提供定性能力矩阵(Tab.comparison_matrix)+指标频率(Tab.metric_usage),但**不**伪造统一数值 leaderboard(需重跑所有方法于同一协议,超出综述范围且源论文协议异质),将 Golden Protocol 的执行定位为未来工作/社区采用;pdflatex 通过,19pp | ✅ 已修 |
| 45 | 缺相关综述区分(Fan TVCG24 / Garcia CGF24 / Zhang2025 decade survey) | 新颖性 | 🟡 次要 | Sec.1 | 增 related-work 小节 + 对比表 | ✅ 已修(差异化措辞强化):L64 在既有 Kyprianidis/Jing/Xia 三引文基础上,显式对比本综述增量——相对 NPR/NST 综述限定"人像"且以身份保持为核心约束;相对 inversion 综述覆盖至 2024-25 生成范式(diff/AR/video/3D)并贡献 Trilemma + Golden Protocol;未臆造 Fan TVCG24 / Garcia CGF24 / Zhang2025 条目(前者作者/venue 未核实、Zhang2025 decade survey 已在 R29 因"非肖像专述"删除,避免重复引入);pdflatex 通过 | ✅ 已修 |
| 46 | 缺正式 Appendix(PRISMA 图/完整方法清单/benchmark 代码) | 组织 | 🟡 次要 | 文末 | 增 Appendix | ✅ 已修:新增 Appendix 两节——(A) PRISMA Screening Detail(展开 Tab.prisma 漏斗的 480/160 dup/140 排除/115+ 终库数字与排除理由);(B) Surveyed Method Checklist(完整 ~90 方法 corpus 由策展 BibTeX 维护、各范式覆盖 ~12/25/45/10 + 3D/video 前沿);置于 bibliography 前;pdflatex+bibtex 通过,19pp | ✅ 已修 |
| 47 | 无代码/数据可用性声明 | 规范 | 🟡 次要 | 文末 | 补 Data/Code Availability | ✅ 已修:新增独立子节 "Data and Code Availability"(Sec.9,L637 前),明确本综述不产新数据/代码、所有方法数据集引自原始源、BibTeX 与能力矩阵可合理索取;audit E4 由弱命中升级为显式声明;pdflatex 通过 | ✅ 已修 |
| 48 | OmniStyle-1M 整句逐字重复两次(L542 & L556) | 重复 | 🟡 次要 | Sec.5 | 合并为一处 | ✅ 已修:L584 逐字重复句删除,改为 forward-reference 至 Sec.6.2(OmniStyle-1M 段)的偏差缓解说明;现仅 L570 保留原句一处;pdflatex 通过 | ✅ 已修 |
| 49 | Table V LPIPS 对经典 NST 标 "Common"(LPIPS 2018 才提出) | 事实错误 | 🟡 次要 | Tab.V | 改 Rare/N-A,注明现代 retrospectively 应用 | ✅ 已修:LPIPS 行 NST 列由 "Common" 改 "N/A*";caption 加脚注说明 LPIPS(Zhang 2018)晚于经典 NST(Gatys 2015-16),仅后期 retrospectively 应用;pdflatex 通过 | ✅ 已修 |
| 50 | "Structure/Texture Masters" 二分法仍需在 abstract/conclusion 加 caveat(reviewer 仍认为自相矛盾) | 写作 | 🟡 次要 | Abstract / Sec.8 | 确保已加 caveat;考虑改 continuum | ✅ 已验证:caveat 已存在 — L23 abstract "though modern hybrid methods increasingly blur this boundary";L645 conclusion "this dichotomy is a historical generalization rather than a strict partition... boundary continues to blur as hybrid designs emerge" | ✅ 已修 |

## 表格 / 结构 TODO（2026-07-14 补充，对标 5 篇 Zotero `survey`）

> 背景：与 Zotero `survey` 收藏 5 篇综述对标后，补结构范式（图/表/定义/实践指南）。详见 `review-stage/SURVEY_STRUCTURE.zh.md`、`STRUCTURE_PLAN.zh.md`、`GAP_AND_HANDOFF.zh.md`。

### Archived（已实现）
| # | 项 | 说明 | 提交 | 状态 |
|---|---|---|---|---|
| T1 | Table III (`tab:unified_paradigms`) 重设计 | 新增 *Representative methods* 列，逐范式补具体被引方法（Gatys/AdaIN/Johnson；StyleGAN/BlendGAN/DualStyleGAN；LDM-SD/IP-Adapter/InstantID；StyleTokenizer/EditAR/VAR）；`tabularx` 消除 280pt 溢出 | 451cb0a | ✅ |
| T2 | PRISMA 表 (`tab:prisma`) | `table`→`table*`，修复 75pt 单列溢出 | daf4f9e | ✅ |
| T3 | Trilemma 三轴术语统一 | Identity Preservation / Stylization Strength / Computational Efficiency；同步 `tab:trilemma_paradigms` 表头与图注 | daf4f9e | ✅ |
| T4 | 新增 3 篇前沿引用落正文 | shiri2019（身份恢复）、zhang2026 TeleStyle（内容保持）、he2026 StyleGallery（免训练语义感知） | 451cb0a / 3cafe71 | ✅ |
| T5 | 时间线图 + taxonomy 树图 | `fig:pst_timeline`（已纳入，待人工目检）、`fig:pst_taxonomy`（TikZ 三轴） | daf4f9e | ✅（图） |
| T6 | PST 形式化 Definition 1 + 实践指南 G1–G7 | Introduction / Discussion | daf4f9e | ✅ |

### Pending（待做，交接 Prism）
| # | 项 | 优先级 | 说明 |
|---|---|---|---|
| T7 | 人工目检 `images/timeline.png` / 必要时矢量重绘 | P1 | 模型无法看图，需人工确认节点与范式覆盖（NST→GAN→Diffusion→AR→video/3D）；否则重绘 TikZ 与 `fig:pst_taxonomy` 同风格 |
| T8 | 补年份排序 PST 里程碑总览表（对标 Decade Survey Table 1） | P1 | 与 `tab:method_overview` 互补（后者未按年份）；四列 Year / Method / Venue / Innovation |
| T9 | Table IV (`tab:trilemma_paradigms`) 补具体方法示例 | P2 | 目前仅范式级评级（★▲●），可加每行 1–2 代表方法 |
| T10 | 应用域索引表 / 附录方法全表 | P3 | 对标 Decade Survey Table 7，压缩规模；附录可出 ~90 方法精简全表 |
| T11 | 表编号与引用一致性复核 | P3 | 运行 `refine-logs/audit.sh` 确认 A5=0；核对 Table I–IX 编号 |

## 评审意见（参考）

| # | 维度 | 评价 |
|---|------|------|
| R1 | 论文概要 | 系统综述 2015–2025 十年人像风格迁移，覆盖 ~115 篇文献 / ~90 种方法。提出"人像编辑三难困境"(Identity Preservation / Editing Fidelity / Inference Speed) 作为统一分析框架，以及 Multi-Pillar Golden Protocol。主题有实效性，覆盖广泛，但距离 TVCG 标准在若干关键维度仍有差距 |
| R2 | 技术深度与数学严谨性 | 优点：关键公式统一了不同范式优化目标。不足：(a) 扩散模型 SDE/DDIM 采样过程缺形式化推导；(b) GAN latent inversion (W/W+) 讨论简略，缺 PTI 数学表述；(c) Trilemma 未形式化为可量化 Pareto frontier；(d) 视频时域一致性缺光流 warping loss 等公式 |
| R3 | 分类体系与全面对比 | 优点：按生成机制分类具有逻辑一致性。关键缺失：未提供任何结构化方法对比表，仅 Table I 年表信息密度不足 |
| R4 | 评估方法论 | 优点：Golden Protocol Multi-Pillar 方向正确。不足：缺用户研究设计方法论讨论、ArtFID 等指标局限分析、MLLM-as-judge 仅一笔带过、缺标准评估基准对比表 |
| R5 | 开放挑战与未来方向 | 优点：识别了 3D/NeRF/3DGS、视频一致性、伦理等前沿方向。不足：缺与经典图形学变形方法 (ARAP/MLS) 的联系、交互编辑未讨论蒸馏/量化/edge 部署、方法论融合展望不够深入 |
| R6 | 最终建议 | Major Revision（大修） |
