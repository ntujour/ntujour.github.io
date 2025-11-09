#!/usr/bin/env python3
"""
更新所有 HTML 檔案中的教師照片路徑
將 001/Upload/xxx/ckfile/[GUID].{jpg|png} 替換為 images/faculty/[英文ID].{jpg|png}
"""

import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / 'faculty-mapping.csv'

def load_photo_mapping():
    """從 CSV 載入照片對應關係"""
    mapping = {}

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_file = row['照片檔名(001原檔)']
            new_file = row['新照片檔名']

            if old_file and new_file:
                # 建立對應關係
                mapping[old_file] = new_file

    return mapping

def update_html_file(html_path, mapping):
    """更新單個 HTML 檔案中的照片路徑"""

    # 跳過 .archive 目錄中的檔案
    if '.archive' in str(html_path):
        return 0, []

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取: {html_path} - {e}")
        return 0, []

    original_content = content
    replacements = []

    # 建立替換模式
    # 匹配: ../001/Upload/xxx/ckfile/[GUID].{jpg|png} 或 001/Upload/xxx/ckfile/[GUID].{jpg|png}
    for old_file, new_file in mapping.items():
        # 各種可能的路徑格式
        patterns = [
            rf'\.\.\/001\/Upload\/\d+\/ckfile\/{re.escape(old_file)}',
            rf'001\/Upload\/\d+\/ckfile\/{re.escape(old_file)}',
            rf'\.\.\/\.\.\/001\/Upload\/\d+\/ckfile\/{re.escape(old_file)}',
        ]

        for pattern in patterns:
            if re.search(pattern, content):
                # 根據檔案位置決定新路徑
                if 'faculty/' in str(html_path):
                    new_path = f'../images/faculty/{new_file}'
                else:
                    new_path = f'images/faculty/{new_file}'

                old_match = re.search(pattern, content)
                if old_match:
                    old_path = old_match.group(0)
                    content = re.sub(pattern, new_path, content)
                    replacements.append((old_path, new_path))

    # 如果有變更，寫回檔案
    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return len(replacements), replacements

    return 0, []

def update_all_html_files():
    """更新所有 HTML 檔案"""
    print("=" * 70)
    print("更新 HTML 檔案中的照片路徑")
    print("=" * 70)

    # 載入對應關係
    mapping = load_photo_mapping()
    print(f"\n已載入 {len(mapping)} 組照片對應關係\n")

    # 找出所有 HTML 檔案（排除 .archive）
    html_files = []
    for pattern in ['**/*.html']:
        html_files.extend(BASE_DIR.glob(pattern))

    # 過濾掉 .archive 目錄
    html_files = [f for f in html_files if '.archive' not in str(f)]

    print(f"找到 {len(html_files)} 個 HTML 檔案\n")
    print("-" * 70)

    total_replacements = 0
    updated_files = []

    for html_file in html_files:
        count, replacements = update_html_file(html_file, mapping)

        if count > 0:
            total_replacements += count
            updated_files.append(html_file)

            relative_path = html_file.relative_to(BASE_DIR)
            print(f"\n✓ {relative_path}")
            for old_path, new_path in replacements:
                print(f"    {old_path}")
                print(f"  → {new_path}")

    print("\n" + "-" * 70)
    print(f"\n統計:")
    print(f"  更新的檔案: {len(updated_files)}")
    print(f"  替換次數: {total_replacements}")

    if len(updated_files) > 0:
        print(f"\n更新的檔案清單:")
        for f in updated_files:
            print(f"  - {f.relative_to(BASE_DIR)}")

    print("\n" + "=" * 70)
    print("完成！")
    print("=" * 70)

if __name__ == '__main__':
    update_all_html_files()
