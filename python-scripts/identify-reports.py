#!/usr/bin/env python3
"""
識別 001/Upload/366/ckfile/ 目錄中的所報文件
根據文件大小和類型來識別可能的所報文件
"""

import os
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
CKFILE_DIR = BASE_DIR / '001' / 'Upload' / '366' / 'ckfile'

def get_file_info():
    """取得所有 PDF 和 PNG 文件的資訊"""
    files = []

    # 收集所有 PDF 和 PNG 文件
    for ext in ['*.pdf', '*.png']:
        for filepath in CKFILE_DIR.glob(ext):
            size = filepath.stat().st_size
            mtime = filepath.stat().st_mtime
            files.append({
                'filename': filepath.name,
                'path': str(filepath.relative_to(BASE_DIR)),
                'size': size,
                'size_kb': size // 1024,
                'mtime': mtime,
                'ext': filepath.suffix
            })

    # 依大小排序（較大的文件可能是完整的所報）
    files.sort(key=lambda x: x['size'], reverse=True)

    return files

def main():
    """主函數"""
    print("掃描 001/Upload/366/ckfile/ 目錄中的文件...")

    files = get_file_info()

    print(f"\n找到 {len(files)} 個 PDF/PNG 文件")
    print("\n較大的文件（可能是完整所報）：")
    print("-" * 80)

    # 顯示前 40 個最大的文件
    for i, f in enumerate(files[:40], 1):
        print(f"{i:2}. {f['filename'][:45]:45} | {f['size_kb']:6} KB | {f['ext']}")

    # 創建 CSV 模板
    csv_path = BASE_DIR / 'data' / 'e-reports.csv'
    csv_path.parent.mkdir(exist_ok=True)

    # 根據現有 e-report.html 中的期數創建模板
    # 第 31-50 期，共 20 期
    report_data = []

    # 從第 50 期開始往回（最新的在前）
    dates = [
        ('50', '2024年12月'), ('49', '2024年6月'), ('48', '2023年12月'), ('47', '2023年6月'),
        ('46', '2022年12月'), ('45', '2022年6月'), ('44', '2021年12月'), ('43', '2021年6月'),
        ('42', '2020年12月'), ('41', '2020年6月'), ('40', '2019年12月'), ('39', '2019年6月'),
        ('38', '2018年12月'), ('37', '2018年6月'), ('36', '2017年12月'), ('35', '2017年6月'),
        ('34', '2016年12月'), ('33', '2016年6月'), ('32', '2015年12月'), ('31', '2015年6月'),
    ]

    for issue, date in dates:
        report_data.append({
            'issue': issue,
            'title': f'第{issue}期 所報',
            'date': date,
            'filepath': ''  # 留空待填
        })

    # 寫入 CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['issue', 'title', 'date', 'filepath'])
        writer.writeheader()
        writer.writerows(report_data)

    print(f"\n✓ 已創建 CSV 模板: {csv_path}")
    print("\n接下來需要手動將文件路徑填入 CSV 中，或者提供更多資訊來自動匹配。")
    print("\n可能的匹配方式：")
    print("1. 如果有舊網站的備份或資料庫")
    print("2. 如果文件名有規律（例如包含期數）")
    print("3. 手動檢視較大的 PDF/PNG 文件來確認期數")

if __name__ == '__main__':
    main()
