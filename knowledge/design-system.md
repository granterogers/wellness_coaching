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

**A — Field Notes (recommended)**
- Paper `#F2EFE9` (background), Bone `#E6E0D5` (alternate sections), Ink `#15191A` (text), Graphite `#5A5F5C` (secondary text), Rule `#CFC8BB` (hairlines)
- Night `#101415` (dark sections), Moonlight `#E9E4DA` (text on Night)
- Accent: Deep Kelp `#2F4A40` (links, buttons). Signal: Phosphor `#D4F06A` (tiny data marks, breath pacer glow, focus rings on dark — at most ~2% of the surface)

**B — Night Practice (moody alternative)**: `#0E1112` base, `#171B1C` surface, `#ECE7DD` text, `#9A9D97` muted, brass `#C9A56A` accent.

**C — Mediterranean Morning (warmer)**: `#F5F0E6` lime-wash, `#1C2B35` deep sea, `#6B7046` olive, `#E4A44B` sun (sparingly).

## Typography (free Google Fonts)

- Display: **Newsreader** — mix roman and italic in one headline, e.g. "Calm you can *measure*."
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
5. Images: subtle clip reveal, parallax at most 6–10%.
6. Avoid: custom cursors, scroll-jacking, typewriter effects, particles, 3D blobs, autoplay sound.
7. Everything switches off when the visitor's device requests reduced motion.

## Breath pacer (signature interaction)

An SVG ring that expands over 4 seconds (in) and contracts over 6 seconds (out), with localised "in"/"out" labels. Ambient in the hero; a tap or click starts "60 seconds with me" — a guided minute with a gentle count and a short completion message. Pausable, keyboard-accessible, announced to screen readers. Reused in the Breathe pillar. Static under reduced motion.

## Voice feature

A 20–30 second clip of Grant guiding a breath, with a play button and transcript, in the Restore section. Never autoplays.

## Logo usage

Files in `assets/brand/`. Full logo at 64px and above; `icon.svg` (snake + orbit) below that and for the favicon.

## Photography

Natural light, real settings, slightly warm grade. ~70% calm and environmental, ~30% close detail. Mostly colour, with a black-and-white set for About and night sections. No stock, no logos on clothing. Plain tonal wardrobe (ink, stone, olive).

Shot list:
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

AI may enhance real photos (light, colour, clutter removal, extended backgrounds, upscaling) and generate non-person textures. It must not generate realistic images of Grant: that undermines trust and, under EU AI Act Article 50, would need visible labelling.
