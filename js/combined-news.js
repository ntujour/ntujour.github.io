document.addEventListener('DOMContentLoaded', () => {
    const tabs = Array.from(document.querySelectorAll('[data-news-archive-tab]'));
    const panels = Array.from(document.querySelectorAll('[data-news-archive-panel]'));

    if (tabs.length === 0 || panels.length === 0) return;

    const panelMap = new Map(panels.map((panel) => [panel.dataset.newsArchivePanel, panel]));

    function activateYear(year, syncHash = true) {
        const activePanel = panelMap.get(year);
        if (!activePanel) return;

        tabs.forEach((tab) => {
            const isActive = tab.dataset.newsArchiveTab === year;
            tab.classList.toggle('is-active', isActive);
            tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });

        panels.forEach((panel) => {
            panel.hidden = panel.dataset.newsArchivePanel !== year;
        });

        if (syncHash) {
            history.replaceState(null, '', `#year-${year}`);
        }
    }

    tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
            activateYear(tab.dataset.newsArchiveTab);
        });
    });

    const hashYear = window.location.hash.startsWith('#year-')
        ? window.location.hash.slice('#year-'.length)
        : '';
    const defaultYear = panelMap.has(hashYear)
        ? hashYear
        : tabs[0].dataset.newsArchiveTab;

    activateYear(defaultYear, Boolean(hashYear));
});
