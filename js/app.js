const CART_KEY = "pallethaven-cart";
const USERS_KEY = "pallethaven-users";
const SESSION_KEY = "pallethaven-session";
const ORDERS_KEY = "pallethaven-orders";

function euro(n) {
  return "€" + Number(n).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
function imgSrc(path) {
  if (!path) return "";
  if (/^https?:/i.test(path)) return path;
  return ROOT + path;
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
    return `<div class="mini-item"><img src="${imgSrc(p.image)}" alt=""><div><a href="${ROOT}product/${p.slug}.html">${p.name}</a><div>${i.qty} × ${euro(p.price)}</div></div><strong>${euro(p.price * i.qty)}</strong></div>`;
  }).join("") + `<div class="mini-total"><span>Subtotaal</span><span>${euro(cartTotal())}</span></div><a class="btn btn-dark btn-block" href="${ROOT}winkelwagen.html">Bekijk winkelwagen</a>`;
}

function productCard(p) {
  const cat = categoryBySlug(p.category);
  return `<article class="product-card">
    <div class="thumb">
      <a href="${ROOT}product/${p.slug}.html"><img src="${imgSrc(p.image)}" alt="${p.name}"></a>
      <button class="quick" data-quick="${p.slug}">Snel bekijken</button>
    </div>
    <div class="info">
      <p class="product-cat">${cat ? cat.name : ""}</p>
      <h3><a href="${ROOT}product/${p.slug}.html">${p.name}</a></h3>
      <div class="price">${euro(p.price)}</div>
    </div>
  </article>`;
}

function openQuick(slug) {
  const p = productBySlug(slug);
  if (!p) return;
  const modal = document.getElementById("quick-modal");
  modal.querySelector("img").src = imgSrc(p.image);
  modal.querySelector("img").alt = p.name;
  modal.querySelector("h3").textContent = p.name;
  modal.querySelector("[data-q-price]").textContent = euro(p.price);
  modal.querySelector("[data-q-desc]").textContent = p.short;
  modal.querySelector("[data-q-add]").dataset.add = p.slug;
  modal.querySelector("[data-q-link]").href = ROOT + "product/" + p.slug + ".html";
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
      box.textContent = "Bedankt. We reageren binnen één werkdag op sales@pallethaven.nl.";
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
          <td style="display:flex;gap:12px;align-items:center"><img src="${imgSrc(p.image)}" alt=""><div><a href="${ROOT}product/${p.slug}.html">${p.name}</a><br><button class="btn btn-sm" data-remove="${p.slug}">Verwijderen</button></div></td>
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
    }).join("") + `<div class="grand"><span>Totaal</span><span>${euro(cartTotal())}</span></div>`;
  }
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const email = (form.email.value || "").trim().toLowerCase();
    saveOrder({
      id: crypto.randomUUID(),
      email,
      name: form.name.value,
      date: new Date().toLocaleDateString("nl-NL"),
      total: cartTotal(),
      status: "Wacht op betaling",
      items: getCart().map(i => {
        const p = productBySlug(i.slug);
        return { slug: i.slug, name: p ? p.name : i.slug, qty: i.qty, price: p ? p.price : 0 };
      })
    });
    localStorage.removeItem(CART_KEY);
    renderCartUI();
    form.innerHTML = `<div class="alert alert-ok"><strong>Bestelling ontvangen.</strong> We sturen een manifest en betaalinstructie (bankoverschrijving of Revolut) naar ${email}. Tot die tijd is er geen betaling verschuldigd.${user ? " Je vindt deze order terug onder Mijn account." : " Maak een account aan om je orders later terug te zien."}</div>`;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bindCommon();
  renderShop();
  renderCartPage();
  renderCheckout();
  renderAccount();
});
