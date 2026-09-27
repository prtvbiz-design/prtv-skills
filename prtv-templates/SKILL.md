---
name: prtv-templates
description: Free PRTV (prtv.pro) system templates as a first test of the service — where the catalogue is (about 110 templates in Menu board, Business, Calendar, School, Residential building, Misc), how to preview a template by number on a TV without signing up, how to copy it to your account (the Copy button needs a slideshow group), rename it, replace prices, fix an expired countdown and restyle a widget, lighten a template for a weak TV, which templates are paid and the padlock trap; template numbers by industry. Use when someone wants to try PRTV quickly, take a ready menu-board or industry slideshow template, or an agent is asked to copy a template and edit it. Triggers (RU) шаблон PRTV, бесплатный шаблон меню борда, забрать шаблон, скопировать шаблон prtv.pro, поменять цены в шаблоне, шаблон слайд-шоу для телевизора.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: prtv-digital-signage, menu-board-by-venue, prtv-text-element, prtv-widgets-catalog, prtv-tv-player
---

# PRTV templates — a first test in 10 minutes

The fastest way to try PRTV is not to build from scratch but to take a free template for your industry, change the prices and open it on the TV. The first licence (one slideshow on three screens at once) is free and not time-limited.

## 1. Preview before signing up

- Catalogue with previews: https://s.prtv.su/shablony/katalog-shablonov.
- Any template opens in a TV or computer browser by number: `prtv.su/<5 digits>` (older templates) or `prtv.pro/<7 digits>` (PRO, with leading zeros, e.g. `prtv.pro/0012746`). In the PRTV TV app only the number is typed.
- In a desktop browser, click the edge of a slide to page through; on a TV use the remote's arrows.
- This lets you show a venue owner a template on their own TV before any registration.

## 2. Copy a template to your account (prtv.pro)

1. Sign in at https://prtv.pro (the user types their own login and password).
2. Open **Templates** (prtv.pro/templates). Categories: All, Purchased, Paid, Calendar, Menu board, Business, School, Residential building, Misc and themed collections.
3. Press **Copy** on the template.
   - Error "slideshow groups not found" — the account has no group yet. Create one in the slideshow list (any name) and retry.
   - Every Copy click creates another copy. Click once and wait for the editor to open.
4. The copy opens at `prtv.pro/slideshow/<code>` named "Slideshow No. <number>". **Rename it at once** in the slideshow settings, or the list fills with identical copies.
5. You can take single slides instead of a whole template: save a slide as a layout and insert it with "Slide from layout".

## 3. Make it yours

1. **Prices and names**: click the text, then double-click — it becomes editable; select all, type the new value, click an empty area. Font, size and colour are kept. Details and traps — **prtv-text-element**.
2. **Expired promos and countdowns.** Templates were made over several years: some have past dates and countdowns showing 00:00:00. Check every countdown.
3. **Countdown widget** (HTML block with `s.prtv.su/informers/countdown/get_timer.php?p=<JSON>`): select the block and in the "HTML code" field change in the JSON:
   - `type.params.utc` — end time in milliseconds UTC (e.g. New Year in Moscow: 1798750800000);
   - `design.params.background-color` — plate colour; `number-font-color` — digit colour;
   - `text-on: true` — "days, hours, minutes, seconds" labels, plus `text-font-color`.

   With labels on, make the element about 20 px taller or they are clipped. Simpler: build a new code at https://s.prtv.su/informery/countdown and paste it over the old one.
4. **Other widgets** (clock, weather, rates, traffic): on the widget page at https://s.prtv.su/informery choose city, colours, font → "Generate widget code" → replace the code in the selected block. Per-widget parameters — **prtv-widgets-catalog**.
5. **Dead elements**: Twitter, Facebook and Instagram feeds in old templates do not show in Russia — replace with VK, Telegram or RSS.
6. **Word garbage**: if a text shows "Normal 0 false … mso-style", retype the line.
7. Verify by reloading the page, then open the public address on the TV.

## 4. Lighten for a weak TV

Templates use maximum-quality graphics. On a TV with 1 GB of memory:
- bake dish photos and decoration into one background image; keep only price texts editable;
- convert images to WebP (background under 200 KB); compare prtv.su/66980 with its light copy prtv.su/99303 (PNG 1.3 MB → WebP 181 KB);
- make a widget needed on every slide a "permanent element" instead of copying it to each slide;
- pick "Light" rather than "Heavy" variants (calendars).
More — **prtv-tv-player**.

## 5. Paid templates

Most templates are free. Paid ones show a padlock and a price (e.g. "Beer bar", "Beige beer menu", "Grill menu", "Beauty salon. Black"). Buy → pay → always press "Continue". **Trap**: copy the template to your account right after paying — the padlock returns on the system template after a month. The free catalogue often holds a couple of slides from a paid template as a sample.

## 6. Numbers by industry (`prtv.su/<number>`)

| Industry | Numbers |
|---|---|
| Menu boards | see **menu-board-by-venue** (coffee, burgers, shawarma, pizza, sushi, beer, sports bar, bakery) |
| Grocery | 11448 (red), 11449 (green), 11451 (yellow); meat 11440, fish 11441, dairy 11462, dry goods 11465, confectionery 11463, drinks 11466, bakery 11467, fruit and veg 11468 |
| Beauty | salons 11425, 11426, 11427 (black), 11460; cosmetics 57783, 15381 |
| Medical | medical centre 11435, dentistry 11414, pharmacies 11436 and 11438, "Aquarium" for dentistry and labs 11439 |
| Auto | filling station 11417; car washes 11428, 11429, 11430, 11432, 11433 |
| Business | corporate channel 11415, business centre 11419, exhibition stand 11416, factory 37859, travel agency 11411, real estate 11412 and 11413, currency exchange 11418, dry cleaning 84650, jewellery and pawnshop 93486, flower boutique 11423 |
| Fitness | 11420 (light), 11421 (dark), 11422 (simple) |
| School | 11511, 11512, 11513, 11514 |
| Residential building | 11711, 11712 |
| Calendars | Moscow 11211, St Petersburg 11212, "Seasons" 11213 |
| Misc | Olympics 2024 32024, "Fireplace", "Music for 8 March" 11815 |

PRO template numbers (7 digits) are shown under Templates; the older 5-digit templates sit in the same categories in PRO.

## What not to do

- Do not show a client a template with past dates and zeroed countdowns.
- Do not click Copy repeatedly — you get duplicates; only the user deletes extra copies.
- Do not keep the name "Slideshow No. …".
- Do not put a heavy template on a weak TV without lightening it.
