# 📝 新聞活動內容管理指南

## 🎯 系統概述

我們使用 **CSV 檔案** 作為輕量級資料庫，配合一個**純瀏覽器端的編輯器**，讓學生可以輕鬆管理新聞和活動內容。

## ✨ 優點

| 特點 | 說明 |
|------|------|
| **輕量級** | 不需要資料庫，只需要 CSV 檔案 |
| **簡單** | 像編輯 Excel 一樣簡單 |
| **安全** | 資料不上傳到任何伺服器 |
| **版本控制** | Git 自動追蹤所有修改 |
| **無需後端** | 完全在瀏覽器中運行 |
| **易於備份** | 只需複製 CSV 檔案 |

## 🚀 快速開始（3 步驟）

### 學生操作流程

```bash
# 1. 開啟編輯器
open admin/content-editor.html

# 2. 載入 CSV → 編輯 → 下載 CSV

# 3. 提交到 Git
git add data/content.csv
git commit -m "更新新聞內容"
git push
```

就這麼簡單！

## 📂 檔案結構

```
journalism-ntu.github.io/
├── admin/
│   ├── content-editor.html    # 內容編輯器
│   └── README.md              # 詳細使用說明
├── data/
│   └── content.csv            # 新聞活動資料
├── news.html                  # 新聞列表頁
├── activities.html            # 活動列表頁
└── js/
    └── homepage.js            # 載入 CSV 的程式
```

## 💡 三種使用方式

### 方式 1：直接開啟（最簡單）✨

```bash
# 用瀏覽器直接開啟
open admin/content-editor.html
```

**優點**：不需要任何設定
**缺點**：某些瀏覽器可能有安全限制

### 方式 2：VS Code + Live Server

1. 安裝 VS Code 擴充套件：**Live Server**
2. 右鍵 `admin/content-editor.html` → **Open with Live Server**
3. 瀏覽器自動開啟

**優點**：穩定，自動重新載入
**推薦**：✅ 最推薦學生使用

### 方式 3：Python 簡易伺服器

```bash
# 在專案根目錄執行
python3 -m http.server 8000

# 開啟瀏覽器
open http://localhost:8000/admin/content-editor.html
```

**優點**：跨平台，不需安裝額外軟體

## 📊 資料格式

### CSV 欄位說明

```csv
id,type,title,date,category,time,location,content,slug,originalFile,image
259107,news,【招生訊息】115學年度甄試招生簡章,2025-11-04,招生,,,<p>內容...</p>,news-259107,,
```

### 必填欄位

- ✅ `id`：自動生成（時間戳）
- ✅ `type`：news 或 activity
- ✅ `title`：標題
- ✅ `date`：日期
- ✅ `content`：HTML 內容
- ✅ `slug`：自動生成

### 選填欄位

- ❌ `category`：分類（招生、榮譽、徵才等）
- ❌ `time`：活動時間（例如：14:00-16:00）
- ❌ `location`：活動地點
- ❌ `image`：圖片路徑

## 🎨 內容範例

### 新聞範例

```html
<p>115學年度碩士班甄試招生簡章已公告。</p>
<p>報名時間：114年10月1日至10月15日<br>
口試日期：114年11月中旬<br>
放榜日期：114年11月下旬</p>
<p>詳細資訊請參閱教務處網頁。</p>
```

### 活動範例

```html
<p>本所邀請 ETtoday 總編林妏純女士演講。</p>
<p><strong>講座重點：</strong></p>
<ul>
  <li>網路新聞編輯室運作</li>
  <li>即時新聞產製流程</li>
  <li>媒體自律機制</li>
</ul>
<p>歡迎師生參加！</p>
```

## 🔄 完整工作流程

```mermaid
graph LR
    A[開啟編輯器] --> B[載入 CSV]
    B --> C[新增/編輯]
    C --> D[下載 CSV]
    D --> E[覆蓋原檔案]
    E --> F[Git 提交]
    F --> G[推送到 GitHub]
    G --> H[網站自動更新]
```

### 詳細步驟

1. **開啟編輯器**
   ```bash
   open admin/content-editor.html
   ```

2. **載入 CSV**
   - 點擊「📂 載入 CSV」
   - 選擇 `data/content.csv`

3. **編輯內容**
   - 新增：填寫表單 → 點擊「新增」
   - 編輯：點擊「編輯」→ 修改 → 點擊「更新」
   - 刪除：點擊「刪除」→ 確認

4. **下載 CSV**
   - 點擊「💾 下載 CSV」
   - 檔名：`content_2025-11-09.csv`

5. **覆蓋檔案**
   ```bash
   mv ~/Downloads/content_2025-11-09.csv data/content.csv
   ```

6. **提交到 Git**
   ```bash
   git add data/content.csv
   git commit -m "新增新聞：XXX"
   git push
   ```

7. **驗證**
   - 等待 30-60 秒
   - 刷新網站（Ctrl+F5）
   - 檢查新內容

## 🛡️ 安全考量

### 選項 1：不公開編輯器（推薦）

在 `.gitignore` 中加入：
```
admin/
```

學生只能在**本機**使用編輯器。

### 選項 2：公開但有說明

保留 `admin/` 在 Git 中，但在 `admin/README.md` 中說明這是內部工具。

### 選項 3：密碼保護

創建 `admin/.htaccess`：
```apache
AuthType Basic
AuthName "Restricted Access"
AuthUserFile /path/to/.htpasswd
Require valid-user
```

## 📦 備份策略

### 自動備份（Git）

```bash
# Git 自動保留所有歷史
git log --oneline data/content.csv

# 查看某個時間點的版本
git show HEAD~5:data/content.csv

# 恢復舊版本
git checkout HEAD~5 -- data/content.csv
```

### 手動備份

```bash
# 建立備份目錄
mkdir -p data/backups

# 定期備份
cp data/content.csv data/backups/content_$(date +%Y%m%d).csv

# 或使用 Git 標籤
git tag backup-$(date +%Y%m%d)
```

## 🐛 疑難排解

### 問題 1：CSV 中文亂碼

**原因**：編碼問題

**解決**：
1. 用 VS Code 開啟 CSV
2. 右下角點擊編碼
3. 選擇「以編碼重新開啟」→ UTF-8
4. 儲存

### 問題 2：無法載入 CSV

**原因**：瀏覽器安全限制

**解決**：使用 Live Server 或 Python 簡易伺服器

### 問題 3：內容沒顯示

**原因**：瀏覽器緩存

**解決**：
- Chrome/Edge: Ctrl+Shift+R
- Firefox: Ctrl+F5
- Safari: Cmd+Option+R

### 問題 4：CSV 格式錯誤

**原因**：逗號或引號問題

**解決**：
1. 用編輯器檢查 CSV
2. 確保 HTML 內容用引號包起來
3. 檢查沒有多餘的逗號

## 📈 進階功能

### 批次匯入

如果有大量資料要匯入：

1. 用 Excel 編輯 CSV
2. 確保格式正確
3. 另存為「CSV UTF-8」
4. 載入到編輯器檢查
5. 下載並覆蓋

### 圖片管理

```bash
# 上傳圖片到適當目錄
cp photo.jpg images/news/

# 在編輯器中填入路徑
images/news/photo.jpg
```

### 自動化腳本

可以寫簡單的 Python 腳本來批次處理：

```python
import csv
from datetime import datetime

# 讀取 CSV
with open('data/content.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# 新增一筆資料
new_item = {
    'id': str(int(datetime.now().timestamp())),
    'type': 'news',
    'title': '測試新聞',
    'date': '2025-11-09',
    'content': '<p>這是測試內容</p>',
    # ... 其他欄位
}
data.insert(0, new_item)

# 寫回 CSV
with open('data/content.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
```

## 🎓 學生訓練建議

### 第一次使用（30 分鐘）

1. 老師示範操作（10 分鐘）
2. 學生實際操作（15 分鐘）
3. Q&A（5 分鐘）

### 練習任務

1. 新增一則測試新聞
2. 編輯該新聞
3. 刪除該新聞
4. 下載 CSV 並檢查
5. 提交到 Git

### 常見錯誤

- ❌ 忘記下載 CSV
- ❌ 忘記提交到 Git
- ❌ HTML 標籤沒有關閉
- ❌ 檔案覆蓋錯位置

## 📚 延伸閱讀

- 📖 詳細使用說明：`admin/README.md`
- 🏗️ 網站架構：`README.md`
- 📊 資料來源：`DATA_SOURCES.md`
- 🤖 AI 助手指南：`CLAUDE.md`

## 🔮 未來可能的改進

如果需要更進階的功能：

1. **Markdown 編輯器**
   - 使用 SimpleMDE 或 EasyMDE
   - 更直觀的編輯體驗

2. **圖片上傳**
   - 整合 Imgur API
   - 或使用 GitHub Issues 的圖床功能

3. **自動發布**
   - GitHub Actions 自動部署
   - 發布前預覽

4. **通知系統**
   - 發布後自動發送 Email
   - Slack/Discord 通知

5. **Headless CMS**
   - 考慮使用 Netlify CMS
   - 或 Forestry.io

但目前的 CSV 方案已經足夠輕量且穩定！

---

**維護者**：台大新聞所
**建立日期**：2025-11-09
**適用對象**：助教、學生、編輯人員
