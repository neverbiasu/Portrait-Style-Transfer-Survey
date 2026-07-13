#!/usr/bin/env bash
# audit.sh — 人像风格迁移综述 机械审核 (POSIX/macOS portable, no GNU -P)
# 用法: ./audit.sh            (跑全部)
#       ./audit.sh --cite-keys --unused-bib --dup-lines ...
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEX="$ROOT/main.tex"
BIB="$ROOT/references.bib"
RUN_ALL=1
FLAGS=()
for a in "$@"; do RUN_ALL=0; FLAGS+=("$a"); done
has_flag(){ [ "$RUN_ALL" = 1 ] && return 0; for f in "${FLAGS[@]}"; do [ "$f" = "$1" ] && return 0; done; return 1; }

# bib keys
grep -E '^@[a-zA-Z]+\{' "$BIB" | sed -E 's/^@[a-zA-Z]+\{//; s/,.*//' | sort -u > /tmp/bibkeys.txt
# cited keys (split multi-cite)
grep -oE '\\cite[tp]?\*?\{[^}]*\}' "$TEX" \
  | sed -E 's/\\cite[tp]?\*?\{//; s/\}//' \
  | tr ',' '\n' | sed 's/^ *//; s/ *$//' | sort -u > /tmp/cited.txt

echo "=== audit.sh : $TEX ==="; echo

if has_flag --cite-keys || has_flag --all; then
  echo "[A1] cite keys in main.tex NOT in references.bib:"
  miss=$(comm -23 /tmp/cited.txt /tmp/bibkeys.txt)
  if [ -z "$miss" ]; then echo "  OK: all cite keys resolve"; else echo "$miss" | sed 's/^/  MISSING: /'; fi
  echo
fi

if has_flag --unused-bib || has_flag --all; then
  echo "[A5] bib entries NOT cited in main.tex:"
  un=$(comm -13 /tmp/cited.txt /tmp/bibkeys.txt)
  if [ -z "$un" ]; then echo "  OK: no uncited bib entries"; else echo "$un" | sed 's/^/  UNUSED: /'; fi
  echo
fi

if has_flag --and-others || has_flag --all; then
  echo "[A6] author lists with 'and others' (TVCG/TOG: list to 6th + et al):"
  grep -n "and others" "$BIB" | sed 's/^/  /'
  echo
fi

if has_flag --preprint-label || has_flag --count || has_flag --all; then
  echo "[A7/B1] preprint-like entries (contain 'arXiv' or lack journal&booktitle):"
  # extract key + whether it has arXiv / journal / booktitle
  awk 'BEGIN{RS="@"} {
    if ($0 ~ /^[a-zA-Z]+\{/) {
      k=$0; sub(/^[a-zA-Z]+\{/,"",k); sub(/,.*/,"",k);
      has_arxiv=($0 ~ /arXiv/);
      has_j=($0 ~ /journal[[:space:]]*=/);
      has_b=($0 ~ /booktitle[[:space:]]*=/);
      if (has_arxiv || (!has_j && !has_b)) print "  PREPRINT?: " k;
    }
  }' "$BIB"
  total=$(grep -cE '^@' "$BIB")
  pre=$(awk 'BEGIN{RS="@"} {
    if ($0 ~ /^[a-zA-Z]+\{/) {
      h=($0 ~ /arXiv/); j=($0 ~ /journal[[:space:]]*=/); b=($0 ~ /booktitle[[:space:]]*=/);
      if (h || (!j && !b)) c++;
    }
  } END{print c+0}' "$BIB")
  echo "  bib total=$total  preprint-like=$pre  peer-reviewed(est)=$(($total-$pre))"
  echo "  body: 'preprint' hits=$(grep -ci 'preprint' "$TEX")  'peer-reviewed' hits=$(grep -ci 'peer-reviewed' "$TEX")"
  echo
fi

if has_flag --dup-lines || has_flag --all; then
  echo "[D3] verbatim-duplicated lines (len>40) in main.tex:"
  dups=$(awk 'length($0)>40{print}' "$TEX" | sort | uniq -d)
  if [ -z "$dups" ]; then echo "  OK: no dup lines"; else echo "$dups" | sed 's/^/  DUP: /'; fi
  echo
fi

if has_flag --absolutes || has_flag --all; then
  echo "[B3] absolute-adjective candidates (verify evidence/caveat):"
  grep -noiE '(unbiased|theoretically optimal|state-of-the-art|[^a-z]SOTA|optimal|flawless|perfect)' "$TEX" | sed 's/^/  /'
  echo
fi

if has_flag --orphan-paradigm || has_flag --all; then
  echo "[C2] paradigm terms — body hits:"
  for p in "Flow Mapping" "flow mapping" "Autoregressive" "autoregressive" "Neural ODE" "Score-based" "Diffusion"; do
    echo "  '$p': $(grep -c "$p" "$TEX")"
  done
  echo "  tab: labels present:"; grep -oE 'tab:[a-z_]+' "$TEX" | sort -u | sed 's/^/    /'
  echo
fi

if has_flag --coverage || has_flag --all; then
  echo "[C3] must-cover 2024-25 SOTA (body hit count):"
  for m in PhotoMaker PULID LivePortrait ConsistentID MagicAnimate AnimateAnyone AnimateDiff GaussianHair 3DGS-Avatar DragGAN Barbershop JoJoGAN DCT-Net StyleShot; do
    printf "  %-16s %s\n" "$m" "$(grep -c "$m" "$TEX")"
  done
  echo
fi

if has_flag --availability || has_flag --all; then
  echo "[E4] Code/Data Availability statement:"
  echo "  hits=$(grep -ciE 'availability|data and code|code availability' "$TEX")"
  echo
fi

if has_flag --numbers || has_flag --all; then
  echo "[A2] number+cite locations (MANUAL verify vs cited table):"
  grep -noE '[0-9]+(\.[0-9]+)?[[:space:]]*\\cite' "$TEX" | sed 's/^/  /' | head -50
  echo
fi

echo "=== done. Per-rule: ./audit.sh --flag  (see RULES.md) ==="
