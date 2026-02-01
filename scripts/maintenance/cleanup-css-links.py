#!/usr/bin/env python3
"""
清理重複的 CSS 連結並使用 {{site-head-common}}
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def process_html_file(file_path):
    """處理單個 HTML 檔案"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False

    original_content = content

    # 1. 移除所有 site-common.css 和多餘的 tailwind.css 連結
    content = re.sub(r'    <link rel="stylesheet" href=".*?site-common\.css">\n', '', content)
    content = re.sub(r'    <link rel="stylesheet" href=".*?tailwind\.css">\n{{site-head-common}}\n', '    <link rel="stylesheet" href="{{path_prefix}}css/tailwind.css">\n{{site-head-common}}\n', content)

    # 2. 移除重複的 {{site-head-common}}
    content = re.sub(r'({{site-head-common}}\n)+', '{{site-head-common}}\n', content)

    # 3. 確保只有一個 tailwind.css + 一個 {{site-head-common}}
    # 先移除所有 tailwind 連結
    content = re.sub(r'    <link rel="stylesheet" href=".*?tailwind\.css">\n', '', content)

    # 在 favicon 後面插入正確的結構
    favicon_pattern = r'(<link rel="icon".*?>)\n'
    if re.search(favicon_pattern, content):
        if '{{site-head-common}}' not in content:
            content = re.sub(favicon_pattern, r'\1\n    <link rel="stylesheet" href="{{path_prefix}}css/tailwind.css">\n{{site-head-common}}\n', content)
        else:
            content = re.sub(favicon_pattern, r'\1\n    <link rel="stylesheet" href="{{path_prefix}}css/tailwind.css">\n', content)

    # 如果有變更，寫回檔案
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """主函數"""
    print("=" * 70)
    print("清理重複的 CSS 連結")
    print("=" * 70)
    print()

    # 找出所有 HTML 檔案
    html_files = list(BASE_DIR.glob('**/*.html'))

    # 排除 templates, archive, node_modules 目錄
    html_files = [f for f in html_files
                  if 'templates' not in str(f)
                  and 'archive' not in str(f)
                  and 'node_modules' not in str(f)]

    print(f"找到 {len(html_files)} 個 HTML 檔案\n")

    print("-" * 70)
    print("處理檔案:")
    print("-" * 70)

    processed_count = 0
    for file_path in html_files:
        relative_path = file_path.relative_to(BASE_DIR)
        if process_html_file(file_path):
            print(f"  ✓ {relative_path}")
            processed_count += 1

    print("-" * 70)
    print(f"\n總共處理了 {processed_count} 個檔案\n")

    if processed_count > 0:
        print("現在執行建置腳本...")
        print("=" * 70)
        import subprocess
        subprocess.run(['python3', 'build-templates.py'])

    print("\n完成！")

if __name__ == '__main__':
    main()
