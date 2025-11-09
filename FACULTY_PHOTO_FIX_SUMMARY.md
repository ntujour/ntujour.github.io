# Faculty 照片尺寸修正總結

## ✅ 已完成的修改

### 1. 所有照片統一使用 Tailwind CSS

**個人頁面** (7個 HTML):
- w-64 h-64 (256px × 256px)
- object-cover (裁切適配)
- rounded-lg (圓角)
- shadow-md (陰影)

**列表頁面** (JavaScript 生成):
- w-full aspect-square (響應式正方形)
- object-cover
- rounded-lg
- shadow-sm, hover:shadow-md

**Practical 頁面 Tabs**:
- w-20 h-20 (80px × 80px)
- object-cover
- rounded-lg

### 2. CSS 已更新

**新增樣式**:
- `.faculty-tabs` - Tab 容器樣式
- `.faculty-tab` - Tab 按鈕樣式
- `.faculty-tab.active` - 活動 tab 樣式
- `.faculty-detail-card` - 詳細卡片樣式

### 3. Tailwind CSS 已重新編譯

```bash
npm run build:css
```

所有 Tailwind utility classes 都已正確包含在 css/tailwind.css 中。

### 4. 瀏覽器緩存提醒

如果照片仍顯示很大，請**強制刷新瀏覽器緩存**:
- Chrome/Edge: Ctrl+Shift+R (Windows) 或 Cmd+Shift+R (Mac)
- Firefox: Ctrl+F5 (Windows) 或 Cmd+Shift+R (Mac)
- Safari: Cmd+Option+R

## 修改的檔案清單

### HTML (7個)
- faculty/jerryhsieh.html
- faculty/lihyunlin.html
- faculty/clhung.html
- faculty/carolinelin.html
- faculty/tsaihuiju.html
- faculty/chanii311.html
- faculty/RauchfleischA.html

### JavaScript (6個)
- js/faculty.js
- js/fulltime-faculty-detail.js
- js/parttime-faculty-detail.js
- js/practical-faculty-detail.js
- js/honorary-faculty-detail.js
- js/joint-faculty-detail.js

### CSS (2個)
- css/site-common.css (新增 faculty tabs 樣式)
- css/tailwind.css (重新編譯)

## 驗證結果

```bash
# 個人頁面照片: 7/7 ✓
# JavaScript 詳細頁: 5/5 ✓
# 列表卡片: 5/5 ✓
# CSS tabs 樣式: ✓
# Tailwind 重新編譯: ✓
```

## 使用的 Tailwind Classes

| Class | 尺寸 | 用途 |
|-------|------|------|
| `w-20 h-20` | 80px × 80px | Tab 小照片 |
| `w-64 h-64` | 256px × 256px | 個人頁面大照片 |
| `w-full aspect-square` | 100% 寬度, 1:1 比例 | 列表頁卡片 |
| `object-cover` | - | 裁切適配 |
| `rounded-lg` | 8px | 圓角 |
| `shadow-md` | - | 中等陰影 |
| `shadow-sm` | - | 小陰影 |

