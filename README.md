# 國立臺灣大學新聞研究所網站

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Last Updated](https://img.shields.io/badge/updated-2025--11--09-blue)]()

## 🎯 Overview

Modern, responsive academic website built with **Tailwind CSS**, **vanilla JavaScript**, and a powerful **template system** + **integrated CMS** for easy maintenance.

**Key Features**:
- ✨ Template-based architecture (centralized banner, navigation, footer)
- 📝 **Decap CMS** (Git-based) for Banner, navigation, news/activities, faculty via `/admin/`
- 📊 JSON data-driven content; `_data/` for bilingual Banner/settings; `news/_posts`, `activities/_posts`, `faculty/_profiles` (Markdown) → `data/*.json` at build
- 🚀 **Decap + Netlify + GitHub Pages**: push or CMS publish → Netlify build → deploy
- ♿ Accessibility features (skip links, ARIA labels)
- 📱 Fully responsive design
- 🎨 Clean, professional styling

**Website**: [https://journalism-ntu.github.io](https://journalism-ntu.github.io)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js 14+ and npm

### Setup

```bash
# 1. Clone repository
git clone https://github.com/journalism-ntu/journalism-ntu.github.io.git
cd journalism-ntu.github.io

# 2. Install dependencies
npm install

# 3. Setup Git hooks (auto-build templates)
bash scripts/setup-git-hooks.sh

# 4. Build everything
npm run build
```

### Content Management (CMS)

Content is managed via **Decap CMS** (Git-based):

- **URL**: `https://your-site.netlify.app/admin/` (after Netlify + Identity setup)
- **Managed**: Banner (`_data/banner.json`), navigation, site settings; news/activities/faculty (Markdown in `_posts`/`_profiles`)
- **Login**: Netlify Identity
- **Deploy**: Single path — Decap + Netlify + GitHub Pages. See [docs/DEPLOY_DECAP_NETLIFY.md](docs/DEPLOY_DECAP_NETLIFY.md), [ARCHITECTURE.md](ARCHITECTURE.md), [CLAUDE.md](CLAUDE.md).

### Development Workflow

**One-command local dev (recommended)**:

```bash
# Start: generate JSON from .md → build templates → run Netlify Dev (opens browser at http://localhost:8888)
./start.sh

# When done: press Ctrl+C in the terminal, then run stop.sh to write all updates to static files
./stop.sh
# Then: git add / commit
```

`start.sh` runs: `pip install -r requirements.txt` → `generate-news-json.py` → `generate-activities-json.py` → `generate-faculty-json.py` → `build-templates.py` → `netlify dev`.  
`stop.sh` runs the same generate + build step so `data/*.json` and built HTML are up to date from current `news/_posts`, `activities/_posts`, and `faculty/_profiles` (`.md`). Requires [Netlify CLI](https://docs.netlify.com/cli/get-started/): `npm install -g netlify-cli`.

**Other commands**:

```bash
# Build templates + CSS
npm run build

# Development mode (build + watch CSS)
npm run dev

# Validate HTML
npm test

# Build only templates
npm run build:templates

# Build only CSS
npm run build:css
```

---

## 📁 Project Structure

```
journalism-ntu.github.io/
├── 📄 Main Pages
│   ├── index.html                 # Homepage
│   ├── news.html                  # News listing
│   ├── activities.html            # Activities listing
│   ├── resources.html             # Resources
│   ├── staff.html                 # Staff directory
│   └── 404.html                   # Error page
│
├── 🎨 Assets
│   ├── css/
│   │   ├── tailwind.css          # Compiled Tailwind CSS
│   │   ├── site-common.css       # Custom site styles
│   │   └── input.css             # Tailwind source
│   ├── js/                       # JavaScript (homepage, news, faculty, banner, etc.)
│   └── images/                   # Images (53MB)
│
├── 📊 Data
│   └── data/
│       ├── faculty_data.json     # From faculty/_profiles/*.md (build)
│       ├── news.json             # From news/_posts/*.md (build)
│       ├── activities.json       # From activities/_posts/*.md (build)
│       ├── faculty-mapping.csv   # Photo mapping reference
│       └── backups/              # Auto-backups
│
├── 📑 Content Directories
│   ├── faculty/                  # Faculty pages
│   ├── admissions/               # Admissions info
│   ├── students/                 # Student resources
│   ├── publications/             # Publications
│   └── about/                    # About pages
│
├── 🔧 Build System
│   ├── templates/                # Reusable templates
│   │   ├── site-banner.html
│   │   ├── site-nav.html
│   │   ├── site-sitemap.html
│   │   └── site-footer.html
│   ├── build-templates.py        # Template builder
│   ├── convert-and-build.py      # Convert & build utility
│   └── package.json              # Build scripts
│
├── 📝 CMS & Data
│   ├── admin/
│   │   ├── index.html            # Decap CMS entry
│   │   └── config.yml            # CMS config (Banner, navigation, etc.)
│   ├── _data/                    # Banner, navigation, site settings (JSON)
│   └── scripts/data/             # generate-*-json.py (build from _posts/_profiles)
│
├── 🛠️ Scripts
│   └── scripts/
│       ├── data/                 # generate-news-json, generate-activities-json, generate-faculty-json
│       ├── validate-html.py      # HTML validator
│       └── setup-git-hooks.sh   # Optional: auto-build on commit
│
├── 📚 Documentation
│   ├── README.md                 # This file
│   ├── CLAUDE.md                 # AI copilot guide
│   ├── IMPROVEMENTS.md           # Change log
│   ├── DATA_SOURCES.md           # Data documentation
│   └── archive/README.md         # Archive documentation
│
└── 📦 Archive
    └── archive/                  # Legacy files (~210MB)
```

---

## 🎨 Design System

### Color Palette
- **Primary**: `#671919` (Burgundy)
- **Accent**: `#efa22a` (Gold)
- **Dark**: `#3e0f0f` (Dark Brown)
- **Background**: `#f5f5f5` (Light Gray)

### Typography
- **Font Size**: 15px base
- **Line Height**: 1.6
- **Headings**: Bold, various sizes

### Spacing
- **Consistent**: `py-4` for vertical padding
- **Container**: Max-width 1200px, centered

---

## 🔨 Template System

### How It Works

1. **Edit templates** in `templates/` directory:
   ```html
   templates/site-nav.html    # Navigation bar
   templates/site-banner.html # Header banner
   templates/site-footer.html # Footer
   ```

2. **HTML files use placeholders**:
   ```html
   {{site-banner}}
   {{site-nav}}
   <!-- Your content -->
   {{site-sitemap}}
   {{site-footer}}
   ```

3. **Build replaces placeholders**:
   ```bash
   npm run build:templates
   # or
   python3 build-templates.py
   ```

4. **Path handling automatic**: Script calculates `../` prefixes based on file location

### Benefits
- ✅ Update navigation once, applies to all pages
- ✅ Consistent layout across site
- ✅ Easy maintenance
- ✅ No code duplication

---

## 📊 Data Management

### Faculty Data

**Primary Source**: `faculty_data.json`

Structure:
```json
{
  "fulltime": [...],
  "parttime": [...],
  "practical": [...],
  "honorary": [...],
  "joint": [...]
}
```

**Photo Naming**: `images/faculty/{englishID}.{jpg|png}`

Example: `images/faculty/jerryhsieh.png`

### News & Activities

**Source**: `data/content.csv`

Columns: `id, type, title, date, category, time, location, content, slug, originalFile, image`

**Used by**: `js/homepage.js` (loads top 3 of each)

---

## 🛠️ Common Tasks

### Update Navigation

```bash
# 1. Edit template
vim templates/site-nav.html

# 2. Build
npm run build:templates
```

### Add New Faculty Member

```bash
# 1. Add photo
cp photo.jpg images/faculty/newperson.jpg

# 2. Edit data
vim faculty_data.json
# Add entry with matching ID

# 3. Verify
# Open faculty/faculty.html in browser
```

### Update News/Activities

```bash
# Edit CSV
vim data/content.csv

# Homepage auto-loads from CSV (no build needed)
```

### Validate Everything

```bash
npm test
# Checks:
# - Template placeholders replaced
# - DOCTYPE, meta tags present
# - No broken internal links
# - Images have alt text
```

---

## 🧪 Testing & Quality

### HTML Validation

```bash
npm test
# or
python3 scripts/validate-html.py
```

Checks:
- ✅ Template placeholders replaced
- ✅ Proper DOCTYPE
- ✅ Required meta tags
- ✅ No unclosed tags
- ✅ Images have alt attributes
- ✅ No broken internal links

### Link Checking

Automatically included in `npm test`

### Accessibility

Features implemented:
- Skip-to-content link (keyboard accessible)
- ARIA roles on major sections
- Semantic HTML5 elements
- Alt text on images (validated)

Test with:
- Tab navigation
- Screen reader (NVDA, JAWS, VoiceOver)
- Lighthouse audit

---

## 🖼️ Image Optimization

### Optimize All Images

```bash
# Install Pillow if needed
pip install pillow

# Run optimizer
python3 scripts/optimize-images.py
```

Features:
- Compresses JPEG/PNG
- Creates WebP versions
- Reports space savings
- Potential to save 20-30MB

### Manual Optimization

For individual images:
```bash
# JPEG
convert input.jpg -quality 85 output.jpg

# PNG
optipng -o7 image.png

# WebP
cwebp -q 85 input.jpg -o output.webp
```

---

## 📝 Content Management

### Adding a Page

1. **Copy template**:
   ```bash
   cp templates/example-page.html new-page.html
   ```

2. **Edit content** (keep template placeholders)

3. **Build**:
   ```bash
   npm run build:templates
   ```

4. **Add to navigation** (edit `templates/site-nav.html`)

### Removing a Page

1. Delete HTML file
2. Remove from navigation
3. Update sitemap.xml
4. Rebuild templates

---

## 🚢 Deployment

### GitHub Pages (Current)

Automatically deploys `main` branch to:
```
https://journalism-ntu.github.io
```

### Manual Deployment

1. **Build everything**:
   ```bash
   npm run build
   ```

2. **Test locally**: Open `index.html` in browser

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```

4. **Wait 1-2 minutes** for GitHub Pages to update

---

## 🐛 Troubleshooting

### Templates not replacing

**Problem**: See `{{site-banner}}` in browser

**Solution**:
```bash
# Manual build
python3 build-templates.py

# Check for errors in output
```

### CSS not updating

**Problem**: Changes to Tailwind not showing

**Solution**:
```bash
# Rebuild CSS
npm run build:css

# Hard refresh browser (Cmd+Shift+R / Ctrl+F5)
```

### Homepage shows mock data

**Problem**: Old hardcoded news/activities

**Solution**: Already fixed in 2025-11-08 update. Ensure using latest `js/homepage.js`

### Links broken

**Problem**: Relative paths incorrect

**Solution**:
```bash
# Run link checker
npm test

# Check console for "Broken link" messages
```

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| `README.md` | This file - Quick start and overview |
| `CLAUDE.md` | Comprehensive guide for AI assistants |
| `IMPROVEMENTS.md` | Complete change log (2025-11-08) |
| `DATA_SOURCES.md` | Data file documentation |
| `templates/README.md` | Template system guide |
| `python-scripts/README.md` | Script categorization |
| `archive/README.md` | Archived files explanation |

---

## 🤝 Contributing

### Development Setup

1. Fork repository
2. Create feature branch
3. Make changes
4. Test thoroughly (`npm test`)
5. Commit with clear messages
6. Push and create pull request

### Commit Messages

Use conventional commits:
```
feat: Add new faculty page
fix: Correct photo paths
docs: Update README
style: Fix CSS formatting
refactor: Reorganize JavaScript
test: Add validation checks
```

### Pre-commit Hooks

Auto-installed via `scripts/setup-git-hooks.sh`

Automatically:
- Builds templates
- Adds modified HTML files
- Prevents broken builds

---

## 📞 Support

### Questions?

1. Check `CLAUDE.md` for detailed information
2. Review `IMPROVEMENTS.md` for recent changes
3. Run `npm test` to diagnose issues
4. Check browser console for JavaScript errors

### Contact

- **Email**: jour@ntu.edu.tw
- **Phone**: (02) 3366-3383
- **Address**: 106台北市大安區羅斯福路四段1號

---

## 📜 License

© 2025 國立臺灣大學新聞研究所 版權所有

---

## 🎉 Recent Updates (2025-11-08)

Major improvements implemented:
- ✅ Build automation (npm scripts)
- ✅ Pre-commit hooks
- ✅ HTML validation tools
- ✅ Image optimization script
- ✅ 404 page and sitemap.xml
- ✅ Accessibility improvements
- ✅ Legacy code cleanup (32 files archived)
- ✅ Data consolidation
- ✅ Homepage real data integration
- ✅ Comprehensive documentation

See `IMPROVEMENTS.md` for complete details.

**Project Health**: 8.5/10 (up from 6.7/10)

---

**Last Updated**: 2025-11-08
**Version**: 2.1.0
**Maintained By**: NTU Journalism Team
