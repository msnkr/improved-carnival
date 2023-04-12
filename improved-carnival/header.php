<?php get_header(); ?>

<?php get_sidebar(); ?>

<?php get_footer(); ?>

<?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>

<?php endwhile; else : ?>
    <p> <?php esc_html_e("Sorry. No posts match your criteria. "); ?></p>
<?php endif; ?>