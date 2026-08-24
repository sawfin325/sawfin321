<?php get_header(); ?>
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Missing page</p>
    <h1>We cannot find that page.</h1>
    <p class="lead">Try the puppy list, or send a WhatsApp or email order.</p>
    <div class="btn-row">
      <a class="btn gold" href="<?php echo esc_url(home_url('/')); ?>">Home</a>
      <a class="btn" href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">Puppies</a>
    </div>
  </div>
</section>
<?php get_footer(); ?>
