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
                ${article.category ? `<span class="inline-block px-2 py-1 text-xs rounded bg-red-100 text-red-800">${article.category}</span>` : ''}
            </div>
        </div>

        ${extraInfo}

        <div class="article-body">
            ${article.content}
        </div>

        ${article.originalFile ? `
            <div class="original-file-box">
                <p class="text-sm text-gray-700">
                    註：本文內容已經過重新編排。如需查看原始頁面，請
                    <a href="${article.originalFile}" class="text-blue-600 hover:underline" target="_blank">點此查看</a>。
                </p>
            </div>
        ` : ''}
    `;
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
