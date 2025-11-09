# CMS 快速啟動指南

## 🚀 一鍵啟動

```bash
python3 cms.py
```

瀏覽器會自動開啟編輯器：`http://localhost:8080/admin/content-editor-v2.html`

## ✨ 功能特色

### 📝 內容編輯
- 富文本編輯器（Quill.js）
- 圖片上傳與管理
- 即時搜尋與篩選
- 按類型分類（新聞/活動）

### 🔄 變更追蹤
- 追蹤所有新增、更新、刪除
- 標題顯示未儲存變更數量
- 離開前警告提示
- 儲存時顯示詳細變更記錄

### 💾 資料管理
- **Save to DB**：儲存到 `data/content.csv`
- **Download Backup CSV**：下載本地備份
- 自動備份到 `data/backups/`

## 📊 變更記錄範例

點擊「Save to DB」時會顯示：

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

## 🔧 進階操作

### 從 HTML 抽取內容
```bash
python3 parse-content.py
```

### 去除重複資料
```bash
python3 deduplicate-content.py
```

### 停止伺服器
按 `Ctrl+C`

## 📁 相關檔案

- CMS 主程式：`cms.py`
- 編輯器：`admin/content-editor-v2.html`
- 資料檔：`data/content.csv`
- 備份目錄：`data/backups/`
- 完整文檔：`CLAUDE.md`

---

**最後更新**：2025-11-09
