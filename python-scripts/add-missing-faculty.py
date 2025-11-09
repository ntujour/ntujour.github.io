#!/usr/bin/env python3
"""
添加缺失的實務教師到 faculty-mapping.csv
"""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / 'faculty-mapping.csv'
JSON_PATH = BASE_DIR / 'faculty_data.json'

# 讀取 faculty_data.json
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    faculty_data = json.load(f)

# 讀取現有的 CSV
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    existing_rows = list(reader)
    fieldnames = reader.fieldnames

# 找出 CSV 中已存在的實務教師 ID
existing_ids = set()
for row in existing_rows:
    if row.get('類別') == '實務教師':
        existing_ids.add(row.get('英文ID', ''))

print(f"CSV 中已存在的實務教師: {len(existing_ids)} 位")
print(f"  {existing_ids}")

# 從 JSON 中找出所有實務教師
all_practical = faculty_data.get('practical', [])
print(f"\nJSON 中的實務教師: {len(all_practical)} 位")

# 照片對應表
PHOTO_MAPPING = {
    'lichihte': ('53af1fb5-1aec-4f55-830b-edfbf0006864.jpg', 'lichihte.jpg'),
    'liangyufang': ('1c2ce31c-d49b-4625-94bf-0b5b157effa5.jpg', 'liangyufang.jpg'),
    'archietse': ('4c12656a-53c0-441c-9e40-9a7e969dfb67.jpg', 'archie-tse.jpg'),
    'lihsuehli': ('230f5d3d-e187-4ddd-8fd0-4fa5c2aed6ac.png', 'lihsuehli.png'),
    'liyenfu': ('9aa3e815-bd5c-4a93-8e57-6cffeeda2951.jpg', 'liyenfu.jpg'),
    'huangchaohui': ('706b4518-c20f-459b-b8da-66504a3c2d49.jpg', 'huangchaohui.jpg'),
    'yangkuangsheng': ('164abf25-1b97-45d6-8299-730fb6ea2d9f.jpg', 'yangkuangsheng.jpg'),
    'liulijen': ('13078eaf-617b-49eb-8b76-ace1d55ae44d.jpg', 'liulijen.jpg'),
    'kuochunglun': ('e030bb4a-e544-43eb-8264-e26f408377cb.jpg', 'kuochunglun.jpg'),
    'hsiaofuyuan': ('b1cc1948-c2e3-452f-9b33-50214ff16ba4.jpg', 'hsiaofuyuan.jpg'),
    'chengkaichun': ('4dad0521-d297-4d11-af07-7bbeda467a26.png', 'chengkaichun.png'),
    'changchiehping': ('11e70ed5-bc85-43b5-8606-ac81a2a45a11.jpg', 'changchiehping.jpg'),
    'huangchepin': ('97e073af-b0de-4e40-b316-0ed9a790361d.jpg', 'hwangchepin.jpg'),
    'fangterlin': ('91603e44-a732-4695-97e5-ed5dc048ee9f.jpg', 'fangtelin.jpg')
}

# 添加缺失的實務教師
missing_count = 0
for faculty in all_practical:
    faculty_id = faculty.get('id', '')

    if faculty_id not in existing_ids:
        missing_count += 1
        print(f"\n添加缺失的教師: {faculty['name']} ({faculty_id})")

        # 獲取照片信息
        old_photo, new_photo = PHOTO_MAPPING.get(faculty_id, ('', ''))

        # 處理學歷和經歷
        education = ', '.join(faculty.get('education', []))
        experience = ', '.join(faculty.get('experience', []))

        new_row = {
            '類別': '實務教師',
            '姓名': faculty['name'],
            '英文ID': faculty_id,
            '職稱': faculty.get('title', ''),
            '照片檔名(001原檔)': old_photo,
            '新照片檔名': new_photo,
            '個人頁面': '',
            '電話': faculty.get('phone', ''),
            'Email': faculty.get('email', ''),
            '授課領域': faculty.get('teaching', ''),
            '研究專長': faculty.get('research', ''),
            '學歷': education,
            '經歷': experience
        }

        existing_rows.append(new_row)
        print(f"  ✓ 已添加 {faculty['name']}")

print(f"\n總共添加了 {missing_count} 位實務教師")

# 寫回 CSV（將實務教師放在最後）
with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(existing_rows)

print(f"\n✓ CSV 已更新，現在有 {len([r for r in existing_rows if r.get('類別') == '實務教師'])} 位實務教師")
