---
name: prtv-tv-player
description: Running a PRTV slideshow on a TV and keeping it stable — prtv.su (5-digit) and prtv.pro (7-digit) numbers, the PRTV app for Android TV, Google TV, Yandex TV and Sber TV (APK, unknown sources), browsers for Samsung, LG, Sony, Xiaomi, Huawei, a plain TV with a stick, autostart after power-on (Launch On Boot), screen on/off by schedule via HDMI-CEC, caching and full offline from a USB stick (prtvsh folder), burn-in prevention, remote control, portrait screens, TV requirements, diagnosing and speeding up a slow slideshow. Use when a PRTV slideshow must go on a TV, lags, does not start by itself, disappears without internet, or the screen must switch off at night. Triggers (RU) приложение PRTV для телевизора, APK PRTV, тормозит слайд-шоу на Android TV, автозапуск приложения Android TV, режим сна HDMI-CEC, слайд-шоу с флешки без интернета, выгорание экрана телевизора.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: tv-signage-setup, prtv-digital-signage, prtv-templates, prtv-editor-overview
---

# PRTV on a TV

General display, player and network choices are in **tv-signage-setup**. This skill covers what is specific to the PRTV player.

## 1. Number and address

- Every slideshow, collection and stream has a number. The old prtv.su editor uses 5 digits (`prtv.su/11417`), the new prtv.pro uses 7 digits with leading zeros (`prtv.pro/0012746`).
- Two ways to show it: type the number into the PRTV app, or open the address in the TV browser. The app is more reliable.
- Several screens with the same content: the same number on each TV (the free licence covers up to three screens at once; beyond that a watermark appears, not a black screen). Different content per branch: one slideshow per branch in one account.

## 2. The app

- **App for PRTV.PRO** (since May 2026, test version): APK from https://s.prtv.su/prilozhenie-dlya-prtv-pro. Plays 5- and 7-digit numbers, collections and streams, iiko / R_Keeper / Quick Resto menus; caching and offline. Android 6.0+, 1 GB RAM (2 GB better). Installs on Android TV, Google TV, boxes, Yandex TV and Sber TV.
- **Old app**, prtv.su only: Google Play (`su.prtv.tvapp`), RuStore, RuMarket or APK from https://s.prtv.su/prilozheniya-dlya-tv. When installing an APK over an old version, uninstall the old one first if it fails.
- APK install: download in the TV browser or bring it on a USB stick → enable "Unknown sources" (Settings → Apps → Security & restrictions) → install.
- Samsung (Tizen, 2015+) and LG (webOS, 2014+): via their stores or the browser.

## 3. Browser instead of the app

The stock TV browser often shows an address bar or leaves full screen. Install:
- Android TV: TV Bro (no ads), Open Browser, BrowseHere, Firefox TV; Puffin TV is free for only an hour a day.
- Xiaomi (often no browser at all): Open Browser, TV Bro.
- LG webOS 2020+: Opera, Chrome, Yandex Browser.
- Sony Bravia (Android/Google TV): Vewd, DuckDuckGo.
- Huawei: Kiwi, Via, UC Browser Turbo.
For an unattended screen, set the address as the home page or in the box's autostart.

## 4. Plain (non-smart) TV

Any Android box on HDMI. The cheapest ones lag; Xiaomi Mi TV Stick is tested with the app. A tablet works too.

## 5. Autostart after power-on

The app does not start by itself after a power cut. On Android TV: **Launch On Boot** (F-Droid or Aptoide) → switch it on → "Select App" → PRTV (`su.prtv.tvapp`) → grant autostart permission to both apps → reboot and check. Alternatives: AutoStart for AndroidTV, AutoStart No Root. Not every model works; on Android 14 it depends on the Launch On Boot version.

## 6. Screen on schedule — sleep mode via HDMI-CEC

The app switches the TV on and off via HDMI-CEC **only from an external Android box**: an app inside the TV itself lacks the system permission to control power.
1. On the box: Settings → About → press "Build" 5–10 times (developer mode).
2. Find HDMI-CEC (Developer options, Inputs, HDMI settings, Display & sound or Advanced).
3. Enable "Control HDMI devices", "Auto device off", "Auto device on".
4. Update the app to the latest version and set the schedule there.

## 7. Cache and offline

Without internet a cloud slideshow does not show unless caching is on. Three scenarios in the PRO app:
1. **One TV**: grant the app "Storage" ("Files and media"), switch on "Caching" on the home screen, enter the number — files go to TV memory.
2. **Lots of video**: insert a USB stick, allow access, enable cache — videos are saved to `prtv/cache/` on the stick and play from there.
3. **Full offline**: press "Download" in the editor on a computer — 30+ files (slide html, videos, images). Copy them all into a `prtvsh` folder (lower case) in the stick's root, with no duplicates like `video(3).mp4`. On the TV press "Slideshow from USB". Cloud edits do not arrive in this mode.

Slideshow settings also have an **offline image** shown if the connection drops.

## 8. Burn-in prevention

A static menu for hours burns the panel. At the bottom of slideshow settings — **screen matrix prevention**: a "rainbow" band sweeps the screen at an interval. Recommended: a slow wide band every 3 hours.

## 9. Remote control

- Left / right — previous and next slide (a salon master shows a client the right slide; a presentation without a USB stick).
- Up on a YouTube-channel slide — the channel's previous video; down — scrolls an RSS feed.

## 10. Portrait screen

- If the TV can rotate the picture, mount it vertically and choose portrait orientation in slideshow settings.
- If not, keep the slideshow landscape, rotate every element by 90° and mount the TV vertically. Awkward to edit, but works on any TV. Check the manufacturer allows vertical mounting.
- In PRO the canvas size is free-form, so non-standard screens fit.

## 11. Requirements and speed

- Minimum: 2 cores at 1.5 GHz, 1 GB RAM, HD. Recommended: 4 cores from 2 GHz, 2 GB, Full HD, current firmware, wired network.
- **Diagnose a heavy slideshow**: open the number in desktop Chrome → View source → Sources → the `upload` folder lists every image and its size.
- **Fix**:
  - images to WebP (50–70 % lighter, keeps transparency), background under 200 KB, longest side ≤ 2500–3000 px; compress before upload rather than scaling in the editor;
  - repeated icons and flags as SVG;
  - bake dish photos and decoration into one background, keep prices as text;
  - widgets with external data (traffic, weather, air) — refresh less often and set as a permanent element instead of one per slide;
  - drop animated transitions, change slides less often;
  - on the TV clear the cache, close background apps, disable auto power-off and sleep.
- The editor itself lags on a computer — switch off slide previews and "sticky edges" in the left menu.
- For network allow-lists: PRTV server IP 86.110.194.167.

## What not to do

- Do not expect an app inside the TV to switch the screen off on schedule — use an external box.
- Do not promise offline playback without enabling cache or offline mode.
- Do not leave a static menu all day without burn-in prevention.
- Do not put a heavy template on a 1 GB TV without lightening it.
