document.addEventListener('DOMContentLoaded', async () => {
    const root = document.getElementById('news-archive-root');
    if (!root) return;
    const esc = value => String(value || '').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;');
    const yearOf = item => /^\d{4}/.test(item.date || '') ? item.date.slice(0, 4) : '未分類';

    function tagsHtml(item) {
        return (item.hashtags || []).map(tag => `<span class="front-hashtag">${esc(tag)}</span>`).join('');
    }
    function newsItem(item) {
        return `<article class="home-news-item"><a href="article-view.html?type=cloud-news&amp;id=${encodeURIComponent(item.id)}"><div class="home-list-copy"><div class="home-list-topline"><time>${esc(item.date)}</time><span class="front-hashtags">${tagsHtml(item)}</span></div><div><h3>${esc(item.title)}</h3><p class="home-news-excerpt">${esc(item.excerpt)}</p></div></div></a></article>`;
    }
    function activityItem(item) {
        return `<article class="home-activity-item"><a href="article-view.html?type=cloud-activity&amp;id=${encodeURIComponent(item.id)}"><div class="home-list-copy"><div class="home-list-topline"><time>${esc(item.date)}</time><span class="front-hashtags">${tagsHtml(item)}</span></div><div><h3>${esc(item.title)}</h3><p class="home-activity-excerpt">${esc(item.excerpt)}</p></div></div></a></article>`;
    }
    function empty(label) { return `<div class="news-archive-empty">${label}</div>`; }
    function renderArchive(news, activities) {
        const years = [...new Set([...news, ...activities].map(yearOf))].sort((a,b) => b.localeCompare(a));
        const tabs = years.map((year, i) => `<button class="news-archive-tab${i ? '' : ' is-active'}" type="button" role="tab" aria-selected="${i ? 'false' : 'true'}" aria-controls="news-archive-panel-${year}" id="news-archive-tab-${year}" data-news-archive-tab="${year}">${year}</button>`).join('');
        const panels = years.map((year, i) => {
            const yearNews = news.filter(item => yearOf(item) === year).map(newsItem).join('') || empty('本年暫無最新消息');
            const yearActivities = activities.filter(item => yearOf(item) === year).map(activityItem).join('') || empty('本年暫無活動資訊');
            return `<section class="news-archive-panel" id="news-archive-panel-${year}" role="tabpanel" aria-labelledby="news-archive-tab-${year}" data-news-archive-panel="${year}"${i ? ' hidden' : ''}><div class="home-columns-shell"><div class="home-columns"><div class="home-panel"><div class="home-panel-header"><div class="home-panel-heading"><h2>最新消息</h2><p>NEWS</p></div></div><div class="home-news-list">${yearNews}</div></div><div class="home-panel"><div class="home-panel-header"><div class="home-panel-heading"><h2>活動資訊</h2><p>EVENTS</p></div></div><div class="home-activities-list">${yearActivities}</div></div></div></div></section>`;
        }).join('');
        root.innerHTML = `<div class="news-archive-shell"><div class="news-archive-tabs" role="tablist" aria-label="年份">${tabs}</div><div class="news-archive-panels">${panels}</div></div>`;
    }
    function activateTabs() {
        const tabs = [...document.querySelectorAll('[data-news-archive-tab]')];
        const panels = [...document.querySelectorAll('[data-news-archive-panel]')];
        if (!tabs.length || !panels.length) return;
        const map = new Map(panels.map(panel => [panel.dataset.newsArchivePanel, panel]));
        const activate = (year, syncHash = true) => {
            if (!map.has(year)) return;
            tabs.forEach(tab => { const active = tab.dataset.newsArchiveTab === year; tab.classList.toggle('is-active', active); tab.setAttribute('aria-selected', String(active)); });
            panels.forEach(panel => { panel.hidden = panel.dataset.newsArchivePanel !== year; });
            if (syncHash) history.replaceState(null, '', `#year-${year}`);
        };
        tabs.forEach(tab => tab.addEventListener('click', () => activate(tab.dataset.newsArchiveTab)));
        const hashYear = location.hash.startsWith('#year-') ? location.hash.slice(6) : '';
        activate(map.has(hashYear) ? hashYear : tabs[0].dataset.newsArchiveTab, Boolean(hashYear));
    }
    try {
        const [news, activities] = await Promise.all([
            window.NTUJourNews.loadIndex('zh', 'data/news.json'),
            window.NTUJourNews.loadIndex('zh', 'data/activities.json', 'activities')
        ]);
        renderArchive(news, activities);
    } catch (error) {
        console.warn('Keeping the built-in news archive.', error);
    }
    activateTabs();
});
