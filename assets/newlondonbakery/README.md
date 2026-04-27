# New London Bakery Image Enhancement

Source images were downloaded from the public `newlondonbakery.com` product page and enhanced locally without changing pixel dimensions.

## Outputs
- Originals: `assets/newlondonbakery/originals/`
- Enhanced: `assets/newlondonbakery/enhanced/`

## Processed files
- `dinner-rolls.jpeg` -> `600x800`
- `grinders-rack-side-golden.jpg` -> `1080x1440`
- `hoagies-2-size-toasty.jpg` -> `1080x1440`
- `hoagies-light.jpg` -> `1080x1440`
- `marble-bread.jpg` -> `600x600`
- `part0.jpg` -> `768x1024`
- `part0_1-1.jpg` -> `600x800`
- `rye-pumpernickel.jpg` -> `600x400`
- `sliced-bread.jpg` -> `970x746`
- `variety-of-breads-3.jpeg` -> `2404x2356`

## Enhancement pass
- light denoise
- auto contrast correction
- mild contrast and color lift
- sharpen + unsharp mask

This pass is intended to improve softness and compression artifacts while keeping layout-safe dimensions unchanged.
