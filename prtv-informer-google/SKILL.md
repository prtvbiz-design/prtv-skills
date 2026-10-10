---
name: prtv-informer-google
description: The «PRTV Google» widget (s.prtv.su) — a Google Sheet, Google Calendar or Google News on a PRTV TV slide through one iframe in an HTML block; how to share a sheet («Anyone with the link — Viewer») and a calendar (public, iCal address), sheet columns (Section, Name, Price, Note, Title, Text, Picture, Show from / to), choosing the tab, column mapping, currency, modes (services and prices, tiles, table as is, announcements, ticker; schedule by day, today and tomorrow, next event; news headlines), time zone, recurring and multi-day events, update delay; recipes — a coffee-shop price list, promotions with photos, a week's events listing. Use when prices, menus, announcements, timetables or event listings on a screen must update from a spreadsheet or calendar without editing slides. Triggers (RU) информер PRTV Google, Google Таблица на экран, прайс из таблицы, Google Календарь на экран, афиша на экране, расписание на ТВ, Google Новости на экран.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-10-10"
  language: en
  related: prtv-informer-rss, prtv-design-mockups, prtv-feed-widget, prtv-widgets, prtv-integrations
---

# The «PRTV Google» widget

«PRTV Google» moves screen data to where the business already keeps it: prices and promotions in a Google Sheet, timetables and events in a Google Calendar. The owner edits the sheet from a phone and the screen follows; the slide design is untouched. The third source is Google News by keyword. One widget = one source; two sources need two HTML blocks. No API keys are needed: the widget reads only public Google addresses.

Builder (v1.0.0, Russian UI): **https://s.prtv.su/wp-content/plugins/prtv-informer-google/index_in.php**. Step 1 — «Что показываем» (what to show): Google Таблица (Sheet), Google Календарь (Calendar) or Google Новости (News); then the source settings, «Вид на экране» (on-screen view) and a live preview in four sizes (16:9 · 1920×1080, 9:16 · 1080×1920, block · 600×300, strip · 1920×200). Labels are given in Russian as they appear, with the meaning in English.

## 1. Putting it on a slide

1. Choose the source, set the view.
2. «Код для вставки — блок «HTML» на слайде» → **«Скопировать код»** (copy code) — an `<iframe>` 100%×100% that fills the whole HTML block.
3. In the prtv.pro editor: left panel → **HTML** → paste into «Код HTML»; size and position are set on the slide.
4. On a photo or coloured background — block background alpha 0 (prtv-widgets §5).
5. To change it later: on step 1 paste the finished link or iframe code into «Или вставьте готовую ссылку (или код iframe) информера, чтобы изменить его» → «Открыть» (open).

## 2. Google Sheet

### Sharing

1. Open the sheet in Google Sheets → **«Настройки доступа»** (Share, top right).
2. General access → **«Все, у кого есть ссылка»** (Anyone with the link), role **«Читатель»** (Viewer) → Done.
3. Copy the address from the browser bar, paste into «Ссылка на таблицу» (sheet link) → **«Проверить»** (check). Any sheet link works (`…/edit`, `…/edit#gid=…`, `…/edit?usp=sharing`). A private sheet shows nothing.

### Sheet layout

First row = column names, rows below = lines for the screen, in the order they will appear; up to 300 rows are read. Columns are recognised by their (Russian) names:

| Column (any of these names) | Meaning | Used in |
|---|---|---|
| Название, Заголовок, Услуга, Наименование, Позиция | Row name / title (required) | everywhere |
| Цена, Стоимость | Price | price list, ticker |
| Примечание, Описание, Состав | Small text under the name | price list |
| Раздел, Рубрика, Категория, Группа | Group heading (section) | price list, announcements |
| Текст | Announcement text | announcements |
| Дата | Entry date | announcements |
| Картинка, Фото, Изображение | Picture link | announcements |
| Показывать с / Показывать по | Show from / show until: `13.09.2026` or `13.09.2026 14:30` | everywhere |
| Показывать | `нет` (no) hides the row | everywhere |

- **Tab.** After the check, pick it from the «Лист» list; if the list could not be read, enter «Номер листа (gid)» — the number after `gid=` in the tab's address. Empty = first tab.
- **«Какие колонки что означают»** (which column means what). «Авто» = found by name; if it is wrong or your columns have their own names, pick the column letter by hand or «Не использовать» (do not use).
- **«Колонки на экране»** (columns on screen, «table as is» mode) — untick to hide a column. The service «Показывать…» columns are never shown.
- **Price.** A number is shown with a thousands separator and currency (`12500` → `12 500 ₽`). The **«Валюта»** (currency) field is what to append to the number; empty = nothing. If the cell holds text («от 500», «500 ₽», «free») it is shown as is.
- **Pictures.** A direct link to a jpg / png / webp / gif file or a Google Drive «Share» link to a file open to anyone with the link. Google Photos albums do not work.
- **Update delay.** A sheet edit usually reaches the screen in 1–2 minutes, worst case **about 4 minutes** (Google's export delay + the widget's 2-minute cache + the screen refresh interval).

### Sheet modes — «Вид на экране → Режим»

| Mode (label) | On screen | Settings |
|---|---|---|
| Услуги и цены — название … цена (services and prices) | Price list: dotted leader to the price, groups by section, note under the name | View: rows with dots / **tiles**; columns 1–3; sections; note; currency; zebra stripes |
| Таблица как есть — все колонки (table as is) | The sheet's columns as they are | Header row; stripes; columns on screen |
| Объявления — по одному на экран (announcements, one per screen) | One row large: title, text, picture | Seconds per entry, transition, picture, effects |
| Объявления — лента с прокруткой (scrolling) | Column of cards | Scroll speed |
| Объявления — сетка карточек (card grid) | Several announcements at once | Seconds per page |
| Бегущая строка (ticker) | Name and price (or title) in a line | Scroll speed |

Long price lists, tables and schedules: «Если не помещается» (if it does not fit) — **Листать страницы** (page through, «Секунд на страницу» = seconds per page) or **Прокручивать** (scroll). Sheet presets: Прайс (price list), Прайс в 2 колонки (two columns), Меню плитками (menu as tiles), Объявление (announcement), Таблица как есть (table as is).

## 3. Google Calendar

### Sharing

1. Google Calendar on a computer → hover over the calendar on the left → three dots → **«Настройки и общий доступ»** (Settings and sharing).
2. «Разрешения на доступ к мероприятиям» (access permissions) → turn on **«Открыть общий доступ»** (make available to public) and keep **«Доступ ко всем сведениям о мероприятиях»** (see all event details) — otherwise titles show as «Busy».
3. «Интеграция календаря» (integrate calendar) → copy **«Общедоступный адрес в формате iCal»** (public address in iCal format) → paste into the builder → «Проверить».

The builder also accepts a normal calendar link (`calendar.google.com/calendar/embed?src=…`, an «add to calendar» link with `cid=…`) and a calendar ID (`…@group.calendar.google.com` or a Gmail address) — it converts them to the iCal address itself. Yandex, Outlook, Bitrix24 and other calendars — by their `.ics` address. **Do not use the «secret address in iCal format»**: it would be visible in the widget link.

«+ Добавить календарь (до 3)» (add a calendar, up to 3), each with an optional on-screen name. With several calendars events get colour marks but there is no legend on screen — give the calendars names.

### Calendar settings

- **Time zone** — a list of Russian and CIS cities (Kaliningrad … Kamchatka, Minsk, Almaty, Tashkent and others) or «Другой…» (other) with an IANA zone name (`Asia/Dubai`). Display does not depend on the TV's clock zone.
- **Period:** today only / today and tomorrow / 7 days / month / next N events.
- Show events already finished today, end time, place, event description (video-meeting links and web addresses are stripped from descriptions), text when there are no events (default «Нет предстоящих событий» — no upcoming events).
- Recurring events (daily, by weekday, "second Tuesday of the month", excluded and moved occurrences) are expanded correctly; a multi-day event appears on each of its days; an event in progress is marked «сейчас» (now).
- New events reach the screen within 5–7 minutes.

### Calendar modes

| Mode (label) | On screen |
|---|---|
| Расписание по дням (schedule by day) | Events grouped by day — event listing, class timetable |
| Сегодня и завтра — две колонки (today and tomorrow) | Two columns, good for a lobby or reception |
| Ближайшее событие крупно (next event, large) | One event per screen, in turn |
| Бегущая строка (ticker) | Events in a line |

Presets: week schedule, today and tomorrow, next event, month listing.

## 4. Google News

- «+ Добавить запрос (до 3)» (add a query, up to 3). Words as in a search: `кофейня Москва`; `"exact phrase"`, `-word` to exclude, `site:rbc.ru` for one site.
- **Language** and **country** of the results; **not older than** — a day / 3 days (default) / a week / a month / no limit; **similar stories** — one per story (default) / up to two / up to three / no limit (exact duplicates are always removed).
- **Google News has no pictures and no article text** — only the headline, publication and time. So the modes are headline modes: carousel of headlines, scrolling list, card grid, ticker.
- «Только со словами» / «Исключить слова» (include / exclude words) work here too (whole-word match).

## 5. View and styling (common to all sources)

Selection («Какие записи брать»): number of entries, not older than, order (as in the sheet / newest first / oldest first), only rows with a picture, word filter. «Что показывать в записи» (what to show): picture (position, fit), text and max lines, section, publication, date, «new» badge. Header — «Показывать шапку над содержимым» (own text; empty = sheet, calendar or query name). Effects: title entrance, progress bar to the next entry, slow zoom on the photo, text shadow. Styling: theme (cards / no plate / dark), font (Inter, Roboto, Montserrat, PT Sans, Open Sans, Oswald, Arial; the widget's bundled fonts — all but the system Arial — include the ₽ sign), card background, text, accent, «Прозрачный фон вокруг (виден фон слайда)» (transparent surround, slide background shows), alignment, font size / radius / padding for 1920×1080, scaled to the block. «Обновлять данные каждые, с» (refresh every, s) — 30–3600, default 120.

On failure the screen keeps the previous data, and stays transparent until the first load; if a source is down the server serves its saved copy (up to 3 days). "Nothing to show" (announcement expired, no events) is not a failure: the screen clears, and the calendar shows its "no events" text. The «show a small caption on failure» checkbox is for debugging only.

**Fit to the block.** For a narrow strip (1920×200) only the ticker and the carousel work — the other modes need height. In «table as is» narrow columns break words mid-word: hide unneeded columns (especially picture links) in «Колонки на экране». A price list on a portrait screen with the default font fills only the top — raise the font size or the number of columns. A carousel of short announcements without pictures leaves empty space — use the «Объявление» preset (centred, large font).

## 6. Recipes

### 6.1. Coffee-shop price list

1. Sheet: `Раздел | Название | Цена | Примечание` (section, name, price, note) — «Кофе | Капучино 300 мл | 220 | double espresso, milk»; sharing «Anyone with the link — Viewer».
2. «Ссылка на таблицу» → «Проверить» → «Лист».
3. Preset «Прайс в 2 колонки» (services and prices, 2 columns) or «Меню плитками» (view: tiles); currency `₽`; sections grouped.
4. Theme dark or cards; a font readable from afar — Oswald or Montserrat; raise the font size until the list fills the block without an empty bottom; «Если не помещается → Листать страницы».
5. Stop list: write `нет` in the «Показывать» column — the item leaves the screen, no need to delete the row.

### 6.2. Promotions with photos

1. Sheet: `Заголовок | Текст | Картинка | Показывать с | Показывать по` (title, text, picture, show from, show until) — «Breakfast till 11:00 | Porridge and coffee — 290 ₽ | <jpg link> | 01.11.2026 | 30.11.2026 23:59».
2. Mode «Объявления — по одному на экран», only rows with a picture, picture position **«Фоном»** (background), text shadow, slow zoom, 8–12 seconds per entry.
3. A promotion leaves the screen by itself at «Показывать по»; one prepared in advance appears at «Показывать с».
4. Photos — your own or freely licensed; a direct file link or a Google Drive «Share» link.

### 6.3. A week's events listing

1. A separate Google Calendar «Events», made public (§3); copy the public iCal address.
2. Preset «Расписание на неделю»: mode schedule by day, period 7 days, header on.
3. The venue's time zone; place shown, description as needed; no-events text such as «New events coming soon».
4. Make regular events recurring (yoga on Tuesdays, a tasting every Friday) — the widget expands them; a three-day festival is one multi-day event.
5. For a reception desk — «Сегодня и завтра — две колонки»; for a single screen at the entrance — «Ближайшее событие крупно».

## What not to do

- Do not publish a sheet or calendar with personal data of guests, patients or staff: "anyone with the link" means anyone.
- Do not paste the secret iCal address.
- Do not expect instant updates: sheet — up to ~4 minutes, calendar — up to 5–7 minutes.
- Do not promise pictures or article text from Google News.
- Do not put a price list, schedule or grid into a 200 px strip — only a ticker or carousel fits there.
- Do not retype prices on the slide when the sheet feeds them: the screen price must match the till.

## Related

prtv-informer-rss · prtv-design-mockups · prtv-feed-widget · prtv-widgets · prtv-integrations · menu-board-by-venue
