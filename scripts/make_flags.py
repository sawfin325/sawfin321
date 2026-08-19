#!/usr/bin/env python3
"""Generate compact SVG flags for the Vespera footer."""
from pathlib import Path

OUT = Path("/workspace/assets/flags")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 60, 40


def svg(inner, w=W, h=H):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice">\n'
        f"{inner}\n</svg>\n"
    )


def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'


def stripe3(c1, c2, c3, vertical=False):
    if vertical:
        return rect(0, 0, 20, 40, c1) + rect(20, 0, 20, 40, c2) + rect(40, 0, 20, 40, c3)
    return rect(0, 0, 60, 40 / 3, c1) + rect(0, 40 / 3, 60, 40 / 3, c2) + rect(0, 80 / 3, 60, 40 / 3, c3)


def star(cx, cy, r, fill, n=5, rot=-90):
    import math
    pts = []
    for i in range(n * 2):
        ang = math.radians(rot + i * 180 / n)
        rad = r if i % 2 == 0 else r * 0.4
        pts.append(f"{cx + rad * math.cos(ang):.2f},{cy + rad * math.sin(ang):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


flags = {}

# Germany
flags["de"] = svg(stripe3("#000", "#dd0000", "#ffce00"))
# United Kingdom
flags["gb"] = svg(
    rect(0, 0, 60, 40, "#012169")
    + '<path d="M0 0 L60 40 M60 0 L0 40" stroke="#fff" stroke-width="8"/>'
    + '<path d="M0 0 L60 40" stroke="#c8102e" stroke-width="2.6"/>'
    + '<path d="M60 0 L0 40" stroke="#c8102e" stroke-width="2.6"/>'
    + '<path d="M30 0 V40 M0 20 H60" stroke="#fff" stroke-width="13"/>'
    + '<path d="M30 0 V40 M0 20 H60" stroke="#c8102e" stroke-width="8"/>'
)
# Belgium
flags["be"] = svg(stripe3("#000", "#fdda24", "#ef3340", vertical=True))
# Croatia — red white blue with simplified shield
flags["hr"] = svg(
    stripe3("#ff0000", "#fff", "#171796")
    + '<g transform="translate(24,12)">'
    + rect(0, 0, 12, 12, "#fff")
    + "".join(
        rect(c * 3, r * 3, 3, 3, "#ff0000" if (r + c) % 2 == 0 else "#171796")
        for r in range(4)
        for c in range(4)
    )
    + "</g>"
)
# South Korea
flags["kr"] = svg(
    rect(0, 0, 60, 40, "#fff")
    + f'<circle cx="30" cy="20" r="8" fill="#cd2e3a"/>'
    + f'<path d="M30 20 a8 8 0 0 1 0 -16 a4 4 0 0 1 0 8 a4 4 0 0 0 0 8" fill="#0047a0"/>'
    + '<g stroke="#000" stroke-width="1.6" fill="none">'
    + '<path d="M16 10 l6 -4 M16 13 l6 -4 M16 16 l6 -4"/>'
    + '<path d="M44 30 l-6 4 M44 27 l-6 4 M44 24 l-6 4"/>'
    + "</g>"
)
# India
flags["in"] = svg(
    stripe3("#ff9933", "#fff", "#138808")
    + '<circle cx="30" cy="20" r="5.2" fill="none" stroke="#000080" stroke-width="1"/>'
    + "".join(
        f'<line x1="30" y1="20" x2="{30 + 5.2 * __import__("math").cos(__import__("math").radians(i*15)):.2f}" '
        f'y2="{20 + 5.2 * __import__("math").sin(__import__("math").radians(i*15)):.2f}" '
        f'stroke="#000080" stroke-width="0.4"/>'
        for i in range(24)
    )
)
# Singapore
flags["sg"] = svg(
    rect(0, 0, 60, 20, "#ed2939")
    + rect(0, 20, 60, 20, "#fff")
    + '<circle cx="12" cy="10" r="6" fill="#fff"/>'
    + '<circle cx="15" cy="10" r="5.2" fill="#ed2939"/>'
    + star(22, 6, 1.6, "#fff")
    + star(26.5, 8.5, 1.6, "#fff")
    + star(24.8, 13.2, 1.6, "#fff")
    + star(19.2, 13.2, 1.6, "#fff")
    + star(17.5, 8.5, 1.6, "#fff")
)
# Philippines
flags["ph"] = svg(
    '<polygon points="0,0 60,0 60,20 26,20" fill="#0038a8"/>'
    + '<polygon points="0,40 60,40 60,20 26,20" fill="#ce1126"/>'
    + '<polygon points="0,0 26,20 0,40" fill="#fff"/>'
    + star(9, 20, 4.2, "#fcd116")
    + star(7, 11, 1.7, "#fcd116")
    + star(7, 29, 1.7, "#fcd116")
)
# United States
us_stars = ""
for r in range(5):
    for c in range(6):
        us_stars += star(3.2 + c * 3.9, 3 + r * 3.6, 1.15, "#fff")
flags["us"] = svg(
    rect(0, 0, 60, 40, "#fff")
    + "".join(rect(0, i * (40 / 13), 60, 40 / 13, "#b22234") for i in range(0, 13, 2))
    + rect(0, 0, 24, 40 * 7 / 13, "#3c3b6e")
    + us_stars
)
# Austria
flags["at"] = svg(stripe3("#ed2939", "#fff", "#ed2939"))
# Hungary
flags["hu"] = svg(stripe3("#ce2939", "#fff", "#477050"))
# Hong Kong
flags["hk"] = svg(
    rect(0, 0, 60, 40, "#de2910")
    + "".join(
        f'<g transform="translate(30,20) rotate({i*72})">'
        f'<polygon points="0,-11 2.2,-3.4 0,-1.6 -2.2,-3.4" fill="#fff"/>'
        f'<circle cx="0" cy="-4.8" r="0.7" fill="#de2910"/>'
        f"</g>"
        for i in range(5)
    )
)
# Portugal
flags["pt"] = svg(
    rect(0, 0, 24, 40, "#006600")
    + rect(24, 0, 36, 40, "#ff0000")
    + '<circle cx="24" cy="20" r="7" fill="#ffd700"/>'
    + '<circle cx="24" cy="20" r="4.2" fill="#fff"/>'
    + '<circle cx="24" cy="20" r="2.2" fill="#ff0000"/>'
)
# Finland
flags["fi"] = svg(
    rect(0, 0, 60, 40, "#fff")
    + rect(16, 0, 10, 40, "#003580")
    + rect(0, 15, 60, 10, "#003580")
)
# UAE
flags["ae"] = svg(
    rect(15, 0, 45, 40 / 3, "#00732f")
    + rect(15, 40 / 3, 45, 40 / 3, "#fff")
    + rect(15, 80 / 3, 45, 40 / 3, "#000")
    + rect(0, 0, 15, 40, "#ff0000")
)
# Thailand
flags["th"] = svg(
    rect(0, 0, 60, 40, "#ed1c24")
    + rect(0, 6.5, 60, 27, "#fff")
    + rect(0, 13, 60, 14, "#241d4f")
)
# Switzerland
flags["ch"] = svg(
    rect(0, 0, 60, 40, "#ff0000")
    + rect(26, 8, 8, 24, "#fff")
    + rect(18, 16, 24, 8, "#fff")
)
# Czechia
flags["cz"] = svg(
    rect(0, 0, 60, 20, "#fff")
    + rect(0, 20, 60, 20, "#d7141a")
    + '<polygon points="0,0 26,20 0,40" fill="#11457e"/>'
)
# China
flags["cn"] = svg(
    rect(0, 0, 60, 40, "#de2910")
    + star(10, 10, 5.2, "#ffde00")
    + star(20, 4.5, 1.7, "#ffde00", rot=20)
    + star(24, 9, 1.7, "#ffde00", rot=40)
    + star(24, 14.5, 1.7, "#ffde00", rot=10)
    + star(20, 18.5, 1.7, "#ffde00", rot=-20)
)
# Spain
flags["es"] = svg(
    rect(0, 0, 60, 10, "#aa151b")
    + rect(0, 10, 60, 20, "#f1bf00")
    + rect(0, 30, 60, 10, "#aa151b")
    + rect(12, 14, 8, 12, "#c60b1e")
)
# Brazil
flags["br"] = svg(
    rect(0, 0, 60, 40, "#009b3a")
    + '<polygon points="30,4 56,20 30,36 4,20" fill="#fedf00"/>'
    + '<circle cx="30" cy="20" r="8" fill="#002776"/>'
    + '<path d="M22 21 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="1.4"/>'
)
# Norway
flags["no"] = svg(
    rect(0, 0, 60, 40, "#ba0c2f")
    + rect(16, 0, 12, 40, "#fff")
    + rect(0, 14, 60, 12, "#fff")
    + rect(18.5, 0, 7, 40, "#00205b")
    + rect(0, 16.5, 60, 7, "#00205b")
)
# South Africa
flags["za"] = svg(
    rect(0, 0, 60, 40, "#de3831")
    + rect(0, 20, 60, 20, "#002395")
    + '<polygon points="0,6 28,20 0,34" fill="#fff"/>'
    + '<polygon points="0,13 18,20 0,27" fill="#007a4d"/>'
    + '<path d="M0 6 L28 20 L60 20 L60 14 L32 14 Z" fill="#fff"/>'
    + '<path d="M0 34 L28 20 L60 20 L60 26 L32 26 Z" fill="#fff"/>'
    + '<path d="M18 20 L60 20 L60 16.8 L28 16.8 Z" fill="#ffb612"/>'
    + '<path d="M18 20 L60 20 L60 23.2 L28 23.2 Z" fill="#ffb612"/>'
)
# Oman
flags["om"] = svg(
    rect(18, 0, 42, 40 / 3, "#fff")
    + rect(18, 40 / 3, 42, 40 / 3, "#c8102e")
    + rect(18, 80 / 3, 42, 40 / 3, "#00833e")
    + rect(0, 0, 18, 40, "#c8102e")
    + star(9, 8, 3.2, "#fff")
)
# Poland
flags["pl"] = svg(rect(0, 0, 60, 20, "#fff") + rect(0, 20, 60, 20, "#dc143c"))
# Türkiye
flags["tr"] = svg(
    rect(0, 0, 60, 40, "#e30a17")
    + '<circle cx="22" cy="20" r="10" fill="#fff"/>'
    + '<circle cx="26" cy="20" r="8" fill="#e30a17"/>'
    + star(36, 20, 5, "#fff")
)
# Netherlands
flags["nl"] = svg(stripe3("#ae1c28", "#fff", "#21468b"))
# Mexico
flags["mx"] = svg(
    stripe3("#006847", "#fff", "#ce1126", vertical=True)
    + '<circle cx="30" cy="20" r="5" fill="#c4a36a"/>'
    + '<circle cx="30" cy="20" r="2.4" fill="#006847"/>'
)
# Argentina
flags["ar"] = svg(
    stripe3("#74acdf", "#fff", "#74acdf")
    + star(30, 20, 5.5, "#f6b40e", n=8, rot=-90)
    + '<circle cx="30" cy="20" r="2" fill="#f6b40e"/>'
)
# Slovakia
flags["sk"] = svg(
    stripe3("#fff", "#0b4ea2", "#ee1c25")
    + '<polygon points="10,8 22,8 22,28 16,32 10,28" fill="#fff" stroke="#0b4ea2" stroke-width="0.6"/>'
    + '<polygon points="12,12 20,12 20,22 16,24 12,22" fill="#ee1c25"/>'
    + '<rect x="14.5" y="14" width="3" height="8" fill="#fff"/>'
    + '<rect x="13" y="16.5" width="6" height="3" fill="#fff"/>'
)
# Chile
flags["cl"] = svg(
    rect(0, 0, 60, 20, "#fff")
    + rect(0, 20, 60, 20, "#d52b1e")
    + rect(0, 0, 20, 20, "#0039a6")
    + star(10, 10, 5, "#fff")
)
# Qatar
flags["qa"] = svg(
    rect(0, 0, 60, 40, "#8d1b3d")
    + '<path d="M0 0 H18 l8 2.5 L18 5 l8 2.5 L18 10 l8 2.5 L18 15 l8 2.5 L18 20 l8 2.5 L18 25 l8 2.5 L18 30 l8 2.5 L18 35 l8 2.5 L18 40 H0 Z" fill="#fff"/>'
)
# Greece
flags["gr"] = svg(
    rect(0, 0, 60, 40, "#0d5eaf")
    + "".join(rect(0, i * (40 / 9), 60, 40 / 9, "#fff") for i in range(1, 9, 2))
    + rect(0, 0, 22, 40 * 5 / 9, "#0d5eaf")
    + rect(8.5, 0, 5, 40 * 5 / 9, "#fff")
    + rect(0, 8.5, 22, 5, "#fff")
)
# Italy
flags["it"] = svg(stripe3("#009246", "#fff", "#ce2b37", vertical=True))
# Australia
au_stars = star(42, 22, 5.4, "#fff") + star(42, 8, 2.2, "#fff") + star(50, 14, 2.2, "#fff") + star(34, 14, 2.2, "#fff") + star(38, 32, 2.4, "#fff")
flags["au"] = svg(
    rect(0, 0, 60, 40, "#00008b")
    + rect(0, 0, 30, 20, "#012169")
    + '<path d="M0 0 L30 20 M30 0 L0 20" stroke="#fff" stroke-width="4"/>'
    + '<path d="M0 0 L30 20 M30 0 L0 20" stroke="#c8102e" stroke-width="1.5"/>'
    + '<path d="M15 0 V20 M0 10 H30" stroke="#fff" stroke-width="6"/>'
    + '<path d="M15 0 V20 M0 10 H30" stroke="#c8102e" stroke-width="3.2"/>'
    + au_stars
)
# Sweden
flags["se"] = svg(
    rect(0, 0, 60, 40, "#006aa7")
    + rect(18, 0, 8, 40, "#fecc00")
    + rect(0, 16, 60, 8, "#fecc00")
)
# Russia
flags["ru"] = svg(stripe3("#fff", "#0039a6", "#d52b1e"))
# Taiwan
flags["tw"] = svg(
    rect(0, 0, 60, 40, "#fe0000")
    + rect(0, 0, 30, 22, "#000095")
    + star(15, 11, 7, "#fff", n=12, rot=-90)
    + '<circle cx="15" cy="11" r="3.2" fill="#000095"/>'
    + '<circle cx="15" cy="11" r="2.2" fill="#fff"/>'
)
# Indonesia
flags["id"] = svg(rect(0, 0, 60, 20, "#ff0000") + rect(0, 20, 60, 20, "#fff"))
# Bahrain
flags["bh"] = svg(
    rect(0, 0, 60, 40, "#ce1126")
    + '<path d="M0 0 H16 l8 4 L16 8 l8 4 L16 16 l8 4 L16 24 l8 4 L16 32 l8 4 L16 40 H0 Z" fill="#fff"/>'
)
# France
flags["fr"] = svg(stripe3("#002395", "#fff", "#ed2939", vertical=True))
# Canada
flags["ca"] = svg(
    rect(0, 0, 15, 40, "#d52b1e")
    + rect(45, 0, 15, 40, "#d52b1e")
    + rect(15, 0, 30, 40, "#fff")
    + '<polygon points="30,8 33,16 41,16 35,21 37,30 30,24 23,30 25,21 19,16 27,16" fill="#d52b1e"/>'
    + '<rect x="28.5" y="28" width="3" height="6" fill="#d52b1e"/>'
)
# Denmark
flags["dk"] = svg(
    rect(0, 0, 60, 40, "#c60c30")
    + rect(18, 0, 8, 40, "#fff")
    + rect(0, 16, 60, 8, "#fff")
)
# Romania
flags["ro"] = svg(stripe3("#002b7f", "#fcd116", "#ce1126", vertical=True))
# Japan
flags["jp"] = svg(rect(0, 0, 60, 40, "#fff") + '<circle cx="30" cy="20" r="10" fill="#bc002d"/>')
# New Zealand
flags["nz"] = svg(
    rect(0, 0, 60, 40, "#00247d")
    + rect(0, 0, 30, 20, "#012169")
    + '<path d="M0 0 L30 20 M30 0 L0 20" stroke="#fff" stroke-width="4"/>'
    + '<path d="M0 0 L30 20 M30 0 L0 20" stroke="#c8102e" stroke-width="1.5"/>'
    + '<path d="M15 0 V20 M0 10 H30" stroke="#fff" stroke-width="6"/>'
    + '<path d="M15 0 V20 M0 10 H30" stroke="#c8102e" stroke-width="3.2"/>'
    + star(44, 12, 3.6, "#fff")
    + star(44, 12, 2.2, "#cc142b")
    + star(50, 22, 3.2, "#fff")
    + star(50, 22, 1.9, "#cc142b")
    + star(38, 22, 2.6, "#fff")
    + star(38, 22, 1.5, "#cc142b")
    + star(46, 32, 3.0, "#fff")
    + star(46, 32, 1.7, "#cc142b")
)
# Malaysia
flags["my"] = svg(
    rect(0, 0, 60, 40, "#fff")
    + "".join(rect(0, i * (40 / 14), 60, 40 / 14, "#cc0000") for i in range(0, 14, 2))
    + rect(0, 0, 28, 20, "#010066")
    + '<circle cx="14" cy="10" r="6" fill="#ffcc00"/>'
    + '<circle cx="16.4" cy="10" r="5" fill="#010066"/>'
    + star(20, 10, 3.6, "#ffcc00", n=14, rot=-90)
)
# Kuwait
flags["kw"] = svg(
    rect(0, 0, 60, 40 / 3, "#007a3d")
    + rect(0, 40 / 3, 60, 40 / 3, "#fff")
    + rect(0, 80 / 3, 60, 40 / 3, "#ce1126")
    + '<polygon points="0,0 18,13.3 18,26.7 0,40" fill="#000"/>'
)

assert len(flags) == 48, len(flags)

for code, markup in flags.items():
    (OUT / f"{code}.svg").write_text(markup)

print(f"Wrote {len(flags)} flags to {OUT}")
