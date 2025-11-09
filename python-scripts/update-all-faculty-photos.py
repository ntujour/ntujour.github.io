#!/usr/bin/env python3
"""
更新所有實務教師照片 - 根據 faculty_data.json 和 faculty-mapping.csv
"""

import json
import shutil
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'images' / 'faculty'

# 從 faculty_data.json 中讀取所有實務教師的資料
def get_practical_faculty():
    """讀取 faculty_data.json 中的實務教師資料"""
    json_path = BASE_DIR / 'faculty_data.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('practical', [])

# 所有實務教師的照片對應（根據 faculty_data.json）
PHOTO_MAPPING = {
    'lichihte': {
        'old_file': '53af1fb5-1aec-4f55-830b-edfbf0006864.jpg',
        'new_file': 'lichihte.jpg',
        'source_dir': '001/Upload/690/ckfile'
    },
    'liangyufang': {
        'old_file': '1c2ce31c-d49b-4625-94bf-0b5b157effa5.jpg',
        'new_file': 'liangyufang.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'archietse': {
        'old_file': '4c12656a-53c0-441c-9e40-9a7e969dfb67.jpg',
        'new_file': 'archie-tse.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'lihsuehli': {
        'old_file': '230f5d3d-e187-4ddd-8fd0-4fa5c2aed6ac.png',
        'new_file': 'lihsuehli.png',
        'source_dir': '001/Upload/366/ckfile'
    },
    'liyenfu': {
        'old_file': '9aa3e815-bd5c-4a93-8e57-6cffeeda2951.jpg',
        'new_file': 'liyenfu.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'huangchaohui': {
        'old_file': '706b4518-c20f-459b-b8da-66504a3c2d49.jpg',
        'new_file': 'huangchaohui.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'yangkuangsheng': {
        'old_file': '164abf25-1b97-45d6-8299-730fb6ea2d9f.jpg',
        'new_file': 'yangkuangsheng.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'liulijen': {
        'old_file': '13078eaf-617b-49eb-8b76-ace1d55ae44d.jpg',
        'new_file': 'liulijen.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'kuochunglun': {
        'old_file': 'e030bb4a-e544-43eb-8264-e26f408377cb.jpg',
        'new_file': 'kuochunglun.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'hsiaofuyuan': {
        'old_file': 'b1cc1948-c2e3-452f-9b33-50214ff16ba4.jpg',
        'new_file': 'hsiaofuyuan.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'chengkaichun': {
        'old_file': '4dad0521-d297-4d11-af07-7bbeda467a26.png',
        'new_file': 'chengkaichun.png',
        'source_dir': '001/Upload/366/ckfile'
    },
    'changchiehping': {
        'old_file': '11e70ed5-bc85-43b5-8606-ac81a2a45a11.jpg',
        'new_file': 'changchiehping.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'huangchepin': {
        'old_file': '97e073af-b0de-4e40-b316-0ed9a790361d.jpg',
        'new_file': 'hwangchepin.jpg',
        'source_dir': '001/Upload/366/ckfile'
    },
    'fangterlin': {
        'old_file': '91603e44-a732-4695-97e5-ed5dc048ee9f.jpg',
        'new_file': 'fangtelin.jpg',
        'source_dir': '001/Upload/366/ckfile'
    }
}

def copy_photos():
    """複製所有實務教師照片到正確位置"""
    print("\n=== 複製實務教師照片 ===")

    for faculty_id, info in PHOTO_MAPPING.items():
        old_path = BASE_DIR / info['source_dir'] / info['old_file']
        new_path = IMAGES_DIR / info['new_file']

        if old_path.exists():
            shutil.copy2(old_path, new_path)
            print(f"  ✓ {faculty_id}: {info['new_file']}")
        else:
            print(f"  ✗ 找不到: {old_path}")

def update_faculty_data():
    """更新 faculty_data.json 中所有實務教師的照片路徑"""
    print("\n=== 更新 faculty_data.json ===")
    json_path = BASE_DIR / 'faculty_data.json'

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'practical' in data:
        for faculty in data['practical']:
            faculty_id = faculty.get('id', '')
            if faculty_id in PHOTO_MAPPING:
                new_file = PHOTO_MAPPING[faculty_id]['new_file']
                old_photo = faculty.get('photo', '')
                new_photo = f'images/faculty/{new_file}'

                faculty['photo'] = new_photo
                print(f"  ✓ {faculty['name']}: {new_photo}")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("  ✓ faculty_data.json 已更新")

def update_csv():
    """更新 faculty-mapping.csv 中的照片檔名"""
    print("\n=== 更新 faculty-mapping.csv ===")
    csv_path = BASE_DIR / 'faculty-mapping.csv'

    if not csv_path.exists():
        print("  ✗ faculty-mapping.csv 不存在")
        return

    # 讀取 CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # 更新照片檔名
    for row in rows:
        english_id = row.get('英文ID', '')
        if english_id in PHOTO_MAPPING:
            row['照片檔名(001原檔)'] = PHOTO_MAPPING[english_id]['old_file']
            row['新照片檔名'] = PHOTO_MAPPING[english_id]['new_file']
            print(f"  ✓ {row['姓名']}: {PHOTO_MAPPING[english_id]['new_file']}")

    # 寫回 CSV
    if rows:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print("  ✓ faculty-mapping.csv 已更新")

def verify_photos():
    """驗證所有照片是否存在"""
    print("\n=== 驗證照片檔案 ===")

    for faculty_id, info in PHOTO_MAPPING.items():
        photo_path = IMAGES_DIR / info['new_file']
        if photo_path.exists():
            print(f"  ✓ {info['new_file']}")
        else:
            print(f"  ✗ {info['new_file']} 不存在")

def main():
    """主函數"""
    print("=" * 60)
    print("更新所有實務教師照片")
    print("=" * 60)

    # 確保目錄存在
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # 複製照片
    copy_photos()

    # 更新 JSON
    update_faculty_data()

    # 更新 CSV
    update_csv()

    # 驗證照片
    verify_photos()

    print("\n" + "=" * 60)
    print("完成！")
    print("=" * 60)
    print("\n所有 14 位實務教師照片：")
    print("  1. lichihte.jpg       李志德")
    print("  2. liangyufang.jpg    梁玉芳")
    print("  3. archie-tse.jpg     謝艾契 (Archie Tse)")
    print("  4. lihsuehli.png      李雪莉")
    print("  5. liyenfu.jpg        李彥甫")
    print("  6. huangchaohui.jpg   黃兆徽")
    print("  7. yangkuangsheng.jpg 楊光昇")
    print("  8. liulijen.jpg       劉力仁")
    print("  9. kuochunglun.jpg    郭崇倫")
    print(" 10. hsiaofuyuan.jpg    蕭富元")
    print(" 11. chengkaichun.png   鄭凱駿")
    print(" 12. changchiehping.jpg 張潔平")
    print(" 13. hwangchepin.jpg    黃哲斌")
    print(" 14. fangtelin.jpg      方德琳")

if __name__ == '__main__':
    main()
