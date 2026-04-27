from __future__ import annotations

from pathlib import Path
from typing import Iterable

from PIL import Image, ImageEnhance, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parent.parent
ORIGINALS_DIR = ROOT / "assets" / "newlondonbakery" / "originals"
ENHANCED_DIR = ROOT / "assets" / "newlondonbakery" / "enhanced"


def enhance_image(path: Path) -> tuple[Path, tuple[int, int], tuple[int, int]]:
    with Image.open(path) as img:
        original_size = img.size
        working = img.convert("RGB")

        # Light denoise + local contrast adjustments keep the size identical
        # while recovering some detail from soft/compressed source images.
        working = working.filter(ImageFilter.MedianFilter(size=3))
        working = ImageOps.autocontrast(working, cutoff=0.5)
        working = ImageEnhance.Contrast(working).enhance(1.08)
        working = ImageEnhance.Color(working).enhance(1.04)
        working = ImageEnhance.Sharpness(working).enhance(1.18)
        working = working.filter(
            ImageFilter.UnsharpMask(radius=1.5, percent=115, threshold=3)
        )

        target = ENHANCED_DIR / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        working.save(target, quality=95, optimize=True)
        return target, original_size, working.size


def iter_images() -> Iterable[Path]:
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.JPG", "*.JPEG", "*.PNG", "*.WEBP"):
        yield from ORIGINALS_DIR.glob(ext)


def main() -> None:
    print("Enhancing New London Bakery images...")
    for image_path in sorted(iter_images()):
        target, before, after = enhance_image(image_path)
        print(f"{image_path.name}: {before[0]}x{before[1]} -> {after[0]}x{after[1]} saved to {target}")


if __name__ == "__main__":
    main()
