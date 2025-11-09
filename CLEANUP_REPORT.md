# 專案整理報告

## 執行日期
2025-11-08

## 整理摘要

### 移動的檔案

#### 1. 舊頁面 → archive/
- `cp_n_*.html` (4 個舊版頁面)
- `Default.html` (舊首頁)
- `SiteMap.html` (舊網站地圖)
- `Advanced_Search.html` (舊搜尋)
- `News_Content.aspx` (舊檔案)
- `*.backup` (備份檔案)
- `international-communication.html`
- `resident-reporter.html`
- `event.html`
- `contact.html`
- `academic-activity.html`
- `practical_faculty_data.json` (舊資料)

#### 2. 文檔 → docs/
- `ORGANIZATION_STRUCTURE.md`
- `REBUILD_SUMMARY.md`
- `E-REPORT-INTEGRATION.md`
- `PHOTO_PATH_UPDATE_REPORT.md`
- `PHOTO_REORGANIZATION_REPORT.md`

#### 3. 腳本 → scripts/
- `*.sh` (Shell 腳本)

#### 4. 大型目錄 → archive/
- `001/` (206MB - 舊圖片)
- `photos/` (2MB - 重複照片)
- `Scripts/` (舊腳本目錄)
- `Logs/` (暫存紀錄)

#### 5. Python 腳本 → python-scripts/
- 37 個資料處理腳本（已在之前整理）

### 保留在主目錄

**HTML 頁面**：
- index.html
- news.html
- resources.html
- staff.html
- activities.html
- article.html
- article-view.html

**重要腳本**：
- build-templates.py
- convert-to-templates.py

**資料檔案**：
- faculty_data.json
- faculty-mapping.csv

**設定檔**：
- package.json
- tailwind.config.js

**文檔**：
- README.md
- CLAUDE.md ⭐ 新增

**目錄**：
- templates/
- faculty/
- admissions/
- students/
- publications/
- about/
- images/
- css/
- js/
- data/
- python-scripts/
- scripts/
- docs/
- archive/

### 整理後的目錄結構

```
journalism-ntu.github.io/
├── 📄 HTML 頁面 (7 個)
├── 🔧 建置腳本 (2 個)
├── 📊 資料檔案 (2 個)
├── 📁 templates/ (模板)
├── 📁 faculty/ (教師頁面)
├── 📁 admissions/ (招生)
├── 📁 students/ (學生)
├── 📁 publications/ (出版)
├── 📁 about/ (關於)
├── 📁 images/ (圖片)
├── 📁 css/ (樣式)
├── 📁 js/ (腳本)
├── 📁 data/ (資料)
├── 📁 python-scripts/ (37 個 Python 腳本)
├── 📁 scripts/ (Shell 腳本)
├── 📁 docs/ (文檔)
├── 📁 archive/ (舊檔案)
└── 📄 README.md, CLAUDE.md
```

## 空間節省

- 移除/歸檔：~210MB
- 主目錄變得整潔易讀

## 新增文檔

### CLAUDE.md ⭐
完整的 AI Copilot 協作指南，包含：
- 專案概述
- 目錄結構
- 核心系統（模板、教師資料、腳本）
- 常見任務
- 重要概念
- 技術細節
- 維護注意事項
- 快速參考
- 歷史記錄

### 其他文檔
- `templates/README.md` - 模板系統說明
- `python-scripts/README.md` - 腳本分類說明

## 建議

### 立即行動
1. ✅ 將 `node_modules/` 加入 `.gitignore`
2. ✅ 定期檢查 `archive/` 目錄，刪除不需要的舊檔案
3. ✅ 閱讀 `CLAUDE.md` 了解專案結構

### 未來維護
- 新增腳本時，區分：
  - 網頁生成 → 主目錄
  - 資料處理 → python-scripts/
- 定期更新 `CLAUDE.md`
- 保持目錄整潔

## 清理前後對比

### 清理前
- 主目錄：60+ 個項目
- 混雜：舊檔案、腳本、文檔
- 難以辨識重要檔案

### 清理後
- 主目錄：30 個項目
- 分類清楚：頁面、腳本、資料、目錄
- 重要檔案一目了然

---

**整理者**：Claude AI
**日期**：2025-11-08
