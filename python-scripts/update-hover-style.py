#!/usr/bin/env python3
"""
更新導航欄hover樣式：
- 移除hover時的背景色變化
- 只改變文字顏色為黃色
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

    # 1. 更新CSS樣式
    if '.dropdown-menu a:hover {' in content:
        # 將dropdown hover背景色改回深紅色
        content = re.sub(
            r'\.dropdown-menu a:hover \{\s*background-color: #efa22a;',
            '.dropdown-menu a:hover {\n            background-color: #991b1b;',
            content
        )

        # 更新nav-item hover樣式（從背景色改為文字顏色）
        content = re.sub(
            r'\.nav-item > a:hover \{\s*background-color: #efa22a !important;',
            '.nav-item > a:hover {\n            color: #efa22a !important;',
            content
        )

        # 更新nav-item active樣式（從背景色改為文字顏色）
        content = re.sub(
            r'\.nav-item > a\.active \{\s*background-color: #efa22a;',
            '.nav-item > a.active {\n            color: #efa22a;',
            content
        )

    # 2. 移除導航連結中的 hover:bg-red-800 類別
    content = re.sub(
        r'class="([^"]*?)hover:bg-red-800([^"]*?)"',
        r'class="\1\2"',
        content
    )

    # 清理多餘的空格
    content = re.sub(r'class="([^"]*?)\s+([^"]*?)"', r'class="\1 \2"', content)
    content = re.sub(r'class="([^"]*?)\s+"', r'class="\1"', content)
    content = re.sub(r'class="\s+([^"]*?)"', r'class="\1"', content)

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
    # 根目錄的文件
    root_files = [
        'news.html',
        'about.html',
        'activities.html',
        'resources.html',
    ]

    # 子目錄的文件
    subdirs = {
        'faculty': ['faculty.html', 'fulltime-professor.html', 'parttime-professor.html',
                   'practical-professor.html', 'parttime-professor-detail.html',
                   'practical-professor-detail.html', 'honorary-professor-detail.html',
                   'joint-professor-detail.html',
                   'jerryhsieh.html', 'lihyunlin.html', 'clhung.html',
                   'carolinelin.html', 'tsaihuiju.html', 'chanii311.html', 'RauchfleischA.html'],
        'admissions': ['admissions.html', 'qualifying-exam.html', 'entrance-exam.html',
                      'past-exam.html', 'international-students.html', 'ochkmc-students.html',
                      'mainland-chinese-students.html'],
        'courses': ['student-learning.html', 'course-map.html', 'course-regulation.html',
                   'statute-and-form.html', 'cross-school-course-cooperation.html'],
        'about': ['intro.html', 'mission.html', 'gallery.html', 'transportation.html', 'donate.html'],
        'publications': ['e-report.html', 'master-thesis.html', 'books.html', 'ntu-news-forum.html'],
    }

    count = 0

    # 更新根目錄文件
    for filename in root_files:
        filepath = BASE_DIR / filename
        if filepath.exists():
            if update_html_file(filepath):
                count += 1

    # 更新子目錄文件
    for subdir, files in subdirs.items():
        for filename in files:
            filepath = BASE_DIR / subdir / filename
            if filepath.exists():
                if update_html_file(filepath):
                    count += 1

    print(f"\n✅ 已更新 {count} 個文件")

if __name__ == '__main__':
    main()
