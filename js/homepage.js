// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Load latest news and activities
    loadLatestNews();
    loadLatestActivities();
});

// Load latest news (first 3 items) from data/news.json (generated from news/_posts)
async function loadLatestNews() {
    const newsListElement = document.getElementById('news-list');

    try {
        const response = await fetch('data/news.json');
        if (!response.ok) {
            throw new Error('Failed to load news data');
        }
        const data = await response.json();
        const news = data
            .sort((a, b) => new Date(b.date) - new Date(a.date))
            .slice(0, 3)
            .map(item => ({
                id: item.id,
                title: (item.title || '').replace(/【.*?】/, '').trim(),
                excerpt: stripHTML(item.content || '').substring(0, 100),
                date: item.date,
                category: item.category || ''
            }));

        renderNewsCards(newsListElement, news, 'news');
    } catch (error) {
        console.error('Error loading news:', error);
        newsListElement.innerHTML = '<div class="text-center py-12 col-span-full text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load latest activities (first 3 items) from data/activities.json (generated from activities/_posts)
async function loadLatestActivities() {
    const activitiesListElement = document.getElementById('activities-list');

    try {
        const response = await fetch('data/activities.json');
        if (!response.ok) {
            throw new Error('Failed to load activities data');
        }
        const data = await response.json();
        const activities = data
            .sort((a, b) => new Date(b.date) - new Date(a.date))
            .slice(0, 3)
            .map(item => ({
                id: item.id,
                title: (item.title || '').replace(/【.*?】/, '').trim(),
                excerpt: stripHTML(item.content || '').substring(0, 100),
                date: item.date,
                category: item.category || '活動',
                time: item.time,
                location: item.location
            }));

        renderNewsCards(activitiesListElement, activities, 'activities');
    } catch (error) {
        console.error('Error loading activities:', error);
        activitiesListElement.innerHTML = '<div class="text-center py-12 col-span-full text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Render news/activity cards (links to article-view.html?type=...&id=...)
function renderNewsCards(container, items, type) {
    const cardsHTML = items.map(item => `
        <article class="bg-white border border-gray-200 rounded hover:shadow-md transition-shadow cursor-pointer" onclick="window.location.href='article-view.html?type=${type === 'news' ? 'news' : 'activity'}&id=${item.id}'">
            <div class="p-4">
                <div class="flex items-center gap-2 mb-2">
                    <span class="inline-block px-2 py-1 text-xs rounded bg-red-100 text-red-800">${item.category}</span>
                    <time class="text-xs text-gray-500">${formatDate(item.date)}</time>
                </div>
                <h3 class="text-base font-bold text-gray-900 mb-2 line-clamp-2">${item.title}</h3>
                <p class="text-sm text-gray-600 line-clamp-3">${item.excerpt}...（繼續閱讀）</p>
            </div>
        </article>
    `).join('');

    container.innerHTML = cardsHTML;
}

// Strip HTML tags from string
function stripHTML(html) {
    const tmp = document.createElement('div');
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || '';
}

// Format date to Chinese format
function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}年${month}月${day}日`;
}

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
