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

    $wp_customize->add_setting('evergold_gmail_app_password', ['default' => '', 'sanitize_callback' => 'sanitize_text_field']);
    $wp_customize->add_control('evergold_gmail_app_password', [
        'label' => 'Gmail app password (required for inquiry emails)',
        'description' => 'Google Account → Security → 2-Step Verification → App passwords. Create one for Mail and paste the 16-character password here. Inquiry forms then send through Gmail to miaspomeranian@gmail.com.',
        'section' => 'evergold_contact',
        'type' => 'password',
    ]);
}
add_action('customize_register', 'evergold_customize_register');
