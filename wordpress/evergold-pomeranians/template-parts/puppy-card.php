<?php
$photos = evergold_puppy_photos($post->ID);
$photo = $photos ? $photos[0] : '';
$status = get_post_meta($post->ID, '_evergold_status', true) ?: 'Available';
$color = get_post_meta($post->ID, '_evergold_color', true);
$sex = get_post_meta($post->ID, '_evergold_sex', true);
$price = get_post_meta($post->ID, '_evergold_price', true);
$temperament = get_post_meta($post->ID, '_evergold_temperament', true);
$pill = strtolower($status) === 'reserved' ? 'reserved' : 'available';
?>
<article class="puppy-card">
  <a href="<?php the_permalink(); ?>" class="media">
    <?php if ($photo) : ?>
      <img src="<?php echo esc_url($photo); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
    <?php endif; ?>
  </a>
  <div class="body">
    <div class="meta">
      <span class="pill <?php echo esc_attr($pill); ?>"><?php echo esc_html($status); ?></span>
      <?php if ($color) : ?><span class="pill"><?php echo esc_html($color); ?></span><?php endif; ?>
      <?php if ($sex) : ?><span class="pill"><?php echo esc_html($sex); ?></span><?php endif; ?>
    </div>
    <h3><?php the_title(); ?></h3>
    <p><?php echo esc_html($color ?: $temperament); ?></p>
    <?php if ($price) : ?><div class="price"><?php echo esc_html($price); ?></div><?php endif; ?>
    <a class="btn" href="<?php the_permalink(); ?>">View <?php the_title(); ?></a>
  </div>
</article>
