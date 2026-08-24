---
hide:
  - navigation
  - footer
  - toc
---
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"><section class="activiteiten">

<style>
.about-page{
max-width:1100px;
margin:auto;
}

/* header */
.about-header{
text-align:center;
margin-bottom:30px;
border-radius: 12px 0px 0px 12px;
}
.about-header h1{
font-size:38px;
margin-bottom:8px;
}
.subtitle{
color:#777;
font-size:18px;
}

/* cards */
.card{
background:white;
border-radius:12px;
padding:22px;
border-left:5px solid var(--primary-color);
box-shadow:0 4px 12px rgba(0,0,0,0.06);
}
.card h3{
  margin: 0px;
}

/* intro */
.about-intro{
width: 50%;
margin:0 0 30px 0;
}

/* grid */
.about-grid{
display:grid;
grid-template-columns:1.3fr 1fr;
gap:25px;
margin-bottom:30px;
}
.about-image img{
border-radius:12px;
width:50%;
float: right;
}
.mobile-image{
  display:none;
}
.mobile-image img{
  border-radius:12px;
}

/* quote */
.quote-block{
background:color-mix(in srgb, var(--primary-color) 10%, white);
border-left:5px solid var(--primary-color);
padding:22px;
border-radius:12px;
margin:40px 0;
font-style:italic;
display:flex;
gap:14px;
align-items:flex-start;
}
.quote-block i{
color:var(--primary-color);
font-size:22px;
}

/* sections */
.section{
margin-top:40px;
}
.section h2{
margin-bottom:14px;
}
#driestroom{
  display: flex;
  gap: 25px;
}
#driestroom img{
max-width:50%;
border-radius:12px;
}

/* bestuur banner */
.bestuur-banner{
display:flex;
align-items:center;
gap:20px;
background:#eae2df;
border-radius:12px;
padding:20px 25px;
text-decoration:none;
color:#333;
margin-top:20px;
transition:opacity 0.2s ease;
}
.bestuur-banner:hover{
opacity:0.85;
}
.bestuur-banner img{
width:90px;
height:90px;
min-width:90px;
border-radius:50%;
object-fit:cover;
}
.bestuur-banner p{
flex:1;
margin:0;
font-size:17px;
line-height:1.4;
}
.bestuur-banner .button{
flex-shrink:0;
margin-left:auto;
white-space:nowrap;
}
@media (max-width:800px){
  .bestuur-banner{
    flex-wrap:wrap;
    gap:15px;
    padding:15px;
  }
  .bestuur-banner img{
    width:65px;
    height:65px;
    min-width:65px;
  }
  .bestuur-banner p{
    flex:1 1 auto;
    font-size:15px;
  }
  .bestuur-banner .button{
    margin-left:0;
    width:100%;
    text-align:center;
  }
}

/* links */
.links-grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:15px;
margin-top:10px;
}
.link-card{
display:flex;
align-items:center;
gap:10px;
padding:14px;
background:white;
border-radius:12px;
box-shadow:0 3px 10px rgba(0,0,0,0.06);
text-decoration:none;
color:#333;
}
.link-card i{
color:var(--primary-color);
}

/* mobile */
@media (max-width:800px){
  .about-intro {
    width: 100%;
  }
  .about-image img{
    display:none;
  }
  .mobile-image{
    display:block;
  }
  .about-grid{
    grid-template-columns:1fr;
  }
  .about-header h1{
    font-size:28px;
  }
  #driestroom {
  display: block;
  }
  #driestroom img{
  max-width: 100%;
  }
}
</style>

<section class="about-page">

  <div class="about-header">
    <h1>De Rooms-katholieke kerk in Gorinchem</h1>
    <p class="subtitle">Met hoofd en hart op Christus betrokken.</p>
  </div>

  <div class="about-image">
    <img src="/assets/altaar.jpg" alt="Kerk Gorinchem">
  </div>

  <div class="about-intro card">
    <p> De parochie van Gorinchem heeft de Heilige Martelaren van Gorcum als patronen. 
    Zij vormt met de parochie de Heilige Drie-eenheid de federatie het Driestromenland. 
    Beide parochies behoren tot het bisdom Rotterdam.</p>
  </div>

  <div class="mobile-image">
    <img src="/assets/altaar.jpg" alt="Kerk Gorinchem">
  </div>

  <div class="quote-block" style="border-radius: 12px 0 0 12px;">
    <i class="fa-solid fa-cross"></i>
    <p> Het is en blijft de droom van de Kerk dat steeds meer mensen Christus leren kennen als fundament in hun leven.</p>
  </div>

  <div class="section">
    <div class="card about-text">
      <p>Wij zien de missie van de Kerk en dus ook van de parochie als het de gelegenheid bieden aan mensen om Christus te ontmoeten. 
      Dit heeft betrekking op zowel gelovigen als ongelovigen.</p>

      <p>In de beleidsnota Samenwerking Geboden van bisdom Rotterdam staat het aldus geformuleerd: 
      De Kerk is niet zomaar een organisatie van mensen omwille van zichzelf. 
      Zij is de verzameling van mensen, die door God als zijn volk bijeen zijn geroepen om Christus en Zijn heilswerk in de wereld present te stellen. 
      De Kerk is er voor het heil van de mensen en van de wereld.</p>

      <p>De reden van bestaan voor de parochie is dus het verkondigen van het Evangelie en mensen in relatie met Christus te brengen. 
      Vooral door catechese zullen mensen beter in staat zijn hun geloof te verwoorden en daarmee actief kunnen deelnemen aan deze zending van de Kerk.</p>

      <p>Wij zetten erop in dat mensen met hoofd en hart op Christus betrokken worden of blijven. 
      Hoewel het niet vanzelfsprekend is in deze tijd, is het de overtuiging in de Kerk dat wie een levende relatie kan onderhouden met Jezus Christus zijn leven zinvol zal ervaren.</p>

      <p>De parochie wil de missie tot uitvoer brengen. In woord en daad wil zij Christus verkondigen in deze maatschappij. 
      Het is en blijft de droom van de Kerk dat steeds meer mensen Christus leren kennen als fundament in hun leven. 
      Het ideaal van het pastoraal team is dat parochies gelovige, liefdevolle en geëngageerde gemeenschappen zijn.</p>

      <p class="source">(uit “Met hoofd en hart op Christus betrokken”, het beleidsplan van het pastoraal team)</p>
    </div>

  </div>

  <div class="quote-block">
    <i class="fa-solid fa-quote-left"></i>
    <p>De Kerk is niet zomaar een organisatie van mensen omwille van zichzelf. 
    Zij is de verzameling van mensen die door God bijeen zijn geroepen om Christus present te stellen.</p>
  </div>

  <div class="section">
    <h2>Het Driestromenland</h2>
    <div id="driestroom" class="card">
        <img src="/assets/driestromenland.jpg" alt="Driestromenland">

      <div>
      <p>De parochie van de Heilige Martelaren van Gorcum is in een federatief verband met de parochie van de Heilige Drie-eenheid. 
      Deze laatste heeft de parochiekerk in Vianen en daarnaast twee kerken, in Everdingen en in Leerdam.</p>

      <p>De naam van de parochiefederatie is Het Driestromenland. Deze wijst erop dat alle kerken van de twee parochies aan drie stromen liggen: 
      de Linge (Gorinchem en Leerdam), de Lek (Vianen en Everdingen) en de Merwede (Gorinchem).</p>

      <p>Maar de naam Het Driestromenland heeft ook een bijbelse achtergrond. Toen het joodse volk in ballingschap was, leefde het in Mesopotamië, 
      het Tweestromenland. En in Genesis 2 kunnen we van het paradijs, de hof van Eden, lezen dat er vier stromen waren.</p>

      <p>Wij, gelovigen, bevinden ons op weg van ballingschap naar paradijs, van Tweestromenland naar Vierstromenland. 
      Wij bevinden ons dus in het Driestromenland.</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>ANBI-informatie</h2>
    <div class="card">
      <h3>Algemene ANBI-informatie</h3>
      <p>Onze parochie is aangemerkt als ANBI-instelling (Algemeen Nut Beogende Instelling). 
      Dit is van belang voor de fiscale verwerking van kerkbijdragen, giften en legaten aan onze parochie.</p>

      <p>De mogelijkheden voor kerkbijdrage zijn: De jaarlijkse bijdrage ‘actie Kerkbalans’ evenals de opties 
      ‘Periodieke Gift in geld’ (schenking over een periode van vijf jaar) en ‘doorlopende automatische incasso’.</p>

      <h3>Bisdom Rotterdam</h3>
      <p>Via <a href="https://anbi.rkcn.nl/publicaties/ROT26882">deze link</a> vindt u de verkorte staat van baten en lasten.</p>

      <h3>Parochiële Caritas Instelling</h3>
      <p>De verkorte staat van baten en lasten van de PCI vindt u via 
      <a href="https://anbi.rkcn.nl/publicaties/ROT613">deze link</a>.</p>

    </div>
  </div>

  <div class="section">
    <a href="/artikelen/parochiebestuur" class="bestuur-banner">
      <img src="/assets/authors/bestuur.jpeg" alt="Parochiebestuur">
      <p style="color:black;">Het Parochiebestuur van de Heilige Martelaren van Gorcum parochie stelt zich hier graag aan u voor.</p>
      <span class="button">Lees meer</span>
    </a>
  </div>

  <div class="section">
    <h2>Links</h2>
    <div class="links-grid">
      <a href="https://www.bisdomrotterdam.nl/" class="link-card">
      <i class="fa-solid fa-church"></i>
      <span>Bisdom <span class='desktop-break'></span>Rotterdam</span>
      </a>

      <a href="https://www.rkkerk.nl/" class="link-card">
        <i class="fa-solid fa-cross"></i>
        <span>Nederlandse Kerkprovincie</span>
      </a>

      <a href="http://heiligedrieeenheid.eu/" class="link-card">
        <i class="fa-solid fa-people-group"></i>
        <span>Parochie <span class='desktop-break'></span>H. Drie-eenheid</span>
      </a>

      <a href="https://www.rkdocumenten.nl/" class="link-card">
        <i class="fa-solid fa-book-bible"></i>
        <span>RK documenten</span>
      </a>

  </div>

</section>