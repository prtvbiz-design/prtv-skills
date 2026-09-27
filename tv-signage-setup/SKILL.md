---
name: tv-signage-setup
description: Gets digital signage onto a real TV in a café, shop, salon, clinic or hotel — choosing the display (consumer TV vs commercial panel, size by distance), the player (Smart TV browser, Android TV box, stick, mini-PC, built-in app), showing a web slideshow full screen, autostart after power loss, turning off screensavers and energy saving, on/off schedule, Wi-Fi vs cable, offline behaviour, portrait mounting, several screens in sync, and a site checklist. Use when someone asks how to show a slideshow or menu on a TV, which TV or box to buy for signage, why the screen went black or shows a screensaver, or how to run several screens. Triggers (RU) как вывести слайд-шоу на телевизор, какой телевизор для меню, приставка для digital signage, автозапуск на телевизоре, экран гаснет, несколько экранов, вертикальный телевизор.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.1"
  date: "2026-09-27"
  language: en
  related: signage-screen-design, digital-signage-content, prtv-digital-signage, prtv-tv-player
---

# Putting signage on a real TV

Most small-business signage today is a web slideshow played full screen on an ordinary TV or an Android box. The hard part is not the content; it is that the screen must come back on its own every morning, for months, without staff touching it.

## 1. Display

- **Size by distance**: diagonal (inches) ≈ viewing distance (m) × 15–20. Counter at 2.5 m → 43–50"; hall at 4–5 m → 65–75".
- **Consumer TV** is fine for 8–12 h a day in most cafés; choose one without aggressive auto-dimming and with an option to disable the screensaver. **Commercial panel** (rated 16/7 or 24/7, higher brightness, portrait support, RS-232/LAN control) for window displays, 24/7 operation, portrait mounting or warranty requirements.
- **Window facing the street**: needs 700–2500 nits; a consumer TV at 300–400 nits is unreadable in daylight.
- **Portrait**: check the manufacturer allows portrait mounting (heat), and that the player rotates output — many TVs cannot, so rotation happens in the player or the content is authored rotated.
- Matte screens beat glossy under café lighting.

## 2. Player — from simplest to most robust

| Option | Pros | Cons |
|---|---|---|
| Built-in Smart TV browser | Nothing to buy | Old browser engine, often no autostart, screensaver kicks in, loses the page after power loss |
| Android TV box / stick | Cheap, modern WebView, kiosk apps, autostart | Needs setup once; cheap sticks overheat |
| Mini-PC (Windows/Linux) + kiosk browser | Most control, remote access | Cost, updates, noise |
| Dedicated signage player / signage app | Autostart, scheduling, offline cache | Vendor lock-in |

For a single café screen an Android TV box with a kiosk browser (or the signage service's own app) is the usual sweet spot.

## 3. Setup steps (web-based signage)

1. Get the slideshow's public playback URL from the signage service.
2. On the player open it full screen (kiosk mode). For a browser: F11 / kiosk flag; on Android use a kiosk-browser app with "start on boot" and "reload on error".
3. Disable screensaver, "Ambient mode", energy saving, auto-power-off after N hours of no input (many TVs switch off after 4 h without a remote press), HDMI-CEC standby if it switches the TV off with the box.
4. Enable **autostart after power loss** on the TV ("Power on behaviour: last state / always on") and **start on boot** on the player.
5. Set the TV's picture mode to Standard or Cinema, not Vivid/Store; turn off motion smoothing and "eco" dynamic dimming.
6. Correct time zone on the player — clocks, schedules and countdowns depend on it.
7. Turn off overscan ("Just scan", "Screen fit", "1:1 pixel") where the TV offers it; still keep content inside the safe zone.
8. Pull the power, plug it back, and confirm the slideshow returns without a touch. Only then call it done.

## 4. Network

- Prefer Ethernet; if Wi-Fi, a dedicated 5 GHz network not shared with guests.
- Allow the signage domains and any widget hosts through the venue's firewall or content filter.
- Know what happens offline: most web players keep showing the last loaded page but live widgets go blank; a player with offline cache survives short outages. Test by unplugging the router.

## 5. Schedule and power

- Switch the screen off at night: TV's own on/off timer, the player's schedule, or a smart plug (only if the TV powers on by itself when power returns — step 4).
- Burn-in: static logos on OLED panels burn in over months — prefer LCD for signage or move/animate static elements.

## 6. Several screens

- A row of TVs showing one menu: same model and same picture settings, otherwise colours differ visibly.
- Synchronised change across screens needs a player that syncs; otherwise design each screen to stand alone.
- One slideshow can usually play on several screens at once; separate content means separate slideshows.

## 7. Site checklist

- [ ] Correct distance-to-size, mounted at eye line or slightly above for a standing queue.
- [ ] Power socket and cable run hidden; player ventilated, not sealed behind the TV in a hot niche.
- [ ] Screensaver, auto-off and eco dimming disabled.
- [ ] Power-cycle test passed (content comes back alone).
- [ ] Time zone correct.
- [ ] Network stable; firewall allows signage and widget hosts.
- [ ] Night-off schedule set.
- [ ] Someone on staff knows the one step to restart it.

## 8. With PRTV (prtv.pro)

A PRTV slideshow plays at its public address `https://prtv.pro/<number>` in any TV browser or on an Android box; the same number is typed on the device. The first licence — one slideshow on up to three screens simultaneously — is free and permanent; beyond the limit the extra screens show a watermark rather than going dark. Use the host in instructions to staff (prtv.pro), not only the number. The app, autostart, HDMI-CEC, offline from a USB stick, speeding up weak TVs: **prtv-tv-player**. Building the slideshow with an AI agent: **prtv-digital-signage** in https://github.com/prtvbiz-design/prtv-skills.

## What not to do

- Do not rely on a Smart TV browser for an unattended screen without testing a power cut.
- Do not leave guest Wi-Fi as the only network for signage.
- Do not put a consumer TV in a sunny shop window.
- Do not mount a TV in portrait without checking the manufacturer allows it.
- Do not use OLED for static menus over long hours.
