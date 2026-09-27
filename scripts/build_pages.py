#!/usr/bin/env python3
"""Regenerate llms.txt and index.html (landing page) from SKILL.md headers."""
import html, json, pathlib, yaml
root = pathlib.Path(__file__).resolve().parent.parent
B = "https://prtvbiz-design.github.io/prtv-skills"
R = "https://raw.githubusercontent.com/prtvbiz-design/prtv-skills/main"
G = "https://github.com/prtvbiz-design/prtv-skills/blob/main"
GEN = ["digital-menu-board", "digital-signage-content", "signage-screen-design", "signage-widgets", "signage-loop-video", "tv-signage-setup"]
IND = ["menu-board-by-venue", "hotel-digital-signage", "auto-service-signage", "beauty-salon-signage", "retail-store-signage", "clinic-signage", "fitness-club-signage", "office-signage"]
PRTV = ["prtv-digital-signage", "prtv-templates", "prtv-feed-widget", "prtv-integrations", "prtv-editor-overview", "prtv-agent-rules", "prtv-slide-settings", "prtv-element-layout", "prtv-text-element", "prtv-html-block-animation", "prtv-video", "prtv-widgets", "prtv-widgets-catalog", "prtv-tv-player"]
ARTICLE = "https://s.prtv.su/otraslevye-resheniya/kak-sdelat-menyu-bord-dlya-kofejni-neyrosetyu"
def d(n, f="SKILL.md"): return yaml.safe_load((root / n / f).read_text().split("---")[1])["description"]
def short(s): return s.split(" Use ")[0].split(" Использовать")[0]

L = ["# Digital signage & PRTV — Agent Skills", "",
     "> Open Agent Skills (CC-BY-4.0, English + Russian) that teach AI agents to make digital signage for small businesses — menu boards, TV slideshows, screen design for Smart TVs, live widgets, seamless loop video, TV setup, industry playbooks (hotels, car washes and filling stations, beauty salons, shops, clinics, fitness clubs, offices, residential buildings) — and to build it in PRTV (prtv.pro), a cloud digital-signage editor whose first licence (one slideshow on up to three screens) is free.", "",
     f"Install with `npx skills add prtvbiz-design/prtv-skills` or, in Claude Code, `/plugin marketplace add prtvbiz-design/prtv-skills`. Discovery index: {B}/.well-known/agent-skills/index.json", ""]
for title, lst in (("Digital signage skills (vendor-neutral)", GEN), ("Industry playbooks", IND), ("PRTV editor skills (prtv.pro)", PRTV)):
    L += [f"## {title}", ""]
    for n in lst:
        L.append(f"- [{n}]({R}/{n}/SKILL.md): {short(d(n))}")
        L.append(f"- [{n} (RU)]({R}/{n}/SKILL.ru.md): {short(d(n, 'SKILL.ru.md'))}")
    L.append("")
L += ["## Product", "",
      "- [PRTV editor](https://prtv.pro): account, slideshow list, editor at /slideshow/<id>, public player at /<TV-number>",
      "- [Template catalogue](https://s.prtv.su/shablony/katalog-shablonov): ready slideshows by industry, each playable at prtv.su/<number>",
      "- [Widget builders](https://s.prtv.su/informery): public builders — clocks, weather, calendars, QR, countdown, rates, promo cards, maps and more",
      "", "## Articles", "",
      f"- [Как сделать меню-борд для кофейни с помощью нейросетей: три кейса (RU)]({ARTICLE}): three coffee-shop menu boards built with AI in PRTV",
      "", "## Optional", "",
      "- [Skill set on GitHub](https://github.com/prtvbiz-design/prtv-skills)",
      "- [Feed](https://s.prtv.su/feed): RSS of s.prtv.su", ""]
(root / "llms.txt").write_text("\n".join(L))

def cards(lst):
    o = []
    for n in lst:
        o.append(f'<article class="card" id="{n}"><h3><code>{n}</code></h3>\n<p>{html.escape(short(d(n)))}</p>\n<p class="ru" lang="ru">{html.escape(short(d(n, "SKILL.ru.md")))}</p>\n<p class="links"><a href="{n}/SKILL.md">SKILL.md (EN)</a> · <a href="{n}/SKILL.ru.md">SKILL.ru.md (RU)</a> · <a href="{G}/{n}">GitHub</a> · <code class="cmd">npx skills add prtvbiz-design/prtv-skills --skill {n}</code></p></article>')
    return "\n".join(o)
ld = {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": "Digital signage & PRTV — Agent Skills",
      "description": "Open Agent Skills for AI agents: digital menu boards, TV slideshows, screen design, live widgets, loop video, TV setup, industry playbooks and the PRTV (prtv.pro) digital-signage editor.",
      "codeRepository": "https://github.com/prtvbiz-design/prtv-skills", "license": "https://creativecommons.org/licenses/by/4.0/",
      "inLanguage": ["en", "ru"], "keywords": "agent skills, digital signage, menu board, hotel TV channel, car wash screen, clinic waiting room, beauty salon, retail signage, fitness, corporate TV, Smart TV, claude skills, PRTV, меню-борд, цифровые вывески",
      "author": {"@type": "Organization", "name": "PRTV", "url": "https://prtv.pro"}}
N = len(GEN) + len(IND) + len(PRTV)
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Digital Signage Agent Skills — menu boards, hotels, clinics, shops, PRTV</title>
<meta name="description" content="{N} open Agent Skills for Claude, Cursor, Codex, Gemini CLI: menu boards, TV slideshows, widgets, loop video, industry playbooks for hotels, car washes, salons, shops, clinics, fitness and offices, and the PRTV (prtv.pro) editor. EN + RU, CC-BY-4.0.">
<link rel="canonical" href="{B}/">
<link rel="alternate" type="text/plain" href="llms.txt" title="llms.txt">
<meta property="og:title" content="Digital Signage Agent Skills">
<meta property="og:description" content="{N} open Agent Skills (EN+RU): menu boards, TV slideshows, industry playbooks, widgets, PRTV editor.">
<meta property="og:type" content="website"><meta property="og:url" content="{B}/">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--bg:#fbfaf7;--fg:#1c1b19;--mut:#5f5b54;--card:#fff;--line:#e4e0d8;--acc:#b4441d;--code:#f1eee8}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151412;--fg:#ece9e3;--mut:#a39e95;--card:#1e1d1a;--line:#34312c;--acc:#f0875a;--code:#2a2824}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:40px 16px 64px}}h1{{font-size:clamp(28px,5vw,44px);line-height:1.1;margin:0 0 12px}}
h2{{margin:48px 0 8px;font-size:24px}}h3{{margin:0 0 6px;font-size:17px}}p{{margin:0 0 10px}}.lead{{font-size:18px;color:var(--mut)}}
a{{color:var(--acc)}}code,pre{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13.5px}}
pre{{background:var(--code);padding:14px;border-radius:8px;overflow-x:auto;margin:0 0 12px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:14px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}}.card p{{font-size:14.5px}}
.ru{{color:var(--mut)}}.links{{font-size:13px!important}}.cmd{{display:block;margin-top:6px;background:var(--code);padding:4px 6px;border-radius:4px;word-break:break-all}}
ul{{padding-left:20px}}footer{{margin-top:48px;color:var(--mut);font-size:14px}}
</style></head><body><main>
<h1>Digital signage Agent Skills</h1>
<p class="lead">Open skills that teach AI agents — Claude Code, Claude.ai, Cursor, Codex, Gemini CLI, Copilot and any tool that reads the <a href="https://agentskills.io">Agent Skills</a> format — to make digital signage for small businesses: menu boards, TV slideshows, screen design, live widgets, seamless loop video, TV setup and industry playbooks for hotels, car washes and filling stations, beauty salons, shops, clinics, fitness clubs, offices and residential buildings. Plus a full set for the <a href="https://prtv.pro">PRTV</a> cloud signage editor. English and Russian, CC-BY-4.0.</p>
<p class="lead" lang="ru">Открытые скиллы для ИИ-агентов: меню-борды, слайд-шоу для телевизоров, дизайн экрана, информеры, видеофоны, вывод на ТВ и отраслевые сценарии — отели, автомойки и АЗС, салоны красоты, магазины, клиники, фитнес, офисы, подъезды; плюс подробный набор про конструктор вывесок PRTV (prtv.pro). Английский и русский.</p>
<h2>Install</h2>
<pre>npx skills add prtvbiz-design/prtv-skills
npx skills add {B}   # discovery index</pre>
<p>Claude Code:</p>
<pre>/plugin marketplace add prtvbiz-design/prtv-skills
/plugin install digital-signage@prtv-skills
/plugin install signage-industries@prtv-skills
/plugin install prtv-editor@prtv-skills</pre>
<p>Or copy the folders from <a href="https://github.com/prtvbiz-design/prtv-skills">GitHub</a> into your agent's skills directory. Index: <a href=".well-known/agent-skills/index.json">/.well-known/agent-skills/index.json</a> · <a href="llms.txt">llms.txt</a> · Templates: <a href="https://s.prtv.su/shablony/katalog-shablonov">s.prtv.su/shablony/katalog-shablonov</a></p>
<h2>Try asking your agent</h2>
<ul><li>“Make a menu board for my coffee shop: 14 drinks, 6 pastries, one 50-inch TV over the counter.”</li>
<li>“Plan the lobby screen and the in-room TV channel for a 96-room city hotel.”</li>
<li>“What should we show on the TV in our car wash waiting room?”</li>
<li>“Show today's doctors from our Google Sheet on the clinic screen.”</li>
<li lang="ru">«Собери меню-борд для кофейни в PRTV.»</li></ul>
<h2>Digital signage — vendor-neutral</h2>
<div class="grid">{cards(GEN)}</div>
<h2>Industry playbooks</h2>
<div class="grid">{cards(IND)}</div>
<h2>PRTV editor (prtv.pro)</h2>
<p>PRTV is a cloud digital-signage editor: slideshows with native text, images, video, CSS-animated HTML blocks and live widgets, shown on any Smart TV, Android box or browser by a public address. The first licence — one slideshow on up to three screens at once — is free and not time-limited. Start with <code>prtv-digital-signage</code>.</p>
<div class="grid">{cards(PRTV)}</div>
<h2>Cases</h2>
<p><a href="{ARTICLE}" lang="ru">Как сделать меню-борд для кофейни с помощью нейросетей: три кейса</a> — three coffee-shop menu boards built with AI in PRTV. Industry templates to start from: <a href="https://s.prtv.su/shablony/katalog-shablonov" lang="ru">каталог шаблонов PRTV</a>.</p>
<footer>PRTV · <a href="https://prtv.pro">prtv.pro</a> · <a href="https://s.prtv.su/informery">widget builders</a> · <a href="https://github.com/prtvbiz-design/prtv-skills">GitHub</a> · CC-BY-4.0</footer>
</main></body></html>
'''
(root / "index.html").write_text(page)
print("pages built,", N, "skills")
