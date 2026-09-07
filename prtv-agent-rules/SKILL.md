---
name: prtv-agent-rules
description: Discipline for an AI browser agent working in the PRTV (prtv.pro) digital-signage editor — zero screenshots (the 2000-px image limit and why runs die), reading the DOM instead, computing click coordinates instead of eyeballing them, what does and does not persist (edits through the interface only), verifying by reload and by preview, sanitising output that contains URLs, isolated-world and cross-tab traps of JavaScript tools, hover-only controls, slide activation, element-creation timing, duplicated permanent elements, hand-built widget URLs, and how to pace a long session. Use at the start of any automated session in the prtv.pro editor, before the first click.
license: CC-BY-4.0
metadata:
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-09-06"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# Rules for a browser agent in the PRTV editor

These rules were paid for with broken sessions. They apply to any agent that drives the editor through a browser — Claude in Chrome, Playwright-based agents, similar tools. The editor's map is in prtv-editor-overview; the other prtv-* skills cover the objects. This one covers how to behave.

## 1. Zero screenshots

**Rule zero: no screenshots during a run.** Agent image APIs reject requests when the context holds many images and any of them exceeds **2000 px on a side**; a full-page screenshot of the tall editor is always larger. Runs with more than about five screenshots stall or die.

Replace screenshots with:

- **Read page** (interactive elements, or the whole DOM as text).
- **JavaScript inspection** — `document.querySelectorAll`, `getBoundingClientRect`, `getComputedStyle`, the element and slide ids, the read-only local store (prtv-editor-overview §4).
- **Console messages** — to read the result of a script.

If a picture is unavoidable: viewport only, never full-page; at most about ten per session, one at the end of a logical block (slide done, edit accepted), never after every click; a tall page as two or three viewport frames; keep the browser window at 1920×1080 or smaller so frames stay under the limit. Report in text — tables of edits, statuses, measurements — and keep any pictures for the final result.

A screenshot cannot show motion anyway. Animation and rotation are checked in the preview player or by scrubbing `getAnimations()` (prtv-html-block-animation).

## 2. Coordinates are computed, not seen

Three scales coexist: the internal 1920×1080 slide space, the CSS pixels of the page, and the pixels of a screenshot. A click coordinate read by eye from a screenshot lands in the wrong place, and the miss looks like "the editor does not react".

- Slide → page: take scale and offset from any absolute element on the canvas (prtv-editor-overview §3): `page = offset + scale × slide`. Linear — compute once, reuse, recompute after any window resize.
- Page → tool: if the click tool works in screenshot pixels, the factor is `screenshot_width / window.innerWidth`; measure it once instead of assuming it.
- Toolbar and panel buttons: take their coordinates from `getBoundingClientRect()` of the button, not from a picture. Within one element they are stable; between elements they shift.
- The left panel is about 1500 px tall — fields may be below the window; scroll it (`document.querySelector('.lefmenu').scrollTop = 1e6`) before looking for a field.

## 3. Read everything, write through the interface only

The editor keeps its state in its own client-side model and redraws the page from it. **A change written by a script straight into the DOM looks applied and vanishes on the next redraw or reload.** In one live session this cost two full passes over a menu's fonts.

What persists: real mouse and keyboard input, toolbar commands, and a value written into a panel field through the field's native setter followed by `input` and `change` events (the field must be a real interface field — see prtv-html-block-animation for the snippet). Dispatching `change` or `blur` on a form field does not save it — type the value, then press Tab or click elsewhere (a real blur).

The private methods the editor uses to talk to its server are not part of this skill set and are not to be called; attempts return "access denied" and would in any case bypass the safeguards of the interface. Everything is done as a person would do it.

**Verify by reload.** Whatever survives a page reload is saved; nothing else is. Undo lives only within the page session; there is no version history.

## 4. JavaScript-tool traps

- **Isolated world.** The tool's scripts run in an isolated context: page globals are reachable as `window.<name>`; a bare global may be `undefined` on a fully loaded page. Some helpers on the page's collections (`_docs._map`) may not be visible from there — use `.find().fetch()` on the collection instead.
- **Promises are not awaited.** An async script returns `{}`. Pattern: start the work and store the result on `window.__r`, then read `JSON.stringify(window.__r)` in a second, synchronous call.
- **`window.__*` is per tab.** A value built in one tab (a widget builder) does not exist in another (the editor). An iframe built from an undefined variable gets `src="undefined"`, the browser resolves it against prtv.pro and the canvas shows a "404 slideshow not found" plate. Build URLs and HTML in the same tab where the element is created, or paste them as literals; after setting HTML, check for `src="undefined"`.
- **Output sanitising.** The tool may refuse to return a string that contains URLs with query strings or data-URLs, reporting "cookie / query string data" — a false positive. Do not dump an element's HTML or text wholesale. Return metadata (length, presence of a substring, node counts), cut URLs at `?`, or wrap the result in `JSON.stringify`. Strip URLs from any text you return to the person.
- **Fetch to verify.** A widget URL built by hand is checked with `fetch(url).then(r => r.ok)` before it goes into a block.

## 5. Interface habits that break automation

- **Hover-only controls.** The four buttons on a slide thumbnail and the "Choose" buttons of image fields appear only on a **real pointer hover**; a dispatched `mouseenter` does nothing. Move the pointer physically, then click.
- **The slide strip is dangerous ground.** Do not click near it without a target — the delete-slide button lives there and deletes without confirmation. Do not start a drag on a thumbnail unless reordering; a drag left unfinished leaves the thumbnail displaced (recover with `document.querySelectorAll('[data-slide-id]').forEach(el => el.style.transform = '')`).
- **Deselect** by clicking the empty canvas area to the left of the slide. Escape is unreliable.
- **«Назад» in the element panel** leaves the editor for the slideshow list — it is not "one step back". From slide settings it returns to the element list.
- **Entering text editing** takes 2–5 attempts (click, double click); check for `[contenteditable="true"]` after each one and never fire blind series of double clicks — an extra click becomes a drag that carries the element off the slide. See prtv-text-element.
- **Duplicate elements are easy to create**: a left-panel button adds an element instantly, without a dialog. Count `[id^="slide-element-"]` before and after the click.
- **Right-click on the canvas** opens slideshow defaults, not the active slide's settings.

## 6. Slide activation and element timing

- **Activating a slide** = hover + click on its thumbnail. Changing the URL or the browser history does not switch the model the left-panel buttons write to; an element may land on the previously active slide. After switching, confirm through the DOM which slide node is on the canvas; when in doubt add a throw-away element and see which slide's thumbnail it appears in, then delete it.
- **The canvas may show elements of neighbouring slides** — a preview artefact, not data. Confirm an element's slide by the thumbnails (same ids) or the store.
- **A new element changes its id.** Right after the click the element exists under a temporary id; a few seconds later the server's id replaces it. Create all needed empty elements first, wait about 10–15 s, then find them again by their default geometry (a new text element is at 0,0 with size 500×120) before editing.
- **Duplicating a slide copies permanent elements too**, so a duplicated slide carries a second logo, clock or video marked "on all slides" — doubled on every slide. For a clean new slide use the strip's **add slide** button; permanent elements appear on it automatically. If doubles were created, delete the extra elements or the duplicated slide.
- The "general settings" block of the element panel has two related controls — «Постоянный элемент» (No/Yes) and a «На всех слайдах» toggle — plus «Позиция» (a select; «Под всеми» = bottom layer) and «Глубина» (number). Read them from the panel, not from assumptions.

## 7. Widgets from builders

The public builders on s.prtv.su often do not read values that a script has typed into their fields — the generated code comes out with defaults (except transparency). Build the widget URL **by hand** from the parameter reference in prtv-widgets-catalog, encode colours as `%23…` and text with `encodeURIComponent`, verify with `fetch`, wrap in the standard `<iframe>` and paste into the HTML block in the editor tab. Check the result on the public TV page, not in thumbnails.

## 8. Acceptance

1. **Preview player** (eye button) — the reference. Wait at least one full slide duration per slide.
2. **Public page** `https://prtv.pro/<TV-number>` (`?tv=true` shows it as the TV does) — a secondary check. During a transition `body.innerText` is briefly empty — poll several times. Heavy embeds (video players, widget iframes) may mount late — a viewer artefact; check live full-screen. The desktop viewer may park on the first slide for a long time while the data is right.
3. **Reload the editor** and read the element back.
4. **Watermark**: `img[alt="watermark"]` on the public page means no TV slot is attached to the slideshow.
5. A layout is accepted visually, not by the absence of errors: wrapping, clipping, missing backgrounds and unloaded fonts are found by looking (prtv-element-layout §7).

## 9. Pacing a session

- Split long jobs: after about 100–150 steps or when the tool slows down, finish the block, report in text, and continue in a new session with a short context.
- One logical block per report: what was changed, where, verified how.
- Never "push through" a stalled session — start a new one.
- Keep a list of ids you created, so that a new session can find them.

## What not to do

- Do not take screenshots to find where to click.
- Do not edit the DOM and call it saved.
- Do not call the editor's private methods.
- Do not dispatch synthetic hover, change or blur and expect the interface to react.
- Do not build a widget URL in one tab and use it in another.
- Do not duplicate a slide that carries permanent elements.
- Do not trust a new element's id for the first fifteen seconds.
- Do not click around the slide strip.
- Do not dump element HTML into tool output.
- Do not run a session past the point where the tool starts to lag.

## Related

prtv-editor-overview · prtv-slide-settings · prtv-element-layout · prtv-text-element · prtv-html-block-animation · prtv-video · prtv-widgets · prtv-widgets-catalog
