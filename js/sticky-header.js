/**
 * Sticky Header + Nav setup
 * Instead of relying on scroll events, this simply tracks the height of the banner
 * and sets a CSS variable `--banner-height` on the root.
 * The actual pinning is handled natively via CSS `position: sticky;` in `site-common.css`.
 */
(function () {
    const banner = document.getElementById('site-banner');
    const siteNav = document.getElementById('site-nav');
    const pageHeader = document.getElementById('page-header');

    if (!banner && !siteNav && !pageHeader) return;

    function updateStickyMetrics() {
        const bannerHeight = banner ? banner.offsetHeight : 0;
        const siteNavHeight = siteNav ? siteNav.offsetHeight : 0;
        const pageHeaderHeight = pageHeader ? pageHeader.offsetHeight : 0;

        document.documentElement.style.setProperty('--banner-height', `${bannerHeight}px`);
        document.documentElement.style.setProperty('--site-nav-height', `${siteNavHeight}px`);
        document.documentElement.style.setProperty('--page-header-height', `${pageHeaderHeight}px`);
        document.documentElement.style.setProperty(
            '--sticky-stack-offset',
            `${bannerHeight + siteNavHeight + pageHeaderHeight}px`
        );
    }

    updateStickyMetrics();

    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(updateStickyMetrics, 100);
    });
})();
