// Faculty page functionality
document.addEventListener('DOMContentLoaded', function() {
    loadFulltimeFaculty();
    loadParttimeFaculty();
    loadPracticalFaculty();
    loadHonoraryFaculty();
    loadJointFaculty();
});

// Load full-time faculty data
async function loadFulltimeFaculty() {
    const container = document.getElementById('fulltime-faculty');

    try {
        // Fetch faculty data
        const response = await fetch('../faculty_data.json');
        const data = await response.json();

        // Render faculty photo cards - open in new tab
        const cardsHTML = data.fulltime.map(faculty => `
            <a href="${faculty.file}" target="_blank" rel="noopener noreferrer" class="block text-center transition-transform hover:-translate-y-1">
                <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
            </a>
        `).join('');

        container.innerHTML = cardsHTML;
    } catch (error) {
        console.error('Error loading faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load part-time faculty data
async function loadParttimeFaculty() {
    const container = document.getElementById('parttime-faculty');

    try {
        // Fetch faculty data
        const response = await fetch('../faculty_data.json');
        const data = await response.json();

        if (!data.parttime || data.parttime.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }

        // Render faculty photo cards - all link to parttime-professor-detail.html
        const cardsHTML = data.parttime.map((faculty, index) => `
            <a href="parttime-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
                <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
            </a>
        `).join('');

        container.innerHTML = cardsHTML;
    } catch (error) {
        console.error('Error loading parttime faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load practical faculty data
async function loadPracticalFaculty() {
    const container = document.getElementById('practical-faculty');

    try {
        // Fetch faculty data
        const response = await fetch('../faculty_data.json');
        const data = await response.json();

        if (!data.practical || data.practical.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }

        // Render faculty photo cards - link to practical-professor-detail.html
        const cardsHTML = data.practical.map((faculty, index) => {
            // Only show cards with photos
            if (!faculty.photo) {
                return '';
            }
            return `
                <a href="practical-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
                    <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                    <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
                </a>
            `;
        }).filter(html => html).join('');

        container.innerHTML = cardsHTML || '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
    } catch (error) {
        console.error('Error loading practical faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load honorary faculty data
async function loadHonoraryFaculty() {
    const container = document.getElementById('honorary-faculty');

    try {
        // Fetch faculty data
        const response = await fetch('../faculty_data.json');
        const data = await response.json();

        if (!data.honorary || data.honorary.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }

        // Render faculty photo cards
        const cardsHTML = data.honorary.map((faculty, index) => `
            <a href="honorary-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
                <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
            </a>
        `).join('');

        container.innerHTML = cardsHTML;
    } catch (error) {
        console.error('Error loading honorary faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load joint appointment faculty data
async function loadJointFaculty() {
    const container = document.getElementById('joint-faculty');

    try {
        // Fetch faculty data
        const response = await fetch('../faculty_data.json');
        const data = await response.json();

        if (!data.joint || data.joint.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }

        // Render faculty photo cards
        const cardsHTML = data.joint.map((faculty, index) => `
            <a href="joint-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
                <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
            </a>
        `).join('');

        container.innerHTML = cardsHTML;
    } catch (error) {
        console.error('Error loading joint faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}
