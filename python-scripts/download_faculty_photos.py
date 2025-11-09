#!/usr/bin/env python3
"""
從原始網站下載教師照片
"""

import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_photo(img_url, save_path):
    """下載照片"""
    try:
        # 如果是相對路徑，轉換為絕對路徑
        if img_url.startswith('001/Upload'):
            full_url = f'http://www.journalism.ntu.edu.tw/{img_url}'
        else:
            full_url = img_url

        print(f"下載: {full_url}")
        response = requests.get(full_url, verify=False, timeout=10)

        if response.status_code == 200:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"✓ 已儲存: {save_path}")
            return True
        else:
            print(f"✗ 下載失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 錯誤: {e}")
        return False

def extract_photo_from_html(html_file):
    """從本地HTML文件提取照片URL"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        img = soup.find('img', alt='Art editor Img')

        if img and 'src' in img.attrs:
            return img['src']
        return None
    except Exception as e:
        print(f"錯誤讀取 {html_file}: {e}")
        return None

def main():
    base_dir = Path(__file__).parent
    faculty_dir = base_dir / 'faculty'
    images_dir = base_dir / 'images' / 'faculty'

    # 從JSON讀取教師資料
    json_file = base_dir / 'faculty_data.json'
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("開始下載教師照片...\n")

    for faculty in data['fulltime']:
        name = faculty['name']
        html_file = faculty_dir / faculty['file']
        photo_path = faculty['photo']

        print(f"\n處理: {name}")

        # 從HTML文件提取照片URL
        img_url = extract_photo_from_html(html_file)

        if img_url:
            # 取得檔案名稱
            filename = Path(photo_path).name
            save_path = images_dir / filename

            # 下載照片
            download_photo(img_url, save_path)
        else:
            print(f"✗ 找不到照片URL")

    print("\n完成！")

if __name__ == '__main__':
    main()
