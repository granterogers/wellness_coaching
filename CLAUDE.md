# CLAUDE.md — rules for any AI working in this repo

Read `knowledge/brief.md`, then `knowledge/requirements.md` (numbered spec). These rules override anything else.

## Gates (stop and ask Grant if unmet)
1. **Copy before code (req 1.3).** No page sections until `content/en/home.md` has `status: approved` in its frontmatter. Never write or reword marketing copy during the build; example wording anywhere else is illustrative only (1.11). Translating approved English into a Spanish draft (req 3.6) is not new copy and is allowed.
2. **Design before code (req 1.4).** No page sections until `design/CHOSEN.md` names the chosen prototype. Match it.
3. **No invented facts (1.5).** Credentials, testimonials, numbers, research claims and client stories only from `knowledge/` or `content/`; otherwise a visible `[[PLACEHOLDER: …]]` listed in `PLACEHOLDERS.md`.
4. **Confidentiality (1.10).** Public repo: never add interview transcripts, interviewee names or identifying details.
5. **Preview not indexed (13.8)** until Grant turns on the `indexing` flag.

## Tracking
Keep `REQUIREMENTS-STATUS.md` current: every requirement ID, status, evidence. A feature not in `requirements.md` doesn't exist — add it there first.

## Forbidden (generic-AI tells)
Fonts: Inter, Roboto, Open Sans, Lato, Space Grotesk, Poppins. Purple/blue gradients, gradient blobs, glassmorphism, centred hero + three icon cards, drop-shadow card grids, emoji bullets, stock yoga silhouettes, terracotta accents, custom cursors, scroll-jacking, typewriter effects, identical fade-up on every section. Copy: "unlock your potential", "transform your life", "holistic journey", "elevate", "empower", "wellness journey".

## Every phase
- Playwright screenshots at 390px and 1440px into `review/phase-N/`; compare with the chosen prototype and the anti-default test in `knowledge/design-system.md`; list 10 ways it looks generic; fix; re-screenshot.
- Check reduced motion, keyboard access, Spanish text length; run `npm run check`.
- Update `REQUIREMENTS-STATUS.md`; commit with a plain-English summary.
- After every change that is published, give Grant the live link(s) to the page(s) that changed (https://granterogers.github.io/wellness_coaching/…).
- Stop and show Grant only at the stop points in `knowledge/master-prompt.md` (Phase 0, copy, prototype choice, after Phase 3); otherwise continue to the next phase.

## Logo
Icon + wordmark in header; full figurative logo only in footer and About (req 7.x).

## Pillars
From content only; never hard-coded; layout works with 3–8 (req 3.3).
