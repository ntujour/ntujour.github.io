#!/usr/bin/env python3
"""
將 faculty_data.json 轉換為 Markdown 格式
以便透過 Decap CMS 管理
"""

import json
import os
from pathlib import Path

# 讀取 JSON 資料
with open('data/faculty_data.json', 'r', encoding='utf-8') as f:
    faculty_data = json.load(f)

# 建立輸出目錄
output_dir = Path('faculty/_profiles')
output_dir.mkdir(parents=True, exist_ok=True)

# 類別對應
category_map = {
    'fulltime': '專任教師',
    'practical': '實務教師',
    'parttime': '兼任教師',
    'honorary': '名譽教授',
    'joint': '合聘教師'
}

def convert_faculty_to_markdown(person, category, order):
    """將單一教師資料轉換為 Markdown"""
    
    # 優先使用已有的 ID
    if 'id' in person:
        faculty_id = person['id']
    else:
        # 從照片路徑提取 ID
        photo = person.get('photo', '')
        if photo:
            # 從 ../images/faculty/xxx.jpg 提取檔名（不含副檔名）
            import os
            photo_filename = os.path.splitext(photo.split('/')[-1])[0]
            faculty_id = photo_filename
        else:
            # 使用姓名的拼音（簡化版，只取英文字母）
            import re
            name = person.get('name', 'unknown')
            # 移除所有非英文字元
            faculty_id = re.sub(r'[^a-zA-Z]', '', name).lower()
            if not faculty_id:
                faculty_id = f'faculty_{order}'
    
    # 從照片路徑提取檔名
    photo = person.get('photo', '')
    if photo:
        # 從 ../images/faculty/xxx.jpg 格式提取
        photo_filename = photo.split('/')[-1]
        photo = f"/images/faculty/{photo_filename}"
    
    # 建立 Markdown 內容
    lines = ['---']
    
    # 基本資訊
    lines.append(f'id: "{faculty_id}"')
    
    # 處理姓名和職稱
    name = person.get('name', '')
    title = person.get('title', '')
    
    # 從 name 中分離職稱（例如：謝吉隆 副教授兼所長）
    name_parts = name.split()
    if len(name_parts) > 1:
        # 檢查是否包含職稱關鍵字
        for i, part in enumerate(name_parts[1:], 1):
            if any(職稱詞 in part for 職稱詞 in ['教授', '副教授', '助理教授', '講師']):
                # 提取職稱
                title = ' '.join(name_parts[i:])
                name = ' '.join(name_parts[:i])
                break
    
    lines.append(f'name: "{name}"')
    lines.append(f'name_en: "{person.get("name_en", name)}"')
    
    # 職稱
    if not title:
        title = category_map.get(category, '')
    
    lines.append(f'title: "{title}"')
    lines.append(f'title_en: "{title}"')  # 暫時使用中文，之後可手動翻譯
    
    # 類別
    lines.append(f'category: "{category}"')
    
    # 照片
    if photo:
        lines.append(f'photo: "{photo}"')
    
    # 聯絡資訊
    if person.get('phone'):
        lines.append(f'phone: "{person["phone"]}"')
    if person.get('email'):
        lines.append(f'email: "{person["email"]}"')
    if person.get('office'):
        lines.append(f'office: "{person["office"]}"')
    
    # 專長（從 teaching 或 research 欄位提取）
    expertise = []
    if person.get('teaching'):
        teaching_items = person['teaching'].replace('、', '，').split('，')
        expertise.extend([item.strip() for item in teaching_items if item.strip()])
    if person.get('research'):
        research_items = person['research'].replace('、', '，').split('，')
        expertise.extend([item.strip() for item in research_items if item.strip()])
    
    if expertise:
        lines.append('expertise:')
        for item in expertise[:5]:  # 最多5個
            lines.append(f'  - "{item}"')
    
    # 學歷
    if person.get('education'):
        lines.append('education:')
        for edu in person['education']:
            if isinstance(edu, str):
                lines.append(f'  - zh: "{edu}"')
                lines.append(f'    en: ""')
            elif isinstance(edu, dict):
                lines.append(f'  - zh: "{edu.get("zh", edu.get("en", ""))}"')
                lines.append(f'    en: "{edu.get("en", "")}"')
    
    # 經歷
    if person.get('experience'):
        lines.append('experience:')
        for exp in person['experience']:
            if isinstance(exp, str):
                lines.append(f'  - zh: "{exp}"')
                lines.append(f'    en: ""')
            elif isinstance(exp, dict):
                lines.append(f'  - zh: "{exp.get("zh", exp.get("en", ""))}"')
                lines.append(f'    en: "{exp.get("en", "")}"')
    
    # 研究領域
    if person.get('research'):
        lines.append('research:')
        research_list = person['research'].replace('、', '，').split('，')
        for r in research_list[:5]:
            if r.strip():
                lines.append(f'  - "{r.strip()}"')
    
    # 順序
    lines.append(f'order: {order}')
    
    lines.append('---')
    
    # 簡介（使用 Markdown body）
    bio_parts = []
    if person.get('teaching'):
        bio_parts.append(f"**授課科目**：{person['teaching']}")
    if person.get('research'):
        bio_parts.append(f"**研究專長**：{person['research']}")
    
    if bio_parts:
        lines.append('')
        lines.extend(bio_parts)
    
    return '\n'.join(lines)

# 轉換所有類別
order_counter = 1
for category, faculty_list in faculty_data.items():
    print(f"\n轉換 {category_map.get(category, category)} ({len(faculty_list)} 位)...")
    
    for person in faculty_list:
        faculty_id = person.get('id', person.get('name', '').replace(' ', '').lower())
        
        # 移除特殊字元
        import re
        faculty_id = re.sub(r'[^a-z0-9]', '', faculty_id.lower())
        
        # 生成 Markdown
        markdown_content = convert_faculty_to_markdown(person, category, order_counter)
        
        # 寫入檔案
        output_file = output_dir / f'{faculty_id}.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"  ✓ {person.get('name', faculty_id)} → {output_file}")
        order_counter += 1

print(f"\n✅ 轉換完成！共建立 {order_counter - 1} 個 Markdown 檔案")
print(f"📁 輸出目錄：{output_dir.absolute()}")
print(f"\n⚠️  注意事項：")
print(f"   1. 照片路徑已更新為 /images/faculty/xxx.jpg")
print(f"   2. 請檢查並手動補充英文版本的資料")
print(f"   3. 可透過 CMS (http://localhost:8000/admin/) 進一步編輯")
