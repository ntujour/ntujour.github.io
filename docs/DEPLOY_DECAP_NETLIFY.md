# Deploy: Decap CMS + Netlify + GitHub Pages

This project uses **one deployment path** only.

## Flow

1. **Content**: Edit via [Decap CMS](https://decapcms.org/) at `https://your-site.netlify.app/admin/` (Banner, navigation, news, activities, faculty), or edit Markdown in `news/_posts/`, `activities/_posts/`, `faculty/_profiles/` and `_data/*.json` in the repo.
2. **Build**: On push (or CMS publish), Netlify runs:
   - `pip install -r requirements.txt`
   - `scripts/data/generate-news-json.py` → `data/news.json`
   - `scripts/data/generate-activities-json.py` → `data/activities.json`
   - `scripts/data/generate-faculty-json.py` → `data/faculty_data.json`
   - `build-templates.py` (inlines templates into HTML)
3. **Publish**: Netlify serves the built static site.

## What you need

- **Netlify**: Site linked to the GitHub repo; build command and publish dir from `netlify.toml`.
- **Netlify Identity + Git Gateway**: So Decap CMS can commit to GitHub.
- **Repo**: Must include `build-templates.py`, `scripts/`, `templates/` (do **not** put them in `.gitignore`), plus `data/*.json` after build (or let Netlify generate them).

## Removed / obsolete

- **No `data/content.csv`**: News and activities come from `news/_posts/` and `activities/_posts/`; frontend uses `data/news.json` and `data/activities.json` (generated at build).
- **No local CMS server** (`cms.py`): Use Decap CMS only.
- **No `js/csv-parser.js`**: Unused; removed.

See [ARCHITECTURE.md](../ARCHITECTURE.md), [CLAUDE.md](../CLAUDE.md), and [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md) for details.
