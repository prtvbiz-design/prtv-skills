---
name: retail-store-signage
description: Plans screens for shops — grocery and convenience stores, butcher, fish, dairy, bakery, drinks, clothing and shoe stores (incl. portrait window screens), flower shops, jewellery, dry cleaning — promotions of the week with countdown, price of the day, new arrivals, recipes for promoted goods, delivery and loyalty card, store load and queue call-back, vacancies, holiday opening hours, seasonal occasions calendar; with slide plans, Google Sheet feeds and ready PRTV templates. Use when someone wants a TV at the checkout, in the window or on the sales floor of a store. Triggers (RU) экран в магазин, телевизор у кассы, витрина экран, магазин одежды вертикальный экран, продуктовый магазин акции на экран, цветочный магазин, ювелирный, химчистка экран.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: digital-signage-content, signage-screen-design, signage-loop-video, prtv-feed-widget
---

# Screens for shops

Three places, three jobs: the **window** brings people in (one offer, readable from 8–10 m, often portrait), the **floor** sells a category or a product next to it, the **checkout** adds one more item and informs (card, delivery, vacancies).

## 1. Grocery / convenience — checkout and floor loop (10–13 slides, 10–15 s)

1. Promotion of the week: product, price, «1+1», end date + countdown — **Google Sheet → carousel** so the manager changes it without the editor.
2. Price of the day / best price on a basic product.
3. New arrival.
4. **Recipe** for the promoted product (video or 3 steps) — turns a discount into a basket.
5. **Store load now / by hour** (high / medium / low) — shoppers choose quiet hours.
6. «More than 5 people in the queue? Call …» — service promise.
7. Delivery in 60 minutes + first-order discount.
8. Loyalty card: how to get it, points.
9. **Vacancies** with schedule and salary — the cheapest recruitment channel a chain has (sheet → carousel).
10. Addresses of other stores, opening hours; **holiday hours** from the production calendar.
11. Weather + clock.

Specialised counters: fish (price per kg, fresh/chilled/frozen, «interesting facts», cutting scheme, recipes), dairy (1+1, recipe of pancakes, new product), bakery (composition, «buy 3 — 4th free», reviews), drinks.

## 2. Clothing and shoes (portrait screens)

Window and fitting-area screens are usually portrait. Plan: lookbook of the new collection (full-height photos, one outfit per slide, price), sale countdown, size and fit tips, «complete the look» cross-sell, QR to the online store and to reserve a size, loyalty. Design at the panel's native resolution (e.g. 1080×1920 or stretched 1488×3840), never a rotated landscape layout. See signage-screen-design.

## 3. Flower shop — the calendar of occasions

The strongest content idea in retail: build the year around occasions and pre-orders. Slides: «language of flowers», popular bouquets with prices, delivery («whatever the traffic, the bouquet arrives on time» — traffic widget as an argument; «fresh flowers in any weather» — weather widget), «no reason needed» with a calendar, wedding bouquet, **New Year countdown for gifts with growing discount**, 8 March pre-order −20% with a deadline, Valentine's Day, tulips by the piece, workshop, gift wrapping how-to.

## 4. Jewellery and dry cleaning

Jewellery: one piece per slide with metal, hallmark, weight, stone and price; «hit»; set −30% with countdown; video. Dry cleaning / laundry: price list per item, «price of the week» with timer, «−20% from 3 items», detergents on sale, loyalty, useful video tips, review.

## 5. Live data

| Data | Source | Mode |
|---|---|---|
| Promotions, price of the day | Google Sheet (title, price, old price, valid till, picture) | carousel / free layout |
| Price lists (dry cleaning, flowers) | Google Sheet | services and prices |
| Store load by hour | Google Sheet | table as is |
| Vacancies | Google Sheet | carousel |
| Holiday opening hours | production calendar + sheet | calendar / carousel |
| Store news | VK community | card grid |
| Countdown to promo end / holiday | countdown widget | — |

## 6. Rules

- Price on screen = price on the shelf tag and at the till; promotions with dates.
- Alcohol and tobacco: no advertising on screens in Russia beyond what the law allows — keep to assortment and price information, check with a lawyer.
- Photos of real products; product photos from suppliers only with rights.

## 7. Cases from the PRTV template catalogue

Section «Продуктовые магазины»: «SHOP-Red» https://prtv.su/11448 (also «SHOP-Green» https://prtv.su/11449 and «SHOP-Yellow» https://prtv.su/11451) — recipe video, 1+1 with timer, **store load**, delivery, loyalty card, traffic, **vacancies**, queue call-back, addresses; counters — butcher https://prtv.su/11440, fish https://prtv.su/11441, dairy https://prtv.su/11462, bakery https://prtv.su/11467 and others in the section. Section «Другой бизнес»: flower boutique https://prtv.su/11423 (19 slides, occasions calendar), jewellery https://prtv.su/93486, dry cleaning https://prtv.su/84650.

## 8. Building it in PRTV

Take a template (s.prtv.su/shablony/katalog-shablonov) or start with prtv-digital-signage; move promotions and prices to a sheet via «Лента» (prtv-feed-widget). Portrait and custom canvases are set in the slideshow settings. One slideshow on up to three screens at once is free.

## What not to do

- Do not leave template demo prices or last year's dates.
- Do not rotate the window screen faster than a passer-by can read one offer.
- Do not put a landscape layout on a portrait window screen.
