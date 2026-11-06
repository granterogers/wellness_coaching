"""Builds design/prototype-a.html, -b.html and -c.html (round 2) from the current copy.

Run from the repo root:  python3 design/build-prototypes.py
Copy comes verbatim from content/en/home.md; photo briefs from knowledge/photo-slots.md.
Round 2 (Grant, 6 Nov 2026): one shared, quieter layout; the three files differ only in palette
(knowledge/design-system.md, "Palettes — round 2"). Round 1 is in git history.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "design"


# ---------------------------------------------------------------- copy parsing
def labels(txt):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^\*\*([^*]+):\*\*\s*(.*)$", txt, flags=re.M)}


def plain(txt):
    lines = [l for l in txt.strip().splitlines() if l.strip() and not l.startswith("**") and not l.startswith("[[")]
    return " ".join(lines).strip()


def parse_home(text):
    body = re.sub(r"<!--.*?-->", "", text.split("---", 2)[2], flags=re.S)
    sections = {}
    for block in re.split(r"^## ", body, flags=re.M)[1:]:
        name, rest = block.split("\n", 1)
        head, *items = re.split(r"^### ", rest, flags=re.M)
        sections[name.strip()] = {
            "labels": labels(rest),  # section labels may sit before or after the ### items
            "items": [{"title": t.split("\n", 1)[0].strip(), "labels": labels(t.split("\n", 1)[1]),
                       "text": plain(t.split("\n", 1)[1])} for t in items],
        }
    return sections


def md(s):
    s = html.escape(s, quote=False)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)


def parse_slots(text):
    slots = {}
    for line in text.splitlines():
        m = re.match(r"^\| (P\d\d) \| `([^`]+)` \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", line)
        if m:
            pid, _f, where, *rest = [x.strip() for x in m.groups()]
            slots[pid] = " · ".join(re.sub(r"\*\*", "", x) for x in rest)
    return slots


NAMES = {"a": "A — Sage & Saffron", "b": "B — Linen & Teal", "c": "C — Moss & Honey", "d": "D — Light & dark (A + C)"}
HOME = parse_home((ROOT / "content/en/home.md").read_text())
SLOTS = parse_slots((ROOT / "knowledge/photo-slots.md").read_text())
PILLAR_SLOT = {"Breathe": "P07", "Move": "P08", "Focus": "P09", "Restore": "P10", "Vitality": "P11", "Grow": "P12"}
# One short line per placeholder (requirement 8.2); the full brief goes in the alt text.
SHORT = {
    "P01": "Grant by a large window, morning light", "P02": "Grant by a window, head and shoulders",
    "P06": "Grant on a video call, over the shoulder", "P07": "Hand resting on the ribs, eyes closed",
    "P08": "A mobility posture on a wooden floor", "P09": "Seated meditation, lots of space",
    "P10": "Yoga Nidra under a blanket, from above", "P11": "Outdoors, strong and moving",
    "P12": "Walking away down a path, golden hour", "P16": "Calm water at dusk",
}

# ---------------------------------------------------------------- palettes (design-system.md, round 2)
PALETTES = {
    "a": dict(name="A — Sage & Saffron", bg="#ECEDE4", alt="#E1E5D6", ink="#1F2A24", muted="#56615A", rule="#CDD2C2",
              rule_strong="#7D877E", accent="#3F5F4A", on_accent="#F4F2EA", warm="#E3A63E", on_warm="#1F2A24",
              night="#22302A", night_alt="#2B3A33", night_ink="#EFEDE4", night_muted="#AEB8AE", night_rule="#3A4A42",
              t1="#D7DFCB", t2="#F1DDAF", t3="#E9E0CC", t4="#D6E0DD", t5="#EED6A2", t6="#CBD5BE", glow="38%"),
    "b": dict(name="B — Linen & Teal", bg="#F2EDE3", alt="#E9E1D2", ink="#1E2A2C", muted="#5C6461", rule="#D8CFBE",
              rule_strong="#8A8475", accent="#1F5E5F", on_accent="#F2EDE3", warm="#D08C2E", on_warm="#1E2A2C",
              night="#173232", night_alt="#1F3D3D", night_ink="#F2EDE3", night_muted="#B3BDB8", night_rule="#2D4A4A",
              t1="#E6D7BD", t2="#D5E2DC", t3="#EBCF9E", t4="#DCE3D2", t5="#E3D9C8", t6="#CFE0E0", glow="38%"),
    "c": dict(name="C — Moss & Honey", bg="#1D2420", alt="#252E29", ink="#EFE8D8", muted="#AEB3A6", rule="#34403A",
              rule_strong="#6A766E", accent="#E2B65C", on_accent="#1D2420", warm="#E2B65C", on_warm="#1D2420",
              night="#141916", night_alt="#1B221E", night_ink="#EFE8D8", night_muted="#AEB3A6", night_rule="#2C3631",
              t1="#2C3830", t2="#3D3A28", t3="#2E3637", t4="#3B3226", t5="#28382F", t6="#33303A", glow="10%"),
}

ICON = ('<svg class="icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
        'stroke-linecap="round"><ellipse cx="32" cy="32" rx="27" ry="11" transform="rotate(-28 32 32)" stroke-width="3.4" '
        'stroke-dasharray="118 14"/><path d="M32 8 c-7 6 7 10 0 16 c-7 6 7 10 0 16 c-7 6 7 10 0 16" stroke-width="4.2"/></g>'
        '<circle cx="53" cy="20.6" r="4.6" fill="currentColor"/></svg>')


def plate(pid, ratio, tint, cls=""):
    return (f'<figure class="plate {cls}" style="--ratio:{ratio};--tint:var(--{tint})">'
            f'<div class="plate-inner" role="img" aria-label="Photo to come: {html.escape(SLOTS[pid], quote=True)}">'
            f'<p class="plate-label" aria-hidden="true"><span class="mono">Photo to come</span>{html.escape(SHORT[pid])}</p>'
            f'</div></figure>')


# ---------------------------------------------------------------- sections
def header(key):
    cta = md(HOME["Hero"]["labels"]["Primary button"])
    switch = " ".join(f'<a href="prototype-{k}.html"{" aria-current=page" if k == key else ""}>{k.upper()}</a>' for k in "abcd")
    toggle = ('<button type="button" class="theme-btn mono" data-theme-toggle aria-pressed="false">'
              '<span class="theme-dot" aria-hidden="true"></span><span data-theme-label>Dark mode</span></button>') if key == "d" else ""
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="proto-bar"><div class="wrap"><span class="mono">Prototype {NAMES[key]}</span>
  <nav aria-label="Compare prototypes" class="mono">{switch}</nav></div></div>
<header class="site-header" id="top"><div class="wrap header-row">
  <a class="brand" href="#top">{ICON}<span class="wordmark">Grant Rogers</span></a>
  <nav class="nav" aria-label="Main"><a href="#approach">Approach</a><a href="#pillars">Pillars</a><a href="#programme">Programme</a><a href="#book">Contact</a></nav>
  {toggle}
  <p class="lang mono"><a href="#" aria-current="true" lang="en">EN</a> / <a href="#" lang="es" title="Spanish version follows the build">ES</a></p>
  <a class="btn btn-small header-cta" href="#book">{cta}</a>
</div></header>'''


def pacer():
    return f'''
<figure class="pacer" data-pacer>
  <button class="pacer-btn" type="button" aria-describedby="pacer-hint" data-pacer-start>
    <svg viewBox="-200 -200 400 400" aria-hidden="true" focusable="false">
      <g transform="rotate(-28)"><ellipse class="pacer-orbit" rx="186" ry="76"/></g>
      <g class="pacer-ring"><circle class="pacer-glow" r="118"/><circle class="pacer-circle" r="118"/></g>
      <g transform="rotate(-28)"><circle class="pacer-electron" r="7" cx="186" cy="0"/></g>
    </svg>
    <span class="pacer-label" data-pacer-label>in</span>
  </button>
  <figcaption>
    <p class="pacer-hint" id="pacer-hint">{md(HOME["Hero"]["labels"]["Pacer hint"])}</p>
    <p class="pacer-meta"><span class="mono">4 s in · 6 s out</span>
      <button type="button" class="link-btn mono" data-pacer-pause aria-pressed="false">Pause</button>
      <button type="button" class="link-btn mono" data-pacer-stop hidden>Stop</button></p>
  </figcaption>
  <p class="sr-only" aria-live="polite" data-pacer-live></p>
</figure>'''


def hero():
    h = HOME["Hero"]["labels"]
    roman, italic = re.match(r"(.*?)\s*\*(.*)\*", h["Headline"]).groups()
    return f'''
<section class="hero" aria-labelledby="h-hero"><div class="wrap grid">
  <div class="hero-text">
    <p class="mono eyebrow">1:1 coaching · online · English &amp; Spanish</p>
    <h1 class="display" id="h-hero"><span class="line"><span>{md(roman)}</span></span> <span class="line"><em>{md(italic)}</em></span></h1>
    <p class="lede">{md(h["Subhead"])}</p>
    <p class="ctas"><a class="btn" href="#book">{md(h["Primary button"])}</a><a class="btn btn-ghost" href="#programme">{md(h["Secondary button"])}</a></p>
  </div>
  <div class="hero-pacer">{pacer()}</div>
  <div class="hero-plate">{plate("P01", "16/9", "t1", "only-wide")}{plate("P02", "4/5", "t1", "only-narrow")}</div>
</div></section>'''


def approach():
    a = HOME["Approach"]
    items = "".join(f'''
    <li><span class="num" aria-hidden="true">{i}</span><div><h3 class="h3">{md(it["title"])}</h3><p>{md(it["text"])}</p></div></li>'''
                    for i, it in enumerate(a["items"], 1))
    return f'''
<section class="approach" id="approach" aria-labelledby="h-approach"><div class="wrap grid">
  <h2 class="h2" id="h-approach">{md(a["labels"]["Heading"])}</h2>
  <ol class="principles">{items}
  </ol>
</div></section>'''


def pillars():
    p = HOME["Pillars"]
    n = len(p["items"])
    cols = []
    for i, it in enumerate(p["items"], 1):
        L = it["labels"]
        slot = PILLAR_SLOT.get(it["title"])
        cols.append(f'''
    <li class="pillar">
      {plate(slot, "1/1", f"t{(i - 1) % 6 + 1}") if slot else ""}
      <p class="mono pillar-n">{i:02d}</p>
      <h3 class="pillar-name">{md(it["title"])}</h3>
      <p class="pillar-desc">{md(L["Description"])}</p>
      <p class="pillar-practice"><span class="mono">Try</span>{md(L["Example practice"])}</p>
      <p class="pillar-why">{md(L["Why"])}</p>
    </li>''')
    return f'''
<section class="pillars-sec" id="pillars" aria-labelledby="h-pillars"><div class="wrap">
  <div class="grid sec-head"><h2 class="h2" id="h-pillars">{md(p["labels"]["Heading"])}</h2><p class="sec-intro">{md(p["labels"]["Intro"])}</p></div>
  <p class="mono swipe-hint" aria-hidden="true">Swipe to see all {n} →</p>
</div>
<div class="pillar-scroll" tabindex="0" role="region" aria-label="{md(p["labels"]["Heading"])} (scrolls sideways)">
  <ol class="pillar-row" style="--n:{n}">{"".join(cols)}
  </ol>
</div></section>'''


def programme():
    p = HOME["Programme"]
    steps = []
    for it in p["items"]:
        num, name = re.match(r"Phase (\d+) / (.*)", it["title"]).groups()
        steps.append(f'''
    <li class="step"><p class="mono step-n">Phase {num}</p><h3 class="h3">{md(name)}</h3><p>{md(it["text"])}</p></li>''')
    incl = "".join(f"<li>{md(x.strip())}</li>" for x in p["labels"]["Included"].split("·"))
    return f'''
<section class="programme-sec" id="programme" aria-labelledby="h-programme"><div class="wrap grid">
  <div class="prog-head"><h2 class="h2" id="h-programme">{md(p["labels"]["Heading"])}</h2><p class="sec-intro">{md(p["labels"]["Intro"])}</p></div>
  <div class="prog-plate">{plate("P06", "3/2", "t4")}</div>
  <ol class="timeline">{"".join(steps)}
  </ol>
  <div class="included-row"><h3 class="mono included-h">Included</h3><ul class="included">{incl}</ul></div>
  <p class="price">{md(p["labels"]["Price line"])}</p>
</div></section>'''


def final_cta():
    f = HOME["Final CTA"]["labels"]
    wa = "https://wa.me/34603834206?text=Hi%20Grant%2C%20I%27d%20like%20to%20book%20a%20conversation."
    return f'''
<section class="night final" id="book" aria-labelledby="h-book">
  <div class="final-bg" aria-hidden="true">{plate("P16", "16/9", "night-alt")}</div>
  <svg class="final-orbit" viewBox="-400 -160 800 320" aria-hidden="true" focusable="false"><g transform="rotate(-10)"><ellipse rx="390" ry="118"/></g><circle class="final-electron" cx="318" cy="-78" r="6"/></svg>
  <div class="wrap grid final-inner">
    <div class="final-text">
      <h2 id="h-book" class="h2">{md(f["Heading"])}</h2>
      <p class="lede">{md(f["Body"])}</p>
      <p class="ctas"><a class="btn btn-warm" data-mail data-subject="Book a conversation" href="#book">{md(f["Primary button"])}</a></p>
    </div>
    <ul class="contact-list">
      <li><span class="mono">Email</span><a data-mail href="#book">{md(f["Email label"])}</a><span class="mail-text" data-mail-text>grant.e.rogers (at) gmail (dot) com</span></li>
      <li><span class="mono">WhatsApp</span><a href="{wa}" rel="noopener">{md(f["WhatsApp label"])}</a></li>
    </ul>
  </div>
</section>'''


def footer():
    return f'''
<footer class="site-footer"><div class="wrap grid">
  <div class="foot-logo"><span class="logo-full" role="img" aria-label="Grant Rogers logo"></span></div>
  <p class="foot-disclaimer">{md(HOME["Footer"]["labels"]["Disclaimer"])}</p>
  <nav class="foot-nav" aria-label="Footer"><a href="#approach">Approach</a><a href="#pillars">Pillars</a><a href="#programme">Programme</a><a href="#book">Contact</a></nav>
  <p class="foot-meta mono"><a href="#" aria-current="true" lang="en">EN</a> / <a href="#" lang="es">ES</a> · <a href="#">Privacy</a> · <a href="#">Terms</a> · © <span data-year>2026</span> Grant Rogers</p>
</div></footer>
<div class="mobile-cta off" data-mobile-cta inert><a class="btn" href="#book">{md(HOME["Hero"]["labels"]["Primary button"])}</a></div>'''


# ---------------------------------------------------------------- CSS
CSS = r'''
@font-face{font-family:"Newsreader";font-style:normal;font-weight:200 800;font-display:swap;src:url(fonts/newsreader-latin-opsz-normal.woff2) format("woff2")}
@font-face{font-family:"Newsreader";font-style:italic;font-weight:200 800;font-display:swap;src:url(fonts/newsreader-latin-opsz-italic.woff2) format("woff2")}
@font-face{font-family:"Hanken Grotesk";font-style:normal;font-weight:100 900;font-display:swap;src:url(fonts/hanken-grotesk-latin-wght-normal.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/ibm-plex-mono-latin-400-normal.woff2) format("woff2")}
:root{--serif:"Newsreader",Georgia,serif;--sans:"Hanken Grotesk",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;
  --s1:8px;--s2:16px;--s3:24px;--s4:32px;--s6:48px;--s8:64px;--s12:96px;--s16:128px;--ease:cubic-bezier(.45,.05,.25,1)}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:clamp(17px,16px + .25vw,19px);line-height:1.6;overflow-x:hidden}
img,svg{display:block;max-width:100%}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:.2em}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:var(--s2);top:-100px;background:var(--ink);color:var(--bg);padding:var(--s1) var(--s2);z-index:100}
.skip:focus{top:var(--s2)}
.mono{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;line-height:1.5;font-weight:400}
.wrap{max-width:1360px;margin:0 auto;padding:0 20px}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:20px}
.grid>*{grid-column:1/-1}
@media (min-width:768px){.wrap{padding:0 32px}.grid{grid-template-columns:repeat(12,minmax(0,1fr));column-gap:24px}}
.display{text-wrap:balance;font-family:var(--serif);font-weight:360;font-size:clamp(2.75rem,2.1rem + 3.4vw,5.5rem);line-height:1.02;letter-spacing:-.02em;margin:0;font-variation-settings:"opsz" 72}
.display em{font-style:italic;font-weight:330;color:var(--accent)}
.display .line{display:block;overflow:hidden;padding-bottom:.1em}
.display .line>*{display:inline-block;animation:rise 1.2s var(--ease) both}
.display .line:nth-child(2)>*{animation-delay:.2s}
@keyframes rise{from{transform:translateY(105%)}to{transform:none}}
.h2{text-wrap:balance;font-family:var(--serif);font-weight:380;font-size:clamp(2.25rem,1.6rem + 2.2vw,3.75rem);line-height:1.08;letter-spacing:-.015em;margin:0 0 var(--s3);font-variation-settings:"opsz" 60}
.h3{font-family:var(--serif);font-weight:450;font-size:clamp(1.375rem,1.2rem + .6vw,1.75rem);line-height:1.2;margin:0 0 var(--s1)}
.lede{font-size:clamp(1.0625rem,1rem + .35vw,1.25rem);max-width:34em;margin:var(--s3) 0 0}
.eyebrow{color:var(--muted);margin:0 0 var(--s3)}
.sec-intro{max-width:30em;color:var(--muted);margin:0}
.btn{display:inline-flex;align-items:center;min-height:48px;padding:12px 24px;background:var(--accent);color:var(--on-accent);text-decoration:none;
  font-weight:600;font-size:1rem;border:1px solid var(--accent);border-radius:999px;position:relative;overflow:hidden;isolation:isolate;transition:color .5s var(--ease)}
.btn::before{content:"";position:absolute;inset:0;background:var(--ink);transform:translateY(101%);transition:transform .6s var(--ease);z-index:-1}
.btn:hover::before{transform:none}.btn:hover{color:var(--bg)}
.btn-ghost{background:transparent;color:var(--ink);border-color:var(--rule-strong)}
.btn-small{min-height:44px;padding:8px 18px;font-size:.9375rem}
.btn-warm{background:var(--warm);border-color:var(--warm);color:var(--on-warm)}
.btn-warm::before{background:var(--night-ink)}.btn-warm:hover{color:var(--night)}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin:var(--s4) 0 0}
.link-btn{background:none;border:0;padding:12px 0;min-height:44px;color:inherit;cursor:pointer;text-decoration:underline;text-underline-offset:.3em}
section{position:relative}

/* prototype switch (comparison only) */
.proto-bar{background:var(--alt);color:var(--muted);border-bottom:1px solid var(--rule)}
.proto-bar .wrap{display:flex;justify-content:space-between;align-items:center;min-height:36px;gap:var(--s2)}
.proto-bar .mono{font-size:11px}
.proto-bar nav{display:flex;gap:2px}.proto-bar a{display:inline-block;padding:8px 12px;text-decoration:none;border-radius:999px}
.proto-bar a[aria-current]{background:var(--ink);color:var(--bg)}

/* header (5.14) */
.site-header{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 94%,transparent);border-bottom:1px solid transparent;transition:border-color .6s var(--ease)}
.header-row{display:flex;align-items:center;gap:var(--s3);min-height:76px;transition:min-height .6s var(--ease)}
.site-header.condensed{border-bottom-color:var(--rule)}.site-header.condensed .header-row{min-height:60px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:auto;min-height:44px}
.brand .icon{width:30px;height:30px;color:var(--accent)}
.wordmark{font-family:var(--serif);font-size:1.375rem;letter-spacing:-.01em;font-weight:450}
.nav{display:none;gap:var(--s4)}
.nav a{text-decoration:none;padding:10px 0;background:linear-gradient(currentColor,currentColor) 0 85%/0 1px no-repeat;transition:background-size .6s var(--ease)}
.nav a:hover{background-size:100% 1px}
.lang{margin:0}.lang a{text-decoration:none;display:inline-block;padding:12px 2px}.lang a[aria-current]{text-decoration:underline}
.header-cta{display:none}
@media (min-width:768px){.header-cta{display:inline-flex}}
@media (min-width:1024px){.nav{display:flex}}

/* light / dark toggle (6.9) */
.theme-btn{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;background:none;color:inherit;border:1px solid var(--rule-strong);border-radius:999px;cursor:pointer}
.theme-dot{width:12px;height:12px;border-radius:50%;background:var(--ink);box-shadow:inset -4px 0 0 var(--bg)}
@media (max-width:420px){.theme-btn [data-theme-label]{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.theme-btn{padding:0 15px}}
body{transition:background-color .6s var(--ease),color .6s var(--ease)}

/* photo placeholders (8.2): soft warm tone, one short line */
.plate{margin:0}
.plate-inner{aspect-ratio:var(--ratio);position:relative;border-radius:4px;overflow:hidden;
  background:radial-gradient(120% 95% at 78% 16%,color-mix(in srgb,var(--tint),white var(--glow)) 0%,var(--tint) 48%,color-mix(in srgb,var(--tint) 88%,var(--ink)) 100%)}
.plate-label{position:absolute;left:0;bottom:0;margin:0;padding:14px 16px;font-size:.875rem;line-height:1.4;color:var(--ink);opacity:.78;max-width:30em}
.plate-label .mono{display:block;font-size:10.5px;margin-bottom:2px}
.only-narrow{display:block}.only-wide{display:none}
@media (min-width:768px){.only-narrow{display:none}.only-wide{display:block}}

/* breath pacer (9.1, 9.2, 9.4) */
.pacer{margin:0;max-width:400px}
.pacer-btn{display:block;width:100%;aspect-ratio:1;background:none;border:0;padding:0;color:var(--ink);cursor:pointer;position:relative;border-radius:50%}
.pacer-btn svg{width:100%;height:100%;overflow:visible}
.pacer-orbit{fill:none;stroke:var(--rule-strong);stroke-width:1;opacity:.7}
.pacer-ring{transform:scale(.62);transform-box:fill-box;transform-origin:center}
.pacer-glow{fill:var(--warm);opacity:.26}
.pacer-circle{fill:none;stroke:var(--accent);stroke-width:1.5;vector-effect:non-scaling-stroke}
.pacer-electron{fill:var(--warm);stroke:var(--accent);stroke-width:1}
.pacer-label{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--serif);font-style:italic;font-size:1.5rem;pointer-events:none}
.pacer figcaption{margin-top:var(--s2)}
.pacer-hint{margin:0;font-family:var(--serif);font-style:italic;font-size:1.125rem;line-height:1.4}
.pacer-meta{margin:var(--s1) 0 0;display:flex;align-items:center;gap:var(--s3);color:var(--muted)}
.pacer.guided .pacer-circle{stroke-width:2.25}
.pacer.reduced .pacer-ring{transform:scale(.84)}

/* hero (5.1) */
.hero{padding:var(--s8) 0 var(--s8)}
.hero-pacer{margin-top:var(--s6)}
.hero-pacer .pacer{max-width:280px;margin:0 auto}
.hero-plate{margin-top:var(--s6)}
@media (min-width:1024px){
  .hero{padding-top:var(--s12)}
  .hero-text{grid-column:1/8;align-self:center}
  .hero-pacer{grid-column:9/-1;margin:0;align-self:center}.hero-pacer .pacer{max-width:380px}
  .hero-plate{margin-top:var(--s8)}
}

/* approach (5.3): heading left, numbered principles right */
.approach{padding:var(--s12) 0;border-top:1px solid var(--rule)}
.principles{list-style:none;margin:0;padding:0}
.principles li{display:grid;grid-template-columns:3.5rem 1fr;gap:var(--s2);padding:var(--s4) 0;border-top:1px solid var(--rule)}
.principles li:last-child{border-bottom:1px solid var(--rule)}
.principles .num{font-family:var(--serif);font-style:italic;font-size:2.5rem;line-height:1;color:var(--accent)}
.principles p{margin:0;max-width:34em}
@media (min-width:1024px){.approach .h2{grid-column:1/6}.principles{grid-column:7/-1}}

/* pillars (5.4): columns side by side; swipe row under 1024px */
.pillars-sec{padding:var(--s12) 0;background:var(--alt)}
.sec-head{margin-bottom:var(--s6);align-items:end}
@media (min-width:1024px){.sec-head .h2{grid-column:1/7;margin:0}.sec-head .sec-intro{grid-column:8/-1}}
.swipe-hint{color:var(--muted);margin:0 0 var(--s2)}
.pillar-scroll{overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 20px;-webkit-overflow-scrolling:touch;scrollbar-width:thin;padding-bottom:var(--s2)}
.pillar-scroll:focus-visible{outline-offset:-2px}
.pillar-row{list-style:none;margin:0;padding:0 20px;display:flex;gap:0;width:max-content}
.pillar{scroll-snap-align:start;width:min(78vw,320px);padding:0 var(--s3) var(--s3);border-left:1px solid var(--rule-strong)}
.pillar:first-child{border-left:0;padding-left:0}
.pillar .plate{margin-bottom:var(--s3)}
.pillar-n{color:var(--accent);margin:0 0 4px}
.pillar-name{font-family:var(--serif);font-weight:400;font-size:clamp(1.875rem,1.5rem + 1vw,2.375rem);line-height:1.05;margin:0 0 var(--s2);letter-spacing:-.01em}
.pillar-desc{margin:0 0 var(--s2);font-size:1rem}
.pillar-practice{margin:0 0 var(--s1);font-size:1rem;padding-top:var(--s2);border-top:1px solid var(--rule)}
.pillar-practice .mono{display:block;color:var(--muted);margin-bottom:2px}
.pillar-why{margin:0;font-size:.9375rem;color:var(--muted)}
@media (min-width:768px){.pillar-row{padding:0 32px}.pillar-scroll{scroll-padding:0 32px}}
@media (min-width:1024px){
  .swipe-hint{display:none}
  .pillar-scroll{overflow:visible;padding:0}
  .pillar-row{max-width:1360px;margin:0 auto;width:auto;display:grid;grid-template-columns:repeat(min(var(--n),6),minmax(0,1fr));row-gap:var(--s6)}
  .pillar{width:auto;border-top:2px solid var(--ink);padding-top:var(--s3)}
  .pillar:first-child{padding-left:0}
  .pillar:nth-child(6n+1){border-left:0;padding-left:0}
}

/* programme (5.5): simple left-to-right timeline */
.programme-sec{padding:var(--s12) 0}
.prog-head{margin-bottom:var(--s4)}
.prog-plate{margin-bottom:var(--s6)}
.prog-plate .plate{max-width:520px}
.timeline{list-style:none;margin:0 0 var(--s6);padding:0}
.step{position:relative;padding:0 0 var(--s4) var(--s6)}
.step::before{content:"";position:absolute;left:7px;top:18px;bottom:-4px;width:1px;background:var(--rule-strong)}
.step:last-child::before{display:none}
.step::after{content:"";position:absolute;left:0;top:4px;width:15px;height:15px;border-radius:50%;background:var(--warm);border:1px solid var(--accent)}
.step-n{color:var(--accent);margin:0 0 4px}
.step p:last-child{margin:0;max-width:30em}
.included-row{border-top:1px solid var(--rule);padding-top:var(--s3)}
.included-h{margin:0 0 var(--s2);color:var(--muted)}
.included{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.included li{padding:8px 16px;border:1px solid var(--rule-strong);border-radius:999px;font-size:.9375rem}
.price{margin:var(--s4) 0 0;font-family:var(--serif);font-style:italic;font-size:1.25rem}
@media (min-width:1024px){
  .prog-head{grid-column:1/7;align-self:end;margin:0}
  .prog-plate{grid-column:8/-1;margin:0}
  .timeline{grid-column:1/-1;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:var(--s4);margin:var(--s8) 0 var(--s6)}
  .step{padding:var(--s6) 0 0}
  .step::before{left:0;right:calc(-1 * var(--s4));top:7px;bottom:auto;width:auto;height:1px}
  .step:last-child::before{display:block;right:0}
  .step::after{top:0}
  .included-row{grid-column:1/9;display:grid;grid-template-columns:8em 1fr;align-items:start}
  .included-h{padding-top:9px}
  .price{grid-column:9/-1;align-self:center;margin:0;text-align:right}
}

/* night final CTA (5.11) */
.night{background:var(--night);color:var(--night-ink);--ink:var(--night-ink);--muted:var(--night-muted);--rule:var(--night-rule);--accent:var(--warm)}
.final{padding:var(--s16) 0 var(--s12);overflow:hidden}
.final-bg{position:absolute;inset:0;opacity:.6}
.final-bg .plate,.final-bg .plate-inner{height:100%}
.final-bg .plate-inner{aspect-ratio:auto;border-radius:0;--glow:8%}
.final-bg .plate-label{left:auto;right:0;text-align:right;opacity:.6}
.final-orbit{position:absolute;left:-8%;top:10%;width:116%;max-width:none;overflow:visible;pointer-events:none}
.final-orbit ellipse{fill:none;stroke:var(--night-muted);stroke-width:1;opacity:.35;vector-effect:non-scaling-stroke}
.final-electron{fill:var(--warm)}
.final-inner{position:relative}
.contact-list{list-style:none;margin:var(--s8) 0 0;padding:0;border-top:1px solid var(--night-muted)}
.contact-list li{display:flex;flex-wrap:wrap;gap:4px var(--s3);align-items:baseline;padding:var(--s2) 0;border-bottom:1px solid var(--night-rule)}
.contact-list .mono{width:7em;color:var(--night-muted)}
.contact-list a{display:inline-block;padding:8px 0;font-family:var(--serif);font-size:1.375rem}
.mail-text{color:var(--night-muted);font-size:.9375rem}
@media (min-width:1024px){.final-text{grid-column:1/7}.contact-list{grid-column:8/-1;align-self:end;margin:0}}

/* footer (5.12) */
.site-footer{padding:var(--s8) 0 120px;border-top:1px solid var(--rule)}
.site-footer .grid{row-gap:var(--s3);align-items:start}
.logo-full{display:block;width:96px;aspect-ratio:1600/1444;background:var(--accent);-webkit-mask:url(assets/logo.svg) center/contain no-repeat;mask:url(assets/logo.svg) center/contain no-repeat}
.foot-disclaimer{margin:0;max-width:34em;font-family:var(--serif);font-style:italic;font-size:1.125rem}
.foot-nav{display:flex;flex-wrap:wrap;gap:0 var(--s3)}.foot-nav a{padding:10px 0}
.foot-meta{margin:0;color:var(--muted)}.foot-meta a{display:inline-block;padding:12px 0}
@media (min-width:1024px){.site-footer{padding-bottom:var(--s8)}.foot-logo{grid-column:1/3}.foot-disclaimer{grid-column:3/8}.foot-nav{grid-column:9/-1;flex-direction:column}.foot-meta{grid-column:3/-1;border-top:1px solid var(--rule);padding-top:var(--s2)}}

/* sticky mobile CTA (5.13) */
.mobile-cta{position:fixed;left:0;right:0;bottom:0;z-index:60;padding:10px 20px calc(10px + env(safe-area-inset-bottom));background:var(--bg);border-top:1px solid var(--rule);transition:transform .6s var(--ease)}
.mobile-cta .btn{width:100%;justify-content:center}
.mobile-cta.off{transform:translateY(110%)}
@media (min-width:768px){.mobile-cta{display:none}}

@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}html{scroll-behavior:auto}}
'''

JS = r'''
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const header = document.querySelector('.site-header');
  const onScroll = () => header.classList.toggle('condensed', scrollY > 40);
  addEventListener('scroll', onScroll, {passive: true}); onScroll();

  // Email assembled in JS (11.1)
  const addr = ['grant.e.rogers', 'gmail.com'].join('@');
  document.querySelectorAll('[data-mail]').forEach(a => a.href = 'mailto:' + addr + (a.dataset.subject ? '?subject=' + encodeURIComponent(a.dataset.subject) : ''));
  document.querySelectorAll('[data-mail-text]').forEach(s => s.textContent = addr);

  // Breath pacer (9.1, 9.2, 9.4)
  document.querySelectorAll('[data-pacer]').forEach(fig => {
    const ring = fig.querySelector('.pacer-ring'), el = fig.querySelector('.pacer-electron');
    const label = fig.querySelector('[data-pacer-label]'), live = fig.querySelector('[data-pacer-live]');
    const pauseBtn = fig.querySelector('[data-pacer-pause]'), stopBtn = fig.querySelector('[data-pacer-stop]');
    const hint = fig.querySelector('.pacer-hint'), hintHTML = hint.innerHTML;
    const IN = 4000, CYCLE = 10000, GUIDED = 60000;
    const ease = x => .5 - .5 * Math.cos(Math.PI * x);
    const level = t => t < IN ? ease(t / IN) : 1 - ease((t - IN) / (CYCLE - IN));
    let start = performance.now(), paused = false, pausedAt = 0, guided = false, lastPhase = '', doneTimer;
    const finish = msg => {
      guided = false; fig.classList.remove('guided'); stopBtn.hidden = true; start = performance.now();
      hint.textContent = msg; live.textContent = msg;
      clearTimeout(doneTimer); doneTimer = setTimeout(() => { hint.innerHTML = hintHTML; }, 8000);
    };
    const frame = now => {
      if (!paused) {
        const run = now - start, t = run % CYCLE, s = level(t);
        if (reduce.matches) { fig.classList.add('reduced'); ring.style.transform = ''; ring.style.opacity = (.45 + .55 * s).toFixed(3); }
        else {
          fig.classList.remove('reduced'); ring.style.opacity = ''; ring.style.transform = 'scale(' + (.62 + .38 * s).toFixed(4) + ')';
          const a = 2 * Math.PI * (t / CYCLE); el.setAttribute('cx', (186 * Math.cos(a)).toFixed(2)); el.setAttribute('cy', (76 * Math.sin(a)).toFixed(2));
        }
        const phase = t < IN ? 'in' : 'out', n = t < IN ? Math.floor(t / 1000) + 1 : Math.floor((t - IN) / 1000) + 1;
        label.textContent = guided ? phase + ' · ' + n : phase;
        if (guided && phase !== lastPhase) live.textContent = phase === 'in' ? 'Breathe in' : 'Breathe out';
        lastPhase = phase;
        if (guided) {
          hint.textContent = 'Breath ' + Math.min(6, Math.floor(run / CYCLE) + 1) + ' of 6 · ' + Math.max(0, Math.ceil((GUIDED - run) / 1000)) + ' s left';
          if (run >= GUIDED) finish("That's a minute. Notice how you feel.");
        }
      }
      requestAnimationFrame(frame);
    };
    fig.querySelector('[data-pacer-start]').addEventListener('click', () => {
      guided = true; paused = false; pauseBtn.setAttribute('aria-pressed', 'false'); pauseBtn.textContent = 'Pause';
      fig.classList.add('guided'); stopBtn.hidden = false; start = performance.now(); lastPhase = ''; clearTimeout(doneTimer);
    });
    pauseBtn.addEventListener('click', () => {
      paused = !paused;
      if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
      pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? 'Resume' : 'Pause';
    });
    stopBtn.addEventListener('click', () => finish('Stopped.'));
    requestAnimationFrame(frame);
  });

  // Light / dark toggle (6.9): device setting first, then the visitor's choice, remembered on this device
  const tbtn = document.querySelector('[data-theme-toggle]');
  if (tbtn) {
    const root = document.documentElement, dark = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : dark.matches;
    const sync = () => { const d = isDark(); tbtn.setAttribute('aria-pressed', String(d)); };
    tbtn.addEventListener('click', () => {
      const next = isDark() ? 'light' : 'dark'; root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
      sync();
    });
    dark.addEventListener('change', sync); sync();
  }

  // Sticky mobile CTA (5.13): after the hero, hidden when the final CTA is in view
  const bar = document.querySelector('[data-mobile-cta]'), hero = document.querySelector('.hero'), fin = document.querySelector('#book');
  let pastHero = false, atEnd = false;
  const upd = () => { const off = !pastHero || atEnd; bar.classList.toggle('off', off); bar.inert = off; };
  new IntersectionObserver(([e]) => { pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; upd(); }).observe(hero);
  new IntersectionObserver(([e]) => { atEnd = e.isIntersecting; upd(); }).observe(fin);
  document.querySelectorAll('[data-year]').forEach(y => y.textContent = new Date().getFullYear());
})();
'''


def tokens(t):
    return "".join(f"--{k.replace('_', '-')}:{v};" for k, v in t.items() if k != "name")


def theme_css(key):
    if key != "d":
        return f":root{{{tokens(PALETTES[key])}}}"
    light, dark = tokens(PALETTES["a"]) + "color-scheme:light;", tokens(PALETTES["c"]) + "color-scheme:dark;"
    return (f":root{{{light}}}:root[data-theme=dark]{{{dark}}}"
            f"@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{{dark}}}}}")


def page(key):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Prototype {key.upper()} · Grant Rogers</title>
<meta name="description" content="Design prototype {NAMES[key]} for Grant Rogers' coaching site. Not for sharing.">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/icon-180.png">
<link rel="preload" href="fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<script>try{{var t=localStorage.getItem("theme");if(t&&{str(key == "d").lower()})document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<style>{theme_css(key)}{CSS}</style>
</head>
<body class="proto-{key}">
{header(key)}
<main id="main">
{hero()}
{approach()}
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
    for k in "abcd":
        (OUT / f"prototype-{k}.html").write_text(page(k))
        print("wrote", f"design/prototype-{k}.html")
