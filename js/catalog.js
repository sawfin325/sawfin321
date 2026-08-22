const PAGE_SIZE = 48;
const CONDITIONS = ["New", "New", "Used (Mint)", "Used (Very good)", "Used (Very good)", "Used (Good)", "Used (Fair)"];

function catalogHash(n, salt) {
  let x = Math.imul(n + 1, 0x9e3779b1) ^ salt;
  x = Math.imul(x ^ (x >>> 16), 0x85ebca6b);
  x = Math.imul(x ^ (x >>> 13), 0xc2b2ae35);
  return (x ^ (x >>> 16)) >>> 0;
}

function brandIndex(name) {
  return BRANDS.findIndex((b) => b.name === name);
}

function makeListing(brand, n) {
  const seeds = SEEDS_BY_BRAND[brand];
  if (!seeds || !seeds.length) return null;
  const seed = seeds[n % seeds.length];
  const h = catalogHash(n, brandIndex(brand) + 17);
  const seller = SELLERS[h % SELLERS.length];
  const year = Math.min(2026, Math.max(1988, (seed.year || 2020) - (h % 22)));
  const condition = CONDITIONS[h % CONDITIONS.length];
  const box = h % 5 !== 2;
  const papers = h % 4 !== 1;
  const price = Math.max(199, Math.round(seed.price * (0.72 + (h % 8000) / 8000 * 0.9) / 5) * 5);
  const cats = seed.cats.slice();
  if (year <= 2010 && !cats.includes("vintage")) cats.push("vintage");
  if (condition.startsWith("Used") && !cats.includes("preowned")) cats.push("preowned");
  if (/automatic/i.test(seed.movement) && !cats.includes("automatic")) cats.push("automatic");
  const bi = brandIndex(brand);
  const gallery = galleryPaths(brand, seed.model);
  return {
    id: `w-${bi}-${n}`,
    brand,
    model: seed.model,
    ref: seed.ref,
    year,
    price,
    image: gallery[n % 8],
    images: gallery,
    cats,
    movement: seed.movement,
    case: seed.case,
    condition,
    box,
    papers,
    seller,
    location: seller.loc,
    views: 80 + (h % 4200),
    description: `A ${condition.toLowerCase()} ${brand} ${seed.model} (ref. ${seed.ref}) from ${year}. ${seed.case}. ${seed.movement} movement. ${box ? "Original box included." : "No box."} ${papers ? "Papers included." : "No papers."} Ships worldwide with insured courier and Buyer Protection.`,
  };
}

function getWatchById(id) {
  const m = /^w-(\d+)-(\d+)$/.exec(id || "");
  if (!m) return WATCHES.find((w) => w.id === id) || null;
  const brand = BRANDS[Number(m[1])]?.name;
  if (!brand) return null;
  return makeListing(brand, Number(m[2]));
}

function listingMatches(brand, n, filters) {
  const seeds = SEEDS_BY_BRAND[brand];
  const seed = seeds[n % seeds.length];
  const q = filters.q;
  if (q && !`${brand} ${seed.model} ${seed.ref}`.toLowerCase().includes(q)) return false;
  const h = catalogHash(n, brandIndex(brand) + 17);
  const year = Math.min(2026, Math.max(1988, (seed.year || 2020) - (h % 22)));
  const condition = CONDITIONS[h % CONDITIONS.length];
  const price = Math.max(199, Math.round(seed.price * (0.72 + (h % 8000) / 8000 * 0.9) / 5) * 5);
  const cat = filters.cat;
  if (cat === "preowned" && !condition.startsWith("Used")) return false;
  if (cat === "vintage" && year > 2010) return false;
  if (cat && cat !== "preowned" && cat !== "vintage" && !(seed.cats || []).includes(cat)) return false;
  if (filters.min && price < filters.min) return false;
  if (filters.max && price > filters.max) return false;
  if (filters.sort === "new") { /* used only in collect */ }
  return { price, year };
}

function queryCatalog() {
  const p = params();
  const filters = {
    q: (p.get("q") || "").trim().toLowerCase(),
    brand: p.get("brand") || "",
    cat: p.get("cat") || "",
    min: Number(p.get("min") || 0),
    max: Number(p.get("max") || 0),
    sort: p.get("sort") || "popular",
  };
  const page = Math.max(1, Number(p.get("page") || 1));
  const brands = filters.brand ? BRANDS.filter((b) => b.name === filters.brand) : BRANDS;
  const simple = !filters.q && !filters.cat && !filters.min && !filters.max && filters.sort === "popular";
  const start = (page - 1) * PAGE_SIZE;
  const items = [];
  let total = 0;

  if (simple) {
    for (const b of brands) {
      if (!SEEDS_BY_BRAND[b.name]) continue;
      const count = b.count;
      const overlapStart = Math.max(0, start - total);
      const overlapEnd = Math.min(count, start + PAGE_SIZE - total);
      if (overlapEnd > overlapStart) {
        for (let n = overlapStart; n < overlapEnd && items.length < PAGE_SIZE; n++) {
          items.push(makeListing(b.name, n));
        }
      }
      total += count;
    }
  } else {
  const ranked = (filters.brand || filters.q) && (filters.sort === "price-asc" || filters.sort === "price-desc" || filters.sort === "new");
    const bag = ranked ? [] : null;
    for (const b of brands) {
      if (!SEEDS_BY_BRAND[b.name]) continue;
      for (let n = 0; n < b.count; n++) {
        const hit = listingMatches(b.name, n, filters);
        if (!hit) continue;
        if (ranked) bag.push({ brand: b.name, n, price: hit.price, year: hit.year });
        else {
          if (total >= start && items.length < PAGE_SIZE) items.push(makeListing(b.name, n));
          total++;
        }
      }
    }
    if (ranked) {
      if (filters.sort === "price-asc") bag.sort((a, b) => a.price - b.price);
      if (filters.sort === "price-desc") bag.sort((a, b) => b.price - a.price);
      if (filters.sort === "new") bag.sort((a, b) => b.year - a.year);
      total = bag.length;
      for (const row of bag.slice(start, start + PAGE_SIZE)) items.push(makeListing(row.brand, row.n));
    }
  }

  return {
    total,
    items,
    page,
    pageSize: PAGE_SIZE,
    pages: Math.max(1, Math.ceil(total / PAGE_SIZE)),
    filters,
  };
}

function pagerQuery(page) {
  const p = new URLSearchParams(location.search);
  if (page <= 1) p.delete("page");
  else p.set("page", String(page));
  const q = p.toString();
  return q ? `search.html?${q}` : "search.html";
}
