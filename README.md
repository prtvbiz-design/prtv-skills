# Digital signage & PRTV — Agent Skills

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-16-blue)](https://agentskills.io)
[![skills.sh](https://img.shields.io/badge/npx%20skills%20add-prtvbiz--design%2Fprtv--skills-black)](https://skills.sh/prtvbiz-design/prtv-skills)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/lang-EN%20%7C%20RU-green)](#)

Open skills that teach AI agents (Claude Code, Claude.ai, Cursor, Codex, Gemini CLI, GitHub Copilot, Windsurf, OpenCode and any tool that reads the Agent Skills format) how to make **digital signage** for small businesses: **menu boards for cafés and restaurants**, TV slideshows and promo loops, screen layout for Smart TVs, live widgets (clock, weather, QR, countdown), seamless loop video, and putting it all on a real TV — plus a detailed set for the **PRTV** editor (https://prtv.pro).

**По-русски.** Открытые скиллы для ИИ-агентов про цифровые вывески: **меню-борды для кофеен и ресторанов**, слайд-шоу и промо-циклы для телевизоров, вёрстка под Smart TV, информеры (часы, погода, QR, таймер), бесшовные видеофоны, вывод на настоящий ТВ — и подробный набор про конструктор **PRTV** (prtv.pro). Каждый скилл — папка с `SKILL.md` (английский) и `SKILL.ru.md` (русский). Лицензия CC-BY-4.0.

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

### PRTV editor (prtv.pro)

Start with **prtv-digital-signage** (router) or **prtv-editor-overview** (map of the editor).

| Skill | What it covers |
|---|---|
| **[prtv-digital-signage](prtv-digital-signage/SKILL.md)** | Entry point: what PRTV is, when to use it, the end-to-end workflow and which skill to load at each step |
| **[prtv-editor-overview](prtv-editor-overview/SKILL.md)** | Slideshow → slide → element, the 1920×1080 space, URLs, panels, DOM conventions, fonts, uploads, licences, watermark |
| **[prtv-agent-rules](prtv-agent-rules/SKILL.md)** | Discipline for an AI browser agent: DOM over screenshots, computed coordinates, verification by reload, JS-tool traps |
| **[prtv-slide-settings](prtv-slide-settings/SKILL.md)** | Slide strip, duration, 15 transitions, progress bar, backgrounds, defaults, templates |
| **[prtv-element-layout](prtv-element-layout/SKILL.md)** | Position, depth, right-click menu, 57 entrance presets, kiosk links, TV layout rules |
| **[prtv-text-element](prtv-text-element/SKILL.md)** | Native text via TinyMCE: what persists, menu-row traps, bulk edits |
| **[prtv-html-block-animation](prtv-html-block-animation/SKILL.md)** | HTML block, CSS keyframes, SVG filters, SMIL without JavaScript; recipes |
| **[prtv-video](prtv-video/SKILL.md)** | Video element, background video, embeds, sound on TVs, seamless loops |
| **[prtv-widgets](prtv-widgets/SKILL.md)** | Widgets (informers): URL rules, transparency, sizing, network risks, acceptance |
| **[prtv-widgets-catalog](prtv-widgets-catalog/SKILL.md)** | Per-widget parameters and ready embeds for ~30 widget builders on s.prtv.su |

## About PRTV

PRTV (https://prtv.pro) is a cloud digital-signage editor for cafés, restaurants, shops, salons, clinics and hotels: slideshows with native text, images, video, CSS-animated HTML blocks and live widgets, played on any Smart TV, Android box or browser by a public address. The first licence — one slideshow on up to three screens at once — is free and not time-limited. Widget builders: https://s.prtv.su/informery.

## Format and scope

Every `SKILL.md` follows the [Agent Skills specification](https://agentskills.io/specification): YAML front matter with `name`, `description` (what it does + when to use it + RU/EN trigger words), `license`, `metadata`; then the body. The vendor-neutral skills contain no product lock-in — PRTV appears only in a final "doing it in PRTV" section. The prtv-* skills cover the editor interface and reading page state from the DOM; no private APIs.

Discovery index (Agent Skills Discovery RFC v0.2.0): https://prtvbiz-design.github.io/prtv-skills/.well-known/agent-skills/index.json — rebuilt by `scripts/build_index.py`.

## Links

- Site of the set: https://prtvbiz-design.github.io/prtv-skills/
- Editor: https://prtv.pro · Widgets: https://s.prtv.su/informery · Articles and cases: https://s.prtv.su
- Raw files: `https://raw.githubusercontent.com/prtvbiz-design/prtv-skills/main/<skill>/SKILL.md`

Contributions and issues welcome. License: [CC-BY-4.0](LICENSE).
