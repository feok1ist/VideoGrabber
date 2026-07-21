const form = document.getElementById('download-form');
const btn = document.getElementById('submit-btn');
const formatSelect = document.getElementById('format-select');
const qualitySelect = document.getElementById('quality-select');

const qualityOptions = {
    mp4: ['best', '1080', '720', '480', '360'],
    webm: ['best', '4320', '2160', '1440', '1080', '720', '480', '360'],
    mp3: ['320', '256', '192', '128'],
    flac: ['best'],
};

const qualityLabels = {
    mp4: { best: 'Best', '1080': '1080p', '720': '720p', '480': '480p', '360': '360p' },
    webm: { best: 'Best', '4320': '8K', '2160': '4K', '1440': '2K', '1080': '1080p', '720': '720p', '480': '480p', '360': '360p' },
    mp3: { '320': '320 kbps', '256': '256 kbps', '192': '192 kbps', '128': '128 kbps' },
    flac: { best: 'Lossless' },
};

function updateQualityOptions() {
    const type = formatSelect.value;

    let currentVal = qualitySelect.dataset.submitted;
    if (!currentVal || !qualityOptions[type].includes(currentVal)) {
        currentVal = qualitySelect.dataset[type] || qualityOptions[type][0];
    }
    qualitySelect.dataset.submitted = '';

    qualitySelect.innerHTML = '';
    qualityOptions[type].forEach(val => {
        const opt = document.createElement('option');
        opt.value = val;
        opt.textContent = qualityLabels[type][val];
        if (val === currentVal) opt.selected = true;
        qualitySelect.appendChild(opt);
    });
}

formatSelect.addEventListener('change', () => {
    const prev = formatSelect.dataset.prev;
    if (prev) qualitySelect.dataset[prev] = qualitySelect.value;
    formatSelect.dataset.prev = formatSelect.value;
    updateQualityOptions();
});

form.addEventListener('submit', () => {
    btn.disabled = true;
    btn.classList.add('loading');
});

updateQualityOptions();
