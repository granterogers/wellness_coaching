# Project brief — read this first

Last updated: 4 November 2026. This file is the single source of truth. Any AI assistant should read it before doing anything else, then the other files in `knowledge/`.

## What this is

A credibility and portfolio website for Grant Rogers' personalised 1:1 wellness coaching. A place to send people, not a sales funnel.

## Decisions made

| Topic | Decision |
|---|---|
| Brand name | "Grant Rogers" for now (final brand name undecided) |
| Purpose | Credibility / portfolio site to send people to |
| Audience | Men and women equally |
| Positioning | "Scientist turned practitioner" — hero line and backbone of About (Grant's decision) |
| Offer | One flagship 1:1 programme, 3–6 months, fully online |
| Pillars | Flexible draft — see `pillars-draft.md`; must be easy to change later |
| Sexual wellbeing | Covered inside one pillar, never the headline |
| Pricing | Not shown; "Book a conversation" |
| Languages | English + Spanish, switchable; Spanish reviewed by a native speaker |
| Design | See `design-system.md` (light "field notebook" direction recommended by research; final direction chosen from 3 prototypes) |
| Logo | Grant's atom + meditator + snake logo, vectorised in `assets/brand/`; interim usage rules in `design-system.md`; to be refined (see `roadmap.md`) |
| Build order | Copy approved → prototype chosen → build (gates in `CLAUDE.md`) |
| Sharing the preview | Only after the minimum viable photo set is in |
| Signature interaction | Breath pacer (see `design-system.md`) |
| Voice | A short audio clip of Grant's voice is a planned feature |
| Hosting (now) | Free preview on GitHub Pages: `granterogers.github.io/wellness_coaching`. No domain, email or payments until Grant is satisfied with the site |
| Hosting (launch) | Cloudflare Pages + own domain |
| Tax / legal | Grant is UK tax resident. UK rules only (UK GDPR, UK consumer law). No Spanish legal pages |
| Account sign-ups | Done later by a browser agent (Claude in Chrome / Cowork) where possible; Grant handles logins, codes and payment details |

## Still needed from Grant

- A contact email to use on the preview (booking fallback, requirement 11.2)

- Photos (see shot list in `design-system.md`)
- Credentials: trainings (style, hours, provider), degrees, published research
- Client quotes, with permission
- Voice clip recording (20–30 seconds)
- More interviews (5 done; see `client-language.md`)

## Files

- `../CLAUDE.md` — hard rules and gates for any AI working in the repo
- `copywriting-brief.md` — how copy is written and approved before building
- `client-language.md` — anonymised phrases from interviews, for wording only (does not shape the offer or positioning)
- `offer.md` — the offer, programme phases, differentiators
- `pillars-draft.md` — current draft pillars (editable)
- `voice-and-messaging.md` — tone, key messages, words to use and avoid
- `scope-and-boundaries.md` — coaching scope and referral rules
- `requirements.md` — numbered specification of every feature (the build contract)
- `design-system.md` — research-backed design direction, palettes, type, motion, photography
- `master-prompt.md` — the short prompt for Claude Code; phases mapped to requirement IDs
- `roadmap.md` — status, next steps, future ideas
