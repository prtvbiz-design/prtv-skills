---
name: auto-service-signage
description: Plans screens for car washes, car service stations (waiting room) and filling stations — price by body type, extra services, order status by ticket, promotions with countdown, cross-sell of coffee and snacks, fuel price board, station services, route weather and traffic, local-history slides for drivers, news to pass the wait, reviews; with slide plans, live data from Google Sheets and feeds, and ready PRTV templates to start from. Use when someone needs a TV screen for a car wash, auto service waiting area, tyre service, detailing studio or gas station shop. Triggers (RU) экран для автомойки, телевизор в зале ожидания автосервиса, СТО, шиномонтаж, АЗС экран, стела цен на топливо, прайс автомойки на экран.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: digital-signage-content, signage-screen-design, signage-widgets, prtv-feed-widget
---

# Screens for car washes, service stations and filling stations

The viewer is almost always «stuck»: 15–40 minutes at a car wash, 30–90 at a service station, 3–5 minutes in a filling-station shop. The screen has time to inform, entertain and sell — and nothing to do but that.

## 1. Car wash / detailing — loop (8–10 slides, 15–20 s each)

1. Wash prices by body type (sedan/hatch, estate/coupé, crossover/minivan, SUV, van/bus) — **Google Sheet → price list**.
2. Extra services: interior cleaning, odour removal, body polish, glass and headlight polish, wax, tyre blackening; «today −10%».
3. Promotion with conditions and end date + countdown timer.
4. Subscription / loyalty card: «every 6th wash free», cashback, QR to join.
5. Order status by ticket number (no plates, no names) — **sheet, «table as is»**, filled by the operator.
6. «May come in handy»: coffee to go, snacks, washer fluid, wipes, phone holders — mini-shop with prices.
7. Weather and traffic: «rain tomorrow — anti-rain coating −20%» (weather as a reason to buy).
8. Car news or short videos to pass the wait (RSS of car media, own VK/Telegram).
9. Review: «How was it?» + QR to maps.

## 2. Service station (waiting room) — loop (10–11 slides)

Status by ticket · price list and what the service includes · promotion #1 · car news (RSS) · own community posts · video about the workshop or maintenance tips · weather + traffic + clock · Wi-Fi QR · promotion #2 · review QR · optional «how car acceptance works» for new clients. Show warranty terms and the operator's details (legal entity, contacts for claims) — in Russia the rules for car maintenance services require prices, list of services and warranty information before the contract.

## 3. Filling station shop — loop (≈ 12 slides, 15–20 s)

Permanent: **fuel price board** (92/95/98/diesel/LPG/CNG) — from a sheet the operator updates in one place; clock; phone; site.
Slides: weather in cities along the route · loyalty card discount · traffic and the station's km mark · station services (café, shop, pharmacy, self-service wash, Wi-Fi, toilet, free tyre inflation, vacuum) · «coffee −20% before 11:00» · car wash video · **local-history slides** («you are on the old Vladimirka road», a museum 10 km away, a relic lake 10 minutes' drive) — the strongest idea in the category: it makes a stop memorable and gives a reason to come back.

## 4. Live data

| Data | Source | Mode |
|---|---|---|
| Prices, extras, mini-shop | Google Sheet | services and prices |
| Order status | Google Sheet, ticket № + stage | table as is |
| Fuel prices | Google Sheet | table as is |
| Car news | RSS of car media, Google News «ПДД», «автомобили» | carousel |
| Own news | VK community / Telegram | carousel / card grid |
| Weather, traffic, clock | built-in widgets | — |
| Promotion end | countdown widget | — |

## 5. Rules

- No car plates or client names on screen; ticket numbers only.
- No exact repair times unless synchronised with the workshop.
- Wi-Fi password only as a QR code, not as open text.
- Prices with «valid on <date>»; promotions with an end date — old dates (e.g. «until 29 December 2023» left in a template) destroy trust.
- Other brands' logos only with permission.

## 6. Cases from the PRTV template catalogue

Free templates to take and adapt (https://s.prtv.su/shablony/katalog-shablonov, section «Автомойки»):
- «Автомойка. Кристаллы чистоты» https://prtv.su/11433 — prices, extras, traffic, promo with ticker, VK, cross-sell of coffee from the café next door, review QR, accessories with countdown.
- «Автомойка. С постоянным видео» https://prtv.su/11428 — video background, «may come in handy» snacks and mini-shop with timer.
- «Автомойка. Часы на стене» https://prtv.su/11432 — analogue clock, radio, calendar.
- «Автомойка. Красно-белая инфографика» https://prtv.su/11430 — adds engine services (plugs, filters, diagnostics).
- «Автомойка. За рулём» https://prtv.su/11429 — road videos, radio, neon clock, Free Wi-Fi and snacks.
- «АЗС» https://prtv.su/11417 — fuel board, route weather in four cities, station services, local-history slides.

Upgrade these templates by moving typed prices into a Google Sheet (prtv-feed-widget) and replacing old promotion dates.

## 7. Building it in PRTV

Take a template above or start from scratch (prtv-digital-signage). One slideshow runs on up to three screens at once on the free first licence — enough for a waiting room plus a cashier screen. Clocks, weather, traffic, countdown — built-in and https://s.prtv.su/informery; prices, status and news — «Лента».

## What not to do

- Do not show plates, names or personal data.
- Do not leave demo prices («500 ₽» everywhere) or expired promotions.
- Do not run several moving elements on one slide; the viewer is sitting close.
