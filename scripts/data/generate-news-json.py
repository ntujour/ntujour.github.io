#!/usr/bin/env python3
"""
Generate data/news.json from news/_posts/*.md (frontmatter + markdown body).
Run after editing news in Decap CMS or when adding new _posts so the list page stays in sync.
Usage: python3 scripts/data/generate-news-json.py
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
POSTS_DIR = REPO_ROOT / "news" / "_posts"
OUTPUT_FILE = REPO_ROOT / "data" / "news.json"


def parse_frontmatter(content):
    """Parse YAML-like frontmatter and return (data dict, body string)."""
    if not content.startswith("---"):
        return {}, content
    end = content.index("---", 3)
    head = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")
    data = {}
    for line in head.split("\n"):
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False
        data[key] = value
    return data, body


def markdown_to_html(text):
    """Simple markdown to HTML for body (paragraphs, bold, lists)."""
    if not text.strip():
        return ""
    html_parts = []
    in_list = False
    for block in text.split("\n\n"):
        block = block.strip()
        if not block:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            continue
        # Unordered list: support multiple "- item" lines in one block
        lines = block.split("\n")
        if lines[0].startswith("- ") or re.match(r"^\d+\. ", lines[0]):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            for line in lines:
                line = re.sub(r"^- ", "", line)
                line = re.sub(r"^\d+\. ", "", line)
                if not line.strip():
                    continue
                line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
                html_parts.append(f"<li>{line}</li>")
            continue
        if in_list:
            html_parts.append("</ul>")
            in_list = False
        # Paragraph: **bold** and single newlines -> <br>
        line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", block)
        line = line.replace("\n", "<br>")
        html_parts.append(f"<p>{line}</p>")
    if in_list:
        html_parts.append("</ul>")
    return "\n".join(html_parts)


def slug_to_id(slug):
    """Derive id from slug (e.g. news-259107 -> 259107)."""
    if not slug:
        return ""
    if slug.startswith("news-"):
        return slug[5:]
    return slug


def main():
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(raw)
        # Filename is YYYY-MM-DD-<slug>.md
        stem = path.stem
        parts = stem.split("-", 3)  # year, month, day, slug
        slug = parts[3] if len(parts) > 3 else stem
        id_ = fm.get("id") or slug_to_id(slug)
        date = fm.get("date", "")
        title = fm.get("title", "")
        category = fm.get("category", "")
        body_html = markdown_to_html(body)
        entries.append({
            "id": id_,
            "title": title,
            "date": date,
            "category": category,
            "content": body_html,
            "slug": slug,
            "originalFile": fm.get("originalFile", ""),
        })

    entries.sort(key=lambda x: x["date"], reverse=True)
    OUTPUT_FILE.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} news entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
