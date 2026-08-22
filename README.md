# PalletHaven

Static HTML wholesale shop for liquidation pallets (Netherlands and Europe).

Open `index.html` in a browser, or serve the folder locally:

```bash
python3 -m http.server 8080
```

Then: http://localhost:8080

## Pages

- Home, shop, categories and product pages
- Contact, about, account, cart and checkout
- Privacy, terms, shipping and disclaimer

The cart runs in the browser (localStorage). Orders in this demo do not go to a real payment provider. Send orders by email or WhatsApp.

Rebuild the pages:

```bash
python3 scripts/build_site.py
```
