# Admin 登入說明：按「Netlify 登入」後跳回

## 為什麼會跳回來？

當你在**本機**打開 admin（例如 `http://localhost:8000/admin/`）並點「使用你的 Netlify 帳號來進行登入」時：

1. 瀏覽器會導向 Netlify 登入頁。
2. 登入成功後，Netlify 會把您導回「**已設定的網站網址**」（例如 `https://你的站.netlify.app/admin/`）。
3. 您現在是在 **localhost**，不是 Netlify 的網址，所以導回時會變成回到本機或錯誤頁，看起來就像「按了又跳回登入頁」。

也就是說：**Netlify 登入只適合在「已部署到 Netlify 的網址」使用**，不適合在 localhost 使用。

---

## 解決方式

### 方式一：本機編輯（不用 Netlify 登入，推薦開發時用）

使用 **Decap 本地後端**，在本機就能編輯內容，不需點 Netlify 按鈕。

1. **安裝並啟動本地後端**（在專案根目錄執行一次即可）：
   ```bash
   npx decap-server
   ```
   預設會佔用 **8081**，若 8081 已被使用，請看下方「自訂 port」。

2. **啟動靜態網站**（另開一個終端機）：
   ```bash
   python3 -m http.server 8000
   ```

3. **開啟 Admin**  
   瀏覽器打開：**http://localhost:8000/admin/**  
   此時 CMS 會連到本機後端（8081），**不會**再要求用 Netlify 登入，可直接編輯並寫入本機 repo。

4. **自訂 port（若 8081 被佔用）**  
   在專案根目錄建立 `.env`，例如：
   ```env
   PORT=8082
   ```
   並在 `admin/config.yml` 的 `local_backend` 改成：
   ```yaml
   local_backend:
     url: http://localhost:8082/api/v1
   ```
   再執行 `npx decap-server`（會改用 8082）。

**注意**：`decap-server` 僅供本機開發使用，不要對外網開放。

---

### 方式二：用 Netlify 登入（正式環境）

若您要使用「使用你的 Netlify 帳號來進行登入」：

1. 網站需已部署到 Netlify（且已設定 Netlify Identity / Git Gateway）。
2. 請改開 **Netlify 上的網址**，例如：
   - `https://你的站名.netlify.app/admin/`
   或您自訂的網域對應到的 `/admin/`。
3. 在該網址點「使用你的 Netlify 帳號來進行登入」，登入後就會正常留在 admin 頁面，不會再跳回。

---

## 總結

| 情境           | 作法 |
|----------------|------|
| 本機開發、想改內容 | 用**方式一**：先 `npx decap-server`，再開 `http://localhost:8000/admin/`，不要點 Netlify 登入。 |
| 正式環境、要用 Netlify 帳號 | 用**方式二**：開 `https://你的站.netlify.app/admin/` 再點 Netlify 登入。 |

您目前遇到的「按了以後來不及輸入又跳回來」是因為在本機 (localhost) 使用 Netlify 登入；改成本機用 decap-server，或改到 Netlify 網址再登入，即可解決。
