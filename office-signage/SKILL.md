---
name: office-signage
description: Plans screens for offices, corporate TV channels, factories and warehouses, business centres, co-working spaces and residential building lobbies (management company channel) — company news, KPIs and shift schedules, birthdays and employee of the month, canteen menu, safety rules, evacuation and first aid, production calendar, business news and rates, events and meeting rooms, tenant directory, outages and announcements for residents, paid ad slots; with slide plans, Google Sheet and calendar feeds and ready PRTV templates. Use when someone wants an internal company TV channel, a factory floor screen, a business centre lobby display or a screen in an apartment building entrance. Triggers (RU) корпоративный телеканал, экран в офис, экран на производство, охрана труда на экране, бизнес-центр экран, информационный экран в подъезде, управляющая компания экран, именинники на экране.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: digital-signage-content, signage-screen-design, prtv-feed-widget
---

# Screens for offices, factories, business centres and residential buildings

The same people pass the screen every day. It must change daily or it disappears. The rule: at least one slide in the loop carries today's data (menu, shift, birthdays, events, outages).

## 1. Office / corporate channel loop (10–14 slides, 10–15 s)

Permanent: logo, clock, weather, exchange rates.
1. Company news (sheet or company VK/Telegram).
2. Figures and goals of the quarter.
3. **Birthdays today** and **employee of the month** — sheet → carousel.
4. Team: new colleagues, department of the week.
5. Canteen **menu today** with prices — sheet → price list.
6. Events: training, corporate events, conference countdown — iCal / countdown.
7. **Production calendar** of the month (working days and holidays).
8. «Work day ends in …» countdown on Fridays — optional, light.
9. Business news (RSS of business media) and rates — short.
10. Traffic before leaving time.
11. Safety reminder of the week.

## 2. Factory / warehouse floor

Large type, high contrast, readable from 5–10 m. Slides: shift schedule (table), KPIs of the shift/line, **safety rules**, PPE reminder, fire safety and **evacuation plan**, **first aid scheme**, sanitary rules at entry to clean zones, canteen menu, birthdays, employee of the month, company products. Safety slides — static, no animation, text approved by the safety officer.

## 3. Business centre lobby

What most business-centre templates miss: **tenant directory by floor** (sheet «table as is»), events in the conference halls today (iCal), building news and works («lift 2 closed 10–12» — one-row announcement), taxi and traffic, weather, lunch offers of the ground-floor cafés (paid slots for tenants), QR to the building's app or help desk. Business news and market indices are fillers, not the core.

## 4. Residential building / management company

Permanent: management company phone, site, building address, calendar.
Slides: welcome; management company details; service contacts (water, heating, lifts, intercom, CCTV); **outages and works** (sheet → first slide while active); meetings of owners; payment reminder; annual maintenance costs table; waste and bulky-waste rules; congratulations to residents; useful services (electrician, plumber); **paid ad slots** for local businesses (monetises the screen); evacuation plan. 10 s per slide — residents pass by.

## 5. Live data

| Data | Source | Mode |
|---|---|---|
| Birthdays, employee of the month, news | Google Sheet | carousel / free layout |
| Canteen menu | Google Sheet | services and prices |
| Shift schedule, KPIs, tenant directory | Google Sheet | table as is |
| Events, meeting rooms, owners' meetings | iCal / Google Calendar | schedule |
| Working days | production calendar | calendar |
| Rates | Central Bank rates | rate table |
| Business news | RSS / Google News by industry keyword | carousel |
| Outages, urgent notices | Google Sheet, one row | carousel / ticker |

## 6. Rules

- Personal data: birthdays with the employee's consent (name and department, no dates of birth with year); KPIs by team or line, not by named person, unless the company policy allows.
- Safety, evacuation and first-aid texts come from the responsible officer; the screen duplicates the posted plans.
- In residential buildings, advertising slots follow the house owners' decision and advertising law.

## 7. Cases from the PRTV template catalogue

- «Производство» https://prtv.su/37859 — 17 slides: about the company, documents, news, employee of the month, birthdays, productivity table, shift schedule, evacuation plan, first aid, canteen menu, labour safety, fire safety, sanitary rules, products, partners.
- «Корпоративный канал» https://prtv.su/11415 — company figures, principles, team, «work day ends in» timer, precious metals, traffic, business news RSS, Telegram, conference countdown.
- «Бизнес-центр» https://prtv.su/11419 — business news, market indices, traffic, weather (add a tenant directory and building events).
- «Подъезд» https://prtv.su/11711 — 17 slides for residents: management company, service contacts, maintenance costs, notices, outages, congratulations, ad slots, evacuation.

Upgrade: move birthdays, menus, schedules and notices to sheets via «Лента» (prtv-feed-widget); add the production calendar.

## 8. Building it in PRTV

Start from a template or prtv-digital-signage. Several floors or entrances with the same content — one slideshow; the free first licence covers up to three screens at once, more screens need licences for simultaneous showing.

## What not to do

- Do not run a static corporate loop — nobody reads it after a week.
- Do not publish personal data beyond what employees agreed to.
- Do not animate safety and evacuation slides.
