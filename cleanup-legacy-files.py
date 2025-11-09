#!/usr/bin/env python3
"""
Identify and move unused legacy JavaScript files to archive
"""

import os
import glob
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Known active JS files
ACTIVE_JS = {
    'activities.js',
    'article-view.js',
    'article.js',
    'combined-news.js',
    'homepage.js',
    'faculty.js',
    'fulltime-faculty-detail.js',
    'fulltime-faculty-profile.js',
    'honorary-faculty-detail.js',
    'joint-faculty-detail.js',
    'parttime-faculty-detail.js',
    'practical-faculty-detail.js',
    'csv-parser.js',
}

def find_js_references(js_file):
    """Search for references to a JS file in HTML files"""
    html_files = list(BASE_DIR.glob('**/*.html'))
    # Exclude archive
    html_files = [f for f in html_files if 'archive' not in str(f) and 'node_modules' not in str(f)]

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                if js_file in f.read():
                    return True
        except:
            pass
    return False

def main():
    print("=" * 70)
    print("Cleaning up legacy JavaScript files")
    print("=" * 70)
    print()

    js_dir = BASE_DIR / 'js'
    archive_js_dir = BASE_DIR / 'archive' / 'legacy-js'
    archive_js_dir.mkdir(parents=True, exist_ok=True)

    js_files = list(js_dir.glob('*.js'))

    moved_count = 0
    kept_count = 0

    for js_file in sorted(js_files):
        filename = js_file.name

        # Skip if in active list
        if filename in ACTIVE_JS:
            print(f"✅ KEEPING (known active): {filename}")
            kept_count += 1
            continue

        # Check if referenced in HTML
        if find_js_references(filename):
            print(f"✅ KEEPING (found references): {filename}")
            kept_count += 1
        else:
            print(f"❌ MOVING to archive: {filename}")
            shutil.move(str(js_file), str(archive_js_dir / filename))
            moved_count += 1

    print()
    print("=" * 70)
    print(f"Summary:")
    print(f"  Kept: {kept_count} files")
    print(f"  Moved: {moved_count} files to archive/legacy-js/")
    print("=" * 70)

if __name__ == '__main__':
    main()
