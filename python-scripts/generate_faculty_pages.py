#!/usr/bin/env python3
"""
為每位專任教師生成統一版式的個人頁面
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_detailed_info_from_html(html_file):
    """從原始HTML文件中提取詳細資訊"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 尋找主要內容區域
        editor_area = soup.find('div', class_='area-editor user-edit')
        if not editor_area:
            return None

        # 移除照片img標籤（因為照片會單獨顯示）
        img_tag = editor_area.find('img', alt='Art editor Img')
        if img_tag:
            img_tag.decompose()

        # 清理多餘空白：將連續的空白字符替換為單一空格
        # 處理所有文本節點
        for element in editor_area.find_all(string=True):
            if element.parent.name not in ['script', 'style']:
                # 替換連續的空白字符（空格、tab、全角空格等）為單一空格
                cleaned_text = re.sub(r'[\s\u3000]+', ' ', str(element))
                # 如果文本只包含空白，保留單個空格
                if cleaned_text.strip():
                    element.replace_with(cleaned_text)
                elif str(element).strip() == '':
                    element.replace_with(' ')

        # 獲取處理後的HTML
        processed_html = str(editor_area)

        return processed_html
    except Exception as e:
        print(f"錯誤處理 {html_file}: {e}")
        return None

def generate_faculty_page(faculty_info, template_path, output_path):
    """生成教師個人頁面"""
    try:
        # 讀取模板
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # 替換基本資訊
        page_content = template.replace('[教師姓名]', faculty_info['name'])

        # 設置照片
        photo_html = f'<img id="faculty-photo" src="{faculty_info["photo"]}" alt="{faculty_info["name"]}" class="faculty-profile-photo mx-auto md:mx-0">'
        page_content = page_content.replace('<img id="faculty-photo" src="" alt="" class="faculty-profile-photo mx-auto md:mx-0">', photo_html)

        # 生成聯絡資訊HTML - 使用統一字級 text-base
        contact_html = ''
        if faculty_info.get('phone'):
            contact_html += f'''
                <div class="flex items-start text-base">
                    <span class="info-label">聯絡電話：</span>
                    <span class="text-gray-600">{faculty_info["phone"]}</span>
                </div>
            '''

        if faculty_info.get('email'):
            contact_html += f'''
                <div class="flex items-start text-base">
                    <span class="info-label">Email：</span>
                    <span class="text-gray-600"><a href="mailto:{faculty_info["email"]}" class="hover:text-gray-900">{faculty_info["email"]}</a></span>
                </div>
            '''

        if faculty_info.get('teaching'):
            contact_html += f'''
                <div class="flex items-start text-base">
                    <span class="info-label">授課領域：</span>
                    <span class="text-gray-600">{faculty_info["teaching"]}</span>
                </div>
            '''

        if faculty_info.get('research'):
            contact_html += f'''
                <div class="flex items-start text-base">
                    <span class="info-label">研究專長：</span>
                    <span class="text-gray-600">{faculty_info["research"]}</span>
                </div>
            '''

        page_content = page_content.replace(
            '<div class="space-y-3 text-base" id="contact-info">\n                        <!-- 聯絡資訊將由JavaScript動態載入 -->\n                    </div>',
            f'<div class="space-y-3 text-base" id="contact-info">{contact_html}\n                    </div>'
        )

        # 提取詳細資訊（學歷、經歷等）
        faculty_html_file = Path(__file__).parent / 'faculty' / faculty_info['file']
        detailed_html = extract_detailed_info_from_html(faculty_html_file)

        if detailed_html:
            # 清理HTML內容
            soup = BeautifulSoup(detailed_html, 'html.parser')

            # 移除聯絡資訊段落（因為已經在上面顯示）
            for p in soup.find_all('p'):
                text = p.get_text()
                if '聯絡電話' in text or 'E-mail' in text or '授課領域' in text or '研究專長' in text:
                    p.decompose()

            # 獲取清理後的HTML
            detailed_html = str(soup)

            # 添加樣式包裝 - 使用統一字級
            detailed_content = f'''
                <div class="content-section text-base">
                    {detailed_html}
                </div>
            '''
        else:
            detailed_content = ''

        page_content = page_content.replace(
            '<div id="detailed-info">\n                <!-- 詳細資訊將由JavaScript動態載入 -->\n            </div>',
            f'<div id="detailed-info">{detailed_content}\n            </div>'
        )

        # 移除JavaScript引用（因為不再需要動態載入）
        page_content = page_content.replace('<script src="../js/fulltime-faculty-profile.js"></script>', '')

        # 保存文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_content)

        print(f"✓ 已生成: {output_path.name}")
        return True

    except Exception as e:
        print(f"✗ 生成失敗 {output_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("為專任教師生成統一版式的個人頁面")
    print("=" * 60)

    # 讀取教師資料
    faculty_data_path = Path(__file__).parent / 'faculty_data.json'
    with open(faculty_data_path, 'r', encoding='utf-8') as f:
        faculty_data = json.load(f)

    fulltime_faculty = faculty_data.get('fulltime', [])

    if not fulltime_faculty:
        print("未找到專任教師資料")
        return

    # 模板文件路徑
    template_path = Path(__file__).parent / 'faculty' / 'fulltime-faculty-template.html'

    if not template_path.exists():
        print(f"模板文件不存在: {template_path}")
        return

    # 為每位教師生成頁面
    success_count = 0
    for faculty in fulltime_faculty:
        faculty_filename = faculty['file']
        output_path = Path(__file__).parent / 'faculty' / f'{faculty_filename.replace(".html", "")}-new.html'

        print(f"\n處理: {faculty['name']}")
        if generate_faculty_page(faculty, template_path, output_path):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"完成！成功生成 {success_count}/{len(fulltime_faculty)} 個頁面")
    print("=" * 60)

    # 詢問是否要替換原始文件
    print("\n新頁面已生成為 *-new.html")
    print("如果確認無誤，可以手動將新文件重命名以替換原始文件")

if __name__ == '__main__':
    main()
