---
name: prtv-feed-widget
description: The «Лента» (Feed) widget of PRTV (s.prtv.su) — one iframe that turns a Google Sheet, RSS, a VK community, Google News by keyword, Wikipedia «this day», an iCal calendar, the Russian production calendar or Central Bank exchange rates into a live block on a TV slide; its display modes (carousel, free layout, scrolling feed, card grid, ticker, day schedule, month calendar, rate table, price list, table as is), filters and styling, and ready Google Sheet recipes per industry (price list, doctors' schedule, free slots, transfers, announcements, vacancies). Use when screen content must update without editing slides, or when someone wants prices, schedules or news on a signage screen fed from a spreadsheet. Triggers (RU) информер Лента, прайс из Google Таблицы, расписание на экран, объявление на экран, лента новостей на ТВ, курс ЦБ на экран, производственный календарь на экран.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: signage-widgets, prtv-widgets, prtv-digital-signage
---

# PRTV «Лента» (Feed) widget

The main weakness of most signage slideshows is hard-coded content: prices, schedules and promo dates typed into slides go stale, and every change means opening the editor. «Лента» moves that content into a source the business already maintains — usually a Google Sheet edited from a phone — and renders it on the slide. The slide design stays; the data updates itself.

Builder (v1.0, Russian UI): https://s.prtv.su/wp-content/plugins/prtv-informer-rss/index_in.php — the address may move to the public widget catalogue https://s.prtv.su/informery. The builder produces an `<iframe>` (100%×100%) that goes into an **HTML block** on the slide; size and position are set on the slide (see prtv-widgets for the general rules).

## 1. Sources

Several sources can be added to one feed; their records are merged and ordered by date.

| Source | What you enter | Typical use |
|---|---|---|
| RSS | feed URL | news of a trade medium, city news, a blog |
| Google Sheet | the sheet's URL from the browser address bar (sheet shared for viewing) | prices, schedules, announcements, vacancies, menus |
| Central Bank of Russia rates | nothing | exchange rates with flags and daily change |
| VK community | vk.com/address or short name | posts of the venue's own community |
| Google News | keywords, e.g. «кофейня Москва» | topical news without a ready RSS |
| Wikipedia | `otd` (this day) or `potd` (picture of the day) | calm, neutral «interesting» content |
| iCal calendar | link to an .ics / iCal address | events, classes, meeting rooms, conferences |
| Production calendar (RU) | nothing | working days and public holidays of the month |

Filters: number of records, max age in hours, minimum text length, include-only words, exclude words, only records with a picture, order (new first / old first).

## 2. Display modes

- **Carousel** — one record at a time, time per record and transition set.
- **Free layout** — one record at a time; photo, title, text, source, date, category are blocks you arrange on a canvas.
- **Feed** — vertical scrolling list.
- **Card grid** — several records at once.
- **Ticker** — crawling line of titles.
- **Schedule** — events grouped by day (for iCal).
- **Production calendar** — month grid or two weeks enlarged.
- **Exchange rates** — table with flags, currency names, arrow and delta, decimal places.
- **Services and prices** — price list from a sheet (name … price), grouped by section, note under the name, 1–3 columns, rows or tiles.
- **Table as is** — sheet columns on screen, header row and zebra stripes optional.

Styling: themes (cards / no plate / dark), 7 fonts, card, text and accent colours, transparent background, alignment, font size set for 1920×1080 and scaled to the block, radius, padding; effects — title animation (fade, slide up, from blur, by letters, typewriter), Ken Burns on photos, progress bar to the next record, text shadow for text over photos, «new» badge for fresh records, header above the feed.

## 3. Google Sheet recipes

Keep one sheet per screen purpose, first row = headers, one row = one item. The owner edits the sheet; the screen follows. Recommended columns (the builder maps name / price / section / note for the price mode; «table as is» shows whatever columns exist):

| Purpose | Mode | Columns |
|---|---|---|
| Price list (salon, car wash, clinic, laundry, hotel services) | services and prices | section · name · price · note |
| Menu of the day / canteen | services and prices | section · dish · price · weight |
| Doctors' or masters' schedule for the week | table as is | specialist · room · Mon … Sun |
| Free slots today (salon, service) | table as is | time · service · master |
| Transfers and excursions tomorrow (hotel) | table as is | time · route · meeting point · price |
| Order status by ticket (car wash, service) | table as is | ticket № · stage (no names or plates) |
| Urgent announcement | carousel or ticker | one row: text; delete the row to hide |
| Promotions of the week | carousel / free layout | title · text · picture URL · valid till |
| Vacancies | carousel | position · schedule · salary · contact |
| Fuel prices (filling station) | table as is | fuel · price |
| Gym load by hour | table as is | hour · load |

Rules: prices on screen must match the till and printed lists; write «valid till <date>» on promotions; never put personal data (names of guests or patients, car plates) in a sheet that feeds a public screen.

## 4. Industry use in one line each

Hotel — services and prices, transfers, events (iCal), CB rates incl. CNY, urgent announcements, Wikipedia «this day» for the in-room channel. Car wash / service — price by body type, ticket status, auto news via RSS/Google News. Beauty — price list, free slots, VK portfolio, workshops (iCal). Retail — promotions of the week, vacancies, holiday opening hours via the production calendar. Clinic — doctors' schedule, paid services price list, patient school events (iCal). Fitness — class timetable (iCal or sheet), memberships, gym load. Office / factory — production calendar, birthdays, canteen menu, business news and rates. Residential building — outages and meetings (sheet), waste collection schedule (iCal). Details and full screen plans: the industry skills (hotel-digital-signage, auto-service-signage, beauty-salon-signage, retail-store-signage, clinic-signage, fitness-club-signage, office-signage).

## 5. Checks

- Open the widget link in a browser tab first; then on the target TV. The feed needs the network at every showing.
- A Google Sheet must be viewable by link; a private sheet shows nothing.
- VK and Google News depend on the venue's network reaching those services — test on site.
- Size the HTML block to the mode: ticker — a strip; carousel with photo — 16:9 or square; price list — a tall column.
- Transparent background + element background alpha 0 when the feed sits on a photo (prtv-widgets §5).

## What not to do

- Do not type prices or schedules into slides when a sheet can feed them.
- Do not put personal data in a sheet that feeds a public screen.
- Do not stack two feeds with motion on one slide.
- Do not rely on third-party news for a clinic or a children's venue without word filters.
