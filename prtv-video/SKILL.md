---
name: prtv-video
description: Video in the PRTV (prtv.pro) digital-signage editor — the Video element (YouTube incl. playlists, VK Video, Kinescope, Vimeo, own files via PRTV video hosting), background video with elements on top, embedding other players through an HTML block, sound and autoplay on TVs, and what a file must be to loop seamlessly as a menu-board background. Use when putting a video or video background on a slide in prtv.pro, choosing a hosting, or finding out why a video does not play or loop cleanly on a TV screen. Triggers (RU) видео на слайде, видеофон, YouTube на экране, видео не играет на телевизоре, зацикленное видео PRTV.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  product: PRTV (prtv.pro) digital signage editor
  version: "1.1"
  date: "2026-09-26"
  language: en
  scope: editor UI + reading page state from DOM; no private API calls
---

# Video in the PRTV editor

PRTV has three ways to show moving video on a screen, and they are not interchangeable: a **Video element** on a slide, a **background video** under the whole slide, and a foreign player embedded through an **HTML block**. There is also PRTV's own video hosting for files the venue owns. This skill maps them and sets the requirements for a video that has to loop for hours on a menu board. General editor conventions are in prtv-editor-overview; placement and depth of elements in prtv-element-layout; slide-level settings in prtv-slide-settings.

## 1. The Video element

Left panel → **Базовые** → **Видео**. A dedicated element type, not a widget and not an HTML block, placed and sized like any element (drag; keep it inside the safe zone — prtv-element-layout §7).

**Supported sources**, by link or by file:

| Source | Notes |
|---|---|
| YouTube | single videos and playlists |
| VK Video | own player integration |
| Kinescope | Russian video hosting — the practical choice for venues in Russia/CIS where YouTube may be slow or blocked on the venue's network |
| Vimeo | supported by the player |
| Own file | uploaded to PRTV video hosting (§3) and picked in the element |

Rutube is not a source of the Video element; see §4.

**What the element can do** (the exact labels depend on the panel version — check the element panel after adding the element): a poster image shown before the video loads; a logo overlaid on the video for branding; loop; readiness handling so the first frame is ready when the slide appears; volume and mute.

**Sound.** Signage video plays silently by default, and that is the right default: autoplay *with* sound is restricted by browser and TV policies, and a video that needs sound to start may never start on a Smart TV. Design for muted playback; if sound is required, test on the actual device.

**Thumbnails and canvas.** Like widgets, embedded players are not rendered in the slide strip thumbnails; judge a video slide in the preview player (eye button) or on the public TV page, waiting at least one full slide duration.

## 2. Background video of a slide

A separate mechanism: the video is the **background of the whole slide**, and any elements — text, prices, widgets, promo plates — sit on top of it. Set in slide settings: gear on the thumbnail → «Стили по умолчанию» → «Фоновое видео» — paste an `https://` link, choose «Без звука» — Yes. The same field exists in slideshow defaults (paintbrush button) for all new slides. If the link is not supported, an overlay in the field says so.

Sources for background video: YouTube, VK Video, Kinescope.

This is the strongest pattern for HoReCa showcases and promo slides — "cooking-process video under the menu", "steam and rain behind the offer" — and it is under-used. Keep the centre of the frame calm in the video itself so that the content on top stays readable (§5), and put a scrim under text as usual (prtv-element-layout §7).

The background is drawn at depth 0; elements start at depth 1. There is no way to put an element *under* a background video.

## 3. PRTV video hosting (own files)

The account has a video hosting section where a venue uploads its own files and then picks them in a Video element. This removes the dependency on external hosts, their autoplay rules and network blocks. The section is a paid feature; limits on file size, duration and formats are shown in the upload dialog of the account and should be read there.

For background video of a slide, the confirmed hosting in real builds was Kinescope: upload there, paste the link into the background-video field.

## 4. Other players through an HTML block

An HTML block accepts any valid `<iframe>` embed code of a video host — Rutube, YouTube, VK, Vimeo — and shows the player. For Rutube this is currently the only path (neither the Video element nor the legacy video widget supports it). Set the block's background alpha to 0 and its depth as for any HTML block (prtv-html-block-animation). Autoplay, mute and loop then follow the rules of the host's embed parameters and the TV's policies — verify on the real device, not only in the editor.

There is also a legacy **video widget** on s.prtv.su that wraps VK and Facebook embeds only. It has no Kinescope, no own hosting, no poster or logo; prefer the native Video element for anything new.

## 5. Requirements for a looping background video

A menu board plays the same clip for hours; a visible seam every 10 seconds is worse than a still image. The rules below are what a file must satisfy *before* it goes into PRTV.

**Seamless loop = the last frame is identical to the first, and the motion arrives back at the start naturally.** Three kinds of loop, best to worst for signage:

1. **True loop** — the content returns to the identical start frame through a closed, meaningful movement. The goal.
2. **Crossfade loop** — a 0.5–1 s crossfade hides a small mismatch at the seam. The fallback.
3. **Ping-pong (mirror)** — forward then reversed. Only for symmetric effects (flicker, breathing light). Never for directed or causal motion: smoke goes back into the chimney, a crane returns the load to the ship.

Two independent clips joined end to end do not loop — every element is out of phase at the join. One clip made to end where it started does.

**What loops well:** smoke, steam, water and ripples, clouds, leaves in wind, flickering light, sparks — slow, inherently cyclic motion; the seam is invisible. **What loops badly:** a crane carrying a load, vehicles, walking people, anything "from A to B"; fast or abrupt motion; small figures; irreversible actions (cutting).

**Layer strategy:** put ambient motion (smoke, sea, foliage) into the video and directed motion (a moving vehicle, a swinging sign) into a CSS animation in an HTML block on top, where its period and path are exact — see prtv-html-block-animation. Compose both over a still base.

**Technical checklist for the file:**

- Aspect 16:9, matching the 1920×1080 canvas; 1280×720 is usually enough for a background, 1920×1080 if fine detail matters.
- No audio track. Signage plays muted; a silent audio track only adds size.
- H.264, `yuv420p` pixel format — the safest combination for Smart TV browsers.
- Duration: aim for about 10 s for a generated loop; longer clips loop less reliably.
- Verify the seam before delivery: the mean difference between the last and the first frame should be small (under about 3 on a 0–255 scale is invisible after compression; above 8 the seam shows). If it is large, map the difference by zones to find which element did not return to its start.
- The loop period should fit the slide's display duration (prtv-slide-settings) so the cut to the next slide does not land mid-motion.
- Keep the centre of the frame empty of motion when text or prices will sit there.

## 6. Checking a video slide

- The editor canvas shows a still; the slide strip shows a placeholder. Use the preview player and wait a full slide duration.
- Check on the target TV or set-top box at least once: autoplay, mute and codec support differ between desktop browsers and TV browsers.
- If the video does not start on the TV: confirm it is muted, the source is reachable from the venue's network, and the format is H.264 / yuv420p.
- Uploaded files are served from the PRTV domain, so there are no cross-origin issues in the player.

## What not to do

- Do not rely on sound for a video to start.
- Do not judge a video slide by the thumbnail or the editor canvas.
- Do not join two clips end to end and call it a loop.
- Do not mirror (ping-pong) a clip with directed motion.
- Do not put text directly over a busy area of a background video without a scrim.
- Do not use the legacy VK/Facebook video widget for new slides.
- Do not expect an element to sit under a background video.
- Do not upload a background clip with an audio track.

## Related

prtv-editor-overview · prtv-slide-settings · prtv-element-layout · prtv-html-block-animation · prtv-widgets · prtv-agent-rules
