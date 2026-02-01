#!/usr/bin/env python3
"""
Generate data/faculty_data.json from faculty/_profiles/*.md (YAML front matter).
Keeps faculty list pages in sync with Decap CMS; run on build or after editing profiles.
Usage: python3 scripts/data/generate-faculty-json.py
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PROFILES_DIR = REPO_ROOT / "faculty" / "_profiles"
OUTPUT_FILE = REPO_ROOT / "data" / "faculty_data.json"

try:
    import yaml
except ImportError:
    yaml = None


def parse_frontmatter(content):
    """Parse YAML frontmatter and return (data dict, body string)."""
    if not content.strip().startswith("---"):
        return {}, content
    end = content.index("---", 3)
    head = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")
    if yaml is None:
        raise SystemExit("PyYAML required. Run: pip install pyyaml")
    data = yaml.safe_load(head)
    return data or {}, body


def to_list_string(items):
    """Turn expertise/research list (strings or {zh, en}) into one string joined by 、."""
    if not items:
        return ""
    out = []
    for x in items:
        if isinstance(x, str):
            out.append(x.strip())
        elif isinstance(x, dict):
            out.append((x.get("zh") or x.get("en") or "").strip())
        else:
            out.append(str(x).strip())
    return "、".join(filter(None, out))


def to_zh_string_list(items):
    """Turn education/experience list of {zh, en} into list of zh strings."""
    if not items:
        return []
    out = []
    for x in items:
        if isinstance(x, str):
            out.append(x.strip())
        elif isinstance(x, dict):
            out.append((x.get("zh") or x.get("en") or "").strip())
        else:
            out.append(str(x).strip())
    return [s for s in out if s]


def photo_for_list(photo_path, id_from_file):
    """Convert CMS photo path to path used by pages under faculty/ (../images/...)."""
    if not photo_path:
        return ""
    # CMS often uses /images/faculty/xxx; list pages are under faculty/ so need ../
    if photo_path.startswith("/images/"):
        return ".." + photo_path
    if photo_path.startswith("images/"):
        return "../" + photo_path
    return photo_path


def entry_fulltime(fm, id_from_file, file_stem):
    """Build one fulltime entry for faculty_data.json. file_stem = profile filename stem (e.g. RauchfleischA) so link matches existing HTML."""
    name = (fm.get("name") or "").strip()
    title = (fm.get("title") or "").strip()
    display_name = f"{name} {title}".strip() if title else name
    expertise = fm.get("expertise") or []
    research = fm.get("research") or []
    return {
        "name": display_name,
        "photo": photo_for_list(fm.get("photo"), id_from_file),
        "phone": (fm.get("phone") or "").strip(),
        "email": (fm.get("email") or "").strip(),
        "teaching": to_list_string(expertise),
        "research": to_list_string(research),
        "file": f"{file_stem}.html",
    }


def entry_parttime_honorary_joint(fm, id_from_file):
    """Build one parttime/honorary/joint entry (no file link)."""
    name = (fm.get("name") or "").strip()
    title = (fm.get("title") or "").strip()
    display_name = f"{name} {title}".strip() if title else name
    expertise = fm.get("expertise") or []
    research = fm.get("research") or []
    return {
        "name": display_name,
        "photo": photo_for_list(fm.get("photo"), id_from_file),
        "phone": (fm.get("phone") or "").strip(),
        "email": (fm.get("email") or "").strip(),
        "teaching": to_list_string(expertise),
        "research": to_list_string(research),
    }


def entry_practical(fm, id_from_file):
    """Build one practical entry (id, name, title, education[], experience[])."""
    name = (fm.get("name") or "").strip()
    # Display name: use name_en for Archie Tse (id archietse) per existing site behavior
    if id_from_file == "archietse":
        display_name = (fm.get("name_en") or name or "Archie Tse").strip()
    else:
        display_name = name
    expertise = fm.get("expertise") or []
    research = fm.get("research") or []
    education = to_zh_string_list(fm.get("education") or [])
    experience = to_zh_string_list(fm.get("experience") or [])
    return {
        "id": id_from_file,
        "name": display_name,
        "title": (fm.get("title") or "").strip(),
        "photo": photo_for_list(fm.get("photo"), id_from_file),
        "phone": (fm.get("phone") or "").strip(),
        "email": (fm.get("email") or "").strip(),
        "teaching": to_list_string(expertise),
        "research": to_list_string(research),
        "education": education,
        "experience": experience,
    }


# 教師類別（中文），與 CMS 選項一致
CATEGORIES_ZH = ["專任", "兼任", "合聘", "榮譽", "實務", "追思", "職員"]
# 舊英文值 → 中文（相容既有 .md）
CATEGORY_EN_TO_ZH = {
    "fulltime": "專任",
    "parttime": "兼任",
    "joint": "合聘",
    "honorary": "榮譽",
    "名譽": "榮譽",
    "practical": "實務",
}


def normalize_category(cat):
    """Return Chinese category; accept legacy English."""
    if not cat:
        return ""
    cat = (cat or "").strip()
    return CATEGORY_EN_TO_ZH.get(cat.lower()) or (cat if cat in CATEGORIES_ZH else "")


def main():
    PROFILES_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    by_category = {c: [] for c in CATEGORIES_ZH}

    for path in sorted(PROFILES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        try:
            fm, _ = parse_frontmatter(raw)
        except Exception as e:
            print(f"Warning: skip {path.name}: {e}")
            continue
        cat = normalize_category(fm.get("category"))
        id_from_file = (fm.get("id") or path.stem).strip()
        order = fm.get("order")
        if isinstance(order, str) and order.isdigit():
            order = int(order)
        if order is None:
            order = 9999

        if not cat or cat not in by_category:
            continue

        if cat == "專任":
            entry = entry_fulltime(fm, id_from_file, path.stem)
        elif cat == "實務":
            entry = entry_practical(fm, id_from_file)
        else:
            entry = entry_parttime_honorary_joint(fm, id_from_file)

        by_category[cat].append((order, entry))

    # Sort each category by order, then drop order
    for cat in by_category:
        by_category[cat].sort(key=lambda x: (x[0], x[1].get("name", "")))
        by_category[cat] = [e for _, e in by_category[cat]]

    payload = {c: by_category[c] for c in CATEGORIES_ZH}
    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(len(v) for v in payload.values())
    print(f"Wrote {total} faculty entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
