<?php get_header(); ?>
<?php while (have_posts()) : the_post(); ?>
<section class="page-hero">
  <div class="wrap article">
    <p class="eyebrow"><?php echo esc_html(get_the_date()); ?></p>
    <h1><?php the_title(); ?></h1>
    <?php $hero_img = get_post_meta(get_the_ID(), '_evergold_hero', true); ?>
    <?php if ($hero_img) : ?>
      <div class="article-hero"><img src="<?php echo esc_url($hero_img); ?>" alt="<?php the_title_attribute(); ?>"></div>
    <?php elseif (has_post_thumbnail()) : ?>
      <div class="article-hero"><?php the_post_thumbnail('large'); ?></div>
    <?php endif; ?>
    <?php the_content(); ?>
  </div>
</section>
<?php endwhile; ?>
<?php get_footer(); ?>
