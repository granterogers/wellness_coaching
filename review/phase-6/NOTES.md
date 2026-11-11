# Phase 6 review: audit and handover (11 Nov 2026)

## Lighthouse, mobile (local build with indexing on, as 15.1 asks)
| Page | Perf | A11y | Best practice | SEO | LCP | CLS |
|---|---|---|---|---|---|---|
| /en/ | 100 | 100 | 100 | 100 | 1.2 s | 0 |
| /es/ | 100 | 100 | 100 | 100 | 1.1 s | 0 |
| /en/about/ | 100 | 100 | 100 | 100 | 0.9 s | 0 |
| /en/programme/ | 100 | 100 | 100 | 100 | 0.9 s | 0 |
| /en/book/ | 100 | 100 | 100 | 100 | 0.9 s | 0 |
| /en/privacy/ | 100 | 100 | 100 | 100 | 0.9 s | 0 |
| /404.html | 100 | 100 | 100 | 60 (noindex, by design) | 1.1 s | 0 |

Found and fixed on the way:
- **Home LCP was 4.1 s** (perf 87): the hero waited for the motion script. The hero entrance is now pure CSS and starts on the first paint.
- **Home CLS 0.033:** splitting the headline into lines re-flowed the text below it. Gone with the CSS hero.
- **About: an empty button** at the bottom (its label sits in the "Where I've taught" section). Fixed.
- **Keyboard users skipped content not yet revealed** (GSAP's autoAlpha sets visibility: hidden). Entrances now use opacity only, and focusing inside a section finishes its entrance at once.
- **Flags 40 px wide and skip link 43 px tall on phones** → 44 px.
- **Tailwind's default font stack (it lists Roboto)** → the html default font is now ours.

## Accessibility (14.x)
- Contrast, both themes (computed): body 12.6 / 13.0, muted 5.5 / 7.4, accent 6.0 / 8.4, buttons 6.4 / 8.4, night text 11.8 / 14.6. All AA.
- Tab order on home covers the skip link, nav, theme, flags, CTAs, pacer, Listen, pillar row, both Try links, body scan, all 8 FAQ questions, contact and footer; every stop has a visible focus ring. Enter opens FAQs and starts the pacer.
- Tap targets ≥ 44 px on all 11 pages at 390 px, light and dark (inline text links excepted, as WCAG allows).
- Every control has a name; every decorative SVG is hidden from assistive tech.
- Reduced motion: nothing animates; content is there at once (9.10, 14.4). The ambient loops are Grant's decision D-11 Nov.

## Responsive (15.4)
No horizontal scroll and the header fits at 360, 390, 768, 1024, 1440 and 1920 px on all 11 pages.

## Browsers (15.5)
Chromium desktop and phone emulation (touch, mobile viewport) here. Firefox and WebKit aren't available in this environment; a real iPhone and Firefox check is on `LAUNCH-CHECKLIST.md` for Grant.

## Ten ways it could look generic (whole site), and the answer
1. Centred hero + three icon cards → offer-first split hero with a working breath pacer; no icon cards anywhere.
2. Drop-shadow card grid → no shadows; pillars are columns marked by slabs, lists are ruled.
3. Stock yoga silhouette → none; the body scan figure is an anatomical line drawing that does a job.
4. Purple/blue gradients, blobs, glass → none; two palettes from the brief, flat surfaces.
5. Forbidden fonts → Newsreader, Hanken Grotesk, IBM Plex Mono only.
6. Identical fade-up everywhere → entrances by purpose (Phase 4 notes).
7. Emoji bullets → none.
8. Generic wellness phrases → none of the banned phrases appear (checked by search).
9. Testimonial carousel with stars → stories hidden until real; when on, plain arcs, no stars.
10. A cookie banner by reflex → none needed; nothing sets cookies.
