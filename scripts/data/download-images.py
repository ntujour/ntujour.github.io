#!/usr/bin/env python3
"""
下載圖片檔案到 images/ 目錄並重新命名
根據文章的 slug 命名：slug-1.ext, slug-2.ext
同時更新 CSV 中的圖片路徑
"""

import csv
import os
import urllib.request
from pathlib import Path
from urllib.parse import urlparse
import time

BASE_DIR = Path(__file__).parent.parent
CSV_FILE = BASE_DIR / 'data' / 'content.csv'
IMAGES_DIR = BASE_DIR / 'images'

def get_file_extension(url):
    """從 URL 獲取副檔名"""
    path = urlparse(url).path
    ext = Path(path).suffix
    # 如果副檔名太長（包含參數），只取前面部分
    if len(ext) > 5:
        ext = '.jpg'
    return ext if ext else '.jpg'

def download_and_rename_images():
    print("🖼️  開始下載圖片...")

    # 建立 images 目錄
    IMAGES_DIR.mkdir(exist_ok=True)

    # 讀取 CSV
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    updated_count = 0
    downloaded_count = 0
    error_count = 0
    skipped_count = 0

    for row in data:
        slug = row.get('slug', '')
        image_urls = row.get('image', '')

        if not image_urls:
            continue

        # 分割多張圖片
        urls = [url.strip() for url in image_urls.split('|||') if url.strip()]
        new_paths = []

        for idx, url in enumerate(urls, 1):
            # 新檔名：slug-序號.副檔名
            ext = get_file_extension(url)
            new_filename = f"{slug}-{idx}{ext}"
            dest_file = IMAGES_DIR / new_filename

            # 如果檔案已存在，跳過
            if dest_file.exists():
                new_paths.append(f"images/{new_filename}")
                skipped_count += 1
                print(f"  ⏭️  已存在: {new_filename}")
                continue

            # 下載檔案
            try:
                print(f"  ⬇️  下載: {url}")
                headers = {'User-Agent': 'Mozilla/5.0'}
                req = urllib.request.Request(url, headers=headers)

                with urllib.request.urlopen(req, timeout=10) as response:
                    with open(dest_file, 'wb') as out_file:
                        out_file.write(response.read())

                new_paths.append(f"images/{new_filename}")
                downloaded_count += 1
                print(f"  ✅ 儲存: {new_filename}")

                # 避免請求太快
                time.sleep(0.5)

            except Exception as e:
                print(f"  ❌ 下載失敗: {url[:80]}... - {str(e)}")
                error_count += 1
                # 下載失敗的話，保留原 URL
                new_paths.append(url)
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
    print(f"   - 下載圖片: {downloaded_count} 個檔案")
    print(f"   - 已存在跳過: {skipped_count} 個")
    print(f"   - 下載失敗: {error_count} 個")
    print(f"   - 圖片目錄: {IMAGES_DIR}")

if __name__ == '__main__':
    download_and_rename_images()
