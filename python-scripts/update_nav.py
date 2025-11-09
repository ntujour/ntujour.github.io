#!/usr/bin/env python3
"""
批量更新網站中所有頁面的 banner 和 navigation
"""

import os
import re
from pathlib import Path

# 舊的 banner 模式（沒有連結的版本）
OLD_BANNER_PATTERN = r'''<!-- Banner -->
<header class="site-banner py-6">
    <div class="container-1200">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">國立臺灣大學新聞研究所</h1>
        <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
        <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
    </div>
</header>'''

# 新的 banner 模板（會根據目錄層級調整路徑）
NEW_BANNER_TEMPLATE = '''<!-- Banner -->
<header class="site-banner py-6">
    <div class="container-1200">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">
            <a href="{index_path}" class="hover:text-gray-600 transition" style="text-decoration: none; color: inherit;">國立臺灣大學新聞研究所</a>
        </h1>
        <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
        <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
    </div>
</header>'''

# 舊的 navigation 模式（簡單版本，沒有下拉選單）
OLD_NAV_PATTERNS = [
    # 模式1: 有首頁連結
    r'''<!-- Navigation -->
<nav class="site-nav">
    <div class="container-1200">
        <ul class="flex flex-wrap items-center gap-2 py-3">
            <li><a href="[^"]*index\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">首頁</a></li>
            <li><a href="[^"]*about/intro\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">關於[^<]*</a></li>
            <li><a href="[^"]*faculty/faculty\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">師資陣容</a></li>
            <li><a href="[^"]*admissions/admissions\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">招生[^<]*</a></li>
            <li><a href="[^"]*students/student-learning\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">學生學習</a></li>
            <li><a href="[^"]*e-report\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">出版發表</a></li>
            <li><a href="[^"]*news\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">最新消息</a></li>
            <li><a href="[^"]*activities\.html" class="px-5 py-2\.5 text-base text-white[^"]*rounded font-medium[^"]*">活動資訊</a></li>
        </ul>
    </div>
</nav>''',
]

# 新的 navigation 模板
NEW_NAV_TEMPLATE = '''<!-- Navigation -->
<nav class="site-nav">
    <div class="container-1200">
        <ul class="flex flex-wrap items-center gap-2 py-3">
            <li class="nav-item has-dropdown">
                <a href="{path}about/intro.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">關於我們</a>
                <div class="dropdown-menu">
                    <a href="{path}about/intro.html">本所簡介</a>
                    <a href="{path}about/transportation.html">交通資訊</a>
                    <a href="{path}about/donate.html">捐款支持</a>
                </div>
            </li>
            <li class="nav-item has-dropdown">
                <a href="{path}faculty/faculty.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">師資陣容</a>
                <div class="dropdown-menu">
                    <a href="{path}faculty/fulltime-professor.html">專任教師</a>
                    <a href="{path}faculty/practical-professor.html">實務教師</a>
                    <a href="{path}faculty/parttime-professor.html">兼任教師</a>
                    <a href="{path}faculty/honorary-professor-detail.html">名譽教授</a>
                    <a href="{path}faculty/joint-professor-detail.html">合聘教師</a>
                    <a href="{path}staff.html">行政人員</a>
                </div>
            </li>
            <li class="nav-item has-dropdown">
                <a href="{path}admissions/admissions.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">入學資訊</a>
                <div class="dropdown-menu">
                    <a href="{path}admissions/qualifying-exam.html">推甄入學</a>
                    <a href="{path}admissions/entrance-exam.html">入學考試</a>
                    <a href="{path}admissions/past-exam.html">歷屆考古題</a>                        <a href="{path}admissions/international-students.html">國際生</a>
                    <a href="{path}admissions/ochkmc-students.html">港澳僑生</a>
                </div>
            </li>
            <li class="nav-item"><a href="{path}students/student-learning.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">學生學習</a></li>
            <li class="nav-item"><a href="{path}publications/e-report.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition{active_publications}">出版發表</a></li>
            <li class="nav-item"><a href="{path}news.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">最新消息</a></li>
            <li class="nav-item"><a href="{path}resources.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">相關資源</a></li>
        </ul>
    </div>
</nav>'''

# 需要添加的 CSS 樣式（用於下拉選單）
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

/* Active and hover states - only text color changes */
.nav-item > a:hover {
    color: #efa22a !important;
}

.nav-item > a.active {
    color: #efa22a;
}
'''

def get_relative_path(file_path):
    """根據檔案路徑計算相對路徑前綴"""
    # 計算檔案在目錄結構中的層級
    rel_path = os.path.relpath(file_path, start='/Users/jirlong/Library/CloudStorage/Dropbox/Programming/WWW/journalism-ntu.github.io')
    depth = len(Path(rel_path).parent.parts)

    if depth == 0:
        return '', ''  # 根目錄
    else:
        return '../' * depth, '../' * depth

def update_file(file_path):
    """更新單個檔案的 banner 和 navigation"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        path_prefix, index_path = get_relative_path(file_path)

        # 判斷是否為 publications 目錄下的檔案
        is_publications = '/publications/' in file_path
        active_publications = ' active' if is_publications else ''

        # 更新 banner
        new_banner = NEW_BANNER_TEMPLATE.format(index_path=index_path + 'index.html')
        content = re.sub(
            re.escape(OLD_BANNER_PATTERN),
            new_banner,
            content
        )

        # 更新 navigation - 嘗試所有模式
        for pattern in OLD_NAV_PATTERNS:
            new_nav = NEW_NAV_TEMPLATE.format(
                path=path_prefix,
                active_publications=active_publications
            )
            content = re.sub(
                pattern,
                new_nav,
                content,
                flags=re.DOTALL
            )

        # 檢查是否需要添加下拉選單 CSS
        if 'nav-item {' not in content and '.nav-item > a:hover {' not in content:
            # 在 /* Sticky Navigation */ 之後添加下拉選單樣式
            css_pattern = r'(/\* Sticky Navigation \*/\s+\.site-nav\s*\{[^}]+\})'
            content = re.sub(
                css_pattern,
                r'\1\n' + DROPDOWN_CSS,
                content
            )

        # 如果內容有變化，寫入檔案
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """主函數：掃描並更新所有需要的檔案"""
    base_dir = '/Users/jirlong/Library/CloudStorage/Dropbox/Programming/WWW/journalism-ntu.github.io'

    # 需要更新的目錄
    directories = [
        'publications',
        'about',
        'faculty',
        'admissions',
        'students',
    ]

    updated_files = []

    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if os.path.exists(dir_path):
            for html_file in Path(dir_path).glob('*.html'):
                if 'old' not in str(html_file).lower():  # 跳過 *-old.html 檔案
                    if update_file(str(html_file)):
                        updated_files.append(str(html_file))
                        print(f"✓ Updated: {html_file.name}")

    # 也更新根目錄的主要頁面
    root_files = ['news.html', 'activities.html', 'resources.html', 'staff.html']
    for filename in root_files:
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            if update_file(file_path):
                updated_files.append(file_path)
                print(f"✓ Updated: {filename}")

    print(f"\n總共更新了 {len(updated_files)} 個檔案")
    return updated_files

if __name__ == '__main__':
    main()
