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

// Load latest news (first 3 items)
async function loadLatestNews() {
    const newsListElement = document.getElementById('news-list');

    try {
        // Fetch real data from CSV
        const response = await fetch('data/content.csv');
        if (!response.ok) {
            throw new Error('Failed to load news data');
        }

        const csvText = await response.text();
        const allContent = parseCSV(csvText);

        // Filter news items, sort by date (newest first), take first 3
        const news = allContent
            .filter(item => item.type === 'news')
            .sort((a, b) => new Date(b.date) - new Date(a.date))
            .slice(0, 3)
            .map(item => ({
                id: item.id,
                title: item.title.replace(/【.*?】/, '').trim(), // Remove category prefix
                excerpt: stripHTML(item.content).substring(0, 100),
                date: item.date,
                category: item.category,
                slug: item.originalFile || `News_Content_n_35497_s_${item.id}.html`
            }));

        renderNewsCards(newsListElement, news, 'news');
    } catch (error) {
        console.error('Error loading news:', error);
        newsListElement.innerHTML = '<div class="text-center py-12 col-span-full text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load latest activities (first 3 items)
async function loadLatestActivities() {
    const activitiesListElement = document.getElementById('activities-list');

    try {
        // Fetch real data from CSV
        const response = await fetch('data/content.csv');
        if (!response.ok) {
            throw new Error('Failed to load activities data');
        }

        const csvText = await response.text();
        const allContent = parseCSV(csvText);

        // Filter activity items, sort by date (newest first), take first 3
        const activities = allContent
            .filter(item => item.type === 'activity')
            .sort((a, b) => new Date(b.date) - new Date(a.date))
            .slice(0, 3)
            .map(item => ({
                id: item.id,
                title: item.title.replace(/【.*?】/, '').trim(), // Remove category prefix
                excerpt: stripHTML(item.content).substring(0, 100),
                date: item.date,
                category: item.category || '活動',
                time: item.time,
                location: item.location,
                slug: item.originalFile || `News_Content_n_35498_s_${item.id}.html`
            }));

        renderNewsCards(activitiesListElement, activities, 'activities');
    } catch (error) {
        console.error('Error loading activities:', error);
        activitiesListElement.innerHTML = '<div class="text-center py-12 col-span-full text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Render news/activity cards
function renderNewsCards(container, items, type) {
    const folder = type === 'news' ? 'news' : 'activities';

    const cardsHTML = items.map(item => `
        <article class="bg-white border border-gray-200 rounded hover:shadow-md transition-shadow cursor-pointer" onclick="window.location.href='${folder}/${item.slug}'">
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

// CSV Parser (inline for simplicity)
function parseCSV(csvText) {
    const lines = csvText.split('\n');
    const headers = lines[0].split(',').map(h => h.trim());
    const data = [];

    for (let i = 1; i < lines.length; i++) {
        if (!lines[i].trim()) continue;

        const values = parseCSVLine(lines[i]);
        if (values.length === headers.length) {
            const obj = {};
            headers.forEach((header, index) => {
                obj[header] = values[index];
            });
            data.push(obj);
        }
    }

    return data;
}

function parseCSVLine(line) {
    const values = [];
    let current = '';
    let inQuotes = false;

    for (let i = 0; i < line.length; i++) {
        const char = line[i];

        if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            values.push(current.trim());
            current = '';
        } else {
            current += char;
        }
    }

    values.push(current.trim());
    return values;
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
