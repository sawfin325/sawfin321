<?php
/**
 * Template Name: Order via inquiry form
 */
get_header();
$puppies = new WP_Query([
    'post_type' => 'puppy',
    'posts_per_page' => -1,
    'orderby' => 'title',
    'order' => 'ASC',
]);
$wanted = evergold_inquiry_wanted_puppy();
?>
<section class="inquiry-hero">
  <div class="wrap">
    <h1><span class="inquiry-paw" aria-hidden="true">🐾</span> Welcome Your New Companion <span class="inquiry-paw" aria-hidden="true">🐾</span></h1>
    <p>We are excited to help you find the perfect Pomeranian puppy for your family. Please fill out the form below with your information and puppy preference, and we will contact you shortly with the next steps.</p>
  </div>
</section>
<section class="inquiry-section">
  <div class="wrap">
    <?php echo evergold_inquiry_notice(); ?>
    <form class="inquiry-box" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="evergold_inquiry">
      <?php wp_nonce_field('evergold_inquiry', 'evergold_inquiry_nonce'); ?>
      <div class="inquiry-hp" aria-hidden="true">
        <label>Name pets? your
          <input type="text" name="pets_name" tabindex="-1" autocomplete="off">
        </label>
      </div>
      <div class="inquiry-field">
        <span class="inquiry-label">Full Name <span class="inquiry-req">*</span></span>
        <div class="inquiry-name">
          <label> <input type="text" name="first_name" required autocomplete="given-name"> <span class="inquiry-sub">First</span></label>
          <label> <input type="text" name="last_name" required autocomplete="family-name"> <span class="inquiry-sub">Last</span></label>
        </div>
      </div>
      <label class="inquiry-field">
        <span class="inquiry-label">Phone Number <span class="inquiry-req">*</span></span>
        <input type="tel" name="phone" required autocomplete="tel">
      </label>
      <label class="inquiry-field">
        <span class="inquiry-label">Email <span class="inquiry-req">*</span></span>
        <input type="email" name="email" required autocomplete="email">
      </label>
      <label class="inquiry-field">
        <span class="inquiry-label">Location <span class="inquiry-req">*</span></span>
        <input type="text" name="location" required autocomplete="address-level2">
      </label>
      <label class="inquiry-field">
        <span class="inquiry-label">Select Your Puppy <span class="inquiry-req">*</span></span>
        <select id="inquiry-puppy" name="puppy" required>
          <option value="">--- Select Choice ---</option>
          <?php
          if ($puppies->have_posts()) :
              while ($puppies->have_posts()) :
                  $puppies->the_post();
                  $name = get_the_title();
                  $sel = evergold_inquiry_puppy_selected($name, get_post_field('post_name'), $wanted) ? ' selected' : '';
                  echo '<option value="' . esc_attr($name) . '"' . $sel . '>' . esc_html($name) . '</option>';
              endwhile;
              wp_reset_postdata();
          endif;
          ?>
          <option value="Upcoming litter"<?php echo evergold_inquiry_puppy_selected('Upcoming litter', 'upcoming-litter', $wanted) ? ' selected' : ''; ?>>Upcoming litter</option>
        </select>
      </label>
      <label class="inquiry-field">
        <span class="inquiry-label">Living Situation <span class="inquiry-req">*</span></span>
        <select name="living" required>
          <option value="">--- Select Choice ---</option>
          <option value="Appartment">Appartment</option>
          <option value="House with small yard">House with small yard</option>
          <option value="House with big yard">House with big yard</option>
          <option value="Farm/Acreage">Farm/Acreage</option>
        </select>
      </label>
      <fieldset class="inquiry-field">
        <legend class="inquiry-label">Do you have other pets? <span class="inquiry-req">*</span></legend>
        <div class="inquiry-radios">
          <label><input type="radio" name="other_pets" value="No" required> No</label>
          <label><input type="radio" name="other_pets" value="Yes"> Yes</label>
        </div>
      </fieldset>
      <fieldset class="inquiry-field">
        <legend class="inquiry-label">How would you like to get your puppy? <span class="inquiry-req">*</span></legend>
        <div class="inquiry-radios">
          <label><input type="radio" name="delivery" value="Pickup" required> Pickup</label>
          <label><input type="radio" name="delivery" value="Delivery"> Delivery</label>
        </div>
      </fieldset>
      <fieldset class="inquiry-field">
        <legend class="inquiry-label">When would you like to have the puppy? <span class="inquiry-req">*</span></legend>
        <div class="inquiry-radios">
          <label><input type="radio" name="when" value="Right away" required> Right away</label>
          <label><input type="radio" name="when" value="Within a week"> Within a week</label>
          <label><input type="radio" name="when" value="Not certain"> Not certain</label>
          <label><input type="radio" name="when" value="Just looking"> Just looking</label>
        </div>
      </fieldset>
      <label class="inquiry-field">
        <span class="inquiry-label">Message <span class="inquiry-req">*</span></span>
        <textarea name="message" rows="6" required></textarea>
      </label>
      <button class="inquiry-submit" type="submit">Submit</button>
    </form>
    <p class="inquiry-home-line">HOME IS WHERE THE DOG IS</p>
  </div>
</section>
<section class="section">
  <div class="wrap article">
    <?php
    while (have_posts()) :
        the_post();
        the_content();
    endwhile;
    ?>
    <div class="order-grid">
      <a class="order-card whatsapp" id="order-whatsapp" href="<?php echo esc_url(evergold_wa_url()); ?>" target="_blank" rel="noopener">
        <p class="eyebrow">Also available</p>
        <h2>WhatsApp</h2>
        <p>Message <?php echo esc_html(evergold_phone()); ?> if you want a faster video reply after you submit the form.</p>
        <span class="btn gold">Open WhatsApp</span>
      </a>
      <a class="order-card email" id="order-email" href="<?php echo esc_url(evergold_mail_url()); ?>">
        <p class="eyebrow">Direct line</p>
        <h2>Email</h2>
        <p>Inquiries from this form are sent to <?php echo esc_html(evergold_email()); ?>. You can also write that address yourself.</p>
        <span class="btn">Open email</span>
      </a>
    </div>
  </div>
</section>
<?php get_footer(); ?>
