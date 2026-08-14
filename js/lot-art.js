/** Unique warehouse lot artwork from a product slug. No two slugs share a design. */
const LOT_ART_CACHE = new Map();

function lotHash(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}
function lotRng(seed) {
  return function () {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function lotHsl(h, s, l) {
  return `hsl(${Math.round(h)} ${Math.round(s)}% ${Math.round(l)}%)`;
}

function lotArtUrl(slug, category) {
  const key = slug + "|" + (category || "");
  if (LOT_ART_CACHE.has(key)) return LOT_ART_CACHE.get(key);
  const rnd = lotRng(lotHash(key));
  const n = (a, b) => a + rnd() * (b - a);
  const pick = arr => arr[Math.floor(rnd() * arr.length)];
  const layout = Math.floor(rnd() * 6);
  const wall = lotHsl(n(0, 360), n(6, 42), n(14, 36));
  const wall2 = lotHsl(n(0, 360), n(8, 40), n(22, 48));
  const floor = lotHsl(n(20, 50), n(6, 22), n(38, 62));
  const wood = lotHsl(n(18, 40), n(28, 55), n(28, 48));
  const wrap = `rgba(220,235,255,${(0.18 + rnd() * 0.28).toFixed(2)})`;
  const accent = lotHsl(n(0, 360), n(55, 85), n(38, 58));
  const lotNo = String(10000 + (lotHash(slug) % 90000));
  const boxCount = 5 + Math.floor(rnd() * 16);
  let boxes = "";
  for (let i = 0; i < boxCount; i++) {
    const bw = n(28, 92);
    const bh = n(22, 88);
    const bx = n(24, 360 - bw);
    const by = n(70, 330 - bh);
    const fill = lotHsl(n(0, 360), n(25, 80), n(28, 78));
    const stroke = lotHsl(n(0, 360), n(10, 40), n(10, 30));
    const rx = rnd() > 0.7 ? n(2, 8) : 0;
    boxes += `<rect x="${bx.toFixed(1)}" y="${by.toFixed(1)}" width="${bw.toFixed(1)}" height="${bh.toFixed(1)}" rx="${rx.toFixed(1)}" fill="${fill}" stroke="${stroke}" stroke-width="${n(0.6, 2.2).toFixed(1)}"/>`;
    if (rnd() > 0.55) {
      boxes += `<rect x="${(bx + 4).toFixed(1)}" y="${(by + 4).toFixed(1)}" width="${Math.max(8, bw - 8).toFixed(1)}" height="${n(4, 14).toFixed(1)}" fill="rgba(255,255,255,0.28)"/>`;
    }
  }
  let extra = "";
  if (layout === 1) {
    extra = `<rect x="${n(40, 90)}" y="${n(90, 140)}" width="${n(90, 140)}" height="${n(120, 180)}" fill="${lotHsl(n(20, 40), n(20, 40), n(40, 60))}" stroke="#222" stroke-width="3"/>
      <rect x="${n(200, 250)}" y="${n(80, 130)}" width="${n(90, 140)}" height="${n(130, 190)}" fill="${lotHsl(n(180, 220), n(15, 35), n(35, 55))}" stroke="#222" stroke-width="3"/>`;
  } else if (layout === 2) {
    extra = `<ellipse cx="${n(170, 230)}" cy="${n(210, 250)}" rx="${n(90, 130)}" ry="${n(70, 100)}" fill="${lotHsl(n(25, 40), n(30, 50), n(42, 58))}" stroke="#333" stroke-width="3"/>`;
  } else if (layout === 3) {
    extra = `<polygon points="${n(40, 80)},${n(300, 340)} ${n(160, 200)},${n(80, 120)} ${n(320, 360)},${n(300, 340)}" fill="${accent}" opacity="0.35"/>`;
  } else if (layout === 4) {
    extra = `<rect x="0" y="${n(40, 90)}" width="400" height="${n(18, 40)}" fill="${accent}"/>
      <rect x="${pick([0, 360])}" y="0" width="${n(18, 36)}" height="400" fill="${lotHsl(n(0, 360), n(40, 70), n(20, 40))}"/>`;
  } else if (layout === 5) {
    for (let t = 0; t < 3 + Math.floor(rnd() * 3); t++) {
      extra += `<rect x="${(30 + t * n(70, 95)).toFixed(1)}" y="${n(150, 200).toFixed(1)}" width="${n(50, 80).toFixed(1)}" height="${n(90, 140).toFixed(1)}" fill="${lotHsl(n(0, 360), n(20, 60), n(30, 70))}" stroke="#111" stroke-width="2"/>`;
    }
  }
  const slats = [0, 1, 2, 3, 4].map(i => {
    const y = 318 + i * 10;
    return `<rect x="28" y="${y}" width="344" height="7" fill="${wood}" opacity="${(0.55 + i * 0.08).toFixed(2)}"/>`;
  }).join("");
  const lights = `<circle cx="${n(80, 160)}" cy="${n(20, 50)}" r="${n(18, 40)}" fill="rgba(255,240,180,${n(0.15, 0.45).toFixed(2)})"/>
    <circle cx="${n(240, 340)}" cy="${n(18, 60)}" r="${n(12, 36)}" fill="rgba(255,255,255,${n(0.08, 0.3).toFixed(2)})"/>`;
  const cat = (category || "lot").replace(/[^a-z0-9 ]/gi, "").slice(0, 22).toUpperCase();
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
    <defs>
      <linearGradient id="g${lotNo}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="${wall}"/>
        <stop offset="1" stop-color="${wall2}"/>
      </linearGradient>
    </defs>
    <rect width="400" height="400" fill="url(#g${lotNo})"/>
    <rect x="0" y="300" width="400" height="100" fill="${floor}"/>
    ${lights}
    ${extra}
    ${slats}
    <rect x="22" y="312" width="356" height="14" fill="${wood}"/>
    ${boxes}
    <rect x="30" y="70" width="340" height="250" fill="${wrap}" pointer-events="none"/>
    <path d="M40 80 L360 90 L350 310 L50 300 Z" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="${n(1, 4).toFixed(1)}"/>
    <rect x="${n(8, 24)}" y="${n(8, 24)}" width="${n(120, 190)}" height="44" fill="#111"/>
    <text x="${n(16, 36)}" y="${n(36, 48)}" fill="#fff" font-family="Lato,Arial,sans-serif" font-size="15" font-weight="700">LOT ${lotNo}</text>
    <rect x="0" y="368" width="400" height="32" fill="rgba(0,0,0,0.72)"/>
    <text x="12" y="389" fill="#eee" font-family="Lato,Arial,sans-serif" font-size="11">${cat}</text>
  </svg>`;
  const url = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
  LOT_ART_CACHE.set(key, url);
  return url;
}

function applyLotArt(root) {
  (root || document).querySelectorAll("img[data-lot]").forEach(img => {
    img.src = lotArtUrl(img.dataset.lot, img.dataset.cat || "");
  });
}
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => applyLotArt());
} else {
  applyLotArt();
}
