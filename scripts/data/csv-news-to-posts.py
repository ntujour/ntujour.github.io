#!/usr/bin/env python3
"""
Convert all news rows from data/content.csv to news/_posts/*.md.
Only creates files for news that don't already have a matching _posts file (by id/slug).
Usage: python3 scripts/data/csv-news-to-posts.py
"""

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONTENT_CSV = REPO_ROOT / "data" / "content.csv"
POSTS_DIR = REPO_ROOT / "news" / "_posts"


def html_to_markdown(html):
    """Convert simple HTML to markdown (paragraphs, links, line breaks)."""
    if not (html or "").strip():
        return ""
    s = html.strip()
    # Links: <a href="url">text</a> -> [text](url)
    s = re.sub(r'<a\s+href=["\']([^"\']*)["\'][^>]*>([^<]*)</a>', r'[\2](\1)', s, flags=re.I)
    # <br>, <br/>
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    # <p>...</p> -> paragraph (strip inner tags first for nested)
    def para(m):
        inner = m.group(1)
        inner = re.sub(r'<[^>]+>', '', inner)
        inner = inner.replace('&nbsp;', ' ').strip()
        return '\n\n' + inner + '\n\n' if inner else '\n\n'
    s = re.sub(r'<p[^>]*>\s*([\s\S]*?)\s*</p>', para, s, flags=re.I)
    # Remaining tags: strip
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    # Normalize whitespace
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def slug_from_id(id_):
    return f"news-{id_}"


def existing_ids():
    """Return set of news ids already in _posts (from filename slug)."""
    ids = set()
    for p in POSTS_DIR.glob("*.md"):
        stem = p.stem  # e.g. 2025-11-04-news-259107
        if "-news-" in stem:
            part = stem.split("-news-", 1)[-1]
            # part might be 259107 or 測試01311124
            ids.add(part)
    return ids


def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    have = existing_ids()

    with open(CONTENT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if (r.get("type") or "").strip() == "news"]

    created = 0
    for row in rows:
        id_ = (row.get("id") or "").strip()
        if not id_ or id_ in have:
            continue
        title = (row.get("title") or "").strip()
        date = (row.get("date") or "").strip().replace("/", "-")
        category = (row.get("category") or "").strip() or "公告"
        content = (row.get("content") or "").strip()
        slug = (row.get("slug") or slug_from_id(id_)).strip()
        if not slug.startswith("news-"):
            slug = slug_from_id(id_)

        body = html_to_markdown(content)
        if not date or len(date) < 10:
            date = "2022-01-01"

        title_esc = title.replace('"', '\\"')
        frontmatter = f"""---
title: "{title_esc}"
title_en: ""
date: {date}
category: {category}
body_en: ""
featured: false
lang: zh
---
"""
        filename = f"{date}-{slug}.md"
        out_path = POSTS_DIR / filename
        out_path.write_text(frontmatter + body, encoding="utf-8")
        created += 1
        have.add(id_)
        print(f"Created {filename}")

    print(f"Created {created} new news posts.")


if __name__ == "__main__":
    main()
