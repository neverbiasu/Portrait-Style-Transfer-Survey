# Zotero `survey` Collection — Citation Alignment Report

**Date:** 2026-07-14
**Reviewer:** current model (no Codex/gemini MCP configured; Zotero used as ground-truth source)
**Review method:** Zotero-grounded citation audit. The `survey` collection in the local
Zotero library (`~/Zotero/zotero.sqlite`, recovered via online backup) is treated as the
authoritative reference set. Its 5 entries were extracted with canonical metadata
(authors, year, venue, volume/pages, DOI) and diffed against `references.bib` + `main.tex`.

## Zotero `survey` collection (collectionID=24) — 5 items

| # | Zotero title | Canonical authors (Zotero) | Venue / year | DOI |
|---|---|---|---|---|
| 1 | Personalized Image Generation with Deep Generative Models: A Decade Survey | Y. Zhang, Y. Wei, Z. Ji, W. Zuo, L. Zhang, Y. Zheng, M. Liu | Comput. Visual Media 11:1141–1194, 2025 | 10.26599/CVM.2025.9450495 |
| 2 | Style Transfer Review: Traditional Machine Learning to Deep Learning | Y. Xu, M. Xia, K. Hu, S. Zhou, L. Weng | Information 16(2):157, 2025 | 10.3390/info16020157 |
| 3 | Style Transfer: A Decade Survey | T. Zhang, H. Tang | arXiv:2506.19278, 2025 | 10.48550/arXiv.2506.19278 |
| 4 | Image neural style transfer: A review | Q. Cai, M. Ma, C. Wang, H. Li | Comput. Electr. Eng. 108:108723, 2023 | 10.1016/j.compeleceng.2023.108723 |
| 5 | Advances in 3D Neural Stylization: A Survey | Y. Chen, G. Shao, K. C. Shum, B.-S. Hua, S.-K. Yeung | IJCV 133:5026–5061, 2025 | 10.1007/s11263-025-02403-9 |

## Findings (diff against manuscript)

| Zotero item | In `references.bib`? | Cited in `main.tex`? | Action taken |
|---|---|---|---|
| 1 Personalized Image Gen. Decade Survey | **absent** | **absent** | Added `zhang2025personalized`; cited in methodology paragraph |
| 2 Style Transfer Review (ML→DL) | **absent** | **absent** | Added `xu2025stylereview`; cited in methodology paragraph |
| 3 Style Transfer: A Decade Survey | **absent** (R2 gap) | **absent** | Added `zhang2025decadesurvey`; cited in methodology paragraph |
| 4 Image neural style transfer: A review | **absent** (we had a *different* NST review: `jing2020neural`) | **absent** | Added `cai2023imagestyle`; cited in NST section |
| 5 Advances in 3D Neural Stylization | **absent** | **absent** | Added `chen20253dstylization`; cited in 3D-aware section |

**Additional norm defect found during alignment:**
- Venue typo in methodology paragraph: `ECCCV (5)` → corrected to `ECCV (5)`.
  (`ECCCV` is not a real venue; the venue list earlier correctly uses `ECCV`.)

## Notes / non-issues
- Our existing `jing2020neural` ("Neural Style Transfer: A Review", Jing et al., IEEE TVCG 2020)
  is a **legitimately different** paper from Zotero #4; both are now cited. Kept as-is.
- Zotero BBT citation keys are not pinned for these items, so matching was done by title/DOI.
- The `survey` collection holds only 5 items. Other clearly-relevant Zotero collections exist
  (e.g. `portrait_stylization` = 53 items, `new_buds` = 28+6, `diffusion` = 18, `ref` = 19) but
  were out of scope for this alignment pass per the requested `survey` directory.

## Result
- 5 canonical survey entries added to `references.bib` with Zotero-verified metadata.
- 4 positioning citations added to `main.tex` (methodology ×3, NST ×1, 3D ×1).
- 1 venue typo fixed.
- Compiles cleanly (pdflatex+bibtex); undefined refs = 0; A5 (cited-not-in-bib) = 0.
- Verdict: manuscript now aligns with the Zotero `survey` collection reference norms.
