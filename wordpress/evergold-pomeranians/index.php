<?php get_header(); ?>
<section class="page-hero">
  <div class="wrap">
    <h1><?php echo wp_kses_post(get_the_archive_title()); ?></h1>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap grid grid-2">
    <?php if (have_posts()) : ?>
      <?php while (have_posts()) : the_post(); ?>
        <article class="post-card">
          <div class="body">
            <p class="eyebrow"><?php echo esc_html(get_the_date()); ?></p>
            <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
            <p><?php echo esc_html(get_the_excerpt()); ?></p>
            <a class="btn ghost" href="<?php the_permalink(); ?>">Read article</a>
          </div>
        </article>
      <?php endwhile; ?>
    <?php endif; ?>
  </div>
</section>
<?php get_footer(); ?>
