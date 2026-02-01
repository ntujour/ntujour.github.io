#!/usr/bin/env python3
"""
解析 news/ 和 activities/ 目錄下的所有 HTML 文章
提取標題、日期、分類、內容等資訊，並儲存到 CSV
"""

import os
import re
import csv
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import html

# 設定基礎目錄
BASE_DIR = Path(__file__).parent.parent

def extract_id_from_filename(filename):
    """從檔名提取 ID (例如: News_Content_n_35497_s_259107.html -> 259107)"""
    match = re.search(r'_s_(\d+)\.html$', filename)
    if match:
        return match.group(1)
    # 如果沒有 _s_ 格式,嘗試其他模式
    match = re.search(r'_(\d+)\.html$', filename)
    if match:
        return match.group(1)
    # 如果都沒有,使用時間戳
    return str(int(datetime.now().timestamp()))

def extract_date(soup, filepath):
    """提取發布日期"""
    # 嘗試從 meta 標籤提取
    meta_date = soup.find('meta', {'name': 'DC.Date'})
    if meta_date and meta_date.get('content'):
        return meta_date.get('content')

    # 嘗試找包含「發布」或「日期」的元素
    date_patterns = [
        r'發布日期[：:]\s*(\d{4}[/-]\d{1,2}[/-]\d{1,2})',
        r'(\d{4}[/-]\d{1,2}[/-]\d{1,2})',
        r'發表日期[：:]\s*(\d{4}[/-]\d{1,2}[/-]\d{1,2})'
    ]

    text = soup.get_text()
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            date_str = match.group(1).replace('/', '-')
            return date_str

    # 使用檔案修改時間
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

def extract_title(soup):
    """提取標題"""
    # 先在HTML中找包含【】或特殊格式的標題
    text = soup.get_text()

    # 尋找【】格式的標題 (例如：【招生訊息】115學年度甄試招生簡章)
    bracket_title_match = re.search(r'【[^】]+】[^\n]{5,80}', text)
    if bracket_title_match:
        title = bracket_title_match.group().strip()
        # 清理多餘空白
        title = re.sub(r'\s+', ' ', title)
        if len(title) > 5:
            return title

    # 嘗試從 span 標籤找標題 (很多新聞標題在 span 中)
    for span in soup.find_all('span'):
        span_text = span.get_text().strip()
        # 檢查是否符合標題特徵
        if (span_text.startswith('【') or
            span_text.startswith('【') or
            (len(span_text) > 10 and len(span_text) < 100 and '：' not in span_text)):
            # 排除導航、連結等常見文字
            if any(keyword in span_text for keyword in [':::',  '回上一頁', '回最上面', '列印', '分享']):
                continue
            if len(span_text) > 10:
                return re.sub(r'\s+', ' ', span_text)

    # 嘗試從 meta 標籤提取
    meta_title = soup.find('meta', {'name': 'DC.Title'})
    if meta_title and meta_title.get('content'):
        title = meta_title.get('content')
        if title and len(title) > 3 and '網頁' not in title:
            return title

    # 嘗試從 title 標籤
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text().strip()
        # 移除常見的網站名稱
        title = re.sub(r'\s*[-|]\s*(國立臺灣大學|新聞研究所|臺大新聞所).*$', '', title)
        if title and len(title) > 3 and '網頁' not in title:
            return title

    # 嘗試找主要標題 h1, h2
    for tag in ['h1', 'h2', 'h3']:
        heading = soup.find(tag)
        if heading:
            title = heading.get_text().strip()
            if title and len(title) > 5 and '網頁' not in title:
                return title

    return "無標題"

def extract_content(soup):
    """提取主要內容 - 改進版：只提取純文字段落，保持簡潔"""

    # 移除不需要的標籤
    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'iframe']):
        tag.decompose()

    # 尋找所有段落
    paragraphs = soup.find_all('p')

    valid_content = []
    seen_text = set()  # 用於去重

    for p in paragraphs:
        # 取得純文字內容
        text = p.get_text().strip()

        # 過濾條件
        if len(text) < 15:  # 太短的段落
            continue
        if text in seen_text:  # 重複的段落
            continue
        if any(keyword in text for keyword in [
            ':::', '回首頁', '回上一頁', '回最上面', '列印', '分享',
            'Facebook', 'Twitter', 'Line', 'Email', 'LinkedIn',
            '另開新視窗', '網站導覽', 'Copyright', '上版日期',
            'Share to', 'Bopomofo', '網頁功能', '相關檔案', '相關圖片'
        ]):
            continue

        seen_text.add(text)

        # 保留基本的 HTML 結構（只保留 p, strong, em, br, a）
        # 先清理 p 標籤內的複雜結構
        p_copy = BeautifulSoup(str(p), 'html.parser')

        # 移除所有 span, div, 保留 p, strong, em, br, a, ul, li
        for tag in p_copy.find_all(True):
            if tag.name not in ['p', 'strong', 'em', 'br', 'a', 'ul', 'ol', 'li', 'b', 'i']:
                tag.unwrap()

        # 清理屬性（只保留 href）
        for tag in p_copy.find_all(True):
            attrs_to_keep = {}
            if tag.name == 'a' and tag.get('href'):
                attrs_to_keep['href'] = tag.get('href')
            tag.attrs = attrs_to_keep

        clean_html = str(p_copy)
        valid_content.append(clean_html)

    if valid_content:
        # 只返回前 10 個段落，避免內容過長
        return '\n'.join(valid_content[:10])

    # 如果沒有找到有效段落，嘗試找 ul/ol 列表
    lists = soup.find_all(['ul', 'ol'])
    if lists:
        for lst in lists[:3]:  # 最多 3 個列表
            text = lst.get_text().strip()
            if len(text) > 20:
                # 簡化列表HTML
                clean_list = BeautifulSoup(str(lst), 'html.parser')
                for tag in clean_list.find_all(True):
                    if tag.name not in ['ul', 'ol', 'li']:
                        tag.unwrap()
                valid_content.append(str(clean_list))

    if valid_content:
        return '\n'.join(valid_content)

    return "<p>無內容</p>"

def extract_category(filepath, soup, title):
    """提取分類（根據標題優先，再檢查內容）"""

    # 優先從標題中提取分類
    if title:
        title_category_map = {
            '招生': ['招生', '甄試', '入學', '報名', '考試'],
            '榮譽': ['榮譽', '獲獎', '得獎', '表揚', '恭賀', '賀'],
            '徵才': ['徵才', '招募', '應徵', '職缺', '人才'],
            '演講': ['演講', '講座', '座談', '分享會'],
            '學術': ['學術', '研討會', '論文', '期刊', '研究'],
            '活動': ['活動', '工作坊', '研習', '參訪', '活動預告'],
            '公告': ['公告', '通知', '重要事項', '注意']
        }

        for category, keywords in title_category_map.items():
            for keyword in keywords:
                if keyword in title:
                    return category

    # 如果標題中沒有找到，再檢查內容
    text = soup.get_text()

    # 內容關鍵字（範圍更精確）
    content_categories = {
        '招生': ['招生簡章', '口試', '筆試', '錄取'],
        '榮譽': ['獲獎名單', '得獎', '優選', '首獎'],
        '徵才': ['徵求', '職缺公告', '招募啟事'],
        '演講': ['講者', '主講人', '歡迎參加'],
        '學術': ['研討會議程', '論文發表', 'Call for Papers'],
        '活動': ['報名資訊', '活動時間', '活動地點']
    }

    for category, keywords in content_categories.items():
        for keyword in keywords:
            if keyword in text[:1000]:  # 檢查前1000字
                return category

    return ''

def extract_images(soup):
    """提取文章中的圖片 URL"""
    images = []

    # 尋找所有帶 data-src 屬性的元素（相關圖片區塊）
    for element in soup.find_all(attrs={'data-src': True}):
        img_url = element.get('data-src')
        if img_url and img_url.startswith('http'):
            images.append(img_url)

    # 如果沒找到 data-src，嘗試找一般的 img 標籤
    if not images:
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and (src.startswith('http') or src.startswith('001/Upload')):
                # 如果是相對路徑，轉換為完整 URL
                if src.startswith('001/Upload'):
                    src = f"https://webpageprod-ws.ntu.edu.tw/{src}"
                images.append(src)

    # 去重並返回（用 ||| 分隔多張圖片）
    unique_images = []
    seen = set()
    for img in images:
        if img not in seen:
            seen.add(img)
            unique_images.append(img)

    return '|||'.join(unique_images) if unique_images else ''

def parse_html_file(filepath):
    """解析單個 HTML 檔案"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # 提取資訊
        item_id = extract_id_from_filename(filepath.name)

        # 改進類型判斷：根據父目錄名稱
        parent_dir = filepath.parent.name
        item_type = 'activity' if parent_dir == 'activities' else 'news'

        title = extract_title(soup)
        date = extract_date(soup, filepath)
        category = extract_category(filepath, soup, title)  # 傳入 title 參數
        content_html = extract_content(soup)
        images = extract_images(soup)  # 提取圖片

        # 生成 slug
        slug = f"{item_type}-{item_id}"

        return {
            'id': item_id,
            'type': item_type,
            'title': title,
            'date': date,
            'category': category,
            'time': '',  # 活動時間（稍後可手動補充）
            'location': '',  # 活動地點（稍後可手動補充）
            'content': content_html,
            'slug': slug,
            'originalFile': filepath.name,
            'image': images  # 儲存圖片 URL
        }

    except Exception as e:
        print(f"❌ 解析失敗: {filepath.name} - {str(e)}")
        return None

def main():
    print("🔍 開始掃描 HTML 檔案...")

    # 掃描目錄
    news_dir = BASE_DIR / 'news'
    activities_dir = BASE_DIR / 'activities'

    html_files = []
    if news_dir.exists():
        html_files.extend(list(news_dir.glob('*.html')))
    if activities_dir.exists():
        html_files.extend(list(activities_dir.glob('*.html')))

    print(f"📁 找到 {len(html_files)} 個 HTML 檔案")

    # 解析所有檔案
    data = []
    success = 0
    failed = 0

    for i, filepath in enumerate(html_files, 1):
        print(f"[{i}/{len(html_files)}] 解析: {filepath.name}")
        result = parse_html_file(filepath)
        if result:
            data.append(result)
            success += 1
        else:
            failed += 1

    print(f"\n✅ 成功解析: {success} 個檔案")
    print(f"❌ 失敗: {failed} 個檔案")

    # 按日期排序（新的在前）
    data.sort(key=lambda x: x['date'], reverse=True)

    # 儲存到 CSV
    output_file = BASE_DIR / 'data' / 'content.csv'
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'type', 'title', 'date', 'category', 'time', 'location',
                      'content', 'slug', 'originalFile', 'image']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"\n💾 資料已儲存到: {output_file}")
    print(f"📊 總共 {len(data)} 筆資料")

    # 統計
    news_count = sum(1 for item in data if item['type'] == 'news')
    activity_count = sum(1 for item in data if item['type'] == 'activity')
    print(f"   - 新聞: {news_count} 筆")
    print(f"   - 活動: {activity_count} 筆")

if __name__ == '__main__':
    main()
