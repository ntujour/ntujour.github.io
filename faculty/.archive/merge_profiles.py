#!/usr/bin/env python3
"""Merge: keep _profiles (CMS format) as base, overwrite body with content/ detailed body for the 7."""
import re
from pathlib import Path

FACULTY_DIR = Path(__file__).resolve().parent
PROFILES = FACULTY_DIR / "_profiles"
LEGACY = FACULTY_DIR / ".archive" / "_profiles_legacy"

# 7 that had detailed content in content/ (current _profiles has that content)
# RauchfleischA: HTML uses RauchfleischA.md; legacy has adrianrauchfleisch.md
IDS_WITH_CONTENT = ["carolinelin", "chanii311", "clhung", "jerryhsieh", "lihyunlin", "tsaihuiju"]
RAUCHFLEISCH_LEGACY = "adrianrauchfleisch"  # YAML source for RauchfleischA.md


def extract_body_after_first_dash(content: str) -> str:
    """Content/ format: first --- then body."""
    parts = re.split(r"^---\s*$", content.strip(), maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 2:
        return parts[1].strip()
    return content


def extract_yaml_block(content: str) -> str:
    """CMS format: first --- ... second ---. Return including both ---."""
    if not content.strip().startswith("---"):
        return ""
    parts = re.split(r"^---\s*$", content.strip(), maxsplit=2, flags=re.MULTILINE)
    if len(parts) >= 2:
        return "---\n" + parts[1].strip() + "\n---"
    return ""


def main():
    # 1) Save body (after first ---) from current _profiles for the 7
    bodies = {}
    for fid in IDS_WITH_CONTENT:
        p = PROFILES / f"{fid}.md"
        if p.exists():
            bodies[fid] = extract_body_after_first_dash(p.read_text(encoding="utf-8"))
    rauch_path = PROFILES / "RauchfleischA.md"
    if rauch_path.exists():
        bodies["RauchfleischA"] = extract_body_after_first_dash(rauch_path.read_text(encoding="utf-8"))

    # 2) Restore all 29 from legacy to _profiles (overwrite)
    for f in LEGACY.glob("*.md"):
        (PROFILES / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")

    # 3) Overwrite the 6 with merged (YAML from legacy + body from content)
    for fid in IDS_WITH_CONTENT:
        legacy_path = LEGACY / f"{fid}.md"
        if not legacy_path.exists():
            continue
        yaml_block = extract_yaml_block(legacy_path.read_text(encoding="utf-8"))
        body = bodies.get(fid, "")
        merged = yaml_block + "\n\n" + body if body else yaml_block
        (PROFILES / f"{fid}.md").write_text(merged, encoding="utf-8")

    # 4) Write RauchfleischA.md (YAML from adrianrauchfleisch + body from content)
    adrian_path = LEGACY / f"{RAUCHFLEISCH_LEGACY}.md"
    if adrian_path.exists() and "RauchfleischA" in bodies:
        yaml_block = extract_yaml_block(adrian_path.read_text(encoding="utf-8"))
        merged = yaml_block + "\n\n" + bodies["RauchfleischA"]
        (PROFILES / "RauchfleischA.md").write_text(merged, encoding="utf-8")

    print("Merged 7 files (YAML from _profiles + body from content). Restored 29 from legacy.")


if __name__ == "__main__":
    main()
