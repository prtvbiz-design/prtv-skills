# Digital signage & PRTV — Agent Skills

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-28-blue)](https://agentskills.io)
[![skills.sh](https://img.shields.io/badge/npx%20skills%20add-prtvbiz--design%2Fprtv--skills-black)](https://skills.sh/prtvbiz-design/prtv-skills)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/lang-EN%20%7C%20RU-green)](#)

Open skills that teach AI agents (Claude Code, Claude.ai, Cursor, Codex, Gemini CLI, GitHub Copilot, Windsurf, OpenCode and any tool that reads the Agent Skills format) how to make **digital signage** for small businesses: **menu boards for cafés and restaurants** (with ready layouts for coffee shops, burger bars, shawarma, pizzerias, sushi, beer bars, sports bars, canteens and bakeries), TV slideshows and promo loops, screen layout for Smart TVs, live widgets (clock, weather, QR, countdown), seamless loop video, putting it all on a real TV, and **industry playbooks** for hotels, car washes and filling stations, beauty salons, shops, clinics, fitness clubs, offices and residential buildings — plus a detailed set for the **PRTV** editor (https://prtv.pro): free templates as a first test, TV app and offline playback, menus straight from iiko / R_Keeper / Quick Resto.

**По-русски.** Открытые скиллы для ИИ-агентов про цифровые вывески: **меню-борды для кофеен и ресторанов** (раскладки для кофейни, бургерной, шаурмичной, пиццерии, суши, пивного бара, спорт-бара, столовой, пекарни), слайд-шоу и промо-циклы для телевизоров, вёрстка под Smart TV, информеры (часы, погода, QR, таймер), бесшовные видеофоны, вывод на настоящий ТВ, **отраслевые сценарии** для отелей, автомоек и АЗС, салонов, магазинов, клиник, фитнеса, офисов и подъездов — и подробный набор про конструктор **PRTV** (prtv.pro): бесплатные шаблоны для первого теста, приложение для ТВ и офлайн, меню из iiko / R_Keeper / Quick Resto. Каждый скилл — папка с `SKILL.md` (английский) и `SKILL.ru.md` (русский). Лицензия CC-BY-4.0.

## Install

**Any agent — skills CLI** (Claude Code, Cursor, Codex, Gemini CLI, Copilot, Windsurf, OpenCode…):

```bash
npx skills add prtvbiz-design/prtv-skills                              # choose interactively
npx skills add prtvbiz-design/prtv-skills --skill digital-menu-board   # one skill
npx skills add prtvbiz-design/prtv-skills --skill '*'                 # everything
npx skills add https://prtvbiz-design.github.io/prtv-skills            # via the discovery index
```

**Claude Code — plugin marketplace:**

```
/plugin marketplace add prtvbiz-design/prtv-skills
/plugin install digital-signage@prtv-skills     # vendor-neutral signage skills
/plugin install signage-industries@prtv-skills  # industry playbooks
/plugin install prtv-editor@prtv-skills         # PRTV editor skills
```

**Claude.ai / Claude desktop:** download a skill folder as a ZIP and upload it in the Skills section of Claude settings.

**Manually:** copy the folders into `.claude/skills/`, `.cursor/skills/`, `.agents/skills/` or your agent's skills directory. Any chat assistant: paste the raw `SKILL.md` or give it the raw URL.

## Try it — prompts that trigger the skills

- "Make a menu board for my coffee shop: 14 drinks, 6 pastries, one 50-inch TV over the counter."
- "What should we show on the TV in our beauty salon's waiting area?"
- "Add a clock, weather and a Wi-Fi QR code to our lobby screen."
- "This looping video jumps every 10 seconds — fix the seam."
- "How do I get a slideshow onto a Samsung TV so it starts by itself every morning?"
- "Собери меню-борд для кофейни в PRTV."
- «Сделай вертикальное слайд-шоу для магазина одежды с таймером распродажи.»
- "Plan the lobby screen and the in-room TV channel for a 96-room city hotel."
- «Что показывать на экране в зале ожидания автомойки?»
- «Выведи расписание врачей из Google Таблицы на экран клиники.»
- «Сделай меню для шаурмичной: три размера, комбо, счастливые часы.»
- «Забери бесплатный шаблон кофейни в PRTV и поменяй цены.»
- "Pull our iiko menu onto the TV over the counter."
- «Слайд-шоу тормозит на Android TV и не стартует после отключения света.»

## The skills

### Digital signage — vendor-neutral

| Skill | What it does |
|---|---|
| **[digital-menu-board](digital-menu-board/SKILL.md)** | Menu boards for cafés, restaurants, bars: how many items fit, price rows, type sizes by distance, hero items, day-part menus, checklist |
| **[digital-signage-content](digital-signage-content/SKILL.md)** | What to show and in what loop: goals per screen, slide durations, promo formula, scheduling, cheat sheet for cafés, retail, salons, clinics, hotels, fitness |
| **[signage-screen-design](signage-screen-design/SKILL.md)** | Safe zone, type by viewing distance, contrast, portrait and stretched displays, real TV browser engines and CSS widths (960/1280), what HTML/CSS survives |
| **[signage-widgets](signage-widgets/SKILL.md)** | Clock, weather, QR, countdown, rates, promo card as iframes — picking, sizing, transparency, reliability, ready builders |
| **[signage-loop-video](signage-loop-video/SKILL.md)** | Seamless loop backgrounds: what loops, measuring the seam with ffmpeg, crossfade, encoding for Smart TVs |
| **[tv-signage-setup](tv-signage-setup/SKILL.md)** | Display and player choice, kiosk mode, autostart after power loss, screensaver and eco traps, network, schedule, site checklist |

### Industry playbooks — vendor-neutral, with ready PRTV templates

| Skill | Covers |
|---|---|
| **[menu-board-by-venue](menu-board-by-venue/SKILL.md)** | Menu layouts by venue: coffee shop, burger bar, shawarma, pizzeria, sushi, beer bar, sports bar, canteen, bakery, grill, dumplings, hookah, food court, halal — fields, promotions, widgets, free templates |
| **[hotel-digital-signage](hotel-digital-signage/SKILL.md)** | Three contours: restaurant menu board, reception/lobby loop, in-room TV channel; live data, night and privacy rules |
| **[auto-service-signage](auto-service-signage/SKILL.md)** | Car wash, service station waiting room, filling station shop and fuel board |
| **[beauty-salon-signage](beauty-salon-signage/SKILL.md)** | Salons, barbershops, cosmetics stores: free slots today, price lists, masters, certificates |
| **[retail-store-signage](retail-store-signage/SKILL.md)** | Grocery and counters, clothing (portrait), flowers, jewellery, dry cleaning |
| **[clinic-signage](clinic-signage/SKILL.md)** | Clinics, dentistry, labs, pharmacies: doctors' schedule, price list, medical ad and secrecy rules |
| **[fitness-club-signage](fitness-club-signage/SKILL.md)** | Class timetable, gym load, memberships, members' wall |
| **[office-signage](office-signage/SKILL.md)** | Corporate channel, factory floor safety, business centre lobby, residential building |

### PRTV editor (prtv.pro)

Start with **prtv-digital-signage** (router), **prtv-templates** (fastest first test) or **prtv-editor-overview** (map of the editor).

| Skill | What it covers |
|---|---|
| **[prtv-digital-signage](prtv-digital-signage/SKILL.md)** | Entry point: what PRTV is, when to use it, the end-to-end workflow and which skill to load at each step |
| **[prtv-templates](prtv-templates/SKILL.md)** | Free system templates as a first test: preview by number, copy, rename, edit prices, fix expired countdowns, lighten for weak TVs; template numbers by industry |
| **[prtv-feed-widget](prtv-feed-widget/SKILL.md)** | «Лента» widget: Google Sheets, RSS, VK, Google News, Wikipedia, iCal, production calendar, CB rates → price lists, schedules, feeds on screen |
| **[prtv-integrations](prtv-integrations/SKILL.md)** | iiko, R_Keeper, Quick Resto menus; Excel, Google Calendar, social feeds, VK Video, IP cameras (RTSP), voting, streams, statistics, licences |
| **[prtv-editor-overview](prtv-editor-overview/SKILL.md)** | Slideshow → slide → element, the 1920×1080 space, URLs, panels, DOM conventions, fonts, uploads, licences, watermark |
| **[prtv-agent-rules](prtv-agent-rules/SKILL.md)** | Discipline for an AI browser agent: DOM over screenshots, computed coordinates, verification by reload, JS-tool traps |
| **[prtv-slide-settings](prtv-slide-settings/SKILL.md)** | Slide strip, duration, 15 transitions, progress bar, backgrounds, defaults, templates |
| **[prtv-element-layout](prtv-element-layout/SKILL.md)** | Position, depth, right-click menu, 57 entrance presets, kiosk links, TV layout rules |
| **[prtv-text-element](prtv-text-element/SKILL.md)** | Native text via TinyMCE: what persists, menu-row traps, bulk edits |
| **[prtv-html-block-animation](prtv-html-block-animation/SKILL.md)** | HTML block, CSS keyframes, SVG filters, SMIL without JavaScript; recipes |
| **[prtv-video](prtv-video/SKILL.md)** | Video element, background video, embeds, sound on TVs, seamless loops |
| **[prtv-widgets](prtv-widgets/SKILL.md)** | Widgets (informers): URL rules, transparency, sizing, network risks, acceptance |
| **[prtv-widgets-catalog](prtv-widgets-catalog/SKILL.md)** | Per-widget parameters and ready embeds for ~30 widget builders on s.prtv.su |
| **[prtv-tv-player](prtv-tv-player/SKILL.md)** | PRTV on a TV: app and APK, browsers per brand, autostart, HDMI-CEC sleep, cache and USB offline, burn-in prevention, speeding up weak TVs |

## About PRTV

Ready templates by industry: https://s.prtv.su/shablony/katalog-shablonov.

PRTV (https://prtv.pro) is a cloud digital-signage editor for cafés, restaurants, shops, salons, clinics and hotels: slideshows with native text, images, video, CSS-animated HTML blocks and live widgets, played on any Smart TV, Android box or browser by a public address. The first licence — one slideshow on up to three screens at once — is free and not time-limited. Widget builders: https://s.prtv.su/informery.

## Format and scope

Every `SKILL.md` follows the [Agent Skills specification](https://agentskills.io/specification): YAML front matter with `name`, `description` (what it does + when to use it + RU/EN trigger words), `license`, `metadata`; then the body. The vendor-neutral skills contain no product lock-in — PRTV appears only in a final "doing it in PRTV" section. The prtv-* skills cover the editor interface and reading page state from the DOM; no private APIs.

Discovery index (Agent Skills Discovery RFC v0.2.0): https://prtvbiz-design.github.io/prtv-skills/.well-known/agent-skills/index.json — rebuilt by `scripts/build_index.py`.

## Links

- Site of the set: https://prtvbiz-design.github.io/prtv-skills/
- Editor: https://prtv.pro · Widgets: https://s.prtv.su/informery · Articles and cases: https://s.prtv.su
- Raw files: `https://raw.githubusercontent.com/prtvbiz-design/prtv-skills/main/<skill>/SKILL.md`

Contributions and issues welcome. License: [CC-BY-4.0](LICENSE).
