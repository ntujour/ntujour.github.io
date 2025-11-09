#!/usr/bin/env python3
"""
根據 faculty-mapping.csv 重新整理所有教師照片
- 使用英文 ID 統一命名
- 集中所有照片到 images/faculty/
- 更新所有相關的 JSON 和 HTML 檔案
"""

import csv
import json
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'images' / 'faculty'
CSV_PATH = BASE_DIR / 'faculty-mapping.csv'

# 確保目錄存在
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def find_photo_in_001(filename):
    """在 001 目錄中尋找照片檔案"""
    search_dirs = [
        BASE_DIR / '001' / 'Upload' / '366' / 'ckfile',
        BASE_DIR / '001' / 'Upload' / '690' / 'ckfile'
    ]

    for search_dir in search_dirs:
        photo_path = search_dir / filename
        if photo_path.exists():
            return photo_path

    return None

def find_photo_in_images(filename):
    """在現有 images/faculty 目錄中尋找照片"""
    photo_path = IMAGES_DIR / filename
    if photo_path.exists():
        return photo_path
    return None

def consolidate_photos():
    """整合所有教師照片"""
    print("=" * 70)
    print("根據 CSV 重新整理所有教師照片")
    print("=" * 70)

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # 統計資料
    stats = {
        'total': 0,
        'copied': 0,
        'already_exists': 0,
        'not_found': 0
    }

    # 建立照片對應表
    photo_mapping = {}

    print(f"\n處理 {len(rows)} 位教師的照片...")
    print("-" * 70)

    for row in rows:
        category = row['類別']
        name = row['姓名']
        english_id = row['英文ID']
        old_filename = row['照片檔名(001原檔)']
        new_filename = row['新照片檔名']

        if not english_id or not new_filename:
            continue

        stats['total'] += 1
        target_path = IMAGES_DIR / new_filename

        # 記錄對應關係
        photo_mapping[english_id] = {
            'name': name,
            'category': category,
            'old_file': old_filename,
            'new_file': new_filename,
            'target_path': f'images/faculty/{new_filename}'
        }

        # 檢查目標檔案是否已存在
        if target_path.exists():
            print(f"  ✓ {name:12s} ({english_id:20s}) - {new_filename:25s} [已存在]")
            stats['already_exists'] += 1
            continue

        # 先在 001 目錄中尋找
        source_path = None
        if old_filename:
            source_path = find_photo_in_001(old_filename)

        # 如果在 001 找不到，嘗試在現有 images/faculty 中尋找
        if not source_path:
            source_path = find_photo_in_images(old_filename)

        # 複製檔案
        if source_path:
            shutil.copy2(source_path, target_path)
            print(f"  ✓ {name:12s} ({english_id:20s}) - {new_filename:25s} [已複製]")
            stats['copied'] += 1
        else:
            print(f"  ✗ {name:12s} ({english_id:20s}) - {new_filename:25s} [找不到原檔]")
            stats['not_found'] += 1

    print("-" * 70)
    print(f"\n統計結果:")
    print(f"  總教師數: {stats['total']}")
    print(f"  已複製: {stats['copied']}")
    print(f"  已存在: {stats['already_exists']}")
    print(f"  找不到: {stats['not_found']}")

    return photo_mapping

def update_faculty_data_json(photo_mapping):
    """更新 faculty_data.json"""
    print("\n" + "=" * 70)
    print("更新 faculty_data.json")
    print("=" * 70)

    json_path = BASE_DIR / 'faculty_data.json'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = ['fulltime', 'parttime', 'honorary', 'joint', 'practical']

    for category in categories:
        if category not in data:
            continue

        for faculty in data[category]:
            # 對於 practical，使用 id 欄位
            if category == 'practical':
                faculty_id = faculty.get('id', '')
            else:
                # 對於其他類別，需要從 name 或其他方式推斷 ID
                # 先檢查現有 photo 路徑中的檔名
                old_photo = faculty.get('photo', '')
                if old_photo:
                    old_filename = Path(old_photo).name
                    # 從 photo_mapping 中找到對應的 ID
                    faculty_id = None
                    for fid, info in photo_mapping.items():
                        if info['new_file'] == old_filename or info['old_file'] == old_filename:
                            faculty_id = fid
                            break
                else:
                    continue

            if faculty_id in photo_mapping:
                new_photo = photo_mapping[faculty_id]['target_path']
                old_photo = faculty.get('photo', '')

                # 專任教師的照片路徑需要加 ../
                if category == 'fulltime':
                    faculty['photo'] = f'../{new_photo}'
                else:
                    faculty['photo'] = new_photo

                print(f"  ✓ {faculty.get('name', faculty_id):20s} → {new_photo}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n  ✓ faculty_data.json 已更新")

def verify_photos():
    """驗證所有照片"""
    print("\n" + "=" * 70)
    print("驗證照片檔案")
    print("=" * 70)

    photos = list(IMAGES_DIR.glob('*.*'))
    print(f"\nimages/faculty/ 目錄中共有 {len(photos)} 個檔案：\n")

    # 按檔名排序
    photos.sort(key=lambda p: p.name)

    for i, photo in enumerate(photos, 1):
        size_kb = photo.stat().st_size / 1024
        print(f"  {i:2d}. {photo.name:30s} ({size_kb:7.1f} KB)")

    print(f"\n  ✓ 所有照片已集中到 images/faculty/")

def main():
    """主函數"""
    # 1. 整合照片
    photo_mapping = consolidate_photos()

    # 2. 更新 JSON
    update_faculty_data_json(photo_mapping)

    # 3. 驗證照片
    verify_photos()

    print("\n" + "=" * 70)
    print("完成！所有教師照片已重新整理")
    print("=" * 70)
    print("\n目錄結構:")
    print("  images/")
    print("    └── faculty/        (所有教師照片，使用英文 ID 命名)")
    print("\n更新的檔案:")
    print("  ✓ faculty_data.json  (所有照片路徑已更新)")

if __name__ == '__main__':
    main()
