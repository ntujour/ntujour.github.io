// Combined news and activities listing page JavaScript

let allItems = [];
const ITEMS_PER_PAGE = 12;
let currentPage = 1;
let currentFilter = 'all'; // 'all', 'news', 'activity'

document.addEventListener('DOMContentLoaded', async function() {
    await loadAllData();
    setupFilters();
    renderPage();
});

async function loadAllData() {
    try {
        // Load both news and activities
        const [newsResponse, activitiesResponse] = await Promise.all([
            fetch('data/news.json'),
            fetch('data/activities.json')
        ]);

        const newsData = await newsResponse.json();
        const activitiesData = await activitiesResponse.json();

        // Add type field to distinguish between news and activities
        const newsItems = newsData.map(item => ({...item, type: 'news'}));
        const activityItems = activitiesData.map(item => ({...item, type: 'activity'}));

        // Combine and sort by date descending
        allItems = [...newsItems, ...activityItems];
        allItems.sort((a, b) => new Date(b.date) - new Date(a.date));
    } catch (error) {
        console.error('Error loading data:', error);
        allItems = [];
    }
}

function setupFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]');
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            currentFilter = this.dataset.filter;
            currentPage = 1;

            // Update active state
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            renderPage();
        });
    });
}

function getFilteredItems() {
    if (currentFilter === 'all') {
        return allItems;
    }
    return allItems.filter(item => item.type === currentFilter);
}

function renderPage() {
    renderItemsList();
    renderPagination();
}

function renderItemsList() {
    const container = document.getElementById('items-list');
    if (!container) return;

    const filteredItems = getFilteredItems();

    if (filteredItems.length === 0) {
        container.innerHTML = '<p class="text-center text-gray-500 py-8 col-span-full">目前沒有內容</p>';
        return;
    }

    // Calculate pagination
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    const endIndex = startIndex + ITEMS_PER_PAGE;
    const pageItems = filteredItems.slice(startIndex, endIndex);

    const cardsHTML = pageItems.map(item => {
        // Extract text from HTML content for excerpt
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = item.content;
        const textContent = tempDiv.textContent || tempDiv.innerText || '';
        const excerpt = textContent.substring(0, 100);

        const typeLabel = item.type === 'news' ? '消息' : '活動';
        const typeClass = item.type === 'news' ? 'bg-blue-100 text-blue-800' : 'bg-green-100 text-green-800';

        return `
        <article class="bg-white border border-gray-200 rounded hover:shadow-md transition-shadow cursor-pointer" onclick="window.location.href='article-view.html?type=${item.type}&id=${item.id}'">
            <div class="p-4">
                <div class="flex items-center gap-2 mb-2">
                    <span class="inline-block px-2 py-1 text-xs rounded ${typeClass}">${typeLabel}</span>
                    <span class="inline-block px-2 py-1 text-xs rounded bg-red-100 text-red-800">${item.category}</span>
                    <time class="text-xs text-gray-500">${formatDate(item.date)}</time>
                </div>
                <h3 class="text-base font-bold text-gray-900 mb-2 line-clamp-2">${item.title}</h3>
                <p class="text-sm text-gray-600 line-clamp-3">${excerpt}...（繼續閱讀）</p>
            </div>
        </article>
        `;
    }).join('');

    container.innerHTML = cardsHTML;
}

function renderPagination() {
    const container = document.getElementById('pagination');
    if (!container) return;

    const filteredItems = getFilteredItems();
    const totalPages = Math.ceil(filteredItems.length / ITEMS_PER_PAGE);

    if (totalPages <= 1) {
        container.innerHTML = '';
        return;
    }

    let paginationHTML = '';

    // Previous button
    if (currentPage > 1) {
        paginationHTML += `
            <button onclick="goToPage(${currentPage - 1})" class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-100">
                上一頁
            </button>
        `;
    }

    // Page numbers
    for (let i = 1; i <= totalPages; i++) {
        if (i === currentPage) {
            paginationHTML += `
                <button class="px-3 py-1 text-sm bg-gray-800 text-white rounded">
                    ${i}
                </button>
            `;
        } else if (i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {
            paginationHTML += `
                <button onclick="goToPage(${i})" class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-100">
                    ${i}
                </button>
            `;
        } else if (i === currentPage - 3 || i === currentPage + 3) {
            paginationHTML += `<span class="px-2 text-gray-500">...</span>`;
        }
    }

    // Next button
    if (currentPage < totalPages) {
        paginationHTML += `
            <button onclick="goToPage(${currentPage + 1})" class="px-3 py-1 text-sm border border-gray-300 rounded hover:bg-gray-100">
                下一頁
            </button>
        `;
    }

    container.innerHTML = paginationHTML;
}

function goToPage(page) {
    currentPage = page;
    renderPage();
    // Scroll to top of items list
    document.getElementById('items-list').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Format date to Chinese format
function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}年${month}月${day}日`;
}
