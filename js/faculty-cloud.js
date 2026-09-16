/* Reader for published faculty JSON with a bundled read-only snapshot fallback. */
(function () {
  'use strict';

  const script = document.currentScript;
  const cloudBase = 'https://storage.googleapis.com/ntujour-graduate/faculty-pilot/v1/';
  const localBase = new URL('../data/faculty-snapshot/', script && script.src ? script.src : location.href).href;
  const kind = script && script.dataset.facultyView;
  const facultyId = (script && script.dataset.facultyId) || new URLSearchParams(location.search).get('id');
  const facultyCategory = script && script.dataset.facultyCategory;
  const paths = JSON.parse((script && script.dataset.facultyPaths) || '{}');
  const configuredPaths = Object.keys(paths).length ? paths : (window.NTUJourFacultyPaths || {});
  const esc = value => String(value || '').replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));

  async function read(base, path, cache) {
    const response = await fetch(base + path, { cache: cache || 'no-store' });
    if (!response.ok) throw new Error(`Faculty JSON request failed: ${response.status}`);
    return response.json();
  }
  async function dataFor(filename) {
    try {
      const release = (await read(cloudBase, 'current.json')).release;
      return await read(cloudBase, `releases/${release}/${filename}`);
    } catch (error) {
      console.warn('Cloud faculty data unavailable; using the local published snapshot.', error);
      const release = (await read(localBase, 'current.json', 'no-cache')).release;
      const data = await read(localBase, `releases/${release}/${filename}`, 'no-cache');
      const localPhoto = item => {
        if (!item || !item.photo) return item;
        const filename = String(item.photo).split('/').pop();
        return { ...item, photo: new URL(`media/${filename}`, localBase).href };
      };
      if (Array.isArray(data.items)) return { ...data, items: data.items.map(localPhoto) };
      return localPhoto(data);
    }
  }
  const category = value => value === 'former_practical' ? 'practical' : value;
  const categories = item => {
    const values = Array.isArray(item.categories) ? item.categories : [item.category];
    return [...new Set(values.map(category).filter(Boolean))];
  };

  async function loadZhIndex(pathMap) {
    const json = await dataFor('index.zh.json');
    if (!Array.isArray(json.items)) throw new Error('Invalid Chinese faculty index');
    return json.items.map(item => {
      const mappedPath = pathMap && pathMap[item.id];
      return {
        ...item,
        category_key: category(item.category),
        category_keys: categories(item),
        html_link: mappedPath
          ? `${mappedPath}.html`
          : `profile.html?id=${encodeURIComponent(item.id)}`,
      };
    });
  }

  async function loadEnglishIndex() {
    const json = await dataFor('index.en.json');
    if (!Array.isArray(json.items)) throw new Error('Invalid English faculty index');
    const groups = { fulltime: [], adjunct: [], specialist: [], emeritus: [], joint: [], retired: [], remembrance: [] };
    const groupFor = { fulltime: 'fulltime', parttime: 'adjunct', practical: 'specialist', former_practical: 'specialist', honorary: 'emeritus', joint: 'joint', retired: 'retired' };
    json.items.forEach(item => {
      categories(item).forEach(itemCategory => {
        const group = groupFor[itemCategory];
        if (!group) return;
        const card = {
          ...item,
          tags: [],
          profileUrl: configuredPaths[item.id]
            ? `faculty/${item.id}.html`
            : `faculty/profile.html?id=${encodeURIComponent(item.id)}`,
        };
        groups[group].push(card);
      });
    });
    return groups;
  }

  window.NTUJourFacultyCloud = { loadZhIndex, loadEnglishIndex };

  function profileUrl(id, language) {
    if (language === 'en') {
      return configuredPaths[id]
        ? `faculty/${encodeURIComponent(id)}.html`
        : `faculty/profile.html?id=${encodeURIComponent(id)}`;
    }
    const mapped = configuredPaths[id];
    return mapped
      ? `${encodeURIComponent(mapped)}.html`
      : `profile.html?id=${encodeURIComponent(id)}`;
  }

  async function renderZhIndex() {
    const grid = document.getElementById('faculty-grid');
    const status = document.getElementById('faculty-status');
    const buttons = Array.from(document.querySelectorAll('[data-faculty-category]'));
    const counts = new Map(Array.from(document.querySelectorAll('[data-count]')).map(el => [el.dataset.count, el]));
    const json = await dataFor('index.zh.json');
    const items = (json.items || []).map(item => ({ ...item, category_key: category(item.category), category_keys: categories(item) }));
    const labels = { fulltime: '專任教師', parttime: '兼任教師', practical: '實務教師', honorary: '名譽教授', joint: '合聘教師', retired: '退休教師', staff: '職員', all: '全部' };
    const initial = new URLSearchParams(location.search).get('category') || 'all';

    // The copied page still starts its original local-JSON renderer.  Let it
    // finish first so the cloud-backed test result is always the final view.
    for (let attempt = 0; grid && !grid.querySelector('.faculty-card') && attempt < 40; attempt += 1) {
      await new Promise(resolve => setTimeout(resolve, 250));
    }

    function render(key) {
      const selected = (key === 'all' ? items : items.filter(item => item.category_keys.includes(key)))
        .slice().sort((a, b) => Number(a.order || 9999) - Number(b.order || 9999));
      grid.innerHTML = selected.length ? selected.map(item => `
        <a href="${profileUrl(item.id, 'zh')}" class="faculty-card group" target="_blank" rel="noopener noreferrer">
          <div class="faculty-card-image-container"><img src="${esc(item.photo)}" alt="${esc(item.name)}" class="faculty-card-image group-hover:scale-105"></div>
          <div class="faculty-card-content"><h3 class="text-sm font-medium text-neutral-900 mb-1">${esc(item.name)}</h3><p class="text-ntu-maroon font-medium text-xs">${esc(item.title)}</p></div>
        </a>`).join('') : '<div class="faculty-empty-state" style="grid-column:1 / -1;">此類別目前沒有教師資料。</div>';
      grid.setAttribute('aria-busy', 'false');
      if (status) status.textContent = `${labels[key] || '教師'}：${selected.length} 位`;
      buttons.forEach(button => {
        const active = button.dataset.facultyCategory === key;
        button.classList.toggle('active', active);
        button.setAttribute('aria-pressed', String(active));
      });
    }
    Object.keys(labels).forEach(key => { const el = counts.get(key); if (el) el.textContent = `(${key === 'all' ? items.length : items.filter(item => item.category_keys.includes(key)).length})`; });
    buttons.forEach(button => button.addEventListener('click', () => render(button.dataset.facultyCategory || 'all')));
    render(labels[initial] ? initial : 'all');
  }

  function zhContact(label, value, href) {
    if (!value) return '';
    const content = href ? `<a href="${href}" class="hover:text-ntu-maroon transition">${esc(value)}</a>` : esc(value);
    return `<div class="flex items-start text-base"><span class="font-bold text-neutral-700 w-24">${label}：</span><span class="text-neutral-600">${content}</span></div>`;
  }
  async function renderZhProfile() {
    const data = await dataFor(`${facultyId}.zh.json`);
    document.title = `國立臺灣大學新聞研究所 - ${data.name} ${data.title}`;
    const title = document.querySelector('#page-header h2');
    if (title) title.textContent = `${data.name} ${data.title}`;
    const article = document.querySelector('#main-content .article-detail-main');
    if (!article) return;
    article.innerHTML = `<div class="flex flex-col md:flex-row gap-8 mb-12"><div class="flex-shrink-0"><img src="${esc(data.photo)}" alt="${esc(data.name)}" class="w-64 h-auto object-cover rounded-2xl shadow-md mx-auto md:mx-0" style="aspect-ratio:1 / 1"></div>
      <div class="flex-1"><h3 class="text-lg font-bold text-neutral-900 mb-6">${esc(data.name)} ${esc(data.title)}</h3><div class="space-y-3 text-base">
      ${zhContact('Email', data.email, `mailto:${encodeURIComponent(data.email || '')}`)}${zhContact('授課領域', data.expertise)}${zhContact('電話', data.phone)}${zhContact('研究室', data.office)}${data.website ? zhContact('個人網站', '連結', esc(data.website)) : ''}</div></div></div>
      <div class="markdown-content prose max-w-none text-neutral-800 leading-relaxed">${data.bodyHtml || ''}</div>`;
  }

  async function renderZhCategory() {
    if (!facultyCategory) throw new Error('Missing faculty category');
    const grid = document.getElementById(`${facultyCategory}-list`) || document.querySelector('#main-content .faculty-grid');
    if (!grid) throw new Error('Missing faculty category grid');
    const json = await dataFor('index.zh.json');
    if (!Array.isArray(json.items)) throw new Error('Invalid Chinese faculty index');
    const items = json.items
      .filter(item => categories(item).includes(facultyCategory))
      .sort((a, b) => Number(a.order || 9999) - Number(b.order || 9999));
    grid.innerHTML = items.length ? items.map(item => `
      <a href="${profileUrl(item.id, 'zh')}" class="faculty-card group" target="_blank" rel="noopener noreferrer">
        <div class="faculty-card-image-container"><img src="${esc(item.photo)}" alt="${esc(item.name)}" class="faculty-card-image group-hover:scale-105"></div>
        <div class="faculty-card-content"><h3 class="text-sm font-medium text-neutral-900 mb-1">${esc(item.name)}</h3><p class="text-ntu-maroon font-medium text-xs">${esc(item.title)}</p></div>
      </a>`).join('') : '<div class="faculty-empty-state">此類別目前沒有教師資料。</div>';
  }

  function enCard(item, linkProfile) {
    const tag = linkProfile ? 'a' : 'div';
    const href = linkProfile ? ` href="${profileUrl(item.id, 'en')}"` : '';
    return `<${tag} class="faculty-card"${href}><div class="faculty-photo-wrap"><img class="faculty-photo" src="${esc(item.photo)}" alt="${esc(item.name)}" loading="lazy"></div><div class="faculty-body"><span class="faculty-name">${esc(item.name)}</span><span class="faculty-badge">${esc(item.title)}</span></div></${tag}>`;
  }
  async function renderEnIndex() {
    const groups = await loadEnglishIndex();
    const firstGrid = document.querySelector('#faculty-fulltime .faculty-grid');
    for (let attempt = 0; firstGrid && !firstGrid.querySelector('.faculty-card') && attempt < 40; attempt += 1) {
      await new Promise(resolve => setTimeout(resolve, 250));
    }
    Object.entries(groups).forEach(([group, items]) => {
      const grid = document.querySelector(`#faculty-${group} .faculty-grid`);
      if (grid) grid.innerHTML = items.slice().sort((a, b) => Number(a.order || 9999) - Number(b.order || 9999)).map(item => enCard(item, true)).join('');
    });
  }
  async function renderEnProfile() {
    const data = await dataFor(`${facultyId}.en.json`);
    const existingHeader = document.getElementById('profile-header-inner');
    for (let attempt = 0; existingHeader && !existingHeader.textContent.trim() && attempt < 40; attempt += 1) {
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    document.title = `${data.name} — Graduate Institute of Journalism, NTU`;
    const header = document.getElementById('profile-header-inner');
    const meta = document.getElementById('profile-meta');
    const main = document.getElementById('profile-main');
    const sidebar = document.getElementById('profile-sidebar');
    if (header) header.innerHTML = `<div class="profile-photo-wrap"><img class="profile-photo-large" src="${esc(data.photo)}" alt="${esc(data.name)}"></div><div><p class="profile-dept">Graduate Institute of Journalism · NTU</p><h1 class="profile-name">${esc(data.name)}</h1><p class="profile-title-text">${data.title || ''}</p></div>`;
    if (main) main.innerHTML = `<div class="profile-section">${data.bodyHtml || ''}</div>`;
    if (sidebar) sidebar.innerHTML = `<div class="sidebar-card"><h3>Contact</h3>${data.email ? `<a href="mailto:${esc(data.email)}">${esc(data.email)}</a>` : ''}${data.phone ? `<p>${esc(data.phone)}</p>` : ''}${data.office ? `<p>${esc(data.office)}</p>` : ''}${data.website ? `<a href="${esc(data.website)}" target="_blank" rel="noopener">Personal Website</a>` : ''}</div>`;
  }

  const renderers = { 'zh-index': renderZhIndex, 'zh-profile': renderZhProfile, 'zh-category': renderZhCategory, 'en-index': renderEnIndex, 'en-profile': renderEnProfile };
  if (renderers[kind]) renderers[kind]().catch(error => {
    console.error(error);
    // The generated HTML remains visible as the offline fallback.
  });
})();
