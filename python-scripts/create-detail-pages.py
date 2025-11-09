#!/usr/bin/env python3
"""
創建 fulltime-professor.html 和 parttime-professor.html
使用 honorary-professor-detail.html 的 detail 格式
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

# Fulltime professor HTML
fulltime_html = '''<!DOCTYPE html>
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


        /* 教師介紹卡片 */
        .faculty-detail-card {
            scroll-margin-top: 100px;
        }
        .faculty-detail-photo {
            width: 200px;
            height: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
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
                <span class="text-gray-900">專任教師</span>
            </nav>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">專任教師</h2>
            <p class="text-gray-600">優秀的專任教師團隊</p>
        </div>
    </section>

    <!-- Faculty Details -->
    <section class="py-12 bg-white">
        <div class="container-1200">
            <div class="space-y-12" id="faculty-details">
                <!-- Faculty details will be loaded dynamically -->
                <div class="text-center py-12 text-gray-500">載入中...</div>
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

    <script src="../js/fulltime-faculty-detail.js"></script>
</body>
</html>
'''

# Parttime professor HTML (same structure, different title/description)
parttime_html = fulltime_html.replace(
    '專任教師', '兼任教師'
).replace(
    'fulltime-faculty-detail.js', 'parttime-faculty-detail.js'
).replace(
    '優秀的專任教師團隊', '豐富的兼任教師陣容'
).replace(
    '<title>國立臺灣大學新聞研究所 - 兼任教師</title>',
    '<title>國立臺灣大學新聞研究所 - 兼任教師</title>'
).replace(
    '<meta name="description" content="國立臺灣大學新聞研究所兼任教師介紹">',
    '<meta name="description" content="國立臺灣大學新聞研究所兼任教師介紹">'
)

def main():
    """主函數"""
    # Save fulltime-professor.html
    fulltime_path = BASE_DIR / 'faculty' / 'fulltime-professor.html'
    with open(fulltime_path, 'w', encoding='utf-8') as f:
        f.write(fulltime_html)
    print(f"✓ 已創建 fulltime-professor.html (detail 格式)")

    # Save parttime-professor.html
    parttime_path = BASE_DIR / 'faculty' / 'parttime-professor.html'
    with open(parttime_path, 'w', encoding='utf-8') as f:
        f.write(parttime_html)
    print(f"✓ 已創建 parttime-professor.html (detail 格式)")

if __name__ == '__main__':
    main()
