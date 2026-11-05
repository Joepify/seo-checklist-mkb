# SEO checklist voor het Nederlandse mkb

Een praktische checklist voor technische en lokale SEO, geschreven voor Nederlandse mkb-bedrijven met een eigen website. Met een klein script (`seo_quickcheck.py`) dat de basis van een pagina controleert: titel, description, kopjes, canonical, robots, sitemap en structured data.

Er staat geen beloofde positie in Google in deze lijst. Wel de punten die ervoor zorgen dat Google je site kan lezen en begrijpt, en dat klanten in je regio je kunnen vinden.

## Voor wie

- Ondernemers die zelf iets aan hun vindbaarheid willen doen.
- Webbouwers die een oplevering of een bestaande site willen controleren.

## Wat zit erin

| Bestand | Doel |
|---|---|
| `README.md` | De checklist |
| `seo_quickcheck.py` | Controleert de SEO-basis van een URL (Python 3, geen afhankelijkheden) |

## 1. Technische basis

- [ ] **Eén versie van je site.** `http` en `www`/zonder `www` sturen met een 301 naar één voorkeursadres.
- [ ] **HTTPS** overal, zonder waarschuwingen voor gemengde inhoud.
- [ ] **Geïndexeerd:** zoek `site:jouwdomein.nl` in Google en kijk in Search Console bij Pagina's welke pagina's niet geïndexeerd zijn en waarom.
- [ ] **robots.txt** blokkeert niets wat je in Google wilt. Controleer op `Disallow: /` na een livegang.
- [ ] **Geen `noindex`** op pagina's die gevonden moeten worden (let op: een testomgeving die `noindex` meekreeg naar productie komt vaak voor).
- [ ] **XML-sitemap** op `/sitemap.xml`, ingediend in Search Console, met alleen pagina's die status 200 geven.
- [ ] **Canonical-tag** op elke pagina, die naar de eigen voorkeurs-URL wijst.
- [ ] **Geen 404-pagina's** in menu of interne links, en een nuttige 404-pagina voor de rest.
- [ ] **Redirectketens** voorkomen: maximaal één redirect naar de eindbestemming.
- [ ] **Mobiel:** de site werkt goed op een telefoon (Google indexeert mobiel eerst).

## 2. Inhoud per pagina

- [ ] **Titel (`<title>`)**: uniek per pagina, ongeveer 50 tot 60 tekens, belangrijkste onderwerp vooraan, plaats of dienst erin als dat past.
- [ ] **Meta description**: uniek, ongeveer 120 tot 155 tekens, beschrijft wat de bezoeker vindt. Dit is een uitnodiging om te klikken, geen rankingfactor.
- [ ] **Eén H1** die zegt waar de pagina over gaat.
- [ ] **Kopjes (H2, H3)** in logische volgorde, bij voorkeur als vragen die klanten stellen.
- [ ] **Eigen tekst** van een zinnige lengte. Geen gekopieerde fabrikantsteksten of dezelfde tekst op meerdere pagina's.
- [ ] **Afbeeldingen** met een beschrijvende bestandsnaam en `alt`-tekst waar de afbeelding inhoud heeft.
- [ ] **Een duidelijke vervolgstap** (bel, offerte, bestel).

## 3. Snelheid

- [ ] Meet de belangrijkste pagina's met PageSpeed Insights, op mobiel.
- [ ] Richtwaarden voor "goed" (Core Web Vitals): LCP onder 2,5 seconde, INP onder 200 milliseconden, CLS onder 0,1.
- [ ] Afbeeldingen verkleind en in een moderne indeling (WebP of AVIF), met `width` en `height` ingesteld zodat de pagina niet verspringt.
- [ ] Geen zware plugins, sliders of ongebruikte scripts. Elke externe widget kost laadtijd.
- [ ] Caching en een goede host. Een trage server is met geen enkele plugin op te lossen.

## 4. Lokale SEO

Voor bedrijven die klanten in een regio bedienen.

- [ ] **Google Bedrijfsprofiel** geclaimd en geverifieerd, met de juiste hoofdcategorie en secundaire categorieën.
- [ ] **NAP gelijk overal:** naam, adres en telefoonnummer staan precies hetzelfde op je site, in Google Bedrijfsprofiel, op Bing Places en in branchegidsen.
- [ ] **Openingstijden** actueel, ook voor feestdagen.
- [ ] **Diensten en gebied** ingevuld in het profiel, met foto's van het bedrijf en het werk.
- [ ] **Reviews:** vraag tevreden klanten gericht om een review, reageer op alle reviews, ook de slechte, en beloon nooit voor een review.
- [ ] **Een pagina per dienst** en, als je echt in meerdere plaatsen werkt, een pagina per plaats met unieke, eigen inhoud (geen kopieën waar alleen de plaatsnaam verandert).
- [ ] **KvK-nummer, adres en contactgegevens** zichtbaar op de site (ook wettelijk verplicht).
- [ ] **Vermeldingen:** je bedrijf staat op een paar relevante, betrouwbare lijsten (branchevereniging, KvK, lokale gidsen). Kwaliteit boven kwantiteit.

## 5. Structured data (schema)

- [ ] `LocalBusiness` of `Organization` op de homepage met naam, adres, telefoon, KvK, openingstijden en `sameAs` (profielen).
- [ ] `Service` of `Product` waar het past, met een prijs die ook op de pagina staat.
- [ ] `FAQPage` alleen als de vragen ook zichtbaar op de pagina staan.
- [ ] Test met de [Rich Results Test](https://search.google.com/test/rich-results).
- [ ] Kant-en-klare sjablonen: [schema-templates-nl](https://github.com/Joepify/schema-templates-nl).

## 6. Interne links

- [ ] Elke belangrijke pagina is binnen drie klikken te bereiken vanaf de homepage.
- [ ] Blogs en kennispagina's linken naar de dienst of het product waar ze bij horen, met een beschrijvende linktekst (niet "klik hier").
- [ ] Geen weespagina's: pagina's zonder enige interne link.
- [ ] Het menu bevat de pagina's die geld opleveren.
- [ ] Breadcrumbs op diepere pagina's.

## 7. Meten

- [ ] Google Search Console gekoppeld en geverifieerd.
- [ ] Bing Webmaster Tools (ook voor Copilot).
- [ ] Analytics met correcte toestemming (cookiebanner en Consent Mode).
- [ ] Maandelijks: kijk naar klikken, vertoningen en gemiddelde positie van je belangrijkste pagina's.
- [ ] Noteer wijzigingen met datum, zodat je later weet wat effect had.

## 8. Wat je laat staan

Dingen die vaak tijd kosten zonder resultaat: keywordstuffing, honderden dunne plaatspagina's, gekochte linkpakketten, en wekelijks de meta keywords aanpassen (Google gebruikt ze niet).

## Het script gebruiken

```bash
python3 seo_quickcheck.py https://www.jouwdomein.nl
python3 seo_quickcheck.py https://www.jouwdomein.nl/diensten --json
```

Voorbeeld van de uitvoer:

```
URL: https://www.example.nl/
OK    Status 200
OK    https gebruikt
OK    Titel (47 tekens): Loodgieter in Rotterdam | Voorbeeld BV
OK    Meta description (138 tekens)
OK    Eén H1: Loodgieter in Rotterdam
WARN  Canonical ontbreekt
OK    Geen noindex
OK    robots.txt bereikbaar (geen 'Disallow: /')
OK    sitemap.xml bereikbaar
OK    Structured data: LocalBusiness
```

Het script controleert één pagina en de twee bestanden op de root (`robots.txt`, `sitemap.xml`). Het vervangt geen volledige audit.

## Laat het mij doen

Ik werk deze checklist voor je af: technische SEO en lokale vindbaarheid. Vaste prijs: €295 (tot 20 pagina's) of €495 (tot 100 pagina's of een webshop) (excl. btw). [Meer over SEO](https://www.joepify.nl/seo-rotterdam?utm_source=github&utm_medium=readme&utm_campaign=seo-checklist-mkb) of [stuur een WhatsApp-bericht](https://wa.me/31687195043?text=Hoi%20Ayoub%2C%20ik%20kom%20via%20GitHub%20%28seo-checklist-mkb%29%20en%20wil%20hulp%20met%20seo.).

## Over Joepify

[Joepify](https://www.joepify.nl?utm_source=github&utm_medium=readme&utm_campaign=seo-checklist-mkb) is een webbureau aan de Metaalhof 27 in Rotterdam. Ayoub Assaidi bouwt websites en doet de SEO zelf. Wil je hulp bij vindbaarheid in de regio, dan kun je bij hem [SEO laten doen in Rotterdam](https://www.joepify.nl/seo-rotterdam?utm_source=github&utm_medium=readme&utm_campaign=seo-checklist-mkb). Een eerste controle van je hele site doe je gratis met de [website check](https://www.joepify.nl/website-apk?utm_source=github&utm_medium=readme&utm_campaign=seo-checklist-mkb).

## English

A technical and local SEO checklist for Dutch small and medium-sized businesses (Google Business Profile, NAP consistency, schema, speed, internal links), plus `seo_quickcheck.py`, a standard-library Python 3 script that checks title, meta description, H1, canonical, noindex, robots.txt, sitemap.xml and JSON-LD for a URL.

## Licentie

Tekst: CC BY 4.0. Code: MIT. Zie [LICENSE](LICENSE).
