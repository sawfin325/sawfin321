# PalletHaven

Statische HTML-website voor groothandel in liquidatiepallets (Nederland en Europa).

Open `index.html` in een browser, of serveer de map lokaal:

```bash
python3 -m http.server 8080
```

Daarna: http://localhost:8080

## Pagina’s

- Home, winkel, categorieën en productpagina’s
- Contact, over ons, account, winkelwagen en afrekenen
- Privacy, algemene voorwaarden, levering en disclaimer

De winkelwagen draait in de browser (localStorage). Bestellingen in deze demo gaan niet naar een echte betaalprovider.

Pagina’s opnieuw opbouwen:

```bash
python3 scripts/build_site.py
```
