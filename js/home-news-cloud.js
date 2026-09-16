document.addEventListener('DOMContentLoaded', async () => {
    const root = document.getElementById('news-list');
    const activityRoot = document.getElementById('activities-list');
    if ((!root && !activityRoot) || !window.NTUJourNews) return;
    const esc = value => String(value || '').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;');
    try {
        const [news, activities] = await Promise.all([
            window.NTUJourNews.loadIndex('zh', 'data/news.json'),
            window.NTUJourNews.loadIndex('zh', 'data/activities.json', 'activities'),
        ]);
        if (root) root.innerHTML = news.slice(0, 6).map(item => {
            const image = item.image ? `<div class="home-list-thumb"><img src="${esc(item.image)}" alt="${esc(item.title)}" class="w-full" loading="lazy"></div>` : '';
            const tags = (item.hashtags || []).map(tag => `<span class="text-[11px] font-semibold text-ntu-maroon">${esc(tag)}</span>`).join('');
            return `<article class="home-news-item${item.image ? ' has-thumb' : ''}"><a href="article-view.html?type=cloud-news&amp;id=${encodeURIComponent(item.id)}">${image}<div class="home-list-copy"><div class="home-list-topline"><time>${esc(item.date)}</time><span class="inline-flex flex-wrap items-center gap-x-2 gap-y-0.5">${tags}</span></div><div><h3>${esc(item.title)}</h3><p class="home-news-excerpt">${esc(item.excerpt)}</p></div></div></a></article>`;
        }).join('') || '<div class="news-archive-empty">目前沒有消息</div>';
        if (activityRoot) activityRoot.innerHTML = activities.slice(0, 6).map(item => {
            const image = item.image ? `<div class="home-list-thumb"><img src="${esc(item.image)}" alt="${esc(item.title)}" class="w-full" loading="lazy"></div>` : '';
            const tags = (item.hashtags || []).map(tag => `<span class="front-hashtag">${esc(tag)}</span>`).join('');
            return `<article class="home-activity-item${item.image ? ' has-thumb' : ''}"><a href="article-view.html?type=cloud-activity&amp;id=${encodeURIComponent(item.id)}">${image}<div class="home-list-copy"><div class="home-list-topline"><time>${esc(item.date)}</time><span class="front-hashtags">${tags}</span></div><div><h3>${esc(item.title)}</h3><p class="home-activity-excerpt">${esc(item.excerpt)}</p></div></div></a></article>`;
        }).join('') || '<div class="news-archive-empty">目前沒有活動</div>';
    } catch (error) {
        console.warn('Keeping the built-in homepage news.', error);
    }
});
