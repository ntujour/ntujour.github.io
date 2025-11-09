#!/usr/bin/env python3
"""
從所有頁面的導航中移除轉學考連結
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def remove_transfer_link(filepath):
    """從單個HTML文件中移除轉學考連結"""
    print(f"更新: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # 嘗試其他編碼
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            print(f"  跳過 (編碼錯誤): {filepath}")
            return

    # 移除轉學考連結行（包含換行）
    # 匹配 <a href="...transfer.html">轉學考</a> 這一整行
    patterns = [
        r'\s*<a href="[^"]*transfer\.html">轉學考</a>\n',
        r'\s*<a href="[^"]*transfer\.html">轉學考</a>',
    ]

    original_content = content
    for pattern in patterns:
        content = re.sub(pattern, '', content)

    # 只有內容有變化時才寫入
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ 已移除轉學考連結")
    else:
        print(f"  - 未找到轉學考連結")

def main():
    """主函數"""

    # 根目錄的文件
    root_files = [
        'index.html',
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

    # 更新根目錄文件
    for filename in root_files:
        filepath = BASE_DIR / filename
        if filepath.exists():
            remove_transfer_link(filepath)

    # 更新子目錄文件
    for subdir, files in subdirs.items():
        for filename in files:
            filepath = BASE_DIR / subdir / filename
            if filepath.exists():
                remove_transfer_link(filepath)

    print("✅ 已從所有頁面移除轉學考連結！")

if __name__ == '__main__':
    main()
