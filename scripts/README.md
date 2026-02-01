# Scripts 資料夾

本資料夾包含各類輔助腳本，分類如下：

## 📁 資料夾結構

```
scripts/
├── build/          # 建置相關腳本
├── data/           # 資料處理腳本
├── maintenance/    # 維護工具腳本
├── optimize-images.py
├── setup-git-hooks.sh
└── validate-html.py
```

---

## 🔨 build/ - 建置相關腳本

用於網站建置流程的輔助工具（不常用，多為一次性設定）

### convert-to-templates.py
- **用途**：將現有 HTML 檔案轉換為使用模板標記
- **使用時機**：首次設定模板系統時使用（已完成，不需再執行）
- **執行方式**：
  ```bash
  python3 scripts/build/convert-to-templates.py
  ```

### generate-static-faculty.py ⭐ 新增
- **用途**：從 faculty_data.json 生成靜態教職員頁面（不需前端 JavaScript）
- **優點**：完全靜態、載入更快、SEO 友善、可直接用 file:// 開啟
- **使用時機**：教職員資料更新時執行
- **執行方式**：
  ```bash
  python3 scripts/build/generate-static-faculty.py
  ```
- **說明**：請參閱 `BUILD_VS_FRONTEND.md` 瞭解建置工具與前端程式碼的區別

---

## 📊 data/ - 資料處理腳本

用於處理和整理網站內容資料

### parse-content.py
- **用途**：從 news/ 和 activities/ 目錄下的 HTML 檔案提取內容到 CSV
- **使用時機**：需要從舊的 HTML 檔案匯入資料時
- **執行方式**：
  ```bash
  python3 scripts/data/parse-content.py
  ```

### deduplicate-content.py
- **用途**：去除 data/content.csv 中的重複項目（根據標題和日期判斷）
- **使用時機**：發現資料有重複時
- **執行方式**：
  ```bash
  python3 scripts/data/deduplicate-content.py
  ```

### organize-images.py
- **用途**：重新組織圖片到分類資料夾（news → images/news/, activity → images/activities/）
- **使用時機**：需要整理圖片檔案時
- **執行方式**：
  ```bash
  python3 scripts/data/organize-images.py
  ```

### copy-images.py
- **用途**：複製圖片檔案
- **使用時機**：需要批次複製圖片時
- **執行方式**：
  ```bash
  python3 scripts/data/copy-images.py
  ```

### download-images.py
- **用途**：下載圖片檔案
- **使用時機**：需要從舊網站下載圖片時
- **執行方式**：
  ```bash
  python3 scripts/data/download-images.py
  ```

### generate-news-json.py ⭐ 靜態新聞來源
- **用途**：從 `news/_posts/*.md` 產生 `data/news.json`，供最新消息列表與文章頁使用
- **使用時機**：在 Decap CMS 或手動編輯 `news/_posts/` 後，需讓列表與文章內容同步時；Netlify 建置時會自動執行
- **執行方式**：
  ```bash
  python3 scripts/data/generate-news-json.py
  ```

### csv-news-to-posts.py（一次性遷移）
- **用途**：將 `data/content.csv` 中 type 為 news 的項目轉成 `news/_posts/*.md`，僅會建立尚未存在的文章
- **使用時機**：從 CSV 遷移到 Netlify/Decap 靜態模式時使用（已執行過，之後以 _posts 為準）
- **執行方式**：
  ```bash
  python3 scripts/data/csv-news-to-posts.py
  ```

### generate-activities-json.py ⭐ 靜態活動來源
- **用途**：從 `activities/_posts/*.md` 產生 `data/activities.json`，供最新消息／活動列表與文章頁使用
- **使用時機**：在 Decap CMS 或手動編輯 `activities/_posts/` 後，需讓列表與文章內容同步時；Netlify 建置時會自動執行
- **執行方式**：
  ```bash
  python3 scripts/data/generate-activities-json.py
  ```

### generate-faculty-json.py ⭐ 師資列表來源（與 Decap CMS 一致）
- **用途**：從 `faculty/_profiles/*.md`（YAML front matter）產生 `data/faculty_data.json`，供師資列表與詳情頁使用
- **使用時機**：在 Decap CMS 或手動編輯 `faculty/_profiles/` 後，需讓師資列表與 CMS 內容同步時；Netlify 建置時會自動執行
- **依賴**：需安裝 PyYAML（`pip install -r requirements.txt`）
- **執行方式**：
  ```bash
  python3 scripts/data/generate-faculty-json.py
  ```

### csv-activities-to-posts.py（一次性遷移）
- **用途**：將 `data/content.csv` 中 type 為 activity 的項目轉成 `activities/_posts/*.md`，僅會建立尚未存在的活動
- **使用時機**：從 CSV 遷移到 Netlify/Decap 靜態模式時使用（已執行過，之後以 _posts 為準）
- **執行方式**：
  ```bash
  python3 scripts/data/csv-activities-to-posts.py
  ```

---

## 🔧 maintenance/ - 維護工具腳本

用於網站維護和修正的工具

### cleanup-css-links.py
- **用途**：清理 HTML 檔案中重複的 CSS 連結
- **使用時機**：發現 HTML 有重複的 CSS 引用時
- **執行方式**：
  ```bash
  python3 scripts/maintenance/cleanup-css-links.py
  ```

### cleanup-legacy-files.py
- **用途**：識別並移動未使用的舊 JavaScript 檔案到 archive
- **使用時機**：需要清理專案中的舊檔案時
- **執行方式**：
  ```bash
  python3 scripts/maintenance/cleanup-legacy-files.py
  ```

### fix-path-prefix.py
- **用途**：修正 HTML 檔案中的 {{path_prefix}} 佔位符
- **使用時機**：發現路徑前綴有問題時
- **執行方式**：
  ```bash
  python3 scripts/maintenance/fix-path-prefix.py
  ```

### remove-inline-styles.py
- **用途**：移除 HTML 檔案中的 inline styles
- **使用時機**：需要清理 inline styles 時
- **執行方式**：
  ```bash
  python3 scripts/maintenance/remove-inline-styles.py
  ```

### convert-and-build.py
- **用途**：組合腳本，執行轉換和建置流程
- **使用時機**：需要一次執行多個轉換步驟時
- **執行方式**：
  ```bash
  python3 scripts/maintenance/convert-and-build.py
  ```

---

## 📝 根目錄腳本

### optimize-images.py
- **用途**：優化圖片檔案大小
- **執行方式**：
  ```bash
  python3 scripts/optimize-images.py
  ```

### validate-html.py
- **用途**：驗證 HTML 檔案的正確性
- **執行方式**：
  ```bash
  python3 scripts/validate-html.py
  ```

### setup-git-hooks.sh
- **用途**：設定 Git hooks
- **執行方式**：
  ```bash
  ./scripts/setup-git-hooks.sh
  ```

---

## ⚠️ 重要提醒

1. **這些腳本多為一次性工具**：
   - 用於專案初期的資料遷移和整理
   - 日常維護不需要頻繁使用

2. **執行前請備份**：
   - 這些腳本會修改檔案
   - 建議先 commit 當前狀態

3. **路徑設定**：
   - 所有腳本都使用 `BASE_DIR = Path(__file__).parent.parent`
   - 自動指向專案根目錄
   - 從專案根目錄執行即可

4. **常用操作請使用根目錄的核心腳本**：
   - 建置模板：`python3 build-templates.py`
   - 啟動 CMS：`python3 cms.py`

---

**最後更新**：2025-12-11
**維護者**：台大新聞所團隊
