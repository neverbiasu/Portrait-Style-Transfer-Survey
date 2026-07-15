# Golden Protocol — Visual Gallery Spec

This document defines the **executed pilot** of the survey's proposed *Golden Protocol*
(Section 6) that produces the visual gallery (Fig. 1–3). It exists so the gallery is
reproducible and honestly scoped: a *representative subset* of PST methods on *unified*
inputs, **not** an exhaustive 90-method leaderboard.

## Deployed artifact
- `gallery/gallery.py` — the engine (downloads unified assets, runs methods, builds grids).
- `gallery/PST_Gallery.ipynb` — Colab notebook (free T4 GPU) that runs the engine.

## Unified inputs (Golden Protocol)
- **Content portrait**: one frontal, neutral portrait (public-domain; author may substitute
  a rights-clear portrait via Colab upload). All methods stylize *this same* image.
- **Style references**: one unified set of six public-domain paintings — StarryNight
  (Van Gogh), Scream (Munch), GreatWave (Hokusai), AmericanGothic (Wood), WaterLilies
  (Monet), Cubism (Picasso). All methods receive *this same* style set.

## Representative methods (spanning the survey's paradigms)
| Method | Paradigm | Mechanism |
|---|---|---|
| Gatys (2016) | Optimization-based | Per-image Gram-matrix optimization over VGG features |
| AdaIN (2017) | Feed-forward encoder | Real-time affine instance-norm alignment |
| IP-Adapter (2023) | Diffusion-based | Image-prompt adapter on Stable Diffusion v1.5 |

Each method is isolated in `try/except`; a failure yields a smaller grid, not a crash.
The grid therefore reports *whatever succeeded*, which keeps the gallery honest about
coverage.

## Outputs (written to `images/`)
| File | Figure | Content |
|---|---|---|
| `gallery_overview.png` | Fig. 1 | Paradigm highlight: unified content + one representative output per paradigm (StarryNight) |
| `gallery_grid.png` | Fig. 2 | Methods (rows) × Styles (cols) matrix; content in first column |
| `gallery_failures.png` | Fig. 3 | Failure modes: optimization drift (Gatys, hard style) vs controlled diffusion (IP-Adapter) |

## How to run
1. Open `gallery/PST_Gallery.ipynb` in Colab; Runtime → Change runtime type → GPU (T4).
2. Run all. Upload `gallery.py` when prompted (and optionally a content portrait).
3. Download the three PNGs; place in `images/`. Recompile the paper.

## Scope honesty (for the paper)
State explicitly: the gallery is a *pilot execution* of the Golden Protocol on a
representative subset, demonstrating the protocol's value (unified inputs expose
identity/stylization/structure trade-offs across paradigms). It is **not** a claim of
exhaustive benchmarking of all 90 surveyed methods; the full protocol remains a call for
community adoption, consistent with the survey's positioning.

## Status / validation
- Engine validated locally on Apple MPS: Gatys produced a real 256px stylization
  (~93s for 40 LBFGS steps). The full grid (6 styles x 250 steps) is practical on a
  Colab free T4 GPU (a few minutes) but too slow for local CPU/MPS at scale.
- The six canonical style references are public-domain Wikimedia paintings; Wikimedia
  is blocked from the authoring sandbox but downloads normally on Colab, so the
  canonical figures are produced by the Colab notebook, not locally.
- Until the Colab run completes, `images/gallery_*.png` are labelled placeholders.

