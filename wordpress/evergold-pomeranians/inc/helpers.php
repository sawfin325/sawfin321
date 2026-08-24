<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_phone() {
    return get_theme_mod('evergold_phone', '+1 743-259-3337');
}

function evergold_phone_tel() {
    return preg_replace('/\D+/', '', evergold_phone());
}

function evergold_email() {
    return get_theme_mod('evergold_email', 'miaspomeranian@gmail.com');
}

function evergold_wa_number() {
    return get_theme_mod('evergold_whatsapp', '17432593337');
}

function evergold_order_message($puppy = 'a Pomeranian puppy') {
    return 'Hello Evergold, I would like to order ' . $puppy . '. Please send the latest video, the health packet, and reservation steps.';
}

function evergold_wa_url($puppy = 'a Pomeranian puppy') {
    return 'https://wa.me/' . rawurlencode(evergold_wa_number()) . '?text=' . rawurlencode(evergold_order_message($puppy));
}

function evergold_mail_url($puppy = 'a Pomeranian puppy') {
    return 'mailto:' . evergold_email() . '?subject=' . rawurlencode('Puppy order: ' . $puppy) . '&body=' . rawurlencode(evergold_order_message($puppy));
}

function evergold_seed_data() {
    static $data = null;
    if ($data === null) {
        $file = get_template_directory() . '/inc/seed-data.json';
        $data = file_exists($file) ? json_decode(file_get_contents($file), true) : [];
    }
    return is_array($data) ? $data : [];
}

function evergold_theme_uri($relative) {
    $relative = ltrim($relative, '/');
    if (strpos($relative, 'http') === 0) {
        return $relative;
    }
    return get_template_directory_uri() . '/' . $relative;
}

function evergold_puppy_photos($post_id) {
    $photos = get_post_meta($post_id, '_evergold_photos', true);
    if (is_array($photos) && $photos) {
        return array_map('evergold_theme_uri', $photos);
    }
    if (has_post_thumbnail($post_id)) {
        return [get_the_post_thumbnail_url($post_id, 'large')];
    }
    return [];
}

function evergold_page_url($slug) {
    $page = get_page_by_path($slug);
    if ($page) {
        return get_permalink($page);
    }
    if ($slug === 'puppies') {
        return get_post_type_archive_link('puppy');
    }
    if ($slug === 'blog') {
        $posts = get_option('page_for_posts');
        return $posts ? get_permalink($posts) : home_url('/blog/');
    }
    return home_url('/' . $slug . '/');
}

function evergold_fallback_menu() {
    $links = [
        ['Home', home_url('/')],
        ['Puppies', get_post_type_archive_link('puppy')],
        ['About Us', evergold_page_url('about-us')],
        ['Care Guide', evergold_page_url('care-guide')],
        ['Solution', evergold_page_url('solution')],
        ['Blog', evergold_page_url('blog')],
        ['Order', evergold_page_url('order')],
        ['Shipping', evergold_page_url('shipping')],
        ['Health', evergold_page_url('health')],
    ];
    echo '<ul>';
    foreach ($links as $link) {
        echo '<li><a href="' . esc_url($link[1]) . '">' . esc_html($link[0]) . '</a></li>';
    }
    echo '</ul>';
}
