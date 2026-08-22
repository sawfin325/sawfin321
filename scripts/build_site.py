#!/usr/bin/env python3
"""Generate the PalletHaven static wholesale website."""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import CATEGORIES, CAT_MAP, IMG, by_category, generate_products

PRODUCTS = generate_products(10000)
PRODUCT_BY_SLUG = {p["slug"]: p for p in PRODUCTS}

EMAIL = "Eu.wholesalestock@gmail.com"
PHONE = "+49 1577 8431615"
WA_NUM = "4915778431615"
MAIL_HREF = f"mailto:{EMAIL}"
WA_HREF = f"https://wa.me/{WA_NUM}"
ADMIN_PASSWORD = "HavenBeheer2026"
ADMIN_HASH = hashlib.sha256(("ph-admin:" + ADMIN_PASSWORD).encode()).hexdigest()

NAV = [
    ("index.html", "Home"),
    ("winkel.html", "Shop"),
    ("blog.html", "Blog"),
    ("plaats-pallet.html", "List a pallet"),
    ("contact.html", "Contact us"),
    ("over-ons.html", "About us"),
    ("privacybeleid.html", "Privacy Policy"),
    ("algemene-voorwaarden.html", "Terms and Conditions"),
    ("leveringsvoorwaarden.html", "Shipping Terms"),
    ("disclaimer.html", "Legal Disclaimer"),
]

BLOG_POSTS = [
    {
        "slug": "hoe-bestel-je-via-email-of-whatsapp",
        "title": "How to order from PalletHaven: email or WhatsApp",
        "date": "12 August 2026",
        "excerpt": "There is no online checkout. To buy a pallet, send the order by email or WhatsApp. Here is how it works, step by step.",
        "image": "assets/products/pallet-electronics.jpg",
        "body": """
<p>PalletHaven does not take online payment. When you click Order, you choose email or WhatsApp. The order stays a conversation: lot, quantity, delivery address and freight are confirmed before money changes hands.</p>
<h2>What you need</h2>
<p>Company name, contact person, email, phone, and a delivery address where a pallet jack or forklift can take the lot. Quote the lot shown on the product page, plus the quantity.</p>
<h2>By email</h2>
<p>Send your order to <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a>. The product page has a button that pre-fills the message. We confirm availability, the manifest (where promised) and freight.</p>
<h2>By WhatsApp</h2>
<p>Same content, faster back-and-forth: <a href="https://wa.me/4915778431615">+49 1577 8431615</a>. Useful if you still need to send a photo of the unload point or a company registration number.</p>
<h2>After that</h2>
<p>Once confirmed, you pay by bank transfer or Revolut. Shipping starts after payment is received. Tracking follows with each shipment.</p>
""",
    },
    {
        "slug": "wat-is-een-liquidatiepallet",
        "title": "What is a liquidation pallet?",
        "date": "8 August 2026",
        "excerpt": "Overstock, seasonal clearance or return stock, bundled below retail. What you buy depends on the lot type and whether there is a manifest.",
        "image": "assets/products/pallet-amazon-boxes.jpg",
        "body": """
<p>A liquidation pallet is a bundle of merchandise that a retailer, manufacturer or distributor moves into wholesale. Think overstock, seasonal clearance or consumer returns. Resellers buy the bundle below retail and sell piece by piece.</p>
<h2>Why resellers buy this</h2>
<p>You get brands without a full wholesale catalog. Testing new categories without locking in truckload volume is part of that. Many buyers start with one or two pallets and grow from there.</p>
<h2>The risk</h2>
<p>Condition varies. That is why we issue a line-by-line rundown on standard lots. A high-count with no list is a different product, at a different price, for a different buyer. Read the lot page: new, returns or salvage is stated there.</p>
<h2>Ordering</h2>
<p>Pick a lot in the shop and send the order by email or WhatsApp. No walk-in, no pickup on standard pallets.</p>
""",
    },
    {
        "slug": "pallet-flipping-bijverdienste-of-fulltime",
        "title": "Pallet flipping: side income or full-time business?",
        "date": "2 August 2026",
        "excerpt": "Evenings and weekends to test, or cash flow and storage to scale. The pace decides which lot you take first.",
        "image": "assets/products/pallet-sneakers.jpg",
        "body": """
<p>As a side income you test the market with limited risk. Full-time offers more scale — from a few pallets to truckloads — but it needs cash flow, storage and a fixed buying plan.</p>
<h2>Start small</h2>
<p>Most buyers who stick with it start with one or two manifest lots. They build their sort-and-list system and scale after that. A high-count gaylord as a first purchase is rarely a good idea.</p>
<h2>When full-time fits</h2>
<p>When you already have a sales channel, you know how long stock sits with you, and freight plus fallout are in your price. Then volume is leverage, not a gamble.</p>
<p>PalletHaven is built for both tempos: small cartons to test and truckloads when the operation can take them. Orders by email or WhatsApp.</p>
""",
    },
    {
        "slug": "zijn-liquidatiepallets-de-moeite-waard",
        "title": "Are liquidation pallets worth it?",
        "date": "28 July 2026",
        "excerpt": "Only if the inputs are right: a manifest, a realistic exit price, freight and fallout. Without those, the low buy-in is a false advantage.",
        "image": "assets/products/pallet-tools.jpg",
        "body": """
<p>Liquidation gives access to branded stock at a fraction of retail. That gap is the margin — if you know what is inside.</p>
<h2>Work the lot through</h2>
<p>Take the expected sale price minus platform fees, freight, storage and any refurbishment. Divide by the piece count. If that number does not clear your hourly rate plus risk, leave the lot.</p>
<h2>Manifest or not</h2>
<p>Without a detailed rundown there is no reliable way to judge what you will receive. Lots without a list are labelled that way. Those are for sorting operations, not a first test.</p>
<p>Questions on a specific lot: Eu.wholesalestock@gmail.com or WhatsApp +49 1577 8431615.</p>
""",
    },
    {
        "slug": "amazon-pallets-met-of-zonder-manifest",
        "title": "Amazon pallets: with or without a manifest",
        "date": "21 July 2026",
        "excerpt": "FC gaylords with no list are a different product from an electronics lot with item lines. Buy the format that fits your operation.",
        "image": "assets/products/pallet-gaylord.jpg",
        "body": """
<p>Not every “Amazon pallet” is the same. Some lots come from return streams with an item file. Others are tall gaylords with no list, fixed price, meant for buyers who can sort.</p>
<h2>With a manifest</h2>
<p>Brand, model, condition grade and estimated MSRP per line where it applies. Suitable for listing in advance or for running your margin before you commit.</p>
<h2>Without a list</h2>
<p>High-count FC stacks: electronics, toys, bedding mixed together. No auction. Only worth it if you have space, time and a channel for remainder stock.</p>
<p>If you are unsure which format fits, email or message us before you order.</p>
""",
    },
    {
        "slug": "truckloads-wanneer-heeft-het-zin",
        "title": "Truckloads: when do they make sense?",
        "date": "14 July 2026",
        "excerpt": "Volume lowers the unit price, but it needs unload capacity, storage and cash flow. Truckloads at PalletHaven go through a conversation, not a click.",
        "image": "assets/products/truck-a.jpg",
        "body": """
<p>A truckload is not a larger shopping cart. It is a logistics agreement: load window, freight, an unload address with a forklift, and often several categories in one run.</p>
<h2>What you need ready</h2>
<p>Storage, sorting space and a plan for slow SKUs. If one pallet already stalls in your shed, wait before you take a full trailer.</p>
<h2>How you order</h2>
<p>We discuss truckloads first. Send category, volume and delivery address to Eu.wholesalestock@gmail.com or WhatsApp +49 1577 8431615. Standard pallets stay LTL to the curb.</p>
""",
    },
]


def euro(n):
    if n is None:
        return "—"
    return f"€{n:,.2f}"


def price_label(p):
    if p.get("priceMax") and p["priceMax"] > p["price"] + 0.01:
        return f"{euro(p['price'])} – {euro(p['priceMax'])}"
    return euro(p["price"])


def product_href(slug, prefix=""):
    return f"{prefix}product.html?p={slug}"


def src_img(path: str, prefix: str) -> str:
    if path.startswith("http"):
        return path
    return prefix + path


def header(prefix: str, active: str) -> str:
    links = "".join(
        f'<a href="{prefix}{href}" class="{"active" if active == href else ""}">{label}</a>'
        for href, label in NAV
    )
    mobile = "".join(f'<a href="{prefix}{href}">{label}</a>' for href, label in NAV)
    search_icon = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'''
    return f"""
<header class="site-header">
  <div class="topbar"><div class="container topbar-inner">
    <span>Order by email <a class="notranslate" href="{MAIL_HREF}">{EMAIL}</a> or WhatsApp <a class="notranslate" href="{WA_HREF}">{PHONE}</a> · Delivery across Europe. Free shipping in the Netherlands from €3,000.</span>
    <div class="translate-wrap notranslate" aria-label="Language">
      <label class="translate-label" for="site-lang">Language</label>
      <select id="site-lang" class="lang-select" data-site-lang>
        <option value="en">English</option>
        <option value="nl">Nederlands</option>
        <option value="de">Deutsch</option>
        <option value="fr">Français</option>
        <option value="es">Español</option>
        <option value="it">Italiano</option>
        <option value="pl">Polski</option>
        <option value="pt">Português</option>
        <option value="ro">Română</option>
        <option value="tr">Türkçe</option>
        <option value="ar">العربية</option>
        <option value="zh-CN">中文</option>
        <option value="ru">Русский</option>
        <option value="uk">Українська</option>
        <option value="sv">Svenska</option>
        <option value="da">Dansk</option>
        <option value="nb">Norsk</option>
        <option value="fi">Suomi</option>
        <option value="cs">Čeština</option>
        <option value="hu">Magyar</option>
        <option value="el">Ελληνικά</option>
        <option value="ja">日本語</option>
        <option value="ko">한국어</option>
        <option value="hi">हिन्दी</option>
        <option value="id">Indonesia</option>
        <option value="vi">Tiếng Việt</option>
        <option value="th">ไทย</option>
        <option value="bg">Български</option>
        <option value="hr">Hrvatski</option>
        <option value="sk">Slovenčina</option>
        <option value="sl">Slovenščina</option>
        <option value="lt">Lietuvių</option>
        <option value="lv">Latviešu</option>
        <option value="et">Eesti</option>
      </select>
    </div>
  </div></div>
  <div class="container header-main">
    <button class="menu-btn" data-menu aria-label="Menu">☰</button>
    <a class="logo notranslate" href="{prefix}index.html"><img src="{prefix}assets/logo.svg" alt="PalletHaven"></a>
    <form class="search-wrap" data-search>
      <label class="sr-only" for="q">Search</label>
      <input id="q" name="s" placeholder="Search…">
      <button type="submit" aria-label="Search">{search_icon}</button>
    </form>
    <div class="header-actions">
      <a class="account-link hide-sm" href="{prefix}account.html" data-open-login>LOGIN</a>
      <span class="header-divider hide-sm"></span>
      <a class="cart-link" href="{prefix}winkelwagen.html">
        <span class="cart-meta hide-sm">Cart / <span data-cart-total>€0.00</span></span>
        <span class="cart-icon"><strong data-cart-count>0</strong></span>
        <div class="mini-cart" data-mini-cart></div>
      </a>
    </div>
  </div>
  <nav class="nav-bar"><div class="container">{links}</div></nav>
  <div class="mobile-menu" data-mobile>{mobile}<a href="{prefix}account.html" data-open-login>LOGIN</a></div>
</header>"""


def footer(prefix: str) -> str:
    return f"""
<footer>
  <div class="container footer-grid">
    <div>
      <h4>PalletHaven</h4>
      <p>Wholesale liquidation pallets for resellers in the Netherlands and Europe. Manifest before purchase on every standard lot.</p>
      <p>Distelweg 72<br>1031 HH Amsterdam<br>The Netherlands</p>
    </div>
    <div>
      <h4>Navigate</h4>
      <a href="{prefix}winkel.html">Shop</a>
      <a href="{prefix}blog.html">Blog</a>
      <a href="{prefix}plaats-pallet.html">List a pallet</a>
      <a href="{prefix}over-ons.html">About us</a>
      <a href="{prefix}contact.html">Contact</a>
      <a href="{prefix}account.html">My account</a>
    </div>
    <div>
      <h4>Policies</h4>
      <a href="{prefix}privacybeleid.html">Privacy Policy</a>
      <a href="{prefix}algemene-voorwaarden.html">Terms and Conditions</a>
      <a href="{prefix}leveringsvoorwaarden.html">Shipping Terms</a>
      <a href="{prefix}disclaimer.html">Legal Disclaimer</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="{MAIL_HREF}">{EMAIL}</a>
      <a href="{WA_HREF}">WhatsApp {PHONE}</a>
      <p>Mon–Fri 09:00–17:00 CET<br>No walk-in, no pickup except truckloads by appointment.</p>
    </div>
  </div>
  <div class="copy">© 2026 PalletHaven. Wholesale liquidation pallets for the Netherlands and Europe.</div>
</footer>
<div id="google_translate_element" class="sr-only" hidden></div>
<div class="modal" id="quick-modal">
  <div class="modal-box">
    <img alt="">
    <div class="modal-body">
      <button class="close-x" data-close>×</button>
      <h3></h3>
      <p class="price" data-q-price></p>
      <p data-q-desc></p>
      <p class="form-note">Orders go by email or WhatsApp. Choose below.</p>
      <p><a class="btn btn-dark btn-block" data-q-mail>Order by email<br><small>{EMAIL}</small></a></p>
      <p><a class="btn btn-dark btn-block" data-q-wa>Order by WhatsApp<br><small>{PHONE}</small></a></p>
      <p><a data-q-link>View product</a></p>
    </div>
  </div>
</div>
<div class="modal" id="order-modal">
  <div class="auth-box" style="max-width:520px">
    <button class="close-x" data-close-order aria-label="Close">×</button>
    <h3>How do you want to order?</h3>
    <p>Orders go by email or WhatsApp. We do not take online payment. Send your order to <strong>{EMAIL}</strong> or WhatsApp <strong>{PHONE}</strong>.</p>
    <div data-order-prompt-body></div>
    <div class="order-via" style="margin-top:16px">
      <a class="btn btn-dark btn-block" data-order-mail>Order by email<br><small>{EMAIL}</small></a>
      <a class="btn btn-dark btn-block" data-order-wa>Order by WhatsApp<br><small>{PHONE}</small></a>
    </div>
  </div>
</div>
<div class="modal" id="login-modal">
  <div class="auth-box">
    <button class="close-x" data-close-auth aria-label="Close">×</button>
    <div class="auth-grid">
      <form data-login>
        <h3>Login</h3>
        <label>Username or email address *</label>
        <input name="email" type="email" required autocomplete="username">
        <label>Password *</label>
        <input name="password" type="password" required autocomplete="current-password">
        <p class="remember"><label><input type="checkbox" name="remember"> Remember me</label></p>
        <button class="btn btn-dark" type="submit">Log in</button>
        <div data-result></div>
      </form>
      <form data-register>
        <h3>Register</h3>
        <label>Name *</label>
        <input name="name" required autocomplete="name">
        <label>Email address *</label>
        <input name="email" type="email" required autocomplete="email">
        <label>Company name</label>
        <input name="company" autocomplete="organization">
        <label>Password *</label>
        <input name="password" type="password" required minlength="6" autocomplete="new-password">
        <label>Confirm password *</label>
        <input name="password2" type="password" required minlength="6" autocomplete="new-password">
        <p class="form-note">Your personal data is used to run your account and orders, as described in our <a href="{prefix}privacybeleid.html">privacy policy</a>.</p>
        <button class="btn btn-dark" type="submit">Create account</button>
        <div data-result></div>
      </form>
    </div>
  </div>
</div>"""


def page(title: str, prefix: str, active: str, body: str, extra_js: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} – PalletHaven</title>
  <meta name="description" content="PalletHaven supplies wholesale liquidation pallets to resellers in the Netherlands and Europe. Manifest before purchase, direct shipping.">
  <link rel="icon" href="{prefix}favicon.ico" sizes="any">
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{prefix}assets/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
  <link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
{header(prefix, active)}
<main>
{body}
</main>
{footer(prefix)}
<script>const ROOT = "{prefix}"; const CONTACT = {{email: "{EMAIL}", phone: "{PHONE}", wa: "{WA_NUM}"}}; const ADMIN = {{email: "{EMAIL.lower()}", hash: "{ADMIN_HASH}"}};</script>
<script src="{prefix}js/data.js"></script>
<script src="{prefix}js/app.js"></script>
{extra_js}
</body>
</html>
"""


def cards(slugs, prefix=""):
    html = ['<div class="product-grid">']
    for slug in slugs:
        p = PRODUCT_BY_SLUG.get(slug)
        if not p:
            continue
        cat = CAT_MAP[p["category"]]["name"]
        href = product_href(p["slug"], prefix)
        html.append(f"""
        <article class="product-card">
          <div class="thumb">
            <a href="{href}"><img src="{prefix}{p["image"]}" alt="{p["name"]}"></a>
            <button class="quick" data-quick="{p["slug"]}">Quick view</button>
          </div>
          <div class="info">
            <p class="product-cat">{cat}</p>
            <h3><a href="{href}">{p["name"]}</a></h3>
            <div class="price">{price_label(p)}</div>
            <button class="btn btn-dark btn-sm btn-block" type="button" data-order="{p["slug"]}">Order</button>
          </div>
        </article>""")
    html.append("</div>")
    return "\n".join(html)


def blog_card(post, prefix=""):
    href = f"{prefix}blog/{post['slug']}.html"
    return f"""
        <article class="blog-card">
          <a href="{href}"><img src="{prefix}{post['image']}" alt="{post['title']}"></a>
          <div class="body">
            <p class="meta">{post['date']}</p>
            <h3><a href="{href}">{post['title']}</a></h3>
            <p>{post['excerpt']}</p>
            <a class="btn btn-dark btn-sm" href="{href}">Read article</a>
          </div>
        </article>"""


def blog_grid(posts, prefix="", limit=None):
    shown = posts[:limit] if limit else posts
    return '<div class="blog-grid">' + "".join(blog_card(p, prefix) for p in shown) + "</div>"


def blog_index_page():
    return f"""
<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="index.html">Home</a> / Blog</div>
  <h1>Blog</h1>
  <p>Anyone can post a blog article here. No account needed. Write below and your article appears with the rest of the posts.</p>
</div></section>
<section class="section" id="plaats-blog">
  <div class="container">
    <form class="blog-composer" data-post-blog>
      <h2>Post your blog article</h2>
      <p>Title, text and an optional photo. After you publish, your article appears at the top of the blog.</p>
      <label>Article title *</label>
      <input name="title" required maxlength="140" placeholder="e.g. My first pallet in the Netherlands">
      <label>Your article *</label>
      <textarea name="body" required placeholder="Write your article here. Anyone on the blog can read it afterwards."></textarea>
      <label>Photo (optional)</label>
      <input name="photo" type="file" accept="image/*">
      <div class="row">
        <div><label>Your name *</label><input name="name" required autocomplete="name"></div>
        <div><label>Email *</label><input name="email" type="email" required autocomplete="email"></div>
      </div>
      <p class="form-note">Questions: <a href="{MAIL_HREF}">{EMAIL}</a> or WhatsApp <a href="{WA_HREF}">{PHONE}</a>.</p>
      <p><button class="btn btn-dark btn-block" type="submit">Publish blog article</button></p>
      <div data-result></div>
    </form>
  </div>
</section>
<section class="section alt"><div class="container">
  <h2 class="section-title">All blog posts</h2>
  <p class="lead">Posted articles sit at the top, followed by PalletHaven guides.</p>
  <div class="blog-admin" data-blog-admin></div>
  <div class="blog-grid" data-blog-grid></div>
</div></section>
"""


def blog_post_page(post):
    return f"""
<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="../index.html">Home</a> / <a href="../blog.html">Blog</a> / {post['title']}</div>
  <h1>{post['title']}</h1>
  <p>{post['date']}</p>
</div></section>
<section class="section"><div class="container prose blog-article" data-editorial-slug="{post['slug']}">
  <img class="featured" src="../{post['image']}" alt="{post['title']}">
  {post['body']}
  <p class="hero-actions" style="justify-content:flex-start;margin-top:28px">
    <a class="btn btn-dark" href="{MAIL_HREF}">Order by email</a>
    <a class="btn btn-dark" href="{WA_HREF}">Order by WhatsApp</a>
    <a class="btn btn-sm" href="../blog.html">Back to blog</a>
  </p>
  <div class="blog-admin" data-blog-admin data-delete-slug="{post['slug']}"></div>
</div></section>
"""


def home_grid(slug, title):
    return f"""
<section class="section">
  <div class="container">
    <h2 class="section-title">{title}</h2>
    {cards(by_category(PRODUCTS, slug, 8))}
    <p class="grid-more"><a class="btn btn-dark" href="categorie/{slug}.html">View all {CAT_MAP[slug]["name"]}</a></p>
  </div>
</section>"""


def homepage():
    cats = "".join(
        f"""<article class="cat-card">
          <a href="categorie/{c["slug"]}.html"><img src="{c["image"]}" alt="{c["name"]}"></a>
          <div class="body">
            <h3><a href="categorie/{c["slug"]}.html">{c["name"]}</a></h3>
            <p>{c["blurb"]}</p>
            <a class="btn btn-dark btn-sm" href="categorie/{c["slug"]}.html">View category</a>
          </div>
        </article>"""
        for c in CATEGORIES
    )
    return f"""
<section class="hero" style="background-image:url('{IMG["hero"]}')">
  <div class="hero-inner">
    <h1>Wholesale liquidation pallets for the Netherlands and Europe — branded goods, full manifest, direct delivery</h1>
    <p>Buy wholesale liquidation pallets in the categories resellers actually move: electronics, sneakers, apparel, fragrance, tools, home appliances, building sets and mystery boxes. Every manifest lot shows the mix before you buy. Order by email or WhatsApp: <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> · <a href="https://wa.me/4915778431615">+49 1577 8431615</a></p>
    <div class="hero-actions">
      <a class="btn btn-light" href="winkel.html">Shop all pallets</a>
      <a class="btn btn-outline" href="contact.html">Order by email / WhatsApp</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container features">
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="7" width="13" height="10" rx="1"/><path d="M16 10h3l2 3v4h-5"/><circle cx="7.5" cy="18.5" r="1.5" fill="#fff" stroke="none"/><circle cx="18.5" cy="18.5" r="1.5" fill="#fff" stroke="none"/></svg></div><h3>Priority shipping</h3><p>Fast shipping across the Netherlands and the rest of Europe, with reliable freight partners.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg></div><h3>Clear terms</h3><p>Review manifest lots before you pay. Salvage, mystery and high-count lots ship as-is.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="4" y="11" width="16" height="9" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div><h3>Order by email or WhatsApp</h3><p>No online checkout. Send your order to Eu.wholesalestock@gmail.com or WhatsApp +49 1577 8431615. Payment after that by bank transfer or Revolut.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><path d="M12 3l8 4v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg></div><h3>Verified brand sources</h3><p>Overstock, surplus and return streams through retail and distribution channels. No replica lots.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M8 8h8M8 12h8M8 16h5"/></svg></div><h3>Full manifest before you buy</h3><p>Brand, model, condition grade and estimated MSRP per line where it applies.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="10" width="7" height="10"/><rect x="14" y="10" width="7" height="10"/><path d="M7 10V7a5 5 0 0 1 10 0v3"/></svg></div><h3>B2B and export ready</h3><p>Invoice, packing list and export documents for business buyers in the EU.</p></article>
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>What is PalletHaven?</h2>
    <p>PalletHaven is a wholesale platform for liquidation pallets. We supply professional resellers, eBay.de and Amazon.de sellers, boutique retailers, market operators, B2B distributors and export traders in the Netherlands, Germany, Belgium and across Europe.</p>
    <p>We source overstock, distributor surplus, seasonal clearance and consumer returns from North American and European retail distribution networks. Buying direct cuts out middle layers. You keep more margin.</p>
    <p>On every manifest lot you see brand, model, condition grade, size range where it applies and estimated MSRP before you commit. Blind boxes are not the default. High-count gaylords and mystery boxes without a list are labelled that way.</p>
  </div>
</section>

<section class="section">
  <div class="container prose">
    <h2>Our product categories</h2>
    <h3>Electronics liquidation pallets</h3>
    <p>Return electronics and overstock in audio, monitors, IT and smart home. From 9-piece cartons to 43-piece pallets to truckloads. Tested working or new sealed, listed accurately. Built for eBay.de, Amazon.de FBA, Back Market and B2B distributors.</p>
    <h3>Sneaker liquidation pallets</h3>
    <p>Sport and lifestyle footwear with brand, model, colorway and size run before you buy. Mass-market, premium lifestyle and limited-release lots. For eBay.de, Vinted, StockX-style channels and sneaker boutiques.</p>
    <h3>Amazon high-count FC pallets</h3>
    <p>High Count FC gaylords, 1.8 to 2.1 metre stacks of mixed merchandise from fulfillment returns. Electronics, toys, bedding and more. No manifest. Fixed price, no auction. For experienced sorters only.</p>
    <h3>iPhone and smartphone pallets</h3>
    <p>New sealed, Grade A refurbished and consumer returns. Manifest with model, storage, color, condition and battery health. For iPhone sellers, refurbishers and business buyers.</p>
    <h3>Home appliances</h3>
    <p>Coffee machines, vacuums, mixers, blenders and air fryers. Condition grade per unit. For marketplace sellers, housewares shops and weekly markets.</p>
    <h3>Apparel and fashion</h3>
    <p>Branded clothing, warehouse fashion, gym wear and bags. New with tags or overstock. Lots from 250 pieces to full pallets.</p>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2 class="section-title">How PalletHaven works</h2>
    <div class="steps">
      <article class="step"><b>1</b><h3>Pick a category</h3><p>Review brand mix, condition and expected MSRP on the category page.</p></article>
      <article class="step"><b>2</b><h3>Request the manifest</h3><p>Email Eu.wholesalestock@gmail.com. You get the item lines before payment.</p></article>
      <article class="step"><b>3</b><h3>Run your margin</h3><p>Compare recent solds on eBay.de, Amazon.de or Back Market minus freight.</p></article>
      <article class="step"><b>4</b><h3>Order by email or WhatsApp</h3><p>No online payment. Send the order to Eu.wholesalestock@gmail.com or WhatsApp +49 1577 8431615.</p></article>
      <article class="step"><b>5</b><h3>Receive and sell</h3><p>Professionally wrapped, with tracking, ready to test and list.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Our best-selling pallets</h2>
    {cards(by_category(PRODUCTS, "keuken", 1) + by_category(PRODUCTS, "pokemon", 1) + by_category(PRODUCTS, "cosmetica", 1) + by_category(PRODUCTS, "elektronica", 1) + by_category(PRODUCTS, "mystery-box", 1) + by_category(PRODUCTS, "koelkast", 1) + by_category(PRODUCTS, "gereedschap", 1) + by_category(PRODUCTS, "iphone", 1))}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Why Dutch and European resellers choose PalletHaven</h2>
    <p>Because on standard lots you know the mix before you pay: brand, model, condition grade and estimated MSRP per unit. Most European brokers show that only after purchase. Here the manifest is the default.</p>
    <p>Stock comes from overstock, surplus and return channels. No fakes to fill pallets. New sealed is new sealed. Tested working is functionally checked. Returns list a realistic fallout rate. Salvage is salvage.</p>
    <p>We ship to the Netherlands (3–7 working days) and the rest of Europe (5–14 working days). Import duties and VAT outside our invoice are for the buyer. Volume and truckloads via Eu.wholesalestock@gmail.com.</p>
  </div>
</section>

{home_grid("high-count", "Shop Amazon clearance pallets.")}

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Who PalletHaven is for</h2>
    <div class="audience">
      <article><h3>eBay.de and Amazon.de FBA</h3><p>Branded electronics, footwear, apparel, tools and home appliances with identifiers so you can list in advance.</p></article>
      <article><h3>Boutiques and outlets</h3><p>Shops in the NL and DE that want branded stock under ticket price without standard wholesale minimums.</p></article>
      <article><h3>Weekly markets and pop-ups</h3><p>Volume at a low unit cost for face-to-face sales to buyers who respond to brand value.</p></article>
      <article><h3>Distributors and export</h3><p>Lots you split to local retailers or export onward inside the EU.</p></article>
    </div>
  </div>
</section>

{home_grid("pokemon", "Shop Pokémon clearance pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>Ready to start? Here is what you do</h2>
    <p>PalletHaven is online only. No walk-in and no pickup on standard pallets. Browse the category pages, click Order, and send the order by email (Eu.wholesalestock@gmail.com) or WhatsApp (+49 1577 8431615). You get the manifest, check your exit prices and confirm. For truckloads we agree freight and load date first.</p>
  </div>
</section>

{home_grid("gereedschap", "Shop mixed tool stock pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>Shipping information</h2>
    <p>Orders in the Netherlands go by insured LTL pallet freight, 3 to 7 working days after confirmation, to every province including North Holland, South Holland, Utrecht, North Brabant, Gelderland, Overijssel, Groningen, Friesland and Zeeland.</p>
    <p>European deliveries cover Germany, Belgium, France, the United Kingdom, Spain, Italy, Poland, Austria, Denmark, Sweden and other EU destinations, 5 to 14 working days. Customs, import and local VAT are for the buyer. We include the documents.</p>
    <p>No local pickup, except container and truckload orders by appointment.</p>
  </div>
</section>

{home_grid("sneakers", "Shop surplus sneaker pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>What is a liquidation pallet?</h2>
    <p>A liquidation pallet is a bundle of merchandise that a retailer or manufacturer moves into wholesale: overstock, seasonal clearance or return stock. Resellers buy that bundle below retail and sell piece by piece through webshops, markets or physical stores.</p>
    <p>The advantage is access to brands without a full wholesale catalog. Testing new categories without locking in large volumes is part of that. Many buyers start with one or two pallets and grow to multi-pallet or truckload.</p>
    <p>The risk is condition variation. That is why we issue a line-by-line rundown on standard lots. A high-count with no list is a different product, at a different price, for a different buyer.</p>
    <p>Buyers pay a fraction of original retail. Low buy-in plus market-rate selling is a growth model for SMEs in the Netherlands and Europe.</p>
  </div>
</section>

{home_grid("kleding", "Shop mixed apparel pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>Liquidation pallet flipping: side income or full-time business?</h2>
    <p>As a side income you test the market with minimal risk, in evenings or weekends. Full-time offers more scale — from a few pallets to truckloads — but it needs cash flow, storage and a fixed buying plan.</p>
    <p>Most successful resellers start with one or two manifest lots, build their sort-and-list system, and scale in a controlled way. PalletHaven is built for both tempos: small cartons to test and truckloads when the operation can take them.</p>
  </div>
</section>

{home_grid("keuken", "Shop home and kitchen appliance pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>Is buying liquidation pallets worth it?</h2>
    <p>Only if the inputs are right. Liquidation gives access to branded stock at a fraction of retail. That gap is the margin. Without a detailed manifest there is no reliable way to judge what you will receive. Work expected sale price minus platform fees, freight, storage and refurbishment. If a supplier cannot produce a manifest on a lot sold as a manifest lot, that is a reason to stop.</p>
  </div>
</section>

{home_grid("amazon-mystery", "Shop mystery-box pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>Liquidation sales: margin for resellers in the Netherlands and Europe</h2>
    <p>Liquidation happens when retailers, manufacturers or distributors move surplus stock, seasonal clearance or return streams. Wholesale prices typically sit 40 to 60 percent under original retail. That leaves room on eBay.de, Amazon.de, Back Market and in physical shops.</p>
    <h3>The wholesale buying advantage</h3>
    <p>Bulk buying through liquidation channels delivers a lower unit cost than regular wholesale. Branded stock at liquidation prices cuts your buy-in without giving up recognisability. Lots often consist of factory-new units, new with tags, or lightly used A-brands.</p>
    <h3>Benefits for retailers and resellers</h3>
    <p>A broad mix from one purchase widens your sales potential and reduces dependence on a single category. Low buy-in plus market-rate selling makes margins that standard wholesale rarely hits. Buying overstock also keeps usable products out of the shredder.</p>
    <p>PalletHaven ships lots with a manifest where promised, condition grading and direct freight. Whether you test one pallet or buy truckload volume, the lot structure is the same.</p>
  </div>
</section>

{home_grid("amazon-electronics", "Shop mixed general merchandise pallets.")}

<section class="section alt">
  <div class="container prose">
    <h2>The difference between pallet flipping and a real resale business</h2>
    <p>Pallet flipping feels low-friction until volume grows: capital sits longer, storage fills up and decisions stack. Some pallets move fast, others sit. That needs repricing and reshuffling. The problem is rarely effort. It is the lack of a buying plan.</p>
    <h3>Reactive buying</h3>
    <p>Reactive buying — chasing deals because they look attractive right now — produces inconsistent margins. One purchase performs, the next does not. Cash flow becomes unpredictable and storage fills faster than planned.</p>
    <h3>Building a business</h3>
    <p>A resale business buys on market demand, price structure and realistic sell-through timelines. Categories are chosen because they perform consistently, not because they are trending. Margins are known before the stock arrives.</p>
    <p>PalletHaven supplies the lot structure for that: manifests, condition grading and recurring availability, from one pallet to a truckload.</p>
  </div>
</section>

{home_grid("bouwsets", "Shop LEGO clearance pallets.")}
{home_grid("cosmetica", "Shop cosmetic liquidation pallets.")}
{home_grid("iphone", "Shop iPhone liquidation pallets.")}
{home_grid("airco", "Shop air-conditioner pallets.")}
{home_grid("winterschoenen", "Shop winter shoe pallets.")}
{home_grid("parfum", "Shop fragrance liquidation pallets.")}
{home_grid("speelgoed", "Shop toy clearance pallets.")}
{home_grid("handtassen", "Shop women's handbag pallets.")}
{home_grid("truckload", "Shop truckloads and multi-pallet volume.")}

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Blog</h2>
    <p class="lead">Articles on buying, ordering by email or WhatsApp, and running a liquidation trade.</p>
    <div class="blog-grid" data-blog-home></div>
    <p class="grid-more">
      <a class="btn btn-dark" href="blog.html#plaats-blog">Post your blog article</a>
      <a class="btn btn-sm" href="blog.html">All blog posts</a>
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">All categories</h2>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Testimonials</h2>
    <p class="lead">What our customers say</p>
    <div class="reviews">
      <article class="review"><div class="stars">★★★★★</div><p>Pallets arrived as described, well packed, smooth delivery across Europe. Clear communication.</p><cite>Thomas de Vries — Eindhoven</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Electronics lot was authentic, the manifest matched. Profit potential was real. Ordered again.</p><cite>Lea Hoffmann — Düsseldorf</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Sneakers mostly new in box. Freight to Rotterdam was clear up front.</p><cite>Samir El Idrissi — Rotterdam</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Beauty pallet was clean, sealed and ready to resell. Fair wholesale price.</p><cite>Nina Bakker — Utrecht</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>High-count is not for beginners, and they said so. For our sorting operation it fits.</p><cite>Marco Bianchi — Milan</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Tracking was accurate. Invoice and packing list complete for the books.</p><cite>Sophie Laurent — Lille</cite></article>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container contact-grid">
    <div>
      <h2>Send us a message</h2>
      <p>Questions about a lot, a manifest or freight? We reply on working days.</p>
      <form data-contact>
        <div class="row"><div><label>Your name</label><input name="name" required></div><div><label>Your email address</label><input type="email" name="email" required></div></div>
        <label>Subject</label><input name="subject" required>
        <label>Your message</label><textarea name="message"></textarea>
        <p><button class="btn btn-dark" type="submit">Send</button></p>
        <div data-result></div>
      </form>
    </div>
    <div class="faq">
      <h2>Frequently asked questions about our liquidation pallets</h2>
      <details open><summary>How do I order?</summary><p>Orders go by email or WhatsApp, not through an online checkout. Click Order on a lot and choose <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> or WhatsApp <a href="https://wa.me/4915778431615">+49 1577 8431615</a>. We confirm the lot and freight, then you pay by bank transfer or Revolut.</p></details>
      <details><summary>Is PalletHaven a verified business?</summary><p>PalletHaven is a wholesale platform that supplies resellers, retailers, B2B distributors and exporters in the Netherlands, Germany, Belgium and across Europe.</p></details>
      <details><summary>Does PalletHaven provide a manifest before purchase?</summary><p>Yes, on every manifest lot. Brand, model, condition grade, size range where it applies and estimated MSRP follow before payment. No-manifest lots such as high-count gaylords are clearly labelled that way.</p></details>
      <details><summary>Which categories are available?</summary><p>Electronics, sneakers, apparel, fragrance, tools, home appliances, smartphones, building sets, TCG, mystery boxes, air-con, truckloads and more. The shop lists 10,000 live lots.</p></details>
      <details><summary>Do you ship to Germany and the rest of Europe?</summary><p>Yes. Import duties, VAT and customs on international orders are for the buyer.</p></details>
      <details><summary>Are there local pickup options?</summary><p>Not on standard pallets. Truckloads possible by appointment.</p></details>
      <details><summary>What is the minimum order?</summary><p>The smallest lot in the shop. Volume via Eu.wholesalestock@gmail.com.</p></details>
      <details><summary>Are returns accepted?</summary><p>Sale is final after shipment, except for a proven shipping error or a lot that materially differs from the confirmed manifest.</p></details>
      <details><summary>What are the best lots for beginners in the Netherlands?</summary><p>Manifest-verified single-category lots: small electronics cartons, fragrance or 120-pair shoes. Not a high-count gaylord as a first purchase.</p></details>
      <details><summary>What are wholesale liquidation pallets for the Netherlands and Europe?</summary><p>Bulk lots of consumer goods from return channels, retailer overstock, seasonal clearance and distributor surplus, sold below retail to professional resellers. PalletHaven issues a manifest before purchase on every lot labelled as a manifest lot.</p></details>
      <details><summary>How does PalletHaven differ from other suppliers?</summary><p>We price in euro, state condition honestly (returns are returns, salvage is salvage) and do not inflate the brand mix. High-count with no list is labelled that way.</p></details>
      <details><summary>Are these pallets profitable for resellers?</summary><p>For buyers with a sales channel and the capacity to process the chosen category. Recognisable brands draw demand on eBay.nl, eBay.de and Amazon.nl. Results depend on your price, freight and fallout.</p></details>
      <details><summary>Which categories are available for the Dutch market?</summary><p>Electronics, toys, Amazon returns, handbags, winter shoes, sneakers, apparel, fragrance, tools, home appliances, building sets, TCG and truckloads. Each category page shows live lots with EUR prices.</p></details>
      <details><summary>Do you offer pallets with a manifest?</summary><p>Yes, on standard lots: item lines, identifiers where available and estimated MSRP. For some high-count formats the file is on request via Eu.wholesalestock@gmail.com.</p></details>
      <details><summary>How long does delivery take?</summary><p>Netherlands 3 to 7 working days. EU 7 to 14 working days. Larger monitor pallets can take 10 to 21 days.</p></details>
      <details><summary>Do you offer local pickup or warehouse sales in the Netherlands?</summary><p>No, except truckloads by appointment. Standard pallets go to the stated delivery address.</p></details>
      <details><summary>Are these pallets suitable for beginner resellers?</summary><p>Some lots are: toys, small smart-home cartons and handbags. Salvage monitor pallets are for technicians. High-count gaylords are not a starter product.</p></details>
    </div>
  </div>
</section>
"""


def shop_page(title, crumbs, category=None, intro=""):
    cat_links = "".join(
        f'<a href="{"../" if category else ""}categorie/{c["slug"]}.html" class="{"active" if category==c["slug"] else ""}">{c["name"]}<span>{sum(1 for p in PRODUCTS if p["category"]==c["slug"])}</span></a>'
        for c in CATEGORIES
    )
    prefix = "../" if category else ""
    data_cat = f'data-category="{category}"' if category else ""
    return f"""
<section class="page-hero"><div class="container">
  <div class="crumbs">{crumbs}</div>
  <h1>{title}</h1>
  {f"<p>{intro}</p>" if intro else ""}
</div></section>
<section class="section"><div class="container shop-layout">
  <aside class="sidebar">
    <h4>Categories</h4>
    <a href="{prefix}winkel.html">All pallets</a>
    {cat_links}
  </aside>
  <div>
    <div class="toolbar">
      <div data-result-count></div>
      <div data-search-hint></div>
      <label>Sort
        <select data-sort>
          <option value="featured">Featured</option>
          <option value="price-asc">Price low–high</option>
          <option value="price-desc">Price high–low</option>
          <option value="name">Name</option>
        </select>
      </label>
    </div>
    <div class="product-grid" data-shop-grid {data_cat}></div>
    <div class="pager" data-pager></div>
  </div>
</div></section>
"""


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    data = {
        "CATEGORIES": [{k: c[k] for k in ("slug", "name", "image", "blurb")} for c in CATEGORIES],
        "PRODUCTS": PRODUCTS,
    }
    js = "const CATEGORIES=" + json.dumps(data["CATEGORIES"], ensure_ascii=False, separators=(",", ":")) + ";\n"
    js += "const PRODUCTS=" + json.dumps(data["PRODUCTS"], ensure_ascii=False, separators=(",", ":")) + ";\n"
    blog_public = [{k: p[k] for k in ("slug", "title", "date", "excerpt", "image")} for p in BLOG_POSTS]
    js += "const BLOG_POSTS=" + json.dumps(blog_public, ensure_ascii=False, separators=(",", ":")) + ";\n"
    write(ROOT / "js" / "data.js", js)
    print(f"Wrote catalog: {len(PRODUCTS)} products, {len(CATEGORIES)} categories, data.js { (ROOT/'js'/'data.js').stat().st_size // 1024 } KB")

    write(ROOT / "index.html", page("Home", "", "index.html", homepage()))
    write(ROOT / "winkel.html", page("Shop", "", "winkel.html", shop_page(
        "Shop", "Home / Shop",
        intro=f"All {len(PRODUCTS):,} available liquidation pallets. Filter by category or search by keyword.".replace(",", ","),
    )))

    cat_dir = ROOT / "categorie"
    keep = {c["slug"] + ".html" for c in CATEGORIES}
    if cat_dir.exists():
        for f in cat_dir.glob("*.html"):
            if f.name not in keep:
                f.unlink()
    for c in CATEGORIES:
        body = shop_page(
            c["name"],
            f'<a href="../index.html">Home</a> / <a href="../winkel.html">Shop</a> / {c["name"]}',
            category=c["slug"],
            intro=c["blurb"],
        )
        write(ROOT / "categorie" / f"{c['slug']}.html", page(c["name"], "../", "winkel.html", body))

    shutil.rmtree(ROOT / "product", ignore_errors=True)
    write(ROOT / "product.html", page("Product", "", "winkel.html", """
<section class="page-hero"><div class="container">
  <div class="crumbs" data-product-crumbs></div>
</div></section>
<section class="section"><div class="container" data-product-page>
  <p>Loading product…</p>
</div></section>
"""))

    write(ROOT / "blog.html", page("Blog", "", "blog.html", blog_index_page()))
    blog_dir = ROOT / "blog"
    keep_posts = {p["slug"] + ".html" for p in BLOG_POSTS}
    if blog_dir.exists():
        for f in blog_dir.glob("*.html"):
            if f.name not in keep_posts:
                f.unlink()
    for post in BLOG_POSTS:
        write(blog_dir / f"{post['slug']}.html", page(post["title"], "../", "blog.html", blog_post_page(post)))
    write(ROOT / "bericht.html", page("Blog post", "", "blog.html", """
<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="index.html">Home</a> / <a href="blog.html">Blog</a></div>
  <h1 data-blog-title>Blog post</h1>
</div></section>
<section class="section"><div class="container prose blog-article" data-blog-article>
  <p>Loading post…</p>
</div>
<div class="container"><div class="blog-admin" data-blog-admin></div></div>
</section>
"""))

    write(ROOT / "contact.html", page("Contact us", "", "contact.html", """
<section class="page-hero"><div class="container"><h1>Contact us</h1>
<p>Order and request quotes by email or WhatsApp. We reply on working days.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div>
    <h2>Send us a message</h2>
    <div class="order-via">
      <p><a class="btn btn-dark" href="mailto:Eu.wholesalestock@gmail.com">Email Eu.wholesalestock@gmail.com</a></p>
      <p><a class="btn btn-dark" href="https://wa.me/4915778431615">WhatsApp +49 1577 8431615</a></p>
    </div>
    <form data-contact>
      <div class="row"><div><label>Your name</label><input name="name" required></div><div><label>Your email address</label><input type="email" required></div></div>
      <label>Subject</label><input name="subject" required>
      <label>Your message</label><textarea name="message"></textarea>
      <p><button class="btn btn-dark" type="submit">Send</button></p>
      <div data-result></div>
    </form>
  </div>
  <div>
    <h2>Details</h2>
    <dl class="info-list">
      <dt>Address</dt><dd>Distelweg 72, 1031 HH Amsterdam, The Netherlands</dd>
      <dt>Opening hours</dt><dd>Not open to the public. Pickup only on truckloads by appointment.</dd>
      <dt>Email</dt><dd><a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a></dd>
      <dt>WhatsApp</dt><dd><a href="https://wa.me/4915778431615">+49 1577 8431615</a></dd>
    </dl>
  </div>
</div></section>
"""))

    write(ROOT / "plaats-pallet.html", page("List a pallet", "", "plaats-pallet.html", """
<section class="page-hero"><div class="container">
  <h1>List a pallet</h1>
  <p>Anyone can list their own liquidation pallet or lot here. After you publish, your listing appears on this page and in the shop.</p>
</div></section>
<section class="section"><div class="container contact-grid">
  <form data-post-pallet>
    <h2>List a new pallet</h2>
    <label>Lot title *</label>
    <input name="title" required placeholder="e.g. Branded clothing pallet 250 pcs">
    <label>Category *</label>
    <select name="category" required></select>
    <div class="row">
      <div><label>Price in euro *</label><input name="price" type="number" min="1" step="0.01" required></div>
      <div><label>Piece count</label><input name="items" type="number" min="1"></div>
    </div>
    <label>Description *</label>
    <textarea name="description" required placeholder="What is in the lot, condition, location"></textarea>
    <label>Photo of your pallet</label>
    <input name="photo" type="file" accept="image/*">
    <div class="row">
      <div><label>Your name *</label><input name="name" required></div>
      <div><label>Email *</label><input name="email" type="email" required></div>
    </div>
    <label>Phone / WhatsApp</label>
    <input name="phone" placeholder="+49 …">
    <p class="form-note">Questions about listing: <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> or WhatsApp <a href="https://wa.me/4915778431615">+49 1577 8431615</a>.</p>
    <p><button class="btn btn-dark" type="submit">Publish pallet</button></p>
    <div data-result></div>
  </form>
  <div>
    <h2>Public listings</h2>
    <div class="product-grid" data-community-grid></div>
  </div>
</div></section>
"""))

    write(ROOT / "over-ons.html", page("About us", "", "over-ons.html", """
<section class="page-hero"><div class="container"><h1>About PalletHaven</h1></div></section>
<section class="section"><div class="container prose legal">
  <p>PalletHaven is a wholesale platform for liquidation and overstock pallets. We exist to give buyers in the Netherlands and Europe branded stock at prices where resale still works, with product information before purchase.</p>
  <h2>What we supply</h2>
  <p>Consumer electronics, smartphones, apparel, footwear, tools, fragrance, home appliances, toys and mixed lots. Most units are new or tagged. Returns and salvage are stated as such on the lot.</p>
  <h2>The Netherlands as a core market</h2>
  <p>We deliver in every province. The local resale market wants recognisable brands, clean condition grades and identifiers you can list. That is what we buy against.</p>
  <h2>Europe</h2>
  <p>Germany, Belgium, France, the UK, Spain, Italy, Poland and other EU countries. Lead time 5–14 working days. Customs and local charges are for the buyer. We supply the paperwork.</p>
  <h2>How we work</h2>
  <p>Lot online, manifest where promised, payment after confirmation, shipping within 1–2 working days, tracking per shipment. Sale is final after dispatch, except for a material difference from the confirmed file.</p>
</div></section>
"""))

    write(ROOT / "privacybeleid.html", page("Privacy Policy", "", "privacybeleid.html", """
<section class="page-hero"><div class="container"><h1>Privacy Policy</h1></div></section>
<section class="section"><div class="container legal">
  <p>PalletHaven, Distelweg 72, 1031 HH Amsterdam, processes personal data to handle orders, quotes and customer accounts.</p>
  <h2>What data</h2>
  <p>Name, email, phone, delivery address, company details, registration/VAT number and correspondence. Payment proofs from bank transfer or Revolut.</p>
  <h2>Purposes</h2>
  <p>Performance of the contract, legal bookkeeping duties, fraud prevention and — only with consent — messages about new lots.</p>
  <h2>Retention</h2>
  <p>Order data for seven years in the accounts. Accounts until closure plus a reasonable aftercare period.</p>
  <h2>Sharing</h2>
  <p>Carriers, payment providers and IT hosting, limited to what is needed. No sale of mailing lists.</p>
  <h2>Rights</h2>
  <p>Access, correction, erasure, restriction and objection via Eu.wholesalestock@gmail.com. Complaints may go to the Dutch Data Protection Authority (Autoriteit Persoonsgegevens).</p>
  <h2>Cookies</h2>
  <p>This demo site uses local storage for the cart. No tracking pixel runs.</p>
</div></section>
"""))

    write(ROOT / "algemene-voorwaarden.html", page("Terms and Conditions", "", "algemene-voorwaarden.html", """
<section class="page-hero"><div class="container"><h1>Terms and Conditions</h1></div></section>
<section class="section"><div class="container legal">
  <h2>1. Applicability</h2>
  <p>These terms apply to all quotes and deliveries from PalletHaven to business buyers. Distance-sale consumer protection does not apply to B2B liquidation.</p>
  <h2>2. Offer and manifest</h2>
  <p>Prices in euro, excluding freight unless stated otherwise. A lot is a snapshot. Availability can change until confirmation. On manifest lots the file we send prevails over the product page.</p>
  <h2>3. Payment</h2>
  <p>Advance payment by bank transfer or Revolut after lot confirmation. Title passes after full payment.</p>
  <h2>4. Condition</h2>
  <p>Liquidation stock is mixed by definition. Salvage, returns and high-count with no list are sold as-is. Buyers inspect the manifest before they agree.</p>
  <h2>5. Delivery</h2>
  <p>Lead times are indicative. Risk passes on handover to the carrier unless otherwise agreed. Report arrival damage in writing within 24 hours with photos of wrapping and pallet.</p>
  <h2>6. Cancellation</h2>
  <p>No right of withdrawal after shipment. Exception: a proven lot mix-up or a material difference from the confirmed manifest.</p>
  <h2>7. Liability</h2>
  <p>Liability is limited to the invoice amount of the lot concerned, except in cases of intent or gross negligence.</p>
  <h2>8. Law</h2>
  <p>Dutch law. Competent court: Amsterdam.</p>
</div></section>
"""))

    write(ROOT / "leveringsvoorwaarden.html", page("Shipping Terms", "", "leveringsvoorwaarden.html", """
<section class="page-hero"><div class="container"><h1>Shipping Terms</h1></div></section>
<section class="section"><div class="container legal">
  <p>PalletHaven ships pallets through LTL freight partners. Standard pallets are not collected on site.</p>
  <h2>The Netherlands</h2>
  <p>3 to 7 working days after order confirmation. Free shipping from €3,000 to a Dutch address, unless the lot is marked as truckload or extra volume.</p>
  <h2>Europe</h2>
  <p>5 to 14 working days. Larger formats can take 10 to 21 days. Import, customs and VAT are for the buyer. We supply invoice and packing list.</p>
  <h2>Delivery</h2>
  <p>Delivery to the curb or loading dock, depending on the location. A forklift or pallet jack on the receiving side is your responsibility. A failed delivery due to inaccessibility may incur extra costs.</p>
  <h2>Damage</h2>
  <p>Note visible transit damage on the consignment note and email photos within 24 hours to Eu.wholesalestock@gmail.com.</p>
</div></section>
"""))

    write(ROOT / "disclaimer.html", page("Legal Disclaimer", "", "disclaimer.html", """
<section class="page-hero"><div class="container"><h1>Legal Disclaimer</h1></div></section>
<section class="section"><div class="container legal">
  <p>Information on this website is intended for business buyers of liquidation stock. Listings, manifests and prices can change. We work for accuracy but do not guarantee that every page is error-free at all times.</p>
  <p>Brand names are used only to identify the goods. PalletHaven is not affiliated with those brands unless expressly stated.</p>
  <p>Resale results depend on your channels, prices and processing. Earlier lots are not a guarantee of future mix.</p>
  <p>This site is a static demonstration of a wholesale shop. Do not place real payments based on this demo without a separate written confirmation.</p>
</div></section>
"""))

    write(ROOT / "winkelwagen.html", page("Cart", "", "winkelwagen.html", """
<section class="page-hero"><div class="container"><h1>Cart</h1>
<p>Order the selected pallets by email or WhatsApp.</p></div></section>
<section class="section"><div class="container">
  <div data-cart-table></div>
  <div data-cart-totals></div>
</div></section>
"""))

    write(ROOT / "afrekenen.html", page("Checkout", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>Order by email or WhatsApp</h1>
<p>Choose how you send the order. Nothing is charged automatically.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div>
    <h2>How do you want to order?</h2>
    <p>Send your order to <strong>Eu.wholesalestock@gmail.com</strong> or WhatsApp <strong>+49 1577 8431615</strong>. Fill in your details below and click one of the buttons.</p>
    <form data-checkout>
      <div class="row"><div><label>Company name</label><input name="company"></div><div><label>Company registration no.</label><input name="kvk"></div></div>
      <div class="row"><div><label>Contact person</label><input name="name" required></div><div><label>Email</label><input name="email" type="email" required></div></div>
      <label>Phone</label><input name="phone" required>
      <label>Delivery address</label><input name="address" required>
      <div class="row"><div><label>Postcode</label><input name="zip" required></div><div><label>City</label><input name="city" required></div></div>
      <label>Country</label>
      <select name="country"><option>Netherlands</option><option>Belgium</option><option>Germany</option><option>France</option><option>Other EU</option><option>United Kingdom</option></select>
      <label>Note / requested lot manifest</label><textarea name="note"></textarea>
      <p class="form-note">Your email program or WhatsApp opens with the order ready to send.</p>
      <p class="hero-actions" style="justify-content:flex-start">
        <button class="btn btn-dark" type="submit" name="via" value="email">Order by email</button>
        <button class="btn btn-dark" type="submit" name="via" value="whatsapp">Order by WhatsApp</button>
      </p>
    </form>
  </div>
  <div>
    <h2>Your pallets</h2>
    <div class="totals" data-order-summary></div>
  </div>
</div></section>
"""))

    write(ROOT / "account.html", page("My account", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>My account</h1>
<p>Log in with your existing account or create a new wholesale account here.</p></div></section>
<section class="section"><div class="container">
  <div data-account-panel></div>
  <div class="account-grid" data-auth-forms>
    <form data-login>
      <h2>Log in</h2>
      <label>Username or email address *</label>
      <input name="email" type="email" required autocomplete="username">
      <label>Password *</label>
      <input name="password" type="password" required autocomplete="current-password">
      <p class="remember"><label><input type="checkbox" name="remember"> Remember me</label></p>
      <p><button class="btn btn-dark" type="submit">Log in</button></p>
      <div data-result></div>
    </form>
    <form data-register>
      <h2>Create account</h2>
      <label>Name *</label>
      <input name="name" required autocomplete="name">
      <label>Email address *</label>
      <input name="email" type="email" required autocomplete="email">
      <label>Company name</label>
      <input name="company" autocomplete="organization">
      <label>Password *</label>
      <input name="password" type="password" required minlength="6" autocomplete="new-password">
      <label>Confirm password *</label>
      <input name="password2" type="password" required minlength="6" autocomplete="new-password">
      <p class="form-note">Your data is used as described in the <a href="privacybeleid.html">privacy policy</a>.</p>
      <p><button class="btn btn-dark" type="submit">Register</button></p>
      <div data-result></div>
    </form>
  </div>
</div></section>
"""))

    print(f"Wrote {len(PRODUCTS)} products and {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
