# Placeholders

Everything on the site that is waiting for Grant. `npm run check` fails if a `[[PLACEHOLDER` in the site is missing from this list (requirement 15.6).

| What | Where | What Grant needs to supply |
|---|---|---|
| Voice in the breath pacer | Hero widget | Record the "Breath pacer" script in `content/en/practices.md` (1 minute) as `src/assets/audio/pacer-en.mp3` (Spanish: `pacer-es.mp3`) — after approving the script |
| Voice in the body scan | Body scan widget | Record the "Body scan" script in `content/en/practices.md` (about 2 minutes) as `src/assets/audio/bodyscan-en.mp3` (Spanish: `bodyscan-es.mp3`) |
| Voice scripts | `content/en/practices.md`, `content/es/practices.md` (`draft`) | Read and edit the scripts, then set `status: approved` |
| Client stories | `content/en/home.md` → Proof | Up to three stories (first name, before / what we did / now) with written permission; then switch on the `testimonials` flag |
| Photos P01–P18 | Every photo slot (see `knowledge/photo-slots.md`) | Real photos; the minimum set before sharing the preview is listed at the end of `photo-slots.md` |
| Calendly booking link | Book page (marked placeholder) | Your Calendly event link (e.g. `https://calendly.com/yourname/conversation`) in `bookingUrl` in `content/shared/site.json`; until then the Book page asks people to email or WhatsApp |
| Spanish translation | `content/es/home.md`, `content/es/pages.md` (`translation_status: draft`) | A native Spanish speaker reviews the draft; then set `translation_status: approved` and the "Traducción en revisión" note disappears |
