// E-Report list loader - loads report data from CSV and renders dynamically
document.addEventListener('DOMContentLoaded', function() {
    loadEReports();
});

// Load e-reports from CSV
async function loadEReports() {
    const container = document.getElementById('report-list');

    try {
        // Fetch CSV data
        const response = await fetch('../data/e-reports.csv');
        const csvText = await response.text();

        // Parse CSV
        const reports = parseCSV(csvText);

        if (reports.length === 0) {
            container.innerHTML = '<div class="text-center py-12 text-gray-500">暫無資料</div>';
            return;
        }

        // Render report list
        const listHTML = reports.map(report => {
            const { issue, title, date, filepath } = report;

            // Skip if no filepath
            if (!filepath) {
                return '';
            }

            return `
                <li>
                    <a href="../${filepath}" target="_blank" rel="noopener noreferrer">
                        ${title}
                        <span class="text-gray-500 text-sm">(${date})</span>
                    </a>
                </li>
            `;
        }).filter(html => html !== '').join('');

        container.innerHTML = listHTML;

    } catch (error) {
        console.error('Error loading e-reports:', error);
        container.innerHTML = '<div class="text-center py-12 text-red-500">載入失敗，請稍後再試</div>';
    }
}

// Simple CSV parser
function parseCSV(csvText) {
    const lines = csvText.trim().split('\n');

    // Skip header line
    const dataLines = lines.slice(1);

    const reports = [];

    for (const line of dataLines) {
        // Skip empty lines
        if (!line.trim()) continue;

        // Parse CSV line (simple parser, assumes no commas in fields)
        const parts = line.split(',');

        if (parts.length >= 4) {
            reports.push({
                issue: parts[0].trim(),
                title: parts[1].trim(),
                date: parts[2].trim(),
                filepath: parts[3].trim()
            });
        }
    }

    return reports;
}
