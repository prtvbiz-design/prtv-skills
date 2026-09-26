---
name: prtv-element-layout
description: Placing and controlling elements on a slide in the PRTV (prtv.pro) digital-signage editor — position and size by dragging, rotation, depth (layers), keep aspect ratio, permanent elements on every slide, the right-click menu, entrance animations (57 presets), clickable links for touch kiosks, and layout rules for a TV screen (safe zone, type sizes by distance, contrast, 60/30/10 palette, motion). Use when moving, resizing, layering, animating or linking an element, or checking the composition of a menu board or promo slide in prtv.pro. Triggers (RU) расположить элемент, слои, анимация появления, кликабельный элемент, безопасная зона, вёрстка слайда PRTV.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-26"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# Element layout in the PRTV editor

Every element on a PRTV slide — text, image, video, HTML block, widget — shares the same set of controls above its content: where it sits, how big it is, which layer it is on, whether it repeats on every slide, how it appears, and what happens when someone taps it. This skill covers those controls and the rules for laying elements out on a TV screen. Everything about the interface below was checked in the browser, not taken from documentation. The canvas, panels and coordinate space are described in prtv-editor-overview; this skill assumes it.

## 1. Position, size, rotation

**There are no numeric X / Y / width / height fields.** Position and size are set only by dragging on the canvas. Values live in the 1920×1080 slide space and scale to any screen.

- **A new element** appears in the top-left corner of the slide, at (0, 0), with a default size (an HTML block, for example, is 400×200).
- **Move** — drag an element that is *not* selected. Dragging a *selected* text element starts text editing instead of moving it; press Escape first, then drag.
- **Resize** — drag the handles of the selection frame (`.moveable-control-box`). The middle-right handle is the safest: the bottom handles may sit below the visible edge of the browser window.
- **Rotation** — a field in the element panel, 0–360° with a step.
- **Keep aspect ratio** — a toggle in the element panel; on by default for images, so resizing an image keeps its proportions unless you switch it off.
- **Opacity, border, padding, background colour and image** — also in the element panel, common to all types.

### Reading the exact geometry

Screenshots are the wrong instrument for positions. Read the element node instead — the values are already in slide pixels:

```js
const el = document.getElementById('slide-element-<id>');
const s = getComputedStyle(el);
({ left: s.left, top: s.top, width: s.width, height: s.height, depth: s.zIndex });
```

For a whole-slide inventory (ids, types, positions, depth of every element) use the read-only local store described in prtv-editor-overview.

### Dragging precisely

Convert slide coordinates to screen coordinates with the scale and offset from prtv-editor-overview (screen = offset + scale × slide). A move is one pointer-down, a pointer-move, a pointer-up, with a pause between steps. After the drop, re-read the geometry from the DOM and correct with a second drag if needed. Do not chain clicks or double-clicks "to be safe": a stray click on an element becomes a drag that carries it off the slide.

## 2. Depth — layering

**Depth** is the z-index of the element: a stepper in the element panel. Higher depth = closer to the viewer. The slide background (colour, image or video from slide settings) is drawn at depth 0 and hides nothing; content sits at depth ≥ 1.

The top-panel button with the picture icon opens the list of the current slide's elements ordered by depth — the quickest way to see the stack without clicking through elements.

A layout that works in practice:

| Depth | Layer |
|---|---|
| 0 | background image or video (a stretched Image element, when you need effects on top of it) |
| 1 | atmosphere: sky, wind, particles (HTML blocks) |
| 2–10 | the main content: texts, product photos, cards |
| 11–16 | overlays: plates, tints, screen effects |
| 20 | text that must stay above an overlay |

Two consequences:

- To make something "emerge from behind" a detail of the background, cover that detail with an opaque plate placed at a depth above the moving element. The background itself cannot occlude anything.
- A semi-transparent tint over the whole frame is an element with a translucent fill stretched to 1920×1080 at a depth between the background and the content.

There are no groups and no lock in the editor; layering is done element by element.

## 3. Permanent elements and element actions

**Permanent element** (Yes / No) in the element panel shows the element on every slide of the slideshow — the tool for a logo, a clock or a ticker that should never leave the screen. This is the closest thing to "pinning" an element; there is no separate lock. The same "general settings" block also has a «На всех слайдах» (on all slides) toggle, which does the same for the rotation, and a «Позиция» select («Под всеми» = the bottom layer) next to the numeric «Глубина»; read their current state from the panel rather than assuming it. A permanent element appears on new slides automatically, and duplicating a slide copies permanent elements too — see prtv-agent-rules.

Actions at the bottom of the element panel: deselect (✕), **duplicate**, **delete** (trash). A small toolbar next to the selected element on the canvas repeats the trash icon and, for images, adds **crop**.

Duplicate, delete and depth are *not* in the right-click menu — look for them in the panel.

## 4. Right-click menu on an element

Seven items, identical for every element type. The editor's interface is in Russian; labels are given as they appear, with the meaning in English.

| # | Label in the editor | Meaning | What happens |
|---|---|---|---|
| 1 | Сделать кликабельным | Make clickable | Opens the link dialog (§6). If the element already has a link the item reads **Удалить ссылку** (Remove link) and removes it immediately. |
| 2 | Настройки стиля элемента | Element style settings | Opens the element panel. |
| 3 | Настройки анимации элемента | Element animation settings | Opens the animation dialog (§5). |
| 4 | Включить сбор статистики | Collect statistics | Toggle: per-element analytics. |
| 5 | Сделать рекламным элементом | Mark as an advertising element | Often greyed out; the conditions under which it becomes available are not documented here. |
| 6 | Включить режим работы с перспективой | Perspective mode | Toggle. |
| 7 | Включить режим масштабирования | Scaling mode | Toggle. |

Items 4–7 change modes whose visible effect was not examined for this skill; leave them off unless the task asks for them.

Right-click on an *empty* part of the canvas opens the slideshow defaults (styles of new slides and elements), not an element menu.

## 5. Entrance animation

Open from the right-click menu (item 3) or from the "Animation" block of the element panel — it is the same configuration.

| Field | Default |
|---|---|
| Type | dropdown, 57 presets |
| Delay, ms | 0 |
| Hide before start | off |
| Duration, ms | 500 |
| Repeat count | 1; **0 = endless repeat** |

There is one configuration per element, no separate "in" and "out" — the character is set by the type. With repeat count 1 a preset is an **entrance effect** that plays once when the slide appears; with repeat count **0 it loops for the whole slide** — the way to get a pulsing price badge or a flashing accent without any code. Loops are limited to the preset shapes; for custom continuous motion (a shine across text, drift, a towed banner) use an HTML block — see prtv-html-block-animation.

### The 57 presets, as labelled in the editor

Labels are in Russian; each label is followed by the direction options where applicable.

- **Без эффекта** — no effect.
- **Появление** слева / справа / сверху / снизу — fade in from left / right / top / bottom.
- **Затухание** влево / вправо / вверх / вниз — fade out to the left / right / up / down.
- **Выезд** слева / справа / сверху / снизу — slide in from a side.
- **Сдвиг** влево / вправо / вверх / вниз — slide out toward a side.
- **Разворот** — flip, two groups: from a side (слева / справа / сверху / снизу) and toward a side (влево / вправо / вверх / вниз).
- **Качели** — swing, the same two groups of four.
- **Вылет** слева / справа / сверху / снизу — fly in.
- **Улет** влево / вправо / вверх / вниз — fly out.
- **Пояление-2** слева / справа — a second fade-in variant from the left or right (the label is spelled this way in the editor).
- **Исчезновение** влево / вправо — disappear to the left or right.
- **Выпадание**, **Падение** — drop in, fall.
- **Увеличение**, **Уменьшение** — grow, shrink.
- **Приближение**, **Отдаление** — zoom in, zoom out.
- **Вспышка** — flash.
- **Тряска** горизонтальная / вертикальная, **Встряска** — horizontal / vertical shake, jolt.
- **Пульс** — pulse.
- **Сплющивание** — squash.
- **Подсветка** — highlight.

### Checking an animation

A screenshot does not show motion. Open the preview player (eye button in the top panel) and wait at least one full slide duration; the public TV page is a secondary check. For frame-by-frame inspection of a CSS animation, pause it and scrub `currentTime` through `getAnimations()` — the snippet is in prtv-html-block-animation.

### Motion rules

- Entrance ≤ 2–4 s, then a still pause for reading ≥ 5 s.
- Not more than **one** moving element in the frame at a time. Several things moving at once compete for attention and end up ignored.
- Animation is a function — it draws the eye to a new item or an offer. If removing it changes nothing, it is not needed.

## 6. Clickable elements — links for touch kiosks

Right-click → **Сделать кликабельным** opens a small dialog: the PRTV title, the caption «Введите ссылку для открытия по клику» ("Enter the link to open on click"), **one text field**, Cancel / OK. Any element type can carry a link (checked on images and text). There is no selector of action types — what happens is defined by what you type.

Confirmed:

- **An external URL** (`https://…`) — opens on tap in the player / on a kiosk screen. The basic case: the venue's website, a menu page, a form, a promo landing.
- **The public address of another PRTV slideshow** — the tap switches the screen to that slideshow. This is how to build a "showcase menu": a landing screen → tap → another slideshow.

Not confirmed: jumping to a specific slide *inside the same slideshow*. The dialog has no such option, and whether a slide number typed in the field is understood by the player was not tested. Until it is, build the "pages" of a kiosk as **separate slideshows** linked to each other by their public addresses — that path works.

To remove a link: right-click → **Удалить ссылку**.

## 7. Layout rules for a 1920×1080 TV screen

These come from real menu-board builds and from broadcast practice. They are written as checks, not wishes.

**Safe zone — a hard gate, not taste.** Many TVs overscan by default and physically crop the edge of the frame. Keep every meaningful element — text, price, logo, QR code — at least **96 px** from the left and right edges and **60 px** from the top and bottom (the broadcast title-safe area is 90 % of the frame; this is slightly stricter). Decorative elements may run to the edge.

**Grid.** Inside the safe zone use a logical 12-column grid and align elements to it, not to arbitrary pixel values. Equal gaps between cards and equal row heights within a section — uneven spacing is the first sign of an unfinished slide.

**Type sizes** (in the 1920 space, for a viewer about 3 m away): headings ≥ 110–120 px, body text ≥ 44 px, captions ≥ 40 px. Counter or till (1.5–2 m): body may drop to 36–40 px, not lower. Hall or food court (4–5 m): the top of the range or larger — roughly 70 px and up at 5 m.

**Text boxes need a margin.** There is no reliable formula "font size × number of characters = width" for the editor's native text: typographic estimates come out too narrow, and the text wraps or is clipped. Make the box 30–40 % wider than the naive estimate; a slightly smaller font is better than a wrapped or clipped line. A one-line heading inside an HTML block can additionally get `white-space: nowrap`.

**Hierarchy** rests on at least two parameters at once (size + weight, size + colour, size + position), never on size alone. The three-second test: hide the slide after three seconds — the main message (item + price, or the offer) should be remembered without the rest.

**Colour.** One palette for the whole slideshow, roughly 60 % dominant / 30 % secondary / 10 % accent. The accent is the brightest colour and appears only at the decision point — price, call to action, "new" badge. Spread over five elements it stops being an accent. Contrast of text against its background: about 4.5:1 for body text, 3:1 for large headings.

**Text over a photo needs a scrim.** Either a dark semi-transparent panel behind the text or a darkening of the whole frame by 20–30 %; without it no font colour reaches a readable contrast. In PRTV this is done with the RGBA background of a Text element (a dark colour at about 70 % opacity worked in a live build) or with a translucent element stretched over the frame (§2). Text over photos should also be bolder than text on a flat background — light weights sink into the texture.

**Cards.** Rounded corners plus a soft shadow or a thin border — otherwise it is a filled rectangle, not a card. One card visibly highlighted (the top item or the offer), the rest uniform but not monotonous. At most one or two highlighted items per slide: highlighting works only against a calm background. Every content block gets a photo or an icon; a text block without a visual anchor is a slide not yet finished. The heading plate is attached to the content grid (zero or minimal gap, shared frame), not floating above it.

**Air.** An empty area is either a composition device or a mistake; there is no third option.

**One visual anchor per slide** — a hero photo or the top item — rather than attention spread evenly over the grid.

**Verify visually.** A layout is not done when the edit went through; it is done when the preview shows it. Text wrapping, clipping and a missing background are all found by looking, not by the absence of errors. Custom fonts must be checked in the preview or on the TV, not only in the editor — the two render differently.

### Quick checklist before handing a slide over

- [ ] No placeholder or TODO text left on the slide.
- [ ] Every meaningful element is inside the safe zone (96 / 60 px).
- [ ] Type sizes match the viewing distance of the installation point.
- [ ] Hierarchy on two parameters; the three-second test passes.
- [ ] One palette, about 60/30/10; accent only at decision points.
- [ ] No text wraps or is clipped — checked in the preview.
- [ ] Text over photos has a scrim.
- [ ] Cards: equal rhythm, rounded + shadow, one highlighted.
- [ ] At most one moving element at a time; entrance ≤ 4 s, pause ≥ 5 s.
- [ ] Same palette and card style on every slide of the cycle.

## What not to do

- Do not look for coordinate fields — there are none — and do not take coordinates from a screenshot.
- Do not drag a selected text element expecting it to move; it opens the text editor.
- Do not search the right-click menu for duplicate, delete or depth — they are in the element panel.
- Do not build custom continuous motion out of presets — repeat 0 loops a preset as it is; anything custom lives in an HTML block.
- Do not run several animated elements at once.
- Do not leave text, prices or logos closer than 96 / 60 px to the edges.
- Do not promise in-slideshow navigation on a kiosk; link separate slideshows instead.
- Do not leave the statistics / advertising / perspective / scaling toggles on by accident.
- Do not treat an edit made through the DOM as saved — reload and read back.

## Related

prtv-editor-overview · prtv-slide-settings · prtv-text-element · prtv-html-block-animation · prtv-video · prtv-widgets · prtv-agent-rules
