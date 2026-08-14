#!/usr/bin/env python3
"""Generate the PalletHaven static wholesale website."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IMG = {
    "hero": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1600&q=80",
    "electronics": "https://images.unsplash.com/photo-1498049794561-7780e7231661?auto=format&fit=crop&w=900&q=80",
    "monitor": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=900&q=80",
    "keyboard": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?auto=format&fit=crop&w=900&q=80",
    "box": "https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?auto=format&fit=crop&w=900&q=80",
    "gaylord": "https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=900&q=80",
    "sneakers": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80",
    "shoes": "https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=900&q=80",
    "clothing": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=900&q=80",
    "fashion": "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=900&q=80",
    "kitchen": "https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&w=900&q=80",
    "coffee": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?auto=format&fit=crop&w=900&q=80",
    "tools": "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=900&q=80",
    "drill": "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?auto=format&fit=crop&w=900&q=80",
    "perfume": "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=900&q=80",
    "beauty": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=900&q=80",
    "phone": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=900&q=80",
    "watch": "https://images.unsplash.com/photo-1434493789847-2f02dc6ce246?auto=format&fit=crop&w=900&q=80",
    "toys": "https://images.unsplash.com/photo-1558060370-d644479cb6f7?auto=format&fit=crop&w=900&q=80",
    "blocks": "https://images.unsplash.com/photo-1587654780291-39c9404d73a7?auto=format&fit=crop&w=900&q=80",
    "cards": "https://images.unsplash.com/photo-1606503153255-059d8f0d0d0a?auto=format&fit=crop&w=900&q=80",
    "ac": "https://images.unsplash.com/photo-1631545806608-5c505ba57b56?auto=format&fit=crop&w=900&q=80",
    "fridge": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=900&q=80",
    "winter": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=900&q=80",
    "bags": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=900&q=80",
    "tv": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=900&q=80",
    "console": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=900&q=80",
}

CATEGORIES = [
    {"slug": "elektronica", "name": "Elektronica pallets", "image": IMG["electronics"],
     "blurb": "Retour- en overstocklots met laptops, audio, monitors en accessoires. Manifest per artikel."},
    {"slug": "high-count", "name": "High Count FC pallets", "image": IMG["gaylord"],
     "blurb": "Hoge gaylord-stapels gemengde fulfillment-retouren. Geen itemmanifest, lagere stukprijs."},
    {"slug": "sneakers", "name": "Sneaker pallets", "image": IMG["sneakers"],
     "blurb": "Sport- en lifestyle schoeisel met merk, model, kleurweg en maatreks in het manifest."},
    {"slug": "kleding", "name": "Kleding en mode", "image": IMG["clothing"],
     "blurb": "Merkkleding in nieuwe of tagged staat. Partijen van 250 stuks tot volle pallets."},
    {"slug": "keuken", "name": "Huishoudapparaten", "image": IMG["kitchen"],
     "blurb": "Koffiemachines, mixers, stofzuigers en airfryers. Conditieklasse per toestel."},
    {"slug": "gereedschap", "name": "Gereedschap pallets", "image": IMG["tools"],
     "blurb": "Accu- en handgereedschap voor wederverkoop via marktplaatsen en bouwgroothandel."},
    {"slug": "parfum", "name": "Parfum en cosmetica", "image": IMG["perfume"],
     "blurb": "Geur, huid- en haarverzorging in verzegelde of testerstaat. Volledige SKU-lijst."},
    {"slug": "iphone", "name": "Smartphone pallets", "image": IMG["phone"],
     "blurb": "iPhone- en Android-lots met model, opslag, kleur en batterijstatus vóór aankoop."},
    {"slug": "speelgoed", "name": "Speelgoed en collectibles", "image": IMG["toys"],
     "blurb": "Bouwsets, kaarten en seizoensspeelgoed. Geschikt voor webshops en kermissen."},
    {"slug": "mystery-box", "name": "Mystery box pallets", "image": IMG["box"],
     "blurb": "Gemengde retourdozen. Inhoud varieert; conditie van nieuw tot salvage."},
    {"slug": "airco", "name": "Airco en HVAC", "image": IMG["ac"],
     "blurb": "Draagbare en split-units uit overstock en retourprogramma's."},
    {"slug": "winterschoenen", "name": "Winterschoenen", "image": IMG["winter"],
     "blurb": "Laarzen en gevoerde schoenen voor het najaar. Maatreks in het manifest."},
]

CAT_MAP = {c["slug"]: c for c in CATEGORIES}

PRODUCTS = [
    {"slug": "elektronica-retourdoos-24", "name": "Retourdoos elektronica – 24 stuks – MSRP €4.650",
     "category": "elektronica", "price": 1322.00, "msrp": 4650, "items": 24, "condition": "Retour / gemengd",
     "badge": "Manifest", "image": IMG["electronics"],
     "short": "Geteste en ongeteste consumentenelektronica in een compacte doos. Volledig artikelmanifest.",
     "body": "Deze doos is bedoeld voor verkopers die snel willen listen op eBay.de of Bol. Elk artikel staat in het manifest met merk, model en conditieklasse. Reken op een mix van audio, randapparatuur en kleine IT-accessoires."},
    {"slug": "monitor-salvage-19", "name": "Salvage monitorpallet – 19 stuks – MSRP €6.300",
     "category": "elektronica", "price": 535.03, "msrp": 6300, "items": 19, "condition": "Salvage",
     "badge": "Salvage", "image": IMG["monitor"],
     "short": "Schermen met cosmetische of functionele schade. Alleen voor reparatie of onderdelen.",
     "body": "Niet geschikt als eerste aankoop. De lotomschrijving vermeldt schermmaat en merk waar bekend. Kopers met een reparatielijn halen hier de hoogste restwaarde uit."},
    {"slug": "toetsenborden-defect-15", "name": "Defecte toetsenborden – 15 stuks – MSRP €2.204",
     "category": "elektronica", "price": 311.39, "msrp": 2204, "items": 15, "condition": "Salvage",
     "badge": "Salvage", "image": IMG["keyboard"],
     "short": "Kleine salvage-box voor onderdelen of refurbishment.",
     "body": "Vijftien gaming- en kantoortoetsenborden met uiteenlopende gebreken. Manifest vermeldt visuele staat. Verkoop as-is of strip voor switches en behuizingen."},
    {"slug": "elektronica-pallet-43", "name": "Elektronica retourpallet – 43 stuks – MSRP €10.625",
     "category": "elektronica", "price": 1890.00, "msrp": 10625, "items": 43, "condition": "Retour",
     "badge": "Manifest", "image": IMG["electronics"],
     "short": "Middelgroot elektronicalot met ASIN-lijst vóór betaling.",
     "body": "Mix van headphones, speakers, webcams en smart-home items. Conditie loopt van nieuw-in-doos tot gebruikte retour. Uitvalpercentage staat in de lotnotitie."},
    {"slug": "high-count-12", "name": "High Count Gaylord #12",
     "category": "high-count", "price": 3000.00, "msrp": None, "items": None, "condition": "Gemengd / as-is",
     "badge": "Geen manifest", "image": IMG["gaylord"],
     "short": "Hoge gaylord van fulfillment-retouren. Geen itemlijst, vaste prijs.",
     "body": "Stapel van circa 1,8 tot 2,1 meter. Categorieën kunnen elektronica, speelgoed, textiel en huishoud zijn. Alleen voor ervaren sorteerders. Verkoop is definitief."},
    {"slug": "high-count-18", "name": "High Count Gaylord #18",
     "category": "high-count", "price": 1980.00, "msrp": None, "items": None, "condition": "Gemengd / as-is",
     "badge": "Geen manifest", "image": IMG["gaylord"],
     "short": "Tweede gaylord in dezelfde reeks, andere mix, zelfde voorwaarden.",
     "body": "Geen veiling en geen bieden. Beschikbaar zolang de voorraad strekt. Vracht wordt na adresbevestiging berekend."},
    {"slug": "high-count-21", "name": "High Count Gaylord #21",
     "category": "high-count", "price": 1171.97, "msrp": None, "items": None, "condition": "Gemengd / as-is",
     "badge": "Geen manifest", "image": IMG["box"],
     "short": "Compactere high-count voor wie volume wil testen zonder truckload.",
     "body": "Lagere instapprijs dan de 3.000-euro gaylords. Nog steeds zonder artikelmanifest. Niet aanbevolen voor beginners."},
    {"slug": "high-count-27", "name": "High Count Gaylord #27",
     "category": "high-count", "price": 2320.00, "msrp": None, "items": None, "condition": "Gemengd / as-is",
     "badge": "Geen manifest", "image": IMG["gaylord"],
     "short": "Standaard FC-hoogte, gemengde merchandise, directe verzending.",
     "body": "Geschikt voor veilingoperators en export. Verwacht een breed conditiebereik van nieuw tot onverkoopbaar."},
    {"slug": "sneaker-mixed-120", "name": "Gemengde sneakerpallet – 120 paar",
     "category": "sneakers", "price": 2140.00, "msrp": 9600, "items": 120, "condition": "Nieuw / overstock",
     "badge": "Manifest", "image": IMG["sneakers"],
     "short": "Atletisch en lifestyle schoeisel met maat- en kleuroverzicht.",
     "body": "Merken wisselen per lot. Het manifest noemt modelnamen en EU-maten. Populaire exitkanalen: Vinted, eBay.de en fysieke outlets."},
    {"slug": "sneaker-premium-80", "name": "Premium lifestyle sneakers – 80 paar",
     "category": "sneakers", "price": 2680.00, "msrp": 11200, "items": 80, "condition": "Nieuw in doos",
     "badge": "Nieuw", "image": IMG["shoes"],
     "short": "Hogere retailwaarde per paar, volledige doospresentatie.",
     "body": "Kleinere teller, hogere stukprijs. Bedoeld voor boutiques en sneakerresellers die liever minder volume en schonere lots hebben."},
    {"slug": "hardloop-overstock-96", "name": "Hardloopschoenen overstock – 96 paar",
     "category": "sneakers", "price": 1750.00, "msrp": 7680, "items": 96, "condition": "Nieuw",
     "badge": "Overstock", "image": IMG["sneakers"],
     "short": "Seizoensoverstock uit Europese distributie.",
     "body": "Vooral neutrale kleuren en middensegment. Maatreks loopt van 38 tot 46, details in het Excel-manifest."},
    {"slug": "kleding-merk-250-a", "name": "Merkkleding pallet #3 – 250 stuks",
     "category": "kleding", "price": 1592.47, "msrp": 8750, "items": 250, "condition": "Nieuw met tags",
     "badge": "250 stuks", "image": IMG["clothing"],
     "short": "Dames- en herenmix, tagged, klaar voor rek of online listing.",
     "body": "Geen replica's. Maattabel en merksplit staan in het manifest. Geschikt voor weekmarkten en outletshops."},
    {"slug": "kleding-merk-250-b", "name": "Merkkleding pallet #4 – 250 stuks",
     "category": "kleding", "price": 1211.00, "msrp": 7200, "items": 250, "condition": "Nieuw met tags",
     "badge": "250 stuks", "image": IMG["fashion"],
     "short": "Tweede kledinglot uit dezelfde reeks, andere merkmix.",
     "body": "Lagere instapprijs door meer basics. Controleer het seizoen in de lotomschrijving voordat je bestelt."},
    {"slug": "kleding-merk-250-c", "name": "Merkkleding pallet #7 – 250 stuks",
     "category": "kleding", "price": 1242.75, "msrp": 6900, "items": 250, "condition": "Nieuw / overstock",
     "badge": "250 stuks", "image": IMG["clothing"],
     "short": "Casual en sportkleding, tagged of in polybag.",
     "body": "Goede starter voor Vinted-verkopers die volume willen zonder truckload. Retouren na verzending worden niet geaccepteerd."},
    {"slug": "kleding-warehouse-400", "name": "Warehouse modepallet – 400 stuks",
     "category": "kleding", "price": 1890.00, "msrp": 11000, "items": 400, "condition": "Nieuw / mixed",
     "badge": "Volume", "image": IMG["fashion"],
     "short": "Hoger volume voor distributeurs die splitsen naar lokale winkels.",
     "body": "Bevat meerdere merklagen. Vraag het Excel-bestand aan vóór betaling via sales@pallethaven.nl."},
    {"slug": "keuken-mix-36", "name": "Keukenapparatuur mix – 36 stuks",
     "category": "keuken", "price": 1480.00, "msrp": 7200, "items": 36, "condition": "Nieuw / open box",
     "badge": "Manifest", "image": IMG["kitchen"],
     "short": "Airfryers, mixers en koffieapparaten met modelnummers in het manifest.",
     "body": "Populair bij Facebook Marketplace-verkopers. Controleer voltage (230V) in de specificaties; alle lots voor de EU-markt zijn 230V tenzij anders vermeld."},
    {"slug": "stofzuiger-overstock-20", "name": "Stofzuiger overstock – 20 stuks",
     "category": "keuken", "price": 980.00, "msrp": 5400, "items": 20, "condition": "Nieuw verzegeld",
     "badge": "Nieuw", "image": IMG["kitchen"],
     "short": "Steel- en cilinderstofzuigers, fabrieksverzegeld.",
     "body": "Beperkte merkmix, hoge herkenning. Accessoires volgens doosinhoud; ontbrekende onderdelen worden in het manifest gemeld."},
    {"slug": "koffie-pallet-28", "name": "Koffiemachine pallet – 28 stuks",
     "category": "keuken", "price": 1625.00, "msrp": 8900, "items": 28, "condition": "Nieuw / retour",
     "badge": "Manifest", "image": IMG["coffee"],
     "short": "Volautomaten en capsuleapparaten, conditie per serienummer.",
     "body": "Open-box toestellen zijn visueel gecontroleerd. Functionele garanties van de fabrikant kunnen vervallen bij liquidatievoorraad."},
    {"slug": "gereedschap-accu-mix", "name": "Accugereedschap mixpallet",
     "category": "gereedschap", "price": 1540.00, "msrp": 6800, "items": 42, "condition": "Nieuw / overstock",
     "badge": "Manifest", "image": IMG["tools"],
     "short": "Boormachines, slijpers en combosets. Accu's vermeld waar aanwezig.",
     "body": "Niet alle sets bevatten accu en lader. Het manifest maakt dat per regel zichtbaar zodat je je inkoopprijs per werkende kit kunt rekenen."},
    {"slug": "handgereedschap-bulk", "name": "Handgereedschap bulkpallet",
     "category": "gereedschap", "price": 890.00, "msrp": 3100, "items": 180, "condition": "Nieuw",
     "badge": "Bulk", "image": IMG["drill"],
     "short": "Tangen, sleutels, bitsets en opbergkoffers.",
     "body": "Lage stukprijs, breed assortiment. Geschikt voor bouwmarkten en marktkramen. Geen elektrische apparaten in dit lot."},
    {"slug": "job-site-combo", "name": "Jobsite combo – 30 kits",
     "category": "gereedschap", "price": 2110.00, "msrp": 9400, "items": 30, "condition": "Nieuw in doos",
     "badge": "Nieuw", "image": IMG["tools"],
     "short": "Combopacks voor wederverkoop aan ZZP'ers en webshops.",
     "body": "Elke kit is als één SKU te listen. Voltage en accuplatform staan in het manifest."},
    {"slug": "parfum-100", "name": "Parfumpallet – 100 stuks",
     "category": "parfum", "price": 1280.00, "msrp": 6200, "items": 100, "condition": "Nieuw verzegeld",
     "badge": "Nieuw", "image": IMG["perfume"],
     "short": "Designer- en masstige geuren, verzegelde flacons.",
     "body": "Geen testers in dit lot. Batchcodes waar beschikbaar. Parallelimport mogelijk; controleer lokale etikettering voor jouw verkoopkanaal."},
    {"slug": "beauty-mix-180", "name": "Beauty mixpallet – 180 stuks",
     "category": "parfum", "price": 960.00, "msrp": 4100, "items": 180, "condition": "Nieuw",
     "badge": "Mix", "image": IMG["beauty"],
     "short": "Huid, haar en make-up. THT-data in het spreadsheet.",
     "body": "Let op houdbaarheidsdata. Lots met minder dan zes maanden THT worden als zodanig gemarkeerd."},
    {"slug": "iphone-grade-a-12", "name": "Smartphone Grade A – 12 stuks",
     "category": "iphone", "price": 3240.00, "msrp": 9600, "items": 12, "condition": "Grade A refurbished",
     "badge": "Grade A", "image": IMG["phone"],
     "short": "Geteste toestellen met batterijgezondheid in het manifest.",
     "body": "IMEI-lijst volgt na reservering. Cosmetisch hoog, functioneel getest. Niet nieuw verzegeld tenzij expliciet vermeld."},
    {"slug": "iphone-nieuw-8", "name": "Nieuwe smartphones – 8 stuks",
     "category": "iphone", "price": 4120.00, "msrp": 10300, "items": 8, "condition": "Nieuw verzegeld",
     "badge": "Nieuw", "image": IMG["phone"],
     "short": "Fabrieksverzegelde retaildozen, EU-stekker.",
     "body": "Beperkte voorraad. Model en opslag per seriële regel. Identiteitsverificatie kan worden gevraagd bij high-value lots."},
    {"slug": "wearables-24", "name": "Wearables en watches – 24 stuks",
     "category": "iphone", "price": 1180.00, "msrp": 4800, "items": 24, "condition": "Nieuw / retour",
     "badge": "Manifest", "image": IMG["watch"],
     "short": "Smartwatches en bands, mix van nieuw en open box.",
     "body": "Bandjesmaten en kastmaten staan in het bestand. Geschikt als add-on bij telefoonverkopen."},
    {"slug": "bouwsets-mix", "name": "Bouwsets mixpallet",
     "category": "speelgoed", "price": 1350.00, "msrp": 5200, "items": 40, "condition": "Nieuw verzegeld",
     "badge": "Nieuw", "image": IMG["blocks"],
     "short": "Grote bouwdozen, sealed, met setnummers in het manifest.",
     "body": "Hoge herkenning, relatief eenvoudig te listen. Controleer of sets retired zijn; dat staat in de kolom status."},
    {"slug": "collectible-cards-6", "name": "Collectible card case – 6 displays",
     "category": "speelgoed", "price": 890.00, "msrp": 2400, "items": 6, "condition": "Nieuw",
     "badge": "Sealed", "image": IMG["cards"],
     "short": "Sealed displays voor kaartwinkels en online resellers.",
     "body": "Niet geopend. Foto's van seal en batch waar beschikbaar. Geen pull-garantie."},
    {"slug": "speelgoed-algemeen-200", "name": "Algemeen speelgoed – 200 stuks",
     "category": "speelgoed", "price": 760.00, "msrp": 3800, "items": 200, "condition": "Nieuw / overstock",
     "badge": "Beginners", "image": IMG["toys"],
     "short": "Toegankelijk instaplot voor nieuwe wederverkopers.",
     "body": "Lage complexiteit, brede doelgroep. Aanbevolen als eerste pallet voordat je naar high-count of salvage gaat."},
    {"slug": "mystery-electronics", "name": "Mystery box elektronica – pallet",
     "category": "mystery-box", "price": 640.00, "msrp": None, "items": None, "condition": "As-is",
     "badge": "As-is", "image": IMG["box"],
     "short": "Gemengde elektronica-retouren zonder volledige SKU-garantie.",
     "body": "Er is een categorieraming, geen artikel-voor-artikel lijst. Koop alleen als je as-is accepteert."},
    {"slug": "mystery-general", "name": "Mystery box algemeen – pallet",
     "category": "mystery-box", "price": 520.00, "msrp": None, "items": None, "condition": "As-is",
     "badge": "As-is", "image": IMG["box"],
     "short": "Huishouden, speelgoed en accessoires in één stapel.",
     "body": "Goedkoop instappen, hoge sorteertijd. Niet hetzelfde als een manifestlot."},
    {"slug": "airco-retour-40", "name": "Airco retouren – 40 stuks (3 pallets)",
     "category": "airco", "price": 1203.11, "msrp": 12000, "items": 40, "condition": "Retour",
     "badge": "3 pallets", "image": IMG["ac"],
     "short": "Draagbare units uit een retourprogramma. 230V.",
     "body": "Sommige units missen een slang of afstandsbediening. Dat staat per regel. Vracht is hoger door volume; vraag een offerte."},
    {"slug": "airco-overstock-12", "name": "Airco overstock – 12 stuks",
     "category": "airco", "price": 1680.00, "msrp": 5400, "items": 12, "condition": "Nieuw",
     "badge": "Nieuw", "image": IMG["ac"],
     "short": "Nieuwe draagbare airco's, seizoensclearance.",
     "body": "Schonere lot dan retouren. Beperkt tot de zomerpiek; daarna langzamere exit."},
    {"slug": "winter-boots-1", "name": "Winterlaarzen pallet #1",
     "category": "winterschoenen", "price": 900.00, "msrp": 4200, "items": 72, "condition": "Nieuw",
     "badge": "Seizoen", "image": IMG["winter"],
     "short": "Gevoerde laarzen, dames en heren, maatoverzicht in Excel.",
     "body": "Seizoensgevoelig. Bestel ruim voor november als je winterpiek wilt meepakken."},
    {"slug": "winter-boots-2", "name": "Winterschoenen pallet #2",
     "category": "winterschoenen", "price": 800.00, "msrp": 3600, "items": 60, "condition": "Nieuw / overstock",
     "badge": "Seizoen", "image": IMG["shoes"],
     "short": "Lagere teller, gemengde stijlen.",
     "body": "Bevat enkelhoge en kuit-hoge modellen. Waterdichtheid per model in het manifest."},
    {"slug": "handtassen-mix", "name": "Dameshandtassen mix – 80 stuks",
     "category": "kleding", "price": 450.00, "msrp": 2400, "items": 80, "condition": "Nieuw",
     "badge": "Instap", "image": IMG["bags"],
     "short": "Toegankelijk lot voor nieuwe modeverkopers.",
     "body": "Geen replica-lederclaims. Materialen staan als PU, textiel of leer volgens het bestand."},
    {"slug": "tv-salvage-10", "name": "TV salvage – 10 stuks",
     "category": "elektronica", "price": 740.00, "msrp": 5800, "items": 10, "condition": "Salvage",
     "badge": "Salvage", "image": IMG["tv"],
     "short": "Schermen met schade. Alleen voor technici.",
     "body": "Geen beeldgarantie. Serienummers en inch-maten staan in het manifest."},
    {"slug": "console-accessoires", "name": "Console en accessoires – 35 stuks",
     "category": "elektronica", "price": 1560.00, "msrp": 6100, "items": 35, "condition": "Nieuw / retour",
     "badge": "Manifest", "image": IMG["console"],
     "short": "Controllers, headsets en gesealde accessoires.",
     "body": "Geen garantie dat consoles zelf in het lot zitten. Lees de SKU-lijst voordat je uitgaat van hardware."},
]

NAV = [
    ("index.html", "Home"),
    ("winkel.html", "Winkel"),
    ("contact.html", "Neem contact met ons op"),
    ("over-ons.html", "Over ons"),
    ("privacybeleid.html", "Privacybeleid"),
    ("algemene-voorwaarden.html", "Algemene voorwaarden"),
    ("leveringsvoorwaarden.html", "Leveringsvoorwaarden"),
    ("disclaimer.html", "Juridische disclaimer"),
]


def euro(n):
    return f"€ {n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def header(prefix: str, active: str) -> str:
    links = "".join(
        f'<a href="{prefix}{href}" class="{"active" if active == href else ""}">{label}</a>'
        for href, label in NAV
    )
    mobile = "".join(f'<a href="{prefix}{href}">{label}</a>' for href, label in NAV)
    return f"""
<header class="site-header">
  <div class="topbar"><div class="container">Wij leveren in heel Europa, waaronder België, Nederland, Frankrijk, Italië, Spanje, Portugal, het Verenigd Koninkrijk, Polen, Zwitserland en Oostenrijk. Gratis verzending in Nederland vanaf € 3.000.</div></div>
  <div class="container header-main">
    <button class="menu-btn" data-menu aria-label="Menu">☰</button>
    <a class="logo" href="{prefix}index.html"><img src="{prefix}assets/logo.svg" alt="PalletHaven"></a>
    <form class="search-wrap" data-search>
      <label class="sr-only" for="q">Zoeken</label>
      <input id="q" name="s" placeholder="Zoeken…">
      <button type="submit" aria-label="Zoeken">⌕</button>
    </form>
    <div class="header-actions">
      <a class="hide-sm" href="{prefix}account.html">Login</a>
      <a class="cart-link" href="{prefix}winkelwagen.html">
        <span class="cart-meta hide-sm">Winkelwagen / <span data-cart-total>€ 0,00</span></span>
        <span class="bag">👜<b data-cart-count>0</b></span>
        <div class="mini-cart" data-mini-cart></div>
      </a>
    </div>
  </div>
  <nav class="nav-bar"><div class="container">{links}</div></nav>
  <div class="mobile-menu" data-mobile>{mobile}<a href="{prefix}account.html">Login</a></div>
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
      <a href="mailto:sales@pallethaven.nl">sales@pallethaven.nl</a>
      <a href="https://wa.me/31201234567">WhatsApp +31 20 123 4567</a>
      <p>Ma–vr 09:00–17:00 CET<br>Geen walk-in, geen afhaling behalve truckloads op afspraak.</p>
    </div>
  </div>
  <div class="copy">© 2026 PalletHaven. Demo-website voor groothandel liquidatiepallets.</div>
</footer>
<div class="modal" id="quick-modal">
  <div class="modal-box">
    <img alt="">
    <div class="modal-body">
      <button class="close-x" data-close>×</button>
      <h3></h3>
      <p class="price" data-q-price></p>
      <p data-q-desc></p>
      <p><button class="btn btn-dark" data-q-add data-add="" data-label="In winkelwagen">In winkelwagen</button></p>
      <p><a data-q-link>Bekijk product</a></p>
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
<script>const ROOT = "{prefix}";</script>
<script src="{prefix}js/data.js"></script>
<script src="{prefix}js/app.js"></script>
{extra_js}
</body>
</html>
"""


def cards(slugs):
    items = [p for p in PRODUCTS if p["slug"] in slugs]
    html = ['<div class="product-grid">']
    for p in items:
        html.append(f"""
        <article class="product-card">
          {'<span class="badge">' + p["badge"] + "</span>" if p.get("badge") else ""}
          <div class="thumb">
            <a href="product/{p["slug"]}.html"><img src="{p["image"]}" alt="{p["name"]}"></a>
            <button class="quick" data-quick="{p["slug"]}">Snel bekijken</button>
          </div>
          <div class="info">
            <h3><a href="product/{p["slug"]}.html">{p["name"]}</a></h3>
            <div class="price">{'<span class="msrp">' + euro(p["msrp"]) + "</span>" if p.get("msrp") else ""}{euro(p["price"])}</div>
          </div>
        </article>""")
    html.append("</div>")
    return "\n".join(html)


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
    <h1>Wholesale liquidatiepallets voor Nederland en Europa — merkproducten, volledig manifest, directe levering</h1>
    <p>Koop groothandelspallets in elektronica, sneakers, kleding, parfum, gereedschap en huishoudapparaten. Op elk standaardlot ontvang je het artikelmanifest vóór je betaalt, zodat je je marge kunt rekenen. Vragen vooraf: <a href="mailto:sales@pallethaven.nl">sales@pallethaven.nl</a></p>
    <div class="hero-actions">
      <a class="btn btn-light" href="winkel.html">Winkel alle pallets</a>
      <a class="btn btn-outline" href="contact.html">Vraag een offerte aan</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container features">
    <article class="feature"><div class="icon">🚚</div><h3>Prioritaire verzending</h3><p>LTL-vracht binnen Nederland en naar de rest van Europa met tracking.</p></article>
    <article class="feature"><div class="icon">↺</div><h3>Duidelijke voorwaarden</h3><p>Manifestlots kun je beoordelen vóór betaling. Salvage en high-count gaan as-is.</p></article>
    <article class="feature"><div class="icon">🔒</div><h3>Beveiligde betalingen</h3><p>Bankoverschrijving of Revolut. Geen betaling voordat het lot is bevestigd.</p></article>
    <article class="feature"><div class="icon">✓</div><h3>Geverifieerde sourcing</h3><p>Overstock, surplus en retourstromen via retail- en distributiekanalen.</p></article>
    <article class="feature"><div class="icon">📋</div><h3>Manifest vóór aankoop</h3><p>Merk, model, conditie en geschatte MSRP per regel waar van toepassing.</p></article>
    <article class="feature"><div class="icon">🏢</div><h3>B2B en export</h3><p>Factuur, paklijst en exportdocumenten voor EU-kopers op aanvraag.</p></article>
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Wat is PalletHaven?</h2>
    <p>PalletHaven is een Nederlands groothandelsplatform voor liquidatiepallets. We bevoorraden wederverkopers, Amazon- en eBay-verkopers, boutiques, marktondernemers, B2B-distributeurs en exporteurs in Nederland, Duitsland, België en de rest van Europa.</p>
    <p>We kopen wekelijks overstock, seizoensclearance en consumentenretouren in bij Noord-Amerikaanse en Europese retailnetwerken. Door rechtstreeks in te kopen vallen tussenlagen weg. Jij houdt meer marge over.</p>
    <p>Op elk manifestlot zie je merk, model, conditieklasse en waar mogelijk de geschatte retailwaarde vóór je vastlegt. Geen blinde dozen als standaard. High-count gaylords zonder lijst staan nadrukkelijk zo gelabeld.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Onze productcategorieën</h2>
    <p class="lead">Kies een categorie die past bij jouw verkoopkanaal. Elke pagina beschrijft lotformaat, conditie en voor wie het bedoeld is.</p>
    <div class="cat-grid">{cats}</div>
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Hoe PalletHaven werkt</h2>
    <div class="steps">
      <article class="step"><b>1</b><h3>Kies een categorie</h3><p>Bekijk merkmix, conditie en verwachte MSRP op de categoriepagina.</p></article>
      <article class="step"><b>2</b><h3>Vraag het manifest</h3><p>Mail sales@pallethaven.nl. Je krijgt de artikelregels vóór betaling.</p></article>
      <article class="step"><b>3</b><h3>Reken je marge</h3><p>Vergelijk met recente verkopen op eBay.de, Amazon.de of Back Market minus vracht.</p></article>
      <article class="step"><b>4</b><h3>Bestel online</h3><p>Geen magazijnbezoek. Truckloads kunnen op afspraak worden geladen.</p></article>
      <article class="step"><b>5</b><h3>Ontvang en verkoop</h3><p>Professioneel gewikkeld, met tracking, klaar om te testen en te listen.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Onze bestverkochte pallets</h2>
    {cards(["keuken-mix-36","bouwsets-mix","beauty-mix-180","monitor-salvage-19","mystery-electronics","gereedschap-accu-mix","iphone-grade-a-12","sneaker-mixed-120"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Waarom wederverkopers PalletHaven kiezen</h2>
    <p>Omdat je op standaardlots de samenstelling kent vóór je betaalt. De meeste Europese brokers tonen pas na aankoop wat erin zat. Bij ons is het manifest de default, niet de uitzondering.</p>
    <p>Voorraad komt uit overstock, surplus en retourkanalen. Geen namaak en geen vage huismerken om pallets te vullen. Wat op papier staat, is wat eruit komt, binnen de gemelde conditieklasse.</p>
    <p>Nieuw verzegeld betekent nieuw verzegeld. Getest werkend is functioneel gecontroleerd. Retour vermeldt een realistisch uitvalpercentage. Salvage is salvage.</p>
    <p>We verzenden naar Nederland (3–7 werkdagen) en de rest van Europa (5–14 werkdagen). Invoerrechten en btw buiten onze factuur zijn voor de koper. Volume en truckloads via sales@pallethaven.nl.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met fulfillment-opruiming</h2>
    {cards(["high-count-12","high-count-18","high-count-21","high-count-27"])}
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Voor wie is PalletHaven?</h2>
    <div class="audience">
      <article><h3>Marktplaatsverkopers</h3><p>eBay.de, Amazon.de FBA en Bol-verkopers die merken met identifiers nodig hebben om vooraf te listen.</p></article>
      <article><h3>Boutiques en outlets</h3><p>Winkels in NL en DE die merkvoorraad onder adviesprijs willen zonder standaard groothandelsminimums.</p></article>
      <article><h3>Markten en pop-ups</h3><p>Ondernemers die volume zoeken tegen een lage stukprijs voor face-to-face verkoop.</p></article>
      <article><h3>Distributeurs en export</h3><p>Partijen die splitsen naar lokale retailers of verder exporteren binnen de EU.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met collectibles en speelgoed</h2>
    {cards(["bouwsets-mix","collectible-cards-6","speelgoed-algemeen-200"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Klaar om te beginnen?</h2>
    <p>PalletHaven is online. Geen walk-in en geen afhaling op standaardpallets. Kies een categorie, mail om het manifest, toets je exitprijzen en plaats de order. Voor truckloads overleggen we vracht en laaddatum eerst.</p>
    <p style="text-align:center"><a class="btn btn-dark" href="contact.html">Neem contact op</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met gereedschap</h2>
    {cards(["gereedschap-accu-mix","handgereedschap-bulk","job-site-combo"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Verzendinformatie</h2>
    <p>Nederlandse orders gaan via verzekerde LTL-palletvracht, meestal 3 tot 7 werkdagen na bevestiging, naar alle provincies.</p>
    <p>Europese leveringen omvatten Duitsland, België, Frankrijk, het Verenigd Koninkrijk, Spanje, Italië, Polen, Oostenrijk, Denemarken, Zweden en overige EU-bestemmingen. Reken op 5 tot 14 werkdagen. Douane, invoer en lokale btw zijn voor de koper. Documenten leveren we mee.</p>
    <p>Geen lokale ophaling, behalve container- en truckloadorders na afspraak.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met sneakers</h2>
    {cards(["sneaker-mixed-120","sneaker-premium-80","hardloop-overstock-96"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Wat is een liquidatiepallet?</h2>
    <p>Een liquidatiepallet is een bundel overstock of retourvoorraad die een retailer of fabrikant doorzet naar de groothandel. Wederverkopers kopen die bundel onder retail in en verkopen per stuk via webshops, markten of fysieke winkels.</p>
    <p>Het voordeel is toegang tot merken zonder volle groothandelscatalogus. Het risico is conditievariatie. Daarom leveren wij op standaardlots een regel-voor-regel overzicht. High-count zonder lijst is een ander product, met een andere prijs en een andere koper.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met gemengde kleding</h2>
    {cards(["kleding-merk-250-a","kleding-merk-250-b","kleding-merk-250-c","handtassen-mix"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Pallet flipping: bijverdienste of onderneming?</h2>
    <p>Veel kopers starten in de avonduren met één of twee manifestlots. Dat beperkt het risico en leert je sorteren, fotograferen en listen. Fulltime draaien vraagt opslag, kasstroom en een vast inkoopplan. PalletHaven ondersteunt beide: kleine dozen voor de eerste test en truckloads wanneer je proces staat.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets met huishoudelijke apparaten</h2>
    {cards(["keuken-mix-36","stofzuiger-overstock-20","koffie-pallet-28"])}
  </div>
</section>

<section class="section alt">
  <div class="container prose">
    <h2>Is het kopen van liquidatiepallets de moeite waard?</h2>
    <p>Alleen als de input klopt. Reken verwachte verkoopprijs minus platformkosten, vracht, opslag en refurbishment. Als de leverancier geen manifest kan geven op een lot dat als manifest wordt verkocht, is dat een reden om te stoppen. Salvage en mystery boxes kunnen werken, maar alleen met ervaring en tijd om te sorteren.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Koop pallets vol mystery boxen</h2>
    {cards(["mystery-electronics","mystery-general"])}
  </div>
</section>

<section class="section alt">
  <div class="container">
    <h2 class="section-title">Getuigenissen</h2>
    <div class="reviews">
      <article class="review"><div class="stars">★★★★★</div><p>Pallet kwam overeen met het bestand, netjes gewikkeld, levering in Brabant zonder gedoe.</p><cite>Thomas de Vries — Eindhoven</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Elektronicalot was eerlijk geclassificeerd. Uitval lag binnen de opgegeven band. Opnieuw besteld.</p><cite>Lea Hoffmann — Düsseldorf</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Sneakers grotendeels nieuw in doos. Communicatie over vracht was duidelijk.</p><cite>Samir El Idrissi — Rotterdam</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>Beauty-pallet schoon en sealed. Fijne instap voor onze webshop.</p><cite>Nina Bakker — Utrecht</cite></article>
      <article class="review"><div class="stars">★★★★★</div><p>High-count is niks voor beginners, dat zeiden ze ook. Voor ons sorteerbedrijf past het.</p><cite>Marco Bianchi — Milaan</cite></article>
      <article class="review"><div class="stars">★★★★☆</div><p>Tracking klopte. Factuur en paklijst waren compleet voor onze boekhouding.</p><cite>Sophie Laurent — Lille</cite></article>
    </div>
  </div>
</section>

<section class="section">
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
      <h2>Veelgestelde vragen</h2>
      <details open><summary>Is PalletHaven een groothandel?</summary><p>Ja. We leveren aan wederverkopers, retailers, distributeurs en exporteurs. Consumentenafhaling is er niet.</p></details>
      <details><summary>Krijg ik een manifest vóór aankoop?</summary><p>Ja op elk lot dat als manifestlot staat. High-count en mystery boxes staan als geen-manifest.</p></details>
      <details><summary>Welke categorieën zijn er?</summary><p>Elektronica, sneakers, kleding, parfum, gereedschap, huishoud, smartphones, speelgoed, airco en high-count gaylords.</p></details>
      <details><summary>Verzenden jullie naar Duitsland en de rest van Europa?</summary><p>Ja. Douane, btw en invoer buiten de factuur zijn voor de koper.</p></details>
      <details><summary>Kan ik afhalen?</summary><p>Niet bij standaardpallets. Truckloads mogelijk op afspraak.</p></details>
      <details><summary>Wat is het minimum?</summary><p>Het kleinste lot in de winkel. Volumeafspraken via sales@pallethaven.nl.</p></details>
      <details><summary>Zijn retouren mogelijk?</summary><p>Verkoop is definitief na verzending, behalve bij een aantoonbare verzendfout of een lot dat materieel afwijkt van het bevestigde manifest.</p></details>
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
    js = "const CATEGORIES = " + json.dumps(data["CATEGORIES"], ensure_ascii=False, indent=2) + ";\n"
    js += "const PRODUCTS = " + json.dumps(data["PRODUCTS"], ensure_ascii=False, indent=2) + ";\n"
    write(ROOT / "js" / "data.js", js)

    write(ROOT / "index.html", page("Home", "", "index.html", homepage()))
    write(ROOT / "winkel.html", page("Winkel", "", "winkel.html", shop_page("Winkel", "Home / Winkel", intro="Alle beschikbare liquidatiepallets. Filter op categorie of zoek op trefwoord.")))

    for c in CATEGORIES:
        body = shop_page(
            c["name"],
            f'<a href="../index.html">Home</a> / <a href="../winkel.html">Winkel</a> / {c["name"]}',
            category=c["slug"],
            intro=c["blurb"],
        )
        write(ROOT / "categorie" / f"{c['slug']}.html", page(c["name"], "../", "winkel.html", body))

    for p in PRODUCTS:
        cat = CAT_MAP[p["category"]]
        body = f"""
<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="../index.html">Home</a> / <a href="../winkel.html">Winkel</a> / <a href="../categorie/{cat["slug"]}.html">{cat["name"]}</a></div>
</div></section>
<section class="section"><div class="container product-layout">
  <div class="gallery"><img src="{p["image"]}" alt="{p["name"]}"></div>
  <div>
    <h1>{p["name"]}</h1>
    <p class="price" style="font-size:1.6rem">{euro(p["price"])}</p>
    <p>{p["short"]}</p>
    <div class="meta-list">
      <div><span>Categorie</span><span>{cat["name"]}</span></div>
      <div><span>Conditie</span><span>{p["condition"]}</span></div>
      <div><span>Aantal stuks</span><span>{p["items"] if p["items"] else "Niet gespecificeerd"}</span></div>
      <div><span>Geschatte MSRP</span><span>{euro(p["msrp"]) if p.get("msrp") else "Onbekend / geen manifest"}</span></div>
      <div><span>Verzending</span><span>LTL-vracht, offerte na adres</span></div>
    </div>
    <div class="qty-row">
      <label>Aantal <input type="number" min="1" value="1" data-qty></label>
      <button class="btn btn-dark" data-add="{p["slug"]}" data-label="In winkelwagen">In winkelwagen</button>
    </div>
    <p class="form-note">Vraag het volledige manifest aan via sales@pallethaven.nl voordat je betaalt. High-count en mystery lots gaan as-is.</p>
  </div>
</div></section>
<section class="section alt"><div class="container prose">
  <h2>Omschrijving</h2>
  <p>{p["body"]}</p>
  <p>PalletHaven verkoopt aan professionele kopers. Door te bestellen bevestig je de lotvoorwaarden, inclusief conditieklasse en het wel of niet aanwezig zijn van een itemmanifest.</p>
</div></section>
"""
        write(ROOT / "product" / f"{p['slug']}.html", page(p["name"], "../", "winkel.html", body))

    write(ROOT / "contact.html", page("Neem contact met ons op", "", "contact.html", """
<section class="page-hero"><div class="container"><h1>Neem contact met ons op</h1><p>Stuur een bericht voordat je bestelt als je het manifest, de vracht of het lotformaat wilt checken.</p></div></section>
<section class="section"><div class="container contact-grid">
  <div>
    <h2>Stuur ons een bericht</h2>
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
      <dt>E-mail</dt><dd><a href="mailto:sales@pallethaven.nl">sales@pallethaven.nl</a></dd>
      <dt>WhatsApp</dt><dd><a href="https://wa.me/31201234567">+31 20 123 4567</a></dd>
    </dl>
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
  <p>Inzage, correctie, verwijdering, beperking en bezwaar via sales@pallethaven.nl. Klachten kunnen naar de Autoriteit Persoonsgegevens.</p>
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
  <p>Noteer zichtbare transportschade op de vrachtbrief en mail foto's binnen 24 uur naar sales@pallethaven.nl.</p>
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
<section class="page-hero"><div class="container"><h1>Winkelwagen</h1></div></section>
<section class="section"><div class="container">
  <div data-cart-table></div>
  <div data-cart-totals></div>
</div></section>
"""))

    write(ROOT / "afrekenen.html", page("Afrekenen", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>Afrekenen</h1><p>Na deze aanvraag ontvang je het manifest (waar van toepassing) en de betaalinstructie. Er wordt niet automatisch afgeschreven.</p></div></section>
<section class="section"><div class="container contact-grid">
  <form data-checkout>
    <h2>Factuur- en aflevergegevens</h2>
    <div class="row"><div><label>Bedrijfsnaam</label><input required></div><div><label>KvK-nummer</label><input></div></div>
    <div class="row"><div><label>Contactpersoon</label><input required></div><div><label>E-mail</label><input type="email" required></div></div>
    <label>Telefoon</label><input required>
    <label>Afleveradres</label><input required>
    <div class="row"><div><label>Postcode</label><input required></div><div><label>Plaats</label><input required></div></div>
    <label>Land</label>
    <select><option>Nederland</option><option>België</option><option>Duitsland</option><option>Frankrijk</option><option>Overig EU</option><option>Verenigd Koninkrijk</option></select>
    <label>Opmerking / gewenst lotmanifest</label><textarea></textarea>
    <p><button class="btn btn-dark" type="submit">Bestelling plaatsen</button></p>
  </form>
  <div>
    <h2>Jouw pallets</h2>
    <div class="totals" data-order-summary></div>
    <p class="form-note">Betaling via bankoverschrijving of Revolut ná bevestiging. High-count lots zonder manifest blijven as-is.</p>
  </div>
</div></section>
"""))

    write(ROOT / "account.html", page("Mijn account", "", "winkel.html", """
<section class="page-hero"><div class="container"><h1>Mijn account</h1></div></section>
<section class="section"><div class="container">
  <div data-account-panel></div>
  <div class="account-grid">
    <form data-login>
      <h2>Inloggen</h2>
      <label>E-mailadres</label><input name="email" type="email" required>
      <label>Wachtwoord</label><input type="password" required>
      <p><label><input type="checkbox"> Onthouden</label></p>
      <p><button class="btn btn-dark" type="submit">Inloggen</button></p>
    </form>
    <form data-register>
      <h2>Registreren</h2>
      <label>E-mailadres</label><input type="email" required>
      <p class="form-note">Er wordt een link om een wachtwoord in te stellen naar je e-mailadres verzonden. In deze demo kun je daarna direct inloggen.</p>
      <p>Je gegevens worden gebruikt zoals beschreven in het <a href="privacybeleid.html">privacybeleid</a>.</p>
      <p><button class="btn btn-dark" type="submit">Registreren</button></p>
      <div data-result></div>
    </form>
  </div>
</div></section>
"""))

    print(f"Wrote {len(PRODUCTS)} products and {len(CATEGORIES)} categories.")


if __name__ == "__main__":
    main()
