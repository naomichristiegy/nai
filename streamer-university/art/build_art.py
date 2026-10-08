#!/usr/bin/env python3
"""Rockland Streamer University art: Twitch team brand set and the five OBS scene cards.
python3 build_art.py   (PIL only). On the Mac swap FONT_BOLD for Avenir Next Heavy before the final build."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pathlib, random

OUT = pathlib.Path(__file__).parent / "out"; OUT.mkdir(exist_ok=True)
PINK = (255, 45, 143); BLUSH = (255, 214, 232); BLACK = (11, 11, 15); WHITE = (255, 255, 255); SILVER = (200, 196, 204)
RAINBOW = [(255,45,143),(255,138,0),(255,212,0),(46,204,113),(45,156,219),(142,68,173)]
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def font(size, bold=True): return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def splats(img, seed, n, rmin, rmax, color, alpha=255, region=(0.55, 0.0, 1.0, 1.0)):
    """Pink paint drops: soft circles, never gore. region = fractions of the image (x0, y0, x1, y1) the drops stay inside."""
    rnd = random.Random(seed); w, h = img.size
    x0, y0, x1, y1 = int(region[0]*w), int(region[1]*h), int(region[2]*w), int(region[3]*h)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    for _ in range(n):
        r = rnd.randint(rmin, rmax); x = rnd.randint(x0 + r, max(x0 + r + 1, x1 - r)); y = rnd.randint(y0 + r, max(y0 + r + 1, y1 - r))
        d.ellipse((x-r, y-r, x+r, y+r), fill=color + (alpha,))
        for _ in range(rnd.randint(2, 5)):
            rr = rnd.randint(max(4, r//8), max(6, r//3)); ang = rnd.random()*6.283
            import math; dx = int(math.cos(ang)*(r+rr)); dy = int(math.sin(ang)*(r+rr))
            d.ellipse((x+dx-rr, y+dy-rr, x+dx+rr, y+dy+rr), fill=color + (alpha,))
    img.alpha_composite(layer)

def rainbow_bar(img, y, h):
    d = ImageDraw.Draw(img); w = img.size[0]; seg = w / len(RAINBOW)
    for i, c in enumerate(RAINBOW): d.rectangle((int(i*seg), y, int((i+1)*seg), y+h), fill=c)

def card(w, h, title, sub, small=None, bg=BLACK, fg=WHITE, seed=1):
    img = Image.new("RGBA", (w, h), bg + (255,))
    splats(img, seed, 6, h//10, h//4, PINK, 255)
    splats(img, seed+7, 10, h//40, h//12, BLUSH, 230)
    img = img.filter(ImageFilter.GaussianBlur(0.6))
    rainbow_bar(img, 0, max(4, h//120))
    d = ImageDraw.Draw(img)
    pad = w // 16
    d.text((pad, h*0.22), "ROCKLAND", font=font(h//7), fill=PINK)
    d.text((pad, h*0.22 + h//7 * 0.95), "STREAMER U", font=font(h//7), fill=fg)
    d.text((pad, h*0.22 + h//7 * 2.0), title, font=font(h//11), fill=fg)
    if sub: d.text((pad, h*0.22 + h//7 * 2.0 + h//11 * 1.4), sub, font=font(h//22, False), fill=SILVER)
    if small: d.text((pad, h - pad - h//30), small, font=font(h//30, False), fill=SILVER)
    return img.convert("RGB")

def profile():
    s = 800; img = Image.new("RGBA", (s, s), BLACK + (255,))
    d = ImageDraw.Draw(img); d.ellipse((40, 40, s-40, s-40), fill=PINK + (255,))
    d.ellipse((120, 120, s-120, s-120), fill=BLACK + (255,))
    f = font(150); d.text((s/2, s/2 - 90), "RSU", font=f, fill=WHITE, anchor="mm")
    d.text((s/2, s/2 + 60), "ROCKLAND", font=font(54), fill=PINK, anchor="mm")
    d.text((s/2, s/2 + 120), "STREAMER U", font=font(54), fill=WHITE, anchor="mm")
    rainbow_bar(img, s/2 + 175, 10)
    return img.convert("RGB")

def main():
    profile().save(OUT / "profile-800.png")
    card(1200, 480, "Six weeks. Twelve lessons.", "Berbice, Guyana · a Little Rock school", "lrtvs.gy/university", seed=3).save(OUT / "banner-1200x480.png")
    card(1920, 1080, "Offline. Next class Saturday 10:00", "Guyana time, live from the Pink Room on Channel 10 live", "lrtvs.gy/university", seed=4).save(OUT / "offline-1920x1080.png")
    card(1920, 1080, "Class starts soon", "88.5 Rock FM on the speakers while we wait", "lrtvs.gy/university", seed=5).save(OUT / "scene-starting-soon-1920x1080.png")
    card(1920, 1080, "Be right back", "Stretch. Drink water. Two minutes.", "lrtvs.gy/university", seed=6).save(OUT / "scene-brb-1920x1080.png")
    card(1920, 1080, "That was class", "Homework is in the group. Same time Saturday.", "lrtvs.gy/university", seed=8).save(OUT / "scene-ending-1920x1080.png")
    # Name bug: transparent 1920x1080, bottom-left, for the Class scene.
    bug = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(bug)
    d.rounded_rectangle((40, 960, 640, 1040), 18, fill=BLACK + (210,)); d.rectangle((40, 960, 52, 1040), fill=PINK + (255,))
    d.text((72, 1000), "ROCKLAND STREAMER U · LIVE CLASS", font=font(30), fill=WHITE, anchor="lm")
    bug.save(OUT / "scene-class-namebug-1920x1080.png")
    for p in sorted(OUT.glob("*.png")):
        im = Image.open(p); im.load(); print(f"{p.name:42s} {im.size[0]}x{im.size[1]} {p.stat().st_size//1024} KB")

if __name__ == "__main__": main()
