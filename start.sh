#!/usr/bin/env bash
# start.sh - 啟動本地開發環境：產生 JSON + 建置模板 → 啟動 Netlify Dev（含 CMS）並開啟瀏覽器
# 使用方式：./start.sh  或  bash start.sh
# 停止：在執行 start.sh 的終端機按 Ctrl+C，然後執行 ./stop.sh 將更新轉成靜態檔

set -e
cd "$(dirname "$0")"
REPO_ROOT="$(pwd)"

echo "==> 檢查環境..."
if ! command -v netlify &>/dev/null; then
  echo "錯誤：未找到 netlify CLI。請先安裝：npm install -g netlify-cli"
  exit 1
fi

echo "==> 安裝 Python 依賴 (requirements.txt)..."
pip install -q -r requirements.txt 2>/dev/null || true

echo "==> 從 _posts / _profiles 產生 data/*.json..."
python3 scripts/data/generate-news-json.py
python3 scripts/data/generate-activities-json.py
python3 scripts/data/generate-faculty-json.py

echo "==> 建置模板 (build-templates.py)..."
python3 build-templates.py

echo "==> 啟動 Netlify Dev（預設 http://localhost:8888，會自動開啟瀏覽器）..."
echo "    若要停止：在此終端按 Ctrl+C，然後執行 ./stop.sh 將變更轉成靜態檔。"
exec netlify dev
