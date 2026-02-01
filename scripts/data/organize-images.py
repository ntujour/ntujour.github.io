#!/usr/bin/env python3
"""
重新組織圖片到分類資料夾
news -> images/news/
activity -> images/activities/
同時更新 CSV 中的路徑
"""

import csv
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CSV_FILE = BASE_DIR / 'data' / 'content.csv'
IMAGES_DIR = BASE_DIR / 'images'
NEWS_DIR = IMAGES_DIR / 'news'
ACTIVITIES_DIR = IMAGES_DIR / 'activities'

def organize_images():
    print("📁 開始整理圖片到分類資料夾...")

    # 建立分類目錄
    NEWS_DIR.mkdir(exist_ok=True)
    ACTIVITIES_DIR.mkdir(exist_ok=True)

    # 讀取 CSV
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    moved_count = 0
    updated_count = 0

    for row in data:
        item_type = row.get('type', '')
        image_paths = row.get('image', '')

        if not image_paths:
            continue

        # 分割多張圖片
        paths = [p.strip() for p in image_paths.split('|||') if p.strip()]
        new_paths = []

        for path in paths:
            # 如果已經在分類資料夾中，跳過
            if path.startswith('images/news/') or path.startswith('images/activities/'):
                new_paths.append(path)
                continue

            # 取得檔名
            filename = Path(path).name

            # 確定目標資料夾
            if item_type == 'news':
                target_dir = NEWS_DIR
                new_path = f"images/news/{filename}"
            elif item_type == 'activity':
                target_dir = ACTIVITIES_DIR
                new_path = f"images/activities/{filename}"
            else:
                new_paths.append(path)
                continue

            # 原始檔案路徑
            source_file = BASE_DIR / path
            dest_file = target_dir / filename

            # 移動檔案
            if source_file.exists():
                try:
                    shutil.move(str(source_file), str(dest_file))
                    new_paths.append(new_path)
                    moved_count += 1
                    print(f"  ✅ {path} → {new_path}")
                except Exception as e:
                    print(f"  ❌ 移動失敗: {path} - {str(e)}")
                    new_paths.append(path)
            else:
                # 檔案不存在，保留原路徑
                new_paths.append(path)

        # 更新 CSV 中的圖片路徑
        if new_paths:
            old_paths = row['image']
            row['image'] = '|||'.join(new_paths)
            if old_paths != row['image']:
                updated_count += 1

    # 寫回 CSV
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n📊 整理完成:")
    print(f"   - 移動圖片: {moved_count} 個")
    print(f"   - 更新文章: {updated_count} 筆")
    print(f"   - 新聞圖片目錄: {NEWS_DIR}")
    print(f"   - 活動圖片目錄: {ACTIVITIES_DIR}")

if __name__ == '__main__':
    organize_images()
