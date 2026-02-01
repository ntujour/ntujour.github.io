#!/usr/bin/env python3
"""
Convert all activity rows from data/content.csv to activities/_posts/*.md.
Only creates files for activities that don't already have a matching _posts file (by id/slug).
Usage: python3 scripts/data/csv-activities-to-posts.py
"""

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT_CSV = REPO_ROOT / "data" / "content.csv"
POSTS_DIR = REPO_ROOT / "activities" / "_posts"

# Map CSV category to CMS options (講座, 專題, 參訪, 工作坊, 研討會, 其他)
CATEGORY_MAP = {"活動": "其他", "演講": "講座", "": "其他"}


def html_to_markdown(html):
    """Convert simple HTML to markdown (paragraphs, links, line breaks)."""
    if not (html or "").strip():
        return ""
    s = html.strip()
    s = re.sub(r'<a\s+href=["\']([^"\']*)["\'][^>]*>([^<]*)</a>', r'[\2](\1)', s, flags=re.I)
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    def para(m):
        inner = m.group(1)
        inner = re.sub(r'<[^>]+>', '', inner)
        inner = inner.replace('&nbsp;', ' ').strip()
        return '\n\n' + inner + '\n\n' if inner else '\n\n'
    s = re.sub(r'<p[^>]*>\s*([\s\S]*?)\s*</p>', para, s, flags=re.I)
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def slug_from_id(id_):
    return f"activity-{id_}"


def existing_ids():
    """Return set of activity ids already in _posts (from filename slug)."""
    ids = set()
    if not POSTS_DIR.exists():
        return ids
    for p in POSTS_DIR.glob("*.md"):
        stem = p.stem
        if "-activity-" in stem:
            part = stem.split("-activity-", 1)[-1]
            ids.add(part)
    return ids


def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    have = existing_ids()

    with open(CONTENT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if (r.get("type") or "").strip() == "activity"]

    created = 0
    for row in rows:
        id_ = (row.get("id") or "").strip()
        if not id_ or id_ in have:
            continue
        title = (row.get("title") or "").strip()
        date = (row.get("date") or "").strip().replace("/", "-")
        if len(date) == 10:
            date = date + " 00:00"
        cat_raw = (row.get("category") or "").strip()
        category = CATEGORY_MAP.get(cat_raw, "其他") if cat_raw else "其他"
        time_ = (row.get("time") or "").strip()
        location = (row.get("location") or "").strip()
        content = (row.get("content") or "").strip()
        slug = (row.get("slug") or slug_from_id(id_)).strip()
        if not slug.startswith("activity-"):
            slug = slug_from_id(id_)

        body = html_to_markdown(content)
        if not date or len(date) < 10:
            date = "2022-01-01 00:00"

        title_esc = title.replace('"', '\\"')
        # Filename: YYYY-MM-DD-activity-<id>.md (date part only)
        date_part = date[:10] if len(date) >= 10 else "2022-01-01"
        frontmatter = f"""---
title: "{title_esc}"
title_en: ""
date: {date}
category: {category}
time: "{time_}"
location: "{location}"
body_en: ""
featured: false
lang: zh
---
"""
        filename = f"{date_part}-{slug}.md"
        out_path = POSTS_DIR / filename
        out_path.write_text(frontmatter + body, encoding="utf-8")
        created += 1
        have.add(id_)
        print(f"Created {filename}")

    print(f"Created {created} new activity posts.")


if __name__ == "__main__":
    main()
