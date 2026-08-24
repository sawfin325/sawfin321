# Evergold Pomeranians

Family Pomeranian kennel website. Contact: **+1 743-259-3337**. Orders: WhatsApp or **miaspomeranian@gmail.com**.

## WordPress version (recommended)

A complete WordPress theme lives in `wordpress/evergold-pomeranians/`. Zip that folder and upload it under **Appearance → Themes**.

```bash
cd wordpress
zip -r evergold-pomeranians-wordpress-theme.zip evergold-pomeranians
```

Activate the theme, then set permalinks to **Post name**. Activation creates the pages, 18 puppies, blog posts, and menu. See `wordpress/README.md`.

## Static HTML version

The original static site is still in this folder.

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.
