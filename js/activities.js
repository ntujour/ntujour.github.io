// Activities listing page JavaScript

let activitiesData = [];
const ITEMS_PER_PAGE = 9;
let currentPage = 1;

document.addEventListener('DOMContentLoaded', async function() {
    await loadActivitiesData();
    renderActivitiesPage();
});

async function loadActivitiesData() {
    try {
        const response = await fetch('data/activities.json');
        activitiesData = await response.json();
        // Sort by date descending
        activitiesData.sort((a, b) => new Date(b.date) - new Date(a.date));
    } catch (error) {
        console.error('Error loading activities data:', error);
        activitiesData = [];
    }
}

function renderActivitiesPage() {
    renderActivitiesList();
    renderPagination();
}

function renderActivitiesList() {
    const container = document.getElementById('activities-list');
    if (!container) return;

    if (activitiesData.length === 0) {
        container.innerHTML = '<p class="text-center text-gray-500 py-8 col-span-full">目前沒有活動</p>';
        return;
    }

    // Calculate pagination
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    const endIndex = startIndex + ITEMS_PER_PAGE;
    const pageItems = activitiesData.slice(startIndex, endIndex);

    const cardsHTML = pageItems.map(item => {
        // Extract text from HTML content for excerpt
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = item.content;
        const textContent = tempDiv.textContent || tempDiv.innerText || '';
        const excerpt = textContent.substring(0, 100);
        const hashtags = renderHashtags(item.hashtags);

        return `
        <article class="bg-white border border-gray-200 rounded hover:shadow-md transition-shadow cursor-pointer" onclick="window.location.href='article-view.html?type=activity&id=${item.id}'">
            <div class="p-4">
                <div class="flex items-center gap-2 mb-2">
                    <time class="text-xs text-gray-500">${formatDate(item.date)}</time>
                    ${hashtags}
                </div>
                <h3 class="text-base font-normal text-gray-900 mb-2 line-clamp-1">${item.title}</h3>
                <p class="text-sm text-gray-600 line-clamp-3">${excerpt}...（繼續閱讀）</p>
            </div>
        </article>
        `;
    }).join('');

    container.innerHTML = cardsHTML;
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

function escapeHtml(value) {
    return String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
}

function renderPagination() {
    const container = document.getElementById('pagination');
    if (!container) return;

    const totalPages = Math.ceil(activitiesData.length / ITEMS_PER_PAGE);

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
    renderActivitiesPage();
    // Scroll to top of activities list
    document.getElementById('activities-list').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Format date to Chinese format
function formatDate(dateString) {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}年${month}月${day}日`;
}
