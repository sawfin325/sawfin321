function $(sel, root = document) { return root.querySelector(sel); }
function $all(sel, root = document) { return [...root.querySelectorAll(sel)]; }
function money(n) {
  return new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(n);
}
function params() { return new URLSearchParams(location.search); }
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
  const brandLinks = BRANDS.slice(0, 12).map((b) =>
    `<a href="search.html?brand=${encodeURIComponent(b.name)}">${b.name}</a>`
  ).join("");
  return `
  <div class="promo">Have you tried the Meridian app? <a href="apps.html">Discover now</a></div>
  <header class="header">
    <div class="wrap header-row">
      <button class="menu-btn btn-ghost" type="button" aria-label="Menu" data-menu>☰</button>
      <a class="logo" href="index.html">meridian</a>
      <form class="search" action="search.html" method="get">
        <input name="q" type="search" placeholder="Search through ${SITE.listingCount} watches worldwide" value="${params().get("q") || ""}" />
        <button type="submit" aria-label="Search">${iconSearch()}</button>
      </form>
      ${account}
    </div>
    <nav class="nav wrap" id="main-nav">
      <div class="nav-item">
        <a class="nav-link" href="search.html">Buy a watch <span class="caret">▾</span></a>
        <div class="dropdown">${brandLinks}<a href="brands.html">All brands</a><a href="search.html?cat=mens">Men's watches</a><a href="search.html?cat=womens">Women's watches</a></div>
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
    ["Buy on Meridian", [["security.html","Buyer Protection"],["security.html#escrow","Payment via the Escrow Service"],["security.html#authenticity","Commitment to Authenticity"],["faq.html","Easy Returns"]]],
    ["Sell on Meridian", [["sell.html","Selling as a Private Seller"],["sell.html","Selling Commercially"],["sell.html","Free Appraisal"],["faq.html","Advice for private sellers"]]],
    ["About Meridian", [["about.html","About us"],["about.html","Jobs"],["about.html","Press"],["about.html","Legal Details"]]],
    ["Personalized support", [["faq.html","Frequently Asked Questions"],["contact.html","Contact"]]],
    ["Meridian Apps", [["apps.html","iOS App Store"],["apps.html","Google Play"]]],
    ["Payment methods", [["security.html","Visa · Mastercard · Amex"],["security.html","Wire transfer"],["security.html","Pay over time"]]],
  ];
  return `
  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div>
          <h4>Meridian Newsletter</h4>
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
        ${cols.map(([h, links]) => `<div><h4>${h}</h4><ul>${links.map(([href,t]) => `<li><a href="${href}">${t}</a></li>`).join("")}</ul></div>`).join("")}
      </div>
      <div class="countries">
        ${COUNTRIES.map((c) => `<a href="search.html">${c}</a>`).join("")}
      </div>
      <div class="legal">
        <div>
          <a href="about.html">Data Privacy Policy</a> ·
          <a href="about.html">Accessibility</a> ·
          <a href="about.html">Manage Cookies</a> ·
          <a href="about.html">Terms &amp; Conditions</a>
        </div>
        <div>© ${new Date().getFullYear()} Meridian Marketplace — a demo recreation inspired by chrono24.com. Not affiliated with Chrono24.</div>
      </div>
    </div>
  </footer>`;
}

function watchCard(w) {
  const on = favs().includes(w.id) ? " on" : "";
  return `
  <article class="watch-card">
    <div class="media">
      <button class="heart${on}" type="button" data-fav="${w.id}" aria-label="Save">♥</button>
      <a href="listing.html?id=${encodeURIComponent(w.id)}"><img src="${w.image}" alt="${w.brand} ${w.model}" /></a>
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
  const p = params();
  const q = (p.get("q") || "").trim().toLowerCase();
  const brand = p.get("brand") || "";
  const cat = p.get("cat") || "";
  const min = Number(p.get("min") || 0);
  const max = Number(p.get("max") || 0);
  const sort = p.get("sort") || "popular";
  let list = WATCHES.slice();
  if (q) list = list.filter((w) => `${w.brand} ${w.model} ${w.ref}`.toLowerCase().includes(q));
  if (brand) list = list.filter((w) => w.brand === brand);
  if (cat) list = list.filter((w) => w.cats.includes(cat));
  if (min) list = list.filter((w) => w.price >= min);
  if (max) list = list.filter((w) => w.price <= max);
  if (sort === "price-asc") list.sort((a, b) => a.price - b.price);
  if (sort === "price-desc") list.sort((a, b) => b.price - a.price);
  if (sort === "new") list.sort((a, b) => b.year - a.year);
  return list;
}

function mountChrome() {
  const h = $("#site-header");
  const f = $("#site-footer");
  if (h) h.innerHTML = headerHTML();
  if (f) f.innerHTML = footerHTML();
  const menu = $("[data-menu]");
  if (menu) menu.addEventListener("click", () => $("#main-nav").classList.toggle("open"));
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

function renderHome() {
  const brands = $("#popular-brands");
  if (brands) brands.innerHTML = BRANDS.slice(0, 10).map((b) =>
    `<a class="brand-card" href="search.html?brand=${encodeURIComponent(b.name)}">${b.name}</a>`
  ).join("");
  const explore = $("#explore-grid");
  if (explore) explore.innerHTML = CATEGORIES.map((c) =>
    `<a class="tile" href="search.html?cat=${c.slug}"><img src="${c.image}" alt=""><span>${c.name}</span></a>`
  ).join("");
  const popular = $("#popular-models");
  if (popular) popular.innerHTML = WATCHES.slice(0, 8).map(watchCard).join("");
  const links = $("#model-links");
  if (links) links.innerHTML = POPULAR_MODELS.map((m) => {
    const brand = m.split(" ")[0];
    return `<a href="search.html?q=${encodeURIComponent(m)}">${m}</a>`;
  }).join("");
  const reviews = $("#review-row");
  if (reviews) reviews.innerHTML = REVIEWS.slice(0, 3).map((r) =>
    `<article class="review"><div class="stars">★★★★★</div><p>“${r.text}”</p><div class="who"><div class="avatar">${r.name[0]}</div><div>${r.name}<br>${r.loc}</div></div></article>`
  ).join("");
  const mag = $("#magazine-grid");
  if (mag) mag.innerHTML = ARTICLES.map((a) =>
    `<a class="article" href="article.html?id=${a.id}"><img src="${a.image}" alt=""><div class="tag">${a.tag}</div><h3>${a.title}</h3><div class="byline">${a.author} · ${a.date} · ${a.read}</div></a>`
  ).join("");
  const ig = $("#ig-grid");
  if (ig) ig.innerHTML = INSTAGRAM.map((src) => `<img src="${src}" alt="Meridian on Instagram">`).join("");
  const vids = $("#video-grid");
  if (vids) vids.innerHTML = VIDEOS.map((v) =>
    `<article class="video"><div class="play">▶</div><img src="${v.image}" alt=""><h3>${v.title}</h3><p>${v.host} · ${v.time} · ${v.date}</p></article>`
  ).join("");
}

function renderSearch() {
  const grid = $("#results");
  if (!grid) return;
  const list = filterWatches();
  const count = $("#result-count");
  if (count) count.textContent = `${list.length.toLocaleString()} listings`;
  grid.innerHTML = list.length ? list.map(watchCard).join("") : `<p>No watches matched those filters.</p>`;
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
  const w = WATCHES.find((x) => x.id === params().get("id")) || WATCHES[0];
  document.title = `${w.brand} ${w.model} | meridian`;
  root.innerHTML = `
    <div class="crumbs wrap"><a href="index.html">Home</a> / <a href="search.html?brand=${encodeURIComponent(w.brand)}">${w.brand} watches</a> / ${w.model}</div>
    <div class="product wrap">
      <div>
        <div class="gallery"><img id="main-photo" src="${w.image}" alt="${w.brand} ${w.model}"></div>
        <div class="thumbs"><img class="on" src="${w.image}" alt=""></div>
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
        <p style="margin:10px 0 0;font-size:13px;color:var(--muted)">Meridian Certified available · Buyer Protection included</p>
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
      <div class="watch-grid">${WATCHES.filter((x) => x.brand === w.brand && x.id !== w.id).slice(0, 4).map(watchCard).join("")}</div>
    </section>`;
  $("[data-buy]")?.addEventListener("click", () => {
    toast("Buyer Protection checkout is a demo — no payment is taken.");
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
  document.title = `${a.title} | meridian Magazine`;
  el.innerHTML = `
    <div class="crumbs"><a href="index.html">Home</a> / <a href="magazine.html">Magazine</a> / ${a.tag}</div>
    <p class="tag">${a.tag}</p>
    <h1>${a.title}</h1>
    <p class="byline">${a.author} · ${a.date} · ${a.read}</p>
    <img src="${a.image}" alt="" style="width:100%;max-height:420px;object-fit:cover;margin:18px 0">
    <p style="font-size:18px;max-width:720px">${a.body}</p>
    <p style="max-width:720px;color:var(--muted)">This magazine is part of the Meridian demo site. Stories are original summaries written for the clone and are not copied from Chrono24.</p>`;
}

function renderCollection() {
  const el = $("#collection-grid");
  if (!el) return;
  const ids = favs();
  const list = WATCHES.filter((w) => ids.includes(w.id));
  el.innerHTML = list.length ? list.map(watchCard).join("") : `<p>Your collection is empty. Tap the heart on any listing to save it.</p>`;
}

function renderDeals() {
  const el = $("#deals-grid");
  if (!el) return;
  const list = WATCHES.slice().sort((a, b) => a.price - b.price).slice(0, 12);
  el.innerHTML = list.map(watchCard).join("");
}

function renderPulse() {
  const el = $("#pulse-table");
  if (!el) return;
  el.innerHTML = WATCHES.slice(0, 16).map((w, i) => {
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
