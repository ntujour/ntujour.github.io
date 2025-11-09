#!/usr/bin/env python3
"""
Image Optimization Script
Compresses images and converts to WebP format for better performance
Requires: pillow library (pip install pillow)
"""

import os
import sys
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent.parent
IMAGES_DIR = BASE_DIR / 'images'

def optimize_image(image_path, quality=85):
    """
    Optimize a single image
    - Compress JPEG/PNG
    - Optionally create WebP version
    """
    try:
        with Image.open(image_path) as img:
            # Get original size
            original_size = os.path.getsize(image_path)

            # Convert RGBA to RGB if needed
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background

            # Save optimized version
            if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                img.save(image_path, 'JPEG', quality=quality, optimize=True)
            elif image_path.suffix.lower() == '.png':
                img.save(image_path, 'PNG', optimize=True)

            # Create WebP version
            webp_path = image_path.with_suffix('.webp')
            img.save(webp_path, 'WEBP', quality=quality)

            # Get new sizes
            new_size = os.path.getsize(image_path)
            webp_size = os.path.getsize(webp_path)

            saved = original_size - new_size
            webp_saved = original_size - webp_size

            print(f"✓ {image_path.name}")
            print(f"  Original: {original_size/1024:.1f}KB")
            print(f"  Optimized: {new_size/1024:.1f}KB (saved {saved/1024:.1f}KB)")
            print(f"  WebP: {webp_size/1024:.1f}KB (saved {webp_saved/1024:.1f}KB)")

            return saved, webp_saved

    except Exception as e:
        print(f"✗ Error processing {image_path.name}: {e}")
        return 0, 0

def main():
    print("=" * 70)
    print("Image Optimization Script")
    print("=" * 70)
    print()

    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        print("❌ Error: Pillow library not found!")
        print("Install it with: pip install pillow")
        sys.exit(1)

    # Find all images
    image_extensions = ['.jpg', '.jpeg', '.png']
    image_files = []

    for ext in image_extensions:
        image_files.extend(IMAGES_DIR.glob(f'**/*{ext}'))
        image_files.extend(IMAGES_DIR.glob(f'**/*{ext.upper()}'))

    # Exclude already processed WebP files
    image_files = [f for f in image_files if f.suffix.lower() != '.webp']

    print(f"Found {len(image_files)} images to optimize\n")

    if not image_files:
        print("No images found to optimize")
        return

    response = input("Proceed with optimization? (y/N): ")
    if response.lower() != 'y':
        print("Cancelled")
        return

    print()
    print("-" * 70)

    total_saved = 0
    total_webp_saved = 0

    for image_file in image_files:
        saved, webp_saved = optimize_image(image_file, quality=85)
        total_saved += saved
        total_webp_saved += webp_saved
        print()

    print("-" * 70)
    print(f"\n📊 Summary:")
    print(f"  Images processed: {len(image_files)}")
    print(f"  Total space saved (optimized): {total_saved/1024/1024:.2f}MB")
    print(f"  Total space saved (WebP): {total_webp_saved/1024/1024:.2f}MB")
    print(f"  WebP files created: {len(image_files)}")
    print()
    print("💡 Tip: Update HTML to use WebP images with <picture> tags for better performance")
    print("=" * 70)

if __name__ == '__main__':
    main()
