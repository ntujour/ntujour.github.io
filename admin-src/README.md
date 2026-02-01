# Admin custom script (Option A)

Source for optional CMS custom script. 目前列表僅依 **admin/config.yml** 的 `summary` 顯示資訊（類別、發佈、更新），無額外 JS 渲染。

## Build

From project root:

```bash
npm run build:admin
```

Output: `admin/cms-custom.js` (minified). **Commit this file** so deploy (GitHub Pages / Netlify) stays unchanged.

## When to rebuild

- After editing `admin-src/cms-custom.js` (table columns, view toggle, date display).
- After adding/removing collections that use the table view (news, activities, faculty).

## Deploy

No change: push as usual. The built `admin/cms-custom.js` is loaded by `admin/index.html` alongside the Decap CMS CDN script.
