/**
 * Sticky Header + Nav setup
 * Instead of relying on scroll events, this simply tracks the height of the banner
 * and sets a CSS variable `--banner-height` on the root.
 * The actual pinning is handled natively via CSS `position: sticky;` in `site-common.css`.
 */
(function () {
    const banner = document.getElementById('site-banner');
    if (!banner) return;

    function updateBannerHeight() {
        // Measure real height including borders/padding
        const h = banner.offsetHeight;
        document.documentElement.style.setProperty('--banner-height', `${h}px`);
    }

    // Set height on initial load
    updateBannerHeight();

    // Re-measure height on window resize
    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(updateBannerHeight, 100);
    });
})();
