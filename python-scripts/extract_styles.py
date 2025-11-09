#!/usr/bin/env python3
"""
提取原始網站的主要顏色和樣式
"""

import re
from pathlib import Path

def extract_colors_from_css(css_file):
    """從CSS文件中提取所有顏色"""
    try:
        with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 提取hex顏色
        hex_colors = re.findall(r'#[0-9a-fA-F]{3,6}', content)

        # 提取rgb顏色
        rgb_colors = re.findall(r'rgb\([^)]+\)', content)

        # 去重並統計
        hex_unique = {}
        for color in hex_colors:
            hex_unique[color.lower()] = hex_unique.get(color.lower(), 0) + 1

        # 按出現次數排序
        sorted_colors = sorted(hex_unique.items(), key=lambda x: x[1], reverse=True)

        print(f"\n=== {css_file.name} ===")
        print(f"找到 {len(hex_unique)} 種顏色")
        print("\n最常用的20種顏色:")
        for color, count in sorted_colors[:20]:
            print(f"  {color}: {count}次")

        return sorted_colors

    except Exception as e:
        print(f"錯誤: {e}")
        return []

def main():
    base_dir = Path(__file__).parent
    css_dir = base_dir / 'css'

    # 分析主要CSS文件
    css_files = ['page.css', 'global.css']

    all_colors = {}
    for css_file in css_files:
        css_path = css_dir / css_file
        if css_path.exists():
            colors = extract_colors_from_css(css_path)
            for color, count in colors:
                all_colors[color] = all_colors.get(color, 0) + count

    print("\n\n=== 整體最常用的顏色 ===")
    sorted_all = sorted(all_colors.items(), key=lambda x: x[1], reverse=True)
    for color, count in sorted_all[:30]:
        print(f"  {color}: {count}次")

if __name__ == '__main__':
    main()
