#!/usr/bin/env python3
"""
修正所有頁面的 sitemap heading，確保都有 text-lg
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fix_sitemap_heading(filepath):
    """修正單個 HTML 文件的 sitemap heading"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"跳過 (編碼錯誤): {filepath}")
        return False

    original_content = content

    # 修正 sitemap 中缺少 text-lg 的 h4 標題
    # 匹配 <h4 class="font-bold text-gray-900 mb-3"> 並加上 text-lg
    content = re.sub(
        r'<h4 class="font-bold text-gray-900 mb-3">',
        r'<h4 class="text-lg font-bold text-gray-900 mb-3">',
        content
    )

    # 只有內容有變化時才寫入
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filepath}")
        return True
    else:
        return False

def main():
    """主函數"""
    count = 0

    # 掃描所有 HTML 文件
    for html_file in BASE_DIR.rglob('*.html'):
        # 跳過備份文件和存檔文件
        if '.backup' in str(html_file) or '.archive' in str(html_file) or '-old' in str(html_file):
            continue

        if fix_sitemap_heading(html_file):
            count += 1

    if count > 0:
        print(f"\n✅ 已修正 {count} 個文件的 sitemap heading")
    else:
        print("\n✓ 所有文件的 sitemap heading 已正確")

if __name__ == '__main__':
    main()
