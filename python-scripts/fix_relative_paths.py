#!/usr/bin/env python3
"""
修正子資料夾中的相對路徑
"""

import os
import re
from pathlib import Path

def fix_file_paths(file_path, base_dir):
    """修正單個文件中的路徑"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = 0

        # 取得當前文件相對於基礎目錄的相對路徑
        rel_file_path = file_path.relative_to(base_dir)
        current_dir = rel_file_path.parent

        # 如果文件在子資料夾中
        if current_dir != Path('.'):
            current_folder = current_dir.parts[0]

            # 修正指向同一資料夾的連結
            # 例如在 faculty/ 中，href="faculty/hsiehjl.html" -> href="hsiehjl.html"
            pattern = rf'href="{re.escape(current_folder)}/([^"]+)"'
            def same_folder_replacement(match):
                return f'href="{match.group(1)}"'

            new_content = re.sub(pattern, same_folder_replacement, content)
            if new_content != content:
                changes = len(re.findall(pattern, content))
                changes_made += changes
                content = new_content

            # 修正指向其他資料夾或根目錄的連結
            # 需要加上 ../
            folders = ['faculty', 'news', 'activities', 'photos', 'about', 'admissions', 'courses', 'publications']
            for folder in folders:
                if folder != current_folder:
                    # href="folder/file.html" -> href="../folder/file.html"
                    pattern = rf'href="({re.escape(folder)}/[^"]+)"'
                    def other_folder_replacement(match):
                        return f'href="../{match.group(1)}"'

                    new_content = re.sub(pattern, other_folder_replacement, content)
                    if new_content != content:
                        changes = len(re.findall(pattern, content))
                        changes_made += changes
                        content = new_content

            # 修正指向根目錄文件的連結
            # href="Default.html" -> href="../Default.html"
            root_files = ['Default.html', 'index.html', 'event.html', 'staff.html',
                         'resident-reporter.html', 'international-communication.html',
                         'academic-activity.html', 'SiteMap.html', 'Advanced_Search.html']

            for root_file in root_files:
                # 只匹配沒有路徑前綴的連結
                pattern = rf'href="(?<!\.\./)(?<![a-zA-Z0-9_-]/)({re.escape(root_file)})"'
                replacement = f'href="../{root_file}"'

                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    changes = len(re.findall(pattern, content))
                    changes_made += changes
                    content = new_content

        # 如果有變更，寫回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ 修正 {rel_file_path}: {changes_made} 處")
            return changes_made

        return 0

    except Exception as e:
        print(f"✗ 錯誤處理 {file_path}: {e}")
        return 0

def main():
    """主函數"""
    base_dir = Path(__file__).parent

    # 只處理子資料夾中的文件
    subdirs = ['faculty', 'news', 'activities', 'photos', 'about', 'admissions', 'courses', 'publications']

    all_files = []
    for subdir in subdirs:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            all_files.extend(subdir_path.glob('*.html'))

    print(f"找到 {len(all_files)} 個子資料夾中的HTML文件")
    print("="*50)

    total_changes = 0
    files_updated = 0

    for html_file in all_files:
        changes = fix_file_paths(html_file, base_dir)
        if changes > 0:
            total_changes += changes
            files_updated += 1

    print("="*50)
    print(f"\n完成！")
    print(f"修正了 {files_updated} 個文件")
    print(f"總共修改了 {total_changes} 處")

if __name__ == '__main__':
    main()
