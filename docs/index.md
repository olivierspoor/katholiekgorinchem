---
title: Home
hide:
  - navigation
  - footer
  - toc
---
<style>
  .md-meta__list {
  display: flex !important;
  }
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"><section class="activiteiten">

<div class="hero-banner">
  <h1 class="hero-title">Welkom bij de parochie van de Heilige Martelaren van Gorcum</h1>
  
  <div class="hero-badge">
    <span id="next-mass-display">...laden...</span>
  </div>
</div>

<div class="mis-balk" onclick="location.href='/liturgischeagenda.html'" style="cursor:pointer;">
  <div id="homeIcon" class="icoon">
    <i class="fa-solid fa-church" style="color:#000;"></i>
  </div>

<div class="mis-tekst"> 
<strong>Wekelijkse Eucharistievieringen:</strong> 
Zondag 11:00 |<span class="mobile-label"></span> 
Woensdag 10:00 |<span class="mobile-label"></span> 
Vrijdag 10:00 </div>
</div>

## Laatste berichten
<div id="latest-posts">Loading...</div>

<script>
(async function() {
  try {
    const parser = new DOMParser();
    const container = document.getElementById('latest-posts');
    if (!container) return;

    container.innerHTML = '';

    // Fetch both sources at once
    const [berichtenResp, artikelenResp] = await Promise.all([
      fetch('berichten/index.html'),
      fetch('artikelen/index.html')
    ]);

    const [berichtenHtml, artikelenHtml] = await Promise.all([
      berichtenResp.text(),
      artikelenResp.text()
    ]);

    const berichtenDoc = parser.parseFromString(berichtenHtml, 'text/html');
    const artikelenDoc = parser.parseFromString(artikelenHtml, 'text/html');

    const berichten = Array.from(berichtenDoc.querySelectorAll('article.md-post')).slice(0, 3);
    const artikelen = Array.from(artikelenDoc.querySelectorAll('article.md-post')).slice(0, 1);

    if (berichten.length === 0 && artikelen.length === 0) {
      container.textContent = 'Geen berichten of artikelen gevonden';
      return;
    }

    function normalizeLinks(node, basePath) {
      node.querySelectorAll('a').forEach(a => {
        const href = a.getAttribute('href') || '';
        if (/^(https?:|mailto:|tel:|#)/i.test(href)) return;
        if (href.startsWith(basePath)) return;

        const clean = href.replace(/^\.?\/+/, '');
        a.setAttribute('href', basePath + clean);
      });
    }

    function removeScripts(node) {
      node.querySelectorAll('script').forEach(s => s.remove());
    }

    function injectAuthor(node) {
      const img = node.querySelector(".md-author img");
      if (!img) return;

      const alt = img.getAttribute("alt");
      if (!alt) return;

      const metaList = node.querySelector(".md-meta__list");
      if (!metaList) return;

      // Prevent duplicates
      if (metaList.querySelector(".author-injected")) return;

      const li = document.createElement("li");
      li.className = "md-meta__item author-injected";
      li.textContent = alt;

      // Add as FIRST item
      metaList.insertBefore(li, metaList.firstElementChild);
    }

    function addReadMoreButton(node) {
      const button = document.createElement('a');
      button.className = 'buttonAlle';
      button.textContent = 'Alle artikelen';
      button.href = '/artikelen/index.html';

      const wrapper = document.createElement('p');
      wrapper.appendChild(button);
      node.appendChild(wrapper);
    }

    function append(node) {
      container.appendChild(node);
    }

    // 1. First bericht
    if (berichten[0]) {
      const b0 = berichten[0].cloneNode(true);
      normalizeLinks(b0, '/berichten/');
      removeScripts(b0);
      injectAuthor(b0);
      append(b0);
    }

    // 2. Featured artikel
    if (artikelen[0]) {
      const a0 = artikelen[0].cloneNode(true);
      a0.classList.add('featured-artikel');

      const heading = document.createElement('h2');
      heading.textContent = 'Laatste artikel';
      a0.prepend(heading);

      normalizeLinks(a0, '/artikelen/');
      removeScripts(a0);
      injectAuthor(a0);
      addReadMoreButton(a0);

      append(a0);
    }

    // 3. Remaining berichten
    [1, 2].forEach(i => {
      if (berichten[i]) {
        const b = berichten[i].cloneNode(true);
        normalizeLinks(b, '/berichten/');
        removeScripts(b);
        injectAuthor(b);
        append(b);
      }
    });

  } catch (err) {
    console.error(err);
    const container = document.getElementById('latest-posts');
    if (container) container.textContent = 'Fout bij laden inhoud';
  }
})();
</script>


<a href="/berichten/index.html" class="button" >Alle berichten</a>
---

## Over RK Gorinchem
<div class="homepage-intro">
<p style="text-align: justify;">De parochie van Gorinchem heeft de <a href="/artikelen/de-martelaren-van-gorcum.html">Heilige Martelaren van Gorcum</a> als patronen. Zij vormt met de parochie de <a href="http://heiligedrieeenheid.eu" target="_blank" rel="noopener">Heilige Drie-eenheid</a> de federatie het <a href="/overons.html#het-driestromenland">Driestromenland</a>. Beide parochies behoren tot het <a href="https://www.bisdomrotterdam.nl/">bisdom Rotterdam</a>.</p>
<span class="divider"></span>
<p>De parochie wil de missie tot uitvoer brengen. In woord en daad wil zij Christus verkondigen in deze maatschappij. Het is en blijft de droom van de <strong>Katholieke Kerk</strong> dat steeds meer mensen Christus leren kennen als fundament in hun leven. Het ideaal van het pastoraal team is dat parochies gelovige, liefdevolle en geëngageerde gemeenschappen zijn.</p>
    <p><a href="overons.html" class="button">Doorgaan met lezen →</a></p>

</div>
