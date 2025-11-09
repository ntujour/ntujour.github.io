#!/usr/bin/env python3
"""
爬取林照真老師頁面和實務教師頁面的照片與內容
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

        print(f"  下載照片: {full_url}")
        response = requests.get(full_url, verify=False, timeout=10)

        if response.status_code == 200:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"  ✓ 照片已儲存: {save_path.name}")
            return True
        else:
            print(f"  ✗ 下載失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ 錯誤: {e}")
        return False

def fetch_lincc_page():
    """獲取林照真老師的頁面"""
    url = "http://www.journalism.ntu.edu.tw/lincc.html"
    print(f"\n正在獲取林照真老師頁面: {url}")

    try:
        response = requests.get(url, verify=False, timeout=10)

        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # 儲存HTML
            save_path = Path(__file__).parent / 'faculty' / 'lincc-original.html'
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✓ HTML已儲存: {save_path}")

            # 尋找照片
            img_elem = soup.find('img', alt='Art editor Img')
            if img_elem and 'src' in img_elem.attrs:
                img_url = img_elem['src']
                print(f"  找到照片URL: {img_url}")

                # 下載照片
                # 從URL中提取檔名
                img_filename = img_url.split('/')[-1]
                photo_path = Path(__file__).parent / 'images' / 'faculty' / img_filename

                if download_photo(img_url, photo_path):
                    return img_filename
            else:
                print("  ✗ 未找到照片")
                return None

        else:
            print(f"✗ 獲取失敗: {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ 錯誤: {e}")
        return None

def extract_practical_teachers():
    """提取實務教師資料"""
    url = "http://www.journalism.ntu.edu.tw/practical-professor.html"
    print(f"\n正在獲取實務教師頁面: {url}")

    try:
        response = requests.get(url, verify=False, timeout=10)

        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # 儲存HTML
            save_path = Path(__file__).parent / 'faculty' / 'practical-professor-fetched.html'
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✓ HTML已儲存: {save_path}")

            practical_teachers = []

            # 尋找所有教師區塊 - 使用不同的選擇器策略
            # 先找所有包含教師資訊的區塊
            teacher_sections = soup.find_all('div', class_='area-editor user-edit')

            print(f"找到 {len(teacher_sections)} 個教師區塊")

            for idx, section in enumerate(teacher_sections):
                print(f"\n處理第 {idx + 1} 個區塊...")

                # 提取照片
                img_elem = section.find('img', alt='Art editor Img')
                photo_filename = ''

                if img_elem and 'src' in img_elem.attrs:
                    img_url = img_elem['src']
                    print(f"  找到照片: {img_url}")

                    img_filename = img_url.split('/')[-1]
                    photo_path = Path(__file__).parent / 'images' / 'faculty' / img_filename

                    if download_photo(img_url, photo_path):
                        photo_filename = img_filename

                # 提取文本內容
                text_content = section.get_text(separator='\n')
                lines = [line.strip() for line in text_content.split('\n') if line.strip()]

                # 嘗試提取姓名（通常是第一行或包含在標題中）
                name = ''
                for line in lines[:5]:  # 檢查前5行
                    # 移除常見的前綴
                    line = line.replace('國立臺灣大學新聞研究所-', '').strip()
                    # 如果包含"教授"、"副教授"、"助理教授"等關鍵字，可能是姓名
                    if any(title in line for title in ['教授', '副教授', '助理教授', '講師']):
                        name = line
                        break

                # 提取聯絡資訊
                phone = ''
                email = ''
                teaching = ''
                research = ''

                for i, line in enumerate(lines):
                    if '聯絡電話' in line or '電話' in line:
                        phone_match = re.search(r'[：:]\s*(.+)', line)
                        if phone_match:
                            phone = phone_match.group(1).strip()

                    if 'E-mail' in line or 'email' in line.lower():
                        email_match = re.search(r'[：:]\s*(.+)', line)
                        if email_match:
                            email = email_match.group(1).strip()

                    if '授課領域' in line:
                        teaching_match = re.search(r'[：:]\s*(.+)', line)
                        if teaching_match:
                            teaching = teaching_match.group(1).strip()
                        elif i + 1 < len(lines):
                            teaching = lines[i + 1].strip()

                    if '研究專長' in line:
                        research_match = re.search(r'[：:]\s*(.+)', line)
                        if research_match:
                            research = research_match.group(1).strip()
                        elif i + 1 < len(lines):
                            research = lines[i + 1].strip()

                if name or photo_filename:  # 只有在找到姓名或照片時才添加
                    teacher_info = {
                        'name': name,
                        'photo': f'../images/faculty/{photo_filename}' if photo_filename else '',
                        'phone': phone,
                        'email': email,
                        'teaching': teaching,
                        'research': research
                    }
                    practical_teachers.append(teacher_info)
                    print(f"  ✓ 提取教師: {name}")

            return practical_teachers

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
    print("開始爬取林照真老師和實務教師頁面")
    print("=" * 60)

    # 1. 爬取林照真老師的照片
    lincc_photo = fetch_lincc_page()

    if lincc_photo:
        print(f"\n✓ 成功獲取林照真老師照片: {lincc_photo}")

        # 更新 faculty_data.json
        faculty_data_path = Path(__file__).parent / 'faculty_data.json'
        with open(faculty_data_path, 'r', encoding='utf-8') as f:
            faculty_data = json.load(f)

        # 找到林照真並更新照片
        for teacher in faculty_data['fulltime']:
            if '林照真' in teacher['name']:
                teacher['photo'] = f'../images/faculty/{lincc_photo}'
                print(f"  已更新 faculty_data.json 中的照片路徑")
                break

        with open(faculty_data_path, 'w', encoding='utf-8') as f:
            json.dump(faculty_data, f, ensure_ascii=False, indent=2)

    # 2. 爬取實務教師
    practical_teachers = extract_practical_teachers()

    if practical_teachers:
        print(f"\n✓ 成功提取 {len(practical_teachers)} 位實務教師")

        # 保存實務教師資料
        practical_data_path = Path(__file__).parent / 'practical_faculty_data.json'
        with open(practical_data_path, 'w', encoding='utf-8') as f:
            json.dump({
                'practical': practical_teachers
            }, f, ensure_ascii=False, indent=2)

        print(f"\n已保存實務教師資料到 {practical_data_path}")
        print("\n實務教師列表:")
        for teacher in practical_teachers:
            print(f"  - {teacher['name']}")

    print("\n" + "=" * 60)
    print("爬取完成！")
    print("=" * 60)

if __name__ == '__main__':
    main()
