// Faculty page functionality (category keys: 專任, 兼任, 合聘, 榮譽, 實務, 追思, 職員)
document.addEventListener('DOMContentLoaded', function() {
    loadFulltimeFaculty();
    loadParttimeFaculty();
    loadPracticalFaculty();
    loadHonoraryFaculty();
    loadJointFaculty();
    loadMemorialFaculty();
    loadStaffFaculty();
});

// Load 專任 faculty data
async function loadFulltimeFaculty() {
    const container = document.getElementById('fulltime-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['專任'] || [];
        const cardsHTML = list.map(faculty => `
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

// Load 兼任 faculty data
async function loadParttimeFaculty() {
    const container = document.getElementById('parttime-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['兼任'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => `
            <a href="parttime-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
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

// Load 實務 faculty data
async function loadPracticalFaculty() {
    const container = document.getElementById('practical-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['實務'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => {
            if (!faculty.photo) return '';
            return `
                <a href="practical-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
                    <img src="${faculty.photo}" alt="${faculty.name}" class="w-full aspect-square object-cover rounded-lg shadow-sm hover:shadow-md transition-shadow mb-2">
                    <h4 class="text-sm font-medium text-gray-900">${faculty.name}</h4>
                </a>
            `;
        }).filter(html => html).join('');
        container.innerHTML = cardsHTML || '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
    } catch (error) {
        console.error('Error loading faculty data:', error);
        container.innerHTML = '<div class="col-span-full text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Load 榮譽 faculty data
async function loadHonoraryFaculty() {
    const container = document.getElementById('honorary-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['榮譽'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => `
            <a href="honorary-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
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

// Load 合聘 faculty data
async function loadJointFaculty() {
    const container = document.getElementById('joint-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['合聘'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => `
            <a href="joint-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
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

// Load 追思 faculty data
async function loadMemorialFaculty() {
    const container = document.getElementById('memorial-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['追思'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => `
            <a href="memorial-professor-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
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

// Load 職員 faculty data
async function loadStaffFaculty() {
    const container = document.getElementById('staff-faculty');
    if (!container) return;
    try {
        const response = await fetch('../data/faculty_data.json');
        const data = await response.json();
        const list = data['職員'] || [];
        if (list.length === 0) {
            container.innerHTML = '<div class="col-span-full text-center py-6 text-gray-500">資料整理中</div>';
            return;
        }
        const cardsHTML = list.map((faculty, index) => `
            <a href="staff-detail.html#faculty-${index}" class="block text-center transition-transform hover:-translate-y-1">
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
