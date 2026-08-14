"""Catalog: categories and 10,000 generated liquidation lots."""
from __future__ import annotations

import random

def img(name: str) -> str:
    return f"assets/products/{name}.jpg"

IMG = {
    "hero": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80",
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
    "electronics": [img("pallet-electronics"), img("electronics-pallet-b"), img("electronics-pallet-c"), img("pallet-monitors")],
    "clothing": [img("pallet-clothing"), img("clothing-bin-b"), img("clothing-bin-c"), img("clothing-bin-d")],
    "mystery": [img("pallet-amazon-boxes"), img("pallet-mystery"), img("mystery-pallet-b"), img("mystery-pallet-c"), img("mystery-pallet-d")],
    "pokemon": [img("pallet-cards"), img("tcg-boosters"), img("tcg-packs"), img("tcg-tins")],
    "tools": [img("pallet-tools"), img("tools-pallet-b")],
    "sneakers": [img("pallet-sneakers"), img("sneakers-pallet-b"), img("pallet-winter")],
    "kitchen": [img("pallet-kitchen"), img("kitchen-pallet-b")],
    "toys": [img("pallet-toys"), img("lego-duplo"), img("lego-modular"), img("lego-speed")],
}


def pick(pool, i):
    return pool[(i - 1) % len(pool)]

CATEGORIES = [
    {"slug": "elektronica", "name": "electronic liquidation pallets", "image": IMG["electronics"],
     "blurb": "Amazon-retouren, salvage monitors, audio en IT-accessoires. Manifest of as-is per lot."},
    {"slug": "premium-electronics", "name": "Premium Electronics", "image": IMG["electronics"],
     "blurb": "Hogere MSRP-elektronica met artikelmanifest vóór aankoop."},
    {"slug": "amazon-electronics", "name": "amazon electronic liquidation pallets", "image": IMG["electronics"],
     "blurb": "FC-retourdozen en pallets elektronica, vast geprijsd, geen veiling."},
    {"slug": "high-count", "name": "AMZ High Counts", "image": IMG["gaylord"],
     "blurb": "Hoge gaylord-stapels gemengde fulfillment-retouren. Geen itemmanifest."},
    {"slug": "amazon-mystery", "name": "amazon mystery box nederland", "image": IMG["box"],
     "blurb": "Mystery box pallets en dozen uit fulfillment-retourstromen."},
    {"slug": "sneakers", "name": "sneaker liquidation pallets", "image": IMG["sneakers"],
     "blurb": "Sport- en lifestyle schoeisel met maat- en kleuroverzicht."},
    {"slug": "schoenen", "name": "shoe liquidation pallets", "image": IMG["sneakers"],
     "blurb": "Gemengd schoeisel, overstock en seizoensclearance."},
    {"slug": "winterschoenen", "name": "winter shoes", "image": IMG["winter"],
     "blurb": "Laarzen en gevoerde schoenen voor het najaar."},
    {"slug": "kleding", "name": "Brand Name Clothings", "image": IMG["clothing"],
     "blurb": "Merkkleding in partijen van 250 stuks tot volle pallets."},
    {"slug": "costco-kleding", "name": "cosco Clothings", "image": IMG["clothing"],
     "blurb": "Warehouse-kledinglots voor wederverkopers in NL en EU."},
    {"slug": "zara-kleding", "name": "zara clothing liquidation pallets", "image": IMG["clothing"],
     "blurb": "Mode-overstock in palletformaat voor outlets en Vinted-verkopers."},
    {"slug": "sportkleding", "name": "gymshark fitness clothing", "image": IMG["clothing"],
     "blurb": "Fitness- en athleisure kleding, tagged of in polybag."},
    {"slug": "keuken", "name": "home and kitchen appliances", "image": IMG["kitchen"],
     "blurb": "Koffiemachines, mixers, stofzuigers en airfryers."},
    {"slug": "koelkast", "name": "refrigerator pallet liquidations", "image": IMG["fridge"],
     "blurb": "Koel-vriescombinaties en grote witte goederen op pallet."},
    {"slug": "airco", "name": "Air Conditioners Pallets", "image": IMG["ac"],
     "blurb": "Draagbare en split-units uit overstock en retourprogramma's."},
    {"slug": "gereedschap", "name": "dewalt tool pallet liquidation", "image": IMG["tools"],
     "blurb": "Accu- en handgereedschap, combosets en salvage lots."},
    {"slug": "milwaukee", "name": "milwaukee power tools", "image": IMG["tools"],
     "blurb": "Powertools en jobsitesets voor wederverkoop."},
    {"slug": "parfum", "name": "perfume liquidation pallets", "image": IMG["perfume"],
     "blurb": "Verzegelde geuren, testers uitgesloten tenzij vermeld."},
    {"slug": "cosmetica", "name": "cosmetic liquidation pallets", "image": IMG["beauty"],
     "blurb": "Make-up en verzorging met THT in het spreadsheet."},
    {"slug": "iphone", "name": "iphone liquidation pallets", "image": IMG["phone"],
     "blurb": "Smartphones met model, opslag en batterijstatus."},
    {"slug": "wearables", "name": "apple watch liquidation", "image": IMG["phone"],
     "blurb": "Watches, bands en earbuds in nieuw of open-box staat."},
    {"slug": "laptop", "name": "laptop liquidation pallets", "image": IMG["electronics"],
     "blurb": "Notebooks en Chromebooks, Grade A tot salvage."},
    {"slug": "tv", "name": "tv liquidation pallets", "image": IMG["monitor"],
     "blurb": "Televisies en monitors, inclusief salvage-schermen."},
    {"slug": "console", "name": "playstation 5 pallet", "image": IMG["electronics"],
     "blurb": "Consoles, controllers en gaming-accessoires."},
    {"slug": "bouwsets", "name": "Lego liquidation pallets", "image": IMG["toys"],
     "blurb": "Sealed bouwsets en Technic-lots voor collectible-wederverkopers."},
    {"slug": "pokemon", "name": "pokemon booster box", "image": IMG["cards"],
     "blurb": "Sealed displays, booster packs en trainer boxes."},
    {"slug": "speelgoed", "name": "toy liquidation pallets", "image": IMG["toys"],
     "blurb": "Algemeen speelgoed, seizoenslots en collectibles."},
    {"slug": "mystery-box", "name": "amazon mystery box nederland", "image": IMG["mystery"],
     "blurb": "Gemengde mystery pallets. Inhoud varieert, as-is."},
    {"slug": "handtassen", "name": "womens handbags", "image": IMG["bags"],
     "blurb": "Dameshandtassen in mixlots, nieuw."},
    {"slug": "truckload", "name": "truckload liquidation wholesale", "image": IMG["gaylord"],
     "blurb": "Multi-pallet en truckload-volume, vracht op aanvraag."},
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
    "mystery box kopen amazon",
    "amazon mystery boxes for sale",
    "best place to buy amazon mystery boxes",
    "amazon mystery box nederland",
    "mystery boxen amazon",
]

POKEMON_NAMES = [
    "pokemon card pallets europe bulk buy",
    "pokemon pallets reseller europe",
    "buy pokemon liquidation pallets europe online",
    "wholesale pokemon products pallet europe",
    "pokemon pallets wholesale eu supplier",
    "buy pokemon tcg pallets netherlands",
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
                    condition = "Retour"
                    image = IMG["electronics"]
                elif kind == "neg":
                    name = f"NEG – Returns – Electronics – ITEMS: {items} – MSRP: {max(1, int(msrp/1000))}K"
                    condition = "Retour"
                    image = IMG["electronics"]
                elif kind == "salvage":
                    name = f"PALLET FROM NEG – Salvage – Monitors – ITEMS: {items} – MSRP: {int(msrp)}"
                    condition = "Salvage"
                    image = IMG["monitor"]
                    price = round(msrp * rng.uniform(0.06, 0.14), 2)
                elif kind == "home":
                    name = f"Home Improvements Pallets from AMZ – ITEMS: {items} – MSRP: {int(msrp/1000)}K"
                    condition = "Retour / mixed"
                    image = IMG["electronics"]
                else:
                    name = f"AMZ Electronics – {items} Items – €{msrp:,.2f} MSRP – PALLET – RETURNS"
                    condition = "Retour"
                    image = IMG["electronics"]
                add(cat, name, price, _range_price(rng, price, False), msrp, items, condition, pick(POOL["electronics"], i),
                    "Elektronicalot uit fulfillment-retouren. Manifest waar vermeld, anders as-is.")

            elif cat == "high-count":
                price = _money(rng, 980, 3200)
                name = f"AMZ High Count #{40 + i}" if i % 2 else f"AMZ High Count FC #{i:02d}"
                add(cat, name, price, price, None, None, "Gemengd / as-is", IMG["gaylord"],
                    "Hoge gaylord van fulfillment-retouren. Geen itemlijst, vaste prijs.")

            elif cat in ("amazon-mystery", "mystery-box"):
                price = _money(rng, 180, 980)
                pmax = round(price * rng.uniform(2.5, 5.5), 2)
                name = MYSTERY_NAMES[(i - 1) % len(MYSTERY_NAMES)]
                if i > len(MYSTERY_NAMES):
                    name = f"{name} #{i}"
                add(cat, name, price, pmax, None, None, "As-is", pick(POOL["mystery"], i),
                    "Mystery box pallet. Inhoud varieert; conditie van nieuw tot salvage.")

            elif cat in ("sneakers", "schoenen"):
                pairs = rng.choice([60, 72, 80, 96, 120, 144])
                msrp = pairs * rng.choice([55, 70, 85, 95, 120])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                name = rng.choice([
                    f"Gemengde sneakerpallet – {pairs} paar",
                    f"shoe liquidation pallets #{i}",
                    f"New Balance sneaker palettes – {pairs} paar",
                    f"Pallets met opruimingsgoederen voor sneakers #{i}",
                    f"Groothandel in designer sneakers op pallets #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, pairs, "Nieuw / overstock", pick(POOL["sneakers"], i),
                    "Schoeisel met maat- en kleuroverzicht in het manifest.")

            elif cat == "winterschoenen":
                pairs = rng.choice([48, 60, 72, 80])
                msrp = pairs * rng.choice([45, 60, 75])
                price = round(msrp * rng.uniform(0.22, 0.35), 2)
                name = f"Winter Boots Pallet #{i}" if i % 2 else f"women’s winter shoes #{i}"
                add(cat, name, price, _range_price(rng, price), msrp, pairs, "Nieuw", IMG["winter"],
                    "Gevoerde laarzen, dames en heren, maatoverzicht in Excel.")

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
                add(cat, name, price, pmax, msrp, pcs, "Nieuw met tags", pick(POOL["clothing"], i),
                    "Merkkleding tagged of in polybag. Maattabel in het manifest.")

            elif cat == "keuken":
                items = rng.choice([16, 20, 24, 28, 36, 40])
                msrp = items * rng.choice([90, 140, 190, 240])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                name = rng.choice([
                    f"Keukenapparatuur mix – {items} stuks",
                    f"bulk kitchen appliances pallets europe #{i}",
                    f"home appliance wholesale pallets eu #{i}",
                    f"Opruiming van pallets met huishoudelijke apparaten #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, items, "Nieuw / open box", pick(POOL["kitchen"], i),
                    "Huishoudapparaten met modelnummers in het manifest. 230V.")

            elif cat == "koelkast":
                items = rng.choice([2, 3, 4, 6])
                msrp = items * rng.choice([700, 900, 1200])
                price = round(msrp * rng.uniform(0.22, 0.40), 2)
                add(cat, f"refrigerator pallet liquidations #{i} – {items} units", price, price, msrp, items,
                    "Nieuw / cosmetisch", IMG["fridge"], "Grote witte goederen. Extra vracht door volume.")

            elif cat == "airco":
                items = rng.choice([8, 12, 16, 24, 40])
                msrp = items * rng.choice([220, 280, 350])
                price = round(msrp * rng.uniform(0.14, 0.28), 2)
                add(cat, f"Airco retouren – {items} stuks", price, price, msrp, items, "Retour / nieuw", IMG["ac"],
                    "Draagbare units, 230V. Ontbrekende slangen staan in het manifest.")

            elif cat in ("gereedschap", "milwaukee"):
                items = rng.choice([20, 24, 30, 36, 42, 60])
                msrp = items * rng.choice([70, 95, 140, 180])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                name = rng.choice([
                    f"dewalt tool pallet liquidation #{i}",
                    f"Accugereedschap mixpallet #{i}",
                    f"Jobsite combo – {items} kits",
                    f"Handgereedschap bulkpallet #{i}",
                ])
                add(cat, name, price, _range_price(rng, price), msrp, items, "Nieuw / overstock", pick(POOL["tools"], i),
                    "Gereedschaplots. Accu en lader niet altijd inbegrepen; zie manifest.")

            elif cat == "parfum":
                items = rng.choice([80, 100, 120, 150])
                msrp = items * rng.choice([35, 48, 62])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                add(cat, f"Parfumpallet – {items} stuks #{i}", price, price, msrp, items, "Nieuw verzegeld",
                    IMG["perfume"], "Sealed flacons. Batchcodes waar beschikbaar.")

            elif cat == "cosmetica":
                items = rng.choice([120, 150, 180, 220])
                msrp = items * rng.choice([12, 18, 24])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                add(cat, f"cosmetic liquidation pallets #{i}", price, _range_price(rng, price), msrp, items,
                    "Nieuw", IMG["beauty"], "Beauty mix. THT-data in het spreadsheet.")

            elif cat == "iphone":
                items = rng.choice([6, 8, 10, 12, 16])
                msrp = items * rng.choice([420, 580, 720, 890])
                price = round(msrp * rng.uniform(0.28, 0.48), 2)
                grade = rng.choice(["Grade A refurbished", "Nieuw verzegeld", "Consumentenretour"])
                add(cat, f"Smartphone {grade} – {items} stuks #{i}", price, price, msrp, items, grade,
                    IMG["phone"], "Model, opslag en batterijstatus in het manifest.")

            elif cat == "wearables":
                items = rng.choice([16, 20, 24, 30])
                msrp = items * rng.choice([90, 140, 190])
                price = round(msrp * rng.uniform(0.20, 0.36), 2)
                add(cat, f"Wearables en watches – {items} stuks #{i}", price, price, msrp, items,
                    "Nieuw / retour", IMG["phone"], "Smartwatches en bands, mix van nieuw en open box.")

            elif cat == "laptop":
                items = rng.choice([8, 10, 12, 16, 20])
                msrp = items * rng.choice([280, 450, 700])
                price = round(msrp * rng.uniform(0.18, 0.34), 2)
                add(cat, f"Laptop liquidation pallet – {items} stuks #{i}", price, price, msrp, items,
                    rng.choice(["Grade A", "Retour", "Salvage"]), IMG["electronics"],
                    "Notebooks. Cosmetische staat per seriële regel.")

            elif cat == "tv":
                items = rng.choice([6, 8, 10, 12, 19, 21, 24])
                msrp = items * rng.choice([180, 280, 420])
                price = round(msrp * rng.uniform(0.08, 0.22), 2)
                add(cat, f"TV salvage – {items} stuks #{i}", price, price, msrp, items, "Salvage",
                    IMG["monitor"], "Schermen met schade. Alleen voor technici.")

            elif cat == "console":
                items = rng.choice([12, 18, 24, 35])
                msrp = items * rng.choice([70, 120, 280])
                price = round(msrp * rng.uniform(0.20, 0.38), 2)
                add(cat, f"Console en accessoires – {items} stuks #{i}", price, price, msrp, items,
                    "Nieuw / retour", IMG["electronics"], "Controllers, headsets en gesealde accessoires.")

            elif cat == "bouwsets":
                base, image = LEGO_SETS[(i - 1) % len(LEGO_SETS)]
                name = base if i <= len(LEGO_SETS) else f"{base} #{i}"
                price = _money(rng, 180, 620)
                pmax = round(price * rng.uniform(7, 11), 2)
                add(cat, name, price, pmax, round(price * rng.uniform(2.2, 3.5), 2), rng.choice([1, 2, 4, 6]),
                    "Nieuw verzegeld", image,
                    "Sealed bouwset. Prijsbereik: enkele doos tot volle doos/pallet.")

            elif cat == "pokemon":
                name = POKEMON_NAMES[(i - 1) % len(POKEMON_NAMES)]
                if i > len(POKEMON_NAMES):
                    name = f"{name} #{i}"
                price = _money(rng, 220, 890)
                pmax = round(price * rng.uniform(4, 9), 2)
                add(cat, name, price, pmax, round(price * 2.4, 2), rng.choice([6, 8, 10, 12]),
                    "Nieuw / sealed", pick(POOL["pokemon"], i),
                    "Sealed TCG-product. Prijs afhankelijk van case- of palletformaat.")

            elif cat == "speelgoed":
                items = rng.choice([80, 120, 160, 200])
                msrp = items * rng.choice([12, 16, 22])
                price = round(msrp * rng.uniform(0.16, 0.30), 2)
                add(cat, f"Algemeen speelgoed – {items} stuks #{i}", price, _range_price(rng, price), msrp, items,
                    "Nieuw / overstock", pick(POOL["toys"], i), "Toegankelijk lot voor nieuwe wederverkopers.")

            elif cat == "handtassen":
                items = rng.choice([40, 60, 80, 100])
                msrp = items * rng.choice([18, 28, 40])
                price = round(msrp * rng.uniform(0.18, 0.32), 2)
                add(cat, f"Dameshandtassen mix – {items} stuks #{i}", price, _range_price(rng, price), msrp, items,
                    "Nieuw", IMG["bags"], "Mixlot tassen. Materialen in het bestand.")

            else:  # truckload
                items = rng.choice([800, 1200, 2000, 4913])
                msrp = items * rng.uniform(40, 90)
                price = round(msrp * rng.uniform(0.08, 0.18), 2)
                pallets = rng.choice([6, 10, 14, 22])
                add(cat, f"Truckload – AMZ Electronics – {pallets} Pallets – {items} Items – {int(msrp/1000)}K MSRP",
                    price, price, round(msrp, 2), items, "Gemengd / as-is", IMG["gaylord"],
                    "Alleen voor volume-kopers. Vracht en laadadres op aanvraag.")

    rng.shuffle(products)
    # keep stable unique slugs after shuffle
    for i, p in enumerate(products, 1):
        p["slug"] = f"{p['category']}-{i:05d}"
    return products[:total]


def by_category(products, slug, limit=8, unique_names=True):
    out = []
    seen = set()
    for p in products:
        if p["category"] != slug:
            continue
        key = p["name"].split(" #")[0]
        if unique_names and key in seen:
            continue
        seen.add(key)
        out.append(p["slug"])
        if len(out) >= limit:
            break
    return out
