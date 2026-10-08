#!/usr/bin/env python3
"""Rockland Streamer University art: Twitch team brand set and the OBS scene cards.
python3 build_art.py [storm|pink]   default storm: navy thunderclouds, light-blue lightning.
PIL only. On the Mac swap FONT_BOLD for Avenir Next Heavy before the final build."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pathlib, random, math, sys

THEME = sys.argv[1].lower() if len(sys.argv) > 1 and sys.argv[1].lower() in ("storm", "pink") else "storm"
OUT = pathlib.Path(__file__).parent / ("out" if THEME == "storm" else "out-pink"); OUT.mkdir(exist_ok=True)
WHITE = (255, 255, 255); SILVER = (200, 196, 204)
if THEME == "storm":
    BG = (7, 16, 36); NAVY = (11, 26, 51); CLOUD = [(14, 31, 61), (22, 45, 84), (31, 59, 104), (9, 20, 42)]
    ACCENT = (125, 212, 255); GLOW = (63, 169, 245); CORE = (230, 248, 255); FG = (236, 244, 255); DIM = (150, 178, 210)
    BAR = [(125, 212, 255), (63, 169, 245), (31, 59, 104)]
else:
    BG = (11, 11, 15); NAVY = BG; CLOUD = [(255, 45, 143)]; ACCENT = (255, 45, 143); GLOW = (255, 214, 232); CORE = WHITE; FG = WHITE; DIM = SILVER
    BAR = [(255,45,143),(255,138,0),(255,212,0),(46,204,113),(45,156,219),(142,68,173)]
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def font(size, bold=True): return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def clouds(img, seed, region=(0.0, 0.0, 1.0, 1.0), n=18, blur=40):
    """Navy cloud banks: layered soft ellipses, darker on top, lighter toward the horizon."""
    rnd = random.Random(seed); w, h = img.size
    x0, y0, x1, y1 = int(region[0]*w), int(region[1]*h), int(region[2]*w), int(region[3]*h)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    for i in range(n):
        rw = rnd.randint(w//6, w//2); rh = rnd.randint(h//8, h//3)
        x = rnd.randint(x0 - rw//2, x1 - rw//2); y = rnd.randint(y0 - rh//2, y1 - rh//2)
        c = CLOUD[min(len(CLOUD)-1, int((y - y0) / max(1, (y1 - y0)) * len(CLOUD)))]
        d.ellipse((x, y, x + rw, y + rh), fill=c + (rnd.randint(150, 230),))
    layer = layer.filter(ImageFilter.GaussianBlur(blur)); img.alpha_composite(layer)

def bolt_points(rnd, x, y0, y1, spread, steps):
    pts = [(x, y0)]
    for i in range(1, steps + 1):
        t = i / steps; pts.append((x + rnd.randint(-spread, spread) * (1 - 0.3*t), int(y0 + (y1 - y0) * t)))
    return pts

def lightning(img, seed, x_frac, y0_frac=0.0, y1_frac=0.95, width=None, branches=3, core=None, glow=None, flash=True):
    """One light-blue bolt with a glow and two to three branches. Never touches the left text column."""
    rnd = random.Random(seed); w, h = img.size; width = width or max(3, h // 220); core = core or CORE; glow = glow or GLOW
    x = int(w * x_frac); main = bolt_points(rnd, x, int(h*y0_frac), int(h*y1_frac), w//25, 14)
    lines = [main]
    for b in range(branches):
        i = rnd.randint(3, len(main) - 4); sx, sy = main[i]
        lines.append(bolt_points(rnd, sx, sy, sy + rnd.randint(h//8, h//4), w//30, 5))
        # branches drift sideways
        drift = rnd.choice((-1, 1)) * max(8, min(w, h)//40)
        lines[-1] = [(px + int(k * drift), py) for k, (px, py) in enumerate(lines[-1])]
    for radius, color, wmul in ((width*6, glow + (90,), 4), (width*3, glow + (160,), 2.2), (0, core + (255,), 1)):
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
        for k, ln in enumerate(lines): d.line(ln, fill=color, width=max(1, int(width * wmul * (1 if k == 0 else 0.6))), joint="curve")
        if radius: layer = layer.filter(ImageFilter.GaussianBlur(radius))
        img.alpha_composite(layer)
    if flash:  # sky flash around the bolt's origin
        fl = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(fl).ellipse((x - w//4, -h//3, x + w//4, h//3), fill=glow + (70,))
        img.alpha_composite(fl.filter(ImageFilter.GaussianBlur(h//6)))

def bar(img, y, hgt):
    d = ImageDraw.Draw(img); w = img.size[0]
    if THEME == "storm":
        for i in range(w):
            t = i / w; c = tuple(int(BAR[0][k] * (1 - t) + BAR[1][k] * t) for k in range(3)); d.line((i, y, i, y + hgt), fill=c)
    else:
        seg = w / len(BAR)
        for i, c in enumerate(BAR): d.rectangle((int(i*seg), y, int((i+1)*seg), y+hgt), fill=c)

def backdrop(w, h, seed):
    img = Image.new("RGBA", (w, h), BG + (255,))
    if THEME == "storm":
        clouds(img, seed, region=(0.0, -0.1, 1.0, 0.6), n=16, blur=h//18)
        clouds(img, seed + 1, region=(0.3, 0.3, 1.1, 1.1), n=10, blur=h//12)
        lightning(img, seed + 2, x_frac=0.78, branches=3)
        lightning(img, seed + 3, x_frac=0.62, y0_frac=0.0, y1_frac=0.55, width=max(2, h//400), branches=1)
    else:
        from_pink(img, seed)
    bar(img, 0, max(4, h//120)); return img

def from_pink(img, seed):
    rnd = random.Random(seed); w, h = img.size; d = ImageDraw.Draw(img)
    for _ in range(8):
        r = rnd.randint(h//10, h//4); x = rnd.randint(int(w*0.6), w); y = rnd.randint(0, h); d.ellipse((x-r, y-r, x+r, y+r), fill=ACCENT + (255,))

def card(w, h, title, sub, small=None, seed=1):
    img = backdrop(w, h, seed); d = ImageDraw.Draw(img); pad = w // 16
    d.text((pad, h*0.22), "ROCKLAND", font=font(h//7), fill=ACCENT)
    d.text((pad, h*0.22 + h//7 * 0.95), "STREAMER U", font=font(h//7), fill=FG)
    d.text((pad, h*0.22 + h//7 * 2.0), title, font=font(h//11), fill=FG)
    if sub: d.text((pad, h*0.22 + h//7 * 2.0 + h//11 * 1.4), sub, font=font(h//22, False), fill=DIM)
    if small: d.text((pad, h - pad - h//30), small, font=font(h//30, False), fill=DIM)
    return img.convert("RGB")

def profile():
    s = 800; img = Image.new("RGBA", (s, s), BG + (255,))
    if THEME == "storm":
        clouds(img, 11, region=(-0.2, -0.2, 1.2, 0.7), n=14, blur=50); lightning(img, 12, x_frac=0.5, y0_frac=0.0, y1_frac=1.0, width=5, branches=3)
    d = ImageDraw.Draw(img); d.ellipse((150, 150, s-150, s-150), fill=NAVY + (235,), outline=ACCENT + (255,), width=10)
    d.text((s/2, s/2 - 70), "RSU", font=font(150), fill=FG, anchor="mm")
    d.text((s/2, s/2 + 70), "ROCKLAND", font=font(50), fill=ACCENT, anchor="mm")
    d.text((s/2, s/2 + 125), "STREAMER U", font=font(50), fill=FG, anchor="mm")
    return img.convert("RGB")

def main():
    profile().save(OUT / "profile-800.png")
    card(1200, 480, "Six weeks. Twelve lessons.", "Berbice, Guyana · a Little Rock school", "lrtvs.gy/university", seed=3).save(OUT / "banner-1200x480.png")
    card(1920, 1080, "Offline. Next class Saturday 10:00", "Guyana time, live from the Pink Room on Channel 10 live", "lrtvs.gy/university", seed=4).save(OUT / "offline-1920x1080.png")
    card(1920, 1080, "Class starts soon", "88.5 Rock FM on the speakers while we wait", "lrtvs.gy/university", seed=5).save(OUT / "scene-starting-soon-1920x1080.png")
    card(1920, 1080, "Be right back", "Stretch. Drink water. Two minutes.", "lrtvs.gy/university", seed=6).save(OUT / "scene-brb-1920x1080.png")
    card(1920, 1080, "That was class", "Homework is in the group. Same time Saturday.", "lrtvs.gy/university", seed=8).save(OUT / "scene-ending-1920x1080.png")
    bug = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(bug)
    d.rounded_rectangle((40, 960, 640, 1040), 18, fill=NAVY + (215,)); d.rectangle((40, 960, 52, 1040), fill=ACCENT + (255,))
    d.text((72, 1000), "ROCKLAND STREAMER U · LIVE CLASS", font=font(30), fill=FG, anchor="lm")
    bug.save(OUT / "scene-class-namebug-1920x1080.png")
    for p in sorted(OUT.glob("*.png")):
        im = Image.open(p); im.load(); print(f"{p.name:42s} {im.size[0]}x{im.size[1]} {p.stat().st_size//1024} KB")

if __name__ == "__main__": main()
