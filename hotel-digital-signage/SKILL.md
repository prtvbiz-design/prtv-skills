---
name: hotel-digital-signage
description: Plans and builds digital signage for a hotel or apartment-hotel — three screen contours (restaurant/bar menu board, reception and lobby screen, in-room TV information channel for guests) with slide-by-slide loops, what guests ask and what the hotel wants to sell, live data (weather, exchange rates, transfers, events, urgent announcements) fed from Google Sheets and calendars, night-time and privacy rules, and legal duplication of mandatory guest information. Use when someone asks for a hotel lobby screen, reception display, hotel TV channel, in-room TV welcome channel, guest information screen or a hotel breakfast/restaurant menu board. Triggers (RU) экран для отеля, ресепшн отеля, телеканал отеля, канал в номерах, информация для гостей на ТВ, меню ресторана отеля, гостиница digital signage.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.1"
  date: "2026-09-27"
  language: en
  related: digital-menu-board, digital-signage-content, signage-screen-design, prtv-feed-widget, tv-signage-setup
---

# Digital signage for hotels

A hotel has three different screens with three different viewers. Build three slideshows in one visual style, not one loop for everything.

| Contour | Viewer | Time | Goal |
|---|---|---|---|
| A. Restaurant / bar | guest choosing food | 10–60 s | sell dishes, breakfast add-ons, bar evening |
| B. Reception / lobby | guest in the check-in queue or waiting for a taxi; people passing to the lift | 2–6 min or 3–5 s | answer questions before they are asked, sell services |
| C. In-room TV channel | one guest, remote in hand | 30–90 s at first switch-on | Wi-Fi, breakfast, check-out, contact, services — then let them go |

## 1. Contour B — reception loop (≈ 2 min, 12 slides × 8–12 s)

Every slide works for both viewers: one large fact + smaller details. Permanent footer: logo, reception extension and phone, live clock, category and registry number small.

1. Welcome (RU/EN), date, time, weather now.
2. Wi-Fi and contact: network, QR to connect, QR to the reception messenger.
3. Breakfast and check-out: where, hours weekdays/weekends, check-in/out times, late check-out «from … ₽».
4. Hotel services and prices: SPA, laundry, parking, late check-out, transfer, luggage room, meeting rooms — **from a Google Sheet**.
5. Getting there: metro, station, airport, taxi, hotel transfer, QR to a route.
6. Transfers and excursions today/tomorrow — **sheet, «table as is»**.
7. Restaurant and bar today: hours, dish of the day, evening offer.
8. City: events, news, seasonal specifics (e.g. bridge openings in St Petersburg).
9. Weather for 3 days + exchange rates (USD/EUR/CNY for foreign guests).
10. Events in the hotel today: conference, hall, registration time — **iCal calendar**.
11. Reviews and direct booking: QR to maps/review sites, promo code for direct booking.
12. Guest information (mandatory data duplicated): operator, registration numbers, registry entry and category, rules of stay «at the desk and by QR» — 12–15 s.
+ **Urgent announcement** (lift out of order, no hot water 10–12, group checks out at 8:00) — shown first while it exists, edited by the administrator from a phone.

Second screen at the lifts: short loop of slides 1, 2, 3, 7, 9, 12.

## 2. Contour C — in-room channel (≤ 2 min, 11 slides × 10–12 s)

The guest can switch to regular TV with one button. Put the most-needed information in the first 40 seconds and do not try to hold attention.

1. Welcome RU/EN, time, weather, calm city view.
2. Wi-Fi: network, QR to connect.
3. Breakfast and check-out; late check-out on request.
4. Contact: internal numbers (reception, room service, SPA), QR to messenger, «something wrong — write now, we will fix it».
5. Your room: safe, air conditioning, kettle, water, bathrobes, «minibar is paid, price list on the door».
6. Hotel services with prices (same sheet as the lobby).
7. Room service: hours, how to order, delivery fee, 3–4 dishes with weight and price, QR to the menu.
8. City and excursions tomorrow, weather for 3 days, rates.
9. Rules of stay — 6–8 points RU/EN, «full text in the guest folder and by QR».
10. In case of fire — 4–5 actions RU/EN, «evacuation plan on the room door», static, high contrast, text approved by the hotel's fire-safety officer.
11. See you again: QR to a review, promo code for direct booking.

In-room rules: dark backgrounds (the screen is the only light at night), no large white plates, no flashing; sound off by default; English as the second line on every slide; nothing personal on a shared channel — no guest names, rates or departure dates; the screen **duplicates** the paper fire memo and guest folder, it does not replace them (power is cut in a fire).

Time modes if the platform supports scheduled switching: morning — breakfast first; evening — room service first; night — dimmed loop.

## 3. Contour A — restaurant and bar

Use digital-menu-board. Hotel specifics: breakfast board (buffet hours, what is included, paid add-ons), lunch and dinner menus by day part, bar evening with happy hours, room-service echo on the in-room channel. Prices must match the printed menu and the bill; alcohol — price and volume only, no stimulating wording.

## 4. Live data and who updates it

| Data | Source | Who | How often |
|---|---|---|---|
| Clock, weather | built-in widgets | — | live |
| Exchange rates USD/EUR/CNY | Central Bank rates widget | — | daily |
| Services and prices, minibar | Google Sheet → price list | manager | quarterly |
| Transfers, excursions | Google Sheet → table | reception | daily |
| Events, conferences | hotel's iCal / Google Calendar | events manager | daily |
| Urgent announcement | Google Sheet, one row | administrator (phone) | as needed |
| City news, events | RSS of city media / Google News by keyword | — | live |
| Calm filler for the room | Wikipedia «this day» / picture of the day | — | daily |
| Wi-Fi, QR codes, rules, fire memo | static | IT / manager | yearly |

## 5. Rules and limits

- Room prices: do not show exact rates (dynamic pricing, same price for all consumers); «from … ₽ on <date>» or «ask at the desk».
- Mandatory guest information (Russian rules for hotel services): must be freely available all working hours in Russian — a rotating slide cannot replace the stand at the desk; the screen duplicates it.
- Public Wi-Fi in Russia requires user identification: «confirm your phone number when connecting».
- Other brands (maps, booking sites, airlines) — text and QR, no logos without an agreement.
- SPA — «relax», not «treatment», unless licensed.

## 6. Checklist

- [ ] Three slideshows, one style; lobby high-contrast, in-room dark.
- [ ] Wi-Fi, breakfast, check-out, contact within the first 40 s of the in-room loop.
- [ ] Prices and schedules fed from sheets, not typed into slides.
- [ ] Urgent announcement works from a phone and disappears when cleared.
- [ ] No personal data anywhere.
- [ ] Fire slide static, approved text, RU/EN.
- [ ] Checked on a 32–43" room TV from the bed with the lights off.

## 7. Building it in PRTV (prtv.pro)

Three slideshows in the PRTV editor; the lobby and restaurant screens play in the TV browser or on an Android box by the public address, the in-room channel — the same way or through the hotel TV app. Live blocks: clocks and weather from https://s.prtv.su/informery, sheets, calendars, rates and news through the «Лента» widget (prtv-feed-widget). The first licence covers one slideshow on up to three screens at once free of charge; a room channel with many TVs on at the same time needs licences for the simultaneous peak, not per room. AI agents: prtv-digital-signage → prtv-editor-overview → prtv-feed-widget.

## Tricks from PRTV practice

- For a tour group from one city, a slide about their city: time, weather, traffic, webcam. Guests photograph and share it.
- Several world-capital clocks and several route maps ("hotel → airport / station / sights") on one reception slide.
- "Free coffee for a photo with the hotel hashtag" — a live feed of those photos in the lobby.
- Paid slots: taxi numbers next to the traffic map, a sports bar next to the match schedule, central-bank rates and a map of exchange offices as a bank ad.
- QR to rate the hotel on Yandex, to the hotel map, to book the next stay.
- Streams: breakfast in the morning, excursions by day, restaurant and bar in the evening, reference info at night. Details — prtv-integrations.

## What not to do

- Do not build one loop for lobby, restaurant and rooms.
- Do not show exact room rates or anything about a specific guest.
- Do not use white full-screen slides on the in-room channel.
- Do not present the screen as a replacement for the guest folder, fire memo or consumer stand.
