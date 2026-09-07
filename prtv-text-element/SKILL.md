---
name: prtv-text-element
description: Working with the native Text element of the PRTV (prtv.pro) digital-signage editor — entering and leaving text editing, the TinyMCE toolbar (fonts, size, colour, spacing), what kinds of edits are saved and what is silently lost, the triple-click trap on menu rows with right-aligned prices, replacing text with Ctrl+A, menu-row layout, known display quirks, and when to prefer a Text element over an HTML block. Use when an AI agent or a person needs to write, restyle or bulk-edit text on a slide in the prtv.pro editor, or when text edits keep disappearing after a reload.
license: CC-BY-4.0
metadata:
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "2026-09-06"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# The Text element in the PRTV editor

The native **Text** element is where menu items, prices, headings and descriptions should live: it is the one element the client can later edit without touching code. Under the hood it is a rich-text editor (TinyMCE) whose content is HTML — paragraphs and spans with inline styles plus a small built-in stylesheet with the element's defaults. This skill is about editing that content so that the edit actually survives a reload. Placement, size, depth and animation of the element are in prtv-element-layout; the editor map is in prtv-editor-overview.

## 1. Creating and selecting

- Left panel → **Текст** adds a text element to the active slide at the top-left corner, 500×120 px, with the slide's default element styles (Arial 24 px black unless changed in slide settings — see prtv-slide-settings).
- **One click** on a text element selects it as a box (the selection frame appears; the element panel opens).
- **Double click** enters text editing: a `[contenteditable="true"]` node appears and the formatting toolbar shows above the canvas.

Entering edit mode is the least reliable step of the whole workflow for an agent: a click followed by a double click usually needs 2–5 attempts. After each attempt check `document.querySelector('[contenteditable="true"]')` and stop as soon as it exists. Never fire a series of double clicks blindly — an extra click on a selected element becomes a drag that carries it off the slide.

## 2. Editing, replacing, leaving

- **Replace all text**: inside edit mode press Ctrl+A, then type. Typed text always persists.
- **Leave edit mode**: click an empty part of the canvas *to the left of the slide*. Escape is unreliable. Do not click near the slide strip at the bottom — its hover buttons include "delete slide".
- Saving is automatic; "Сохранено" appears after the change. The definitive test is a page reload: whatever survived the reload is saved.
- Enter inside the text creates a new paragraph. When you only need to confirm a value in a toolbar field (font size), press Enter in that field, not in the text body.

Dragging a *selected* text element does not move it — it opens editing. To move it, deselect first (Escape or click outside), then drag the unselected element.

## 3. The toolbar

Left to right:

`undo redo | bold italic underline strikethrough · font family · font size · h1 · table | text colour · background colour · align · bullet list · numbered list · outdent · indent · line height · letter spacing · remove formatting`

Details that matter:

- **Font family** — a dropdown with the 26 built-in fonts (list in prtv-editor-overview) plus any font added in slideshow settings → «Дополнительные шрифты». **Fonts are applied only through this dropdown.** It writes the font with `!important`, which is what overrides the element's built-in stylesheet; a font set any other way is ignored.
- **Font size** — an input field. Click it, Ctrl+A, type the value with units (`56px`), Enter. Values are in the 1920×1080 slide space.
- **Bold** — only weights 400 and 700 exist. Variable fonts are reduced to those two.
- **Text colour** — a split button. Click the chevron → a palette of 25 swatches → «Custom color» → hex field → Save. Wait until the hex field actually has focus before typing; typing early sends the characters into the text body and destroys the selection.
- **Line height** and **letter spacing** — dedicated buttons.
- **Remove formatting** — strips inline styles from the selection; useful before re-styling text pasted from elsewhere.

Not available in the toolbar: text-transform (type capitals as capitals), tabular figures and other specialised CSS. If a design needs them, that piece goes into an HTML block — see prtv-html-block-animation.

## 4. What is saved and what is silently lost

The element's content is kept in the editor's own state; the visible text is only a view of it. The editor rebuilds the view from its state on blur and on reload, so **anything written straight into the DOM by a script looks applied and then disappears**. In one live session this cost two full passes over a menu's fonts before it was noticed.

| Edit | Persists? |
|---|---|
| Real typing, Ctrl+A + typing, paste | yes |
| Toolbar commands (font, size, bold, colour, align, line height, letter spacing) | yes |
| A style written into the DOM by a script, with no real input after it | no — reverts on blur |
| Editor content replaced by a script without a keystroke after it | may revert on blur |
| `gap` on a row, `transform: scale()` on a span | filtered out even with a keystroke |

**The keystroke trick.** A DOM change made *before* a real keystroke is included in what the editor serialises, because the editor reads the live content when the keystroke fires its change handler. So: apply the style to the DOM by script, then press End, Space, Backspace in the editor (real keyboard events). This is how structural styles — `flex: 1` on a name span, a margin, a `display` value — can be committed. What the editor's filter drops (`gap`, `transform`) cannot be committed this way; use `flex: 1` instead of `gap` and `font-size` instead of `transform: scale()`.

**Verify.** Click outside, reload the page, then check the element's HTML for the expected fragment (read-only):

```js
document.getElementById('slide-element-<id>').innerHTML.includes('flex: 1')
```

If the fragment is gone after the reload, the edit was not persistent — repeat it with a real keystroke after the change.

## 5. The triple-click trap on menu rows

Menu rows are usually one paragraph with two spans — the item name and the price — laid out with `display: flex; justify-content: space-between` so the price sits at the right edge.

If you select the whole paragraph (triple click) and apply a font from the toolbar, the editor **wraps the whole content in one new span**. The row now has a single flex child, and the price snaps to the name. The fix is to apply the font **span by span**: select the name, apply; select the price, apply.

For many rows, select each span by script (a selection is not a DOM edit and does not interfere with saving) and apply the font by clicking the toolbar:

```js
window.__selNext = function () {
  const ed = document.querySelector('[contenteditable="true"]'); if (!ed) return 'noed';
  const sp = [...ed.querySelectorAll('span')].filter(s =>
    s.children.length === 0 && s.textContent.trim() &&
    parseFloat(getComputedStyle(s).fontSize) >= 29 &&
    !/TargetFont/.test(getComputedStyle(s).fontFamily));
  if (!sp.length) return 'done';
  ed.focus();
  const r = document.createRange(); r.selectNodeContents(sp[0]);
  const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
  return sp[0].textContent.trim();
};
```

Loop: `__selNext()` → click the font dropdown (`.tox-tbtn--select`) → click the wanted item (`.tox-collection__item`) → repeat until `'done'`. The filter skips spans that already carry the target font, so the loop is safe to rerun. Take the toolbar coordinates from the DOM; they are stable within one element and shift between elements.

## 6. Menu rows and pasted markup

- Layout of a row: one paragraph, `display: flex; justify-content: space-between`, name span with `flex: 1`, price span after it. With `flex: 1` on the name the price is pushed to the right edge whatever the text length; without it, spacing depends on typed spaces.
- In a **freshly created** text element, a whole block of marked-up rows can be inserted at once (paste, or the browser's insert-HTML command after selecting the element's contents) and it is saved. In an **existing** element the same insertion is not reliable — edit row by row and commit with a keystroke.
- Spaces, non-breaking spaces and any typed characters persist; the editor does not filter content, only some styles.
- Text over photos, box widths, type sizes and safe zones: prtv-element-layout §7. There is no reliable "font size × characters = width" formula for the native text — give the box a 30–40 % margin over the naive estimate.

## 7. Known quirks of the display

- The rouble sign ₽ is shown as «Р» in the editor canvas; on the TV it renders correctly. Judge currency signs in the preview or on the screen, not on the canvas.
- Editing by a person can split a paragraph in two; the new fragment may lose the inline styles of the original. Re-apply the font and colour from the toolbar to the new fragment.
- A custom font added in slideshow settings must be checked in the preview or on the TV — the editor canvas and the player are different rendering contexts.
- The element's built-in stylesheet sets the defaults for the whole element; a style from the toolbar wins over it. Styles that come from an HTML block's `<style>` are global to the page and can also target native text (see §8).

## 8. Animating native text without converting it

The panel presets loop with repeat count 0 (a pulse, a flash — see prtv-element-layout), but they cannot do a shine or a colour sweep. To give a heading a continuous custom effect **and keep it editable**, leave it as a Text element and add a small HTML block whose `<style>` targets the text's span by one of its inline properties, for example the font size:

```css
.text-widget span[style*="font-size: 52px"] { … animation: promoShine 5s linear infinite; }
```

The recipe with the full gradient-shine keyframes is in prtv-html-block-animation. Editing the words does not break the effect.

## 9. Ticker (marquee) — the other native text

The **Бегущая строка** element has its own panel: text, speed, scroll direction, font size, font, text colour, background colour, animation, depth. Speed × 10 = pixels per second (20 → 200 px/s); the loop duration follows the text length, so the ticker cannot be synchronised with a separately animated picture. Details and the "banner behind a plane" workaround are in prtv-html-block-animation.

## 10. Text element or HTML block?

Rule of thumb from real menu boards: **all readable content — names, prices, descriptions, headings — goes into native Text elements**, so the venue can edit it later. HTML blocks are for what Text cannot do: gradient plates (there is no native gradient), widgets embedded by URL, continuous animation, tables with dotted leaders, uppercase or tabular-figure typography.

## What not to do

- Do not set a font any way other than the toolbar dropdown.
- Do not apply a font to a whole flex row at once — span by span.
- Do not treat a script edit of the DOM as saved; commit it with a real keystroke and confirm by reload.
- Do not type a hex colour before the custom-colour field has focus.
- Do not press Enter in the text body to "confirm" a toolbar value.
- Do not judge the rouble sign on the canvas.
- Do not fire blind series of double clicks to enter editing — check for `[contenteditable="true"]` after each attempt.
- Do not put editable menu content into an HTML block.

## Related

prtv-editor-overview · prtv-element-layout · prtv-slide-settings · prtv-html-block-animation · prtv-agent-rules
