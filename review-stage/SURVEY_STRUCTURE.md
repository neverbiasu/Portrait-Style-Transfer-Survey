# Structural Deep-Dive: the 5 Zotero `survey` Papers

**Purpose:** Understand, for each of the 5 curated survey papers, its (a) section plan, (b) format/venue, and (c) figure & table arrangement — so we can borrow proven structural patterns for our *Portrait Style Transfer: A Decade Survey (2015–2025)*.

Data sourced from open-access full texts (arXiv ar5iv / HTML, MDPI, IJCV, Elsevier snippets). Paper #2 (MDPI) was bot-blocked; its shape is inferred from the DOI/venue and noted as such.

---

## 1. Personalized Image Generation with Deep Generative Models: A Decade Survey
**Wei, Zheng, Zhang, Liu, Ji, Zhang, Zuo** — arXiv:2502.13081 (CVM 2025, 39 pp.). `zhang2025personalized`

- **Format:** Journal *Review Article* (Computational Visual Media), **single-column**, ~39 pages, 300+ methods reviewed.
- **Section plan**
  1. Introduction  *(Fig 1: paper-count growth timeline, color-coded by paradigm; Fig 2: survey-organization taxonomy tree)*
  2. Problem Definition and Preliminary  *(2.1 Problem Definition; 2.2 Generative Models → GAN / T2I Diffusion / Multi-modal AR)*  *(Fig 3 generative models; Fig 4 AR)*
  3. Personalized Image Generation in **GANs**  *(3.1 Overview; 3.2 Inversion Space; 3.3 GAN Inversion Method [optimization/learning/hybrid]; 3.4 Latent-based Editing [navigation/text-driven])*
  4. Personalized Image Generation in **DMs**  *(4.1 Overview; 4.2 Inversion Space; 4.3 Concept Inversion [training-free/optimization/learning/hybrid]; 4.4 Personalized Generation [subject/face/character/style/high-level/multi-concept]; 4.5 Text-driven Editing)*
  5. Personalized Image Generation in **ARs**
  6. Evaluation  *(6.1 Dataset; 6.2 Metrics [concept fidelity / text editability / subjective])*
  7. Challenge and Future Directions  *(5 sub-axes)*
  8. Conclusion
- **Figures/Tables:** 4+ figures (growth timeline, **taxonomy tree of the whole survey**, model illustrations). Comparison/taxonomy tables per method family.
- **Signature device:** A **unified framework** (concept inversion + personalization = 3 components: *inversion spaces / inversion methods / personalization schemes*) that *drives the entire per-generative-model organization*, plus a **taxonomy-tree figure as the paper's spine**.

---

## 2. Style Transfer Review: Traditional Machine Learning to Deep Learning
**Xu, Xia, Hu, Zhou, Weng** — Information (MDPI) 2025, 16(2):157, DOI 10.3390/info16020157. `xu2025stylereview`

- **Format:** MDPI *Information*, **single-column**, open access, 2025. *(Full text was bot-blocked with HTTP 403; structure inferred from venue conventions + abstract.)*
- **Likely section plan** (MDPI review convention): Introduction → traditional / pre-deep style transfer → deep-learning (CNN/GAN/Diffusion) style transfer → applications → challenges/future.
- **Figures/Tables:** typical MDPI review carries 5–15 figures (pipeline diagrams, taxonomies) and 2–5 summary tables.
- **Signature device (expected):** A **historical/temporal arc** from classical ML to deep learning — i.e., organization *by era* rather than by generative family.
- **Caveat for our use:** treat the section breakdown as provisional until the PDF is opened in Zotero; the citation metadata in `references.bib` is already verified.

---

## 3. Style Transfer: A Decade Survey
**Zhang, Tang** — arXiv:2506.19278 (2025, under submission). `zhang2025decadesurvey`

- **Format:** arXiv preprint (journal-style double-column manuscript), reviews **500+ papers**.
- **Section plan**
  1. Introduction  *(1.1 Technological Evolution; 1.2 Research Objectives & Contributions)*  *(Fig 1: milestone timeline, color-coded by paradigm)*
  2. Fundamental Theories of Style Transfer  *(2.1 Style/Content separation; 2.2 Loss functions; 2.3 Hand-crafted; 2.4 VAE; 2.5 GAN; 2.6 Flow-Matching; 2.7 AR; 2.8 Diffusion)*  *(Fig 2: NST example)*
  3. Development & Application of Generative Models in Style Transfer  *(3.1 VAE; 3.2 GAN; 3.3 Diffusion; 3.4 AR)*
  4. Evaluation Metrics and Key Innovations  *(4.1 Metrics; 4.2 Techniques/Innovations)*
  5. Domain-specific Applications (portrait, video, text, 3D…)
  6. Datasets and Evaluation Methodologies
  - Appendices 9 (generative-model details), 10 (metric details)
- **Figures/Tables:** Fig 1 timeline, Fig 2 NST example. **Six tables**: Table I *chronological overview* (Year/Method/Venue/Innovation), Table II VAE variants, Table III GAN variants, Table IV Diffusion innovations (tree), Table V AR milestones, Table VI *evaluation benchmark* with multi-axis ratings (MC/AM/VQ/CE/R, ✓/✗ symbols).
- **Signature devices:** (a) **chronological overview table** (year-by-year, the workhorse of a "decade survey"); (b) **per-paradigm theory section** with explicit loss/formalism; (c) **evaluation benchmark table** scoring methods across axes; (d) **timeline figure**; (e) **appendices** holding exhaustive method lists.

---

## 4. Image neural style transfer: A review
**Cai, Ma, Wang, Li** — Comput. Electr. Eng. 2023, 108:108723 (Elsevier). `cai2023imagestyle`

- **Format:** Journal (Elsevier), **double-column**, 2023, 57 references.
- **Section plan** (from ScienceDirect snippets): Introduction *(Fig 1: field split into pre-CNN vs neural, as a diagram)* → "Style transfer for non-neural network" → CNN/neural style transfer reviewed **through the GAN lens** (principle details, advantages/disadvantages, performance evaluation) → future directions.
- **Figures/Tables:** Fig 1 (categorization diagram); ScienceDirect lists dedicated *Figures* and *Tables* sections.
- **Signature device:** A **binary temporal split (pre-CNN → CNN-era)** as the primary organizer, with **per-method pros/cons + performance evaluation** rather than a benchmark table.

---

## 5. Advances in 3D Neural Stylization: A Survey
**Chen, Shao, Shum, Hua, Yeung** — IJCV 2025, 133(8):5026–5061 (arXiv:2311.18328). `chen20253dstylization`

- **Format:** IJCV **double-column** journal (also arXiv); includes a **mini-benchmark** (experiments on selected mesh & neural-field methods).
- **Section plan**
  1. Introduction  *(1.1 Definition & Terminologies [formal Definition 1]; 1.2 Related Surveys)*  *(Fig 1: 3D representations; Fig 2: rendering pipelines; Fig 3: survey structure)*
  2. Background  *(2.1 NST [single/arbitrary/generative/linking 2D→3D]; 2.2 3D Content Generation [representations/generative models/diffusion priors])*  *(Fig 4: 2D NST pipelines; Fig 5: SDS)*
  3. 3D Neural Stylization  *(3.1 Taxonomy; 3.2 Mesh-based [geometric deformation/texture]; 3.3 Neural Field-based [feed-forward / optimization image-guided / text-guided]; 3.4 Volume; 3.5 Point Cloud; 3.6 Implicit Shape Editing; 3.7 Practical Guidelines)*
  4. Datasets and Evaluation  *(4.1 Datasets; 4.2 Criteria/Metrics; 4.3 Benchmark [settings/discussion])*
  5. Applications  *(5.1–5.5 asset design / avatar / NPR / PBR / industrial)*
  6. Open Challenges and Future Works  *(generalization / controllability / efficiency / 3D consistency / evaluation)*
  7. Conclusion
- **Figures/Tables:** 5 figures (representations, pipelines, structure, 2D-NST pipelines, SDS). Taxonomy table + **benchmark table with quantitative results**.
- **Signature devices:** (a) **taxonomy organized by 3D representation** (mesh/field/volume/point cloud); (b) a **formal Definition box**; (c) a **"Practical Guidelines" subsection** giving actionable tips; (d) a **real benchmark with experiments**; (e) a dedicated **Applications** section; (f) **challenges structured along 5 named axes**.

---

# Cross-Paper Synthesis → What to adopt in our PST Survey

| Structural pattern | Seen in | In our manuscript? | Action |
|---|---|---|---|
| **Taxonomy-tree / survey-organization figure** (spine of paper) | #1 (Fig 2), #5 (Fig 3) | Partial (we have Tab.IV capability matrix, not a tree figure) | Add a **survey-organization figure** mapping PST by generative mechanism × task axis |
| **Milestone timeline figure (2015–2025)** | #3 (Fig 1), #1 (Fig 1) | **Missing** | Add a **PST timeline figure** (NST→GAN→Diffusion→AR→3D/Video) — strongest single gap |
| **Chronological overview table** (Year/Method/Venue/Innovation) | #3 (Table I), #4 (implicit) | Partial (`tab:method_overview` exists but not year-ordered) | Add a **year-ordered PST overview table** |
| **Per-generative-paradigm organization** | all 5 | ✓ (NST/GAN/Diffusion/AR sections) | Keep — this is our strength |
| **Unified framework / formalism** | #1 (3-component framework), #5 (Definition 1), ours (Trilemma) | ✓ (Portrait Editing Trilemma) | Keep; consider a framed **Definition box** for "PST" |
| **Evaluation / Datasets / Metrics section** | #1 §6, #3 §4, #5 §4 | ✓ (evaluation + benchmark sections) | Keep |
| **Multi-axis capability/benchmark rating table** | #3 (Table VI), #5 (benchmark) | ✓ (`tab:comparison_matrix`) | Keep; cross-check rating symbols are defined |
| **Applications section** | #5 §5, #3 §5 | Partial (applications mentioned, no dedicated section) | Optional: a short "Applications & Deployment" subsection |
| **Challenges along named axes** | #5 §6 (5 axes), #1 §7 | ✓ (Discussion/Open Challenges) | Keep |
| **Appendices with exhaustive method lists** | #3 (Apps 9–10) | ✗ | Optional: appendix listing all ~90 surveyed methods |
| **Practical Guidelines / future tips** | #5 §3.7 | Partial | Optional: a "Guidelines for Practitioners" callout |

## Recommended concrete additions (highest leverage)
1. **Timeline figure** of PST milestones 2015–2025 (mirrors #3 Fig 1 / #1 Fig 1) — currently our biggest figure gap.
2. **Year-ordered overview table** complementing `tab:method_overview` (mirrors #3 Table I).
3. **Survey-organization taxonomy figure** as the paper's navigational spine (mirrors #1 Fig 2 / #5 Fig 3).
4. Optional **appendix** enumerating all ~90 methods for reproducibility (mirrors #3).
5. Optional short **Applications** subsection + **Definition box** for "Portrait Style Transfer" (mirrors #5).

These align our manuscript's *format and figure/table economy* with the strongest recent surveys while preserving our differentiators (Trilemma framework, portrait-specific focus, Golden Protocol).
