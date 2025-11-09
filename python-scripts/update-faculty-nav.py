#!/usr/bin/env python3
"""
更新所有頁面的師資陣容導航，恢復成獨立的多個頁面
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def get_faculty_dropdown(relative_path=''):
    """生成師資陣容下拉選單HTML"""
    return f'''<li class="nav-item has-dropdown">
                    <a href="{relative_path}faculty/faculty.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">師資陣容</a>
                    <div class="dropdown-menu">
                        <a href="{relative_path}faculty/fulltime-professor.html">專任教師</a>
                        <a href="{relative_path}faculty/practical-professor.html">實務教師</a>
                        <a href="{relative_path}faculty/parttime-professor.html">兼任教師</a>
                        <a href="{relative_path}faculty/honorary-professor-detail.html">名譽教授</a>
                        <a href="{relative_path}faculty/joint-professor-detail.html">合聘教師</a>
                        <a href="{relative_path}staff.html">行政人員</a>
                    </div>
                </li>'''

def update_html_file(filepath):
    """更新單個HTML文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"跳過 (編碼錯誤): {filepath}")
        return False

    original_content = content

    # 確定相對路徑
    relative_path = ''
    if 'faculty/' in str(filepath) or 'admissions/' in str(filepath) or 'courses/' in str(filepath) or 'about/' in str(filepath) or 'publications/' in str(filepath):
        relative_path = '../'

    # 更新師資陣容導航（找到整個師資陣容的nav-item並替換）
    faculty_pattern = r'<li class="nav-item has-dropdown">\s*<a[^>]*>師資陣容</a>\s*<div class="dropdown-menu">.*?</div>\s*</li>'

    if re.search(faculty_pattern, content, flags=re.DOTALL):
        content = re.sub(
            faculty_pattern,
            get_faculty_dropdown(relative_path),
            content,
            flags=re.DOTALL
        )

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
