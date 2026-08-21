function $(sel, root = document) { return root.querySelector(sel); }
function $all(sel, root = document) { return [...root.querySelectorAll(sel)]; }
function money(n) {
  return new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(n);
}
function params() { return new URLSearchParams(location.search); }

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

function purchaseMessage(w) {
  return `Hello, I want to purchase ${w.brand} ${w.model} (ref. ${w.ref}, listing ${w.id}) listed at ${money(w.price)}. Please confirm availability and send payment instructions.`;
}

function whatsappBuyHref(w) {
  return `${CONTACT.whatsapp}?text=${encodeURIComponent(purchaseMessage(w))}`;
}

function emailBuyHref(w) {
  const subject = `Purchase inquiry: ${w.brand} ${w.model} ${w.ref}`;
  return `mailto:${CONTACT.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(purchaseMessage(w))}`;
}

function openPurchasePrompt(w) {
  let el = $("#buy-prompt");
  if (!el) {
    el = document.createElement("div");
    el.id = "buy-prompt";
    el.className = "buy-prompt";
    document.body.appendChild(el);
  }
  const title = w ? `${w.brand} ${w.model}` : "this watch";
  const wa = w ? whatsappBuyHref(w) : CONTACT.whatsapp;
  const mail = w ? emailBuyHref(w) : `mailto:${CONTACT.email}`;
  el.innerHTML = `
    <div class="buy-prompt-card">
      <button class="buy-prompt-close" type="button" aria-label="Close">&times;</button>
      <h3>Purchase ${title}</h3>
      <p>Complete this order by WhatsApp or email. We will confirm availability and send payment instructions. No card is charged on this page.</p>
      <a class="btn btn-block" href="${wa}" target="_blank" rel="noopener">Continue on WhatsApp</a>
      <a class="btn btn-outline btn-block" href="${mail}">Email ${CONTACT.email}</a>
      <p class="buy-prompt-phone">Or call <a href="${CONTACT.tel}">${CONTACT.phone}</a></p>
    </div>`;
  el.classList.add("open");
  el.querySelector(".buy-prompt-close").onclick = () => el.classList.remove("open");
  el.onclick = (e) => { if (e.target === el) el.classList.remove("open"); };
}

function toast(msg) {
  let el = $(".toast");
  if (!el) {
    el = document.createElement("div");
    el.className = "toast";
    el.id = "toast";
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.style.display = "block";
  clearTimeout(toast._t);
  toast._t = setTimeout(() => { el.style.display = "none"; }, 2200);
}

function favs() { return JSON.parse(localStorage.getItem("meridian-favs") || "[]"); }
function toggleFav(id) {
  const set = new Set(favs());
  if (set.has(id)) set.delete(id); else set.add(id);
  localStorage.setItem("meridian-favs", JSON.stringify([...set]));
  return set.has(id);
}
function currentUser() { return JSON.parse(localStorage.getItem("meridian-user") || "null"); }

function iconUser() {
  return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="3.2"/><path d="M5 19c1.6-3.2 4.2-4.8 7-4.8S17.4 15.8 19 19"/></svg>`;
}
function iconSearch() {
  return `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.2-3.2"/></svg>`;
}

function headerHTML() {
  const user = currentUser();
  const account = user
    ? `<a class="header-account" href="account.html">${iconUser()}<span>${user.name}</span></a>`
    : `<a class="header-account" href="login.html">${iconUser()}<span>Log in or register</span></a>`;
  const left = MENU_BRANDS_LEFT.map((name) =>
    `<a class="row${name === "Gauri" ? " featured" : ""}" href="search.html?brand=${encodeURIComponent(name)}">${name}</a>`
  ).join("");
  const right = MENU_BRANDS_RIGHT.map((name) =>
    `<a class="row" href="search.html?brand=${encodeURIComponent(name)}">${name}</a>`
  ).join("");
  const cats = MENU_CATEGORIES.map((c) =>
    `<a class="row" href="search.html?cat=${encodeURIComponent(c.slug)}">${c.name}</a>`
  ).join("");
  return `
  <div class="promo">Have you tried the Chrono24 app? <a href="apps.html">Discover now</a></div>
  <header class="header">
    <div class="wrap header-row">
      <button class="menu-btn" type="button" aria-label="Menu" data-menu>☰</button>
      <a class="logo" href="index.html">chrono24</a>
      <form class="search" action="search.html" method="get">
        <input name="q" type="search" placeholder="Search through ${SITE.listingCount} watches worldwide" value="${params().get("q") || ""}" />
        <button type="submit" aria-label="Search">${iconSearch()}</button>
      </form>
      ${account}
    </div>
    <nav class="nav wrap" id="main-nav">
      <div class="nav-item has-mega">
        <a class="nav-link" href="search.html">Buy a watch <span class="caret">▾</span></a>
        <div class="mega">
          <div class="wrap mega-grid">
            <div>
              <h4>Brands</h4>
              <div class="mega-brands">
                <div>${left}</div>
                <div>${right}</div>
              </div>
              <a class="more" href="brands.html">Display all</a>
            </div>
            <div>
              <h4>Categories</h4>
              ${cats}
              <a class="more" href="search.html">Display all</a>
            </div>
            <div>
              <h4>Services</h4>
              <a class="row" href="collection.html">Watch Collection</a>
              <a class="row" href="sell.html">Appraisal</a>
              <a class="row" href="search.html">Advanced Search</a>
              <a class="mega-card" href="search.html?brand=Gauri">
                <img src="assets/lifestyle/hero-bestsellers.jpg" alt="Top models">
                <div class="cap">
                  <span style="opacity:.8;font-size:12px">On the wrists of watch enthusiasts.</span>
                  <strong>TOP MODELS ON CHRONO24.</strong>
                  <span class="btn btn-light">Discover now</span>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link" href="sell.html">Sell a watch <span class="caret">▾</span></a>
        <div class="dropdown">
          <a href="sell.html">Start a listing</a>
          <a href="sell.html#how">How selling works</a>
          <a href="faq.html">Advice for private sellers</a>
        </div>
      </div>
      <a class="nav-link" href="deals.html">Best Deals</a>
      <a class="nav-link" href="magazine.html">Magazine</a>
      <a class="nav-link" href="collection.html">Watch Collection</a>
      <a class="nav-link" href="pulse.html">ChronoPulse</a>
      <a class="nav-link" href="faq.html">FAQ</a>
      <div class="nav-item">
        <a class="nav-link" href="security.html">Security <span class="caret">▾</span></a>
        <div class="dropdown">
          <a href="security.html">Buyer Protection</a>
          <a href="security.html#escrow">Escrow Service</a>
          <a href="security.html#authenticity">Commitment to Authenticity</a>
        </div>
      </div>
    </nav>
  </header>`;
}

function footerHTML() {
  const cols = [
    ["Buy on Chrono24", [["security.html","Buyer Protection"],["security.html#escrow","Payment via the Escrow Service"],["security.html#authenticity","Commitment to Authenticity"],["faq.html","Easy Returns"]]],
    ["Sell on Chrono24", [["sell.html","Selling as a Private Seller"],["sell.html","Selling Commercially"],["sell.html","Free Appraisal"],["faq.html","Advice for private sellers"]]],
    ["About Chrono24", [["about.html","About us"],["about.html","Jobs"],["about.html","Press"],["about.html","Legal Details"]]],
    ["Personalized support", [["faq.html","Frequently asked questions"],["contact.html","Contact"]]],
    ["Chrono24 Apps", [["apps.html","iOS App Store"],["apps.html","Google Play"]]],
    ["Payment methods", [["security.html","Visa · Mastercard · Amex"],["security.html","Wire transfer"],["security.html","Pay over time"]]],
  ];
  return `
  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div>
          <h4>Chrono24 Newsletter</h4>
          <p>Market stories, new listings, and collector notes — free.</p>
          <form class="search" style="max-width:360px;margin-top:10px" data-newsletter>
            <input type="email" required placeholder="Email address" />
            <button class="btn" type="submit" style="width:auto;padding:0 12px">Subscribe</button>
          </form>
        </div>
        <div>
          <h4>Settings</h4>
          <p>.COM · English · USD</p>
        </div>
        <div>
          <h4>Theme</h4>
          <p>System default</p>
        </div>
      </div>
      <div class="footer-cols">
        ${cols.map(([h, links]) => {
          if (h === "Personalized support") {
            return `<div><h4>${h}</h4><ul>${links.map(([href,t]) => `<li><a href="${href}">${t}</a></li>`).join("")}
              <li><a href="${CONTACT.tel}">${CONTACT.phone}</a></li>
              <li><a href="mailto:${CONTACT.email}">${CONTACT.email}</a></li>
              <li><a href="${CONTACT.whatsapp}" target="_blank" rel="noopener">WhatsApp</a></li>
            </ul></div>`;
          }
          if (h === "Payment methods") {
            return `<div><h4>${h}</h4>
              <div class="pay-pills"><span>VISA</span><span>Mastercard</span><span>AMEX</span><span>Wire transfer</span></div>
            </div>`;
          }
          return `<div><h4>${h}</h4><ul>${links.map(([href,t]) => `<li><a href="${href}">${t}</a></li>`).join("")}</ul></div>`;
        }).join("")}
      </div>
      <div class="countries">
        ${COUNTRIES.map((c) => `<a class="country" href="search.html"><img src="assets/flags/${c.code}.jpg" alt="" width="22" height="16">${c.name}</a>`).join("")}
      </div>
      <div class="legal">
        <div>
          <a href="about.html">Data Privacy Policy</a> ·
          <a href="about.html">Accessibility</a> ·
          <a href="about.html">Manage Cookies</a> ·
          <a href="about.html">Terms &amp; Conditions</a>
        </div>
        <div>© ${new Date().getFullYear()} Chrono24 demo recreation. Not affiliated with Chrono24 GmbH.</div>
      </div>
    </div>
  </footer>`;
}

function watchCard(w) {
  const on = favs().includes(w.id) ? " on" : "";
  const shots = (w.images && w.images.length) || 1;
  return `
  <article class="watch-card">
    <div class="media">
      <button class="heart${on}" type="button" data-fav="${w.id}" aria-label="Save">♥</button>
      <a href="listing.html?id=${encodeURIComponent(w.id)}"><img src="${w.image}" alt="${w.brand} ${w.model}" /></a>
      <span class="shot-count">${shots} photos</span>
    </div>
    <div class="watch-meta">
      <a href="listing.html?id=${encodeURIComponent(w.id)}">
        <div class="brand">${w.brand}</div>
        <div class="model">${w.model}</div>
        <div class="price">${money(w.price)}</div>
        <div class="loc">${w.location}</div>
      </a>
    </div>
  </article>`;
}

function filterWatches() {
  return queryCatalog().items;
}

function mountChrome() {
  const h = $("#site-header");
  const f = $("#site-footer");
  if (h) h.innerHTML = headerHTML();
  if (f) f.innerHTML = footerHTML();
  const menu = $("[data-menu]");
  if (menu) menu.addEventListener("click", () => $("#main-nav").classList.toggle("open"));
  document.body.addEventListener("click", (e) => {
    const buy = e.target.closest(".has-mega > .nav-link");
    if (buy && window.matchMedia("(max-width: 980px)").matches) {
      e.preventDefault();
      buy.parentElement.classList.toggle("open");
    }
  });
  document.body.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-fav]");
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();
    const on = toggleFav(btn.getAttribute("data-fav"));
    btn.classList.toggle("on", on);
    toast(on ? "Saved to your collection" : "Removed from collection");
  });
  const news = $("[data-newsletter]");
  if (news) news.addEventListener("submit", (e) => {
    e.preventDefault();
    toast("You are subscribed.");
    news.reset();
  });
}

function uniqueByModel(list) {
  const seen = new Set();
  return list.filter((w) => {
    const key = w.brand + w.model;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

function renderHome() {
  const brands = $("#popular-brands");
  if (brands) brands.innerHTML = BRANDS.slice(0, 10).map((b) =>
    `<a class="brand-card" href="search.html?brand=${encodeURIComponent(b.name)}">${b.name}</a>`
  ).join("");
  const explore = $("#explore-grid");
  if (explore) explore.innerHTML = CATEGORIES.map((c) =>
    `<a class="tile" href="search.html?cat=${c.slug}"><img src="${c.image}" alt=""><span>${c.name}</span></a>`
  ).join("");
  const gauri = $("#gauri-models");
  if (gauri) gauri.innerHTML = uniqueByModel(WATCHES.filter((w) => w.brand === "Gauri")).map(watchCard).join("");
  const popular = $("#popular-models");
  if (popular) popular.innerHTML = uniqueByModel(WATCHES).slice(0, 8).map(watchCard).join("");
  const links = $("#model-links");
  if (links) links.innerHTML = POPULAR_MODELS.map((m) =>
    `<a href="search.html?q=${encodeURIComponent(m)}">${m}</a>`
  ).join("");
  const reviews = $("#review-row");
  if (reviews) reviews.innerHTML = REVIEWS.slice(0, 3).map((r) =>
    `<article class="review"><div class="stars">★★★★★</div><p>“${r.text}”</p><div class="who"><div class="avatar">${r.name[0]}</div><div>${r.name}<br>${r.loc}</div></div></article>`
  ).join("");
  const mag = $("#magazine-grid");
  if (mag) mag.innerHTML = ARTICLES.map((a) =>
    `<a class="article" href="article.html?id=${a.id}"><img src="${a.image}" alt=""><div class="tag">${a.tag}</div><h3>${a.title}</h3><div class="byline">${a.author} · ${a.date} · ${a.read}</div></a>`
  ).join("");
  const ig = $("#ig-grid");
  if (ig) ig.innerHTML = INSTAGRAM.map((src) => `<img src="${src}" alt="Chrono24 on Instagram">`).join("");
  const vids = $("#video-grid");
  if (vids) vids.innerHTML = VIDEOS.map((v) =>
    `<article class="video"><div class="play">▶</div><img src="${v.image}" alt=""><h3>${v.title}</h3><p>${v.host} · ${v.time} · ${v.date}</p></article>`
  ).join("");
}

function renderSearch() {
  const grid = $("#results");
  if (!grid) return;
  const result = queryCatalog();
  const count = $("#result-count");
  const brand = params().get("brand") || "";
  const heading = $("#search-heading") || $(".page-head h1");
  if (heading) heading.textContent = brand ? `${brand} watches` : "Luxury watches";
  if (count) {
    count.textContent = `${result.total.toLocaleString()} listings`;
    if (brand) count.textContent += " including promoted listings";
  }
  document.title = brand ? `${brand} watches | Chrono24` : "Search luxury watches | Chrono24";
  grid.innerHTML = result.items.length ? result.items.map(watchCard).join("") : `<p>No watches matched those filters.</p>`;
  const pager = $("#pager");
  if (pager) {
    const pages = result.pages;
    const page = result.page;
    const links = [];
    if (page > 1) links.push(`<a href="${pagerQuery(page - 1)}">Previous</a>`);
    const from = Math.max(1, page - 2);
    const to = Math.min(pages, page + 2);
    for (let i = from; i <= to; i++) {
      links.push(i === page ? `<span class="on">${i}</span>` : `<a href="${pagerQuery(i)}">${i}</a>`);
    }
    if (page < pages) links.push(`<a href="${pagerQuery(page + 1)}">Next</a>`);
    pager.innerHTML = links.join("");
  }
  const featured = $("#featured-models");
  if (featured) {
    const models = FEATURED_MODELS[brand];
    if (models) {
      featured.innerHTML = models.map((m) =>
        `<a class="feat-card" href="search.html?brand=${encodeURIComponent(brand)}&q=${encodeURIComponent(m.model)}">
          <img src="${m.img}" alt="${brand} ${m.model}">
          <strong>${m.model}</strong>
          <span>from ${money(m.from)}</span>
        </a>`
      ).join("");
      featured.hidden = false;
    } else featured.hidden = true;
  }
  const chips = $("#filter-chips");
  if (chips && brand) {
    const items = [["Used", "cat=preowned"], ["New/Unworn", ""]];
    if (brand === "Rolex") items.push(["Datejust 36", "q=Datejust"]);
    chips.innerHTML = items.map(([label, extra]) => {
      const p = new URLSearchParams({ brand });
      extra.split("&").forEach((pair) => {
        if (!pair) return;
        const [k, v] = pair.split("=");
        if (k) p.set(k, decodeURIComponent(v || ""));
      });
      return `<a href="search.html?${p}">${label}</a>`;
    }).join("");
    chips.hidden = false;
  }
  const brandSel = $("#filter-brand");
  if (brandSel && !brandSel.options.length) {
    brandSel.innerHTML = `<option value="">All brands</option>` + BRANDS.map((b) =>
      `<option ${params().get("brand") === b.name ? "selected" : ""}>${b.name}</option>`
    ).join("");
  }
}

function renderListing() {
  const root = $("#listing");
  if (!root) return;
  const w = getWatchById(params().get("id")) || makeListing(BRANDS[0].name, 0);
  const n = Number((w.id.match(/-(\d+)$/) || ["", "0"])[1]);
  const similar = [1, 2, 3, 4].map((d) => makeListing(w.brand, n + d)).filter(Boolean);
  document.title = `${w.brand} ${w.model} | Chrono24`;
  root.innerHTML = `
    <div class="crumbs wrap"><a href="index.html">Home</a> / <a href="search.html?brand=${encodeURIComponent(w.brand)}">${w.brand} watches</a> / ${w.model}</div>
    <div class="product wrap">
      <div>
        <div class="gallery"><img id="main-photo" src="${(w.images && w.images[0]) || w.image}" alt="${w.brand} ${w.model}"></div>
        <div class="thumbs">${(w.images || [w.image]).map((src, i) => `<img class="${i === 0 ? "on" : ""}" src="${src}" alt="${w.brand} ${w.model} · photo ${i + 1}">`).join("")}</div>
      </div>
      <aside class="buybox">
        <div class="views">${w.views.toLocaleString()} views in 48 hours</div>
        <h1>${w.brand} ${w.model}</h1>
        <div class="sub">${w.ref} · ${w.case}</div>
        <span class="badge">${w.condition}</span>
        <span class="badge">${w.year}</span>
        <span class="badge">${w.box ? "With box" : "No box"}</span>
        <span class="badge">${w.papers ? "With papers" : "No papers"}</span>
        <div class="price-lg">${money(w.price)}</div>
        <p>Ships from ${w.location}. Insured worldwide shipping.</p>
        <button class="btn btn-block" data-buy>Buy</button>
        <p style="margin:10px 0 0;font-size:13px;color:var(--muted)">Purchase via WhatsApp or email · ${CONTACT.phone}</p>
        <div class="seller">
          <div>
            <strong>${w.seller.name}</strong><br>
            <span style="color:var(--star)">★ ${w.seller.rating}</span> · ${w.seller.reviews.toLocaleString()} reviews<br>
            <span class="sub">${w.seller.type}</span>
          </div>
          <a class="btn btn-outline" href="contact.html?seller=${encodeURIComponent(w.seller.name)}">Contact seller</a>
        </div>
      </aside>
    </div>
    <section class="specs wrap">
      <h2>Basic Info</h2>
      <table>
        <tr><th>Listing code</th><td>${w.id}</td></tr>
        <tr><th>Brand</th><td>${w.brand}</td></tr>
        <tr><th>Model</th><td>${w.model}</td></tr>
        <tr><th>Reference number</th><td>${w.ref}</td></tr>
        <tr><th>Movement</th><td>${w.movement}</td></tr>
        <tr><th>Case</th><td>${w.case}</td></tr>
        <tr><th>Year of production</th><td>${w.year}</td></tr>
        <tr><th>Condition</th><td>${w.condition}</td></tr>
        <tr><th>Scope of delivery</th><td>${[w.box ? "Original box" : null, w.papers ? "Original papers" : null].filter(Boolean).join(", ") || "Watch only"}</td></tr>
        <tr><th>Location</th><td>${w.location}</td></tr>
        <tr><th>Price</th><td>${money(w.price)}</td></tr>
      </table>
      <p style="margin-top:18px">${w.description}</p>
    </section>
    <section class="section wrap">
      <h2>Similar watches</h2>
      <div class="watch-grid">${similar.map(watchCard).join("")}</div>
    </section>`;
  $("[data-buy]")?.addEventListener("click", () => openPurchasePrompt(w));
  $all(".thumbs img", root).forEach((thumb) => {
    thumb.addEventListener("click", () => {
      const main = $("#main-photo");
      if (main) main.src = thumb.getAttribute("src");
      $all(".thumbs img", root).forEach((t) => t.classList.toggle("on", t === thumb));
    });
  });
}

function renderBrands() {
  const el = $("#brand-list");
  if (!el) return;
  el.innerHTML = BRANDS.map((b) =>
    `<a class="brand-card" href="search.html?brand=${encodeURIComponent(b.name)}">${b.name}<br><small style="font-weight:400;color:var(--muted)">${b.count.toLocaleString()} listings</small></a>`
  ).join("");
}

function renderMagazine() {
  const el = $("#magazine-list");
  if (!el) return;
  el.innerHTML = ARTICLES.map((a) =>
    `<a class="article" href="article.html?id=${a.id}"><img src="${a.image}" alt=""><div class="tag">${a.tag}</div><h3>${a.title}</h3><div class="byline">${a.author} · ${a.date} · ${a.read}</div></a>`
  ).join("");
}

function renderArticle() {
  const el = $("#article");
  if (!el) return;
  const a = ARTICLES.find((x) => x.id === params().get("id")) || ARTICLES[0];
  document.title = `${a.title} | Chrono24 Magazine`;
  el.innerHTML = `
    <div class="crumbs"><a href="index.html">Home</a> / <a href="magazine.html">Magazine</a> / ${a.tag}</div>
    <p class="tag">${a.tag}</p>
    <h1>${a.title}</h1>
    <p class="byline">${a.author} · ${a.date} · ${a.read}</p>
    <img src="${a.image}" alt="" style="width:100%;max-height:420px;object-fit:cover;margin:18px 0">
    <p style="font-size:18px;max-width:720px">${a.body}</p>
    <p style="max-width:720px;color:var(--muted)">Original magazine copy for this demo. Not copied from Chrono24 editorial.</p>`;
}

function renderCollection() {
  const el = $("#collection-grid");
  if (!el) return;
  const list = favs().map(getWatchById).filter(Boolean);
  el.innerHTML = list.length ? list.map(watchCard).join("") : `<p>Your collection is empty. Tap the heart on any listing to save it.</p>`;
}

function renderDeals() {
  const el = $("#deals-grid");
  if (!el) return;
  const cheap = BRANDS.filter((b) => ["Seiko", "Tissot", "Hamilton", "NOMOS", "Oris", "Longines"].includes(b.name));
  const list = [];
  for (const b of cheap) {
    for (let n = 0; n < 8; n++) list.push(makeListing(b.name, n));
  }
  list.sort((a, b) => a.price - b.price);
  el.innerHTML = list.slice(0, 16).map(watchCard).join("");
}

function renderPulse() {
  const el = $("#pulse-table");
  if (!el) return;
  el.innerHTML = uniqueByModel(WATCHES).slice(0, 16).map((w, i) => {
    const chg = ((i % 7) - 3) * 1.4;
    const color = chg >= 0 ? "var(--green)" : "var(--danger)";
    return `<tr><td>${w.brand} ${w.model}</td><td>${money(w.price)}</td><td style="color:${color}">${chg >= 0 ? "+" : ""}${chg.toFixed(1)}%</td><td>${w.views}</td></tr>`;
  }).join("");
}

document.addEventListener("DOMContentLoaded", () => {
  mountChrome();
  const page = document.body.dataset.page;
  if (page === "home") renderHome();
  if (page === "search") renderSearch();
  if (page === "listing") renderListing();
  if (page === "brands") renderBrands();
  if (page === "magazine") renderMagazine();
  if (page === "article") renderArticle();
  if (page === "collection") renderCollection();
  if (page === "deals") renderDeals();
  if (page === "pulse") renderPulse();
});
