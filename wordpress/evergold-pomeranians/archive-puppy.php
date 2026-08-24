<?php get_header(); ?>
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Meet the litter</p>
    <h1>Available Pomeranian puppies</h1>
    <p class="lead">Each puppy is raised in our home, vet-checked, and placed with a family that fits their temperament. Open a profile for owner photos, then order on WhatsApp or email. There is no website checkout. The current price is $1,250.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="grid grid-3">
      <?php if (have_posts()) : ?>
        <?php while (have_posts()) : the_post(); ?>
          <?php get_template_part('template-parts/puppy-card'); ?>
        <?php endwhile; ?>
      <?php endif; ?>
    </div>
  </div>
</section>
<?php get_footer(); ?>
