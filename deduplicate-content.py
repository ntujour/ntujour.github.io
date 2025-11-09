#!/usr/bin/env python3
"""
去除 data/content.csv 中的重複項目
根據 title 和 date 判斷是否重複
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / 'data' / 'content.csv'
OUTPUT_FILE = BASE_DIR / 'data' / 'content.csv'
BACKUP_FILE = BASE_DIR / 'data' / 'content_backup.csv'

def deduplicate_csv():
    print("🔍 開始去重處理...")

    # 讀取 CSV
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    print(f"📊 原始資料: {len(data)} 筆")

    # 去重邏輯：根據 (title, date) 組合判斷
    seen = set()
    unique_data = []
    duplicates = []

    for row in data:
        key = (row['title'], row['date'])

        if key not in seen:
            seen.add(key)
            unique_data.append(row)
        else:
            duplicates.append(row)
            print(f"  ❌ 重複: {row['title']} ({row['date']}) - {row['originalFile']}")

    print(f"\n✅ 去重後資料: {len(unique_data)} 筆")
    print(f"🗑️  移除重複: {len(duplicates)} 筆")

    # 備份原始檔案
    if not BACKUP_FILE.exists():
        with open(BACKUP_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"\n💾 已備份原始檔案到: {BACKUP_FILE}")

    # 寫入去重後的資料
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        if unique_data:
            fieldnames = unique_data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(unique_data)

    print(f"✨ 已儲存去重後的資料到: {OUTPUT_FILE}")

    # 統計
    news_count = sum(1 for item in unique_data if item['type'] == 'news')
    activity_count = sum(1 for item in unique_data if item['type'] == 'activity')
    print(f"\n📊 去重後統計:")
    print(f"   - 新聞: {news_count} 筆")
    print(f"   - 活動: {activity_count} 筆")

    # 分類統計
    categories = {}
    for item in unique_data:
        cat = item.get('category', '未分類') or '未分類'
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\n📂 分類統計:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   - {cat}: {count} 筆")

if __name__ == '__main__':
    deduplicate_csv()
