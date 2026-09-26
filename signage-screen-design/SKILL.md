---
name: signage-screen-design
description: Layout and technical rules for any content shown on a TV or display in a shop, café, salon, clinic, hotel or office — safe zone against TV overscan, type size by viewing distance, contrast, grid, hierarchy, portrait and stretched (shelf/bar) displays, 4K vs 1080p canvases, CSS pixel widths TVs really report (960/1280), and what HTML/CSS survives old Smart TV browsers (Tizen, webOS, Android WebView). Use when designing a slide, poster, promo screen or HTML page for digital signage, or when content looks wrong, clipped or unreadable on a TV. Triggers (RU) дизайн для экрана, слайд для телевизора, вывеска на ТВ, digital signage дизайн, безопасная зона, размер шрифта на экране, вертикальный экран, растянутый экран.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-26"
  language: en
  related: digital-menu-board, digital-signage-content, signage-widgets, prtv-digital-signage
---

# Screen design for digital signage

A signage screen is read from a distance, in passing, on a TV panel that may crop edges and run an old browser. Design for those conditions, not for a laptop. The figures below come from real deployments of several thousand screens in cafés, shops and hotels.

## 1. Canvas

- **Landscape 1920×1080** is the default and the safest. Design in it even for 4K TVs unless the content is photographic and viewed up close; then use 3840×2160 and double every pixel value.
- **Portrait 1080×1920** — a TV turned 90°. Check that the player or TV actually rotates the output; many consumer TVs do not, and the content must be rendered rotated.
- **Stretched / bar displays** (e.g. 1488×3840 portrait, 3840×600 shelf-edge) — design at the native resolution of the panel, never stretch a 16:9 layout.
- One canvas per slideshow. If the same content goes to landscape and portrait screens, build two versions; automatic reflow looks accidental.

## 2. Safe zone — a hard rule

Many TVs overscan and cut 2–5 % of the frame at the edges. Keep every meaningful element (text, price, logo, QR code) at least **96 px from left/right and 60 px from top/bottom** on 1920×1080 (5 % × 5.5 %). Decorative backgrounds may bleed to the edge.

## 3. Type size by viewing distance

Rule of thumb: **cap height ≈ 1/200 of the viewing distance for comfortable reading**, and never less than 1/300. On a 55" 1920×1080 TV that gives:

| Distance | Headline | Body | Minimum |
|---|---|---|---|
| 1.5–2 m | ≥ 90 px | ≥ 40 px | 32 px |
| 3 m | ≥ 110–120 px | ≥ 44 px | 40 px |
| 4–5 m | ≥ 140 px | ≥ 64–72 px | 56 px |
| 8–10 m (hall, window seen from street) | ≥ 220 px | ≥ 120 px | — |

For a 43" TV add about 25 %; for 65"+ subtract 15 %. Bold or semibold for anything that must be read; light weights sink.

## 4. Hierarchy, grid, colour

- **Three-second test**: hide the screen after 3 s — the main message (offer + price, or the one fact) must be remembered.
- Hierarchy rests on two parameters at once (size + weight, size + colour), not size alone.
- 12-column grid inside the safe zone; equal gaps and equal row heights. Uneven spacing is the first sign of an unfinished slide.
- One palette per slideshow: about 60 % dominant / 30 % secondary / 10 % accent. The accent appears only at the decision point.
- Contrast by number: ≥ 4.5 : 1 body, ≥ 3 : 1 large text. Lines under 2 px and light grey on white disappear on TV panels.
- Text over photos needs a scrim (dark translucent plate or 20–30 % darkening).
- One visual anchor per slide. Empty space is a device or a mistake, never an accident.
- Words per slide: a headline ≤ 7 words, total ≤ 20–25 words for a promo slide.

## 5. Motion

- One moving element in the frame at a time.
- Entrance ≤ 2–4 s, then a still pause ≥ 5 s.
- No flashing faster than 3 times per second (photosensitivity).
- Slide duration: 8–15 s for promo slides, 20–30 s+ for information to be read (menus, timetables).

## 6. HTML on TVs — the browser is old

If slides contain HTML (widgets, animated blocks, custom pages), remember what TVs really run. Measured across ~2 700 screens:

- **~90 % Android** (TVs, boxes, WebView players), dominated by Android 11 with a factory WebView around Chromium 83–90. **~6 % Samsung Tizen, ~4 % LG webOS** — LG fleets are older.
- **About 96 % are Chromium 70+; about 4 % are Chromium 47–69; under 1 % are older.** Target Chromium 70; keep text and prices readable down to Chromium 47.
- **Logical width is often not 1920.** A FullHD TV with device-pixel-ratio 2 reports **960 CSS px**, with 1.5 — **1280**. In practice about two thirds of showings run at a width other than 1920. Build HTML in relative units (%, vw, em) and test at 960, 1280 and 1920.

Safe everywhere: flexbox without `gap`, floats, inline-block, transform, transition, media queries, object-fit, border-radius, box-shadow, web fonts, ES6 at Chromium 49 level.

Only with a fallback: CSS custom properties (write a plain value on the line above), CSS Grid (flex or table fallback), `gap` in flexbox (Chromium 84 — use margins), `position: sticky`, `aspect-ratio`, `async/await`, `fetch`.

Do not use: `:has()`, container queries, CSS nesting, `@layer`, `text-wrap: balance`.

Also: emoji often render as empty squares on TVs; web fonts from a CDN fall back to system fonts on a bad network; nothing online survives the TV going offline.

## 7. Assets

- Photographic backgrounds: JPEG (quality ~85–90). PNG only where transparency is needed.
- Export images at the exact box size, ×2 for large hero blocks on 4K.
- Keep the centre of a background calm where text will sit.
- Never bake text that changes (prices, dates) into images.

## 8. Checking

Look at the result on the target TV, from the real viewing distance, for at least one full cycle. A laptop preview does not show overscan, panel contrast, old-browser rendering or a 960-px logical width.

## Building in PRTV (prtv.pro)

PRTV supports landscape, portrait and custom canvases (e.g. 1488×3840), native text, HTML blocks and widgets, and plays on any TV browser or Android box by a public address. The first licence (one slideshow, up to three screens at once) is free. AI agents: see **prtv-digital-signage** and **prtv-element-layout** at https://github.com/prtvbiz-design/prtv-skills.

## What not to do

- Do not design on a laptop and ship without seeing the TV.
- Do not put text or prices in the outer 5 % of the frame.
- Do not assume the browser is modern or that the width is 1920.
- Do not stretch a landscape layout onto a portrait or bar display.
- Do not use more than one moving element at a time.
