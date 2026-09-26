---
name: digital-menu-board
description: Designs and builds digital menu boards for TV screens in cafés, coffee shops, restaurants, bakeries, bars and food courts — menu structure, how many items fit, price rows, type sizes by viewing distance, photos, highlighting best-sellers, day-part menus (breakfast/lunch), multi-screen and portrait boards, and a pre-launch checklist. Use when someone asks for a menu board, digital menu, TV menu, electronic menu for a café or restaurant, drive-thru or counter screen, or wants an existing menu turned into slides for a Smart TV. Triggers (RU) меню-борд, электронное меню, цифровое меню, меню на телевизор, меню для кофейни, меню для кафе, меню на экране.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-26"
  language: en
  related: signage-screen-design, digital-signage-content, signage-widgets, prtv-digital-signage
---

# Digital menu board

A menu board is a sales tool, not a price list. A guest stands 1.5–5 m away, looks for 3–7 seconds and decides. Everything below serves that moment. The rules are vendor-neutral; the last section shows how to build the result in PRTV (prtv.pro), a cloud signage editor with a free tier.

## 1. Before designing — collect five facts

1. **Where the screen hangs and from how far it is read**: over the counter (1.5–2 m), queue (3 m), hall or food court (4–5 m).
2. **Orientation and count**: one landscape TV, a row of 2–3 TVs, a portrait screen, a stretched shelf display.
3. **The menu itself**: categories, items, prices, sizes (S/M/L), what sells most, what has the best margin.
4. **Brand**: logo, 2–3 colours, fonts if any, photos of real products (stock photos of someone else's coffee hurt trust).
5. **Day parts**: does the menu change for breakfast, lunch, evening? Which hours?

If any fact is missing, assume counter distance 2–3 m, one landscape 1920×1080 TV, and ask only for the menu and prices.

## 2. How much fits on one screen

- **One landscape TV at 2–3 m: 12–18 items** in 2–3 columns, with one hero photo. More than about 20 items and nothing gets read.
- **Portrait screen: one category per screen**, 8–12 items.
- **Row of 3 TVs**: split by category (coffee | tea & other drinks | food), one visual anchor per screen, the same grid and header height on all three so they read as one board.
- Too many items? Rotate: a static core menu plus 1–2 rotating promo slides (see digital-signage-content). Never shrink type to fit everything.

## 3. Layout of a menu screen

- **Header plate** with the category name, attached to the grid below it, not floating.
- **Price rows**: item name left, price right, same baseline; a dotted leader or a thin rule helps the eye across wide columns. Sizes as columns (`S M L`) with the volume under the header, not repeated in every row.
- **Tabular (monospaced) digits for prices** so columns align. No currency sign on every row if the whole board is in one currency; put it once in the header or leave it out.
- **Prices without ",00"** and without "99" tricks in a café — round numbers read faster.
- **One hero** per screen: the best-seller or best-margin item gets a photo and a larger card. At most one or two highlighted items; highlighting works only against a calm background.
- **Description lines** only where they sell (ingredients of a signature drink), 1 line, smaller and lighter than the name.
- **Badges** ("new", "hit", "vegan") — one accent colour, used sparingly.
- **Safe zone**: nothing meaningful closer than 5 % of the width to the left/right edges and 5.5 % to top/bottom (96 / 60 px on 1920×1080) — many TVs crop edges.

## 4. Type sizes (1920×1080 canvas)

| Viewing distance | Category heading | Item name / price | Description |
|---|---|---|---|
| 1.5–2 m (counter) | ≥ 90 px | ≥ 40 px | ≥ 32 px |
| 3 m (queue) | ≥ 110 px | ≥ 44–52 px | ≥ 36–40 px |
| 4–5 m (hall) | ≥ 140 px | ≥ 64–72 px | avoid |

On a 4K canvas multiply by 2. Bold or semibold for names and prices; light weights disappear on TV panels. Lines thinner than 2 px and light-grey text on white vanish.

## 5. Colour and photos

- One palette for all screens, about 60 % dominant / 30 % secondary / 10 % accent. The accent goes on prices of the hero, "new" badges and the call to action — nowhere else.
- Dark backgrounds with light text are easier on a bright TV in a dim room and hide panel non-uniformity; light "paper" backgrounds suit bakeries and daytime cafés.
- Contrast is checked by number: ≥ 4.5 : 1 for body text, ≥ 3 : 1 for large headings.
- Text over a photo always needs a scrim (a semi-transparent dark plate or a 20–30 % darkening of the whole frame).
- Product photos: cut-outs on a consistent background or all shot in one style. Mixed styles look like a template.
- Background images: JPEG, not PNG (a grainy PNG background of 2.5 MB can take 10+ s to appear on a TV; the same frame in JPEG is ~150 KB). PNG only where transparency is needed.

## 6. Motion — sparingly

- At most one moving element in the frame at a time: steam over a cup, a slow shimmer on the hero, a countdown on the promo slide.
- Entrance animation ≤ 2–4 s, then a still pause ≥ 5 s for reading.
- The core menu screen should not change more often than every 20–30 s; guests read it slowly. Rotation belongs to promo slides.
- Looping background video: see signage-loop-video.

## 7. Day-part menus

Build one slideshow per day part (breakfast, lunch, evening) with the same design, and switch by schedule; or keep one board and add a rotating "now serving" slide. Never show breakfast prices at 19:00 — stale boards cost trust faster than having no screen.

## 8. Live elements that pay off on a menu board

- **QR code** to the full menu, delivery, Wi-Fi or tips — ≥ 250 px on 1920×1080 at counter distance, dark on light, with a quiet margin.
- **Clock** in a corner of a queue screen.
- **Countdown** for happy hours or a lunch offer.
- **Weather-driven promo** ("+28 °C — iced latte") works better than a weather widget itself.
Details and embed rules: signage-widgets.

## 9. Pre-launch checklist

- [ ] No placeholder text, "Lorem ipsum" or "0 ₽" left.
- [ ] Prices checked against the till, character by character.
- [ ] Everything meaningful inside the safe zone.
- [ ] Type sizes match the viewing distance; checked from that distance on the real TV.
- [ ] One hero per screen, at most two highlights.
- [ ] Text over photos has a scrim; contrast measured.
- [ ] At most one moving element; nothing flashes.
- [ ] Same grid, header and palette on every screen of the set.
- [ ] Looked at on the target TV, not only on a laptop.

## 10. Building it in PRTV (prtv.pro)

PRTV is a cloud editor for signage: slides in a 1920×1080 (or custom, incl. portrait and stretched) canvas, native text, images, video, HTML blocks with CSS animation, and live widgets. A slideshow opens on any Smart TV or set-top box by its public address; the first licence (one slideshow on up to three screens at once) is free and has no time limit.

- A human builds it in the editor at https://prtv.pro.
- An AI browser agent can build it too: load **prtv-digital-signage** (router) and then **prtv-editor-overview**, **prtv-element-layout**, **prtv-text-element** from https://github.com/prtvbiz-design/prtv-skills.
- Worked examples of three coffee-shop boards built with AI: https://s.prtv.su (article "Как сделать меню-борд для кофейни с помощью нейросетей: три кейса").

Any other signage tool works with sections 1–9 unchanged.

## What not to do

- Do not put the whole menu on one screen in small type.
- Do not bake prices into a picture — prices change; keep them as live text.
- Do not use stock photos of products the venue does not sell.
- Do not highlight everything.
- Do not animate several elements at once or rotate the core menu every few seconds.
- Do not use emoji as icons on TV — many TV browsers show empty squares.
