/**
 * Banner 動態載入腳本
 * 根據當前語言從 _data/banner.json 載入並渲染 Banner 內容
 */

(function() {
  'use strict';

  /**
   * 偵測當前頁面語言
   * @returns {string} 'en' 或 'zh'
   */
  function detectLanguage() {
    const path = window.location.pathname;
    return path.startsWith('/en/') ? 'en' : 'zh';
  }

  /**
   * 計算 banner.json 的相對路徑
   * @returns {string} banner.json 的路徑
   */
  function getBannerDataPath() {
    const path = window.location.pathname;
    const depth = (path.match(/\//g) || []).length - 1;
    
    // 根目錄頁面
    if (depth === 0 || path === '/' || path === '/index.html') {
      return './_data/banner.json';
    }
    
    // 計算需要幾個 ../
    const prefix = '../'.repeat(depth);
    return `${prefix}_data/banner.json`;
  }

  /**
   * 計算首頁連結
   * @returns {string} 首頁 URL
   */
  function getHomeUrl() {
    const path = window.location.pathname;
    const depth = (path.match(/\//g) || []).length - 1;
    
    if (depth === 0 || path === '/' || path === '/index.html') {
      return 'index.html';
    }
    
    const isEnglish = path.startsWith('/en/');
    const prefix = '../'.repeat(depth);
    
    return isEnglish ? `${prefix}index.html` : `${prefix}index.html`;
  }

  /**
   * 計算英文首頁連結
   * @returns {string} 英文首頁 URL
   */
  function getEnglishUrl() {
    const path = window.location.pathname;
    const depth = (path.match(/\//g) || []).length - 1;

    if (depth === 0 || path === '/' || path === '/index.html') {
      return 'en/index.html';
    }

    const prefix = '../'.repeat(depth);
    return `${prefix}en/index.html`;
  }

  /**
   * 載入並渲染 Banner
   */
  async function loadBanner() {
    const banner = document.querySelector('.site-banner');
    if (!banner) {
      console.warn('Banner container not found');
      return;
    }

    try {
      const dataPath = getBannerDataPath();
      const response = await fetch(dataPath);
      
      if (!response.ok) {
        throw new Error(`Failed to load banner data: ${response.status}`);
      }
      
      const data = await response.json();
      const lang = detectLanguage();
      const homeUrl = getHomeUrl();
      const titleZh = data.title_zh || data.title || '國立臺灣大學新聞研究所';
      const titleEn = data.title_en || 'Graduate Institute of Journalism, National Taiwan University';
      const subtitleZh = data.subtitle_zh || data.subtitle || '培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才';
      const subtitleEn = data.subtitle_en || 'Cultivating journalism and communication talent for the new era through a balance of theory and practice, with professional knowledge and critical thinking.';
      const title = lang === 'en' ? titleEn : titleZh;
      const altTitle = lang === 'en' ? titleZh : titleEn;
      const subtitle = lang === 'en' ? subtitleEn : subtitleZh;
      const showLogo = Boolean(data.logo) && data.show_logo !== false;
      const englishUrl = getEnglishUrl();
      const logoHtml = showLogo
        ? `<a class="site-banner-logo-link" href="${homeUrl}" aria-label="${titleZh}">
            <img src="${data.logo}" alt="${titleZh}" class="site-banner-logo">
          </a>`
        : '';

      banner.innerHTML = `
        <div class="container-1200">
          <div class="site-banner-shell${showLogo ? ' has-logo' : ''}">
            <div class="site-banner-brand">
              ${logoHtml}
              <div class="site-banner-copy">
                <h1 class="site-banner-title">
                  <a href="${homeUrl}" class="site-banner-title-link">
                    ${title}
                  </a>
                </h1>
                <p class="site-banner-english">${altTitle}</p>
                <p class="site-banner-subtitle">${subtitle}</p>
              </div>
            </div>
            <a class="site-banner-english-link" href="${englishUrl}" target="_blank" rel="noopener noreferrer">English</a>
          </div>
        </div>
      `;
      
    } catch (error) {
      console.error('Error loading banner:', error);
      
      // 降級方案：使用預設內容
      const lang = detectLanguage();
      const homeUrl = getHomeUrl();
      const titleZh = '國立臺灣大學新聞研究所';
      const titleEn = 'Graduate Institute of Journalism, National Taiwan University';
      const subtitleZh = '培育新時代新聞傳播人才｜結合理論與實務，培養具有專業知識與批判思考能力的新聞傳播專業人才';
      const subtitleEn = 'Cultivating journalism and communication talent for the new era through a balance of theory and practice, with professional knowledge and critical thinking.';
      const title = lang === 'en' ? titleEn : titleZh;
      const altTitle = lang === 'en' ? titleZh : titleEn;
      const subtitle = lang === 'en' ? subtitleEn : subtitleZh;
      const englishUrl = getEnglishUrl();
      
      banner.innerHTML = `
        <div class="container-1200">
          <div class="site-banner-shell">
            <div class="site-banner-brand">
              <div class="site-banner-copy">
                <h1 class="site-banner-title">
                  <a href="${homeUrl}" class="site-banner-title-link">
                    ${title}
                  </a>
                </h1>
                <p class="site-banner-english">${altTitle}</p>
                <p class="site-banner-subtitle">${subtitle}</p>
              </div>
            </div>
            <a class="site-banner-english-link" href="${englishUrl}" target="_blank" rel="noopener noreferrer">English</a>
          </div>
        </div>
      `;
    }
  }

  // 頁面載入完成後執行
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadBanner);
  } else {
    loadBanner();
  }

})();
