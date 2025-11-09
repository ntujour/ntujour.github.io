#!/usr/bin/env python3
"""
提取兼任教師資料
"""

import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_parttime_faculty():
    """從兼任教師HTML文件中提取資訊"""
    html_file = Path(__file__).parent / 'faculty' / 'parttime-professor.html'

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 找到所有教師區塊（每個tab-cp-target）
        faculty_blocks = soup.find_all('div', {'data-type': '0', 'data-child': '3'})

        parttime_faculty = []

        for block in faculty_blocks:
            editor_area = block.find('div', class_='area-editor user-edit')
            if not editor_area:
                continue

            # 提取照片
            img = editor_area.find('img', alt='Art editor Img')
            photo = ''
            if img and 'src' in img.attrs:
                photo = img['src']
                # 修正路徑
                if not photo.startswith('http'):
                    photo = '../' + photo.replace('001/Upload/366/ckfile/', 'images/faculty/')

            # 提取文本內容
            text = editor_area.get_text(separator='\n', strip=True)

            # 提取姓名（從h3標籤）
            h3 = editor_area.find('h3')
            if not h3:
                continue
            name = h3.get_text(strip=True).replace('*', '').strip()

            # 提取Email
            email_match = re.search(r'E-mail[：:](.+?)(?:\n|個人網站)', text, re.IGNORECASE)
            email = ''
            if email_match:
                email_text = email_match.group(1).strip()
                # 清理email（移除html標籤等）
                email = re.sub(r'<.*?>', '', email_text)
                email = email.split('／')[0].strip()  # 取第一個email

            # 提取電話
            phone_match = re.search(r'聯絡電話[：:](.*?)[\n]', text)
            phone = phone_match.group(1).strip() if phone_match else ''

            # 提取授課領域
            teaching_match = re.search(r'授課領域[：:](.*?)[\n]', text)
            teaching = teaching_match.group(1).strip() if teaching_match else ''

            # 提取研究專長/領域
            research_match = re.search(r'研究(?:專長|領域)[：:](.*?)[\n]', text)
            research = research_match.group(1).strip() if research_match else ''

            if name:
                parttime_faculty.append({
                    'name': name,
                    'photo': photo,
                    'phone': phone,
                    'email': email,
                    'teaching': teaching,
                    'research': research
                })
                print(f"✓ 已提取: {name}")

        return parttime_faculty

    except Exception as e:
        print(f"錯誤: {e}")
        import traceback
        traceback.print_exc()
        return []

def main():
    parttime_faculty = extract_parttime_faculty()

    # 讀取現有的faculty_data.json
    json_file = Path(__file__).parent / 'faculty_data.json'

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = {}

    # 添加兼任教師資料
    data['parttime'] = parttime_faculty

    # 保存
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n已保存 {len(parttime_faculty)} 位兼任教師資料")

    # 顯示摘要
    print("\n兼任教師:")
    for faculty in parttime_faculty:
        print(f"  - {faculty['name']}")

if __name__ == '__main__':
    main()
