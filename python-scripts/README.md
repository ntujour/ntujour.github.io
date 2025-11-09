# Python 腳本目錄

本目錄包含用於資料處理和網站維護的各種 Python 腳本。

## 目錄組織

```
journalism-ntu.github.io/
├── build-templates.py          # 【網頁生成】模板建置腳本
├── convert-to-templates.py     # 【網頁生成】轉換 HTML 為使用模板
│
└── python-scripts/             # 【資料處理】各種維護腳本
    ├── 教師照片處理/
    ├── 教師資料處理/
    ├── 頁面修正/
    ├── 導航更新/
    └── 其他工具/
```

## 腳本分類

### 1. 教師照片處理 (7 個)

處理教師照片的下載、重新命名、路徑更新等。

- `fix-faculty-photos.py` - 修正教師照片對應
- `reorganize-images.py` - 重組圖片結構
- `consolidate-faculty-photos.py` - 整合所有教師照片
- `cleanup-old-photos.py` - 清理舊照片檔案
- `update-all-faculty-photos.py` - 批量更新所有實務教師照片
- `download_faculty_photos.py` - 下載教師照片
- `download_parttime_photos.py` - 下載兼任教師照片

### 2. 教師資料處理 (9 個)

處理教師資料的提取、轉換、生成等。

- `add-missing-faculty.py` - 添加缺失的實務教師到 CSV
- `extract_faculty_data.py` - 提取教師資料
- `extract_faculty_markdown.py` - 提取教師 Markdown 資料
- `extract_parttime_faculty.py` - 提取兼任教師資料
- `fetch_all_faculty_types.py` - 獲取所有類型教師資料
- `fetch_lincc_and_practical.py` - 獲取合聘和實務教師資料
- `fetch_lincc.py` - 獲取合聘教師資料
- `generate_faculty_markdown_pages.py` - 生成教師 Markdown 頁面
- `generate_faculty_pages.py` - 生成教師 HTML 頁面

### 3. 頁面修正 (7 個)

修正 HTML 頁面中的各種問題。

- `update-html-photo-paths.py` - 更新 HTML 中的照片路徑
- `fix_css_js_paths.py` - 修正 CSS/JS 路徑
- `fix_relative_paths.py` - 修正相對路徑
- `fix-sitemap-headings.py` - 修正 sitemap 標題
- `update-hover-style.py` - 更新 hover 樣式
- `remove-transfer-link.py` - 移除轉學連結
- `replace-admission-term.py` - 替換招生術語

### 4. 導航更新 (7 個)

更新網站導航列和連結。

- `add-nav-css.py` - 添加導航 CSS
- `update_links.py` - 更新連結
- `update_nav.py` - 更新導航列
- `update-faculty-nav.py` - 更新教師頁面導航
- `update-navigation-v2.py` - 更新導航（版本 2）
- `update-navigation.py` - 更新導航
- （注：有重複的 update-links.py）

### 5. 其他工具 (6 個)

其他實用工具腳本。

- `convert-to-csv.py` - 轉換資料為 CSV
- `check-page-consistency.py` - 檢查頁面一致性
- `create-detail-pages.py` - 創建詳細頁面
- `create-new-pages.py` - 創建新頁面
- `extract_styles.py` - 提取樣式
- `identify-reports.py` - 識別所報檔案
- `match-reports.py` - 匹配所報檔案

## 使用說明

### 網頁生成腳本（主目錄）

這些腳本用於日常的網站維護和內容生成：

```bash
# 建置模板（將 {{site-banner}} 等標記替換為實際內容）
python3 build-templates.py

# 轉換現有 HTML 為使用模板標記
python3 convert-to-templates.py
```

### 資料處理腳本（python-scripts/）

這些腳本用於一次性的資料處理或修正任務：

```bash
# 執行資料處理腳本
python3 python-scripts/[腳本名稱].py

# 範例：更新照片路徑
python3 python-scripts/update-html-photo-paths.py
```

## 注意事項

1. **資料處理腳本**：通常只需要執行一次，用於修正或轉換資料
2. **網頁生成腳本**：日常使用，每次修改模板後都需要執行
3. **備份建議**：執行腳本前建議先備份或使用 Git 版本控制
4. **路徑問題**：某些舊腳本可能使用舊的路徑結構，使用前請檢查

## 常見任務

### 修改網站共用區塊（Banner、Navigation 等）

```bash
# 1. 編輯模板檔案
vim templates/site-nav.html

# 2. 執行建置（在主目錄）
python3 build-templates.py
```

### 更新教師資料

```bash
# 1. 編輯 faculty_data.json 或 faculty-mapping.csv

# 2. 如需更新照片路徑
python3 python-scripts/update-html-photo-paths.py

# 3. 建置模板
python3 build-templates.py
```

### 添加新頁面

```bash
# 使用模板範例創建新頁面
cp templates/example-page.html my-new-page.html

# 編輯內容
vim my-new-page.html

# 建置
python3 build-templates.py
```

## 維護建議

- **定期清理**：移除不再使用的腳本
- **文檔更新**：新增腳本時更新本 README
- **命名規範**：使用描述性的檔名，如 `update-xxx.py` 或 `fix-xxx.py`
- **版本控制**：使用 Git 追蹤腳本變更

---

*最後更新：2025-11-08*
