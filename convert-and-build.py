#!/usr/bin/env python3
"""
將現有 HTML 檔案轉換為使用模板標記並建置
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def convert_html_file(file_path):
    """轉換單個 HTML 檔案"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False, []

    original_content = content
    changes = []

    # 1. 替換 Banner
    banner_pattern = r'<!-- Banner -->.*?</header>'
    if re.search(banner_pattern, content, re.DOTALL):
        content = re.sub(banner_pattern, '{{site-banner}}', content, count=1, flags=re.DOTALL)
        changes.append('Banner')

    # 2. 替換 Navigation
    nav_pattern = r'<!-- Navigation -->.*?</nav>'
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, '{{site-nav}}', content, count=1, flags=re.DOTALL)
        changes.append('Navigation')

    # 3. 替換 Sitemap
    sitemap_pattern = r'<!-- Sitemap.*?-->.*?<section class="site-sitemap.*?</section>'
    if re.search(sitemap_pattern, content, re.DOTALL):
        content = re.sub(sitemap_pattern, '{{site-sitemap}}', content, count=1, flags=re.DOTALL)
        changes.append('Sitemap')

    # 4. 替換 Footer
    footer_pattern = r'<!-- Footer -->.*?</footer>'
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, '{{site-footer}}', content, count=1, flags=re.DOTALL)
        changes.append('Footer')

    # 如果有變更，寫回檔案
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes

    return False, []

def main():
    """主函數"""
    print("=" * 70)
    print("轉換 HTML 檔案為使用模板標記")
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
    print("轉換檔案:")
    print("-" * 70)

    converted_count = 0
    for file_path in html_files:
        relative_path = file_path.relative_to(BASE_DIR)
        result, changes = convert_html_file(file_path)

        if result:
            print(f"  ✓ {relative_path}")
            if changes:
                print(f"    替換: {', '.join(changes)}")
            converted_count += 1

    print("-" * 70)
    print(f"\n總共轉換了 {converted_count} 個檔案\n")

    if converted_count > 0:
        print("現在執行建置腳本...")
        print("=" * 70)
        import subprocess
        subprocess.run(['python3', 'build-templates.py'])

    print("\n完成！")

if __name__ == '__main__':
    main()
