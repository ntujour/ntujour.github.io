# 台大新聞所網站 - 雙語架構與 CMS 快速指南

> **快速參考**：給網站管理員的實用操作指南  
> **完整文件**：請參閱 [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 📋 目錄

- [修改 Banner](#修改-banner)
- [管理新聞與活動](#管理新聞與活動)
- [編輯師資資料](#編輯師資資料)
- [語言切換設定](#語言切換設定)
- [部署到 Netlify](#部署到-netlify)

---

## 🎨 修改 Banner

### 方法 1：透過 Decap CMS（推薦）

1. 訪問 CMS：`https://your-site.netlify.app/admin/`
2. 登入（使用 Netlify Identity）
3. 點擊「網站設定」→「Banner 設定」
4. 編輯中文/英文標題和副標題
5. 點擊「Save」→「Publish」
6. 等待自動部署（約 1-2 分鐘）

### 方法 2：直接編輯檔案

```bash
# 編輯 Banner 資料檔案
vim _data/banner.json

# 範例內容
{
  "title_zh": "國立臺灣大學新聞研究所",
  "title_en": "Graduate Institute of Journalism, NTU",
  "subtitle_zh": "培育新時代新聞傳播人才",
  "subtitle_en": "Cultivating journalism professionals"
}

# 提交變更
git add _data/banner.json
git commit -m "Update banner content"
git push
```

### 驗證

開啟任何頁面，檢查 Banner 是否已更新。JavaScript 會自動根據語言載入對應內容。

---

## 📰 管理新聞與活動

### 透過 CMS 新增新聞

1. 登入 CMS（`/admin/`）
2. 點擊「最新消息」
3. 點擊「New 最新消息」
4. 填寫表單：
   - **標題（中文）**：必填
   - **標題（英文）**：選填
   - **發布日期**：選擇日期
   - **分類**：選擇類別
   - **內文（中文）**：使用 Markdown 格式
   - **內文（英文）**：選填
   - **封面圖片**：選填
   - **語言版本**：選擇「僅中文」、「僅英文」或「雙語」
5. 點擊「Publish」

### 編輯現有新聞

1. 在「最新消息」列表中找到文章
2. 點擊文章標題
3. 修改內容
4. 點擊「Save」→「Publish」

### 檔案位置

- 新聞 Markdown 檔案：`news/_posts/`
- 活動 Markdown 檔案：`activities/_posts/`

---

## 👥 編輯師資資料

### 透過 CMS 新增教師

1. 登入 CMS
2. 點擊「師資介紹」
3. 點擊「New 師資介紹」
4. 填寫表單：
   - **英文 ID**：小寫英文，用於 URL 和照片檔名（例如：`jerryhsieh`）
   - **姓名（中文/英文）**
   - **職稱（中文/英文）**
   - **類別**：選擇教師類型
   - **照片**：上傳教師照片（建議 400x400px）
   - **聯絡資訊**：電話、Email、辦公室
   - **專長**：中英文專長列表
   - **學經歷**：中英文對照
5. 點擊「Publish」

### 照片命名規則

- 自動命名：透過 CMS 上傳會自動處理
- 手動上傳：使用「英文 ID」命名，例如：`jerryhsieh.jpg`
- 位置：`images/faculty/` 或 `images/uploads/`

### 檔案位置

- 教師 Markdown 檔案：`faculty/_profiles/`
- 教師照片：`images/faculty/` 或 `images/uploads/`

---

## 🌍 語言切換設定

### 頁面對應關係

| 功能 | 中文路徑 | 英文路徑 |
|------|---------|---------|
| 首頁 | `/index.html` | `/en/index.html` |
| 關於我們 | `/about/intro.html` | `/en/about/intro.html` |
| 師資介紹 | `/faculty/faculty.html` | `/en/faculty/faculty.html` |
| 最新消息 | `/news.html` | `/en/news.html` |

### 在頁面中加入語言切換器

```html
<!-- 在導航列中加入 -->
<div class="language-switcher">
    <a href="#" data-lang-switch="zh" class="lang-link">中文</a>
    <a href="#" data-lang-switch="en" class="lang-link">English</a>
</div>

<!-- 確保載入 i18n.js -->
<script src="/js/i18n.js"></script>
```

### 自動偵測邏輯

`i18n.js` 會根據 URL 路徑自動偵測：
- `/en/` 開頭 → 英文
- 其他 → 中文

---

## 🚀 部署到 Netlify

### 初次設定

1. **建立 Netlify 帳號**
   - 訪問 https://netlify.com
   - 使用 GitHub 帳號登入

2. **連結 GitHub Repository**
   - New site from Git → GitHub
   - 選擇 `jirlong/ntujour-web`
   - 建置設定：
     - Build command: `python3 build-templates.py`
     - Publish directory: `.`

3. **啟用 Netlify Identity**
   - Site settings → Identity
   - 點擊「Enable Identity」
   - 設定：「Invite only」（僅邀請）

4. **啟用 Git Gateway**
   - Identity → Services → Git Gateway
   - 點擊「Enable Git Gateway」

5. **邀請管理員**
   - Identity → Invite users
   - 輸入管理員 Email
   - 管理員會收到邀請信

### 自動部署

每次推送到 `main` 分支，Netlify 會自動：
1. 拉取最新程式碼
2. 執行 `python3 build-templates.py`
3. 部署到 CDN
4. 約 1-2 分鐘完成

### 查看部署狀態

- Netlify Dashboard → Deploys
- 綠色勾 ✓ = 成功
- 紅色 X = 失敗（點擊查看錯誤日誌）

### 自訂域名（選填）

1. Domain settings → Add custom domain
2. 輸入域名（例如：`journalism.ntu.edu.tw`）
3. 設定 DNS：
   - 類型：CNAME
   - 名稱：journalism
   - 值：your-site.netlify.app

---

## 🔧 常見問題

### Q: Banner 沒有更新？

**A**: 檢查以下步驟：
1. 確認 `_data/banner.json` 已正確修改
2. 清除瀏覽器快取（Ctrl+Shift+R 或 Cmd+Shift+R）
3. 確認 JavaScript 沒有錯誤（開啟開發者工具 Console）

### Q: CMS 無法登入？

**A**: 
1. 確認已啟用 Netlify Identity
2. 確認已收到邀請信並完成註冊
3. 檢查 Email 是否正確

### Q: 語言切換沒反應？

**A**:
1. 確認已載入 `i18n.js`
2. 檢查連結是否設定 `data-lang-switch` 屬性
3. 確認英文版目錄 `/en/` 已建立

### Q: 新增的新聞沒有顯示？

**A**:
1. 確認已點擊「Publish」（不是只有「Save」）
2. 等待 Netlify 部署完成（約 1-2 分鐘）
3. 檢查檔案是否已推送到 GitHub

---

## 📚 相關文件

- [ARCHITECTURE.md](ARCHITECTURE.md) - 完整架構規劃
- [CLAUDE.md](CLAUDE.md) - AI 協作指南
- [README.md](README.md) - 專案說明
- [Decap CMS 官方文件](https://decapcms.org/docs/)
- [Netlify 文件](https://docs.netlify.com/)

---

## 💡 小技巧

### 使用 Editorial Workflow（草稿模式）

在 CMS 中：
1. 編輯內容後點擊「Save」（不是 Publish）
2. 內容會儲存為「Draft」（草稿）
3. 可以在「Workflow」中查看所有草稿
4. 確認無誤後再點擊「Publish」

### 批次上傳圖片

1. 直接將圖片放到 `images/uploads/`
2. Git 推送
3. 在 CMS 中編輯文章時可選擇已上傳的圖片

### 備份資料

定期備份重要資料：
```bash
# 備份所有資料檔案
cp -r _data/ _data_backup_$(date +%Y%m%d)/
cp -r data/ data_backup_$(date +%Y%m%d)/
```

---

**最後更新**：2026-01-31  
**維護者**：台大新聞所 + Claude AI
