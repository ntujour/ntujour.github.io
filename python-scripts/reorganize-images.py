#!/usr/bin/env python3
"""
重組圖片結構 - 將 001 資料夾中的圖片移出到合理的位置
"""

import json
import shutil
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# 定義新的圖片目錄結構
IMAGES_DIR = BASE_DIR / 'images'
FACULTY_IMAGES = IMAGES_DIR / 'faculty'
REPORTS_DIR = IMAGES_DIR / 'reports'
REGULATIONS_DIR = IMAGES_DIR / 'regulations'

# 建立目錄
FACULTY_IMAGES.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
REGULATIONS_DIR.mkdir(parents=True, exist_ok=True)

# 教師照片對應表（從 faculty_data.json 中的檔案名對應到新的英文名）
FACULTY_NAME_MAP = {
    '1c2ce31c-d49b-4625-94bf-0b5b157effa5.jpg': 'lianyf.jpg',  # 梁玉芳
    '97e073af-b0de-4e40-b316-0ed9a790361d.jpg': 'hwangwf.jpg',  # 黃瑋峰
    '91603e44-a732-4695-97e5-ed5dc048ee9f.jpg': 'wangch.jpg',   # 王泰俐
    '4c12656a-53c0-441c-9e40-9a7e969dfb67.jpg': 'chenyt.jpg',   # 陳宜婷
    '53af1fb5-1aec-4f55-830b-edfbf0006864.jpg': 'archie-tse.jpg',  # Archie Tse
}

# 修業規定圖片對應
REGULATION_MAP = {
    'f6e21b3b-2c8e-4a87-9972-be430be20251.jpg': 'regulation-114.jpg',  # 114學年度
    '7cb2ba41-fe26-46b8-b8ca-29db26d7e659.jpg': 'regulation-113.jpg',  # 113學年度
    '2b5a9f1a-9ea7-4e73-a2ad-f65d63d27ba6.jpg': 'regulation-112.jpg',  # 112學年度
    '59f0b488-6984-4c53-a9e7-7a9a90fb4d77.jpg': 'regulation-111.jpg',  # 111學年度
}

def copy_faculty_images():
    """複製教師照片"""
    print("\n=== 複製教師照片 ===")
    for old_name, new_name in FACULTY_NAME_MAP.items():
        old_path = BASE_DIR / '001' / 'Upload' / '366' / 'ckfile' / old_name
        new_path = FACULTY_IMAGES / new_name

        if old_path.exists():
            shutil.copy2(old_path, new_path)
            print(f"  ✓ {old_name} → {new_name}")
        else:
            # 也檢查 690 目錄
            old_path_690 = BASE_DIR / '001' / 'Upload' / '690' / 'ckfile' / old_name
            if old_path_690.exists():
                shutil.copy2(old_path_690, new_path)
                print(f"  ✓ {old_name} (from 690) → {new_name}")
            else:
                print(f"  ✗ 找不到: {old_name}")

def copy_regulation_images():
    """複製修業規定圖片"""
    print("\n=== 複製修業規定圖片 ===")
    for old_name, new_name in REGULATION_MAP.items():
        old_path = BASE_DIR / '001' / 'Upload' / '366' / 'ckfile' / old_name
        new_path = REGULATIONS_DIR / new_name

        if old_path.exists():
            shutil.copy2(old_path, new_path)
            print(f"  ✓ {old_name} → {new_name}")
        else:
            print(f"  ✗ 找不到: {old_name}")

def copy_report_files():
    """複製所報檔案（從 data/e-reports.csv）"""
    print("\n=== 複製所報檔案 ===")
    csv_path = BASE_DIR / 'data' / 'e-reports.csv'

    if not csv_path.exists():
        print("  ✗ e-reports.csv 不存在")
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]  # Skip header

    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 4 and parts[3]:
            issue = parts[0]
            old_path_str = parts[3]
            old_path = BASE_DIR / old_path_str

            if old_path.exists():
                ext = old_path.suffix
                new_name = f'report-{issue.zfill(2)}{ext}'
                new_path = REPORTS_DIR / new_name
                shutil.copy2(old_path, new_path)
                print(f"  ✓ 第{issue}期 → {new_name}")

def update_faculty_data():
    """更新 faculty_data.json"""
    print("\n=== 更新 faculty_data.json ===")
    json_path = BASE_DIR / 'faculty_data.json'

    if not json_path.exists():
        print("  ✗ faculty_data.json 不存在")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 更新 practical 教師的照片路徑
    if 'practical' in data:
        for faculty in data['practical']:
            if 'photo' in faculty and faculty['photo']:
                old_photo = faculty['photo']
                # 從路徑中提取檔案名
                filename = old_photo.split('/')[-1]
                if filename in FACULTY_NAME_MAP:
                    new_photo = f'images/faculty/{FACULTY_NAME_MAP[filename]}'
                    faculty['photo'] = new_photo
                    print(f"  ✓ {faculty['name']}: {old_photo} → {new_photo}")

    # 寫回檔案
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("  ✓ faculty_data.json 已更新")

def update_e_reports_csv():
    """更新 e-reports.csv"""
    print("\n=== 更新 e-reports.csv ===")
    csv_path = BASE_DIR / 'data' / 'e-reports.csv'

    if not csv_path.exists():
        print("  ✗ e-reports.csv 不存在")
        return

    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = lines[0]
    new_lines = [header]

    for line in lines[1:]:
        parts = line.strip().split(',')
        if len(parts) >= 4 and parts[3]:
            issue = parts[0]
            old_path = parts[3]
            ext = Path(old_path).suffix
            new_path = f'images/reports/report-{issue.zfill(2)}{ext}'
            parts[3] = new_path
            new_lines.append(','.join(parts) + '\n')
        else:
            new_lines.append(line)

    with open(csv_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("  ✓ e-reports.csv 已更新")

def update_student_learning_html():
    """更新 student-learning.html 中的圖片路徑"""
    print("\n=== 更新 student-learning.html ===")
    html_path = BASE_DIR / 'students' / 'student-learning.html'

    if not html_path.exists():
        print("  ✗ student-learning.html 不存在")
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替換修業規定圖片路徑
    for old_name, new_name in REGULATION_MAP.items():
        old_path = f'001/Upload/366/ckfile/{old_name}'
        new_path = f'../images/regulations/{new_name}'
        content = content.replace(old_path, new_path)
        if old_path in content or new_path in content:
            print(f"  ✓ {old_name} → {new_name}")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✓ student-learning.html 已更新")

def main():
    """主函數"""
    print("=" * 60)
    print("重組圖片結構")
    print("=" * 60)

    # 複製檔案
    copy_faculty_images()
    copy_regulation_images()
    copy_report_files()

    # 更新引用
    update_faculty_data()
    update_e_reports_csv()
    update_student_learning_html()

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)
    print("\n新的目錄結構：")
    print("  images/")
    print("    ├── faculty/        (教師照片)")
    print("    ├── reports/        (所報 PDF/PNG)")
    print("    └── regulations/    (修業規定圖片)")

if __name__ == '__main__':
    main()
