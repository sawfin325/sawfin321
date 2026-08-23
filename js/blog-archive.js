(function () {
  const SUBJECTS = [
    "crate training",
    "double-coat brushing",
    "small-breed feeding",
    "first-week potty trips",
    "apartment barking",
    "puppy socialization",
    "harness walking",
    "teacup size myths",
    "merle eye care",
    "cream coat staining",
    "chocolate Pomeranian sun care",
    "parti-color grooming",
    "go-home kit packing",
    "nanny flight days",
    "ground transport rest stops",
    "vaccine record folders",
    "patella watch-outs",
    "hypoglycemia warning signs",
    "tooth brushing starts",
    "nail care at home",
    "ear cleaning habits",
    "tear-stain wiping",
    "summer heat safety",
    "winter coat drying",
    "kids meeting a toy breed",
    "cat introductions",
    "larger-dog gates",
    "stair and sofa rules",
    "crate cover tricks",
    "night waking plans",
    "visitor limits in week one",
    "name-recognition games",
    "sit and wait rewards",
    "puzzle feeder use",
    "treat portion control",
    "kibble transition weeks",
    "water bowl placement",
    "groomer interviews",
    "line-brushing sections",
    "high-velocity drying",
    "never-shave reminders",
    "sanitary trim timing",
    "health-agreement reading",
    "WhatsApp order messages",
    "email reservation threads",
    "deposit confirmation steps",
    "pickup appointment flow",
    "first vet visit packet",
    "aftercare year-five calls",
    "honest color matching",
  ];
  const FRAMES = [
    "How to start",
    "A practical guide to",
    "What we tell families about",
    "Kennel notes on",
    "A calmer approach to",
    "Common mistakes in",
    "A first-month plan for",
    "Why we insist on",
    "Field notes about",
    "A short briefing on",
    "The Evergold take on",
    "How home-raised pups learn",
    "Questions to ask before",
    "A weekend checklist for",
    "What good looks like in",
    "When to slow down",
    "How to talk to your vet about",
    "A go-home reminder on",
    "The honest version of",
    "Daily habits that help",
  ];
  const SETTINGS = [
    "a first-time home",
    "an apartment",
    "a house with children",
    "a quiet adult household",
    "travel families",
  ];
  const IMAGES = [
    "https://images.unsplash.com/photo-1558788353-f76d92427f16?auto=format&fit=crop&w=900&q=70",
    "https://images.unsplash.com/photo-1620189507195-68309c04c4d0?auto=format&fit=crop&w=900&q=70",
    "https://images.unsplash.com/photo-1615751072497-5f5169febe17?auto=format&fit=crop&w=900&q=70",
    "https://images.unsplash.com/photo-1591946614720-90a587da4a36?auto=format&fit=crop&w=900&q=70",
    "https://images.unsplash.com/photo-1594099691860-c940b5768c45?auto=format&fit=crop&w=900&q=70",
  ];
  const TOTAL = 5000;
  const PAGE_SIZE = 24;

  function entry(index) {
    const subject = SUBJECTS[index % SUBJECTS.length];
    const frame = FRAMES[Math.floor(index / SUBJECTS.length) % FRAMES.length];
    const setting = SETTINGS[Math.floor(index / (SUBJECTS.length * FRAMES.length)) % SETTINGS.length];
    const id = index + 1;
    const title = frame + " " + subject + " for " + setting;
    const excerpt =
      "Card " +
      id +
      " of 5,000. A kennel note on " +
      subject +
      " when the puppy is going to " +
      setting +
      ".";
    return {
      id: id,
      title: title,
      excerpt: excerpt,
      subject: subject,
      frame: frame,
      setting: setting,
      img: IMAGES[index % IMAGES.length],
      date: "Archive note " + id,
    };
  }

  function paragraphs(item) {
    return [
      item.frame +
        " " +
        item.subject +
        " is one of the conversations we have before a puppy leaves Evergold. This archive card is written for " +
        item.setting +
        ". It is not a substitute for the featured guides or the solution page, but it repeats the same standard: a home-raised Pomeranian, a written health start, and an order that happens on WhatsApp or email.",
      "Begin with the puppy in front of you, not with a trend word. Watch how the dog rests, eats, and accepts a comb. If you are ordering, name the puppy, your city, and whether you will pick up or need delivery. Ask for the latest video and the health packet. A reservation is complete when the deposit is received and we confirm it in writing.",
      "For " +
        item.subject +
        ", keep the plan small enough to repeat every day. A Pomeranian does better with short sessions, measured meals, and a person who is actually home. If the coat is part of the question, remember the comb test: if a metal comb cannot pass to the skin, you are not finished. If food is part of the question, do not skip breakfast. If travel is part of the question, wait for a veterinarian clearance and safe weather.",
      "Read the solution page for the full placement path, including matching, vaccines, go-home day, and aftercare. Use the care guide for brushing, baths, stairs, and children. When you are ready to order, return to the contact page and send WhatsApp or email. Call +1 743-259-3337 if you want a voice first, then put the order in writing anyway.",
    ];
  }

  function renderArchive() {
    const grid = document.getElementById("blog-archive");
    const pager = document.getElementById("blog-pager");
    const count = document.getElementById("blog-count");
    if (!grid || !pager) return;
    const params = new URLSearchParams(window.location.search);
    const page = Math.max(1, Math.min(Math.ceil(TOTAL / PAGE_SIZE), parseInt(params.get("page") || "1", 10) || 1));
    const start = (page - 1) * PAGE_SIZE;
    const items = [];
    for (let i = start; i < Math.min(TOTAL, start + PAGE_SIZE); i += 1) {
      items.push(entry(i));
    }
    if (count) {
      count.textContent = "Showing " + (start + 1) + "–" + (start + items.length) + " of " + TOTAL + " cards";
    }
    grid.innerHTML = items
      .map(function (item) {
        return (
          '<article class="post-card">' +
          '<a class="media" href="blog/entry.html?id=' +
          item.id +
          '"><img src="' +
          item.img +
          '" alt="' +
          item.title +
          '" loading="lazy"></a>' +
          '<div class="body"><p class="eyebrow">' +
          item.date +
          "</p><h3><a href=\"blog/entry.html?id=" +
          item.id +
          '">' +
          item.title +
          "</a></h3><p>" +
          item.excerpt +
          '</p><a class="btn ghost" href="blog/entry.html?id=' +
          item.id +
          '">Read card</a></div></article>'
        );
      })
      .join("");

    const pages = Math.ceil(TOTAL / PAGE_SIZE);
    const buttons = [];
    const windowStart = Math.max(1, page - 2);
    const windowEnd = Math.min(pages, page + 2);
    if (page > 1) {
      buttons.push('<a href="blog.html?page=' + (page - 1) + '">Prev</a>');
    }
    if (windowStart > 1) {
      buttons.push('<a href="blog.html?page=1">1</a>');
    }
    for (let p = windowStart; p <= windowEnd; p += 1) {
      if (p === page) {
        buttons.push('<button class="is-current" type="button">' + p + "</button>");
      } else {
        buttons.push('<a href="blog.html?page=' + p + '">' + p + "</a>");
      }
    }
    if (windowEnd < pages) {
      buttons.push('<a href="blog.html?page=' + pages + '">' + pages + "</a>");
    }
    if (page < pages) {
      buttons.push('<a href="blog.html?page=' + (page + 1) + '">Next</a>');
    }
    pager.innerHTML = buttons.join("");
  }

  function renderEntry() {
    const titleEl = document.getElementById("entry-title");
    const dateEl = document.getElementById("entry-date");
    const bodyEl = document.getElementById("entry-body");
    const hero = document.getElementById("entry-hero");
    if (!titleEl || !bodyEl) return;
    const id = parseInt(new URLSearchParams(window.location.search).get("id") || "1", 10);
    const safe = Math.max(1, Math.min(TOTAL, id || 1));
    const item = entry(safe - 1);
    document.title = item.title + " | Evergold Pomeranians";
    titleEl.textContent = item.title;
    if (dateEl) dateEl.textContent = item.date;
    if (hero) {
      hero.innerHTML = '<img src="' + item.img + '" alt="' + item.title + '">';
    }
    bodyEl.innerHTML = paragraphs(item)
      .map(function (p) {
        return "<p>" + p + "</p>";
      })
      .join("");
  }

  if (document.getElementById("blog-archive")) {
    renderArchive();
  }
  if (document.getElementById("entry-body")) {
    renderEntry();
  }
})();
