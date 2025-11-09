#!/usr/bin/env python3
"""
創建新格式的頁面：
1. staff.html - 行政人員
2. parttime-professor.html - 兼任教師
3. fulltime-professor.html - 專任教師
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# 7位專任教師的資料
FULLTIME_FACULTY = [
    {"name": "謝吉隆", "title": "副教授兼所長", "filename": "jerryhsieh", "photo": "images/faculty/jerryhsieh.jpg"},
    {"name": "林麗雲", "title": "教授", "filename": "lihyunlin", "photo": "images/faculty/lihyunlin.jpg"},
    {"name": "洪貞玲", "title": "教授", "filename": "clhung", "photo": "images/faculty/clhung.jpg"},
    {"name": "林照真", "title": "教授", "filename": "carolinelin", "photo": "images/faculty/carolinelin.jpg"},
    {"name": "蔡蕙如", "title": "副教授", "filename": "tsaihuiju", "photo": "images/faculty/tsaihuiju.jpg"},
    {"name": "張錦華", "title": "兼任教授", "filename": "chanii311", "photo": "images/faculty/chanii311.jpg"},
    {"name": "Adrian Rauchfleisch", "title": "助理教授", "filename": "RauchfleischA", "photo": "images/faculty/RauchfleischA.jpg"}
]

def create_staff_html():
    """創建行政人員頁面"""
    html = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>國立臺灣大學新聞研究所 - 行政人員</title>
    <meta name="description" content="國立臺灣大學新聞研究所行政人員介紹">
    <link rel="icon" href="images/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="css/tailwind.css">
    <style>
        /* 原始色系 */
        .site-banner {
            background-color: #f5f5f5;
            background-image: url('images/hd-bg-lt.png'), url('images/hd-bg-rt.png');
            background-position: left bottom, right bottom;
            background-repeat: no-repeat, no-repeat;
            background-size: auto 60%, auto 60%;
            position: relative;
        }
        .site-sitemap { background-color: #efa22a; }
        .site-footer { background-color: #3e0f0f; }
        body { font-size: 15px; line-height: 1.6; }
        .container-1200 { max-width: 1200px; margin: 0 auto; padding: 0 15px; }

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

        /* Staff Card */
        .staff-card {
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 24px;
            transition: box-shadow 0.2s;
        }
        .staff-card:hover {
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body class="bg-white">
    <!-- Banner -->
    <header class="site-banner py-6">
        <div class="container-1200">
            <h1 class="text-4xl font-bold text-gray-800 mb-2">
                <a href="index.html" class="hover:text-gray-600 transition" style="text-decoration: none; color: inherit;">國立臺灣大學新聞研究所</a>
            </h1>
            <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
            <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="site-nav">
        <div class="container-1200">
            <ul class="flex flex-wrap items-center gap-2 py-3">
                <li class="nav-item has-dropdown">
                    <a href="about/intro.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">關於我們</a>
                    <div class="dropdown-menu">
                        <a href="about/intro.html">本所簡介</a>
                        <a href="about/transportation.html">交通資訊</a>
                        <a href="about/donate.html">捐款支持</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="faculty/faculty.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">師資陣容</a>
                    <div class="dropdown-menu">
                        <a href="faculty/fulltime-professor.html">專任教師</a>
                        <a href="faculty/practical-professor.html">實務教師</a>
                        <a href="faculty/parttime-professor.html">兼任教師</a>
                        <a href="faculty/honorary-professor-detail.html">名譽教授</a>
                        <a href="faculty/joint-professor-detail.html">合聘教師</a>
                        <a href="staff.html">行政人員</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="admissions/admissions.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">入學資訊</a>
                    <div class="dropdown-menu">
                        <a href="admissions/qualifying-exam.html">推甄入學</a>
                        <a href="admissions/entrance-exam.html">入學考試</a>
                        <a href="admissions/past-exam.html">歷屆考古題</a>                        <a href="admissions/international-students.html">國際生</a>
                        <a href="admissions/ochkmc-students.html">港澳僑生</a>
                    </div>
                </li>
                <li class="nav-item"><a href="students/student-learning.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">學生學習</a></li>
                <li class="nav-item"><a href="publications/e-report.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">出版發表</a></li>
                <li class="nav-item"><a href="news.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">最新消息</a></li>
                <li class="nav-item"><a href="resources.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">相關資源</a></li>
            </ul>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="bg-gray-50 py-8">
        <div class="container-1200">
            <nav class="text-sm text-gray-600 mb-4">
                <a href="faculty/faculty.html" class="hover:text-gray-900">師資陣容</a>
                <span class="mx-2">/</span>
                <span class="text-gray-900">行政人員</span>
            </nav>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">行政人員</h2>
            <p class="text-gray-600">專業的行政服務團隊</p>
        </div>
    </section>

    <!-- Staff List -->
    <section class="py-12 bg-white">
        <div class="container-1200">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Staff cards will be added here -->
                <div class="staff-card">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">辦公室主任</h3>
                    <p class="text-gray-600 mb-1">姓名：待更新</p>
                    <p class="text-gray-600 mb-1">電話：(02) 3366-3383</p>
                    <p class="text-gray-600">Email：jour@ntu.edu.tw</p>
                </div>

                <div class="staff-card">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">行政助理</h3>
                    <p class="text-gray-600 mb-1">姓名：待更新</p>
                    <p class="text-gray-600 mb-1">電話：(02) 3366-3383</p>
                    <p class="text-gray-600">Email：jour@ntu.edu.tw</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Sitemap (Quick Links) Section -->
    <section class="site-sitemap py-8">
        <div class="container-1200">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">認識本所</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="about/intro.html" class="text-gray-700 hover:text-gray-900">本所介紹</a></li>
                        <li><a href="about/mission.html" class="text-gray-700 hover:text-gray-900">宗旨與目標</a></li>
                        <li><a href="about/gallery.html" class="text-gray-700 hover:text-gray-900">新聞所圖集</a></li>
                        <li><a href="about/transportation.html" class="text-gray-700 hover:text-gray-900">聯絡我們</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">師資陣容</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="faculty/faculty.html" class="text-gray-700 hover:text-gray-900">師資總覽</a></li>
                        <li><a href="faculty/fulltime-professor.html" class="text-gray-700 hover:text-gray-900">專任教師</a></li>
                        <li><a href="faculty/parttime-professor.html" class="text-gray-700 hover:text-gray-900">兼任教師</a></li>
                        <li><a href="staff.html" class="text-gray-700 hover:text-gray-900">行政人員</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">入學資訊</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="admissions/admissions.html" class="text-gray-700 hover:text-gray-900">招生總覽</a></li>
                        <li><a href="admissions/qualifying-exam.html" class="text-gray-700 hover:text-gray-900">甄試入學</a></li>
                        <li><a href="admissions/entrance-exam.html" class="text-gray-700 hover:text-gray-900">招生考試</a></li>
                        <li><a href="admissions/past-exam.html" class="text-gray-700 hover:text-gray-900">歷屆考古題</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">課程與出版</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="students/course-map.html" class="text-gray-700 hover:text-gray-900">課程地圖</a></li>
                        <li><a href="students/course-regulation.html" class="text-gray-700 hover:text-gray-900">修業規定</a></li>
                        <li><a href="publications/e-report.html" class="text-gray-700 hover:text-gray-900">前期所報</a></li>
                        <li><a href="publications/master-thesis.html" class="text-gray-700 hover:text-gray-900">畢業生論文</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer py-10 text-gray-400">
        <div class="container-1200">
            <div class="mb-8">
                <ul class="space-y-2 text-sm">
                    <li>地址：106台北市大安區羅斯福路四段1號</li>
                    <li>電話：(02) 3366-3383</li>
                    <li>Email：jour@ntu.edu.tw</li>
                </ul>
            </div>

            <div class="pt-6 border-t border-gray-700 text-center text-sm">
                <p>&copy; 2025 國立臺灣大學新聞研究所 版權所有</p>
            </div>
        </div>
    </footer>
</body>
</html>
'''

    filepath = BASE_DIR / 'staff.html'
    # Backup old file
    if filepath.exists():
        backup_path = BASE_DIR / 'staff.html.backup'
        os.rename(filepath, backup_path)
        print(f"✓ Backed up staff.html to staff.html.backup")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Created new staff.html")


def create_parttime_professor_html():
    """創建兼任教師頁面"""
    html = '''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>國立臺灣大學新聞研究所 - 兼任教師</title>
    <meta name="description" content="國立臺灣大學新聞研究所兼任教師介紹">
    <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="../css/tailwind.css">
    <style>
        /* 原始色系 */
        .site-banner {
            background-color: #f5f5f5;
            background-image: url('../images/hd-bg-lt.png'), url('../images/hd-bg-rt.png');
            background-position: left bottom, right bottom;
            background-repeat: no-repeat, no-repeat;
            background-size: auto 60%, auto 60%;
            position: relative;
        }
        .site-sitemap { background-color: #efa22a; }
        .site-footer { background-color: #3e0f0f; }
        body { font-size: 15px; line-height: 1.6; }
        .container-1200 { max-width: 1200px; margin: 0 auto; padding: 0 15px; }

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

        /* Faculty Card */
        .faculty-card {
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 24px;
            transition: box-shadow 0.2s;
        }
        .faculty-card:hover {
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body class="bg-white">
    <!-- Banner -->
    <header class="site-banner py-6">
        <div class="container-1200">
            <h1 class="text-4xl font-bold text-gray-800 mb-2">
                <a href="../index.html" class="hover:text-gray-600 transition" style="text-decoration: none; color: inherit;">國立臺灣大學新聞研究所</a>
            </h1>
            <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
            <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="site-nav">
        <div class="container-1200">
            <ul class="flex flex-wrap items-center gap-2 py-3">
                <li class="nav-item has-dropdown">
                    <a href="../about/intro.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">關於我們</a>
                    <div class="dropdown-menu">
                        <a href="../about/intro.html">本所簡介</a>
                        <a href="../about/transportation.html">交通資訊</a>
                        <a href="../about/donate.html">捐款支持</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="../faculty/faculty.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">師資陣容</a>
                    <div class="dropdown-menu">
                        <a href="../faculty/fulltime-professor.html">專任教師</a>
                        <a href="../faculty/practical-professor.html">實務教師</a>
                        <a href="../faculty/parttime-professor.html">兼任教師</a>
                        <a href="../faculty/honorary-professor-detail.html">名譽教授</a>
                        <a href="../faculty/joint-professor-detail.html">合聘教師</a>
                        <a href="../staff.html">行政人員</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="../admissions/admissions.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">入學資訊</a>
                    <div class="dropdown-menu">
                        <a href="../admissions/qualifying-exam.html">推甄入學</a>
                        <a href="../admissions/entrance-exam.html">入學考試</a>
                        <a href="../admissions/past-exam.html">歷屆考古題</a>                        <a href="../admissions/international-students.html">國際生</a>
                        <a href="../admissions/ochkmc-students.html">港澳僑生</a>
                    </div>
                </li>
                <li class="nav-item"><a href="../students/student-learning.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">學生學習</a></li>
                <li class="nav-item"><a href="../publications/e-report.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">出版發表</a></li>
                <li class="nav-item"><a href="../news.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">最新消息</a></li>
                <li class="nav-item"><a href="../resources.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">相關資源</a></li>
            </ul>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="bg-gray-50 py-8">
        <div class="container-1200">
            <nav class="text-sm text-gray-600 mb-4">
                <a href="faculty.html" class="hover:text-gray-900">師資陣容</a>
                <span class="mx-2">/</span>
                <span class="text-gray-900">兼任教師</span>
            </nav>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">兼任教師</h2>
            <p class="text-gray-600">豐富的兼任教師陣容</p>
        </div>
    </section>

    <!-- Faculty List -->
    <section class="py-12 bg-white">
        <div class="container-1200">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Faculty cards will be added here -->
                <div class="faculty-card">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">兼任教授</h3>
                    <p class="text-gray-600 mb-2">姓名：待更新</p>
                    <p class="text-gray-600 text-sm">專長領域：待更新</p>
                </div>

                <div class="faculty-card">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">兼任副教授</h3>
                    <p class="text-gray-600 mb-2">姓名：待更新</p>
                    <p class="text-gray-600 text-sm">專長領域：待更新</p>
                </div>

                <div class="faculty-card">
                    <h3 class="text-lg font-bold text-gray-900 mb-2">兼任助理教授</h3>
                    <p class="text-gray-600 mb-2">姓名：待更新</p>
                    <p class="text-gray-600 text-sm">專長領域：待更新</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Sitemap (Quick Links) Section -->
    <section class="site-sitemap py-8">
        <div class="container-1200">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">認識本所</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../about/intro.html" class="text-gray-700 hover:text-gray-900">本所介紹</a></li>
                        <li><a href="../about/mission.html" class="text-gray-700 hover:text-gray-900">宗旨與目標</a></li>
                        <li><a href="../about/gallery.html" class="text-gray-700 hover:text-gray-900">新聞所圖集</a></li>
                        <li><a href="../about/transportation.html" class="text-gray-700 hover:text-gray-900">聯絡我們</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">師資陣容</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../faculty/faculty.html" class="text-gray-700 hover:text-gray-900">師資總覽</a></li>
                        <li><a href="../faculty/fulltime-professor.html" class="text-gray-700 hover:text-gray-900">專任教師</a></li>
                        <li><a href="../faculty/parttime-professor.html" class="text-gray-700 hover:text-gray-900">兼任教師</a></li>
                        <li><a href="../staff.html" class="text-gray-700 hover:text-gray-900">行政人員</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">入學資訊</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../admissions/admissions.html" class="text-gray-700 hover:text-gray-900">招生總覽</a></li>
                        <li><a href="../admissions/qualifying-exam.html" class="text-gray-700 hover:text-gray-900">甄試入學</a></li>
                        <li><a href="../admissions/entrance-exam.html" class="text-gray-700 hover:text-gray-900">招生考試</a></li>
                        <li><a href="../admissions/past-exam.html" class="text-gray-700 hover:text-gray-900">歷屆考古題</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">課程與出版</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../students/course-map.html" class="text-gray-700 hover:text-gray-900">課程地圖</a></li>
                        <li><a href="../students/course-regulation.html" class="text-gray-700 hover:text-gray-900">修業規定</a></li>
                        <li><a href="../publications/e-report.html" class="text-gray-700 hover:text-gray-900">前期所報</a></li>
                        <li><a href="../publications/master-thesis.html" class="text-gray-700 hover:text-gray-900">畢業生論文</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer py-10 text-gray-400">
        <div class="container-1200">
            <div class="mb-8">
                <ul class="space-y-2 text-sm">
                    <li>地址：106台北市大安區羅斯福路四段1號</li>
                    <li>電話：(02) 3366-3383</li>
                    <li>Email：jour@ntu.edu.tw</li>
                </ul>
            </div>

            <div class="pt-6 border-t border-gray-700 text-center text-sm">
                <p>&copy; 2025 國立臺灣大學新聞研究所 版權所有</p>
            </div>
        </div>
    </footer>
</body>
</html>
'''

    filepath = BASE_DIR / 'faculty' / 'parttime-professor.html'
    # Backup old file
    if filepath.exists():
        backup_path = BASE_DIR / 'faculty' / 'parttime-professor.html.backup'
        os.rename(filepath, backup_path)
        print(f"✓ Backed up parttime-professor.html to parttime-professor.html.backup")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Created new parttime-professor.html")


def create_fulltime_professor_html():
    """創建專任教師頁面（包含7位教師的卡片）"""

    # Generate faculty cards HTML
    faculty_cards_html = ""
    for faculty in FULLTIME_FACULTY:
        faculty_cards_html += f'''
                <div class="faculty-card">
                    <div class="flex items-center gap-4 mb-4">
                        <img src="../{faculty['photo']}" alt="{faculty['name']}" class="w-24 h-24 rounded-full object-cover border-2 border-gray-200">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900">{faculty['name']}</h3>
                            <p class="text-gray-600">{faculty['title']}</p>
                        </div>
                    </div>
                    <a href="{faculty['filename']}.html" class="inline-block px-4 py-2 bg-red-900 text-white rounded hover:bg-red-800 transition">查看詳細資料</a>
                </div>
'''

    html = f'''<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>國立臺灣大學新聞研究所 - 專任教師</title>
    <meta name="description" content="國立臺灣大學新聞研究所專任教師介紹">
    <link rel="icon" href="../images/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="../css/tailwind.css">
    <style>
        /* 原始色系 */
        .site-banner {{
            background-color: #f5f5f5;
            background-image: url('../images/hd-bg-lt.png'), url('../images/hd-bg-rt.png');
            background-position: left bottom, right bottom;
            background-repeat: no-repeat, no-repeat;
            background-size: auto 60%, auto 60%;
            position: relative;
        }}
        .site-sitemap {{ background-color: #efa22a; }}
        .site-footer {{ background-color: #3e0f0f; }}
        body {{ font-size: 15px; line-height: 1.6; }}
        .container-1200 {{ max-width: 1200px; margin: 0 auto; padding: 0 15px; }}

        /* Sticky Navigation */
        .site-nav {{
            background-color: #671919;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        /* Navigation dropdown */
        .nav-item {{
            position: relative;
        }}

        .nav-item.has-dropdown > a::after {{
            content: ' ▼';
            font-size: 0.7em;
            margin-left: 4px;
        }}

        .dropdown-menu {{
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background-color: #671919;
            min-width: 180px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
            padding: 0.5rem 0;
        }}

        .nav-item:hover .dropdown-menu {{
            display: block;
        }}

        .dropdown-menu a {{
            display: block;
            padding: 0.5rem 1.25rem;
            color: #ffffff;
            text-decoration: none;
            transition: background-color 0.15s;
        }}

        .dropdown-menu a:hover {{
            background-color: #991b1b;
        }}

        /* Active and hover states */
        .nav-item > a:hover {{
            color: #efa22a !important;
        }}

        .nav-item > a.active {{
            color: #efa22a;
        }}

        /* Faculty Card */
        .faculty-card {{
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 24px;
            transition: box-shadow 0.2s;
        }}
        .faculty-card:hover {{
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body class="bg-white">
    <!-- Banner -->
    <header class="site-banner py-6">
        <div class="container-1200">
            <h1 class="text-4xl font-bold text-gray-800 mb-2">
                <a href="../index.html" class="hover:text-gray-600 transition" style="text-decoration: none; color: inherit;">國立臺灣大學新聞研究所</a>
            </h1>
            <p class="text-gray-700 text-base mb-1">Graduate Institute of Journalism, National Taiwan University</p>
            <p class="text-gray-600 text-base">培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才</p>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="site-nav">
        <div class="container-1200">
            <ul class="flex flex-wrap items-center gap-2 py-3">
                <li class="nav-item has-dropdown">
                    <a href="../about/intro.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">關於我們</a>
                    <div class="dropdown-menu">
                        <a href="../about/intro.html">本所簡介</a>
                        <a href="../about/transportation.html">交通資訊</a>
                        <a href="../about/donate.html">捐款支持</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="../faculty/faculty.html" class="px-5 py-2.5 text-base text-white rounded font-medium transition">師資陣容</a>
                    <div class="dropdown-menu">
                        <a href="../faculty/fulltime-professor.html">專任教師</a>
                        <a href="../faculty/practical-professor.html">實務教師</a>
                        <a href="../faculty/parttime-professor.html">兼任教師</a>
                        <a href="../faculty/honorary-professor-detail.html">名譽教授</a>
                        <a href="../faculty/joint-professor-detail.html">合聘教師</a>
                        <a href="../staff.html">行政人員</a>
                    </div>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="../admissions/admissions.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">入學資訊</a>
                    <div class="dropdown-menu">
                        <a href="../admissions/qualifying-exam.html">推甄入學</a>
                        <a href="../admissions/entrance-exam.html">入學考試</a>
                        <a href="../admissions/past-exam.html">歷屆考古題</a>                        <a href="../admissions/international-students.html">國際生</a>
                        <a href="../admissions/ochkmc-students.html">港澳僑生</a>
                    </div>
                </li>
                <li class="nav-item"><a href="../students/student-learning.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">學生學習</a></li>
                <li class="nav-item"><a href="../publications/e-report.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">出版發表</a></li>
                <li class="nav-item"><a href="../news.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">最新消息</a></li>
                <li class="nav-item"><a href="../resources.html" class="px-5 py-2.5 text-base text-white  rounded font-medium transition">相關資源</a></li>
            </ul>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="bg-gray-50 py-8">
        <div class="container-1200">
            <nav class="text-sm text-gray-600 mb-4">
                <a href="faculty.html" class="hover:text-gray-900">師資陣容</a>
                <span class="mx-2">/</span>
                <span class="text-gray-900">專任教師</span>
            </nav>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">專任教師</h2>
            <p class="text-gray-600">優秀的專任教師團隊</p>
        </div>
    </section>

    <!-- Faculty List -->
    <section class="py-12 bg-white">
        <div class="container-1200">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
{faculty_cards_html}
            </div>
        </div>
    </section>

    <!-- Sitemap (Quick Links) Section -->
    <section class="site-sitemap py-8">
        <div class="container-1200">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">認識本所</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../about/intro.html" class="text-gray-700 hover:text-gray-900">本所介紹</a></li>
                        <li><a href="../about/mission.html" class="text-gray-700 hover:text-gray-900">宗旨與目標</a></li>
                        <li><a href="../about/gallery.html" class="text-gray-700 hover:text-gray-900">新聞所圖集</a></li>
                        <li><a href="../about/transportation.html" class="text-gray-700 hover:text-gray-900">聯絡我們</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">師資陣容</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../faculty/faculty.html" class="text-gray-700 hover:text-gray-900">師資總覽</a></li>
                        <li><a href="../faculty/fulltime-professor.html" class="text-gray-700 hover:text-gray-900">專任教師</a></li>
                        <li><a href="../faculty/parttime-professor.html" class="text-gray-700 hover:text-gray-900">兼任教師</a></li>
                        <li><a href="../staff.html" class="text-gray-700 hover:text-gray-900">行政人員</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">入學資訊</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../admissions/admissions.html" class="text-gray-700 hover:text-gray-900">招生總覽</a></li>
                        <li><a href="../admissions/qualifying-exam.html" class="text-gray-700 hover:text-gray-900">甄試入學</a></li>
                        <li><a href="../admissions/entrance-exam.html" class="text-gray-700 hover:text-gray-900">招生考試</a></li>
                        <li><a href="../admissions/past-exam.html" class="text-gray-700 hover:text-gray-900">歷屆考古題</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-lg font-bold text-gray-900 mb-3">課程與出版</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="../students/course-map.html" class="text-gray-700 hover:text-gray-900">課程地圖</a></li>
                        <li><a href="../students/course-regulation.html" class="text-gray-700 hover:text-gray-900">修業規定</a></li>
                        <li><a href="../publications/e-report.html" class="text-gray-700 hover:text-gray-900">前期所報</a></li>
                        <li><a href="../publications/master-thesis.html" class="text-gray-700 hover:text-gray-900">畢業生論文</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer py-10 text-gray-400">
        <div class="container-1200">
            <div class="mb-8">
                <ul class="space-y-2 text-sm">
                    <li>地址：106台北市大安區羅斯福路四段1號</li>
                    <li>電話：(02) 3366-3383</li>
                    <li>Email：jour@ntu.edu.tw</li>
                </ul>
            </div>

            <div class="pt-6 border-t border-gray-700 text-center text-sm">
                <p>&copy; 2025 國立臺灣大學新聞研究所 版權所有</p>
            </div>
        </div>
    </footer>
</body>
</html>
'''

    filepath = BASE_DIR / 'faculty' / 'fulltime-professor.html'
    # Backup old file
    if filepath.exists():
        backup_path = BASE_DIR / 'faculty' / 'fulltime-professor.html.backup'
        os.rename(filepath, backup_path)
        print(f"✓ Backed up fulltime-professor.html to fulltime-professor.html.backup")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Created new fulltime-professor.html with {len(FULLTIME_FACULTY)} faculty members")


def main():
    """主函數"""
    print("開始創建新格式頁面...")
    create_staff_html()
    create_parttime_professor_html()
    create_fulltime_professor_html()
    print("\n✅ 所有頁面已成功創建！")


if __name__ == '__main__':
    main()
