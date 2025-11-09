#!/bin/bash
# Identify unused JavaScript files

ACTIVE_JS=(
    "activities.js"
    "article-view.js"
    "article.js"
    "combined-news.js"
    "homepage.js"
    "faculty.js"
    "fulltime-faculty-detail.js"
    "fulltime-faculty-profile.js"
    "honorary-faculty-detail.js"
    "joint-faculty-detail.js"
    "parttime-faculty-detail.js"
    "practical-faculty-detail.js"
    "csv-parser.js"
)

echo "===== Identifying Unused JS Files ====="
echo ""

for file in js/*.js; do
    filename=$(basename "$file")

    # Check if file is in active list
    is_active=false
    for active in "${ACTIVE_JS[@]}"; do
        if [[ "$filename" == "$active" ]]; then
            is_active=true
            break
        fi
    done

    if [[ "$is_active" == false ]]; then
        echo "❌ UNUSED: $filename"
        # Move to archive
        mv "$file" "archive/legacy-js/"
    else
        echo "✅ ACTIVE: $filename"
    fi
done

echo ""
echo "===== Summary ====="
echo "Active JS files: ${#ACTIVE_JS[@]}"
echo "Moved to archive/legacy-js/"
