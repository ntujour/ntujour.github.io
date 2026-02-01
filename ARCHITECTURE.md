# 台大新聞所網站 - 架構規劃文件

> **版本**: 2.0  
> **更新日期**: 2026-01-31  
> **架構類型**: GitHub Pages + Netlify + Decap CMS + 雙語靜態網站

---

## 📋 目錄

1. [網站定位](#網站定位)
2. [技術架構](#技術架構)
3. [目錄結構](#目錄結構)
4. [雙語設計方案](#雙語設計方案)
5. [Decap CMS 整合](#decap-cms-整合)
6. [Banner 統一管理](#banner-統一管理)
7. [部署流程](#部署流程)
8. [實施階段](#實施階段)

---

## 🎯 網站定位

### 核心目標
- **主要語言**: 繁體中文（默認）
- **次要語言**: 英文（國際化需求）
- **目標受眾**: 
  - 主要：台灣本地學生、教職員、校友
  - 次要：國際學生、國際學者

### 功能需求
- ✅ 雙語內容管理
- ✅ 新聞與活動發布
- ✅ 師資介紹
- ✅ 招生資訊
- ✅ 學生資源
- ✅ 後台內容管理系統（CMS）

### 技術要求
- ✅ 靜態網站（快速、安全）
- ✅ 易於維護（非技術人員可操作）
- ✅ SEO 友善
- ✅ 行動裝置優化
- ✅ 無障礙設計

---

## 🏗️ 技術架構

### 技術棧

```
┌─────────────────────────────────────────┐
│         使用者訪問網站                    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    GitHub Pages / Netlify (託管)         │
│    - 靜態 HTML/CSS/JavaScript            │
│    - Tailwind CSS 樣式                   │
│    - 動態資料載入 (Fetch API)            │
└─────────────────────────────────────────┘
                    ↑
┌─────────────────────────────────────────┐
│         內容管理者透過 CMS 編輯           │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│          Decap CMS (管理介面)            │
│    - 視覺化編輯器                        │
│    - 圖片上傳                            │
│    - 雙語內容管理                        │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│      Netlify Identity (身份驗證)         │
│    - 登入/登出                           │
│    - 權限管理                            │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│     GitHub Repository (版本控制)         │
│    - 自動提交變更                        │
│    - 版本歷史追蹤                        │
│    - 自動部署觸發                        │
└─────────────────────────────────────────┘
```

### 核心技術

| 技術 | 用途 | 版本/來源 |
|------|------|-----------|
| **HTML5** | 頁面結構 | - |
| **Tailwind CSS** | 樣式框架 | v3.x |
| **JavaScript (ES6+)** | 互動邏輯、資料載入 | 原生 JS |
| **Decap CMS** | 內容管理系統 | Latest |
| **GitHub Pages** | 靜態網站託管 | - |
| **Netlify** | 部署、Identity | - |
| **Git** | 版本控制 | - |

---

## 📁 目錄結構

### 完整目錄樹

```
ntujour.github.io/
│
├── 📁 admin/                          # Decap CMS 管理後台
│   ├── index.html                    # CMS 入口頁面
│   └── config.yml                    # CMS 配置檔案 ⭐
│
├── 📁 _data/                          # 共用資料檔案（JSON）
│   ├── banner.json                   # Banner 內容（雙語）⭐
│   ├── navigation.json               # 導航選單（雙語）⭐
│   ├── site_settings.json            # 網站全域設定（雙語）⭐
│   └── backups/                      # 資料備份目錄
│
├── 📁 templates/                      # HTML 模板
│   ├── site-banner.html              # Banner 模板
│   ├── site-nav.html                 # 導航列模板
│   ├── site-footer.html              # 頁尾模板
│   └── site-sitemap.html             # 網站地圖模板
│
├── 📁 js/                             # JavaScript 檔案
│   ├── load-banner.js                # 動態載入 Banner ⭐
│   ├── load-nav.js                   # 動態載入導航 ⭐
│   ├── i18n.js                       # 多語言切換 ⭐
│   ├── faculty.js                    # 師資頁面邏輯
│   └── ...
│
├── 📁 css/                            # 樣式檔案
│   ├── styles.css                    # 主要樣式表
│   └── tailwind.css                  # Tailwind 編譯輸出
│
├── 📁 images/                         # 圖片資源
│   ├── uploads/                      # CMS 上傳的圖片 ⭐
│   ├── faculty/                      # 教師照片
│   └── ...
│
├── 📁 data/                           # 原有資料檔案
│   ├── faculty_data.json             # 教師資料（將遷移）
│   ├── content.csv                   # 新聞活動資料（將遷移）
│   └── backups/                      # 備份
│
├── 📁 news/                           # 新聞/消息
│   └── _posts/                       # Markdown 格式文章 ⭐
│       ├── 2026-01-31-example.md
│       └── ...
│
├── 📁 activities/                     # 系所活動
│   └── _posts/                       # Markdown 格式文章 ⭐
│       ├── 2026-01-31-workshop.md
│       └── ...
│
├── 📁 faculty/                        # 師資介紹（中文）
│   ├── _profiles/                    # 教師個人頁面 Markdown（單一來源）⭐
│   ├── .archive/                     # 舊版 HTML、_profiles_legacy/
│   ├── faculty.html                  # 師資總覽
│   ├── fulltime-professor.html       # 專任教師
│   └── ...
│
├── 📁 about/                          # 關於我們（中文）
│   ├── intro.html                    # 簡介
│   ├── mission.html                  # 宗旨
│   └── ...
│
├── 📁 admissions/                     # 入學資訊（中文）
├── 📁 students/                       # 學生學習（中文）
├── 📁 publications/                   # 出版發表（中文）
│
├── 📁 en/                             # 英文版本 ⭐
│   ├── index.html                    # 英文首頁
│   ├── news.html                     # 英文新聞
│   ├── about/                        # 英文關於我們
│   ├── admissions/                   # 英文入學資訊
│   ├── faculty/                      # 英文師資介紹
│   └── ...
│
├── 📁 graduate/                       # 學生專用區域（隱藏）
│   └── ...                           # 不列入主選單
│
├── 📄 index.html                      # 中文首頁
├── 📄 news.html                       # 中文新聞頁面
├── 📄 activities.html                 # 中文活動頁面
├── 📄 resources.html                  # 中文資源頁面
├── 📄 staff.html                      # 中文行政人員
├── 📄 404.html                        # 404 錯誤頁面
│
├── 📄 build-templates.py              # 模板建置腳本
├── 📄 netlify.toml                    # Netlify 配置 ⭐
├── 📄 package.json                    # Node.js 依賴
└── 📄 tailwind.config.js              # Tailwind 設定
```

**圖例**：
- ⭐ = 新增或重點修改的檔案
- 📁 = 目錄
- 📄 = 檔案

### 目錄設計原則

1. **中文優先**: 根目錄為中文版本（預設語言）
2. **英文獨立**: `/en/` 目錄包含完整的英文版本
3. **資料分離**: `_data/` 統一管理所有可編輯資料
4. **內容分類**: 新聞和活動使用 Markdown 格式儲存
5. **隱藏目錄**: `graduate/` 不列入主選單，只供知道連結者訪問

---

## 🌍 雙語設計方案

### 語言架構

#### 方案：**語言目錄分離（推薦）**

```
/                    → 中文版本（預設）
/en/                 → 英文版本
```

**優點**：
- ✅ URL 語義清晰 (`/en/about/` = 英文關於頁面)
- ✅ SEO 友善（搜尋引擎易於區分語言）
- ✅ 易於維護（各語言獨立目錄）
- ✅ 支援 `hreflang` 標籤
- ✅ 符合國際化標準

### 頁面對應關係

| 功能 | 中文路徑 | 英文路徑 |
|------|---------|---------|
| 首頁 | `/index.html` | `/en/index.html` |
| 關於我們 | `/about/intro.html` | `/en/about/intro.html` |
| 師資介紹 | `/faculty/faculty.html` | `/en/faculty/faculty.html` |
| 入學資訊 | `/admissions/admissions.html` | `/en/admissions/admissions.html` |
| 最新消息 | `/news.html` | `/en/news.html` |
| 系所活動 | `/activities.html` | `/en/activities.html` |
| 學生學習 | `/students/...` | `/en/students/...` |

### 語言切換機制

#### 1. 導航列語言切換器

```html
<!-- 位於每個頁面的導航列 -->
<div class="language-switcher">
    <a href="/index.html" class="lang-link active">中文</a>
    <a href="/en/index.html" class="lang-link">English</a>
</div>
```

#### 2. 自動偵測語言

```javascript
// js/i18n.js
function detectLanguage() {
    const path = window.location.pathname;
    return path.startsWith('/en/') ? 'en' : 'zh';
}

function switchLanguage(targetLang) {
    const currentPath = window.location.pathname;
    let newPath;
    
    if (targetLang === 'en' && !currentPath.startsWith('/en/')) {
        newPath = '/en' + currentPath;
    } else if (targetLang === 'zh' && currentPath.startsWith('/en/')) {
        newPath = currentPath.replace('/en/', '/');
    }
    
    if (newPath) {
        window.location.href = newPath;
    }
}
```

#### 3. SEO 優化（hreflang 標籤）

```html
<!-- 在每個頁面的 <head> 中 -->
<link rel="alternate" hreflang="zh-TW" href="https://journalism-ntu.github.io/about/intro.html" />
<link rel="alternate" hreflang="en" href="https://journalism-ntu.github.io/en/about/intro.html" />
<link rel="alternate" hreflang="x-default" href="https://journalism-ntu.github.io/about/intro.html" />
```

---

## ⚙️ Decap CMS 整合

### 為什麼選擇 Decap CMS？

| 優勢 | 說明 |
|------|------|
| ✅ **開源免費** | MIT 授權，無額外費用 |
| ✅ **Git-based** | 所有變更儲存在 GitHub，完整版本控制 |
| ✅ **視覺化編輯** | 非技術人員也能輕鬆使用 |
| ✅ **靜態網站完美整合** | 專為 JAMstack 設計 |
| ✅ **彈性配置** | 支援各種資料結構和欄位類型 |
| ✅ **預覽功能** | 發布前可預覽內容 |

### CMS 管理範圍

透過 Decap CMS 可以管理：

1. **網站全域設定**
   - Banner 內容（中英文標題、副標題、Logo）
   - 導航選單結構
   - 聯絡資訊
   - 社群媒體連結

2. **內容管理**
   - 新聞/消息（雙語）
   - 系所活動（雙語）
   - 師資介紹（雙語）

3. **媒體資源**
   - 圖片上傳與管理
   - 教師照片
   - 活動照片

### CMS 配置重點

#### 1. 後端設定

```yaml
backend:
  name: git-gateway
  branch: main
```

#### 2. 媒體檔案

```yaml
media_folder: "images/uploads"
public_folder: "/images/uploads"
```

#### 3. 集合定義

- **設定類集合** (`files`): Banner、導航、網站資訊
- **內容類集合** (`folder`): 新聞、活動、教師

詳細配置請參考 `admin/config.yml`

---

## 🎨 Banner 統一管理

### 設計目標

- ✅ 透過 CMS 視覺化編輯 Banner
- ✅ 支援中英文內容
- ✅ 自動語言切換
- ✅ 所有頁面統一更新

### 技術方案

#### 1. 資料儲存

`_data/banner.json`:
```json
{
  "title_zh": "國立臺灣大學新聞研究所",
  "title_en": "Graduate Institute of Journalism, National Taiwan University",
  "subtitle_zh": "培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才",
  "subtitle_en": "Cultivating journalism professionals for the new era",
  "logo": ""
}
```

#### 2. 動態載入

`js/load-banner.js`:
- 根據當前語言載入對應內容
- 自動偵測中文/英文頁面
- 動態生成 HTML

#### 3. 模板整合

`templates/site-banner.html`:
- 提供 Banner 外框
- 載入 JavaScript 腳本
- 自動渲染內容

### 工作流程

```
1. 管理員登入 CMS (/admin/)
          ↓
2. 編輯 "Banner 設定"
          ↓
3. 修改中文/英文標題、副標題
          ↓
4. 儲存變更
          ↓
5. GitHub 自動提交
          ↓
6. Netlify 自動部署
          ↓
7. 網站所有頁面的 Banner 自動更新
```

---

## 🚀 部署流程

### 部署架構

```
開發 → GitHub → Netlify → 生產環境
```

### Netlify 設定

#### 1. 基本配置 (`netlify.toml`)

```toml
[build]
  publish = "."
  command = "python3 build-templates.py"

[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404
```

#### 2. Netlify Identity 設定

- **用途**: CMS 登入驗證
- **設定位置**: Netlify Dashboard → Site settings → Identity
- **必要步驟**:
  1. 啟用 Identity
  2. 啟用 Git Gateway
  3. 邀請使用者（管理員）

#### 3. 環境變數（可選）

| 變數名稱 | 用途 |
|---------|------|
| `NODE_VERSION` | Node.js 版本（建議 18） |

### 自動部署流程

1. **觸發條件**:
   - Push 到 `main` 分支
   - 透過 CMS 儲存內容

2. **建置步驟**:
   ```bash
   # 安裝依賴
   npm ci
   
   # 建置模板
   python3 build-templates.py
   
   # 編譯 Tailwind (可選)
   npm run build:css
   ```

3. **部署**:
   - Netlify 自動部署到 CDN
   - 約 1-2 分鐘完成

### 域名設定

| 環境 | 域名 |
|------|------|
| **Netlify** | `https://ntujour.netlify.app` |
| **GitHub Pages** | `https://ntujour.github.io` |
| **自訂域名**（可選） | `https://journalism.ntu.edu.tw` |

---

## 📅 實施階段

### 階段一：基礎架構建置（Week 1-2）

**目標**: 建立 CMS 基礎和雙語框架

- [ ] 設定 Netlify 專案
- [ ] 啟用 Netlify Identity
- [ ] 配置 Decap CMS (`admin/config.yml`)
- [ ] 建立 `_data/` 資料結構
- [ ] 實作動態 Banner 載入
- [ ] 建立語言切換機制

**驗收標準**:
- ✅ 可透過 `/admin/` 登入 CMS
- ✅ 可編輯 Banner 內容並即時預覽
- ✅ 語言切換功能正常運作

---

### 階段二：內容遷移（Week 3-4）

**目標**: 將現有內容遷移到新架構

- [ ] 遷移教師資料到 Markdown 格式
- [ ] 遷移新聞資料（`data/content.csv` → Markdown）
- [ ] 遷移活動資料
- [ ] 建立英文目錄結構 (`/en/`)
- [ ] 翻譯核心頁面（首頁、關於、招生）

**驗收標準**:
- ✅ 所有教師資料可透過 CMS 編輯
- ✅ 新聞與活動正確顯示
- ✅ 英文頁面基本架構完成

---

### 階段三：雙語內容建置（Week 5-6）

**目標**: 完成雙語內容和功能

- [ ] 翻譯所有核心頁面
- [ ] 實作導航選單雙語切換
- [ ] 建立雙語新聞/活動模板
- [ ] 設定 SEO 雙語標籤
- [ ] 測試所有語言切換功能

**驗收標準**:
- ✅ 所有頁面有對應英文版本
- ✅ 語言切換無死連結
- ✅ SEO 標籤正確設定

---

### 階段四：整合與優化（Week 7-8）

**目標**: 系統整合和效能優化

- [ ] 整合註冊表單
- [ ] 優化圖片載入（lazy loading）
- [ ] 設定 CDN 快取
- [ ] 無障礙測試（WCAG 2.1）
- [ ] 行動裝置測試
- [ ] 瀏覽器相容性測試

**驗收標準**:
- ✅ Lighthouse 分數 > 90
- ✅ 無障礙等級達 AA
- ✅ 所有主流瀏覽器正常運作

---

### 階段五：上線與移交（Week 9）

**目標**: 正式上線和文件移交

- [ ] 最終測試
- [ ] 備份舊網站
- [ ] DNS 切換（如使用自訂域名）
- [ ] 培訓管理員使用 CMS
- [ ] 撰寫操作手冊
- [ ] 正式上線

**驗收標準**:
- ✅ 網站正式上線
- ✅ 管理員能獨立操作 CMS
- ✅ 文件完整移交

---

## 📚 相關文件

| 文件 | 說明 | 位置 |
|------|------|------|
| **README.md** | 專案說明和快速開始 | `/README.md` |
| **CLAUDE.md** | AI 協作指南和技術細節 | `/CLAUDE.md` |
| **ARCHITECTURE.md** | 本文件 - 架構規劃 | `/ARCHITECTURE.md` |
| **CMS 操作手冊** | 給管理員的 CMS 使用指南 | `/docs/CMS_USER_GUIDE.md` |
| **部署指南** | 部署流程和注意事項 | `/DEPLOYMENT_GUIDE.md` |

---

## 🔗 參考資源

- [Decap CMS 官方文件](https://decapcms.org/docs/)
- [Netlify 文件](https://docs.netlify.com/)
- [GitHub Pages 文件](https://docs.github.com/pages)
- [Tailwind CSS 文件](https://tailwindcss.com/docs)
- [Web 無障礙指南 (WCAG)](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 📞 聯絡資訊

- **專案維護**: 台大新聞所資訊小組
- **技術支援**: [開發者聯絡方式]
- **CMS 問題回報**: [GitHub Issues](https://github.com/jirlong/ntujour-web/issues)

---

**最後更新**: 2026-01-31  
**文件版本**: 2.0  
**維護者**: Claude AI + 台大新聞所團隊
