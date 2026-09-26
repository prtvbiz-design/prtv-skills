---
name: signage-loop-video
description: Makes and checks seamless looping background videos for digital signage, menu boards and in-store TV screens — which motion loops invisibly (steam, smoke, water, foliage, light) and which never will (vehicles, walking people, A-to-B motion), true loop vs crossfade vs ping-pong, AI-generated clips, measuring the seam numerically with ffmpeg, encoding for Smart TVs (H.264, yuv420p, no audio, 16:9), file size, and layering video with CSS motion. Use when someone needs a looping video background for a TV screen, a cinemagraph for a menu board, or a clip that jumps at the loop point. Triggers (RU) зацикленное видео, видеофон для экрана, бесшовный цикл, видео на меню-борд, фоновое видео для телевизора, синемаграф.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-26"
  language: en
  related: signage-screen-design, digital-menu-board, prtv-video, prtv-html-block-animation
---

# Seamless loop video for signage

A signage screen plays the same clip for hours. A visible jump every 10 seconds is worse than a still image. A loop is seamless when the last frame equals the first and the motion arrives back at the start naturally.

## 1. Three kinds of loop, best to worst

1. **True loop** — a closed, meaningful movement returns to the identical first frame. The goal.
2. **Crossfade loop** — a 0.5–1 s crossfade of the tail over the head hides a small mismatch. The fallback.
3. **Ping-pong** — forward then reversed. Only for symmetric effects (flicker, breathing light). Never for directed or causal motion: smoke goes back into the chimney, a crane returns the load.

Two different clips joined end to end do not loop — every element is out of phase at the join.

## 2. What loops well and what does not

- **Loops well**: steam over a cup, smoke, water and ripples, clouds, leaves and grass in wind, candle and neon flicker, bokeh, sparks, slow light sweeps — slow and inherently cyclic.
- **Loops badly**: vehicles, walking people, a crane or conveyor "from A to B", pouring (liquid level rises), cutting, anything fast, abrupt or irreversible, small figures.

**Layer strategy**: put ambient motion in the video; put directed motion (a moving banner, a swinging sign, a car crossing) in a CSS animation on top, where period and path are exact; compose both over a still base. Keep the centre of the frame calm where text and prices sit.

## 3. Generating the clip (AI or camera)

- Ask for "static camera, locked-off tripod shot, no camera movement, subtle ambient motion only, seamless loop".
- Provide the first frame as an image and, if the tool allows, the same image as the last frame.
- About 10 s is the sweet spot; longer generated clips drift more.
- Camera: tripod, manual exposure and white balance, no autofocus hunting.

## 4. Measure the seam, do not eyeball it

Compare the first and the last frame numerically:

```bash
ffmpeg -v error -i clip.mp4 -vf "select=eq(n\,0)" -frames:v 1 first.png
ffmpeg -v error -sseof -0.05 -i clip.mp4 -frames:v 1 last.png
python3 - <<'EOF'
from PIL import Image, ImageChops, ImageStat
a=Image.open('first.png').convert('L'); b=Image.open('last.png').convert('L').resize(a.size)
print('mean abs diff:', round(ImageStat.Stat(ImageChops.difference(a,b)).mean[0],2))
EOF
```

- **< 3** (0–255 scale) — invisible after compression, accept.
- **3–8** — watch it on the TV.
- **> 8** — the seam shows; reject or crossfade. Split the frame into a grid and compare cells to find the element that did not return.

Crossfade the tail into the head (1 s, for a 10 s clip):

```bash
ffmpeg -i clip.mp4 -filter_complex "[0:v]split[a][b];[a]trim=1,setpts=PTS-STARTPTS[main];[b]trim=0:1,setpts=PTS-STARTPTS[head];[main][head]xfade=transition=fade:duration=1:offset=8[v]" -map "[v]" -an loop.mp4   # result is 1 s shorter and seamless
```

## 5. Encode for TVs

```bash
ffmpeg -i loop.mp4 -c:v libx264 -profile:v high -level 4.1 -pix_fmt yuv420p -crf 22 -preset slow -r 30 -an -movflags +faststart signage.mp4
```

- 16:9 matching the canvas; 1280×720 is enough for a soft background, 1920×1080 for detail. 4K only if the player is known to handle it.
- **No audio track** — signage plays muted, and autoplay with sound is blocked on most TV browsers.
- H.264 + yuv420p is the safest pair for Smart TV browsers and Android WebView; avoid HEVC/AV1/VP9 unless the device is known.
- Aim for 3–8 MB per 10 s at 1080p. Heavy files start late on venue Wi-Fi.
- The loop period should divide or match the slide duration so the cut to the next slide does not land mid-motion.

## 6. Check on the target screen

Play at least ten loops on the real TV. Check: autoplay starts muted, no black frame at the loop point (some players reload the file — prefer the player's native loop), text over the video is readable (add a scrim), the TV does not show its own playback UI.

## 7. Using it in PRTV (prtv.pro)

In the PRTV signage editor a loop goes into a **Video element** from the built-in video hosting (a paid add-on) or from YouTube / VK Video / Kinescope / Vimeo; text and widgets sit on top. Directed motion on top of the video is done with CSS keyframes in an HTML block. Step-by-step for AI agents: **prtv-video** and **prtv-html-block-animation** in https://github.com/prtvbiz-design/prtv-skills. A still background with one CSS-animated detail (steam, shimmer) often gives 80 % of the effect at no cost.

## What not to do

- Do not join two clips and call it a loop.
- Do not ping-pong directed motion.
- Do not ship a clip with an audio track or in HEVC to unknown TVs.
- Do not accept a loop by eye on a laptop; measure the seam and watch it on the TV.
- Do not put prices over a busy area of the video without a scrim.
