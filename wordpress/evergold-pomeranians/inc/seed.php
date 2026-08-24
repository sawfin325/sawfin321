<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_seed_site() {
    if (get_option('evergold_seeded')) {
        return;
    }
    if (!did_action('init')) {
        return;
    }
    $data = evergold_seed_data();
    if (!$data) {
        return;
    }

    set_theme_mod('evergold_phone', $data['phone'] ?? '+1 743-259-3337');
    set_theme_mod('evergold_email', $data['email'] ?? 'miaspomeranian@gmail.com');
    set_theme_mod('evergold_whatsapp', $data['whatsapp'] ?? '17432593337');

    $page_ids = [];
    foreach ($data['pages'] as $page) {
        $existing = get_page_by_path($page['slug']);
        if ($existing) {
            $page_ids[$page['slug']] = $existing->ID;
            continue;
        }
        $id = wp_insert_post([
            'post_title' => $page['title'],
            'post_name' => $page['slug'],
            'post_status' => 'publish',
            'post_type' => 'page',
            'post_content' => $page['content'],
        ]);
        if (!is_wp_error($id) && !empty($page['template'])) {
            update_post_meta($id, '_wp_page_template', $page['template']);
        }
        if (!is_wp_error($id)) {
            $page_ids[$page['slug']] = $id;
        }
    }

    if (!empty($page_ids['home'])) {
        update_option('show_on_front', 'page');
        update_option('page_on_front', $page_ids['home']);
    }
    if (!empty($page_ids['blog'])) {
        update_option('page_for_posts', $page_ids['blog']);
    }

    foreach ($data['puppies'] as $puppy) {
        if (get_page_by_path($puppy['slug'], OBJECT, 'puppy')) {
            continue;
        }
        $id = wp_insert_post([
            'post_title' => $puppy['name'],
            'post_name' => $puppy['slug'],
            'post_status' => 'publish',
            'post_type' => 'puppy',
            'post_content' => $puppy['bio'],
        ]);
        if (is_wp_error($id)) {
            continue;
        }
        foreach (['color', 'sex', 'age', 'weight', 'price', 'status', 'temperament'] as $key) {
            update_post_meta($id, '_evergold_' . $key, $puppy[$key]);
        }
        update_post_meta($id, '_evergold_photos', $puppy['photos']);
    }

    foreach ($data['posts'] as $post) {
        if (get_page_by_path($post['slug'], OBJECT, 'post')) {
            continue;
        }
        $id = wp_insert_post([
            'post_title' => $post['title'],
            'post_name' => $post['slug'],
            'post_status' => 'publish',
            'post_type' => 'post',
            'post_content' => $post['html'],
            'post_excerpt' => $post['excerpt'],
            'post_date' => date('Y-m-d H:i:s', strtotime($post['date'])),
        ]);
        if (!is_wp_error($id) && !empty($post['img'])) {
            update_post_meta($id, '_evergold_hero', $post['img']);
        }
    }

    $menu_name = 'Evergold Primary';
    $menu = wp_get_nav_menu_object($menu_name);
    if (!$menu) {
        $menu_id = wp_create_nav_menu($menu_name);
        $items = [
            ['title' => 'Home', 'url' => home_url('/')],
            ['title' => 'Puppies', 'url' => get_post_type_archive_link('puppy')],
            ['title' => 'About Us', 'slug' => 'about-us'],
            ['title' => 'Care Guide', 'slug' => 'care-guide'],
            ['title' => 'Solution', 'slug' => 'solution'],
            ['title' => 'Blog', 'slug' => 'blog'],
            ['title' => 'Order', 'slug' => 'order'],
            ['title' => 'Shipping', 'slug' => 'shipping'],
            ['title' => 'Health', 'slug' => 'health'],
        ];
        foreach ($items as $item) {
            $args = [
                'menu-item-title' => $item['title'],
                'menu-item-status' => 'publish',
                'menu-item-type' => 'custom',
            ];
            if (!empty($item['url'])) {
                $args['menu-item-url'] = $item['url'];
            } elseif (!empty($item['slug']) && !empty($page_ids[$item['slug']])) {
                $args['menu-item-type'] = 'post_type';
                $args['menu-item-object'] = 'page';
                $args['menu-item-object-id'] = $page_ids[$item['slug']];
            } else {
                $args['menu-item-url'] = evergold_page_url($item['slug'] ?? '');
            }
            wp_update_nav_menu_item($menu_id, 0, $args);
        }
        $locations = get_theme_mod('nav_menu_locations', []);
        $locations['primary'] = $menu_id;
        set_theme_mod('nav_menu_locations', $locations);
    }

    flush_rewrite_rules();
    update_option('evergold_seeded', 1);
}
add_action('init', 'evergold_seed_site', 20);
