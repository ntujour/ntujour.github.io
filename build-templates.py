#!/usr/bin/env python3
"""
模板建置腳本
將 HTML 檔案中的 {{site-banner}}, {{site-nav}} 等標記替換為實際內容
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'templates'

# 載入所有模板
TEMPLATES = {}

def load_templates():
    """載入所有模板檔案"""
    print("載入模板檔案...")
    template_files = ['site-banner.html', 'site-nav.html', 'site-sitemap.html', 'site-footer.html', 'site-head-common.html']

    for template_file in template_files:
        template_path = TEMPLATES_DIR / template_file
        if template_path.exists():
            with open(template_path, 'r', encoding='utf-8') as f:
                template_name = template_file.replace('.html', '')
                TEMPLATES[template_name] = f.read()
                print(f"  ✓ {template_file}")
        else:
            print(f"  ✗ {template_file} 不存在")

    print(f"\n已載入 {len(TEMPLATES)} 個模板\n")

def calculate_path_prefix(file_path):
    """根據檔案位置計算路徑前綴"""
    # 計算檔案相對於根目錄的深度
    relative_path = file_path.relative_to(BASE_DIR)
    depth = len(relative_path.parts) - 1

    if depth == 0:
        # 在根目錄
        return ''
    else:
        # 在子目錄中
        return '../' * depth

def process_html_file(file_path):
    """處理單個 HTML 檔案"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ 無法讀取 {file_path}: {e}")
        return False

    original_content = content

    # 計算路徑前綴
    path_prefix = calculate_path_prefix(file_path)

    # 替換模板標記
    for template_name, template_content in TEMPLATES.items():
        placeholder = f'{{{{{template_name}}}}}'

        if placeholder in content:
            # 替換路徑前綴
            processed_template = template_content.replace('{{path_prefix}}', path_prefix)
            content = content.replace(placeholder, processed_template)

    # 如果有變更，寫回檔案
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def build_all():
    """建置所有 HTML 檔案"""
    print("=" * 70)
    print("開始建置模板")
    print("=" * 70)
    print()

    # 載入模板
    load_templates()

    # 找出所有包含模板標記的 HTML 檔案
    print("搜尋包含模板標記的檔案...")
    html_files = list(BASE_DIR.glob('**/*.html'))

    # 排除 templates 和 .archive 目錄
    html_files = [f for f in html_files
                  if 'templates' not in str(f) and '.archive' not in str(f)]

    files_with_templates = []
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if '{{site-' in content:
                    files_with_templates.append(file_path)
        except:
            pass

    print(f"找到 {len(files_with_templates)} 個包含模板標記的檔案\n")

    if len(files_with_templates) == 0:
        print("沒有檔案需要處理")
        return

    print("-" * 70)
    print("處理檔案:")
    print("-" * 70)

    processed_count = 0
    for file_path in files_with_templates:
        relative_path = file_path.relative_to(BASE_DIR)
        if process_html_file(file_path):
            print(f"  ✓ {relative_path}")
            processed_count += 1
        else:
            print(f"  - {relative_path} (無變更)")

    print("-" * 70)
    print(f"\n總共處理了 {processed_count} 個檔案")
    print()
    print("=" * 70)
    print("建置完成！")
    print("=" * 70)

if __name__ == '__main__':
    build_all()
