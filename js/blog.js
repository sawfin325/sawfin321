const BLOG_COUNT = 10000;
const BLOG_PAGE_SIZE = 24;

const BLOG_AUTHORS = [
  "Nora Blake", "Marcus Ellison", "Priya Raman", "James Whitford", "Elena Vargas",
  "Kenji Sato", "Amelia Thorne", "Omar Haddad", "Clara Jensen", "Theo Moreau",
  "Sofia Almeida", "Daniel Cho",
];

const BLOG_TAGS = [
  "Buying guide", "Watch market", "Collector notes", "Authentication", "Steel sports",
  "Vintage", "Service", "Travel", "Investment", "Gauri atelier",
];

const BLOG_TITLES = [
  "How to buy a {brand} {model} without overpaying",
  "A collector's field guide to the {brand} {model}",
  "What {year} taught the market about the {brand} {model}",
  "Eight photographs that decide a {brand} {model} purchase",
  "Why the {brand} {model} still belongs on a shortlist",
  "Pre-owned {brand} {model}: condition, papers, and price",
  "The {brand} {model} versus the rest of the steel-sports field",
  "Service history, box codes, and the {brand} {model}",
  "Travel, insurance, and wearing a {brand} {model} abroad",
  "Investment case for the {brand} {model} in {year}",
  "First luxury watch: starting with a {brand} {model}",
  "Dealer vs private seller when hunting a {brand} {model}",
  "Reading a {brand} {model} listing like a professional",
  "What collectors get wrong about the {brand} {model}",
  "From WhatsApp to wrist: closing a {brand} {model} deal",
  "The {brand} {model} in gold, steel, and two-tone",
  "Authentication notes for a {brand} {model} in the wild",
  "A week with the {brand} {model} on a working wrist",
  "Why {brand} built the {model} the way they did",
  "Secondary-market patience and the {brand} {model}",
];

function blogHash(n, salt) {
  let x = Math.imul(n + 1, 0x9e3779b1) ^ salt;
  x = Math.imul(x ^ (x >>> 16), 0x85ebca6b);
  x = Math.imul(x ^ (x >>> 13), 0xc2b2ae35);
  return (x ^ (x >>> 16)) >>> 0;
}

function blogPick(arr, h) {
  return arr[h % arr.length];
}

function blogDate(n) {
  const start = Date.UTC(2018, 0, 1);
  const day = blogHash(n, 3) % 3100;
  const d = new Date(start + day * 86400000);
  return d.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });
}

function blogParagraphs(ctx) {
  const { brand, model, ref, year, price, condition, loc, n, movement, caseSize } = ctx;
  return [
    `Collectors do not buy a ${brand} ${model} because a thumbnail looked expensive. They buy it because the case, the bracelet, the movement, and the paperwork can survive a conversation with a watchmaker. This essay is written for that conversation. It is about the ${year} market for reference ${ref}, about ${condition.toLowerCase()} examples shipping from ${loc}, and about the difference between a listing that photographs well and a watch that still ticks with dignity after a week on the wrist. The asking price in our sample catalogue sits near ${price}, which is not a promise and not a floor. It is a coordinate. Everything else in these 1,500 words is how you navigate from that coordinate to a watch you will actually keep.`,
    `The ${brand} ${model} is a product of a maison that already knows how to sell desire. What it cannot sell on your behalf is patience. A rushed purchase of this reference usually fails in the same three places: a polished case that no longer has its factory brushed planes, a bracelet with stretch you only notice at 5 p.m., and papers that belong to a different serial. Those failures are not exotic. They are common. They are why luxerywatchsales puts eight photographs on every listing and why the Buy button opens WhatsApp or email instead of charging a card in silence. If you cannot see the ${model} from the side, you cannot buy the ${model}.`,
    `Start with the photographs. Front, three-quarter left, three-quarter right, profile, caseback, wrist, macro dial, clasp. That is the minimum a ${brand} ${model} deserves. Look at the lugs. Look at the crown guards if the design has them. Look at whether the bezel click, even in a still image, looks crisp or rounded by a decade of pockets. The macro dial on a ${model} will tell you if the lume plots are even, if the date wheel sits straight, and if the printer who did the text still worked for ${brand} that year. A seller who sends one hero shot is asking you to finance their lighting, not their watch.`,
    `Condition language is a dialect. New, mint, very good, good, and fair do not mean the same thing in every city. On a ${brand} ${model} listed as ${condition}, ask what that grade excludes. Hairlines on the clasp? A ding at 6? A replaced crystal? The honest answer is always specific. The dishonest answer is always a vibe. Write the listing code into WhatsApp. Ask for a video of the winding, the hand-setting, and the bracelet opening. A ${movement} movement should sound like a machine, not like sand. If the seller cannot film that, the watch is not ready to travel.`,
    `Papers and box are not decorations. On a ${brand} ${model}, the inner box stamp, the outer sleeve, the booklets, and the dated warranty card are a chain. Break one link and the price should move. Watch-only examples still have a market. They should not have a watch-with-papers price. Our listings badge box and papers separately so you can sort by the story you want. If you are buying this ${model} as a first luxury watch, papers will teach you less than a reputable seller. If you are buying it as a fifth, papers will teach you whether you can sell it as a sixth.`,
    `Price discovery on a ${brand} ${model} is public if you look at enough listings. Steel, gold, and two-tone do not trade on the same graph. A ${year} example at ${price} might be cheap, fair, or a trap depending on metal, bezel, and whether the clasp code matches the era. Compare at least five listings of the same reference ${ref}. Ignore the loudest discount. The loudest discount is often a polish, a missing link, or a seller who needs to make rent by Friday. Patience is the only free accessory ${brand} never charged extra for.`,
    `The movement inside a ${brand} ${model} is ${movement}. That sentence is not trivia. It tells you service intervals, parts availability, and whether a local watchmaker will smile or send the watch to a service center that quotes in months. A ${caseSize} case changes which straps you can wear and which cuffs you can ignore. Try the ${model} on in photographs first, then in person if you can, then on a video call if you cannot. Wrist shots in our galleries exist because a 40 mm promise on a spec sheet is not a 40 mm experience on a 16 cm wrist.`,
    `Authentication is a craft, not a filter. For a ${brand} ${model}, the usual tells live in fonts, rehaut alignment, serial engraving, clasp stamps, and the way the second hand hits the markers. A good dealer will point those out before you ask. A private seller might not know them and still have a genuine watch. That is why a named desk at luxerywatchsales sits between you and the parcel. Call +1 913-278-5312. Email luxerywatchsales@gmail.com. Open WhatsApp. Send the listing. If the ${model} is wrong, you want to hear it before the courier does.`,
    `Geography still matters. A ${brand} ${model} leaving ${loc} will cross customs, insurance desks, and a night in a warehouse you will never see. Insured shipping is not optional on a watch at ${price}. Ask who the courier is. Ask whether the invoice declares the correct value. Ask what happens if the box arrives crushed and the ${model} does not. Buyer Protection, on eligible orders, exists so that the seller is paid after you have inspected the piece, not after they have uploaded a tracking number. That sequence is the whole product.`,
    `Wearing the ${brand} ${model} is the part forums skip. A steel sports watch will pick up the grocery run, the airport tray, and the undersides of desks. A gold ${model} will pick up opinions. A diver will pick up water if you actually dive, which most owners will not. Decide which scratches you can love. A ${condition.toLowerCase()} example from ${year} already has a biography. Your job is not to freeze it. Your job is to not pay mint money for a biography someone already wrote with keys.`,
    `Service is the unglamorous chapter. A ${brand} ${model} with a ${movement} calibre will eventually need gaskets, oil, and a watchmaker who has seen this reference before. Ask for the last service date. Ask whether the crown seals. Ask whether the seller will stand behind a pressure test. If the answer is a shrug, the ${price} should fall. If the answer is a stack of invoices from a ${brand} service center, the ${price} can hold. Keep the same WhatsApp thread after the sale. A marketplace that disappears after delivery is a classifieds site with better type.`,
    `There is a version of this hobby that treats every ${brand} ${model} as a ticker symbol. That version is loud and often wrong. Watches are machines with taste attached. The ${model} will not email you a quarterly report. It will either make Tuesday nicer or it will sit in a safe while you check listings of a different reference. Buy the one you will wind. If that is this ${model}, the rest of the market can keep its charts. If it is not, no amount of ${year} hype will make the clasp feel like yours.`,
    `Gauri collectors should read this the same way Rolex collectors do: as a method, not a maison sermon. The eight-angle rule, the papers rule, the WhatsApp rule, and the escrow rule do not change because the dial is saffron or the case is a temple. A Gauri Lotus and a ${brand} ${model} both fail in the photographs first. They both succeed when a human being answers the phone. luxerywatchsales lists them in the same catalogue because a serious desk does not keep a second set of ethics for a second set of logos.`,
    `Private sellers and professional dealers are not moral opposites. They are different risk shapes. A dealer of the ${brand} ${model} in ${loc} lives on reviews and will still be there next year. A private seller of the same ${model} might be selling the only watch they ever loved. Ask both the same questions. Score the answers, not the job titles. Our listings label the seller type so you can choose which night you want to sleep. Neither path is wrong. Pretending they are identical is.`,
    `Search hygiene saves money. Filter ${brand}, then ${model}, then the year band around ${year}, then condition, then price. Open more than one tab. Walk the eight photographs on each. Note the listing codes. Message us with a shortlist, not a panic. We would rather talk you out of the wrong ${model} than pack it. That is not charity. A returned watch and an angry collector cost more than a slow yes. The Buy prompt exists so the yes is slow on purpose.`,
    `Steel, gold, and two-tone change the ${brand} ${model} more than marketing copy admits. Steel takes a life. Gold takes a light. Two-tone takes a decision about which half you will notice when it wears. The ${caseSize} case will look larger in gold because gold throws light. It will look smaller on a tropical strap. None of that is in the reference number ${ref} alone. It is in the photographs, in the wrist shot, and in the five minutes you spend imagining the ${model} next to your shirt cuffs instead of next to a studio infinity curve.`,
    `Counterfeits of a popular ${brand} ${model} have never been cheaper to manufacture or more expensive to ignore. The fakes got better at lume color and worse at the way a genuine clasp spring feels. Video helps. Macro helps. A second opinion helps. If a ${model} is thousands below every other ${year} example and the seller can only talk in emojis, you are not finding a deal. You are finding a tutorial. Close the tab. Open a listing with eight photographs and a telephone number that rings.`,
    `Travel with a ${brand} ${model} is a packing problem dressed as a lifestyle photograph. Use a cushioned pouch, not a loose pocket. Declare what customs requires. Photograph the ${model} on your wrist in the hotel safe lighting before you go out, so you have a baseline if something happens. Insurance that names the reference ${ref} is dull and correct. Instagram that names the restaurant is neither. Wear the watch. Do not audition it for strangers who did not pay for it.`,
    `When you are ready, the purchase path is short. Open the ${brand} ${model} listing. Read the badges. Tap Buy. Continue on WhatsApp or email luxerywatchsales@gmail.com. The message already carries the listing code, the reference ${ref}, and the ${price} coordinate. We confirm the watch is still in the case. We send payment instructions. You pay. The ${model} ships insured from ${loc}. You inspect it. Eligible protected orders pay the seller after that inspection. If something is wrong, you are already on the channel that can fix it. That is the entire pitch, stretched to the length a ${price} decision deserves.`,
    `Keep this essay. The ${brand} ${model} will still be here when you finish coffee. The market for reference ${ref} will move a little, then a little more, then it will pretend it never moved. Your wrist will not care. Your watchmaker will. Buy the example whose photographs you trust, whose seller you can still message in a year, and whose ${condition.toLowerCase()} life you are willing to continue. Then wear it as if the internet cannot see you. That is the only way a ${model} from ${year} becomes yours instead of remaining a listing that followed you around.`,
  ];
}

function makePost(n) {
  n = ((n % BLOG_COUNT) + BLOG_COUNT) % BLOG_COUNT;
  const h = blogHash(n, 91);
  const brand = BRANDS[h % BRANDS.length];
  const seeds = SEEDS_BY_BRAND[brand.name];
  const seed = seeds[h % seeds.length];
  const listing = makeListing ? makeListing(brand.name, n) : null;
  const year = listing ? listing.year : seed.year;
  const price = listing ? money(listing.price) : money(seed.price);
  const condition = listing ? listing.condition : seed.condition;
  const loc = listing ? listing.location : "Geneva, Switzerland";
  const title = blogPick(BLOG_TITLES, h)
    .replaceAll("{brand}", brand.name)
    .replaceAll("{model}", seed.model)
    .replaceAll("{year}", String(year));
  const tag = blogPick(BLOG_TAGS, blogHash(n, 7));
  const author = blogPick(BLOG_AUTHORS, blogHash(n, 11));
  const image = galleryPaths(brand.name, seed.model)[n % 8];
  const ctx = {
    brand: brand.name,
    model: seed.model,
    ref: seed.ref,
    year,
    price,
    condition,
    loc,
    n,
    movement: seed.movement,
    caseSize: seed.case,
  };
  const paras = blogParagraphs(ctx);
  const order = paras.map((_, i) => i);
  for (let i = order.length - 1; i > 0; i--) {
    const j = blogHash(n, 200 + i) % (i + 1);
    const tmp = order[i];
    order[i] = order[j];
    order[j] = tmp;
  }
  const lede = `Post ${n + 1} of ${BLOG_COUNT.toLocaleString("en-US")} in the luxerywatchsales journal. This entry is about the ${brand.name} ${seed.model}, written so a buyer can spend twenty minutes before spending ${price}.`;
  const close = `If this ${brand.name} ${seed.model} is the one, message the desk with listing notes from the catalogue, or open the live search for ${brand.name} and walk the eight photographs yourself. The journal is the homework. The watch is the point.`;
  const bodyParas = [lede, ...order.map((i) => paras[i]), close];
  const wordCount = bodyParas.join(" ").trim().split(/\s+/).length;
  const excerpt = paras[order[0]].split(". ").slice(0, 2).join(". ") + ".";
  return {
    id: `b-${n}`,
    n,
    tag,
    title,
    author,
    date: blogDate(n),
    read: `${Math.max(8, Math.round(wordCount / 180))} min`,
    image,
    brand: brand.name,
    model: seed.model,
    excerpt,
    wordCount,
    bodyParas,
  };
}

function getPostById(id) {
  if (!id) return makePost(0);
  if (id === "speedmaster-models" || id === "hublot-expensive") {
    const i = ARTICLES.findIndex((a) => a.id === id);
    return makePost(Math.max(0, i));
  }
  const m = /^b-(\d+)$/.exec(id);
  if (!m) return makePost(0);
  return makePost(Number(m[1]));
}

function queryBlog() {
  const page = Math.max(1, parseInt(params().get("page") || "1", 10));
  const pages = Math.ceil(BLOG_COUNT / BLOG_PAGE_SIZE);
  const start = (page - 1) * BLOG_PAGE_SIZE;
  const items = [];
  for (let n = start; n < Math.min(BLOG_COUNT, start + BLOG_PAGE_SIZE); n++) items.push(makePost(n));
  return { items, page, pages, total: BLOG_COUNT };
}

function blogCard(a) {
  return `<a class="article blog-card" href="article.html?id=${a.id}">
    <img src="${a.image}" alt="">
    <div class="tag">${a.tag}</div>
    <h3>${a.title}</h3>
    <p class="blog-excerpt">${a.excerpt}</p>
    <div class="byline">${a.author} · ${a.date} · ${a.read} · ${a.wordCount.toLocaleString()} words</div>
  </a>`;
}
