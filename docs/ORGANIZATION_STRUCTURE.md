# 網站檔案組織結構

## 📁 資料夾結構

```
journalism-ntu.github.io/
├── faculty/          (11個文件) - 師資陣容
├── news/            (22個文件) - 最新消息
├── activities/      (97個文件) - 活動資訊
├── photos/          (25個文件) - 照片內容
├── about/           (4個文件) - 關於本所
├── admissions/      (7個文件) - 招生專區
├── courses/         (4個文件) - 課程規劃
├── publications/    (4個文件) - 出版發表
├── css/             - 樣式文件
├── js/              - JavaScript文件
├── images/          - 圖片資源
├── Scripts/         - 舊有JavaScript庫
├── data/            - JSON數據文件
└── (根目錄)         - 主要頁面和其他文件
```

## 📂 詳細內容

### 1. faculty/ (師資陣容) - 11個文件
```
faculty/
├── faculty.html                      # 師資總覽頁面
├── fulltime-professor.html           # 專任教師列表
├── parttime-professor.html           # 兼任教師列表
├── practical-professor.html          # 實務教師列表
├── Professorjointappointment.html    # 合聘教師列表
├── hsiehjl.html                      # 謝吉隆 副教授兼所長
├── linly.html                        # 林麗雲 教授
├── hungcl.html                       # 洪貞玲 教授
├── lincc.html                        # 林照真 教授
├── RauchfleischA.html                # Adrian Rauchfleisch 教授
├── tsaihj.html                       # 蔡蕙如 副教授
└── chanii.html                       # 詹怡宜 副教授
```

### 2. news/ (最新消息) - 22個文件
```
news/
├── News_n_35497_sms_26652.html           # 最新消息列表頁
├── News_Content_n_35497_s_259107.html    # 115學年度甄試招生簡章
├── News_Content_n_35497_s_258976.html    # 學生獲獎消息
├── News_Content_n_35497_s_258800.html    # 學術研討會
├── News_Content_n_35497_s_257861.html    # 入圍獎項
├── News_Content_n_35497_s_257857.html    # 口試榜單
├── News_Content_n_35497_s_250871.html    # 徵聘教師
├── News_Content_n_35497_s_211542.html    # 榮退教授專訪
├── News_Content_n_35497_s_211541.html    # 榮退教授專訪
├── News_Content_n_35497_s_104734.html    # 新聘教師專訪
├── News_Content_n_35497_s_104732.html    # 新聘教師專訪
├── News_Content_n_35497_s_104731.html    # 新聘教師專訪
└── (以及對應的 sms_26652 版本)
```

### 3. activities/ (活動資訊) - 97個文件
```
activities/
├── News2_n_35498_sms_26668.html          # 活動資訊列表頁
├── News_Content_n_35498_s_258988.html    # ETtoday總編演講
├── News_Content_n_35498_s_257550.html    # 訪問學者講座
├── News_Content_n_35498_s_257534.html    # 新書分享會
├── News_Content_n_35498_s_254585.html    # 學者講座
├── News_Content_n_35498_s_254584.html    # 以巴衝突講座
├── News_Content_n_35498_s_244147.html    # AI新聞論壇
├── News_Content_n_35498_s_242697.html    # 假訊息研討會
├── News_Content_n_35498_s_242587.html    # 國際影展講座
└── ... (共97個活動內容頁面)
```

### 4. photos/ (照片內容) - 25個文件
```
photos/
├── News_Photo_n_18801_sms_26671.html     # 照片內容列表頁
├── News_Photo_Content_n_18801_s_*.html   # 各期照片內容
└── ... (共25個照片頁面)
```

### 5. about/ (關於本所) - 4個文件
```
about/
├── intro.html            # 本所介紹
├── mission.html          # 宗旨與目標
├── gallery.html          # 新聞所圖集
└── transportation.html   # 聯絡我們
```

### 6. admissions/ (招生專區) - 7個文件
```
admissions/
├── admissions.html                    # 招生總覽
├── qualifying-exam.html               # 甄試入學簡章
├── entrance-exam.html                 # 招生考試簡章
├── past-exam.html                     # 歷屆考古題
├── international-students.html        # 國際生
├── ochkmc-students.html               # 僑港澳生
└── mainland-chinese-students.html     # 陸生
```

### 7. courses/ (課程規劃) - 4個文件
```
courses/
├── course-map.html                       # 課程地圖
├── course-regulation.html                # 修業規定
├── statute-and-form.html                 # 學位考試資訊
└── cross-school-course-cooperation.html  # 校際與跨系選課
```

### 8. publications/ (出版發表) - 4個文件
```
publications/
├── e-report.html           # 前期所報
├── master-thesis.html      # 畢業生論文
├── books.html              # 報導專書
└── ntu-news-forum.html     # 臺大新聞論壇
```

### 9. 根目錄主要頁面
```
根目錄/
├── Default.html          # 原始首頁（保持原有layout）
├── index.html            # 新版首頁（可選）
├── event.html            # 消息與活動總覽
├── staff.html            # 行政人員
├── resident-reporter.html # 駐地記者
├── international-communication.html # 國際交流
├── academic-activity.html # 學術活動
├── cp_n_*.html           # 其他內容頁面
├── SiteMap.html          # 網站地圖
├── Advanced_Search.html  # 進階搜尋
└── update_links.py       # 連結更新腳本
```

## 📊 統計資訊

| 類別 | 資料夾 | 文件數量 | 說明 |
|------|--------|----------|------|
| 師資 | faculty/ | 11 | 包含個別教師頁面和總覽頁面 |
| 新聞 | news/ | 22 | 最新消息列表和內容頁 |
| 活動 | activities/ | 97 | 活動資訊列表和內容頁 |
| 照片 | photos/ | 25 | 照片內容列表和圖集頁 |
| 關於 | about/ | 4 | 本所介紹相關頁面 |
| 招生 | admissions/ | 7 | 招生相關資訊 |
| 課程 | courses/ | 4 | 課程規劃相關 |
| 出版 | publications/ | 4 | 出版發表相關 |
| **總計** | - | **174** | **已組織的頁面** |

## 🔗 連結與資源路徑更新

所有頁面中的連結和資源路徑已經更新：

### 內部連結更新
- ✅ 第一階段：更新了 194 個 HTML 文件的連結路徑
- ✅ 第二階段：修正了 174 個子資料夾文件的相對路徑（21,521 處修正）
- ✅ 所有內部連結都已更新到正確的相對路徑：
  - 根目錄文件使用 `folder/file.html` 格式
  - 子資料夾文件使用 `../folder/file.html` 格式訪問其他資料夾
  - 子資料夾文件使用 `file.html` 格式訪問同一資料夾內的文件

### CSS/JS資源路徑修正
- ✅ 修正了 174 個子資料夾文件的資源路徑（3,855 處修正）
- ✅ 所有子資料夾文件的資源路徑已更新：
  - CSS路徑：`../css/global.css`, `../css/page.css`
  - JS路徑：`../Scripts/jquery.min.js`, `../js/airdatepicker/datepicker.min.js`
  - 圖片路徑：`../images/favicon.ico`

## 📝 維護說明

### 新增教師頁面
1. 在 `faculty/` 資料夾創建新的 HTML 文件
2. 更新 `faculty/fulltime-professor.html` 添加連結
3. 確保連結格式：`href="教師檔名.html"`

### 新增新聞文章
1. 在 `news/` 資料夾創建新的 `News_Content_n_35497_s_*.html`
2. 更新 `news/News_n_35497_sms_26652.html` 添加到列表
3. 保持檔案命名規則一致

### 新增活動資訊
1. 在 `activities/` 資料夾創建新的 `News_Content_n_35498_s_*.html`
2. 更新 `activities/News2_n_35498_sms_26668.html` 添加到列表
3. 保持檔案命名規則一致

### 連結規則
從根目錄頁面連結到子資料夾：
```html
<a href="faculty/faculty.html">師資陣容</a>
<a href="news/News_n_35497_sms_26652.html">最新消息</a>
<a href="activities/News2_n_35498_sms_26668.html">活動資訊</a>
```

從子資料夾連結回根目錄：
```html
<a href="../Default.html">首頁</a>
<a href="../event.html">消息與活動</a>
```

## 🎯 優點

1. **清晰的結構** - 每個類別都有專屬資料夾
2. **易於維護** - 相關文件集中管理
3. **可擴展性** - 容易新增新的內容
4. **保持原有layout** - 所有原始頁面layout都未改變
5. **連結完整性** - 所有內部連結都已更新

## ⚠️ 注意事項

1. **保持原有layout** - 本次整理只是組織檔案結構，未改變頁面設計
2. **圖片路徑** - 如果頁面中有相對路徑的圖片，可能需要調整
3. **CSS/JS路徑** - 子資料夾頁面的CSS/JS路徑需使用 `../` 前綴
4. **備份** - 建議保留原始檔案的備份

## 🛠️ 使用的腳本工具

1. **update_links.py** - 初始連結更新腳本
   - 批量更新所有HTML文件中的連結，指向新的資料夾結構

2. **fix_relative_paths.py** - 相對路徑修正腳本
   - 修正子資料夾中文件的相對路徑
   - 確保同一資料夾內的連結不含路徑前綴
   - 確保跨資料夾連結使用 `../` 前綴

3. **fix_css_js_paths.py** - CSS/JS資源路徑修正腳本
   - 修正子資料夾文件中的CSS和JavaScript路徑
   - 為所有資源路徑添加 `../` 前綴

---

最後更新：2025-11-06
