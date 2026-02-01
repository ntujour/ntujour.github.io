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
      
      // 根據語言選擇對應內容
      const title = lang === 'en' ? data.title_en : data.title_zh;
      const subtitle = lang === 'en' ? data.subtitle_en : data.subtitle_zh;
      const altTitle = lang === 'en' ? data.title_zh : data.title_en; // 顯示另一種語言
      
      // 渲染 Banner HTML
      banner.innerHTML = `
        <div class="container-1200">
          ${data.logo ? `<img src="${data.logo}" alt="Logo" class="mb-3" style="max-height: 60px;">` : ''}
          <h1 class="text-4xl font-bold text-gray-800 mb-2">
            <a href="${homeUrl}" 
               class="hover:text-gray-600 transition" 
               style="text-decoration: none; color: inherit;">
              ${title}
            </a>
          </h1>
          <p class="text-gray-700 text-base mb-1">${altTitle}</p>
          <p class="text-gray-600 text-base">${subtitle}</p>
        </div>
      `;
      
    } catch (error) {
      console.error('Error loading banner:', error);
      
      // 降級方案：使用預設內容
      const lang = detectLanguage();
      const homeUrl = getHomeUrl();
      
      banner.innerHTML = `
        <div class="container-1200">
          <h1 class="text-4xl font-bold text-gray-800 mb-2">
            <a href="${homeUrl}" 
               class="hover:text-gray-600 transition" 
               style="text-decoration: none; color: inherit;">
              ${lang === 'en' 
                ? 'Graduate Institute of Journalism, National Taiwan University' 
                : '國立臺灣大學新聞研究所'}
            </a>
          </h1>
          <p class="text-gray-700 text-base mb-1">
            ${lang === 'en' 
              ? '國立臺灣大學新聞研究所' 
              : 'Graduate Institute of Journalism, National Taiwan University'}
          </p>
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
