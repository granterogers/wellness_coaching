# Placeholders

Everything on the site that is waiting for Grant. `npm run check` fails if a `[[PLACEHOLDER` in the site is missing from this list (requirement 15.6).

| What | Where | What Grant needs to supply |
|---|---|---|
| Voice in the breath pacer | Hero widget | Record the "Breath pacer" script in `content/en/practices.md` (1 minute) as `src/assets/audio/pacer-en.mp3` (Spanish: `pacer-es.mp3`) — after approving the script |
| Voice in the body scan | Body scan widget | Record the "Body scan" script in `content/en/practices.md` (about 2 minutes) as `src/assets/audio/bodyscan-en.mp3` (Spanish: `bodyscan-es.mp3`) |
| Voice scripts | `content/en/practices.md`, `content/es/practices.md` (`draft`) | Read and edit the scripts, then set `status: approved` |
| Client stories | `content/en/home.md` → Proof | Up to three stories (first name, before / what we did / now) with written permission; then switch on the `testimonials` flag |
| Photos | The eight slots the site uses: P03, P04, P06, P07, P08, P10, P11, P16 (`CONTENT-EDITING.md` → Photos; briefs in `knowledge/photo-slots.md`) | Real photos; first the portrait (P03) and the four pillars (P07, P08, P10, P11) |
| Calendly booking link | Book page (marked placeholder) | Your Calendly event link (e.g. `https://calendly.com/yourname/conversation`) in `bookingUrl` in `content/shared/site.json`; until then the Book page asks people to message you on WhatsApp |
| Legal details | Privacy page (`content/en/legal.md`) | Trading name and postal address for the privacy notice; whether you are registered with the ICO |
| Retention | Privacy page | How long you keep client notes and booking details after coaching ends, and where they are stored |
| Payment and cancellation | Terms page | How and when clients pay, notice to cancel or move a session, refund policy, and the 14-day cancellation wording (Consumer Contracts Regulations 2013) |
| Liability | Terms page | Limit-of-liability wording from your adviser; professional indemnity insurance, if any |
| Governing law | Terms page | Confirm England and Wales (or Scotland) |
| Legal review | `content/en/legal.md` (`status: draft`) | Have Privacy and Terms reviewed; then set `status: approved` and the draft banner disappears |
