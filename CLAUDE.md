# CLAUDE.md — rules for any AI working in this repo

Read `knowledge/brief.md` first. These rules override anything else.

## Gates (stop and ask Grant if a gate isn't met)
1. **Copy before code.** Do not build page sections until `content/en/home.md` exists with `status: approved`. Never write marketing copy yourself during the build.
2. **Design before code.** Do not build until a prototype in `design/` is marked `chosen`. Match it.
3. **No invented facts.** Credentials, testimonials, numbers, research claims and client stories come only from `knowledge/` or `content/`. Otherwise use a visible `[[PLACEHOLDER: …]]` and list it in `PLACEHOLDERS.md`.
4. **Confidentiality.** Never add interview transcripts, interviewee names or identifying details to this repo — it is public. Only anonymised themes and short unattributed phrases (see `knowledge/client-language.md`).

## Forbidden (generic-AI tells)
Fonts: Inter, Roboto, Open Sans, Lato, Space Grotesk, Poppins. Purple/blue gradients, gradient blobs, glassmorphism, centred hero + three icon cards, drop-shadow card grids, emoji bullets, stock yoga silhouettes, terracotta accents, custom cursors, scroll-jacking, typewriter effects. Copy: "unlock your potential", "transform your life", "holistic journey", "elevate", "empower", "wellness journey".

## Every phase
- Screenshot at 390px and 1440px, compare against the chosen prototype and the anti-default test in `knowledge/design-system.md`, list 10 ways it looks generic, fix them, re-screenshot.
- Check reduced-motion, keyboard access and Spanish text length.
- Commit with a plain-English summary of what changed.

## Logo
Interim rules in `knowledge/design-system.md` → "Logo usage": icon + wordmark in the header; full figurative logo only in footer and About.

## Pillars
Loaded from content files only; never hard-coded. Layout must work with 3–8 pillars.
