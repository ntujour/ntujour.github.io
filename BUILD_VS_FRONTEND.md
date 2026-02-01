# 建置工具 vs 前端程式碼 - 架構說明

> 本文檔說明哪些是「建置工具」（本地使用，不上傳），哪些是「前端程式碼」（部署到 GitHub Pages）

---

## 🎯 核心概念

這是一個**靜態網站**，部署在 GitHub Pages 上：
- ❌ **不需要** Python 伺服器運行
- ✅ **需要** 建置工具來生成靜態內容
- ✅ 部分內容可以前端動態載入（經常更新的資料）

---

## 📦 檔案分類

### 🔨 建置工具（本地使用，不上傳到 GitHub Pages）

```
build-templates.py              # 模板建置工具
scripts/                        # 所有建置腳本
  ├── build/
  │   ├── convert-to-templates.py
  │   └── generate-static-faculty.py  # 新增：生成靜態教職員頁面
  ├── data/
  │   ├── parse-content.py
  │   ├── deduplicate-content.py
  │   └── ...
  └── maintenance/
      └── ...

templates/                      # HTML 模板（用於建置）
data/
  ├── faculty_data.json         # 資料來源（建置時讀取）
  ├── faculty-mapping.csv
  └── content.csv
```

**這些檔案的作用**：
- 在**本地開發**時使用
- 用來**生成靜態內容**
- **不會部署**到線上

---

### 🌐 前端程式碼（部署到 GitHub Pages）

```
index.html                      # 網站頁面
faculty/
  ├── faculty.html              # 靜態生成的教職員頁面
  ├── fulltime-professor.html
  └── ...
news.html
activities.html
...

css/                            # 樣式表
  └── tailwind.css

js/                             # 前端 JavaScript
  ├── combined-news.js          # 動態載入新聞（保留）
  ├── activities.js             # 動態載入活動（保留）
  └── ❌ faculty.js             # 可以移除（改用靜態生成）

images/                         # 圖片資源
```

**這些檔案的作用**：
- 部署到 **GitHub Pages**
- 用戶訪問時直接載入
- 純靜態 HTML + CSS + JavaScript

---

## 🔄 兩種載入方式對比

### 方式 1️⃣：前端動態載入（目前的做法）

```javascript
// js/faculty.js
fetch('../data/faculty_data.json')
    .then(response => response.json())
    .then(data => {
        // 動態生成 HTML
        renderFacultyCards(data);
    });
```

**優點**：
- 資料更新時只需修改 JSON
- 不需重新 generate HTML

**缺點**：
- ❌ 本地開發必須用 HTTP 伺服器
- ❌ 首次載入較慢（額外的網路請求）
- ❌ SEO 不友善
- ❌ JavaScript 失效時無法顯示內容

---

### 方式 2️⃣：建置時靜態生成（推薦做法）

```python
# scripts/build/generate-static-faculty.py
with open('data/faculty_data.json') as f:
    data = json.load(f)

html = generate_html_from_data(data)

with open('faculty/faculty.html', 'w') as f:
    f.write(html)
```

**優點**：
- ✅ 完全靜態，可以直接用 `file://` 開啟
- ✅ 載入速度更快
- ✅ SEO 友善
- ✅ 不依賴 JavaScript

**缺點**：
- 資料更新時需要重新執行 generate 腳本

---

## 📋 建議的工作流程

### **更新教職員資料時**：

```bash
# 1. 編輯資料
vim data/faculty_data.json

# 2. 執行建置腳本（生成靜態 HTML）
python3 scripts/build/generate-static-faculty.py

# 3. 建置模板
python3 build-templates.py

# 4. 提交到 Git
git add faculty/faculty.html
git commit -m "更新教職員資料"
git push
```

### **更新新聞與活動時**：

- 使用 **Decap CMS**：登入 `/admin/`（Netlify Identity）→ 編輯新聞/活動集合 → 發布（自動提交至 GitHub）。
- 或直接編輯 `data/content.csv` 後 `git add` / `git commit` / `git push`。

---

## 🎯 混合架構建議

| 內容類型 | 更新頻率 | 建議方式 | 原因 |
|---------|---------|---------|------|
| 教職員列表 | 每學期 1-2 次 | 建置時生成 | 不常變動，SEO 重要 |
| 教職員個人頁面 | 不定期 | 建置時生成 | 同上 |
| 首頁內容 | 每月 1-2 次 | 建置時生成 | 首頁載入速度很重要 |
| 最新消息 | 每週數次 | 前端動態載入 | 更新頻繁，內容較多 |
| 活動資訊 | 每週數次 | 前端動態載入 | 同上 |

---

## 📝 .gitignore 建議

建立 `.gitignore` 來排除不需要上傳的檔案：

```gitignore
# 建置工具（若僅本地使用；Netlify 建置時通常需保留 build-templates.py、templates/）
# build-templates.py
scripts/

# 資料來源（建置時讀取）
data/faculty_data.json
data/faculty-mapping.csv
data/content.csv
data/backups/

# 模板（用於建置）
templates/

# 開發工具
node_modules/
*.pyc
__pycache__/
.DS_Store
```

**但是**，如果你希望其他開發者也能執行建置，可以保留這些檔案。

---

## 🚀 下一步

1. **測試 generate-static-faculty.py**：
   ```bash
   python3 scripts/build/generate-static-faculty.py
   ```

2. **比較效能**：
   - 開啟生成的靜態頁面
   - 開啟原本的動態載入頁面
   - 比較載入速度和 SEO

3. **逐步遷移**：
   - 先遷移教職員頁面
   - 再考慮其他不常更新的頁面
   - 保持新聞/活動的動態載入

---

**最後更新**：2025-12-11
**維護者**：台大新聞所團隊
