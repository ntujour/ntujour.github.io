#!/usr/bin/env python3
"""
更新所有頁面的連結：
1. courses/ 改為 students/
2. about.html 改為 about/intro.html
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def update_html_file(filepath):
    """更新單個HTML文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"跳過 (編碼錯誤): {filepath}")
        return False

    original_content = content

    # 1. 更新 courses/ 為 students/
    content = re.sub(r'href="([^"]*?)courses/', r'href="\1students/', content)

    # 2. 更新 about.html 為 about/intro.html（只在導航中）
    content = re.sub(r'href="about\.html"', 'href="about/intro.html"', content)
    content = re.sub(r'href="\.\./about\.html"', 'href="../about/intro.html"', content)

    # 只有內容有變化時才寫入
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filepath}")
        return True
    else:
        print(f"- {filepath} (無需更新)")
        return False

def main():
    """主函數"""
    count = 0

    # 掃描所有 HTML 文件
    for html_file in BASE_DIR.rglob('*.html'):
        # 跳過備份文件
        if '.backup' in str(html_file) or '-old' in str(html_file):
            continue

        if update_html_file(html_file):
            count += 1

    print(f"\n✅ 已更新 {count} 個文件")

if __name__ == '__main__':
    main()
