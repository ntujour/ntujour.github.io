#!/usr/bin/env python3
"""
台大新聞所內容管理系統 (CMS)
整合內容編輯器和 CSV 儲存功能
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from pathlib import Path
import urllib.parse
from datetime import datetime
import shutil
import mimetypes
import base64
import uuid

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / 'data' / 'content.csv'
NEWS_IMAGE_DIR = BASE_DIR / 'images' / 'news'
ACTIVITIES_IMAGE_DIR = BASE_DIR / 'images' / 'activities'

class CMSHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """處理 GET 請求 - 提供靜態檔案"""
        if self.path == '/' or self.path == '/cms':
            # 重定向到編輯器
            self.send_response(302)
            self.send_header('Location', '/admin/content-editor-v2.html')
            self.end_headers()
        else:
            # 使用父類別的 do_GET 處理靜態檔案
            super().do_GET()
    
    def do_OPTIONS(self):
        """處理 CORS 預檢請求"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        """處理 POST 請求 - 儲存 CSV 或上傳圖片"""
        if self.path == '/upload-image':
            try:
                # 讀取請求內容
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # 取得 Base64 圖片資料
                image_data = data.get('imageData', '')
                article_id = data.get('articleId', '')
                article_type = data.get('articleType', 'news')  # 'news' or 'activity'
                image_index = data.get('imageIndex', 1)  # 第幾張圖片（1, 2, 3...）

                if not image_data:
                    raise ValueError("圖片資料為空")

                if not article_id:
                    raise ValueError("文章 ID 為空")

                # 解析 Base64 資料 (格式: data:image/jpeg;base64,/9j/4AAQ...)
                if ',' in image_data:
                    header, encoded = image_data.split(',', 1)
                    # 從 header 取得 MIME type
                    if 'image/' in header:
                        mime_type = header.split(';')[0].split(':')[1]
                        ext = mimetypes.guess_extension(mime_type) or '.jpg'
                    else:
                        ext = '.jpg'
                else:
                    encoded = image_data
                    ext = '.jpg'

                # 確保副檔名正確（處理 .jpe 等問題）
                if ext == '.jpe':
                    ext = '.jpg'

                # 解碼 Base64
                image_bytes = base64.b64decode(encoded)

                # 根據類型決定目錄
                if article_type == 'activity':
                    upload_dir = ACTIVITIES_IMAGE_DIR
                    dir_name = 'activities'
                else:
                    upload_dir = NEWS_IMAGE_DIR
                    dir_name = 'news'

                # 確保上傳目錄存在
                upload_dir.mkdir(parents=True, exist_ok=True)

                # 生成檔名: news-259107-1.png 或 activity-259107-1.png
                safe_filename = f"{article_type}-{article_id}-{image_index}{ext}"

                # 儲存檔案
                file_path = upload_dir / safe_filename
                file_path.write_bytes(image_bytes)

                # 回傳相對路徑（從網站根目錄開始）
                relative_path = f"images/{dir_name}/{safe_filename}"

                print(f"✅ 圖片已上傳: {relative_path} ({len(image_bytes) / 1024:.2f} KB)")

                # 回應成功
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                response = json.dumps({
                    'success': True,
                    'path': relative_path,
                    'filename': safe_filename,
                    'size': len(image_bytes)
                })
                self.wfile.write(response.encode('utf-8'))

            except Exception as e:
                print(f"❌ 圖片上傳錯誤: {str(e)}")

                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                response = json.dumps({
                    'success': False,
                    'error': str(e)
                })
                self.wfile.write(response.encode('utf-8'))

        elif self.path == '/save-csv':
            try:
                # 讀取請求內容
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                csv_content = data.get('csv', '')

                if not csv_content:
                    raise ValueError("CSV 內容為空")

                # 備份現有檔案
                if CSV_FILE.exists():
                    backup_dir = BASE_DIR / 'data' / 'backups'
                    backup_dir.mkdir(exist_ok=True)

                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_file = backup_dir / f'content_{timestamp}.csv'
                    shutil.copy(CSV_FILE, backup_file)
                    print(f"✅ 已備份到: {backup_file}")

                # 寫入新內容
                CSV_FILE.write_text(csv_content, encoding='utf-8')

                # 正確統計資料筆數（使用 csv 模組）
                import csv as csv_module
                from io import StringIO

                csv_reader = csv_module.DictReader(StringIO(csv_content))
                row_count = sum(1 for row in csv_reader if any(row.values()))  # 只計算非空行

                print(f"💾 CSV 已儲存: {CSV_FILE} ({row_count} 筆資料)")

                # 回應成功
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                response = json.dumps({
                    'success': True,
                    'message': f'成功儲存 {row_count} 筆資料',
                    'timestamp': datetime.now().isoformat()
                })
                self.wfile.write(response.encode('utf-8'))

            except Exception as e:
                print(f"❌ 儲存錯誤: {str(e)}")

                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                response = json.dumps({
                    'success': False,
                    'error': str(e)
                })
                self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """自訂日誌格式"""
        if self.path != '/save-csv':  # 只顯示非 save-csv 的請求
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {self.command} {self.path}")

def run_cms(port=8080):
    """啟動 CMS 伺服器"""
    
    # 確保資料目錄存在
    (BASE_DIR / 'data' / 'backups').mkdir(parents=True, exist_ok=True)
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, CMSHandler)
    
    print("=" * 60)
    print("🎯 台大新聞所內容管理系統 (CMS) v2")
    print("=" * 60)
    print(f"🚀 伺服器啟動於: http://localhost:{port}")
    print(f"📝 編輯器網址: http://localhost:{port}/admin/content-editor-v2.html")
    print(f"💾 CSV 儲存端點: http://localhost:{port}/save-csv")
    print(f"📷 圖片上傳端點: http://localhost:{port}/upload-image")
    print(f"📁 資料檔案: {CSV_FILE}")
    print(f"🖼️  新聞圖片目錄: {NEWS_IMAGE_DIR}")
    print(f"🖼️  活動圖片目錄: {ACTIVITIES_IMAGE_DIR}")
    print(f"💼 備份目錄: {BASE_DIR / 'data' / 'backups'}")
    print("=" * 60)
    print("按 Ctrl+C 停止伺服器")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("⏹️  CMS 伺服器已停止")
        print("=" * 60)

if __name__ == '__main__':
    run_cms()
