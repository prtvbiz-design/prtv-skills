---
name: prtv-widgets-catalog
description: Parameter reference for the PRTV (prtv.pro / s.prtv.su) widget builders — for each widget its builder page, render file, views, proportion, exact parameter names, defaults, limitations and a ready iframe embed — clocks (21 types + 30 dials), weather (7 views), countdown, QR (menu / Wi-Fi / text), calendar, Google calendar, currency and precious-metal rates, stocks, promo card (happy hours / business lunch / combo / closing discount), moon, holidays, work-day countdown, weather and air-quality maps, TV programme, radio, timetable, poll, cloud photo feed, Yandex widgets, social feeds, RSS. Use with prtv-widgets when building or reading a specific widget URL for a TV screen or menu board. Triggers (RU) параметры информера, код часов, код погоды, QR Wi-Fi, счастливые часы, бизнес-ланч.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-26"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# PRTV widget catalogue

All builders live under `https://s.prtv.su/informery/<page>`; their render files under `https://s.prtv.su/informers/<type>/<file>.php`. Every embed is the same tag with a different `src`:

```html
<iframe src="https://s.prtv.su/informers/<type>/<file>.php?<params>" frameborder="0" width="100%" height="100%" style="overflow:hidden;"></iframe>
```

Universal rules (colours `%23`, cities in Cyrillic, `encodeURIComponent`, transparency, sizing) are in prtv-widgets and are not repeated below. Font lists: most older widgets take one of 29 Google fonts (Anton, Bad Script, Comfortaa, Indie Flower, Fira Code, Forum, Jura, El Messiri, Kurale, Kelly Slab, Lobster, Marck Script, Neucha, Open Sans, Orbitron, Oswald, Pangolin, Play, Poiret One, Pacifico, Press Start 2P, Pattaya, Roboto, Ruslan Display, Russo One, Rubik Mono One, Seymour One, Stalinist One, Underdog); the newer family (promo card, moon, work-day) takes 7 (Roboto, Open Sans, Oswald, Comfortaa, Play, Russo One, Pacifico). For reading from a distance choose Russo One, Anton, Oswald.

## 1. Clocks — two different widgets

**[A] «Часы»** — builder `/chasy`, files `clock/<type>.php`, **21 types**, colours, fonts and sizes configurable. Works without any data source. The builder is not a wizard: a "type" tab with 21 previews and a "settings" tab; each type has its own code box.

**[B] «Аналоговые часы (выбор циферблата)»** — builder `/analogovye-chasy-vybor-cziferblata`, files `analog_clocks/index<N>.php`, N = 1…30, **30 finished dials**; the only parameter is `city`. Colours, fonts and size cannot be changed (any extra parameter is ignored). Proportion 1:1.

Choosing: a finished themed design (kids, Roman, sport) → [B]; your own palette or the venue's name on the clock → [A]. A task with "kids" in it — look at [B] first. Only `clock_analog` in [A] carries a name and a slogan.

**Proportion rule:** square 1:1 — `clock_analog`, `analog2–4`, `cube`, `progress` and all 30 dials; wide 2:1 — every `digital*`, `flip`, `flip1`, `neon`, `neon2`, `glitch`, `rotate`, `skeleton`, `progress1`, `analog5`.

**Types of [A]** (file · proportion · look · where it fits):

| # | File | Look | Fits |
|---|---|---|---|
| 1 | clock_analog.php | round face + **name and slogan** under it — the only branded one | cafés, hotels, offices, shops |
| 2 | analog2_clock.php | dark disc, glowing neon arcs | bars, clubs, gaming |
| 3 | analog3_clock.php | light minimal, thin hands (no font choice) | clinics, offices, spa, banks |
| 4 | analog4_clock.php | dark dial in a frame, disc hands, date | premium, hotels, car dealers |
| 5 | analog5_clock.php | semi-transparent face (2:1) | over photo or video |
| 6 | clock_digital.php | plain digits, two parameters (no font choice) | when the clock must not argue with the design |
| 7 | digital2_clock.php | digits + accent line | office, reception, dashboards |
| 8 | digital4_clock.php | red LED board (no font choice) | retro, station, gym, garage |
| 9 | digital5_clock.php | light digits on dark, minimal | universal |
| 10 | digital6_clock.php | seconds in another colour | office, dashboards |
| 11 | digital7_clock.php | cyan digits (no font choice) | IT, gaming |
| 12 | flip_clock.php | flip cards (airport board) | retro, hotels, barbershops |
| 13 | flip_clock1.php | flip cards, variant 2 — **parameters carry suffix 1** | same |
| 14 | neon_clock.php | neon with glow, date and weekday; most configurable digital | bars, clubs, hookah lounges |
| 15 | neon2_clock.php | neon, dark/light switch | bars, clubs |
| 16 | glitch_clock.php | glitch effect | gaming, streetwear |
| 17 | cube_clock.php | 3D cube (square only) | gaming, showcases, kids' zones |
| 18 | rotate_clock.php | columns of bright multicoloured digits, most "cartoon" | kids' cafés, play centres, schools |
| 19 | skeleton_clock.php | digits in frames | loft, industrial, craft bars |
| 20 | progress_clock.php | coloured concentric rings (days/hours/min/sec) + date | kids' venues, co-working, fitness |
| 21 | progress1_clock.php | neon progress bars with glow | tech, dashboards |

**Parameters per type** (each type has its own names — never mix):

- **clock_analog:** `transpar`, `color_fon`, `color_clockface` (face digits), `color_hour`, `color_min`, `color_sec` (default `#c40007`), `color_font`, `name` + `color_name` + `font_name` + `size_name`, `slogan` + `color_slogan` + `font_slogan` + `size_slogan`, `font_family_clockface`, `size_clockface`, `city`. Sizes are 0–100 in steps of 5; 0 hides the item. Keep `size_name` 15–20 (a long name above 20 overlaps the digits), slogan 10–13, face 40–50. The transparency box is ticked by default in the builder.
- **analog2_:** `color_fon`, `color_clockface`, `color_hour`, `color_min`, `color_sec`, `color_font`, `font_family`, `transpar`, `city`.
- **analog3_:** `color_fon`, `color_clockface`, `color_arr` (hour + minute together), `color_sec`, `transpar`, `city`.
- **analog4_:** `color_fon`, `color_frame`, `color_date`, `color_marker`, `color_hour` + `color_hourdisk`, `color_min` + `color_mindisk`, `color_sec` + `color_secdisk`, `font_family`, `transpar`, `date_check` (on by default), `city`.
- **analog5_:** `color_fon`, `color_font`, `color_clockface` (default `#fff9`, with alpha), `font_family`, `transpar`, `city`.
- **clock_digital:** `dig_color_font`, `city`.
- **digital2_:** `color_fon`, `color_font`, `color_line`, `font_family`, `transpar`, `city`. **digital4_:** `color_fon`, `color_font`, `transpar`, `city`. **digital5_:** `color_fon`, `color_font`, `transpar`, `font_family`, `city`. **digital6_:** adds `color_sec`. **digital7_:** `color_fon`, `color_font`, `transpar`, `city`.
- **flip:** `flip_color_font`, `flip_color_fon`, `color_cards`, `font_family`, `city`. **flip1:** `color_font1`, `flip_color_fon1`, `color_cards1`, `font_family1`, `city1`.
- **neon_:** `color_font`, `color_fon`, `color_glow` (glow colour), `font_family`, `transpar`, `city`, `date` (on), `week`, `size_time` (0–15, default 9), `size_date` (0–15, default 4), `size_week` (0–15, default 3), `separator` (0–50, default 25 — gap between digits).
- **neon2_:** `color_fon`, `fon_tip` (0 dark / 1 light), `font_family`, `transpar`, `city`.
- **glitch_ / cube_:** `color_font`, `color_fon`, `font_family`, `transpar`, `city`.
- **rotate_:** `color_fon`, `color_hours`, `color_min`, `color_sec` (three digit colours), `font_family`, `transpar`, `city`.
- **skeleton_:** `color_fon`, `color_font`, `color_hour` / `color_min` / `color_sec`, `hour_frame` / `min_frame` / `sec_frame` (frame colours), `font_family`, `city`. Its own transparency flag is ineffective — use `skeleton_color_fon=transparent` or the element's alpha.
- **progress_:** `color_fon`, `color_days`, `color_hours`, `color_min`, `color_sec` (four ring colours), `color_font`, `font_family`, `transpar`, `city`.
- **progress1_:** `color_fon`, `color_font`, `glow` (a colour, not a flag), `transpar`, `font_family`, `city`.

For prefixed types the URL parameter is `<type>_<name>` — e.g. `rotate_clock.php?rotate_color_fon=%23FFFDE7&rotate_color_hours=%232E7D32&rotate_font_family=Pangolin&rotate_transpar=0&rotate_city=Москва`.

Transparency in the widget itself: `<prefix>_color_fon=transparent` **and** `<prefix>_transpar=1` for transparent; a hex colour and `transpar=0` for opaque. Simpler: the element's background alpha in the editor.

**Dials [B]:** `analog_clocks/index<N>.php?city=Москва`. Groups: Arabic 1, 5, 13, 19, 22–27; Roman 2, 3, 4, 6, 17, 18, 20, 28, 29, 30; kids 10, 11, 12, 14, 15, 16, 21; sport 7, 8, 9. Previews at `analog_clocks/images/tip<N>.jpg`. On the builder page a dial thumbnail reacts to a dispatched click event, not to `.click()`.

Layout: one branded square clock (~440×440) as an accent plus at most one dynamic wide one (~600×300); more than three clocks on a working slide is clutter.

## 2. Weather — 7 views

Builder `/openweather`, files `weather_openweathermap/<file>.php`. Data from OpenWeather via PRTV's server — the TV talks only to s.prtv.su; no key needed. Units °C, m/s, mmHg, Russian labels; no parameters to change them.

| View | File | Look | k (height/width) |
|---|---|---|---|
| 1 | weather_wide_flexible.php | wide light banner: city, date, time, condition, wind/humidity/pressure | ≈ 0.28 |
| 2 | weather_narrow_flexible.php | compact light: date, temperature, wind/humidity/pressure | ≈ 0.55 |
| 3 | weather_wide_litle_flexible.php | one-line ultra-wide strip | ≈ 0.24 |
| 4 | weather_color_flexible.php | colour card, near-square — **colours fixed** (white bg, black text), pickers and transparency off; only icons and font | ≈ 0.85 |
| 5 | weather_5.php | dark wide, temperature + day max/min | ≈ 0.45 **only at box width ≥ 1050 px** — below that the layout switches to a mobile variant and clips |
| 6 | weather_6.php | dark card with large temperature, city, date, wind/humidity/pressure | 0.73 (measured) |
| 7 | weather_7.php | dark square, hourly forecast | 1.08 (measured) — slightly taller than square |

Parameters: `city` (required, Cyrillic), `fon_table` (background), `font_text` (text), `font_tempo` (temperature/data), `transpar` 0/1, `font_family`, `type_img` (icon set: `img_7_svg`, `img_8_svg`, `img_9_svg`, `img_10_svg`, or `img` for PNG) with `img_tip` = `svg` or `png` to match. Form labels differ from these names (form `color_fon` → URL `fon_table`).

Known limitations: temperature is not rounded (e.g. 20.79°); a wrong city prints an error sentence on the slide; the time shown in view 1 may not be the city's live local time — verify. Transparency confirmed on views 1 and 7 (a faint card plate remains and reads well over photos); not verified on 5 and 6.

Example: `weather_wide_flexible.php?transpar=0&font_family=Oswald&type_img=img_7_svg&img_tip=svg&fon_table=%23f2f2f2&font_text=%23111111&font_tempo=%231565C0&city=Москва`

## 3. Countdown

Builder `/countdown`, file `countdown/timer.htm`. A four-step wizard: 1) timer type («До даты» — to a date, and others) → next; 2) date `DD/MM/YYYY` and time `HH:MM`; 3) design — text / plate / circle — and checkboxes for units; 4) the code. There is no field for a custom caption — add the caption as a native Text element (≥ 40 px). Counts on the device's clock.

## 4. QR — menu, Wi-Fi, text

Builder `/qr-infomer`, file `qr_horeca/qr.php`. Modes by `type`: `link` (URL), `wifi`, `text`. Parameters: `title` (caption above the code), `text` (URL or text, encoded), `wifi_name`, `wifi_pass`, `wifi_type` (`WPA`, `WPA2`, `WEP`, `nopass`), `font_family`, `font_text`, `font_title`, `fon_table`, `transpar`. The builder regenerates the code on every input. Note that the Wi-Fi password is part of the URL — treat the embed accordingly. Give the code a margin: uploads are downsized and TVs blur edges; keep the module square and ≥ 300 px on the 1920 canvas.

Example (menu): `qr.php?type=link&title=Меню&text=https%3A%2F%2Fexample.com%2Fmenu&font_family=Oswald&transpar=1&font_text=%23ffffff`

## 5. Plain calendar

Builder `/kalendar`, file `calendar/calendar.php`. A date grid without events; works from the device's date. Views `tip=1` today's date (large), `tip=2` month grid (vertical), `tip=3` horizontal day strip. `align` 1/2 for tip 2.

**Two independent month-parameter sets** — the typical mistake:

- for `tip=1` and `tip=2`: `cur_month=MM/YYYY` (current), `month=MM/YYYY` (specific; ignored when `cur_month` is present), `month_start` + `month_end` (range);
- for `tip=3`: `gor_current_month`, `gor_month`, `gor_month_start` + `gor_month_end`.

A view given only the other set draws an empty block. Safe practice, as the builder does: pass **both** sets with the same value. `cur_month` effectively supplies the year; the month itself is taken from the server clock (a mismatch is possible at the turn of the year). Colours: `fon_table`, `font_text`, `font_weekend` (default `#bd0f0f`), `font_now` (today, default `#c0f788`), `transpar`, `font_family`.

Example (horizontal): `calendar.php?tip=3&gor_current_month=09%2F2026&gor_month=09%2F2026&align=1&fon_table=%23f2f2f2&font_text=%23111111&font_weekend=%23bd0f0f&font_now=%23c0f788&font_family=Oswald&transpar=0`

## 6. Google calendar

Builder `/google-kalendar`, file `google_calendar/calendar.php`. Shows events of **public** Google calendars; no sign-in. Make the calendar public in Google Calendar settings and copy its ID (`…@group.calendar.google.com` or a Gmail address); several IDs separated by commas. Never publish a personal calendar — create a separate public one with only the events meant for the screen.

Parameters: `calendar_name` — the ID(s) in **base64** (the builder encodes; if the base64 contains `+` or `/`, URL-encode it), `calendar_tip` — `dayGridMonth` (month grid), `dayGridWeek`, `dayGridDay`, `listMonth` (list of the month's events); undocumented but working: `listYear`, `listWeek`, `listDay`, `multiMonthYear` (check visually — a year list may start with past events and the box does not scroll). Colours: `calendar_color_fon`, `calendar_data_color` (dates), `calendar_event_fon`, `calendar_event_color`, `calendar_today_fon`, `calendar_transpar`, `calendar_font_family`, `calendar_size_font` (em, 0–6 step 0.5, default 1).

Sizing: `dayGridMonth` needs height ≥ 1.0 × width (else an inner scroll appears); `listMonth` fits any box, extra rows are hidden at the bottom, days without events are not shown; week/day ≥ 0.6 × width.

Known limitations: in `listMonth` the day headers keep a white background, so with a dark `calendar_color_fon` and light `calendar_data_color` the dates become invisible — use a **light background with dark dates** for list views (month grid does not have this problem). Events can intermittently fail to load and the widget shows "no events" without an error — on slides prefer `dayGridMonth`, where an empty grid still looks intentional. Needs Google API and CDN access from the TV.

## 7. Currency rates, precious metals, stocks

**Rates** — builder `course/index_in.php`, files `course/course1.php` (vertical table with flags), `course2.php` (with date in the header), `course3.php` (horizontal). Parameters: `tip_value1..3` — exactly three currency codes (USD EUR CNY JPY GBP BYN KZT UAH TRY PLN RUB), `course_country` — `rf` (CB RF, server-side), `rkh` (NB Kazakhstan, server-side), `rb` (NB Belarus — fetched by the TV itself from nbrb.by; network risk), `fon_table`, `font_text`, `font_curs` (rate digits), `font_family`, `transpar`. A wrong code yields a broken row without an error. Rates update once a day (CB RF after ~11:30 MSK for the next day). Three currencies ≈ 520×470 box (course1); measure k for others.

**Precious metals** — `metal/course1.php` (vertical), `course2.php` (horizontal); always four metals (gold, silver, palladium, platinum, CB RF accounting prices, ₽/g). Same colour parameters. The "buy/sell" columns show the same figure. The metal-price **chart** (`metal_grafic`) depends on an external chart library and returned empty data in tests — not recommended.

**Stocks** — `stock/stock1.php?stocks=<tickers,comma>&color_fon=&color_text=&color_curs=&font_family=` — note the **different colour names** here. Tickers (lowercase): aflt sber lkoh gazp five mgnt mtss rosn | aapl amzn googl ibm ko msft nflx pfe tsla. Some tickers are stale or empty (`yndx`, `mail`, `fb`) — do not use them. Wide table with six columns: box ≥ 1100 px wide. Loads a script from a CDN.

## 8. Promo card — happy hours, lunch, combo, closing discount

Builder `horeca_action/index_in.php`, file `horeca_action/action.php`. Server-drawn card with a client-side timer; self-contained. Parameters: `type` 1–4, `title`, `subtitle`, `offer`, `price` (empty hides the price block), `start` and `end` `HH:MM` (crossing midnight is supported), `show_timer=1` ("until start" before the window, "until end" inside it, then flips to tomorrow — the card is **always visible**; hide it outside the window with the slide's rotation, not with the widget), `transpar` (1 or empty), `fon_table`, `font_text`, `font_accent`, `font_family` (7 fonts).

`type` fixes the badge text and, for 2–4, the accent colour: 1 = «СЧАСТЛИВЫЕ ЧАСЫ» (accent from `font_accent` — the only fully customisable type); 2 = «БИЗНЕС-ЛАНЧ» green `#2f8f46`; 3 = «КОМБО ДНЯ» orange `#d98200`; 4 = «СКИДКА ДО ЗАКРЫТИЯ» dark red `#8b1e1e`. For 2–4 design the slide around that colour. Fits any box (500×280 to 900×520 recommended); on very wide boxes the fonts stop growing.

Example: `action.php?type=3&title=Комбо%20дня&subtitle=Только%20сегодня&offer=Кофе%20%2B%20круассан&price=299%20%E2%82%BD&start=08:00&end=22:00&show_timer=1&transpar=1&font_text=%23FFF3E0&font_family=Oswald`

## 9. Moon, holidays, work-day countdown

**Moon** — `moon_calendar/moon.php?type=1|2|3` (compact / card / detailed), `transpar`, `fon_table`, `font_text`, `font_accent`, `font_family` (7). Phase emoji, phase name, lunar day, age, illumination, a recommendation; approximate calculation, as the widget itself notes. Fits any box (420×420 to 700×640). Emoji may show as squares on some TVs.

**Holidays** — `holidays/holidays.php?font_family=<font>`. The **only** parameter is the font; text is fixed dark grey on a transparent background, so it is unreadable on dark slides — put a light plate under it. Lists today's holidays, historical dates, name days; 2–6 lines; box from 500×280 with height margin (overflow is hidden).

**Work day** — `worktime/worktime.php?type=1|2|3&mode=day|friday|close&end=HH:MM&transpar=&fon_table=&font_text=&font_timer=&font_family=`. `type` 1 compact / 2 large card / 3 "fun" with rotating phrases. `mode=day` — "until the end of the working day" (weekends show a day-off message), `friday` — "until Friday", `close` — "until closing" (works seven days). After `end` the countdown immediately targets tomorrow — there is no "day is over" state; schedule the slide accordingly. Device time; no city. Fits any box (520×300 to 900×500).

## 10. Maps and air quality

All load tiles and data from third-party services on the TV at every show; no colour customisation; no dark themes (frame them as a "window" on dark slides); give the slide ≥ 15 s.

- **Weather map** — `weather_maps/map.php?tip=1..5&lat=&lng=&zoom=1..10` (temperature / precipitation / clouds / pressure / wind). Some tiles are `http://` — an https player may drop the layer. Box from 800×600.
- **Weather on a region map** — `weather_new/weather.php?city=<Cyrillic>&transpar=&fon_table=&font_text=&font_tempo=&font_family=`: hourly forecast table plus a Google map; the map may degrade when the shared map quota is exhausted.
- **Air pollution level (Moscow only)** — `air/air.php?name=<station>`, 23 Moscow stations (parkovaya, veshnyaki, marin, guryanova, ochakovskaya, melitopolskaya, troitsk, proletarskiy, cheremushki, mgu, shabol, kojuhovo, novokosino, spirid, suhar, spartakovskaya, narod_op, ostankino, glebovskaya, dolgoprud, turist, zelen_15, zelen_11). Official WAQI widget loaded from the TV; light cards, no styling; box ≈ 1:1.2.
- **Air-quality map of Moscow** — `airmap/map.php`, no parameters (Yandex map with station markers).
- **World air-pollution map** — `airmap_world/map.php?lat=&lng=&zoom=` (zoom 8–11 for a city, 4–6 for a country).

## 11. TV programme, radio, timetable

- **TV programme** — `tv/tv_informer.php?max=<N>&size=large|small&channel=<id,id,…>&color_fon=&color_font=&font_family=&transpar=`. Channel IDs come from the builder's select (535 channels, no search). `max` = programmes per channel. Server-side content; channel logos are `http://` (mixed content). Best for foyers, hotels, barbershops.
- **Radio** — `radio/radio_informer.php?channel=<playlist.m3u>&radio_color_fon=&controls=0|1`: 35 genre streams (top_40, jazz, lounge, 80s …); `radio_free/radio.php` — server-rotated tracks. **Autoplay with sound is blocked on most TV players** — the widget may stay silent; test on the device and position sound carefully.
- **Timetable (trains, flights)** — a wrapper of the Yandex timetable widget: `https://rasp.yandex.ru/informers/station/<ID>/?size=5|15|25&color=<N>&type=schedule|tablo`. Moscow stations: Киевский 2000007, Павелецкий 2000005, Белорусский 2000006, Ярославский 2000002, Савёловский 2000009, Рижский 2000008, Ленинградский 2006004, Курский 2000001, Казанский 2000003. Airports: Внуково 9600215, Шереметьево 9600213, Домодедово 9600216, Сочи 9623547, Пулково 9600366, Нижний Новгород 9623052, Симферополь 9600396, Екатеринбург 9600370, Самара 9600380, Анапа 9623572. Any other Yandex station ID works in the same format. Height is fixed by `size` (5 rows ≈ 302 px). Yandex may refuse data-centre or bot-like clients — verify on the real TV.

## 12. Poll, cloud photo feed, Yandex widgets

- **Poll** — builder `informers/voter/`: a form that **creates a poll on the server on every submit** (test submissions leave real polls; there is no editing or deleting from the UI). Fields: `type` bars/pie, `bar_color` (bars only), `font_size`, question, answers. Result: `voter/frame.php?qid=<N>` — the screen shows the question, options and a QR; viewers vote on their phones; results appear on the next show of the slide. Only the three basic answer fields are reliably saved. Loads scripts from CDNs.
- **Cloud photo feed** — `cloud/mail_ru.php?link=<public cloud.mail.ru folder>&number_time=<sec>`: a slideshow of images from a public Mail.ru Cloud folder, cover-fit, change every N seconds (default 5). The simplest client content channel — drop a photo in the folder, the screen updates. Depends on the cloud's public-page format.
- **Yandex organisation reviews** — in Yandex Maps: organisation → «⋯» → share → copy the reviews-widget code → HTML block. Live rating and fresh reviews.
- **Street panoramas** — Yandex Maps → panoramas → point → share → copy the **code** (not the link) → HTML block. Static imagery.
- Any third-party embed follows the same rule: HTML block, size by the block, test on the TV — heavy widgets are slow on weak panels.

## 13. Native social feeds and RSS

Left panel → «Социальные сети». These are native elements, not iframes, with card styles set in the element panel and demo data shown until a source is connected:

- **VKontakte** — wall posts, album photos, post attachments; requires the VK service connected in account settings (OAuth), and an account with rights to the group.
- **Telegram** — posts of a public channel or chat.
- **Odnoklassniki** — group posts.
- **RSS** — any valid RSS/Atom feed URL (a news site's `/feed`; `https://s.prtv.su/feed` is a valid test feed).

Only public sources work. Images and avatars load from the source sites — blocked source = empty feed. Icons for Facebook, Instagram and Twitter/X exist in the panel but working elements were not confirmed; do not promise them.

## Related

prtv-widgets · prtv-html-block-animation · prtv-editor-overview · prtv-element-layout · prtv-agent-rules
