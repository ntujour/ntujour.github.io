#!/usr/bin/env python3
"""
批量更新所有頁面的 banner 和 navigation
"""

import os
import re
from pathlib import Path

# 基礎路徑
BASE_DIR = Path(__file__).parent

# 新的 CSS 樣式（dropdown）
DROPDOWN_CSS = '''
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
'''

def get_navigation_html(relative_path='', active_page=''):
    """
    生成 navigation HTML
    relative_path: 相對於根目錄的路徑（如 '../' 或 ''）
    active_page: 當前激活的頁面（如 'about', 'faculty', 'admissions' 等）
    """

    # 確定活動狀態的class
    def get_active_class(page):
        return ' bg-gray-800' if page == active_page else ' hover:bg-red-800'

    return f'''    <!-- Navigation -->
    <nav class="site-nav">
        <div class="container-1200">
            <ul class="flex flex-wrap items-center gap-2 py-3">
                <li class="nav-item has-dropdown">
                    <a href="{relative_path}about.html" class="px-5 py-2.5 text-base text-white{get_active_class('about')} rounded font-medium transition">關於我們</a>
                    <div class="dropdown-menu">
                        <a href="{relative_path}about/intro.html">本所簡介</a>
                        <a href="{relative_path}about/transportation.html">交通資訊</a>
                        <a href="{relative_path}about/donate.html">捐款支持</a>
                    </div>
                </li>
                <li class="nav-item"><a href="{relative_path}faculty/faculty.html" class="px-5 py-2.5 text-base text-white{get_active_class('faculty')} rounded font-medium transition">師資陣容</a></li>
                <li class="nav-item has-dropdown">
                    <a href="{relative_path}admissions/admissions.html" class="px-5 py-2.5 text-base text-white{get_active_class('admissions')} rounded font-medium transition">入學資訊</a>
                    <div class="dropdown-menu">
                        <a href="{relative_path}admissions/qualifying-exam.html">推甄入學</a>
                        <a href="{relative_path}admissions/entrance-exam.html">入學考試</a>
                        <a href="{relative_path}admissions/past-exam.html">歷屆考古題</a>
                        <a href="{relative_path}admissions/transfer.html">轉學考</a>
                        <a href="{relative_path}admissions/international-students.html">國際生</a>
                        <a href="{relative_path}admissions/ochkmc-students.html">港澳僑生</a>
                    </div>
                </li>
                <li class="nav-item"><a href="{relative_path}courses/student-learning.html" class="px-5 py-2.5 text-base text-white{get_active_class('courses')} rounded font-medium transition">學生學習</a></li>
                <li class="nav-item"><a href="{relative_path}publications/e-report.html" class="px-5 py-2.5 text-base text-white{get_active_class('publications')} rounded font-medium transition">出版發表</a></li>
                <li class="nav-item"><a href="{relative_path}news.html" class="px-5 py-2.5 text-base text-white{get_active_class('news')} rounded font-medium transition">最新消息</a></li>
                <li class="nav-item"><a href="{relative_path}resources.html" class="px-5 py-2.5 text-base text-white{get_active_class('resources')} rounded font-medium transition">相關資源</a></li>
            </ul>
        </div>
    </nav>'''

def get_banner_html(relative_path=''):
    """生成可點擊的 banner HTML"""
    return f'''    <!-- Banner -->
    <header class="site-banner py-6">
        <div class="container-1200">
            <h1 class="text-4xl font-bold text-gray-800 mb-2">
                <a href="{relative_path}index.html" class="hover:text-gray-600 transition" style="text-decoration: none; color: inherit;">國立臺灣大學新聞研究所</a>
            </h1>
            <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
            <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
        </div>
    </header>'''

def update_html_file(filepath, relative_path='', active_page=''):
    """更新單個HTML文件"""
    print(f"更新: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 添加 dropdown CSS（如果還沒有）
    if '.nav-item.has-dropdown' not in content:
        # 在 .site-nav 樣式後添加 dropdown CSS
        content = re.sub(
            r'(\.site-nav\s*\{[^}]+\})',
            r'\1\n' + DROPDOWN_CSS,
            content
        )

    # 2. 更新 banner（讓標題可點擊）
    # 查找現有的 banner section
    banner_pattern = r'<header class="site-banner[^>]*>.*?</header>'
    if re.search(banner_pattern, content, re.DOTALL):
        content = re.sub(
            banner_pattern,
            get_banner_html(relative_path),
            content,
            flags=re.DOTALL
        )

    # 3. 更新 navigation
    nav_pattern = r'<nav class="site-nav">.*?</nav>'
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(
            nav_pattern,
            get_navigation_html(relative_path, active_page),
            content,
            flags=re.DOTALL
        )

    # 寫回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """主函數"""

    # 根目錄的文件
    root_files = [
        ('about.html', '', 'about'),
        ('activities.html', '', 'activities'),  # 雖然會被整合，但先更新
    ]

    # 子目錄的文件
    subdirs = {
        'faculty': ['faculty.html', 'fulltime-professor.html', 'parttime-professor.html',
                   'practical-professor.html', 'parttime-professor-detail.html',
                   'practical-professor-detail.html', 'honorary-professor-detail.html',
                   'joint-professor-detail.html'],
        'admissions': ['admissions.html', 'qualifying-exam.html', 'entrance-exam.html',
                      'past-exam.html', 'international-students.html', 'ochkmc-students.html',
                      'mainland-chinese-students.html'],
        'courses': ['student-learning.html', 'course-map.html', 'course-regulation.html',
                   'statute-and-form.html', 'cross-school-course-cooperation.html'],
        'about': ['intro.html', 'mission.html', 'gallery.html', 'transportation.html'],
    }

    # 更新根目錄文件
    for filename, rel_path, active in root_files:
        filepath = BASE_DIR / filename
        if filepath.exists():
            update_html_file(filepath, rel_path, active)

    # 更新子目錄文件
    for subdir, files in subdirs.items():
        for filename in files:
            filepath = BASE_DIR / subdir / filename
            if filepath.exists():
                update_html_file(filepath, '../', subdir)

    # 個別教師頁面
    faculty_pages = ['jerryhsieh.html', 'lihyunlin.html', 'clhung.html',
                    'carolinelin.html', 'tsaihuiju.html', 'chanii311.html', 'RauchfleischA.html']
    for filename in faculty_pages:
        filepath = BASE_DIR / 'faculty' / filename
        if filepath.exists():
            update_html_file(filepath, '../', 'faculty')

    print("✅ 所有頁面更新完成！")

if __name__ == '__main__':
    main()
