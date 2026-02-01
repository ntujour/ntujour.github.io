# ✅ GitHub Pages 部署檢查清單

> 在推送到 GitHub 之前，請確認以下項目

---

## 📋 部署前檢查

### ✅ **必要檔案確認**

```bash
# 執行以下命令檢查關鍵檔案（Netlify 建置會產生 data/*.json）
ls -lh css/tailwind.css data/faculty_data.json data/news.json data/activities.json
```

- [ ] `css/tailwind.css` 存在且不為空
- [ ] `data/faculty_data.json` 存在且格式正確
- [ ] `data/activities.json` 存在
- [ ] `data/news.json` 存在
- [ ] `index.html` 在根目錄
- [ ] `build-templates.py`、`scripts/`、`templates/` 已提交（Netlify 建置需要）
- [ ] `images/faculty/` 資料夾有教師照片

---

### ✅ **.gitignore 設定確認**

```bash
# 檢查這些檔案不會被忽略（應該要上傳）
git check-ignore -v data/faculty_data.json data/news.json css/tailwind.css build-templates.py
# 如果沒有輸出，表示這些檔案會被上傳（正確）
```

**應該上傳**（Decap + Netlify 建置需要）：
- [ ] `data/faculty_data.json`、`data/news.json`、`data/activities.json` 不在 .gitignore 中
- [ ] `css/tailwind.css` 不在 .gitignore 中
- [ ] `build-templates.py`、`scripts/`、`templates/` 不在 .gitignore 中（Netlify 建置會執行）

**不應上傳**：
- [ ] `archive/` 在 .gitignore 中
- [ ] `data/backups/` 在 .gitignore 中

---

### ✅ **本地測試**

```bash
# 啟動本地伺服器
python3 -m http.server 8000

# 在瀏覽器開啟：http://localhost:8000
```

**測試項目**：
- [ ] 首頁正常顯示
- [ ] 教職員頁面正常載入資料
- [ ] 新聞頁面正常載入
- [ ] 活動頁面正常載入
- [ ] 所有圖片正常顯示
- [ ] 導航連結都有效
- [ ] 手機版排版正常

---

### ✅ **資料完整性檢查**

#### 教職員資料

```bash
# 檢查 JSON 格式
python3 -m json.tool data/faculty_data.json > /dev/null
echo $?  # 應該輸出 0（表示格式正確）
```

- [ ] `faculty_data.json` JSON 格式正確
- [ ] 所有教師都有照片（檢查 `images/faculty/`）
- [ ] 照片檔名與 JSON 中的 ID 一致

#### 新聞與活動資料

- [ ] `news/_posts/`、`activities/_posts/` 內有 Markdown 文章（或由 Decap CMS 發布）
- [ ] 建置後 `data/news.json`、`data/activities.json` 存在且格式正確
- [ ] 相關圖片存在於 `images/uploads/` 或指定路徑

---

### ✅ **Git 準備**

```bash
# 檢查 Git 狀態
git status

# 檢查要提交的檔案
git add .
git status
```

**確認**：
- [ ] Git repository 已初始化（`git init`）
- [ ] 已設定 remote（`git remote -v` 應該有輸出）
- [ ] 分支名稱是 `main`（`git branch` 查看）

---

## 🚀 部署步驟

### 1️⃣ **首次部署**

```bash
# 1. 加入所有檔案
git add .

# 2. Commit
git commit -m "Initial commit: 台大新聞所網站"

# 3. 推送到 GitHub
git push -u origin main
```

### 2️⃣ **設定 GitHub Pages**

到 GitHub Repository 設定：
- [ ] Settings → Pages
- [ ] Source: Deploy from a branch
- [ ] Branch: `main`
- [ ] Folder: `/` (root)
- [ ] 點擊 Save

### 3️⃣ **等待部署完成**

- [ ] 等待 1-2 分鐘
- [ ] 訪問：`https://[你的帳號].github.io/[repo名稱]`
- [ ] 確認網站正常運作

---

## 🔄 日常更新檢查

### **更新內容時**

- **新聞/活動/師資**：使用 Decap CMS（`/admin/`）編輯 → 發布即提交至 GitHub；或編輯 `news/_posts/`、`activities/_posts/`、`faculty/_profiles/` 的 Markdown 後執行 `./stop.sh`（或 Netlify 建置）產生 `data/*.json`，再 commit 並 push。
- **Banner/導航/網站設定**：Decap CMS「網站設定」或直接編輯 `_data/*.json` → commit 並 push。

**檢查清單**：
- [ ] 本地測試過新內容（可執行 `./start.sh` 預覽）
- [ ] Commit 訊息清楚描述變更
- [ ] 只加入需要的檔案（不要 `git add .` 全部加入）

---

## ⚠️ 常見問題檢查

### **問題：教職員資料不顯示**

```bash
# 檢查檔案是否上傳
git ls-files | grep faculty_data.json

# 如果沒有，手動加入
git add data/faculty_data.json
git commit -m "加入教職員資料"
git push
```

### **問題：樣式跑版**

```bash
# 檢查 CSS 是否上傳
git ls-files | grep tailwind.css

# 檢查 .gitignore
git check-ignore css/tailwind.css
# 如果有輸出，表示被忽略了（錯誤）
```

### **問題：圖片不顯示**

```bash
# 檢查圖片是否上傳
git ls-files | grep "images/faculty/"

# 檢查圖片大小（GitHub 單檔限制 100MB）
find images -type f -size +10M
```

---

## 📊 檔案大小檢查

```bash
# 檢查大檔案（超過 10MB）
find . -type f -size +10M | grep -v node_modules | grep -v .git

# 檢查 data 資料夾總大小
du -sh data/

# 檢查 images 資料夾總大小
du -sh images/
```

**建議**：
- 單個檔案 < 10MB
- images/ 總大小 < 500MB
- data/ 總大小 < 50MB

---

## ✅ 最終檢查

部署後，請到線上網站檢查：

- [ ] 所有頁面都能正常訪問
- [ ] 教職員資料正確顯示
- [ ] 新聞與活動正確載入
- [ ] 所有圖片正確顯示
- [ ] 手機版排版正常
- [ ] 沒有 404 錯誤
- [ ] 沒有 console 錯誤（按 F12 查看）

---

## 📞 需要協助？

參閱 `DEPLOYMENT_GUIDE.md` 獲取詳細說明。

---

**最後更新**：2025-12-11
