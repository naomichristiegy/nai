#!/usr/bin/env python3
"""Numbered graduation certificate, PNG and PDF.
python3 certificate.py --name "Full Name" --track Gamers --number 1 --date "19 December 2026" [--handle name]"""
from PIL import Image, ImageDraw, ImageFont
import argparse, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from build_art import splats, rainbow_bar, font, PINK, BLACK, WHITE, SILVER, BLUSH

def make(name, track, number, date, handle=None, out=None, signer="Naomi Christie"):
    w, h = 2480, 1754  # A4 landscape at 300 dpi
    img = Image.new("RGBA", (w, h), WHITE + (255,))
    splats(img, 40 + number, 5, 60, 160, BLUSH, 255, region=(0.62, 0.02, 1.0, 0.42)); splats(img, 90 + number, 4, 20, 50, PINK, 255, region=(0.62, 0.02, 1.0, 0.42))
    rainbow_bar(img, 0, 16); d = ImageDraw.Draw(img); pad = 180
    d.text((pad, 150), "ROCKLAND STREAMER UNIVERSITY", font=font(64), fill=PINK)
    d.text((pad, 240), "A Little Rock school · Berbice, Guyana", font=font(36, False), fill=SILVER)
    d.text((pad, 460), "Certificate of graduation", font=font(72), fill=BLACK)
    d.text((pad, 600), "awarded to", font=font(40, False), fill=BLACK)
    d.text((pad, 680), name, font=font(120), fill=BLACK)
    line = f"who completed the twelve lessons of Cohort 1 in the {track} track"
    d.text((pad, 860), line, font=font(40, False), fill=BLACK)
    d.text((pad, 920), "and streamed a one-hour graduation show on the Little Rock network.", font=font(40, False), fill=BLACK)
    if handle: d.text((pad, 1000), f"Streams as {handle}", font=font(40), fill=PINK)
    d.text((pad, 1300), f"Certificate no. {number:03d}", font=font(40), fill=BLACK)
    d.text((pad, 1360), date, font=font(40, False), fill=BLACK)
    d.line((w - pad - 700, 1380, w - pad, 1380), fill=BLACK, width=3)
    d.text((w - pad - 700, 1400), signer, font=font(32, False), fill=BLACK)
    d.text((w - pad - 700, 1450), "for Little Rock", font=font(32, False), fill=SILVER)
    rgb = img.convert("RGB"); out = pathlib.Path(out or f"certificate-{number:03d}.png")
    rgb.save(out); rgb.save(out.with_suffix(".pdf"), "PDF", resolution=300)
    return out

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("--name", required=True); a.add_argument("--track", required=True)
    a.add_argument("--number", type=int, required=True); a.add_argument("--date", required=True); a.add_argument("--handle"); a.add_argument("--out"); a.add_argument("--signer", default="Naomi Christie")
    p = make(**vars(a.parse_args())); print(p, p.with_suffix(".pdf"))
