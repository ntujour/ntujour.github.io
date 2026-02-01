// Practical faculty detail page with tabs functionality
document.addEventListener('DOMContentLoaded', function() {
    loadPracticalFacultyDetails();
});

// Load practical faculty details
async function loadPracticalFacultyDetails() {
    const tabsContainer = document.getElementById('faculty-tabs');
    const detailsContainer = document.getElementById('faculty-details');

    try {
        // Fetch faculty data
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();

        if (!data['實務'] || data['實務'].length === 0) {
            tabsContainer.innerHTML = '<div class="text-center py-12 text-gray-500 w-full">暫無資料</div>';
            return;
        }

        // Render faculty tabs
        const tabsHTML = data['實務'].map((faculty, index) => {
            const photoSrc = faculty.photo || '';
            const photoHTML = photoSrc
                ? `<img src="${photoSrc}" alt="${faculty.name}" class="w-20 h-20 object-cover rounded-lg">`
                : `<div class="w-20 h-20 rounded-lg bg-gray-100 flex items-center justify-center text-gray-400 text-xs">暫無照片</div>`;

            // Special handling for Archie Tse (謝艾契)
            const displayName = faculty.name === '謝艾契' ? 'Archie Tse' : faculty.name;

            return `
                <div class="faculty-tab ${index === 0 ? 'active' : ''}" data-faculty-id="${faculty.id}" data-index="${index}">
                    ${photoHTML}
                    <div class="faculty-tab-name">${displayName}</div>
                </div>
            `;
        }).join('');

        tabsContainer.innerHTML = tabsHTML;

        // Render faculty detail cards
        const detailsHTML = data['實務'].map((faculty, index) => {
            const photoSrc = faculty.photo || '';
            const photoHTML = photoSrc
                ? `<img src="${photoSrc}" alt="${faculty.name}" class="w-64 h-64 object-cover rounded-lg shadow-md">`
                : `<div class="w-64 h-64 rounded-lg bg-gray-100 flex items-center justify-center text-gray-400">暫無照片</div>`;

            return `
                <div id="faculty-${faculty.id}" class="faculty-detail-card ${index === 0 ? 'active' : ''}" data-index="${index}">
                    <div class="flex flex-col md:flex-row gap-6">
                        <!-- Photo -->
                        <div class="flex-shrink-0">
                            ${photoHTML}
                        </div>

                        <!-- Info -->
                        <div class="flex-1">
                            <h3 class="text-2xl font-bold text-gray-900 mb-2">${faculty.name}</h3>
                            ${faculty.title ? `<p class="text-base text-gray-600 mb-4">${faculty.title}</p>` : ''}

                            <div class="space-y-3">
                                ${faculty.teaching ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">授課領域：</span>
                                        <span class="text-gray-600">${faculty.teaching}</span>
                                    </div>
                                ` : ''}

                                ${faculty.research ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">研究專長：</span>
                                        <span class="text-gray-600">${faculty.research}</span>
                                    </div>
                                ` : ''}

                                ${faculty.education && faculty.education.length > 0 ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">學歷：</span>
                                        <div class="text-gray-600">
                                            <ul class="list-disc list-inside space-y-1">
                                                ${faculty.education.map(edu => `<li>${edu}</li>`).join('')}
                                            </ul>
                                        </div>
                                    </div>
                                ` : ''}

                                ${faculty.experience && faculty.experience.length > 0 ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">經歷：</span>
                                        <div class="text-gray-600">
                                            <ul class="list-disc list-inside space-y-1">
                                                ${faculty.experience.map(exp => `<li>${exp}</li>`).join('')}
                                            </ul>
                                        </div>
                                    </div>
                                ` : ''}

                                ${faculty.email ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">Email：</span>
                                        <span class="text-gray-600"><a href="mailto:${faculty.email}" class="hover:text-gray-900">${faculty.email}</a></span>
                                    </div>
                                ` : ''}

                                ${faculty.phone ? `
                                    <div class="flex items-start">
                                        <span class="font-semibold text-gray-700 w-28 flex-shrink-0">聯絡電話：</span>
                                        <span class="text-gray-600">${faculty.phone}</span>
                                    </div>
                                ` : ''}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }).join('');

        detailsContainer.innerHTML = detailsHTML;

        // Add click event listeners to tabs
        const tabs = document.querySelectorAll('.faculty-tab');
        tabs.forEach(tab => {
            tab.addEventListener('click', function() {
                const index = parseInt(this.dataset.index);
                switchToFaculty(index);
            });
        });

        // Handle URL hash if present (for direct linking)
        if (window.location.hash) {
            const facultyId = window.location.hash.substring(1).replace('faculty-', '');
            const targetIndex = data['實務'].findIndex(f => f.id === facultyId);
            if (targetIndex !== -1) {
                switchToFaculty(targetIndex);
            }
        }

    } catch (error) {
        console.error('Error loading practical faculty details:', error);
        tabsContainer.innerHTML = '<div class="text-center py-12 text-red-500 w-full">載入失敗，請稍後再試</div>';
    }
}

// Switch to a specific faculty member
function switchToFaculty(index) {
    // Update active tab
    const tabs = document.querySelectorAll('.faculty-tab');
    tabs.forEach((tab, i) => {
        if (i === index) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    // Update active detail card
    const cards = document.querySelectorAll('.faculty-detail-card');
    cards.forEach((card, i) => {
        if (i === index) {
            card.classList.add('active');
        } else {
            card.classList.remove('active');
        }
    });

    // Scroll to make the detail section appear right below the faculty tabs
    const tabsContainer = document.getElementById('faculty-tabs');
    const detailsContainer = document.getElementById('faculty-details');

    if (tabsContainer && detailsContainer) {
        // Get the absolute position of details container in the document
        const detailsRect = detailsContainer.getBoundingClientRect();
        const detailsTop = window.pageYOffset + detailsRect.top;

        // Get the height of sticky tabs and navigation
        // Navigation is at top: 0, tabs are at top: 58px
        // So we need to offset by nav height (58px) + tabs height
        const tabsHeight = tabsContainer.offsetHeight;
        const navHeight = 58; // Navigation bar height

        // Calculate scroll position: details position - nav height - tabs height
        const scrollTarget = detailsTop - navHeight - tabsHeight;

        // Smooth scroll to position
        window.scrollTo({
            top: scrollTarget,
            behavior: 'smooth'
        });
    }
}
