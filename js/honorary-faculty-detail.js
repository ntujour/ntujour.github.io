// Honorary faculty detail page functionality
const CROP_RATIO = '3 / 2';
const DEFAULT_IMAGE_CROP = { x: 50, y: 50, zoom: 1 };

document.addEventListener('DOMContentLoaded', function() {
    loadHonoraryFacultyDetails();
});

function normalizeImageCrop(crop) {
    if (!crop || typeof crop !== 'object') return DEFAULT_IMAGE_CROP;
    const x = Number.isFinite(Number(crop.x)) ? Number(crop.x) : DEFAULT_IMAGE_CROP.x;
    const y = Number.isFinite(Number(crop.y)) ? Number(crop.y) : DEFAULT_IMAGE_CROP.y;
    const zoom = Number.isFinite(Number(crop.zoom)) ? Number(crop.zoom) : DEFAULT_IMAGE_CROP.zoom;
    return {
        x: Math.min(100, Math.max(0, x)),
        y: Math.min(100, Math.max(0, y)),
        zoom: Math.min(4, Math.max(1, zoom)),
    };
}

function renderCroppedImage(src, alt, crop, className) {
    if (!src) return '';
    const normalized = normalizeImageCrop(crop);
    return `<img src="${src}" alt="${alt}" class="${className}" style="aspect-ratio: ${CROP_RATIO}; display: block; object-fit: cover; object-position: ${normalized.x}% ${normalized.y}%; transform: scale(${normalized.zoom}); transform-origin: center center;">`;
}

// Load honorary faculty details
async function loadHonoraryFacultyDetails() {
    const container = document.getElementById('faculty-details');

    try {
        // Fetch faculty data
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();

        if (!data['榮譽'] || data['榮譽'].length === 0) {
            container.innerHTML = '<div class="text-center py-12 text-gray-500">暫無資料</div>';
            return;
        }

        // Render faculty detail cards
        const cardsHTML = data['榮譽'].map((faculty, index) => `
            <div id="faculty-${index}" class="faculty-detail-card bg-white border border-gray-200 rounded-lg p-6 md:p-8">
                <div class="flex flex-col md:flex-row gap-6">
                    <!-- Photo -->
                    ${faculty.photo ? `
                    <div class="flex-shrink-0">
                        ${renderCroppedImage(faculty.photo, faculty.name, faculty.photo_crop, 'w-64 h-auto object-cover rounded-lg shadow-md mx-auto md:mx-0')}
                    </div>
                    ` : ''}

                    <!-- Info -->
                    <div class="flex-1">
                        <h3 class="text-2xl font-bold text-gray-900 mb-4">${faculty.name}</h3>

                        <div class="space-y-3">
                            ${faculty.phone ? `
                                <div class="flex items-start">
                                    <span class="font-semibold text-gray-700 w-24 flex-shrink-0">聯絡電話：</span>
                                    <span class="text-gray-600">${faculty.phone}</span>
                                </div>
                            ` : ''}

                            ${faculty.email ? `
                                <div class="flex items-start">
                                    <span class="font-semibold text-gray-700 w-24 flex-shrink-0">Email：</span>
                                    <span class="text-gray-600"><a href="mailto:${faculty.email}" class="hover:text-gray-900">${faculty.email}</a></span>
                                </div>
                            ` : ''}

                            ${faculty.teaching ? `
                                <div class="flex items-start">
                                    <span class="font-semibold text-gray-700 w-24 flex-shrink-0">授課領域：</span>
                                    <span class="text-gray-600">${faculty.teaching}</span>
                                </div>
                            ` : ''}

                            ${faculty.research ? `
                                <div class="flex items-start">
                                    <span class="font-semibold text-gray-700 w-24 flex-shrink-0">研究專長：</span>
                                    <span class="text-gray-600">${faculty.research}</span>
                                </div>
                            ` : ''}
                        </div>
                    </div>
                </div>
            </div>
        `).join('');

        container.innerHTML = cardsHTML;

        // Scroll to the faculty member if hash is present
        if (window.location.hash) {
            setTimeout(() => {
                const target = document.querySelector(window.location.hash);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 100);
        }
    } catch (error) {
        console.error('Error loading honorary faculty details:', error);
        container.innerHTML = '<div class="text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}
