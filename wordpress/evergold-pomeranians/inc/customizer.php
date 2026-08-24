<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_customize_register($wp_customize) {
    $wp_customize->add_section('evergold_contact', [
        'title' => 'Evergold contact',
        'priority' => 30,
    ]);

    $wp_customize->add_setting('evergold_phone', ['default' => '+1 743-259-3337', 'sanitize_callback' => 'sanitize_text_field']);
    $wp_customize->add_control('evergold_phone', [
        'label' => 'Phone',
        'section' => 'evergold_contact',
        'type' => 'text',
    ]);

    $wp_customize->add_setting('evergold_email', ['default' => 'miaspomeranian@gmail.com', 'sanitize_callback' => 'sanitize_email']);
    $wp_customize->add_control('evergold_email', [
        'label' => 'Order email',
        'section' => 'evergold_contact',
        'type' => 'email',
    ]);

    $wp_customize->add_setting('evergold_whatsapp', ['default' => '17432593337', 'sanitize_callback' => 'sanitize_text_field']);
    $wp_customize->add_control('evergold_whatsapp', [
        'label' => 'WhatsApp number (digits only)',
        'section' => 'evergold_contact',
        'type' => 'text',
    ]);
}
add_action('customize_register', 'evergold_customize_register');
