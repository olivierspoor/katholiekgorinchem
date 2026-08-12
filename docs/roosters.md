---
hide:
  - navigation
  - footer
  - toc
---

# Roosters

<script>
// Freeze "today" to any date you want
// const RealDate = Date;
// Date = class extends RealDate {
//   constructor(...args) {
//     if (args.length === 0) return super(2026, 7, 17); // month is 0-based, so 5 = June
//     return super(...args);
//   }
// };
// console.log(new Date().toLocaleDateString('nl-NL', { day: 'numeric', month: 'long', year: 'numeric' }));

document.addEventListener("DOMContentLoaded", function () {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // Step 1: hide all past rows
  document.querySelectorAll(".schedule-row[data-date]").forEach(row => {
    const d = new Date(row.getAttribute("data-date"));
    d.setHours(0, 0, 0, 0);
    if (d < today) row.style.display = "none";
  });

  // Step 2: find months that still have at least one visible upcoming row
  const months = Array.from(document.querySelectorAll(".schedule-month[data-date]"));
  const monthsWithUpcoming = months.filter(month => {
    return Array.from(month.querySelectorAll(".schedule-row[data-date]"))
      .some(row => row.style.display !== "none");
  });

  // Step 3: show the first 2 months that have upcoming dates; hide the rest
  months.forEach(month => month.style.display = "none");
  monthsWithUpcoming.slice(0, 2).forEach(month => month.style.display = "");

  // Step 4: "Load more" reveals everything and unhides past rows
  const btn = document.getElementById("show-more-roosters");
  if (btn) {
    btn.addEventListener("click", function () {
      months.forEach(month => month.style.display = "");
      document.querySelectorAll(".schedule-row[data-date]").forEach(row => {
        row.style.display = "";
      });
      btn.remove();
    });
  }
});
</script>

<div class="schedule-board">
  <div class="schedule-month"  data-date="2026-05-01">
    <h2 class="month-title">Mei 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row gold" data-date="2026-05-03">
        <div>Zondag 3 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">K. Orfaly</div>
        <div data-label="Misdienaars">Asaira,<br> Adriana,<br> Melanie en<br> Savyo</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-05-10">
        <div>Zondag 10 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Arthur,<br> Yfke,<br> Khaled en<br> Marcos</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Jocelyn en Corien</div>
      </div>

      <div class="schedule-row gold" data-date="2026-05-14">
        <div>Donderdag 14 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Hemelvaartsdag</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Asaira,<br> Reinilde en<br> Yfke</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-05-17">
        <div>Zondag 17 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Gruiters</div>
        <div data-label="Misdienaars">Asaira,<br> Destiny,<br> Reinilde en<br> Daniel</div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row red" data-date="2026-05-24">
        <div>Zondag 24 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Pinksteren</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Yfke,<br> Adriana,<br> Melanie en<br> Chisom</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Rood</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee">Marijke en Gerlinde</div>
      </div>

      <div class="schedule-row gold" data-date="2026-05-31">
        <div>Zondag 31 mei <span class='desktop-break'></span>11:00</div>
        <div data-label="Bijzonderheden">Heilige Drieëenheid</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Arthur,<br> Destiny,<br> Savyo en<br> Marcos</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

    </div>
  </div>

  <div class="schedule-month" data-date="2026-06-01">
    <h2 class="month-title">Juni 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row gold" data-date="2026-06-07">
        <div>Zondag 7 juni <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Sacramentsdag</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Arthur,<br> Adriana,<br> Savyo en<br> Chisom</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-06-14">
      <div>Zondag 14 juni <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">K. Orfaly</div>
        <div data-label="Misdienaars">Yfke,<br> Asaira,<br> Khaled en<br> Marcos</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Teresa en Jocelyn</div>
    </div>

    <div class="schedule-row green" data-date="2026-06-21">
      <div>Zondag 21 juni <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Arthur,<br> Destiny,<br> Khaled en<br> Daniel</div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-06-28">
      <div>Zondag 28 juni <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Asaira,<br> Adriana,<br> Melanie en<br> Savyo</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Fadia en Corien</div>
    </div>

    </div>
  </div>


  <div class="schedule-month" data-date="2026-07-01">
    <h2 class="month-title">Juli 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row green" data-date="2026-07-05">
        <div>Zondag 5 juli <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">K. Orfaly</div>
        <div data-label="Misdienaars">Arthur,<br> Destiny,<br> Chisom en<br> Marcos</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee"></div>
    </div>

    <div class="schedule-row green" data-date="2026-07-12">
      <div>Zondag 12 juli <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">V. Osterhaus</div>
        <div data-label="Misdienaars">Yfke,<br> Asaira,<br> Reinilde en<br> Khaled</div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Gerlinde en Jocelyn</div>
    </div>

    <div class="schedule-row green" data-date="2026-07-19">
      <div>Zondag 19 juli <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Adriana,<br> Destiny,<br> Savyo en<br> Marcos</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-07-26">
      <div>Zondag 26 juli <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">V. Osterhaus</div>
        <div data-label="Misdienaars">Yfke,<br> Adriana,<br> Khaled en<br> Chisom</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Corien en Carolien</div>
    </div>

    </div>
  </div>



</div>
  <div class="schedule-month" data-date="2026-08-01">
    <h2 class="month-title">Augustus 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row green" data-date="2026-08-02">
        <div>Zondag 2 augustus <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">V. Osterhaus</div>
        <div data-label="Misdienaars">Destiny, <br>Melanie en <br>Chisom</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-08-09">
      <div>Zondag 9 augustus <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Asaira, <br>Destiny, <br>Daniel en <br>Marcos</div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Fadia en Corien</div>
    </div>

    <div class="schedule-row green" data-date="2026-08-16">
      <div>Zondag 16 augustus <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Maria Tenhemelopneming</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Arthur, <br>Adriana, <br>Chisom en <br>Savyo</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-08-23">
      <div>Zondag 23 augustus <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">V. Osterhaus</div>
        <div data-label="Misdienaars">Asaira, <br>Destiny, <br>Daniel en <br>Marcos</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Carolien en Gerlinde</div>
    </div>

    <div class="schedule-row green" data-date="2026-08-30">
      <div>Zondag 30 augustus <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Arthur, <br>Yfke, <br>Reinilde en <br>Chisom</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    </div>
  </div>

  <div class="schedule-month" data-date="2026-09-01">
    <h2 class="month-title">September 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row green" data-date="2026-09-06">
        <div>Zondag 6 september <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Klaver</div>
        <div data-label="Misdienaars">Asaira, <br>Adriana, <br>Melanie en <br>Savyo</div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-09-13">
      <div>Zondag 13 september <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars">Yfke, <br>Destiny, <br>Daniel en <br>Marcos</div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Jocelyn en Carolien</div>
    </div>

    <div class="schedule-row green" data-date="2026-09-20">
      <div>Zondag 20 september <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">L. Ekelmans</div>
        <div data-label="Misdienaars">Arthur, <br>Adriana, <br>Chisom en <br>Savyo</div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee">-</div>
    </div>

    <div class="schedule-row green" data-date="2026-09-27">
      <div>Zondag 27 september <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars">Yfke, <br>Asaira, <br>Melanie en <br>Marcos</div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Teresa en Fadia</div>
    </div>

    </div>
  </div>

  <div class="schedule-month" data-date="2026-10-01">
    <h2 class="month-title">Oktober 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row green" data-date="2026-10-04">
        <div>Zondag 4 oktober <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">V. Osterhaus</div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row green" data-date="2026-10-11">
        <div>Zondag 11 oktober <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">L. Ekelmans</div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Marijke en Jocelyn</div>
      </div>

      <div class="schedule-row green" data-date="2026-10-18">
        <div>Zondag 18 oktober <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">A. Bakker</div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">A. v d Diepstraten</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row green" data-date="2026-10-25">
        <div>Zondag 25 oktober <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren">H. Gruiters</div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Marijke en Ela</div>
      </div>

    </div>
  </div>

  <div class="schedule-month" data-date="2026-11-01">
    <h2 class="month-title">November 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row gold" data-date="2026-11-01">
        <div>Zondag 1 november <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Allerheiligen</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row green" data-date="2026-11-08">
        <div>Zondag 8 november <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Teresa en Gerlinde</div>
      </div>

      <div class="schedule-row green" data-date="2026-11-15">
        <div>Zondag 15 november <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eucharistieviering</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Groen</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-11-22">
        <div>Zondag 22 november <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Christus, <br>Koning van het heelal</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">A. v d Diepstraten</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee">Teresa en Gerlinde</div>
      </div>

      <div class="schedule-row purple" data-date="2026-11-29">
        <div>Zondag 29 november <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Eerste zondag <br>van de advent</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">K. Wirken</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Paars</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

    </div>
  </div>

  <div class="schedule-month" data-date="2026-12-01">
    <h2 class="month-title">December 2026</h2>

    <div class="schedule-table">

      <div class="schedule-row schedule-head">
        <div>Datum</div>
        <div>Bijzonderheden</div>
        <div>Lectoren</div>
        <div>Misdienaars</div>
        <div>Kosters</div>
        <div>Koor</div>
        <div>Koffie & Thee</div>
      </div>

      <div class="schedule-row purple" data-date="2026-12-06">
        <div>Zondag 6 december <span class='desktop-break'></span>11:00</div>
      	<div data-label="Bijzonderheden">Tweede zondag <br>van de advent</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Paars</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row rose" data-date="2026-12-13">
        <div>Zondag 13 december <span class='desktop-break'></span>11:00</div>
     	  <div data-label="Bijzonderheden">Derde zondag <br>van de advent</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Rose</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">Marijke en Ela</div>
      </div>

      <div class="schedule-row purple" data-date="2026-12-20">
        <div>Zondag 20 december <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Vierde zondag <br>van de advent</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Paars</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-12-24">
        <div>Donderdag 24 december <span class='desktop-break'></span>22:00</div>
    	  <div data-label="Bijzonderheden">Kerstnachtmis</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">K. Wirken /<br> J. van Oord</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">Intermezzo</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-12-25">
        <div>Vrijdag 25 december <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Kerstmis</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">E. van Es</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">Tutti</div>
        <div data-label="Koffie & Thee">-</div>
      </div>

      <div class="schedule-row gold" data-date="2026-12-27">
        <div>Zondag 27 december <span class='desktop-break'></span>11:00</div>
    	  <div data-label="Bijzonderheden">Heilige familie</div>
        <div data-label="Lectoren"></div>
        <div data-label="Misdienaars"></div>
        <div data-label="Kosters">I. Scarpa</div>       
        <div data-label="Liturgische kleur" class="mobile-label">Wit</div>
        <div data-label="Koor">-</div>
        <div data-label="Koffie & Thee">Corien en Fadia</div>
      </div>

    </div>
  </div>
  <div style="text-align:center; margin-top:20px;">
    <span id="show-more-roosters" class="button">Overige roosters</span>
  </div>
</div>
