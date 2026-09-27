---
name: prtv-integrations
description: Live data and automation in PRTV (prtv.pro) — menus and prices from iiko, R_Keeper and Quick Resto, tables from Excel, schedules from Google Calendar, VK, Telegram and Odnoklassniki posts, YouTube, VK Video and own video hosting, Google Slides, Yandex Maps reviews and panoramas, IP cameras over RTSP, voting from phones, ad-free music, streams (switching slideshows on a schedule), collections, impression statistics for advertisers, licences and the binding trap, earning from the screen. Use when a menu or schedule must update on screen without manual edits, a POS system, camera, social feed or video must be connected, different slideshows should run in the morning and evening, or an advertiser needs a report. Triggers (RU) меню из iiko на телевизор, R_Keeper меню борд, Quick Resto экран, Excel на телевизоре, Google календарь на экране, IP-камера RTSP на телевизор, VK видео на экране, потоки PRTV расписание, статистика показов рекламы.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: prtv-feed-widget, prtv-widgets-catalog, prtv-video, prtv-tv-player, menu-board-by-venue
---

# PRTV: live data, schedules, statistics

A screen that updates itself never goes stale. Rule: whatever staff change (prices, stop list, timetable, deal of the day) should come from the system where they already change it. Google Sheets, RSS, iCal, central-bank rates and the production calendar go through the «Лента» (Feed) widget — skill **prtv-feed-widget**.

## 1. POS systems — menus and prices automatically

Connect once in prtv.pro: **Settings → Restaurant services** (prtv.pro/settings). On a slide use the **Restaurant menu** widget: pick the service, dishes (all by default), items per row, separate font and size for name and price, photos (4 positions, padding, size, rounding).

- **R_Keeper**: in R_Keeper "Integrations → API connection → Add API connection" → copy client_id and client_secret → in PRTV "Stand number (Client ID)" and "Token (Client Secret)".
- **iiko**: "External menus → Add → Generate menu" (edit dishes, photos, order there) → "Cloud API settings → Integrations → Add" (external menu, price source, outlet) → API key into PRTV. On the slide pick organisation and menu. If there is no price-category ID use `00000000-0000-0000-0000-000000000000`.
- **Quick Resto**: login and password from "Enterprise → Settings". Quick Resto does not send dish photos — add them to the slide by hand.
- The venue owner enters POS credentials; an agent never asks for or stores them.

## 2. Tables and calendars

- **Excel / table**: the Table element (new or imported from Excel) or an online table in an HTML block. Changes reach the TV within minutes. Cases: canteen menu per day, doctors' schedule (name, speciality, room, days), shifts and KPIs on a factory floor, salon masters' schedule.
- **Google Sheet** with prices and timetables — via the Feed widget (prtv-feed-widget).
- **Google Calendar**: make the calendar public, copy its ID from "Integrate calendar" → https://s.prtv.su/informery/google-kalendar (day / week / month view, font, colours) → code into an HTML block. Used for school timetables, doctors' hours, shifts, staff birthdays.
- **Google Slides**: File → Share → Publish to the web → Embed → iframe into an HTML block.

## 3. Social feeds — content arrives by itself

- Feed element: Telegram (channels and chats), VK, Odnoklassniki, RSS. Connect VK once in account settings (prtv.pro/settings). Set post count, order, image position, refresh rate.
- Trick: **a post is a slide**. The chef posts the dish of the day to a Telegram channel, the salon posts a promo in its VK group — and it appears on screen with no slideshow edit.
- Instagram, Facebook and Twitter in old templates do not work in Russia — replace them.

## 4. Video and music

- **YouTube**: a video, Shorts, a playlist or a **channel page** — then the latest channel video always plays (remote "up" = previous video). If it does not start, check `autoplay=1` in the code; embedded video size is set by width/height in the code, not by dragging. Increase the slide duration for video slides (default 30 s).
- **VK Video** (YouTube replacement): connect VK in the PRTV profile, set the video's access to "All users" or by link, enable loop if needed, Video button → link.
- **PRTV own video hosting** (paid feature): avi/mp4 up to 300 MB, any length, no ads or third-party logos; "Video → Kinescope → Choose video". Vimeo works; RuTube does not support autoplay.
- **Background streams**: 24/7 YouTube streams (lofi, café music, nature, city webcams, NASA) and live TV channels via RuTube "Share → Player embed code".
- **Music**: built-in radio stations of the old version were switched off on 28.04.2026. In PRO — the "Coffee shop" radio in slideshow settings (instrumental, picked by weekday and time of day). Alternative — the "Ad-free radio" widget, https://s.prtv.su/informery/radio-free (Instrumental, Acoustics, Indie, Nu Jazz, Smooth, Background): it plays across the whole slideshow whichever slide holds it; the player can hide under an image. Other players (Yandex Music, Mixcloud with Autoplay) via HTML.

## 5. Cameras and maps

- **IP camera or DVR (RTSP)**: a static public IP; a camera with RTSP (tested: HiWatch, Hikvision, TP-Link, D-Link, iCSee); port 554 forwarded on the router (several cameras on external 5541, 5542…). URL like `rtsp://user:password@public_ip:port/…` (HiWatch: `/ISAPI/Streaming/Channels/101`, 101 = camera 1 stream 1, 201 = camera 2). Browsers cannot play RTSP — convert to HLS with rtsp.me and paste its iframe into an HTML block. Ideas: restaurant kitchen, playground by the entrance, a beach for a travel agency.
- **Yandex Maps reviews**: organisation card → "⋮ → Share" → reviews widget code → HTML block.
- **Yandex street panoramas**: "Panoramas and photos" → point → Share → "Widget with map" → HTML block (not live; the capture year is in the corner).
- **Traffic map**: the address from slideshow settings fills in automatically; several maps can share a slide (hotel → airport, sights).
- **OpenStreetMap**: pick a layer (e.g. transport) → "Share / Embed" → HTML.

## 6. Voting

The voting widget (https://s.prtv.su/golosovanie): the screen shows a question and a QR, guests vote from phones, results as bars or a pie. Set the slide to 60 s so results refresh. Ideas: next month's dish, music choice, residents' poll.

## 7. Streams — different slideshows on a schedule (paid feature)

- "Add stream" → name → click a day × hour cell → choose the slideshow and end time; the "All day" row sets one slideshow per weekday; weekly repeat.
- A **background slideshow** plays whenever nothing is scheduled.
- On the TV a stream opens by its own code in the app or by link in a browser; several TVs can run in sync.
- Scenarios: breakfast until 12:00, business lunch 12–16, main menu from 17:00; hotel — breakfast, excursions, restaurant and bar, reference info at night; school and office — a one-slide greeting slideshow scheduled on each birthday.
- A **collection** plays several slideshows in a row under one number.

## 8. Impression statistics (paid feature)

Counts impressions of any element: video, image, ticker, post. The argument for an outside advertiser: a pharmacy sells a slot to a drug maker, a filling station to a partner, a business centre to tenants, a supermarket to a supplier.

## 9. Licences — the binding trap

The first licence is free: one slideshow on three screens at once. More in "Licences" (prtv.pro/licenses): choose the quantity → pay → **always press "Continue"** → **attach the licence to the slideshow** with the button in the list. A paid but unattached licence does not remove the watermark. The balance is in profile settings. Paid features (video hosting, streams, statistics) are enabled there too and are optional.

## 10. A screen that earns

- Beeline partner programme (since September 2026): the screen owner creates a personal QR at partners.beeline.ru, shows it on a slide and is paid for connected subscribers.
- Ads from neighbours and partners (taxi, designated driver, flowers, dry cleaning in a residential building) — a slot backed by impression statistics.

## What not to do

- Do not retype prices by hand if they already live in the POS.
- Do not rely on video autoplay without checking on the actual TV.
- Do not expose a camera without a password; do not show visitors' faces without consent.
- Do not quote paid-feature prices to a client — check the current ones under Licences.
