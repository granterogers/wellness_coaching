"""Builds design/prototype-a.html, -b.html and -c.html from the approved copy.

Run from the repo root:  python3 design/build-prototypes.py
Copy comes verbatim from content/en/home.md; photo briefs from knowledge/photo-slots.md.
The three files share structure and differ in palette (knowledge/design-system.md) and hero composition.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "design"


# ---------------------------------------------------------------- copy parsing
def parse_home(text):
    body = text.split("---", 2)[2]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    sections = {}
    for block in re.split(r"^## ", body, flags=re.M)[1:]:
        name, rest = block.split("\n", 1)
        sec = {"labels": {}, "items": [], "list": []}
        head, *items = re.split(r"^### ", rest, flags=re.M)
        sec["labels"] = labels(rest)  # section labels may sit before or after the ### items
        sec["list"] = [l[2:].strip() for l in head.splitlines() if l.startswith("- ")]
        for it in items:
            title, txt = it.split("\n", 1)
            sec["items"].append({"title": title.strip(), "labels": labels(txt), "text": plain(txt)})
        sections[name.strip()] = sec
    return sections


def labels(txt):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\*\*([^*]+):\*\*\s*(.*)$", txt, flags=re.M)}


def plain(txt):
    lines = [l for l in txt.strip().splitlines() if l.strip() and not l.startswith("**")]
    return " ".join(lines).strip()


def md(s):
    """Escape, then *italic* -> <em>."""
    s = html.escape(s, quote=False)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)


def parse_slots(text):
    slots = {}
    for line in text.splitlines():
        m = re.match(r"^\| (P\d\d) \| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            pid, fname, where, subject, framing, setting, mood = [x.strip() for x in m.groups()]
            clean = lambda s: re.sub(r"\*\*", "", s)
            slots[pid] = {"file": fname, "where": where,
                          "brief": " · ".join(clean(x) for x in (subject, framing, setting, mood))}
    return slots


HOME = parse_home((ROOT / "content/en/home.md").read_text())
SLOTS = parse_slots((ROOT / "knowledge/photo-slots.md").read_text())
PILLAR_SLOT = {"Breathe": "P07", "Move": "P08", "Focus": "P09", "Restore": "P10", "Vitality": "P11", "Grow": "P12"}

# ---------------------------------------------------------------- palettes
PALETTES = {
    "a": dict(name="A — Field Notes", bg="#EEEEEA", alt="#E2E2DC", ink="#15191A", muted="#5A5F5C", rule="#CBCBC3",
              rule_strong="#7F847F", accent="#2F4A40", on_accent="#EEEEEA", focus="#2F4A40",
              night="#101415", night_alt="#181D1E", night_ink="#E6E6E0", night_muted="#A3A8A3", night_rule="#2A3031",
              signal="#D4F06A", night_accent="#D4F06A", on_night_accent="#101415"),
    "b": dict(name="B — Night Practice", bg="#0E1112", alt="#171B1C", ink="#ECE7DD", muted="#9A9D97", rule="#2C3233",
              rule_strong="#646A69", accent="#C9A56A", on_accent="#0E1112", focus="#C9A56A",
              night="#080A0B", night_alt="#121516", night_ink="#ECE7DD", night_muted="#9A9D97", night_rule="#262B2C",
              signal="#C9A56A", night_accent="#C9A56A", on_night_accent="#0E1112"),
    "c": dict(name="C — Tidal", bg="#E6EBEA", alt="#D8E0DF", ink="#13232A", muted="#4A5C61", rule="#B9C5C4",
              rule_strong="#728287", accent="#2E5E66", on_accent="#E6EBEA", focus="#2E5E66",
              night="#13232A", night_alt="#1B2E35", night_ink="#E6EBEA", night_muted="#A9B8B8", night_rule="#2C424A",
              signal="#D9C27A", night_accent="#D9C27A", on_night_accent="#13232A"),
}

ICON = ('<svg class="icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
        'stroke-linecap="round"><ellipse cx="32" cy="32" rx="27" ry="11" transform="rotate(-28 32 32)" stroke-width="3.4" '
        'stroke-dasharray="118 14"/><path d="M32 8 c-7 6 7 10 0 16 c-7 6 7 10 0 16 c-7 6 7 10 0 16" stroke-width="4.2"/></g>'
        '<circle cx="53" cy="20.6" r="4.6" fill="currentColor"/></svg>')

ORBIT_MARK = ('<svg class="plate-orbit" viewBox="-60 -60 120 120" aria-hidden="true" focusable="false"><g transform="rotate(-28)" '
              'fill="none" stroke="currentColor" stroke-width="1"><ellipse rx="54" ry="20"/></g>'
              '<circle cx="38" cy="-24" r="3" fill="currentColor"/></svg>')


def plate(pid, fig, ratio, cls=""):
    s = SLOTS[pid]
    return (f'<figure class="plate {cls}" style="--ratio:{ratio}">'
            f'<div class="plate-inner">{ORBIT_MARK}<p class="plate-brief"><span class="plate-id">{pid} · Photo to come</span>'
            f'{html.escape(s["brief"])}</p></div>'
            f'<figcaption class="mono">Fig. {fig} — {html.escape(s["where"])}</figcaption></figure>')


# ---------------------------------------------------------------- sections
def header(key):
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="proto-bar mono"><div class="wrap">
  <span>Prototype {PALETTES[key]["name"]}</span>
  <nav aria-label="Compare prototypes">{" ".join(f'<a href="prototype-{k}.html"{" aria-current=page" if k == key else ""}>{k.upper()}</a>' for k in "abc")}</nav>
</div></div>
<header class="site-header" id="top"><div class="wrap header-row">
  <a class="brand" href="#top">{ICON}<span class="wordmark">Grant Rogers</span></a>
  <nav class="nav" aria-label="Main">
    <a href="#pillars">Pillars</a><a href="#programme">Programme</a><a href="#book">Contact</a>
  </nav>
  <div class="header-end">
    <p class="lang mono"><a href="#" aria-current="true" lang="en">EN</a> / <a href="#" lang="es" title="Spanish version follows the build">ES</a></p>
    <a class="btn btn-small header-cta" href="#book">{md(HOME["Hero"]["labels"]["Primary button"])}</a>
  </div>
</div></header>'''


def pacer(extra=""):
    hint = md(HOME["Hero"]["labels"]["Pacer hint"])
    return f'''
<figure class="pacer {extra}" data-pacer>
  <button class="pacer-btn" type="button" aria-describedby="pacer-hint" data-pacer-start>
    <svg viewBox="-200 -200 400 400" aria-hidden="true" focusable="false">
      <g transform="rotate(-28)">
        <ellipse class="pacer-orbit" rx="186" ry="76"/>
        <ellipse class="pacer-orbit pacer-orbit-2" rx="186" ry="76" transform="rotate(64)"/>
      </g>
      <g class="pacer-ring"><circle class="pacer-disc" r="118"/><circle class="pacer-circle" r="118"/></g>
      <g transform="rotate(-28)"><circle class="pacer-electron" r="6" cx="186" cy="0"/></g>
    </svg>
    <span class="pacer-label mono" data-pacer-label>in</span>
  </button>
  <svg class="pacer-trace" viewBox="0 0 300 40" preserveAspectRatio="none" aria-hidden="true" focusable="false">
    <path class="trace-line" d=""/><circle class="trace-dot" r="3.2" cx="0" cy="20"/>
  </svg>
  <figcaption class="mono pacer-caption"><span>Fig. 00 — Resting breath</span><span>4 s in / 6 s out</span></figcaption>
  <p class="pacer-hint" id="pacer-hint">{hint}</p>
  <p class="pacer-controls">
    <button type="button" class="link-btn mono" data-pacer-pause aria-pressed="false">Pause</button>
    <button type="button" class="link-btn mono" data-pacer-stop hidden>Stop</button>
  </p>
  <p class="sr-only" aria-live="polite" data-pacer-live></p>
</figure>'''


def hero(key):
    h = HOME["Hero"]["labels"]
    headline = h["Headline"]
    roman, italic = re.match(r"(.*?)\s*\*(.*)\*", headline).groups()
    h1 = f'<h1 class="display"><span class="line"><span>{md(roman)}</span></span> <span class="line"><em>{md(italic)}</em></span></h1>'
    meta = '<p class="mono eyebrow">1:1 coaching · online · English &amp; Spanish</p>'
    sub = f'<p class="lede">{md(h["Subhead"])}</p>'
    ctas = (f'<p class="ctas"><a class="btn" href="#book">{md(h["Primary button"])}</a>'
            f'<a class="btn btn-ghost" href="#programme">{md(h["Secondary button"])}</a></p>')
    plates = plate("P01", "01", "16/9", "only-wide") + plate("P02", "01", "4/5", "only-narrow")
    if key == "a":
        return f'''
<section class="hero hero-a" aria-labelledby="h-hero"><div class="wrap grid">
  <div class="hero-text">{meta}<div id="h-hero">{h1}</div>{sub}{ctas}</div>
  <div class="hero-pacer">{pacer()}</div>
  <div class="hero-plate">{plates}</div>
</div></section>'''
    if key == "b":
        return f'''
<section class="hero hero-b" aria-labelledby="h-hero">
  <div class="hero-bleed">{plates}</div>
  <div class="wrap grid hero-over">
    <div class="hero-text">{meta}<div id="h-hero">{h1}</div>{sub}{ctas}</div>
  </div>
</section>
<section class="breath-band" aria-label="Breath pacer"><div class="wrap grid">
  <div class="band-pacer">{pacer("pacer-wide")}</div>
</div></section>'''
    return f'''
<section class="hero hero-c" aria-labelledby="h-hero"><div class="wrap grid">
  <div class="hero-head">{meta}<div id="h-hero">{h1}</div></div>
  <div class="hero-side">{sub}{ctas}{pacer("pacer-small")}</div>
  <div class="hero-plate">{plates}</div>
</div></section>'''


def pillars():
    p = HOME["Pillars"]
    items = []
    for i, it in enumerate(p["items"], 1):
        L = it["labels"]
        slot = PILLAR_SLOT.get(it["title"])
        fig = plate(slot, f"{i + 1:02d}", "1/1", "plate-sq") if slot else ""
        items.append(f'''
    <li class="pillar" data-index="{i - 1}">
      <h3 class="pillar-h"><button type="button" class="pillar-btn" aria-expanded="{"true" if i == 1 else "false"}" aria-controls="pillar-{i}">
        <span class="mono pillar-n">{i:02d}</span><span class="pillar-name">{md(it["title"])}</span><span class="pillar-sign" aria-hidden="true"></span>
      </button></h3>
      <div class="pillar-panel" id="pillar-{i}"{"" if i == 1 else " hidden"}>
        <p class="pillar-desc">{md(L["Description"])}</p>
        <dl class="pillar-notes">
          <div><dt class="mono">Practice</dt><dd>{md(L["Example practice"])}</dd></div>
          <div><dt class="mono">Why</dt><dd>{md(L["Why"])}</dd></div>
        </dl>
        {fig}
      </div>
    </li>''')
    return f'''
<section class="pillars-sec" id="pillars" aria-labelledby="h-pillars"><div class="wrap grid">
  <header class="sec-head">
    <p class="mono eyebrow">Pillars · {len(p["items"])}</p>
    <h2 id="h-pillars" class="h2">{md(p["labels"]["Heading"])}</h2>
    <p class="sec-intro">{md(p["labels"]["Intro"])}</p>
    <svg class="pillar-orbit" viewBox="-160 -70 320 140" aria-hidden="true" focusable="false" data-pillar-orbit>
      <ellipse rx="150" ry="56" />
    </svg>
  </header>
  <ol class="pillar-list" data-pillars style="--n:{len(p["items"])}">{"".join(items)}
  </ol>
</div></section>'''


def programme():
    p = HOME["Programme"]
    phases = []
    nodes = []
    for i, it in enumerate(p["items"], 1):
        num, name = re.match(r"Phase (\d+) / (.*)", it["title"]).groups()
        phases.append(f'''
      <li class="phase" data-phase="{i - 1}">
        <p class="mono phase-label">Phase {num} / {md(name)}</p>
        <h3 class="h3">{md(name)}</h3>
        <p>{md(it["text"])}</p>
      </li>''')
        nodes.append(f'<li data-node="{i - 1}"><span class="mono">{num}</span> {md(name)}</li>')
    incl = "".join(f"<li>{md(x.strip())}</li>" for x in p["labels"]["Included"].split("·"))
    return f'''
<section class="programme-sec" id="programme" aria-labelledby="h-programme"><div class="wrap grid">
  <div class="prog-rail">
    <p class="mono eyebrow">Programme · 3–6 months</p>
    <h2 id="h-programme" class="h2">{md(p["labels"]["Heading"])}</h2>
    <p class="sec-intro">{md(p["labels"]["Intro"])}</p>
    <ol class="prog-nodes" aria-hidden="true">{"".join(nodes)}</ol>
  </div>
  <ol class="phases">{"".join(phases)}
  </ol>
  <div class="prog-foot">
    <p class="mono eyebrow">Included</p>
    <ul class="included">{incl}</ul>
    <p class="price mono">{md(p["labels"]["Price line"])}</p>
    {plate("P06", "08", "3/2", "plate-call")}
  </div>
</div></section>'''


def final_cta():
    f = HOME["Final CTA"]["labels"]
    return f'''
<section class="night final" id="book" aria-labelledby="h-book">
  <div class="final-bg">{plate("P16", "09", "16/9", "plate-night")}</div>
  <svg class="final-orbit" viewBox="-400 -160 800 320" aria-hidden="true" focusable="false"><g transform="rotate(-12)"><ellipse rx="390" ry="120"/></g><circle class="final-electron" cx="300" cy="-60" r="5"/></svg>
  <div class="wrap grid final-inner">
    <div class="final-text">
      <h2 id="h-book" class="h2">{md(f["Heading"])}</h2>
      <p class="lede">{md(f["Body"])}</p>
      <p class="ctas"><a class="btn btn-night" data-mail data-subject="Book a conversation" href="#book">{md(f["Primary button"])}</a></p>
    </div>
    <ul class="contact-list">
      <li><span class="mono">Email</span> <a data-mail href="#book">{md(f["Email label"])}</a> <span class="mail-text" data-mail-text>grant.e.rogers (at) gmail (dot) com</span></li>
      <li><span class="mono">WhatsApp</span> <a href="https://wa.me/34603834206?text=Hi%20Grant%2C%20I%27d%20like%20to%20book%20a%20conversation." rel="noopener">{md(f["WhatsApp label"])}</a></li>
    </ul>
  </div>
</section>'''


def footer():
    d = HOME["Footer"]["labels"]["Disclaimer"]
    return f'''
<footer class="site-footer"><div class="wrap grid">
  <div class="foot-logo"><span class="logo-full" role="img" aria-label="Grant Rogers logo"></span></div>
  <nav class="foot-nav" aria-label="Footer"><a href="#pillars">Pillars</a><a href="#programme">Programme</a><a href="#book">Contact</a></nav>
  <p class="foot-lang mono"><a href="#" aria-current="true" lang="en">EN</a> / <a href="#" lang="es">ES</a></p>
  <p class="foot-disclaimer">{md(d)}</p>
  <p class="foot-legal mono"><a href="#">Privacy</a> · <a href="#">Terms</a> · © <span data-year>2026</span> Grant Rogers</p>
</div></footer>
<div class="mobile-cta" data-mobile-cta hidden><a class="btn" href="#book">{md(HOME["Hero"]["labels"]["Primary button"])}</a></div>'''


# ---------------------------------------------------------------- CSS + JS
def css(key):
    t = PALETTES[key]
    tokens = "\n".join(f"  --{k.replace('_', '-')}: {v};" for k, v in t.items() if k != "name")
    return f''':root {{
{tokens}
}}
''' + BASE_CSS + VARIANT_CSS[key]


BASE_CSS = r'''
@font-face{font-family:"Newsreader";font-style:normal;font-weight:200 800;font-display:swap;src:url(fonts/newsreader-latin-opsz-normal.woff2) format("woff2")}
@font-face{font-family:"Newsreader";font-style:italic;font-weight:200 800;font-display:swap;src:url(fonts/newsreader-latin-opsz-italic.woff2) format("woff2")}
@font-face{font-family:"Hanken Grotesk";font-style:normal;font-weight:100 900;font-display:swap;src:url(fonts/hanken-grotesk-latin-wght-normal.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/ibm-plex-mono-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:500;font-display:swap;src:url(fonts/ibm-plex-mono-latin-500-normal.woff2) format("woff2")}
:root{--serif:"Newsreader",Georgia,serif;--sans:"Hanken Grotesk",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;
  --s1:8px;--s2:16px;--s3:24px;--s4:32px;--s6:48px;--s8:64px;--s12:96px;--s16:128px;--ease:cubic-bezier(.45,.05,.25,1)}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:clamp(17px,16px + .25vw,19px);line-height:1.6;overflow-x:hidden}
img,svg{display:block;max-width:100%}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:.2em}
:focus-visible{outline:2px solid var(--focus);outline-offset:3px}
.night :focus-visible{outline-color:var(--night-accent)}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:var(--s2);top:-100px;background:var(--ink);color:var(--bg);padding:var(--s1) var(--s2);z-index:100}
.skip:focus{top:var(--s2)}
.mono{font-family:var(--mono);font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;line-height:1.5}
.wrap{max-width:1360px;margin:0 auto;padding:0 20px}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:20px}
.grid>*{grid-column:1/-1}
@media (min-width:768px){.wrap{padding:0 24px}.grid{grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px}}
.display{font-family:var(--serif);font-weight:340;font-size:clamp(3rem,2.3rem + 3.6vw,5.5rem);line-height:1.0;letter-spacing:-.02em;margin:0;font-variation-settings:"opsz" 72}
.display em{font-style:italic;font-weight:300}
.display .line{display:block;overflow:hidden;padding-bottom:.08em}
.display .line>*{display:inline-block}
.h2{font-family:var(--serif);font-weight:350;font-size:clamp(2.25rem,1.5rem + 2.6vw,4rem);line-height:1.05;letter-spacing:-.015em;margin:0 0 var(--s3);font-variation-settings:"opsz" 60}
.h3{font-family:var(--serif);font-weight:400;font-size:clamp(1.375rem,1.2rem + .6vw,1.75rem);line-height:1.2;margin:0 0 var(--s1)}
.lede{font-size:clamp(1.0625rem,1rem + .35vw,1.25rem);max-width:36em;margin:var(--s3) 0 0}
.eyebrow{color:var(--muted);margin:0 0 var(--s3)}
.sec-intro{max-width:30em;color:var(--muted);margin:0}
.btn{display:inline-flex;align-items:center;min-height:48px;padding:12px 22px;background:var(--accent);color:var(--on-accent);text-decoration:none;
  font-weight:550;font-size:1rem;border:1px solid var(--accent);position:relative;overflow:hidden;isolation:isolate;transition:color .5s var(--ease)}
.btn::before{content:"";position:absolute;inset:0;background:var(--ink);transform:translateY(101%);transition:transform .6s var(--ease);z-index:-1}
.btn:hover::before{transform:none}
.btn:hover{color:var(--bg)}
.btn-ghost{background:transparent;color:var(--ink);border-color:var(--rule-strong)}
.btn-small{min-height:44px;padding:8px 16px;font-size:.9375rem}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:var(--s4) 0 0}
.link-btn{background:none;border:0;padding:12px 0;min-height:44px;color:inherit;cursor:pointer;text-decoration:underline;text-underline-offset:.3em}
section{position:relative}

/* prototype switch */
.proto-bar{background:var(--ink);color:var(--bg);font-size:11px}
.proto-bar .wrap{display:flex;justify-content:space-between;align-items:center;min-height:32px;gap:var(--s2)}
.proto-bar nav{display:flex;gap:4px}.proto-bar a{display:inline-block;padding:6px 10px;text-decoration:none}
.proto-bar a[aria-current]{background:var(--bg);color:var(--ink)}

/* header */
.site-header{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 94%,transparent);border-bottom:1px solid transparent;transition:border-color .6s var(--ease)}
.header-row{display:flex;align-items:center;gap:var(--s3);min-height:76px;transition:min-height .6s var(--ease)}
.site-header.condensed{border-bottom-color:var(--rule)}
.site-header.condensed .header-row{min-height:60px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto;min-height:44px}
.brand .icon{width:30px;height:30px}
.wordmark{font-family:var(--serif);font-size:1.375rem;letter-spacing:-.01em;font-weight:420}
.nav{display:none;gap:var(--s4)}
.nav a{text-decoration:none;padding:10px 0;background:linear-gradient(currentColor,currentColor) 0 85%/0 1px no-repeat;transition:background-size .6s var(--ease)}
.nav a:hover{background-size:100% 1px}
.header-end{display:flex;align-items:center;gap:var(--s3)}
.lang{margin:0}.lang a{text-decoration:none;display:inline-block;padding:12px 2px}.lang a[aria-current]{text-decoration:underline}
.header-cta{display:none}
@media (min-width:768px){.header-cta{display:inline-flex}}
@media (min-width:1024px){.nav{display:flex}}

/* photo placeholders (8.2) */
.plate{margin:0}
.plate-inner{aspect-ratio:var(--ratio);position:relative;background-color:var(--alt);
  background-image:linear-gradient(var(--rule) 1px,transparent 1px),linear-gradient(90deg,var(--rule) 1px,transparent 1px);
  background-size:24px 24px;background-position:-1px -1px;border:1px solid var(--rule-strong);overflow:hidden;color:var(--muted)}
.plate-inner::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,var(--alt) 0,transparent 70%);opacity:.9}
.plate-orbit{position:absolute;right:6%;top:8%;width:min(34%,180px);color:var(--rule-strong)}
.plate-brief{position:absolute;left:0;right:0;bottom:0;margin:0;padding:var(--s2);z-index:1;font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;
  text-transform:uppercase;line-height:1.55;color:var(--muted);max-width:52em}
.plate-id{display:block;color:var(--ink);margin-bottom:6px}
.plate figcaption{margin-top:10px;color:var(--muted);font-size:11.5px}
.only-narrow{display:block}.only-wide{display:none}
@media (min-width:768px){.only-narrow{display:none}.only-wide{display:block}}

/* pacer (9.1, 9.2, 9.4) */
.pacer{margin:0;max-width:440px}
@media (max-width:767px){.pacer-btn{max-width:300px;margin:0 auto}}
.pacer-btn{display:block;width:100%;aspect-ratio:1;background:none;border:0;padding:0;color:var(--ink);cursor:pointer;position:relative;border-radius:50%}
.pacer-btn svg{width:100%;height:100%;overflow:visible}
.pacer-orbit{fill:none;stroke:var(--rule-strong);stroke-width:1}
.pacer-orbit-2{stroke-dasharray:3 7}
.pacer-ring{transform:scale(.62);transform-box:fill-box;transform-origin:center}
.pacer-disc{fill:var(--accent);opacity:.07}
.pacer-circle{fill:none;stroke:var(--accent);stroke-width:1.5;vector-effect:non-scaling-stroke}
.pacer-electron{fill:var(--accent)}
.pacer-label{position:absolute;inset:0;display:grid;place-items:center;font-size:13px;color:var(--ink);pointer-events:none}
.pacer-trace{width:100%;height:32px;margin-top:var(--s2);overflow:visible}
.trace-line{fill:none;stroke:var(--rule-strong);stroke-width:1;vector-effect:non-scaling-stroke}
.trace-dot{fill:var(--accent)}
.pacer-caption{display:flex;flex-wrap:wrap;justify-content:space-between;gap:0 var(--s2);border-top:1px solid var(--rule);padding-top:10px;margin-top:10px;color:var(--muted)}
.pacer-hint{margin:var(--s2) 0 0;font-family:var(--serif);font-style:italic;font-size:1.125rem}
.pacer-controls{margin:0;display:flex;gap:var(--s3)}
.pacer.guided .pacer-circle{stroke-width:2.25}
.pacer.reduced .pacer-ring{transform:scale(.84)}

/* hero */
.hero{padding:var(--s6) 0 var(--s8)}
.hero .display .line>*{animation:rise 1.2s var(--ease) both}
.hero .display .line:nth-child(2)>*{animation-delay:.18s}
@keyframes rise{from{transform:translateY(105%)}to{transform:none}}

/* sections */
.pillars-sec,.programme-sec{padding:var(--s12) 0}
.pillars-sec{border-top:1px solid var(--rule)}
.programme-sec{background:var(--alt)}
.programme-sec .plate-inner{background-color:var(--bg)}
.programme-sec .plate-inner::after{background:linear-gradient(to top,var(--bg) 0,transparent 70%)}

/* pillars (5.4): accordion on mobile, typographic index + reveal on desktop */
.sec-head{margin-bottom:var(--s6)}
.pillar-orbit{display:none}
.pillar-list{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule-strong);position:relative}
.pillar{border-bottom:1px solid var(--rule)}
.pillar-h{margin:0;font-weight:inherit}
.pillar-btn{all:unset;box-sizing:border-box;display:flex;align-items:baseline;gap:var(--s2);width:100%;min-height:64px;padding:var(--s2) 0;cursor:pointer}
.pillar-btn:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.pillar-n{color:var(--muted);min-width:2.5em}
.pillar-name{font-family:var(--serif);font-size:clamp(2rem,1.4rem + 2.4vw,3.75rem);line-height:1.05;letter-spacing:-.015em;font-weight:340}
.pillar-sign{margin-left:auto;width:14px;height:14px;position:relative;align-self:center}
.pillar-sign::before,.pillar-sign::after{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:currentColor;transition:transform .5s var(--ease)}
.pillar-sign::after{transform:rotate(90deg)}
.pillar-btn[aria-expanded=true] .pillar-sign::after{transform:rotate(0)}
.pillar-panel{padding:0 0 var(--s4) calc(2.5em + var(--s2))}
.pillar-desc{font-size:1.125rem;margin:0 0 var(--s3);max-width:32em}
.pillar-notes{margin:0 0 var(--s3);display:grid;gap:var(--s2)}
.pillar-notes div{display:grid;grid-template-columns:7em 1fr;gap:var(--s2);border-top:1px solid var(--rule);padding-top:10px}
.pillar-notes dt{color:var(--muted);padding-top:3px}.pillar-notes dd{margin:0}
.plate-sq{max-width:320px}
@media (min-width:1024px){
  .pillars-sec .sec-head{grid-column:1/6;margin:0}
  .pillar-list{grid-column:6/-1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);grid-template-rows:repeat(var(--n),auto) 1fr;column-gap:var(--s6);border-top:0;align-items:start}
  .pillar{display:contents}
  .pillar-h{grid-column:1;border-bottom:1px solid var(--rule)}
  .pillar:first-child .pillar-h{border-top:1px solid var(--rule-strong)}
  .pillar-sign{display:none}
  .pillar-btn{min-height:76px;transition:color .5s var(--ease)}
  .pillar-list:has(.pillar-btn[aria-expanded=true]) .pillar-btn[aria-expanded=false]{color:var(--muted)}
  .pillar-btn[aria-expanded=true] .pillar-n{color:var(--accent)}
  .pillar-panel{grid-column:2;grid-row:1/-1;padding:var(--s2) 0 0;align-self:start}
  .pillar-panel .plate-sq{max-width:280px}
  .pillar-panel[hidden]{display:none}
  .pillar-orbit{display:block;width:100%;max-width:420px;margin-top:var(--s8);overflow:visible}
  .pillar-orbit ellipse{fill:none;stroke:var(--rule-strong);stroke-width:1}
  .pillar-orbit .pd{fill:var(--bg);stroke:var(--rule-strong);stroke-width:1;transition:fill .5s var(--ease)}
  .pillar-orbit .pd.on{fill:var(--accent);stroke:var(--accent)}
  .pillar-orbit text{font-family:var(--mono);font-size:9px;letter-spacing:.08em;fill:var(--muted);text-transform:uppercase}
}

/* programme (5.5) */
.prog-rail{margin-bottom:var(--s6)}
.prog-nodes{display:none}
.phases{list-style:none;margin:0;padding:0;position:relative}
.phases::before{content:"";position:absolute;left:5px;top:10px;bottom:10px;width:1px;background:var(--rule-strong)}
.phase{position:relative;padding:0 0 var(--s6) var(--s6)}
.phase::before{content:"";position:absolute;left:0;top:6px;width:11px;height:11px;border-radius:50%;background:var(--alt);border:1px solid var(--ink)}
.phase-label{color:var(--accent);margin:0 0 var(--s1)}
.phase p:last-child{margin:0;max-width:30em}
.prog-foot{margin-top:var(--s4)}
.included{list-style:none;margin:0 0 var(--s3);padding:0;display:flex;flex-wrap:wrap;border-top:1px solid var(--rule-strong)}
.included li{padding:var(--s2) var(--s3) var(--s2) 0;margin-right:var(--s3);border-bottom:1px solid var(--rule);flex:1 1 220px}
.price{color:var(--muted);margin:0 0 var(--s6)}
.plate-call{max-width:560px}
@media (min-width:1024px){
  .prog-rail{grid-column:1/6;position:sticky;top:110px;align-self:start;margin:0}
  .prog-nodes{display:block;list-style:none;margin:var(--s6) 0 0;padding:0;border-top:1px solid var(--rule-strong)}
  .prog-nodes li{padding:14px 0;border-bottom:1px solid var(--rule);color:var(--muted);transition:color .6s var(--ease),padding .6s var(--ease)}
  .prog-nodes li span{display:inline-block;width:3em}
  .prog-nodes li.on{color:var(--ink);padding-left:var(--s2)}
  .prog-nodes li.on span{color:var(--accent)}
  .phases{grid-column:7/-1}
  .phases::before{display:none}
  .phase{min-height:34vh;padding:var(--s4) 0 var(--s6);border-top:1px solid var(--rule-strong)}
  .phase::before{display:none}
  .phase .h3{font-size:clamp(2rem,1.4rem + 1.6vw,3rem);margin-bottom:var(--s3)}
  .prog-foot{grid-column:7/-1}
}

/* night final CTA (5.11) */
.night{background:var(--night);color:var(--night-ink);--rule:var(--night-rule);--muted:var(--night-muted);--ink:var(--night-ink);--alt:var(--night-alt);--rule-strong:var(--night-rule);--accent:var(--night-accent)}
.final{padding:var(--s16) 0 var(--s12);overflow:hidden}
.final-bg{position:absolute;inset:0;opacity:.55}
.final-bg .plate,.final-bg .plate-inner{height:100%}
.final-bg .plate-inner{aspect-ratio:auto;border:0}
.final-bg figcaption{position:absolute;right:20px;bottom:14px;margin:0}
.final-bg .plate-brief{top:0;bottom:auto;left:auto;right:0;max-width:34em;text-align:right;padding-top:var(--s3);font-size:10.5px;opacity:.8}
.final-bg .plate-orbit{display:none}
.final-orbit{position:absolute;left:-10%;top:12%;width:120%;max-width:none;overflow:visible;pointer-events:none}
.final-orbit ellipse{fill:none;stroke:var(--night-muted);stroke-width:1;opacity:.5;vector-effect:non-scaling-stroke}
.final-electron{fill:var(--signal)}
.final-inner{position:relative}
.final-text .lede{color:var(--night-ink)}
.btn-night{background:var(--night-accent);border-color:var(--night-accent);color:var(--on-night-accent)}
.btn-night::before{background:var(--night-ink)}
.btn-night:hover{color:var(--night)}
.contact-list{list-style:none;margin:var(--s8) 0 0;padding:0;border-top:1px solid var(--night-muted)}
.contact-list li{display:flex;flex-wrap:wrap;gap:4px var(--s3);align-items:baseline;padding:var(--s2) 0;border-bottom:1px solid var(--night-rule)}
.contact-list .mono{width:7em;color:var(--night-muted)}
.contact-list a{display:inline-block;padding:8px 0;font-family:var(--serif);font-size:1.375rem}
.mail-text{color:var(--night-muted);font-size:.9375rem}
@media (min-width:1024px){.final-text{grid-column:2/8}.contact-list{grid-column:8/-1;align-self:end;margin:0}}

/* footer (5.12) */
.site-footer{padding:var(--s8) 0 120px;border-top:1px solid var(--rule)}
.site-footer .grid{row-gap:var(--s3);align-items:start}
.logo-full{display:block;width:96px;aspect-ratio:1600/1444;background:currentColor;-webkit-mask:url(assets/logo.svg) center/contain no-repeat;mask:url(assets/logo.svg) center/contain no-repeat}
.foot-nav{display:flex;flex-wrap:wrap;gap:var(--s3)}
.foot-nav a{padding:10px 0}
.foot-lang,.foot-legal{margin:0;color:var(--muted)}
.foot-lang a,.foot-legal a{display:inline-block;padding:12px 0}
.foot-disclaimer{margin:0;max-width:34em;font-family:var(--serif);font-style:italic;font-size:1.125rem}
@media (min-width:1024px){
  .site-footer{padding-bottom:var(--s8)}
  .foot-logo{grid-column:1/3}.foot-disclaimer{grid-column:3/8}.foot-nav{grid-column:8/11;flex-direction:column;gap:0}
  .foot-lang{grid-column:11/-1}.foot-legal{grid-column:3/-1;border-top:1px solid var(--rule);padding-top:var(--s2)}
}

/* sticky mobile CTA (5.13) */
.mobile-cta{position:fixed;left:0;right:0;bottom:0;z-index:60;padding:10px 20px calc(10px + env(safe-area-inset-bottom));
  background:var(--bg);border-top:1px solid var(--rule);transform:translateY(0);transition:transform .6s var(--ease)}
.mobile-cta .btn{width:100%;justify-content:center}
.mobile-cta.off{transform:translateY(110%)}
@media (min-width:768px){.mobile-cta{display:none!important}}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  html{scroll-behavior:auto}
}
'''

VARIANT_CSS = {
    "a": r'''
/* A — hero: text left, pacer right, plate below */
.hero-a{padding-top:var(--s8)}
.hero-a .hero-pacer{margin-top:var(--s6)}
.hero-a .hero-plate{margin-top:var(--s8)}
@media (min-width:1024px){
  .hero-a .hero-text{grid-column:1/8;align-self:end}
  .hero-a .hero-pacer{grid-column:9/-1;margin:0;align-self:end}
  .hero-a .hero-plate{grid-column:1/-1}
}
''',
    "b": r'''
/* B — hero: full-bleed plate, text over the open two-thirds; pacer in its own breath band */
.hero-b{padding:0;border-bottom:1px solid var(--rule)}
.hero-b .hero-bleed .plate-inner{border-left:0;border-right:0}
.hero-b .hero-bleed figcaption{padding:0 20px}
.hero-b .hero-over{padding-top:var(--s6);padding-bottom:var(--s8)}
@media (max-width:767px){.hero-b{display:flex;flex-direction:column}.hero-b .hero-over{order:-1}.hero-b .hero-bleed{padding:0 20px}}
.breath-band{padding:var(--s8) 0;background:var(--alt);border-bottom:1px solid var(--rule)}
.breath-band .plate-inner{background-color:var(--bg)}
.pacer-wide{max-width:none;display:grid;gap:0 var(--s4)}
.pacer-wide .pacer-btn{max-width:360px}
@media (min-width:768px){
  .hero-b{min-height:auto}
  .hero-b{display:grid}
  .hero-b .hero-bleed,.hero-b .hero-over{grid-area:1/1}
  .hero-b .hero-bleed{position:relative;min-height:56.25vw}
  .hero-b .hero-bleed .plate.only-wide,.hero-b .hero-bleed .plate-inner{height:100%}
  .hero-b .hero-bleed .plate-inner{aspect-ratio:auto;min-height:56.25vw}
  .hero-b .hero-bleed figcaption{position:absolute;right:24px;bottom:14px;margin:0;z-index:2}
  .hero-b .hero-bleed .plate-brief{left:auto;right:0;max-width:38%;text-align:right;bottom:40px}
  .hero-b .hero-over{position:relative;z-index:2;align-content:end;padding-top:var(--s12);padding-bottom:var(--s12);pointer-events:none;width:100%}
  .hero-b .hero-over>*{pointer-events:auto}
  .hero-b .hero-text{grid-column:1/9}
  .hero-b .plate-inner::after{background:linear-gradient(90deg,var(--bg) 0,color-mix(in srgb,var(--bg) 85%,transparent) 45%,transparent 75%);opacity:1}
  .pacer-wide{grid-template-columns:minmax(0,360px) minmax(0,1fr);align-items:center}
  .pacer-wide .pacer-btn{grid-row:1/span 4}
  .pacer-wide .pacer-trace,.pacer-wide .pacer-caption,.pacer-wide .pacer-hint,.pacer-wide .pacer-controls{grid-column:2}
  .pacer-wide .pacer-hint{font-size:clamp(1.5rem,1rem + 1.4vw,2.25rem);line-height:1.2}
  .band-pacer{grid-column:1/-1}
}
@media (min-width:1024px){.band-pacer{grid-column:2/12}.hero-b .hero-text{grid-column:1/8}}
''',
    "c": r'''
/* C — hero: wide headline on top; narrow column with lede, CTAs and pacer; plate to the right */
.hero-c .hero-side{margin-top:var(--s2)}
.hero-c .pacer-small{max-width:300px;margin-top:var(--s6)}
.hero-c .hero-plate{margin-top:var(--s6)}
.hero-c .display{font-weight:320}
@media (min-width:1024px){
  .hero-c .hero-head{grid-column:1/11}
  .hero-c .hero-side{grid-column:1/5;margin-top:var(--s6)}
  .hero-c .hero-side .lede{font-size:1.0625rem}
  .hero-c .hero-plate{grid-column:5/-1;margin-top:var(--s6)}
}
.programme-sec{background:var(--night);color:var(--night-ink);--rule:var(--night-rule);--muted:var(--night-muted);--ink:var(--night-ink);--alt:var(--night-alt);--rule-strong:#4E646C;--accent:var(--night-accent);--focus:var(--night-accent)}
.programme-sec .plate-inner{background-color:var(--night-alt)}
.programme-sec .plate-inner::after{background:linear-gradient(to top,var(--night-alt) 0,transparent 70%)}
.programme-sec .phase::before{background:var(--night)}
''',
}

JS = r'''
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  // Header condenses on scroll (5.14)
  const header = document.querySelector('.site-header');
  const onScroll = () => header.classList.toggle('condensed', scrollY > 40);
  addEventListener('scroll', onScroll, {passive: true}); onScroll();

  // Email assembled in JS (11.1)
  const addr = ['grant.e.rogers', 'gmail.com'].join('@');
  document.querySelectorAll('[data-mail]').forEach(a => {
    const subj = a.dataset.subject ? '?subject=' + encodeURIComponent(a.dataset.subject) : '';
    a.href = 'mailto:' + addr + subj;
  });
  document.querySelectorAll('[data-mail-text]').forEach(s => s.textContent = addr);

  // Breath pacer (9.1, 9.2, 9.4)
  document.querySelectorAll('[data-pacer]').forEach(fig => {
    const ring = fig.querySelector('.pacer-ring'), el = fig.querySelector('.pacer-electron');
    const label = fig.querySelector('[data-pacer-label]'), live = fig.querySelector('[data-pacer-live]');
    const pauseBtn = fig.querySelector('[data-pacer-pause]'), stopBtn = fig.querySelector('[data-pacer-stop]');
    const hint = fig.querySelector('.pacer-hint'), hintText = hint.textContent;
    const trace = fig.querySelector('.trace-line'), tdot = fig.querySelector('.trace-dot');
    const IN = 4000, CYCLE = 10000, GUIDED = 60000;
    const ease = x => .5 - .5 * Math.cos(Math.PI * x);
    const level = t => t < IN ? ease(t / IN) : 1 - ease((t - IN) / (CYCLE - IN));
    // waveform: two cycles drawn, 300 units wide
    let d = ''; for (let i = 0; i <= 300; i++) { const t = (i / 300) * CYCLE * 2 % CYCLE; d += (i ? 'L' : 'M') + i + ' ' + (34 - 28 * level(t)).toFixed(2); }
    trace.setAttribute('d', d);
    let start = performance.now(), paused = false, pausedAt = 0, guided = false, lastPhase = '', doneTimer;
    const setPhaseText = (phase, n) => {
      label.textContent = guided ? phase + ' · ' + n : phase;
      if (guided && phase !== lastPhase) live.textContent = phase === 'in' ? 'Breathe in' : 'Breathe out';
      lastPhase = phase;
    };
    const frame = now => {
      if (!paused) {
        const el_t = now - start, t = el_t % CYCLE, s = level(t);
        if (reduce.matches) { ring.style.transform = ''; ring.style.opacity = (.45 + .55 * s).toFixed(3); fig.classList.add('reduced'); }
        else { fig.classList.remove('reduced'); ring.style.opacity = ''; ring.style.transform = 'scale(' + (.62 + .38 * s).toFixed(4) + ')';
          const a = 2 * Math.PI * (t / CYCLE); el.setAttribute('cx', (186 * Math.cos(a)).toFixed(2)); el.setAttribute('cy', (76 * Math.sin(a)).toFixed(2)); }
        const x = (t / CYCLE) * 150 + 75 * 0; tdot.setAttribute('cx', x.toFixed(2)); tdot.setAttribute('cy', (34 - 28 * s).toFixed(2));
        const phase = t < IN ? 'in' : 'out', n = t < IN ? Math.floor(t / 1000) + 1 : Math.floor((t - IN) / 1000) + 1;
        setPhaseText(phase, n);
        if (guided) {
          const left = Math.max(0, Math.ceil((GUIDED - el_t) / 1000));
          hint.textContent = 'Breath ' + Math.min(6, Math.floor(el_t / CYCLE) + 1) + ' of 6 · ' + left + ' s left';
          if (el_t >= GUIDED) finish();
        }
      }
      requestAnimationFrame(frame);
    };
    const finish = () => {
      guided = false; fig.classList.remove('guided'); stopBtn.hidden = true;
      hint.textContent = "That's a minute. Notice how you feel.";
      live.textContent = "That's a minute. Notice how you feel.";
      clearTimeout(doneTimer); doneTimer = setTimeout(() => { hint.textContent = hintText; }, 8000);
      start = performance.now();
    };
    fig.querySelector('[data-pacer-start]').addEventListener('click', () => {
      guided = true; paused = false; pauseBtn.setAttribute('aria-pressed', 'false'); pauseBtn.textContent = 'Pause';
      fig.classList.add('guided'); stopBtn.hidden = false; start = performance.now(); lastPhase = '';
      clearTimeout(doneTimer);
    });
    pauseBtn.addEventListener('click', () => {
      paused = !paused;
      if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
      pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? 'Resume' : 'Pause';
    });
    stopBtn.addEventListener('click', () => { guided = false; fig.classList.remove('guided'); stopBtn.hidden = true; hint.textContent = hintText; live.textContent = 'Stopped'; start = performance.now(); });
    requestAnimationFrame(frame);
  });

  // Pillars (5.4): accordion on mobile; hover/focus reveal on desktop; orbit diagram
  const wide = matchMedia('(min-width: 1024px)');
  const list = document.querySelector('[data-pillars]');
  if (list) {
    const btns = [...list.querySelectorAll('.pillar-btn')];
    const orbit = document.querySelector('[data-pillar-orbit]');
    const NS = 'http://www.w3.org/2000/svg', dots = [];
    btns.forEach((b, i) => {
      const a = -Math.PI / 2 + (2 * Math.PI * i) / btns.length;
      const c = document.createElementNS(NS, 'circle'); c.setAttribute('class', 'pd'); c.setAttribute('r', 6);
      c.setAttribute('cx', (150 * Math.cos(a)).toFixed(1)); c.setAttribute('cy', (56 * Math.sin(a)).toFixed(1)); orbit.appendChild(c);
      const tx = document.createElementNS(NS, 'text'); tx.textContent = String(i + 1).padStart(2, '0');
      tx.setAttribute('x', (150 * Math.cos(a) + (Math.cos(a) >= 0 ? 10 : -22)).toFixed(1)); tx.setAttribute('y', (56 * Math.sin(a) + (Math.sin(a) < 0 ? -10 : 18)).toFixed(1));
      orbit.appendChild(tx); dots.push(c);
    });
    const show = (i, toggle) => btns.forEach((b, j) => {
      const open = toggle && !wide.matches ? (j === i ? b.getAttribute('aria-expanded') !== 'true' : b.getAttribute('aria-expanded') === 'true') : j === i;
      b.setAttribute('aria-expanded', String(open)); document.getElementById(b.getAttribute('aria-controls')).hidden = !open;
      dots[j].classList.toggle('on', open);
    });
    btns.forEach((b, i) => {
      b.addEventListener('click', () => show(i, true));
      b.addEventListener('mouseenter', () => wide.matches && show(i));
      b.addEventListener('focus', () => wide.matches && show(i));
    });
    wide.addEventListener('change', () => { const k = btns.findIndex(b => b.getAttribute('aria-expanded') === 'true'); show(k < 0 ? 0 : k); });
    show(0);
  }

  // Programme nodes follow the phase in view (5.5) — native scroll, nothing pinned by JS
  const nodes = document.querySelectorAll('[data-node]');
  if (nodes.length) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) nodes.forEach(n => n.classList.toggle('on', n.dataset.node === e.target.dataset.phase));
    }), {rootMargin: '-45% 0px -45% 0px'});
    document.querySelectorAll('[data-phase]').forEach(p => io.observe(p));
  }

  // Sticky mobile CTA (5.13): after the hero, hidden when the final CTA is in view
  const bar = document.querySelector('[data-mobile-cta]');
  const hero = document.querySelector('.hero'), fin = document.querySelector('#book');
  if (bar && hero && fin) {
    let pastHero = false, atEnd = false;
    const upd = () => { bar.hidden = false; bar.classList.toggle('off', !pastHero || atEnd); bar.inert = !pastHero || atEnd; };
    new IntersectionObserver(([e]) => { pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; upd(); }).observe(hero);
    new IntersectionObserver(([e]) => { atEnd = e.isIntersecting; upd(); }).observe(fin);
  }
  document.querySelectorAll('[data-year]').forEach(y => y.textContent = new Date().getFullYear());
})();
'''


def page(key):
    t = PALETTES[key]
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Prototype {key.upper()} · Grant Rogers</title>
<meta name="description" content="Design prototype {t["name"]} for Grant Rogers' coaching site. Not for sharing.">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/icon-180.png">
<link rel="preload" href="fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{css(key)}</style>
</head>
<body class="proto-{key}">
{header(key)}
<main id="main">
{hero(key)}
{pillars()}
{programme()}
{final_cta()}
</main>
{footer()}
<script>{JS}</script>
</body>
</html>
'''


if __name__ == "__main__":
    for k in "abc":
        (OUT / f"prototype-{k}.html").write_text(page(k))
        print("wrote", f"design/prototype-{k}.html")
