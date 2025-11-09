#!/usr/bin/env python3
"""
Fix {{path_prefix}} placeholders in HTML files
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def calculate_path_prefix(file_path):
    """根據檔案位置計算路徑前綴"""
    relative_path = file_path.relative_to(BASE_DIR)
    depth = len(relative_path.parts) - 1

    if depth == 0:
        return ''
    else:
        return '../' * depth

def fix_file(file_path):
    """修正單個檔案的 {{path_prefix}}"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False

    if '{{path_prefix}}' not in content:
        return False

    # 計算正確的路徑前綴
    path_prefix = calculate_path_prefix(file_path)

    # 替換所有 {{path_prefix}}
    new_content = content.replace('{{path_prefix}}', path_prefix)

    # 寫回檔案
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    print("=" * 70)
    print("修正 {{path_prefix}} 佔位符")
    print("=" * 70)
    print()

    # 找出所有 HTML 檔案
    html_files = list(BASE_DIR.glob('**/*.html'))

    # 排除 templates 和 archive 目錄
    html_files = [f for f in html_files
                  if 'templates' not in str(f)
                  and 'archive' not in str(f)
                  and 'node_modules' not in str(f)]

    # 找出包含 {{path_prefix}} 的檔案
    files_to_fix = []
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                if '{{path_prefix}}' in f.read():
                    files_to_fix.append(file_path)
        except:
            pass

    print(f"找到 {len(files_to_fix)} 個需要修正的檔案\n")

    if len(files_to_fix) == 0:
        print("沒有檔案需要處理")
        return

    print("-" * 70)
    print("修正檔案:")
    print("-" * 70)

    fixed_count = 0
    for file_path in files_to_fix:
        relative_path = file_path.relative_to(BASE_DIR)
        if fix_file(file_path):
            path_prefix = calculate_path_prefix(file_path)
            print(f"  ✓ {relative_path} (path_prefix: '{path_prefix}')")
            fixed_count += 1

    print("-" * 70)
    print(f"\n總共修正了 {fixed_count} 個檔案")
    print()
    print("=" * 70)
    print("修正完成！")
    print("=" * 70)

if __name__ == '__main__':
    main()
