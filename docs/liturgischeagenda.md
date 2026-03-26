---
hide:
  - navigation
  - footer
  - toc
---
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>
/* Container */
.agenda-container {
  margin: 0 auto;
}
.agenda-section h2 {
  color: var(--primary-color);
}
.agenda-section h2 i {
  padding-right:10px;
  color: var(--primary-color); /* match your purple */
}

/* WEEKLY GRID */
.weekly-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.mass-card {
  background: color-mix(in srgb, var(--primary-color) 10%, white);;
  border-radius: 14px;
  padding: 20px;
  display: flex;
  gap: 15px;
  align-items: flex-start;
  box-shadow:0 4px 12px rgba(0,0,0,0.06);
  transition: 0.2s ease;
}
.mass-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 22px rgba(0,0,0,0.06);
}
.mass-card .icon {
  font-size: 1.4rem;
  color: var(--primary-color);
}
.mass-card .day {
  font-weight: 600;
  font-size: 1.1rem;
}
.mass-card .time {
  font-size: 1.2rem;
}
.mass-card .extra {
  font-size: 0.8rem;
  color: #666;
}

/* EVENT LIST */
.event-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.event-item {
  display: flex;
  gap: 15px;
  align-items: center;
  background: #fff;
  padding: 14px 16px;
  border-radius: 12px;
  box-shadow:0 4px 12px rgba(0,0,0,0.06);
  transition: 0.2s ease;
}
.event-item:hover {
  transform: translateX(4px);
  box-shadow: 0 10px 22px rgba(0,0,0,0.06);
}

/* Date block */
.date {
  min-width: 55px;
  text-align: center;
  background-color:#fff;
  border-radius: 10px;
  padding: 6px 0;
}
.date .day {
  font-weight: 700;
  font-size: 1.2rem;
}

.date .month {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #777;
}

/* Event details */
.details .title {
  font-weight: 600;
  margin-bottom: 2px;
}
.details .meta {
  font-size: 0.85rem;
  color: #666;
}


/* ROSTER LINK */
.rooster-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
  transition: 0.2s;
}
.rooster-link:hover {
  gap: 12px;
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .weekly-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 600px) {
  .weekly-grid {
    grid-template-columns: 1fr;
  }
  .page-title {
    font-size: 2rem;
  }
  .agenda-section h2 {
    font-size: 1.3em;
  } 
}
  </style>

<div class="agenda-container">

  <h1 class="page-title">Liturgische Agenda</h1>

  <!-- WEEKLY MASSES -->
  <section class="agenda-section">
    <h2><i class="fa-solid fa-calendar-week"></i> Wekelijkse Eucharistievieringen</h2>

    <div class="weekly-grid">
      
      <div class="mass-card">
        <div class="icon"><i class="fa-solid fa-church"></i></div>
        <div class="content">
          <div class="day">Zondag</div>
          <div class="time">11:00</div>
          <div class="extra">Koffie na de mis: <span class='mobile-break'></span>Elke 2e en 4e zondag van de maand.</div>
        </div>
      </div>

      <div class="mass-card">
        <div class="icon"><i class="fa-solid fa-church"></i></div>
        <div class="content">
          <div class="day">Woensdag</div>
          <div class="time">10:00</div>
          <div class="extra">Aanbidding: <span class='mobile-break'></span>elke 1e woensdag van de maand.</div>
        </div>
      </div>

      <div class="mass-card">
        <div class="icon"><i class="fa-solid fa-church"></i></div>
        <div class="content">
          <div class="day">Vrijdag</div>
          <div class="time">10:00</div>
          <div class="extra"></div>
        </div>
      </div>

    </div>
  </section>

  <!-- FEASTS -->
  <section class="agenda-section">
    <h2><i class="fa-solid fa-cross"></i> Feesten en gedachtenissen</h2>

    <div class="event-list">

      <div class="event-item" style="background-color: #ffe5e8; border-left: 4px solid #B11226;">
        <div class="date">
          <div class="day" style="color: #B11226;">29</div>
          <div class="month" style="color: #B11226;">mrt</div>
        </div>
        <div class="details">
          <div class="title">Palmzondag</div>
          <div class="meta">zondag • 11:00</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #ffe5e8; border-left: 4px solid #B11226;">
        <div class="date">
          <div class="day" style="color: #B11226;">3</div>
          <div class="month" style="color: #B11226;">apr</div>
        </div>
        <div class="details">
          <div class="title">Kruisweg (Goede Vrijdag)</div>
          <div class="meta">vrijdag • 15:00</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #ffe5e8; border-left: 4px solid #B11226;">
        <div class="date">
          <div class="day" style="color: #B11226;">3</div>
          <div class="month" style="color: #B11226;">apr</div>
        </div>
        <div class="details">
          <div class="title">Kruisverering (Goede Vrijdag)</div>
          <div class="meta">vrijdag • 19:00</div>
        </div>
      </div>

    <div class="event-item" style="background-color: #fffef2; border-left: 4px solid #dcc600;">
      <div class="date">
        <div class="day">4</div>
        <div class="month">apr</div>
        </div>
        <div class="details">
          <div class="title">Paaswake</div>
          <div class="meta">zaterdag • 21:00</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #fffef2; border-left: 4px solid #dcc600;">
        <div class="date">
          <div class="day">5</div>
          <div class="month">apr</div>
        </div>
        <div class="details">
          <div class="title">Paaszondag</div>
          <div class="meta">zondag • 10:00</div>
        </div>
      </div>

    </div>
  </section>

  <!-- BIBLE STUDY -->
  <section class="agenda-section">
    <h2><i class="fa-solid fa-book-bible"></i> Bijbelcursus en catechese</h2>

    <div class="event-list">

      <div class="event-item" style="background-color: #f7f3ff; border-left: 4px solid #5A2A82;">
        <div class="date">
          <div class="day" style="color: #5A2A82;">2</div>
          <div class="month" style="color: #5A2A82;">mrt</div>
        </div>
        <div class="details">
          <div class="title">Bijbelcursus</div>
          <div class="meta">Maandag • 19:30 • <span class='mobile-break'></span>mw. Van den Akker-Savelsbergh</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #f7f3ff; border-left: 4px solid #5A2A82;">
        <div class="date">
          <div class="day" style="color: #5A2A82;">16</div>
          <div class="month" style="color: #5A2A82;">mrt</div>
        </div>
        <div class="details">
          <div class="title">Docat</div>
          <div class="meta">Maandag • 19:30 • <span class='mobile-break'></span>pastoor Meijer</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #f7f3ff; border-left: 4px solid #5A2A82;">
        <div class="date">
          <div class="day" style="color: #5A2A82;">30</div>
          <div class="month" style="color: #5A2A82;">mrt</div>
        </div>
        <div class="details">
          <div class="title">Bijbelcursus</div>
          <div class="meta">Maandag • 19:30 • <span class='mobile-break'></span>mw. Van den Akker-Savelsbergh</div>
        </div>
      </div>

      <div class="event-item" style="background-color: #fffef2; border-left: 4px solid #dcc600;">
        <div class="date">
          <div class="day">13</div>
          <div class="month">apr</div>
        </div>
        <div class="details">
          <div class="title">Docat</div>
          <div class="meta">Maandag • 19:30 • <span class='mobile-break'></span>pastoor Meijer</div>
        </div>
    </div>

    </div>
  </section>


  <!-- ROSTERS -->
  <section class="agenda-section">
    <h2><i class="fa-solid fa-list"></i> Roosters</h2>

    <a href="/roosters" class="rooster-link">
      Bekijk de roosters <i class="fa-solid fa-arrow-right"></i>
    </a>
  </section>

</div>