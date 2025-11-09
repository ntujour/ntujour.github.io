#!/usr/bin/env python3
"""
將所有頁面的「招生專區」改為「入學資訊」
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

def replace_in_file(filepath):
    """替換單個文件中的文字"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            print(f"跳過 (編碼錯誤): {filepath}")
            return False

    if '招生專區' in content:
        content = content.replace('招生專區', '入學資訊')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filepath}")
        return True
    return False

def main():
    """主函數"""
    count = 0
    for html_file in BASE_DIR.rglob('*.html'):
        if replace_in_file(html_file):
            count += 1

    print(f"\n✅ 已更新 {count} 個文件")

if __name__ == '__main__':
    main()
