# Netlify confirmation checklist

After you **push** this repo, confirm the following in the Netlify dashboard.

## 1. Site is connected to the repo

- [ ] Netlify → **Site configuration** → **Build & deploy** → **Build settings**
- [ ] **Repository** shows the correct GitHub repo (e.g. `jirlong/ntujour-web` or `journalism-ntu/journalism-ntu.github.io`)
- [ ] **Branch to deploy**: `main` (or your production branch)

## 2. Build command and publish dir come from `netlify.toml`

- [ ] **Build command**: should match `netlify.toml` (or leave empty so Netlify uses the file):
  - `pip install -q -r requirements.txt && python3 scripts/data/generate-news-json.py && python3 scripts/data/generate-activities-json.py && python3 scripts/data/generate-faculty-json.py && python3 build-templates.py`
- [ ] **Publish directory**: `.` (root)
- [ ] **Base directory**: leave empty unless you use a subdirectory

## 3. Identity + Git Gateway are enabled for Decap CMS

- [ ] Netlify → **Site configuration** → **Identity**
  - [ ] **Enable Identity** is on
- [ ] **Registration preferences**: Invite only (recommended)
- [ ] **Services** → **Git Gateway**: **Enable Git Gateway**
- [ ] **Identity** → **Invite users**: at least one admin invited and accepted

## 4. After first deploy

- [ ] Build log shows no errors (Python scripts and `build-templates.py` run successfully)
- [ ] Visit `https://<your-site>.netlify.app` — site loads
- [ ] Visit `https://<your-site>.netlify.app/admin/` — Decap CMS loads; log in with Netlify Identity

---

**Push command** (when ready):

```bash
git push origin main
```

Then open your Netlify dashboard and run through this checklist.
