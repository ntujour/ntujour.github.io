# Agent 操作記錄 (LOG)

本檔案記錄 AI Agent（Claude/Cursor）在本專案中執行的主要工作，便於追蹤與交接。

---

## 2026-02-01

### 1. 專案檢視與理解

**目標**：Review and understand the project.

**執行內容**：
- 閱讀 `ARCHITECTURE.md`、`README.md`、`CLAUDE.md`、`build-templates.py`
- 檢視目錄結構、`index.html`、`_data/banner.json`、`js/load-banner.js`、`templates/site-banner.html`、`admin/config.yml`、`netlify.toml`、`docs/IMPLEMENTATION_SUMMARY_2026.md`、`js/i18n.js`
- 產出專案檢視摘要：技術棧、模板系統、資料流、雙語架構、Decap CMS、部署流程
- **備註**：指出 `netlify.toml` 中 `[[redirects]] from = "/*" to = "/404.html" status = 404` 會使所有請求都導向 404，建議依需求調整或移除

**產出**：口頭/對話摘要，未新增檔案。

---

### 2. 更新 CLAUDE.md 以對齊 ARCHITECTURE.md

**目標**：Update CLAUDE.md to follow current structure in ARCHITECTURE.md.

**執行內容**：
- **目錄結構**：改為與 ARCHITECTURE 一致之樹狀結構，加入 `_data/`、`admin/`（index.html、config.yml）、`en/`、`news/_posts/`、`activities/_posts/`、`faculty/_profiles/`、`graduate/`、`netlify.toml` 等，移除已刪除之 content-editor-v2 引用
- **核心系統**：新增「2. _data/ 與 Banner 統一管理」；CMS 改為以 Decap CMS（admin/config.yml、_data/）為主，移除「本地 CSV 編輯」獨立小節；新增「部署流程」節；章節重新編號（輔助腳本 5、部署流程 6）
- **常見任務**：修改 Banner 區分「改文案」（_data/banner.json 或 CMS）與「改結構」（templates + 建置）；管理內容改為以 Decap CMS 為推薦方式；任務編號修正（任務 4～6）
- **檔案清單與快速參考**：納入 _data/、admin/config.yml、netlify.toml、load-banner.js、i18n.js；常用指令移除 cms.py
- **雙語架構與協作**：雙語目錄、常見任務速查、給 AI 的建議均對齊 ARCHITECTURE
- **歷史記錄**：新增 2026-01-31 條目（與 ARCHITECTURE 對齊）；2025-11-09 改為簡述「本地 cms.py 已移除，現行架構為 Decap CMS」；最後更新改為 2026-01-31

**修改檔案**：`CLAUDE.md`

---

### 3. 依架構移除無關程式碼

**目標**：根據所採取的架構（Decap CMS + _data/ + Netlify）移除無關程式碼。

**刪除檔案**：
- `cms.py`（本地 CMS 伺服器與 CSV 編輯器啟動腳本）
- `CMS_QUICK_START.md`
- `QUICK_START.md`
- `CONTENT_MANAGEMENT_GUIDE.md`
- `IMAGE_UPLOAD_GUIDE.md`

**修改檔案**：
- `CLAUDE.md`：目錄樹移除 cms.py；移除「5. 本地 CSV 編輯（可選）」；章節編號調整；歷史記錄簡化 cms.py 相關描述
- `ARCHITECTURE.md`：目錄樹移除 cms.py
- `README.md`：CMS 改為 Decap CMS 說明；專案結構改為 admin/index.html、config.yml、_data/
- `DEPLOYMENT_CHECKLIST.md`：移除「cms.py 在 .gitignore 中」
- `DEPLOYMENT_GUIDE.md`：admin 清單改為 index.html、config.yml、_data/；情境 2 改為 Decap CMS 流程；.gitignore 說明移除 cms.py
- `BUILD_VS_FRONTEND.md`：建置工具清單移除 cms.py；更新新聞與活動改為 Decap CMS；.gitignore 範例移除 cms.py
- `IMAGE_NAMING_CONVENTION.md`：「後端（cms.py）/ 前端（content-editor-v2）」改為「Decap CMS 與圖片上傳」
- `CONTENT_PARSING_SUMMARY.md`：編輯器 URL 改為根路徑或 Decap CMS 說明
- `.claude/settings.local.json`：移除 `open .../content-editor.html` 與 `open .../content-editor-v2.html` 之 Bash 權限

**產出**：無新增檔案，僅刪除與修改。

---

### 4. 教師原始頁面轉錄為 Admin 管理之 Markdown

**目標**：從教師原始頁面複製學歷、經歷、發表，手動轉為 admin 系統所管理之 .md，並協助開啟 admin 檢視。

**來源頁面**（擷取結果）：
- 實務教師：http://www.journalism.ntu.edu.tw/practical-professor.html（成功擷取）
- 合聘教師：http://www.journalism.ntu.edu.tw/jointly-appointed-professor.html（成功擷取）
- 感謝與追思：http://www.journalism.ntu.edu.tw/remembrance.html（成功擷取）
- 行政人員：http://www.journalism.ntu.edu.tw/staff.html（成功擷取）
- 專任、兼任、cp_n_105608：擷取逾時，未取得內容

**執行內容**：
- **實務教師**（14 位）：更新 `lichihte.md`、`liangyufang.md`、`lihsuehli.md`、`liyenfu.md`、`huangchaohui.md`、`yangkuangsheng.md`、`liulijen.md`、`chengkaichun.md`、`hsiaofuyuan.md`、`changchiehping.md`、`huangchepin.md`、`fangterlin.md`，補齊或新增 `bio`、學歷、經歷、得獎/著作；新增 `wuwanyu.md`（吳婉瑜）
- **合聘教師**：更新 `liuchingi.md`，補上個人網站 URL
- **感謝與追思**：新增 `niyenyuan.md`（倪炎元）、`chenjoumin.md`（陳柔縉），category 設為 honorary，職稱標註「感謝與追思」
- **行政人員**：未納入 faculty 集合（Decap CMS 目前無行政人員 collection）
- 啟動本機 HTTP 伺服器（port 8000）供開啟 admin 檢視

**修改/新增檔案**：`faculty/_profiles/` 下多個 .md（見上）；刪除過渡用 `wuwan yu.md`、`niyen yuan.md`，改為 `wuwanyu.md`、`niyenyuan.md`（檔名無空格）。

**產出**：口頭說明如何開啟 admin 與驗證轉錄；專任/兼任因來源逾時未轉錄，建議後續手動補齊。

---

### 5. Admin 登入「按了又跳回來」問題說明與解法

**目標**：說明為何在 admin 頁面按 Netlify 登入後會跳回，並提供解決方式。

**原因說明**：
- 在本機（如 localhost:8000/admin/）開啟 admin 時，點「使用你的 Netlify 帳號來進行登入」會導向 Netlify 登入；登入完成後 Netlify 會導回「已設定的網站網址」（例如 xxx.netlify.app），而非 localhost，導致導回失敗或回到登入頁。

**執行內容**：
- 新增 `docs/ADMIN_LOCAL_LOGIN.md`，內容包含：
  - 問題原因（localhost vs Netlify OAuth callback）
  - **方式一（本機編輯）**：執行 `npx decap-server`，再以 `python3 -m http.server 8000` 開靜態站，開啟 http://localhost:8000/admin/，使用本地後端，不需 Netlify 登入
  - **方式二（正式環境）**：改開 Netlify 上的 admin URL（如 https://站名.netlify.app/admin/）再使用 Netlify 登入
  - 自訂 decap-server port 與 config 設定說明

**新增檔案**：`docs/ADMIN_LOCAL_LOGIN.md`

---

## 維護說明

- 本 LOG 由 Agent 依對話內容撰寫，後續若有手動或 Agent 執行之重要變更，建議在此補上日期與簡述。
- 若需更細的變更紀錄，可搭配 Git commit 與 `IMPROVEMENTS.md` 使用。

---

**最後更新**：2026-02-01
