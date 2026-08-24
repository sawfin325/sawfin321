</main>
<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <p class="eyebrow">Ready to order a puppy?</p>
        <h2>Reserve with the inquiry form.</h2>
        <p>Submissions go to <?php echo esc_html(evergold_email()); ?>. We send videos, the health packet, and deposit instructions in writing. Call <?php echo esc_html(evergold_phone()); ?> if you want to talk first.</p>
      </div>
      <div class="btn-row">
        <a class="btn gold" href="<?php echo esc_url(evergold_page_url('order')); ?>">Inquiry form</a>
        <a class="btn ghost" href="<?php echo esc_url(evergold_wa_url()); ?>" target="_blank" rel="noopener" style="color:#fff;border-color:rgba(255,255,255,.25)">WhatsApp</a>
      </div>
    </div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h3>Evergold Pomeranians</h3>
      <p>Home-raised Pomeranian puppies with health testing, early socialization, and nationwide delivery support.</p>
      <p><a href="tel:+<?php echo esc_attr(evergold_phone_tel()); ?>"><?php echo esc_html(evergold_phone()); ?></a></p>
      <p><a href="<?php echo esc_url(evergold_mail_url()); ?>"><?php echo esc_html(evergold_email()); ?></a></p>
    </div>
    <div>
      <h3>Explore</h3>
      <ul>
        <li><a href="<?php echo esc_url(get_post_type_archive_link('puppy')); ?>">Available puppies</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('about-us')); ?>">About us</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('care-guide')); ?>">Care guide</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('solution')); ?>">Our solution</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('blog')); ?>">Blog</a></li>
      </ul>
    </div>
    <div>
      <h3>Families</h3>
      <ul>
        <li><a href="<?php echo esc_url(evergold_page_url('order')); ?>">Puppy inquiry form</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('shipping')); ?>">Shipping &amp; delivery</a></li>
        <li><a href="<?php echo esc_url(evergold_page_url('health')); ?>">Health &amp; vaccination</a></li>
      </ul>
    </div>
    <div>
      <h3>Visit</h3>
      <p>Inquiries daily 9am–6pm.<br>Puppy visits by appointment.</p>
    </div>
  </div>
  <div class="wrap copyright">© <?php echo esc_html(gmdate('Y')); ?> Evergold Pomeranians. All rights reserved.</div>
</footer>
<a class="wa-float" href="<?php echo esc_url(evergold_wa_url()); ?>" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>
<a class="call-bar" href="tel:+<?php echo esc_attr(evergold_phone_tel()); ?>">Call <?php echo esc_html(evergold_phone()); ?></a>
<?php wp_footer(); ?>
</body>
</html>
