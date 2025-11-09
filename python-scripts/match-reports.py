#!/usr/bin/env python3
"""
根據最大的 PNG/PDF 文件手動匹配所報
因為有 20 期所報(31-50期)和 39 個文件，我們選擇最大的 20 個文件來匹配
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent
CKFILE_DIR = BASE_DIR / '001' / 'Upload' / '366' / 'ckfile'

# 手動選擇最大的 20 個文件（按照之前的掃描結果）
# 從最新的第50期開始往回匹配到第31期
MANUAL_MAPPING = {
    '50': '8aae5008-c04f-4ec9-a1ec-0e4b5c03f8c4.png',  # 最大的文件 (21MB) 可能是最新的
    '49': 'b0ca00a1-06e8-489b-9804-4d54e7f1c491.png',
    '48': '806ebfdb-f858-4c25-bd8d-5c7ec2d36862.png',
    '47': 'b66cfaca-ecbf-4073-8d11-d91ffe412b47.png',
    '46': '45bdfd2c-cb3b-4879-9680-0ca5ab65f04e.png',
    '45': '18e83aac-2534-4254-88db-90ad428c1a96.png',
    '44': '1c6d41ad-f266-46e3-a4cd-cf12a9030f93.png',
    '43': '1275c644-ca7f-4600-abbe-1ca9ee4849ad.png',
    '42': 'a9fcead1-ce29-4446-b539-c6f5ea0f02b6.png',
    '41': '6e3c9bb0-4e1e-41ee-9e2b-78be4e982550.png',
    '40': '4e9250ba-cc41-4c5e-89ee-9cd702414257.png',
    '39': 'c38b215a-6c3d-42d7-b6bc-2091a5c670c1.png',
    '38': '42c7503a-6bd0-4fdc-8b29-a688ccd04e28.pdf',
    '37': '2eef07ff-1c4b-4644-9085-36bbc52fa9f6.png',
    '36': '37514a83-5139-4d6a-b44f-8eb49240c95b.png',
    '35': 'a22921b8-2e01-4781-ac49-ff6a72adbc35.pdf',
    '34': '230f5d3d-e187-4ddd-8fd0-4fa5c2aed6ac.png',
    '33': 'b83392ac-fa70-47a9-8d24-b866829eff6a.pdf',
    '32': 'c689a9b1-a6d4-48aa-9113-5905dea87f02.pdf',
    '31': '922310ad-46a2-4204-ab5c-795c071257de.pdf',
}

def main():
    """更新 CSV 文件"""
    csv_path = BASE_DIR / 'data' / 'e-reports.csv'

    # 讀取現有 CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        reports = list(reader)

    # 更新文件路徑
    for report in reports:
        issue = report['issue']
        if issue in MANUAL_MAPPING:
            filename = MANUAL_MAPPING[issue]
            report['filepath'] = f'001/Upload/366/ckfile/{filename}'

    # 寫回 CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['issue', 'title', 'date', 'filepath'])
        writer.writeheader()
        writer.writerows(reports)

    print(f"✓ 已更新 CSV 文件: {csv_path}")
    print(f"\n已匹配 {len(MANUAL_MAPPING)} 個所報文件")

    # 驗證文件是否存在
    print("\n驗證文件:")
    missing = []
    for issue, filename in MANUAL_MAPPING.items():
        filepath = CKFILE_DIR / filename
        if filepath.exists():
            size_kb = filepath.stat().st_size // 1024
            print(f"  ✓ 第{issue}期: {filename} ({size_kb} KB)")
        else:
            print(f"  ✗ 第{issue}期: {filename} (文件不存在)")
            missing.append(issue)

    if missing:
        print(f"\n⚠️  警告: {len(missing)} 個文件不存在")
    else:
        print("\n✓ 所有文件都存在")

if __name__ == '__main__':
    main()
