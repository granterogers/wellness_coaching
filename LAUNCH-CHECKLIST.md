# Launch checklist

What's left before the site is public and findable, in order. The UK operations plan (offline; see
`knowledge/roadmap.md`) covers the business side: registration, insurance, payments and client paperwork.
Everything here points at a file you can edit on github.com (`CONTENT-EDITING.md`).

## 1. Content you supply
- [ ] **Photos:** at least the portrait (P03) and the four pillar photos (P07, P08, P10, P11); then P04, P06, P16. `CONTENT-EDITING.md` → Photos.
- [ ] **Voice:** approve `content/en/practices.md`, record and upload `pacer-en.mp3` and `bodyscan-en.mp3` (Spanish optional).
- [ ] **Client stories** (optional at launch): up to three, with written permission; then `testimonials: true`.
- [ ] Look through `PLACEHOLDERS.md`: anything still listed shows as a visible `[[PLACEHOLDER: …]]` on the site.

## 2. Booking and contact
- [ ] Create the Calendly event: free, 30 minutes, video. Include your time zone and morning/evening slots (FAQ promise).
- [ ] Paste the link into `bookingUrl` in `content/shared/site.json`, then book a test call from your phone.
- [ ] Contact form (optional): create a form at a service such as Formspree, put its link in `formEndpoint`, set `contactForm: true`, and send yourself a test message. The privacy notice must then mention the form service (ask Claude to update `content/en/legal.md`).

## 3. Legal review
- [ ] Have Privacy and Terms (`content/en/legal.md`) reviewed: legal details, retention, payment and cancellation (including the 14-day cancellation right), liability, governing law. Then set `status: approved`.
- [ ] Check whether you need to register with the ICO (data protection fee).
- [ ] If you add Calendly, a form or analytics, update the privacy notice first.

## 4. Domain (optional, recommended)
- [ ] Buy the domain, then follow `DEPLOY.md` → "Moving to Cloudflare Pages and your own domain".

## 5. Analytics (optional)
- [ ] None is installed, which is why there's no cookie banner. If you want numbers, choose a cookie-free service (e.g. Cloudflare Web Analytics or Plausible), add it to the privacy notice, and ask Claude to add the snippet.

## 6. Go live
- [ ] Final check on a real iPhone (Safari) and in Firefox: open each page, switch language and theme, press Listen, open an FAQ, book a test call. Note anything odd in `REQUIREMENTS-STATUS.md` (15.5).
- [ ] Set `"indexing": true` in `content/shared/site.json`. Search engines can then index every page, and the sitemap is announced.
- [ ] On your own domain, add the site to Google Search Console and submit `/sitemap-index.xml`. (On the GitHub preview address, search engines only read the per-page tags; robots.txt and the sitemap need a domain root.)
- [ ] Share the link: the share images are ready for every page in both languages.
