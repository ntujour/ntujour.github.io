#!/usr/bin/env python3
"""
檢查所有頁面是否符合標準樣式：
1. Navigation 下拉選單結構
2. Sitemap 標題使用 text-lg
3. Banner 和 Footer 結構
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def check_page(filepath):
    """檢查單個頁面"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return None

    issues = []

    # 檢查 1: 是否有新的導航結構（has-dropdown）
    if '<nav' in content and 'site-nav' in content:
        if 'has-dropdown' not in content:
            issues.append("缺少 has-dropdown 導航結構")

    # 檢查 2: 如果有 sitemap，標題應該有 text-lg
    if 'site-sitemap' in content:
        # 檢查是否有缺少 text-lg 的 h4
        if re.search(r'<h4 class="font-bold text-gray-900', content):
            issues.append("Sitemap 標題缺少 text-lg")

    # 檢查 3: CSS 中的 hover 應該是文字顏色而非背景色
    if '.nav-item > a:hover' in content:
        # 檢查 hover 定義
        hover_section = re.search(r'\.nav-item > a:hover \{([^}]+)\}', content, re.DOTALL)
        if hover_section:
            hover_css = hover_section.group(1)
            if 'background-color' in hover_css and 'color' not in hover_css:
                issues.append("Navigation hover 應該改變文字顏色而非背景色")

    # 檢查 4: Banner 是否有正確的樣式
    if 'site-banner' in content:
        if 'hd-bg-lt.png' not in content or 'hd-bg-rt.png' not in content:
            issues.append("Banner 缺少背景圖片")

    return issues

def main():
    """主函數"""
    print("檢查頁面一致性...\n")

    problem_files = []
    checked_count = 0

    # 掃描所有 HTML 文件
    for html_file in BASE_DIR.rglob('*.html'):
        # 跳過備份和存檔文件
        if any(x in str(html_file) for x in ['.backup', '.archive', '-old', 'Scripts/']):
            continue

        issues = check_page(html_file)
        if issues is None:
            continue

        checked_count += 1

        if issues:
            problem_files.append((html_file, issues))

    # 顯示結果
    print(f"已檢查 {checked_count} 個頁面\n")

    if problem_files:
        print("⚠️  發現以下問題：\n")
        for filepath, issues in problem_files:
            rel_path = filepath.relative_to(BASE_DIR)
            print(f"📄 {rel_path}")
            for issue in issues:
                print(f"   - {issue}")
            print()
    else:
        print("✅ 所有頁面樣式一致！")

if __name__ == '__main__':
    main()
