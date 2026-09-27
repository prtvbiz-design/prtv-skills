---
name: prtv-editor-overview
description: Map of the PRTV (prtv.pro) cloud digital-signage editor, where menu boards, promo screens and TV slideshows are built — how a slideshow, its slides and elements are organised, the 1920×1080 coordinate space and custom canvases, URLs, panels, slide strip, element panel, fonts, uploads, licences (TV slots) and the watermark, and how to read the editor state from the DOM. Use first for any task in the prtv.pro editor — building or editing a menu board, slideshow or info screen there, by hand or with an AI browser agent; other prtv-* skills assume it. Triggers (RU) конструктор PRTV, редактор prtv.pro, слайд-шоу для ТВ, меню-борд в PRTV.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-27"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# PRTV editor — overview for AI agents

PRTV is a cloud editor for digital signage: menu boards, promo screens, info channels shown on Smart TVs, set-top boxes and browsers. An agent works in it the way a person does — through the interface — and may read the page state with JavaScript. Everything below was verified in the browser, not taken from documentation.

## 1. Objects

**Slideshow → Slide → Element.**

- **Slideshow** — the unit the TV plays. Has a name, size (default HORIZONTAL 1920×1080), default styles for new slides and elements, a set of active fonts, and licences (TV slots).
- **Slide** — one screen in the rotation. Own settings: display duration in seconds, transition type (e.g. NONE, FADE), progress bar (colour, background, hide), background colour / image / video, image display type (STRETCH), default styles for elements on that slide (font family, size, text colour, background).
- **Element** — an object on a slide. Has a type, position and size (`top`, `left`, `width`, `height` in slide pixels), depth (z-index), an entrance animation, flags "permanent" (repeated on every slide of the slideshow), and type-specific content.

Element types by left-panel section:

| Section | Elements |
|---|---|
| Basic | Text, Ticker (marquee), HTML, Image, Video, Table |
| Widgets ("informers") | Clock, Weather, Air quality, Currency rates, Transport timetable, Traffic, Restaurant menu (POS integration) |
| Social | VKontakte, Odnoklassniki, Telegram, RSS news |

Each left-panel button adds one element to the **currently active** slide.

## 2. Addresses

| What | URL |
|---|---|
| Account, slideshow list | `https://prtv.pro/` |
| Editor | `https://prtv.pro/slideshow/<editor-id>` — a short hash, different from the TV number |
| Public player (what the TV shows) | `https://prtv.pro/<TV-number>` — seven digits, e.g. `https://prtv.pro/0012233`; the same number is typed on the TV |
| Account settings and integrations | `https://prtv.pro/settings` |
| Widget builders (public) | `https://s.prtv.su/informery`, e.g. `/chasy` (clocks), `/openweather`, `/qr-infomer`, `/countdown` |
| Uploaded media | `https://prtv.pro/download/folder-prtvpro/<hash>` — every upload is proxied through the PRTV domain, so there are no CORS issues in the player |

The editor id and the TV number are different identifiers. Don't mix them.

## 3. Coordinate space

The internal canvas is fixed at **1920 × 1080 px**. All element coordinates and font sizes live in this space and scale proportionally to any physical screen. Use absolute pixels, never percentages.

In the editor the canvas is shown scaled down (roughly ×0.57 on a desktop). Screen position = internal position × scale + canvas offset. The scale can be read from any element:

```js
const el = document.querySelector('[id^="slide-element-"]');
const r = el.getBoundingClientRect(), st = getComputedStyle(el);
const scale = r.width / parseFloat(st.width);
const ox = r.x - parseFloat(st.left) * scale;
const oy = r.y - parseFloat(st.top) * scale;
// screen = ox + scale * slideX
```

Recompute after any window resize. Never take click coordinates by eye from a screenshot — the screenshot is drawn in a third scale, and the miss looks like "the editor does not react".

Layers: the slide background is drawn at depth 0 and hides nothing. Content sits above it at depth ≥ 1; higher depth = closer to the viewer. See prtv-element-layout.

## 4. DOM conventions (for reading state)

- Slide element node: `id="slide-element-<id>"`.
- Slide node: `id="slide-<id>"`.
- Canvas: `#slide-factory`.
- Selected element frame: `.moveable-control-box`.
- Left panel: `.lefmenu` (about 1500 px tall — scroll it to reach lower fields: `document.querySelector('.lefmenu').scrollTop = 1e6`).
- Slide strip at the bottom: `.bottom-layer`, 160 px high. Thumbnails are full scaled-down copies of the slides with the same element ids — you can inventory every slide from the strip without switching slides. Exception: widgets are not rendered in thumbnails ("iframe blocked" placeholder).
- Text editor when a text element is being edited: `[contenteditable="true"]` (TinyMCE).
- Public player page: body class `active-slide-<id>` names the slide currently on screen; `IMG[alt="watermark"]` is present only when no TV slot is attached.

The client keeps a local copy of the data; reading it is a reliable way to inventory a slide (ids, types, positions, depth) without screenshots:

```js
const map = Meteor.connection._stores['slide-elements']._getCollection()._docs._map;
const list = Object.values(map).map(e => ({ id: e._id, slide: e.slideId, type: e.type, z: e.zIndex, ...e.styles }));
```

Read only. Do not try to write through it — the editor will not persist such changes, and public methods for writing are not part of this skill set.

Output that contains URLs with query strings may be blocked by agent tooling; strip URLs before returning text.

## 5. Top panel of the editor (7 buttons, no tooltips)

| # | Icon | Opens |
|---|---|---|
| 0 | settings | Slideshow settings: name, cover, canvas size, additional fonts, offline |
| 1 | paintbrush | Slideshow defaults: styles of a new slide and new elements; "Apply to all" pushes them to every slide. Right-click on the canvas opens the same |
| 2 | table-cells | Canvas: grid, snap, guides |
| 3 | eye | Preview player — the reference for checking rotation |
| 4 | image | List of the slide's elements ordered by depth (the icon is misleading) |
| — | undo | Ctrl+Z, within the page session only |
| — | redo | Ctrl+Shift+Z |

There is no version history. After a reload, undo is gone.

## 6. Slide strip and slide settings

Each thumbnail shows four buttons **only on a real mouse hover** (a synthetic `mouseenter` does not reveal them): slide settings, save as template (not a regular save), duplicate, delete.

Slide settings open in the left panel: duration, transition, progress bar, background (colour / image file or URL / video), element defaults.

Switching the active slide: click the thumbnail. A click sometimes registers on the second attempt — verify through the DOM, not by eye. Avoid clicking near the strip "just in case": the delete button lives there. Do not drag on a thumbnail unless you mean to reorder: an unfinished drag leaves the thumbnail displaced.

Right-click on the canvas = slideshow defaults, **not** the active slide.

## 7. Element panel ("Element styling")

Common to all types: rotation (0–360° + step), opacity, border (width + colour), padding, background colour (RGBA picker; alpha 0 = transparent, stored as `#ffffff00`), background image (cover / contain / stretch), display mode (STRETCH / TILE / FILL), animation (type from 57 presets + delay + duration + repeat count, 0 = endless + "hide before start"), keep aspect ratio (images), permanent element (on all slides), **depth** (z-index), actions (click behaviour).

There are no numeric X/Y/W/H fields. Position and size are set by dragging and resizing the frame. Drag an **unselected** element to move it; dragging a selected text element enters text editing. Resize by the frame handles; the middle-right handle is the safest.

"Choose" buttons for background images are hidden until hover and open a system file picker. There is no built-in image gallery: file picker or an image already on the slide.

Right-click on an element — context menu: make clickable, style settings, animation settings, collect statistics, mark as advertising, perspective mode, scaling mode.

## 8. Fonts

26 built-in Google fonts with Cyrillic: Arial (default), Bad Script, Comfortaa, El Messiri, Fira Code, Forum, Jura, Kelly Slab, Kurale, Lobster, Marck Script, Neucha, Open Sans, Oswald, Pacifico, Pangolin, Play, Poiret One, Press Start 2P, Roboto, Rubik Mono One, Ruslan Display, Russo One, Seymour One, Stalinist One, Underdog.

Custom fonts: slideshow settings → "Additional fonts" → "Add font" (TTF/WOFF). Only weights 400/700 are used; variable fonts are truncated. Fonts are applied to text through the TinyMCE toolbar — see prtv-text-element.

## 9. Uploads

Images and videos upload through the file picker of the corresponding field. Files are stored under the PRTV domain and served without CORS issues. Large images are downsized by roughly a quarter (1920×1080 → about 1456×819); keep a margin on logos and QR codes. Upload has no visible progress bar; the URL appears in the DOM after a few seconds.

## 10. Background of a slide — three ways

1. **Slideshow defaults** (paintbrush): colour, image or video for all new slides; "Apply to all".
2. **Slide settings** (thumbnail → settings): colour, image (file or URL) or video for this slide only.
3. **An Image element** stretched to 1920×1080 at depth 0 — when you want layers or effects on top of the background.

There is no native gradient; upload a pre-rendered gradient image instead.

## 11. TV slots, watermark, public address

Every slideshow is available by its TV number immediately, **with a watermark**. Attaching a TV slot (licence) removes it. A new account has one free TV slot. Slots are attached and detached with the −/+ counter on the slideshow card in the account; a slot can be moved between slideshows. The "+" does nothing silently when no free slots remain.

## 12. Checking the result

Screenshots do not show rotation or animation. Use the preview player (eye button) and wait at least one full slide duration. The public page in a desktop browser may "park" on the first slide for a long time while the data is correct — the preview is the reference, the public URL is a secondary check.

Saving is automatic. There is no save button; "Saved" appears after an edit. To verify, reload the page: whatever survives a reload is saved.

## 13. What agents get wrong most often

- Taking click coordinates from a screenshot.
- Editing the DOM directly and assuming it is saved.
- Using the editor id where the TV number is needed, or vice versa.
- Clicking blindly in series of double clicks — an extra click drags the element off the slide.
- Judging widgets by thumbnails (they are blank there) or weather by the editor preview (fixed-pixel layout clips icons; the public page is fluid).
- Expecting a free-standing "free licence": the free tier is one TV slot; without it the slideshow plays with a watermark.

## 14. Tricks from the PRTV instructions

- Hotkeys: arrows move the selected element, Shift+arrow faster; Del deletes; Esc deselects; Ctrl+Z, Ctrl+C / Ctrl+V also work in the Russian layout; Shift+click selects several elements.
- Pan the canvas with the middle mouse button held, zoom with Ctrl + wheel. Elements and the background can extend past the canvas edge — used for "slide in from off-screen" animation.
- The **element list** button selects the right element on a layered slide when a click lands on the background or a neighbouring image.
- A slide can be saved as a **layout** (floppy icon on the thumbnail) and inserted into other slideshows with "Slide from layout" — handy for chains with a brand style.
- A **permanent element** (logo, clock, radio, map) shows on every slide — do not copy it to each slide.
- If the editor lags, switch off slide previews and "sticky edges".
- Changes save instantly and undo works only until you leave the editor: duplicate a designer-made slideshow first and edit the copy.
- Several people can edit one slideshow under one account; there are no roles.
- **Mobile version**: new slideshow and element via the "three dots" at the top, drag with a long press, properties under "Element settings" at the bottom; convenient for changing prices from a phone.
- Snowfall effect — GIF https://s.prtv.su/wp-content/uploads/snezhinki.gif added via "Photo" above the other layers; image collection — "Photo → Choose → From collection".
- Free backgrounds: https://s.prtv.su/wp-content/uploads/shablony/city/city_N.jpg (1–32), …/textures/textureN.jpg (1–29), …/flowers/flowersN.jpg (1–18).

## Related

prtv-slide-settings · prtv-element-layout · prtv-text-element · prtv-html-block-animation · prtv-video · prtv-widgets · prtv-agent-rules