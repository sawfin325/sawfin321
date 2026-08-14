#!/usr/bin/env python3
"""Generate the PalletHaven static wholesale website."""
from __future__ import annotations

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

NAV = [
    ("index.html", "Home"),
    ("winkel.html", "Winkel"),
    ("plaats-pallet.html", "Plaats een pallet"),
    ("contact.html", "Neem contact met ons op"),
    ("over-ons.html", "Over ons"),
    ("privacybeleid.html", "Privacybeleid"),
    ("algemene-voorwaarden.html", "Algemene voorwaarden"),
    ("leveringsvoorwaarden.html", "Leveringsvoorwaarden"),
    ("disclaimer.html", "Juridische disclaimer"),
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
  <div class="topbar"><div class="container">Bestel via e-mail <a href="{MAIL_HREF}">{EMAIL}</a> of WhatsApp <a href="{WA_HREF}">{PHONE}</a> · Levering in heel Europa. Gratis verzending in Nederland vanaf € 3.000.</div></div>
  <div class="container header-main">
    <button class="menu-btn" data-menu aria-label="Menu">☰</button>
    <a class="logo" href="{prefix}index.html"><img src="{prefix}assets/logo.jpg" alt="PalletHaven"></a>
    <form class="search-wrap" data-search>
      <label class="sr-only" for="q">Zoeken</label>
      <input id="q" name="s" placeholder="Zoeken…">
      <button type="submit" aria-label="Zoeken">{search_icon}</button>
    </form>
    <div class="header-actions">
      <a class="account-link hide-sm" href="{prefix}account.html" data-open-login>LOGIN</a>
      <span class="header-divider hide-sm"></span>
      <a class="cart-link" href="{prefix}winkelwagen.html">
        <span class="cart-meta hide-sm">Winkelwagen / <span data-cart-total>€0.00</span></span>
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
      <p>Groothandel in liquidatiepallets voor wederverkopers in Nederland en Europa. Manifest vóór aankoop op alle standaardlots.</p>
      <p>Distelweg 72<br>1031 HH Amsterdam<br>Nederland</p>
    </div>
    <div>
      <h4>Navigatie</h4>
      <a href="{prefix}winkel.html">Winkel</a>
      <a href="{prefix}plaats-pallet.html">Plaats een pallet</a>
      <a href="{prefix}over-ons.html">Over ons</a>
      <a href="{prefix}contact.html">Contact</a>
      <a href="{prefix}account.html">Mijn account</a>
    </div>
    <div>
      <h4>Voorwaarden</h4>
      <a href="{prefix}privacybeleid.html">Privacybeleid</a>
      <a href="{prefix}algemene-voorwaarden.html">Algemene voorwaarden</a>
      <a href="{prefix}leveringsvoorwaarden.html">Leveringsvoorwaarden</a>
      <a href="{prefix}disclaimer.html">Juridische disclaimer</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="{MAIL_HREF}">{EMAIL}</a>
      <a href="{WA_HREF}">WhatsApp {PHONE}</a>
      <p>Ma–vr 09:00–17:00 CET<br>Geen walk-in, geen afhaling behalve truckloads op afspraak.</p>
    </div>
  </div>
  <div class="copy">© 2026 PalletHaven. Groothandel liquidatiepallets voor Nederland en Europa.</div>
</footer>
<div class="modal" id="quick-modal">
  <div class="modal-box">
    <img alt="">
    <div class="modal-body">
      <button class="close-x" data-close>×</button>
      <h3></h3>
      <p class="price" data-q-price></p>
      <p data-q-desc></p>
      <p class="form-note">Bestellen gaat via e-mail of WhatsApp. Kies hieronder.</p>
      <p><a class="btn btn-dark btn-block" data-q-mail>Bestel via e-mail<br><small>{EMAIL}</small></a></p>
      <p><a class="btn btn-dark btn-block" data-q-wa>Bestel via WhatsApp<br><small>{PHONE}</small></a></p>
      <p><a data-q-link>Bekijk product</a></p>
    </div>
  </div>
</div>
<div class="modal" id="order-modal">
  <div class="auth-box" style="max-width:520px">
    <button class="close-x" data-close-order aria-label="Sluiten">×</button>
    <h3>Hoe wil je bestellen?</h3>
    <p>Orders gaan via e-mail of WhatsApp. We nemen geen online betaling. Stuur je order naar <strong>{EMAIL}</strong> of WhatsApp <strong>{PHONE}</strong>.</p>
    <div data-order-prompt-body></div>
    <div class="order-via" style="margin-top:16px">
      <a class="btn btn-dark btn-block" data-order-mail>Bestel via e-mail<br><small>{EMAIL}</small></a>
      <a class="btn btn-dark btn-block" data-order-wa>Bestel via WhatsApp<br><small>{PHONE}</small></a>
    </div>
  </div>
</div>
<div class="modal" id="login-modal">
  <div class="auth-box">
    <button class="close-x" data-close-auth aria-label="Sluiten">×</button>
    <div class="auth-grid">
      <form data-login>
        <h3>Login</h3>
        <label>Gebruikersnaam of e-mailadres *</label>
        <input name="email" type="email" required autocomplete="username">
        <label>Wachtwoord *</label>
        <input name="password" type="password" required autocomplete="current-password">
        <p class="remember"><label><input type="checkbox" name="remember"> Onthouden</label></p>
        <button class="btn btn-dark" type="submit">Inloggen</button>
        <div data-result></div>
      </form>
      <form data-register>
        <h3>Registreren</h3>
        <label>Naam *</label>
        <input name="name" required autocomplete="name">
        <label>E-mailadres *</label>
        <input name="email" type="email" required autocomplete="email">
        <label>Bedrijfsnaam</label>
        <input name="company" autocomplete="organization">
        <label>Wachtwoord *</label>
        <input name="password" type="password" required minlength="6" autocomplete="new-password">
        <label>Bevestig wachtwoord *</label>
        <input name="password2" type="password" required minlength="6" autocomplete="new-password">
        <p class="form-note">Je persoonsgegevens worden gebruikt om je account en bestellingen te beheren, zoals beschreven in ons <a href="{prefix}privacybeleid.html">privacybeleid</a>.</p>
        <button class="btn btn-dark" type="submit">Account aanmaken</button>
        <div data-result></div>
      </form>
    </div>
  </div>
</div>"""


def page(title: str, prefix: str, active: str, body: str, extra_js: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} – PalletHaven</title>
  <meta name="description" content="PalletHaven levert groothandel liquidatiepallets aan wederverkopers in Nederland en Europa. Manifest vóór aankoop, directe verzending.">
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
{header(prefix, active)}
<main>
{body}
</main>
{footer(prefix)}
<script>const ROOT = "{prefix}"; const CONTACT = {{email: "{EMAIL}", phone: "{PHONE}", wa: "{WA_NUM}"}};</script>
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
            <button class="quick" data-quick="{p["slug"]}">Snel bekijken</button>
          </div>
          <div class="info">
            <p class="product-cat">{cat}</p>
            <h3><a href="{href}">{p["name"]}</a></h3>
            <div class="price">{price_label(p)}</div>
            <button class="btn btn-dark btn-sm btn-block" type="button" data-order="{p["slug"]}">Bestellen</button>
          </div>
        </article>""")
    html.append("</div>")
    return "\n".join(html)


def home_grid(slug, title):
    return f"""
<section class="section">
  <div class="container">
    <h2 class="section-title">{title}</h2>
    {cards(by_category(PRODUCTS, slug, 8))}
    <p class="grid-more"><a class="btn btn-dark" href="categorie/{slug}.html">Bekijk alle {CAT_MAP[slug]["name"]}</a></p>
  </div>
</section>"""


def homepage():
    cats = "".join(
        f"""<article class="cat-card">
          <a href="categorie/{c["slug"]}.html"><img src="{c["image"]}" alt="{c["name"]}"></a>
          <div class="body">
            <h3><a href="categorie/{c["slug"]}.html">{c["name"]}</a></h3>
            <p>{c["blurb"]}</p>
            <a class="btn btn-dark btn-sm" href="categorie/{c["slug"]}.html">Bekijk categorie</a>
          </div>
        </article>"""
        for c in CATEGORIES
    )
    return f"""
<section class="hero" style="background-image:url('{IMG["hero"]}')">
  <div class="hero-inner">
    <h1>Wholesale Liquidation Pallets voor Nederland en Europa — Merkproducten, Volledig Manifest, Directe Levering</h1>
    <p>Koop groothandel liquidatiepallets van de meest gevraagde categorieën op de Europese wederverkoopmarkt. Elektronica, sneakers, kleding, parfums, gereedschap, huishoudapparaten, bouwsets en mystery boxes. Elk manifestlot toont de samenstelling vóór aankoop. Bestellen gaat via e-mail of WhatsApp: <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> · <a href="https://wa.me/4915778431615">+49 1577 8431615</a></p>
    <div class="hero-actions">
      <a class="btn btn-light" href="winkel.html">Winkel alle pallets</a>
      <a class="btn btn-outline" href="contact.html">Bestel via e-mail / WhatsApp</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container features">
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="7" width="13" height="10" rx="1"/><path d="M16 10h3l2 3v4h-5"/><circle cx="7.5" cy="18.5" r="1.5" fill="#fff" stroke="none"/><circle cx="18.5" cy="18.5" r="1.5" fill="#fff" stroke="none"/></svg></div><h3>Prioritaire verzending</h3><p>Snelle verzending binnen Nederland en naar heel Europa, met betrouwbare logistieke partners.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg></div><h3>Duidelijke voorwaarden</h3><p>Manifestlots beoordeel je vóór betaling. Salvage, mystery en high-count gaan as-is.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="4" y="11" width="16" height="9" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></div><h3>Bestel via e-mail of WhatsApp</h3><p>Geen online checkout. Stuur je order naar Eu.wholesalestock@gmail.com of WhatsApp +49 1577 8431615. Betaling daarna via bankoverschrijving of Revolut.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><path d="M12 3l8 4v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/></svg></div><h3>Geverifieerde merkbronnen</h3><p>Overstock, surplus en retourstromen via retail- en distributiekanalen. Geen replica-lots.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M8 8h8M8 12h8M8 16h5"/></svg></div><h3>Volledig manifest vóór aankoop</h3><p>Merk, model, conditieklasse en geschatte MSRP per regel waar van toepassing.</p></article>
    <article class="feature"><div class="icon"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="10" width="7" height="10"/><rect x="14" y="10" width="7" height="10"/><path d="M7 10V7a5 5 0 0 1 10 0v3"/></svg></div><h3>B2B en export beschikbaar</h3><p>Factuur, paklijst en exportdocumenten voor zakelijke kopers in de EU.</p></article>
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Wat is PalletHaven?</h2>
    <p>PalletHaven is een Nederlands groothandelsplatform voor liquidatiepallets. We bevoorraden professionele wederverkopers, eBay.de- en Amazon.de-verkopers, boutique retailers, weekmarktoperators, B2B-distributeurs en exporthandelaren in Nederland, Duitsland, België en heel Europa.</p>
    <p>We sourcen overstock, distributeurssurplus, seizoensclearance en consumentenretouren bij Noord-Amerikaanse en Europese retaildistributienetwerken. Door direct in te kopen vallen tussenlagen weg. Jij houdt meer marge over.</p>
    <p>Op elk manifestlot zie je merk, model, conditieklasse, maatreeks waar van toepassing en geschatte MSRP vóór je vastlegt. Geen blinde dozen als standaard. High-count gaylords en mystery boxes zonder lijst staan nadrukkelijk zo gelabeld.</p>
  </div>
</section>

<section class="section">
  <div class="container prose">
    <h2>Onze productcategorieën</h2>
    <h3>Elektronica liquidatiepallets</h3>
    <p>Retourelektronica en overstock van audio, monitors, IT en smart home. Van 9-stuks dozen tot 43-stuks pallets tot truckloads. Getest werkend of nieuw verzegeld, nauwkeurig vermeld. Geschikt voor eBay.de, Amazon.de FBA, Back Market en B2B-distributeurs.</p>
    <h3>Sneaker liquidatiepallets</h3>
    <p>Sport- en lifestyle schoeisel met merk, model, kleurweg en maatreeks vóór aankoop. Massamarkt, premium lifestyle en limited-release lots. Voor eBay.de, Vinted, StockX-achtige kanalen en sneakerboutiques.</p>
    <h3>Amazon hoog-volume FC pallets</h3>
    <p>High Count FC gaylords, 1,8 tot 2,1 meter hoge stapels gemengde merchandise uit fulfillment-retouren. Elektronica, speelgoed, beddengoed en meer. Geen manifest. Vaste prijs, geen veiling. Alleen voor ervaren sorteerders.</p>
    <h3>iPhone en smartphone pallets</h3>
    <p>Nieuw verzegeld, Grade A refurbished en consumentenretour. Manifest met model, opslag, kleur, conditie en batterijgezondheid. Voor iPhone-verkopers, refurbishers en zakelijke kopers.</p>
    <h3>Huishoudapparaten</h3>
    <p>Koffiemachines, stofzuigers, mixers, blenders en airfryers. Conditieklasse per toestel. Voor Marketplace-verkopers, huishoudwinkels en weekmarkten.</p>
    <h3>Kleding en mode</h3>
    <p>Merkkleding, warehouse-mode, sportkleding en tassen. Nieuw met tags of overstock. Partijen van 250 stuks tot volle pallets.</p>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Hoe PalletHaven werkt</h2>
    <div class="steps">
      <article class="step"><b>1</b><h3>Kies een categorie</h3><p>Bekijk merkmix, conditie en verwachte MSRP op de categoriepagina.</p></article>
      <article class="step"><b>2</b><h3>Vraag het manifest</h3><p>Mail Eu.wholesalestock@gmail.com. Je krijgt de artikelregels vóór betaling.</p></article>
      <article class="step"><b>3</b><h3>Reken je marge</h3><p>Vergelijk met recente verkopen op eBay.de, Amazon.de of Back Market minus vracht.</p></article>
      <article class="step"><b>4</b><h3>Bestel via e-mail of WhatsApp</h3><p>Geen online betaling. Stuur de order naar Eu.wholesalestock@gmail.com of WhatsApp +49 1577 8431615.</p></article>
      <article class="step"><b>5</b><h3>Ontvang en verkoop</h3><p>Professioneel gewikkeld, met tracking, klaar om te testen en te listen.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Onze bestverkochte pallets</h2>
    {cards(by_category(PRODUCTS, "keuken", 1) + by_category(PRODUCTS, "pokemon", 1) + by_category(PRODUCTS, "cosmetica", 1) + by_category(PRODUCTS, "elektronica", 1) + by_category(PRODUCTS, "mystery-box", 1) + by_category(PRODUCTS, "koelkast", 1) + by_category(PRODUCTS, "gereedschap", 1) + by_category(PRODUCTS, "iphone", 1))}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Waarom Nederlandse en Europese wederverkopers PalletHaven kiezen</h2>
    <p>Omdat je op standaardlots de samenstelling kent vóór je betaalt: merk, model, conditieklasse en geschatte MSRP per eenheid. De meeste Europese brokers tonen dat pas na aankoop. Bij ons is het manifest de default.</p>
    <p>Voorraad komt uit overstock, surplus en retourkanalen. Geen namaak om pallets te vullen. Nieuw verzegeld is nieuw verzegeld. Getest werkend is functioneel gecontroleerd. Retour vermeldt een realistisch uitvalpercentage. Salvage is salvage.</p>
    <p>We verzenden naar Nederland (3–7 werkdagen) en de rest van Europa (5–14 werkdagen). Invoerrechten en btw buiten onze factuur zijn voor de koper. Volume en truckloads via Eu.wholesalestock@gmail.com.</p>
  </div>
</section>

{home_grid("high-count", "Koop pallets met Amazon-opruimingsproducten.")}

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Voor wie is PalletHaven?</h2>
    <div class="audience">
      <article><h3>eBay.de en Amazon.de FBA</h3><p>Merkgebonden elektronica, schoeisel, kleding, gereedschap en huishoudapparaten met identifiers om vooraf te listen.</p></article>
      <article><h3>Boutiques en outlets</h3><p>Winkels in NL en DE die merkvoorraad onder adviesprijs willen zonder standaard groothandelsminimums.</p></article>
      <article><h3>Weekmarkten en pop-ups</h3><p>Volume tegen een lage stukprijs voor face-to-face verkoop aan kopers die op merkwaarde reageren.</p></article>
      <article><h3>Distributeurs en export</h3><p>Partijen die splitsen naar lokale retailers of verder exporteren binnen de EU.</p></article>
    </div>
  </div>
</section>

{home_grid("pokemon", "Koop pallets met Pokémon-opruiming.")}

<section class="section alt">
  <div class="container prose">
    <h2>Klaar om te beginnen? Dit is wat je doet</h2>
    <p>PalletHaven is uitsluitend online. Geen walk-in en geen afhaling op standaardpallets. Bekijk de categoriepagina’s, klik op Bestellen, en stuur de order via e-mail (Eu.wholesalestock@gmail.com) of WhatsApp (+49 1577 8431615). Je krijgt het manifest, toetst je exitprijzen en bevestigt. Voor truckloads overleggen we vracht en laaddatum eerst.</p>
  </div>
</section>

{home_grid("gereedschap", "Koop pallets met gemengde gereedschapsvoorraden.")}

<section class="section alt">
  <div class="container prose">
    <h2>Verzendinformatie</h2>
    <p>Nederlandse bestellingen gaan via verzekerde LTL-palletvracht, 3 tot 7 werkdagen na bevestiging, naar alle provincies inclusief Noord-Holland, Zuid-Holland, Utrecht, Noord-Brabant, Gelderland, Overijssel, Groningen, Friesland en Zeeland.</p>
    <p>Europese leveringen omvatten Duitsland, België, Frankrijk, het Verenigd Koninkrijk, Spanje, Italië, Polen, Oostenrijk, Denemarken, Zweden en overige EU-bestemmingen, 5 tot 14 werkdagen. Douane, invoer en lokale btw zijn voor de koper. Documenten leveren we mee.</p>
    <p>Geen lokale ophaling, behalve container- en truckloadorders na afspraak.</p>
  </div>
</section>

{home_grid("sneakers", "Koop pallets met overtollige sneakerpartijen.")}

<section class="section alt">
  <div class="container prose">
    <h2>Wat is een liquidatiepallet?</h2>
    <p>Een liquidatiepallet is een bundel merchandise die een retailer of fabrikant doorzet naar de groothandel: overstock, seizoensclearance of retourvoorraad. Wederverkopers kopen die bundel onder retail in en verkopen per stuk via webshops, markten of fysieke winkels.</p>
    <p>Het voordeel is toegang tot merken zonder volle groothandelscatalogus. Nieuwe categorieën testen zonder grote volumes vast te leggen hoort daarbij. Veel kopers starten met één of twee pallets en groeien naar multi-pallet of truckload.</p>
    <p>Het risico is conditievariatie. Daarom leveren wij op standaardlots een regel-voor-regel overzicht. High-count zonder lijst is een ander product, met een andere prijs en een andere koper.</p>
    <p>Kopers betalen een fractie van de oorspronkelijke retailwaarde. De combinatie van lage inkoop en marktconforme verkoop maakt dit een groeimodel voor mkb in Nederland en Europa.</p>
  </div>
</section>

{home_grid("kleding", "Koop pallets met gemengde kleding.")}

<section class="section alt">
  <div class="container prose">
    <h2>Liquidatiepallet flipping: bijverdienste of fulltime onderneming?</h2>
    <p>Als bijverdienste test je de markt met minimaal risico, in avonden of weekenden. Fulltime biedt meer schaal — van enkele pallets naar truckloads — maar vraagt kasstroom, opslag en een vast inkoopplan.</p>
    <p>De meeste succesvolle wederverkopers beginnen met één of twee manifestlots, bouwen hun sorteer- en listingsysteem, en schalen daarna gecontroleerd op. PalletHaven is ingericht op beide tempo’s: kleine dozen om te testen en truckloads wanneer de operatie dat aankan.</p>
  </div>
</section>

{home_grid("keuken", "Koop pallets met huishoudelijke en keukenapparaten.")}

<section class="section alt">
  <div class="container prose">
    <h2>Is het kopen van liquidatiepallets de moeite waard?</h2>
    <p>Alleen als de input klopt. Liquidatie geeft toegang tot merkvoorraad tegen een fractie van de retailprijs. Dat verschil is de marge. Zonder gedetailleerd manifest is er geen betrouwbare manier om te beoordelen wat je ontvangt. Reken verwachte verkoopprijs minus platformkosten, vracht, opslag en refurbishment. Als de leverancier geen manifest kan geven op een lot dat als manifest wordt verkocht, is dat een reden om te stoppen.</p>
  </div>
</section>

{home_grid("amazon-mystery", "Koop pallets vol mystery boxen.")}

<section class="section alt">
  <div class="container prose">
    <h2>Liquidatieverkoop: maximale winst voor wederverkopers in Nederland en Europa</h2>
    <p>Liquidatie vindt plaats wanneer retailers, fabrikanten of distributeurs overtollige voorraad, seizoensclearance of retourstromen afstoten. Groothandelsprijzen liggen doorgaans 40 tot 60 procent onder de oorspronkelijke retailwaarde. Dat geeft prijsruimte op eBay.de, Amazon.de, Back Market en fysieke winkels.</p>
    <h3>Het voordeel van groothandelsinkoop</h3>
    <p>Bulkinkoop via liquidatiekanalen levert een lagere stukprijs op dan reguliere groothandel. Merkvoorraad tegen liquidatieprijzen verlaagt de inkoop zonder dat je concessies doet aan herkenbaarheid. Lots bestaan vaak uit fabrieksnieuwe eenheden, nieuw met tags of licht gebruikte A-merken.</p>
    <h3>Voordelen voor retailers en wederverkopers</h3>
    <p>Een breed assortiment uit één aankoop vergroot het verkooppotentieel en vermindert de afhankelijkheid van één categorie. De combinatie van lage inkoop en marktconforme verkoop maakt marges mogelijk die standaard groothandel zelden haalt. Inkoop van overstock voorkomt bovendien dat bruikbare producten worden vernietigd.</p>
    <p>PalletHaven levert lots met manifest waar beloofd, conditieclassificatie en directe verzending. Of je één pallet test of op truckload-volume inkoopt: de lotstructuur is hetzelfde.</p>
  </div>
</section>

{home_grid("amazon-electronics", "Koop pallets met gemengde algemene merchandise.")}

<section class="section alt">
  <div class="container prose">
    <h2>Het verschil tussen pallet flipping en een echte wederverkooponderneming</h2>
    <p>Pallet flipping voelt laagdrempelig tot het volume groeit: kapitaal blijft langer vastzitten, opslag raakt vol en beslissingen stapelen zich op. Sommige pallets gaan snel, andere blijven staan. Dat vraagt herprijzing en herschikking. Het probleem is zelden inzet, maar het ontbreken van een inkoopplan.</p>
    <h3>Reactief inkopen</h3>
    <p>Reactief inkopen — deals najagen omdat ze nu aantrekkelijk lijken — levert inconsistente marges op. De ene aankoop presteert, de volgende niet. Kasstroom wordt onvoorspelbaar en opslag loopt voller dan gepland.</p>
    <h3>Een onderneming bouwen</h3>
    <p>Een wederverkooponderneming koopt op marktvraag, prijsstructuur en realistische verkooptijdlijnen. Categorieën worden gekozen omdat ze consistent presteren, niet omdat ze trending zijn. Marges zijn bekend vóór de voorraad aankomt.</p>
    <p>PalletHaven levert de lotstructuur daarvoor: manifesten, conditieclassificatie en terugkerende beschikbaarheid, van één pallet tot truckload.</p>
  </div>
</section>

{home_grid("bouwsets", "Koop pallets met Lego-opruimingspallets.")}
{home_grid("cosmetica", "Koop pallets met cosmetic liquidatie.")}
{home_grid("iphone", "Koop pallets met iPhone liquidatie.")}
{home_grid("airco", "Koop pallets met airconditioners.")}
{home_grid("winterschoenen", "Koop pallets met winterschoenen.")}
{home_grid("parfum", "Koop pallets met parfum liquidatie.")}
{home_grid("speelgoed", "Koop pallets met speelgoed-opruiming.")}
{home_grid("handtassen", "Koop pallets met dameshandtassen.")}
{home_grid("truckload", "Koop truckloads en multi-pallet volume.")}

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Alle categorieën</h2>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Getuigenissen</h2>
    <p class="lead">Wat onze klanten over ons zeggen</p>
    <div class="reviews">
      <article class="review"><div class="stars">★★★★★</div><p>Pallets kwamen aan zoals beschreven, goed verpakt, levering binnen Europa soepel. Duidelijke communicatie.</p><cite>Thomas de Vries — Eindhoven</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Elektronicalot authentiek, manifest klopte. Winstpotentieel was reëel. Opnieuw besteld.</p><cite>Lea Hoffmann — Düsseldorf</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Sneakers grotendeels nieuw in doos. Vracht naar Rotterdam was duidelijk vooraf.</p><cite>Samir El Idrissi — Rotterdam</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Beauty-pallet schoon, sealed en klaar voor wederverkoop. Goede groothandelsprijs.</p><cite>Nina Bakker — Utrecht</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>High-count is niks voor beginners, dat zeiden ze ook. Voor ons sorteerbedrijf past het.</p><cite>Marco Bianchi — Milaan</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Tracking klopte. Factuur en paklijst compleet voor de boekhouding.</p><cite>Sophie Laurent — Lille</cite></article>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container contact-grid">
    <div>
      <h2>Stuur ons een bericht</h2>
      <p>Vragen over een lot, manifest of vracht? We reageren op werkdagen.</p>
      <form data-contact>
        <div class="row"><div><label>Je naam</label><input name="name" required></div><div><label>Je e-mailadres</label><input type="email" name="email" required></div></div>
        <label>Onderwerp</label><input name="subject" required>
        <label>Je bericht</label><textarea name="message"></textarea>
        <p><button class="btn btn-dark" type="submit">Versturen</button></p>
        <div data-result></div>
      </form>
    </div>
    <div class="faq">
      <h2>Veelgestelde vragen over onze liquidatiepallets</h2>
      <details open><summary>Hoe bestel ik?</summary><p>Bestellen gaat via e-mail of WhatsApp, niet via een online checkout. Klik op Bestellen bij een lot en kies <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> of WhatsApp <a href="https://wa.me/4915778431615">+49 1577 8431615</a>. We bevestigen het lot en de vracht, daarna betaal je via bankoverschrijving of Revolut.</p></details>
      <details><summary>Is PalletHaven een geverifieerd bedrijf?</summary><p>PalletHaven is een groothandelsplatform dat wederverkopers, retailers, B2B-distributeurs en exporteurs bevoorraadt in Nederland, Duitsland, België en heel Europa.</p></details>
      <details><summary>Geeft PalletHaven een manifest vóór aankoop?</summary><p>Ja, op elk manifestlot. Merk, model, conditieklasse, maatreeks waar van toepassing en geschatte MSRP volgen vóór betaling. No-manifest lots zoals high-count gaylords staan duidelijk zo gelabeld.</p></details>
      <details><summary>Welke categorieën zijn beschikbaar?</summary><p>Elektronica, sneakers, kleding, parfum, gereedschap, huishoudapparaten, smartphones, bouwsets, TCG, mystery boxes, airco, truckloads en meer. De winkel telt 10.000 live lots.</p></details>
      <details><summary>Verzenden jullie naar Duitsland en de rest van Europa?</summary><p>Ja. Invoerrechten, btw en douane op internationale orders zijn voor de koper.</p></details>
      <details><summary>Zijn er lokale ophalingopties?</summary><p>Niet bij standaardpallets. Truckloads mogelijk op afspraak.</p></details>
      <details><summary>Wat is de minimale bestelling?</summary><p>Het kleinste lot in de winkel. Volume via Eu.wholesalestock@gmail.com.</p></details>
      <details><summary>Zijn retouren geaccepteerd?</summary><p>Verkoop is definitief na verzending, behalve bij een aantoonbare verzendfout of een lot dat materieel afwijkt van het bevestigde manifest.</p></details>
      <details><summary>Wat zijn de beste lots voor beginners in Nederland?</summary><p>Manifest-geverifieerde enkele-categorie lots: kleine elektronica dozen, parfum of 120-paar schoenen. Geen high-count gaylord als eerste aankoop.</p></details>
      <details><summary>Wat zijn wholesale liquidation pallets voor Nederland en Europa?</summary><p>Bulklots van consumentenproducten uit retourkanalen, retailer-overstock, seizoensclearance en distributeursurplus, verkocht onder retail aan professionele wederverkopers. PalletHaven geeft een manifest vóór aankoop op elk lot dat als manifestlot is gelabeld.</p></details>
      <details><summary>Hoe verschilt PalletHaven van andere leveranciers?</summary><p>We prijzen in euro, vermelden conditie eerlijk (retour is retour, salvage is salvage) en overdrijven geen merkmix. High-count zonder lijst staat zo gelabeld.</p></details>
      <details><summary>Zijn deze pallets winstgevend voor wederverkopers?</summary><p>Voor kopers met een verkoopkanaal en de capaciteit om de gekozen categorie te verwerken. Herkenbare merken trekken vraag op eBay.nl, eBay.de en Amazon.nl. Resultaten hangen af van jouw prijs, vracht en uitval.</p></details>
      <details><summary>Welke categorieën zijn beschikbaar voor de Nederlandse markt?</summary><p>Elektronica, speelgoed, Amazon-retouren, handtassen, winterschoenen, sneakers, kleding, parfum, gereedschap, huishoudapparaten, bouwsets, TCG en truckloads. Elke categoriepagina toont live lots met EUR-prijzen.</p></details>
      <details><summary>Bieden jullie pallets mét manifest?</summary><p>Ja, op standaardlots: artikelregels, identifiers waar beschikbaar en geschatte MSRP. Voor sommige high-count formats is het bestand op verzoek via Eu.wholesalestock@gmail.com.</p></details>
      <details><summary>Hoe lang duurt levering?</summary><p>Nederland 3 tot 7 werkdagen. EU 7 tot 14 werkdagen. Grotere monitorpallets kunnen 10 tot 21 dagen vragen.</p></details>
      <details><summary>Bieden jullie lokale afhaling of magazijnverkoop aan in Nederland?</summary><p>Nee, behalve truckloads op afspraak. Standaardpallets gaan naar het opgegeven bezorgadres.</p></details>
      <details><summary>Zijn deze pallets geschikt voor beginnende wederverkopers?</summary><p>Sommige lots wel: speelgoed, kleine smart-home dozen en handtassen. Salvage-monitorpallets zijn voor technici. High-count gaylords zijn geen startersproduct.</p></details>
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
    <h4>Categorieën</h4>
    <a href="{prefix}winkel.html">Alle pallets</a>
    {cat_links}
  </aside>
  <div>
    <div class="toolbar">
      <div data-result-count></div>
      <div data-search-hint></div>
      <label>Sorteren
        <select data-sort>
          <option value="featured">Aanbevolen</option>
          <option value="price-asc">Prijs laag-hoog</option>
          <option value="price-desc">Prijs hoog-laag</option>
          <option value="name">Naam</option>
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
    write(ROOT / "js" / "data.js", js)
    print(f"Wrote catalog: {len(PRODUCTS)} products, {len(CATEGORIES)} categories, data.js { (ROOT/'js'/'data.js').stat().st_size // 1024 } KB")

    write(ROOT / "index.html", page("Home", "", "index.html", homepage()))
    write(ROOT / "winkel.html", page("Winkel", "", "winkel.html", shop_page(
        "Winkel", "Home / Winkel",
        intro=f"Alle {len(PRODUCTS):,} beschikbare liquidatiepallets. Filter op categorie of zoek op trefwoord.".replace(",", "."),
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
            f'<a href="../index.html">Home</a> / <a href="../winkel.html">Winkel</a> / {c["name"]}',
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
  <p>Product wordt geladen…</p>
</div></section>
"""))

    write(ROOT / "contact.html", page("Neem contact met ons op", "", "contact.html", """
<section class="page-hero"><div class="container"><h1>Neem contact met ons op</h1>
<p>Bestel en vraag offertes via e-mail of WhatsApp. We reageren op werkdagen.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div>
    <h2>Stuur ons een bericht</h2>
    <div class="order-via">
      <p><a class="btn btn-dark" href="mailto:Eu.wholesalestock@gmail.com">E-mail Eu.wholesalestock@gmail.com</a></p>
      <p><a class="btn btn-dark" href="https://wa.me/4915778431615">WhatsApp +49 1577 8431615</a></p>
    </div>
    <form data-contact>
      <div class="row"><div><label>Je naam</label><input name="name" required></div><div><label>Je e-mailadres</label><input type="email" required></div></div>
      <label>Onderwerp</label><input name="subject" required>
      <label>Je bericht</label><textarea name="message"></textarea>
      <p><button class="btn btn-dark" type="submit">Versturen</button></p>
      <div data-result></div>
    </form>
  </div>
  <div>
    <h2>Gegevens</h2>
    <dl class="info-list">
      <dt>Adres</dt><dd>Distelweg 72, 1031 HH Amsterdam, Nederland</dd>
      <dt>Openingstijden</dt><dd>Niet open voor publiek. Afhalen alleen bij truckloads op afspraak.</dd>
      <dt>E-mail</dt><dd><a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a></dd>
      <dt>WhatsApp</dt><dd><a href="https://wa.me/4915778431615">+49 1577 8431615</a></dd>
    </dl>
  </div>
</div></section>
"""))

    write(ROOT / "plaats-pallet.html", page("Plaats een pallet", "", "plaats-pallet.html", """
<section class="page-hero"><div class="container">
  <h1>Plaats een pallet</h1>
  <p>Iedereen kan hier een eigen liquidatiepallet of lot plaatsen. Na publicatie staat je advertentie op deze pagina en in de winkel.</p>
</div></section>
<section class="section"><div class="container contact-grid">
  <form data-post-pallet>
    <h2>Nieuwe pallet plaatsen</h2>
    <label>Titel van het lot *</label>
    <input name="title" required placeholder="Bijv. Merkkleding pallet 250 stuks">
    <label>Categorie *</label>
    <select name="category" required></select>
    <div class="row">
      <div><label>Prijs in euro *</label><input name="price" type="number" min="1" step="0.01" required></div>
      <div><label>Aantal stuks</label><input name="items" type="number" min="1"></div>
    </div>
    <label>Omschrijving *</label>
    <textarea name="description" required placeholder="Wat zit er in het lot, conditie, locatie"></textarea>
    <label>Foto van jouw pallet</label>
    <input name="photo" type="file" accept="image/*">
    <div class="row">
      <div><label>Jouw naam *</label><input name="name" required></div>
      <div><label>E-mail *</label><input name="email" type="email" required></div>
    </div>
    <label>Telefoon / WhatsApp</label>
    <input name="phone" placeholder="+49 …">
    <p class="form-note">Vragen over plaatsing: <a href="mailto:Eu.wholesalestock@gmail.com">Eu.wholesalestock@gmail.com</a> of WhatsApp <a href="https://wa.me/4915778431615">+49 1577 8431615</a>.</p>
    <p><button class="btn btn-dark" type="submit">Pallet publiceren</button></p>
    <div data-result></div>
  </form>
  <div>
    <h2>Geplaatste pallets van het publiek</h2>
    <div class="product-grid" data-community-grid></div>
  </div>
</div></section>
"""))

    write(ROOT / "over-ons.html", page("Over ons", "", "over-ons.html", """
<section class="page-hero"><div class="container"><h1>Over PalletHaven</h1></div></section>
<section class="section"><div class="container prose legal">
  <p>PalletHaven is een groothandelsplatform voor liquidatie- en overstockpallets. We bestaan om kopers in Nederland en Europa merkvoorraad te geven tegen prijzen waarmee wederverkoop nog werkt, mét productinformatie vóór aankoop.</p>
  <h2>Wat we leveren</h2>
  <p>Consumentenelektronica, smartphones, kleding, schoeisel, gereedschap, parfum, huishoudapparaten, speelgoed en gemengde lots. Het merendeel is nieuw of tagged. Retour en salvage staan als zodanig in het lot.</p>
  <h2>Nederland als kernmarkt</h2>
  <p>We leveren in alle provincies. De lokale wederverkoopmarkt vraagt herkenbare merken, schone conditieklassen en identifiers die je kunt listen. Daar kopen we op in.</p>
  <h2>Europa</h2>
  <p>Duitsland, België, Frankrijk, het VK, Spanje, Italië, Polen en overige EU-landen. Levertijd 5–14 werkdagen. Douane en lokale heffingen zijn voor de koper. Documentatie leveren we.</p>
  <h2>Hoe we werken</h2>
  <p>Lot online, manifest waar beloofd, betaling na bevestiging, verzending binnen 1–2 werkdagen, tracking per zending. Verkoop is definitief na verzending, behalve bij een materiële afwijking van het bevestigde bestand.</p>
</div></section>
"""))

    write(ROOT / "privacybeleid.html", page("Privacybeleid", "", "privacybeleid.html", """
<section class="page-hero"><div class="container"><h1>Privacybeleid</h1></div></section>
<section class="section"><div class="container legal">
  <p>PalletHaven, Distelweg 72, 1031 HH Amsterdam, verwerkt persoonsgegevens om bestellingen, offertes en klantaccounts af te handelen.</p>
  <h2>Welke gegevens</h2>
  <p>Naam, e-mail, telefoon, bezorgadres, bedrijfsgegevens, KvK/btw-nummer en correspondentie. Betalingsbewijzen van overschrijving of Revolut.</p>
  <h2>Doelen</h2>
  <p>Uitvoering van de overeenkomst, wettelijke administratieplicht, fraudepreventie en — alleen met toestemming — berichten over nieuwe lots.</p>
  <h2>Bewaartermijn</h2>
  <p>Ordergegevens tot zeven jaar in de administratie. Accounts tot beëindiging plus een redelijke nazorgperiode.</p>
  <h2>Delen</h2>
  <p>Vervoerders, betaaldienstverleners en IT-hosting, beperkt tot wat nodig is. Geen verkoop van adressenlijsten.</p>
  <h2>Rechten</h2>
  <p>Inzage, correctie, verwijdering, beperking en bezwaar via Eu.wholesalestock@gmail.com. Klachten kunnen naar de Autoriteit Persoonsgegevens.</p>
  <h2>Cookies</h2>
  <p>Deze demo-site gebruikt lokale opslag voor de winkelwagen. Er draait geen trackingpixel.</p>
</div></section>
"""))

    write(ROOT / "algemene-voorwaarden.html", page("Algemene voorwaarden", "", "algemene-voorwaarden.html", """
<section class="page-hero"><div class="container"><h1>Algemene voorwaarden</h1></div></section>
<section class="section"><div class="container legal">
  <h2>1. Toepasselijkheid</h2>
  <p>Deze voorwaarden gelden voor alle offertes en leveringen van PalletHaven aan zakelijke kopers. Consumentenbescherming van afstandsaankopen is niet van toepassing op B2B-liquidatie.</p>
  <h2>2. Aanbod en manifest</h2>
  <p>Prijzen in euro, exclusief vracht tenzij anders vermeld. Een lot is een momentopname. Beschikbaarheid kan wijzigen tot bevestiging. Bij manifestlots prevaleert het toegestuurde bestand boven de productpagina.</p>
  <h2>3. Betaling</h2>
  <p>Vooruitbetaling via bankoverschrijving of Revolut na lotbevestiging. Eigendom gaat over na volledige betaling.</p>
  <h2>4. Conditie</h2>
  <p>Liquidatievoorraad is per definitie gemengd. Salvage, retour en high-count zonder lijst worden as-is verkocht. Kopers inspecteren het manifest vóór akkoord.</p>
  <h2>5. Levering</h2>
  <p>Levertijden zijn indicatief. Risico gaat over bij overdracht aan de vervoerder, tenzij anders overeengekomen. Schade bij aankomst binnen 24 uur schriftelijk melden met foto's van wrapping en pallet.</p>
  <h2>6. Herroeping</h2>
  <p>Geen herroepingsrecht na verzending. Uitzondering: aantoonbare verwisseling van lot of materiële afwijking van het bevestigde manifest.</p>
  <h2>7. Aansprakelijkheid</h2>
  <p>Aansprakelijkheid is beperkt tot het factuurbedrag van het betreffende lot, behalve bij opzet of grove schuld.</p>
  <h2>8. Recht</h2>
  <p>Nederlands recht. Bevoegde rechter: Amsterdam.</p>
</div></section>
"""))

    write(ROOT / "leveringsvoorwaarden.html", page("Leveringsvoorwaarden", "", "leveringsvoorwaarden.html", """
<section class="page-hero"><div class="container"><h1>Leveringsvoorwaarden</h1></div></section>
<section class="section"><div class="container legal">
  <p>PalletHaven verzendt pallets via LTL-vrachtpartners. Standaardpallets worden niet ter plaatse afgehaald.</p>
  <h2>Nederland</h2>
  <p>3 tot 7 werkdagen na orderbevestiging. Gratis verzending vanaf € 3.000 naar een Nederlands adres, tenzij het lot als truckload of extra volume is gemarkeerd.</p>
  <h2>Europa</h2>
  <p>5 tot 14 werkdagen. Grotere formaten kunnen 10 tot 21 dagen vragen. Invoer, douane en btw zijn voor de koper. We leveren factuur en paklijst.</p>
  <h2>Aanlevering</h2>
  <p>Bezorging tot de stoeprand of laadperron, afhankelijk van de locatie. Een heftruck of palletwagen aan de ontvangstzijde is jouw verantwoordelijkheid. Mislukte levering door ontoegankelijkheid kan extra kosten geven.</p>
  <h2>Schade</h2>
  <p>Noteer zichtbare transportschade op de vrachtbrief en mail foto's binnen 24 uur naar Eu.wholesalestock@gmail.com.</p>
</div></section>
"""))

    write(ROOT / "disclaimer.html", page("Juridische disclaimer", "", "disclaimer.html", """
<section class="page-hero"><div class="container"><h1>Juridische disclaimer</h1></div></section>
<section class="section"><div class="container legal">
  <p>Informatie op deze website is bedoeld voor zakelijke kopers van liquidatievoorraad. Listings, manifests en prijzen kunnen wijzigen. We spannen ons in voor nauwkeurigheid maar garanderen niet dat elke pagina te allen tijde foutloos is.</p>
  <p>Merknamen dienen alleen ter identificatie van de goederen. PalletHaven is niet verbonden aan die merken, tenzij uitdrukkelijk vermeld.</p>
  <p>Wederverkoopresultaten hangen af van jouw kanalen, prijzen en verwerking. Eerdere lots zijn geen garantie voor toekomstige samenstelling.</p>
  <p>Deze site is een statische demonstratie van een groothandelswebshop. Plaats geen echte betalingen op basis van deze demo zonder een afzonderlijke schriftelijke bevestiging.</p>
</div></section>
"""))

    write(ROOT / "winkelwagen.html", page("Winkelwagen", "", "winkelwagen.html", """
<section class="page-hero"><div class="container"><h1>Winkelwagen</h1>
<p>Bestel de geselecteerde pallets via e-mail of WhatsApp.</p></div></section>
<section class="section"><div class="container">
  <div data-cart-table></div>
  <div data-cart-totals></div>
</div></section>
"""))

    write(ROOT / "afrekenen.html", page("Afrekenen", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>Bestel via e-mail of WhatsApp</h1>
<p>Kies hoe je de order verstuurt. Er wordt niets automatisch afgeschreven.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div>
    <h2>Hoe wil je bestellen?</h2>
    <p>Stuur je bestelling naar <strong>Eu.wholesalestock@gmail.com</strong> of WhatsApp <strong>+49 1577 8431615</strong>. Vul hieronder je gegevens in en klik op een van de knoppen.</p>
    <form data-checkout>
      <div class="row"><div><label>Bedrijfsnaam</label><input name="company"></div><div><label>KvK-nummer</label><input name="kvk"></div></div>
      <div class="row"><div><label>Contactpersoon</label><input name="name" required></div><div><label>E-mail</label><input name="email" type="email" required></div></div>
      <label>Telefoon</label><input name="phone" required>
      <label>Afleveradres</label><input name="address" required>
      <div class="row"><div><label>Postcode</label><input name="zip" required></div><div><label>Plaats</label><input name="city" required></div></div>
      <label>Land</label>
      <select name="country"><option>Nederland</option><option>België</option><option>Duitsland</option><option>Frankrijk</option><option>Overig EU</option><option>Verenigd Koninkrijk</option></select>
      <label>Opmerking / gewenst lotmanifest</label><textarea name="note"></textarea>
      <p class="form-note">Je e-mailprogramma of WhatsApp opent met de order klaar om te versturen.</p>
      <p class="hero-actions" style="justify-content:flex-start">
        <button class="btn btn-dark" type="submit" name="via" value="email">Bestel via e-mail</button>
        <button class="btn btn-dark" type="submit" name="via" value="whatsapp">Bestel via WhatsApp</button>
      </p>
    </form>
  </div>
  <div>
    <h2>Jouw pallets</h2>
    <div class="totals" data-order-summary></div>
  </div>
</div></section>
"""))

    write(ROOT / "account.html", page("Mijn account", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>Mijn account</h1>
<p>Log in met je bestaande account of maak hier een nieuw groothandelsaccount aan.</p></div></section>
<section class="section"><div class="container">
  <div data-account-panel></div>
  <div class="account-grid" data-auth-forms>
    <form data-login>
      <h2>Inloggen</h2>
      <label>Gebruikersnaam of e-mailadres *</label>
      <input name="email" type="email" required autocomplete="username">
      <label>Wachtwoord *</label>
      <input name="password" type="password" required autocomplete="current-password">
      <p class="remember"><label><input type="checkbox" name="remember"> Onthouden</label></p>
      <p><button class="btn btn-dark" type="submit">Inloggen</button></p>
      <div data-result></div>
    </form>
    <form data-register>
      <h2>Account aanmaken</h2>
      <label>Naam *</label>
      <input name="name" required autocomplete="name">
      <label>E-mailadres *</label>
      <input name="email" type="email" required autocomplete="email">
      <label>Bedrijfsnaam</label>
      <input name="company" autocomplete="organization">
      <label>Wachtwoord *</label>
      <input name="password" type="password" required minlength="6" autocomplete="new-password">
      <label>Bevestig wachtwoord *</label>
      <input name="password2" type="password" required minlength="6" autocomplete="new-password">
      <p class="form-note">Je gegevens worden gebruikt zoals beschreven in het <a href="privacybeleid.html">privacybeleid</a>.</p>
      <p><button class="btn btn-dark" type="submit">Registreren</button></p>
      <div data-result></div>
    </form>
  </div>
</div></section>
"""))

    print(f"Wrote {len(PRODUCTS)} products and {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
