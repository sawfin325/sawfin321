<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_register_inquiry_cpt() {
    register_post_type('evergold_inquiry', [
        'labels' => [
            'name' => 'Inquiries',
            'singular_name' => 'Inquiry',
        ],
        'public' => false,
        'show_ui' => true,
        'show_in_menu' => true,
        'menu_icon' => 'dashicons-email-alt',
        'supports' => ['title', 'editor'],
        'capability_type' => 'post',
    ]);
}
add_action('init', 'evergold_register_inquiry_cpt');

function evergold_inquiry_wanted_puppy() {
    return isset($_GET['puppy']) ? sanitize_text_field(wp_unslash($_GET['puppy'])) : '';
}

function evergold_inquiry_puppy_selected($name, $slug, $wanted) {
    $wanted = strtolower(trim((string) $wanted));
    if ($wanted === '') {
        return false;
    }
    return $wanted === strtolower($name) || $wanted === strtolower($slug);
}

function evergold_handle_inquiry() {
    $order_url = evergold_page_url('order');

    if (!isset($_POST['evergold_inquiry_nonce']) || !wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['evergold_inquiry_nonce'])), 'evergold_inquiry')) {
        wp_safe_redirect(add_query_arg('inquiry', 'error', $order_url));
        exit;
    }

    if (!empty($_POST['pets_name'])) {
        wp_safe_redirect(add_query_arg('inquiry', 'sent', $order_url));
        exit;
    }

    $first = sanitize_text_field(wp_unslash($_POST['first_name'] ?? ''));
    $last = sanitize_text_field(wp_unslash($_POST['last_name'] ?? ''));
    $phone = sanitize_text_field(wp_unslash($_POST['phone'] ?? ''));
    $email = sanitize_email(wp_unslash($_POST['email'] ?? ''));
    $location = sanitize_text_field(wp_unslash($_POST['location'] ?? ''));
    $puppy = sanitize_text_field(wp_unslash($_POST['puppy'] ?? ''));
    $living = sanitize_text_field(wp_unslash($_POST['living'] ?? ''));
    $other_pets = sanitize_text_field(wp_unslash($_POST['other_pets'] ?? ''));
    $delivery = sanitize_text_field(wp_unslash($_POST['delivery'] ?? ''));
    $when = sanitize_text_field(wp_unslash($_POST['when'] ?? ''));
    $message = sanitize_textarea_field(wp_unslash($_POST['message'] ?? ''));

    if ($first === '' || $last === '' || $phone === '' || !is_email($email) || $location === '' || $puppy === '' || $living === '' || $other_pets === '' || $delivery === '' || $when === '' || $message === '') {
        wp_safe_redirect(add_query_arg('inquiry', 'missing', $order_url));
        exit;
    }

    $full_name = trim($first . ' ' . $last);
    $lines = [
        'A new Evergold puppy inquiry was submitted from the website.',
        '',
        'Full name: ' . $full_name,
        'Phone: ' . $phone,
        'Email: ' . $email,
        'Location: ' . $location,
        'Puppy: ' . $puppy,
        'Living situation: ' . $living,
        'Other pets: ' . $other_pets,
        'Pickup or delivery: ' . $delivery,
        'Timeline: ' . $when,
        '',
        'Message:',
        $message,
    ];
    $body = implode("\n", $lines);
    $subject = 'Puppy inquiry: ' . $puppy . ' from ' . $full_name;

    wp_insert_post([
        'post_type' => 'evergold_inquiry',
        'post_status' => 'private',
        'post_title' => $full_name . ' — ' . $puppy,
        'post_content' => $body . "\n\nSubmitted: " . gmdate('Y-m-d H:i:s') . ' UTC',
    ]);

    $headers = [
        'Content-Type: text/plain; charset=UTF-8',
        'Reply-To: ' . $full_name . ' <' . $email . '>',
    ];
    wp_mail(evergold_email(), $subject, $body, $headers);

    wp_safe_redirect(add_query_arg('inquiry', 'sent', $order_url));
    exit;
}
add_action('admin_post_nopriv_evergold_inquiry', 'evergold_handle_inquiry');
add_action('admin_post_evergold_inquiry', 'evergold_handle_inquiry');

function evergold_refresh_order_copy() {
    if (get_option('evergold_inquiry_copy')) {
        return;
    }
    $page = get_page_by_path('order');
    if ($page) {
        wp_update_post([
            'ID' => $page->ID,
            'post_content' => '<p>Submit the inquiry form above and the message is delivered to ' . esc_html(evergold_email()) . '. We reply with videos, the health packet, and deposit instructions in writing. If you want to talk first, call ' . esc_html(evergold_phone()) . '.</p><p>We answer inquiries from 9am to 6pm. Puppy visits are by appointment so the litter can rest.</p>',
        ]);
    }
    update_option('evergold_inquiry_copy', 1);
}
add_action('init', 'evergold_refresh_order_copy', 30);

function evergold_inquiry_notice() {
    $status = isset($_GET['inquiry']) ? sanitize_key(wp_unslash($_GET['inquiry'])) : '';
    if ($status === 'sent') {
        return '<div class="inquiry-notice is-success" role="status">Thank you. Your puppy inquiry was sent to ' . esc_html(evergold_email()) . '. We will contact you shortly with the next steps.</div>';
    }
    if ($status === 'missing') {
        return '<div class="inquiry-notice is-error" role="alert">Please fill every required field, including a valid email address, then submit again.</div>';
    }
    if ($status === 'error') {
        return '<div class="inquiry-notice is-error" role="alert">The form could not be submitted. Please try again, or email ' . esc_html(evergold_email()) . ' directly.</div>';
    }
    return '';
}
