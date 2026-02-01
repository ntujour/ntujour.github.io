// Honorary faculty detail page functionality
document.addEventListener('DOMContentLoaded', function() {
    loadHonoraryFacultyDetails();
});

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
                        <img src="${faculty.photo}" alt="${faculty.name}" class="w-64 h-64 object-cover rounded-lg shadow-md mx-auto md:mx-0">
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
