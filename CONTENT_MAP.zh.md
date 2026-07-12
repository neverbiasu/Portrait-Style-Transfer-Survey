# 论文内容对应表

> 用途：团队内部对齐论文各节内容覆盖与逻辑结构。
> 版本：对应 `main.tex`（2026-07-11），18 页，7 表 3 图。

---

## 总览

| 节 | 标题 | 页数 | 表 | 图 | 公式 |
|----|------|------|----|----|------|
| I | Introduction | ~2 | — | 2 (trilemma, timeline) | 1 (Pareto) |
| II | Theoretical Foundations | ~4.5 | 3 (glossary, unified, trilemma map) | — | 10+ (AdaIN, loss, PTI, SDE, DDIM, CFG, cross-attn, unified) |
| III | Methods & Method Taxonomy | ~3.5 | 1 (comparison matrix) | 1 (pipeline) | — |
| IV | Advanced Tasks | ~2 | — | — | 3 (warp, temp) |
| V | Evaluation | ~2 | 1 (metric usage) | — | — |
| VI | Datasets & Ethics | ~1.5 | 1 (datasets) | — | — |
| VII | Discussion | ~1 | — | — | — |
| VIII | Conclusion | ~1.5 | 1 (roadmap) | — | — |

---

## Sec I: Introduction

### I-A Technological Evolution（技术演进，行 31）
**内容**：从 NST → feed-forward → GAN → Diffusion → AR 的五阶段技术演进路线概述。

### I-B The Portrait Editing Trilemma: A Framework（三难困境框架，行 35）
**内容**：
- 定义 Trilemma 三个目标：Identity Preservation / Editing Fidelity / Inference Speed
- **Pareto 形式化**：$m$ Pareto-dominates $m'$ if $I_m ≥ I_{m'}$, $E_m ≥ E_{m'}$, $S_m ≥ S_{m'}$
- 定性映射各范式到帕累托前沿

### I-C Research Objectives and Contributions（目标与贡献，行 55）
**内容**：
- 三个贡献：统一分类法 / 失败模式分析 / Golden Protocol
- **PRISMA 漏斗**：480 → 320 → 180 → 115+，含 venue 分解计数
- 与三大已有综述的差异化声明

**图 1** `images/overview.png` — Trilemma 概念图 + 示意
**图 2** `images/timeline.png` — 机制中心时间线

---

## Sec II: Theoretical Foundations

**表 1** `tab:definitions_glossary` — 8 个核心术语定义

### II-A Separation of Style and Identity（风格/身份分离，行 105）
**内容**：
- Eq.(1) AdaIN: $Z_f = σ_s((Z_c-μ_c)/σ_c) + μ_s$
- 全局统计的局限性 → 语义感知表示（face parsing, landmark, StyleGAN W/W+）
- Self-attention vs cross-attention 假设

### II-B Loss Functions（损失函数，行 117）
**内容**：综述级损失函数框架 Eq.(2): $L_{total} = λ_{sty}L_{style} + λ_{con}L_{content} + λ_{id}L_{id} + λ_{geo}L_{geo}$

#### Identity Loss（行 127）
Eq.(3) $L_{id} = 1 - cos(F(I_{gen}), F(I_{src}))$

#### Reference-free Alignment（行 134）
CLIPScore 作为免参考度量

#### Geometric and Perceptual Losses（行 137）
Eq.(4) landmark loss: $L_{lmk} = Σ_i ‖P_i(I_{gen}) - P_i(I_{src})‖_2$

### II-C Early Image Processing Priors（早期图像处理先验，行 146）
**内容**：
- NPR 基础：Hertzmann Image Analogies, Winnemöller 实时视频抽象, Kyprianidis IB-AR 分类学
- 拉普拉斯金字塔 → 多尺度分解 → 特征统计假设的先驱

### II-D VAEs（行 153）
**内容**：VAE 隐空间采样、VQ-VAE 离散化、Latent Diffusion 中的 VAE 压缩模块

### II-E GANs（行 159）
**内容**：
- StyleGAN 架构 / W+ 反演 / pSp, e4e
- **PTI 二阶段优化** Eq.(5-6):
  - 阶段 1: $w^+ = argmin L_{LPIPS}(G(w), x) + λ_{L2}‖G(w)-x‖²₂$
  - 阶段 2: $min_{G'} ‖G'(w^+)-x‖²₂ + λ_{LPIPS}L_{LPIPS}(G'(w^+), x)$
- 引用 Xia et al. GAN inversion 综述

### II-F Flow Matching（流匹配，行 170）
**内容**：FlowEdit/SVRF/DVRF/FlowAlign，确定性 ODE 映射减少迭代步数

### II-G Diffusion Models（扩散模型，行 178）
**内容**：
- **正向 SDE** Eq.(7): $dx = f(x,t)dt + g(t)dw$
- **反向 SDE** Eq.(8): $dx = [f - g²∇log p_t]dt + g dw̄$
- **DDIM** Eq.(9): 确定性反向采样
- **CFG** Eq.(10): $\tilde{ε} = ε(x_t,t,∅) + γ[ε(x_t,t,c) - ε(x_t,t,∅)]$
- **Cross-attention** Eq.(11): $Attn(Q_s^i, W_K e_c, W_V e_c) = softmax(Q_s^i (W_K e_c)^T / √d_k) W_V e_c$
- Adapter alignment loss Eq.(12): $L_{align} = 1/N Σ_i ‖Q_f^i - Q_c^i‖²$
- Style moment-matching loss Eq.(13)

### II-H Unifying Framework（统一框架，行 217）
**内容**：提出 Eq.(14) 三分量分解 $x* = ℱ(Control(c), Prior(p_θ), Constraint(L))$

**表 2** `tab:unified_paradigms` — 四范式 Control/Prior/Constraint 实例化对照
**表 3** `tab:trilemma_paradigms` — 范式 × Trilemma 定性映射（★ ▲ ●）

---

## Sec III: Methods and Method Taxonomy

### III-A NST & Feature Transforms（行 276）
**内容**：
- Core: Gram 矩阵统计匹配 / AdaIN 前馈
- 代表方法(~12): Gatys, AdaIN, Deep Photo, Avatar-Net, AdaAttN
- 局限: Structural drift, 纹理 washed-out
- 引用 Selim（首个人像 NST）、Jing 综述

### III-B GAN-Based Architectures（行 290）
**内容**：
- Core: StyleGAN 反演 + 隐空间算术 / 双路径解耦
- 代表方法(~25): DualStyleGAN, pSp/e4e, AgileGAN, BlendGAN, StyleFace, VToonify
- DualStyleGAN FS2K 指标 + 83%/93% 用户偏好
- 局限: Domain lock-in

**图 3** `images/pipeline.png` — StyleGAN 反演工作流

### III-C Diffusion Models（行 313）
**内容**：
- Core: UNet cross-attention / self-attention K/V 替换 / Adapter
- 代表方法(~45): DreamBooth, Textual Inversion, InstantStyle, StyleAligned, IP-Adapter, InstantID, ControlNet, StyleMaster...
- 3 个子类: Fine-tuning / Training-free / Adapters
- 局限: 延迟大, Content leakage

### III-D Autoregressive Models（行 332）
**内容**：
- Core: VQ-VAE 离散 token → next-token/size prediction
- 代表方法(~10): VQGAN, MaskGIT, VAR, EditAR, Infinity
- EditAR CLIP Score (75.13) 定量
- 局限: Quantization artifacts

**表 4** `tab:comparison_matrix` — 14 个代表方法 × 7 维能力矩阵（新增）

---

## Sec IV: Advanced Stylization Tasks

> 导语（新增）：从 2D 全局 → 局部精细控制 → 视频时序 → 3D 多视角的递进逻辑

### IV-A Video Portrait Stylization（行 383）
**内容**：
- Flickering 问题
- **光流 warping loss** Eq.(15): $L_{warp} = Σ_t ‖φ(I_t) - 𝒲(φ(I_{t-1}), F)‖₁$
- **时序 VGG loss** Eq.(16): $L_{temp} = Σ_{t,l} ‖Φ_l(I_t) - Φ_l(𝒲(I_{t-1}, F))‖²₂$

#### StyleMaster（行 399）：Motion adapter + 全局投影
#### Style-A-Video（行 403）：Conditional guidance + attention maps
#### Baselines（行 407）：VToonify 等

### IV-B Local Editing & Makeup（行 413）
**内容**：Stable-Makeup / BeautyGAN / PSGAN / LADN

### IV-C 3D-Aware Stylization（行 425）
**内容**：3DToonify / StyleSplat / NeRF → 3DGS 转变

### IV-D Summary（行 440）
**内容**：引用 Table `tab:research_roadmap` 汇总开放挑战

---

## Sec V: Evaluation

**表 5** `tab:metric_usage` — 各范式指标使用频率调查（FID/LPIPS/ID/CLIP/ArtFID/UserStudy）

### V-A Golden Protocol（行 475）
**内容**：三项标准化配置（数据集/采样超参/报告格式）

### V-B Multi-Pillar Quantitative（行 489）
**内容**：
1. **ID Score**（ArcFace/CurricularFace）— 注：抽象风格下会自然退化
2. **ArtFID** — Eq. ArtFID = (1+LPIPS)·(1+FID) — 含局限性分析（LPIPS 非真实感偏置 / FID Inception 纹理敏感）
3. **CLIP Score** — CLIP-T / CLIP-I

### V-C Qualitative Evaluation（行 506）
**内容**：
- **2AFC / MOS 协议**：5-point Likert, 三维评分
- **方法论**：样本量 20-30 / 15+ pairs → 80% power @ α=0.05
- **MLLM-as-Judge**：Position bias / authority bias / 色彩饱和偏置 / 校准策略（multi-prompt aggregation, temperature averaging）
- **Failure Modes**（从 VII-C 移入）：Content leakage, Identity distortion, High-strength collapse

---

## Sec VI: Datasets, Privacy, Ethical Benchmarks

### VI-A Content & Style Datasets（行 532）
**内容**：FFHQ（opt-out）/ CelebA-HQ / Danbooru（版权风险）/ WikiArt / AAHQ

### VI-B OmniStyle-1M（行 542）
**内容**：大规模合成三元组范式，解决 ground-truth 稀缺

### VI-C Dataset Selection Guide（行 554）
**表 6** `tab:datasets_pst` — 8 个关键数据集汇总（含 License 状态）

---

## Sec VII: Discussion and Open Challenges

### VII-A Trilemma in Practice（行 588）
**内容**：部署中的具体操作点，非单一最优解

### VII-B Key Innovations（行 593）
**内容**：最新技术方向

#### Style—Identity Trade-off（行 597）：Statistical alignment hypothesis
#### Computational Efficiency（行 601）：Consistency distillation, fast samplers
#### Multimodal Control（行 605）：解耦条件机制, parameter-efficient adapters

### VII-C Ethics & Regulation（行 609）
**内容**：
- EU AI Act / GDPR / 人脸嵌入作为生物特征数据
- 非自愿合成媒体 / 深度伪造检测 / watermarking
- 双栈设计：生成质量控制 + 政策控制

---

## Sec VIII: Conclusion

### VIII-A Retrospective（行 622）
**内容**：从 NST 到扩散的 Trilemma 历史演化总结

### VIII-B Open Challenges（行 628）
**表 7** `tab:research_roadmap` — 4 个开放挑战 + 技术路线

1. 视频时序一致性（FlowAlign + 4D Gaussian）
2. 3D 几何风格化（3DGS + 去耦）
3. Content Leakage（CLIP 空间解耦）
4. 亚秒推理（单步蒸馏 + LCM）

### VIII-C Practical Deployment（行 668）
**内容**：从技术指标到 UX / 可解释控制 / fail-aware 设计

### VIII-D Limitations（行 671）
**内容**：跨协议比较困难、预印本更新快、广度优先于重现细节

---

## 附表: 全部引用统计

| 来源 | 数量 |
|------|------|
| CVPR | 28 |
| SIGGRAPH/TOG | 10 |
| ICCV | 8 |
| ECCV | 5 |
| NeurIPS/ICLR | 12 |
| TPAMI/其他期刊 | 10 |
| 其他会议 | 15 |
| arXiv 预印本 | ~28 |
| **合计** | **115+** |
