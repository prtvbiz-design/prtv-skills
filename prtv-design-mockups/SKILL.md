---
name: prtv-design-mockups
description: Design techniques with live widgets in the PRTV (prtv.pro) digital-signage editor — the editor's built-in perspective (right-click → «Включить режим работы с перспективой» → drag corners to the frame's corners) and ready mock-ups — news on a billboard against a city with date and source on panels under it, a screen in the client's interior with glass glare, a newspaper page built from several widgets, three screens on building facades with a single moving animation, a frosted card over a photo; general rules — background as an «Image» element on the bottom layer, widget without plate on a transparent background, one moving element per frame, captions readable on a TV. Use when you need a striking demo slide, a promo or a pitch showing a client their screen, a "screen within a screen", or a widget on a billboard, in a newspaper or over a photo. Triggers (RU) мокап экрана, информер на щите, экран в интерьере, перспектива в PRTV, газетная полоса, стекло поверх фото, дизайн-приёмы PRTV.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-10-10"
  language: en
  scope: editor UI and widget builders; no private API calls
  related: prtv-informer-rss, prtv-informer-google, prtv-element-layout, prtv-widgets, prtv-slide-settings, signage-screen-design
---

# Mock-ups and design techniques with PRTV widgets

A live widget on its own is a card in a rectangle. The same widget fitted into a street billboard, a TV on a café wall or a newspaper column becomes a demonstration: the client sees not "a widget" but their future screen in their own setting. The techniques below were built and checked on the PRTV RSS and PRTV Google tutorial slideshows (October 2026) and use only the standard tools of the editor and the widget builders. The editor's interface is in Russian; labels are given as they appear, with the meaning in English.

## 1. General rules

1. **The background is an «Изображение» (Image) element covering the whole slide on the bottom layer**, not the slide's «Фоновое изображение» (background image) field: that way it reliably loads and shows on every device. Bottom layer — «Позиция → Под всеми» (position: below all) or the «Глубина» (depth) buttons (prtv-element-layout §2). Check the layer order after all content edits.
2. **Background as JPEG, 1920×1080, about 100–200 KB** (quality ~85–90). PNG only where transparency is needed (glass glare, a darkening overlay). A 2–3 MB PNG background takes 10–15 seconds to load on a TV.
3. **A widget over a picture has no plate of its own:** in the builder «Тема → Без подложки» (theme: no plate) + **«Прозрачный фон вокруг карточек»** (transparent background around the cards); in the editor, HTML element background alpha 0. Pick the text colour to suit the background; over photos turn on the text shadow.
4. **No more than one moving element per frame.** With several widgets on a slide only one moves (a carousel with a short «Время на новость», time per item); the others get 120 s so they do not change while the slide is shown (15–20 s). The eye must know where to look.
5. **Captions and hints must read on a TV:** captions from 40 px, headings from 56–110 px in the 1920×1080 space (prtv-element-layout §7); the smallest text inside a mock-up (a newspaper column, a panel under a billboard) not below ~24 px. Check in full-screen preview, not on the editor canvas.
6. **The empty frame before loading.** A widget appears a few seconds after the slide changes. Draw the frame under it in the background as a "switched-off screen" (dark glass) or a neutral surface, so the pause looks natural. Give the slide at least 15–20 s.
7. **Draw backgrounds without other brands or recognisable real buildings**; photos — your own or freely licensed.

## 2. The editor's built-in perspective

Fitting a widget into a slanted frame (billboard, screen on a wall, facade) is a standard editor function; no CSS wrappers in the HTML code are needed.

1. Place the HTML element with the widget code roughly over the frame in the background and size it to the frame (prtv-element-layout §1). The element's proportion ≈ the frame seen head-on (a 6×3 billboard — 2:1, a TV — 16:9).
2. Right-click the element on the canvas → **«Включить режим работы с перспективой»** (enable perspective mode).
3. Drag the element's corners one by one to the four corners of the frame in the background. Zoom the canvas in first — a corner a few screen pixels wide is easy to miss.
4. Check in the slideshow preview: the widget's corners match the frame's corners, the text is sharp and readable. Use a large font in the builder (64–96) — perspective shrinks the far edge.
5. Perspective applies to the whole element including the iframe content. How TV browsers render it has not been checked separately — always look on the target TV.

Perspective works for ordinary images too (glare, frames). Do not switch it on by accident: the menu item is a toggle (prtv-element-layout §4).

## 3. Mock-ups

### 3.1. News on a billboard

- **Background:** a city (sky gradient, haze, lit windows) and a 6×3 billboard on a pole, turned slightly; two empty light panels under the billboard.
- **Widget:** PRTV RSS, type **«Свободная компоновка»** (free layout), only entries with a picture. On the builder canvas: Photo — left part of the billboard, Title — right part, and the **Date** and **Source** blocks moved down onto the panels under the billboard. Theme «Без подложки», transparent background, radius and padding 0, a large font (Oswald 96), 8 s per item.
- **Fitting:** one HTML element over the billboard and panels, built-in perspective by the corners (§2). Date and source change with the story because it is one widget.

### 3.2. A screen in the client's interior

- **Background:** the venue's wall (brick, a shelf, a lamp) and a TV on the wall at an angle; the TV screen in the background is dark glass.
- **Widget:** carousel with the picture on the left, dark theme, topical feeds (food for a café, cars for a car wash), accent in the interior's colour.
- **Fitting:** perspective by the screen's corners. **Glass glare** — a separate «Изображение» element with a PNG (transparent diagonal glare) **one layer above** the widget, with the same perspective or drawn already in perspective. Without glare the screen looks like a sticker.
- This mock-up works well on a photo of the client's real room: "this is how it will look at your place".

### 3.3. A newspaper page from several widgets

- **Background:** a newspaper sheet — masthead, column rules, section labels, paper texture; the column areas are empty, no placeholder text.
- **Widgets:** one HTML element per column, **each column with its own feed and its own section** (culture, science, food, events, travel); the section label comes from the feed's on-screen caption or is printed on the background. All in free layout, «Тема → Без подложки», transparent background, dark text (#1A1A1A), one newspaper accent (dark red), PT Sans.
- **Motion:** only the lead story changes (~12 s per item); the columns get 120 s and do not change during the slide.
- Columns from feeds without pictures — title only or title with text; the page looks more natural that way.

### 3.4. Three screens on facades

- **Background:** a square in the evening, three media screens on facades at different angles.
- **Widgets:** each screen has its own HTML element, its own link and its own perspective; different content (sports, science, travel) and different looks (photo as background; titles only, centred; picture on top on a light card).
- **Motion:** one screen is animated (carousel, 7 s); the other two get 20 s or more — exactly one change at a time in the frame.

### 3.5. A frosted card over a photo

- **Background:** a calm photo (sunset, lake, interior) with a translucent frosted card already drawn in — the blur and the light edge are made in the image, not in the widget.
- **Widget:** a scrolling feed or carousel **without plate, on a transparent background**, white text, a warm accent, text shadow, a header above the feed ("Where to go"); feeds matching the photo (travel, events).
- HTML element exactly over the card, no perspective.

## 4. Build order

1. Draw or pick a 1920×1080 background (JPEG), upload it as an «Изображение» element, stretch it over the slide, send it to the bottom.
2. Build the widget in its builder (prtv-informer-rss, prtv-informer-google) and check it in the preview at the right size.
3. HTML element → code → background alpha 0 → size to the frame → perspective (if needed).
4. Layers above the widget (glare, frame) as separate images.
5. Captions and hints as native text in a free part of the frame (sky, wall), not over the main object.
6. Slide duration 20 s, transition «Затухание» (fade); full-screen preview; check on the TV.

## What not to do

- Do not put the background into the slide's «Фоновое изображение» field under a mock-up — use an element.
- Do not leave the widget's plate on over a background picture: a white card on a billboard or in a newspaper breaks the illusion.
- Do not run two carousels in one frame.
- Do not write hints smaller than 24 px or put them over the main object.
- Do not build perspective with CSS transforms in the HTML block's code when the built-in mode exists.
- Do not promise that perspective looks on every TV as it does in the preview — check on the target device.

## Related

prtv-informer-rss · prtv-informer-google · prtv-element-layout · prtv-widgets · prtv-slide-settings · signage-screen-design
