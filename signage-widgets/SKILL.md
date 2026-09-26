---
name: signage-widgets
description: Adds live widgets to digital signage screens and TV slideshows — clock, weather, countdown timer, QR code (menu, Wi-Fi, reviews, tips), calendar, currency and metal rates, happy-hour or business-lunch promo card, RSS and social feeds — as an iframe in any signage tool that accepts HTML; how to pick a widget for the goal, size it so nothing is clipped, make it transparent over a photo, keep it working on old TV browsers and poor networks, and ready builder URLs. Use when someone wants a clock, weather, QR, timer or rates on a TV screen, menu board or info display. Triggers (RU) информер, виджет на экран, часы на телевизор, погода на экране, QR-код на экран, таймер обратного отсчёта, курсы валют на экран, счастливые часы, бизнес-ланч.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-26"
  language: en
  related: signage-screen-design, digital-signage-content, prtv-widgets, prtv-widgets-catalog
---

# Live widgets on signage screens

A widget is live content on a slide: a clock, weather, a countdown, a QR code, rates, a feed. Widgets are accents that make a screen feel alive and current; the content (menu, offer) stays the main thing.

## 1. Pick by goal, not by looks

| Goal | Widget |
|---|---|
| Urgency for an offer | Countdown; promo card with a timer (happy hours, business lunch, closing discount) |
| Relevance to the moment | Weather — best used as a trigger for an offer ("+28 °C — iced latte") |
| Guest action | QR: full menu, Wi-Fi, booking, tips, review |
| Waiting area, lobby | Clock, weather, currency rates, timetable, TV programme |
| Freshness without redesign | Daily items (holidays, moon phase, work-day countdown), calendar events, RSS |
| Social proof | Reviews or social feed |

Rule: one "hot" live widget per loop (a countdown *or* a weather promo *or* a video hero). Two animated widgets on one slide compete and both lose.

## 2. How widgets get onto a screen

Almost every signage tool accepts either native widget elements or an **HTML / web-page element that shows an `<iframe>`**. The universal path:

```html
<iframe src="https://<widget-url>" frameborder="0" width="100%" height="100%" style="overflow:hidden;"></iframe>
```

Put it into the HTML element, size the element, set the element's own background to transparent. Always write `https://` explicitly — protocol-relative `//host/...` breaks in some players.

## 3. Rules that make widget URLs work

1. **Colours with the hash encoded**: `%23FFFFFF`, not `#FFFFFF` (a raw `#` ends the URL) and not `FFFFFF` (an invalid CSS colour, silently ignored).
2. **Every text value through `encodeURIComponent`** — titles, offers, Wi-Fi names, prices with currency signs. A raw `&`, `+`, `/` or `#` breaks the query.
3. **Read the widget's own parameter names.** There is rarely a shared convention between widget types; never carry names from one type to another.
4. **City names** — use the exact spelling the service expects; many regional services want the local-language name. A wrong city makes a clock silently show UTC.

## 4. Transparency — two layers

A widget page has its own background, and the element holding the iframe in the editor has another. The outer one wins. For a widget over a photo: transparent background in the widget URL **and** alpha 0 on the element; text colours chosen to read against the photo (add a scrim if needed).

## 5. Sizing — match the widget's shape

- **Fixed-proportion** widgets (analogue clocks 1:1, digital clocks ~2:1, rate tables): give the box that proportion or circles flatten and cards spill.
- **Fluid** widgets (weather, calendars) scale fonts with width; content height ≈ k × width. A box lower than that clips the bottom. Measure k by opening the URL in a tab at the target width and running `document.body.scrollHeight / window.innerWidth` (not `documentElement.scrollHeight`, which never drops below the window).
- **Self-fitting** widgets (built with `clamp()` and flex centring) fit any box.
- Remember that many TVs report 960 or 1280 CSS px, not 1920 (signage-screen-design §6): test there.

## 6. Reliability on real TVs

- Nothing live survives the TV going offline. For unattended screens prefer self-contained widgets (clock, countdown, QR, promo card) that need only their own host.
- Widgets that call third-party services from the TV (maps, stock scripts, Google Calendar, social feeds) fail silently if the venue's network blocks them. Test on site.
- `http://` resources inside an `https://` player are blocked (mixed content).
- Emoji render as squares on many TVs.
- Countdowns count on the device clock — a TV with a wrong time zone shows a wrong timer.
- Give slides with maps or feeds ≥ 15 s so they finish loading in view.
- Slide thumbnails in most editors do not render iframes; judge only in the player.

## 7. QR codes on screens

- ≥ 250–300 px on a 1920×1080 canvas at 2–3 m, dark modules on a light plate, a quiet margin of at least 4 modules.
- Short URLs make sparser, more scannable codes.
- Caption with the benefit ("Menu", "Wi-Fi", "−10 % on review"), not "Scan me".
- A Wi-Fi QR embeds the password in the widget URL — treat the embed as containing it.

## 8. Ready-made widget builders (PRTV)

PRTV (prtv.pro) publishes about 30 public widget builders at **https://s.prtv.su/informery** — each builder page generates the iframe code. Useful ones:

- Clocks, 21 configurable types — `https://s.prtv.su/informery/chasy`; 30 finished analogue dials — `/analogovye-chasy-vybor-cziferblata`
- Weather, 7 views — `/openweather`
- Countdown — `/countdown`
- QR (link / Wi-Fi / text) — `/qr-infomer`; render file `https://s.prtv.su/informers/qr_horeca/qr.php?type=link&title=Menu&text=https%3A%2F%2Fexample.com%2Fmenu&transpar=1&font_text=%23ffffff`
- Calendar — `/kalendar`; Google Calendar — `/google-kalendar`
- Promo card (happy hours / business lunch / combo / closing discount) with a live timer, currency and precious-metal rates, holidays, moon phase, maps, TV programme, RSS and more.

Builders are in Russian; widget text and city names are Russian-first. Full parameter reference for every widget: **prtv-widgets** and **prtv-widgets-catalog** in https://github.com/prtvbiz-design/prtv-skills. In the PRTV editor itself widgets go into an HTML block or come from the native «Информеры» buttons.

## What not to do

- Do not stack two live widgets on one slide.
- Do not write colours without `%23` or text values unencoded.
- Do not put a fluid widget into a box lower than k × width.
- Do not use a network-dependent widget on a screen whose network you have not tested.
- Do not judge a widget by an editor thumbnail.
