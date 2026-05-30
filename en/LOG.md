# Change Log — Graduate Institute of Journalism, NTU (English Website)

> **Rule:** Every time a prompt is used to revise the code, record the entry here with:
> `## [YYYY-MM-DD HH:MM TST] — Brief title`
> followed by the prompt summary and files changed.
> Time zone: Taiwan Standard Time (TST, UTC+8).

---

## [2026-05-07 ~15:20 TST] — Initial website build

**Prompt summary:**
> 「我現在想要架設一個一頁式的英文版網頁，其中文版網頁為：https://ntujour.github.io/ （視覺風格參考）。英文資訊請參考：https://webpageprodvm.ntu.edu.tw/Journalism/Default.aspx。這個頁面會有以下資訊：簡短的 Introduction、新聞所 news、新聞所教師（full-time 專任教師需額外有連結，建立一個新的頁面）」

**Actions taken:**
- Fetched content from `ntujour.github.io` and `webpageprodvm.ntu.edu.tw/Journalism/` to gather design references, English content, faculty info, and news items.
- Fetched all 7 full-time faculty profile pages from the NTU official site.
- Created `css/style.css` — full stylesheet with dark-blue NTU color scheme (initial draft, later revised).
- Created `index.html` — one-page site with: site banner, sticky nav, hero section, Introduction (with pillar cards and stats), News (5 cards), Faculty grid (7 cards).
- Created 7 faculty profile pages under `faculty/`:
  - `ji-lung-hsieh.html`
  - `lih-yun-lin.html`
  - `chen-ling-hung.html`
  - `adrian-rauchfleisch.html`
  - `hui-ju-tsai.html`
  - `i-i-chan.html`
  - `lokman-tsui.html`

**Files created:** `css/style.css`, `index.html`, `faculty/ji-lung-hsieh.html`, `faculty/lih-yun-lin.html`, `faculty/chen-ling-hung.html`, `faculty/adrian-rauchfleisch.html`, `faculty/hui-ju-tsai.html`, `faculty/i-i-chan.html`, `faculty/lokman-tsui.html`

---

## [2026-05-07 ~15:34 TST] — Color scheme & banner redesign to match ntujour.github.io

**Prompt summary:**
> 「我的配色要和 https://ntujour.github.io/ 的配色一模一樣！還有最頂端的 bar 也要一樣！」

**Actions taken:**
- Fetched raw HTML source of `ntujour.github.io` via `curl` to obtain exact class names and structure.
- Fetched `ntujour.github.io/css/site-common.css` to extract exact color values.
- Fetched `ntujour.github.io/js/load-banner.js` to understand dynamic banner rendering.
- Identified the correct color palette:
  - Nav background: `#671919` (maroon)
  - Active/hover nav text: `#efa22a` (gold)
  - Footer background: `#3e0f0f` (dark maroon)
  - Banner background: `#f5f5f5` (light gray) with decorative images
- Rewrote `css/style.css` completely with the new color variables and banner styles.
- Updated `index.html`: replaced dark-blue `.topbar` + `.navbar` with light-gray `.site-banner` + maroon `.site-nav`; moved 中文 language link into nav; fixed scroll-spy offset calculation.
- Updated all 7 faculty pages via Python batch script: replaced `.topbar` + `.navbar` blocks with the new `.site-banner` + `.site-nav` structure.

**Files modified:** `css/style.css`, `index.html`, `faculty/ji-lung-hsieh.html`, `faculty/lih-yun-lin.html`, `faculty/chen-ling-hung.html`, `faculty/adrian-rauchfleisch.html`, `faculty/hui-ju-tsai.html`, `faculty/i-i-chan.html`, `faculty/lokman-tsui.html`

---

## [2026-05-07 ~15:40 TST] — Project review and documentation

**Prompt summary:**
> 「Please review whole project, and save the record as INSTRUCTION.md, and generate another LOG.md used to record each operation. And note a rule on INSTRUCTION.md, each time when using prompt to revise the code, please record each prompt's date and time.」

**Actions taken:**
- Reviewed full project file structure and all source files.
- Created `INSTRUCTION.md` with: project overview, file structure, design system (colors, typography, layout), banner/nav spec, content update guide, deployment notes, external dependencies, and the logging rule.
- Created `LOG.md` (this file) with retrospective entries for all previous sessions and the logging rule explanation.

**Files created:** `INSTRUCTION.md`, `LOG.md`

---

## [2026-05-07 ~16:00 TST] — Expand Faculty section with additional categories

**Prompt summary:**
> 「請幫我修改 index.html，我希望在 faculty 的階段，可以將標題「Full-Time Faculty」放大一點，且接續幫我加上 adjunct faculty, adjunct specialist faculty, professor emeritus, joint appointment, rememberance，新加的內容不用額外的頁面，簡短介紹這些老師就好。名單請參考：https://webpageprodvm.ntu.edu.tw/Journalism/faculty.htm」

**Actions taken:**
- Fetched faculty data from NTU official pages: `adjunct.htm`, `practical-faculty.htm`, `emeritus-professor.htm`, `jointly-appointed-professor.htm`, `remembrance.htm`.
- Added new CSS classes to `css/style.css`: `.faculty-section-heading`, `.heading-fulltime`, `.heading-remembrance`, `.faculty-compact-grid`, `.faculty-compact-card`, `.card-remembrance`, `.faculty-compact-name`, `.faculty-compact-title`, `.faculty-compact-sub`.
- Updated `index.html` Faculty section:
  - Changed "Full-Time Faculty" label from `.faculty-label` to a larger `<h3 class="faculty-section-heading heading-fulltime">`.
  - Added 5 new subsections with compact card grids:
    - **Adjunct Faculty** (3 members): Tai-Li Wang, Shuen-Xiao Chen, Lin-Lin Ku
    - **Adjunct Specialist Faculty** (13 members): Li, Liang, Lee, Lee, Huang, Yang, Liou, Cheng, Shiau, Zhang, Huang, Fang, Wu
    - **Professor Emeritus** (1 member): Chin-Hua Chang
    - **Jointly Appointed Faculty** (2 members): Ching-Yi Liu, Hui-Chieh Su
    - **In Remembrance** (2 members): Rou-Jin Chen, Yen-Yuan Ni

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-07 ~16:15 TST] — Remove Hero, remove news links, delete first news item

**Prompt summary:**
> 「請幫我 1. 把 HERO 刪掉 2. news 不要有任何的 href 3. news的第一條 2026 entrance刪掉」

**Actions taken:**
- Deleted the `<!-- HERO -->` section (`<div class="hero">`) from `index.html`.
- Changed all 5 `<a class="news-card" href="...">` elements to `<div class="news-card">` (removed all `href`, `target`, `rel` attributes).
- Deleted the first news card "2026 Entrance Examination and Admissions Brochure".
- Synced `index.html` to main repo folder.

**Files modified:** `index.html`

---

## [2026-05-07 ~18:25 TST] — All faculty tabs use full-time card style; remove Chao-Hwei Huang; add Wan-Yu Wu photo

**Prompt summary:**
> 「請幫我把所有 faculty 的 card 改成和 fulltime faculty 一樣，另外幫我把 adjunct 裡面的 Chao-Hwei Huang 整個拿掉，並且要增加 Wan-Yu Wu 的圖片（在 image 資料夾）」

**Actions taken:**
- Converted all 5 non-full-time tab panels (Adjunct, Adjunct Specialist, Professor Emeritus, Jointly Appointed, In Remembrance) from `.faculty-compact-grid` / `.faculty-compact-card` to `.faculty-grid` / `.faculty-card`, matching the full-time faculty card layout (300px photo on top, name/badge/tags below).
- Removed Chao-Hwei Huang (黃兆徽) entirely from the Adjunct Specialist panel.
- Replaced Wan-Yu Wu's character placeholder with `<img src="image/Wan-Yu%20Wu.jpg">`.
- Added `.faculty-card-remembrance` CSS variant (gray top border, slight opacity) for In Remembrance cards.

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-07 ~18:10 TST] — Faculty section: NHK-style tab switcher

**Prompt summary:**
> 「faculty 那塊我想要改成 nhk網站中 class為section-colored-nowonair的那種感覺，也就是有按鈕可以切換目前看到的內容」

**Actions taken:**
- Added a `.faculty-tab-bar` with 6 `<button class="faculty-tab-btn">` elements (Full-Time, Adjunct, Adjunct Specialist, Prof. Emeritus, Jointly Appointed, In Remembrance).
- Wrapped each faculty category in a `<div class="faculty-tab-panel">` with a matching `id` (`faculty-fulltime`, `faculty-adjunct`, `faculty-specialist`, `faculty-emeritus`, `faculty-joint`, `faculty-remembrance`); only the first panel has `class="active"` by default.
- Added CSS: tab buttons styled with a browser-tab look (rounded top corners, maroon filled when active); panels use `display:none` / `display:block` toggling.
- Added JS: clicking a tab button hides all panels, shows the selected one, and updates `aria-selected`.
- Updated sidebar sub-nav links to use `data-faculty-tab` attributes; added JS handler that activates the matching tab and smooth-scrolls to the faculty section.

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-07 ~17:50 TST] — Font size, photo height, pillar layout, sidebar sub-nav, remove sidebar header

**Prompt summary:**
> 「1. 整體非標題的文字幫我加大 2. 把 index 介面的 full-time faculty 的照片，高度改為 300 3. introduction 右側的 grid 改為一個 column，不要兩個 4. navigation bar 保留 introduction, news 和 faculty 就好，faculty 下面可以增加 fulltime, adjunct...... 的子欄位 5. navigation bar 上面的「Graduate Institute of Journalism 國立臺灣大學新聞研究所 Cultivating Journalism Talent for a New Era」拿掉」

**Actions taken:**
- `body { font-size: 18px }` (up from 16px).
- `.faculty-photo-wrap { height: 300px }` (up from 200px).
- `.intro-pillars { grid-template-columns: 1fr }` (collapsed from 2-col).
- Removed `.sidebar-institute` block from sidebar HTML.
- Replaced sidebar nav with 3 top-level links (Introduction, News, Faculty); added 6 sub-items under Faculty linking to anchors `#faculty-fulltime`, `#faculty-adjunct`, `#faculty-adjunct-specialist`, `#faculty-emeritus`, `#faculty-joint`, `#faculty-remembrance`.
- Added corresponding `id` attributes to all 6 faculty subsection `<h3>` headings.
- Added `.sidebar-nav-sub-list` and `.sidebar-nav-sub-link` CSS.
- Cleaned up now-redundant responsive `.intro-pillars` overrides.

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-07 ~17:35 TST] — Left sidebar nav + slim top header (NHK-style layout)

**Prompt summary:**
> 「請幫我把 navigator bar 移至左側，最上面的新聞所 bar 再小一點，感覺會像：https://www.nhk.or.jp/」

**Actions taken:**
- Replaced large `.site-banner` + horizontal `.site-nav` with:
  - `.site-header` — 54px slim sticky top bar (maroon) with site name, Chinese sub-title, and 中文 language link
  - `.site-layout` flex wrapper containing `.site-sidebar` (210px sticky left nav) + `.site-main` (flex content area)
  - `.site-sidebar` — white background, left-border active indicator (gold), institute mini-card on top, then nav links
- Rewrote scroll-spy JS to target `.sidebar-nav-link[data-section]` instead of old `.nav-link`
- Added responsive breakpoints: sidebar narrows to 170px at ≤960px; collapses to horizontal strip at ≤720px
- Updated all 7 `faculty/*.html` to use the new `.site-header` (replacing `.site-banner`)

**Files modified:** `css/style.css`, `index.html`, all 7 `faculty/*.html`

---

## [2026-05-07 ~17:20 TST] — Footer 2/3+1/3 layout; remove nav from faculty pages

**Prompt summary:**
> 「請幫我把 footer 改成左邊是 Graduate Institute of Journalism 的小簡介（內容不改），占寬度的 2/3；右邊是聯絡方式（內容不改），占寬度的 1/3。另外，再幫我把所有 fulltime faculty 的網頁拿掉 navigator」

**Actions taken:**
- Changed `.footer-cols` from `grid-template-columns: 2fr 1fr 1fr` to `2fr 1fr`; updated responsive breakpoint at ≤960px to collapse to `1fr` (was `1fr 1fr`).
- Removed the "Quick Links" `<div class="footer-col">` from `index.html` and all 7 faculty pages.
- Removed `<nav class="site-nav">` from the 5 faculty pages that had the new banner structure.
- For `lih-yun-lin.html` and `i-i-chan.html` (still had old `topbar`+`navbar` structure): replaced with new `<header class="site-banner">` and removed `<nav class="navbar">`, bringing them in line with the other 5 faculty pages.

**Files modified:** `css/style.css`, `index.html`, all 7 `faculty/*.html`

---

## [2026-05-07 ~17:10 TST] — Compact faculty: 3-column grid, larger name & photo

**Prompt summary:**
> 「我覺得除了 fulltime faculty 的老師名字都太小了，請幫我將所有人的名字格式，改成和 fulltime faculty 一樣的大小。同時，將除了 fulltime faculty 以外的其他區塊，從原本的一列兩個 card 變成一列三個 card，且照片再大一點」

**Actions taken:**
- Changed `.faculty-compact-grid` from `repeat(2, 1fr)` to `repeat(3, 1fr)`.
- Added responsive fallback: 2 columns at ≤960px, 1 column at ≤600px.
- Increased `.faculty-compact-name` font-size from `0.95rem` to `1.04rem` (matching `.faculty-name`).
- Enlarged `.faculty-compact-photo-wrap` from 64×76px to 80×96px; bumped placeholder font-size accordingly.

**Files modified:** `css/style.css`

---

## [2026-05-07 ~17:00 TST] — Switch all faculty photos to local image/ folder

**Prompt summary:**
> 「我有將所有 faculty 的照片放在 image 資料夾，請幫我將照片來源更新為 image 資料夾中的照片」

**Actions taken:**
- Copied `image/` folder from main repo into worktree.
- Ran Python batch script to replace all NTU media-server `src="https://webpageprod-ws..."` URLs with local `image/<Name>.<ext>` paths (URL-encoded spaces as `%20`) across `index.html` and all 7 `faculty/*.html` files; also removed `onerror` fallback handlers since files are now local.
- Replaced character placeholder divs for Lih-Yun Lin and I-I Chan (both in `index.html` and their profile pages) with proper `<img>` tags pointing to local files.

**Files modified:** `index.html`, `faculty/lih-yun-lin.html`, `faculty/i-i-chan.html`, `faculty/ji-lung-hsieh.html`, `faculty/chen-ling-hung.html`, `faculty/adrian-rauchfleisch.html`, `faculty/hui-ju-tsai.html`, `faculty/lokman-tsui.html`

---

## [2026-05-07 ~16:45 TST] — Compact faculty grid: 2-column layout, maroon/gray name colors

**Prompt summary:**
> 「請把除了 full-time faculty 以外的所有 faculty，將原本一列四個老師改為一列兩位老師，card 內容改為左邊為圖片，右邊為老師名字、職稱（如果有再加）、授課項目。老師的名字顏色格式如同 full-time faculty，英文名為 #671919，中文部分為灰色」

**Actions taken:**
- Changed `.faculty-compact-grid` from `repeat(auto-fill, minmax(240px, 1fr))` to `repeat(2, 1fr)` so exactly 2 cards appear per row.
- Added `@media (max-width: 600px)` breakpoint to collapse compact grid to 1 column on small screens.
- Name color (`.faculty-compact-name`) was already `var(--maroon)` = `#671919`; Chinese span (`.faculty-compact-zh`) was already `var(--text-500)` = gray — no change needed.

**Files modified:** `css/style.css`

---

## [2026-05-07 ~16:30 TST] — Add photos and Chinese-name styling to all compact faculty cards

**Prompt summary:**
> 「針對所有index.html 的所有 faculty card，我希望格式可以像 full-time faculty 一樣，中文名以灰色小字呈現 另外所有人請附上照片，但放在 card 左邊、小張圖片就好」

**Actions taken:**
- Added horizontal flex layout CSS to `css/style.css`: `.faculty-compact-photo-wrap`, `.faculty-compact-photo`, `.faculty-compact-placeholder-sm`, `.faculty-compact-info`, `.faculty-compact-zh`.
- Fetched photo URLs for all 21 compact faculty members from NTU official pages (`adjunct.htm`, `practical-faculty.htm`, `emeritus-professor.htm`, `jointly-appointed-professor.htm`, `remembrance.htm`).
- Rewrote all 21 compact cards in `index.html` to use the new horizontal layout: photo wrap on the left (64×76px), info block on the right with English name + `<span class="faculty-compact-zh">(中文名)</span>` in gray small text.
- Wan-Yu Wu uses a character placeholder (吳) as her photo URL matched another faculty member's, likely a scraping error.

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-07 ~17:00 TST] — Convert all non-full-time faculty cards to full-time card style; remove Chao-Hwei Huang; add Wan-Yu Wu photo

**Prompt summary:**
> 「請幫我把所有 faculty 的 card 改成和 fulltime faculty 一樣，另外幫我把 adjunct 裡面的 Chao-Hwei Huang 整個拿掉，並且要增加 Wan-Yu Wu 的圖片（在image資料夾）」

**Actions taken:**
- Replaced all 21 compact cards (`.faculty-compact-grid` / `.faculty-compact-card`) in the 5 non-full-time panels with full-size cards using `.faculty-grid` / `.faculty-card` (300px photo, badge, tags), matching the full-time panel layout.
- Removed Chao-Hwei Huang's card from the Adjunct Specialist panel entirely.
- Added `<img class="faculty-photo" src="image/Wan-Yu%20Wu.jpg">` for Wan-Yu Wu, replacing the character placeholder.

**Files modified:** `index.html`

---

## [2026-05-07 ~17:20 TST] — Full-width footer; suppress non-full-time hover effects; make full-time cards fully clickable

**Prompt summary:**
> 「1. footer 的寬度請幫我撐到網頁寬，不要讓 navigator 區塊壓住它。2. 除了 fulltime faculty 的其他faculty，在滑鼠點到他們的名字時，不要有底線。滑鼠點到他們的 card 時，不要讓 card 浮起來。3. 點選 fulltime faculty 的 card 的任何位置，就可以連到他們各自的網站」

**Actions taken:**
- Moved `<footer>` outside of `<div class="site-layout">` so it renders as a full-width block-level element, no longer constrained by the 210px sidebar column.
- Changed all 7 full-time faculty cards from `<div class="faculty-card">` to `<a class="faculty-card" href="faculty/[name].html">` so the entire card is clickable; replaced inner `<a class="faculty-name">` with `<span class="faculty-name">` to avoid nested anchors.
- Added CSS in `style.css`:
  - `a.faculty-card { display:block; text-decoration:none; color:inherit; cursor:pointer; }` — makes the `<a>` wrapper behave like the old `<div>`.
  - `a.faculty-card:hover .faculty-name { text-decoration: underline; }` — preserves name underline on hover for full-time cards only.
  - `.faculty-tab-panel:not(#faculty-fulltime) .faculty-card:hover { box-shadow:none; transform:none; cursor:default; }` — suppresses card lift and pointer cursor on all non-full-time panels.
  - Removed old `.faculty-name:hover { text-decoration: underline; }` rule that would have applied to non-full-time cards.

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-13 ~12:50 TST] — Lokman Tsui profile: full content rewrite

**Prompt summary:**
> 「針對 lokman-tsui.html，請幫我做以下修改：1. Teaching Field 中，將標籤刪除，新增：Freedom of Speech and Society, Information Technologies, Information Sociologies 2. 刪除 Research Areas 3. 將以下內容加入頁面：Language, Employment, Books, Special Journal Issues, Journal Articles and Other Publications, Academic conferences and workshops, Presentations for civil society, government and others, Awards and Honors, Grants, Service (selected)」

**Actions taken:**
- Rewrote `data/faculty/lokman-tsui.json` with 10 sections from NTU faculty page.
- Updated Teaching Field to: Freedom of Speech and Society, Information Technologies, Information Sociologies.
- Added sections: Language (text type), Employment (6 items), Books (1), Special Journal Issues (1), Journal Articles and Other Publications (26 items), Academic Conferences and Workshops (15 items), Presentations for Civil Society, Government and Others (25 items), Awards and Honors (3), Grants (3), Service Selected (6).

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-13 ~13:02 TST] — Sidebar overflow fix; External Links label updates; Adrian Rauchfleisch Teaching Field

**Prompt summary:**
> 「1. 所有 faculty 頁面的 sidebar-card，不要讓內容超出框框，可換行 2. lokman-tsui.html 的 External Links 文字改為「lokman.org」 3. adrian-rauchfleisch.html 的 External Links 文字改為「arauchfleisch.ch」 4. adrian-rauchfleisch.html 請刪除 Articles in Peer-Reviewed Journals，改為根據 https://arauchfleisch.ch/publications/ 的 Journal Article, Book Chapter, Working Paper 三區塊」
> 「針對 adrian-rauchfleisch.html，請幫我做以下修改：1. Teaching Field 中，將標籤 Social Media and Social Network Analysis 刪除，新增：Social Media, Social Network Analysis, Communication Research Method」

**Actions taken:**
- Added `overflow-wrap: break-word; word-break: break-word; min-width: 0;` to `.sidebar-card` in `css/style.css`.
- Changed `contacts[2].text` and `externalLinks[0].text` in `lokman-tsui.json` from "Personal Website" to "lokman.org".
- Changed `externalLinks[0].text` in `adrian-rauchfleisch.json` from "Personal Website" to "arauchfleisch.ch".
- Removed "Articles in Peer-Reviewed Journals" section from `adrian-rauchfleisch.json`; added 3 new sections: Journal Articles, Book Chapters, Working Papers (initially with placeholder items).
- Updated Adrian Rauchfleisch Teaching Field: removed "Social Media and Social Network Analysis", added "Social Media", "Social Network Analysis", "Communication Research Method".

**Files modified:** `css/style.css`, `data/faculty/lokman-tsui.json`, `data/faculty/adrian-rauchfleisch.json`

---

## [2026-05-13 ~13:08 TST] — Hui-Ju Tsai: reformat Experiences dates; fix External Links label

**Prompt summary:**
> 「針對 hui-ju-tsai.html，請幫我做以下修改：1. Experiences 區塊的內文，時間放至最後 2. External Links 連結文字改為「tintincai.wixsite.com/hjtsai」」

**Actions taken:**
- Reformatted all 3 Experiences items in `data/faculty/hui-ju-tsai.json`: moved date ranges to end in parentheses (e.g., `(2021.8–present)`).
- Changed `contacts[2].text` and `externalLinks[0].text` to "tintincai.wixsite.com/hjtsai".

**Files modified:** `data/faculty/hui-ju-tsai.json`

---

## [2026-05-13 ~16:24 TST] — Adrian Rauchfleisch: replace Journal Articles with curated list from arauchfleisch.ch

**Prompt summary:**
> 「針對 adrian-rauchfleisch.html，請幫我刪除 Journal Article 目前的內文，並新增：[31 items]」
> 「針對 adrian-rauchfleisch.html，請幫我在 Journal Article 目前的內文後新增：[22 more items]」

**Actions taken:**
- Replaced Journal Articles section in `data/faculty/adrian-rauchfleisch.json` with curated list of 53 items (2013–2026) sourced from arauchfleisch.ch. Format: `Authors. (Year). Title. <em>Journal</em>.`

**Files modified:** `data/faculty/adrian-rauchfleisch.json`

---

## [2026-05-13 ~16:44 TST] — Adrian Rauchfleisch: replace Book Chapters and Working Papers

**Prompt summary:**
> 「針對 adrian-rauchfleisch.html，請幫我刪除 Book Chapter 目前的內文，並新增：[16 items]」
> 「針對 adrian-rauchfleisch.html，請幫我刪除 Working Papers 目前的內文，並新增：[2 items]」

**Actions taken:**
- Replaced Book Chapters section with 16 items (2015–2026).
- Replaced Working Papers section with 2 items.

**Files modified:** `data/faculty/adrian-rauchfleisch.json`

---

## [2026-05-13 ~16:47 TST] — Hide profile sidebar on narrow screens

**Prompt summary:**
> 「針對所有 faculty 頁面，當 profile-body 寬度無法放置兩欄（左內文、右 sidebar）時，請自動隱藏 sidebar，不用顯示在畫面上」

**Actions taken:**
- Added `@media (max-width: 960px)` rules to `css/style.css`: `.profile-sidebar { display: none; }`, `.profile-body-inner { grid-template-columns: 1fr; }`, `.profile-meta-inner { grid-template-columns: 1fr; }`.

**Files modified:** `css/style.css`

---

## [2026-05-13 ~17:02 TST] — Responsive fixes: news cards stack at ≤960px; faculty tab buttons shrink

**Prompt summary:**
> 「針對 index.html 頁面，若頁面寬度 ≤960px：1. news 區塊從左右分欄改為上下 2. Faculty 區塊的按鍵調小，裡面的標籤也調小」

**Actions taken:**
- Added `@media (max-width: 960px)` rules: `.news-card { grid-template-columns: 1fr; gap: 0.4rem; }`, `.news-meta { flex-direction: row; align-items: center; gap: 0.6rem; }`, `.faculty-tab-btn { font-size: 0.75rem; padding: 0.35rem 0.7rem; }`.

**Files modified:** `css/style.css`

---

## [2026-05-13 ~22:41 TST] — Update full-time faculty tags on index page

**Prompt summary:**
> 「針對 index.html 的頁面，幫我修改 faculty 下的 full-time 區塊：Ji-Lung Hsieh (Data Journalism, Web Design, Social Network Analysis), Lih-Yun Lin (History of News, Media Sociology, Communication Theories), Chen-Ling Hung (Communication Laws, Globalization and Communications, Political Economy of Communication), Adrian Rauchfleisch (Social Media, Political Communication, Methods for Communication Science), Hui-Ju Tsai (STS, Cultural Studies, Public Service Media), Lokman Tsui (Information Sociologies, Freedom of Speech and Society, Digital Security)」

**Actions taken:**
- Updated `tags` arrays for all 6 full-time faculty in `data/faculty.json`.

**Files modified:** `data/faculty.json`

---

## [2026-05-13 ~22:43 TST] — Responsive font scaling at ≤960px and ≤600px

**Prompt summary:**
> 「當 ≤960px 時，請把整體頁面的字縮小」
> 「當 ≤600px 時，字要比 ≤960px 再小」
> 「≤960px ≤600px 的文字在 Curriculum 的內文沒被改到（fix）」

**Actions taken:**
- Changed `body { font-size: 18px }` to `body { font-size: 1.125rem }` so it inherits from `html` font-size and scales with breakpoints.
- Added `html { font-size: 15px }` at `@media (max-width: 960px)` and `html { font-size: 13px }` at `@media (max-width: 600px)`.

**Files modified:** `css/style.css`

---

## [2026-05-13 ~22:52 TST] — Update adjunct and specialist faculty tags; shrink tags at ≤600px

**Prompt summary:**
> 「針對 index.html 的頁面，幫我修改 faculty 下的 adjunct 區塊：Tai-Li Wang (add Video Journalism), Shuen-Xiao Chen (News Industry Innovation, Media Literacy), Lin-Lin Ku (Communication Statistics, News Writing in English)」
> 「當 ≤600px，請把 index.html 頁面的所有 faculty 的 tag，字再縮小」
> 「針對 index.html 的頁面，幫我修改 faculty 下的 Adjunct Specialist 區塊：[4 faculty single combined tags]」

**Actions taken:**
- Updated adjunct and specialist tags in `data/faculty.json`.
- Added `@media (max-width: 600px)` rule: `.ftag { font-size: 0.6rem; padding: 0.12rem 0.35rem; }`.
- Added `@media (max-width: 600px)` rule: `.faculty-name, .faculty-compact-name { font-size: 1.2rem; }` (2px larger than inherited base).

**Files modified:** `data/faculty.json`, `css/style.css`

---

## [2026-05-13 ~23:02 TST] — Update Jointly Appointed and In Remembrance faculty tags

**Prompt summary:**
> 「針對 index.html 的頁面，幫我修改 faculty 下的 Jointly Appointed 區塊：Ching-Yi Liu (Communication and Society, Digital Humanities), Hui-Chieh Su (Philosophy of Communication, Logic)」
> 「針對 index.html 的頁面，幫我修改 faculty 下的 In Remembrance 區塊：Rou-Jin Chen (Political Economy, News Editing), Yen-Yuan Ni (Media Ethics, News Writing)」

**Actions taken:**
- Updated `joint` and `remembrance` group tags in `data/faculty.json`.

**Files modified:** `data/faculty.json`

---

## [2026-05-13 ~23:09 TST] — Add Retired faculty section with Chao-Chen Lin

**Prompt summary:**
> 「針對 index.html 的頁面，在 faculty 下的 Jointly Appointed 與 In Remembrance 之間新增 Retired，底下有 Chao-Chen Lin（林照真），Professor，tag 有 Visual Journalism, Investigative Journalism, In-depth Reporting」

**Actions taken:**
- Added "Retired" tab button between Jointly Appointed and In Remembrance in `index.html`.
- Added sidebar nav link for Retired section.
- Added `<div id="faculty-retired" class="faculty-tab-panel">` panel with Chao-Chen Lin card.
- Added `retired` group to JavaScript tabs map.
- Added Chao-Chen Lin entry to `data/faculty.json` under new "retired" group.

**Files modified:** `index.html`, `data/faculty.json`

---

## [2026-05-13 ~23:13 TST] — Update Hui-Ju Tsai header contact link text

**Prompt summary:**
> 「hui-ju-tsai.html 的 profile-header 下的第三個 profile-contact-item，請將文字從「Personal Website」改為「tintincai.wixsite.com/hjtsai」」

**Actions taken:**
- Updated `contacts[2].text` in `data/faculty/hui-ju-tsai.json` (already done in earlier session; confirmed correct value).

**Files modified:** `data/faculty/hui-ju-tsai.json`

---

## [2026-05-13 ~23:15 TST] — Match News title font size to Introduction body text; remove acceptance rate stat

**Prompt summary:**
> 「幫我把 News 標題改成和 Introduction 內文一樣大」
> 「請把 Introduction 下的 intro-stats 的第二個 stat（<5% acceptance rate）刪掉」

**Actions taken:**
- Changed `.news-title { font-size }` to `1.125rem` in `css/style.css` (matching body text size).
- Removed the `<5% Acceptance Rate` stat block from `index.html`.

**Files modified:** `css/style.css`, `index.html`

---

## [2026-05-13 ~23:29 TST] — Hide news-excerpt at ≤600px

**Prompt summary:**
> 「當畫面 ≤600px，請把 News-card 的 news-excerpt 隱藏」

**Actions taken:**
- Added `.news-excerpt { display: none; }` inside `@media (max-width: 600px)` in `css/style.css`.

**Files modified:** `css/style.css`

---

## [2026-05-13 ~23:34 TST] — Responsive faculty grid fixes (faculty-compact-grid → faculty-grid at ≤960px)

**Prompt summary:**
> 「Faculty compact grid 改單欄，請在 ≤1200px 便執行」（initial request, later corrected）
> 「當畫面 ≤1200px 時，應該是要改 faculty-grid 吧？」
> 「faculty-compact-grid 出現在哪？」
> 「那請刪掉 faculty-compact-grid，另外，faculty-grid → 單欄 改為 ≤960px」

**Actions taken:**
- Confirmed `faculty-compact-grid` is not used anywhere in HTML or JS.
- Removed all `faculty-compact-grid` CSS rules from `css/style.css`.
- Added `.faculty-grid { grid-template-columns: 1fr; }` inside `@media (max-width: 960px)`.

**Files modified:** `css/style.css`

---

## [2026-05-14 ~00:11 TST] — Shorten faculty tags for display

**Prompt summary:**
> 「請幫我修改 faculty 的 tag：1. Tai-Li Wang 刪除 Video Journalism 2. Chen-Ling Hung 的「Globalization and Communication」改為「Globalization」，「Political Economy of Communication」改為「Political Economy」 3. Lokman Tsui 的「Freedom of Speech and Society」改為「Freedom of Speech」 4. Chao-Chen Lin 刪除 In-depth Reporting」

**Actions taken:**
- Updated `data/faculty.json`: Tai-Li Wang → [Media Psychology, Political Communication]; Chen-Ling Hung → [Communication Laws, Globalization, Political Economy]; Lokman Tsui → [Information Sociologies, Freedom of Speech, Digital Security]; Chao-Chen Lin → [Visual Journalism, Investigative Journalism].

**Files modified:** `data/faculty.json`

---

## [2026-05-14 ~00:30 TST] — Fix ftag font size to match ≤960px size at all widths

**Prompt summary:**
> 「> 960px 時，我希望和 ≤ 960px 一樣，是 10.5px」

**Actions taken:**
- Changed `.ftag { font-size }` from `0.7rem` (= 11.2px at 16px base) to `10.5px` (fixed), so tags are consistently 10.5px at all widths above 600px.

**Files modified:** `css/style.css`

---

## [2026-05-14 ~00:45 TST] — Update Introduction body text and pillar labels

**Prompt summary:**
> 「請幫我針對 index.html 的 introduction 作出修改：1. 內文改為 6 段新文字，第二段 'learning by doing' 加粗體 2. 四個標籤改為：Journalism Skill, Independent Thinking & Multicultural Awareness, Global Outlook, Academic Expertise，各附新說明文字」

**Actions taken:**
- Replaced 3 intro-text paragraphs with 6 new paragraphs.
- Added `<strong>'learning by doing'</strong>` in second paragraph.
- Updated all 4 pillar-tag labels and pillar-body descriptions.

**Files modified:** `index.html`

---

## [2026-05-14 ~00:50 TST] — Rename pillar tag to #Critical Thinking

**Prompt summary:**
> 「#Independent Thinking & Multicultural Awareness 幫我改成 #Critical Thinking」

**Actions taken:**
- Changed pillar-btn label from `#Independent Thinking & Multicultural Awareness` to `#Critical Thinking` in `index.html`.

**Files modified:** `index.html`

---

## [2026-05-14 ~01:00 TST] — Add "5 Elective Courses" to intro-stats

**Prompt summary:**
> 「intro-stats 新增一個：5 elective courses」

**Actions taken:**
- Added a new `.stat` block (stat-num: 5, stat-label: Elective Courses) to `.intro-stats` in `index.html`.

**Files modified:** `index.html`

---

## [2026-05-14 ~01:10 TST] — Reduce ftag font-size to 9.5px

**Prompt summary:**
> 「> 600px 時，請幫我改成 9.5px」

**Actions taken:**
- Changed `.ftag { font-size }` from `10.5px` to `9.5px` in `css/style.css`.

**Files modified:** `css/style.css`

---

## [2026-05-14 ~01:20 TST] — Rebuild Curriculum section with track tabs and course lists

**Prompt summary:**
> 「Curriculum 區塊，請幫我先增加一段內文，內文後要有 Professional Track 和 Research Track 兩個區塊按鈕（要易讀美觀），最後還有一個小內文區塊」

**Actions taken:**
- Replaced curriculum-body content in `index.html` with: 2 intro paragraphs, `.track-tabs` with Professional/Research tab buttons and panels, and a `.curriculum-footer-note` link.
- Each track panel contains 3 course groups (Required, Elective Required, Elective Courses) with counts and a numbered notes list.
- Added JS tab switching logic for `.track-tab-btn` / `.track-panel`.
- Rewrote curriculum CSS in `css/style.css`: removed old grid layout, added `.track-tabs`, `.track-tab-bar`, `.track-tab-btn`, `.track-panel`, `.course-group`, `.course-group-label`, `.course-group-note`, `.course-list`, `.track-notes`, `.curriculum-footer-note`.

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-14 ~01:35 TST] — Curriculum and Introduction styling fixes

**Prompt summary:**
> 「1. Curriculum 兩個區塊按鈕顏色和風格改成和 faculty 區塊類似 2. 兩個 track 最後的列點字再大一點 3. For more information 字和內文一樣格式 4. Introduction 下的四個 tag 字小一點」

**Actions taken:**
- Rewrote `.track-tab-btn` / `.track-tab-bar` / `.track-panel` CSS to match faculty tab style: top-rounded borders, active = maroon fill, panel with border.
- `.track-notes li` font-size: `0.8rem` → `0.88rem`.
- `.curriculum-footer-note`: removed fixed font-size, set `color: var(--text-600)` and `line-height: 1.75` to match intro body text.
- `.pillar-btn` font-size: `0.9rem` → `0.78rem`.

**Files modified:** `css/style.css`

---

## [2026-05-14 ~01:45 TST] — Rename Adrian Rauchfleisch tag

**Prompt summary:**
> 「Adrian Rauchfleisch faculty-card 的「Methods for Communication Science」改成「Communication Methods」」

**Actions taken:**
- Updated tag in `data/faculty.json`.

**Files modified:** `data/faculty.json`

---

## [2026-05-14 ~01:55 TST] — Update Ji-Lung Hsieh profile: contacts, journals, conference, awards, services

**Prompt summary:**
> 「針對 ji-lung-hsieh.html 頁面，幫我做出以下修改：1. 電話改成 +886-2-3366-9867 2. 第三個網頁文字改成 C.C. Lab 3. Journals 全部替換（3 items，斜體期刊名）4. Conference 全部替換（3 items，斜體會議名）5. Honors and Awards 全部替換 6. Professional Services 全部替換」

**Actions taken:**
- contacts[0].value: `(02) 3366-9867` → `+886-2-3366-9867`
- contacts[2].text: `C.C.Lab Website` → `C.C. Lab`; externalLinks[0].text: `C.C.Lab` → `C.C. Lab`
- Replaced all 3 Journals items with new formatted entries (journal names in `<em>`).
- Replaced all 3 Conference items with new formatted entries (conference names in `<em>`).
- Honors and Awards: same content, reconfirmed.
- Professional Services: removed comma after "General".

**Files modified:** `data/faculty/ji-lung-hsieh.json`

---

## [2026-05-14 ~02:05 TST] — Update Ji-Lung Hsieh Education: add ", Taiwan" to all three entries

**Prompt summary:**
> 「Education 內文改為：加上 , Taiwan 在 National Chiao-Tung University 後面」

**Actions taken:**
- Added ", Taiwan" after "National Chiao-Tung University" in all 3 Education items.

**Files modified:** `data/faculty/ji-lung-hsieh.json`

---

## [2026-05-14 ~02:15 TST] — Update Lih-Yun Lin profile: education, appointments order, book chapters

**Prompt summary:**
> 「1. Education M.A. 改為 National Cheng-Chi University 2. Professional Appointments 順序顛倒 3. Book Chapters 三處新增共 8 筆條目」

**Actions taken:**
- Education: "National Chengchi University (NCCU)" → "National Cheng-Chi University".
- Professional Appointments: reversed order of all 7 items (most recent first).
- Book Chapters: added 3 items after 2009 Transformation entry; added 2 items after 2004 entry; added 3 items after 2001 Looking back entry.

**Files modified:** `data/faculty/lih-yun-lin.json`

---

## [2026-05-14 ~02:30 TST] — Lih-Yun Lin: add commissioned project, reverse awards, add 8 conference papers

**Prompt summary:**
> 「1. Other Commissioned Research Projects 新增 Weng S.C. (2000) Formosa Incident 項目 2. Honors and Awards 順序顛倒 3. Conference Presentations and Papers 四處新增共 8 筆條目」

**Actions taken:**
- Other Commissioned Research Projects: added 1 new item after "Retrospect and prospect..." entry.
- Honors and Awards: reversed order of all 11 items (most recent first).
- Conference Presentations and Papers: added 3 items after 2017 TAIS; added 2 items after 2015 July Montreal post-authoritarian; added 3 items after 2013 June NATSC; added 2 items after 2012 July IAMCR Durban.

**Files modified:** `data/faculty/lih-yun-lin.json`

---

## [2026-05-14 ~02:40 TST] — Lih-Yun Lin: add 2 conference papers after 2010 IAMCR entry

**Prompt summary:**
> 「Conference Presentations and Papers 新增在 2010 IAMCR Braga 下方：2 筆 2008 年論文」

**Actions taken:**
- Added 2 items after the 2010 IAMCR Braga entry: Lin, L. (2008, January 9) and Lin, L. (2008, May 24–25).

**Files modified:** `data/faculty/lih-yun-lin.json`

---

## [2026-05-14 ~02:50 TST] — Lih-Yun Lin: add 1 conference paper after 2008 IAMCR Stockholm entry

**Prompt summary:**
> 「Conference Presentations and Papers 新增在 2008 IAMCR Stockholm 下方：Lin, L. (2007, April 26–27)」

**Actions taken:**
- Added 1 item after the 2008 IAMCR Stockholm entry.

**Files modified:** `data/faculty/lih-yun-lin.json`

---

## [2026-05-14 ~03:00 TST] — Lih-Yun Lin: append 2 conference papers at end of list

**Prompt summary:**
> 「Conference Presentations and Papers 新增在最後：Lin, L. (2001) 和 Lin, L. (1999)」

**Actions taken:**
- Appended 2 items at the end of Conference Presentations and Papers.

**Files modified:** `data/faculty/lih-yun-lin.json`

---

## [2026-05-14 ~03:10 TST] — Update Chen-Ling Hung profile: phone and education

**Prompt summary:**
> 「1. 電話改成 +886-2-3366-3124 2. Education M.A. 改為 National Cheng-Chi University」

**Actions taken:**
- contacts[0].value: `(02) 3366-3124` → `+886-2-3366-3124`
- Education M.A. item: `National Chengchi University` → `National Cheng-Chi University`

**Files modified:** `data/faculty/chen-ling-hung.json`

---

## [2026-05-14 ~03:20 TST] — Update Hui-Ju Tsai profile: phone and experiences

**Prompt summary:**
> 「1. 電話改成 +886-2-3366-3121 2. Experiences Associate Professor 日期改為 2024.8–present，下方新增 Assistant Professor NTU (2022.8–2024.7)」

**Actions taken:**
- contacts[0].value: `(02) 3366-3121` → `+886-2-3366-3121`
- Experiences: updated Associate Professor date to `2024.8–present`; inserted new item "Assistant Professor, Graduate Institute of Journalism, National Taiwan University (2022.8–2024.7)" below it.

**Files modified:** `data/faculty/hui-ju-tsai.json`

---

## [2026-05-14 ~03:30 TST] — Update I-I Chan profile: education and honors

**Prompt summary:**
> 「1. Education B.A. 加上 , Taiwan 2. Honors and Awards 刪除內容，新增 7 筆詳細獎項」

**Actions taken:**
- Education: added ", Taiwan" after "National Taiwan University".
- Honors and Awards: replaced 6 existing items with 7 new detailed entries.

**Files modified:** `data/faculty/i-i-chan.json`

---

## [2026-05-14 ~03:40 TST] — Update Lokman Tsui profile: education, language, publications, remove research interests

**Prompt summary:**
> 「1. 刪除 Research Interests 區塊 2. Education 加上國家 3. Language 句號換行 4. 刪除 Journal Articles and Other Publications 全部內文，新增 10 筆」

**Actions taken:**
- Education: added country names (USA, UK, Netherlands) to all 5 items.
- Language content: added `<br>` between sentences for line breaks.
- Journal Articles and Other Publications: replaced all 26 items with 10 new items (journal names in `<em>`).
- sidebar.researchInterests: set to empty array to remove Research Interests block.

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-14 ~03:50 TST] — Lokman Tsui: append 17 older publications to Journal Articles section

**Prompt summary:**
> 「在 Journal Articles and Other Publications 內文新增：[17 items from 2002–2018]」

**Actions taken:**
- Appended 17 items after the existing 10 entries, covering 2002–2018 publications.

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-14 ~04:00 TST] — Lokman Tsui: replace Academic Conferences content with 15 detailed entries

**Prompt summary:**
> 「刪除 Academic Conferences and Workshops 所有內文，並新增：[15 items]」

**Actions taken:**
- Replaced all 15 existing items with 15 new detailed entries including paper titles and full conference information.

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-14 ~04:10 TST] — Lokman Tsui: replace Presentations for Civil Society content with 25 detailed entries

**Prompt summary:**
> 「刪除 Presentations for Civil Society, Government and Others 所有內文，並新增：[25 items]」

**Actions taken:**
- Replaced all 25 existing items with 25 new detailed entries including full titles and event information.

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-14 ~04:20 TST] — Lokman Tsui: expand Awards and Honors descriptions

**Prompt summary:**
> 「刪除 Awards and Honors 所有內文，並新增：3 筆含完整描述的獎項」

**Actions taken:**
- Updated all 3 Awards and Honors items with fuller descriptions (prize subtitle and host institution).

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-14 ~04:30 TST] — Lokman Tsui: replace Service (Selected) with 7 detailed entries

**Prompt summary:**
> 「刪除 Service (Selected) 所有內文，並新增：[7 items with full descriptions]」

**Actions taken:**
- Replaced 6 existing items with 7 new detailed entries; journal names in `<em>`.

**Files modified:** `data/faculty/lokman-tsui.json`

---

## [2026-05-18 ~10:00 TST] — Restructure gallery to top-level between header and site-layout

**Prompt summary:**
> 「[image] 請先幫我修改 index.html，關於banner和hero，我希望放在同一個區塊，如圖所示」

**Actions taken:**
- Moved `<section id="gallery">` from inside `<main class="site-main">` to between `</header>` and `<div class="site-layout">`, making it a full-width top-level block.
- Updated `#gallery` CSS in `css/style.css`: removed `width: 100vw; left: 50%; transform: translateX(-50%)` (no longer needed at top level); changed to `width: 100%; position: relative; overflow: hidden;`.

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-18 ~10:30 TST] — Restructure header: two-row with utility strip + inline nav

**Prompt summary:**
> 「不是這樣，我希望可以把原本 banner 的 fb, yt, ntu, 中文網站連結變小，然後放在右上，像圖中 contact us 那邊。Site navigation 併到 bar 內」

**Actions taken:**
- Replaced single-row `.site-header` with two-row structure:
  - `.site-header-topbar` (28px, light bg): FB/YT/NTU small icons + `|` separator + 中文 link, right-aligned
  - `.site-header-main` (64px): brand name on left, inline nav links on right (Introduction, News, Faculty, Visiting Scholars, Curriculum)
- Removed `<nav class="site-sidebar">` from `site-layout`; nav items now live in the header
- Updated JS scroll-spy: `sidebar-nav-link` → `header-nav-link`; `HEADER_H` = 92px; removed unused sidebar sub-nav click handler
- Updated CSS: new `.site-header-topbar`, `.site-header-main`, `.header-nav-list/link` styles; replaced all old `.sidebar-nav-*` rules; updated `min-height` to `calc(100vh - 92px)`
- Added `@media (max-width: 720px) { .site-header-nav { display: none; } }` for mobile

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-18 ~10:45 TST] — Header nav: fix vertical centering; shrink 中文 link font

**Prompt summary:**
> 「1. Introduction · News · Faculty · Visiting Scholars · Curriculum nav 上下置中 bar 2. Top strip 中文 link 字體變小」

**Actions taken:**
- Replaced `border-bottom: 3px solid transparent` on `.header-nav-link` with a `::after` pseudo-element (`position: absolute; bottom: 0; height: 3px`) so the underline indicator doesn't affect box height or shift text off-center; text is now truly vertically centered via `align-items: center`.
- Reduced `.site-header-lang` font-size from `0.72rem` → `0.64rem`.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:00 TST] — Fix header nav still not vertically centered

**Prompt summary:**
> 「Nav 並沒有上下置中呀，現在長這樣 [screenshot]」

**Actions taken:**
- Added `height: 100%` to `.header-nav-list` so it fills `.site-header-nav`'s stretched height.
- Added `.header-nav-list > li { display: flex; align-items: stretch; }` to propagate height through `<li>` elements to the `<a>` flex container, completing the stretch chain.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:10 TST] — Header topbar: same bg as main bar, remove divider

**Prompt summary:**
> 「site-header-topbar 與 site-header-main 顏色一致，不用分隔線」

**Actions taken:**
- Removed `background: #faf9f8` and `border-bottom` from `.site-header-topbar`; both rows now share the same white `#ffffff` background inherited from `.site-header`.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:20 TST] — Topbar: shrink 中文 link; add top padding to topbar

**Prompt summary:**
> 「.site-header-topbar 的中文 link 再小，.site-header-topbar可以離頁面上方遠壹點點」

**Actions taken:**
- Reduced `.site-header-lang` font-size: `0.64rem` → `0.58rem`.
- Added `padding-top: 5px` to `.site-header-topbar` to push it slightly away from the top edge.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:30 TST] — Header: brand spans full height via CSS Grid

**Prompt summary:**
> 「site-header-brand 與 site-header-topbar+nav 等高」

**Actions taken:**
- Changed `.site-header` to `display: grid` with `grid-template-areas: "brand topbar" / "brand nav"` and `grid-template-columns: auto 1fr`, so brand naturally spans both rows.
- Moved `<a class="site-header-brand">` from inside `.site-header-main` to a direct child of `<header>`; promoted `<nav class="site-header-nav">` to direct child; removed `.site-header-main` wrapper entirely.
- Updated CSS: `grid-area` assigned to brand, topbar, nav; removed `.site-header-main` rule; added `padding: 0 2rem 0 1.5rem` on brand.

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-18 ~11:40 TST] — Header nav: right-align links

**Prompt summary:**
> 「nav 靠右對齊」

**Actions taken:**
- Removed `width: 100%` from `.header-nav-list`; the parent `.site-header-nav` already has `justify-content: flex-end`, so the list now floats to the right edge.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:45 TST] — Header: enlarge brand title; nav list margin-right

**Prompt summary:**
> 「1. 品牌名稱 字體放大 2. .header-nav-list margin-right 2px」

**Actions taken:**
- `.site-header-title` font-size: `1rem` → `1.15rem`.
- `.header-nav-list` added `margin-right: 2px`.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:50 TST] — header-nav-list margin-right 2px → 5px

**Prompt summary:**
> 「.header-nav-list margin-right 5px」

**Actions taken:**
- `.header-nav-list` margin-right: `2px` → `5px`.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~11:55 TST] — Header grid: topbar full-width, brand+nav same row

**Prompt summary:**
> 「我希望左右兩個的字，高度可以看起來一致，比較整齊」

**Actions taken:**
- Changed grid-template-areas from `"brand topbar" / "brand nav"` to `"topbar topbar" / "brand nav"`: topbar now spans full width as the first row; brand and nav share the second row, so both are naturally at the same vertical height.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~12:05 TST] — Revert grid; topbar spacing smaller; brand sub font larger + more gap

**Prompt summary:**
> 「NO!!! 改回原本，讓 topbar 和 nav 的間距小一點，品牌名稱的中英文間距加大，且中文字加大」

**Actions taken:**
- Reverted grid-template-areas back to `"brand topbar" / "brand nav"`.
- Reduced `.site-header-topbar` padding: `5px 1.5rem 0` → `3px 1.5rem 1px` to tighten topbar/nav gap.
- `.site-header-sub`: font-size `0.7rem` → `0.82rem`; added `margin-top: 0.4rem` for more spacing from the English title.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~12:10 TST] — Brand subtitle margin-top: 0.4rem → 0.25rem

**Prompt summary:**
> 「中文品牌名margin-top: 0.4rem改為0.25rem」

**Actions taken:**
- `.site-header-sub` margin-top: `0.4rem` → `0.25rem`.

**Files modified:** `css/style.css`

---

## [2026-05-18 ~12:20 TST] — Responsive: shrink brand subtitle font and margin at narrow widths

**Prompt summary:**
> 「請幫我在螢幕寬度縮小時，把中文品牌名的字體和標題間距縮小」

**Actions taken:**
- `@media (max-width: 720px)`: `.site-header-sub` font-size `0.72rem`, margin-top `0.15rem`.
- `@media (max-width: 600px)`: `.site-header-sub` font-size `0.62rem`, margin-top `0.1rem`.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~10:00 TST] — ≤720px: hide topbar and nav, keep only brand

**Prompt summary:**
> 「我希望在 ≤ 720px 時，banner 只保留品牌名稱，其餘 Topbar/Nav 請幫我隱藏」

**Actions taken:**
- Added `.site-header-topbar { display: none; }` to the existing `@media (max-width: 720px)` block.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~10:10 TST] — Gallery always full viewport width

**Prompt summary:**
> 「且 banner 寬度在任何時候，都要符合畫面寬度」

**Actions taken:**
- `#gallery`: `width: 100%` → `width: 100vw` to guarantee full viewport width regardless of parent context.
- `body`: added `overflow-x: hidden` to prevent horizontal scrollbar from `100vw`.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~10:20 TST] — Faculty pages: update header to new grid style

**Prompt summary:**
> 「針對 faculty 的 html，請幫我改成左邊品牌名稱，右邊是那些連結們。當 ≤ 720px 時，banner 只保留品牌名稱」

**Actions taken:**
- Replaced old flex header (`.site-header-icons` + 18px SVGs + separate lang link) with new structure: brand (`grid-area: brand`) + `.site-header-topbar` (14px icons + `|` + 中文) across all 7 faculty HTML files.
- ≤720px hiding of topbar already handled by existing CSS rule.

**Files modified:** `faculty/adrian-rauchfleisch.html`, `faculty/chen-ling-hung.html`, `faculty/hui-ju-tsai.html`, `faculty/i-i-chan.html`, `faculty/ji-lung-hsieh.html`, `faculty/lih-yun-lin.html`, `faculty/lokman-tsui.html`

---

## [2026-05-19 ~10:35 TST] — Add 7 visiting scholars, sorted by year descending

**Prompt summary:**
> 「我要新增 Visiting Scholar，請幫我依據年份排列，越新的越上面 [7 scholars]」

**Actions taken:**
- Replaced placeholder entry in `data/visiting-scholars.json` with 7 scholars sorted newest first: Weronika Jakubczak (2025, Poland), Alexander Haentzschel (2025, Germany), Neal E Robbins (2023, UK), Han-Teng Liao (2019, China), Ji Yang (2017, China), Li-Fen Cheng (2014, Spain), Hui-Ching Chang (2003, USA).

**Files modified:** `data/visiting-scholars.json`

---

## [2026-05-19 ~10:50 TST] — Visiting Scholars: add pagination (5 per page)

**Prompt summary:**
> 「Visiting Scholars 若超過五筆，請幫我像 news 區塊一樣，做下一頁的按鈕」

**Actions taken:**
- Added `#scholars-pagination` bar (reusing `.news-pagination` / `.news-page-btn` styles) below `#scholars-list` in HTML.
- Replaced single-render scholars JS with paginated `renderScholarsPage()` function (5 per page); pagination bar auto-hides when ≤1 page.

**Files modified:** `index.html`

---

## [2026-05-19 ~11:00 TST] — Swap Alexander Haentzschel and Weronika Jakubczak order

**Prompt summary:**
> 「Visiting Scholar 的 Alexander Haentzschel 和 Weronika Jakubczak 順序對調」

**Actions taken:**
- Swapped the two 2025 entries in `data/visiting-scholars.json`; Alexander Haentzschel now first.

**Files modified:** `data/visiting-scholars.json`

---

## [2026-05-19 ~11:10 TST] — Mobile banner height increased

**Prompt summary:**
> 「針對手機版的 banner，我希望高度可以高一點」

**Actions taken:**
- `@media (max-width: 720px)` `.gallery-viewport` height: `300px` → `420px`.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~11:20 TST] — Fix Visiting Scholars column alignment

**Prompt summary:**
> 「這是 visiting scholar，為什麼沒辦法排列整齊？」

**Actions taken:**
- `.scholar-row` `align-items: center` → `align-items: start`: all three columns (name, affiliation, meta) now anchor from the top, so year text always aligns horizontally with the scholar name.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~11:30 TST] — Fix Visiting Scholars middle column misalignment

**Prompt summary:**
> 「我是指中間欄的學校」

**Actions taken:**
- Root cause: each `.scholar-row` is an independent grid; `auto` on the third column sized differently per row (tag widths vary: "NEW MEDIA" vs "EUROPEAN & ASIAN MEDIA"), shifting the `1fr 1fr` columns inconsistently.
- Fix: `grid-template-columns: 1fr 1fr auto` → `1fr 1fr 160px` (fixed third column) so all rows share identical column boundaries.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~11:45 TST] — Visiting Scholars: 4-column layout with header row

**Prompt summary:**
> 「我希望 Visiting Scholars 可以分成四欄，從左到右分別是學者名、大學＋國家名、年份、標籤，並且幫我在最上方新增一列各欄的標題」

**Actions taken:**
- Updated `buildScholarRow` JS: year and tag now in separate `<div>` cells instead of combined `.scholar-meta`.
- Added `.scholars-header-row` in HTML with labels: Scholar / University & Country / Year / Field.
- CSS: `grid-template-columns: 1fr 1.5fr 60px 160px` on both header and rows; `.scholars-list` border-top removed (header provides top border); `.scholars-header-row` styled with uppercase label treatment.
- Mobile (≤720px): header row hidden, scholar-row collapses to 2 columns (name + affiliation), year and tag hidden.

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-19 ~12:00 TST] — Alexander Haentzschel field: European & Asian Media → Media Industry

**Prompt summary:**
> 「Alexander Haentzschel 的 field 改成 Media Industry」

**Actions taken:**
- Updated `area` field in `data/visiting-scholars.json`.

**Files modified:** `data/visiting-scholars.json`

---

## [2026-05-19 ~12:15 TST] — Visiting Scholars: name color, column widths, tag restyling, field rename

**Prompt summary:**
> 「1. 學者名用酒紅色（中文維持灰色小字）2. University & Country 區塊寬度縮小，多的長度給 Field 3. Cross-cultural communication 改為 Intercultural Communication 4. Field 文字縮小，標籤顏色可以像 news 那樣多樣」

**Actions taken:**
- `.scholar-name` color: `var(--text-900)` → `var(--maroon)`.
- Grid columns: `1fr 1.5fr 60px 160px` → `1fr 1.1fr 60px 185px`.
- JSON: "Cross-cultural Communication" → "Intercultural Communication" for Li-Fen Cheng and Hui-Ching Chang.
- JS `buildScholarRow`: added `FIELD_CLASS` map → `sfield-*` CSS class on tag.
- `.scholar-area` font-size: `0.72rem` → `0.62rem`; solid background (solid maroon default); color variants: sfield-tech (teal), sfield-security (green), sfield-industry (purple), sfield-culture (gold/amber), sfield-regional (maroon).

**Files modified:** `index.html`, `css/style.css`, `data/visiting-scholars.json`

---

## [2026-05-19 ~12:30 TST] — Add Visiting Scholar: Sunny Yoon

**Prompt summary:**
> 「新增 Visiting Scholars: Scholar：Sunny Yoon, University：Hanyang University, Country：Korea, Year：2019, Area：Cultural Studies」

**Actions taken:**
- Added Sunny Yoon entry to `data/visiting-scholars.json` after Han-Teng Liao (both 2019), before Ji Yang (2017).

**Files modified:** `data/visiting-scholars.json`

---

## [2026-05-19 ~12:35 TST] — Add Cultural Studies tag color

**Actions taken:**
- Added `'Cultural Studies': 'sfield-creative'` to `FIELD_CLASS` map in `index.html`.
- Added `.scholar-area.sfield-creative { background: #7a4e1a; }` to `css/style.css` (warm brown).

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-19 ~12:45 TST] — Visiting Scholars: revert name color and tag colors

**Prompt summary:**
> 「1. University & Country 區塊寬度再縮小，多的長度給 Field 2. 學者名改回原本深灰色，Field 標籤改回原本統一酒紅色」

**Actions taken:**
- Grid columns: `1fr 1.1fr 60px 185px` → `1fr 0.8fr 60px 220px` (University & Country narrowed, Field widened).
- `.scholar-name` color: `var(--maroon)` → `var(--text-900)` (dark gray).
- Removed all `sfield-*` color variant rules; all tags now use the base `.scholar-area` maroon background.

**Files modified:** `css/style.css`

---

## [2026-05-19 ~12:50 TST] — Visiting Scholars: field tag to light maroon

**Prompt summary:**
> 「field tags 的填色要淺淺酒紅色」

**Actions taken:**
- `.scholar-area` background: `var(--maroon)` → `#f3e6e6`; color: `#fff` → `var(--maroon)` (light maroon fill, maroon text).

**Files modified:** `css/style.css`

---

## [2026-05-20 ~TST] — Visiting Scholars: narrow Scholar name column, widen University & Country

**Prompt summary:**
> 「Visiting Scholars 區塊，Scholar name 區塊太寬，寬度增加在University & Country區塊」

**Actions taken:**
- Grid columns: `1fr 0.8fr 60px 220px` → `0.7fr 1.1fr 60px 220px`.

**Files modified:** `css/style.css`

---

## [2026-05-20 ~10:15 TST] — Pillar tags → static cards; field tag color fix

**Prompt summary:**
> 「在index.html 中，請幫我把 pillar-tag 改成小卡的形式，沒有點選功能，所有文字放在小卡當中」

**Actions taken:**
- HTML: replaced `<button class="pillar-btn">` / `<div class="pillar-body" hidden>` with static `<div class="pillar-card-title">` / `<div class="pillar-card-body">` inside each `.pillar-tag`.
- Removed the JS pillar toggle block (`document.querySelectorAll('.pillar-btn')`).
- CSS: removed `.pillar-btn`, `.pillar-btn:hover`, `.pillar-btn[aria-expanded]`, `.pillar-body` rules; replaced with card styles: `.pillar-tag` (white bg, top maroon border 3px, shadow, flex-column), `.pillar-card-title` (maroon, 0.82rem bold), `.pillar-card-body` (text-600, 0.84rem).
- Removed redundant `.scholar-area.sfield-default` rule (base `.scholar-area` already sets `#f3e6e6` bg and `var(--maroon)` text).

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-20 ~10:40 TST] — Pillar cards: add illustrations (image + text layout)

**Prompt summary:**
> 「在 image 資料夾中有四張插圖，分別為Journalism-Skill, Critical-Thinking, Global-Outlook, Academic-Expertise，我想要將 pillar-tag 改為有圖加文字，請幫我設計與改動」

**Actions taken:**
- HTML: added `<img class="pillar-card-img">` at the top of each `.pillar-tag`, wrapped text in `<div class="pillar-card-text">`.
  - Images: `image/Journalism-Skill.jpg`, `image/Critical-Thinking.jpg`, `image/Global-Outlook.jpg`, `image/Academic-Expertise.jpg`
- CSS:
  - `.pillar-tag`: removed `border-top` and `padding`; added `overflow: hidden` so image clips to card radius.
  - `.pillar-card-img`: `width: 100%; height: 175px; object-fit: cover; object-position: center top`.
  - `.pillar-card-text`: `padding: 0.9rem 1.1rem 1.1rem; border-top: 3px solid var(--maroon)` (accent line between image and text).

**Files modified:** `index.html`, `css/style.css`

---

## [2026-05-20 ~11:00 TST] — Faculty pages: add nav to site-header

**Prompt summary:**
> 「幫我把所有 faculty 的 site-header 改成和 index.html 一樣」

**Actions taken:**
- All 7 faculty HTML files previously had brand + topbar only (no nav).
- Used Python batch script to insert `<nav class="site-header-nav">` block before `</header>` in each file.
- Nav links use `../index.html#section` paths (subdirectory prefix) for correct routing from faculty/.
- No `data-section` attribute on links (scroll-spy only runs on index.html).

**Files modified:** `faculty/adrian-rauchfleisch.html`, `faculty/chen-ling-hung.html`, `faculty/hui-ju-tsai.html`, `faculty/i-i-chan.html`, `faculty/ji-lung-hsieh.html`, `faculty/lih-yun-lin.html`, `faculty/lokman-tsui.html`

---

## [2026-05-20 ~11:10 TST] — 中文連結改為 journalism.ntu.edu.tw

**Prompt summary:**
> 「幫我把所有介面的中文按鈕，連結改為：http://www.journalism.ntu.edu.tw」

**Actions taken:**
- Replaced `https://ntujour.github.io/` → `http://www.journalism.ntu.edu.tw` in all 8 files (index.html + 7 faculty/*.html).

**Files modified:** `index.html`, all 7 `faculty/*.html`

---

## [2026-05-20 ~11:20 TST] — 新增 news：2026 Asian Journalism Forum

**Prompt summary:**
> 「我要更新一篇news，Title: Graduate Institute of Journalism Co-hosts 2026 Asian Journalism Forum / Body: We are proud to co-host... / tag: forum」

**Actions taken:**
- Added new entry at top of `data/news.json` (date: 2026-05-20, tag: Forum).

**Files modified:** `data/news.json`

---

## [2026-05-20 ~11:30 TST] — 兩篇 news tag 改為 Lecture；新增 Lecture tag 樣式

**Prompt summary:**
> 「幫我把 Stephan Somogyi... 和 Visiting scholar Alexander Haentzschel... 兩篇 news 的 tag 改為 lecture」

**Actions taken:**
- `data/news.json`: 兩筆 `"tag": "Forum"` → `"tag": "Lecture"`。
- `index.html` TAG_CLASS map 新增 `Lecture: 'tag-lecture'`。
- `css/style.css` 新增 `.news-tag.tag-lecture { background: #1a6b7a; }`（青藍色）。

**Files modified:** `data/news.json`, `index.html`, `css/style.css`

---

<!-- Template for future entries:

## [YYYY-MM-DD HH:MM TST] — Short title

**Prompt summary:**
> 「...」

**Actions taken:**
- ...

**Files modified/created:** ...

-->
