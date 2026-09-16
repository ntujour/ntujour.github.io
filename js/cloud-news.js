(function () {
    'use strict';
    const BASE = 'https://storage.googleapis.com/ntujour-graduate/news/v1/';
    const scriptUrl = document.currentScript && document.currentScript.src
        ? document.currentScript.src
        : window.location.href;
    const siteBase = new URL('../', scriptUrl);

    function siteAssetUrl(value) {
        const clean = String(value || '').trim();
        if (/^\/images\//i.test(clean)) {
            return new URL(clean.slice(1), siteBase).href;
        }
        return clean;
    }

    function normalizeBodyImages(value) {
        return String(value || '').replace(
            /(\bsrc\s*=\s*["'])\/images\//gi,
            `$1${siteBase.href}images/`,
        );
    }

    function tags(value) {
        if (Array.isArray(value)) return value;
        return String(value || '').split(/[、,\n]+/).map(v => v.trim().replace(/^#/, '')).filter(Boolean);
    }

    function normalize(item) {
        const content = item.content || item.content_html || item.bodyHtml || '';
        return {
            ...item,
            hashtags: item.hashtags || tags(item.tag),
            image: siteAssetUrl(item.image),
            gallery_images: Array.isArray(item.gallery_images)
                ? item.gallery_images.map(siteAssetUrl)
                : item.gallery_images,
            gallery_images_crop: item.gallery_images_crop || {},
            image_crop: item.image_crop || {},
            content: normalizeBodyImages(content),
            external_url: item.external_url || item.externalUrl || '',
        };
    }

    async function requestJson(url, options) {
        const response = await fetch(url, options);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    }

    async function releaseInfo() {
        const pointer = await requestJson(BASE + 'current.json', {cache: 'no-store'});
        if (!/^[a-f0-9]{64}$/.test(pointer.release || '')) throw new Error('Invalid news release');
        return pointer.release;
    }

    async function loadIndex(lang, fallbackUrl, collection = 'news') {
        try {
            const release = await releaseInfo();
            const filename = collection === 'news' ? `index.${lang}.json` : `index.${collection}.${lang}.json`;
            const data = await requestJson(`${BASE}releases/${release}/${filename}`);
            if (!Array.isArray(data.items)) throw new Error('Invalid news index');
            return data.items.map(normalize);
        } catch (error) {
            console.warn('Cloud news unavailable; using the built-in copy.', error);
            if (!fallbackUrl) throw error;
            const local = await requestJson(fallbackUrl, {cache: 'no-cache'});
            return (Array.isArray(local) ? local : local.items || []).map(normalize);
        }
    }

    async function loadDetail(lang, id, fallbackUrl) {
        try {
            const release = await releaseInfo();
            return normalize(await requestJson(`${BASE}releases/${release}/${encodeURIComponent(id)}.${lang}.json`));
        } catch (error) {
            console.warn('Cloud news detail unavailable; using the built-in copy.', error);
            if (!fallbackUrl) throw error;
            const local = await requestJson(fallbackUrl, {cache: 'no-cache'});
            const item = (Array.isArray(local) ? local : local.items || []).find(value => value.id === id);
            if (!item) throw error;
            return normalize(item);
        }
    }

    window.NTUJourNews = {BASE, loadIndex, loadDetail};
})();
