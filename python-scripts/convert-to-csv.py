#!/usr/bin/env python3
"""
將news.json和activities.json轉換為單一CSV文件
包含所有內容，方便JavaScript動態渲染
"""

import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_json_file(filepath):
    """讀取JSON文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_to_csv():
    """將JSON數據轉換為CSV"""

    # 讀取數據
    news_data = load_json_file(BASE_DIR / 'data' / 'news.json')
    activities_data = load_json_file(BASE_DIR / 'data' / 'activities.json')

    # 準備CSV數據
    csv_data = []

    # 處理新聞數據
    for item in news_data:
        csv_data.append({
            'id': item['id'],
            'type': 'news',
            'title': item['title'],
            'date': item['date'],
            'category': item.get('category', ''),
            'time': '',
            'location': '',
            'content': item['content'],
            'slug': item['slug'],
            'originalFile': item.get('originalFile', ''),
            'image': ''  # 預留圖片欄位
        })

    # 處理活動數據
    for item in activities_data:
        csv_data.append({
            'id': item['id'],
            'type': 'activity',
            'title': item['title'],
            'date': item['date'],
            'category': '',
            'time': item.get('time', ''),
            'location': item.get('location', ''),
            'content': item['content'],
            'slug': item['slug'],
            'originalFile': item.get('originalFile', ''),
            'image': ''  # 預留圖片欄位
        })

    # 按日期排序（最新的在前）
    csv_data.sort(key=lambda x: x['date'], reverse=True)

    # 寫入CSV
    csv_file = BASE_DIR / 'data' / 'content.csv'
    fieldnames = ['id', 'type', 'title', 'date', 'category', 'time', 'location',
                  'content', 'slug', 'originalFile', 'image']

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(csv_data)

    print(f'✅ 已將 {len(news_data)} 則新聞和 {len(activities_data)} 則活動轉換為CSV')
    print(f'✅ CSV文件已儲存至: {csv_file}')
    print(f'\n總共 {len(csv_data)} 筆資料')

if __name__ == '__main__':
    convert_to_csv()
