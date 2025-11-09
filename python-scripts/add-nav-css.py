#!/usr/bin/env python3
"""
為 detail 頁面添加 navigation CSS
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

NAV_CSS = """
        /* Sticky Navigation */
        .site-nav {
            background-color: #671919;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Navigation dropdown */
        .nav-item {
            position: relative;
        }

        .nav-item.has-dropdown > a::after {
            content: ' ▼';
            font-size: 0.7em;
            margin-left: 4px;
        }

        .dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background-color: #671919;
            min-width: 180px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
            padding: 0.5rem 0;
        }

        .nav-item:hover .dropdown-menu {
            display: block;
        }

        .dropdown-menu a {
            display: block;
            padding: 0.5rem 1.25rem;
            color: #ffffff;
            text-decoration: none;
            transition: background-color 0.15s;
        }

        .dropdown-menu a:hover {
            background-color: #991b1b;
        }

        /* Active and hover states */
        .nav-item > a:hover {
            color: #efa22a !important;
        }

        .nav-item > a.active {
            color: #efa22a;
        }
"""

def add_nav_css(filepath):
    """為頁面添加 navigation CSS"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 檢查是否已經有 .site-nav CSS
    if '.site-nav' in content and 'position: sticky' in content:
        print(f"✓ {filepath.name} 已有完整的 navigation CSS")
        return False

    # 在 .container-1200 定義後添加 navigation CSS
    pattern = r'(\.container-1200 \{[^}]+\})'
    replacement = r'\1' + NAV_CSS

    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 已添加 navigation CSS 到 {filepath.name}")
        return True
    else:
        print(f"⚠️  無法修改 {filepath.name}")
        return False

def main():
    """主函數"""
    files_to_fix = [
        BASE_DIR / 'faculty' / 'joint-professor-detail.html',
        BASE_DIR / 'faculty' / 'honorary-professor-detail.html'
    ]

    for filepath in files_to_fix:
        if filepath.exists():
            add_nav_css(filepath)
        else:
            print(f"✗ 文件不存在: {filepath}")

if __name__ == '__main__':
    main()
