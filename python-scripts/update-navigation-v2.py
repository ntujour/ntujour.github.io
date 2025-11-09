#!/usr/bin/env python3
"""
更新所有頁面的導航結構：
1. 師資陣容改為下拉選單
2. Active和hover改為黃色 (#efa22a)
3. 更新sitemap區塊（只有4欄，移除學生資源和相關連結）
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# 新的CSS樣式（hover改為黃色）
NEW_CSS_STYLES = '''        /* Navigation dropdown */
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
            background-color: #efa22a;
        }

        /* Active and hover states */
        .nav-item > a:hover {
            background-color: #efa22a !important;
        }

        .nav-item > a.active {
            background-color: #efa22a;
        }'''

def get_faculty_nav_html(relative_path=''):
    """生成師資陣容的導航HTML（帶下拉選單）"""
    return f'''<li class="nav-item has-dropdown">
                    <a href="{relative_path}faculty/faculty.html" class="px-5 py-2.5 text-base text-white hover:bg-red-800 rounded font-medium transition">師資陣容</a>
                    <div class="dropdown-menu">
                        <a href="{relative_path}faculty/fulltime-professor.html">專任教師</a>
                        <a href="{relative_path}faculty/practical-professor.html">實務教師</a>
                        <a href="{relative_path}faculty/parttime-professor.html">兼任、合聘與名譽教師</a>
                    </div>
                </li>'''

def get_sitemap_html(relative_path=''):
    """生成新的sitemap HTML（4欄版本）"""
    return f'''            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">認識本所</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{relative_path}about/intro.html" class="text-gray-700 hover:text-gray-900">本所介紹</a></li>
                        <li><a href="{relative_path}about/mission.html" class="text-gray-700 hover:text-gray-900">宗旨與目標</a></li>
                        <li><a href="{relative_path}about/gallery.html" class="text-gray-700 hover:text-gray-900">新聞所圖集</a></li>
                        <li><a href="{relative_path}about/transportation.html" class="text-gray-700 hover:text-gray-900">聯絡我們</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">師資陣容</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{relative_path}faculty/faculty.html" class="text-gray-700 hover:text-gray-900">師資總覽</a></li>
                        <li><a href="{relative_path}faculty/fulltime-professor.html" class="text-gray-700 hover:text-gray-900">專任教師</a></li>
                        <li><a href="{relative_path}faculty/parttime-professor.html" class="text-gray-700 hover:text-gray-900">兼任教師</a></li>
                        <li><a href="{relative_path}staff.html" class="text-gray-700 hover:text-gray-900">行政人員</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">入學資訊</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{relative_path}admissions/admissions.html" class="text-gray-700 hover:text-gray-900">招生總覽</a></li>
                        <li><a href="{relative_path}admissions/qualifying-exam.html" class="text-gray-700 hover:text-gray-900">甄試入學</a></li>
                        <li><a href="{relative_path}admissions/entrance-exam.html" class="text-gray-700 hover:text-gray-900">招生考試</a></li>
                        <li><a href="{relative_path}admissions/past-exam.html" class="text-gray-700 hover:text-gray-900">歷屆考古題</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">課程與出版</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{relative_path}courses/course-map.html" class="text-gray-700 hover:text-gray-900">課程地圖</a></li>
                        <li><a href="{relative_path}courses/course-regulation.html" class="text-gray-700 hover:text-gray-900">修業規定</a></li>
                        <li><a href="{relative_path}publications/e-report.html" class="text-gray-700 hover:text-gray-900">前期所報</a></li>
                        <li><a href="{relative_path}publications/master-thesis.html" class="text-gray-700 hover:text-gray-900">畢業生論文</a></li>
                    </ul>
                </div>
            </div>'''

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

    # 1. 更新CSS樣式（如果包含舊的dropdown CSS）
    if '.dropdown-menu a:hover {' in content:
        # 找到整個navigation dropdown區塊並替換
        pattern = r'/\* Navigation dropdown \*/.*?\.dropdown-menu a:hover \{[^}]+\}'
        content = re.sub(pattern, NEW_CSS_STYLES, content, flags=re.DOTALL)

    # 2. 更新師資陣容導航項（如果是單行的話）
    old_faculty_nav_pattern = r'<li class="nav-item"><a href="[^"]*faculty/faculty\.html"[^>]*>師資陣容</a></li>'
    if re.search(old_faculty_nav_pattern, content):
        content = re.sub(old_faculty_nav_pattern, get_faculty_nav_html(relative_path), content)

    # 3. 更新sitemap區塊（如果是6欄的話，改為4欄）
    sitemap_pattern = r'<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">.*?</div>\s*</div>\s*</div>\s*</section>\s*<!-- Footer -->'
    if re.search(sitemap_pattern, content, flags=re.DOTALL):
        new_sitemap_section = f'''            {get_sitemap_html(relative_path)}
        </div>
    </section>

    <!-- Footer -->'''
        content = re.sub(sitemap_pattern, new_sitemap_section, content, flags=re.DOTALL)

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
