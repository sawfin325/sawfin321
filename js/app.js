const CART_KEY = "pallethaven-cart";
const USERS_KEY = "pallethaven-users";
const SESSION_KEY = "pallethaven-session";
const ORDERS_KEY = "pallethaven-orders";
const LISTINGS_KEY = "pallethaven-listings";
const CONTACT_INFO = (typeof CONTACT !== "undefined" && CONTACT) || {
  email: "Eu.wholesalestock@gmail.com",
  phone: "+49 1577 8431615",
  wa: "4915778431615"
};
function mailHref(subject, body) {
  let url = "mailto:" + CONTACT_INFO.email;
  const q = [];
  if (subject) q.push("subject=" + encodeURIComponent(subject));
  if (body) q.push("body=" + encodeURIComponent(body));
  return q.length ? url + "?" + q.join("&") : url;
}
function waHref(text) {
  let url = "https://wa.me/" + CONTACT_INFO.wa;
  return text ? url + "?text=" + encodeURIComponent(text) : url;
}
function lotImage(p) {
  if (p && p.image && /^data:image\//.test(p.image)) return p.image;
  return p && p.image ? imgSrc(p.image) : "";
}

function euro(n) {
  return "€" + Number(n).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
function imgSrc(path) {
  if (!path) return "";
  if (/^https?:/i.test(path)) return path;
  return ROOT + path;
}
function productHref(slug) {
  return ROOT + "product.html?p=" + encodeURIComponent(slug);
}
function priceLabel(p) {
  if (p.priceMax && p.priceMax > p.price + 0.009) return euro(p.price) + " – " + euro(p.priceMax);
  return euro(p.price);
}

let PRODUCT_INDEX = null;
function loadListings() {
  try { return JSON.parse(localStorage.getItem(LISTINGS_KEY) || "[]"); }
  catch { return []; }
}
function saveListings(list) { localStorage.setItem(LISTINGS_KEY, JSON.stringify(list)); }
function allProducts() {
  return PRODUCTS.concat(loadListings());
}
function productBySlug(slug) {
  const listed = loadListings().find(p => p.slug === slug);
  if (listed) return listed;
  if (!PRODUCT_INDEX) PRODUCT_INDEX = new Map(PRODUCTS.map(p => [p.slug, p]));
  return PRODUCT_INDEX.get(slug);
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
    const p = productBySlug(i.slug);
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
function categoryBySlug(slug) { return CATEGORIES.find(c => c.slug === slug); }
function productsInCategory(slug) {
  return allProducts().filter(p => p.category === slug);
}

async function sha256(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode("ph:" + text));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, "0")).join("");
}
function loadUsers() {
  try { return JSON.parse(localStorage.getItem(USERS_KEY) || "[]"); }
  catch { return []; }
}
function saveUsers(users) { localStorage.setItem(USERS_KEY, JSON.stringify(users)); }
function getSession() {
  try {
    return JSON.parse(localStorage.getItem(SESSION_KEY) || sessionStorage.getItem(SESSION_KEY) || "null");
  } catch { return null; }
}
function setSession(user, remember) {
  const session = { email: user.email, name: user.name, company: user.company || "" };
  const raw = JSON.stringify(session);
  sessionStorage.removeItem(SESSION_KEY);
  localStorage.removeItem(SESSION_KEY);
  (remember ? localStorage : sessionStorage).setItem(SESSION_KEY, raw);
}
function currentUser() {
  const session = getSession();
  if (!session) return null;
  return loadUsers().find(u => u.email === session.email) || session;
}
function loadOrders() {
  try { return JSON.parse(localStorage.getItem(ORDERS_KEY) || "[]"); }
  catch { return []; }
}
function saveOrder(order) {
  const orders = loadOrders();
  orders.unshift(order);
  localStorage.setItem(ORDERS_KEY, JSON.stringify(orders));
}

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
    return `<div class="mini-item"><img src="${lotImage(p)}" alt=""><div><a href="${productHref(p.slug)}">${p.name}</a><div>${i.qty} × ${euro(p.price)}</div></div><strong>${euro(p.price * i.qty)}</strong></div>`;
  }).join("") + `<div class="mini-total"><span>Subtotaal</span><span>${euro(cartTotal())}</span></div><a class="btn btn-dark btn-block" href="${ROOT}winkelwagen.html">Bekijk winkelwagen</a>`;
}

function productCard(p) {
  const cat = categoryBySlug(p.category);
  return `<article class="product-card">
    <div class="thumb">
      <a href="${productHref(p.slug)}"><img src="${lotImage(p)}" alt="${p.name}"></a>
      <button class="quick" data-quick="${p.slug}">Snel bekijken</button>
    </div>
    <div class="info">
      <p class="product-cat">${cat ? cat.name : (p.category || "Community")}</p>
      <h3><a href="${productHref(p.slug)}">${p.name}</a></h3>
      <div class="price">${priceLabel(p)}</div>
    </div>
  </article>`;
}

function openQuick(slug) {
  const p = productBySlug(slug);
  if (!p) return;
  const modal = document.getElementById("quick-modal");
  modal.querySelector("img").src = lotImage(p);
  modal.querySelector("img").alt = p.name;
  modal.querySelector("h3").textContent = p.name;
  modal.querySelector("[data-q-price]").textContent = priceLabel(p);
  modal.querySelector("[data-q-desc]").textContent = p.short || "";
  modal.querySelector("[data-q-add]").dataset.add = p.slug;
  modal.querySelector("[data-q-link]").href = productHref(p.slug);
  modal.classList.add("open");
}

function openLoginModal(e) {
  if (e) e.preventDefault();
  if (currentUser()) {
    location.href = ROOT + "account.html";
    return;
  }
  document.getElementById("login-modal")?.classList.add("open");
}

function renderHeaderAuth() {
  const user = currentUser();
  document.querySelectorAll("[data-open-login]").forEach(el => {
    if (user) {
      el.textContent = user.name ? user.name.split(" ")[0] : "Account";
      el.classList.add("is-logged-in");
    } else {
      el.textContent = "LOGIN";
      el.classList.remove("is-logged-in");
    }
  });
}

function showFormMessage(form, ok, text) {
  const box = form.querySelector("[data-result]");
  if (!box) return;
  box.className = "alert " + (ok ? "alert-ok" : "alert-err");
  box.textContent = text;
}

function bindAuth() {
  document.querySelectorAll("[data-open-login]").forEach(el => {
    el.addEventListener("click", openLoginModal);
  });
  document.querySelectorAll("[data-close-auth]").forEach(el => {
    el.addEventListener("click", () => document.getElementById("login-modal")?.classList.remove("open"));
  });
  document.getElementById("login-modal")?.addEventListener("click", (e) => {
    if (e.target.id === "login-modal") e.target.classList.remove("open");
  });

  document.querySelectorAll("[data-login]").forEach(form => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = form.email.value.trim().toLowerCase();
      const password = form.password.value;
      const remember = form.remember?.checked;
      const users = loadUsers();
      const user = users.find(u => u.email === email);
      if (!user) {
        showFormMessage(form, false, "Geen account gevonden met dit e-mailadres. Maak eerst een account aan.");
        return;
      }
      const hash = await sha256(password);
      if (hash !== user.passwordHash) {
        showFormMessage(form, false, "Onjuist wachtwoord.");
        return;
      }
      setSession(user, remember);
      document.getElementById("login-modal")?.classList.remove("open");
      location.href = ROOT + "account.html";
    });
  });

  document.querySelectorAll("[data-register]").forEach(form => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      const email = form.email.value.trim().toLowerCase();
      const company = form.company?.value.trim() || "";
      const password = form.password.value;
      const password2 = form.password2.value;
      if (password.length < 6) {
        showFormMessage(form, false, "Kies een wachtwoord van minimaal 6 tekens.");
        return;
      }
      if (password !== password2) {
        showFormMessage(form, false, "Wachtwoorden komen niet overeen.");
        return;
      }
      const users = loadUsers();
      if (users.some(u => u.email === email)) {
        showFormMessage(form, false, "Dit e-mailadres heeft al een account. Log in aan de linkerkant.");
        return;
      }
      const user = {
        id: crypto.randomUUID(),
        name,
        email,
        company,
        passwordHash: await sha256(password),
        createdAt: new Date().toISOString()
      };
      users.push(user);
      saveUsers(users);
      setSession(user, true);
      document.getElementById("login-modal")?.classList.remove("open");
      location.href = ROOT + "account.html";
    });
  });
}

function renderAccount() {
  const panel = document.querySelector("[data-account-panel]");
  if (!panel) return;
  const user = currentUser();
  const forms = document.querySelector("[data-auth-forms]");
  if (!user) {
    panel.innerHTML = "";
    if (forms) forms.style.display = "";
    return;
  }
  if (forms) forms.style.display = "none";
  const orders = loadOrders().filter(o => o.email === user.email);
  const orderHtml = orders.length
    ? `<table class="cart-table"><thead><tr><th>Datum</th><th>Lots</th><th>Totaal</th><th>Status</th></tr></thead><tbody>` +
      orders.map(o => `<tr><td>${o.date}</td><td>${o.items.map(i => i.name + " × " + i.qty).join("<br>")}</td><td>${euro(o.total)}</td><td>${o.status}</td></tr>`).join("") +
      `</tbody></table>`
    : `<p>Je hebt nog geen bestellingen. <a href="${ROOT}winkel.html">Bekijk de winkel</a>.</p>`;
  panel.innerHTML = `
    <div class="account-dash">
      <h2>Welkom, ${user.name || user.email}</h2>
      <p>Je bent ingelogd als <strong>${user.email}</strong>${user.company ? " · " + user.company : ""}.</p>
      <p><button class="btn btn-dark btn-sm" id="logout">Uitloggen</button></p>
      <h3>Accountgegevens</h3>
      <form data-account-update class="account-update">
        <div class="row">
          <div><label>Naam</label><input name="name" value="${user.name || ""}" required></div>
          <div><label>Bedrijfsnaam</label><input name="company" value="${user.company || ""}"></div>
        </div>
        <label>Nieuw wachtwoord (optioneel)</label>
        <input name="password" type="password" minlength="6" autocomplete="new-password">
        <p><button class="btn btn-dark" type="submit">Gegevens opslaan</button></p>
        <div data-result></div>
      </form>
      <h3>Bestellingen</h3>
      ${orderHtml}
    </div>`;
  document.getElementById("logout")?.addEventListener("click", () => {
    localStorage.removeItem(SESSION_KEY);
    sessionStorage.removeItem(SESSION_KEY);
    location.href = ROOT + "account.html";
  });
  document.querySelector("[data-account-update]")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    const users = loadUsers();
    const idx = users.findIndex(u => u.email === user.email);
    if (idx < 0) return;
    users[idx].name = form.name.value.trim();
    users[idx].company = form.company.value.trim();
    if (form.password.value) users[idx].passwordHash = await sha256(form.password.value);
    saveUsers(users);
    setSession(users[idx], true);
    showFormMessage(form, true, "Gegevens opgeslagen.");
    renderHeaderAuth();
  });
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
      box.textContent = "Bedankt. We reageren via " + CONTACT_INFO.email + " of WhatsApp " + CONTACT_INFO.phone + ".";
      form.reset();
    });
  });

  renderCartUI();
  renderHeaderAuth();
  bindAuth();
}

function renderShop() {
  const grid = document.querySelector("[data-shop-grid]");
  if (!grid) return;
  const params = new URLSearchParams(location.search);
  const q = (params.get("s") || "").toLowerCase();
  const cat = grid.dataset.category || params.get("categorie") || "";
  const sort = document.querySelector("[data-sort]");
  const pager = document.querySelector("[data-pager]");
  const PAGE_SIZE = 24;
  let list = cat ? productsInCategory(cat) : allProducts().slice();
  if (q) {
    list = list.filter(p => (p.name + " " + (p.short || "") + " " + p.category).toLowerCase().includes(q));
    const hint = document.querySelector("[data-search-hint]");
    if (hint) hint.textContent = `Zoekresultaten voor “${params.get("s")}”`;
  }
  const apply = () => {
    let shown = list.slice();
    const v = sort ? sort.value : "featured";
    if (v === "price-asc") shown.sort((a, b) => a.price - b.price);
    if (v === "price-desc") shown.sort((a, b) => b.price - a.price);
    if (v === "name") shown.sort((a, b) => a.name.localeCompare(b.name, "nl"));
    const pages = Math.max(1, Math.ceil(shown.length / PAGE_SIZE));
    const page = Math.min(pages, Math.max(1, parseInt(params.get("page") || "1", 10)));
    const slice = shown.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);
    grid.innerHTML = slice.map(productCard).join("") || "<p>Geen pallets gevonden.</p>";
    const count = document.querySelector("[data-result-count]");
    if (count) count.textContent = shown.length.toLocaleString("nl-NL") + " resultaten · pagina " + page + " van " + pages;
    if (pager) pager.innerHTML = pagerHtml(page, pages);
  };
  if (sort) sort.addEventListener("change", () => {
    const u = new URL(location.href);
    u.searchParams.set("page", "1");
    history.replaceState({}, "", u);
    params.set("page", "1");
    apply();
  });
  apply();
}

function pagerHtml(page, pages) {
  if (pages <= 1) return "";
  const url = (n) => {
    const u = new URL(location.href);
    u.searchParams.set("page", n);
    return u.pathname + u.search;
  };
  const items = [];
  const add = (n, label, disabled, active) => {
    if (disabled) items.push(`<span class="off">${label}</span>`);
    else if (active) items.push(`<span class="active">${label}</span>`);
    else items.push(`<a href="${url(n)}">${label}</a>`);
  };
  add(page - 1, "Vorige", page <= 1, false);
  const start = Math.max(1, page - 3);
  const end = Math.min(pages, page + 3);
  if (start > 1) add(1, "1", false, page === 1);
  if (start > 2) items.push("<span class='off'>…</span>");
  for (let n = start; n <= end; n++) add(n, String(n), false, n === page);
  if (end < pages - 1) items.push("<span class='off'>…</span>");
  if (end < pages) add(pages, String(pages), false, page === pages);
  add(page + 1, "Volgende", page >= pages, false);
  return items.join("");
}

function renderProductPage() {
  const mount = document.querySelector("[data-product-page]");
  if (!mount) return;
  const slug = new URLSearchParams(location.search).get("p");
  const p = productBySlug(slug);
  if (!p) {
    mount.innerHTML = `<p>Dit lot is niet gevonden.</p><p><a class="btn btn-dark" href="${ROOT}winkel.html">Terug naar winkel</a></p>`;
    return;
  }
  const cat = categoryBySlug(p.category) || { slug: "winkel", name: p.category || "Community pallet" };
  document.title = p.name + " – PalletHaven";
  const crumbs = document.querySelector("[data-product-crumbs]");
  if (crumbs) crumbs.innerHTML = `<a href="${ROOT}index.html">Home</a> / <a href="${ROOT}winkel.html">Winkel</a> / ${cat.name}`;
  mount.innerHTML = `
    <div class="product-layout">
      <div class="gallery"><img src="${lotImage(p)}" alt="${p.name}"></div>
      <div>
        <p class="product-cat">${cat.name}</p>
        <h1>${p.name}</h1>
        <p class="price" style="font-size:1.6rem">${priceLabel(p)}</p>
        <p>${p.short || ""}</p>
        <div class="meta-list">
          <div><span>Categorie</span><span>${cat.name}</span></div>
          <div><span>Conditie</span><span>${p.condition || "Zie lotomschrijving"}</span></div>
          <div><span>Aantal stuks</span><span>${p.items != null ? p.items : "Niet gespecificeerd"}</span></div>
          <div><span>Geschatte MSRP</span><span>${p.msrp ? euro(p.msrp) : "Onbekend / geen manifest"}</span></div>
          <div><span>Verzending</span><span>LTL-vracht, offerte na adres</span></div>
        </div>
        <div class="qty-row">
          <label>Aantal <input type="number" min="1" value="1" data-qty></label>
          <button class="btn btn-dark" data-add="${p.slug}" data-label="In winkelwagen">In winkelwagen</button>
        </div>
        <p class="form-note">Vraag het volledige manifest aan via ${CONTACT_INFO.email} of WhatsApp ${CONTACT_INFO.phone} voordat je betaalt. Bestellen gaat via e-mail of WhatsApp. High-count en mystery lots gaan as-is.</p>
      </div>
    </div>
    <section class="section alt" style="padding-left:0;padding-right:0">
      <h2>Omschrijving</h2>
      <p>${p.short || ""} PalletHaven verkoopt aan professionele kopers. Door te bestellen bevestig je de lotvoorwaarden, inclusief conditieklasse en het wel of niet aanwezig zijn van een itemmanifest.</p>
    </section>`;
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
          <td style="display:flex;gap:12px;align-items:center"><img src="${lotImage(p)}" alt=""><div><a href="${productHref(p.slug)}">${p.name}</a><br><button class="btn btn-sm" data-remove="${p.slug}">Verwijderen</button></div></td>
          <td>${euro(p.price)}</td>
          <td><input type="number" min="1" value="${i.qty}" data-qty-slug="${p.slug}" style="width:70px"></td>
          <td>${euro(p.price * i.qty)}</td>
        </tr>`;
      }).join("") + `</tbody></table>`;
    const totals = document.querySelector("[data-cart-totals]");
    if (totals) totals.innerHTML = `<div class="totals"><h3>Overzicht</h3><div><span>Subtotaal</span><span>${euro(cartTotal())}</span></div><div><span>Verzending</span><span>Offerte na adres</span></div><div class="grand"><span>Totaal</span><span>${euro(cartTotal())}</span></div><p class="form-note">Bestel via e-mail of WhatsApp.</p><a class="btn btn-dark btn-block" href="${ROOT}afrekenen.html">Afrekenen via e-mail / WhatsApp</a></div>`;
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

function orderMessage(form, items) {
  const lines = items.map(i => {
    const p = productBySlug(i.slug);
    return `- ${p ? p.name : i.slug} × ${i.qty} (${p ? euro(p.price * i.qty) : ""})`;
  });
  return [
    "Nieuwe PalletHaven-order",
    "",
    "Contact: " + form.name.value,
    "E-mail: " + form.email.value,
    "Telefoon: " + form.phone.value,
    "Bedrijf: " + (form.company?.value || "-"),
    "Adres: " + form.address.value + ", " + form.zip.value + " " + form.city.value + ", " + form.country.value,
    "",
    "Lots:",
    ...lines,
    "",
    "Totaal: " + euro(cartTotal()),
    form.note?.value ? "Opmerking: " + form.note.value : ""
  ].filter(Boolean).join("\n");
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
  const user = currentUser();
  if (user) {
    if (form.name) form.name.value = user.name || "";
    if (form.email) form.email.value = user.email || "";
    if (form.company) form.company.value = user.company || "";
  }
  if (summary) {
    summary.innerHTML = items.map(i => {
      const p = productBySlug(i.slug);
      return `<div><span>${p.name} × ${i.qty}</span><strong>${euro(p.price * i.qty)}</strong></div>`;
    }).join("") + `<div class="grand"><span>Totaal</span><span>${euro(cartTotal())}</span></div>
      <p><a class="btn btn-dark btn-block" href="${mailHref("PalletHaven order", orderMessage(form, items))}">Order via e-mail</a></p>
      <p><a class="btn btn-dark btn-block" href="${waHref(orderMessage(form, items))}">Order via WhatsApp</a></p>
      <p class="form-note">${CONTACT_INFO.email}<br>WhatsApp ${CONTACT_INFO.phone}</p>`;
  }
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const via = (e.submitter && e.submitter.value) || "email";
    const email = (form.email.value || "").trim().toLowerCase();
    const msg = orderMessage(form, getCart());
    saveOrder({
      id: crypto.randomUUID(),
      email,
      name: form.name.value,
      date: new Date().toLocaleDateString("nl-NL"),
      total: cartTotal(),
      status: "Verstuurd via " + (via === "whatsapp" ? "WhatsApp" : "e-mail"),
      items: getCart().map(i => {
        const p = productBySlug(i.slug);
        return { slug: i.slug, name: p ? p.name : i.slug, qty: i.qty, price: p ? p.price : 0 };
      })
    });
    localStorage.removeItem(CART_KEY);
    renderCartUI();
    if (via === "whatsapp") location.href = waHref(msg);
    else location.href = mailHref("PalletHaven order", msg);
    form.innerHTML = `<div class="alert alert-ok"><strong>Stuur je order nu via e-mail of WhatsApp.</strong>
      <p>E-mail: <a href="${mailHref("PalletHaven order", msg)}">${CONTACT_INFO.email}</a></p>
      <p>WhatsApp: <a href="${waHref(msg)}">${CONTACT_INFO.phone}</a></p>
      ${user ? "<p>Je vindt deze order terug onder Mijn account.</p>" : ""}</div>`;
  });
}

function renderCommunity() {
  const select = document.querySelector("[data-post-pallet] select[name=category]");
  if (select && !select.options.length) {
    CATEGORIES.forEach(c => {
      const opt = document.createElement("option");
      opt.value = c.slug;
      opt.textContent = c.name;
      select.appendChild(opt);
    });
  }
  const grid = document.querySelector("[data-community-grid]");
  if (grid) {
    const list = loadListings();
    grid.innerHTML = list.length ? list.map(productCard).join("") : "<p>Nog geen openbare pallets. Plaats de eerste.</p>";
  }
  const form = document.querySelector("[data-post-pallet]");
  if (!form || form.dataset.bound) return;
  form.dataset.bound = "1";
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const file = form.photo?.files?.[0];
    let image = "";
    if (file) {
      image = await new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
    }
    const listing = {
      slug: "community-" + Date.now(),
      name: form.title.value.trim(),
      category: form.category.value,
      price: parseFloat(form.price.value) || 0,
      priceMax: parseFloat(form.price.value) || 0,
      items: form.items.value ? parseInt(form.items.value, 10) : null,
      condition: "Community listing",
      image,
      short: form.description.value.trim() + " · Contact: " + form.name.value + " " + (form.phone.value || form.email.value),
      seller: { name: form.name.value.trim(), email: form.email.value.trim(), phone: form.phone.value.trim() }
    };
    const list = loadListings();
    list.unshift(listing);
    saveListings(list);
    showFormMessage(form, true, "Je pallet staat online in de winkel en op deze pagina.");
    form.reset();
    renderCommunity();
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bindCommon();
  renderShop();
  renderProductPage();
  renderCartPage();
  renderCheckout();
  renderAccount();
  renderCommunity();
});
