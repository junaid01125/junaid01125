"""
Builds card.svg (animated player card) with your picture embedded.

Usage:
    1. Put your picture next to this script, named avatar.png (or avatar.jpg)
    2. python build_card.py
    3. Upload the generated card.svg to your junaid01125 repo

The picture must be embedded (base64) because GitHub blocks SVGs from
loading outside files. This script does that for you.
"""
import base64
import mimetypes
import os
import sys

# ---------- edit these ----------
NAME = "JUNAID"
POSITION = "ST"
COUNTRY = "IND"
TAGLINE = "BUILDER"
FOOTER = "B.TECH STUDENT"
STATS = [
    ("CREATIVITY", 92),
    ("IDEAS", 94),
    ("BUILDING", 88),
    ("PROBLEM SOLVING", 86),
    ("ADAPTABILITY", 93),
    ("TEAMWORK", 91),
]
# --------------------------------

# Overall = average of all stats
RATING = str(round(sum(v for _, v in STATS) / len(STATS)))

here = os.path.dirname(os.path.abspath(__file__))
img_path = None
for cand in ("avatar.png", "avatar.jpg", "avatar.jpeg", "avatar.webp"):
    p = os.path.join(here, cand)
    if os.path.exists(p):
        img_path = p
        break
if not img_path:
    sys.exit("Put your picture here as avatar.png / avatar.jpg first.")

mime = mimetypes.guess_type(img_path)[0] or "image/png"
with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

# Stats: one column, full names
stat_svg = []
for i, (label, val) in enumerate(STATS):
    x, w = 62, 296
    y = 398 + i * 24
    delay = 2.0 + i * 0.18
    stat_svg.append(f"""
  <g class="reveal" style="animation-delay:{delay:.2f}s">
    <text x="{x}" y="{y}" class="slabel">{label}</text>
    <text x="{x + w}" y="{y}" class="sval" text-anchor="end">{val}</text>
    <rect x="{x}" y="{y + 6}" width="{w}" height="3" rx="1.5" fill="#ffffff" opacity="0.12"/>
    <rect x="{x}" y="{y + 6}" width="{val * w / 100:.1f}" height="3" rx="1.5" fill="url(#gold)"
          class="bar" style="animation-delay:{delay + 0.15:.2f}s"/>
  </g>""")

svg = """<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="420" height="600" viewBox="0 0 420 600" role="img" aria-label="__NAME__ player card">
  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f6e7a8"/>
      <stop offset="0.5" stop-color="#d4a73a"/>
      <stop offset="1" stop-color="#8a6a1c"/>
    </linearGradient>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2a2a33"/>
      <stop offset="0.5" stop-color="#15151b"/>
      <stop offset="1" stop-color="#0a0a0e"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.35" r="0.6">
      <stop offset="0" stop-color="#d4a73a" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#d4a73a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="shineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.22"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="cardClip">
      <path id="cardShape" d="M60 10 H360 L410 60 V540 L360 590 H60 L10 540 V60 Z"/>
    </clipPath>
    <clipPath id="avatarClip">
      <rect x="150" y="62" width="214" height="214" rx="18"/>
    </clipPath>
  </defs>

  <style>
    text { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; }
    .rating { font-size: 64px; font-weight: 800; fill: url(#gold); }
    .pos    { font-size: 22px; font-weight: 700; fill: #f3e3a0; letter-spacing: 2px; }
    .small  { font-size: 12px; font-weight: 700; fill: #d4a73a; letter-spacing: 3px; }
    .name   { font-size: 36px; font-weight: 800; fill: #ffffff; letter-spacing: 6px; }
    .tag    { font-size: 12px; font-weight: 600; fill: #d4a73a; letter-spacing: 5px; }
    .slabel { font-size: 13px; font-weight: 600; fill: #cfcfd6; letter-spacing: 1.5px; }
    .sval   { font-size: 16px; font-weight: 800; fill: #f3e3a0; }
    .foot   { font-size: 11px; font-weight: 600; fill: #8d8d98; letter-spacing: 4px; }

    .spin   { transform-box: view-box; transform-origin: 210px 300px;
              animation: spin 1.3s cubic-bezier(.2,.8,.2,1) both; }
    @keyframes spin {
      0%   { transform: scaleX(0) rotate(-6deg); opacity: 0; }
      30%  { opacity: 1; }
      70%  { transform: scaleX(1.05) rotate(1deg); }
      100% { transform: scaleX(1) rotate(0); opacity: 1; }
    }

    .float  { animation: float 5s ease-in-out infinite; }
    @keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }

    .pop    { opacity: 0; animation: pop 0.8s ease-out 1.0s forwards; }
    @keyframes pop { from { opacity:0; transform: translateY(8px); } to { opacity:1; transform: translateY(0); } }

    .reveal { opacity: 0; animation: reveal 0.6s ease-out forwards; }
    @keyframes reveal { from { opacity:0; transform: translateX(-8px); } to { opacity:1; transform: translateX(0); } }

    .bar    { transform-box: fill-box; transform-origin: left center; transform: scaleX(0);
              animation: grow 0.9s ease-out forwards; }
    @keyframes grow { to { transform: scaleX(1); } }

    .shine  { animation: shine 6s ease-in-out 3s infinite; }
    @keyframes shine { 0% { transform: translateX(-260px) skewX(-20deg); }
                       40%,100% { transform: translateX(520px) skewX(-20deg); } }

    .pulse  { animation: pulse 4s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { opacity: 0.55; } 50% { opacity: 1; } }
  </style>

  <g class="spin">
  <!-- card body -->
  <use href="#cardShape" fill="url(#bg)"/>
  <rect x="10" y="10" width="400" height="580" fill="url(#glow)" clip-path="url(#cardClip)" class="pulse"/>
  <use href="#cardShape" fill="none" stroke="url(#gold)" stroke-width="4"/>
  <path d="M66 20 H354 L400 62 V538 L354 580 H66 L20 538 V62 Z" fill="none"
        stroke="#d4a73a" stroke-opacity="0.35" stroke-width="1"/>

  <!-- rating / position / country -->
  <g class="pop">
    <text x="42" y="112" class="rating">__RATING__</text>
    <text x="46" y="146" class="pos">__POS__</text>
    <line x1="46" y1="160" x2="106" y2="160" stroke="#d4a73a" stroke-opacity="0.5"/>
    <text x="46" y="182" class="small">__COUNTRY__</text>
  </g>

  <!-- player picture -->
  <g class="float">
    <rect x="146" y="58" width="222" height="222" rx="21" fill="none" stroke="url(#gold)" stroke-width="2"/>
    <image x="150" y="62" width="214" height="214" preserveAspectRatio="xMidYMid slice"
           clip-path="url(#avatarClip)" href="data:__MIME__;base64,__B64__"/>
  </g>

  <!-- name -->
  <g class="pop" style="animation-delay:1.4s">
    <text x="210" y="332" class="name" text-anchor="middle">__NAME__</text>
    <text x="210" y="356" class="tag" text-anchor="middle">__TAGLINE__</text>
    <line x1="50" y1="374" x2="370" y2="374" stroke="url(#gold)" stroke-opacity="0.7"/>
  </g>

  <!-- stats -->
  __STATS__

  <!-- footer -->
  <text x="210" y="562" class="foot" text-anchor="middle">__FOOTER__</text>

  <!-- shine sweep -->
  <g clip-path="url(#cardClip)">
    <rect class="shine" x="0" y="0" width="90" height="600" fill="url(#shineGrad)"/>
  </g>
  </g>
</svg>
"""

svg = (svg.replace("__NAME__", NAME)
          .replace("__RATING__", RATING)
          .replace("__POS__", POSITION)
          .replace("__COUNTRY__", COUNTRY)
          .replace("__TAGLINE__", TAGLINE)
          .replace("__FOOTER__", FOOTER)
          .replace("__STATS__", "".join(stat_svg))
          .replace("__MIME__", mime)
          .replace("__B64__", b64))

out = os.path.normpath(os.path.join(here, "..", "card.svg"))
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"Done -> {out} ({len(svg)//1024} KB)")
