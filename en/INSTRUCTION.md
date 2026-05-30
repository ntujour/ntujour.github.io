# Graduate Institute of Journalism, NTU — English Website
## Project Instruction Manual

---

## ⚠️ Logging Rule

**Every time a prompt is used to revise the code, the date, time (Taiwan Standard Time, UTC+8), and a brief description of the change MUST be recorded in `LOG.md`.** This applies to all AI-assisted edits, whether via Claude Code or any other tool.

---

## 1. Project Overview

This is the official **English-language one-page website** for the Graduate Institute of Journalism, National Taiwan University (臺大新聞所).

- **Reference site (Chinese):** https://ntujour.github.io/
- **English content source:** https://webpageprodvm.ntu.edu.tw/Journalism/Default.aspx
- **Design:** Visual identity (colors, banner, nav) mirrors the Chinese site exactly.
- **Deployment target:** GitHub Pages (`ntujour-en.github.io`)

---

## 2. File Structure

```
/
├── index.html              ← Main one-page site (Introduction, News, Faculty)
├── css/
│   └── style.css           ← All styles; single stylesheet for the entire site
├── faculty/
│   ├── ji-lung-hsieh.html      謝吉隆 — Associate Professor & Director
│   ├── lih-yun-lin.html        林麗雲 — Professor
│   ├── chen-ling-hung.html     洪貞玲 — Professor
│   ├── adrian-rauchfleisch.html — Professor
│   ├── hui-ju-tsai.html        蔡蕙如 — Associate Professor
│   ├── i-i-chan.html           詹怡宜 — Associate Professor
│   └── lokman-tsui.html        徐洛文 — Assistant Professor
├── INSTRUCTION.md          ← This file
└── LOG.md                  ← Change log (date + time + description of each revision)
```

No build tools, bundlers, or frameworks are used. The site is plain HTML + CSS.

---

## 3. Design System

### 3.1 Color Palette

All colors are defined as CSS custom properties in `css/style.css (:root)`.
They are matched exactly to the Chinese reference site (`ntujour.github.io`).

| Variable | Hex | Usage |
|---|---|---|
| `--maroon` | `#671919` | Navigation bar background, primary links, section titles |
| `--maroon-dark` | `#3e0f0f` | Footer background, profile header gradient start |
| `--maroon-hover` | `#991b1b` | Hover states, gradient end |
| `--gold` | `#efa22a` | Accent: active nav text, section title underline, bullet markers, faculty label |
| `--gold-light` | `#f4bb5a` | Lighter gold for tints |
| `--banner-bg` | `#f5f5f5` | Site banner background |
| `--text-900` | `#1f2937` | Banner title, body text |
| `--text-700` | `#374151` | Banner subtitle |
| `--text-600` | `#4b5563` | Tagline, secondary text |
| `--text-500` | `#6b7280` | Muted/meta text, pillar body |
| `--bg` | `#ffffff` | Main background |
| `--bg-alt` | `#f9fafb` | Alternate section background |
| `--border` | `#e5e7eb` | Card borders, dividers |

### 3.2 Typography

- **Body / headings:** `Georgia, 'Times New Roman', serif`
- **UI elements (nav, tags, labels, captions):** `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- No external font libraries are loaded.

### 3.3 Layout

- Maximum content width: **1200px** (`.container-1200`)
- Sections use `padding: 5rem 1rem` (collapses on mobile)
- Faculty grid: `repeat(auto-fill, minmax(260px, 1fr))`
- Responsive breakpoints: 960px, 720px, 480px

### 3.4 Banner & Navigation (mirrors ntujour.github.io exactly)

**Banner** (`.site-banner`):
- Background color: `#f5f5f5`
- Background images (decorative): `hd-bg-lt.png` and `hd-bg-rt.png`, referenced cross-origin from `https://ntujour.github.io/images/`
- Title: large (2.25rem), bold, dark gray text
- Sub-line: Chinese name `國立臺灣大學新聞研究所`
- Tagline: English description

**Navigation** (`.site-nav`):
- Background: `#671919` (maroon), sticky (top: 0)
- Nav link text: white; hover/active: `#efa22a` (gold)
- Language switcher `中文` is right-aligned in the nav bar
- Box shadow: `0 4px 6px rgba(0,0,0,0.15)`

---

## 4. Page Structure: `index.html`

The main page has four visible sections:

| Section ID | Content |
|---|---|
| `#introduction` | Institute history, mission, four pillars, stats |
| `#news` | 5 recent news/event cards with tags, dates, and external links |
| `#faculty` | Grid of 7 full-time faculty cards linking to individual pages |

A **Hero** banner (maroon gradient) appears between the site-nav and the Introduction section. It can be removed without breaking layout.

**Scroll-spy** is implemented with vanilla JavaScript: the active nav link updates based on scroll position.

---

## 5. Faculty Profile Pages (`faculty/*.html`)

Each profile page shares the same banner, nav, and footer as `index.html`.

Structure per page:
1. **Breadcrumb** — Home / Faculty / Name
2. **Profile header** — maroon gradient with photo, name, title, contact
3. **Profile body** — two-column grid:
   - Left (main): Education, Research Areas, Courses, Publications
   - Right (sidebar, sticky): Research keywords pills, Contact, External links
4. **Footer** — same as main page

### Faculty photo URLs (NTU server)

| Faculty | Photo URL |
|---|---|
| Ji-Lung Hsieh | `https://webpageprod-ws.ntu.edu.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzY2L2NrZmlsZS82ZTNjOWJiMC00ZTFlLTQxZWUtOWUyYi03OGJlNGU5ODI1NTAucG5n` |
| Lih-Yun Lin | No URL available — shows character placeholder `林` |
| Chen-Ling Hung | `https://webpageprod-ws.ntu.edu.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzY2L2NrZmlsZS81MjM0YTlkYy0xYjMyLTQ1YTktODY4ZC1jZjlmMDNlY2Y3NWMuanBn&n=aHVuZy5qcGc%3d` |
| Adrian Rauchfleisch | `https://webpageprod-ws.ntu.edu.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzY2L2NrZmlsZS81Yjg5MDZmZi0yZjA2LTQxMjUtOTRhMS0xZDg5NTZiYTUzMDUucG5n&n=QWRSYTIwMTgucG5n` |
| Hui-Ju Tsai | `https://webpageprod-ws.ntu.edu.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzY2L2NrZmlsZS9kOGY1NTdhOC1kYjM3LTQyMjAtOWY5Yy1hYjkzMThhZjQ4OWUuanBn&n=SU1HXzAzMzdfMi5qcGc%3d` |
| I-I Chan | No URL available — shows character placeholder `詹` |
| Lokman Tsui | `https://webpageprod-ws.ntu.edu.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzY2L2NrZmlsZS9kYmZkZWFkNS1iZTU5LTRlZDItYjZmOC02ZjZiNmYzMzEyMGYuanBn&n=bG9rbWFuLWZpdmV3YXlzLmpwZw%3d%3d` |

Photos use `onerror` fallback to a CSS character placeholder if the NTU server is unreachable.

---

## 6. How to Update Content

### Add a news item
In `index.html`, find the `<div class="news-list">` block and add a new `.news-card` anchor element following the existing pattern. Available tag classes: (none = admissions default maroon), `tag-event` (green), `tag-award` (gold), `tag-forum` (purple).

### Update a faculty profile
Edit the corresponding `faculty/[name].html` file. The contact details, education list, and research section are plain HTML — no templating engine is involved.

### Add a new faculty page
1. Copy an existing `faculty/*.html` as a template.
2. Update all content sections.
3. Add a new `.faculty-card` in the `#faculty` section of `index.html`.

### Change colors
Edit the CSS custom properties in the `:root` block at the top of `css/style.css`. Do **not** hardcode color values elsewhere.

### Update the banner background images
The decorative images (`hd-bg-lt.png`, `hd-bg-rt.png`) are currently loaded cross-origin from `ntujour.github.io`. If that becomes unreliable, download the images and host them locally under `images/`, then update the URL in `.site-banner` in `style.css`.

---

## 7. Deployment

The site is designed for **GitHub Pages** deployment from the `main` branch root or a `/docs` folder.

No build step is required — push the files and Pages will serve them directly.

Suggested repo: `ntujour-en.github.io` → served at `https://ntujour-en.github.io/`

---

## 8. External Dependencies

| Resource | URL | Purpose |
|---|---|---|
| Banner bg images | `https://ntujour.github.io/images/hd-bg-*.png` | Decorative header images |
| Faculty photos | `https://webpageprod-ws.ntu.edu.tw/...` | Profile photos (NTU media server) |
| Chinese site | `https://ntujour.github.io/` | Language switch target |
| NTU official (news links) | `https://webpageprodvm.ntu.edu.tw/Journalism/` | News article links |

All external resources fail gracefully (CSS fallbacks for images, `onerror` for photos).
