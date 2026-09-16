// Article view page JavaScript

document.addEventListener('DOMContentLoaded', async function() {
    const urlParams = new URLSearchParams(window.location.search);
    const type = urlParams.get('type'); // 'news' or 'activity'
    const id = urlParams.get('id');

    if (!type || !id) {
        showError('無效的文章參數');
        return;
    }

    await loadArticle(type, id);
});

async function loadArticle(type, id) {
    try {
        if (type === 'cloud-news') {
            const article = await window.NTUJourNews.loadDetail('zh', id, 'data/news.json');
            document.getElementById('breadcrumb-category').innerHTML = '<a href="news.html" class="hover:text-gray-900">最新消息</a>';
            document.title = article.title + ' - 國立臺灣大學新聞研究所';
            displayArticle(article, 'news');
            return;
        }
        if (type === 'cloud-activity') {
            const article = await window.NTUJourNews.loadDetail('zh', id, 'data/activities.json');
            document.getElementById('breadcrumb-category').innerHTML = '<a href="activities.html" class="hover:text-gray-900">活動資訊</a>';
            document.title = article.title + ' - 國立臺灣大學新聞研究所';
            displayArticle(article, 'activity');
            return;
        }
        const filename = type === 'news' ? 'data/news.json' : 'data/activities.json';
        const response = await fetch(filename);
        const articles = await response.json();

        const article = articles.find(item => item.id === id);

        if (!article) {
            showError('找不到文章');
            return;
        }

        // Update breadcrumb
        const breadcrumb = document.getElementById('breadcrumb-category');
        const categoryText = type === 'news' ? '最新消息' : '活動資訊';
        const categoryLink = type === 'news' ? 'news.html' : 'activities.html';
        breadcrumb.innerHTML = `<a href="${categoryLink}" class="hover:text-gray-900">${categoryText}</a>`;

        // Update page title
        document.title = article.title + ' - 國立臺灣大學新聞研究所';

        // Display article
        displayArticle(article, type);
    } catch (error) {
        console.error('Error loading article:', error);
        showError('載入文章時發生錯誤');
    }
}

function displayArticle(article, type) {
    const container = document.getElementById('article-content');
    const hashtags = renderHashtags(article.hashtags);
    const mediumLink = renderMediumLink(article.external_url);
    const coverImage = renderArticleCover(article);
    const galleryImages = renderArticleGallery(article);

    let extraInfo = '';
    if (type === 'activity' && (article.time || article.location)) {
        extraInfo = '<div class="activity-info-box">';
        if (article.time) {
            extraInfo += `<p class="text-base text-gray-700 mb-2"><strong>時間：</strong>${article.time}</p>`;
        }
        if (article.location) {
            extraInfo += `<p class="text-base text-gray-700"><strong>地點：</strong>${article.location}</p>`;
        }
        extraInfo += '</div>';
    }

    container.innerHTML = `
        <div class="article-meta">
            <h1>${article.title}</h1>
            <div class="flex items-center gap-4 text-sm text-gray-500">
                <span>發布日期：${formatDate(article.date)}</span>
                ${hashtags}
            </div>
        </div>

        ${mediumLink}
        ${coverImage}

        ${extraInfo}

        <div class="article-body">
            ${article.content}
        </div>

        ${galleryImages}
    `;
}

function renderArticleCover(article) {
    const coverImage = String(article.image || '').trim();
    if (!coverImage) return '';
    return `
        <figure class="article-cover-container group">
            <div class="article-cover-inner">
                ${renderCroppedImage(coverImage, article.title || '', article.image_crop, 'article-cover-img')}
            </div>
        </figure>
    `;
}

function renderArticleGallery(article) {
    const coverImage = String(article.image || '').trim();
    const gallery = (Array.isArray(article.gallery_images) ? article.gallery_images : [])
        .map((value) => String(value || '').trim())
        .filter((value) => value && value !== coverImage);
    if (!gallery.length) return '';
    return `
        <section class="article-gallery clear-both mt-8 mb-8 border-t border-neutral-200 pt-6">
            <h2 class="mb-4 text-lg font-bold text-neutral-900">相關照片</h2>
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                ${gallery.map((src) => `
                    <figure class="article-gallery-item">
                        ${renderCroppedImage(src, article.title || '', getGalleryCrop(article, src), 'content-image')}
                    </figure>
                `).join('')}
            </div>
        </section>
    `;
}

function renderMediumLink(url) {
    const href = String(url || '').trim();
    if (!isMediumUrl(href)) return '';
    return `
        <div class="article-external-link mb-6">
            <a href="${escapeHtml(href)}" target="_blank" rel="noreferrer" class="inline-flex items-center gap-2 border border-neutral-300 px-4 py-2 text-sm font-medium text-neutral-700 transition hover:border-neutral-500 hover:text-neutral-900">
                <span>Medium</span><span aria-hidden="true">↗</span>
            </a>
        </div>
    `;
}

function renderHashtags(hashtags) {
    const tags = normalizeHashtags(hashtags);
    if (tags.length === 0) return '';
    return `
        <span class="inline-flex flex-wrap items-center gap-x-2 gap-y-0.5">
            ${tags.map((tag) => `<span class="text-[11px] font-semibold text-ntu-maroon">${escapeHtml(tag)}</span>`).join('')}
        </span>
    `;
}

function renderCroppedImage(src, alt, crop, className = '') {
    const normalized = normalizeCrop(crop);
    const classAttr = className ? ` class="${className}"` : '';
    return `
        <img src="${escapeHtml(src)}" alt="${escapeHtml(alt)}"${classAttr}
            style="aspect-ratio: 3 / 2; display: block; width: 100%; height: auto; object-fit: cover; object-position: ${normalized.x}% ${normalized.y}%; transform: scale(${normalized.zoom}); transform-origin: center center;">
    `;
}

function getGalleryCrop(article, src) {
    const source = article?.gallery_images_crop || {};
    return source[src] || source[String(src || '').replace(/^\//, '')] || article.image_crop || null;
}

function normalizeCrop(value) {
    const raw = value || {};
    const clamp = (num, min, max, fallback) => {
        const parsed = Number.parseFloat(num);
        if (!Number.isFinite(parsed)) return fallback;
        return Math.min(max, Math.max(min, parsed));
    };
    return {
        x: clamp(raw.x ?? raw.crop_x ?? raw['x'], 0, 100, 50),
        y: clamp(raw.y ?? raw.crop_y ?? raw['y'], 0, 100, 50),
        zoom: clamp(raw.zoom ?? raw.scale ?? raw['zoom'], 1, 3, 1).toFixed(2),
    };
}

function normalizeHashtags(value) {
    if (!value) return [];
    const raw = Array.isArray(value) ? value : String(value).split(/[\n,]+/);
    const seen = new Set();
    const tags = [];
    for (const entry of raw) {
        const tag = String(entry).trim().replace(/^#/, '');
        if (!tag || seen.has(tag)) continue;
        seen.add(tag);
        tags.push(tag);
    }
    return tags;
}

function isMediumUrl(value) {
    const href = String(value || '').trim().toLowerCase();
    return href.startsWith('https://medium.com/') || href.startsWith('http://medium.com/') || href.includes('medium.com/');
}

function escapeHtml(value) {
    return String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
}

function showError(message) {
    const container = document.getElementById('article-content');
    container.innerHTML = `
        <div class="text-center py-8">
            <p class="text-red-600 mb-4">${message}</p>
            <a href="index.html" class="text-base text-gray-700 hover:text-gray-900 font-medium">返回首頁</a>
        </div>
    `;
}

// Format date to Chinese format
function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}年${month}月${day}日`;
}
