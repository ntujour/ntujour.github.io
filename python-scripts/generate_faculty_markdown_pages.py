#!/usr/bin/env python3
"""
為每位專任教師生成使用 Markdown 的頁面
"""

import json
from pathlib import Path

def generate_faculty_markdown_page(faculty_info, template_path, output_path):
    """生成教師個人頁面（使用 Markdown）"""
    try:
        # 讀取模板
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # 替換基本資訊
        page_content = template.replace('[教師姓名]', faculty_info['name'])
        page_content = page_content.replace('[PHOTO_PATH]', faculty_info['photo'])

        # 寫入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        return True
    except Exception as e:
        print(f"錯誤生成 {output_path}: {e}")
        return False

def main():
    """主程序"""
    print("=" * 60)
    print("為專任教師生成使用 Markdown 的個人頁面")
    print("=" * 60)
    print()

    # 讀取faculty_data.json
    with open('faculty_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 設置模板路徑
    template_path = Path('faculty/faculty-markdown-template.html')

    if not template_path.exists():
        print(f"✗ 找不到模板文件: {template_path}")
        return

    success_count = 0
    total_count = len(data['fulltime'])

    for faculty in data['fulltime']:
        print(f"處理: {faculty['name']}")

        # 從文件路徑提取文件名
        file_name = Path(faculty['file']).name
        output_path = Path('faculty') / file_name

        # 生成頁面
        if generate_faculty_markdown_page(faculty, template_path, output_path):
            print(f"✓ 已生成: {output_path}")
            success_count += 1
        else:
            print(f"✗ 生成失敗")

        print()

    print("=" * 60)
    print(f"完成！成功生成 {success_count}/{total_count} 個頁面")
    print("=" * 60)
    print()
    print("現在所有教師頁面將動態載入 Markdown 內容")
    print("Markdown 文件位於: faculty/content/*.md")

if __name__ == '__main__':
    main()
