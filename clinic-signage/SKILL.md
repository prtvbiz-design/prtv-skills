---
name: clinic-signage
description: Plans screens for clinics, dental clinics, laboratories, pharmacies and veterinary clinics — doctors' schedule for today and the week, specialties directory, doctor cards with qualification, paid services price list, clinic map «you are here», how to book again, neutral prevention content, loyalty app, reviews, mandatory information (licence, operator details, free care under state programme) and the limits of medical advertising and medical secrecy; with slide plans, Google Sheet feeds and ready PRTV templates. Use when someone wants a TV in a clinic waiting room, dental reception, lab or pharmacy. Triggers (RU) экран в клинику, телевизор в стоматологии, расписание врачей на экран, аптека экран, лаборатория, медицинский центр digital signage, зал ожидания поликлиники.
license: CC-BY-4.0
metadata:
  author: PRTV (prtv.pro)
  version: "1.0"
  date: "2026-09-27"
  language: en
  related: digital-signage-content, signage-screen-design, prtv-feed-widget
---

# Screens for clinics, dentistry, labs and pharmacies

Patients wait 10–40 minutes, often anxious, sometimes with children. The screen informs calmly, reduces questions at the desk, helps choose a doctor and book again. It is not an advertising billboard and never a source of medical advice.

## 1. Clinic / dental waiting room loop (9–11 slides, 12–15 s)

1. **Doctors today**: specialist, room, hours — Google Sheet, «table as is»; the administrator updates it daily.
2. Specialties directory A–Z with floor/room.
3. Doctor cards: photo, specialty, experience, qualification (rotate 2–3 per cycle).
4. Paid services and prices by section — sheet → price list, «valid on <date>».
5. Clinic map «you are here».
6. How to book again: phone, QR to online booking or app.
7. Neutral prevention content: check-ups, vaccination season, oral hygiene — facts, not advice.
8. Loyalty / app: points for services, QR.
9. Events: open days, patient schools — iCal calendar.
10. Wi-Fi QR, review QR.
11. Mandatory information duplicated: operator, licence number and date, where to find the full information, availability of free care under the state guarantees programme.

Dental specifics: calmer visuals (aquarium or nature video backgrounds work well), children's zone content without sound on a separate screen, hygiene and implant information with «contraindications apply — consult a specialist».

## 2. Laboratory and pharmacy

Lab: test groups with «from» prices, «three ultrasounds for the price of one», preparation rules for tests, loyalty app. Pharmacy: branch addresses, free blood pressure/temperature measurement, app with points, seasonal discount on a category with legal wording, online reservation.

## 3. Rules — stricter than in other industries

- **Medical secrecy**: never show patient names, diagnoses, results or anything linking a person to a specialist; queue — anonymous ticket numbers only.
- **Medical advertising (Russia, law «On advertising», art. 24)**: an advertising slide about a service or method must carry a warning about contraindications and the need to consult a specialist; no guaranteed results, no pressure («don't delay»), no comparison with other clinics. Keep price lists and doctor cards informational.
- **Mandatory information** for paid medical services (price list, doctors and qualification, operator and licence, free-care programme) must be available on the stand and website all working hours; the screen duplicates it and does not replace it. Check the current government rules for paid medical services.
- No medical recommendations («what to do if…») on screen.
- Children and patients in photos or video only with documented consent.
- Wi-Fi password as QR only.
- No third-party news feeds without word filters.

## 4. Live data

| Data | Source | Mode |
|---|---|---|
| Doctors today / week | Google Sheet (specialist · room · Mon … Sun) or clinic system export | table as is |
| Paid services prices | Google Sheet | services and prices |
| Events, patient schools | iCal | schedule |
| Holiday opening hours | production calendar | calendar |
| Clock, weather | built-in widgets | — |

## 5. Cases from the PRTV template catalogue

Section «Медицинские учреждения, аптеки» of https://s.prtv.su/shablony/katalog-shablonov:
- «Медицинский центр» https://prtv.su/11435 — clinic figures, specialties directory, doctor rating cards, **schedule table**, **clinic map «you are here»**, service with video and price, flu vaccination info slide with figures, free pregnancy care under state insurance, patient reviews with QR.
- «Аптека» https://prtv.su/11436 — branches, free measurements, app with points, antiviral discount with conditions.
- «Стоматологическая клиника» https://prtv.su/11414 — services, about the clinic, implant/crown/bridge videos with prices, complex hygiene price, children's dentistry.
- «Аквариум. Стоматология» https://prtv.su/11438 and «Аквариум. Лаборатория» https://prtv.su/11439 — calm aquarium video background, points for services, price lists, «three ultrasounds for one».

Upgrade: replace typed schedules and prices with sheet feeds (prtv-feed-widget); add the mandatory-information slide; remove social elements that no longer work.

## 6. Building it in PRTV

Start from a template or prtv-digital-signage. One waiting-room screen plus a reception screen fit the free first licence (one slideshow, up to three screens at once).

## What not to do

- Do not show anything that identifies a patient.
- Do not advertise treatment without the contraindications warning.
- Do not give medical advice on screen.
