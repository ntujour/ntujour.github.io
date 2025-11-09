#!/usr/bin/env python3
"""
清理 images/faculty/ 中的舊照片檔案
只保留使用英文 ID 命名的照片
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'images' / 'faculty'
CSV_PATH = BASE_DIR / 'faculty-mapping.csv'

def get_valid_filenames():
    """從 CSV 中讀取有效的照片檔名"""
    valid_files = set()

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            new_filename = row['新照片檔名']
            if new_filename:
                valid_files.add(new_filename)

    return valid_files

def cleanup_photos():
    """清理舊照片"""
    print("=" * 70)
    print("清理舊照片檔案")
    print("=" * 70)

    # 獲取有效的檔名
    valid_files = get_valid_filenames()
    print(f"\n有效的照片檔案數: {len(valid_files)}")

    # 列出所有照片
    all_photos = list(IMAGES_DIR.glob('*.*'))
    print(f"目錄中的檔案數: {len(all_photos)}")

    # 找出要刪除的檔案
    to_delete = []
    for photo in all_photos:
        if photo.name not in valid_files:
            to_delete.append(photo)

    print(f"\n要刪除的檔案數: {len(to_delete)}")

    if to_delete:
        print("\n以下檔案將被刪除（GUID 格式的舊檔名）：")
        print("-" * 70)

        for i, photo in enumerate(to_delete, 1):
            size_kb = photo.stat().st_size / 1024
            print(f"  {i:2d}. {photo.name:45s} ({size_kb:7.1f} KB)")

        print("-" * 70)
        response = input("\n確定要刪除這些檔案嗎？ (y/N): ")

        if response.lower() == 'y':
            for photo in to_delete:
                photo.unlink()
                print(f"  ✓ 已刪除: {photo.name}")

            print(f"\n✓ 已刪除 {len(to_delete)} 個舊檔案")
        else:
            print("\n✗ 取消刪除")
    else:
        print("\n✓ 沒有需要刪除的檔案")

    # 顯示最終狀態
    print("\n" + "=" * 70)
    print("清理後的照片檔案")
    print("=" * 70)

    remaining_photos = list(IMAGES_DIR.glob('*.*'))
    remaining_photos.sort(key=lambda p: p.name)

    print(f"\n剩餘照片數: {len(remaining_photos)}\n")

    for i, photo in enumerate(remaining_photos, 1):
        size_kb = photo.stat().st_size / 1024
        print(f"  {i:2d}. {photo.name:30s} ({size_kb:7.1f} KB)")

    print("\n✓ 所有照片已使用英文 ID 命名")

if __name__ == '__main__':
    cleanup_photos()
