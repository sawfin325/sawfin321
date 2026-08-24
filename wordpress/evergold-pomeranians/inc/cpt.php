<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_register_puppy_cpt() {
    register_post_type('puppy', [
        'labels' => [
            'name' => 'Puppies',
            'singular_name' => 'Puppy',
            'add_new_item' => 'Add Puppy',
            'edit_item' => 'Edit Puppy',
        ],
        'public' => true,
        'has_archive' => true,
        'rewrite' => ['slug' => 'puppies'],
        'menu_icon' => 'dashicons-pets',
        'supports' => ['title', 'editor', 'thumbnail'],
        'show_in_rest' => true,
    ]);
}
add_action('init', 'evergold_register_puppy_cpt');

function evergold_puppy_meta_boxes() {
    add_meta_box('evergold_puppy_details', 'Puppy details', 'evergold_puppy_meta_box_html', 'puppy', 'side', 'high');
}
add_action('add_meta_boxes', 'evergold_puppy_meta_boxes');

function evergold_puppy_meta_box_html($post) {
    wp_nonce_field('evergold_puppy_meta', 'evergold_puppy_nonce');
    $fields = [
        'color' => 'Color',
        'sex' => 'Sex',
        'age' => 'Age',
        'weight' => 'Weight',
        'price' => 'Price',
        'status' => 'Status (Available or Reserved)',
        'temperament' => 'Temperament',
    ];
    foreach ($fields as $key => $label) {
        $value = esc_attr(get_post_meta($post->ID, '_evergold_' . $key, true));
        echo '<p><label>' . esc_html($label) . '<br><input type="text" name="evergold_' . esc_attr($key) . '" value="' . $value . '" class="widefat"></label></p>';
    }
}

function evergold_save_puppy_meta($post_id) {
    if (!isset($_POST['evergold_puppy_nonce']) || !wp_verify_nonce($_POST['evergold_puppy_nonce'], 'evergold_puppy_meta')) {
        return;
    }
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }
    foreach (['color', 'sex', 'age', 'weight', 'price', 'status', 'temperament'] as $key) {
        if (isset($_POST['evergold_' . $key])) {
            update_post_meta($post_id, '_evergold_' . $key, sanitize_text_field(wp_unslash($_POST['evergold_' . $key])));
        }
    }
}
add_action('save_post_puppy', 'evergold_save_puppy_meta');
