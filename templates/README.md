# 模板系統使用說明

## 概述

這個模板系統讓您可以將網站的共用區塊（如 banner、導航列、sitemap、footer）集中管理，方便統一修改。

## 目錄結構

```
templates/
├── site-banner.html      # 網站 Banner
├── site-nav.html         # 導航列
├── site-sitemap.html     # 快速連結區塊
├── site-footer.html      # 頁尾
├── example-page.html     # 示範頁面
└── README.md            # 本說明文件
```

## 使用方法

### 1. 在 HTML 中使用模板標記

在您的 HTML 檔案中，使用以下標記來插入共用區塊：

```html
<!DOCTYPE html>
<html>
<head>
    <title>我的頁面</title>
    <!-- 樣式 -->
</head>
<body>
    {{site-banner}}      <!-- 插入 Banner -->

    {{site-nav}}         <!-- 插入導航列 -->

    <!-- 您的頁面內容 -->
    <section>
        <h1>頁面內容</h1>
    </section>

    {{site-sitemap}}     <!-- 插入快速連結 -->

    {{site-footer}}      <!-- 插入頁尾 -->
</body>
</html>
```

### 2. 執行建置腳本

修改完 HTML 或模板後，執行建置腳本：

```bash
python3 build-templates.py
```

腳本會自動：
- 讀取 templates/ 目錄中的所有模板
- 掃描所有 HTML 檔案中的模板標記
- 將標記替換為實際的 HTML 內容
- 自動處理路徑前綴（根目錄用 ``, 子目錄用 `../`）

### 3. 查看結果

建置完成後，所有模板標記都會被替換為實際內容，您可以在瀏覽器中查看效果。

## 可用的模板標記

| 標記 | 說明 | 檔案 |
|------|------|------|
| `{{site-banner}}` | 網站 Banner（標題、副標題） | templates/site-banner.html |
| `{{site-nav}}` | 導航列（主選單） | templates/site-nav.html |
| `{{site-sitemap}}` | 快速連結區塊 | templates/site-sitemap.html |
| `{{site-footer}}` | 頁尾（聯絡資訊、版權） | templates/site-footer.html |

## 路徑處理

模板系統會自動處理路徑：

- **根目錄的檔案**（如 index.html）：使用空路徑前綴
  ```html
  <a href="about/intro.html">關於我們</a>
  ```

- **子目錄的檔案**（如 faculty/faculty.html）：使用 `../` 前綴
  ```html
  <a href="../about/intro.html">關於我們</a>
  ```

您不需要手動處理路徑，腳本會自動計算！

## 修改共用區塊

### 修改 Banner

編輯 `templates/site-banner.html`：

```html
<header class="site-banner py-6">
    <div class="container-1200">
        <h1>您的網站標題</h1>
        <p>您的副標題</p>
    </div>
</header>
```

### 修改導航列

編輯 `templates/site-nav.html`：

```html
<nav class="site-nav">
    <ul>
        <li><a href="...">選單項目</a></li>
        <!-- 新增或修改選單項目 -->
    </ul>
</nav>
```

### 修改完成後

執行建置腳本，所有使用該模板的頁面都會自動更新：

```bash
python3 build-templates.py
```

## 工作流程

1. **首次設定**：
   ```bash
   # 將現有 HTML 中的共用區塊替換為模板標記
   # 例如：將 Banner HTML 改為 {{site-banner}}
   ```

2. **日常使用**：
   ```bash
   # 修改 templates/ 中的模板檔案
   vim templates/site-nav.html

   # 執行建置
   python3 build-templates.py

   # 所有頁面自動更新！
   ```

3. **新增頁面**：
   ```bash
   # 使用 example-page.html 作為範本
   cp templates/example-page.html my-new-page.html

   # 編輯內容
   vim my-new-page.html

   # 執行建置
   python3 build-templates.py
   ```

## 優點

✓ **統一管理**：修改一個檔案，更新所有頁面
✓ **自動路徑**：不用擔心相對路徑問題
✓ **簡單快速**：一行指令完成建置
✓ **易於維護**：模板和內容分離

## 注意事項

- 建置腳本會直接修改 HTML 檔案
- 建議在修改前先備份或使用版本控制（Git）
- 不要手動編輯建置後的 HTML 中的共用區塊，應該修改模板檔案

## 範例

查看 `templates/example-page.html` 了解完整使用範例。

## 疑難排解

**Q: 執行腳本後沒有變化？**
A: 檢查 HTML 中是否有正確的模板標記（如 `{{site-banner}}`）

**Q: 路徑不正確？**
A: 腳本會自動計算路徑，確保檔案在正確的目錄結構中

**Q: 想要不同的 Banner 樣式？**
A: 可以創建多個模板檔案（如 site-banner-alt.html）並使用不同的標記

---

*最後更新：2025-11-08*
