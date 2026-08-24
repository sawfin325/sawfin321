<?php
get_header();
$data = evergold_seed_data();
$puppies = new WP_Query([
    'post_type' => 'puppy',
    'posts_per_page' => 6,
    'orderby' => 'date',
    'order' => 'ASC',
]);
$hero = new WP_Query([
    'post_type' => 'puppy',
    'posts_per_page' => 18,
    'orderby' => 'date',
    'order' => 'ASC',
]);
$posts = new WP_Query([
    'post_type' => 'post',
    'posts_per_page' => 3,
]);
$topics = $data['topics'] ?? [];
?>
<section class="hero">
  <div class="hero-slides" aria-hidden="true">
    <?php
    $first = true;
    if ($hero->have_posts()) :
        while ($hero->have_posts()) :
            $hero->the_post();
            $photos = evergold_puppy_photos(get_the_ID());
            if (!$photos) {
                continue;
            }
            $class = $first ? ' class="is-active"' : '';
            $first = false;
            echo '<img' . $class . ' src="' . esc_url($photos[0]) . '" alt="' . esc_attr(get_the_title()) . '">';
        endwhile;
        wp_reset_postdata();
    endif;
    ?>
  </div>
  <div class="wrap hero-copy">
    <p class="eyebrow">Home-raised companions</p>
    <h1>Pomeranian puppies with golden hearts.</h1>
    <p>Evergold Pomeranians is a small family kennel producing healthy, well-socialized puppies with honest health records and lifelong support. Order on WhatsApp or email — this site does not take a card.</p>
    <div class="btn-row">
      <a class="btn gold" href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">See available puppies</a>
      <a class="btn ghost" href="<?php echo esc_url(evergold_page_url('order')); ?>" style="color:#fff;border-color:rgba(255,255,255,.35)">Order a puppy</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="frame"><img src="<?php echo esc_url(evergold_theme_uri('assets/images/products/jasper/jasper-3.jpg')); ?>" alt="Jasper the blue merle Pomeranian" loading="lazy"></div>
    <div>
      <p class="eyebrow">A quieter way to raise puppies</p>
      <h2>Raised underfoot, not in a barn.</h2>
      <p>Our puppies live in the house from day one. They hear kitchen sounds, meet visitors, learn crate naps, and leave with a start on potty habits, grooming, and confidence.</p>
      <?php echo wp_kses_post($data['home_story'] ?? ''); ?>
      <div class="stats">
        <div class="stat"><b>12+</b><span>years with the breed</span></div>
        <div class="stat"><b>AKC</b><span>registerable puppies</span></div>
        <div class="stat"><b>2 yr</b><span>health agreement</span></div>
      </div>
      <div class="btn-row">
        <a class="btn" href="<?php echo esc_url(evergold_page_url('solution')); ?>">Read our solution</a>
        <a class="btn ghost" href="<?php echo esc_url(evergold_page_url('order')); ?>">Order via WhatsApp or email</a>
      </div>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Current litter</p>
        <h2>Available Pomeranian puppies</h2>
      </div>
      <a class="btn ghost" href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">View all puppies</a>
    </div>
    <div class="grid grid-3">
      <?php
      if ($puppies->have_posts()) :
          while ($puppies->have_posts()) :
              $puppies->the_post();
              get_template_part('template-parts/puppy-card');
          endwhile;
          wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">From the first brush to the last treat</p>
        <h2>What every Evergold family receives</h2>
      </div>
    </div>
    <div class="grid grid-3">
      <article class="care-card">
        <p class="eyebrow">01</p>
        <h3>Health start</h3>
        <p>Vaccines, deworming, a vet exam, and a packet for your veterinarian.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">02</p>
        <h3>Go-home kit</h3>
        <p>Food, a littermate blanket, and a written first-week plan.</p>
      </article>
      <article class="care-card">
        <p class="eyebrow">03</p>
        <h3>Lifetime guidance</h3>
        <p>Coat, feeding, and travel questions after placement. Call <?php echo esc_html(evergold_phone()); ?>.</p>
      </article>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="home-topics">
      <div class="home-topics-photos">
        <?php foreach ($topics as $topic) : ?>
          <a class="topic-photo" href="<?php echo esc_url(home_url($topic['href_slug'])); ?>">
            <img src="<?php echo esc_url(evergold_theme_uri($topic['photo'])); ?>" alt="<?php echo esc_attr($topic['alt']); ?>" loading="lazy">
          </a>
        <?php endforeach; ?>
      </div>
      <div class="home-topics-copy">
        <p class="eyebrow">Ten more places to look</p>
        <h2>A card for each part of the Evergold path</h2>
        <?php foreach ($topics as $topic) : ?>
          <article class="topic-copy">
            <p class="eyebrow"><?php echo esc_html($topic['n']); ?></p>
            <h3><?php echo esc_html($topic['title']); ?></h3>
            <p><?php echo esc_html($topic['text']); ?></p>
            <a href="<?php echo esc_url(home_url($topic['href_slug'])); ?>">Read more</a>
          </article>
        <?php endforeach; ?>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Pomeranian journal</p>
        <h2>From the blog</h2>
      </div>
      <a class="btn ghost" href="<?php echo esc_url(evergold_page_url('blog')); ?>">Read more</a>
    </div>
    <div class="grid grid-3">
      <?php
      if ($posts->have_posts()) :
          while ($posts->have_posts()) :
              $posts->the_post();
              $hero_img = get_post_meta(get_the_ID(), '_evergold_hero', true);
              ?>
              <article class="post-card">
                <a class="media" href="<?php the_permalink(); ?>">
                  <?php if ($hero_img) : ?>
                    <img src="<?php echo esc_url($hero_img); ?>" alt="<?php the_title_attribute(); ?>" loading="lazy">
                  <?php elseif (has_post_thumbnail()) : ?>
                    <?php the_post_thumbnail('large'); ?>
                  <?php endif; ?>
                </a>
                <div class="body">
                  <p class="eyebrow"><?php echo esc_html(get_the_date()); ?></p>
                  <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
                </div>
              </article>
              <?php
          endwhile;
          wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>
<?php get_footer(); ?>
