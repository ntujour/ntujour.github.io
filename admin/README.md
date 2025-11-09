# 新聞活動內容管理系統

## 📖 系統說明

這是一個輕量級的內容管理系統，讓學生可以輕鬆新增、編輯、刪除新聞與活動內容。

### 特點
- ✅ **無需後端**：完全在瀏覽器中運行
- ✅ **操作簡單**：像 Excel 一樣編輯資料
- ✅ **安全**：資料不會上傳到任何伺服器
- ✅ **版本控制**：透過 Git 追蹤所有變更
- ✅ **輕量級**：只需要瀏覽器和文字編輯器

## 🚀 使用方式

### 方式一：直接開啟 HTML（最簡單）

1. 用瀏覽器開啟 `admin/content-editor.html`
2. 點擊「📂 載入 CSV」，選擇 `data/content.csv`
3. 新增或編輯內容
4. 點擊「💾 下載 CSV」
5. 將下載的檔案覆蓋原本的 `data/content.csv`
6. 提交到 Git

```bash
# Git 操作
git add data/content.csv
git commit -m "更新新聞/活動內容"
git push
```

### 方式二：使用 VS Code + Live Server

1. 在 VS Code 中安裝 "Live Server" 擴充套件
2. 右鍵點擊 `admin/content-editor.html` → "Open with Live Server"
3. 瀏覽器會自動開啟編輯器
4. 後續步驟同方式一

### 方式三：使用 Python 簡易伺服器

```bash
# 在專案根目錄執行
python3 -m http.server 8000

# 或使用 Node.js
npx http-server -p 8000
```

然後在瀏覽器開啟：`http://localhost:8000/admin/content-editor.html`

## 📝 操作指南

### 新增內容

1. 填寫表單：
   - **類型**：選擇「新聞」或「活動」
   - **標題**：例如 `【招生訊息】115學年度甄試招生簡章`
   - **日期**：選擇日期
   - **分類**：選擇適當分類（招生、榮譽、徵才等）
   - **內容**：使用 HTML 格式

2. 點擊「新增」按鈕

### 編輯內容

1. 在列表中找到要編輯的項目
2. 點擊「編輯」按鈕
3. 修改內容
4. 點擊「更新」按鈕

### 刪除內容

1. 在列表中找到要刪除的項目
2. 點擊「刪除」按鈕
3. 確認刪除

### 搜尋和篩選

- 使用搜尋框搜尋標題或內容
- 使用類型下拉選單篩選新聞或活動

## 📄 CSV 格式說明

CSV 檔案包含以下欄位：

| 欄位 | 說明 | 必填 | 範例 |
|------|------|------|------|
| `id` | 唯一識別碼 | ✅ | `259107` |
| `type` | 類型 | ✅ | `news` 或 `activity` |
| `title` | 標題 | ✅ | `【招生訊息】115學年度甄試招生簡章` |
| `date` | 日期 | ✅ | `2025-11-04` |
| `category` | 分類 | ❌ | `招生`, `榮譽`, `徵才` |
| `time` | 時間（活動用） | ❌ | `14:00-16:00` |
| `location` | 地點（活動用） | ❌ | `社科院大樓101教室` |
| `content` | 內容（HTML） | ✅ | `<p>內容...</p>` |
| `slug` | 網址代稱 | ✅ | `news-259107` |
| `originalFile` | 原始檔案名稱 | ❌ | `News_Content_n_35497_s_259107.html` |
| `image` | 圖片路徑 | ❌ | `images/news/photo.jpg` |

## 🎨 HTML 內容格式

支援的 HTML 標籤：

```html
<!-- 段落 -->
<p>這是一段文字。</p>

<!-- 粗體 -->
<p><strong>重要內容</strong></p>

<!-- 列表 -->
<ul>
  <li>項目一</li>
  <li>項目二</li>
</ul>

<!-- 換行 -->
<p>第一行<br>第二行</p>

<!-- 連結 -->
<p><a href="https://example.com">連結文字</a></p>
```

### 範例：新聞內容

```html
<p>115學年度碩士班甄試招生簡章已公告，歡迎對新聞傳播有熱忱的同學報考。</p>
<p>報名時間：114年10月1日至10月15日<br>
口試日期：114年11月中旬<br>
放榜日期：114年11月下旬</p>
<p>詳細資訊請參閱台大教務處招生網頁。</p>
```

### 範例：活動內容

```html
<p>本所邀請ETtoday新聞雲總編輯林妏純女士蒞臨演講，分享網路新聞產製經驗與媒體自律實踐。</p>
<p><strong>講座重點：</strong></p>
<ul>
  <li>網路新聞編輯室運作</li>
  <li>即時新聞的產製流程</li>
  <li>媒體自律機制</li>
  <li>數位時代的新聞倫理</li>
</ul>
<p>歡迎有興趣的師生參加！</p>
```

## 🔧 進階功能

### 批次操作

如果需要批次修改大量資料，建議：

1. 下載 CSV 檔案
2. 用 Excel 或 Google Sheets 開啟
3. 批次編輯
4. 另存為 CSV（UTF-8 編碼）
5. 上傳回系統

### 備份

建議定期備份 `data/content.csv`：

```bash
# 建立備份
cp data/content.csv data/backups/content_$(date +%Y%m%d).csv

# 或使用 Git 標籤
git tag -a backup-$(date +%Y%m%d) -m "Content backup"
git push --tags
```

### 圖片管理

如需上傳圖片：

1. 將圖片放到 `images/news/` 或 `images/activities/`
2. 在表單中填入相對路徑：`images/news/photo.jpg`
3. 圖片建議尺寸：1200x630px（適合社群分享）

## 🛡️ 安全建議

1. **不要公開 admin 目錄**
   - 在 `.gitignore` 中排除，或
   - 使用密碼保護，或
   - 只在本機使用

2. **定期備份資料**
   - Git 自動保留歷史紀錄
   - 額外建立備份檔案

3. **檢查 CSV 格式**
   - 確保沒有多餘的逗號
   - 檢查 HTML 標籤是否正確關閉

## 🐛 常見問題

### Q: CSV 下載後中文亂碼？

A: 確保使用 UTF-8 編碼。在 Excel 中開啟 CSV：
1. 資料 → 從文字/CSV 匯入
2. 選擇「UTF-8」編碼
3. 分隔符號選擇「逗號」

### Q: 如何刪除舊的內容？

A:
1. 在列表中找到項目
2. 點擊「刪除」按鈕
3. 下載並覆蓋 CSV

### Q: 可以一次新增多筆資料嗎？

A: 可以！
1. 用 Excel 開啟 `data/content.csv`
2. 複製最後一行作為範本
3. 修改內容（記得改 ID 和 slug）
4. 儲存為 CSV
5. 重新載入到編輯器中檢查

### Q: 內容沒有顯示在網站上？

A: 檢查：
1. CSV 是否正確覆蓋到 `data/content.csv`
2. 是否已提交並推送到 GitHub
3. 清除瀏覽器緩存（Ctrl+F5）

## 📚 相關文件

- 網站架構說明：`README.md`
- 資料來源文件：`DATA_SOURCES.md`
- Claude 助手指南：`CLAUDE.md`

## 💡 未來改進建議

如果需要更進階的功能，可以考慮：

1. **Markdown 編輯器**：使用 Markdown 取代 HTML
2. **所見即所得編輯器**：整合 TinyMCE 或 CKEditor
3. **圖片上傳**：整合 Imgur API 或使用 GitHub Issues
4. **自動發布**：使用 GitHub Actions 自動部署

---

**維護者**：台大新聞所
**最後更新**：2025-11-09
