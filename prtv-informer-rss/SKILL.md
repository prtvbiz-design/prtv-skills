---
name: prtv-informer-rss
description: The «PRTV RSS» widget (s.prtv.su) — site news from RSS and Atom feeds on a PRTV TV slide through one iframe in an HTML block; builder address and embedding, up to 5 feeds with captions and alternation, a site page instead of a feed, word filters (whole words, list word forms, exclusions), display modes (carousel, free layout, scrolling feed, card grid, headline ticker), presets, styling and effects, block sizes, behaviour on failures; recipes — all sports news from 5 feeds, news about your city only, a ticker in a strip at the bottom of the screen. Use when a menu board, lobby or waiting-room screen needs live news, an industry feed, city news or a headline ticker. Triggers (RU) информер PRTV RSS, RSS на экран, новости на телевизор, бегущая строка новостей, лента новостей на экране, новости города на экране.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-10-10"
  language: en
  related: prtv-informer-google, prtv-design-mockups, prtv-feed-widget, prtv-widgets, prtv-element-layout
---

# The «PRTV RSS» widget

«PRTV RSS» shows the latest entries of websites from their RSS or Atom feeds on a slide: city news, trade news, sports, the venue's own blog. The owner has nothing to update — the site publishes, the screen shows. The widget was split out of «Лента» (prtv-feed-widget) and handles RSS only; Google Sheets, Calendar and News are in the «PRTV Google» widget (prtv-informer-google).

Builder (v1.0.0, Russian UI): **https://s.prtv.su/wp-content/plugins/prtv-informer-feed/index_in.php** — settings on the left, live preview on the right in four sizes (16:9 · 1920×1080, 9:16 · 1080×1920, block · 600×300, strip · 1920×200). There is no "save" button: the code is rebuilt on every change. Labels below are given in Russian as they appear, with the meaning in English.

## 1. Putting it on a slide

1. Configure the widget in the builder.
2. Bottom right, «Код для вставки — блок «HTML» на слайде» (embed code — HTML block on the slide) → **«Скопировать код»** (copy code). It is an `<iframe>` 100%×100% that fills the whole HTML block.
3. In the prtv.pro editor: left panel → **HTML** → paste the code into the «Код HTML» field. Size and position are set on the slide (prtv-element-layout).
4. If the widget sits on a photo or a coloured background, set the block background alpha to 0 in the element panel (prtv-widgets §5).
5. Check in the slideshow preview and on the TV.

To change a finished widget: «Продолжить настройку готового информера» (continue configuring a finished widget) → paste the link or the iframe code (links of the old «Лента» with RSS sources work too) → «Загрузить настройки» (load settings). Then copy the new code and replace the block's HTML.

## 2. Sources — the «Ленты» (feeds) block

- **«+ Добавить ленту (до 5)»** (add a feed, up to 5). The field takes an RSS or Atom feed address — usually `/rss`, `/feed` or `/rss.xml` of the site. The **«Проверить»** (check) button shows whether the feed is readable, how many entries it has and how many with a picture.
- **A page address instead of a feed.** You can paste the site's own address — the widget looks for the feed link on the page. The feed it finds may be the site's general feed rather than the section you wanted: read the title in the check result. If the page has no feed link, the check says so — look for the RSS icon or try `/rss`, `/feed`.
- **On-screen caption.** Each feed has a field «Подпись на экране (пусто — название ленты)» (caption; empty = the feed title). Replace long publication titles with short ones: «Sports.ru», «Science». In the link the caption is written after a tilde: `address~Caption`.
- **«Несколько лент на экране»** (several feeds on screen): **«Чередовать: по записи из каждой ленты»** (alternate: one entry from each feed, the default) — every site is represented and a frequent feed does not crowd out a rare one; **«Поровну из каждой ленты, общий порядок по дате»** (equal share per feed, common order by date). The same story from two feeds is shown once.
- Check every feed before publishing: some well-known addresses answer 404, 403 or time out, and some feeds have no pictures.

## 3. Choosing entries

| Field | What it does |
|---|---|
| Записей (entries) | How many entries to show (1–50, default 10) |
| Не старше, ч (not older than, h) | Drop old entries; 0 = no limit |
| Мин. длина текста (min text length) | Drop stub entries without text; 0 = no limit |
| Только со словами (only with words) | Show only entries containing these words |
| Исключить слова (exclude words) | Hide entries containing these words |
| Только новости с картинкой (only with a picture) | For modes where the photo is the point |
| Порядок (order) | Newest first / Oldest first |

**How the word filter works.** Comma-separated words; it matches **whole words** (or phrases) in the title, text and category; case and Russian «е/ё» are ignored. It does not understand word forms: «кофе» does not match «кофейня», «Москва» does not match «Москве». List the forms: `Москва, Москвы, Москве, Москву, Москвой, московский, московская, московские, москвичи`. Checked on three general feeds: one word gave 2 entries out of 50, the list of forms gave 23.

**Exclusions are not censorship.** In general news feeds politics and incidents come through under hundreds of different words. For children's venues and clinics use topical feeds (food, science, travel, sports) rather than general news; exclusions are the second line of defence.

## 4. Display modes — «Режим показа → Тип»

| Type (label) | What is on screen | Block |
|---|---|---|
| Карусель — по одной новости (carousel) | One entry at a time, changed every «Время на новость, с» (3–120 s), «Переход» (transition): Плавно (fade) / Сдвиг (slide) / Без анимации (none) | 16:9, square, portrait |
| Свободная компоновка (free layout) | One entry; blocks Photo, Title, Text, Source, Date, Category are arranged with the mouse on the builder canvas (red corner = size, click a block = font, colour, alignment). Starting layouts: photo left, photo right, photo as background, photo on top, text only centred | Branded layout, mock-ups (prtv-design-mockups) |
| Лента — вертикальная прокрутка (scrolling feed) | Column of cards, «Скорость прокрутки» (scroll speed) 1–10 | Tall side column |
| Сетка карточек (card grid) | Several entries at once; columns and rows fit the block | 16:9, large lobby screen |
| Бегущая строка заголовков (headline ticker) | Line of titles with the source caption | Strip at the bottom of the screen |

**Presets** («Заготовки») — news with photos, photo as background, big titles, column feed, tiles, ticker — replace all view settings; feeds and entry selection stay. A convenient starting point to adjust from.

«Обновление данных, с» (data refresh, 30–3600 s, default 120) — how often the screen asks for fresh entries; the server re-reads feeds no more than once every 5 minutes.

## 5. What to show, effects, styling

- **What to show:** picture (position: top / bottom / left / right / background; fit: fill / whole / as is), news text and max lines of text, date («5 min ago», time, date, date and time, hidden), source name, category, header above the feed (empty header text = feed titles).
- **Effects:** title animation (fade, slide up, from blur, by letters, typewriter), slow zoom on the photo (Ken Burns), progress bar to the next entry, text shadow (for text over photos), «new» badge for entries younger than N hours.
- **Styling:** theme — Карточки (cards) / **Без подложки** (no plate) / Тёмная (dark); font — Inter, Roboto, Montserrat, PT Sans, Open Sans, Oswald, Arial; colours of card background, text and accent; **«Прозрачный фон вокруг карточек»** (transparent background around the cards); text alignment; font size (24–96, default 44), corner radius (0–48), padding (0–120).
- Font size, radius and padding are set for a 1920×1080 screen and scale to the block by its shorter side. In portrait the text is the same size as in 16:9; in a narrow strip the font is boosted further; the floor is 16 px. Long text is cut by whole lines with an ellipsis: text first, then the title.
- Over a slide photo: theme «Без подложки» + «Прозрачный фон вокруг карточек» + block background alpha 0, text colour to suit the photo, text shadow.
- The checkbox «Мелкая подпись об ошибке в углу» (small error caption in the corner) is for debugging only. Without it the screen shows no messages on failure: the block is transparent until the first load, then the previous news stays.

## 6. Block size

| Task | Block on a 1920×1080 slide | Mode |
|---|---|---|
| News with photo as the main element | 16:9 or square, from 960×540 | Carousel, free layout |
| News column beside the menu | ~600×960 | Scrolling feed |
| News screen in a lobby | whole slide | Card grid |
| Strip under the main content | ~1728×164 inside a 1920×200 strip | Ticker |

Check in the builder preview at the closest size (block 600×300 and strip 1920×200 show what stays readable).

## 7. Recipes

### 7.1. All sports news from five feeds

1. «+ Добавить ленту» five times (addresses checked with «Проверить» on 2026-10-10): `https://www.championat.com/rss/news/`, `https://www.sports.ru/rss/main.xml`, `https://lenta.ru/rss/news/sport`, `https://rsport.ria.ru/export/rss2/index.xml`, `https://www.gazeta.ru/export/rss/sport.xml`.
2. Short captions: Чемпионат, Sports.ru, Лента.ру, РИА Спорт, Газета.Ru.
3. «Несколько лент на экране → Чередовать» — all five publications appear on screen, not just the most frequent one.
4. «Исключить слова»: ставки, ставка, букмекер, букмекеры, прогноз, коэффициент, трансляция (betting, bookmaker, odds, stream) — plus politicians' names if they should not appear.
5. «Только новости с картинкой», type carousel, picture «Фоном» (background), slow zoom, text shadow, Roboto 64, a bright accent.

### 7.2. News about your city only

1. Two or three general feeds (e.g. `https://lenta.ru/rss/news`, `https://ria.ru/export/rss2/archive/index.xml`) and a city feed (`https://www.m24.ru/rss.xml`, `https://www.mos.ru/rss` for Moscow).
2. «Только со словами» — the city name **in every case form** plus adjectives: Москва, Москвы, Москве, Москву, Москвой, московский, московская, московские, москвичи.
3. «Исключить слова» — суд, арест, задержали, ДТП, погиб, погибли (court, arrest, detained, crash, died) and so on; extend the list with whatever slips through.
4. Type scrolling feed, «Шапка над лентой» (header) reading «<City> today», date shown as time.

### 7.3. A ticker in a strip at the bottom of the screen

1. A bottom strip of the slide ~1920×200 (strip background as an image or a rectangle on the slide). HTML element ~1728×164 inside the strip, horizontally within the safe zone.
2. Type «Бегущая строка заголовков», scroll speed 3–4, feeds with short captions (Мос.ру, Travel, Science).
3. Pick the font size in the «полоса · 1920×200» (strip) preview so that the line fills the height: in a strip of ~160–200 px that is about 90–96.
4. Theme «Без подложки», «Прозрачный фон вокруг карточек», light text on a dark strip.

### 7.4. Limitations to state up front

- **The ticker shows titles only.** News text is not shown in it.
- **The widget appears a few seconds after the slide changes** (usually 3–6 s): the player loads the iframe when the slide is shown. Give a slide with this widget at least 15–20 s, and do not leave a visible "hole" in the background under the block before it loads.
- In a strip the line does not stretch to the block height by itself — the font size fills the height.
- Times in captions («5 min ago», «today at 18:30») use the clock of the playback device; there is no time-zone setting.
- The grid shows one page of entries (as many as fit), without paging.
- In a low block the scrolling feed shows cards one at a time instead of scrolling.
- The screen needs the network at every showing; if a source site is down, the server serves its saved copy (up to 3 days) and the screen keeps the previous entries.

## What not to do

- Do not put a general news feed on a clinic, school or children's café screen — use topical feeds and a filter.
- Do not expect one word in the filter to catch all its forms — list them.
- Do not promise news text in the ticker.
- Do not put two moving widgets on one slide: give the second one «Время на новость» 120 s so it does not change during the slide.
- Do not use a feed without checking it with «Проверить».
- Do not leave the error caption switched on for a production screen.

## Related

prtv-informer-google · prtv-design-mockups · prtv-feed-widget · prtv-widgets · prtv-element-layout · prtv-html-block-animation
