#!/usr/bin/env python3
"""
從原始網站獲取林照真老師的頁面
"""

import requests
import urllib3
from pathlib import Path

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_faculty_page(url, filename):
    """從原始網站獲取教師頁面"""
    try:
        print(f"正在獲取: {url}")
        response = requests.get(url, verify=False, timeout=10)

        if response.status_code == 200:
            # 設定正確的編碼
            response.encoding = 'utf-8'

            save_path = Path(__file__).parent / 'faculty' / filename
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(response.text)

            print(f"✓ 已儲存: {save_path}")
            return True
        else:
            print(f"✗ 獲取失敗: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 錯誤: {e}")
        return False

def main():
    # 林照真老師的頁面URL（從原始網站結構推測）
    url = "http://www.journalism.ntu.edu.tw/faculty/lincc.html"

    if fetch_faculty_page(url, 'lincc.html'):
        print("\n成功獲取林照真老師的頁面！")
        print("請重新執行 extract_faculty_data.py 來提取資料")
    else:
        print("\n無法獲取頁面，可能URL不正確")
        print("請手動檢查原始網站的教師列表")

if __name__ == '__main__':
    main()
