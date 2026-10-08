#!/usr/bin/env python3
"""Numbered graduation certificate, PNG and PDF. Storm look: navy clouds along the top, one light-blue bolt at the right.
python3 certificate.py --name "Full Name" --track Gamers --number 1 --date "19 December 2026" [--handle name] [--signer "Naomi Christie"]"""
from PIL import Image, ImageDraw
import argparse, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_art as A

def make(name, track, number, date, handle=None, out=None, signer="Naomi Christie"):
    w, h = 2480, 1754  # A4 landscape at 300 dpi
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    sky = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    A.clouds(sky, 40 + number, region=(0.55, -0.35, 1.05, 0.12), n=12, blur=70)
    img.alpha_composite(sky)
    A.lightning(img, 90 + number, x_frac=0.86, y0_frac=0.0, y1_frac=0.5, width=6, branches=2, core=(125, 212, 255), glow=(31, 110, 190), flash=False)
    A.bar(img, 0, 16); d = ImageDraw.Draw(img); pad = 180; ink = (10, 18, 40); accent = (31, 110, 190); dim = (120, 136, 160)
    d.text((pad, 150), "ROCKLAND STREAMER UNIVERSITY", font=A.font(64), fill=accent)
    d.text((pad, 240), "A Little Rock school · Berbice, Guyana", font=A.font(36, False), fill=dim)
    d.text((pad, 460), "Certificate of graduation", font=A.font(72), fill=ink)
    d.text((pad, 600), "awarded to", font=A.font(40, False), fill=ink)
    d.text((pad, 680), name, font=A.font(120), fill=ink)
    d.text((pad, 860), f"who completed the twelve lessons of Cohort 1 in the {track} track", font=A.font(40, False), fill=ink)
    d.text((pad, 920), "and streamed a one-hour graduation show on the Little Rock network.", font=A.font(40, False), fill=ink)
    if handle: d.text((pad, 1000), f"Streams as {handle}", font=A.font(40), fill=accent)
    d.text((pad, 1300), f"Certificate no. {number:03d}", font=A.font(40), fill=ink)
    d.text((pad, 1360), date, font=A.font(40, False), fill=ink)
    d.line((w - pad - 700, 1380, w - pad, 1380), fill=ink, width=3)
    d.text((w - pad - 700, 1400), signer, font=A.font(32, False), fill=ink)
    d.text((w - pad - 700, 1450), "for Little Rock", font=A.font(32, False), fill=dim)
    rgb = img.convert("RGB"); out = pathlib.Path(out or f"certificate-{number:03d}.png")
    rgb.save(out); rgb.save(out.with_suffix(".pdf"), "PDF", resolution=300)
    return out

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("--name", required=True); a.add_argument("--track", required=True)
    a.add_argument("--number", type=int, required=True); a.add_argument("--date", required=True); a.add_argument("--handle"); a.add_argument("--out"); a.add_argument("--signer", default="Naomi Christie")
    p = make(**vars(a.parse_args())); print(p, p.with_suffix(".pdf"))
