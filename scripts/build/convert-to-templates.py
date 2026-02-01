#!/usr/bin/env python3
"""
將現有 HTML 檔案轉換為使用模板標記
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def convert_html_file(file_path):
    """轉換單個 HTML 檔案"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False

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

def convert_all():
    """轉換所有 HTML 檔案"""
    print("=" * 70)
    print("將 HTML 檔案轉換為使用模板標記")
    print("=" * 70)
    print()

    # 找出所有 HTML 檔案
    html_files = list(BASE_DIR.glob('**/*.html'))

    # 排除 templates 和 .archive 目錄
    html_files = [f for f in html_files
                  if 'templates' not in str(f) and '.archive' not in str(f)]

    print(f"找到 {len(html_files)} 個 HTML 檔案\n")

    # 詢問確認
    response = input("是否要將這些檔案轉換為使用模板標記？(y/N): ")
    if response.lower() != 'y':
        print("\n已取消")
        return

    print("\n" + "-" * 70)
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
    print(f"\n總共轉換了 {converted_count} 個檔案")

    if converted_count > 0:
        print("\n現在執行建置腳本來填入模板內容...")
        import subprocess
        subprocess.run(['python3', 'build-templates.py'])

    print()
    print("=" * 70)
    print("完成！")
    print("=" * 70)
    print("\n下次修改共用區塊時:")
    print("  1. 編輯 templates/ 中的模板檔案")
    print("  2. 執行: python3 build-templates.py")
    print("  3. 所有頁面自動更新！")

if __name__ == '__main__':
    convert_all()
