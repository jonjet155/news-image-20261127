#!/usr/bin/env python3
"""news-image-20261127 — Friday 27 November 2026: The World in One Day.
Code-drawn flat 2D vector front page, 1024x1024. Written fresh from the
competition brief only. No photo, no copied art. All news verified from
live wires (Reuters/AP/BBC/Al Jazeera/Xinhua/Kyodo/Straits Times/
MarketWatch/Barron's) for 27 Nov 2026.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

CREAM = (251, 243, 228)
PAPER = (255, 251, 240)
INK = (30, 27, 22)
MUTED = (90, 82, 70)
CORAL = (212, 61, 42)
MUSTARD = (214, 158, 44)
TEAL = (42, 122, 110)
NAVY = (38, 64, 110)
SKY = (168, 205, 222)
SEA = (126, 178, 205)
LAND = (168, 196, 130)
LAND2 = (146, 182, 112)
RULE = (30, 27, 22)
LIGHT = (238, 226, 205)
BAND = (243, 232, 210)

FD = "/usr/share/fonts/truetype/dejavu/"

def F(name, size):
    return ImageFont.truetype(FD + name, size)

SERIF_B = lambda s: F("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: F("DejaVuSerif.ttf", s)
SANS_B = lambda s: F("DejaVuSans-Bold.ttf", s)
SANS = lambda s: F("DejaVuSans.ttf", s)

# ---------------------------------------------------------------- data
# tag: C=CONFIRMED O=OFFICIALS R=REPORTED F=FORECAST
# Panels 1-13 (heroes 1-3). Headlines in caps by hand (no case transform).
PANELS = [
 dict(n=1, tag="C", region="Middle East", lon=56.3, lat=26.5, scene="tanker",
      head="TANKERS HIT MINES IN HORMUZ",
      deck="Two tankers explode after striking mines off Oman; a supertanker with 2M barrels is left burning."),
 dict(n=2, tag="R", region="Middle East", lon=35.2, lat=31.8, scene="jet",
      head="ISRAEL: READY TO STRIKE IRAN ALONE",
      deck="IDF says it can hit Iran without US help as Netanyahu calls a cabinet meeting."),
 dict(n=3, tag="C", region="North America", lon=-77.0, lat=38.9, scene="flags",
      head="TRUMP TO PUTIN: PULL BACK",
      deck="Trump says he urged Putin to end aggression in Europe and make a quick Ukraine deal."),
 dict(n=4, tag="C", region="Middle East", lon=48.0, lat=29.4, scene="drone",
      head="DRONE KILLS TWO IN KUWAIT",
      deck="Kuwait blames Iran; Tehran denies any role."),
 dict(n=5, tag="R", region="Middle East", lon=42.6, lat=16.9, scene="refinery",
      head="HOUTHIS HIT ARAMCO REFINERY",
      deck="Coalition warns of a strong reply after the Jazan strike."),
 dict(n=6, tag="C", region="Africa", lon=23.0, lat=-3.0, scene="ebola",
      head="EBOLA TOPS 12,000 CASES IN CONGO",
      deck="Nearly 6,000 dead; the outbreak has reached 8 of 26 provinces."),
 dict(n=7, tag="R", region="Asia", lon=140.1, lat=35.6, scene="datacentre",
      head="ANTHROPIC IN JAPAN DATA TALKS",
      deck="JERA in talks with Anthropic, Meta on Tokyo AI centres."),
 dict(n=8, tag="C", region="North America", lon=-74.0, lat=40.7, scene="storm",
      head="STORM CUTS POWER TO 800,000",
      deck="Thanksgiving storm floods the US East Coast and delays flights."),
 dict(n=9, tag="C", region="Europe", lon=-0.1, lat=51.5, scene="chart",
      head="BLACK FRIDAY: STOCKS RALLY",
      deck="World shares climb as Wall Street reopens for a half day."),
 dict(n=10, tag="C", region="Oceania", lon=174.8, lat=-41.3, scene="seats",
      head="NZ COALITION ONE SEAT SHORT",
      deck="Final count: Luxon 65 of 130; Opportunity holds the balance."),
 dict(n=11, tag="R", region="Asia", lon=139.7, lat=35.7, scene="jet",
      head="JAPAN EYES $350B DEFENCE PLAN",
      deck="Tokyo weighs 56.3 trillion yen over five years from 2027."),
 dict(n=12, tag="C", region="Asia", lon=107.6, lat=-6.9, scene="mine",
      head="13 MINERS DEAD IN JAVA FLOOD",
      deck="Thirteen more are missing in a flooded pit in West Java."),
 dict(n=13, tag="C", region="Middle East", lon=51.5, lat=25.4, scene="f1",
      head="F1 OPENS IN QATAR AMID FEUD",
      deck="Verstappen and Russell carry their Las Vegas row into Lusail."),
]

# ALSO ON: (tag, label, text) — label kept short, text one fact each.
ALSO = [
 ("C", "G20", "Trump: Putin \u201ccan come\u201d to Florida G20, 14\u201315 Dec"),
 ("C", "GDP", "Trump demands probe of \u201cfake\u201d GDP; Q3 revised to 4.3%"),
 ("C", "SERBIA", "Serbia sets early presidential vote for 27 Dec"),
 ("C", "TOKYO CPI", "Tokyo core inflation 2.9% in Nov, above target"),
 ("R", "SEKI", "Japan Senate to vote censure of minister Seki"),
 ("C", "OKINAWA", "Heavy rain, 70mm an hour, hits Okinawa"),
 ("C", "LNG", "Australia: LNG exporters must keep 20% at home"),
 ("C", "DIANA", "Diana Award charity goes into administration"),
 ("R", "WEDDING", "400,000 guests at Bihar lawmaker\u2019s wedding"),
 ("C", "OMAN", "Japan, Oman FMs agree Mideast cooperation"),
 ("C", "CHUBU", "Chubu Electric filed plan after faking quake data"),
 ("C", "PACIFIC", "Japan, Marshall Islands deepen Pacific ties"),
 ("R", "CHIPS", "US curbs remote access to AI chips for China firms"),
 ("R", "BRAZIL", "Brazil blasts \u201cunacceptable\u201d US tariff plans"),
 ("R", "KIM", "Kim orders wider deployment of tactical nuclear arms"),
 ("R", "TARIFFS", "New Trump tariffs \u201cnot as bad as feared\u201d"),
 ("R", "MILEI", "Milei accuses Brazil, Mexico of funding smears"),
 ("F", "SALES", "Holiday spending seen up 4-6% as Black Friday opens"),
 ("C", "IMAI", "Wife pleads for reporter Yuki Imai, held in Russia"),
 ("C", "RUTTE", "Trump hosts NATO chief Rutte in Florida"),
 ("R", "URANIUM", "Kim tours uranium site, vows more nuclear arms"),
 ("R", "WOLFF", "Wolff: no outside offers as he plans Mercedes future"),
]

BIG = [
 ("2M+", "barrels of crude on the burning supertanker"),
 ("12,000", "Ebola cases in DR Congo"),
 ("800,000", "without power on the US East Coast"),
 ("$12.9B", "forecast Black Friday online sales"),
 ("400,000", "guests at the Bihar wedding"),
 ("$350B", "Japan's five-year defence plan"),
]

TIMELINE = [
 ("01:00", "NZ final count: Luxon 65 of 130"),
 ("13:30", "F1 Practice One, Lusail"),
 ("14:30", "Wall Street reopens, half day"),
 ("17:00", "F1 Practice Two, Lusail"),
 ("18:00", "Wall Street early close, 1pm ET"),
 ("20:00", "Forest v Chelsea kick off"),
]

TAG_FULL = {"C": "CONFIRMED", "O": "OFFICIALS", "R": "REPORTED", "F": "FORECAST"}
TAG_COLOR = {"C": TEAL, "O": NAVY, "R": MUSTARD, "F": CORAL}

# Pin disc offsets (dx, dy in px). Every disc centre must sit on DRAWN land —
# verified from the rendered map, never from lon/lat alone (v3 failed this:
# pins 2/4/5/8/10/11/13 sat in sea or on the wrong landmass). Offsets move
# discs onto nearby land with a leader line to the true point; 1/13 stay
# separated by 27 px. 7 sits on Tokyo, 11 is offset NW to Manchuria.
PIN_OFF = {1: (14, -14), 2: (-6, -11), 3: (-20, 10), 4: (-3, -11), 5: (2, 6),
           11: (-16, -14), 13: (7, 8)}

# ---------------------------------------------------------------- helpers
def tw(d, text, font):
    return d.textlength(text, font=font)

def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(d, t, font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def block(d, lines, font, x, y, color=INK, leading=None, align="left", max_w=None):
    """Draw lines; returns bottom y. leading defaults to font size + 2."""
    lh = leading or (font.size + 2)
    for ln in lines:
        if align == "center":
            d.text((x + (max_w - tw(d, ln, font)) / 2, y), ln, font=font, fill=color)
        else:
            d.text((x, y), ln, font=font, fill=color)
        y += lh
    return y

def chip(d, x, y, tag):
    """Veracity chip. Returns width used."""
    label = TAG_FULL[tag]
    f = SANS_B(8)
    w = int(tw(d, label, f)) + 10
    col = TAG_COLOR[tag]
    d.rounded_rectangle([x, y, x + w, y + 13], radius=6, fill=col)
    d.text((x + 5, y + 2), label, font=f, fill=(255, 255, 255))
    return w

def fit_check(name, lines, max_lines):
    if len(lines) > max_lines:
        print(f"WARN {name}: {len(lines)} lines > {max_lines}: {' / '.join(lines)}")
    return lines

# ---------------------------------------------------------------- scenes
def scene(d, kind, x, y, w, h):
    """Flat 2D scene band inside a panel at (x,y,w,h)."""
    d.rectangle([x, y, x + w, y + h], fill=BAND)
    cx, cy = x + w / 2, y + h / 2
    if kind == "tanker":
        d.rectangle([x, y + h - 16, x + w, y + h], fill=SEA)
        d.rectangle([x + 18, cy - 2, x + w - 18, cy + 12], fill=(60, 60, 66))
        d.rectangle([x + 30, cy - 14, x + 44, cy - 2], fill=(60, 60, 66))
        d.rectangle([x + w - 52, cy - 10, x + w - 40, cy - 2], fill=(60, 60, 66))
        for fx, fy, r in [(x + 34, cy - 22, 7), (x + 46, cy - 26, 5), (x + w - 46, cy - 20, 6)]:
            d.ellipse([fx - r, fy - r, fx + r, fy + r], fill=CORAL)
            d.ellipse([fx - r // 2, fy - r // 2, fx + r // 2, fy + r // 2], fill=MUSTARD)
        for mx in (x + w - 26, x + 12):
            d.ellipse([mx - 4, y + h - 12, mx + 4, y + h - 4], fill=INK)
    elif kind == "jet":
        # Fighter jets + missile-defence arcs over land.
        d.rectangle([x, y + h - 12, x + w, y + h], fill=LAND)
        # defence arcs rising from the ground, right side
        d.arc([x + w - 78, y + 4, x + w - 2, y + h + 12], 180, 360, fill=NAVY, width=2)
        d.arc([x + w - 62, y + 14, x + w - 18, y + h + 12], 180, 360, fill=CORAL, width=2)
        d.ellipse([x + w - 44, y + 2, x + w - 36, y + 10], fill=CORAL)
        # jet 1, large, upper left flying right
        jx, jy, s, col = x + 92, cy - 12, 1.0, (70, 76, 88)
        d.line([jx - 78, jy + 3, jx - 40, jy + 3], fill=(255, 255, 255), width=2)
        d.polygon([(jx - 34, jy + 2), (jx + 30, jy - 2), (jx + 38, jy),
                   (jx + 30, jy + 3), (jx - 30, jy + 5)], fill=col)
        d.polygon([(jx - 6, jy), (jx + 6, jy - 2), (jx + 14, jy + 9),
                   (jx + 2, jy + 6)], fill=col)
        d.polygon([(jx - 30, jy), (jx - 24, jy - 10), (jx - 18, jy)], fill=col)
        d.ellipse([jx + 8, jy - 4, jx + 18, jy + 1], fill=SKY)
        d.polygon([(jx - 34, jy + 2), (jx - 42, jy), (jx - 34, jy + 5)], fill=MUSTARD)
        # jet 2, smaller, lower centre flying right
        jx, jy, s, col = x + 196, cy + 8, 0.7, (88, 94, 106)
        d.polygon([(jx - 24, jy + 1), (jx + 21, jy - 1), (jx + 27, jy),
                   (jx + 21, jy + 2), (jx - 21, jy + 4)], fill=col)
        d.polygon([(jx - 4, jy), (jx + 4, jy - 1), (jx + 10, jy + 6),
                   (jx + 1, jy + 4)], fill=col)
        d.polygon([(jx - 21, jy), (jx - 17, jy - 7), (jx - 13, jy)], fill=col)
        d.ellipse([jx + 6, jy - 3, jx + 13, jy + 1], fill=SKY)
    elif kind == "flags":
        d.rectangle([x, y, x + w, y + h], fill=(235, 228, 210))
        for i in range(7):  # US stripes
            d.rectangle([x + 14, y + 8 + i * 6, x + 62, y + 13 + i * 6],
                        fill=CORAL if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x + 14, y + 8, x + 34, y + 26], fill=NAVY)
        for s in range(3):  # Russian tricolor
            d.rectangle([x + w - 62, y + 8 + s * 7, x + w - 14, y + 15 + s * 7],
                        fill=[(255, 255, 255), NAVY, CORAL][s])
        d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], fill=SEA,
                  outline=INK, width=2)
        d.ellipse([cx - 6, cy - 8, cx + 2, cy + 1], fill=LAND)
        d.ellipse([cx + 1, cy + 3, cx + 9, cy + 10], fill=LAND)
    elif kind == "drone":
        # Quad-rotor drone over a Kuwait Towers skyline cue.
        d.rectangle([x, y + h - 14, x + w, y + h], fill=LAND)
        # Kuwait Towers: thin spires with spheres, right side
        for tx, sh_, sr in [(x + w - 46, 24, 5), (x + w - 32, 19, 4), (x + w - 20, 13, 0)]:
            d.rectangle([tx - 2, y + h - 14 - sh_, tx + 2, y + h - 14],
                        fill=(120, 110, 96))
            if sr:
                d.ellipse([tx - sr, y + h - 14 - sh_ - 5, tx + sr,
                           y + h - 14 - sh_ + 5], fill=(120, 110, 96))
        # low block, far left
        d.rectangle([x + 8, y + h - 22, x + 26, y + h - 14], fill=(150, 148, 142))
        # quad-rotor drone, centre-left of the band
        dx, dy = x + 78, cy - 2
        for ax, ay in [(-22, -8), (22, -8), (-22, 8), (22, 8)]:
            d.line([dx, dy, dx + ax, dy + ay], fill=(70, 76, 88), width=2)
            d.ellipse([dx + ax - 9, dy + ay - 2, dx + ax + 9, dy + ay + 2],
                      fill=(70, 76, 88))
        d.rounded_rectangle([dx - 12, dy - 4, dx + 12, dy + 4], radius=3,
                            fill=(70, 76, 88))
        d.ellipse([dx - 3, dy + 4, dx + 3, dy + 8], fill=CORAL)
    elif kind == "refinery":
        d.rectangle([x, y + h - 10, x + w, y + h], fill=(120, 110, 96))
        for tx in (x + 20, x + 46, x + 72):
            d.rectangle([tx, cy - 8, tx + 12, y + h - 10], fill=(90, 88, 84))
        d.polygon([(x + w - 34, y + h - 10), (x + w - 28, cy - 20), (x + w - 22, y + h - 10)],
                  fill=(90, 88, 84))
        d.ellipse([x + w - 31, cy - 30, x + w - 19, cy - 18], fill=CORAL)
        d.ellipse([x + w - 28, cy - 27, x + w - 22, cy - 21], fill=MUSTARD)
    elif kind == "ebola":
        d.ellipse([x + 12, y + 8, x + 52, y + h - 8], fill=(205, 225, 190))
        d.ellipse([x + 20, y + 14, x + 44, y + h - 14], fill=LAND2)
        d.rectangle([x + w - 52, cy - 16, x + w - 16, cy + 16], fill=(255, 255, 255),
                    outline=CORAL, width=2)
        d.rectangle([x + w - 44, cy - 3, x + w - 24, cy + 3], fill=CORAL)
        d.rectangle([x + w - 37, cy - 10, x + w - 31, cy + 10], fill=CORAL)
        for vx, vy in [(x + 62, y + 12), (x + 76, y + 24), (x + 60, y + h - 14)]:
            d.ellipse([vx - 3, vy - 3, vx + 3, vy + 3], fill=CORAL)
    elif kind == "missile":
        d.rectangle([x, y + h - 12, x + w, y + h], fill=LAND)
        d.polygon([(cx - 5, cy + 10), (cx - 5, cy - 16), (cx, cy - 26), (cx + 5, cy - 16),
                   (cx + 5, cy + 10)], fill=(70, 76, 88))
        d.polygon([(cx - 5, cy + 4), (cx - 16, cy + 12), (cx - 5, cy + 10)], fill=(70, 76, 88))
        d.polygon([(cx + 5, cy + 4), (cx + 16, cy + 12), (cx + 5, cy + 10)], fill=(70, 76, 88))
        d.ellipse([cx - 5, cy + 12, cx + 5, cy + 24], fill=MUSTARD)
        for sx, sy in [(x + 16, y + 12), (x + w - 18, y + 16), (x + w - 30, y + 8)]:
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=MUSTARD)
    elif kind == "storm":
        d.rectangle([x, y, x + w, y + h], fill=(96, 104, 116))
        d.ellipse([x + 12, y + 6, x + 52, y + 26], fill=(60, 64, 72))
        d.ellipse([x + 34, y + 2, x + 74, y + 22], fill=(60, 64, 72))
        d.ellipse([x + w - 70, y + 8, x + w - 30, y + 28], fill=(60, 64, 72))
        d.polygon([(cx - 4, y + 22), (cx + 6, y + 22), (cx - 2, y + h - 8),
                   (cx - 8, y + h - 8)], fill=MUSTARD)
        for rx in range(x + 8, x + w - 8, 14):
            d.line([rx, y + h - 16, rx - 3, y + h - 6], fill=SKY, width=2)
    elif kind == "chart":
        d.rectangle([x, y + h - 12, x + w, y + h], fill=LIGHT)
        pts = [(x + 12, y + h - 22), (x + 30, y + h - 30), (x + 46, y + h - 26),
               (x + 62, y + h - 36), (x + 78, y + h - 32), (x + w - 16, y + 10)]
        d.line(pts, fill=TEAL, width=3)
        d.polygon([(x + w - 26, y + 8), (x + w - 8, y + 8), (x + w - 16, y + 20)], fill=TEAL)
        d.rectangle([x + 14, y + h - 26, x + 30, y + h - 12], fill=CORAL)
        d.line([x + 14, y + h - 26, x + 30, y + h - 26], fill=INK, width=2)
    elif kind == "seats":
        # Parliament bar: 65 of the 66 needed — one coral seat short.
        bx0, bw = x + 14, w - 28
        # "65" sits right of the number badge (badge covers x+6..x+22).
        d.text((x + 30, y + 3), "65", font=SANS_B(13), fill=TEAL)
        d.text((bx0 + bw, y + 6), "66 NEEDED", font=SANS_B(8), fill=INK,
               anchor="ra")
        by = y + 21
        d.rectangle([bx0, by, bx0 + bw, by + 11], fill=(255, 255, 255),
                    outline=INK, width=1)
        fill_w = int(bw * 65 / 66)
        d.rectangle([bx0 + 1, by + 1, bx0 + fill_w, by + 10], fill=TEAL)
        d.rectangle([bx0 + fill_w, by + 1, bx0 + bw - 1, by + 10], fill=CORAL)
        d.rectangle([bx0 + fill_w - 1, by - 3, bx0 + fill_w + 3, by + 14],
                    outline=CORAL, width=2)
    elif kind == "datacentre":
        # Two server racks + power bolt: AI data centres by the power plants.
        for rx in (x + 16, x + w - 40):
            d.rectangle([rx, cy - 13, rx + 24, cy + 13], fill=(70, 76, 88))
            for sy in range(3):
                d.line([rx + 4, cy - 7 + sy * 8, rx + 20, cy - 7 + sy * 8],
                       fill=(200, 205, 210), width=1)
                d.ellipse([rx + 5, cy - 9 + sy * 8, rx + 8, cy - 6 + sy * 8],
                          fill=TEAL if sy % 2 == 0 else MUSTARD)
        d.polygon([(cx + 3, cy - 16), (cx - 6, cy + 2), (cx - 1, cy + 2),
                   (cx - 4, cy + 16), (cx + 6, cy - 2), (cx + 1, cy - 2)],
                  fill=MUSTARD)
    elif kind == "rocket":
        d.polygon([(cx - 6, cy + 12), (cx - 6, cy - 12), (cx, cy - 24), (cx + 6, cy - 12),
                   (cx + 6, cy + 12)], fill=(235, 235, 230))
        d.polygon([(cx - 6, cy + 6), (cx - 16, cy + 14), (cx - 6, cy + 12)], fill=CORAL)
        d.polygon([(cx + 6, cy + 6), (cx + 16, cy + 14), (cx + 6, cy + 12)], fill=CORAL)
        d.ellipse([cx - 3, cy - 8, cx + 3, cy - 2], fill=SKY)
        d.ellipse([cx - 4, cy + 14, cx + 4, cy + 24], fill=MUSTARD)
        for sx, sy in [(x + 14, y + 10), (x + w - 16, y + 14), (x + 22, y + h - 12),
                       (x + w - 26, y + h - 10)]:
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=INK)
    elif kind == "euro":
        for i, bx in enumerate((x + 16, x + 44, x + 72)):
            d.rectangle([bx, cy - 6, bx + 12, y + h - 10], fill=(150, 142, 126))
            d.rectangle([bx - 2, cy - 10, bx + 14, cy - 6], fill=(150, 142, 126))
        d.text((x + w - 30, y + 4), "\u20ac", font=SANS_B(26), fill=MUSTARD)
    elif kind == "mine":
        d.polygon([(x, y + h), (x + w // 2, y + 6), (x + w, y + h)], fill=(96, 82, 64))
        d.rectangle([x + w - 44, cy - 4, x + w - 20, cy + 8], fill=MUSTARD)
        d.rectangle([x + w - 40, cy - 10, x + w - 24, cy - 4], fill=MUSTARD)
        d.rectangle([x + w - 38, cy + 8, x + w - 26, cy + 12], fill=(60, 60, 66))
        for wx in range(x + 8, x + w - 40, 16):
            d.line([wx, y + h - 8, wx + 8, y + h - 14], fill=SEA, width=2)
    elif kind == "f1":
        d.polygon([(x + 12, cy + 6), (x + 34, cy - 2), (x + 58, cy - 4), (x + 78, cy + 2),
                   (x + 82, cy + 8), (x + 14, cy + 10)], fill=CORAL)
        d.ellipse([x + 24, cy + 6, x + 36, cy + 18], fill=INK)
        d.ellipse([x + 62, cy + 6, x + 74, cy + 18], fill=INK)
        for r in range(3):
            for c in range(3):
                d.rectangle([x + w - 26 + c * 6, y + 8 + r * 6, x + w - 21 + c * 6,
                             y + 13 + r * 6], fill=INK if (r + c) % 2 == 0 else (255, 255, 255))

# ---------------------------------------------------------------- map
N_AMERICA = [(-168,66),(-158,71),(-140,70),(-130,71),(-120,72),(-110,73),(-100,72),
 (-95,80),(-88,74),(-82,72),(-76,71),(-68,66),(-64,60),(-56,52),(-59,47),(-65,44),
 (-70,42),(-74,39),(-76,35),(-80,32),(-81,30),(-81,27),(-80,25.5),(-82,26.5),
 (-84,29),(-86,29.5),(-88,29.5),(-90,29),(-91,28),(-94,29),(-97,26),(-97,22),
 (-95,19),(-93,17),(-91,15),(-88,14),(-85,13),(-83,11),(-81,9),(-79,9),(-76,6),
 (-80,4),(-80,0),(-81,-3),(-80,-6),(-77,-11),(-74,-16),(-71,-18),(-70,-22),
 (-70,-30),(-71,-38),(-73,-45),(-73,-52),(-70,-54),(-68,-50),(-66,-44),(-62,-40),
 (-58,-36),(-53,-33),(-48,-28),(-46,-24),(-40,-20),(-37,-12),(-35,-8),(-38,-5),
 (-44,-3),(-50,0),(-51,4),(-55,5),(-60,8),(-66,10),(-72,8),(-76,6),(-79,9)]
S_AMERICA = [(-79,9),(-76,6),(-72,8),(-66,10),(-60,8),(-55,5),(-51,4),(-50,0),
 (-44,-3),(-38,-5),(-35,-8),(-37,-12),(-40,-20),(-46,-24),(-48,-28),(-53,-33),
 (-58,-36),(-62,-40),(-66,-44),(-68,-50),(-70,-54),(-73,-52),(-73,-45),(-71,-38),
 (-70,-30),(-70,-20),(-72,-15),(-76,-10),(-79,-5),(-81,0),(-80,5)]
AFRICA = [(-17,15),(-16,20),(-12,25),(-9,30),(-5,35),(0,36),(8,37),(11,34),(15,32),
 (20,32),(25,31),(30,31),(33,28),(36,27),(38,22),(39,18),(41,14),(44,11),(48,11),
 (51,10),(48,5),(45,0),(41,-5),(40,-10),(37,-15),(35,-20),(33,-25),(30,-30),
 (27,-33),(22,-35),(19,-33),(16,-30),(14,-25),(12,-18),(11,-12),(9,-5),(9,0),
 (9,4),(5,4),(-2,5),(-8,4),(-12,8),(-15,11)]
EURASIA = [(-9,37),(-9,43),(-4,48),(-2,50),(0,51),(3,53),(6,55),(8,57),(10,59),
 (14,58),(18,56),(21,55),(23,58),(26,60),(30,62),(35,65),(40,67),(45,68),(50,69),
 (55,70),(60,71),(65,72),(70,73),(75,74),(80,75),(90,76),(100,77),(110,76),
 (120,73),(130,72),(140,72),(150,71),(160,70),(170,67),(178,65),(175,62),(170,60),
 (165,58),(162,55),(160,52),(158,48),(156,44),(152,42),(148,40),(144,40),(142,42),
 (141,45),(140,40),(138,37),(136,35),(134,33),(132,32),(130,31),(128,33),(127,35),
 (128,37),(127.5,39.5),(126.5,41),(124,41),(122,39),(121,36),(120,33),(119,30),
 (117,27),(115,24),(113,22),(110,20),(109,18),(108,14),(106,10),(104,9),(102,7),
 (100,6),(99,9),(98,12),(97,15),(95,16),(93,20),(91,22),(89,22),(87,21),(85,19),
 (83,17),(81,14),(80,10),(78,8),(77,8),(76,10),(74,14),(72,19),(70,21),(68,23),
 (66,25),(63,25),(61,25),(58,25),(57,26),(56,27),(55,26),(53,26),(51,27),(50,29),
 (49,30),(47,30),(44,29),(42,28),(40,29),(38,30),(36,31),(35,31.5),(34.5,32),
 (34.8,33),(35.5,34),(35.8,35.5),(34,36),(33,36),(30,36),(27,37),(26,38),
 (24,38),(22,37),(20,39),(18,40),(16,40),(14,42),(12,44),(10,44),(8,44),(6,43),
 (3,43),(1,41),(0,39),(-2,37),(-5,36),(-9,37)]
ISLANDS = [(95,5),(100,0),(104,-3),(106,-6),(110,-8),(115,-8.5),(120,-9.5),(125,-9),
 (130,-6),(135,-4),(140,-8),(136,-4),(132,-1),(128,1),(124,1),(120,1),(116,2),
 (112,3),(108,2),(104,1),(100,4)]
AUSTRALIA = [(113,-22),(114,-30),(115,-35),(120,-34),(125,-32),(129,-32),(132,-32),
 (135,-35),(138,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),
 (146,-19),(142,-15),(142,-11),(137,-12),(135,-15),(132,-12),(130,-13),(126,-14),
 (122,-17),(118,-20)]
UK = [(-5,50),(-3,53),(-5,56),(-2,58),(0,53),(1,51)]
JAPAN = [(130,31),(132,33),(135,34),(137,35),(139,36),(140,38),(141,40),(142,42),
 (143,44),(141,43),(140,40),(138,37),(136,35),(133,34),(131,32)]
NZ = [(167,-45),(170,-42),(174,-40),(177,-38),(175,-37),(172,-41),(168,-44)]
# Arabian peninsula (missing from the Eurasia outline above, which stops at
# the Gulf coast — without it, Yemen/Saudi pins read as sea). Drawn in LAND.
ARABIA = [(38,27),(39,24),(40,21),(42,18),(43,14),(44,12.5),(47,13),(50,14.5),
 (53,16),(56,18),(58.5,20),(59,22.5),(57.5,25),(55,26),(52,26.5),(50.5,29),
 (48,29.5),(45,29),(42,28),(39,28)]
# Island chains drawn as fat lines so the discs can sit ON visible land:
# Honshu (Tokyo), UK (London), NZ (Wellington), Indonesia (Java).
JAPAN_LINE = [(130,31),(132,33),(134,34),(136,35),(138,35.5),(139.5,36.5),
 (140.5,38.5),(141.5,40.5),(142.5,42.5),(143.5,44)]
UK_LINE = [(-5,50),(-4,52),(-3,54),(-2,56),(-1,57.5),(0,54),(1,51.5)]
NZ_NORTH = [(173,-36.5),(174.5,-38),(176,-39.5),(174.8,-41.2)]
NZ_SOUTH = [(172.5,-40.5),(170.5,-42.5),(168.5,-44.5),(167.5,-46)]
ISLANDS_LINE = [(95,5),(100,1),(104,-3),(107,-6.5),(111,-7.5),(115,-8.5),
 (120,-9.5),(125,-9),(130,-5),(136,-4),(140,-7)]

# ---------------------------------------------------------------- layout
def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    X0, CW = 24, 976

    # Masthead
    d.text((W / 2, 12), "THE DAY IN WORLD NEWS", font=SANS_B(12), fill=CORAL,
           anchor="ma")
    d.text((W / 2, 28), "FRIDAY 27 NOVEMBER 2026", font=SERIF_B(40), fill=INK,
           anchor="ma")
    d.line([X0, 82, X0 + CW, 82], fill=RULE, width=2)
    tick = ("TANKERS HIT MINES IN HORMUZ  \u2022  ISRAEL READY TO STRIKE IRAN ALONE  "
            "\u2022  TRUMP PRESSES PUTIN TO PULL BACK")
    d.text((W / 2, 90), tick, font=SANS_B(12), fill=INK, anchor="ma")
    total = len(PANELS) + len(ALSO)
    d.text((W / 2, 112), f"{total} STORIES  \u2022  7 REGIONS  \u2022  ONE DAY",
           font=SANS_B(13), fill=INK, anchor="ma")

    # UTC timeline strip
    d.rectangle([X0, 136, X0 + CW, 160], fill=BAND)
    cell = CW / len(TIMELINE)
    for i, (t, label) in enumerate(TIMELINE):
        cx = X0 + i * cell
        d.text((cx + 10, 139), t, font=SANS_B(9), fill=CORAL)
        d.text((cx + 10, 150), label, font=SANS(8), fill=MUTED)
        if i:
            d.line([cx, 140, cx, 156], fill=(200, 186, 160), width=1)

    # Big numbers strip
    bw = (CW - 5 * 4) / 6
    for i, (num, label) in enumerate(BIG):
        bx = X0 + i * (bw + 4)
        d.rectangle([bx, 166, bx + bw, 210], fill=PAPER, outline=(210, 196, 170))
        d.text((bx + bw / 2, 170), num, font=SERIF_B(20), fill=CORAL, anchor="ma")
        lines = fit_check("bignum", wrap(d, label, SANS(8), bw - 12), 2)
        block(d, lines, SANS(8), bx + 6, 194, color=MUTED, align="center",
              max_w=bw - 12, leading=10)

    # Region bar (counts computed from data)
    regions = ["Asia", "North America", "Europe", "Middle East",
               "Latin America", "Oceania", "Africa"]
    rcol = {"Asia": TEAL, "North America": NAVY, "Europe": MUSTARD,
            "Middle East": CORAL, "Latin America": (120, 90, 160),
            "Oceania": (60, 140, 160), "Africa": (90, 140, 70)}
    rlab = {"Asia": "ASIA", "North America": "N AMERICA", "Europe": "EUROPE",
            "Middle East": "M EAST", "Latin America": "LATAM", "Oceania": "OCEANIA",
            "Africa": "AFRICA"}
    counts = {r: 0 for r in regions}
    for p in PANELS:
        counts[p["region"]] += 1
    for r in ALSO_REG:
        counts[r] += 1
    assert sum(counts.values()) == total, (counts, total)
    # Segment widths proportional to counts, but every segment gets at least
    # its full label width + 8 px so no label collapses to a bare number.
    # Deficit is taken from the segments with the most spare width.
    widths = {r: CW * counts[r] / total for r in regions}
    for _ in range(20):
        need = {r: tw(d, f"{rlab[r]} {counts[r]}", SANS_B(8)) + 8 for r in regions}
        short = [r for r in regions if widths[r] < need[r]]
        if not short:
            break
        deficit = sum(need[r] - widths[r] for r in short)
        donors = [r for r in regions if widths[r] > need[r]]
        spare = sum(widths[r] - need[r] for r in donors)
        if spare <= 0:
            break
        for r in short:
            widths[r] = need[r]
        for r in donors:
            widths[r] -= deficit * (widths[r] - need[r]) / spare
    rx = X0
    for r in regions:
        seg = widths[r]
        d.rectangle([rx, 216, rx + seg - 1, 236], fill=rcol[r])
        lab = f"{rlab[r]} {counts[r]}"
        if tw(d, lab, SANS_B(8)) <= seg - 6:
            d.text((rx + seg / 2, 222), lab, font=SANS_B(8),
                   fill=(255, 255, 255), anchor="ma")
        elif tw(d, str(counts[r]), SANS_B(8)) <= seg - 4:
            d.text((rx + seg / 2, 222), str(counts[r]), font=SANS_B(8),
                   fill=(255, 255, 255), anchor="ma")
        rx += seg

    # Panels
    def panel(p, x, y, w, h, hero):
        d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=(200, 186, 160))
        sh = 58 if hero else 38
        scene(d, p["scene"], x + 1, y + 1, w - 2, sh)
        # number badge
        d.ellipse([x + 6, y + 6, x + 22, y + 22], fill=INK)
        num = str(p["n"])
        d.text((x + 14, y + 8), num, font=SANS_B(10 if len(num) == 1 else 9),
               fill=(255, 255, 255), anchor="ma")
        hf = SANS_B(20 if hero else 15)
        df = SANS(10)
        hl = fit_check(f"head{p['n']}", wrap(d, p["head"], hf, w - 16),
                       2 if hero else 2)
        hy = y + sh + 4 if hero else y + sh + 4
        block(d, hl, hf, x + 8, hy, leading=(22 if hero else 16))
        dy = (y + sh + 50) if hero else (y + sh + 36)
        dl = fit_check(f"deck{p['n']}", wrap(d, p["deck"], df, w - 16), 2)
        block(d, dl, df, x + 8, dy, color=MUTED, leading=11)
        chip(d, x + 8, y + h - 20, p["tag"])

    for i, p in enumerate(PANELS[:3]):
        panel(p, X0 + i * (318 + 11), 244, 318, 158, True)
    for row in range(2):
        for col in range(5):
            p = PANELS[3 + row * 5 + col]
            panel(p, X0 + col * (187 + 10), 410 + row * 118, 187, 118, False)

    # Map + ALSO ON
    d.text((X0, 660), "THE WORLD \u2014 13 PINNED STORIES", font=SANS_B(11), fill=INK)
    d.text((512, 660), "ALSO ON \u2014 22 MORE STORIES", font=SANS_B(11), fill=INK)
    map_box = (X0, 678, 500, 920)
    d.rectangle(map_box, fill=(208, 226, 236), outline=(200, 186, 160))
    mx0, my0, mw, mh = X0 + 4, 682, 468, 200
    lon0, lon1, lat0, lat1 = -168, 192, 84, -58
    def proj(lon, lat):
        return (mx0 + (lon - lon0) * mw / (lon1 - lon0),
                my0 + (lat0 - lat) * mh / (lat0 - lat1))
    for poly, col in [(N_AMERICA, LAND), (AFRICA, LAND), (EURASIA, LAND),
                      (ARABIA, LAND), (ISLANDS, LAND2), (AUSTRALIA, LAND2),
                      (UK, LAND2), (JAPAN, LAND2), (NZ, LAND2)]:
        d.polygon([proj(lo, la) for lo, la in poly], fill=col)
    # Fat island lines so pin discs sit on visible land, not sea.
    for line, wd in [(JAPAN_LINE, 7), (UK_LINE, 6), (NZ_NORTH, 12),
                     (NZ_SOUTH, 12), (ISLANDS_LINE, 5)]:
        d.line([proj(lo, la) for lo, la in line], fill=LAND2, width=wd,
               joint="curve")
    # pins: leader line from true point to offset disc
    for p in PANELS:
        tx, ty = proj(p["lon"], p["lat"])
        dx, dy = PIN_OFF.get(p["n"], (0, 0))
        px, py = tx + dx, ty + dy
        if (dx, dy) != (0, 0):
            d.line([tx, ty, px, py], fill=INK, width=1)
        d.ellipse([tx - 2, ty - 2, tx + 2, ty + 2], fill=INK)
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=CORAL,
                  outline=(255, 255, 255), width=2)
        d.text((px, py - 1), str(p["n"]), font=SANS_B(9 if p["n"] < 10 else 8),
               fill=(255, 255, 255), anchor="ma")
    d.text((X0, 890), "REGIONS: ASIA 13 \u2022 N. AMERICA 7 \u2022 EUROPE 4 \u2022 MIDDLE EAST 5 "
           "\u2022 LATIN AMERICA 2 \u2022 OCEANIA 3 \u2022 AFRICA 1",
           font=SANS(8), fill=MUTED)
    d.text((X0, 904), "Pins 1\u201313 match the panel numbers above. Discs are offset with "
           "leader lines where coasts are crowded.",
           font=SANS(8), fill=MUTED)

    # ALSO ON list: 2 columns x 11 rows
    for i, (tag, label, text) in enumerate(ALSO):
        col, row = divmod(i, 11)
        ax = 512 + col * 246
        ay = 678 + row * 22
        d.rectangle([ax, ay + 1, ax + 12, ay + 13], fill=TAG_COLOR[tag])
        d.text((ax + 6, ay + 1), tag, font=SANS_B(8), fill=(255, 255, 255),
               anchor="ma")
        f = SANS_B(9)
        rf = SANS(9)
        # Bold keyword + colon, then regular text with a clear gap.
        # The first line starts after the keyword; each run is wrapped
        # in its own font, so the wider bold keyword can never overrun
        # the headline text that follows it.
        kw = label + ":"
        kw_w = int(tw(d, kw, f))
        gap = 6
        words = text.split()
        lines, cur, limit = [], "", 222 - kw_w - gap
        for w in words:
            t = (cur + " " + w).strip()
            if tw(d, t, rf) <= limit:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
                limit = 222
        if cur:
            lines.append(cur)
        lines = fit_check(f"also{i+14}", lines, 2)
        d.text((ax + 16, ay + 1), kw, font=f, fill=INK)
        if lines:
            d.text((ax + 16 + kw_w + gap, ay + 1), lines[0], font=rf, fill=INK)
        if len(lines) > 1:
            d.text((ax + 16, ay + 12), lines[1], font=rf, fill=INK)

    # DATE CHECK
    d.rectangle([X0, 930, X0 + CW, 964], outline=CORAL, width=2, fill=(255, 244, 240))
    dc = ("DATE CHECK \u2014 Wires read up to 23:30 UTC, Fri 27 Nov 2026. Every story "
          "here was reported, or still developing, on 27 Nov in at least one time "
          "zone. Left out: Las Vegas GP, Verstappen\u2019s win (22 Nov); Trump\u2013Putin "
          "APEC meeting, Shenzhen (19 Nov); FCC satellite approval (25 Nov); de Cos "
          "ECB pick (26 Nov); Musk SpaceX share gift (26 Nov). Not yet: Netanyahu Iran decision; Qatar GP qualifying "
          "(Sat 28 Nov).")
    dl = fit_check("datecheck", wrap(d, dc, SANS(8), CW - 24), 3)
    block(d, dl, SANS(8), X0 + 10, 934, leading=11)

    # Footer
    d.text((X0, 972), "Sources: Reuters, AP, AFP, BBC, Al Jazeera, Xinhua, Kyodo, Straits "
           "Times, MarketWatch, Barron\u2019s, CNA, Middle East Eye.",
           font=SANS(8), fill=MUTED)
    d.text((X0, 985), "Drawn in code \u2014 flat vector, no photographs. Veracity: "
           "C CONFIRMED \u2022 O OFFICIALS \u2022 R REPORTED \u2022 F FORECAST.",
           font=SANS(8), fill=MUTED)

    img.save(OUT)
    print("saved", OUT, os.path.getsize(OUT), "bytes")

ALSO_REG = ["North America", "North America", "Europe", "Asia", "Asia", "Asia",
            "Oceania", "Europe", "Asia", "Asia", "Asia", "Oceania", "Asia",
            "Latin America", "Asia", "North America", "Latin America",
            "North America", "Asia", "North America", "Asia", "Europe"]

if __name__ == "__main__":
    main()
