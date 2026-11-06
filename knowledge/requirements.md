# Requirements — numbered specification

Every feature has an ID. Claude Code tracks each one in `REQUIREMENTS-STATUS.md` (see 1.6). Nothing is done until its ID is marked `done` with evidence. To add or drop a feature, edit this file — never just ask in chat.

Priority: **M** = must have for the preview · **S** = should have for the preview · **L** = later (built behind a flag or documented, not active).

---

## 1. Process and gates

| ID | Requirement | P |
|---|---|---|
| 1.1 | Read `CLAUDE.md`, `knowledge/brief.md` and this file before any work | M |
| 1.2 | Phase 0: critique `master-prompt.md` and this file (gaps, contradictions, generic-output risks); apply clear fixes directly and list them; list anything that needs Grant's decision and wait for his answers. Allowed before gates 1.3–1.4 are met | M |
| 1.3 | Copy gate: no page sections built until `content/en/home.md` has `status: approved` in its frontmatter; pages other than Home also need `content/en/pages.md` approved (drafted and reviewed with `home.md`) | M |
| 1.4 | Design gate: no page sections built until `design/CHOSEN.md` names the chosen prototype file | M |
| 1.5 | No invented facts: credentials, testimonials, numbers, research claims and client stories only from `knowledge/` or `content/`; otherwise a visible `[[PLACEHOLDER: …]]` listed in `PLACEHOLDERS.md` | M |
| 1.6 | Maintain `REQUIREMENTS-STATUS.md`: every ID in this file with status (`todo` / `done` / `partial` / `blocked` / `later`) and evidence (file path or screenshot). Update at the end of every phase | M |
| 1.7 | Visual self-review each phase: Playwright screenshots at 390px and 1440px saved to `review/phase-N/`; compare with the chosen prototype; list 10 ways it looks generic; fix; re-screenshot | M |
| 1.8 | One commit (or more) per phase, with a plain-English summary | M |
| 1.9 | Ask Grant before adding any dependency not listed in 2.x | M |
| 1.10 | Confidentiality: never add interview transcripts, interviewee names or identifying details (public repo) | M |
| 1.11 | Copy written in this file or the master prompt (e.g. example headlines) is illustrative only; approved copy in `content/` always wins | M |

## 2. Tech stack and hosting

| ID | Requirement | P |
|---|---|---|
| 2.1 | Astro (latest stable), static output | M |
| 2.2 | Tailwind CSS v4 (via `@tailwindcss/vite`); design tokens as CSS custom properties | M |
| 2.3 | GSAP (incl. ScrollTrigger, SplitText) and Lenis, from npm, loaded only on pages that use them | M |
| 2.4 | astro:assets for images (AVIF/WebP, responsive srcset) | M |
| 2.5 | @astrojs/sitemap with i18n | M |
| 2.6 | Fonts self-hosted via @fontsource (Newsreader, Hanken Grotesk, IBM Plex Mono), subsets latin + latin-ext | M |
| 2.7 | Social-share image generation at build with `satori` + `@resvg/resvg-js` (approved by Grant, Phase 0) | S |
| 2.8 | Playwright (dev only) for screenshots and smoke tests; `lighthouse` (dev only) for 15.1; `@astrojs/check` + `typescript` for the types check (all approved by Grant, Phase 0) | M |
| 2.9 | GitHub Actions workflow builds and deploys to GitHub Pages at `granterogers.github.io/wellness_coaching`; Astro `site` and `base` set so every link and asset works under `/wellness_coaching/`. Deploys from `main`; Claude merges the working branch into `main` at each stop point (Grant, Phase 0). The three design prototypes stay published at `/wellness_coaching/design/prototype-a.html` (and `-b`, `-c`) after the build, for comparison | M |
| 2.10 | `DEPLOY.md` explains enabling Pages ("Settings → Pages → Source: GitHub Actions"), and the later move to Cloudflare Pages + custom domain as a config change | M |
| 2.11 | Everything runs in the cloud: built with Claude Code on the web and deployed by GitHub Actions — Grant installs nothing. Scripts: `npm run build`, `npm run check` (types + content schemas + internal link check + placeholder check per 15.6; link and placeholder checks are small in-repo scripts, not extra dependencies), `npm run shots` (screenshots) | M |
| 2.12 | No backend, no database, no cookies, no tracking during the preview | M |

## 3. Content architecture

| ID | Requirement | P |
|---|---|---|
| 3.1 | `content/en/home.md` is the approved copy document (one file, one heading per section). The build reads it directly or Claude Code converts it into collection files **verbatim** — no rewording | M |
| 3.2 | Astro content collections with schemas so missing required fields fail the build | M |
| 3.3 | Pillars loaded only from content; renaming, adding or removing one needs no code change; layout works with 3–8 pillars | M |
| 3.4 | `content/shared/site.json`: name, email, WhatsApp, booking URL, social links (Instagram, LinkedIn), credentials and publications taken only from confirmed items in `knowledge/credentials.md`, feature flags | M |
| 3.5 | Feature flags (default in brackets): `freePractice` (off), `voiceClip` (on: shows the audio placeholder until the file exists — Grant, copy round 2), `testimonials` (off until real quotes), `spanish` (on), `contactForm` (off until an endpoint exists), `indexing` (off — see 13.8) | M |
| 3.6 | Spanish copy: if `content/es/home.md` is missing, generate a careful draft in Spain Spanish, addressing the reader as "tú", with `translation_status: draft`, listed in `PLACEHOLDERS.md` | M |
| 3.7 | UI strings (nav, buttons, labels, form messages, pacer labels) in one i18n file per language | M |
| 3.8 | `CONTENT-EDITING.md`: how Grant changes text, pillars, photos and flags on github.com (no software needed), step by step, including uploading a photo to its slot | M |

## 4. Pages (each mirrored under /en/ and /es/)

| ID | Requirement | P |
|---|---|---|
| 4.1 | Home | M |
| 4.2 | Programme (phases in detail, what's included, how it works week to week) | S |
| 4.3 | About (story, credentials, "lab notebook" facts, full logo per 7.3) | S |
| 4.4 | Approach / evidence notes (reasons behind practices; sources linked) | L |
| 4.5 | Book (booking embed or fallback per 11.2) | M |
| 4.6 | Privacy (UK GDPR) and Terms — template text clearly marked "draft, not legal advice" | M |
| 4.7 | Designed 404 with a short breathing prompt | M |
| 4.8 | Root `/wellness_coaching/` sends visitors to `/en/` (static redirect). On English pages, browsers set to Spanish see a small, dismissible "Ver en español" link (dismissal remembered for the session only; no cookies); never auto-redirects to Spanish | M |

## 5. Home page sections (order as in the approved copy)

| ID | Requirement | P |
|---|---|---|
| 5.1 | Hero: headline (serif, roman + italic mix) leading with the offer — evidence-based, customised wellness practices, no woo (Grant, 6 Nov 2026); Grant's "scientist turned practitioner" story belongs in About, not the hero; subhead; primary CTA "Book a conversation"; secondary CTA "How it works" (scrolls to 5.5); portrait (16:9 desktop, 4:5 mobile); ambient breath pacer (9.1) | M |
| 5.2 | Recognition: the problem in three short observations, never laid out as three equal cards or icon columns | M |
| 5.3 | Approach: three principles, each with a one-line reason; a different layout from 5.2 (e.g. numbered annotations beside P05), never three icon cards | M |
| 5.4 | Pillars side by side, like columns (Grant, 6 Nov 2026): desktop = one row of columns (wraps to rows of 4 above 6 pillars), each with photo, number, name, description, example practice and its reason, all visible; under 1024px = a horizontal swipeable row with the next pillar peeking in, keyboard-scrollable. No decorative diagram. Sexual wellbeing only inside its pillar | M |
| 5.5 | Programme: four phases as one simple left-to-right timeline on desktop (line with four numbered points, text under each), a vertical stepper on mobile; nothing pinned; inclusions row; no prices ("investment is discussed on our call") | M |
| 5.6 | About teaser: portrait, short story, mono fact list, link to 4.3 | M |
| 5.7 | Voice clip (10.x), shown when `voiceClip` flag is on; until Grant's recording exists, a designed audio placeholder ("Recording to come") with the transcript stands in its place | S |
| 5.8 | Proof: up to three first-name stories (before / what we did / now) + single quotes elsewhere; looks right with 1–2; hidden while `testimonials` is off | S |
| 5.9 | Free practice email capture, flag `freePractice` | L |
| 5.10 | FAQ: accessible accordion + FAQPage structured data; questions from approved copy | M |
| 5.11 | Final CTA in a dark "night" section: booking + email + WhatsApp | M |
| 5.12 | Footer: nav, language switch, contact, scope disclaimer line, legal links, year, full logo per 7.3 | M |
| 5.13 | Sticky mobile CTA bar (<768px): appears after the hero, hides when the final CTA is in view; it replaces the header CTA on mobile | M |
| 5.14 | Header: icon + "Grant Rogers" wordmark, nav, language switch, CTA (CTA from 768px up; 5.13 carries it on mobile); condenses on scroll | M |

## 6. Design system

| ID | Requirement | P |
|---|---|---|
| 6.1 | Implement `knowledge/design-system.md`, matching the chosen prototype | M |
| 6.2 | Palette comparisons stay available as the published prototypes at `/design/` (preview only). The `?theme=a|b|c` switch is dropped: light and dark mode (6.9) replace it (Grant chose D, 6 Nov 2026) | S |
| 6.3 | Fluid type scale; serif display, sans body, mono labels as specified | M |
| 6.4 | 12-column grid (4 on mobile), 8px spacing scale, generous section padding, asymmetric compositions | M |
| 6.5 | Hairline rules instead of shadowed cards; figure captions in mono ("FIG. 02 — …") | M |
| 6.6 | **Orbit motif from the logo**, used sparingly and only where it does a job: the breath pacer, and at most one quiet line in the night section. Never as decoration without a purpose (Grant, 6 Nov 2026: the six-point orbit diagram was noise) | M |
| 6.7 | Anti-default test (design-system.md) applied to every section and recorded in the phase review | M |
| 6.8 | No forbidden fonts, colours, patterns or phrases (list in `CLAUDE.md`) | M |
| 6.9 | Light and dark mode (Grant, 6 Nov 2026): light = palette A Sage & Saffron, dark = palette C Moss & Honey. First visit follows the device setting; a visible, labelled toggle in the header lets visitors choose, remembered on that device (localStorage, no cookies) and applied before first paint (no flash). Both themes meet 14.1; "night" sections stay dark in both | M |

## 7. Brand and logo

| ID | Requirement | P |
|---|---|---|
| 7.1 | Header and favicon: `assets/brand/icon.svg` + Newsreader wordmark "Grant Rogers" | M |
| 7.2 | Apple touch icon: `assets/brand/icon-180.png`; full favicon set generated from `icon.svg` | M |
| 7.3 | Full figurative logo (`logo-currentcolor.svg`) only in the footer and on the About page (4.3); never in the hero or the home About teaser; never under 64px | M |
| 7.4 | Logo files referenced from one place, so a refined logo is a file swap | M |

## 8. Imagery

| ID | Requirement | P |
|---|---|---|
| 8.1 | Photo slots exactly as listed in `knowledge/photo-slots.md` (IDs P01–P18, fixed file names in `src/assets/photos/`); dropping a file in replaces the placeholder; `.jpg`, `.jpeg`, `.png` and `.webp` all accepted (iPhone HEIC must be exported as JPG first — explained in `CONTENT-EDITING.md`); pillar slots follow pillar IDs in content | M |
| 8.2 | **Descriptive placeholders**: each empty slot shows a soft, warm tonal panel in the palette with one short line saying what the photo will be (e.g. "Photo to come — Grant by a window, morning light"); the full brief stays in `photo-slots.md` and in the image's alt text. Correct aspect ratio so swapping in the real photo causes no layout change. Never stock, never grey boxes, no grid textures | M |
| 8.3 | Alt text in both languages from content files | M |
| 8.4 | Art direction: hero uses different crops for desktop and mobile | M |

## 9. Motion and signature interactions

| ID | Requirement | P |
|---|---|---|
| 9.1 | Breath pacer: SVG orbit/ring (per 6.6) expands 4s, contracts 6s, localised "in"/"out" labels; ambient in hero, with a visible pause control for the ambient loop (WCAG 2.2.2) | M |
| 9.2 | Tap/click starts "60 seconds with me": guided cycle with gentle count and a short completion message; pause/stop control; keyboard operable; `aria-live="polite"` updates | M |
| 9.3 | Pacer reused in the Breathe pillar | S |
| 9.4 | Under reduced motion the pacer uses no scaling: text cues and a slow opacity change only, still usable | M |
| 9.5 | Headline line-by-line masked reveal, once per page load | M |
| 9.6 | Section entrances varied by purpose (never one identical fade everywhere) | M |
| 9.7 | Image clip reveals; parallax ≤ 8% | S |
| 9.8 | No pinned or scroll-linked sections; native scroll speed and distance are never altered (no scroll-jacking, no snapping on the page) | M |
| 9.9 | Lenis smooth scroll only on desktop fine-pointer devices | M |
| 9.10 | One motion utility controls everything and honours `prefers-reduced-motion` (content appears immediately) | M |
| 9.11 | Animate only transform and opacity; zero layout shift | M |
| 9.12 | Subtle link and button micro-interactions (underline draw, fill slide); no custom cursor | S |
| 9.13 | **Mini Yoga Nidra body scan** (Grant, 6 Nov 2026): a gender-neutral figure lying down, drawn in the same thin line style as the pacer; tap to start a short guided scan (about two minutes) in which each body zone (feet, legs, hips, belly, chest, hands and arms, shoulders, face) gently lights up in turn with a short localised cue; pause/stop; keyboard operable; `aria-live="polite"` cues; under reduced motion only the highlight changes. Shown with the Restore pillar. Cue wording is copy: drafted in `content/en/practices.md` and approved by Grant before it goes live | S |

## 10. Voice feature

| ID | Requirement | P |
|---|---|---|
| 10.1 | Custom accessible audio player (play/pause, progress, time), styled to the design system; never autoplays | S |
| 10.2 | Transcript shown alongside, both languages | S |
| 10.3 | Audio file slot `src/assets/audio/voice-en.mp3` (and `-es`); the player replaces the placeholder automatically once the file exists; whole section hidden only if `voiceClip` is off | S |

## 11. Integrations and forms (preview-safe)

| ID | Requirement | P |
|---|---|---|
| 11.1 | All contact details come from `site.json`; nothing hard-coded. Preview email: `grant.e.rogers@gmail.com`. Email addresses are protected from spam-harvesting bots (e.g. assembled with JavaScript, with an accessible fallback) | M |
| 11.2 | Booking: if `bookingUrl` is empty, every "Book a conversation" leads to the Book page with an honest fallback ("Booking opens soon — email me") using the preview email; when set, a Cal.com link or embed (embed loaded only after a click) | M |
| 11.3 | WhatsApp click-to-chat (`wa.me`) with prefilled localised message; hidden while the number is empty | M |
| 11.4 | Contact form built with honeypot and localised success/error states, but hidden while `contactForm` is off; never fakes a successful submission | S |
| 11.5 | No third-party embeds that set cookies during the preview | M |

## 12. Languages

| ID | Requirement | P |
|---|---|---|
| 12.1 | Locales `en` and `es`, routes `/en/…` and `/es/…` | M |
| 12.2 | Language switcher ("EN / ES" text, not flags-only — flags may sit beside the text) links to the equivalent page; current language marked `aria-current` | M |
| 12.3 | `lang` attribute correct per page; date and number formats localised | M |
| 12.4 | Draft Spanish pages show a small, discreet "Traducción en revisión" note until approved | S |
| 12.5 | Layouts tested with Spanish text (20–30% longer): no overflow in nav, buttons or hero | M |

## 13. SEO and preview indexing

| ID | Requirement | P |
|---|---|---|
| 13.1 | Per-page, per-language title and meta description | M |
| 13.2 | Canonical + hreflang (en, es, x-default) on every page | M |
| 13.3 | Social-share tags and images per page and language (2.7) | S |
| 13.4 | Sitemap + robots.txt | M |
| 13.5 | Structured data: Person, ProfessionalService (online, worldwide, en/es), FAQPage | S |
| 13.6 | One `h1` per page; semantic landmarks | M |
| 13.7 | Sexual wellbeing never in hero, page titles, meta descriptions or share images | M |
| 13.8 | **Preview is not indexed**: while flag `indexing` is off, every page (design prototypes included) has `noindex, nofollow` and robots.txt disallows all, from the very first deploy. Flipping the flag at launch restores indexing | M |

## 14. Accessibility

| ID | Requirement | P |
|---|---|---|
| 14.1 | WCAG 2.2 AA colour contrast, including text on photos and night sections | M |
| 14.2 | Visible focus states; skip link; full keyboard support (menu, accordions, pacer, audio, language switch) | M |
| 14.3 | Tap targets ≥ 44px | M |
| 14.4 | Reduced motion honoured everywhere (9.10) | M |
| 14.5 | Screen-reader labels for icon-only controls; decorative SVGs hidden from assistive tech | M |

## 15. Performance and quality

| ID | Requirement | P |
|---|---|---|
| 15.1 | Lighthouse mobile ≥ 95 in Performance, Accessibility, Best Practices, SEO (SEO measured with `indexing` on in a local build) | M |
| 15.2 | LCP < 2.0s, CLS < 0.05 on mobile emulation | M |
| 15.3 | Home page JavaScript ≤ 120KB gzipped | M |
| 15.4 | No horizontal scroll at 360, 390, 768, 1024, 1440, 1920px | M |
| 15.5 | Tested in Chrome, Safari (iOS emulation) and Firefox; real-phone check documented by Grant | S |
| 15.6 | `npm run check` passes: types, content schemas, internal links, no `[[PLACEHOLDER` missing from `PLACEHOLDERS.md` | M |

## 16. Documentation and handover

| ID | Requirement | P |
|---|---|---|
| 16.1 | `README.md` for a non-developer: what the stack is, where the live preview is, and that everything is edited on github.com or via Claude Code on the web | M |
| 16.2 | `DEPLOY.md` (2.10) | M |
| 16.3 | `CONTENT-EDITING.md` (3.8) | M |
| 16.4 | `PLACEHOLDERS.md`: every placeholder, where it is, what Grant needs to supply | M |
| 16.5 | `REQUIREMENTS-STATUS.md` (1.6) complete at the end: every M marked `done`, every S `done` or explained | M |
| 16.6 | `LAUNCH-CHECKLIST.md`: switching on indexing, domain, booking, forms, analytics, legal review — pointing to the operations plan | S |

## 17. Out of scope for the preview

Payments, client portal/app, blog, newsletter sending, analytics accounts, cookie banner, more than two languages, any account sign-ups.
