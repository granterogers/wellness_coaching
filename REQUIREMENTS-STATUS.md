# Requirements status

Every ID in `knowledge/requirements.md` (121). Status: `todo` / `done` / `partial` / `blocked` / `later`. Updated at the end of every phase (1.6).

Last updated: Phase 3 revisions, 6 November 2026.

| ID | P | Phase | Status | Evidence / notes |
|---|---|---|---|---|
| 1.1 | M | all | done | Read CLAUDE.md, brief.md, requirements.md and all of knowledge/ (Phase 0) |
| 1.2 | M | all | done | Fixes applied and decisions D1–D5 answered (below) |
| 1.3 | M | all | done | Round 3 approved by Grant (6 Nov 2026): headline "Science-based wellness, built around your life."; `home.md` and `pages.md` `status: approved` |
| 1.4 | M | all | done | `design/CHOSEN.md` names `prototype-d.html` (Grant, 6 Nov 2026) |
| 1.5 | M | all | todo | Applies throughout |
| 1.6 | M | all | done | This file |
| 1.7 | M | all | partial | review/phase-1, phase-2, phase-3 (+ REVIEW.md) |
| 1.8 | M | all | todo | Applies throughout |
| 1.9 | M | all | todo | Applies throughout |
| 1.10 | M | all | todo | Applies throughout |
| 1.11 | M | all | todo | Applies throughout |
| 2.1 | M | 1 | done | Astro 7.4.7, `output: 'static'` — `astro.config.mjs` |
| 2.2 | M | 1 | done | Tailwind v4 via `@tailwindcss/vite`; tokens as custom properties in `src/styles/tokens.css` |
| 2.3 | M | 1 | partial | gsap + lenis installed; loaded only where used (Phase 4) |
| 2.4 | M | 1 | partial | astro:assets ready; photo component in Phase 3 |
| 2.5 | M | 1 | done | @astrojs/sitemap with en-GB/es-ES — `astro.config.mjs` |
| 2.6 | M | 1 | done | latin + latin-ext only — `src/styles/fonts.css` (from @fontsource) |
| 2.7 | S | 5 | todo | satori + @resvg/resvg-js approved (D4) |
| 2.8 | M | 1 | done | Playwright `scripts/shots.mjs`; lighthouse + @astrojs/check dev deps |
| 2.9 | M | 1 | done | `.github/workflows/pages.yml`; `site`/`base` set; prototypes kept at /design/ (`scripts/copy-prototypes.mjs`) |
| 2.10 | M | 1 | done | `DEPLOY.md` |
| 2.11 | M | 1 | done | `npm run build`, `npm run check`, `npm run shots` — `package.json`, `scripts/` |
| 2.12 | M | 1 | done | No backend, cookies or tracking; theme choice in localStorage only |
| 3.1 | M | 3 | done | Copy read word for word from `content/<lang>/home.md` — `src/lib/copy.ts` |
| 3.2 | M | 1 | done | `src/content.config.ts` (schemas fail the build; en copy must be approved) |
| 3.3 | M | 3 | done | Pillars only from content; grid uses n columns (≤6) or rows of 4 (7–8) — `src/pages/[lang]/index.astro` |
| 3.4 | M | 1 | done | `content/shared/site.json` |
| 3.5 | M | 1 | done | Flags in `site.json` (voiceClip on per Grant) |
| 3.6 | M | 3 | done | `content/es/home.md`, `content/es/pages.md` — Spain Spanish, tú, `translation_status: draft` |
| 3.7 | M | 1 | done | `src/i18n/en.json`, `es.json` |
| 3.8 | M | 6 | todo |  |
| 4.1 | M | 5 | done | `src/pages/[lang]/index.astro` |
| 4.2 | S | 5 | todo |  |
| 4.3 | S | 5 | done | `src/pages/[lang]/about.astro`: story, lab notebook, where I've taught, full logo |
| 4.4 | L | 5 | later | Not active in the preview |
| 4.5 | M | 5 | done | `src/pages/[lang]/book.astro` with honest fallback |
| 4.6 | M | 5 | todo |  |
| 4.7 | M | 5 | todo |  |
| 4.8 | M | 2 | done | Root redirect to /en/; Spanish banner removed per Grant — `src/pages/index.astro` |
| 5.1 | M | 3 | done | Hero: offer-first headline, subhead, 2 CTAs, art-directed photo slot, pacer — review/phase-3 |
| 5.2 | M | 3 | done | Statements on hairlines beside P13 — review/phase-3 |
| 5.3 | M | 3 | done | Removed at Grant's request (6 Nov 2026) |
| 5.4 | M | 3 | done | Equal columns, CSS subgrid aligns every text row; photos identical size (measured 176px / 281px) — review/phase-3 |
| 5.5 | M | 3 | done | Left-to-right timeline, vertical stepper on mobile, inclusions, price line |
| 5.6 | M | 3 | done | About teaser with P03, story, facts, link to /about/ |
| 5.7 | S | 5 | partial | Section with audio placeholder + transcript; real player in Phase 5 |
| 5.8 | S | 5 | todo |  |
| 5.9 | L | 5 | later | Not active in the preview |
| 5.10 | M | 3 | done | Native `<details>` accordion + FAQPage JSON-LD |
| 5.11 | M | 3 | done | Night section with P16, orbit, booking + email + WhatsApp |
| 5.12 | M | 2 | partial | `Footer.astro`; legal links appear when Privacy/Terms pages exist (Phase 5) |
| 5.13 | M | 3 | done | `[data-mobile-cta]`, tested: hidden over hero and final CTA |
| 5.14 | M | 2 | done | `src/components/Header.astro`; condenses on scroll; CTA from 768px |
| 6.1 | M | 2 | done | Matches prototype D — review/phase-3 |
| 6.2 | S | 2 | done | Prototypes A–D published at /design/ (`scripts/copy-prototypes.mjs`) |
| 6.3 | M | 2 | done | Fluid scale: display 44–88px, H2 36–60px, body 17–19px — `src/styles/base.css`, `components.css` |
| 6.4 | M | 2 | done | `.grid` 12/4 columns, 8px spacing tokens — `components.css` |
| 6.5 | M | 2 | done | Hairline rules throughout, no shadows — `components.css` |
| 6.6 | M | 2, 4 | done | Orbit in pacer and night section only |
| 6.7 | M | 6 | todo |  |
| 6.8 | M | 6 | todo |  |
| 6.9 | M | 2 | done | Light (A) / dark (C) tokens, device default, header toggle, localStorage, applied before paint — `tokens.css`, `Base.astro`, `src/scripts/site.ts`; review/phase-2 |
| 7.1 | M | 2 | done | Inline icon + Newsreader wordmark; favicon from icon.svg — `Header.astro`, `Base.astro` |
| 7.2 | M | 2 | done | `scripts/favicons.mjs` → public/brand (32, 180, 192, 512) + manifest |
| 7.3 | M | 2 | done | Full logo only in footer (and About page), 96px — `Footer.astro` |
| 7.4 | M | 2 | done | `src/lib/brand.ts` is the only place logo files are referenced |
| 8.1 | M | 3 | done | `content/shared/photos.json` (P01–P18), `src/components/Photo.astro` picks up `src/assets/photos/<file>.*` |
| 8.2 | M | 3 | done | Warm tonal placeholders with one short line, correct ratio — `Photo.astro` |
| 8.3 | M | 3 | done | Alt text en/es in `photos.json` |
| 8.4 | M | 3 | done | `HeroPhoto.astro`: 16:9 from 768px, 4:5 on phones, one `<picture>` |
| 9.1 | M | 4 | partial | Pacer works (4 s / 6 s, ambient, pause); motion polish in Phase 4 |
| 9.2 | M | 4 | done | Guided minute, count, completion message, pause/stop, keyboard, aria-live — tested |
| 9.3 | S | 4 | todo |  |
| 9.4 | M | 4 | done | Reduced motion: opacity only, no scaling — tested |
| 9.5 | M | 4 | todo |  |
| 9.6 | M | 4 | todo |  |
| 9.7 | S | 4 | todo |  |
| 9.8 | M | 4 | todo |  |
| 9.9 | M | 4 | todo |  |
| 9.10 | M | 4 | todo |  |
| 9.11 | M | 4 | todo |  |
| 9.12 | S | 4 | todo |  |
| 9.13 | S | 4 | done | `src/components/BodyScan.astro`, `src/scripts/bodyscan.ts`: 8 zones, breath glow, guided 2 min, pause/stop, aria-live, reduced motion |
| 10.1 | S | 5 | todo |  |
| 10.2 | S | 5 | todo |  |
| 10.3 | S | 5 | todo |  |
| 11.1 | M | 3 | done | Contact from `site.json`; email assembled in JS, readable fallback, not in page source |
| 11.2 | M | 3 | done | All "Book a conversation" → /book/ with email/WhatsApp fallback while `bookingUrl` is empty |
| 11.3 | M | 3 | done | wa.me link with localised message; hidden if number empty |
| 11.4 | S | 5 | todo |  |
| 11.5 | M | 5 | todo |  |
| 12.1 | M | 1 | done | `/en/` and `/es/` routes — `src/pages/[lang]/` |
| 12.2 | M | 2 | done | UK / Spain flags with accessible names, 44px targets, aria-current ring — `Header.astro`, `src/lib/brand.ts` |
| 12.3 | M | 2 | done | `lang` en-GB / es-ES per page — `Base.astro` |
| 12.4 | S | 3 | done | "Traducción en revisión" note on draft Spanish pages — `Base.astro` |
| 12.5 | M | 3 | done | No overflow at 360–1440px in Spanish — review/phase-3/REVIEW.md |
| 13.1 | M | 5 | todo |  |
| 13.2 | M | 5 | todo |  |
| 13.3 | S | 5 | todo |  |
| 13.4 | M | 5 | todo |  |
| 13.5 | S | 5 | todo |  |
| 13.6 | M | 5 | todo |  |
| 13.7 | M | 5 | todo |  |
| 13.8 | M | 1 | done | noindex meta while `indexing` false (`src/layouts/Base.astro`); `src/pages/robots.txt.ts` |
| 14.1 | M | 6 | todo |  |
| 14.2 | M | 6 | todo |  |
| 14.3 | M | 6 | todo |  |
| 14.4 | M | 4 | todo |  |
| 14.5 | M | 6 | todo |  |
| 15.1 | M | 6 | todo |  |
| 15.2 | M | 6 | todo |  |
| 15.3 | M | 6 | todo |  |
| 15.4 | M | 6 | todo |  |
| 15.5 | S | 6 | todo |  |
| 15.6 | M | 6 | todo |  |
| 16.1 | M | 1 | done | `README.md` |
| 16.2 | M | 6 | todo |  |
| 16.3 | M | 6 | todo |  |
| 16.4 | M | 6 | todo |  |
| 16.5 | M | 6 | todo |  |
| 16.6 | S | 6 | todo |  |

Totals: done 63, later 2, partial 6, todo 50

## Phase 0 log — fixes applied

| # | Problem found | Fix | File |
|---|---|---|---|
| F1 | Master prompt said "stop after every phase"; Grant now wants one build stop, after Phase 3 | Stop points rewritten (Phase 0, copy, prototype choice, after Phase 3) | `master-prompt.md`, `CLAUDE.md` |
| F2 | Noindex (13.8) was scheduled for Phase 5, but the site deploys from Phase 1 | 13.8 moved to Phase 1; prototypes also noindex | `master-prompt.md`, `requirements.md` 13.8 |
| F3 | Master prompt asked for status "todo", which 1.6 didn't allow | `todo` added to 1.6 | `requirements.md` 1.6 |
| F4 | Phase 0 said "propose and wait"; Grant asked for confident fixes to be applied | 1.2 and the master prompt updated | `requirements.md`, `master-prompt.md` |
| F5 | CLAUDE.md banned writing copy during the build, but 3.6 asks for a Spanish draft | Translating approved copy explicitly allowed | `CLAUDE.md` |
| F6 | Palettes B and C had only 4–5 colours, so their prototypes would be improvised; A's Phosphor fails on light (1.1:1), C's Sand on Mist (1.5:1) and Slate Sea on Deep Water (2.2:1) | Full token sets derived for B and C; contrast table with "never" pairs; Rule-strong colours for 3:1 control outlines | `design-system.md` |
| F7 | Recognition (3) and Approach (3) invite the forbidden "three cards" pattern | 5.2/5.3 forbid equal cards and require different layouts; generic-risk table added | `requirements.md`, `design-system.md` |
| F8 | Endless ambient pacer breaks WCAG 2.2.2 (moving content needs a pause) | Pause control added to 9.1 | `requirements.md` 9.1 |
| F9 | Desktop pinning could become scroll-jacking (forbidden) | 9.8: native scroll speed and distance never altered | `requirements.md` 9.8 |
| F10 | 4.8 asked a static redirect to show a suggestion (impossible on a redirect page) | Suggestion moved to English pages, session-only dismissal, no cookies | `requirements.md` 4.8 |
| F11 | Header CTA and sticky mobile CTA would both show on mobile | Header CTA from 768px up; sticky bar below | `requirements.md` 5.13, 5.14 |
| F12 | "About" for the full logo was ambiguous (page or home teaser) | About page only | `requirements.md` 7.3 |
| F13 | Photo slots fixed `.jpg`; phones produce PNG/HEIC | jpg/jpeg/png/webp accepted; HEIC export explained | `requirements.md` 8.1 |
| F14 | Parallax 6–10% (design) vs ≤8% (9.7); voice clip "in Restore" vs 5.7 on home; 25-shot list vs 18 slots | All aligned to requirements / `photo-slots.md` | `design-system.md` |
| F15 | Prototypes had no publishing rule; Astro deploy would have wiped them | Self-contained, noindex, kept at `/design/` after the build | `design/README.md`, `requirements.md` 2.9 |
| F16 | Link/placeholder checks would need new dependencies | Small in-repo scripts | `requirements.md` 2.11 |
| F17 | Usable fact "15+ years in scientific research" overstated the CV line (research **and** GIS and training) | Source wording restored | `credentials.md` |
| F18 | Past clients' first names in a public file (1.10) | Names removed (still in git history) | `roadmap.md` |
| F19 | Voice file's "words that resonate" (nervous-system regulation, evidence-informed…) clash with words clients never use | Plain word in headlines/buttons; term once in body, explained. Pillars need an example practice for 5.4 | `copywriting-brief.md` |
| F20 | README still described `index.html`; images README pointed to a different photo folder | Both updated | `README.md`, `assets/images/README.md` |

## Phase 0 decisions — all approved by Grant, 4 November 2026 (recorded in `requirements.md`, `copywriting-brief.md`, `credentials.md`)

- **D1 Copy beyond the home page.** The copy gate covers only `home.md`, but Programme (4.2), About (4.3), Book (4.5), 404 (4.7) and meta descriptions (13.1) need words, and the build may not write marketing copy. Recommended: draft `content/en/pages.md` in the copy step, reviewed in the same two rounds; I write functional microcopy (buttons, form messages, alt text from photo briefs) during the build and list it in `PLACEHOLDERS.md` for review.
- **D2 Spanish variety.** "Neutral-Castilian" (3.6) is ambiguous. Recommended: Spain Spanish with "tú".
- **D3 Publishing.** Needs Settings → Pages → Source: GitHub Actions (Grant's click). Pages deploys only from `main` by default; recommended: let Claude merge the working branch into `main` at each stop point. Alternative: allow the working branch under Settings → Environments → github-pages.
- **D4 Dependencies (1.9)** implied by M requirements but not listed in 2.x: `@tailwindcss/vite` (Tailwind v4 in Astro), `@astrojs/check` + `typescript` (the "types" check), `lighthouse` (dev only, for 15.1); and for 2.7, `satori` + `@resvg/resvg-js`. Recommended: approve all.
- **D5 Credential wording.** The CV says "40+ software workshops for 100+ international clients"; the usable facts say "100+ professionals". People or organisations? Until confirmed, copy says "40+ technical workshops for international clients".
