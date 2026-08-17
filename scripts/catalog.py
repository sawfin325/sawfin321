"""Catalog: categories and 10,000 generated liquidation lots."""
from __future__ import annotations

import random

def img(name: str) -> str:
    return f"assets/products/{name}.jpg"

IMG = {
    "hero": img("pallet-electronics"),
    "electronics": img("pallet-electronics"),
    "monitor": img("pallet-monitors"),
    "box": img("pallet-amazon-boxes"),
    "gaylord": img("pallet-gaylord"),
    "sneakers": img("pallet-sneakers"),
    "clothing": img("pallet-clothing"),
    "kitchen": img("pallet-kitchen"),
    "tools": img("pallet-tools"),
    "perfume": img("pallet-perfume"),
    "beauty": img("pallet-cosmetics"),
    "phone": img("pallet-phones"),
    "toys": img("pallet-toys"),
    "cards": img("pallet-cards"),
    "ac": img("pallet-airco"),
    "fridge": img("pallet-fridge"),
    "winter": img("pallet-winter"),
    "bags": img("pallet-bags"),
    "mystery": img("pallet-mystery"),
}

POOL = {
    "electronics": [
        img("pallet-electronics"), img("electronics-pallet-b"), img("electronics-pallet-c"),
        img("pallet-monitors"), img("elec-a"), img("elec-b"), img("elec-c"), img("elec-d"),
    ],
    "clothing": [
        img("pallet-clothing"), img("clothing-bin-b"), img("clothing-bin-c"), img("clothing-bin-d"),
        img("cloth-a"), img("cloth-b"), img("cloth-c"), img("pallet-bags"),
    ],
    "mystery": [
        img("pallet-amazon-boxes"), img("pallet-mystery"), img("mystery-pallet-b"),
        img("mystery-pallet-c"), img("mystery-pallet-d"), img("myst-a"), img("myst-b"), img("myst-c"),
    ],
    "pokemon": [img("pallet-cards"), img("tcg-boosters"), img("tcg-packs"), img("tcg-tins")],
    "tools": [img("pallet-tools"), img("tools-pallet-b")],
    "sneakers": [img("pallet-sneakers"), img("sneakers-pallet-b"), img("pallet-winter")],
    "kitchen": [img("pallet-kitchen"), img("kitchen-pallet-b")],
    "toys": [img("pallet-toys"), img("lego-duplo"), img("lego-modular"), img("lego-speed")],
    "phone": [
        img("phone-a"), img("phone-b"), img("phone-c"), img("phone-d"), img("phone-e"),
        img("phone-f"), img("phone-g"), img("phone-h"), img("phone-i"), img("phone-j"),
        img("pallet-phones"),
    ],
    "truck": [
        img("truck-a"), img("truck-b"), img("truck-c"), img("truck-d"),
        img("pallet-gaylord"), img("mystery-pallet-c"), img("mystery-pallet-b"), img("pallet-amazon-boxes"),
    ],
    "beauty": [img("pallet-cosmetics"), img("pallet-perfume")],
    "fridge": [img("pallet-fridge"), img("pallet-kitchen")],
    "ac": [img("pallet-airco"), img("kitchen-pallet-b")],
    "bags": [img("pallet-bags"), img("clothing-bin-b")],
}


def pick(pool, i):
    return pool[(i - 1) % len(pool)]

CATEGORIES = [
    {"slug": "elektronica", "name": "Electronic liquidation pallets", "image": IMG["electronics"],
     "blurb": "Amazon returns, salvage monitors, audio and IT accessories. Manifest or as-is by lot."},
    {"slug": "premium-electronics", "name": "Premium Electronics", "image": IMG["electronics"],
     "blurb": "Higher-MSRP electronics with an item manifest before you buy."},
    {"slug": "amazon-electronics", "name": "Amazon electronic liquidation pallets", "image": IMG["electronics"],
     "blurb": "FC return boxes and electronics pallets. Fixed price, no auction."},
    {"slug": "high-count", "name": "AMZ High Counts", "image": IMG["gaylord"],
     "blurb": "Tall gaylord stacks of mixed fulfillment returns. No item manifest."},
    {"slug": "amazon-mystery", "name": "Amazon mystery box pallets", "image": IMG["box"],
     "blurb": "Mystery box pallets and cartons from fulfillment return streams."},
    {"slug": "sneakers", "name": "Sneaker liquidation pallets", "image": IMG["sneakers"],
     "blurb": "Sport and lifestyle footwear with size and color breakdowns."},
    {"slug": "schoenen", "name": "Shoe liquidation pallets", "image": IMG["sneakers"],
     "blurb": "Mixed footwear, overstock and seasonal clearance."},
    {"slug": "winterschoenen", "name": "Winter shoes", "image": IMG["winter"],
     "blurb": "Boots and insulated shoes for the cold season."},
    {"slug": "kleding", "name": "Brand-name clothing", "image": IMG["clothing"],
     "blurb": "Branded apparel in lots from 250 pieces to full pallets."},
    {"slug": "costco-kleding", "name": "Costco clothing", "image": IMG["clothing"],
     "blurb": "Warehouse clothing lots for resellers in Europe and beyond."},
    {"slug": "zara-kleding", "name": "Zara clothing liquidation pallets", "image": IMG["clothing"],
     "blurb": "Fashion overstock in pallet format for outlets and online sellers."},
    {"slug": "sportkleding", "name": "Gym and fitness clothing", "image": IMG["clothing"],
     "blurb": "Fitness and athleisure apparel, tagged or in polybags."},
    {"slug": "keuken", "name": "Home and kitchen appliances", "image": IMG["kitchen"],
     "blurb": "Coffee machines, mixers, vacuums and air fryers."},
    {"slug": "koelkast", "name": "Refrigerator pallet liquidations", "image": IMG["fridge"],
     "blurb": "Fridge-freezer combos and large white goods on pallet."},
    {"slug": "airco", "name": "Air conditioner pallets", "image": IMG["ac"],
     "blurb": "Portable and split units from overstock and return programs."},
    {"slug": "gereedschap", "name": "Dewalt tool pallet liquidation", "image": IMG["tools"],
     "blurb": "Cordless and hand tools, combo kits and salvage lots."},
    {"slug": "milwaukee", "name": "Milwaukee power tools", "image": IMG["tools"],
     "blurb": "Power tools and jobsite sets for resale."},
    {"slug": "parfum", "name": "Perfume liquidation pallets", "image": IMG["perfume"],
     "blurb": "Sealed fragrances. Testers excluded unless listed."},
    {"slug": "cosmetica", "name": "Cosmetic liquidation pallets", "image": IMG["beauty"],
     "blurb": "Makeup and personal care with expiry dates in the spreadsheet."},
    {"slug": "iphone", "name": "iPhone liquidation pallets", "image": img("phone-a"),
     "blurb": "Smartphones with model, storage and battery status."},
    {"slug": "wearables", "name": "Apple Watch liquidation", "image": IMG["phone"],
     "blurb": "Watches, bands and earbuds in new or open-box condition."},
    {"slug": "laptop", "name": "Laptop liquidation pallets", "image": IMG["electronics"],
     "blurb": "Notebooks and Chromebooks, Grade A to salvage."},
    {"slug": "tv", "name": "TV liquidation pallets", "image": IMG["monitor"],
     "blurb": "Televisions and monitors, including salvage screens."},
    {"slug": "console", "name": "PlayStation 5 pallet", "image": IMG["electronics"],
     "blurb": "Consoles, controllers and gaming accessories."},
    {"slug": "bouwsets", "name": "LEGO liquidation pallets", "image": IMG["toys"],
     "blurb": "Sealed building sets and Technic lots for collectible resellers."},
    {"slug": "pokemon", "name": "Pokemon booster box", "image": IMG["cards"],
     "blurb": "Sealed displays, booster packs and trainer boxes."},
    {"slug": "speelgoed", "name": "Toy liquidation pallets", "image": IMG["toys"],
     "blurb": "General toys, seasonal lots and collectibles."},
    {"slug": "mystery-box", "name": "Amazon mystery box pallets", "image": IMG["mystery"],
     "blurb": "Mixed mystery pallets. Contents vary, sold as-is."},
    {"slug": "handtassen", "name": "Women's handbags", "image": IMG["bags"],
     "blurb": "Women's handbags in mixed lots, new."},
    {"slug": "truckload", "name": "Truckload liquidation wholesale", "image": img("truck-a"),
     "blurb": "Multi-pallet and truckload volume. Freight quoted on request."},
]

CAT_MAP = {c["slug"]: c for c in CATEGORIES}

LEGO_SETS = [
    ("LEGO Marvel Avengers Tower 76269 Building Kit 5201 pcs", img("lego-avengers-tower")),
    ("LEGO Star Wars: UCS Death Star (75159) rebuilt with all minifigures", img("lego-death-star")),
    ("Lego Technic 42055: Bucket Wheel Excavator – RETIRED – MISB – PERFECT!", img("lego-excavator")),
    ("LEGO TECHNIC 42115 Lamborghini Sián FKP 37 New Factory Sealed", img("lego-sian")),
    ("LEGO Technic 42177 Mercedes-Benz G 500 PROFESSIONAL Line", img("lego-g-wagon")),
    ("LEGO Technic McLaren P1 Model Car for Adults, Hyper Racing Car, Model Kit, 42172", img("lego-mclaren")),
    ("LEGO Technic Rough Terrain Crane 42082 Building Kit Gift Set Sealed NEW", img("lego-crane")),
    ("LEGO TECHNIC: App-Controlled Cat D11 Bulldozer (42131)", img("lego-bulldozer")),
    ("LEGO Icons Eiffel Tower 10307", img("lego-eiffel")),
    ("LEGO Technic Bugatti Chiron 42083 MISB", img("lego-bugatti")),
    ("LEGO Creator Expert Modular Building mix", img("lego-modular")),
    ("LEGO Star Wars UCS Millennium Falcon-style display lot", img("lego-falcon")),
    ("LEGO NINJAGO City Markets sealed cases", img("lego-ninjago")),
    ("LEGO Botanicals and seasonal sets pallet", img("lego-botanicals")),
    ("LEGO Speed Champions mixed sealed boxes", img("lego-speed")),
    ("LEGO DUPLO overstock pallet", img("lego-duplo")),
]

MYSTERY_NAMES = [
    "amazon mystery box pallet",
    "amazon mystery box electronics",
    "mystery boxes on amazon",
    "amazon mystery boxes for sale",
    "best place to buy amazon mystery boxes",
    "amazon mystery box wholesale",
    "amazon electronics mystery pallet",
    "mixed amazon mystery boxes",
]

POKEMON_NAMES = [
    "pokemon card pallets europe bulk buy",
    "pokemon pallets reseller europe",
    "buy pokemon liquidation pallets europe online",
    "wholesale pokemon products pallet europe",
    "pokemon pallets wholesale eu supplier",
    "buy pokemon tcg pallets europe",
    "pokemon liquidation pallets for sale eu",
    "pokemon cards pallet bulk europe",
    "pokemon booster box sealed case",
    "pokemon elite trainer box pallet",
]


def _money(rng, a, b):
    return round(rng.uniform(a, b), 2)


def _range_price(rng, price, variable=True):
    if variable and rng.random() < 0.55:
        return round(price * rng.uniform(6, 12), 2)
    return price


def generate_products(total: int = 10000, seed: int = 42) -> list[dict]:
    rng = random.Random(seed)
    weights = {
        "elektronica": 1600, "premium-electronics": 700, "amazon-electronics": 900,
        "high-count": 500, "amazon-mystery": 450, "sneakers": 400, "schoenen": 250,
        "winterschoenen": 200, "kleding": 700, "costco-kleding": 250, "zara-kleding": 200,
        "sportkleding": 180, "keuken": 400, "koelkast": 150, "airco": 180,
        "gereedschap": 350, "milwaukee": 180, "parfum": 220, "cosmetica": 220,
        "iphone": 250, "wearables": 150, "laptop": 180, "tv": 180, "console": 160,
        "bouwsets": 400, "pokemon": 450, "speelgoed": 300, "mystery-box": 400,
        "handtassen": 150, "truckload": 120,
    }
    missing = total - sum(weights.values())
    weights["elektronica"] += missing
    products: list[dict] = []
    n = 0

    def add(cat, name, price, price_max, msrp, items, condition, image, short):
        nonlocal n
        n += 1
        products.append({
            "slug": f"{cat}-{n:05d}",
            "name": name,
            "category": cat,
            "price": price,
            "priceMax": price_max,
            "msrp": msrp,
            "items": items,
            "condition": condition,
            "image": image,
            "short": short,
        })

    for cat, count in weights.items():
        meta = CAT_MAP[cat]
        image = meta["image"]
        for i in range(1, count + 1):
            if cat in ("elektronica", "premium-electronics", "amazon-electronics"):
                items = rng.choice([9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 26, 28, 31, 32, 37, 43, 47, 53, 70, 171, 200, 248, 279, 293, 305, 326])
                msrp = round(items * rng.uniform(48, 175), 2)
                price = round(msrp * rng.uniform(0.11, 0.32), 2)
                kind = rng.choice(["box", "pallet", "neg", "salvage", "home"])
                if kind == "box":
                    name = f"BOX OF RETURNS (Electronics) – ITEMS {items} – MSRP €{msrp:,.2f}"
                    condition = "Returns"
                    image = IMG["electronics"]
                elif kind == "neg":
                    name = f"NEG – Returns – Electronics – ITEMS: {items} – MSRP: {max(1, int(msrp/1000))}K"
                    condition = "Returns"
                    image = IMG["electronics"]
                elif kind == "salvage":
                    name = f"PALLET FROM NEG – Salvage – Monitors – ITEMS: {items} – MSRP: {int(msrp)}"
                    condition = "Salvage"
                    image = IMG["monitor"]
                    price = round(msrp * rng.uniform(0.06, 0.14), 2)
                elif kind == "home":
                    name = f"Home Improvements Pallets from AMZ – ITEMS: {items} – MSRP: {int(msrp/1000)}K"
                    condition = "Returns / mixed"
                    image = IMG["electronics"]
                else:
                    name = f"AMZ Electronics – {items} Items – €{msrp:,.2f} MSRP – PALLET – RETURNS"
                    condition = "Returns"
                    image = IMG["electronics"]
                add(cat, name, price, _range_price(rng, price, False), msrp, items, condition, pick(POOL["electronics"], i),
                    "Electronics lot from fulfillment returns. Manifest where listed, otherwise as-is.")

            elif cat == "high-count":
                price = _money(rng, 980, 3200)
                name = f"AMZ High Count #{40 + i}" if i % 2 else f"AMZ High Count FC #{i:02d}"
                add(cat, name, price, price, None, None, "Mixed / as-is", pick(POOL["truck"], i),
                    "Tall gaylord of fulfillment returns. No item list, fixed price.")

            elif cat in ("amazon-mystery", "mystery-box"):
                price = _money(rng, 180, 980)
                pmax = round(price * rng.uniform(2.5, 5.5), 2)
                name = MYSTERY_NAMES[(i - 1) % len(MYSTERY_NAMES)]
                if i > len(MYSTERY_NAMES):
                    name = f"{name} #{i}"
                add(cat, name, price, pmax, None, None, "As-is", pick(POOL["mystery"], i),
                    "Mystery-box pallet. Contents vary; condition from new to salvage.")

            elif cat in ("sneakers", "schoenen"):
                pairs = rng.choice([60, 72, 80, 96, 120, 144])
                msrp = pairs * rng.choice([55, 70, 85, 95, 120])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                name = rng.choice([
                    f"Mixed sneaker pallet – {pairs} pairs",
                    f"shoe liquidation pallets #{i}",
                    f"New Balance sneaker pallets – {pairs} pairs",
                    f"Sneaker clearance pallets #{i}",
                    f"Wholesale designer sneakers on pallets #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, pairs, "New / overstock", pick(POOL["sneakers"], i),
                    "Footwear with size and color breakdown in the manifest.")

            elif cat == "winterschoenen":
                pairs = rng.choice([48, 60, 72, 80])
                msrp = pairs * rng.choice([45, 60, 75])
                price = round(msrp * rng.uniform(0.22, 0.35), 2)
                name = f"Winter Boots Pallet #{i}" if i % 2 else f"women’s winter shoes #{i}"
                add(cat, name, price, _range_price(rng, price), msrp, pairs, "New", pick(POOL["sneakers"], i),
                    "Insulated boots, women's and men's, size rundown in the spreadsheet.")

            elif cat in ("kleding", "costco-kleding", "zara-kleding", "sportkleding"):
                pcs = rng.choice([200, 250, 300, 400])
                msrp = pcs * rng.choice([18, 24, 28, 35])
                price = round(msrp * rng.uniform(0.14, 0.28), 2)
                pmax = price if rng.random() < 0.45 else round(price * rng.uniform(3, 5), 2)
                if cat == "kleding":
                    name = f"Brand Name Clothing #{i} – {pcs}pcs"
                elif cat == "costco-kleding":
                    name = rng.choice([
                        f"costco clothing pallets bulk buy europe #{i}",
                        f"costco clothing pallets reseller europe #{i}",
                    ])
                elif cat == "zara-kleding":
                    name = f"zara clothing liquidation pallets europe #{i}"
                else:
                    name = f"fitness clothing pallet #{i} – {pcs}pcs"
                add(cat, name, price, pmax, msrp, pcs, "New with tags", pick(POOL["clothing"], i),
                    "Branded apparel tagged or in polybags. Size chart in the manifest.")

            elif cat == "keuken":
                items = rng.choice([16, 20, 24, 28, 36, 40])
                msrp = items * rng.choice([90, 140, 190, 240])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                name = rng.choice([
                    f"Kitchen appliance mix – {items} pcs",
                    f"bulk kitchen appliances pallets europe #{i}",
                    f"home appliance wholesale pallets eu #{i}",
                    f"Home appliance clearance pallets #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, items, "New / open box", pick(POOL["kitchen"], i),
                    "Home appliances with model numbers in the manifest. 230V.")

            elif cat == "koelkast":
                items = rng.choice([2, 3, 4, 6])
                msrp = items * rng.choice([700, 900, 1200])
                price = round(msrp * rng.uniform(0.22, 0.40), 2)
                add(cat, f"refrigerator pallet liquidations #{i} – {items} units", price, price, msrp, items,
                    "New / cosmetic", pick(POOL["fridge"], i), "Large white goods. Extra freight due to volume.")

            elif cat == "airco":
                items = rng.choice([8, 12, 16, 24, 40])
                msrp = items * rng.choice([220, 280, 350])
                price = round(msrp * rng.uniform(0.14, 0.28), 2)
                add(cat, f"Air-con returns – {items} pcs", price, price, msrp, items, "Returns / new", pick(POOL["ac"], i),
                    "Portable units, 230V. Missing hoses are noted in the manifest.")

            elif cat in ("gereedschap", "milwaukee"):
                items = rng.choice([20, 24, 30, 36, 42, 60])
                msrp = items * rng.choice([70, 95, 140, 180])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                name = rng.choice([
                    f"dewalt tool pallet liquidation #{i}",
                    f"Cordless tool mix pallet #{i}",
                    f"Jobsite combo – {items} kits",
                    f"Hand-tool bulk pallet #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, items, "New / overstock", pick(POOL["tools"], i),
                    "Tool lots. Battery and charger are not always included; see the manifest.")

            elif cat == "parfum":
                items = rng.choice([80, 100, 120, 150])
                msrp = items * rng.choice([35, 48, 62])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                add(cat, f"Fragrance pallet – {items} pcs #{i}", price, price, msrp, items, "New sealed",
                    pick(POOL["beauty"], i), "Sealed bottles. Batch codes where available.")

            elif cat == "cosmetica":
                items = rng.choice([120, 150, 180, 220])
                msrp = items * rng.choice([12, 18, 24])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                add(cat, f"cosmetic liquidation pallets #{i}", price, _range_price(rng, price), msrp, items,
                    "New", pick(POOL["beauty"], i), "Beauty mix. Expiry dates in the spreadsheet.")

            elif cat == "iphone":
                items = rng.choice([6, 8, 10, 12, 16])
                msrp = items * rng.choice([420, 580, 720, 890])
                price = round(msrp * rng.uniform(0.28, 0.48), 2)
                grade = rng.choice(["Grade A refurbished", "New sealed", "Consumer returns"])
                add(cat, f"Smartphone {grade} – {items} pcs #{i}", price, price, msrp, items, grade,
                    pick(POOL["phone"], i), "Model, storage and battery status in the manifest.")

            elif cat == "wearables":
                items = rng.choice([16, 20, 24, 30])
                msrp = items * rng.choice([90, 140, 190])
                price = round(msrp * rng.uniform(0.20, 0.36), 2)
                add(cat, f"Wearables and watches – {items} pcs #{i}", price, price, msrp, items,
                    "New / returns", pick(POOL["phone"], i), "Smartwatches and bands, mix of new and open box.")

            elif cat == "laptop":
                items = rng.choice([8, 10, 12, 16, 20])
                msrp = items * rng.choice([280, 450, 700])
                price = round(msrp * rng.uniform(0.18, 0.34), 2)
                add(cat, f"Laptop liquidation pallet – {items} pcs #{i}", price, price, msrp, items,
                    rng.choice(["Grade A", "Returns", "Salvage"]), pick(POOL["electronics"], i),
                    "Notebooks. Cosmetic grade listed per serial line.")

            elif cat == "tv":
                items = rng.choice([6, 8, 10, 12, 19, 21, 24])
                msrp = items * rng.choice([180, 280, 420])
                price = round(msrp * rng.uniform(0.08, 0.22), 2)
                add(cat, f"TV salvage – {items} pcs #{i}", price, price, msrp, items, "Salvage",
                    pick(POOL["electronics"], i), "Screens with damage. For technicians only.")

            elif cat == "console":
                items = rng.choice([12, 18, 24, 35])
                msrp = items * rng.choice([70, 120, 280])
                price = round(msrp * rng.uniform(0.20, 0.38), 2)
                add(cat, f"Consoles and accessories – {items} pcs #{i}", price, price, msrp, items,
                    "New / returns", pick(POOL["electronics"], i), "Controllers, headsets and sealed accessories.")

            elif cat == "bouwsets":
                base, image = LEGO_SETS[(i - 1) % len(LEGO_SETS)]
                name = base if i <= len(LEGO_SETS) else f"{base} #{i}"
                price = _money(rng, 180, 620)
                pmax = round(price * rng.uniform(7, 11), 2)
                add(cat, name, price, pmax, round(price * rng.uniform(2.2, 3.5), 2), rng.choice([1, 2, 4, 6]),
                    "New sealed", image,
                    "Sealed building set. Price range: single box to full case or pallet.")

            elif cat == "pokemon":
                name = POKEMON_NAMES[(i - 1) % len(POKEMON_NAMES)]
                if i > len(POKEMON_NAMES):
                    name = f"{name} #{i}"
                price = _money(rng, 220, 890)
                pmax = round(price * rng.uniform(4, 9), 2)
                add(cat, name, price, pmax, round(price * 2.4, 2), rng.choice([6, 8, 10, 12]),
                    "New / sealed", pick(POOL["pokemon"], i),
                    "Sealed TCG product. Price depends on case or pallet format.")

            elif cat == "speelgoed":
                items = rng.choice([80, 120, 160, 200])
                msrp = items * rng.choice([12, 16, 22])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                add(cat, f"General toys – {items} pcs #{i}", price, _range_price(rng, price), msrp, items,
                    "New / overstock", pick(POOL["toys"], i), "Accessible lot for new resellers.")

            elif cat == "handtassen":
                items = rng.choice([40, 60, 80, 100])
                msrp = items * rng.choice([18, 28, 40])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                add(cat, f"Women's handbag mix – {items} pcs #{i}", price, _range_price(rng, price), msrp, items,
                    "New", pick(POOL["bags"], i), "Mixed bag lot. Materials listed in the file.")

            else:  # truckload
                items = rng.choice([800, 1200, 2000, 4913])
                msrp = items * rng.uniform(40, 90)
                price = round(msrp * rng.uniform(0.08, 0.18), 2)
                pallets = rng.choice([6, 10, 14, 22])
                add(cat, f"Truckload – AMZ Electronics – {pallets} Pallets – {items} Items – {int(msrp/1000)}K MSRP",
                    price, price, round(msrp, 2), items, "Mixed / as-is", pick(POOL["truck"], i),
                    "For volume buyers only. Freight and load address on request.")

    rng.shuffle(products)
    for i, p in enumerate(products, 1):
        p["slug"] = f"{p['category']}-{i:05d}"

    from collections import defaultdict
    groups = defaultdict(list)
    for p in products:
        groups[p["category"]].append(p)
    cat_pool = {
        "iphone": POOL["phone"], "wearables": POOL["phone"],
        "elektronica": POOL["electronics"], "premium-electronics": POOL["electronics"],
        "amazon-electronics": POOL["electronics"], "laptop": POOL["electronics"],
        "tv": POOL["electronics"], "console": POOL["electronics"],
        "kleding": POOL["clothing"], "costco-kleding": POOL["clothing"],
        "zara-kleding": POOL["clothing"], "sportkleding": POOL["clothing"],
        "amazon-mystery": POOL["mystery"], "mystery-box": POOL["mystery"],
        "high-count": POOL["truck"], "truckload": POOL["truck"],
        "pokemon": POOL["pokemon"], "gereedschap": POOL["tools"], "milwaukee": POOL["tools"],
        "sneakers": POOL["sneakers"], "schoenen": POOL["sneakers"], "winterschoenen": POOL["sneakers"],
        "keuken": POOL["kitchen"], "speelgoed": POOL["toys"],
        "parfum": POOL["beauty"], "cosmetica": POOL["beauty"],
        "koelkast": POOL["fridge"], "airco": POOL["ac"], "handtassen": POOL["bags"],
    }
    for cat, items in groups.items():
        if cat == "bouwsets":
            continue
        pool = cat_pool.get(cat)
        if not pool:
            continue
        for i, p in enumerate(items):
            p["image"] = pool[i % len(pool)]
    return products[:total]


def by_category(products, slug, limit=8):
    out = []
    seen_imgs = set()
    for p in products:
        if p["category"] != slug:
            continue
        if p["image"] in seen_imgs:
            continue
        seen_imgs.add(p["image"])
        out.append(p["slug"])
        if len(out) >= limit:
            break
    return out
