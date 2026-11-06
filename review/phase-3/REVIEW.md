# Phase 3 review — homepage

Screenshots: `en-*`, `es-*`, `enabout-*`, `enbook-*`, `esabout-*` at 390px and 1440px, light and dark.
Compared with `design/prototype-d.html` (design/CHOSEN.md): same layout, palettes, pacer, pillar columns and timeline.

## Ten ways it could still look generic (and what was done)

1. **The empty hero photo dominates the first scroll.** Unavoidable until P01/P02 exist; the placeholder is soft and labelled. Real photos are the single biggest upgrade (PLACEHOLDERS.md).
2. **Pill buttons** are a common wellness/SaaS look. Kept (Grant approved them in D); the fill-slide hover keeps them from feeling stock.
3. **Numbered principles** ("1, 2, 3") are an editorial habit. Kept but set as italic serif numerals in the accent colour, not icons or cards.
4. **FAQ accordion with "+"** is standard. Kept for usability (native `<details>`, works without script).
5. **"Included" chips** look like tags in any template. Kept small and outlined; could become a plain sentence if Grant prefers.
6. **Every section had the same padding rhythm.** Recognition now uses a sticky still-life beside the statements; the night section is taller; the voice section is compact.
7. **Dark closing band** is a common pattern. Made ours with the orbit line and warm "electron", and the contact options as a plain list.
8. **Six identical placeholder panels in the pillars.** Each pillar gets its own warm tint; real photos will finish the job.
9. **Centred mobile pacer with left-aligned caption** looked unfinished. Fixed: caption centred under the circle on mobile.
10. **Spanish line breaks** ("500 / %"). Fixed with a non-breaking space; no overflow in nav, buttons or hero at 360–1440px.

## Anti-default test (design-system.md)

1. Recognisable without the logo? Yes: breath pacer, orbit motif, pillar columns with practices and reasons, offer-first copy.
2. Forbidden patterns: none (no Inter/Roboto, no gradients blobs, no glassmorphism, no centred hero + icon cards, no shadow card grids, no emoji).
3. Anything only there because templates have it? The "Included" chips are the closest; flagged above.
4. Who it's for and what changes within 10 seconds? Hero: science-based, built around your life; subhead names the practices, the 3–6 months, and "busy people who know what to do".

## Checks

- `npm run check`: types, content schemas, internal links, placeholders — pass.
- Keyboard: skip link first; header, theme, language, CTAs, pillar row (scrollable region), FAQ, contact all reachable.
- Reduced motion: pacer stops scaling (opacity cue only); headline reveal off.
- Spanish text length: no horizontal scroll at 360, 390, 1440px.
- Mobile CTA bar: hidden over the hero and over the closing section, visible in between.
