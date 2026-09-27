---
name: fitness-club-signage
description: Plans screens for fitness clubs, gyms, yoga, dance and martial-arts studios, swimming pools — group class timetable for today and the week, gym load by hour, memberships and prices, trainers, trial class, promotions with countdown, members' results and social wall, outdoor training with air quality and weather, club addresses and hours, sports news and motivation; with slide plans, Google Sheet and calendar feeds and ready PRTV templates. Use when someone wants TVs at a fitness club reception, gym floor, changing area or studio lobby. Triggers (RU) экран в фитнес-клуб, расписание групповых занятий на экран, телевизор в тренажёрном зале, студия йоги экран, бассейн расписание на ТВ, загруженность зала.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: digital-signage-content, signage-screen-design, prtv-feed-widget
---

# Screens for fitness clubs and studios

Members come 2–4 times a week — a static loop is invisible within a fortnight. Live data (timetable, load, today's changes) keeps the screen useful; members' results keep it personal.

## 1. Reception / lobby loop (10–12 slides, 10–15 s)

1. **Group classes today** — time, class, trainer, studio; changes and cancellations highlighted — iCal calendar («schedule» mode) or Google Sheet.
2. Timetable for the week (table).
3. **Gym load now / by hour** — members choose quiet hours; sheet «table as is».
4. Membership offers with prices and conditions — sheet → price list; promotion with countdown («+1 month free when buying in winter»).
5. Trainer cards: photo, specialisation, certificate; «personal training — book at the desk».
6. Trial class for newcomers + QR to book.
7. **Members' wall**: posts with the club hashtag or from the club's VK/Telegram, «post your result — get a bonus».
8. Challenge of the month / leaderboard (sheet).
9. Outdoor training: weather + **air quality** widget.
10. Club zones and services (cardio, pool, sauna, TRX, massage, fitness bar).
11. Addresses of the network and hours; holiday hours from the production calendar.
12. Motivation or sports news (RSS of a sports medium) — short.

## 2. Gym floor and studios

Gym floor: timer-friendly content, exercise technique videos without sound, «next class in studio 2 starts in 10 min» (countdown), the fitness bar menu. Studio door: today's classes in that studio only, large type, seen from 5–8 m.

## 3. Rules

- Before/after photos only with members' consent; no health promises or medical claims.
- Prices with conditions and dates; «from» prices explained.
- Cancelled classes must disappear from the screen when cancelled — keep the timetable in one source.
- Music video filler: no sound in the reception area.

## 4. Live data

| Data | Source | Mode |
|---|---|---|
| Classes today / week | iCal (Google Calendar) or Google Sheet | schedule / table as is |
| Gym load by hour | Google Sheet | table as is |
| Memberships | Google Sheet | services and prices |
| Members' wall | VK community / Telegram | card grid |
| Sports news | RSS | carousel |
| Air quality, weather, countdown | built-in widgets | — |

## 5. Cases from the PRTV template catalogue

Section «Другой бизнес» of https://s.prtv.su/shablony/katalog-shablonov:
- «Фитнес. Светлый» https://prtv.su/11420 — about the club, −50% on off-peak cards, personal trainers, hashtag photos for bonuses (Telegram), trial class with calendar, timetable table, traffic, **air quality for outdoor training**.
- «Фитнес. Тёмный» https://prtv.su/11421 — annual cards with prices permanently on screen, −40% evening cards, club zones, network addresses and hours, timetable, winter «+1 month» with countdown, newcomer offer, sports news RSS, motivation video.
- «Фитнес. Простой» https://prtv.su/11422 — four-slide starter with programmes for him and her.

Upgrade: feed the timetable from the club's calendar and prices from a sheet through «Лента» (prtv-feed-widget); add the gym-load slide.

## 6. Building it in PRTV

Start from a template or prtv-digital-signage; one slideshow on up to three screens at once is free (reception + gym + studio door).

## What not to do

- Do not type the timetable into slides — it changes weekly.
- Do not show members' photos without consent.
- Do not play motivation videos with sound at reception.
