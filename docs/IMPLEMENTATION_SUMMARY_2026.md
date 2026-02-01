# 雙語架構與 Decap CMS 整合 - 實施摘要

> **完成時間**：2026-01-31  
> **狀態**：✅ 基礎架構已完成

---

## 📦 已建立的檔案

### 1. 架構規劃文件

| 檔案 | 說明 |
|------|------|
| **ARCHITECTURE.md** | 完整的網站架構規劃，包含雙語設計、Decap CMS 整合、目錄結構和實施階段 |
| **docs/QUICK_REFERENCE.md** | 快速參考指南，提供管理員實用操作步驟 |

### 2. 資料檔案（JSON）

| 檔案 | 說明 |
|------|------|
| **_data/banner.json** | Banner 雙語內容（可透過 CMS 編輯） |
| **_data/navigation.json** | 導航選單結構（雙語，支援子選單） |
| **_data/site_settings.json** | 網站全域設定（聯絡資訊、社群媒體連結等） |
| **_data/backups/** | 資料備份目錄 |

### 3. JavaScript 腳本

| 檔案 | 說明 |
|------|------|
| **js/load-banner.js** | 動態載入 Banner，根據語言自動切換內容 |
| **js/i18n.js** | 多語言支援，提供語言偵測、切換和 SEO 優化 |

### 4. 配置檔案

| 檔案 | 說明 |
|------|------|
| **admin/config.yml** | Decap CMS 完整配置，支援 Banner、導航、新聞、活動、教師管理 |
| **netlify.toml** | Netlify 部署配置，包含建置設定、重定向和安全 Headers |

### 5. 目錄結構

| 目錄 | 說明 |
|------|------|
| **_data/** | 統一管理所有可編輯的資料檔案 |
| **news/_posts/** | 新聞 Markdown 檔案（CMS 管理） |
| **activities/_posts/** | 活動 Markdown 檔案（CMS 管理） |
| **faculty/_profiles/** | 教師資料 Markdown 檔案（CMS 管理） |

### 6. 更新的檔案

| 檔案 | 變更內容 |
|------|---------|
| **templates/site-banner.html** | 加入動態載入腳本，支援 CMS 管理 |
| **CLAUDE.md** | 新增雙語架構和 Decap CMS 整合章節 |

---

## ✨ 核心功能

### 1. Banner 統一管理 ✅

**問題**：如何統一調整 Banner 內容？

**解決方案**：
- 所有 Banner 內容儲存在 `_data/banner.json`
- 透過 `load-banner.js` 動態載入
- 可透過 Decap CMS 視覺化編輯
- 一次修改，全站更新

**使用方式**：
```bash
# 方法 1：透過 CMS
訪問 /admin/ → 網站設定 → Banner 設定 → 編輯 → 發布

# 方法 2：直接編輯
vim _data/banner.json
git add _data/banner.json
git commit -m "Update banner"
git push
```

### 2. 雙語架構 ✅

**設計**：
- 中文版本：根目錄 `/`
- 英文版本：獨立目錄 `/en/`
- 語言自動偵測
- URL 對應清晰

**語言切換**：
```html
<a href="#" data-lang-switch="zh">中文</a>
<a href="#" data-lang-switch="en">English</a>
```

`i18n.js` 自動處理切換邏輯和 SEO 標籤。

### 3. Decap CMS 整合 ✅

**功能**：
- 視覺化編輯器
- Git-based（所有變更儲存在 GitHub）
- 支援 Markdown
- 圖片上傳管理
- Editorial Workflow（草稿模式）

**可管理內容**：
1. 網站全域設定（Banner、導航、聯絡資訊）
2. 最新消息（雙語）
3. 系所活動（雙語）
4. 師資介紹（雙語）

---

## 🚀 下一步建議

### 階段一：測試基礎功能（本週）

- [ ] 測試 Banner 動態載入
- [ ] 測試語言切換功能
- [ ] 本地測試 Decap CMS（使用 `local_backend`）

### 階段二：Netlify 部署（下週）

- [ ] 建立 Netlify 專案
- [ ] 啟用 Netlify Identity
- [ ] 啟用 Git Gateway
- [ ] 邀請管理員測試 CMS

### 階段三：內容遷移（第 3-4 週）

- [ ] 遷移現有教師資料到 Markdown 格式
- [ ] 遷移新聞資料（從 `data/content.csv`）
- [ ] 遷移活動資料

### 階段四：英文版本建置（第 5-6 週）

- [ ] 建立 `/en/` 目錄結構
- [ ] 翻譯核心頁面
- [ ] 測試雙語切換

---

## 📋 檢查清單

### 測試 Banner 動態載入

```bash
# 1. 啟動本地伺服器
python3 -m http.server 8000

# 2. 開啟瀏覽器
# 訪問 http://localhost:8000

# 3. 檢查 Banner 是否正確顯示
# 4. 開啟開發者工具，檢查 Console 是否有錯誤
# 5. 修改 _data/banner.json，重新整理頁面確認更新
```

### 測試語言切換

```bash
# 1. 在導航列加入語言切換器
# 2. 點擊「English」應跳轉到 /en/ 版本
# 3. 點擊「中文」應跳轉回根目錄版本
```

### 本地測試 Decap CMS

```bash
# 1. 啟用本地後端
# 在 admin/config.yml 取消註解：
# local_backend: true

# 2. 安裝 Netlify CLI
npm install -g netlify-cli

# 3. 啟動 CMS 代理
npx netlify-cms-proxy-server

# 4. 啟動網站（另一個終端）
python3 -m http.server 8000

# 5. 訪問 http://localhost:8000/admin/
```

---

## 🔗 相關文件連結

| 文件 | 說明 |
|------|------|
| [ARCHITECTURE.md](../ARCHITECTURE.md) | 完整架構規劃 |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | 快速參考指南 |
| [CLAUDE.md](../CLAUDE.md) | AI 協作指南 |
| [admin/config.yml](../admin/config.yml) | Decap CMS 配置 |
| [netlify.toml](../netlify.toml) | Netlify 部署配置 |

---

## 💡 重要提醒

### Banner 系統

- ✅ **動態載入**：每次頁面載入時從 `_data/banner.json` 讀取
- ✅ **雙語支援**：根據 URL 自動選擇語言
- ✅ **降級機制**：如果載入失敗，使用預設內容
- ⚠️ **快取問題**：修改後需清除瀏覽器快取（Ctrl+Shift+R）

### Decap CMS

- ✅ **Git-based**：所有變更都會提交到 GitHub
- ✅ **Editorial Workflow**：可以先存草稿再發布
- ⚠️ **Netlify Identity**：必須先在 Netlify 設定 Identity 才能登入
- ⚠️ **備份**：建議定期備份 `_data/` 目錄

### 雙語架構

- ✅ **SEO 友善**：自動生成 hreflang 標籤
- ✅ **URL 清晰**：`/en/` 明確表示英文版本
- ⚠️ **內容同步**：需手動確保中英文內容對應

---

## 📞 支援

如有問題，請參考：
- [Decap CMS 官方文件](https://decapcms.org/docs/)
- [Netlify 文件](https://docs.netlify.com/)
- [GitHub Issues](https://github.com/jirlong/ntujour.github.io/issues)

---

**建立日期**：2026-01-31  
**維護者**：Claude AI + 台大新聞所團隊  
**版本**：1.0
