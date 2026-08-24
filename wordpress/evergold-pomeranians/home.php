<?php get_header(); ?>
<?php
$card = isset($_GET['card']) ? absint($_GET['card']) : 0;
if ($card) :
    ?>
    <section class="page-hero">
      <div class="wrap article">
        <p class="eyebrow" id="entry-date">Kennel archive</p>
        <h1 id="entry-title">Archive article</h1>
        <div class="article-hero" id="entry-hero"></div>
        <div id="entry-body"></div>
        <div class="btn-row">
          <a class="btn gold" href="<?php echo esc_url(evergold_page_url('order')); ?>">Order via WhatsApp or email</a>
          <a class="btn ghost" href="<?php echo esc_url(evergold_page_url('blog')); ?>">Back to 5,000 cards</a>
        </div>
      </div>
    </section>
    <?php
else :
    ?>
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">Notes from the kennel</p>
        <h1>Pomeranian blog</h1>
        <p class="lead">Featured guides, plus a 5,000-card kennel archive you can browse by page.</p>
      </div>
    </section>
    <section class="section" style="padding-top:0">
      <div class="wrap">
        <div class="section-head"><h2>Featured guides</h2></div>
        <div class="grid grid-2">
          <?php if (have_posts()) : ?>
            <?php while (have_posts()) : the_post(); ?>
              <?php $hero_img = get_post_meta(get_the_ID(), '_evergold_hero', true); ?>
              <article class="post-card">
                <a class="media" href="<?php the_permalink(); ?>">
                  <?php if ($hero_img) : ?>
                    <img src="<?php echo esc_url($hero_img); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
                  <?php endif; ?>
                </a>
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
      </div>
    </section>
    <section class="section alt">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">Kennel archive</p>
            <h2>5,000 blog cards</h2>
          </div>
          <p id="blog-count" class="lead" style="margin:0">Loading archive…</p>
        </div>
        <div id="blog-archive" class="grid grid-3"></div>
        <div class="blog-pager" id="blog-pager"></div>
      </div>
    </section>
    <?php
endif;
?>
<?php get_footer(); ?>
