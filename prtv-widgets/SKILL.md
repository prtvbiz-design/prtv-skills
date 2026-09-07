---
name: prtv-widgets
description: Widgets ("informers") in the PRTV (prtv.pro) digital-signage editor — the two ways to add one (native widget buttons vs. the public builders on s.prtv.su embedded through an HTML block), the universal rules that make a widget URL work (colours with %23, city names in Cyrillic, text through encodeURIComponent, identify the type by the php file name), why parameter names differ between widgets, two-level transparency, sizing fluid widgets so nothing is clipped, offline and dependency risks on TVs, thumbnails that show nothing, and how to accept a widget on the public page. Use before adding, restyling or debugging any clock, weather, calendar, QR, countdown, finance, promo, map or social widget in the prtv.pro editor; the per-widget parameter reference is in prtv-widgets-catalog.
license: CC-BY-4.0
metadata:
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-09-06"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# Widgets in the PRTV editor — common rules

A widget (PRTV calls them **informers**) is live content on a slide: a clock, weather, currency rates, a countdown, a QR code, a promo card, a calendar, a map, a social feed. This skill holds what is true for all of them; prtv-widgets-catalog lists each one with its views and parameters. The editor itself is described in prtv-editor-overview; HTML blocks in prtv-html-block-animation.

## 1. Two ways to get a widget onto a slide

**A. Native widget buttons** in the left panel (section «Информеры»: Clock, Weather, Air quality, Currency rates, Transport timetable, Traffic, Restaurant menu; section «Социальные сети»: VKontakte, Odnoklassniki, Telegram, RSS). One click adds an element with a settings form in the element panel. The Restaurant-menu element needs a POS system connected in account settings (`https://prtv.pro/settings`); the VK element needs the VK service connected there too.

**B. The public builders on s.prtv.su.** The catalogue is `https://s.prtv.su/informery` (30 builders, three pages), each builder at `https://s.prtv.su/informery/<name>` — for example `/chasy` (clocks), `/openweather` (weather), `/qr-infomer`, `/countdown`, `/kalendar`, `/google-kalendar`. A builder produces an `<iframe>` code. Paste it into an **HTML block** on the slide. This path gives the full range of views and parameters and is the one this skill set documents.

A widget already on a slide does **not** reopen its builder: double-click on a clock or weather element opens the general element panel. To change how a widget looks, generate a new code in the builder and replace the HTML of the block.

## 2. Inserting a builder code

1. Configure the widget on its builder page and copy the code (the builder regenerates it on every input; there is no "save" to press). The code is a full tag:
   `<iframe src="https://s.prtv.su/informers/<type>/<file>.php?…" frameborder="0" width="100%" height="100%" style="overflow:hidden;"></iframe>`
   Some builders emit `//s.prtv.su/…`; write `https://` explicitly.
2. In the editor: left panel → **HTML** → click the new block → paste the code into «Код HTML» (see prtv-html-block-animation for the reliable way to fill the field).
3. Element panel → background colour → alpha **0**. Without this the block has a white plate under the widget whatever the URL says (§5).
4. Resize the block to the widget's proportion (§6). Set the depth.
5. Check in the preview and on the public TV page (§8).

## 3. Three rules without which nothing works

1. **Colours with the hash, encoded as `%23`.** `fon_table=%234CAF50` becomes `#4CAF50` in CSS. `fon_table=4CAF50` produces an invalid value, the browser ignores it and the widget stays in its default colours — with no error anywhere.
2. **City by name, in Cyrillic, from PRTV's own city base.** `city=Москва` works; `city=3` (an offset) or `city=Moscow` does not. Clocks then silently show UTC time; weather shows an error text on the slide. Cities confirmed in the base: Москва, Санкт-Петербург, Казань, Краснодар, Сочи, Минск, Калининград, Екатеринбург, Новосибирск, Владивосток, Алматы, Ташкент, Дубай, Берлин, Мюнхен, Париж, Прага, Лондон. Not found: Франкфурт and any Latin spelling.
3. **Text values through `encodeURIComponent`** — titles, slogans, Wi-Fi names, offers, prices with ₽. A raw `&`, `/`, `+` or `#` in a value breaks the query string.

Dates in calendar widgets are `MM/YYYY` with the slash encoded as `%2F`; an ISO date returns a server error.

## 4. Parameter names differ between widgets — identify the type first

There is **no common naming convention**. The colour of digits is `dig_color_font` in one clock, `color_font1` in another, `font_text` in weather, `color_text` in stocks. Many clock types prefix every parameter with the type name (`neon_color_fon`, `rotate_city`). The builder's form labels often differ from the URL names (the form says `color_fon`, the URL says `fon_table`).

Before reading or writing a widget URL, read the **php file name** in the `src` (`clock_digital.php`, `weather_wide_flexible.php`, `calendar.php`, `qr.php`, `action.php` …) and use the parameter block for exactly that file from prtv-widgets-catalog. Never carry parameter names from one type to another.

The city field on the builder pages is an autocomplete: type the name and pick a suggestion; setting the field's value by script does not regenerate the code.

## 5. Transparency — two levels, the outer one decides

A widget page has its own background (parameter `transpar=1`, often paired with `fon_table=transparent`), and the **HTML block that contains it has its own background** in the editor. The block's background covers the iframe's, so a widget with `transpar=1` still sits on a white plate until the element's background alpha is 0.

Recipe for a widget over a photo or video: `transpar=1`, remove `fon_table`, choose text colours that read against the photo, **and** set the block's background alpha to 0 in the element panel. Never combine `transpar=1` with a hex background colour — the two contradict each other. The element-panel opacity and background work for every widget type, including the few whose own transparency flag is ineffective.

In the newer family of widgets (promo card, moon calendar, work-day countdown) `transpar` must be `1` or **empty** — an empty value means "use `fon_table`"; the builders send it empty.

## 6. Sizing — the box must match the widget

Two kinds of layout:

- **Fixed-proportion widgets** (clocks, dials, finance tables): the content is drawn for a proportion — square 1:1 for analogue faces, cubes and rings, wide 2:1 for digital, flip, neon and glitch clocks. In the wrong proportion circles flatten and cards spill over the edge. Give the block the widget's proportion.
- **Fluid widgets** (weather views, calendars): fonts scale with the width (`vw`), so the content height is roughly **k × width**, with k a constant of the view. `width/height=100%` on the iframe does not shrink the content to the box; if the box is lower than k × width, the bottom is clipped. The k values are in the catalogue; the box height is `ceil(k × width) + 6 px`.
- **Self-fitting widgets** (promo card, moon, work-day, QR): typography on `clamp()` with flex centring — they fit any box without clipping.

**Measuring k yourself** — open the widget URL directly in a browser tab at a width close to the target box width and run in the console:

```js
document.body.scrollHeight / window.innerWidth
// or, more robust: document.querySelector('table').getBoundingClientRect().height / window.innerWidth
```

Do not use `document.documentElement.scrollHeight`: it is never smaller than the window, so for content shorter than the viewport you get the window's proportion, not the content's. A tell-tale of that mistake is the same "k" for widgets of different shapes.

Some views change layout below a certain width (media queries) — the catalogue marks them; measure at the target width.

## 7. Two rendering contexts and no thumbnails

- **Slide strip thumbnails do not render widgets** — an "iframe blocked" placeholder stands in. Never assess a widget slide from the strip.
- **The editor canvas is a fixed-pixel preview**; fluid widgets (weather) are laid out for a 1200×300 base there and clip their icons. The public page is fluid and correct. This is a known limitation of the preview, not of the widget.

## 8. Acceptance

1. Preview player (eye button) — the widget is present, the box is not clipped, colours applied.
2. Public TV page `https://prtv.pro/<TV-number>` — the reference for widget layout: fluid widgets render correctly only here. Wait at least one full slide duration.
3. For clocks: the time equals the real time of the city. For weather: the city name and a temperature are shown (a "city does not exist" text means the city string is wrong). For calendars: the month is drawn (an empty block means the wrong month-parameter set — see catalogue).
4. Reload the editor and confirm the HTML of the block is still there.
5. Check at least once on the target TV or set-top box: TV browsers differ from desktop (fonts, emoji, mixed content, autoplay).

## 9. Offline, network and dependency risks

No widget survives the TV going offline; live ones (weather, rates, calendars, maps, feeds) need the network at every show. Beyond that:

- **Self-contained on s.prtv.su:** clocks, dials, plain calendar, QR, countdown, promo card, moon, work-day, holidays, currency rates (CB RF / NB RK), precious metals. They need only s.prtv.su.
- **Depend on third-party services from the TV:** Google calendar (Google API + CDN), maps and air quality (tile servers, map APIs, aqicn), stocks (CDN scripts), NB RB rates (fetched from nbrb.by by the TV), Yandex timetable (rasp.yandex.ru — may reject data-centre or bot-like clients), social feeds and RSS (source sites and CDNs). If any of these is blocked on the venue's network, the widget is empty with no message. Prefer self-contained widgets for unattended screens; test the others on site.
- **Mixed content:** some map tiles and channel logos are served over `http://`; an `https://` player may block them (map without the weather layer, logos missing). Check on the TV.
- **Emoji:** moon phases and the "fun" work-day phrases use emoji; a TV without an emoji font shows squares.
- **Slow networks:** map tiles and feeds load in view; give such slides ≥ 15 s.

## 10. Choosing a widget for a task

| Task | Widget |
|---|---|
| Urgency for an offer (FOMO) | Countdown timer; promo card with timer |
| Day-part trigger | Calendar / Google calendar — as show logic, not as the visual focus of a till board |
| Context relevance ("hot today — take a cold drink") | Weather |
| Weekly freshness without rebuilding | Daily items (moon, holidays, work-day), Google calendar events |
| Social proof, live news | Social feeds, RSS, Yandex reviews widget |
| Guest interaction | QR (menu, Wi-Fi, tips, reviews), poll with QR |
| Foyer, waiting room | TV programme, timetable, currency rates |

Design rule: one "hot" live widget per slideshow cycle (countdown *or* weather promo *or* video hero), plus one or two static content slides. Two animated widgets on one slide compete for attention. Widgets are accents; the menu is the content.

Labels near a widget (a caption under a countdown, a heading above the weather) are native Text elements in the 1920 space — ≥ 40 px for a caption, ≥ 110 px for a heading (prtv-element-layout §7).

## What not to do

- Do not write a colour without `%23`.
- Do not pass a city as a number or in Latin letters.
- Do not reuse parameter names across widget types; read the php name first.
- Do not expect `transpar=1` alone to remove the white plate — set the block's alpha to 0.
- Do not judge a widget by the slide-strip thumbnail or by the editor canvas; use the public page.
- Do not put a fluid widget into a box lower than k × width.
- Do not put a network-dependent widget on a screen whose network you have not tested.
- Do not stack two live widgets on one slide.
- Do not paste a builder code with `//s.prtv.su` — write `https://`.

## Related

prtv-widgets-catalog · prtv-editor-overview · prtv-html-block-animation · prtv-element-layout · prtv-slide-settings · prtv-agent-rules
