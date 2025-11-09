#!/usr/bin/env python3
"""
移除 HTML 中的 inline <style> 並替換為 {{site-head-common}}
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def process_html_file(file_path):
    """處理單個 HTML 檔案"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False

    original_content = content

    # 檢查是否已經有 {{site-head-common}}
    if '{{site-head-common}}' in content:
        return False

    # 1. 移除 <style>...</style> 區塊
    # 匹配從 <style> 到 </style> 的所有內容
    style_pattern = r'    <style>.*?</style>\n'
    if re.search(style_pattern, content, re.DOTALL):
        content = re.sub(style_pattern, '', content, flags=re.DOTALL)

    # 2. 在 tailwind.css 的 link 標籤後面插入 {{site-head-common}}
    # 找到 tailwind.css 的位置
    tailwind_pattern = r'(<link rel="stylesheet" href=".*?tailwind\.css">)\n'
    if re.search(tailwind_pattern, content):
        content = re.sub(tailwind_pattern, r'\1\n{{site-head-common}}\n', content)

    # 如果有變更，寫回檔案
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    """主函數"""
    print("=" * 70)
    print("移除 inline styles 並使用共用 CSS")
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
    print("\n所有頁面現在使用共用的 css/site-common.css")
    print("如需修改共用樣式，請編輯: css/site-common.css")

if __name__ == '__main__':
    main()
