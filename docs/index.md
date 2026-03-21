---
title: Home
hide:
  - navigation
  - footer
  - toc
---
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
    const resp = await fetch('berichten/index.html');
    const html = await resp.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    // Pak de eerste 3 artikelen in de volgorde zoals op berichten/index.html
    const posts = Array.from(doc.querySelectorAll('article.md-post')).slice(0, 3);
    const container = document.getElementById('latest-posts');
    if (!container) return;
    container.innerHTML = '';

    if (posts.length === 0) {
      container.textContent = 'Geen berichten gevonden';
      return;
    }

    posts.forEach(post => {
      // Clone de volledige article node zodat titel, image en meta behouden blijven
      const cloned = post.cloneNode(true);

      // Pas relatieve links aan zodat ze naar /berichten/<slug>.html wijzen
      cloned.querySelectorAll('a').forEach(a => {
        const href = a.getAttribute('href') || '';
        // Laat absolute links, anchor-links en mailto/ tel door
        if (/^(https?:|mailto:|tel:|#)/i.test(href)) return;
        // Als het al begint met /berichten laat het zoals het is
        if (href.startsWith('/berichten')) return;
        // Normaliseer en prefix naar /berichten/
        const clean = href.replace(/^\.?\/+/, '');
        a.setAttribute('href', '/berichten/' + clean);
      });

      // Verwijder eventuele scripts uit de gekloonde inhoud, voor de veiligheid
      cloned.querySelectorAll('script').forEach(s => s.remove());

      // Voeg de gekloonde article toe aan de container
      container.appendChild(cloned);
    });
  } catch (err) {
    console.error(err);
    const container = document.getElementById('latest-posts');
    if (container) container.textContent = 'Fout bij laden berichten';
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