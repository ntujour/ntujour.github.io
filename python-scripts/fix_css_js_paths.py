#!/usr/bin/env python3
"""
修正子資料夾中的CSS和JS路徑
"""

import re
from pathlib import Path

def fix_resource_paths(file_path, base_dir):
    """修正單個文件中的CSS/JS路徑"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = 0

        # 取得當前文件相對於基礎目錄的相對路徑
        rel_file_path = file_path.relative_to(base_dir)
        current_dir = rel_file_path.parent

        # 只處理子資料夾中的文件
        if current_dir != Path('.'):
            # 修正 Scripts/ 路徑
            patterns = [
                (r'src=[\'"]Scripts/', r'src="../Scripts/'),
                (r'href=[\'"]Scripts/', r'href="../Scripts/'),
                # 修正 js/ 路徑
                (r'src=[\'"]js/', r'src="../js/'),
                (r'href=[\'"]js/', r'href="../js/'),
                # 修正 css/ 路徑
                (r'src=[\'"]css/', r'src="../css/'),
                (r'href=[\'"]css/', r'href="../css/'),
                # 修正 images/ 路徑
                (r'src=[\'"]images/', r'src="../images/'),
                (r'href=[\'"]images/', r'href="../images/'),
            ]

            for pattern, replacement in patterns:
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
        changes = fix_resource_paths(html_file, base_dir)
        if changes > 0:
            total_changes += changes
            files_updated += 1

    print("="*50)
    print(f"\n完成！")
    print(f"修正了 {files_updated} 個文件")
    print(f"總共修改了 {total_changes} 處資源路徑")

if __name__ == '__main__':
    main()
