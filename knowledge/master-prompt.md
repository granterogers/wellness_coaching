# Master prompt for Claude Code

Paste everything inside the block into Claude Code, opened in a local clone of this repo.

**Before using it:** `content/en/home.md` must be approved and a prototype in `design/` marked `chosen` (see `CLAUDE.md` → Gates). The short, always-on rules live in `CLAUDE.md`, which Claude Code reads automatically; this prompt holds the detail.

```
You are a senior product designer and front-end engineer building a premium, bilingual (English/Spanish) personal website for Grant Rogers' 1:1 wellness coaching, in this repo (granterogers/wellness_coaching). It must look like a top independent studio built it, not a generic AI template. Work in small, reviewable phases and commit after each one.

## 0. Before anything else
- Read CLAUDE.md and obey its gates. If copy isn't approved or no prototype is chosen, stop and tell me.
- Then critique this prompt: list gaps, contradictions, and places you'd likely produce generic output. Propose fixes and wait for my OK before Phase 1.

## Sources of truth — never invent facts
- knowledge/brief.md (read first), knowledge/copywriting-brief.md, knowledge/client-language.md, knowledge/offer.md, knowledge/pillars-draft.md, knowledge/voice-and-messaging.md, knowledge/scope-and-boundaries.md, knowledge/design-system.md
- Match the prototype in design/ marked chosen.
- Use the approved copy in content/ word for word. Do not write marketing copy yourself.
- Where information is missing (photos, credentials, publications, testimonials, booking URL, WhatsApp number, email), insert visible placeholders like [[PLACEHOLDER: booking link]] and list every one in PLACEHOLDERS.md. Never fabricate credentials, testimonials, statistics or research claims.

## 1. Stack (explain it in README.md for a non-developer on Windows)
- Astro (latest stable), static output; Tailwind CSS v4; GSAP (free, incl. ScrollTrigger and SplitText) and Lenis, loaded only where used.
- Astro i18n: locales en and es, routes /en/ and /es/; the root gently suggests Spanish to Spanish-language browsers, never auto-redirects.
- astro:assets for images (AVIF/WebP, responsive sizes); @astrojs/sitemap with i18n.
- Deploy NOW to GitHub Pages via a GitHub Actions workflow, at granterogers.github.io/wellness_coaching (set Astro's site and base accordingly; all links and assets must work under that base path). Make it a one-line config change to move to Cloudflare Pages and a custom domain later; document both in DEPLOY.md.

## 2. Content architecture (editable by a non-developer on github.com)
- content/en/ and content/es/: one file per section (hero, problem, approach, pillars, programme, about, proof, faq, cta, footer, legal). Use Astro content collections with schemas so missing fields fail the build loudly.
- Pillars come from content files only. Adding, removing or renaming a pillar must need no code change; the layout must handle 3–8 pillars gracefully.
- content/shared/site.json: name, email, WhatsApp, booking link, social links, credentials, publications (title, journal, year, DOI), feature flags.
- Missing Spanish copy: write a careful draft in neutral Castilian Spanish, consistent with the voice file, mark it translation_status: draft, and list it in PLACEHOLDERS.md.

## 3. Pages (mirrored under /en/ and /es/)
Home, Programme, About, Approach (evidence notes), Book, Privacy (UK GDPR), Terms, 404. The language switcher links to the equivalent page. hreflang and canonical tags on every page.

## 4. Home page sections, in order
1. Hero: headline mixing roman and italic serif, leading with "scientist turned practitioner", worded in plain language (see knowledge/client-language.md for wording); one-line subhead; primary CTA "Book a conversation"; secondary "How it works". Large portrait (16:9 desktop, 4:5 mobile) plus the ambient breath pacer.
2. Recognition: "You know what to do. It just doesn't stick." plus three short observations.
3. Approach: three principles (minimum effective dose; reasons, not rituals; built for independence), each with a one-line mechanism.
4. Pillars: from content files. Desktop: large numbered typographic index, hover/focus reveals description and example practice. Mobile: accordion. Never mention sexual wellbeing in the hero, meta description or social-share image.
5. Programme: Baseline, Stabilise, Build capacity, Integrate. Desktop: pinned stepped timeline with mono labels ("PHASE 01 / BASELINE"). Mobile: vertical stepper, no pinning. Then: 3–6 months · online · 1:1 · check-ins · recordings. No prices: "Investment is discussed on our call, once we know it's a fit."
6. About: "Scientist turned practitioner." Editorial portrait, short story, "lab notebook" fact list in mono. Placeholders where unknown.
7. Voice: a 20–30 second audio clip of Grant guiding a breath, with play button and transcript; never autoplays. Placeholder audio until supplied.
8. Proof: up to three first-name client stories (before / what we did / now), plus single quotes scattered elsewhere. Must look good with only one or two.
9. Free practice: email capture for a Yoga Nidra recording, behind a feature flag, off by default.
10. FAQ: accessible accordion plus FAQPage structured data. Include: is this therapy, cost, time commitment, travel and time zones, experience needed, session language, what happens on the call.
11. Final CTA: dark "night" section: "Book a conversation: 30 minutes, no pressure, just clarity." Booking link plus email plus WhatsApp.
12. Footer: navigation, language switch, contact, scope disclaimer line, legal links, year.

## 5. Design system
Implement knowledge/design-system.md as CSS custom properties plus Tailwind theme, using the palette of the chosen prototype; keep the other palettes as alternate themes previewable with ?theme=a|b|c, Newsreader / Hanken Grotesk / IBM Plex Mono self-hosted via @fontsource with latin-ext for Spanish, fluid type scale, 12-column grid, hairline rules, figure captions in mono.
Logo (interim): header = assets/brand/icon.svg plus a "Grant Rogers" wordmark in Newsreader; favicon = icon.svg; Apple touch icon = icon-180.png. The full figurative logo (logo-currentcolor.svg) appears only in the footer and About, never in the hero.
FORBIDDEN: see CLAUDE.md. Apply the anti-default test in design-system.md to every section.

## 6. Imagery
src/assets/photos/ with intentional typographic placeholder panels (palette texture tone, mono label like "FIG. 01 — PORTRAIT, PENDING", thin rule; never grey boxes or stock) until real photos arrive; list required crops in PLACEHOLDERS.md. Meaningful alt text in both languages.

## 7. Motion
- Breath pacer exactly as specified in design-system.md: 4s in, 6s out; tap/click starts a 60-second guided cycle; pausable; keyboard accessible; aria-live updates; reused in the Breathe pillar.
- Headlines: line-by-line masked reveal, once. Sections: opacity plus small translate, varied by purpose, never identical everywhere.
- Images: clip reveal, parallax max 8%. Programme timeline pinned only at 1024px and wider. Lenis only on desktop pointer devices.
- prefers-reduced-motion: disable all of the above via a single motion utility; content appears immediately.
- Animate only transform and opacity; no layout shift.

## 8. Designed details
Designed 404 page (a short breathing prompt), styled form success and error states in both languages, sticky mobile CTA bar after the hero, generated typographic social-share images per page and language, favicon set.

## 9. Integrations (placeholders for now)
Booking link [[PLACEHOLDER]] (Cal.com later), WhatsApp click-to-chat https://wa.me/[[PLACEHOLDER]] with prefilled message, contact form endpoint placeholder (Tally or Formspree later) with honeypot, cookieless analytics only. No Google Analytics, pixels or anything requiring a cookie banner.

## 10. SEO
Per-page, per-language title and description, social-share tags, canonical, hreflang (en, es, x-default), sitemap, robots.txt, structured data: Person, ProfessionalService (online, worldwide, en/es), FAQPage. One h1 per page.

## 11. Quality bars — check before finishing each phase
- Lighthouse mobile 95+ in all four categories; LCP under 2s; CLS under 0.05; home page JS under 120KB gzipped.
- WCAG 2.2 AA: contrast, visible focus, skip link, keyboard navigation for accordions, pacer, menu and audio player.
- No horizontal scroll at 360, 390, 768, 1024, 1440, 1920px; tap targets 44px+; Spanish text (20–30% longer) must not overflow.
- VISUAL SELF-REVIEW as defined in CLAUDE.md, using Playwright screenshots at 390px and 1440px.

## 12. Phases (commit after each, summarise changes)
1. Scaffold: Astro, Tailwind, i18n, content collections, tokens, fonts, GitHub Pages workflow; README for Windows.
2. Layout primitives, header and footer, language switch, logo.
3. Home sections with placeholder imagery, copy from content/ or knowledge/, Spanish drafts.
4. Motion layer and breath pacer with reduced-motion fallbacks.
5. Secondary pages, forms, audio player, legal pages, SEO.
6. Performance and accessibility audit, fixes, DEPLOY.md, PLACEHOLDERS.md, CONTENT-EDITING.md.
Ask before adding any dependency not listed here. Work one phase at a time; at the end of each, re-read CLAUDE.md and the relevant section of this prompt before continuing.
```
