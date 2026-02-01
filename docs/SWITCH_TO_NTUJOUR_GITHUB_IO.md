# Switching to ntujour.github.io (from ntujour-web)

This project’s **remote** is set to the **ntujour** org repo.

## ⚠️ Repo was renamed to ntujour.github.io2

After you pushed, GitHub reported: **"This repository moved. Please use the new location: https://github.com/ntujour/ntujour.github.io2.git"**

- **Where to find the repo:** Under the **ntujour** organization, look for **ntujour.github.io2** (not ntujour.github.io).
- **Direct link:** https://github.com/ntujour/ntujour.github.io2
- Your push succeeded; the code is in that repo. Local `origin` has been updated to point to `ntujour.github.io2`.

(GitHub may have renamed it because `ntujour.github.io` is a special name for a user/org Pages site and there was a conflict, or the org renamed it.)

## What was done

1. **Remote updated**
   - `origin` points to: `https://github.com/ntujour/ntujour.github.io2.git`
   - Future `git push` will go to this repo.

2. **Docs updated**
   - References to `ntujour-web` in docs were changed to `ntujour.github.io` where they refer to the repo.

## You have a previous version on ntujour.github.io

Pushing **main** from this folder will **replace** the current content of the ntujour.github.io repo with this (Decap + Netlify) version.

### Option A: Replace the old site (use this repo as the only source)

1. **(Optional)** Back up the old repo:
   - On GitHub: **ntujour.github.io** → **Settings** → scroll down → **Archive** (or clone it to another folder first).
   - Or clone to a backup folder: `git clone https://github.com/jirlong/ntujour.github.io.git ntujour.github.io-backup`
2. Push this project to ntujour.github.io:
   ```bash
   git push -u origin main
   ```
   If GitHub says “rejected” (e.g. histories don’t match), you can force-push (this overwrites the remote):
   ```bash
   git push -u origin main --force
   ```
   Only use `--force` if you are sure you want to replace the previous version.

### Option B: Keep the old repo and add this as a branch

1. Fetch the current ntujour.github.io:
   ```bash
   git fetch origin
   ```
2. Create a branch from the current remote (e.g. `old-site`) and push this work to a new branch:
   ```bash
   git push origin main:decap-netlify
   ```
3. On GitHub, you can compare branches and later make `decap-netlify` the default branch or merge into main.

## After pushing

- **GitHub Pages**: If the repo is `jirlong/ntujour.github.io` or `<org>/ntujour.github.io`, the site may be served at `https://jirlong.github.io/ntujour.github.io/` or `https://<org>.github.io/ntujour.github.io/` (or custom domain if set).
- **Netlify**: In Netlify, point the site to the **ntujour.github.io** repo (and the branch you push, e.g. `main`). Use [docs/NETLIFY_CONFIRM_CHECKLIST.md](NETLIFY_CONFIRM_CHECKLIST.md) to confirm.

## Check your remote

```bash
git remote -v
```

You should see `origin` → `https://github.com/<owner>/ntujour.github.io.git`.
