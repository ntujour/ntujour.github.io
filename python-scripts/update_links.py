#!/usr/bin/env python3
"""
批量更新HTML文件中的連結，指向新的資料夾結構
"""

import os
import re
from pathlib import Path

# 定義連結映射
LINK_MAPPINGS = {
    # Faculty pages
    'hsiehjl.html': 'faculty/hsiehjl.html',
    'linly.html': 'faculty/linly.html',
    'hungcl.html': 'faculty/hungcl.html',
    'lincc.html': 'faculty/lincc.html',
    'RauchfleischA.html': 'faculty/RauchfleischA.html',
    'tsaihj.html': 'faculty/tsaihj.html',
    'chanii.html': 'faculty/chanii.html',
    'faculty.html': 'faculty/faculty.html',
    'fulltime-professor.html': 'faculty/fulltime-professor.html',
    'parttime-professor.html': 'faculty/parttime-professor.html',
    'practical-professor.html': 'faculty/practical-professor.html',
    'Professorjointappointment.html': 'faculty/Professorjointappointment.html',

    # News pages
    'News_n_35497_sms_26652.html': 'news/News_n_35497_sms_26652.html',

    # Activities pages
    'News2_n_35498_sms_26668.html': 'activities/News2_n_35498_sms_26668.html',

    # Photo pages
    'News_Photo_n_18801_sms_26671.html': 'photos/News_Photo_n_18801_sms_26671.html',

    # About pages
    'intro.html': 'about/intro.html',
    'mission.html': 'about/mission.html',
    'gallery.html': 'about/gallery.html',
    'transportation.html': 'about/transportation.html',

    # Admissions pages
    'admissions.html': 'admissions/admissions.html',
    'qualifying-exam.html': 'admissions/qualifying-exam.html',
    'entrance-exam.html': 'admissions/entrance-exam.html',
    'past-exam.html': 'admissions/past-exam.html',
    'international-students.html': 'admissions/international-students.html',
    'ochkmc-students.html': 'admissions/ochkmc-students.html',
    'mainland-chinese-students.html': 'admissions/mainland-chinese-students.html',

    # Course pages
    'course-map.html': 'courses/course-map.html',
    'course-regulation.html': 'courses/course-regulation.html',
    'statute-and-form.html': 'courses/statute-and-form.html',
    'cross-school-course-cooperation.html': 'courses/cross-school-course-cooperation.html',

    # Publication pages
    'e-report.html': 'publications/e-report.html',
    'master-thesis.html': 'publications/master-thesis.html',
    'books.html': 'publications/books.html',
    'ntu-news-forum.html': 'publications/ntu-news-forum.html',
}

def get_relative_path(from_file, to_file):
    """計算從 from_file 到 to_file 的相對路徑"""
    from_parts = Path(from_file).parent.parts
    to_parts = Path(to_file).parts

    # 如果在同一個資料夾，只需要檔名
    if len(from_parts) == len(to_parts) - 1:
        if from_parts == to_parts[:-1]:
            return to_parts[-1]

    # 如果 from_file 在子資料夾，to_file 在另一個資料夾或根目錄
    if len(from_parts) > 0:
        # 需要用 ../ 回到根目錄
        return '../' + to_file

    # from_file 在根目錄
    return to_file

def update_file_links(file_path, base_dir):
    """更新單個文件中的連結"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = 0

        # 取得當前文件相對於基礎目錄的相對路徑
        rel_file_path = file_path.relative_to(base_dir)

        # 更新每個連結
        for old_link, new_link in LINK_MAPPINGS.items():
            # 計算正確的相對路徑
            correct_relative_path = get_relative_path(rel_file_path, new_link)

            # 匹配 href="filename.html" 格式（不包含路徑的連結）
            pattern = rf'href="{re.escape(old_link)}"'
            replacement = f'href="{correct_relative_path}"'

            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes_made += len(re.findall(pattern, content))
                content = new_content

        # 如果有變更，寫回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ 更新 {file_path.name}: {changes_made} 個連結")
            return changes_made

        return 0

    except Exception as e:
        print(f"✗ 錯誤處理 {file_path}: {e}")
        return 0

def main():
    """主函數"""
    base_dir = Path(__file__).parent

    # 需要更新的根目錄HTML文件
    root_files = list(base_dir.glob('*.html'))

    # 需要更新的子目錄
    subdirs = ['faculty', 'news', 'activities', 'photos', 'about', 'admissions', 'courses', 'publications']

    all_files = root_files
    for subdir in subdirs:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            all_files.extend(subdir_path.glob('*.html'))

    print(f"找到 {len(all_files)} 個HTML文件")
    print("="*50)

    total_changes = 0
    files_updated = 0

    for html_file in all_files:
        changes = update_file_links(html_file, base_dir)
        if changes > 0:
            total_changes += changes
            files_updated += 1

    print("="*50)
    print(f"\n完成！")
    print(f"更新了 {files_updated} 個文件")
    print(f"總共修改了 {total_changes} 個連結")

if __name__ == '__main__':
    main()
