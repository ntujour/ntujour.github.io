#!/usr/bin/env python3
"""
簡單的 HTTP 伺服器，用於儲存 CSV 檔案
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pathlib import Path
import urllib.parse

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / 'data' / 'content.csv'

class SaveCSVHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """處理 CORS 預檢請求"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """儲存 CSV 檔案"""
        if self.path == '/save-csv':
            try:
                # 讀取請求內容
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                csv_content = data.get('csv', '')

                if not csv_content:
                    self.send_error(400, 'No CSV content provided')
                    return

                # 備份原檔案
                if CSV_FILE.exists():
                    backup_file = CSV_FILE.with_suffix('.csv.backup')
                    CSV_FILE.rename(backup_file)
                    print(f"✅ 已備份原檔案到: {backup_file}")

                # 儲存新檔案
                with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
                    f.write(csv_content)

                print(f"✅ CSV 已儲存到: {CSV_FILE}")

                # 回傳成功訊息
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                response = {
                    'success': True,
                    'message': 'CSV 檔案已成功儲存',
                    'file': str(CSV_FILE)
                }
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))

            except Exception as e:
                print(f"❌ 錯誤: {str(e)}")
                self.send_error(500, f'Error saving CSV: {str(e)}')
        else:
            self.send_error(404, 'Not Found')

    def log_message(self, format, *args):
        """自訂日誌格式"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_server(port=8001):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SaveCSVHandler)
    print(f"🚀 CSV 儲存伺服器已啟動在 http://localhost:{port}")
    print(f"📝 CSV 檔案位置: {CSV_FILE}")
    print("按 Ctrl+C 停止伺服器")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  伺服器已停止")
        httpd.shutdown()

if __name__ == '__main__':
    run_server()
