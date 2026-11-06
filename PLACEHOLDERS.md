# Placeholders

Everything on the site that is waiting for Grant. `npm run check` fails if a `[[PLACEHOLDER` in the site is missing from this list (requirement 15.6).

| What | Where | What Grant needs to supply |
|---|---|---|
| Voice clip | `content/en/home.md` → Voice | 20–30 second recording of the script in that section, as `src/assets/audio/voice-en.mp3` (Spanish later: `voice-es.mp3`) |
| Client stories | `content/en/home.md` → Proof | Up to three stories (first name, before / what we did / now) with written permission; then switch on the `testimonials` flag |
| Photos P01–P18 | Every photo slot (see `knowledge/photo-slots.md`) | Real photos; the minimum set before sharing the preview is listed at the end of `photo-slots.md` |
| Booking link | "Book a conversation" buttons | A booking URL (e.g. Cal.com) when ready; until then the Book page asks people to email |
| Spanish translation | `content/es/home.md`, `content/es/pages.md` (`translation_status: draft`) | A native Spanish speaker reviews the draft; then set `translation_status: approved` and the "Traducción en revisión" note disappears |
| Voice clip player | Home → voice section | Until `voice-en.mp3` exists the section shows "Recording to come" with the transcript |
