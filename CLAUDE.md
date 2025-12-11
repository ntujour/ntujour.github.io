# 台大新聞所網站 - Claude AI 協作指南

> 本文檔為 AI Copilot（Claude、GPT 等）提供專案脈絡和工作流程指引

## 專案概述

**專案名稱**：國立臺灣大學新聞研究所網站
**網址**：https://journalism-ntu.github.io
**技術棧**：靜態 HTML + Tailwind CSS + JavaScript + Python 建置腳本
**維護方式**：模板系統 + 動態資料載入

---

## 目錄結構

```
journalism-ntu.github.io/
│
├── 📄 index.html                    # 首頁
├── 📄 news.html                     # 最新消息
├── 📄 resources.html                # 相關資源
├── 📄 staff.html                    # 行政人員
├── 📄 activities.html               # 活動頁面
├── 📄 article.html / article-view.html  # 文章頁面
│
├── 🔧 build-templates.py            # 【重要】模板建置腳本
├── 🔧 cms.py                        # 【重要】整合 CMS 系統（一鍵啟動）
│
├── 📁 templates/                    # 【重要】共用模板
│   ├── site-banner.html            # Banner 模板
│   ├── site-nav.html               # 導航列模板
│   ├── site-sitemap.html           # 快速連結模板
│   ├── site-footer.html            # 頁尾模板
│   ├── example-page.html           # 示範頁面
│   └── README.md                   # 模板系統說明
│
├── 📁 faculty/                      # 教師頁面
│   ├── faculty.html                # 師資總覽
│   ├── fulltime-professor.html     # 專任教師
│   ├── practical-professor.html    # 實務教師
│   ├── parttime-professor.html     # 兼任教師
│   ├── honorary-professor.html     # 名譽教授
│   ├── joint-professor.html        # 合聘教師
│   └── [個人頁面].html             # 各教師個人頁面
│
├── 📁 admissions/                   # 入學資訊
├── 📁 students/                     # 學生學習
├── 📁 publications/                 # 出版發表
├── 📁 about/                        # 關於我們
│
├── 📁 images/                       # 圖片資源
│   ├── faculty/                    # 教師照片（英文 ID 命名）
│   ├── reports/                    # 所報 PDF
│   └── regulations/                # 修業規定圖片
│
├── 📁 css/                          # 樣式表
├── 📁 js/                           # JavaScript
│
├── 📁 data/                         # 【重要】資料檔案
│   ├── faculty_data.json           # 【重要】教師資料庫
│   ├── faculty-mapping.csv         # 【重要】教師照片對應表
│   ├── content.csv                 # 【重要】新聞與活動資料
│   └── backups/                    # 自動備份目錄
│
├── 📁 admin/                        # 【重要】後台管理系統
│   ├── content-editor-v2.html      # 內容編輯器 v2
│   └── EDITOR_V2_README.md         # 編輯器說明
│
├── 📁 scripts/                      # 【重要】輔助腳本（分類整理）
│   ├── build/                      # 建置相關腳本
│   │   └── convert-to-templates.py # HTML 轉模板（一次性設定）
│   ├── data/                       # 資料處理腳本
│   │   ├── parse-content.py        # 內容抽取腳本
│   │   ├── deduplicate-content.py  # 內容去重腳本
│   │   ├── organize-images.py      # 圖片整理腳本
│   │   └── ...                     # 其他資料處理工具
│   ├── maintenance/                # 維護工具腳本
│   │   ├── cleanup-css-links.py    # CSS 清理
│   │   ├── fix-path-prefix.py      # 路徑修正
│   │   └── ...                     # 其他維護工具
│   └── README.md                   # 腳本分類說明
│
├── 📁 docs/                         # 專案文檔
│
├── 📁 archive/                      # 已廢棄的舊檔案
│   ├── python-scripts/             # 舊的遷移腳本（37 個）
│   └── scripts-legacy/             # 其他已棄用腳本
│
├── 📄 README.md                     # 專案說明
├── 📄 CLAUDE.md                     # 本文檔
├── 📄 package.json                  # Node.js 依賴
└── 📄 tailwind.config.js            # Tailwind 設定
```

---

## 核心系統

### 1. 模板系統 🎨

**用途**：統一管理網站共用區塊（Banner、導航列、Sitemap、Footer）

**檔案位置**：
- 模板：`templates/`
- 建置腳本：`build-templates.py`（根目錄）
- 轉換腳本：`scripts/build/convert-to-templates.py`（一次性設定，不常用）

**工作原理**：
1. HTML 中使用標記：`{{site-banner}}`、`{{site-nav}}`、`{{site-sitemap}}`、`{{site-footer}}`
2. 執行建置腳本：`python3 build-templates.py`
3. 標記自動替換為實際內容，路徑自動處理

**修改流程**：
```bash
# 1. 編輯模板
vim templates/site-nav.html

# 2. 執行建置
python3 build-templates.py

# 3. 完成！所有頁面自動更新
```

**重要注意**：
- ✅ 修改共用區塊時，只需編輯 `templates/` 中的模板
- ✅ 腳本會自動處理相對路徑（根目錄 vs 子目錄的 `../`）
- ❌ 不要手動修改建置後的 HTML 中的共用區塊

### 2. 教師資料系統 👥

**資料來源**：
- `data/faculty_data.json` - 主要教師資料庫（動態載入用）
- `data/faculty-mapping.csv` - 教師照片對應表（維護用）

**照片管理**：
- 位置：`images/faculty/`
- 命名：使用英文 ID（如 `jerryhsieh.png`、`lichihte.jpg`）
- 對應：ID 必須與 `faculty_data.json` 中的 `id` 欄位一致

**頁面類型**：
1. **列表頁面**：使用 JavaScript 從 `faculty_data.json` 動態載入
   - `faculty.html` - 師資總覽
   - `fulltime-professor.html` - 專任教師
   - `practical-professor.html` - 實務教師
   - 等等...

2. **個人頁面**：專任教師有獨立 HTML 頁面
   - 如：`jerryhsieh.html`、`lihyunlin.html`

**修改教師資料**：
```bash
# 1. 編輯 JSON
vim data/faculty_data.json

# 2. 如需更新照片，確保檔名與 ID 一致
cp new-photo.jpg images/faculty/[英文ID].jpg

# 3. 建置模板（如有使用模板標記）
python3 build-templates.py
```

**重要規則**：
- 實務教師「謝艾契」只顯示英文名 "Archie Tse"
- 照片路徑格式：`../images/faculty/[ID].jpg`（從 faculty/ 目錄訪問）
- ID 命名一致性：
  - 黃哲斌：`huangchepin`（不是 hwangchepin）
  - 方德琳：`fangterlin`（不是 fangtelin）

### 3. 內容管理系統 (CMS) 📝

**用途**：整合式內容管理系統，管理新聞與活動內容

**核心檔案**：
- CMS 主程式：`cms.py`（一鍵啟動，整合伺服器 + 編輯器 + 儲存功能）
- 編輯器：`admin/content-editor-v2.html`
- 資料檔：`data/content.csv`（119 筆資料：97 筆活動 + 22 筆新聞）
- 備份目錄：`data/backups/`（每次儲存自動備份）

**CMS 系統特色** 🎯

**一鍵啟動**：
```bash
python3 cms.py
```

**功能整合**：
- 🌐 HTTP 伺服器（端口 8080）
- 📝 內容編輯器（自動開啟瀏覽器）
- 💾 CSV 儲存功能（自動端點 `/save-csv`）
- 🔄 自動備份機制（儲存前備份到 `data/backups/`）

**編輯器功能** ✨

**視覺化編輯**：
- ✅ 富文本編輯器（Quill.js）
- ✅ 圖片上傳與管理
- ✅ 即時搜尋與篩選
- ✅ 按類型分類瀏覽（新聞/活動）

**變更追蹤**：
- ✅ 追蹤新增、更新、刪除的記錄
- ✅ 離開前警告（有未儲存變更時）
- ✅ 標題顯示變更數量：`⚠️ (3) 台大新聞所 CMS - 有未儲存的變更`
- ✅ 儲存時顯示詳細變更記錄

**資料操作**：
- ✅ **Save to DB**：儲存到資料庫（`data/content.csv`）
- ✅ **Download Backup CSV**：下載備份到本地
- ✅ 批次操作支援

**使用流程** 📋

```bash
# 1. 啟動 CMS 系統
python3 cms.py

# 2. 瀏覽器自動開啟編輯器
# 網址：http://localhost:8080/admin/content-editor-v2.html

# 3. 編輯內容
#    - 新增文章：填寫表單 → 點擊「新增」
#    - 編輯文章：點擊表格中的「編輯」
#    - 刪除文章：點擊表格中的「刪除」

# 4. 儲存變更
#    - 點擊「Save to DB」→ 查看變更記錄 → 確認儲存
#    - 系統自動備份到 data/backups/

# 5. 下載備份（可選）
#    - 點擊「Download Backup CSV」
```

**變更記錄範例** 📊

儲存時會顯示：
```
📝 本次變更記錄：

✅ 新增 2 筆：
   • ID: 1762668030439 - 測試文章 (news)
   • ID: 1762668030440 - 另一篇測試 (activity)

📝 更新 1 筆：
   • ID: 259107 - 更新的標題 (news)

🗑️ 刪除 1 筆：
   • ID: 104734 - 已刪除的文章 (news)

總共 61 筆資料

確定要儲存到資料庫嗎？
```

**資料抽取與處理** 🔄

```bash
# 從 HTML 檔案抽取內容到 CSV
python3 scripts/data/parse-content.py

# 去除重複資料
python3 scripts/data/deduplicate-content.py
```

**重要提醒**：
- ⚠️ 舊版編輯器（content-editor.html）已棄用
- ✅ 請使用 `cms.py` 啟動系統，不需要手動啟動多個伺服器
- 💾 每次儲存前會自動備份，備份檔案位於 `data/backups/`
- 🔒 離開前會檢查是否有未儲存的變更

### 4. 輔助腳本系統 🐍

**位置**：`scripts/`（分類整理後的輔助工具）

**資料夾結構**：
- `scripts/build/` - 建置相關腳本（如 convert-to-templates.py）
- `scripts/data/` - 資料處理腳本（如 parse-content.py, deduplicate-content.py）
- `scripts/maintenance/` - 維護工具腳本（如 cleanup-css-links.py, fix-path-prefix.py）

**使用時機**：
- ✅ 一次性資料修正
- ✅ 批量更新檔案
- ✅ 資料格式轉換
- ✅ 網站維護和清理

**執行方式**：
```bash
# 資料處理
python3 scripts/data/[腳本名稱].py

# 維護工具
python3 scripts/maintenance/[腳本名稱].py

# 建置工具
python3 scripts/build/[腳本名稱].py
```

**詳細說明**：請參閱 `scripts/README.md`

**注意**：
- 這些是維護工具，不是日常使用腳本
- 舊的遷移腳本（37 個）已移至 `archive/python-scripts/`

---

## 常見任務

### 任務 1：修改導航列

```bash
# 1. 編輯導航模板
vim templates/site-nav.html

# 2. 建置
python3 build-templates.py

# 完成！所有頁面的導航列都更新了
```

### 任務 2：新增教師

```bash
# 1. 準備照片（使用英文 ID 命名）
cp photo.jpg images/faculty/newteacher.jpg

# 2. 編輯教師資料
vim data/faculty_data.json
# 在對應類別中加入：
# {
#   "id": "newteacher",
#   "name": "新教師",
#   "photo": "../images/faculty/newteacher.jpg",
#   "phone": "...",
#   "email": "...",
#   ...
# }

# 3. 更新 CSV（可選）
vim data/faculty-mapping.csv

# 4. 檢查頁面
# 開啟 faculty/faculty.html 檢查是否正確顯示
```

### 任務 3：管理新聞與活動內容

```bash
# 1. 啟動 CMS 系統
python3 cms.py

# 2. 在瀏覽器中編輯內容
#    - 自動開啟：http://localhost:8080/admin/content-editor-v2.html
#    - 新增/編輯/刪除文章
#    - 系統會追蹤所有變更

# 3. 儲存到資料庫
#    - 點擊「Save to DB」
#    - 確認變更記錄
#    - 系統自動備份

# 4. 停止伺服器
#    - 按 Ctrl+C
```

### 任務 4：修改 Banner

```bash
# 1. 編輯 Banner 模板
vim templates/site-banner.html

# 2. 建置
python3 build-templates.py
```

### 任務 4：調整間距

```bash
# 全站統一使用 py-4
# 已執行過批量修正，目前所有 py-8 和 py-12 都改為 py-4

# 如需再次修正（不建議）：
# 使用 scripts/ 中的 fix-padding.sh
```

### 任務 5：新增頁面

```bash
# 1. 複製示範頁面
cp templates/example-page.html my-new-page.html

# 2. 編輯內容
vim my-new-page.html

# 3. 建置（如使用模板標記）
python3 build-templates.py
```

---

## 重要概念

### 路徑處理

**原則**：所有從 `faculty/` 等子目錄訪問根目錄資源時，需要 `../` 前綴

**範例**：
- 根目錄頁面（`index.html`）：`<a href="about/intro.html">`
- 子目錄頁面（`faculty/faculty.html`）：`<a href="../about/intro.html">`

**自動處理**：`build-templates.py` 會根據檔案位置自動處理路徑前綴

### 照片命名規則

**格式**：`[英文ID].[副檔名]`

**範例**：
- ✅ `jerryhsieh.png`
- ✅ `lichihte.jpg`
- ✅ `archie-tse.jpg`（特殊情況）
- ❌ `001.jpg`
- ❌ `teacher-photo.png`

**對應關係**：
```json
{
  "id": "jerryhsieh",           // 必須一致
  "photo": "../images/faculty/jerryhsieh.png"
}
```

### 垂直間距統一

**規則**：全站統一使用 `py-4`

**已棄用**：
- ❌ `py-8`
- ❌ `py-12`

**範例**：
```html
<section class="py-4 bg-white">    <!-- ✅ 正確 -->
<section class="py-8 bg-gray-50">  <!-- ❌ 已棄用 -->
```

---

## 技術細節

### JavaScript 動態載入

**位置**：`js/` 目錄

**主要腳本**：
- `faculty.js` - 師資總覽頁面
- `fulltime-faculty-detail.js` - 專任教師詳細頁面
- `practical-faculty-detail.js` - 實務教師詳細頁面
- `parttime-faculty-detail.js` - 兼任教師詳細頁面
- `honorary-faculty-detail.js` - 名譽教授詳細頁面
- `joint-faculty-detail.js` - 合聘教師詳細頁面

**工作原理**：
```javascript
// 1. 從 faculty_data.json 載入資料
fetch('../faculty_data.json')

// 2. 動態生成 HTML
const cardsHTML = data.fulltime.map(faculty => `
    <a href="${faculty.file}">
        <img src="${faculty.photo}" alt="${faculty.name}">
        <h4>${faculty.name}</h4>
    </a>
`).join('');

// 3. 插入頁面
container.innerHTML = cardsHTML;
```

### Tailwind CSS

**設定檔**：`tailwind.config.js`

**編譯方式**：
```bash
# 如需重新編譯（不常用）
npm run build:css
```

**主要樣式**：
- 色系：`#671919`（主色）、`#efa22a`（強調色）
- 容器：`.container-1200`（最大寬度 1200px）
- 導航：`.site-nav`（sticky top）

---

## 維護注意事項

### ✅ 建議做法

1. **修改共用區塊**：
   - 編輯 `templates/` 中的模板
   - 執行 `build-templates.py`

2. **修改教師資料**：
   - 編輯 `data/faculty_data.json`
   - 確保照片檔名與 ID 一致

3. **新增頁面**：
   - 使用 `templates/example-page.html` 作為範本
   - 記得執行建置腳本

4. **版本控制**：
   - 使用 Git 追蹤變更
   - 修改前先 commit

### ❌ 避免做法

1. **不要直接修改建置後的 HTML 共用區塊**：
   - ❌ 直接改 `faculty.html` 中的 Navigation
   - ✅ 改 `templates/site-nav.html` 然後建置

2. **不要使用舊的照片路徑**：
   - ❌ `001/Upload/366/ckfile/xxx.jpg`
   - ✅ `images/faculty/[英文ID].jpg`

3. **不要使用已棄用的間距**：
   - ❌ `py-8`、`py-12`
   - ✅ `py-4`

4. **不要混用路徑前綴**：
   - ❌ 有時用 `../`，有時不用
   - ✅ 使用建置腳本自動處理

### 🔍 問題排查

**問題：照片不顯示**
```bash
# 檢查步驟：
1. 檢查照片檔案是否存在：ls images/faculty/
2. 檢查檔名是否與 ID 一致
3. 檢查路徑格式：../images/faculty/[ID].jpg
4. 檢查瀏覽器開發者工具的 Network 標籤
```

**問題：模板標記沒有替換**
```bash
# 檢查步驟：
1. 確認 HTML 中有正確的標記：{{site-banner}}
2. 執行建置：python3 build-templates.py
3. 檢查是否有錯誤訊息
```

**問題：導航列不一致**
```bash
# 解決方案：
1. 確認所有頁面都使用模板標記
2. 重新建置：python3 build-templates.py
```

---

## 檔案清單

### 必要檔案（不可刪除）

**核心腳本**：
- `build-templates.py` - 模板建置
- `cms.py` - CMS 系統

**資料檔案**：
- `data/faculty_data.json` - 教師資料
- `data/faculty-mapping.csv` - 照片對應
- `data/content.csv` - 新聞與活動

**模板和資源**：
- `templates/` - 所有模板
- `images/faculty/` - 教師照片
- `css/`, `js/` - 樣式和腳本

### 參考文檔

- `README.md` - 專案說明
- `CLAUDE.md` - 本文檔
- `templates/README.md` - 模板系統說明
- `scripts/README.md` - 輔助腳本說明
- `admin/EDITOR_V2_README.md` - CMS 編輯器說明
- `docs/` - 其他文檔

### 可刪除/已歸檔

- `archive/` - 舊版檔案和已廢棄的腳本
  - `archive/python-scripts/` - 舊的遷移腳本（37 個）
  - `archive/scripts-legacy/` - 其他已棄用腳本
- `node_modules/` - 可用 `npm install` 重建

---

## 快速參考

### 常用指令

```bash
# 建置模板
python3 build-templates.py

# 啟動 CMS 系統
python3 cms.py

# 轉換 HTML 為使用模板（首次設定，不常用）
python3 scripts/build/convert-to-templates.py

# 安裝依賴
npm install

# 編譯 Tailwind（不常用）
npm run build:css

# 執行資料處理腳本
python3 scripts/data/[腳本名].py
python3 scripts/maintenance/[腳本名].py
```

### 重要路徑

```
# 核心系統
cms.py                           # 啟動 CMS 系統
build-templates.py               # 建置模板

# 內容管理
admin/content-editor-v2.html     # 內容編輯器
data/content.csv                 # 新聞與活動資料

# 模板系統
templates/site-nav.html          # 修改導航列
templates/site-banner.html       # 修改 Banner
templates/site-footer.html       # 修改頁尾

# 教師資料
data/faculty_data.json           # 教師資料庫
data/faculty-mapping.csv         # 教師照片對應
images/faculty/                  # 教師照片

# 輔助腳本
scripts/data/                    # 資料處理腳本
scripts/maintenance/             # 維護工具
scripts/build/                   # 建置腳本
```

### 聯絡資訊

- 電話：(02) 3366-3383
- Email：jour@ntu.edu.tw
- 地址：106台北市大安區羅斯福路四段1號

---

## 歷史記錄

### 2025-12-11

#### 專案結構重新整理
- ✅ **資料檔案集中管理**：
  - 移動 `faculty_data.json` 和 `faculty-mapping.csv` 到 `data/` 資料夾
  - 統一資料檔案位置，便於備份和管理

- ✅ **輔助腳本分類整理**：
  - 建立 `scripts/build/`、`scripts/data/`、`scripts/maintenance/` 三個子資料夾
  - 移動 14 個根目錄的 Python 腳本到對應分類
  - 根目錄只保留核心腳本：`build-templates.py`、`cms.py`

- ✅ **舊腳本歸檔**：
  - 移動 `python-scripts/`（37 個舊遷移腳本）到 `archive/`
  - 移動已棄用的 `save-csv-server.py` 到 `archive/scripts-legacy/`

- ✅ **路徑引用更新**：
  - 更新所有移動後腳本的 `BASE_DIR` 路徑
  - 更新 6 個 JS 檔案中的 `faculty_data.json` 路徑引用
  - 確保所有引用正確指向新位置

- ✅ **文檔更新**：
  - 建立 `scripts/README.md` 說明輔助腳本分類和用途
  - 更新 `CLAUDE.md` 反映新的專案結構
  - 更新所有路徑引用和使用說明

#### 專案結構改進
- **更清晰的目錄結構**：核心腳本和輔助工具明確分離
- **更好的可維護性**：按功能分類，易於尋找和管理
- **更簡潔的根目錄**：只保留最常用的核心檔案

### 2025-11-09

#### 整合 CMS 系統開發
- ✅ 建立整合式 CMS 系統（`cms.py`）
- ✅ 一鍵啟動：同時提供 HTTP 伺服器、編輯器、CSV 儲存功能
- ✅ 內容編輯器 v2 功能完善
  - 變更追蹤系統（新增、更新、刪除記錄）
  - 離開前警告（未儲存變更時）
  - 標題顯示變更數量
  - 儲存時顯示詳細變更記錄
- ✅ 自動備份機制（儲存前自動備份到 `data/backups/`）
- ✅ 按鈕重新命名：「Save to DB」、「Download Backup CSV」
- ✅ 修復資料筆數計算錯誤（正確過濾空行）
- ✅ 修復新增文章後不顯示的問題

#### 技術改進
- 自動偵測伺服器端口（`window.location.origin`）
- CSV 正確解析（只計算有內容的行）
- 變更狀態即時更新
- 資料完整性驗證

### 2025-11-08

#### 主要更新
- ✅ 建立模板系統（Banner、Nav、Sitemap、Footer）
- ✅ 整理照片到 `images/faculty/`，使用英文 ID 命名
- ✅ 修正照片對應錯誤（梁玉芳、黃哲斌、方德琳）
- ✅ 統一垂直間距為 `py-4`
- ✅ 整理 Python 腳本到 `python-scripts/`
- ✅ 清理主目錄，歸檔舊檔案

#### 技術改進
- 路徑自動處理（`../` 前綴）
- 照片命名規範化
- 目錄結構優化

### 2025-11-06

#### 初始重構
- 更新網站結構
- 整合教師資料系統
- 建立資料檔案（JSON、CSV）

---

## 給未來 AI Copilot 的建議

### 理解專案架構

1. **模板系統是核心**：
   - 所有共用區塊都使用模板
   - 記得執行建置腳本

2. **資料驅動設計**：
   - 教師頁面由 `data/faculty_data.json` 驅動
   - 修改資料而非 HTML

3. **路徑處理**：
   - 讓建置腳本自動處理
   - 不要手動調整 `../`

### 協作原則

1. **先讀文檔**：
   - 閱讀本文檔（CLAUDE.md）
   - 查看 `templates/README.md`（模板系統說明）
   - 檢查 `scripts/README.md`（輔助腳本說明）

2. **保持一致**：
   - 遵循現有命名規則
   - 使用既有的建置流程

3. **記錄變更**：
   - 更新相關文檔
   - 在本文檔記錄重大改動

### 常見任務速查

| 任務 | 操作 |
|------|------|
| 改導航 | 編輯 `templates/site-nav.html` → 建置 |
| 改 Banner | 編輯 `templates/site-banner.html` → 建置 |
| 加教師 | 編輯 `data/faculty_data.json` + 照片 |
| 改樣式 | 編輯 CSS 檔案 |
| 新頁面 | 複製 `example-page.html` → 建置 |
| 管理內容 | 執行 `python3 cms.py` 啟動編輯器 |

---

**最後更新**：2025-12-11
**維護者**：Claude AI + 台大新聞所團隊
**文檔版本**：2.0
