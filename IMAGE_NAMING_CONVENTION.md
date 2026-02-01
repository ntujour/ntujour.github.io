# 圖片命名規則說明

## 📋 新的命名邏輯

圖片現在使用 **文章 ID** 作為檔名，並根據文章類型儲存到對應目錄：

### 檔名格式

```
{type}-{articleId}-{imageIndex}.{ext}
```

**範例**：
- `news-259107-1.png` - 新聞 259107 的第 1 張圖片
- `news-259107-2.jpg` - 新聞 259107 的第 2 張圖片
- `activity-1731245678-1.png` - 活動 1731245678 的第 1 張圖片

### 儲存目錄

- **新聞圖片**：`images/news/`
- **活動圖片**：`images/activities/`

---

## 🔄 工作流程

### 新增文章時

1. 用戶填寫表單，選擇類型（新聞/活動）
2. 用戶點擊「上傳圖片」
3. 系統自動生成文章 ID（時間戳記，例如：1731245678）
4. 圖片上傳時使用此 ID 命名：
   - 第 1 張圖：`news-1731245678-1.jpg`
   - 第 2 張圖：`news-1731245678-2.png`
5. 圖片儲存到 `images/news/` 或 `images/activities/`
6. CSV 中只儲存路徑：`images/news/news-1731245678-1.jpg`

### 編輯文章時

1. 用戶點擊「編輯」
2. 系統讀取現有文章 ID（例如：259107）
3. 如果新增圖片，使用相同 ID：
   - 已有圖片：`news-259107-1.png`, `news-259107-2.jpg`
   - 新增圖片：`news-259107-3.png`（從現有數量繼續編號）

---

## 💾 CSV 儲存格式

### 單張圖片

```csv
id,type,title,image
259107,news,測試新聞,images/news/news-259107-1.png
```

### 多張圖片（使用 `|||` 分隔）

```csv
id,type,title,image
259107,news,測試新聞,"images/news/news-259107-1.png|||images/news/news-259107-2.jpg"
```

---

## 🎯 優點

1. **易於追蹤**：檔名直接對應文章 ID
2. **組織清楚**：新聞和活動分開儲存
3. **避免衝突**：文章 ID 確保唯一性
4. **便於管理**：可輕鬆找到某篇文章的所有圖片
5. **與現有邏輯一致**：沿用原有的命名規則

---

## 📁 目錄結構

```
ntujour-web/
└── images/
    ├── news/                      # 新聞圖片
    │   ├── news-259107-1.png
    │   ├── news-259107-2.jpg
    │   ├── news-258988-1.jpg
    │   └── ...
    └── activities/                # 活動圖片
        ├── activity-1731245678-1.png
        ├── activity-1731245678-2.jpg
        └── ...
```

---

## 🔍 範例

### 新增一篇新聞，附上 2 張圖片

**步驟**：
1. 選擇類型：新聞
2. 填寫標題、內容等
3. 上傳第 1 張圖片 → 生成 ID `1731245678`
   - 儲存為：`images/news/news-1731245678-1.jpg`
4. 上傳第 2 張圖片
   - 儲存為：`images/news/news-1731245678-2.png`
5. 提交表單

**CSV 結果**：
```csv
id,type,title,image
1731245678,news,測試新聞,"images/news/news-1731245678-1.jpg|||images/news/news-1731245678-2.png"
```

### 編輯現有新聞，新增第 3 張圖片

**步驟**：
1. 點擊編輯（文章 ID: 259107）
2. 系統讀取現有 2 張圖片：
   - `images/news/news-259107-1.png`
   - `images/news/news-259107-2.jpg`
3. 上傳新圖片
   - 儲存為：`images/news/news-259107-3.png`（從 3 開始）
4. 更新文章

**CSV 結果**：
```csv
id,type,title,image
259107,news,測試新聞,"images/news/news-259107-1.png|||images/news/news-259107-2.jpg|||images/news/news-259107-3.png"
```

---

## 🔧 技術實現

### Decap CMS 與圖片上傳

- **媒體目錄**：`images/uploads/`（於 `admin/config.yml` 設定 `media_folder`）。
- 透過 Decap CMS 上傳的圖片會儲存於此，路徑寫入對應內容欄位。
- 命名由 Decap CMS 或上傳流程決定；建議維持可讀檔名與適當副檔名。

---

## ✅ 完成！

新的圖片命名系統已實施，與原有的 `news-259107-1.png` 格式完全一致！
