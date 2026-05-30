/* faculty-profile.js
 * Fetches ../data/faculty/<SLUG>.json and renders the profile page.
 * Expects a global `const SLUG` to be defined before this script runs.
 */

(function () {
  'use strict';

  // --- SVG icons (14×14, stroke) ---
  const ICON_PHONE = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81a19.79 19.79 0 01-3.07-8.63A2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.09 6.09l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>`;
  const ICON_EMAIL = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>`;
  const ICON_WEB   = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>`;

  // HTML-escape for plain text values
  function esc(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function buildContacts(contacts) {
    return contacts.map(function (c) {
      if (c.type === 'phone') {
        return `<span class="profile-contact-item">${ICON_PHONE} ${esc(c.value)}</span>`;
      }
      if (c.type === 'email') {
        return `<span class="profile-contact-item">${ICON_EMAIL} <a href="mailto:${esc(c.value)}">${esc(c.value)}</a></span>`;
      }
      if (c.type === 'web') {
        return `<span class="profile-contact-item">${ICON_WEB} <a href="${esc(c.url)}" target="_blank" rel="noopener">${esc(c.text)}</a></span>`;
      }
      return '';
    }).join('\n');
  }

  function buildHeader(d) {
    const nameZhSpan = d.nameZh
      ? ` <span style="font-size:1.2rem;font-weight:400;opacity:0.7;">(${esc(d.nameZh)})</span>`
      : '';
    const photoStyle = d.placeholder ? '' : '';
    const placeholderStyle = d.placeholder ? 'display:none;' : 'display:none;';
    return `
      <div class="profile-photo-wrap">
        <img class="profile-photo-large" src="${esc(d.photo)}" alt="${esc(d.name)}">
        <div class="profile-placeholder-large" style="${placeholderStyle}">${esc(d.placeholder || '')}</div>
      </div>
      <div>
        <p class="profile-dept">Graduate Institute of Journalism · NTU</p>
        <h1 class="profile-name">${esc(d.name)}${nameZhSpan}</h1>
        <p class="profile-title-text">${d.title}</p>
        <div class="profile-contacts">
          ${buildContacts(d.contacts)}
        </div>
      </div>`;
  }

  function buildSections(sections) {
    return sections.map(function (s) {
      let body = '';
      if (s.type === 'list') {
        // Items may contain HTML (em, &amp; etc.) — inject as innerHTML
        body = '<ul>' + s.items.map(function (item) {
          return `<li>${item}</li>`;
        }).join('') + '</ul>';
      } else if (s.type === 'text') {
        body = `<p>${esc(s.content)}</p>`;
      }
      return `<div class="profile-section"><h2>${s.heading}</h2>${body}</div>`;
    }).join('\n');
  }

  function buildPills(arr) {
    if (!arr || arr.length === 0) return '';
    return arr.map(function (p) {
      return `<span class="research-pill">${p}</span>`;
    }).join('');
  }

  // Teaching Field + Research Interests pill strip (placed below profile-header)
  function buildMeta(d) {
    var sb = d.sidebar;
    var html = '<div class="profile-meta-inner">';

    if (sb.teachingField && sb.teachingField.length > 0) {
      html += `<div class="profile-meta-group">
        <div class="profile-meta-label">Teaching Field</div>
        <div class="profile-meta-pills">${buildPills(sb.teachingField)}</div>
      </div>`;
    }

    if (sb.researchInterests && sb.researchInterests.length > 0) {
      html += `<div class="profile-meta-group">
        <div class="profile-meta-label">Research Interests</div>
        <div class="profile-meta-pills">${buildPills(sb.researchInterests)}</div>
      </div>`;
    }

    html += '</div>';
    return html;
  }

  // Sidebar now only renders Contact + External Links
  function buildSidebar(sb) {
    var html = '';

    // Contact
    var contactBody = '';
    if (sb.contact.phone) {
      contactBody += `<p style="margin-bottom:0.25rem;">${esc(sb.contact.phone)}</p>`;
    }
    if (sb.contact.email) {
      contactBody += `<a href="mailto:${esc(sb.contact.email)}">${esc(sb.contact.email)}</a>`;
    }
    html += `<div class="sidebar-card"><h3>Contact</h3>${contactBody}</div>`;

    // External Links (only render if there are links)
    if (sb.externalLinks && sb.externalLinks.length > 0) {
      var linksBody = sb.externalLinks.map(function (l) {
        return `<a href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.text)}</a>`;
      }).join('<br>');
      html += `<div class="sidebar-card"><h3>External Links</h3>${linksBody}</div>`;
    }

    return html;
  }

  function render(d) {
    // Page title
    document.title = `${d.name} — Graduate Institute of Journalism, NTU`;

    // Breadcrumb name
    const bc = document.getElementById('breadcrumb-name');
    if (bc) bc.textContent = d.name;

    // Profile header
    var headerEl = document.getElementById('profile-header-inner');
    if (headerEl) headerEl.innerHTML = buildHeader(d);

    // Profile meta strip (Teaching Field + Research Interests)
    var metaEl = document.getElementById('profile-meta');
    if (metaEl) metaEl.innerHTML = buildMeta(d);

    // Profile main
    var mainEl = document.getElementById('profile-main');
    if (mainEl) mainEl.innerHTML = buildSections(d.sections);

    // Sidebar (Contact + External Links)
    var sidebarEl = document.getElementById('profile-sidebar');
    if (sidebarEl) sidebarEl.innerHTML = buildSidebar(d.sidebar);
  }

  // Fetch and render
  fetch(`../data/faculty/${SLUG}.json`)
    .then(function (r) {
      if (!r.ok) throw new Error('Failed to load faculty data: ' + r.status);
      return r.json();
    })
    .then(render)
    .catch(function (err) {
      console.error(err);
      const mainEl = document.getElementById('profile-main');
      if (mainEl) mainEl.innerHTML = '<p style="color:red;">Failed to load profile data.</p>';
    });
})();
