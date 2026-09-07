# PRTV Constructor Skills for AI agents

Open, reusable skills that teach an AI agent (Claude, Codex, Gemini CLI, Cursor or any tool that reads the Agent Skills format) how to work in the **PRTV** digital-signage editor — https://prtv.pro — the way a person does: through the interface, reading the page state when needed, never through private APIs.

Each skill is a folder with `SKILL.md` (English) and `SKILL.ru.md` (Russian). The Russian file is not a byte-for-byte translation but the same material written naturally.

**How to use**

- Claude Code / Codex / Gemini CLI / Cursor: copy the folders you need into your project's `skills/` (or `.claude/skills/`) directory — the YAML header tells the agent when to load each one. Start with `prtv-editor-overview`.
- Any chat assistant: paste the raw `SKILL.md` (or `SKILL.ru.md`) into the conversation, or give the agent the raw file URL.
- Clone everything: `git clone https://github.com/prtvbiz-design/prtv-skills.git`

License: CC-BY-4.0. Product: PRTV (prtv.pro), cloud editor for menu boards, promo screens and info channels on Smart TVs, set-top boxes and browsers. Everything in these files was verified in the browser on real builds; where something was not verified, the text says so.

## The set

Load **prtv-editor-overview** first; the others assume it.

| Skill | What it covers | Load when |
|---|---|---|
| **prtv-editor-overview** | Slideshow → slide → element, the 1920×1080 space, URLs, panels, DOM conventions, fonts, uploads, TV slots, watermark | any task in the editor |
| **prtv-slide-settings** | Slide strip and its hover buttons, reordering, duration, 15 transitions, progress bar, background (colour / image / video), element defaults, templates, «Apply to all» | adding, configuring or checking a slide |
| **prtv-element-layout** | Position and size by dragging, rotation, depth, keep-aspect, permanent elements, the 7-item right-click menu, 57 entrance presets, clickable links for kiosks, layout rules (safe zone, type sizes, contrast, motion) | moving, layering, animating, linking an element; checking composition |
| **prtv-text-element** | Native text through TinyMCE: entering edit mode, toolbar, what persists and what is lost, the triple-click trap on menu rows, Ctrl+A replacement, quirks | writing or restyling text; text edits disappearing |
| **prtv-html-block-animation** | HTML block, CSS keyframes, SVG filters and SMIL without JavaScript, layers, ticker, recipes (banner behind a plane, TV static, wind, drift) | steam, shine, wind, looping effects; animating native text |
| **prtv-video** | Video element (YouTube, VK, Kinescope, Vimeo, own files), background video, embeds through HTML, sound on TVs, seamless-loop requirements | putting video on a slide or as a background |
| **prtv-widgets** | Widgets (informers): two ways to add, the three universal URL rules, parameter naming, two-level transparency, sizing fluid widgets, dependency risks, acceptance | any clock, weather, calendar, QR, countdown, finance, promo, map or social widget |
| **prtv-widgets-catalog** | Per-widget reference: builders, files, views, parameters, limitations, embeds — clocks, weather, countdown, QR, calendars, rates, promo card, moon, holidays, work-day, maps, TV programme, radio, timetable, poll, cloud feed, Yandex widgets, social feeds, RSS | building or reading a specific widget URL |
| **prtv-agent-rules** | Zero screenshots, computed coordinates, edits only through the interface, verification by reload and preview, JavaScript-tool traps, hover-only controls, slide activation, element timing, session pacing | the start of any automated session |

## Format

Every `SKILL.md` starts with a YAML header in the Agent Skills format:

```yaml
---
name: prtv-<name>
description: what it covers and when to load it
license: CC-BY-4.0
metadata:
  product: PRTV (prtv.pro) digital signage editor
  version: "1.0"
  date: "YYYY-MM-DD"
  language: en | ru
  scope: editor UI + reading page state from DOM; no private API calls
---
```

The body is a short introduction, numbered sections, a "What not to do" list and a "Related" line naming the neighbouring skills.

## Scope

In: everything visible and doable through the editor interface; reading the page state (element ids, geometry, depth, active slide) with JavaScript; the public widget builders on s.prtv.su and their parameters; emulating input into interface fields.

Out: the editor's private server methods, internal data-field names not visible in the interface, identifiers of any real project, and how to generate images or video with AI. A skill about producing menu-board graphics with AI is a separate publication.

## Links

- Editor: https://prtv.pro
- Widget builders: https://s.prtv.su/informery
- This set on GitHub: https://github.com/prtvbiz-design/prtv-skills
- Raw files: `https://raw.githubusercontent.com/prtvbiz-design/prtv-skills/main/<skill>/SKILL.md`
