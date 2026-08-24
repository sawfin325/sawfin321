<?php
if (!defined('ABSPATH')) {
    exit;
}

define('EVERGOLD_VERSION', '1.1.0');

require get_template_directory() . '/inc/helpers.php';
require get_template_directory() . '/inc/cpt.php';
require get_template_directory() . '/inc/customizer.php';
require get_template_directory() . '/inc/inquiry.php';
require get_template_directory() . '/inc/seed.php';

function evergold_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'gallery', 'caption', 'style', 'script']);
    add_theme_support('custom-logo');
    add_theme_support('automatic-feed-links');
    register_nav_menus([
        'primary' => 'Primary Menu',
    ]);
}
add_action('after_setup_theme', 'evergold_setup');

function evergold_assets() {
    wp_enqueue_style(
        'evergold-fonts',
        'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Outfit:wght@300;400;500;600&display=swap',
        [],
        null
    );
    wp_enqueue_style('evergold', get_template_directory_uri() . '/assets/css/styles.css', [], EVERGOLD_VERSION);
    wp_enqueue_style('evergold-wp', get_template_directory_uri() . '/assets/css/wordpress.css', ['evergold'], EVERGOLD_VERSION);
    wp_enqueue_script('evergold', get_template_directory_uri() . '/assets/js/main.js', [], EVERGOLD_VERSION, true);
    wp_localize_script('evergold', 'evergoldOrder', [
        'wa' => evergold_wa_number(),
        'email' => evergold_email(),
    ]);
    if (is_home()) {
        wp_enqueue_script('evergold-blog', get_template_directory_uri() . '/assets/js/blog-archive.js', [], EVERGOLD_VERSION, true);
        $blog_url = get_option('page_for_posts') ? get_permalink(get_option('page_for_posts')) : home_url('/blog/');
        wp_localize_script('evergold-blog', 'evergoldBlog', [
            'list' => $blog_url,
        ]);
    }
}
add_action('wp_enqueue_scripts', 'evergold_assets');

function evergold_page_html($content) {
    if (is_page()) {
        remove_filter('the_content', 'wpautop');
    }
    return $content;
}
add_filter('the_content', 'evergold_page_html', 9);

function evergold_puppy_archive($query) {
    if (!is_admin() && $query->is_main_query() && is_post_type_archive('puppy')) {
        $query->set('posts_per_page', -1);
        $query->set('orderby', 'date');
        $query->set('order', 'ASC');
    }
}
add_action('pre_get_posts', 'evergold_puppy_archive');

function evergold_excerpt_more() {
    return '…';
}
add_filter('excerpt_more', 'evergold_excerpt_more');
