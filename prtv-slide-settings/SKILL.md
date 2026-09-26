---
name: prtv-slide-settings
description: Slide-level controls in the PRTV (prtv.pro) digital-signage editor — the slide strip and its hover buttons (settings, save as template, duplicate, delete), reordering, display duration, 15 transition effects, progress bar, slide background (colour / image / video), default styles for new elements, slideshow-wide defaults with Apply to all, templates, and reading the active slide from the DOM. Use when adding, duplicating, reordering or configuring slides of a menu board or TV slideshow in prtv.pro — timing, transitions, backgrounds, templates. Triggers (RU) слайды в PRTV, длительность слайда, переход между слайдами, фон слайда, шаблон слайда.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-26"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# Slide settings in the PRTV editor

A PRTV slideshow is a rotation of slides; each slide is one full screen with its own timing, transition, background and defaults for the elements placed on it. This skill covers the middle level of the hierarchy — slideshow → **slide** → element. Elements are in prtv-element-layout, the overall map of the editor in prtv-editor-overview. Everything below was verified in the browser.

## 1. The slide strip

Slides live in a horizontal strip at the bottom of the editor (`.bottom-layer`, 160 px high). Each thumbnail is a full scaled-down copy of its slide with the **same element ids** as the canvas, so the whole slideshow can be inventoried from the strip without switching slides. The one exception: widgets ("informers") are not rendered in thumbnails — an "iframe blocked" placeholder stands in for them.

**Switching the active slide** — click its thumbnail. The click sometimes registers on the second attempt; confirm through the DOM (which slide node is shown on the canvas), not by eye. Every left-panel button adds an element to the *currently active* slide, so always confirm the active slide before adding anything.

**Reordering** — drag a thumbnail along the strip; the order updates immediately. A keyboard drag is also available for accessibility. Do not start a drag on a thumbnail unless you intend to reorder: an unfinished drag leaves the thumbnail displaced.

**Adding a slide** — the "add slide" button at the strip, or **"Слайд из макета"** ("Slide from template") to insert a slide saved earlier as a template (§3).

## 2. The four hover buttons of a thumbnail

Hovering a thumbnail with a real mouse shows a row of four icons above it, left to right:

| # | Button | What it does |
|---|---|---|
| 1 | Settings (gear) | Opens the slide settings panel on the left (§4). |
| 2 | Save as template | Opens a dialog «Укажите название шаблона» ("Enter a template name"). This is **not** a regular save — saving is automatic; this creates a reusable layout. |
| 3 | Duplicate | Duplicates the slide immediately, next to the original. |
| 4 | Delete (red trash) | Deletes the slide immediately, without a confirmation dialog. |

Two traps for agents:

- The icons appear only on a **real pointer hover**. A synthetic `mouseenter` event does not reveal them; move the pointer physically over the thumbnail before clicking.
- The delete button lives exactly where a careless "click somewhere near the strip" lands. Do not click around the strip "just in case".

**Right-click on a thumbnail opens no custom menu** — only the browser's native one. All slide actions are the four hover buttons. (Elements are different: right-click on an element opens a seven-item menu — see prtv-element-layout.)

## 3. Templates

"Save as template" stores the current slide's layout under a name. Saved templates are listed under **"Слайд из макета"** and inserted as a new slide with all elements. Use templates to keep a house layout (header plate, card grid, logo, clock) and to produce slides of the same family quickly.

## 4. Slide settings panel

Opens from the gear on the thumbnail. Three sections.

### «Основные» — Main

| Field | Default |
|---|---|
| Hide the progress bar (No / Yes) | No |
| Display duration, seconds | 30 |
| Progress bar colour | `#3f51b5` |
| Progress bar background | `#b6bce2` |
| Transition effect (list) | «Без эффекта» — none |
| Transition duration (stepper) | appears once a value is set |

The **display duration** is the number every animation on the slide is timed against: entrance effects must finish and leave a reading pause inside it, and looping HTML-block animations should have a period that fits it, so the loop does not stop mid-cycle when the slide changes (see prtv-html-block-animation).

The progress bar is the thin line the viewer sees running across the screen during the slide; hide it on menu boards and promo screens where it is visual noise.

### «Стили по умолчанию» — Default styles (the slide's own background)

| Field | Default |
|---|---|
| Background colour | `#ffffff` |
| Background video | URL (`https://…`) plus «Без звука» (Mute) No / Yes |
| Background image | file upload through the picker |
| Background display (list) | «Растянуть» — Stretch |

### «Стили элементов по умолчанию» — Default element styles (for new elements on this slide)

Background colour `#ffffff`, background image (file), background display «Растянуть», opacity (stepper), font ARIAL, font size 24, text colour `#000000`.

These defaults are applied to elements **added after** they are set; existing elements do not change. Setting the brand font, size and colour here once, before adding elements, saves editing every text element afterwards. The editor's default font is Arial — a brand slide needs its font set explicitly.

**Not in the panel:** a slide name, a display schedule or conditions, orientation. Slides are identified by position only; scheduling is not a per-slide setting.

## 5. Transition effects — 15 values

In the order of the list, as labelled in the editor:

Без эффекта (none) · Затухание (fade) · Сдвиг влево (slide left) · Сдвиг вверх (slide up) · Сдвиг вправо (slide right) · Сдвиг вниз (slide down) · Приближение (zoom in) · Отдаление (zoom out) · Выгнутный влево (convex left) · Выгнутный вправо (convex right) · Вогнутый влево (concave left) · Вогнутый вправо (concave right) · Конвейер (conveyor) · Колесо (wheel) · Появление (appear).

For signage that people read (menus, price lists) «Без эффекта» or «Затухание» is the safe choice; the 3D transitions draw attention to the change rather than to the content and look different on TV hardware than on a desktop.

## 6. Background of a slide — three ways

1. **Slideshow defaults** (paintbrush button in the top panel): colour, image or video for *all new* slides; «Применить ко всем» ("Apply to all") pushes them to every existing slide. Right-click on an empty part of the canvas opens the same panel.
2. **Slide settings** (gear on the thumbnail → «Стили по умолчанию»): colour, image (file) or video (URL, optional mute) for this slide only.
3. **An Image element** stretched to 1920×1080 at depth 0 — when layers or effects must sit on top of the background (see prtv-element-layout). This is the only way to put a stretched image *under* other elements with full control.

A background set in slide settings is drawn at depth 0 and hides nothing. There is no native gradient; upload a pre-rendered gradient image instead.

Image uploads go through the file picker only; there is no gallery of previously uploaded files and no visible progress bar — the image URL appears in the DOM a few seconds after the upload. Large images are downsized by roughly a quarter on upload.

Background video: paste an `https://` URL into the field and choose «Без звука» — Yes for silent playback. Requirements for a seamless loop are in prtv-video.

## 7. Slideshow-wide defaults vs slide settings

Two panels look similar and are easy to confuse:

| | Slideshow defaults (paintbrush, or right-click on the canvas) | Slide settings (gear on the thumbnail) |
|---|---|---|
| Applies to | new slides and new elements across the slideshow; «Применить ко всем» — to all existing slides | this slide only |
| Sections | styles of a new slide, styles of new elements | main, slide background, default element styles |

«Применить ко всем» overwrites the background and defaults of every slide. Use it only for a deliberate global change — a re-brand of a colour, a common background — never to "fix one slide".

## 8. Reading the slide state from the DOM

- Slide node on the canvas: `id="slide-<id>"`.
- Thumbnails in `.bottom-layer` carry the same element ids as the canvas — count elements per slide, find which slide an element belongs to, spot empty slides.
- Public player page: the body class `active-slide-<id>` names the slide currently on screen. Poll it to confirm the rotation order and duration without watching the screen.
- The slide's own settings (duration, transition, background) are shown in the panel; open the gear and read the fields.

A whole-slideshow inventory of elements with their slide ids is available through the read-only local store described in prtv-editor-overview.

## 9. Checking the result

The editor canvas shows a still slide. Rotation, transitions, durations and the progress bar are only visible in the **preview player** (eye button in the top panel) — wait at least one full slide duration per slide. The public TV page in a desktop browser may stay on the first slide for a long time while the data is correct; the preview is the reference, the public page a secondary check.

Saving is automatic. There is no save button; "Сохранено" appears after an edit. To be sure, reload the page: whatever survives a reload is saved. Undo (Ctrl+Z) works only within the page session; there is no version history, and a deleted slide cannot be recovered after a reload — duplicate before risky edits.

## What not to do

- Do not use "save as template" as a save button — saving is automatic; the button creates a template.
- Do not click near the slide strip without a target: the delete button appears there on hover and deletes without confirmation.
- Do not trust a synthetic hover — the four buttons show only on a real pointer move.
- Do not add elements before confirming which slide is active through the DOM.
- Do not press «Применить ко всем» to fix a single slide.
- Do not judge widgets by thumbnails — they are placeholders there.
- Do not look for a slide name, schedule or orientation in slide settings; they are not there.
- Do not set a transition on a text-heavy slide just because it is available.

## Related

prtv-editor-overview · prtv-element-layout · prtv-text-element · prtv-html-block-animation · prtv-video · prtv-widgets · prtv-agent-rules
