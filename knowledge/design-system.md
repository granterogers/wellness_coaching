# Design system

Source: design research, November 2026 (award-recognised wellness and health sites, NN/g usability research, Anthropic's frontend guidance). Treat these as the starting direction; the final look is chosen from three prototypes.

## Concept

"A scientist's field notebook for the nervous system." Editorial, calm, precise, warm. Light pages for reading and explaining; dark "night" sections for the restorative moments (Restore, Yoga Nidra, final call to action).

## What the research found

- The best sites in this space use restraint, not darkness: an off-white page, near-black type, one disciplined accent, real photos of real people and slow, purposeful motion.
- Visitors trust photos of the actual practitioner and ignore stock photos.
- Visitors need to grasp who it's for and what changes within about 10 seconds.
- AI-made sites are recognisable: Inter/Roboto/Space Grotesk fonts, purple gradients, centred hero plus three icon cards, gradient blobs, glassmorphism, emoji bullets, "unlock your potential" copy, and lately cream + terracotta as a default "tasteful" look.

## Reference sites (what to borrow)

| Site | Borrow |
|---|---|
| [Frequency Breathwork](https://frequencybreathwork.com) | Two-colour discipline; motion that follows the rhythm of breath |
| [Kasia Siwosz](https://www.kasiasiwosz.com) | Solo practitioner, premium, no prices; low-pressure CTA; large editorial portrait |
| [Function Health](https://www.functionhealth.com) | Serif headlines mixing roman and italic; proof spread across the page |
| [Neko Health](https://www.nekohealth.com) | One signature visual idea; real-member photography |
| [Early (Peter Attia)](https://earlymedical.com) | Confident credentials paragraph |
| [Othership Learn](https://www.othership.us/learn) | Evidence notes as content |

## Palettes

**Caution — the cream trap.** Warm cream/off-white backgrounds with serif headlines are now a recognised AI-default "tasteful" look. Palette A is therefore shifted to a cooler, neutral stone and must earn its place in the prototype comparison rather than being assumed.

**A — Field Notes (neutral stone)**
- Paper `#EEEEEA` (background), Stone `#E2E2DC` (alternate sections), Ink `#15191A` (text), Graphite `#5A5F5C` (secondary text), Rule `#CBCBC3` (hairlines)
- Night `#101415` (dark sections), Moonlight `#E6E6E0` (text on Night)
- Accent: Deep Kelp `#2F4A40` (links, buttons). Signal: Phosphor `#D4F06A` (tiny data marks, breath pacer glow, focus rings on dark — at most ~2% of the surface)

**B — Night Practice (dark)**: `#0E1112` base, `#171B1C` surface, `#ECE7DD` text, `#9A9D97` muted, brass `#C9A56A` accent.
- Derived in Phase 0 so the prototype is complete: Rule `#2C3233` (hairlines), Rule-strong `#646A69` (control outlines), "night" sections go one step deeper to `#080A0B`; buttons are brass fill with base-colour text; focus rings brass.

**C — Tidal (cool, non-cream)**: Mist `#E6EBEA` background, Deep Water `#13232A` text and dark sections, Slate Sea `#2E5E66` accent, Sand `#D9C27A` signal (sparingly).
- Derived in Phase 0 so the prototype is complete: Shallows `#D8E0DF` (alternate sections), Current `#4A5C61` (secondary text), Rule `#B9C5C4` (hairlines), Rule-strong `#728287` (control outlines), Mist `#E6EBEA` as text on Deep Water, `#A9B8B8` muted text on Deep Water. On dark sections links and focus rings use Sand, never Slate Sea.

A also gets Rule-strong `#7F847F` for control outlines (accordion and input borders need 3:1 against Paper).

### Contrast rules (checked, WCAG 2.2)

| Pair | Ratio | Use |
|---|---|---|
| A Ink on Paper / Kelp on Paper / Graphite on Paper | 15.2 / 8.3 / 5.6 | all text sizes |
| A Phosphor on Night | 14.5 | marks and focus rings on dark |
| A **Phosphor on Paper** | **1.1** | **never** — invisible; focus rings on light are Kelp |
| B Text / Muted / Brass on base | 15.4 / 6.9 / 8.2 | all text sizes |
| C Deep Water on Mist / Slate Sea on Mist / Current on Mist | 13.4 / 6.0 / 5.8 | all text sizes |
| C Sand on Deep Water | 9.2 | links and marks on dark |
| C **Sand on Mist** | **1.5** | **never** as text or an outline |
| C **Slate Sea on Deep Water** | **2.2** | **never** as text |
| Rules (hairlines) on their background | ~1.4 | decoration only; anything clickable also needs a Rule-strong outline, an underline or a fill |

## Anti-default test (apply to every prototype and build)

A design fails if a viewer could swap the logo and use it for any other coach. Check:
1. Would it still be recognisable as Grant's with the logo removed? (Signature: breath pacer, mono "lab notebook" labels, figure captions, real photos.)
2. None of the forbidden patterns (see `CLAUDE.md`).
3. Is anything there only because templates usually have it? Remove it.
4. Does the hero say who it's for and what changes within 10 seconds?

### Known generic-output risks (Phase 0) and the counter-move

| Where an AI drifts to a template | Counter-move |
|---|---|
| Hero = big serif headline left, photo right, two buttons | Build the hero around the pacer and its figure caption ("FIG. 00 — RESTING BREATH, 4s IN / 6s OUT"); the photo carries a caption like a plate in a field notebook |
| Recognition (3) and Approach (3) become two rows of three cards | 5.2 as a short typeset list set against P13; 5.3 as numbered margin notes beside P05. Never the same layout twice |
| Pillars as "01 — Breathe" numbered rows (the stock editorial index) | Each pillar gets a position on an orbit line beside the list and its own mono "practice" line, so the index reads as a diagram, not a menu |
| Mono labels sprinkled everywhere as decoration | Mono only where it carries information: phase numbers, figure captions, facts, the pacer. If a label says nothing, delete it |
| Dark final-CTA band with a centred heading and button | Night section uses P16 and the orbit; the CTA sits off-centre with the contact options as a plain list |
| FAQ with plus icons in a boxed list | Numbered questions (Q.01) on hairlines, answers in body type |
| Copy any coach could use ("personalised", "sustainable", "real life") | The copywriting brief's competitor test, and specifics from `offer.md` and `credentials.md` |
| Same fade-up on each section | 9.6: each entrance chosen for its section (line reveal, clip, draw-on of the orbit, none) |

## Typography (free Google Fonts)

- Display: **Newsreader** — mix roman and italic in one headline, e.g. "Science-minded. *Body-led.*" (example only)
- Body/UI: **Hanken Grotesk** 400/500/600
- Labels/data: **IBM Plex Mono** 400, uppercase, 0.08em tracking, 12–13px — e.g. `PHASE 02 / STABILISE`, "Fig. 02 — Exhale bias"
- Fluid scale: display 56–112px, H2 36–64px, H3 22–28px, body 17–19px / 1.6, lines 60–72 characters

## Layout

12-column grid, 1200–1360px content width, 24px gutters; 4 columns and 20px margins on mobile. 8px spacing scale, generous section padding. Asymmetric compositions (portrait in columns 1–5, text in 7–12). Hairline rules instead of shadowed cards.

## Motion

1. Motion follows breath: 0.8–1.4s durations, soft easing, nothing bounces.
2. One signature element — the **breath pacer** (below).
3. Headlines reveal line by line, once.
4. Gentle smooth scrolling on desktop only; the four-phase programme timeline pins on desktop, stacks on mobile.
5. Images: subtle clip reveal, parallax at most 8% (requirement 9.7).
6. Avoid: custom cursors, scroll-jacking, typewriter effects, particles, 3D blobs, autoplay sound.
7. Everything switches off when the visitor's device requests reduced motion.

## Breath pacer (signature interaction)

An SVG ring that expands over 4 seconds (in) and contracts over 6 seconds (out), with localised "in"/"out" labels. Ambient in the hero; a tap or click starts "60 seconds with me" — a guided minute with a gentle count and a short completion message. Pausable, keyboard-accessible, announced to screen readers. Reused in the Breathe pillar. Static under reduced motion.

## Voice feature

A 20–30 second clip of Grant guiding a breath, with a play button and transcript, on the home page after the About teaser (requirement 5.7) and hidden until the file exists. Never autoplays.

## Logo usage (interim)

The current figurative logo is under review (reads as male; some AI-generation artefacts — see `roadmap.md`). Until it's refined:
- Header and favicon: `icon.svg` (snake + orbit) plus a typographic wordmark "Grant Rogers" in Newsreader.
- The full figurative logo appears only in the footer and the About section, never in the hero.
Files are in `assets/brand/`.

## Photography

Natural light, real settings, slightly warm grade. ~70% calm and environmental, ~30% close detail. Mostly colour, with a black-and-white set for About and night sections. No stock, no logos on clothing. Plain tonal wardrobe (ink, stone, olive).

Shot list (a wish list for the photo shoot; the slots the site actually uses are the 18 in `photo-slots.md`, which wins on any difference):
1. Hero portrait, horizontal 16:9 with space for text — by a window, looking just off camera
2. Hero portrait, vertical 4:5 crop for mobile
3. Direct-to-camera portrait, chest up (About)
4. Black-and-white profile portrait in side light
5. At a desk with notebook or data, hands writing ("scientist")
6. Over-the-shoulder on a video call (shows it's online and 1:1)
7. Hand on ribs or abdomen, eyes closed (breath)
8. Seated meditation, wide, lots of empty space
9. Yoga Nidra rest position with blanket, from above
10. Mobility sequence, three frames
11. Movement outdoors, small in a wide landscape
12. Retreat group from behind, facing the sea (with consent)
13. Hands with an instrument (harmonium, bowl)
14–16. Textures: morning light through linen, water surface, stone or bark
17. Walking away down a path
18. Coffee and notebook on a table ("real life")
19. Wearable showing heart-rate data, no brand logos
20. Candid laughing moment
21–25. Details: feet on wooden floor, hands in mudra, watch placed on a book, tea

### Minimum viable photo set (before sharing the preview with anyone)

1. Hero portrait (horizontal, with a vertical crop)
2. About portrait
3. One practice shot (meditation, breath or mobility)
4. One working shot (desk or video call)
5. One texture or landscape

Phone + tripod + window light is enough.

### Placeholders until then

Descriptive placeholders: each slot shows its brief from `photo-slots.md` (subject, framing, setting, mood) in a designed panel. Never grey boxes or stock photos.

AI may enhance real photos (light, colour, clutter removal, extended backgrounds, upscaling) and generate non-person textures. It must not generate realistic images of Grant: that undermines trust and, under EU AI Act Article 50, would need visible labelling.
