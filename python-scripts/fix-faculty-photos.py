#!/usr/bin/env python3
"""
修正教師照片對應關係
"""

import json
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'images' / 'faculty'

# 正確的對應關係（根據實際的 practical faculty）
CORRECT_MAPPING = {
    # 李志德 (lichihte)
    'lichihte': {
        'old_file': '53af1fb5-1aec-4f55-830b-edfbf0006864.jpg',
        'new_file': 'lichihte.jpg',
        'source_dir': '001/Upload/690/ckfile'
    },
    # 梁玉芳 (liangyufang)
    'liangyufang': {
        'old_file': '1c2ce31c-d49b-4625-94bf-0b5b157effa5.jpg',
        'new_file': 'liangyufang.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    # 謝艾契 (Archie Tse)
    'archietse': {
        'old_file': '4c12656a-53c0-441c-9e40-9a7e969dfb67.jpg',
        'new_file': 'archie-tse.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    # 黃哲斌 (hwangchepin)
    'hwangchepin': {
        'old_file': '97e073af-b0de-4e40-b316-0ed9a790361d.jpg',
        'new_file': 'hwangchepin.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    # 方德琳 (fangtelin)
    'fangtelin': {
        'old_file': '91603e44-a732-4695-97e5-ed5dc048ee9f.jpg',
        'new_file': 'fangtelin.jpg',
        'source_dir': '001/Upload/366/ckfile'
    }
}

def copy_photos():
    """複製照片到正確位置"""
    print("\n=== 複製實務教師照片（正確對應） ===")

    for person_id, info in CORRECT_MAPPING.items():
        old_path = BASE_DIR / info['source_dir'] / info['old_file']
        new_path = IMAGES_DIR / info['new_file']

        if old_path.exists():
            shutil.copy2(old_path, new_path)
            print(f"  ✓ {info['new_file']}")
        else:
            print(f"  ✗ 找不到: {old_path}")

def update_faculty_data():
    """更新 faculty_data.json"""
    print("\n=== 更新 faculty_data.json ===")
    json_path = BASE_DIR / 'faculty_data.json'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 對應到 faculty_data.json 中的正確欄位
    id_to_photo = {
        'lichihte': 'images/faculty/lichihte.jpg',
        'liangyufang': 'images/faculty/liangyufang.jpg',
        'archietse': 'images/faculty/archie-tse.jpg',
        'huangchepin': 'images/faculty/hwangchepin.jpg',  # 注意是 huang 不是 hwang
        'fangterlin': 'images/faculty/fangtelin.jpg'  # 注意是 fangter 不是 fangte
    }

    if 'practical' in data:
        for faculty in data['practical']:
            faculty_id = faculty.get('id', '')
            if faculty_id in id_to_photo:
                old_photo = faculty.get('photo', '')
                faculty['photo'] = id_to_photo[faculty_id]
                print(f"  ✓ {faculty['name']}: {id_to_photo[faculty_id]}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("  ✓ faculty_data.json 已更新")

def main():
    print("=" * 60)
    print("修正實務教師照片對應")
    print("=" * 60)

    copy_photos()
    update_faculty_data()

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)
    print("\n實務教師照片：")
    print("  lichihte.jpg       李志德")
    print("  liangyufang.jpg    梁玉芳")
    print("  archie-tse.jpg     謝艾契 (Archie Tse)")
    print("  hwangchepin.jpg    黃哲斌")
    print("  fangtelin.jpg      方德琳")

if __name__ == '__main__':
    main()
