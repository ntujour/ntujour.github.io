# 🚀 GitHub Pages 部署指南

> 台大新聞所網站 - 部署到 GitHub Pages 的完整指引

---

## 📋 目前架構說明

### ✅ **適合 GitHub Pages 的設計**

- **靜態網站**：不需要後端伺服器（Python/Node.js/PHP）
- **前端動態載入**：使用 JavaScript fetch() 載入 JSON 資料
- **相對路徑**：所有路徑都使用相對路徑，部署後自動正確

### 🎯 **部署策略**

| 內容類型 | 實作方式 | 需要上傳 |
|---------|---------|---------|
| HTML 頁面 | 靜態檔案 | ✅ 是 |
| CSS 樣式 | 靜態檔案 | ✅ 是 |
| JavaScript | 靜態檔案 | ✅ 是 |
| 圖片資源 | 靜態檔案 | ✅ 是 |
| 教職員資料 | JSON（前端動態載入） | ✅ 是 |
| 新聞/活動資料 | JSON/CSV（前端動態載入） | ✅ 是 |
| 建置工具 | Python 腳本 | ❌ 否 |
| 模板檔案 | HTML 模板 | ❌ 否 |

---

## 📦 需要上傳到 GitHub 的檔案

### ✅ **必須上傳**（網站運作所需）

```
📁 根目錄
├── index.html
├── news.html
├── activities.html
├── staff.html
├── resources.html
├── article.html
├── article-view.html
└── README.md（可選）

📁 faculty/
├── faculty.html
├── fulltime-professor.html
├── practical-professor.html
├── parttime-professor.html
├── honorary-professor.html
├── joint-professor.html
└── [教師個人頁面].html

📁 about/
├── intro.html
├── transportation.html
└── donate.html

📁 admissions/
└── [所有入學資訊頁面]

📁 students/
└── [所有學生學習頁面]

📁 publications/
└── [所有出版發表頁面]

📁 css/
├── tailwind.css       ⭐ 必要！
└── site-common.css

📁 js/
├── faculty.js
├── fulltime-faculty-detail.js
├── practical-faculty-detail.js
├── parttime-faculty-detail.js
├── honorary-faculty-detail.js
├── joint-faculty-detail.js
├── combined-news.js
├── news.js
├── activities.js
├── homepage.js
└── article-view.js

📁 data/
├── faculty_data.json    ⭐ 前端需要（由 faculty/_profiles/*.md 建置產生）
├── activities.json      ⭐ 前端需要（由 activities/_posts/*.md 建置產生）
├── news.json            ⭐ 前端需要（由 news/_posts/*.md 建置產生）
├── e-reports.csv
└── faculty-mapping.csv  （可選，前端不需要）

📁 images/
├── faculty/           # 所有教職員照片
├── news/             # 新聞圖片
├── activities/       # 活動圖片
├── reports/          # 所報 PDF
└── regulations/      # 修業規定圖片

📁 admin/
├── index.html              # Decap CMS 入口
└── config.yml              # CMS 配置

📁 _data/
├── banner.json
├── navigation.json
└── site_settings.json
```

### ❌ **不需上傳**（可選加入 .gitignore）

```
📦 開發環境
├── node_modules/
├── archive/
└── data/backups/
```

**必須保留在 repo**（Netlify 建置需要）：
- `build-templates.py`、`scripts/`、`templates/`
```

---

## 🚀 部署步驟

### **方法 1：使用 GitHub Desktop（推薦給不熟悉 Git 的使用者）**

1. **下載並安裝 GitHub Desktop**
   - 訪問：https://desktop.github.com/
   - 安裝後登入你的 GitHub 帳號

2. **Clone 或建立 Repository**
   ```
   File → Clone Repository
   或
   File → New Repository
   ```

3. **選擇專案資料夾**
   - 選擇 `ntujour.github.io` 資料夾

4. **Commit 變更**
   - GitHub Desktop 會自動顯示變更的檔案
   - 輸入 Commit 訊息（例如：「更新教職員資料」）
   - 點擊「Commit to main」

5. **Push 到 GitHub**
   - 點擊「Push origin」

6. **設定 GitHub Pages**
   - 到 GitHub 網站上的 Repository
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
   - 點擊 Save

7. **等待部署完成**
   - 通常需要 1-2 分鐘
   - 部署完成後訪問：`https://[你的帳號].github.io/[repo名稱]`

---

### **方法 2：使用 Git 指令（推薦給熟悉指令的使用者）**

#### **首次部署**

```bash
# 1. 初始化 Git（如果還沒有）
git init

# 2. 加入所有需要的檔案
git add .

# 3. 建立第一次 Commit
git commit -m "Initial commit: 台大新聞所網站"

# 4. 連結到 GitHub Repository
git remote add origin https://github.com/[你的帳號]/[repo名稱].git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main
```

#### **設定 GitHub Pages**
```bash
# 到 GitHub 網站設定 Pages（只需設定一次）
# Repository → Settings → Pages
# Source: Deploy from a branch
# Branch: main
# Folder: / (root)
```

#### **日常更新**

```bash
# 1. 查看變更
git status

# 2. 加入變更的檔案
git add .
# 或只加入特定檔案
git add data/content.csv
git add faculty/faculty.html

# 3. Commit
git commit -m "更新新聞與活動內容"

# 4. 推送到 GitHub
git push

# 5. 等待 GitHub Pages 自動部署（1-2 分鐘）
```

---

## 🔄 常見更新情境

### **情境 1：更新教職員資料**

```bash
# 1. 編輯教職員資料
vim data/faculty_data.json

# 2. 如果照片也更新了
cp new-photo.jpg images/faculty/newteacher.jpg

# 3. Commit 並推送
git add data/faculty_data.json images/faculty/
git commit -m "更新教職員資料"
git push
```

**注意**：目前教職員資料是前端動態載入，更新 `faculty_data.json` 後，前端會自動顯示新資料。

---

### **情境 2：更新新聞或活動**

#### 使用 Decap CMS（推薦，需先設定 Netlify + Identity）

- 登入 `https://your-site.netlify.app/admin/` → 選擇新聞或活動集合 → 編輯 → 發布（自動提交至 GitHub）。

#### 直接編輯 Markdown（不經 CMS）

```bash
# 1. 編輯活動文章
vim activities/_posts/YYYY-MM-DD-slug.md

# 2. 產生 JSON 並建置（或等 Netlify 建置）
./stop.sh   # 或：python3 scripts/data/generate-activities-json.py && python3 build-templates.py

# 3. Commit 並推送
git add activities/_posts/ data/activities.json
git commit -m "新增活動：[活動標題]"
git push
```

---

### **情境 3：更新網站樣式或內容**

```bash
# 1. 修改 HTML 或 CSS
vim faculty/faculty.html
vim css/site-common.css

# 2. 如果修改了模板，需要重新建置
python3 build-templates.py

# 3. Commit 並推送
git add faculty/faculty.html css/
git commit -m "更新樣式：調整教職員頁面排版"
git push
```

---

## ⚠️ 重要注意事項

### **1. .gitignore 已設定**（依專案設定）
- ✅ 備份檔案（data/backups/）可加入 .gitignore
- ✅ 開發環境檔案（node_modules/, .vscode/）不會上傳
- 註：build-templates.py、templates/、scripts/ 通常保留在 repo 內供 Netlify 建置使用

### **2. 資料檔案必須上傳**
- ⚠️ `data/faculty_data.json` - 前端需要（建置自 faculty/_profiles）
- ⚠️ `data/activities.json` - 前端需要（建置自 activities/_posts）
- ⚠️ `data/news.json` - 前端需要（建置自 news/_posts）

### **3. CSS 檔案必須上傳**
- ⚠️ `css/tailwind.css` - 網站樣式必需
- ⚠️ `css/site-common.css` - 網站樣式必需

### **4. 不要上傳敏感資訊**
- ❌ 不要在 CSV 或 JSON 中包含個人敏感資訊
- ❌ 不要上傳私人筆記或內部文件
- ❌ 檢查圖片檔案名稱，避免包含敏感資訊

---

## 🧪 部署前測試

### **本地測試**

```bash
# 方法 1：Python HTTP Server
python3 -m http.server 8000
# 訪問：http://localhost:8000

# 方法 2：Node.js HTTP Server
npx http-server
# 訪問：http://localhost:8080
```

### **檢查清單**

- [ ] 所有頁面連結正常（沒有 404）
- [ ] 教職員資料正確顯示
- [ ] 新聞與活動正確載入
- [ ] 圖片正確顯示
- [ ] CSS 樣式正確套用
- [ ] 手機版排版正常（響應式設計）

---

## 🔍 故障排除

### **問題 1：教職員資料不顯示**

**原因**：JSON 檔案未上傳或路徑錯誤

**解決方案**：
```bash
# 檢查檔案是否在 Git 中
git ls-files | grep faculty_data.json

# 如果沒有，手動加入
git add data/faculty_data.json
git commit -m "加入教職員資料檔案"
git push
```

### **問題 2：樣式跑版**

**原因**：CSS 檔案未上傳

**解決方案**：
```bash
# 檢查 CSS 是否被 .gitignore 排除
git check-ignore css/tailwind.css

# 如果被排除，編輯 .gitignore
vim .gitignore
# 註解掉或刪除 css/tailwind.css 這一行

# 重新加入
git add css/tailwind.css
git commit -m "加入 CSS 檔案"
git push
```

### **問題 3：部署後顯示 404**

**原因**：GitHub Pages 設定錯誤

**解決方案**：
- 檢查 GitHub Pages 設定
- Branch 應該是 `main`
- Folder 應該是 `/` (root)
- 確認 `index.html` 在根目錄

---

## 📊 檔案大小建議

### **優化建議**

- **圖片檔案**：建議壓縮到合理大小
  ```bash
  # 使用 scripts/optimize-images.py
  python3 scripts/optimize-images.py
  ```

- **CSV 檔案**：定期清理舊的備份
  ```bash
  # 保留最近 5 個備份即可
  ls -t data/backups/ | tail -n +6 | xargs -I {} rm data/backups/{}
  ```

### **大檔案處理**

如果遇到單個檔案超過 100MB：
- 使用 Git LFS（Large File Storage）
- 或將大檔案放到其他儲存服務（如 Google Drive）

---

## 🎯 快速參考

### **更新網站的完整流程**

**方式一：Decap CMS（推薦）**
1. 登入 `https://your-site.netlify.app/admin/`
2. 編輯新聞/活動/師資/Banner 等 → 儲存 → 發布
3. 自動提交至 GitHub → Netlify 建置並部署（約 1–2 分鐘）

**方式二：本地編輯後推送**
```bash
# 1. 編輯 Markdown（news/_posts、activities/_posts、faculty/_profiles）或 _data/*.json
# 2. 本地建置（可選，或交給 Netlify）
./stop.sh

# 3. Commit 並推送
git add .
git commit -m "更新內容"
git push

# 4. 等待 Netlify 部署（1–2 分鐘）
# 5. 檢查線上版本
# https://your-site.netlify.app 或 https://[帳號].github.io/[repo]
```

---

## 📞 需要協助？

- **GitHub Pages 官方文件**：https://docs.github.com/pages
- **Git 教學**：https://git-scm.com/book/zh-tw/v2
- **專案文件**：參閱 `CLAUDE.md` 和 `README.md`

---

**最後更新**：2025-12-11
**維護者**：台大新聞所團隊
