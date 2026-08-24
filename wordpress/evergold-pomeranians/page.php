<?php get_header(); ?>
<?php while (have_posts()) : the_post(); ?>
  <?php if (trim(get_the_content())) : ?>
    <?php the_content(); ?>
  <?php else : ?>
    <section class="page-hero">
      <div class="wrap">
        <h1><?php the_title(); ?></h1>
      </div>
    </section>
  <?php endif; ?>
<?php endwhile; ?>
<?php get_footer(); ?>
