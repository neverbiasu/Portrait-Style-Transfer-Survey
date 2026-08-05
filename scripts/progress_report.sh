#!/bin/bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROGRESS_FILE="$REPO_DIR/PROGRESS.md"
TODAY=$(date +%Y-%m-%d)
DAY_NAME=$(date +%A)

cd "$REPO_DIR"

TOTAL_TODOS=$(grep -c '| [0-9]* |' TODO.md | tail -1)
DONE_TODOS=$(grep -c '✅' TODO.md || true)
PENDING_TODOS=$((TOTAL_TODOS - DONE_TODOS))

PDF_PAGES=$(grep -c '\\newpage' main.tex 2>/dev/null || echo "unknown")
BIB_COUNT=$(grep -c '@' references.bib 2>/dev/null || echo "unknown")
CITED_COUNT=$(grep -oE '\\cite\{[^}]+\}' main.tex 2>/dev/null | grep -oE '\{[^\}]+\}' | tr -d '{}' | tr ',' '\n' | sort -u | wc -l 2>/dev/null | tr -d ' ' || echo "unknown")

GIT_COMMITS=$(git log --oneline -1 | head -1 || echo "no commits")
GIT_UNSTAGED=$(git status --short 2>/dev/null | wc -l || echo "0")

cat >> "$PROGRESS_FILE" << EOF

## ${TODAY} (${DAY_NAME})

### 每日进展
<!-- 在此处填写今日完成的任务 -->

### 当前状态
| 维度 | 数值 |
|------|------|
| 论文页数 | ${PDF_PAGES} |
| 参考文献 | ${BIB_COUNT} 条 |
| 正文引用 | ~${CITED_COUNT} 个 |
| TODO 总项 | ${TOTAL_TODOS} |
| TODO 已完成 | ${DONE_TODOS} |
| TODO 待完成 | ${PENDING_TODOS} |
| 未提交更改 | ${GIT_UNSTAGED} 个文件 |
| 最新提交 | ${GIT_COMMITS} |

### 离投稿/发表还差什么
| 障碍 | 说明 | 预计解决时间 |
|------|------|-------------|
| 画廊视觉结果 | G4–G5 待 Colab 跑图 | 1–2 天 |
| 剩余 TODO | T7–T11 结构/表改进 | 1–2 天 |
| 最终审校 | 4 轮审稿意见逐条核对 | 0.5 天 |
| arXiv 预印本 | 提交 arXiv + 补充 artifact 链接 | 1 天 |
| 投稿 | 选 venue + 格式化投稿 | 1–2 周 |
EOF

echo "Progress entry appended to $PROGRESS_FILE"
echo "Edit the '每日进展' section above with today's updates."