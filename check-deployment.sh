#!/bin/bash
# ====================================
# GitHub Pages 部署前檢查腳本
# ====================================

echo "🔍 開始檢查 GitHub Pages 部署準備..."
echo ""

ERRORS=0
WARNINGS=0

# ============ 必要檔案檢查 ============
echo "📋 檢查必要檔案..."

check_file() {
    if [ -f "$1" ]; then
        size=$(ls -lh "$1" | awk '{print $5}')
        echo "  ✅ $1 ($size)"
    else
        echo "  ❌ $1 不存在！"
        ((ERRORS++))
    fi
}

check_file "css/tailwind.css"
check_file "data/faculty_data.json"
check_file "data/activities.json"
check_file "data/news.json"
check_file "index.html"
check_file "build-templates.py"

echo ""

# ============ JSON 格式檢查 ============
echo "🔍 檢查 JSON 格式..."

if command -v python3 &> /dev/null; then
    if python3 -m json.tool data/faculty_data.json > /dev/null 2>&1; then
        echo "  ✅ faculty_data.json 格式正確"
    else
        echo "  ❌ faculty_data.json 格式錯誤！"
        ((ERRORS++))
    fi

    if python3 -m json.tool data/activities.json > /dev/null 2>&1; then
        echo "  ✅ activities.json 格式正確"
    else
        echo "  ⚠️  activities.json 格式可能有問題"
        ((WARNINGS++))
    fi
else
    echo "  ⚠️  找不到 python3，跳過 JSON 格式檢查"
    ((WARNINGS++))
fi

echo ""

# ============ 資料夾檢查 ============
echo "📁 檢查重要資料夾..."

check_dir() {
    if [ -d "$1" ]; then
        count=$(find "$1" -type f 2>/dev/null | wc -l | tr -d ' ')
        echo "  ✅ $1/ ($count 個檔案)"
    else
        echo "  ⚠️  $1/ 不存在"
        ((WARNINGS++))
    fi
}

check_dir "images/faculty"
check_dir "images/news"
check_dir "images/activities"
check_dir "js"
check_dir "css"

echo ""

# ============ .gitignore 檢查 ============
echo "🚫 檢查 .gitignore 設定..."

if [ -f ".gitignore" ]; then
    echo "  ✅ .gitignore 存在"
    # build-templates.py, scripts/, templates/ must be committed for Netlify build (ignore comment lines)
    if grep -v '^[[:space:]]*#' .gitignore 2>/dev/null | grep -qE '^scripts/|^templates/|build-templates\.py'; then
        echo "  ⚠️  build-templates.py 或 scripts/ 不應在 .gitignore（Netlify 建置需要）"
        ((WARNINGS++))
    else
        echo "  ✅ 建置所需檔案可被提交"
    fi
else
    echo "  ⚠️  .gitignore 不存在"
    ((WARNINGS++))
fi

echo ""

# ============ Git 狀態檢查 ============
echo "📦 檢查 Git 狀態..."

if command -v git &> /dev/null; then
    if git rev-parse --git-dir > /dev/null 2>&1; then
        echo "  ✅ Git repository 已初始化"

        # 檢查 remote
        if git remote -v | grep -q "origin"; then
            remote_url=$(git remote get-url origin 2>/dev/null)
            echo "  ✅ Remote 已設定: $remote_url"
        else
            echo "  ⚠️  Remote 未設定"
            ((WARNINGS++))
        fi

        # 檢查分支
        current_branch=$(git branch --show-current 2>/dev/null)
        if [ "$current_branch" = "main" ] || [ "$current_branch" = "master" ]; then
            echo "  ✅ 目前分支: $current_branch"
        else
            echo "  ⚠️  目前分支: $current_branch（建議使用 main 或 master）"
            ((WARNINGS++))
        fi
    else
        echo "  ❌ Git repository 未初始化！"
        echo "     請執行: git init"
        ((ERRORS++))
    fi
else
    echo "  ❌ 找不到 git 指令！"
    ((ERRORS++))
fi

echo ""

# ============ 檔案大小檢查 ============
echo "📊 檢查檔案大小..."

# 檢查大檔案（> 10MB）
large_files=$(find . -type f -size +10M 2>/dev/null | grep -v "node_modules\|.git" | wc -l | tr -d ' ')
if [ "$large_files" -gt 0 ]; then
    echo "  ⚠️  發現 $large_files 個超過 10MB 的檔案："
    find . -type f -size +10M 2>/dev/null | grep -v "node_modules\|.git" | while read file; do
        size=$(ls -lh "$file" | awk '{print $5}')
        echo "     - $file ($size)"
    done
    ((WARNINGS++))
else
    echo "  ✅ 沒有超過 10MB 的大檔案"
fi

# 檢查資料夾總大小
data_size=$(du -sh data 2>/dev/null | awk '{print $1}')
images_size=$(du -sh images 2>/dev/null | awk '{print $1}')
echo "  📁 data/ 總大小: $data_size"
echo "  📁 images/ 總大小: $images_size"

echo ""

# ============ 總結 ============
echo "================================"
echo "📊 檢查完成！"
echo "================================"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "✅ 所有檢查通過！可以部署了！"
    echo ""
    echo "🚀 下一步："
    echo "   git add ."
    echo "   git commit -m \"準備部署\""
    echo "   git push"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "⚠️  發現 $WARNINGS 個警告"
    echo "   建議修正後再部署，但不是必須"
    exit 0
else
    echo "❌ 發現 $ERRORS 個錯誤 和 $WARNINGS 個警告"
    echo "   請修正錯誤後再部署！"
    exit 1
fi
