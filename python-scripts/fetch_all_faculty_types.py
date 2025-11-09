#!/usr/bin/env python3
"""
爬取所有類型的教師頁面（名譽教授、合聘教師等）
"""

import requests
import urllib3
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_photo(img_url, save_path):
    """下載照片"""
    try:
        if img_url.startswith('001/Upload'):
            full_url = f'http://www.journalism.ntu.edu.tw/{img_url}'
        elif not img_url.startswith('http'):
            full_url = f'http://www.journalism.ntu.edu.tw/{img_url}'
        else:
            full_url = img_url

        print(f"    下載照片: {full_url}")
        response = requests.get(full_url, verify=False, timeout=10)

        if response.status_code == 200:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"    ✓ 照片已儲存: {save_path.name}")
            return True
        else:
            print(f"    ✗ 下載失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"    ✗ 錯誤: {e}")
        return False

def extract_teacher_from_section(section, idx):
    """從section中提取教師資訊"""
    teacher_info = {
        'name': '',
        'photo': '',
        'phone': '',
        'email': '',
        'teaching': '',
        'research': ''
    }

    # 提取照片
    img_elem = section.find('img', alt='Art editor Img')
    if img_elem and 'src' in img_elem.attrs:
        img_url = img_elem['src']
        print(f"    找到照片: {img_url}")

        img_filename = img_url.split('/')[-1]
        photo_path = Path(__file__).parent / 'images' / 'faculty' / img_filename

        if download_photo(img_url, photo_path):
            teacher_info['photo'] = f'../images/faculty/{img_filename}'

    # 提取文本內容
    text_content = section.get_text(separator='\n')
    lines = [line.strip() for line in text_content.split('\n') if line.strip()]

    # 提取姓名（通常是第一行或包含職稱）
    for line in lines[:10]:
        line = line.replace('國立臺灣大學新聞研究所-', '').strip()
        if any(title in line for title in ['教授', '副教授', '助理教授', '講師', '特聘', '名譽']):
            if len(line) < 50:  # 避免抓到太長的文字
                teacher_info['name'] = line
                break

    # 提取聯絡資訊
    for i, line in enumerate(lines):
        if '聯絡電話' in line or '電話' in line:
            phone_match = re.search(r'[：:]\s*(.+)', line)
            if phone_match:
                teacher_info['phone'] = phone_match.group(1).strip()

        if 'E-mail' in line or 'email' in line.lower():
            email_match = re.search(r'[：:]\s*(.+)', line)
            if email_match:
                teacher_info['email'] = email_match.group(1).strip()

        if '授課領域' in line:
            teaching_match = re.search(r'[：:]\s*(.+)', line)
            if teaching_match:
                teacher_info['teaching'] = teaching_match.group(1).strip()
            elif i + 1 < len(lines):
                teacher_info['teaching'] = lines[i + 1].strip()

        if '研究專長' in line:
            research_match = re.search(r'[：:]\s*(.+)', line)
            if research_match:
                teacher_info['research'] = research_match.group(1).strip()
            elif i + 1 < len(lines):
                teacher_info['research'] = lines[i + 1].strip()

    return teacher_info

def fetch_faculty_page(url, faculty_type):
    """獲取教師頁面並提取資訊"""
    print(f"\n{'='*60}")
    print(f"正在獲取{faculty_type}頁面: {url}")
    print('='*60)

    try:
        response = requests.get(url, verify=False, timeout=10)

        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # 儲存HTML
            filename = url.split('/')[-1]
            save_path = Path(__file__).parent / 'faculty' / f'{filename.replace(".html", "")}-fetched.html'
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✓ HTML已儲存: {save_path}")

            teachers = []

            # 尋找所有教師區塊
            teacher_sections = soup.find_all('div', class_='area-editor user-edit')

            print(f"找到 {len(teacher_sections)} 個教師區塊")

            for idx, section in enumerate(teacher_sections):
                print(f"\n處理第 {idx + 1} 個區塊...")

                teacher_info = extract_teacher_from_section(section, idx)

                if teacher_info['name'] or teacher_info['photo']:
                    teachers.append(teacher_info)
                    print(f"  ✓ 提取教師: {teacher_info['name']}")
                else:
                    print(f"  ✗ 未找到有效資訊，跳過")

            return teachers
        else:
            print(f"✗ 獲取失敗: {response.status_code}")
            return []
    except Exception as e:
        print(f"✗ 錯誤: {e}")
        import traceback
        traceback.print_exc()
        return []

def main():
    print("=" * 60)
    print("開始爬取所有類型的教師頁面")
    print("=" * 60)

    # 定義要爬取的頁面
    faculty_pages = [
        {
            'url': 'http://www.journalism.ntu.edu.tw/parttime-professor.html',
            'type': '兼任教師',
            'key': 'parttime'
        },
        {
            'url': 'http://www.journalism.ntu.edu.tw/cp_n_105608.html',
            'type': '名譽教授',
            'key': 'honorary'
        },
        {
            'url': 'http://www.journalism.ntu.edu.tw/Professorjointappointment.html',
            'type': '合聘教師',
            'key': 'joint'
        }
    ]

    all_faculty_data = {}

    # 爬取每個頁面
    for page_info in faculty_pages:
        teachers = fetch_faculty_page(page_info['url'], page_info['type'])

        if teachers:
            all_faculty_data[page_info['key']] = teachers
            print(f"\n✓ 成功提取 {len(teachers)} 位{page_info['type']}")
        else:
            all_faculty_data[page_info['key']] = []
            print(f"\n✗ 未提取到{page_info['type']}資料")

    # 讀取現有的 faculty_data.json
    faculty_data_path = Path(__file__).parent / 'faculty_data.json'
    with open(faculty_data_path, 'r', encoding='utf-8') as f:
        faculty_data = json.load(f)

    # 讀取實務教師資料
    practical_data_path = Path(__file__).parent / 'practical_faculty_data.json'
    if practical_data_path.exists():
        with open(practical_data_path, 'r', encoding='utf-8') as f:
            practical_data = json.load(f)
            all_faculty_data['practical'] = practical_data.get('practical', [])

    # 合併所有資料
    faculty_data.update(all_faculty_data)

    # 保存完整的教師資料
    with open(faculty_data_path, 'w', encoding='utf-8') as f:
        json.dump(faculty_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("所有教師資料已整合到 faculty_data.json")
    print("=" * 60)

    # 顯示統計
    print("\n教師統計:")
    print(f"  專任教師: {len(faculty_data.get('fulltime', []))} 位")
    print(f"  兼任教師: {len(faculty_data.get('parttime', []))} 位")
    print(f"  實務教師: {len(faculty_data.get('practical', []))} 位")
    print(f"  名譽教授: {len(faculty_data.get('honorary', []))} 位")
    print(f"  合聘教師: {len(faculty_data.get('joint', []))} 位")

    # 顯示詳細列表
    for key, label in [('parttime', '兼任教師'), ('practical', '實務教師'),
                       ('honorary', '名譽教授'), ('joint', '合聘教師')]:
        if key in faculty_data and faculty_data[key]:
            print(f"\n{label}:")
            for teacher in faculty_data[key]:
                print(f"  - {teacher['name']}")

if __name__ == '__main__':
    main()
