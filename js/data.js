const SITE = {
  name: "chrono24",
  listingCount: "670,418",
  countries: 132,
};

const CONTACT = {
  phone: "+1 913-278-5312",
  tel: "tel:+19132785312",
  email: "luxerywatchsales@gmail.com",
  whatsapp: "https://wa.me/19132785312",
};

const MENU_BRANDS_LEFT = [
  "Gauri", "Rolex", "Patek Philippe", "Breitling", "Cartier", "IWC",
  "Jaeger-LeCoultre", "Hublot", "Vacheron Constantin", "A. Lange & Söhne", "Breguet", "Hamilton", "Oris",
];
const MENU_BRANDS_RIGHT = [
  "Omega", "Audemars Piguet", "Tudor", "Panerai", "Seiko", "TAG Heuer",
  "Zenith", "Longines", "Richard Mille", "Ulysse Nardin", "NOMOS", "Sinn",
];

const MENU_CATEGORIES = [
  { name: "Men's Watches", slug: "mens" },
  { name: "Women's Watches", slug: "womens" },
  { name: "Pre-Owned Watches", slug: "preowned" },
  { name: "Mechanical Watches", slug: "mechanical" },
  { name: "Automatic Watches", slug: "automatic" },
  { name: "Vintage Watches", slug: "vintage" },
  { name: "Chronographs", slug: "chrono" },
  { name: "Diving Watches", slug: "dive" },
  { name: "Pilot's Watches", slug: "pilot" },
  { name: "Military Watches", slug: "military" },
  { name: "Swiss Watches", slug: "swiss" },
  { name: "Affordable Watches", slug: "affordable" },
  { name: "Bracelets and Straps", slug: "straps" },
  { name: "Parts and Accessories", slug: "parts" },
];

const BRANDS = [
  { name: "Gauri", count: 12500 },
  { name: "Rolex", count: 116723 },
  { name: "Omega", count: 96820 },
  { name: "Patek Philippe", count: 18240 },
  { name: "Audemars Piguet", count: 15410 },
  { name: "Breitling", count: 41210 },
  { name: "Cartier", count: 33880 },
  { name: "Tudor", count: 28760 },
  { name: "IWC", count: 22140 },
  { name: "Panerai", count: 19320 },
  { name: "Seiko", count: 54110 },
  { name: "TAG Heuer", count: 36440 },
  { name: "Jaeger-LeCoultre", count: 11280 },
  { name: "Hublot", count: 14890 },
  { name: "Longines", count: 22100 },
  { name: "Zenith", count: 7340 },
  { name: "Vacheron Constantin", count: 5120 },
  { name: "A. Lange & Söhne", count: 2180 },
  { name: "Breguet", count: 1640 },
  { name: "Hamilton", count: 8920 },
  { name: "Oris", count: 6540 },
  { name: "Richard Mille", count: 980 },
  { name: "Ulysse Nardin", count: 1420 },
  { name: "NOMOS", count: 4210 },
  { name: "Sinn", count: 3180 },
  { name: "Grand Seiko", count: 8760 },
  { name: "Tissot", count: 19840 },
];

const POPULAR_MODELS = [
  "Gauri Lotus", "Gauri Tikka", "Gauri Saffron", "Gauri Midnight",
  "Rolex Datejust", "Rolex Submariner", "Rolex Daytona", "Omega Speedmaster",
  "Audemars Piguet Royal Oak", "Rolex Day-Date", "Rolex GMT-Master II", "Patek Philippe Nautilus",
  "Omega Seamaster", "Breitling Navitimer", "Rolex Oyster Perpetual", "Patek Philippe Calatrava",
  "Cartier Santos", "Cartier Tank", "Tudor Black Bay", "IWC Pilot's Watch",
  "Panerai Luminor", "Gauri Heritage", "Gauri Temple", "Gauri Pearl",
  "Gauri Royale", "Hublot Big Bang", "Longines HydroConquest", "Grand Seiko Snowflake",
  "Zenith El Primero", "Vacheron Overseas", "Richard Mille RM 011", "Breguet Classique",
];

const CATEGORIES = [
  { name: "Men's Watches", slug: "mens", image: "assets/lifestyle/cat-mens.jpg" },
  { name: "Pre-Owned Watches", slug: "preowned", image: "assets/lifestyle/cat-preowned.jpg" },
  { name: "Pocket Watches", slug: "pocket", image: "assets/watches/watch-pocket.jpg" },
  { name: "Women's Watches", slug: "womens", image: "assets/lifestyle/cat-womens.jpg" },
  { name: "Automatic Watches", slug: "automatic", image: "assets/watches/watch-submariner.jpg" },
  { name: "Skeleton Watches", slug: "skeleton", image: "assets/watches/watch-skeleton.jpg" },
  { name: "Gold Watches", slug: "gold", image: "assets/watches/watch-gold.jpg" },
  { name: "Moon Phase Watches", slug: "moonphase", image: "assets/watches/watch-moonphase.jpg" },
];

const SELLERS = [
  { name: "Atlantic Timepieces", rating: 4.9, reviews: 1284, type: "Professional dealer", loc: "New York, United States" },
  { name: "Geneva Watch Co.", rating: 4.8, reviews: 892, type: "Professional dealer", loc: "Geneva, Switzerland" },
  { name: "Crown & Caliber Desk", rating: 4.7, reviews: 2104, type: "Professional dealer", loc: "Atlanta, United States" },
  { name: "Horology House", rating: 4.9, reviews: 640, type: "Professional dealer", loc: "London, United Kingdom" },
  { name: "Private seller", rating: 4.6, reviews: 18, type: "Private seller", loc: "Miami, United States" },
  { name: "Tokyo Time Vault", rating: 4.8, reviews: 431, type: "Professional dealer", loc: "Tokyo, Japan" },
  { name: "Dubai Watch Gallery", rating: 4.7, reviews: 305, type: "Professional dealer", loc: "Dubai, United Arab Emirates" },
  { name: "Paris Atelier", rating: 4.9, reviews: 277, type: "Professional dealer", loc: "Paris, France" },
];

const SEED = [
  { brand: "Rolex", model: "Submariner Date", ref: "116610LN", year: 2018, price: 11495, img: "watch-submariner.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Rolex", model: "Daytona", ref: "116500LN", year: 2021, price: 28450, img: "watch-daytona.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Rolex", model: "Datejust 36", ref: "126234", year: 2022, price: 9890, img: "watch-datejust.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel and gold, 36 mm", condition: "Used (Mint)" },
  { brand: "Rolex", model: "GMT-Master II", ref: "126710BLRO", year: 2020, price: 17850, img: "watch-gmt.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Rolex", model: "Day-Date 40", ref: "228238", year: 2019, price: 33900, img: "watch-daydate.jpg", cats: ["mens","gold","automatic"], movement: "Automatic", case: "Yellow gold, 40 mm", condition: "Used (Good)" },
  { brand: "Omega", model: "Speedmaster Professional", ref: "310.30.42.50.01.001", year: 2023, price: 6450, img: "watch-speedmaster.jpg", cats: ["mens","preowned"], movement: "Manual winding", case: "Steel, 42 mm", condition: "New" },
  { brand: "Omega", model: "Seamaster Diver 300M", ref: "210.30.42.20.03.001", year: 2021, price: 4890, img: "watch-seamaster.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "Used (Very good)" },
  { brand: "Audemars Piguet", model: "Royal Oak", ref: "15500ST", year: 2020, price: 42900, img: "watch-royal-oak.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Very good)" },
  { brand: "Patek Philippe", model: "Nautilus", ref: "5711/1A-010", year: 2018, price: 118000, img: "watch-nautilus.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Good)" },
  { brand: "Cartier", model: "Santos de Cartier", ref: "WSSA0018", year: 2022, price: 6790, img: "watch-santos.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 39.8 mm", condition: "Used (Mint)" },
  { brand: "Breitling", model: "Navitimer B01", ref: "AB0121211B1P1", year: 2019, price: 7250, img: "watch-navitimer.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 43 mm", condition: "Used (Very good)" },
  { brand: "Tudor", model: "Black Bay", ref: "M79230N", year: 2022, price: 3290, img: "watch-tudor.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Very good)" },
  { brand: "Panerai", model: "Luminor Marina", ref: "PAM01312", year: 2020, price: 5890, img: "watch-panerai.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 44 mm", condition: "Used (Good)" },
  { brand: "IWC", model: "Pilot's Watch Mark XVIII", ref: "IW327001", year: 2021, price: 3990, img: "watch-pilot.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Jaeger-LeCoultre", model: "Master Ultra Thin Moon", ref: "Q1368420", year: 2019, price: 11200, img: "watch-moonphase.jpg", cats: ["mens","moonphase","automatic"], movement: "Automatic", case: "Steel, 39 mm", condition: "Used (Very good)" },
  { brand: "Cartier", model: "Tank Louis", ref: "WGTA0011", year: 2017, price: 18900, img: "watch-womens.jpg", cats: ["womens","gold"], movement: "Quartz", case: "Yellow gold, 25.5 mm", condition: "Used (Very good)" },
  { brand: "Hublot", model: "Classic Fusion", ref: "511.NX.1171.LR", year: 2021, price: 9800, img: "watch-skeleton.jpg", cats: ["mens","skeleton","automatic"], movement: "Automatic", case: "Titanium, 45 mm", condition: "Used (Mint)" },
  { brand: "Patek Philippe", model: "Calatrava", ref: "5196J", year: 2016, price: 24500, img: "watch-gold.jpg", cats: ["mens","gold"], movement: "Manual winding", case: "Yellow gold, 37 mm", condition: "Used (Good)" },
  { brand: "Rolex", model: "Lady-Datejust", ref: "279173", year: 2020, price: 11240, img: "watch-womens.jpg", cats: ["womens","gold","automatic"], movement: "Automatic", case: "Steel and gold, 28 mm", condition: "Used (Mint)" },
  { brand: "Omega", model: "Speedmaster Reduced", ref: "3510.50", year: 2008, price: 3750, img: "watch-speedmaster.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 39 mm", condition: "Used (Good)" },
  { brand: "Rolex", model: "Explorer II", ref: "216570", year: 2017, price: 9250, img: "watch-gmt.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "Used (Very good)" },
  { brand: "Seiko", model: "Prospex Diver", ref: "SPB143", year: 2023, price: 890, img: "watch-submariner.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 40.5 mm", condition: "New" },
  { brand: "Grand Seiko", model: "Snowflake", ref: "SBGA211", year: 2022, price: 5450, img: "watch-datejust.jpg", cats: ["mens","automatic"], movement: "Spring Drive", case: "Steel, 41 mm", condition: "Used (Mint)" },
  { brand: "TAG Heuer", model: "Carrera Chronograph", ref: "CBN2010", year: 2021, price: 4290, img: "watch-daytona.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "Used (Very good)" },
  { brand: "Longines", model: "HydroConquest", ref: "L3.782.4.96.6", year: 2023, price: 1450, img: "watch-seamaster.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "New" },
  { brand: "Zenith", model: "Chronomaster Sport", ref: "03.3100.3600", year: 2022, price: 8900, img: "watch-daytona.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Mint)" },
  { brand: "Vacheron Constantin", model: "Overseas", ref: "4500V/110A-B126", year: 2019, price: 26800, img: "watch-royal-oak.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Very good)" },
  { brand: "A. Lange & Söhne", model: "Saxonia Moon Phase", ref: "384.026", year: 2018, price: 31200, img: "watch-moonphase.jpg", cats: ["mens","moonphase","gold"], movement: "Manual winding", case: "Pink gold, 40 mm", condition: "Used (Very good)" },
  { brand: "Tissot", model: "PRX Powermatic 80", ref: "T137.407.11.351.00", year: 2024, price: 695, img: "watch-santos.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "New" },
  { brand: "NOMOS", model: "Tangente", ref: "139", year: 2023, price: 1980, img: "watch-pilot.jpg", cats: ["mens","mechanical","affordable"], movement: "Manual winding", case: "Steel, 35 mm", condition: "New" },
  { brand: "Omega", model: "Constellation", ref: "131.20.36.20.02.001", year: 2022, price: 5120, img: "watch-womens.jpg", cats: ["womens","automatic"], movement: "Automatic", case: "Steel, 36 mm", condition: "Used (Mint)" },
  { brand: "Rolex", model: "Yacht-Master 40", ref: "126622", year: 2021, price: 14200, img: "watch-submariner.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel and platinum, 40 mm", condition: "Used (Very good)" },
  { brand: "Patek Philippe", model: "Aquanaut", ref: "5167A", year: 2019, price: 79500, img: "watch-nautilus.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 40.8 mm", condition: "Used (Very good)" },
  { brand: "Audemars Piguet", model: "Royal Oak Offshore", ref: "26420SO", year: 2021, price: 38500, img: "watch-royal-oak.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 43 mm", condition: "Used (Good)" },
  { brand: "Rolex", model: "Oyster Perpetual 36", ref: "126000", year: 2023, price: 8200, img: "watch-datejust.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 36 mm", condition: "New" },
  { brand: "Breitling", model: "Superocean Heritage", ref: "A20350A71B1A1", year: 2020, price: 4120, img: "watch-tudor.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "Used (Very good)" },
  { brand: "IWC", model: "Portugieser Chronograph", ref: "IW371604", year: 2018, price: 6850, img: "watch-navitimer.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Good)" },
  { brand: "Panerai", model: "Radiomir", ref: "PAM01343", year: 2022, price: 6400, img: "watch-panerai.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 45 mm", condition: "Used (Mint)" },
  { brand: "Seiko", model: "Presage Cocktail Time", ref: "SRPB43", year: 2021, price: 420, img: "watch-moonphase.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 40.5 mm", condition: "Used (Very good)" },
  { brand: "Rolex", model: "Sea-Dweller", ref: "126600", year: 2019, price: 13240, img: "watch-submariner.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 43 mm", condition: "Used (Very good)" },
  { brand: "Omega", model: "Planet Ocean", ref: "215.30.44.21.01.001", year: 2020, price: 5680, img: "watch-seamaster.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 43.5 mm", condition: "Used (Good)" },
  { brand: "Hublot", model: "Big Bang Unico", ref: "411.NX.1170.RX", year: 2018, price: 16200, img: "watch-skeleton.jpg", cats: ["mens","skeleton","automatic"], movement: "Automatic", case: "Titanium, 45 mm", condition: "Used (Good)" },
  { brand: "Jaeger-LeCoultre", model: "Reverso Classic", ref: "Q2518410", year: 2021, price: 7450, img: "watch-santos.jpg", cats: ["mens"], movement: "Manual winding", case: "Steel, 45.6 x 27.4 mm", condition: "Used (Mint)" },
  { brand: "Cartier", model: "Ballon Bleu", ref: "W69012Z4", year: 2016, price: 3980, img: "watch-womens.jpg", cats: ["womens","preowned"], movement: "Automatic", case: "Steel, 36 mm", condition: "Used (Good)" },
  { brand: "Tudor", model: "Black Bay Fifty-Eight", ref: "M79030N", year: 2023, price: 3590, img: "watch-tudor.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 39 mm", condition: "New" },
  { brand: "Rolex", model: "Sky-Dweller", ref: "326934", year: 2020, price: 19850, img: "watch-datejust.jpg", cats: ["mens","preowned","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "Used (Very good)" },
  { brand: "Patek Philippe", model: "Grand Complications", ref: "5270P", year: 2015, price: 186000, img: "watch-moonphase.jpg", cats: ["mens","moonphase","preowned"], movement: "Manual winding", case: "Platinum, 41 mm", condition: "Used (Very good)" },
  { brand: "Omega", model: "De Ville Prestige", ref: "424.10.40.20.02.001", year: 2022, price: 3120, img: "watch-pilot.jpg", cats: ["mens","automatic"], movement: "Automatic", case: "Steel, 39.5 mm", condition: "Used (Mint)" },
  { brand: "Patek Philippe", model: "Hunter Pocket Watch", ref: "6000J", year: 1998, price: 22400, img: "watch-pocket.jpg", cats: ["pocket","gold","preowned"], movement: "Manual winding", case: "Yellow gold, 47 mm", condition: "Used (Very good)" },
  { brand: "A. Lange & Söhne", model: "Open-face Pocket Watch", ref: "860.032", year: 1992, price: 18600, img: "watch-pocket.jpg", cats: ["pocket","gold","preowned","vintage"], movement: "Manual winding", case: "Yellow gold, 49 mm", condition: "Used (Good)" },
  { brand: "Breguet", model: "Classique", ref: "5177BA", year: 2019, price: 18900, img: "watch-gold.jpg", cats: ["mens","gold","swiss","mechanical"], movement: "Automatic", case: "Yellow gold, 38 mm", condition: "Used (Very good)" },
  { brand: "Breguet", model: "Type XX", ref: "2067ST", year: 2023, price: 16850, img: "watch-daytona.jpg", cats: ["mens","chrono","pilot","swiss","automatic"], movement: "Automatic", case: "Steel, 42 mm", condition: "New" },
  { brand: "Hamilton", model: "Khaki Field", ref: "H70455533", year: 2022, price: 545, img: "watch-pilot.jpg", cats: ["mens","military","pilot","affordable","automatic"], movement: "Automatic", case: "Steel, 38 mm", condition: "New" },
  { brand: "Hamilton", model: "Jazzmaster", ref: "H32451111", year: 2021, price: 890, img: "watch-datejust.jpg", cats: ["mens","automatic","affordable"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Mint)" },
  { brand: "Oris", model: "Aquis Date", ref: "01.733.7730", year: 2023, price: 2100, img: "watch-seamaster.jpg", cats: ["mens","dive","automatic","swiss"], movement: "Automatic", case: "Steel, 43.5 mm", condition: "New" },
  { brand: "Oris", model: "Big Crown Pointer Date", ref: "01.754.7741", year: 2020, price: 1650, img: "watch-pilot.jpg", cats: ["mens","pilot","automatic","swiss"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Richard Mille", model: "RM 011", ref: "RM011", year: 2018, price: 245000, img: "watch-skeleton.jpg", cats: ["mens","skeleton","chrono","preowned"], movement: "Automatic", case: "Titanium, 50 mm", condition: "Used (Very good)" },
  { brand: "Richard Mille", model: "RM 035", ref: "RM035", year: 2021, price: 198000, img: "watch-skeleton.jpg", cats: ["mens","skeleton","preowned"], movement: "Automatic", case: "NTPT carbon, 49.9 mm", condition: "Used (Mint)" },
  { brand: "Ulysse Nardin", model: "Marine Diver", ref: "263-33", year: 2019, price: 8900, img: "watch-seamaster.jpg", cats: ["mens","dive","automatic","swiss"], movement: "Automatic", case: "Steel, 44 mm", condition: "Used (Good)" },
  { brand: "Ulysse Nardin", model: "Blast", ref: "1723-400", year: 2022, price: 22400, img: "watch-skeleton.jpg", cats: ["mens","skeleton","automatic","swiss"], movement: "Automatic", case: "Carbon, 45 mm", condition: "Used (Mint)" },
  { brand: "NOMOS", model: "Club Sport", ref: "781", year: 2023, price: 2800, img: "watch-datejust.jpg", cats: ["mens","automatic","affordable"], movement: "Automatic", case: "Steel, 42 mm", condition: "New" },
  { brand: "Sinn", model: "856 UTC", ref: "856.010", year: 2021, price: 2190, img: "watch-gmt.jpg", cats: ["mens","pilot","military","automatic"], movement: "Automatic", case: "Steel, 40 mm", condition: "Used (Very good)" },
  { brand: "Sinn", model: "104 St Sa I", ref: "104.011", year: 2022, price: 1650, img: "watch-pilot.jpg", cats: ["mens","pilot","chrono","automatic"], movement: "Automatic", case: "Steel, 41 mm", condition: "New" },
  { brand: "Gauri", model: "Lotus", ref: "GR-LT-36", year: 2024, price: 12400, img: "gauri-lotus.jpg", cats: ["womens","gold","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 36 mm", condition: "New" },
  { brand: "Gauri", model: "Lotus", ref: "GR-LT-36", year: 2022, price: 9800, img: "gauri-lotus.jpg", cats: ["womens","gold","automatic","preowned","swiss"], movement: "Automatic", case: "Yellow gold, 36 mm", condition: "Used (Very good)" },
  { brand: "Gauri", model: "Tikka", ref: "GR-TK-28", year: 2025, price: 18600, img: "gauri-tikka.jpg", cats: ["womens","gold","swiss"], movement: "Quartz", case: "Yellow gold, 28 mm", condition: "New" },
  { brand: "Gauri", model: "Tikka", ref: "GR-TK-28", year: 2021, price: 14200, img: "gauri-tikka.jpg", cats: ["womens","gold","preowned","swiss"], movement: "Quartz", case: "Yellow gold, 28 mm", condition: "Used (Mint)" },
  { brand: "Gauri", model: "Saffron Chronograph", ref: "GR-SF-42", year: 2024, price: 16850, img: "gauri-saffron.jpg", cats: ["mens","gold","chrono","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 42 mm", condition: "New" },
  { brand: "Gauri", model: "Saffron Chronograph", ref: "GR-SF-42", year: 2020, price: 12900, img: "gauri-saffron.jpg", cats: ["mens","gold","chrono","automatic","preowned","swiss"], movement: "Automatic", case: "Yellow gold, 42 mm", condition: "Used (Good)" },
  { brand: "Gauri", model: "Midnight", ref: "GR-MN-41", year: 2025, price: 8900, img: "gauri-midnight.jpg", cats: ["mens","automatic","swiss"], movement: "Automatic", case: "Steel, 41 mm", condition: "New" },
  { brand: "Gauri", model: "Midnight", ref: "GR-MN-41", year: 2023, price: 7200, img: "gauri-midnight.jpg", cats: ["mens","automatic","preowned","swiss"], movement: "Automatic", case: "Steel, 41 mm", condition: "Used (Very good)" },
  { brand: "Gauri", model: "Heritage Moon", ref: "GR-HR-39", year: 2024, price: 15400, img: "gauri-heritage.jpg", cats: ["mens","moonphase","mechanical","swiss"], movement: "Automatic", case: "Steel, 39 mm", condition: "New" },
  { brand: "Gauri", model: "Heritage Moon", ref: "GR-HR-39", year: 2019, price: 11250, img: "gauri-heritage.jpg", cats: ["mens","moonphase","preowned","vintage","swiss"], movement: "Automatic", case: "Steel, 39 mm", condition: "Used (Very good)" },
  { brand: "Gauri", model: "Temple", ref: "GR-TP-27", year: 2025, price: 21400, img: "gauri-temple.jpg", cats: ["womens","gold","mechanical","swiss"], movement: "Manual winding", case: "Yellow gold, 27 x 41 mm", condition: "New" },
  { brand: "Gauri", model: "Temple", ref: "GR-TP-27", year: 2018, price: 16800, img: "gauri-temple.jpg", cats: ["womens","gold","preowned","vintage","swiss"], movement: "Manual winding", case: "Yellow gold, 27 x 41 mm", condition: "Used (Good)" },
  { brand: "Gauri", model: "Pearl", ref: "GR-PR-30", year: 2024, price: 7600, img: "gauri-pearl.jpg", cats: ["womens","gold","swiss"], movement: "Quartz", case: "Rose gold, 30 mm", condition: "New" },
  { brand: "Gauri", model: "Pearl", ref: "GR-PR-30", year: 2022, price: 5900, img: "gauri-pearl.jpg", cats: ["womens","gold","preowned","swiss"], movement: "Quartz", case: "Rose gold, 30 mm", condition: "Used (Mint)" },
  { brand: "Gauri", model: "Royale Diver", ref: "GR-RD-42", year: 2025, price: 24800, img: "gauri-royale.jpg", cats: ["mens","gold","dive","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 42 mm", condition: "New" },
  { brand: "Gauri", model: "Royale Diver", ref: "GR-RD-42", year: 2021, price: 18950, img: "gauri-royale.jpg", cats: ["mens","gold","dive","automatic","preowned","swiss"], movement: "Automatic", case: "Yellow gold, 42 mm", condition: "Used (Very good)" },
  { brand: "Gauri", model: "Lotus Skeleton", ref: "GR-LS-38", year: 2024, price: 19600, img: "watch-skeleton.jpg", cats: ["womens","skeleton","gold","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 38 mm", condition: "New" },
  { brand: "Gauri", model: "Maang", ref: "GR-MG-34", year: 2023, price: 11200, img: "gauri-pearl.jpg", cats: ["womens","gold","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 34 mm", condition: "Used (Mint)" },
  { brand: "Gauri", model: "Saffron Chronograph", ref: "GR-SF-42G", year: 2025, price: 27400, img: "gauri-saffron.jpg", cats: ["mens","gold","chrono","automatic","swiss"], movement: "Automatic", case: "Yellow gold, 42 mm", condition: "New" },
  { brand: "Gauri", model: "Midnight GMT", ref: "GR-MN-GMT", year: 2024, price: 10400, img: "gauri-midnight.jpg", cats: ["mens","automatic","swiss"], movement: "Automatic", case: "Steel, 41 mm", condition: "New" },
];

function slugify(s) {
  return String(s).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

const GALLERY_ALIASES = {
  "rolex-submariner": "rolex-submariner-date",
  "rolex-datejust": "rolex-datejust-36",
  "rolex-day-date": "rolex-day-date-40",
};

function gallerySlug(brand, model) {
  const slug = slugify(`${brand}-${model}`);
  return GALLERY_ALIASES[slug] || slug;
}

function galleryPaths(brand, model) {
  const slug = gallerySlug(brand, model);
  return [1, 2, 3, 4, 5, 6, 7, 8].map((n) => `assets/watches/galleries/${slug}/${String(n).padStart(2, "0")}.jpg`);
}

const WATCHES = SEED.map((w, i) => {
  const seller = SELLERS[i % SELLERS.length];
  const box = i % 5 !== 2;
  const papers = i % 4 !== 1;
  const swiss = new Set(["Rolex","Omega","Patek Philippe","Audemars Piguet","Breitling","Cartier","IWC","Jaeger-LeCoultre","Hublot","Vacheron Constantin","A. Lange & Söhne","Breguet","Oris","Ulysse Nardin","Zenith","Longines","TAG Heuer","Tudor","Gauri","Richard Mille"]);
  const cats = w.cats.slice();
  if (swiss.has(w.brand) && !cats.includes("swiss")) cats.push("swiss");
  if (w.year <= 2010 && !cats.includes("vintage")) cats.push("vintage");
  if (/chrono|daytona|speedmaster|carrera|navitimer/i.test(w.model) && !cats.includes("chrono")) cats.push("chrono");
  if (/submariner|seamaster|diver|aquis|sea-dweller|planet ocean/i.test(w.model) && !cats.includes("dive")) cats.push("dive");
  if (/pilot|khaki|mark xviii|navitimer/i.test(w.model) && !cats.includes("pilot")) cats.push("pilot");
  if (w.price < 2000 && !cats.includes("affordable")) cats.push("affordable");
  if (/automatic/i.test(w.movement) && !cats.includes("automatic")) cats.push("automatic");
  if (/manual/i.test(w.movement) && !cats.includes("mechanical")) cats.push("mechanical");
  return {
    id: slugify(`${w.brand}-${w.model}-${w.ref}-${i}`),
    brand: w.brand,
    model: w.model,
    ref: w.ref,
    year: w.year,
    price: w.price,
    image: galleryPaths(w.brand, w.model)[i % 8],
    images: galleryPaths(w.brand, w.model),
    cats,
    movement: w.movement,
    case: w.case,
    condition: w.condition,
    box,
    papers,
    seller,
    location: seller.loc,
    views: 420 + ((i * 97) % 2800),
    description: `A ${w.condition.toLowerCase()} ${w.brand} ${w.model} (ref. ${w.ref}) from ${w.year}. ${w.case}. ${w.movement} movement. ${box ? "Original box included." : "No box."} ${papers ? "Papers included." : "No papers."} Ships worldwide with insured courier and Buyer Protection.`,
  };
});

const REVIEWS = [
  { name: "James P.", loc: "Chicago, US", text: "Escrow made the purchase painless. Watch arrived exactly as described, fully insured." },
  { name: "Elena R.", loc: "Madrid, ES", text: "I compared dozens of Daytonas here before buying. The listing photos and dealer rating gave me confidence." },
  { name: "Kenji S.", loc: "Osaka, JP", text: "Sold my old Seamaster in under a week. Communication with the buyer was clear and payout was fast." },
  { name: "Amelia T.", loc: "London, UK", text: "First luxury watch purchase. Support walked me through authentication and shipping. Would use again." },
];

const ARTICLES = [
  {
    id: "speedmaster-models",
    tag: "Watch market",
    title: "The 5 Most Popular Omega Speedmaster Models",
    author: "Nora Blake",
    date: "August 12, 2026",
    read: "6 min",
    image: "assets/magazine/mag-speedmaster.jpg",
    body: "The Speedmaster remains one of the most searched chronographs on the market. From the professional Moonwatch to reduced and numbered editions, collectors still treat it as the default mechanical chronograph — and prices have stayed remarkably orderly compared with steel sports watches from other maisons.",
  },
  {
    id: "hublot-expensive",
    tag: "Watch market",
    title: "The 5 Most Expensive Hublot Watches: What Makes Them So Special?",
    author: "Marcus Ellison",
    date: "August 4, 2026",
    read: "5 min",
    image: "assets/magazine/mag-hublot.jpg",
    body: "Hublot built its name on materials experiments — ceramic, carbon, sapphire — and limited collaborations. The top of the catalogue is less about a single icon and more about scarce cases, unique movements, and the secondary-market premium that follows a sold-out launch.",
  },
];

const VIDEOS = [
  { title: "How to read a listing like a dealer", host: "Watch Talk", time: "12:04", date: "Aug 8, 2026", image: "assets/videos/video-1.jpg" },
  { title: "Steel sports watches: what actually holds value", host: "Watch Talk", time: "18:41", date: "Jul 29, 2026", image: "assets/videos/video-2.jpg" },
  { title: "A night in the vault: three unexpected finds", host: "Watch Talk", time: "09:22", date: "Jul 18, 2026", image: "assets/videos/video-3.jpg" },
];

const INSTAGRAM = [1,2,3,4,5,6,7,8].map((n) => `assets/instagram/ig-${n}.jpg`);

const COUNTRIES = [
  { name: "United States", code: "us" },
  { name: "United Kingdom", code: "gb" },
  { name: "Deutschland", code: "de" },
  { name: "France", code: "fr" },
  { name: "Italia", code: "it" },
  { name: "España", code: "es" },
  { name: "日本", code: "jp" },
  { name: "中国", code: "cn" },
  { name: "Suisse", code: "ch" },
  { name: "Nederland", code: "nl" },
  { name: "Australia", code: "au" },
  { name: "Canada", code: "ca" },
  { name: "Hong Kong", code: "hk" },
  { name: "Singapore", code: "sg" },
  { name: "United Arab Emirates", code: "ae" },
  { name: "한국", code: "kr" },
  { name: "Brasil", code: "br" },
  { name: "México", code: "mx" },
  { name: "Sverige", code: "se" },
  { name: "Norge", code: "no" },
  { name: "Österreich", code: "at" },
  { name: "Belgique", code: "be" },
  { name: "Danmark", code: "dk" },
  { name: "Suomi", code: "fi" },
  { name: "Ireland", code: "ie" },
  { name: "Portugal", code: "pt" },
  { name: "Polska", code: "pl" },
  { name: "Ελλάδα", code: "gr" },
  { name: "Россия", code: "ru" },
  { name: "Magyarország", code: "hu" },
  { name: "Česko", code: "cz" },
  { name: "România", code: "ro" },
  { name: "Türkiye", code: "tr" },
  { name: "India", code: "in" },
  { name: "ประเทศไทย", code: "th" },
  { name: "Malaysia", code: "my" },
  { name: "Indonesia", code: "id" },
  { name: "Pilipinas", code: "ph" },
  { name: "New Zealand", code: "nz" },
  { name: "South Africa", code: "za" },
  { name: "Argentina", code: "ar" },
  { name: "Chile", code: "cl" },
  { name: "Colombia", code: "co" },
  { name: "Israel", code: "il" },
  { name: "Saudi Arabia", code: "sa" },
  { name: "Qatar", code: "qa" },
  { name: "臺灣", code: "tw" },
  { name: "Luxembourg", code: "lu" },
];

const SEEDS_BY_BRAND = {};
for (const s of SEED) {
  (SEEDS_BY_BRAND[s.brand] || (SEEDS_BY_BRAND[s.brand] = [])).push(s);
}

const FEATURED_MODELS = {
  Rolex: [
    { model: "GMT-Master II", from: 10764, img: galleryPaths("Rolex", "GMT-Master II")[0] },
    { model: "Daytona", from: 16227, img: galleryPaths("Rolex", "Daytona")[0] },
    { model: "Submariner", from: 8264, img: galleryPaths("Rolex", "Submariner")[0] },
    { model: "Datejust", from: 1873, img: galleryPaths("Rolex", "Datejust")[0] },
    { model: "Day-Date", from: 9038, img: galleryPaths("Rolex", "Day-Date")[0] },
  ],
  Gauri: [
    { model: "Lotus", from: 9800, img: galleryPaths("Gauri", "Lotus")[0] },
    { model: "Tikka", from: 14200, img: galleryPaths("Gauri", "Tikka")[0] },
    { model: "Saffron Chronograph", from: 12900, img: galleryPaths("Gauri", "Saffron Chronograph")[0] },
    { model: "Midnight", from: 7200, img: galleryPaths("Gauri", "Midnight")[0] },
    { model: "Royale Diver", from: 18950, img: galleryPaths("Gauri", "Royale Diver")[0] },
  ],
};

SITE.listingCount = BRANDS.reduce((sum, b) => sum + b.count, 0).toLocaleString("en-US");
