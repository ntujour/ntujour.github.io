document.addEventListener('DOMContentLoaded', async () => {
    const root = document.getElementById('activities-list');
    if (!root || !window.NTUJourNews) return;
    const esc = value => String(value || '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;');
    try {
        const activities = await window.NTUJourNews.loadIndex('zh', 'data/activities.json', 'activities');
        root.innerHTML = activities.map(item => {
            const tags = (item.hashtags || []).map(tag => `<span class="text-[11px] font-semibold text-ntu-maroon">${esc(tag)}</span>`).join('');
            return `<article class="bg-white rounded-3xl border border-neutral-100 shadow-soft hover:shadow-soft-lg transition-shadow cursor-pointer group"><a href="article-view.html?type=cloud-activity&amp;id=${encodeURIComponent(item.id)}" class="block h-full"><div class="p-6"><div class="flex items-center gap-2 mb-3"><time class="text-xs text-neutral-400">${esc(item.date)}</time>${tags}</div><h3 class="text-base font-normal text-neutral-900 mb-2 line-clamp-1 group-hover:text-ntu-maroon transition-colors">${esc(item.title)}</h3><p class="text-sm text-neutral-500 line-clamp-3">${esc(item.excerpt)}</p></div></a></article>`;
        }).join('') || '<div class="col-span-full text-center py-4 text-gray-500">暫無資料</div>';
    } catch (error) {
        console.warn('Keeping the built-in activities list.', error);
    }
});
