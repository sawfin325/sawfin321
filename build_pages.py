#!/usr/bin/env python3
from pathlib import Path

ROOT = Path("/workspace")
PHONE = "+1 743-259-3337"
PHONE_TEL = "+17432593337"
BRAND = "Evergold Pomeranians"

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
    "portrait": "https://images.unsplash.com/photo-1517423440428-a5a00ad98d8a?auto=format&fit=crop&w=1400&q=80",
    "cozy": "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?auto=format&fit=crop&w=1400&q=80",
}


def img(key, alt):
    return f'<img src="{IMG[key]}" alt="{alt}" loading="lazy">'


PUPPIES = [
    {
        "slug": "luna",
        "name": "Luna",
        "color": "Orange sable",
        "sex": "Female",
        "age": "10 weeks",
        "weight": "3.4 lb",
        "status": "Available",
        "price": "$2,800",
        "img": "hero",
        "temperament": "Affectionate, bright, and already crate-comfortable.",
        "bio": "Luna is a classic orange-sable girl with a plush coat, a fox-like expression, and a calm confidence around people. She loves lap time, short play bursts, and following her person from room to room. She is a wonderful match for a first-time Pomeranian family that wants a devoted companion.",
    },
    {
        "slug": "coco",
        "name": "Coco",
        "color": "Chocolate",
        "sex": "Male",
        "age": "9 weeks",
        "weight": "3.1 lb",
        "status": "Available",
        "price": "$3,200",
        "img": "brown",
        "temperament": "Curious, playful, and eager to learn.",
        "bio": "Coco has a rich chocolate coat and a sparkling personality. He is the first to investigate a new toy and the last to leave a snuggle pile. He is well-started on name recognition, gentle handling, and house manners, and he will thrive with daily walks, puzzle toys, and a family that enjoys a little extra sparkle.",
    },
    {
        "slug": "bella",
        "name": "Bella",
        "color": "Cream",
        "sex": "Female",
        "age": "11 weeks",
        "weight": "3.8 lb",
        "status": "Reserved",
        "price": "Reserved",
        "img": "white",
        "temperament": "Gentle, people-oriented, and quietly confident.",
        "bio": "Bella is a cream beauty with a soft expression and a sweet, measured way of meeting new people. She is currently reserved for her family. If you love her look, we can help match you with a similar upcoming puppy from our cream and white lines.",
    },
    {
        "slug": "milo",
        "name": "Milo",
        "color": "Orange",
        "sex": "Male",
        "age": "10 weeks",
        "weight": "3.6 lb",
        "status": "Available",
        "price": "$2,600",
        "img": "tongue",
        "temperament": "Happy, social, and full of comic timing.",
        "bio": "Milo is the sunshine of the current litter. He greets the day with a wag, a stretch, and a request for breakfast. He is sturdy, well-socialized with children in our home, and a great choice for a family that wants a cheerful little shadow who still settles nicely after play.",
    },
    {
        "slug": "pearl",
        "name": "Pearl",
        "color": "White",
        "sex": "Female",
        "age": "8 weeks",
        "weight": "2.9 lb",
        "status": "Available",
        "price": "$3,400",
        "img": "sitting",
        "temperament": "Sensitive, intelligent, and velcro-loyal.",
        "bio": "Pearl is a refined white girl with a powder-puff coat and an old-soul stare. She prefers a calmer household, loves being carried for short moments, and is already learning to sit for meals. She will do best with a family that enjoys grooming, indoor enrichment, and lots of gentle conversation.",
    },
    {
        "slug": "ember",
        "name": "Ember",
        "color": "Red sable",
        "sex": "Male",
        "age": "12 weeks",
        "weight": "4.1 lb",
        "status": "Available",
        "price": "$2,900",
        "img": "grass",
        "temperament": "Outgoing, athletic for his size, and people-smart.",
        "bio": "Ember is a red-sable boy who loves the garden, a rolling ball, and a warm nap in a sun patch. He is a little further along in training than the younger pups and is ready for a family that wants weekend adventures, city walks, and a Pomeranian who still fits in a travel bag.",
    },
]


BLOGS = [
    {
        "slug": "first-week-home",
        "title": "The first week home with a Pomeranian puppy",
        "date": "August 4, 2026",
        "img": "cozy",
        "excerpt": "A calm routine for sleep, meals, potty trips, and bonding in those first seven days.",
    },
    {
        "slug": "grooming-double-coat",
        "title": "How to care for a Pomeranian double coat",
        "date": "July 18, 2026",
        "img": "fluffy",
        "excerpt": "Brushing, bathing, and the one grooming habit that prevents painful mats.",
    },
    {
        "slug": "nutrition-small-breed",
        "title": "Feeding small-breed puppies the right way",
        "date": "June 29, 2026",
        "img": "orange",
        "excerpt": "Meal size, schedule, and why Pomeranians should never skip breakfast.",
    },
    {
        "slug": "teacup-myths",
        "title": "Teacup Pomeranians: what the word really means",
        "date": "June 9, 2026",
        "img": "portrait",
        "excerpt": "Size, health, and how we talk about puppies honestly at Evergold.",
    },
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
        ("blog.html", "blog", "Blog"),
        ("contact.html", "contact", "Contact"),
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
    <a class="btn header-cta" href="{p}contact.html">Inquire</a>
  </div>
</header>'''


def footer(depth):
    p = prefix(depth)
    return f'''<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <p class="eyebrow">Ready to meet a puppy?</p>
        <h2>Call {PHONE} or send an inquiry.</h2>
        <p>We are happy to share videos, pedigrees, and upcoming litter dates.</p>
      </div>
      <div class="btn-row">
        <a class="btn gold" href="tel:{PHONE_TEL}">Call now</a>
        <a class="btn ghost" href="{p}contact.html" style="color:#fff;border-color:rgba(255,255,255,.25)">Contact form</a>
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
    </div>
    <div>
      <h3>Explore</h3>
      <ul>
        <li><a href="{p}puppies.html">Available puppies</a></li>
        <li><a href="{p}about.html">About us</a></li>
        <li><a href="{p}care.html">Care guide</a></li>
        <li><a href="{p}blog.html">Blog</a></li>
      </ul>
    </div>
    <div>
      <h3>Families</h3>
      <ul>
        <li><a href="{p}contact.html">Contact</a></li>
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
<a class="call-bar" href="tel:{PHONE_TEL}">Call {PHONE}</a>
<script src="{p}js/main.js"></script>'''


def page(title, depth, active, body, extra_head=""):
    p = prefix(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | {BRAND}</title>
  <meta name="description" content="Evergold Pomeranians raises healthy, home-socialized Pomeranian puppies. Call {PHONE}.">
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
{footer(depth)}
</body>
</html>
'''


def puppy_card(pup, depth=0):
    p = prefix(depth)
    pill = "available" if pup["status"] == "Available" else "reserved"
    return f'''<article class="puppy-card">
  <a href="{p}puppies/{pup["slug"]}.html" class="media">{img(pup["img"], pup["name"] + " the Pomeranian puppy")}</a>
  <div class="body">
    <div class="meta">
      <span class="pill {pill}">{pup["status"]}</span>
      <span class="pill">{pup["color"]}</span>
      <span class="pill">{pup["sex"]}</span>
    </div>
    <h3>{pup["name"]}</h3>
    <p>{pup["age"]} · {pup["temperament"]}</p>
    <div class="price">{pup["price"]}</div>
    <a class="btn" href="{p}puppies/{pup["slug"]}.html">View {pup["name"]}</a>
  </div>
</article>'''


def home():
    cards = "\n".join(puppy_card(p) for p in PUPPIES[:3])
    posts = "\n".join(
        f'''<article class="post-card">
  <a class="media" href="blog/{b["slug"]}.html">{img(b["img"], b["title"])}</a>
  <div class="body">
    <p class="eyebrow">{b["date"]}</p>
    <h3><a href="blog/{b["slug"]}.html">{b["title"]}</a></h3>
    <p>{b["excerpt"]}</p>
  </div>
</article>'''
        for b in BLOGS[:3]
    )
    body = f'''<section class="hero">
  {img("hero", "Fluffy Pomeranian puppy smiling at the camera")}
  <div class="wrap hero-copy">
    <p class="eyebrow">Home-raised companions</p>
    <h1>Pomeranian puppies with golden hearts.</h1>
    <p>Evergold Pomeranians is a small family kennel producing healthy, well-socialized puppies with honest health records and lifelong support.</p>
    <div class="btn-row">
      <a class="btn gold" href="puppies.html">See available puppies</a>
      <a class="btn ghost" href="tel:{PHONE_TEL}" style="color:#fff;border-color:rgba(255,255,255,.35)">Call {PHONE}</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="frame">{img("sitting", "Cream Pomeranian sitting for a portrait")}</div>
    <div>
      <p class="eyebrow">A quieter way to raise puppies</p>
      <h2>Raised underfoot, not in a barn.</h2>
      <p>Our puppies live in the house from day one. They hear kitchen sounds, meet visitors, learn crate naps, and leave with a start on potty habits, grooming, and confidence.</p>
      <p>Parents are selected for sound structure, sweet temperaments, and coat quality. We share health testing, vaccine records, and a written health agreement with every family.</p>
      <div class="stats">
        <div class="stat"><b>12+</b><span>years with the breed</span></div>
        <div class="stat"><b>AKC</b><span>registerable puppies</span></div>
        <div class="stat"><b>2 yr</b><span>health agreement</span></div>
      </div>
      <div class="btn-row">
        <a class="btn" href="about.html">About our kennel</a>
        <a class="btn ghost" href="health.html">Health information</a>
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
    <div class="grid grid-3">
      {cards}
    </div>
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
        <p>Age-appropriate vaccines, deworming, vet check, and a record packet you can hand to your veterinarian on day one.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">02</p>
        <h3>Go-home kit</h3>
        <p>Food sample, blanket with littermate scent, collar, and a written care plan for sleep, meals, and the first grooming appointment.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">03</p>
        <h3>Lifetime guidance</h3>
        <p>We stay available for questions on coat, feeding, travel, and temperament. Call {PHONE} any time you need us.</p>
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
    cards = "\n".join(puppy_card(p) for p in PUPPIES)
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Meet the litter</p>
    <h1>Available Pomeranian puppies</h1>
    <p class="lead">Each puppy is raised in our home, vet-checked, and placed with a family that fits their temperament. Open a profile to see photos, personality notes, and reservation details.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-3">
    {cards}
  </div>
</section>'''
    return page("Available Pomeranian Puppies", 0, "puppies", body)


def puppy_page(pup):
    others = "\n".join(puppy_card(p, 1) for p in PUPPIES if p["slug"] != pup["slug"])
    pill = "available" if pup["status"] == "Available" else "reserved"
    cta = (
        f'<a class="btn gold" href="../contact.html">Reserve {pup["name"]}</a>'
        if pup["status"] == "Available"
        else '<a class="btn" href="../puppies.html">See other puppies</a>'
    )
    body = f'''<section class="page-hero">
  <div class="wrap puppy-hero">
    <div class="frame">{img(pup["img"], pup["name"] + " the Pomeranian")}</div>
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
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Other puppies</h2><a class="btn ghost" href="../puppies.html">All puppies</a></div>
    <div class="grid grid-3">{others}</div>
  </div>
</section>'''
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
      <p>Call {PHONE} to talk through upcoming litters, color plans, or whether a Pomeranian is the right fit for your home.</p>
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
    <p>Questions about a specific puppy? Call {PHONE} and we will walk through your setup.</p>
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
    <p class="lead">Practical writing on puppies, coats, feeding, and the culture of this little spitz.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-2">{cards}</div>
</section>'''
    return page("Pomeranian Blog", 0, "blog", body)


def blog_article(slug):
    articles = {
        "first-week-home": {
            "title": "The first week home with a Pomeranian puppy",
            "date": "August 4, 2026",
            "img": "cozy",
            "html": f'''<p>The first week is not about perfect training. It is about sleep, food, and feeling safe. Keep the world small and predictable.</p>
<h2>Set up before pickup</h2>
<ul>
  <li>A crate or covered pen in a quiet corner</li>
  <li>The same food we send home</li>
  <li>A playpen, pee pads or a nearby door, and a harness</li>
  <li>A slicker brush, comb, and nail clippers</li>
</ul>
<h2>A first-week schedule</h2>
<p>Puppies this small sleep a lot. Offer meals three times a day, potty trips after waking, eating, and play, and several short training moments of 2–3 minutes. Do not host a parade of visitors in week one.</p>
<h2>What is normal</h2>
<p>Soft stools after travel, a night or two of crying, and a dip in appetite can happen. Call us at {PHONE} or your veterinarian if energy crashes, vomiting continues, or the puppy will not eat.</p>''',
        },
        "grooming-double-coat": {
            "title": "How to care for a Pomeranian double coat",
            "date": "July 18, 2026",
            "img": "fluffy",
            "html": '''<p>A Pomeranian coat is a weather shield: a dense undercoat and a longer guard coat. When it is maintained, it looks like a halo. When it is neglected, it mats at the skin.</p>
<h2>Tools that actually work</h2>
<ul>
  <li>Slicker brush for the body</li>
  <li>Metal comb to check you reached the skin</li>
  <li>Pin brush for finishing</li>
  <li>A high-velocity dryer after baths</li>
</ul>
<h2>The rule we repeat</h2>
<p>If the comb does not pass to the skin, you are not finished. Line-brush in sections. Never shave down a healthy Pom coat for convenience; it can ruin texture and sun protection.</p>
<h2>Puppy coats</h2>
<p>The fluffy puppy coat will blow as the adult coat comes in. This is the season to stay ahead of mats. Book a groomer who knows spitz breeds.</p>''',
        },
        "nutrition-small-breed": {
            "title": "Feeding small-breed puppies the right way",
            "date": "June 29, 2026",
            "img": "orange",
            "html": f'''<p>Pomeranian puppies have tiny stomachs and fast metabolisms. Skipping meals can be dangerous, especially in very small pups.</p>
<h2>What we send home</h2>
<p>We start puppies on a named small-breed puppy kibble. Keep that food for at least two weeks, then transition slowly if you change brands. Measure with a scale, not a giant scoop.</p>
<h2>Treats</h2>
<p>Training treats should be pea-sized. Cheese and table scraps add up. If the waist disappears, cut treats first, not meals.</p>
<h2>Water and hypoglycemia</h2>
<p>Fresh water always. If a young puppy becomes wobbly, weak, or glassy-eyed, this is an emergency. Rub a little honey on the gums and call your vet. We also welcome a call at {PHONE}.</p>''',
        },
        "teacup-myths": {
            "title": "Teacup Pomeranians: what the word really means",
            "date": "June 9, 2026",
            "img": "portrait",
            "html": '''<p>“Teacup” is a marketing word, not an AKC variety. Pomeranians are already a toy breed. Extra-tiny puppies are not a separate, healthier type.</p>
<h2>How we talk about size</h2>
<p>We share current weight, estimated adult range, and parent sizes. Some of our dogs finish smaller; some finish a sturdy 6–8 pounds. Structure and health matter more than fitting in a teacup.</p>
<h2>Risks of chasing tiny</h2>
<p>Very small dogs can have more fragile bones, dental crowding, and blood-sugar swings. We do not breed down to an extreme.</p>
<h2>Choosing honestly</h2>
<p>If you want a lap companion who still has bone and bounce, we will help you pick that puppy. If a listing promises a 2-pound adult as a guaranteed trait, be cautious.</p>''',
        },
    }
    a = articles[slug]
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
    options = "\n".join(f'<option value="{p["name"]}">{p["name"]} ({p["status"]})</option>' for p in PUPPIES)
    body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">We would love to hear from you</p>
    <h1>Contact</h1>
    <p class="lead">Tell us about your home, the puppy you are drawn to, and your timeline. We answer by phone fastest.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap contact-panel">
    <aside class="contact-card">
      <p class="eyebrow">Call the kennel</p>
      <h2>Talk with us today</h2>
      <p><a class="phone-xl" href="tel:{PHONE_TEL}">{PHONE}</a></p>
      <p>Inquiries 9am–6pm daily. Puppy visits are by appointment so the litter can rest.</p>
      <p>We can share recent videos, parent photos, and shipping options for your city.</p>
    </aside>
    <form class="form" id="contact-form">
      <div class="form-row">
        <label>Name<input name="name" required></label>
        <label>Phone<input name="phone" type="tel" required></label>
      </div>
      <label>Email<input name="email" type="email" required></label>
      <label>Puppy of interest
        <select name="puppy">
          <option value="">Select a puppy or litter</option>
          {options}
          <option value="upcoming">Upcoming litter</option>
        </select>
      </label>
      <label>Message<textarea name="message" required placeholder="Tell us about your family, yard, and timeline."></textarea></label>
      <button class="btn" type="submit">Send inquiry</button>
      <div class="form-note">Thank you. We have your message and will follow up. For a faster reply, call {PHONE}.</div>
    </form>
  </div>
</section>'''
    return page("Contact", 0, "contact", body)


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
    <p>In some cases we can meet partway. Call {PHONE} to talk through the kindest route for your puppy.</p>
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
  </div>
</section>'''
    return page("Health and Vaccination", 0, "health", body)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    write(ROOT / "index.html", home())
    write(ROOT / "puppies.html", puppies_index())
    write(ROOT / "about.html", about())
    write(ROOT / "care.html", care())
    write(ROOT / "blog.html", blog_index())
    write(ROOT / "contact.html", contact())
    write(ROOT / "shipping.html", shipping())
    write(ROOT / "health.html", health())
    for pup in PUPPIES:
        write(ROOT / "puppies" / f"{pup['slug']}.html", puppy_page(pup))
    for b in BLOGS:
        write(ROOT / "blog" / f"{b['slug']}.html", blog_article(b["slug"]))
    print("Wrote site pages")


if __name__ == "__main__":
    main()
