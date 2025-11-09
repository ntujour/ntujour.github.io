// Article detail page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const articleId = urlParams.get('id');
    const articleType = urlParams.get('type');

    if (articleId && articleType) {
        loadArticle(articleId, articleType);
    } else {
        showError('無法載入文章：缺少必要參數');
    }
});

// Article data mapping
const articlesMap = {
    news: {
        '259107': { title: '113學年度碩士班甄試招生錄取名單', date: '2024-11-05', file: 'News_Content_n_35497_s_259107.html' },
        '258976': { title: '113學年度碩士班考試入學招生公告', date: '2024-11-01', file: 'News_Content_n_35497_s_258976.html' },
        '258800': { title: '新聞所舉辦學術研討會', date: '2024-10-28', file: 'News_Content_n_35497_s_258800.html' },
        '257861': { title: '學期演講公告', date: '2024-10-20', file: 'News_Content_n_35497_s_257861.html' },
        '257857': { title: '研究生獎學金公告', date: '2024-10-15', file: 'News_Content_n_35497_s_257857.html' },
        '250871': { title: '碩士班修業規定修訂', date: '2024-09-05', file: 'News_Content_n_35497_s_250871.html' },
        '211542': { title: '開學相關事項通知', date: '2024-08-28', file: 'News_Content_n_35497_s_211542.html' },
        '211541': { title: '暑期課程公告', date: '2024-07-10', file: 'News_Content_n_35497_s_211541.html' },
        '104734': { title: '學位考試相關規定', date: '2024-06-15', file: 'News_Content_n_35497_s_104734.html' },
        '104732': { title: '論文口試申請', date: '2024-05-20', file: 'News_Content_n_35497_s_104732.html' },
        '104731': { title: '學術倫理課程', date: '2024-04-25', file: 'News_Content_n_35497_s_104731.html' },
    },
    activity: {
        '258988': { title: '新聞傳播工作坊', date: '2024-11-10', file: 'News_Content_n_35498_s_258988.html' },
        '257550': { title: '媒體素養講座', date: '2024-10-25', file: 'News_Content_n_35498_s_257550.html' },
        '257534': { title: '業界參訪活動', date: '2024-10-18', file: 'News_Content_n_35498_s_257534.html' },
        '254585': { title: '畢業生座談會', date: '2024-09-30', file: 'News_Content_n_35498_s_254585.html' },
        '254584': { title: '國際學術交流', date: '2024-09-15', file: 'News_Content_n_35498_s_254584.html' },
        '246560': { title: '研究生論文發表會', date: '2024-08-20', file: 'News_Content_n_35498_s_246560.html' },
        '244147': { title: '新生迎新活動', date: '2024-08-15', file: 'News_Content_n_35498_s_244147.html' },
        '243181': { title: '學術研討會', date: '2024-07-30', file: 'News_Content_n_35498_s_243181.html' },
        '242697': { title: '暑期實習說明會', date: '2024-06-25', file: 'News_Content_n_35498_s_242697.html' },
        '242587': { title: '期末成果展', date: '2024-06-10', file: 'News_Content_n_35498_s_242587.html' },
    }
};

function loadArticle(id, type) {
    const article = articlesMap[type]?.[id];

    if (!article) {
        showError('找不到指定的文章');
        return;
    }

    // Update page title
    document.title = article.title + ' - 國立臺灣大學新聞研究所';

    // Update breadcrumb
    const breadcrumbCategory = document.getElementById('breadcrumb-category');
    if (breadcrumbCategory) {
        const categoryText = type === 'news' ? '最新消息' : '活動資訊';
        const categoryLink = type === 'news' ? 'news.html' : 'activities.html';
        breadcrumbCategory.innerHTML = `<a href="${categoryLink}" class="hover:text-crimson">${categoryText}</a>`;
    }

    // Try to load the original article file, or show placeholder content
    loadOriginalArticle(article);
}

function loadOriginalArticle(article) {
    const contentDiv = document.getElementById('article-content');

    // Since we're using static hosting, we'll create a simple display
    // In a real scenario, you might want to parse and extract content from the old HTML

    contentDiv.innerHTML = `
        <div class="prose max-w-none">
            <h1 class="text-3xl font-bold text-crimson mb-2">${article.title}</h1>
            <p class="text-sm text-gray-500 mb-6">發布日期：${article.date}</p>

            <div class="bg-gray-50 p-4 border-l-4 border-crimson mb-6">
                <p class="text-gray-700">
                    這是文章的簡化顯示。完整內容請參考原始頁面：
                    <a href="${article.file}" class="text-crimson hover:underline" target="_blank">查看原始文章</a>
                </p>
            </div>

            <div class="text-gray-700 leading-relaxed space-y-4">
                <p>文章內容載入中...</p>
                <p>如果內容未正確顯示，請<a href="${article.file}" class="text-crimson hover:underline">點此查看原始頁面</a>。</p>
            </div>
        </div>
    `;

    // Attempt to fetch and extract content from the original file
    fetch(article.file)
        .then(response => response.text())
        .then(html => {
            // Parse the HTML and extract the main content
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');

            // Try to find the main content area
            // This will vary based on the structure of the old pages
            const contentArea = doc.querySelector('.area-essay') ||
                              doc.querySelector('.ct') ||
                              doc.querySelector('article') ||
                              doc.querySelector('main');

            if (contentArea) {
                // Clean up the content and display it
                const cleanedContent = cleanContent(contentArea.innerHTML);
                contentDiv.innerHTML = `
                    <div class="prose max-w-none">
                        <h1 class="text-3xl font-bold text-crimson mb-2">${article.title}</h1>
                        <p class="text-sm text-gray-500 mb-6">發布日期：${article.date}</p>
                        <div class="text-gray-700 leading-relaxed">
                            ${cleanedContent}
                        </div>
                    </div>
                `;
            }
        })
        .catch(error => {
            console.error('Error loading article:', error);
            // Keep the placeholder content with link to original
        });
}

function cleanContent(html) {
    // Remove scripts and styles
    let cleaned = html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
    cleaned = cleaned.replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '');

    // Remove inline styles and classes for cleaner display
    cleaned = cleaned.replace(/\s(class|style|data-[a-z-]+)="[^"]*"/gi, '');

    return cleaned;
}

function showError(message) {
    const contentDiv = document.getElementById('article-content');
    contentDiv.innerHTML = `
        <div class="text-center py-8">
            <p class="text-red-600 mb-4">${message}</p>
            <a href="index.html" class="text-crimson hover:underline">返回首頁</a>
        </div>
    `;
}
