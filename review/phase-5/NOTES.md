# Phase 5 review: pages and features (11 Nov 2026)

New: Programme page, Privacy and Terms (English, draft), 404 with the breath pacer, share images per page and
language, structured data, contact form and client stories (both built, both off until Grant switches them on).

## Measured
- 11 pages: one h1 and one main each; no horizontal scroll at 390/1440.
- No third-party requests and no cookies on any page (Calendly only after a click).
- Canonical and hreflang correct per page; 404 has neither and is noindex.
- Contact form (tested with a stand-in endpoint): empty → asks for all fields; 2xx → thanks; 500 → says it failed; honeypot → sends nothing.
- Stories: right with one or two (tested with sample text, then removed).

## Ten ways it could look generic, and what was done
1. Legal pages as a wall of grey text → serif section headings, short lists, a dated draft badge.
2. A 404 with a cartoon → the real breath pacer and one line of copy, in both languages.
3. Testimonials as star-rated cards with avatars → no cards, no stars; a rule, the arc (before / what we did / now), first name only.
4. Share images as a stock photo with a logo → the headline in the site's serif, one orbit line, one warm dot.
5. Programme page as icon tiles → the same timeline as the home page, plus plain paragraphs.
6. "What's included" as checkmark bullets → a ruled two-column list.
7. Covers / doesn't cover as green ticks and red crosses → two labelled paragraphs.
8. Contact form with floating labels and gradients → plain labelled fields on the night background.
9. Cookie banner by reflex → none needed: nothing sets cookies.
10. A separate Spanish legal translation of UK terms → English only, labelled "(en inglés)" in the Spanish footer.
