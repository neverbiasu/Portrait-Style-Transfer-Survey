# Portrait Style Transfer Survey — Review Synthesis (4 Reviewers)

> 合成自: NotebookLM 深度评审 + 3 份人工 Reviewer(Rev1/2/3/4)。
> 日期: 2026-07-13。阶段: timeline 已删、gallery 路线弃、LaTeX 可编译。
> ⚠️ 重要: 4 份 review 中**含幻觉**,已逐条用 `references.bib` + `main.tex` 交叉核验。
> 被证伪的 review 指控(不要采纳):
> - Rev4 "Table III 空白" → 假。trilemma 映射表(tab:trilemma_paradigms)有完整 ★/▲/● 内容。
> - Rev4 "StyleAligned 标 CVPR2023" → 假。bib 中 `hertz2023styleai` 实为 2024。
> - Rev1 "StyleID ArtFID 引到 StyleMaster 与原文是两篇" → 半真。StyleMaster 确实不是 StyleID 来源;但**真正问题**是 bib 里**根本没有 StyleID 独立条目**,line 208 把 InstantStyle+StyleID 两个数字都挂到 `ye2024stylemastersy`(视频论文),属错引。

---

## 📊 4-Reviewer 意见汇总矩阵

图例:R1/R2/R3/R4 = 4 位 Reviewer 是否提出(✓/—);**Severity**: F=致命 M=重要 m=次要;**Verified**: ✓=经 bib/正文核验为真 ✗=核验为 review 幻觉 ⚠️=部分真/需作者再核。

| # | 独立问题 | R1 | R2 | R3 | R4 | Sev | Verified |
|---|----------|----|----|----|----|-----|----------|
| 1 | Trilemma 末段脚注4篇引文错挂(4篇均非三角框架来源) | ✓ | — | (术语未定义) | ✓ | **F** | ✓ 真 |
| 2 | ArtFID 数字不可溯源(AdaIN 31.85 / InstantStyle 42.48 / StyleID 38.57;后者错引视频论文 StyleMaster,且 bib 无 StyleID 条目) | ✓ | — | — | ✓ | **F** | ✓ 真(31.85 编造;42.48/38.57 错引) |
| 3 | "115+ peer-reviewed" 统计矛盾(含 28 arXiv 预印本未扣) | ✓ | — | ✓ | ✓ | **F** | ✓ 真 |
| 4 | 2024-25 SOTA 大规模漏引(PhotoMaker/PULID/LivePortrait/ConsistentID/MagicAnimate/AnimateAnyone/AnimateDiff/GaussianHair/3DGS-Avatar/DragGAN/Barbershop 等) | — | ✓ | (隐) | — | **M** | ✓ 真 |
| 5 | "Structure Masters vs Texture Masters" 二分法被自身否定(Sec.7 自承 diffusion 保身份) | ✓ | — | ✓ | ✓ | **M** | ✓ 真 |
| 6 | bib 中 10 条未被正文引用(artflow/jojogan/MUNIT/NeRF-Art 等) | ✓ | — | — | — | **M** | ✓ 真 |
| 7 | PRISMA 声明 vs 28 预印本 + 无 formal inclusion/exclusion + 漏斗空(仅3行) | ✓ | — | ✓ | ✓ | **M** | ✓ 真 |
| 8 | Puff-Net(2D NST)错归类进 3D rigging 语境(Sec.4.3) | — | ✓ | — | — | **M** | ✓ 真 |
| 9 | MOS/2AFC 框架错引 ambiel2023 预印本(streijl2016 已在 bib 却用错) | — | ✓ | ✓ | — | **M** | ✓ 真 |
| 10 | NST "theoretically unbiased" 过度宣称(VGG 有 ImageNet 偏置) | — | ✓ | — | — | m | ✓ 真 |
| 11 | Flow Matching 在 II-F 引入却被排除于 III 分类法 + 对比表 | — | ✓ | ✓ | — | **M** | ✓ 真 |
| 12 | yang2023zeroshotcl 错挂 CLIPScore 段(实为 training loss) | — | ✓ | — | — | m | ✓ 真 |
| 13 | 数据集表许可/数字错(Danbooru BSD 错;WikiArt 引错;AAHQ 缺 bib;CelebAMask-HQ 引错;FFHQ 许可) | — | ✓ | ✓ | — | **M** | ✓ 真 |
| 14 | bib 作者写 "and others" → TVCG/TOG 要求列全至第6 + et al. | — | ✓ | ✓ | — | m | ✓ 真 |
| 15 | 分类法不对称(NST 算法 vs GAN/Diff/AR 架构并列) | — | ✓ | — | — | m | ✓ 合理 |
| 16 | Golden Protocol 仅提议未执行,无统一 benchmark | — | — | ✓ | — | **M** | ✓ 真 |
| 17 | **Table III(trilemma 映射)空白** | — | — | ✓ | ✓ | (F?) | **✗ 幻觉**(表有完整 ★/▲/● 内容) |
| 18 | **StyleAligned 标 CVPR2023** | — | — | ✓ | ✓ | (M) | **✗ 幻觉**(bib `hertz2023styleai` 实为 2024) |
| 19 | 速度列无硬件标注(GPU/显存) | — | — | ✓ | — | m | ✓ 真 |
| 20 | VToonify 表 IV "RT" 与 22ms/8B 混乱 | (RT vs 22ms) | — | ✓ | — | m | ✓ 真 |
| 21 | One-Step 节标注 "SOTA" 带偏见 | — | — | ✓ | — | m | ✓ 真 |
| 22 | 伦理段过度膨胀(EU AI Act+GDPR 复述,与 PST 关联松) | — | — | ✓ | — | m | ✓ 真 |
| 23 | 缺独立 Benchmark 对比章 + PRISMA 流程图 | (隐) | — | ✓ | — | **M** | ✓ 真 |
| 24 | 缺相关综述区分(Fan TVCG24 / Garcia CGF24 / Zhang2025 decade survey) | — | — | ✓ | — | m | ✓ 真 |
| 25 | 缺正式 Appendix(PRISMA 图/完整方法清单/benchmark 代码) | — | — | ✓ | — | m | ✓ 真 |
| 26 | 无代码/数据可用性声明 | — | — | ✓ | — | m | ✓ 真 |
| 27 | OmniStyle-1M 整句逐字重复两次(L542 & L556) | — | — | — | — | m | ✓ 真(我 grep 确认) |
| 28 | Table V LPIPS 对经典 NST 标 "Common"(LPIPS 2018 才提出) | — | — | — | ✓ | m | ✓ 真 |

**汇总统计**:4 位共提出(去重后)28 项;其中 **25 项核验为真**、**2 项证伪为幻觉(#17,#18)**、1 项(#15)属合理改进建议。
致命(F)3 项:#1、#2、#3。重要(M)11 项。次要(m)14 项。
跨 3+ Reviewer 共识(高优先级):#1、#3、#5、#7。

---

## 综合评分(各 reviewer 口径不一,取保守中位)
- 核心贡献新颖性: 2/5 — Trilemma 是已有 trade-off 的形式化,非原创框架
- 事实准确性: 2/5 — 多个 ArtFID 数字不可溯源
- 引文准确性: 2/5 — 多处错挂/灌水
- 覆盖完整性: 2.5/5 — 2024-25 SOTA 大量漏引
- 结构组织: 3/5 — 架构合理,Golden Protocol 未执行
- **总评: Reject & Resubmit 区间**(TVCG/TOG 标准)。需先修事实/引文,再补覆盖,方可重投。

---

## 🔴 致命 / 必须改 (Must-fix)

### C1. 多处 ArtFID 量化数字疑似编造/不可溯源
| 位置 | 数字 | 所引 | 问题 |
|------|------|------|------|
| Sec.3.1 L278 | AdaIN ArtFID=31.85 (StyleInV) | `chung2023styleii` | StyleInV 非公开基准名;AdaIN(2017)早于 ArtFID(2022);该文是 Style Injection in Diffusion,不报 AdaIN 数字 |
| Sec.2.7 L206-208 | InstantStyle=42.48 / StyleID=38.57 | `ye2024stylemastersy`(StyleMaster,视频) | StyleMaster 非二者来源;**bib 无 StyleID 独立条目**;数字在原文查无 |
- 修复: 三数字**全部删除**或替换为可在原 paper 表格精确 trace 的真实值;补 StyleID 独立 bib 条目。

### C2. Trilemma 框架脚注四篇引用全部错挂
- 位置: Sec.1.2 末 `\cite{wang2024instantstyle,wang2025domaingp,yang_2022_cvpr,wright2022artfidqe}`。
- 问题: 这四篇**没有一篇**提出/讨论 Trilemma 或 Impossible Triangle 作为分析框架。属引文灌水。
- 修复: 删除该脚注引用,或改为真正讨论 editing trade-off 的工作;若坚持 Trilemma 为本文原创,明写 "We coin the term..." 并删误导引用。

### C3. 2024-2025 核心 PST 方法大规模漏引(正文有 bib 却没有展开)
- 漏: **PhotoMaker**(CVPR2024)、**PULID**(NeurIPS2024)、**LivePortrait**、ConsistentID、MagicAnimate、AnimateAnyone、AnimateDiff、DragGAN/DragDiffusion、Barbershop、GaussianHair/3DGS-Avatar/HumanGaussian 等。
- 修复: 每类补 3-5 篇近 2 年顶会代表;Sec.3-C 增 "Recent IP-preserving Diffusion (2024-25)";Sec.4 各节扩到 8-10 篇。

### C4. "115+ peer-reviewed" 统计口径矛盾
- 问题: 正文 venue 分解含 28 篇 arXiv preprint(非 peer-reviewed);扣除后 peer-reviewed ≤88,与 "115+" 冲突。摘要 "~90 methods" 与 Sec.7 "≈90" 措辞不一。
- 修复: 明确分层报告(88 peer-reviewed + 28 preprint = 116);摘要改为 "over 110 publications" 或区分两类。

### C5. bib 中 10 条未被正文引用(引而不用)
- `artflow, gal2021stylegannada, gpunit_paper, huang2018multimodal(MUNIT), huang2022stylizednerf, jojogan, karras2021stylegan3, wang2022nerf, zh<|HYBRID_RESERVED_1|>2022inversionbasedst, zhang2025styletransferdecade`。
- 修复: 要么补讨论,要么删 bib。JoJoGAN/ArtFlow/GP-UNIT 对 GAN 有价值;NeRF-Art/StylizedNeRF 应入 3D 节;Zhang2025(decade survey)应在 related work 区分贡献。

---

## 🟠 重要 / 应改 (Should-fix)

### M1. PRISMA 声明与 28 arXiv 预印本自相矛盾
- Sec.1.3 写 "peer-reviewed works",但 24% 为 preprint;漏斗无 formal inclusion/exclusion、无检索引擎/日期。
- 修复: 摘要改 "archival venues + 28 screened preprints";PRISMA 漏斗表格化 + 检索式/引擎/日期。

### M2. "Structure Masters vs Texture Masters" 二分法被自身否定
- Sec.7 自承 IP-Adapter/InstantID(diffusion)也保身份 → 二分不成立。
- 修复: 弱化/改 continuum,加 caveat。

### M3. MOS/2AFC 框架错引 2023 预印本
- L504 把数十年心理测量框架错归 `ambiel2023portraitsa`;`streijl2016mean`(已在 bib)应用错。
- 修复: 删 ambiel 对 MOS/2AFC 的引用,改引经典心理测量文献。

### M4. NST "theoretically unbiased" 过度宣称
- L276 VGG 有明确量化偏置(ImageNet 纹理),称 "unbiased" 为假。
- 修复: 删该词,改为 "deep feature-space texture bias enables arbitrary style"。

### M5. Flow Matching 在 II-F 引入却排除在 III 分类法 + 对比表外
- 结构断裂。修复: 升为独立 paradigm 或并入 III-C diffusion 子节。

### M6. 分类法不对称: NST(算法/损失)与 GAN/Diff/AR(架构)并列不当
- 修复: 改名 "Optimization & Feed-Forward Autoencoders"。

### M7. `yang2023zeroshotcl` 挂错段
- L128 CLIPScore 段引了一篇 training-loss 论文(非评估指标)。
- 修复: 移到 Sec.3.3 zero-shot 段。

### M8. 数据集表(Table VI)许可/数字错标
- Danbooru 标 "BSD" → 实为 CC0/CC-BY-NC + 作者权保留;WikiArt 引 `wikiart`(Saleh&Elgammal 2015, ~80k 评估用)与社区用的 Nichol 2016(~100k 训练用)不符;AAHQ 缺对应 bib 条目;CelebAMask-HQ 引 `lee2020`(MaskGAN)应写明 "introduced in"。
- 修复: 逐条核对正确 arXiv/paper + 许可。

### M9. 表 V LPIPS 对经典 NST 标 "Common" 年代不可能
- LPIPS 2018 才提出,经典 NST(2015-17)不可能常用。
- 修复: 改 Rare/N-A,注明现代 retrospectively 应用。

### M10. OmniStyle-1M 整句逐字重复两次
- L542 与 L556 完全相同。修复: 合并为一处。

---

## 🟡 次要 / 加分 (Minor)

- **m11.** Trilemma 仅出现一次定性映射表,未在各 paradigm 章末复用为分析视角 → 改为 lens,逐章用三轴分析。
- **m12.** Golden Protocol 仅提议未执行 → 降级为 "Proposed Guideline" 或真跑 5-8 方法出统一表。
- **m13.** 多个 bib 条目作者写 "X and others" → TVCG/TOG 要求列全至第 6 位 + et al.
- **m14.** Puff-Net 归类错(2D NST 被放入 3D rigging 语境)→ 移 Sec.3.1。
- **m15.** 速度列 "<1s/RT/130ms" 无硬件标注 → 补 GPU 类型/显存。
- **m16.** 伦理/法规段近乎 EU AI Act+GDPR 法律复述,与 PST 关联松 → 减为 1-2 段 cross-link Sec.5/6。
- **m17.** 缺正式 Appendix(PRISMA 流程图 / 完整方法清单 / benchmark 代码)。

---

## 一句话结论
框架野心与覆盖组织超过多数 PST 综述,但 **Trilemma 几乎没用实、核心引文严重错挂、多个关键数字疑似编造、2024-25 SOTA 大量漏引**——这四点不修,TVCG/TOG 必 major revision 甚至 desk reject(编造参考文献风险高)。先修 C1-C5 + M1-M10,再补实质 benchmark,方可进 revision 接收区间。
