#!/usr/bin/env python3
"""Rebuild the Agent Skills discovery index and sitemap.

Run from the repository root after any SKILL.md changes:
    python3 scripts/build_index.py

Writes:
  .well-known/agent-skills/index.json  (Agent Skills Discovery RFC v0.2.0)
  sitemap.xml
The index points at the copies served by GitHub Pages, whose bytes are
identical to the repository files (.nojekyll disables processing).
"""
import hashlib, json, pathlib, re, datetime

BASE = "https://prtvbiz-design.github.io/prtv-skills"
root = pathlib.Path(__file__).resolve().parent.parent

# order: entry point and general skills first
ORDER = [
    "prtv-digital-signage", "digital-menu-board", "digital-signage-content",
    "signage-screen-design", "signage-widgets", "signage-loop-video",
    "tv-signage-setup", "hotel-digital-signage", "auto-service-signage",
    "beauty-salon-signage", "retail-store-signage", "clinic-signage",
    "fitness-club-signage", "office-signage", "prtv-feed-widget", "prtv-editor-overview", "prtv-agent-rules",
    "prtv-slide-settings", "prtv-element-layout", "prtv-text-element",
    "prtv-html-block-animation", "prtv-video", "prtv-widgets",
    "prtv-widgets-catalog",
]

skills = []
dirs = sorted(p.parent.name for p in root.glob("*/SKILL.md"))
for name in ORDER + [d for d in dirs if d not in ORDER]:
    f = root / name / "SKILL.md"
    if not f.exists():
        continue
    data = f.read_bytes()
    fm = data.decode("utf-8").split("---")[1]
    desc = re.search(r"^description: (.*)$", fm, re.M).group(1).strip()
    fm_name = re.search(r"^name: (.*)$", fm, re.M).group(1).strip()
    assert fm_name == name, (fm_name, name)
    skills.append({
        "name": name,
        "type": "skill-md",
        "description": desc,
        "url": f"{BASE}/{name}/SKILL.md",
        "digest": "sha256:" + hashlib.sha256(data).hexdigest(),
    })

out = root / ".well-known" / "agent-skills" / "index.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({
    "$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json",
    "skills": skills,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

today = datetime.date.today().isoformat()
urls = [f"{BASE}/", f"{BASE}/llms.txt"]
for s in skills:
    urls += [f"{BASE}/{s['name']}/SKILL.md", f"{BASE}/{s['name']}/SKILL.ru.md"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
sm.append("</urlset>")
(root / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
print(f"{len(skills)} skills indexed")
