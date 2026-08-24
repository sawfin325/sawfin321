<?php
if (!defined('ABSPATH')) {
    exit;
}

function evergold_gmail_app_password() {
    return preg_replace('/\s+/', '', (string) get_theme_mod('evergold_gmail_app_password', ''));
}

function evergold_mail_from() {
    $email = evergold_email();
    if (evergold_gmail_app_password()) {
        return $email;
    }
    $host = wp_parse_url(home_url(), PHP_URL_HOST);
    $host = preg_replace('/^www\./', '', (string) $host);
    if ($host && !in_array($host, ['localhost', '127.0.0.1'], true) && strpos($host, '.') !== false) {
        return 'inquiries@' . $host;
    }
    return $email;
}

function evergold_mail_from_name() {
    return 'Evergold Pomeranians';
}

add_filter('wp_mail_from', 'evergold_mail_from');
add_filter('wp_mail_from_name', 'evergold_mail_from_name');

function evergold_phpmailer_smtp($phpmailer) {
    $password = evergold_gmail_app_password();
    if ($password === '') {
        return;
    }
    $phpmailer->isSMTP();
    $phpmailer->Host = 'smtp.gmail.com';
    $phpmailer->SMTPAuth = true;
    $phpmailer->Port = 587;
    $phpmailer->SMTPSecure = 'tls';
    $phpmailer->Username = evergold_email();
    $phpmailer->Password = $password;
    $phpmailer->From = evergold_email();
    $phpmailer->FromName = evergold_mail_from_name();
}
add_action('phpmailer_init', 'evergold_phpmailer_smtp');

function evergold_mail_failed($error) {
    $message = $error instanceof WP_Error ? $error->get_error_message() : 'WordPress could not send the email.';
    update_option('evergold_last_mail_error', $message);
}
add_action('wp_mail_failed', 'evergold_mail_failed');

function evergold_formsubmit_send($to, $subject, $body, $reply_email, $reply_name) {
    $response = wp_remote_post('https://formsubmit.co/ajax/' . rawurlencode($to), [
        'timeout' => 20,
        'headers' => [
            'Content-Type' => 'application/json',
            'Accept' => 'application/json',
        ],
        'body' => wp_json_encode([
            'name' => $reply_name,
            'email' => $reply_email,
            '_subject' => $subject,
            '_template' => 'box',
            'message' => $body,
        ]),
    ]);
    if (is_wp_error($response)) {
        return $response->get_error_message();
    }
    $code = wp_remote_retrieve_response_code($response);
    $json = json_decode(wp_remote_retrieve_body($response), true);
    if ($code >= 200 && $code < 300) {
        return true;
    }
    if (is_array($json) && !empty($json['message'])) {
        return (string) $json['message'];
    }
    return 'Backup email service returned HTTP ' . $code;
}

function evergold_send_inquiry_mail($to, $subject, $body, $reply_email, $reply_name) {
    delete_option('evergold_last_mail_error');
    $headers = [
        'Content-Type: text/plain; charset=UTF-8',
        'Reply-To: ' . $reply_name . ' <' . $reply_email . '>',
    ];
    $sent = wp_mail($to, $subject, $body, $headers);
    if ($sent) {
        update_option('evergold_last_mail_ok', gmdate('c'));
        delete_option('evergold_last_mail_error');
        return true;
    }

    $backup = evergold_formsubmit_send($to, $subject, $body, $reply_email, $reply_name);
    if ($backup === true) {
        update_option('evergold_last_mail_ok', gmdate('c') . ' (backup)');
        delete_option('evergold_last_mail_error');
        return true;
    }

    $error = get_option('evergold_last_mail_error', 'WordPress mail failed.');
    if (is_string($backup) && $backup !== '') {
        $error .= ' Backup: ' . $backup;
    }
    update_option('evergold_last_mail_error', $error);
    return false;
}

function evergold_inquiry_admin_notice() {
    if (!current_user_can('manage_options')) {
        return;
    }
    $screen = function_exists('get_current_screen') ? get_current_screen() : null;
    $id = $screen ? (string) $screen->id : '';
    $on_mail_screen = in_array($id, ['dashboard', 'themes', 'edit-evergold_inquiry', 'evergold_inquiry'], true) || strpos($id, 'evergold_inquiry') !== false;
    if (!$on_mail_screen) {
        return;
    }
    $error = get_option('evergold_last_mail_error');
    if ($error) {
        echo '<div class="notice notice-error"><p><strong>Evergold inquiry email failed.</strong> ' . esc_html($error) . ' Add a Gmail app password under <a href="' . esc_url(admin_url('customize.php?autofocus[section]=evergold_contact')) . '">Appearance → Customize → Evergold contact</a>. Submissions are still saved under Inquiries.</p></div>';
        return;
    }
    if (evergold_gmail_app_password() === '' && strpos($id, 'evergold_inquiry') !== false) {
        echo '<div class="notice notice-warning"><p>To receive inquiry emails in Gmail, add a <strong>Gmail app password</strong> under <a href="' . esc_url(admin_url('customize.php?autofocus[section]=evergold_contact')) . '">Appearance → Customize → Evergold contact</a>. Google Account → Security → 2-Step Verification → App passwords.</p></div>';
    }
}
add_action('admin_notices', 'evergold_inquiry_admin_notice');
