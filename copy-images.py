#!/usr/bin/env python3
"""
複製圖片檔案到 images/ 目錄並重新命名
根據文章的 slug 命名：slug-1.ext, slug-2.ext
"""

import csv
import os
import shutil
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / 'data' / 'content.csv'
IMAGES_DIR = BASE_DIR / 'images'
SOURCE_DIR = BASE_DIR / 'archive' / '001' / 'Upload'

def get_file_extension(url):
    """從 URL 獲取副檔名"""
    path = urlparse(url).path
    ext = Path(path).suffix
    return ext if ext else '.jpg'

def copy_and_rename_images():
    print("🖼️  開始處理圖片...")

    # 建立 images 目錄
    IMAGES_DIR.mkdir(exist_ok=True)

    # 讀取 CSV
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    updated_count = 0
    copied_count = 0
    error_count = 0

    for row in data:
        slug = row.get('slug', '')
        image_urls = row.get('image', '')

        if not image_urls:
            continue

        # 分割多張圖片
        urls = [url.strip() for url in image_urls.split('|||') if url.strip()]
        new_paths = []

        for idx, url in enumerate(urls, 1):
            # 移除前置網址
            if url.startswith('https://webpageprod-ws.ntu.edu.tw/'):
                relative_path = url.replace('https://webpageprod-ws.ntu.edu.tw/', '')
            else:
                relative_path = url

            # 原始檔案路徑（在 archive 中）
            source_file = BASE_DIR / 'archive' / relative_path

            # 如果帶有 @710x470，嘗試找原始檔
            if '@710x470' in str(source_file) or '@' in str(source_file):
                # 移除尺寸標記
                original_file = Path(str(source_file).split('@')[0] + Path(source_file).suffix)
                if original_file.exists():
                    source_file = original_file

            if not source_file.exists():
                print(f"  ⚠️  找不到檔案: {relative_path}")
                error_count += 1
                continue

            # 新檔名：slug-序號.副檔名
            ext = get_file_extension(url)
            new_filename = f"{slug}-{idx}{ext}"
            dest_file = IMAGES_DIR / new_filename

            # 複製檔案
            try:
                shutil.copy2(source_file, dest_file)
                new_paths.append(f"images/{new_filename}")
                copied_count += 1
                print(f"  ✅ {source_file.name} → {new_filename}")
            except Exception as e:
                print(f"  ❌ 複製失敗: {source_file.name} - {str(e)}")
                error_count += 1
                continue

        # 更新 CSV 中的圖片路徑
        if new_paths:
            row['image'] = '|||'.join(new_paths)
            updated_count += 1

    # 寫回 CSV
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n📊 處理完成:")
    print(f"   - 更新文章: {updated_count} 筆")
    print(f"   - 複製圖片: {copied_count} 個檔案")
    print(f"   - 錯誤: {error_count} 個")
    print(f"   - 圖片目錄: {IMAGES_DIR}")

if __name__ == '__main__':
    copy_and_rename_images()
