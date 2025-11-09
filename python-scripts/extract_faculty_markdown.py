#!/usr/bin/env python3
"""
將教師頁面內容提取為 Markdown 格式
"""

import json
from pathlib import Path
from bs4 import BeautifulSoup
import html2text

def html_to_markdown(html_content):
    """將 HTML 轉換為 Markdown"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # 不自動換行
    h.unicode_snob = True
    h.ignore_tables = False

    # 轉換為 Markdown
    markdown = h.handle(html_content)

    # 清理多餘的空行
    lines = markdown.split('\n')
    cleaned_lines = []
    prev_empty = False

    for line in lines:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue  # 跳過連續的空行
        cleaned_lines.append(line)
        prev_empty = is_empty

    return '\n'.join(cleaned_lines)

def extract_faculty_content(html_file):
    """從教師頁面提取內容"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 提取教師姓名
        name_elem = soup.find('h3', id='faculty-name-main')
        if not name_elem:
            name_elem = soup.find('h2', id='faculty-name-header')
        faculty_name = name_elem.text.strip() if name_elem else "未知教師"

        # 提取聯絡資訊
        contact_info = {}
        contact_div = soup.find('div', id='contact-info')
        if contact_div:
            # 提取 Email
            email_elem = contact_div.find('a', href=lambda x: x and x.startswith('mailto:'))
            if email_elem:
                contact_info['email'] = email_elem.text.strip()

            # 提取授課領域
            for div in contact_div.find_all('div', class_='flex'):
                label = div.find('span', class_='info-label')
                if label and '授課領域' in label.text:
                    value_span = label.find_next_sibling('span')
                    if value_span:
                        contact_info['teaching'] = value_span.text.strip()

        # 提取詳細資訊
        detailed_div = soup.find('div', id='detailed-info')
        if not detailed_div:
            return None, None

        # 找到內容區域
        content_area = detailed_div.find('div', class_='area-editor')
        if not content_area:
            return None, None

        # 移除 hr 標籤（橫線）
        for hr in content_area.find_all('hr'):
            hr.decompose()

        # 轉換為 Markdown
        html_content = str(content_area)
        markdown_content = html_to_markdown(html_content)

        # 組合完整的 Markdown
        full_markdown = f"# {faculty_name}\n\n"

        if contact_info.get('email'):
            full_markdown += f"**Email：** {contact_info['email']}\n\n"

        if contact_info.get('teaching'):
            full_markdown += f"**授課領域：** {contact_info['teaching']}\n\n"

        full_markdown += "---\n\n"
        full_markdown += markdown_content

        return faculty_name, full_markdown

    except Exception as e:
        print(f"錯誤處理 {html_file}: {e}")
        return None, None

def main():
    """主程序"""
    print("=" * 60)
    print("提取教師內容為 Markdown 格式")
    print("=" * 60)
    print()

    # 創建輸出目錄
    output_dir = Path('faculty/content')
    output_dir.mkdir(exist_ok=True)

    # 讀取教師資料
    with open('faculty_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    success_count = 0
    total_count = len(data['fulltime'])

    for faculty in data['fulltime']:
        faculty_file = faculty['file']
        # 確保路徑正確
        if not faculty_file.startswith('faculty/'):
            faculty_file = 'faculty/' + faculty_file
        html_path = Path(faculty_file)

        if not html_path.exists():
            print(f"✗ 文件不存在: {faculty_file}")
            continue

        print(f"處理: {faculty['name']}")

        faculty_name, markdown_content = extract_faculty_content(html_path)

        if markdown_content:
            # 生成 Markdown 文件名（基於原始文件名）
            md_filename = html_path.stem + '.md'
            output_path = output_dir / md_filename

            # 寫入 Markdown 文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"✓ 已生成: {output_path}")
            success_count += 1
        else:
            print(f"✗ 提取失敗")

        print()

    print("=" * 60)
    print(f"完成！成功生成 {success_count}/{total_count} 個 Markdown 文件")
    print("=" * 60)

if __name__ == '__main__':
    main()
