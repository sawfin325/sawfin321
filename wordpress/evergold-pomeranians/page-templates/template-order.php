<?php
/**
 * Template Name: Order via WhatsApp or email
 */
get_header();
$puppies = new WP_Query([
    'post_type' => 'puppy',
    'posts_per_page' => -1,
    'orderby' => 'title',
    'order' => 'ASC',
]);
?>
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">No website checkout</p>
    <h1>Order via WhatsApp or email</h1>
    <p class="lead">Choose the puppy, then send the order on WhatsApp or by email. We reply with videos, the health packet, and deposit instructions in writing.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap article">
    <?php
    while (have_posts()) :
        the_post();
        the_content();
    endwhile;
    ?>
    <label class="order-select">Puppy you want to order
      <select id="order-puppy">
        <option value="">A Pomeranian puppy</option>
        <?php
        if ($puppies->have_posts()) :
            while ($puppies->have_posts()) :
                $puppies->the_post();
                $status = get_post_meta(get_the_ID(), '_evergold_status', true) ?: 'Available';
                echo '<option value="' . esc_attr(get_the_title()) . '">' . esc_html(get_the_title() . ' (' . $status . ')') . '</option>';
            endwhile;
            wp_reset_postdata();
        endif;
        ?>
        <option value="Upcoming litter">Upcoming litter</option>
      </select>
    </label>
    <div class="order-grid">
      <a class="order-card whatsapp" id="order-whatsapp" href="<?php echo esc_url(evergold_wa_url()); ?>" target="_blank" rel="noopener">
        <p class="eyebrow">Fastest</p>
        <h2>Order on WhatsApp</h2>
        <p>Send a message to <?php echo esc_html(evergold_phone()); ?>. Ask for the latest video and reservation steps. We answer during 9am–6pm.</p>
        <span class="btn gold">Open WhatsApp</span>
      </a>
      <a class="order-card email" id="order-email" href="<?php echo esc_url(evergold_mail_url()); ?>">
        <p class="eyebrow">Written record</p>
        <h2>Order by email</h2>
        <p>Write <?php echo esc_html(evergold_email()); ?> with your city, the puppy name, and pickup or delivery.</p>
        <span class="btn">Open email</span>
      </a>
    </div>
    <p>Prefer a voice first? <a href="tel:+<?php echo esc_attr(evergold_phone_tel()); ?>">Call <?php echo esc_html(evergold_phone()); ?></a>, then send the written order so the reservation is on record.</p>
  </div>
</section>
<?php get_footer(); ?>
