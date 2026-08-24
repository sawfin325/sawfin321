<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="<?php echo esc_url(get_template_directory_uri() . '/assets/favicon.svg'); ?>" type="image/svg+xml">
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<div class="topbar">
  <div class="wrap">
    <span>Family-raised AKC Pomeranian puppies</span>
    <a href="tel:+<?php echo esc_attr(evergold_phone_tel()); ?>">Call <?php echo esc_html(evergold_phone()); ?></a>
  </div>
</div>
<header class="site-header">
  <div class="wrap nav-wrap">
    <a class="logo" href="<?php echo esc_url(home_url('/')); ?>">
      <svg class="logo-mark" viewBox="0 0 64 64" aria-hidden="true">
        <rect width="64" height="64" rx="16" fill="#2A2218"/>
        <path d="M32 14l4.2 8.8 9.6 1.2-7.1 6.6 1.9 9.5L32 35.6 23.4 40.1l1.9-9.5-7.1-6.6 9.6-1.2z" fill="#B8894A"/>
      </svg>
      <span class="logo-text"><strong>Evergold</strong><span>Pomeranians</span></span>
    </a>
    <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
      <?php
      wp_nav_menu([
          'theme_location' => 'primary',
          'container' => false,
          'fallback_cb' => 'evergold_fallback_menu',
          'depth' => 1,
      ]);
      ?>
    </nav>
    <a class="btn header-cta" href="<?php echo esc_url(evergold_page_url('order')); ?>">Order</a>
  </div>
</header>
<main>
