const CART_KEY = "pallethaven-cart";
const USER_KEY = "pallethaven-user";

function euro(n) {
  return new Intl.NumberFormat("nl-NL", { style: "currency", currency: "EUR" }).format(n);
}

function getCart() {
  try { return JSON.parse(localStorage.getItem(CART_KEY) || "[]"); }
  catch { return []; }
}
function saveCart(items) {
  localStorage.setItem(CART_KEY, JSON.stringify(items));
  renderCartUI();
}
function cartCount() { return getCart().reduce((s, i) => s + i.qty, 0); }
function cartTotal() {
  return getCart().reduce((s, i) => {
    const p = PRODUCTS.find(x => x.slug === i.slug);
    return s + (p ? p.price * i.qty : 0);
  }, 0);
}
function addToCart(slug, qty = 1) {
  const items = getCart();
  const found = items.find(i => i.slug === slug);
  if (found) found.qty += qty;
  else items.push({ slug, qty });
  saveCart(items);
}
function setQty(slug, qty) {
  qty = Math.max(0, parseInt(qty, 10) || 0);
  let items = getCart();
  if (qty <= 0) items = items.filter(i => i.slug !== slug);
  else {
    const found = items.find(i => i.slug === slug);
    if (found) found.qty = qty;
  }
  saveCart(items);
}
function productBySlug(slug) { return PRODUCTS.find(p => p.slug === slug); }
function categoryBySlug(slug) { return CATEGORIES.find(c => c.slug === slug); }
function productsInCategory(slug) { return PRODUCTS.filter(p => p.category === slug); }

function renderCartUI() {
  const count = cartCount();
  document.querySelectorAll("[data-cart-count]").forEach(el => el.textContent = count);
  document.querySelectorAll("[data-cart-total]").forEach(el => el.textContent = euro(cartTotal()));
  const mini = document.querySelector("[data-mini-cart]");
  if (!mini) return;
  const items = getCart();
  if (!items.length) {
    mini.innerHTML = `<div class="mini-empty"><p>Geen producten in de winkelwagen.</p><a class="btn btn-dark btn-sm" href="${ROOT}winkel.html">Terug naar winkel</a></div>`;
    return;
  }
  mini.innerHTML = items.map(i => {
    const p = productBySlug(i.slug);
    if (!p) return "";
    return `<div class="mini-item"><img src="${p.image}" alt=""><div><a href="${ROOT}product/${p.slug}.html">${p.name}</a><div>${i.qty} × ${euro(p.price)}</div></div><strong>${euro(p.price * i.qty)}</strong></div>`;
  }).join("") + `<div class="mini-total"><span>Subtotaal</span><span>${euro(cartTotal())}</span></div><a class="btn btn-dark btn-block" href="${ROOT}winkelwagen.html">Bekijk winkelwagen</a>`;
}

function productCard(p) {
  return `<article class="product-card">
    ${p.badge ? `<span class="badge">${p.badge}</span>` : ""}
    <div class="thumb">
      <a href="${ROOT}product/${p.slug}.html"><img src="${p.image}" alt="${p.name}"></a>
      <button class="quick" data-quick="${p.slug}">Snel bekijken</button>
    </div>
    <div class="info">
      <h3><a href="${ROOT}product/${p.slug}.html">${p.name}</a></h3>
      <div class="price">${p.msrp ? `<span class="msrp">${euro(p.msrp)}</span>` : ""}${euro(p.price)}</div>
    </div>
  </article>`;
}

function openQuick(slug) {
  const p = productBySlug(slug);
  if (!p) return;
  const modal = document.getElementById("quick-modal");
  modal.querySelector("img").src = p.image;
  modal.querySelector("img").alt = p.name;
  modal.querySelector("h3").textContent = p.name;
  modal.querySelector("[data-q-price]").textContent = euro(p.price);
  modal.querySelector("[data-q-desc]").textContent = p.short;
  modal.querySelector("[data-q-add]").dataset.add = p.slug;
  modal.querySelector("[data-q-link]").href = ROOT + "product/" + p.slug + ".html";
  modal.classList.add("open");
}

function bindCommon() {
  const menuBtn = document.querySelector("[data-menu]");
  const mobile = document.querySelector("[data-mobile]");
  if (menuBtn && mobile) menuBtn.addEventListener("click", () => mobile.classList.toggle("open"));

  document.querySelectorAll("[data-search]").forEach(form => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const q = form.querySelector("input").value.trim();
      location.href = ROOT + "winkel.html?s=" + encodeURIComponent(q);
    });
  });

  document.body.addEventListener("click", (e) => {
    const q = e.target.closest("[data-quick]");
    if (q) { e.preventDefault(); openQuick(q.dataset.quick); }
    const add = e.target.closest("[data-add]");
    if (add) {
      e.preventDefault();
      const qtyEl = document.querySelector("[data-qty]");
      const qty = qtyEl ? parseInt(qtyEl.value, 10) || 1 : 1;
      addToCart(add.dataset.add, qty);
      add.textContent = "Toegevoegd";
      setTimeout(() => { add.textContent = add.dataset.label || "In winkelwagen"; }, 1200);
    }
    if (e.target.closest("[data-close]")) document.getElementById("quick-modal")?.classList.remove("open");
  });

  document.querySelectorAll("[data-contact]").forEach(form => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const box = form.querySelector("[data-result]");
      box.className = "alert alert-ok";
      box.textContent = "Bedankt. We reageren binnen één werkdag op sales@pallethaven.nl.";
      form.reset();
    });
  });

  renderCartUI();
}

function renderShop() {
  const grid = document.querySelector("[data-shop-grid]");
  if (!grid) return;
  const params = new URLSearchParams(location.search);
  const q = (params.get("s") || "").toLowerCase();
  const cat = grid.dataset.category || params.get("categorie") || "";
  const sort = document.querySelector("[data-sort]");
  let list = cat ? productsInCategory(cat) : PRODUCTS.slice();
  if (q) {
    list = list.filter(p => (p.name + " " + p.short + " " + p.category).toLowerCase().includes(q));
    const hint = document.querySelector("[data-search-hint]");
    if (hint) hint.textContent = `Zoekresultaten voor “${params.get("s")}”`;
  }
  const apply = () => {
    let shown = list.slice();
    const v = sort ? sort.value : "featured";
    if (v === "price-asc") shown.sort((a, b) => a.price - b.price);
    if (v === "price-desc") shown.sort((a, b) => b.price - a.price);
    if (v === "name") shown.sort((a, b) => a.name.localeCompare(b.name, "nl"));
    grid.innerHTML = shown.map(productCard).join("") || "<p>Geen pallets gevonden.</p>";
    const count = document.querySelector("[data-result-count]");
    if (count) count.textContent = shown.length + " resultaten";
  };
  if (sort) sort.addEventListener("change", apply);
  apply();
}

function renderCartPage() {
  const table = document.querySelector("[data-cart-table]");
  if (!table) return;
  const draw = () => {
    const items = getCart();
    if (!items.length) {
      table.innerHTML = `<p>Je winkelwagen is leeg.</p><p><a class="btn btn-dark" href="${ROOT}winkel.html">Terug naar winkel</a></p>`;
      document.querySelector("[data-cart-totals]")?.replaceChildren();
      return;
    }
    table.innerHTML = `<table class="cart-table"><thead><tr><th>Product</th><th>Prijs</th><th>Aantal</th><th>Subtotaal</th></tr></thead><tbody>` +
      items.map(i => {
        const p = productBySlug(i.slug);
        if (!p) return "";
        return `<tr>
          <td style="display:flex;gap:12px;align-items:center"><img src="${p.image}" alt=""><div><a href="${ROOT}product/${p.slug}.html">${p.name}</a><br><button class="btn btn-sm" data-remove="${p.slug}">Verwijderen</button></div></td>
          <td>${euro(p.price)}</td>
          <td><input type="number" min="1" value="${i.qty}" data-qty-slug="${p.slug}" style="width:70px"></td>
          <td>${euro(p.price * i.qty)}</td>
        </tr>`;
      }).join("") + `</tbody></table>`;
    const totals = document.querySelector("[data-cart-totals]");
    if (totals) totals.innerHTML = `<div class="totals"><h3>Overzicht</h3><div><span>Subtotaal</span><span>${euro(cartTotal())}</span></div><div><span>Verzending</span><span>Offerte na adres</span></div><div class="grand"><span>Totaal</span><span>${euro(cartTotal())}</span></div><p class="form-note">Gratis verzending in Nederland vanaf €3.000.</p><a class="btn btn-dark btn-block" href="${ROOT}afrekenen.html">Afrekenen</a></div>`;
  };
  table.addEventListener("change", (e) => {
    const slug = e.target.dataset.qtySlug;
    if (slug) setQty(slug, e.target.value);
    draw();
  });
  table.addEventListener("click", (e) => {
    const rm = e.target.closest("[data-remove]");
    if (rm) { setQty(rm.dataset.remove, 0); draw(); }
  });
  draw();
}

function renderCheckout() {
  const form = document.querySelector("[data-checkout]");
  if (!form) return;
  const summary = document.querySelector("[data-order-summary]");
  const items = getCart();
  if (!items.length) {
    form.innerHTML = `<p>Je winkelwagen is leeg.</p><a class="btn btn-dark" href="${ROOT}winkel.html">Naar de winkel</a>`;
    return;
  }
  if (summary) {
    summary.innerHTML = items.map(i => {
      const p = productBySlug(i.slug);
      return `<div><span>${p.name} × ${i.qty}</span><strong>${euro(p.price * i.qty)}</strong></div>`;
    }).join("") + `<div class="grand"><span>Totaal</span><span>${euro(cartTotal())}</span></div>`;
  }
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    localStorage.removeItem(CART_KEY);
    renderCartUI();
    form.innerHTML = `<div class="alert alert-ok"><strong>Bestelling ontvangen.</strong> We sturen een manifest en betaalinstructie (bankoverschrijving of Revolut) naar het opgegeven e-mailadres. Tot die tijd is er geen betaling verschuldigd.</div>`;
  });
}

function renderAccount() {
  const login = document.querySelector("[data-login]");
  const register = document.querySelector("[data-register]");
  const panel = document.querySelector("[data-account-panel]");
  const user = JSON.parse(localStorage.getItem(USER_KEY) || "null");
  if (user && panel) {
    panel.innerHTML = `<div class="alert alert-ok">Ingelogd als ${user.email}. <button class="btn btn-sm" id="logout">Uitloggen</button></div>`;
    document.getElementById("logout")?.addEventListener("click", () => {
      localStorage.removeItem(USER_KEY);
      location.reload();
    });
  }
  login?.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = login.querySelector("[name=email]").value;
    localStorage.setItem(USER_KEY, JSON.stringify({ email }));
    location.reload();
  });
  register?.addEventListener("submit", (e) => {
    e.preventDefault();
    const box = register.querySelector("[data-result]");
    box.className = "alert alert-ok";
    box.textContent = "Accountlink is klaargezet. In deze demo kun je direct inloggen met je e-mailadres.";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bindCommon();
  renderShop();
  renderCartPage();
  renderCheckout();
  renderAccount();
});
