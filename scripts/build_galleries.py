#!/usr/bin/env python3
"""Build an 8-angle gallery for every unique brand+model."""
from __future__ import annotations

import math
import os
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

ROOT = Path("/workspace")
OUT = ROOT / "assets" / "watches" / "galleries"
ART = Path("/opt/cursor/artifacts/assets")
EXISTING = ROOT / "assets" / "watches"
SIZE = 900

# Real 8-angle packs that should not be overwritten by derived views.
KEEP_PACKS = {
    "gauri-lotus",
    "gauri-tikka",
    "gauri-saffron-chronograph",
    "gauri-midnight",
    "gauri-heritage-moon",
    "rolex-yacht-master-40",
    "rolex-sea-dweller",
    "seiko-prospex-diver",
    "rolex-submariner-date",
    "rolex-daytona",
    "rolex-datejust-36",
    "rolex-gmt-master-ii",
}

# Unique hero photo per model. Never reuse one file across two models.
SOURCES = {
    "rolex-submariner-date": ART / "rolex-sub-01.jpg",
    "rolex-daytona": ART / "rolex-daytona-01.jpg",
    "rolex-datejust-36": ART / "rolex-dj-01.jpg",
    "rolex-gmt-master-ii": ART / "rolex-gmt-01.jpg",
    "rolex-day-date-40": EXISTING / "watch-daydate.jpg",
    "rolex-lady-datejust": ART / "rolex-lady-dj-01.jpg",
    "rolex-explorer-ii": ART / "rolex-explorer2-01.jpg",
    "rolex-yacht-master-40": ART / "rolex-ym-01.jpg",
    "rolex-oyster-perpetual-36": ART / "rolex-op36-01.jpg",
    "rolex-sea-dweller": ART / "rolex-sd-01.jpg",
    "rolex-sky-dweller": ART / "rolex-skydweller-01.jpg",
    "omega-speedmaster-professional": ART / "omega-speedy-01.jpg",
    "omega-seamaster-diver-300m": ART / "omega-seamaster-01.jpg",
    "omega-speedmaster-reduced": ART / "omega-reduced-01.jpg",
    "omega-constellation": ART / "omega-constellation-01.jpg",
    "omega-planet-ocean": ART / "omega-po-01.jpg",
    "omega-de-ville-prestige": ART / "omega-deville-01.jpg",
    "audemars-piguet-royal-oak": EXISTING / "watch-royal-oak.jpg",
    "audemars-piguet-royal-oak-offshore": ART / "ap-offshore-01.jpg",
    "patek-philippe-nautilus": EXISTING / "watch-nautilus.jpg",
    "patek-philippe-calatrava": EXISTING / "watch-gold.jpg",
    "patek-philippe-aquanaut": ART / "patek-aquanaut-01.jpg",
    "patek-philippe-grand-complications": ART / "patek-grand-01.jpg",
    "patek-philippe-hunter-pocket-watch": EXISTING / "watch-pocket.jpg",
    "cartier-santos-de-cartier": ART / "cartier-santos-01.jpg",
    "cartier-tank-louis": ART / "cartier-tank-01.jpg",
    "cartier-ballon-bleu": ART / "cartier-ballon-01.jpg",
    "breitling-navitimer-b01": EXISTING / "watch-navitimer.jpg",
    "breitling-superocean-heritage": ART / "breitling-soh-01.jpg",
    "tudor-black-bay": EXISTING / "watch-tudor.jpg",
    "tudor-black-bay-fifty-eight": ART / "tudor-bb58-01.jpg",
    "panerai-luminor-marina": EXISTING / "watch-panerai.jpg",
    "panerai-radiomir": ART / "panerai-radiomir-01.jpg",
    "iwc-pilot-s-watch-mark-xviii": EXISTING / "watch-pilot.jpg",
    "iwc-portugieser-chronograph": ART / "iwc-portugieser-01.jpg",
    "jaeger-lecoultre-master-ultra-thin-moon": EXISTING / "watch-moonphase.jpg",
    "jaeger-lecoultre-reverso-classic": ART / "jlc-reverso-01.jpg",
    "hublot-classic-fusion": ART / "hublot-fusion-01.jpg",
    "hublot-big-bang-unico": ART / "hublot-bigbang-01.jpg",
    "seiko-prospex-diver": ART / "seiko-prospex-01.jpg",
    "seiko-presage-cocktail-time": ART / "seiko-presage-01.jpg",
    "grand-seiko-snowflake": ART / "gs-snowflake-01.jpg",
    "tag-heuer-carrera-chronograph": ART / "tag-carrera-01.jpg",
    "longines-hydroconquest": ART / "longines-hydro-01.jpg",
    "zenith-chronomaster-sport": ART / "zenith-chrono-01.jpg",
    "vacheron-constantin-overseas": ART / "vc-overseas-01.jpg",
    "a-lange-s-hne-saxonia-moon-phase": ART / "als-saxonia-01.jpg",
    "a-lange-s-hne-open-face-pocket-watch": ART / "als-pocket-01.jpg",
    "tissot-prx-powermatic-80": ART / "tissot-prx-01.jpg",
    "nomos-tangente": ART / "nomos-tangente-01.jpg",
    "nomos-club-sport": ART / "nomos-club-01.jpg",
    "breguet-classique": ART / "breguet-classique-01.jpg",
    "breguet-type-xx": ART / "breguet-typexx-01.jpg",
    "hamilton-khaki-field": ART / "hamilton-khaki-01.jpg",
    "hamilton-jazzmaster": ART / "hamilton-jazz-01.jpg",
    "oris-aquis-date": ART / "oris-aquis-01.jpg",
    "oris-big-crown-pointer-date": ART / "oris-pointer-01.jpg",
    "richard-mille-rm-011": ART / "rm-011-01.jpg",
    "richard-mille-rm-035": ART / "rm-035-01.jpg",
    "ulysse-nardin-marine-diver": ART / "un-marine-01.jpg",
    "ulysse-nardin-blast": ART / "un-blast-01.jpg",
    "sinn-856-utc": ART / "sinn-856-01.jpg",
    "sinn-104-st-sa-i": ART / "sinn-104-01.jpg",
    "gauri-lotus": EXISTING / "galleries/gauri-lotus/01.jpg",
    "gauri-tikka": EXISTING / "galleries/gauri-tikka/01.jpg",
    "gauri-saffron-chronograph": EXISTING / "gauri-saffron.jpg",
    "gauri-midnight": EXISTING / "gauri-midnight.jpg",
    "gauri-heritage-moon": EXISTING / "gauri-heritage.jpg",
    "gauri-temple": EXISTING / "gauri-temple.jpg",
    "gauri-pearl": EXISTING / "gauri-pearl.jpg",
    "gauri-royale-diver": EXISTING / "gauri-royale.jpg",
    "gauri-lotus-skeleton": ART / "gauri-skeleton-01.jpg",
    "gauri-maang": ART / "gauri-maang-01.jpg",
    "gauri-midnight-gmt": ART / "gauri-midnight-gmt-01.jpg",
}

# Optional real extra-angle files named {slug}-02.jpg … {slug}-08.jpg in ART.
ANGLE_PREFIX = {
    "rolex-submariner-date": "rolex-sub",
    "gauri-lotus": "gauri-lotus",
    "gauri-tikka": "gauri-tikka",
    "rolex-datejust-36": "rolex-dj",
    "rolex-gmt-master-ii": "rolex-gmt",
    "rolex-daytona": "rolex-daytona",
    "gauri-saffron-chronograph": "gauri-saffron",
    "gauri-midnight": "gauri-midnight",
    "gauri-heritage-moon": "gauri-heritage",
    "rolex-yacht-master-40": "rolex-ym",
    "rolex-sea-dweller": "rolex-sd",
    "seiko-prospex-diver": "seiko-prospex",
}


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def parse_models() -> list[tuple[str, str, str]]:
    text = (ROOT / "js" / "data.js").read_text()
    block = re.search(r"const SEED = \[(.*?)\];", text, re.S).group(1)
    rows = []
    seen = set()
    for m in re.finditer(r'brand: "([^"]+)", model: "([^"]+)"', block):
        brand, model = m.group(1), m.group(2)
        slug = slugify(f"{brand}-{model}")
        if slug in seen:
            continue
        seen.add(slug)
        rows.append((brand, model, slug))
    return rows


def square(im: Image.Image, bg=(248, 247, 244)) -> Image.Image:
    im = im.convert("RGB")
    w, h = im.size
    side = max(w, h)
    canvas = Image.new("RGB", (side, side), bg)
    canvas.paste(im, ((side - w) // 2, (side - h) // 2))
    return canvas.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def perspective(im: Image.Image, left: bool) -> Image.Image:
    w, h = im.size
    inset = int(w * 0.18)
    drop = int(h * 0.10)
    if left:
        dest = [(inset, drop), (w, 0), (w, h), (inset, h - drop)]
    else:
        dest = [(0, 0), (w - inset, drop), (w - inset, h - drop), (0, h)]
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    coeffs = _find_coeffs(src, dest)
    warped = im.transform((w, h), Image.Transform.PERSPECTIVE, coeffs, Image.Resampling.BICUBIC, fillcolor=(248, 247, 244))
    return square(warped)


def _find_coeffs(source, target):
    matrix = []
    for s, t in zip(source, target):
        matrix.append([t[0], t[1], 1, 0, 0, 0, -s[0] * t[0], -s[0] * t[1]])
        matrix.append([0, 0, 0, t[0], t[1], 1, -s[1] * t[0], -s[1] * t[1]])
    A = []
    B = []
    for row, s in zip(matrix, [c for p in source for c in p]):
        A.append(row)
        B.append(s)
    # Gaussian elimination for 8 unknowns
    n = 8
    M = [A[i][:] + [B[i]] for i in range(n)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        div = M[i][i] or 1e-9
        for j in range(i, n + 1):
            M[i][j] /= div
        for r in range(n):
            if r == i:
                continue
            f = M[r][i]
            for j in range(i, n + 1):
                M[r][j] -= f * M[i][j]
    return [M[i][n] for i in range(n)]


def side_profile(im: Image.Image) -> Image.Image:
    squeezed = im.resize((int(SIZE * 0.38), SIZE), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (SIZE, SIZE), (248, 247, 244))
    canvas.paste(squeezed, ((SIZE - squeezed.size[0]) // 2, 0))
    return ImageEnhance.Contrast(canvas).enhance(1.15)


def caseback(im: Image.Image, brand: str, model: str) -> Image.Image:
    """Studio caseback: unique metal disc, not a copy of another product."""
    seed = sum(ord(c) for c in brand + model)
    metal = [
        (196, 196, 196),
        (212, 175, 55),
        (203, 164, 122),
        (168, 172, 176),
        (120, 90, 50),
    ][seed % 5]
    bg = Image.new("RGB", (SIZE, SIZE), (248, 247, 244))
    draw = ImageDraw.Draw(bg)
    cx = cy = SIZE // 2
    r = 340
    draw.ellipse((cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8), fill=(90, 90, 90))
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=metal)
    inner = r - 48
    draw.ellipse((cx - inner, cy - inner, cx + inner, cy + inner), outline=(70, 70, 70), width=3)
    # Keep a ghost of the dial so it still reads as the same watch, flipped.
    ghost = ImageOps.mirror(im).resize((int(inner * 1.35), int(inner * 1.35)))
    ghost = ImageEnhance.Brightness(ghost).enhance(0.55)
    ghost = ImageEnhance.Color(ghost).enhance(0.15)
    mask = Image.new("L", ghost.size, 0)
    md = ImageDraw.Draw(mask)
    md.ellipse((8, 8, ghost.size[0] - 8, ghost.size[1] - 8), fill=180)
    bg.paste(ghost, (cx - ghost.size[0] // 2, cy - ghost.size[1] // 2), mask)
    draw = ImageDraw.Draw(bg)
    label = f"{brand.upper()}\n{model.upper()}"
    draw.ellipse((cx - 90, cy - 90, cx + 90, cy + 90), fill=(40, 40, 40))
    return bg


def wrist_shot(im: Image.Image, seed: int) -> Image.Image:
    skin = [(224, 186, 154), (196, 148, 112), (238, 207, 178), (168, 118, 82)][seed % 4]
    canvas = Image.new("RGB", (SIZE, SIZE), (236, 232, 226))
    draw = ImageDraw.Draw(canvas)
    # forearm band
    draw.rectangle((0, 340, SIZE, 620), fill=skin)
    draw.ellipse((-80, 300, 160, 680), fill=tuple(max(0, c - 18) for c in skin))
    watch = im.resize((520, 520), Image.Resampling.LANCZOS)
    canvas.paste(watch, ((SIZE - 520) // 2, (SIZE - 520) // 2 - 20))
    return canvas


def macro_dial(im: Image.Image) -> Image.Image:
    crop = im.crop((180, 140, 720, 680)).resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    return ImageEnhance.Sharpness(crop).enhance(1.4)


def clasp_crop(im: Image.Image) -> Image.Image:
    crop = im.crop((220, 480, 680, 900))
    crop = crop.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    crop = ImageEnhance.Contrast(crop).enhance(1.1)
    return crop


def compress(path: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
            "-vf", f"scale={SIZE}:{SIZE}:force_original_aspect_ratio=increase,crop={SIZE}:{SIZE}",
            "-q:v", "3", str(path.with_suffix(".tmp.jpg")),
        ],
        check=False,
    )
    tmp = path.with_suffix(".tmp.jpg")
    if tmp.exists():
        tmp.replace(path)


def save(im: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(dest, "JPEG", quality=88, optimize=True)


def copy_real_pack(slug: str, dest: Path) -> bool:
    prefix = ANGLE_PREFIX.get(slug)
    if not prefix:
        return False
    files = []
    for i in range(1, 9):
        p = ART / f"{prefix}-{i:02d}.jpg"
        if not p.exists() and i == 1 and slug in SOURCES:
            p = Path(SOURCES[slug])
        files.append(p)
    if not all(p.exists() for p in files):
        gallery_files = [EXISTING / "galleries" / slug / f"{i:02d}.jpg" for i in range(1, 9)]
        if all(p.exists() for p in gallery_files) and slug in KEEP_PACKS:
            return True
        return False
    dest.mkdir(parents=True, exist_ok=True)
    for i, src in enumerate(files, 1):
        im = square(Image.open(src))
        save(im, dest / f"{i:02d}.jpg")
        compress(dest / f"{i:02d}.jpg")
    return True


def build_derived(slug: str, brand: str, model: str, src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    hero = square(Image.open(src))
    seed = sum(ord(c) for c in slug)
    views = [
        hero,
        perspective(hero, True),
        perspective(hero, False),
        side_profile(hero),
        caseback(hero, brand, model),
        wrist_shot(hero, seed),
        macro_dial(hero),
        clasp_crop(hero),
    ]
    for i, im in enumerate(views, 1):
        save(im, dest / f"{i:02d}.jpg")
        compress(dest / f"{i:02d}.jpg")


def main() -> None:
    models = parse_models()
    missing = []
    for brand, model, slug in models:
        dest = OUT / slug
        src = SOURCES.get(slug)
        if src is None or not Path(src).exists():
            missing.append(slug)
            continue
        if copy_real_pack(slug, dest):
            print(f"real  {slug}")
            continue
        build_derived(slug, brand, model, Path(src), dest)
        print(f"built {slug}")
    if missing:
        print("MISSING SOURCES:")
        for s in missing:
            print(" ", s)
        raise SystemExit(1)
    print(f"ok {len(models)} galleries")


if __name__ == "__main__":
    main()
