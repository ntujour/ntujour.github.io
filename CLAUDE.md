# 台大新聞所網站 - Claude AI 協作指南

> 本文檔為 AI Copilot（Claude、GPT 等）提供專案脈絡和工作流程指引

## 專案概述

**專案名稱**：國立臺灣大學新聞研究所網站  
**網址**：https://journalism-ntu.github.io  
**技術棧**：靜態 HTML + Tailwind CSS + JavaScript + Python 建置腳本  
**維護方式**：模板系統 + 動態資料載入 + Decap CMS  
**語言支援**：繁體中文（主要）+ 英文（次要）  
**部署方式**：GitHub Pages + Netlify + Decap CMS

> 📖 **完整架構說明**：請參閱 [`ARCHITECTURE.md`](ARCHITECTURE.md) - 詳細的雙語網站架構規劃文件

---

## 目錄結構

> 與 [`ARCHITECTURE.md`](ARCHITECTURE.md) 目錄結構一致。圖例：⭐ = 雙語/CMS 相關重點

```
ntujour.github.io/
│
├── 📁 admin/                          # Decap CMS 管理後台
│   ├── index.html                    # CMS 入口頁面
│   └── config.yml                    # CMS 配置檔案 ⭐
│
├── 📁 _data/                          # 共用資料檔案（JSON）⭐
│   ├── banner.json                   # Banner 內容（雙語）
│   ├── navigation.json               # 導航選單（雙語）
│   ├── site_settings.json            # 網站全域設定（雙語）
│   └── backups/                      # 資料備份目錄
│
├── 📁 templates/                      # HTML 模板
│   ├── site-banner.html              # Banner 模板
│   ├── site-nav.html                 # 導航列模板
│   ├── site-sitemap.html             # 網站地圖模板
│   ├── site-footer.html              # 頁尾模板
│   ├── site-head-common.html         # 共用 head 區塊
│   ├── example-page.html             # 示範頁面
│   └── README.md                     # 模板系統說明
│
├── 📁 js/                             # JavaScript 檔案
│   ├── load-banner.js                # 動態載入 Banner ⭐
│   ├── load-nav.js                   # 動態載入導航（規劃）⭐
│   ├── i18n.js                       # 多語言切換 ⭐
│   ├── faculty.js                    # 師資頁面邏輯
│   └── ...
│
├── 📁 css/                            # 樣式檔案
│   ├── tailwind.css                  # Tailwind 編譯輸出
│   └── site-common.css               # 網站共用樣式
│
├── 📁 images/                         # 圖片資源
│   ├── uploads/                      # CMS 上傳的圖片 ⭐
│   ├── faculty/                      # 教師照片（英文 ID 命名）
│   ├── reports/                      # 所報 PDF
│   └── ...
│
├── 📁 data/                           # 建置產生的 JSON（來源：_posts、_profiles）
│   ├── faculty_data.json             # 教師資料（由 faculty/_profiles 建置）
│   ├── news.json                     # 新聞（由 news/_posts 建置）
│   ├── activities.json               # 活動（由 activities/_posts 建置）
│   ├── faculty-mapping.csv           # 教師照片對應表
│   └── backups/                      # 自動備份目錄
│
├── 📁 news/                           # 新聞/消息
│   └── _posts/                       # Markdown 格式文章（CMS）⭐
│
├── 📁 activities/                     # 系所活動
│   └── _posts/                       # Markdown 格式文章（CMS）⭐
│
├── 📁 faculty/                        # 師資介紹（中文）
│   ├── _profiles/                    # 教師個人頁面 Markdown（單一來源）⭐
│   ├── .archive/                     # 舊版 HTML、舊版 _profiles_legacy/
│   ├── faculty.html                  # 師資總覽
│   ├── fulltime-professor.html       # 專任教師
│   └── ...
│
├── 📁 about/                          # 關於我們（中文）
├── 📁 admissions/                     # 入學資訊（中文）
├── 📁 students/                       # 學生學習（中文）
├── 📁 publications/                   # 出版發表（中文）
│
├── 📁 en/                             # 英文版本 ⭐
│   ├── index.html                    # 英文首頁
│   ├── about/                        # 英文關於我們
│   ├── faculty/                      # 英文師資介紹
│   └── ...
│
├── 📁 graduate/                       # 學生專用區域（隱藏，不列入主選單）
│
├── 📄 index.html                      # 中文首頁
├── 📄 news.html                       # 中文新聞頁面
├── 📄 activities.html                 # 中文活動頁面
├── 📄 resources.html                  # 相關資源
├── 📄 staff.html                      # 行政人員
├── 📄 404.html                        # 404 錯誤頁面
│
├── 📄 build-templates.py              # 模板建置腳本
├── 📄 netlify.toml                    # Netlify 配置 ⭐
├── 📄 package.json                    # Node.js 依賴
├── 📄 tailwind.config.js              # Tailwind 設定
│
├── 📁 scripts/                        # 輔助腳本（建置/資料/維護）
│   ├── build/                        # 建置相關（如 convert-to-templates.py）
│   ├── data/                         # 資料處理（parse-content.py 等）
│   ├── maintenance/                  # 維護工具
│   └── README.md
│
├── 📁 docs/                           # 專案文檔
├── 📁 archive/                        # 已廢棄的舊檔案
├── 📄 README.md                       # 專案說明
└── 📄 CLAUDE.md                       # 本文檔
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

### 2. _data/ 與 Banner 統一管理 🎨

**用途**：共用資料與雙語 Banner 由 `_data/` 集中管理，與 [ARCHITECTURE.md](ARCHITECTURE.md) 一致。

**資料檔案**（`_data/`）：
- `_data/banner.json` - Banner 中英文標題、副標題、Logo（由 Decap CMS 或手動編輯）
- `_data/navigation.json` - 導航選單結構（雙語，規劃由 load-nav.js 載入）
- `_data/site_settings.json` - 網站全域設定（聯絡資訊、社群連結等）

**Banner 動態載入**：
- `js/load-banner.js` 依 URL 偵測語言，fetch `_data/banner.json` 後渲染
- `templates/site-banner.html` 僅提供外框與腳本引用，實際文案來自 JSON

**修改 Banner 內容**：
- 方法 1：編輯 `_data/banner.json`，或透過 Decap CMS「網站設定 → Banner 設定」
- 方法 2：若只改 Banner 的 HTML 結構，編輯 `templates/site-banner.html` 後執行 `python3 build-templates.py`

### 3. 教師資料系統 👥

**資料來源**：
- `faculty/_profiles/*.md` - 師資內容（Decap CMS 編輯，YAML front matter + Markdown）
- `data/faculty_data.json` - 師資列表用 JSON，由 `scripts/data/generate-faculty-json.py` 從 `_profiles/*.md` 產生，與 CMS 一致
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
# 1. 編輯師資內容（推薦）：Decap CMS「師資介紹」或直接編輯 faculty/_profiles/*.md
# 2. 產生列表 JSON（與 news/activities 一致，建置時會自動執行）
python3 scripts/data/generate-faculty-json.py

# 3. 如需更新照片，確保檔名與 ID 一致
cp new-photo.jpg images/faculty/[英文ID].jpg

# 4. 建置模板（如有使用模板標記）
python3 build-templates.py
```

**重要規則**：
- 實務教師「謝艾契」只顯示英文名 "Archie Tse"
- 照片路徑格式：`../images/faculty/[ID].jpg`（從 faculty/ 目錄訪問）
- ID 命名一致性：
  - 黃哲斌：`huangchepin`（不是 hwangchepin）
  - 方德琳：`fangterlin`（不是 fangtelin）

**師資個人頁面 Markdown（單一來源，CMS 格式）**：
- 專任教師個人頁面內容的 **單一來源** 為 `faculty/_profiles/`，採 **Decap CMS 的 Markdown 格式**（YAML 前言 + 內文）。
- 檔名需與對應 HTML 一致（如 `jerryhsieh.md` → `jerryhsieh.html`）；Adrian Rauchfleisch 頁面載入 `RauchfleischA.md`。
- 各 `.html` 頁面於執行時從 `_profiles/{id}.md` 載入，支援 YAML 前言（解析 name, title, email, expertise）與內文渲染；勿再使用或新增 `faculty/content/`。
- 原 `content/` 中 7 筆詳盡內文已覆蓋至 `_profiles` 對應檔（保留 YAML、替換內文）；完整師資名單維持於 `_profiles`。詳見 `faculty/_profiles/README.md`。

### 4. Decap CMS 整合 📝

**用途**：Git-based 內容管理，與 [ARCHITECTURE.md](ARCHITECTURE.md) 一致。部署後由 Netlify Identity 登入，變更直接提交至 GitHub。

**核心檔案**：
- 入口：`admin/index.html`
- 配置：`admin/config.yml`（backend、collections、media_folder）
- 資料：`_data/banner.json`、`_data/navigation.json`、`_data/site_settings.json`
- 媒體：`images/uploads/`（CMS 上傳）

**CMS 可管理內容**：
1. **網站全域**：Banner、導航選單、聯絡資訊、社群連結
2. **內容**：新聞（`news/_posts/`）、活動（`activities/_posts/`）、師資（`faculty/_profiles/`，規劃中）
3. **媒體**：圖片上傳與管理

**使用流程**：
```bash
# 1. 登入：訪問 https://your-site.netlify.app/admin/ → Netlify Identity
# 2. 編輯：選擇「網站設定」→「Banner 設定」等
# 3. 儲存：Save → Publish → GitHub 自動提交 → Netlify 自動部署
```

**本地開發**：`admin/config.yml` 內 `local_backend: true` 時可用 `npx netlify-cms-proxy-server` 等本地後端測試。

### 5. 輔助腳本系統 🐍

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

### 6. 部署流程 🚀

與 [ARCHITECTURE.md](ARCHITECTURE.md) 一致：**開發 → GitHub → Netlify → 生產環境**。

**Netlify 設定**（`netlify.toml`）：
- `publish = "."`，建置命令：`python3 build-templates.py`
- 環境：`NODE_VERSION = "18"`
- 安全與快取 Headers 已設定；404 行為請依需求調整（避免 `/*` 全導向 404）

**Netlify Identity**（於 Netlify Dashboard 設定）：
- 啟用 Identity 與 Git Gateway，供 Decap CMS 登入
- 邀請管理員使用者

**觸發部署**：Push 至 `main` 或透過 Decap CMS 發布後，Netlify 自動建置並部署。

---

## 🎨 樣式與佈局規範（重要）

### 統一 CSS 架構

**核心原則**：全站使用相同的 CSS 檔案作為中央控制系統

**主要樣式檔案**：
- `css/tailwind.css` - Tailwind CSS 框架（版本 3.4.0）
- `css/site-common.css` - 網站共用樣式（主色系、導航、容器等）

**所有頁面都必須載入**：
```html
<link rel="stylesheet" href="css/tailwind.css">
<link rel="stylesheet" href="css/site-common.css">

<!-- 子目錄頁面使用 -->
<link rel="stylesheet" href="../css/tailwind.css">
<link rel="stylesheet" href="../css/site-common.css">
```

### 頁面寬度規範

**核心規範**：網站所有頁面都應保持一致的內容寬度和左右留白

**容器 Class**：`.container-1200`
- 定義於 `css/site-common.css`
- 最大寬度：`1200px`
- 自動置中：`margin: 0 auto`
- 左右內距：`padding: 0 15px`

**標準用法**：
```html
<!-- Banner -->
<header class="site-banner py-6">
    <div class="container-1200">
        <h1>國立臺灣大學新聞研究所</h1>
    </div>
</header>

<!-- 導航列 -->
<nav class="site-nav">
    <div class="container-1200">
        <ul><!-- 導航項目 --></ul>
    </div>
</nav>

<!-- 主要內容 -->
<section class="py-6">
    <div class="container-1200">
        <!-- 頁面內容 -->
    </div>
</section>

<!-- Footer -->
<footer class="site-footer py-10">
    <div class="container-1200">
        <!-- Footer 內容 -->
    </div>
</footer>
```

### Admin / CMS 頁面規範

**特別注意**：Admin 和 CMS 相關頁面也必須遵循相同的寬度規範

**Admin 頁面**（`admin/index.html`）：
- ✅ **必須載入**：主網站的 CSS（`../css/tailwind.css` + `../css/site-common.css`）
- ✅ **寬度控制**：使用 CSS 強制 CMS 內容置中對齊
  ```css
  body > div {
      max-width: 1200px !important;
      margin: 0 auto !important;
  }
  ```
- ✅ **配色一致**：CMS 導航列和按鈕顏色應與主網站一致（#671919）

**避免的問題**：
- ❌ CMS 內容滿版顯示（無左右留白）
- ❌ CMS 編輯頁面與主網站寬度不一致
- ❌ 使用獨立的 CSS 檔案而不是共用 `site-common.css`

### 主色系定義

**定義位置**：`css/site-common.css`

**主要顏色**：
- 主色（深紅）：`#671919`
- 強調色（橙黃）：`#efa22a`
- Footer 深色：`#3e0f0f`

**使用規範**：
- 導航列背景：主色 `#671919`
- 懸停效果：強調色 `#efa22a`
- 主要按鈕：主色 `#671919`
- Footer 背景：深色 `#3e0f0f`

### 字體大小

**全站統一**：
- 基礎字體大小：`15px`
- 行高：`1.6`

**定義於**：`site-common.css` 的 `body` 選擇器

### 響應式設計

**中等螢幕以下**：
- 左右內距增加至 `20px`
- 容器寬度自動調整為 100%（扣除內距）

**小螢幕**：
- 導航折疊
- 字體大小適度縮小

### 檢查清單

建立或修改任何頁面時，請確認：

- [ ] 已載入 `tailwind.css` 和 `site-common.css`
- [ ] 主要內容使用 `.container-1200` 包裹
- [ ] 頁面有適當的左右留白（在大螢幕上查看）
- [ ] 顏色使用主色系（#671919, #efa22a）
- [ ] 字體大小為 15px
- [ ] 導航列、Banner、Footer 都在 `.container-1200` 容器內

---

## 🌍 雙語架構（2026 新增）

### 概述

網站採用**語言目錄分離**架構：
- **中文版本**（預設）：根目錄 `/`
- **英文版本**：獨立目錄 `/en/`

### 目錄結構

與 [ARCHITECTURE.md](ARCHITECTURE.md) 一致：根目錄為中文，`/en/` 為英文版本；頁面對應見該文件「頁面對應關係」表。

```
/                        # 中文版本（預設）
├── index.html
├── about/
├── faculty/
└── ...

/en/                     # 英文版本
├── index.html
├── about/
├── faculty/
└── ...
```

### 動態 Banner 系統

**資料檔案**：`_data/banner.json`（雙語內容）

**核心腳本**：
- `js/load-banner.js` - 動態載入 Banner
- `js/i18n.js` - 多語言支援

**工作原理**：
1. 頁面載入時自動偵測語言（根據 URL）
2. 從 `banner.json` 載入對應語言內容
3. 動態渲染到頁面

**修改 Banner**：
- 方法 1：直接編輯 `_data/banner.json`
- 方法 2：透過 Decap CMS（`/admin/`）視覺化編輯

### 語言切換

在導航列加入語言切換器：

```html
<div class="language-switcher">
    <a href="#" data-lang-switch="zh">中文</a>
    <a href="#" data-lang-switch="en">English</a>
</div>
```

`i18n.js` 會自動處理點擊事件和 URL 轉換。

---

## ⚙️ Decap CMS 整合（2026 新增）

### 什麼是 Decap CMS？

Decap CMS（前身為 Netlify CMS）是一個開源的內容管理系統，專為靜態網站設計：
- ✅ Git-based：所有變更儲存在 GitHub
- ✅ 視覺化編輯：非技術人員也能使用
- ✅ 支援 Markdown：適合內容撰寫
- ✅ 圖片上傳：內建媒體管理功能

### 存取 CMS

**URL**：`https://your-site.netlify.app/admin/`

**登入**：使用 Netlify Identity

### CMS 可管理的內容

1. **網站全域設定**
   - Banner 內容（中英文）
   - 導航選單
   - 聯絡資訊

2. **新聞與活動**
   - 發布新聞
   - 建立活動資訊
   - 支援雙語內容

3. **師資介紹**
   - 新增/編輯教師資料
   - 上傳教師照片
   - 管理學經歷

### 配置檔案

**位置**：`admin/config.yml`

**結構**：
- **backend**：Git Gateway 設定
- **collections**：定義可管理的內容類型
- **media_folder**：圖片上傳位置

### 使用流程

```bash
# 1. 登入 CMS
# 訪問 /admin/ → 使用 Netlify Identity 登入

# 2. 編輯內容
# 選擇要編輯的集合（如「網站設定」→「Banner 設定」）

# 3. 儲存變更
# 點擊「Save」→「Publish」

# 4. 自動部署
# GitHub 自動接收提交 → Netlify 自動重新部署
```

### 重要提醒

- ⚠️ CMS 的變更會直接提交到 GitHub
- ✅ 使用「Editorial Workflow」可先存為草稿
- 💾 建議定期備份 `_data/` 目錄

### Admin 自訂腳本建置（Option A）

集合列表的**表格/格狀**切換與多欄表格來自自訂腳本；建置後 commit 建檔，deploy 不變。

- **來源**：`admin-src/cms-custom.js`
- **建置**：`npm run build:admin` → 輸出 `admin/cms-custom.js`
- **Deploy**：照常 push；Netlify/GitHub Pages 直接提供建好的 `admin/cms-custom.js`，伺服器不需建置。

**修改自訂邏輯時**：編輯 `admin-src/cms-custom.js` → 執行 `npm run build:admin` → 一併 commit `admin/cms-custom.js`。  
專案內 Cursor 規則 `.cursor/rules/admin-build.mdc` 會提醒 AI：只要改動 `admin-src/`，就自動執行建置並納入建檔。

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
# 1. 在 Decap CMS「師資介紹」新增一筆，或於 faculty/_profiles/ 新增 newteacher.md（YAML front matter + body）
# 2. 準備照片（使用英文 ID 命名）並上傳或放入 images/faculty/newteacher.jpg
# 3. 產生列表 JSON
python3 scripts/data/generate-faculty-json.py

# 4. 建置模板（如有需要）
python3 build-templates.py

# 5. 檢查頁面：開啟 faculty/faculty.html 或對應列表頁
```

### 任務 3：管理新聞與活動內容

**方式一（推薦）**：使用 Decap CMS  
- 訪問 `https://your-site.netlify.app/admin/` → 登入 → 選擇新聞或活動集合編輯 → 發布（自動提交至 GitHub，Netlify 建置產生 `data/news.json`、`data/activities.json`）。

**方式二**：直接編輯 `news/_posts/`、`activities/_posts/` 的 Markdown → 執行 `./stop.sh` 或推送後由 Netlify 建置產生 `data/news.json`、`data/activities.json`。

### 任務 4：修改 Banner

**修改文案（中英文標題、副標題、Logo）**：
- 編輯 `_data/banner.json`，或透過 Decap CMS「網站設定 → Banner 設定」→ 發布。  
- 無需建置，`load-banner.js` 會動態載入。

**修改 Banner 的 HTML 結構或樣式**：
```bash
# 1. 編輯 Banner 模板
vim templates/site-banner.html

# 2. 建置
python3 build-templates.py
```

### 任務 5：調整間距

```bash
# 全站統一使用 py-4
# 已執行過批量修正，目前所有 py-8 和 py-12 都改為 py-4

# 如需再次修正（不建議）：
# 使用 scripts/ 中的 fix-padding.sh
```

### 任務 6：新增頁面

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
// 1. 從 data/faculty_data.json 載入資料（該檔由 generate-faculty-json.py 從 _profiles/*.md 產生）
fetch('../data/faculty_data.json')

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
   - 編輯 `faculty/_profiles/*.md` 或透過 Decap CMS「師資介紹」
   - 執行 `python3 scripts/data/generate-faculty-json.py` 更新列表 JSON
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
- `netlify.toml` - Netlify 建置與部署設定（與 ARCHITECTURE 一致）

**資料檔案**：
- `_data/banner.json`、`_data/navigation.json`、`_data/site_settings.json` - CMS/雙語共用資料
- `data/faculty_data.json` - 教師資料（由 faculty/_profiles 建置）
- `data/news.json`、`data/activities.json` - 新聞與活動（由 news/_posts、activities/_posts 建置）
- `data/faculty-mapping.csv` - 照片對應

**後台與模板**：
- `admin/index.html`、`admin/config.yml` - Decap CMS 入口與配置
- `templates/` - 所有模板
- `images/faculty/`、`images/uploads/` - 教師照片與 CMS 上傳
- `css/`, `js/` - 樣式和腳本（含 `js/load-banner.js`、`js/i18n.js`）

### 參考文檔

- `README.md` - 專案說明
- `CLAUDE.md` - 本文檔
- `ARCHITECTURE.md` - 架構規劃（目錄結構、雙語、Decap CMS、部署）
- `templates/README.md` - 模板系統說明
- `scripts/README.md` - 輔助腳本說明
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
# 建置模板（與 ARCHITECTURE / Netlify 建置一致）
python3 build-templates.py

# 安裝依賴
npm install

# 編譯 Tailwind（可選）
npm run build:css

# 執行資料處理腳本
python3 scripts/data/[腳本名].py
python3 scripts/maintenance/[腳本名].py

# 轉換 HTML 為使用模板（首次設定，不常用）
python3 scripts/build/convert-to-templates.py
```

### 重要路徑

```
# 核心與部署（與 ARCHITECTURE 一致）
build-templates.py               # 建置模板
netlify.toml                     # Netlify 建置/部署設定

# 共用資料與 CMS
_data/banner.json                # Banner 雙語內容（Decap CMS 可編輯）
_data/navigation.json            # 導航選單
admin/config.yml                 # Decap CMS 配置
admin/index.html                 # CMS 入口

# 模板系統
templates/site-nav.html          # 修改導航列
templates/site-banner.html       # Banner 結構（文案來自 _data/banner.json）
templates/site-footer.html       # 修改頁尾

# 動態載入
js/load-banner.js                # Banner 依語言載入 _data/banner.json
js/i18n.js                       # 語言切換

# 教師與內容資料
data/faculty_data.json           # 教師資料庫（建置自 faculty/_profiles）
data/news.json                   # 新聞（建置自 news/_posts）
data/activities.json              # 活動（建置自 activities/_posts）
images/faculty/                  # 教師照片
images/uploads/                  # CMS 上傳

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

### 2026-01-31

#### 與 ARCHITECTURE.md 結構對齊
- ✅ **目錄結構**：改為與 ARCHITECTURE 一致，加入 `_data/`、`admin/`（config.yml）、`en/`、`news/_posts/`、`activities/_posts/`、`graduate/`、`netlify.toml` 等
- ✅ **核心系統**：新增「_data/ 與 Banner 統一管理」；CMS 以 Decap CMS（admin/config.yml、_data/）為主，本地 CSV 編輯為可選；新增「部署流程」節
- ✅ **常見任務**：修改 Banner 區分「文案」（_data/banner.json 或 CMS）與「結構」（templates + 建置）；管理內容改為以 Decap CMS 為推薦方式；任務編號修正（任務 4～6）
- ✅ **檔案清單與快速參考**：納入 _data/、admin/config.yml、netlify.toml、load-banner.js、i18n.js
- ✅ **雙語與協作**：雙語目錄、常見任務速查、給 AI 的建議均對齊 ARCHITECTURE

### 2025-12-11

#### 專案結構重新整理
- ✅ **資料檔案集中管理**：
  - 移動 `faculty_data.json` 和 `faculty-mapping.csv` 到 `data/` 資料夾
  - 統一資料檔案位置，便於備份和管理

- ✅ **輔助腳本分類整理**：
  - 建立 `scripts/build/`、`scripts/data/`、`scripts/maintenance/` 三個子資料夾
  - 移動 14 個根目錄的 Python 腳本到對應分類
  - 根目錄只保留核心腳本：`build-templates.py`

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

#### 歷史：本地 CMS 與編輯器（已移除，現行架構為 Decap CMS）
- 專案現以 **Decap CMS + Netlify + GitHub Pages** 為主：內容來自 `news/_posts`、`activities/_posts`、`faculty/_profiles` 與 `_data/`，建置產生 `data/*.json`。

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

1. **先讀 ARCHITECTURE.md**：目錄結構、雙語設計、Decap CMS、部署流程以該文件為準。

2. **模板系統**：共用區塊在 `templates/`，建置用 `python3 build-templates.py`；Banner 文案在 `_data/banner.json`，由 `load-banner.js` 動態載入。

3. **資料驅動**：教師由 `data/faculty_data.json` 驅動；Banner/導航/設定在 `_data/`，可經 Decap CMS 編輯。

4. **路徑處理**：建置腳本自動處理 `{{path_prefix}}`，勿手動改 `../`。

### 協作原則

1. **先讀文檔**：
   - 架構與目錄以 [ARCHITECTURE.md](ARCHITECTURE.md) 為準
   - 本文檔（CLAUDE.md）為操作與任務指引
   - 必要時查 `templates/README.md`、`scripts/README.md`

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
| 改 Banner 文案 | 編輯 `_data/banner.json` 或 Decap CMS「Banner 設定」→ 發布（無需建置） |
| 改 Banner 結構 | 編輯 `templates/site-banner.html` → 建置 |
| 加教師 | 編輯 `faculty/_profiles/*.md` 或 Decap CMS「師資介紹」→ 執行 `generate-faculty-json.py` + 照片於 `images/faculty/` |
| 改樣式 | 編輯 `css/` 檔案 |
| 新頁面 | 複製 `templates/example-page.html` → 建置 |
| 管理內容（Banner/新聞/活動） | Decap CMS：`/admin/` 登入 → 選擇集合編輯 → 發布 |

---

**最後更新**：2026-01-31
**維護者**：Claude AI + 台大新聞所團隊
**文檔版本**：2.0（與 ARCHITECTURE.md 結構對齊）
