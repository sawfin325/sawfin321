# Evergold Pomeranians WordPress theme

This folder is a complete WordPress theme converted from the static kennel site. It keeps the same design, 18 puppies, WhatsApp/email ordering, blog, and pages.

## Download the upload file

Use this zip in WordPress (Appearance → Themes → Upload Theme):

- [evergold-pomeranians-wordpress-theme.zip](https://github.com/sawfin325/sawfin321/raw/cursor/pomeranian-website-e7ca/wordpress/evergold-pomeranians-wordpress-theme.zip)

## Install on any WordPress host

1. Install WordPress (Hostinger, Bluehost, SiteGround, or wordpress.org).
2. Download `evergold-pomeranians-wordpress-theme.zip` (or zip the `evergold-pomeranians` folder yourself).
3. In wp-admin go to **Appearance → Themes → Add New → Upload Theme**.
4. Upload `evergold-pomeranians-wordpress-theme.zip`.
5. Click **Activate**.
6. Go to **Settings → Permalinks**, choose **Post name**, and save.

On first activation the theme creates:

- Home, About, Care Guide, Solution, Order, Shipping, Health, and Blog pages
- 18 puppy listings with your photos
- 5 featured blog posts
- The main menu
- Phone **+1 743-259-3337** and email **miaspomeranian@gmail.com**

## After activation

- Edit puppies under **Puppies** in wp-admin.
- Change phone, email, or WhatsApp under **Appearance → Customize → Evergold contact**.
- The Order page is an online puppy inquiry form. Submissions are emailed to **miaspomeranian@gmail.com**.
- You can also see them under **Inquiries** in wp-admin.
- To make Gmail actually receive them: **Appearance → Customize → Evergold contact → Gmail app password**.
  1. Open Google Account → Security → 2-Step Verification → App passwords.
  2. Create a password for Mail.
  3. Paste the 16-character password into that Customizer field and Publish.
  4. Send a test inquiry. Also check Gmail spam the first time.

## Local test with Docker (optional)

From the `wordpress` folder:

```bash
docker compose up -d
```

Then open http://localhost:8080, finish the WordPress installer, and activate **Evergold Pomeranians**.
