#!/usr/bin/env python3
"""
Generate static faculty HTML pages from faculty_data.json
將教職員資料直接嵌入 HTML，不需要前端 JavaScript 動態載入

使用方式：
    python3 scripts/build/generate-static-faculty.py
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
FACULTY_DATA = BASE_DIR / 'data' / 'faculty_data.json'
OUTPUT_DIR = BASE_DIR / 'faculty'

def generate_faculty_cards_html(faculty_list, category_name):
    """生成教職員卡片的 HTML"""
    cards_html = []

    for faculty in faculty_list:
        card = f'''
        <a href="{faculty.get('file', '#')}" class="faculty-card">
            <div class="faculty-photo">
                <img src="{faculty.get('photo', '../images/faculty/default.jpg')}"
                     alt="{faculty.get('name', '未命名')}"
                     loading="lazy">
            </div>
            <h4 class="faculty-name">{faculty.get('name', '未命名')}</h4>
            <p class="faculty-title">{faculty.get('title', '')}</p>
        </a>'''
        cards_html.append(card)

    return '\n'.join(cards_html)

def generate_faculty_html():
    """生成師資總覽頁面"""
    print("🔨 開始生成教職員靜態頁面...")

    # 讀取教職員資料
    with open(FACULTY_DATA, 'r', encoding='utf-8') as f:
        faculty_data = json.load(f)

    # 讀取模板（如果存在）
    template_file = OUTPUT_DIR / 'faculty.html'
    if not template_file.exists():
        print(f"⚠️  找不到模板檔案: {template_file}")
        print("   請確保 faculty/faculty.html 存在")
        return False

    with open(template_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 生成各類別的 HTML
    categories = {
        'fulltime': '專任教師',
        'practical': '實務教師',
        'parttime': '兼任教師',
        'honorary': '名譽教授',
        'joint': '合聘教師'
    }

    for category_key, category_name in categories.items():
        if category_key in faculty_data:
            faculty_list = faculty_data[category_key]
            cards_html = generate_faculty_cards_html(faculty_list, category_name)

            # 替換對應的區塊
            placeholder = f'<!-- GENERATED-{category_key.upper()}-START -->.*?<!-- GENERATED-{category_key.upper()}-END -->'
            replacement = f'<!-- GENERATED-{category_key.upper()}-START -->\n{cards_html}\n        <!-- GENERATED-{category_key.upper()}-END -->'

            import re
            html_content = re.sub(placeholder, replacement, html_content, flags=re.DOTALL)

            print(f"  ✓ 已生成 {category_name}: {len(faculty_list)} 位")

    # 寫入檔案
    output_file = OUTPUT_DIR / 'faculty-static.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ 完成！已生成: {output_file}")
    print(f"   此檔案可以直接用瀏覽器開啟（不需要伺服器）")
    return True

if __name__ == '__main__':
    generate_faculty_html()
