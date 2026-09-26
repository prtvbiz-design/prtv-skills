---
name: prtv-html-block-animation
description: Live motion on a PRTV (prtv.pro) digital-signage slide with the HTML block — CSS keyframes, SVG filters and SMIL, no JavaScript, safe for old Smart TV browsers; recipes for steam over a cup, shimmer, wind, TV noise, a banner towed by a plane, tickers, and animating native text. Use when a menu board or promo slide needs a looping animated detail, a CSS or SVG effect, or custom HTML inside prtv.pro. Triggers (RU) анимация на слайде, пар над кофе, CSS-анимация, HTML-блок, бегущая строка, живой меню-борд.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-26"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# HTML block and animation in the PRTV editor

The PRTV editor builds a slide from elements: text, image, video, shapes, widgets ("informers") and an **HTML block**. The HTML block is the only element that can run an **arbitrary** infinite animation. The animation presets in the element panel do loop when their repeat count is set to 0 (a pulsing badge, a flashing accent — see prtv-element-layout), but they are fixed shapes; anything custom — a shine across text, steam, wind, a towed banner — is an HTML block.

## What the HTML block can and cannot do

| | Rule |
|---|---|
| NO | `<script>` is stripped. No canvas, no random particles, no reaction to data. Everything is described in advance in CSS and SVG. |
| NO | The `class` attribute of `<img>` is overwritten by the editor's utility classes. Style images through a parent selector: `.wrap img { … }`. |
| YES | SVG filters and **SMIL** (`<animate>`) work — this is how live noise and flapping cloth are made. |
| YES | A `<style>` tag inside the block is **global for the document**. You can target native elements on the slide from it. |
| YES | Images from the PRTV media library can be used; take the URL from an `<img>` already placed on the slide. |

Content is clipped at the block borders. The default block background is white — set the element background alpha to 0 (see below).

**Heavy pixel filters only on a small area.** Turbulence and blur are computed per pixel: a 445×370 px area is fine on a TV set-top box, a full 1920×1080 frame is not. For full-screen effects use only `transform` and `opacity` — the GPU handles them.

## Creating a block

1. Toolbar button **HTML** → a 400×200 block appears at (0, 0).
2. Click the block, wait for the **"HTML code"** textarea in the element panel.
3. Put the code into the textarea. Keyboard typing works; for long code, write the value through the native setter so the editor's state picks it up:

```js
window.__setRV = function (el, val) {
  const proto = el.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
  Object.getOwnPropertyDescriptor(proto, 'value').set.call(el, val);
  el.dispatchEvent(new Event('input', { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
};
```

4. Element background → color picker → field **A** (alpha) = 0. The stored value becomes `#ffffff00`.
5. Resize by the frame handles (the middle-right handle is the safest — bottom handles may be off-screen).
6. Move by dragging an **unselected** block (press Escape first). Dragging a selected text element enters text editing instead.
7. Set **Depth** (z-index) — see "Layers".

Verify by reloading the page. Only real input (mouse, keyboard, toolbar commands, native-setter writes) is saved. **Changes made by a script directly to the DOM are not saved** — the editor re-renders the element from its own state and the edit disappears on reload. There is no version history; undo lives only within the page session.

## Layers

Depth = z-index. A layout that works:

| Depth | Layer |
|---|---|
| 0 | background image or video |
| 1 | atmospheric blocks: wind, sky |
| 2–10 | native texts and images of the layout |
| 11–16 | covering blocks: plate, TV noise |
| 20 | text on top of the plate |

The background is drawn at depth 0 and hides nothing by itself. **To make an object "emerge from behind" a detail of the background, cover that detail with an opaque plate whose depth is higher than the animation.**

## Timing

The slide settings hold the **display duration**. Fit the period of your animations to it so the loop is not cut mid-move.

## Marquee (native ticker element)

Panel: text, speed, direction, font size, font, text color, background color, animation, depth. Mechanics: CSS animation on the inner span, translateX(block width) → translateX(−text width), linear infinite. **Speed × 10 = px/s** (20 → 200 px/s); duration adapts to text length.

Consequence: a ticker cannot be hard-synchronised with a separately animated image — editing the text changes the period. For a "plane towing a banner" put the image and the text **into one HTML block with one animation**.

## Animating native editor text without converting it to HTML

Native text content is HTML with spans carrying inline styles. Because a style tag in an HTML block is global, you can target a native span by one of its inline properties, e.g. font size:

```css
.text-widget span[style*="font-size: 52px"] {
  display: inline-block;
  background: linear-gradient(100deg, #C9A24B 0 40%, #FFF0C8 50%, #C9A24B 60% 100%);
  background-size: 280% 100%;
  -webkit-background-clip: text; background-clip: text;
  color: transparent !important; -webkit-text-fill-color: transparent;
  animation: promoShine 5s linear infinite;
}
@keyframes promoShine { from { background-position: 190% 0 } to { background-position: -90% 0 } }
```

The text stays editable; changing the words does not break the shimmer.

## Checking an animation

A screenshot does not show motion. Take stable frames by scrubbing the animation:

```js
const a = el.getAnimations()[0];
a.pause(); a.currentTime = 4000; // ms
// capture a frame
a.play();
```

Save frames, stitch them into a GIF, show the result.

## Recipes

### Banner towed behind a plane

Image and text in one flex row with one shared animation — synchronisation is guaranteed whatever the text.

```html
<div class="tow">
  <img src="IMAGE_URL" alt="">
  <span class="rope"></span>
  <div class="cloth"><span class="cloth-t">PROMO TEXT</span></div>
</div>
<svg width="0" height="0">
  <filter id="towWind" x="-15%" y="-60%" width="130%" height="220%">
    <feTurbulence type="fractalNoise" baseFrequency="0.006 0.018" numOctaves="2" seed="7" result="noise">
      <animate attributeName="baseFrequency" dur="6s" values="0.006 0.018;0.012 0.030;0.006 0.018" repeatCount="indefinite"/>
    </feTurbulence>
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="7" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</svg>
<style>
.tow{position:relative;height:145px;display:flex;align-items:center;white-space:nowrap;will-change:transform;animation:towFly 16s linear infinite}
.tow img{width:218px;height:101px;flex:none;object-fit:contain;margin:0}
.rope{flex:none;width:44px;height:3px;background:#2a241c;opacity:.5;margin:0 6px}
.cloth{font-family:Oswald,sans-serif;font-size:40px;letter-spacing:3px;color:#2a241c;line-height:1;filter:url(#towWind);animation:towFlap 3.2s ease-in-out infinite;transform-origin:left center}
@keyframes towFly{0%{transform:translateX(1500px)}78%{transform:translateX(-820px)}100%{transform:translateX(-820px)}}
@keyframes towFlap{0%,100%{transform:skewY(-1.6deg) rotate(-.5deg)}50%{transform:skewY(1.6deg) rotate(.5deg)}}
</style>
```

Cycle maths: the start translateX is the position where the whole group is hidden behind the covering plate; the finish is ≤ minus the group width; the tail of the cycle is a pause so the restart is invisible. filter: url(#…) on the text gives the cloth flutter — "wave in the wind" without JS.

### TV noise overlay

```html
<div class="tvfx">
  <svg class="tvfx-n" preserveAspectRatio="none" viewBox="0 0 320 265">
    <defs>
      <filter id="tvfxNoise" x="0" y="0" width="100%" height="100%">
        <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch">
          <animate attributeName="seed" values="1;4;7;11;15;19;23;27" dur="0.42s" calcMode="discrete" repeatCount="indefinite"/>
        </feTurbulence>
        <feColorMatrix type="saturate" values="0"/>
      </filter>
    </defs>
    <rect width="320" height="265" filter="url(#tvfxNoise)" opacity="0.17"/>
  </svg>
  <div class="tvfx-scan"></div>
  <div class="tvfx-roll"></div>
</div>
<style>
.tvfx{position:relative;width:100%;height:100%;overflow:hidden;pointer-events:none}
.tvfx-n{position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:screen}
.tvfx-scan{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,rgba(255,255,255,.055) 0 2px,transparent 2px 6px)}
.tvfx-roll{position:absolute;left:0;right:0;height:20%;background:linear-gradient(to bottom,transparent,rgba(255,255,255,.07),transparent);animation:tvfxRoll 7s linear infinite}
@keyframes tvfxRoll{from{transform:translateY(-140%)}to{transform:translateY(560%)}}
</style>
```

Keep it on a small area (a "screen" inside the layout), not on the whole frame.

### Wind: gusts and a flying petal

```html
<div class="wind">
  <i class="g" style="top:12%;width:24%;animation-duration:11s"></i>
  <i class="g" style="top:63%;width:28%;animation-duration:12.5s;animation-delay:1.5s;opacity:.8"></i>
  <i class="p" style="top:8%;animation-duration:22s;animation-delay:1s"></i>
</div>
<style>
.wind{position:relative;width:100%;height:100%;overflow:hidden;pointer-events:none}
.wind i{position:absolute;display:block;left:-26%;will-change:transform}
.wind .g{height:3px;border-radius:3px;background:linear-gradient(to right,rgba(120,110,95,0),rgba(120,110,95,.4),rgba(120,110,95,0));animation:windGust linear infinite}
@keyframes windGust{from{transform:translateX(0)}to{transform:translateX(1960px)}}
.wind .p{width:15px;height:18px;background:linear-gradient(135deg,#fff,#D6CFC1);clip-path:polygon(0 12%,100% 0,86% 100%,10% 84%);filter:drop-shadow(0 2px 3px rgba(0,0,0,.18));animation:windFleck linear infinite}
@keyframes windFleck{0%{transform:translate(0,0) rotate(0)}50%{transform:translate(980px,-46px) rotate(200deg)}100%{transform:translate(1960px,28px) rotate(400deg)}}
</style>
```

Crop the block so the petals do not fly over dense cards.

### Floating and sailing in place

```css
@keyframes skyFloat{0%{transform:translate(0,0) rotate(-1.5deg)}50%{transform:translate(6px,-16px) rotate(1.5deg)}100%{transform:translate(0,0) rotate(-1.5deg)}}
@keyframes skySail{0%{transform:translate(0,0)}25%{transform:translate(-75px,-8px) rotate(-.8deg)}50%{transform:translate(-150px,0)}75%{transform:translate(-75px,8px) rotate(.8deg)}100%{transform:translate(0,0)}}
```

Several decorative images are easier to manage as **one** "sky" block with absolute positioning inside, instead of separate native image elements.

## Do not

- Do not hang pixel filters (turbulence, blur) on the full frame.
- Do not treat a DOM edit as saved without reloading.
- Do not try to build a custom effect out of the element-panel presets — with repeat 0 they loop, but only as they are.
- Do not click blindly in series of double clicks: an extra click drags the element off the slide.
- Do not click "just in case" near the slide thumbnail strip — buttons appear there, including slide deletion.

## Related

prtv-editor-overview · prtv-text-element · prtv-element-layout · prtv-agent-rules