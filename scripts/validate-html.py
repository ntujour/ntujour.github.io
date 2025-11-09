#!/usr/bin/env python3
"""
HTML Validation and Link Checker
Validates HTML structure and checks for broken links
"""

import re
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parent.parent

def check_html_file(file_path):
    """Basic HTML validation checks"""
    issues = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for template placeholders that weren't replaced
        placeholders = re.findall(r'\{\{[^}]+\}\}', content)
        if placeholders:
            issues.append(f"Unreplaced template placeholders: {placeholders}")

        # Check for proper DOCTYPE
        if not content.strip().startswith('<!DOCTYPE html>'):
            issues.append("Missing or incorrect DOCTYPE")

        # Check for required meta tags
        if '<meta charset=' not in content:
            issues.append("Missing charset meta tag")

        if '<meta name="viewport"' not in content:
            issues.append("Missing viewport meta tag")

        # Check for proper lang attribute
        if '<html lang=' not in content:
            issues.append("Missing lang attribute on <html>")

        # Check for title tag
        if '<title>' not in content or '</title>' not in content:
            issues.append("Missing title tag")

        # Check for unclosed tags (basic check)
        open_tags = len(re.findall(r'<(div|section|article|nav|header|footer|main|ul|ol)[^>]*>', content))
        close_tags = len(re.findall(r'</(div|section|article|nav|header|footer|main|ul|ol)>', content))

        if open_tags != close_tags:
            issues.append(f"Possible unclosed tags: {open_tags} opening vs {close_tags} closing")

        # Check for inline styles (should use CSS)
        inline_styles = re.findall(r'style="[^"]*"', content)
        if len(inline_styles) > 2:  # Allow a couple
            issues.append(f"Too many inline styles: {len(inline_styles)} found")

        # Check for accessibility
        if '<img ' in content:
            imgs_without_alt = len(re.findall(r'<img(?![^>]*alt=)[^>]*>', content))
            if imgs_without_alt > 0:
                issues.append(f"Images without alt text: {imgs_without_alt}")

    except Exception as e:
        issues.append(f"Error reading file: {e}")

    return issues

def check_internal_links(file_path):
    """Check for broken internal links"""
    issues = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all internal links (href="..." that don't start with http)
        links = re.findall(r'href="([^"]*)"', content)
        internal_links = [l for l in links if not l.startswith(('http://', 'https://', 'mailto:', '#', 'tel:'))]

        for link in internal_links:
            # Calculate absolute path
            if link.startswith('../'):
                # Parent directory
                link_path = (file_path.parent.parent / link.replace('../', '')).resolve()
            elif link.startswith('./'):
                # Current directory
                link_path = (file_path.parent / link.replace('./', '')).resolve()
            else:
                # Relative to file
                link_path = (file_path.parent / link).resolve()

            if not link_path.exists():
                issues.append(f"Broken link: {link} (resolved to {link_path})")

    except Exception as e:
        issues.append(f"Error checking links: {e}")

    return issues

def main():
    print("=" * 70)
    print("HTML Validation and Link Checker")
    print("=" * 70)
    print()

    # Find all HTML files
    html_files = list(BASE_DIR.glob('**/*.html'))

    # Exclude archive and node_modules
    html_files = [f for f in html_files
                  if 'archive' not in str(f)
                  and 'node_modules' not in str(f)
                  and 'templates' not in str(f)]

    print(f"Checking {len(html_files)} HTML files...\n")

    results = defaultdict(list)

    for html_file in html_files:
        relative_path = html_file.relative_to(BASE_DIR)

        # HTML validation
        html_issues = check_html_file(html_file)

        # Link checking
        link_issues = check_internal_links(html_file)

        if html_issues or link_issues:
            results[str(relative_path)] = {
                'html': html_issues,
                'links': link_issues
            }

    # Print results
    if not results:
        print("✅ All checks passed! No issues found.")
    else:
        print(f"⚠️  Found issues in {len(results)} files:\n")
        print("-" * 70)

        for file_path, issues in results.items():
            print(f"\n📄 {file_path}")

            if issues['html']:
                print("  HTML Issues:")
                for issue in issues['html']:
                    print(f"    • {issue}")

            if issues['links']:
                print("  Link Issues:")
                for issue in issues['links']:
                    print(f"    • {issue}")

    print()
    print("=" * 70)
    print(f"Summary: Checked {len(html_files)} files, found issues in {len(results)}")
    print("=" * 70)

if __name__ == '__main__':
    main()
