#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote

import site_content

ROOT = Path("/workspace")
PHONE = "+1 743-259-3337"
PHONE_TEL = "+17432593337"
EMAIL = "hello@evergoldpomeranians.com"
WA_BASE = "https://wa.me/17432593337"
BRAND = "Evergold Pomeranians"


def order_message(puppy="a Pomeranian puppy"):
    return (
        f"Hello Evergold, I would like to order {puppy}. "
        "Please send the latest video, the health packet, and reservation steps."
    )


def wa_href(puppy="a Pomeranian puppy"):
    return f"{WA_BASE}?text={quote(order_message(puppy))}"


def mail_href(puppy="a Pomeranian puppy"):
    subject = quote(f"Puppy order: {puppy}")
    body = quote(order_message(puppy))
    return f"mailto:{EMAIL}?subject={subject}&body={body}"

IMG = {
    "hero": "https://images.unsplash.com/photo-1744032789697-fdc713e03595?auto=format&fit=crop&w=1800&q=80",
    "grass": "https://images.unsplash.com/photo-1770130825884-421c105d6e28?auto=format&fit=crop&w=1400&q=80",
    "white": "https://images.unsplash.com/photo-1594099691860-c940b5768c45?auto=format&fit=crop&w=1400&q=80",
    "brown": "https://images.unsplash.com/photo-1622964430125-f21a872b4586?auto=format&fit=crop&w=1400&q=80",
    "tongue": "https://images.unsplash.com/photo-1745130179738-e9a8eafaf989?auto=format&fit=crop&w=1400&q=80",
    "orange": "https://images.unsplash.com/photo-1620189507195-68309c04c4d0?auto=format&fit=crop&w=1400&q=80",
    "sitting": "https://images.unsplash.com/photo-1591946614720-90a587da4a36?auto=format&fit=crop&w=1400&q=80",
    "fluffy": "https://images.unsplash.com/photo-1558788353-f76d92427f16?auto=format&fit=crop&w=1400&q=80",
    "face": "https://images.unsplash.com/photo-1615751072497-5f5169febe17?auto=format&fit=crop&w=1400&q=80",
    "portrait": "https://images.unsplash.com/photo-1615751072497-5f5169febe17?auto=format&fit=crop&w=1400&q=80",
    "cozy": "https://images.unsplash.com/photo-1558788353-f76d92427f16?auto=format&fit=crop&w=1400&q=80",
}


def img(key, alt):
    return f'<img src="{IMG[key]}" alt="{alt}" loading="lazy">'


def product_photos(pup):
    photos = list(pup.get("photos") or [])
    if pup.get("photo") and pup["photo"] not in photos:
        photos.insert(0, pup["photo"])
    return photos


def resolve_src(src, depth=0):
    if src and not src.startswith("http"):
        return prefix(depth) + src
    return src


def product_img(pup, alt, depth=0):
    photos = product_photos(pup)
    if photos:
        src = resolve_src(photos[0], depth)
        return f'<img src="{src}" alt="{alt}" loading="lazy">'
    tone = pup.get("tone", "cream")
    return f'<div class="photo-wait photo-wait-{tone}" aria-label="{alt}"><span>{pup["name"]}</span></div>'


def gallery_html(pup):
    photos = product_photos(pup)
    if not photos:
        return ""
    thumbs = "\n".join(
        f'<img src="{resolve_src(src, 1)}" alt="{pup["name"]} photo">' for src in photos
    )
    return f'<div class="gallery">{thumbs}</div>'


def _pup(slug, name, color, sex, weight, tone, folder, count, temperament, bio, status="Available"):
    return {
        "slug": slug,
        "name": name,
        "color": color,
        "sex": sex,
        "age": "8 weeks",
        "weight": weight,
        "status": status,
        "price": "$1,250",
        "tone": tone,
        "photos": [f"images/products/{folder}/photo-{i}.jpg" for i in range(1, count + 1)],
        "temperament": temperament,
        "bio": bio,
    }


PUPPIES = [
    {
        "slug": "jasper",
        "name": "Jasper",
        "color": "Blue merle",
        "sex": "Male",
        "age": "8 weeks",
        "weight": "About 3 lb",
        "status": "Available",
        "price": "$1,250",
        "tone": "merle",
        "photos": [
            "images/products/jasper/jasper-1.jpg",
            "images/products/jasper/jasper-2.jpg",
            "images/products/jasper/jasper-3.jpg",
            "images/products/jasper/jasper-4.jpg",
            "images/products/jasper/jasper-5.jpg",
        ],
        "temperament": "Tiny, fluffy, and alert, with a rare merle coat and a bright blue eye.",
        "bio": "Jasper is a blue-merle Pomeranian with a black-and-silver coat, tan points, and heterochromia — one ice-blue eye and one dark eye. He is a pocket-size companion with a plush teddy coat and a curious, people-focused nature.",
    },
    _pup(
        "cotton",
        "Cotton",
        "Cream",
        "Female",
        "About 2.8 lb",
        "cream",
        "p02",
        3,
        "A round teddy-bear coat, calm face, and a classic cream puffball look.",
        "Cotton is an exceptionally fluffy cream Pomeranian with a spherical teddy-bear coat, dark bead eyes, and a soft pinkish-brown nose. She has that classic pom-pom look and a calm, snuggly way of meeting new people.",
    ),
    _pup(
        "cocoa",
        "Cocoa",
        "Chocolate and white",
        "Male",
        "About 3.0 lb",
        "brown",
        "p03",
        4,
        "A chocolate boy with a white chest, plush fox face, and a playful streak.",
        "Cocoa is a chocolate-and-white Pomeranian with a dark mask, a bright white chest, and a dense teddy coat. He is eight weeks old, about three pounds, and already follows people from room to room.",
    ),
    _pup(
        "patch",
        "Patch",
        "Parti tan and white",
        "Female",
        "About 2.9 lb",
        "cream",
        "p04",
        5,
        "A tan, white, and brown parti girl with a saddle coat and bright eyes.",
        "Patch is a parti-color Pomeranian with tan, white, and brown markings and a thick fox-tail. She is curious, vocal, and happiest chasing a toy across a rug.",
    ),
    _pup(
        "mist",
        "Mist",
        "Blue merle",
        "Female",
        "About 2.7 lb",
        "merle",
        "p05",
        5,
        "A merle girl with a pale eye and a thick silver-and-black coat.",
        "Mist is a blue-merle girl with a striking pale eye and a plush silver-and-black coat. She is gentle in a lap, bold with toys, and already crate-curious after short naps.",
    ),
    _pup(
        "honey",
        "Honey",
        "Orange cream",
        "Female",
        "About 2.8 lb",
        "cream",
        "p06",
        5,
        "A tan-and-cream girl with a soft nest of a coat and a sweet face.",
        "Honey is an orange-cream Pomeranian photographed in her teepee nest. She is cuddly, food-motivated, and already offering a sit for a treat.",
    ),
    _pup(
        "mocha",
        "Mocha",
        "Chocolate and tan",
        "Male",
        "About 3.1 lb",
        "brown",
        "p07",
        5,
        "A chocolate boy with tan points, a plush mane, and a bold toy drive.",
        "Mocha is a chocolate-and-tan Pomeranian with a thick mane and tan points. He is bold with toys, gentle with children, and already learning crate naps.",
    ),
    _pup(
        "snow",
        "Snow",
        "White",
        "Female",
        "About 2.6 lb",
        "cream",
        "p08",
        5,
        "A white girl with a teddy-bear face and a dense double coat.",
        "Snow is a white Pomeranian with a round face, dark eyes, and a cloud of a coat. She is quiet in a crate nest, playful in short bursts, and deeply people-oriented.",
    ),
    _pup(
        "cloud",
        "Cloud",
        "Cream",
        "Female",
        "About 2.8 lb",
        "cream",
        "p09",
        5,
        "A cream girl on a soft bed with a round fox face.",
        "Cloud is a cream Pomeranian with a plush coat and a calm, snuggly way of meeting new people. She is food-motivated and already learning her name.",
    ),
    _pup(
        "maple",
        "Maple",
        "Orange sable",
        "Male",
        "About 3.0 lb",
        "orange",
        "p10",
        5,
        "A tan-and-cream boy with a black nose and a fox-red coat.",
        "Maple is an orange-sable boy with a black nose, cream furnishings, and a thick fox-tail. He is playful, food-motivated, and already offering a sit for a treat.",
    ),
    _pup(
        "ember",
        "Ember",
        "Orange sable",
        "Male",
        "About 3.0 lb",
        "orange",
        "p11",
        5,
        "A tan boy with a possible odd eye and a thick fox-tail.",
        "Ember is an orange-sable Pomeranian with a darker mask and a bright, curious face. He is vocal, people-focused, and happiest following you from room to room.",
    ),
    _pup(
        "pearl",
        "Pearl",
        "White",
        "Female",
        "About 2.7 lb",
        "cream",
        "p12",
        5,
        "A white girl with a plush coat and a black button nose.",
        "Pearl is a white Pomeranian with a dense double coat and a black button nose. She is gentle, crate-curious, and already walking short indoor trips.",
    ),
    _pup(
        "cinnamon",
        "Cinnamon",
        "Orange sable",
        "Female",
        "About 2.9 lb",
        "orange",
        "p13",
        5,
        "An orange sable girl from the same owner photo set as Maple.",
        "Cinnamon is an orange-sable girl with a fox-red coat and cream furnishings. The owner listing used the same photos as Maple; call for a current video so you can tell the two apart.",
    ),
    _pup(
        "truffle",
        "Truffle",
        "Dark chocolate",
        "Male",
        "About 3.1 lb",
        "brown",
        "p14",
        5,
        "A dark chocolate boy with a plush mane and a fox face.",
        "Truffle is a dark chocolate Pomeranian with a thick mane and a compact fox face. He is bold with toys, gentle in a lap, and already crate-curious.",
    ),
    _pup(
        "shadow",
        "Shadow",
        "Sable",
        "Male",
        "About 3.0 lb",
        "brown",
        "p15",
        5,
        "A sable boy with a darker mask and a thick double coat.",
        "Shadow is a sable Pomeranian with a darker mask and a dense weather coat. He is curious, vocal, and already walking a short house line.",
    ),
    _pup(
        "butter",
        "Butter",
        "Cream",
        "Female",
        "About 2.8 lb",
        "cream",
        "p16",
        5,
        "A cream girl sitting up with a teddy-bear face.",
        "Butter is a cream Pomeranian with a round teddy-bear face and a soft, dense coat. She is cuddly, food-motivated, and happiest in a lap.",
    ),
    _pup(
        "brindle",
        "Brindle",
        "Brindle and tan",
        "Male",
        "About 3.2 lb",
        "brown",
        "p17",
        4,
        "A tan-and-black brindle boy with a bold coat pattern.",
        "Brindle is a tan-and-black Pomeranian with a striking brindle pattern and a sturdy little frame. He is playful, food-motivated, and already crate-curious.",
    ),
    _pup(
        "amber",
        "Amber",
        "Orange sable",
        "Female",
        "About 2.9 lb",
        "orange",
        "p18",
        5,
        "A tan sable girl with a black nose and a fox-red coat.",
        "Amber is an orange-sable Pomeranian with a black nose, cream furnishings, and a plush fox-tail. She is gentle, people-oriented, and already learning her name.",
    ),
]


BLOG_ARTICLES = site_content.blog_articles()
BLOGS = [
    {
        "slug": slug,
        "title": data["title"],
        "date": data["date"],
        "img": data["img"],
        "excerpt": data["excerpt"],
    }
    for slug, data in BLOG_ARTICLES.items()
]


def prefix(depth):
    return "" if depth == 0 else "../"


def nav_html(depth, active):
    p = prefix(depth)
    links = [
        ("index.html", "home", "Home"),
        ("puppies.html", "puppies", "Puppies"),
        ("about.html", "about", "About Us"),
        ("care.html", "care", "Care Guide"),
        ("solution.html", "solution", "Solution"),
        ("blog.html", "blog", "Blog"),
        ("contact.html", "contact", "Order"),
        ("shipping.html", "shipping", "Shipping"),
        ("health.html", "health", "Health"),
    ]
    items = []
    for href, key, label in links:
        cls = ' class="active"' if key == active else ""
        items.append(f'<a href="{p}{href}"{cls}>{label}</a>')
    return "\n        ".join(items)


def header(depth, active):
    p = prefix(depth)
    return f'''<div class="topbar">
  <div class="wrap">
    <span>Family-raised AKC Pomeranian puppies</span>
    <a href="tel:{PHONE_TEL}">Call {PHONE}</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap nav-wrap">
    <a class="logo" href="{p}index.html">
      <svg class="logo-mark" viewBox="0 0 64 64" aria-hidden="true">
        <rect width="64" height="64" rx="16" fill="#2A2218"/>
        <path d="M32 14l4.2 8.8 9.6 1.2-7.1 6.6 1.9 9.5L32 35.6 23.4 40.1l1.9-9.5-7.1-6.6 9.6-1.2z" fill="#B8894A"/>
      </svg>
      <span class="logo-text"><strong>Evergold</strong><span>Pomeranians</span></span>
    </a>
    <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
        {nav_html(depth, active)}
    </nav>
    <a class="btn header-cta" href="{p}contact.html">Order</a>
  </div>
</header>'''


def wa_float(depth=0):
    return f'''<a class="wa-float" href="{wa_href()}" target="_blank" rel="noopener" aria-label="Order on WhatsApp">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path fill="#fff" d="M16.01 3C9.39 3 4 8.28 4 14.76c0 2.07.55 4.1 1.6 5.88L4 29l8.58-2.25a12.2 12.2 0 0 0 3.43.49c6.62 0 12.01-5.28 12.01-11.76C28.02 8.28 22.63 3 16.01 3zm6.96 16.66c-.29.82-1.45 1.5-2.04 1.6-.52.08-1.18.12-1.9-.12-.44-.14-1-.32-1.73-.63-3.04-1.32-5.02-4.38-5.17-4.58-.15-.2-1.22-1.62-1.22-3.1 0-1.47.77-2.2 1.04-2.5.27-.3.59-.37.79-.37h.57c.18 0 .43-.07.67.51.25.6.84 2.06.91 2.21.08.15.12.33.02.53-.1.2-.14.33-.29.5-.14.18-.31.4-.44.53-.15.15-.3.31-.13.61.18.3.8 1.32 1.72 2.14 1.18 1.05 2.18 1.38 2.48 1.53.3.15.48.13.66-.08.18-.2.75-.87.95-1.17.2-.3.4-.25.67-.15.27.1 1.72.81 2.01.96.3.15.49.22.56.35.08.12.08.71-.21 1.53z"/></svg>
  <span>WhatsApp</span>
</a>'''


def footer(depth, extra_scripts=""):
    p = prefix(depth)
    return f'''<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <p class="eyebrow">Ready to order a puppy?</p>
        <h2>Reserve on WhatsApp or email.</h2>
        <p>We send videos, the health packet, and deposit instructions in writing. Call {PHONE} if you want to talk first.</p>
      </div>
      <div class="btn-row">
        <a class="btn gold" href="{wa_href()}" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn ghost" href="{mail_href()}" style="color:#fff;border-color:rgba(255,255,255,.25)">Email {EMAIL}</a>
      </div>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h3>Evergold Pomeranians</h3>
      <p>Home-raised Pomeranian puppies with health testing, early socialization, and nationwide delivery support.</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE}</a></p>
      <p><a href="{mail_href()}">{EMAIL}</a></p>
    </div>
    <div>
      <h3>Explore</h3>
      <ul>
        <li><a href="{p}puppies.html">Available puppies</a></li>
        <li><a href="{p}about.html">About us</a></li>
        <li><a href="{p}care.html">Care guide</a></li>
        <li><a href="{p}solution.html">Our solution</a></li>
        <li><a href="{p}blog.html">Blog</a></li>
      </ul>
    </div>
    <div>
      <h3>Families</h3>
      <ul>
        <li><a href="{p}contact.html">Order via WhatsApp or email</a></li>
        <li><a href="{p}shipping.html">Shipping &amp; delivery</a></li>
        <li><a href="{p}health.html">Health &amp; vaccination</a></li>
      </ul>
    </div>
    <div>
      <h3>Visit</h3>
      <p>Inquiries daily 9am–6pm.<br>Puppy visits by appointment.</p>
    </div>
  </div>
  <div class="wrap copyright">© <span id="year"></span> Evergold Pomeranians. All rights reserved.</div>
</footer>
{wa_float(depth)}
<a class="call-bar" href="tel:{PHONE_TEL}">Call {PHONE}</a>
<script src="{p}js/main.js"></script>
{extra_scripts}'''


def page(title, depth, active, body, extra_head="", extra_scripts=""):
    p = prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | {BRAND}</title>
  <meta name="description" content="Evergold Pomeranians raises healthy, home-socialized Pomeranian puppies. Order on WhatsApp or email. Call {PHONE}.">
  <link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}css/styles.css">
  {extra_head}
</head>
<body>
{header(depth, active)}
<main>
{body}
</main>
{footer(depth, extra_scripts)}
</body>
</html>
'''


def puppy_card(pup, depth=0, compact=False):
    p = prefix(depth)
    pill = "available" if pup["status"] == "Available" else "reserved"
    blurb = pup["color"] if compact else f'{pup["age"]} · {pup["temperament"]}'
    return f'''<article class="puppy-card">
  <a href="{p}puppies/{pup["slug"]}.html" class="media">{product_img(pup, pup["name"] + " the Pomeranian puppy", depth)}</a>
  <div class="body">
    <div class="meta">
      <span class="pill {pill}">{pup["status"]}</span>
      <span class="pill">{pup["color"]}</span>
      <span class="pill">{pup["sex"]}</span>
    </div>
    <h3>{pup["name"]}</h3>
    <p>{blurb}</p>
    <div class="price">{pup["price"]}</div>
    <a class="btn" href="{p}puppies/{pup["slug"]}.html">View {pup["name"]}</a>
  </div>
</article>'''


def catalog_markup(depth=0, limit=None, compact=False):
    items = PUPPIES[:limit] if limit else PUPPIES
    if not items:
        p = prefix(depth)
        return f'''<div class="empty-catalog">
  <p class="eyebrow">Current availability</p>
  <h2>Puppies will appear here as they are listed.</h2>
  <p>Call {PHONE} to ask about this litter, or send a WhatsApp or email order.</p>
  <a class="btn" href="{p}contact.html">Order now</a>
</div>'''
    return '<div class="grid grid-3">\n' + "\n".join(puppy_card(p, depth, compact=compact) for p in items) + "\n</div>"


def home():
    posts = "\n".join(
        f'''<article class="post-card">
  <a class="media" href="blog/{b["slug"]}.html">{img(b["img"], b["title"])}</a>
  <div class="body">
    <p class="eyebrow">{b["date"]}</p>
    <h3><a href="blog/{b["slug"]}.html">{b["title"]}</a></h3>
  </div>
</article>'''
        for b in BLOGS[:3]
    )
    body = f'''<section class="hero">
  <img src="images/products/jasper/jasper-1.jpg" alt="Jasper the blue merle Pomeranian puppy" loading="lazy">
  <div class="wrap hero-copy">
    <p class="eyebrow">Home-raised companions</p>
    <h1>Pomeranian puppies with golden hearts.</h1>
    <p>Evergold Pomeranians is a small family kennel producing healthy, well-socialized puppies with honest health records and lifelong support. Order on WhatsApp or email — this site does not take a card.</p>
    <div class="btn-row">
      <a class="btn gold" href="puppies.html">See available puppies</a>
      <a class="btn ghost" href="contact.html" style="color:#fff;border-color:rgba(255,255,255,.35)">Order a puppy</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="frame"><img src="images/products/jasper/jasper-3.jpg" alt="Jasper the blue merle Pomeranian" loading="lazy"></div>
    <div>
      <p class="eyebrow">A quieter way to raise puppies</p>
      <h2>Raised underfoot, not in a barn.</h2>
      <p>Our puppies live in the house from day one. They hear kitchen sounds, meet visitors, learn crate naps, and leave with a start on potty habits, grooming, and confidence.</p>
      {site_content.HOME_STORY}
      <div class="stats">
        <div class="stat"><b>12+</b><span>years with the breed</span></div>
        <div class="stat"><b>AKC</b><span>registerable puppies</span></div>
        <div class="stat"><b>2 yr</b><span>health agreement</span></div>
      </div>
      <div class="btn-row">
        <a class="btn" href="solution.html">Read our solution</a>
        <a class="btn ghost" href="contact.html">Order via WhatsApp or email</a>
      </div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Current litter</p>
        <h2>Available Pomeranian puppies</h2>
      </div>
      <a class="btn ghost" href="puppies.html">View all puppies</a>
    </div>
    {catalog_markup(limit=6, compact=True)}
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">From the first brush to the last treat</p>
        <h2>What every Evergold family receives</h2>
      </div>
    </div>
    <div class="grid grid-3">
      <article class="care-card">
        <p class="eyebrow">01</p>
        <h3>Health start</h3>
        <p>Vaccines, deworming, a vet exam, and a packet for your veterinarian.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">02</p>
        <h3>Go-home kit</h3>
        <p>Food, a littermate blanket, and a written first-week plan.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">03</p>
        <h3>Lifetime guidance</h3>
        <p>Coat, feeding, and travel questions after placement. Call {PHONE}.</p>
      </article>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Pomeranian journal</p>
        <h2>From the blog</h2>
      </div>
      <a class="btn ghost" href="blog.html">Read more</a>
    </div>
    <div class="grid grid-3">{posts}</div>
  </div>
</section>'''
    return page("Home", 0, "home", body)


def puppies_index():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Meet the litter</p>
    <h1>Available Pomeranian puppies</h1>
    <p class="lead">Each puppy is raised in our home, vet-checked, and placed with a family that fits their temperament. Open a profile for owner photos, then order on WhatsApp or email. There is no website checkout. The current price is $1,250, and a puppy is reserved only after a written order and a received deposit.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {catalog_markup()}
  </div>
</section>'''
    return page("Available Pomeranian Puppies", 0, "puppies", body)


def puppy_page(pup):
    others = "\n".join(
        puppy_card(p, 1) for p in [x for x in PUPPIES if x["slug"] != pup["slug"]][:3]
    )
    pill = "available" if pup["status"] == "Available" else "reserved"
    cta = (
        (
            f'<a class="btn gold" href="../contact.html?puppy={pup["slug"]}">Order {pup["name"]}</a>'
            f'<a class="btn" href="{wa_href(pup["name"])}" target="_blank" rel="noopener">WhatsApp</a>'
        )
        if pup["status"] == "Available"
        else '<a class="btn" href="../puppies.html">See other puppies</a>'
    )
    gallery = gallery_html(pup)
    others_block = (
        f'''<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Other puppies</h2><a class="btn ghost" href="../puppies.html">All puppies</a></div>
    <div class="grid grid-3">{others}</div>
  </div>
</section>'''
        if others
        else ""
    )
    body = f'''<section class="page-hero">
  <div class="wrap puppy-hero">
    <div>
      <div class="frame">{product_img(pup, pup["name"] + " the Pomeranian", 1)}</div>
      {gallery}
    </div>
    <div>
      <p class="eyebrow">{pup["color"]} · {pup["sex"]}</p>
      <h1>{pup["name"]}</h1>
      <div class="meta">
        <span class="pill {pill}">{pup["status"]}</span>
        <span class="pill">{pup["age"]}</span>
        <span class="pill">{pup["weight"]}</span>
      </div>
      <div class="price">{pup["price"]}</div>
      <p>{pup["bio"]}</p>
      <div class="facts">
        <div class="fact"><span>Color</span><b>{pup["color"]}</b></div>
        <div class="fact"><span>Sex</span><b>{pup["sex"]}</b></div>
        <div class="fact"><span>Age</span><b>{pup["age"]}</b></div>
        <div class="fact"><span>Weight</span><b>{pup["weight"]}</b></div>
      </div>
      <p><strong>Temperament:</strong> {pup["temperament"]}</p>
      <div class="btn-row">
        {cta}
        <a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap article">
    <h2>What {pup["name"]} goes home with</h2>
    <ul>
      <li>Current vaccine and deworming record</li>
      <li>Vet wellness exam notes</li>
      <li>AKC registration application (where eligible)</li>
      <li>Two-year health agreement</li>
      <li>Starter food, blanket, and written care sheet</li>
    </ul>
    <p>Pickup is welcome by appointment. If you need delivery, see our <a href="../shipping.html">shipping and delivery information</a>.</p>
  </div>
</section>
{others_block}'''
    return page(pup["name"], 1, "puppies", body)


def about():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Our story</p>
    <h1>About Evergold Pomeranians</h1>
    <p class="lead">We are a small family kennel devoted to the Pomeranian: compact, bright, coated like a cloud, and happiest when they belong to someone.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div>
      <h2>Why we raise Poms this way</h2>
      <p>Evergold began after years of living with the breed and seeing too many puppies leave facilities that treated them as inventory. We keep only a few females, plan litters carefully, and raise every puppy in the house.</p>
      <p>Our standard is simple. Parents should be healthy, kind, and typey. Puppies should leave confident, handled, and documented. Families should feel they can call us in year five as easily as week one.</p>
      {site_content.ABOUT_EXTRA}
    </div>
    <div class="frame">{img("face", "Pomeranian portrait")}</div>
  </div>
</section>
<section class="section alt">
  <div class="wrap grid grid-3">
    <article class="care-card"><h3>Home-raised</h3><p>Puppies are born and raised indoors with daily handling, crate introductions, and household noise.</p></article>
    <article class="care-card"><h3>Health-first</h3><p>Breeding dogs are selected with attention to patellas, teeth, temperament, and coat. Puppies receive a vet exam before placement.</p></article>
    <article class="care-card"><h3>Honest matching</h3><p>We match energy and coat care expectations, not just color. If a puppy is not the right fit, we will say so.</p></article>
  </div>
</section>
<section class="section">
  <div class="wrap article">
    <h2>How families start with us</h2>
    <p>Look at the owner photos, read the <a href="solution.html">solution</a>, then send a WhatsApp or email order from the <a href="contact.html">order page</a>. We do not take a card on this website.</p>
  </div>
</section>'''
    return page("About Us", 0, "about", body)


def care():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Living well with a Pom</p>
    <h1>Pomeranian care guide</h1>
    <p class="lead">A compact dog still needs a full plan: coat, calories, teeth, and companionship. This is the routine we teach every Evergold family.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-2">
    <article class="care-card"><h3>Daily coat care</h3><p>Brush through the undercoat several times a week with a slicker and a metal comb. Pay extra attention behind the ears, in the pants, and under the collar. Never shave a Pomeranian double coat except for medical need.</p></article>
    <article class="care-card"><h3>Meals and weight</h3><p>Feed a high-quality small-breed puppy food three times a day until about six months, then twice daily. Pomeranians gain weight quickly on treats. Keep a lean waist you can feel.</p></article>
    <article class="care-card"><h3>Exercise</h3><p>Short play sessions and sniffs are better than long forced walks while growth plates are open. Adult Poms enjoy city walks, indoor games, and a safe, fenced yard.</p></article>
    <article class="care-card"><h3>Teeth and grooming</h3><p>Start tooth brushing early. Plan professional grooming every 6–8 weeks for sanitary trims, nail care, and a bath that is fully dried to the skin.</p></article>
    <article class="care-card"><h3>Training</h3><p>Poms are smart and can become barky if bored. Use short positive sessions, a crate or pen for rest, and plenty of people time. They want a job: tricks, puzzle feeders, or simply following you around.</p></article>
    <article class="care-card"><h3>Safety</h3><p>They are small. Watch stairs, larger dogs, and children who may drop them. Use a harness for walks and never leave a puppy unattended with chew hazards.</p></article>
  </div>
</section>
<section class="section alt">
  <div class="wrap article">
    <h2>A simple weekly rhythm</h2>
    <ol>
      <li>Brush coat 3–4 times; comb to the skin.</li>
      <li>Wipe eyes daily if needed; Poms can tear.</li>
      <li>Check ears, paws, and nails once a week.</li>
      <li>Keep vaccines and parasite prevention current with your veterinarian.</li>
      <li>Schedule a grooming day before the coat can mat.</li>
    </ol>
    {site_content.CARE_EXTRA}
    <p>Questions about a specific puppy? Call {PHONE}, or send WhatsApp or email, and we will walk through your setup.</p>
  </div>
</section>'''
    return page("Pomeranian Care Guide", 0, "care", body)


def blog_index():
    cards = "\n".join(
        f'''<article class="post-card">
  <a class="media" href="blog/{b["slug"]}.html">{img(b["img"], b["title"])}</a>
  <div class="body">
    <p class="eyebrow">{b["date"]}</p>
    <h3><a href="blog/{b["slug"]}.html">{b["title"]}</a></h3>
    <p>{b["excerpt"]}</p>
    <a class="btn ghost" href="blog/{b["slug"]}.html">Read article</a>
  </div>
</article>'''
        for b in BLOGS
    )
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Notes from the kennel</p>
    <h1>Pomeranian blog</h1>
    <p class="lead">Five featured guides, plus a 5,000-card kennel archive you can browse by page. Practical writing on puppies, coats, feeding, orders, and life with this little spitz.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2>Featured guides</h2></div>
    <div class="grid grid-2">{cards}</div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Kennel archive</p>
        <h2>5,000 blog cards</h2>
      </div>
      <p id="blog-count" class="lead" style="margin:0">Loading archive…</p>
    </div>
    <div id="blog-archive" class="grid grid-3"></div>
    <div class="blog-pager" id="blog-pager"></div>
  </div>
</section>'''
    return page(
        "Pomeranian Blog",
        0,
        "blog",
        body,
        extra_scripts='<script src="js/blog-archive.js"></script>',
    )


def blog_article(slug):
    a = BLOG_ARTICLES[slug]
    others = "\n".join(
        f'<p><a href="{b["slug"]}.html">{b["title"]}</a></p>'
        for b in BLOGS
        if b["slug"] != slug
    )
    body = f'''<section class="page-hero">
  <div class="wrap article">
    <p class="eyebrow">{a["date"]}</p>
    <h1>{a["title"]}</h1>
    <div class="article-hero">{img(a["img"], a["title"])}</div>
    {a["html"]}
    <h2>More from the journal</h2>
    {others}
  </div>
</section>'''
    return page(a["title"], 1, "blog", body)


def contact():
    options = "\n".join(
        f'<option value="{p["name"]}">{p["name"]} ({p["status"]})</option>' for p in PUPPIES
    )
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">No website checkout</p>
    <h1>Order via WhatsApp or email</h1>
    <p class="lead">Choose the puppy, then send the order on WhatsApp or by email. We reply with videos, the health packet, and deposit instructions in writing.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap article">
    {site_content.CONTACT_COPY}
    <label class="order-select">Puppy you want to order
      <select id="order-puppy">
        <option value="">A Pomeranian puppy</option>
        {options}
        <option value="Upcoming litter">Upcoming litter</option>
      </select>
    </label>
    <div class="order-grid">
      <a class="order-card whatsapp" id="order-whatsapp" href="{wa_href()}" target="_blank" rel="noopener">
        <p class="eyebrow">Fastest</p>
        <h2>Order on WhatsApp</h2>
        <p>Send a message to {PHONE}. Ask for the latest video and reservation steps. We answer during 9am–6pm.</p>
        <span class="btn gold">Open WhatsApp</span>
      </a>
      <a class="order-card email" id="order-email" href="{mail_href()}">
        <p class="eyebrow">Written record</p>
        <h2>Order by email</h2>
        <p>Write {EMAIL} with your city, the puppy name, and pickup or delivery. Keep the thread for your veterinarian.</p>
        <span class="btn">Open email</span>
      </a>
    </div>
    <p>Prefer a voice first? <a href="tel:{PHONE_TEL}">Call {PHONE}</a>, then send the written order so the reservation is on record. Read the <a href="solution.html">solution page</a> for the full placement path.</p>
  </div>
</section>'''
    return page("Order a Puppy", 0, "contact", body)


def solution():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">How placement works</p>
    <h1>The Evergold solution</h1>
    <p class="lead">A complete path from first message to the first night home: honest matching, documented health, WhatsApp or email ordering, and aftercare you can still use in year five.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap article">
    {site_content.SOLUTION_HTML}
    <div class="btn-row">
      <a class="btn gold" href="contact.html">Order via WhatsApp or email</a>
      <a class="btn ghost" href="puppies.html">See available puppies</a>
    </div>
  </div>
</section>'''
    return page("Our Solution", 0, "solution", body)


def shipping():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Getting home safely</p>
    <h1>Shipping &amp; delivery information</h1>
    <p class="lead">Pickup is always welcome. When that is not possible, we arrange ground transport or in-cabin airline delivery with experienced handlers.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-3">
    <article class="care-card"><h3>In-person pickup</h3><p>Meet your puppy at the kennel by appointment. We walk through feeding, coat care, and the health packet before you leave.</p></article>
    <article class="care-card"><h3>Ground transport</h3><p>For many U.S. cities we use trusted nanny services that travel by climate-controlled vehicle. Timing depends on route and weather.</p></article>
    <article class="care-card"><h3>Airline in-cabin</h3><p>When size and airline rules allow, a nanny can fly in-cabin with the puppy. Cargo is not our default and is discussed only when it is the safest remaining option.</p></article>
  </div>
</section>
<section class="section alt">
  <div class="wrap article">
    <h2>What delivery includes</h2>
    <ul>
      <li>Health certificate dated for travel</li>
      <li>Airline-approved carrier when flying</li>
      <li>Food, absorbent pads, and a familiar blanket</li>
      <li>Direct communication on departure and arrival</li>
    </ul>
    <h2>Cost and timing</h2>
    <p>Delivery fees vary by distance, season, and whether a nanny is flying or driving. We quote after we know your airport or city. Puppies travel only after veterinary clearance and when weather is safe.</p>
    <h2>Local meet-ups</h2>
    {site_content.SHIPPING_EXTRA}
  </div>
</section>'''
    return page("Shipping and Delivery", 0, "shipping", body)


def health():
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Records you can trust</p>
    <h1>Health &amp; vaccination information</h1>
    <p class="lead">Every Evergold puppy leaves with a vet exam, a written health agreement, and a record of vaccines and deworming you can hand to your veterinarian.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-2">
    <article class="care-card"><h3>Before go-home</h3><p>Puppies receive age-appropriate DA2PP vaccination, deworming on a schedule, a physical exam, and a health certificate when travel requires one.</p></article>
    <article class="care-card"><h3>What you continue</h3><p>Your veterinarian will finish the puppy series, discuss rabies timing for your state, and set parasite prevention. Bring our packet to the first visit.</p></article>
    <article class="care-card"><h3>Health agreement</h3><p>We offer a two-year agreement covering specified congenital conditions, with the details provided in writing at reservation. It is not a substitute for pet insurance.</p></article>
    <article class="care-card"><h3>Breed notes</h3><p>Pomeranians should be monitored for luxating patellas, dental crowding, tracheal sensitivity, and coat issues from shaving. We discuss these honestly before placement.</p></article>
  </div>
</section>
<section class="section alt">
  <div class="wrap article">
    <h2>Typical vaccine rhythm</h2>
    <p>Individual timing is set by our veterinarian and yours. A common pattern looks like this:</p>
    <ul>
      <li>First DA2PP around 6–8 weeks</li>
      <li>Boosters every 3–4 weeks until 16 weeks</li>
      <li>Rabies per local law, often near 16 weeks</li>
      <li>Bordetella and other vaccines if your vet recommends them for daycare or travel</li>
    </ul>
    <h2>If a puppy is unwell after travel</h2>
    <p>Contact your veterinarian first. Then call us at {PHONE}. Soft stools after a trip are common; lethargy, repeated vomiting, or refusal to eat is not something to wait on.</p>
    <div class="faq">
      <details open><summary>Do you health-test parent dogs?</summary><p>We evaluate breeding dogs for soundness, temperament, and known breed concerns, and we share what we have on each pairing when you inquire.</p></details>
      <details><summary>Are puppies examined by a veterinarian?</summary><p>Yes. Each puppy has a wellness exam before placement, and travel puppies receive a health certificate dated for the trip.</p></details>
      <details><summary>Do you offer a guarantee?</summary><p>Yes. Families receive a written two-year health agreement at reservation. Read it before you commit so the terms are clear.</p></details>
    </div>
    {site_content.HEALTH_EXTRA}
  </div>
</section>'''
    return page("Health and Vaccination", 0, "health", body)


def blog_entry_page():
    body = '''<section class="page-hero">
  <div class="wrap article">
    <p class="eyebrow" id="entry-date">Kennel archive</p>
    <h1 id="entry-title">Archive article</h1>
    <div class="article-hero" id="entry-hero"></div>
    <div id="entry-body"></div>
    <div class="btn-row">
      <a class="btn gold" href="../contact.html">Order via WhatsApp or email</a>
      <a class="btn ghost" href="../blog.html">Back to 5,000 cards</a>
    </div>
  </div>
</section>'''
    return page(
        "Archive article",
        1,
        "blog",
        body,
        extra_scripts='<script src="../js/blog-archive.js"></script>',
    )


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    puppies_dir = ROOT / "puppies"
    if puppies_dir.exists():
        for old in puppies_dir.glob("*.html"):
            old.unlink()
    write(ROOT / "index.html", home())
    write(ROOT / "puppies.html", puppies_index())
    write(ROOT / "about.html", about())
    write(ROOT / "care.html", care())
    write(ROOT / "solution.html", solution())
    write(ROOT / "blog.html", blog_index())
    write(ROOT / "contact.html", contact())
    write(ROOT / "shipping.html", shipping())
    write(ROOT / "health.html", health())
    write(ROOT / "blog" / "entry.html", blog_entry_page())
    for pup in PUPPIES:
        write(ROOT / "puppies" / f"{pup['slug']}.html", puppy_page(pup))
    for b in BLOGS:
        write(ROOT / "blog" / f"{b['slug']}.html", blog_article(b["slug"]))
    print("Wrote site pages")


if __name__ == "__main__":
    main()
