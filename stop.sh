#!/usr/bin/env bash
# stop.sh - 將目前內容轉成靜態檔：從 .md 產生 data/*.json 並建置模板
# 使用方式：在停止 Netlify Dev (Ctrl+C) 後執行 ./stop.sh，再 commit 即可
# 說明：news/_posts、activities/_posts、faculty/_profiles 的 .md 為來源；本腳本會更新 data/*.json 與建置後的 HTML

set -e
cd "$(dirname "$0")"
REPO_ROOT="$(pwd)"

echo "==> 將更新結果轉成靜態檔..."

echo "  - 從 news/_posts/*.md 產生 data/news.json"
python3 scripts/data/generate-news-json.py

echo "  - 從 activities/_posts/*.md 產生 data/activities.json"
python3 scripts/data/generate-activities-json.py

echo "  - 從 faculty/_profiles/*.md 產生 data/faculty_data.json"
python3 scripts/data/generate-faculty-json.py

echo "  - 建置模板 (build-templates.py)"
python3 build-templates.py

echo ""
echo "==> 完成。data/*.json 與建置後的 HTML 已更新，可執行 git add / commit 提交變更。"
