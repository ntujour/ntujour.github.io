#!/usr/bin/env python3
"""
提取教師資料並生成JSON數據
"""

import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_faculty_info(html_file):
    """從教師HTML文件中提取資訊"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 提取標題（教師姓名和職稱）
        title_elem = soup.find('title')
        title = title_elem.text.strip() if title_elem else ''
        # 移除 "國立臺灣大學新聞研究所-" 前綴
        name = title.replace('國立臺灣大學新聞研究所-', '').strip()

        # 提取照片URL
        img_elem = soup.find('img', alt='Art editor Img')
        photo = ''
        if img_elem and 'src' in img_elem.attrs:
            photo = img_elem['src']
            # 修正相對路徑
            if not photo.startswith('http'):
                photo = '../' + photo.replace('001/Upload/366/ckfile/', 'images/faculty/')

        # 提取主要內容
        editor_area = soup.find('div', class_='area-editor user-edit')
        if not editor_area:
            return None

        # 提取文本內容
        text_content = editor_area.get_text(separator='\n')

        # 提取聯絡資訊
        contact_match = re.search(r'聯絡電話[：:](.*?)[\n]', text_content)
        phone = contact_match.group(1).strip() if contact_match else ''

        email_match = re.search(r'E-mail[：:](.+?)[\n]', text_content)
        email = email_match.group(1).strip() if email_match else ''

        # 提取授課領域
        teaching_match = re.search(r'授課領域[：:](.*?)[\n]', text_content)
        teaching = teaching_match.group(1).strip() if teaching_match else ''

        # 提取研究專長
        research_match = re.search(r'研究專長[：:](.*?)[\n]', text_content)
        research = research_match.group(1).strip() if research_match else ''

        return {
            'name': name,
            'photo': photo,
            'phone': phone,
            'email': email,
            'teaching': teaching,
            'research': research,
            'file': html_file.name
        }

    except Exception as e:
        print(f"錯誤處理 {html_file}: {e}")
        return None

def main():
    faculty_dir = Path(__file__).parent / 'faculty'

    # 專任教師列表（按順序）
    fulltime_files = [
        'hsiehjl.html',
        'linly.html',
        'hungcl.html',
        'lincc.html',  # 林照真
        'RauchfleischA.html',
        'tsaihj.html',
        'chanii.html'
    ]

    fulltime_faculty = []
    for filename in fulltime_files:
        filepath = faculty_dir / filename
        if filepath.exists():
            info = extract_faculty_info(filepath)
            if info:
                fulltime_faculty.append(info)
                print(f"✓ 已提取: {info['name']}")

    # 保存為JSON
    output_file = Path(__file__).parent / 'faculty_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'fulltime': fulltime_faculty
        }, f, ensure_ascii=False, indent=2)

    print(f"\n已保存 {len(fulltime_faculty)} 位專任教師資料到 {output_file}")

    # 顯示摘要
    print("\n專任教師:")
    for faculty in fulltime_faculty:
        print(f"  - {faculty['name']}")

if __name__ == '__main__':
    main()
