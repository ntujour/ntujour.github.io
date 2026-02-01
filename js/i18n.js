/**
 * 多語言支援腳本
 * 提供語言偵測和切換功能
 */

(function () {
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
     * 切換語言
     * @param {string} targetLang - 目標語言 ('en' 或 'zh')
     */
    function switchLanguage(targetLang) {
        const currentPath = window.location.pathname;
        const currentLang = detectLanguage();

        // 如果已經是目標語言，不做任何事
        if (currentLang === targetLang) {
            return;
        }

        let newPath;

        if (targetLang === 'en' && currentLang === 'zh') {
            // 中文切換到英文
            if (currentPath === '/' || currentPath === '/index.html') {
                newPath = '/en/index.html';
            } else {
                newPath = '/en' + currentPath;
            }
        } else if (targetLang === 'zh' && currentLang === 'en') {
            // 英文切換到中文
            newPath = currentPath.replace('/en/', '/').replace('/en', '/');
            if (newPath === '/') {
                newPath = '/index.html';
            }
        }

        if (newPath) {
            window.location.href = newPath;
        }
    }

    /**
     * 初始化語言切換器
     */
    function initLanguageSwitcher() {
        const currentLang = detectLanguage();

        // 更新所有語言切換連結
        document.querySelectorAll('[data-lang-switch]').forEach(link => {
            const targetLang = link.getAttribute('data-lang-switch');

            // 標記當前語言
            if (targetLang === currentLang) {
                link.classList.add('active');
                link.setAttribute('aria-current', 'true');
            } else {
                link.classList.remove('active');
                link.removeAttribute('aria-current');
            }

            // 綁定點擊事件
            link.addEventListener('click', (e) => {
                e.preventDefault();
                switchLanguage(targetLang);
            });
        });
    }

    /**
     * 生成對應語言的 URL
     * @param {string} currentPath - 當前路徑
     * @param {string} targetLang - 目標語言
     * @returns {string} 對應語言的 URL
     */
    function getAlternateUrl(currentPath, targetLang) {
        const currentLang = detectLanguage();

        if (currentLang === targetLang) {
            return currentPath;
        }

        if (targetLang === 'en') {
            return '/en' + (currentPath === '/' ? '/index.html' : currentPath);
        } else {
            return currentPath.replace('/en/', '/').replace('/en', '/');
        }
    }

    /**
     * 添加 hreflang 標籤（SEO 優化）
     */
    function addHreflangTags() {
        const currentPath = window.location.pathname;
        const baseUrl = window.location.origin;

        const zhUrl = baseUrl + getAlternateUrl(currentPath, 'zh');
        const enUrl = baseUrl + getAlternateUrl(currentPath, 'en');

        // 移除現有的 hreflang 標籤
        document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(link => {
            link.remove();
        });

        // 添加新的 hreflang 標籤
        const head = document.head;

        const zhLink = document.createElement('link');
        zhLink.rel = 'alternate';
        zhLink.hreflang = 'zh-TW';
        zhLink.href = zhUrl;
        head.appendChild(zhLink);

        const enLink = document.createElement('link');
        enLink.rel = 'alternate';
        enLink.hreflang = 'en';
        enLink.href = enUrl;
        head.appendChild(enLink);

        const defaultLink = document.createElement('link');
        defaultLink.rel = 'alternate';
        defaultLink.hreflang = 'x-default';
        defaultLink.href = zhUrl;
        head.appendChild(defaultLink);
    }

    /**
     * 更新頁面 lang 屬性
     */
    function updateHtmlLang() {
        const lang = detectLanguage();
        document.documentElement.lang = lang === 'en' ? 'en' : 'zh-TW';
    }

    /**
     * 初始化
     */
    function init() {
        updateHtmlLang();
        initLanguageSwitcher();
        addHreflangTags();
    }

    // 頁面載入完成後執行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // 導出到全域（方便其他腳本使用）
    window.i18n = {
        detectLanguage,
        switchLanguage,
        getAlternateUrl
    };

})();
