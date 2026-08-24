<?php
get_header();
$photos = evergold_puppy_photos(get_the_ID());
$status = get_post_meta(get_the_ID(), '_evergold_status', true) ?: 'Available';
$color = get_post_meta(get_the_ID(), '_evergold_color', true);
$sex = get_post_meta(get_the_ID(), '_evergold_sex', true);
$age = get_post_meta(get_the_ID(), '_evergold_age', true);
$weight = get_post_meta(get_the_ID(), '_evergold_weight', true);
$price = get_post_meta(get_the_ID(), '_evergold_price', true);
$temperament = get_post_meta(get_the_ID(), '_evergold_temperament', true);
$pill = strtolower($status) === 'reserved' ? 'reserved' : 'available';
$available = strtolower($status) !== 'reserved';
$others = new WP_Query([
    'post_type' => 'puppy',
    'posts_per_page' => 3,
    'post__not_in' => [get_the_ID()],
]);
?>
<section class="page-hero">
  <div class="wrap puppy-hero">
    <div>
      <div class="frame">
        <?php if ($photos) : ?>
          <img src="<?php echo esc_url($photos[0]); ?>" alt="<?php the_title_attribute(); ?>">
        <?php endif; ?>
      </div>
      <?php if (count($photos) > 1) : ?>
        <div class="gallery">
          <?php foreach ($photos as $photo) : ?>
            <img src="<?php echo esc_url($photo); ?>" alt="<?php the_title_attribute(); ?> photo">
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </div>
    <div>
      <p class="eyebrow"><?php echo esc_html(trim($color . ' · ' . $sex, ' ·')); ?></p>
      <h1><?php the_title(); ?></h1>
      <div class="meta">
        <span class="pill <?php echo esc_attr($pill); ?>"><?php echo esc_html($status); ?></span>
        <?php if ($age) : ?><span class="pill"><?php echo esc_html($age); ?></span><?php endif; ?>
        <?php if ($weight) : ?><span class="pill"><?php echo esc_html($weight); ?></span><?php endif; ?>
      </div>
      <?php if ($price) : ?><div class="price"><?php echo esc_html($price); ?></div><?php endif; ?>
      <?php the_content(); ?>
      <div class="facts">
        <div class="fact"><span>Color</span><b><?php echo esc_html($color); ?></b></div>
        <div class="fact"><span>Sex</span><b><?php echo esc_html($sex); ?></b></div>
        <div class="fact"><span>Age</span><b><?php echo esc_html($age); ?></b></div>
        <div class="fact"><span>Weight</span><b><?php echo esc_html($weight); ?></b></div>
      </div>
      <?php if ($temperament) : ?><p><strong>Temperament:</strong> <?php echo esc_html($temperament); ?></p><?php endif; ?>
      <div class="btn-row">
        <?php if ($available) : ?>
          <a class="btn gold" href="<?php echo esc_url(add_query_arg('puppy', sanitize_title(get_the_title()), evergold_page_url('order'))); ?>">Order <?php the_title(); ?></a>
          <a class="btn" href="<?php echo esc_url(evergold_wa_url(get_the_title())); ?>" target="_blank" rel="noopener">WhatsApp</a>
        <?php else : ?>
          <a class="btn" href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">See other puppies</a>
        <?php endif; ?>
        <a class="btn ghost" href="tel:+<?php echo esc_attr(evergold_phone_tel()); ?>">Call <?php echo esc_html(evergold_phone()); ?></a>
      </div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap article">
    <h2>What <?php the_title(); ?> goes home with</h2>
    <ul>
      <li>Current vaccine and deworming record</li>
      <li>Vet wellness exam notes</li>
      <li>AKC registration application (where eligible)</li>
      <li>Two-year health agreement</li>
      <li>Starter food, blanket, and written care sheet</li>
    </ul>
    <p>Pickup is welcome by appointment. If you need delivery, see our <a href="<?php echo esc_url(evergold_page_url('shipping')); ?>">shipping and delivery information</a>.</p>
  </div>
</section>
<?php if ($others->have_posts()) : ?>
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Other puppies</h2><a class="btn ghost" href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">All puppies</a></div>
    <div class="grid grid-3">
      <?php
      while ($others->have_posts()) :
          $others->the_post();
          get_template_part('template-parts/puppy-card');
      endwhile;
      wp_reset_postdata();
      ?>
    </div>
  </div>
</section>
<?php endif; ?>
<?php get_footer(); ?>
