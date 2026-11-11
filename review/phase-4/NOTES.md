# Phase 4 review: motion (11 Nov 2026)

Screenshots: `review/phase-4/*.png` at 390px and 1440px, light and dark, EN and ES. They are taken with reduced
motion so every section shows its final state; the motion itself was checked in a browser (below).

## What moves, and why
| Where | Motion | Purpose |
|---|---|---|
| Hero headline | Lines rise out of a mask, once per load (9.5) | The first thing read; sets the slow, breath-like pace |
| Hero text, buttons | Fade and lift 14px after the headline | Reading order |
| Pacer | Fades in and grows from 94% | It breathes; it should arrive like a breath |
| Section headings | Lines rise out of a mask; the intro fades after | Marks a new chapter |
| Pillars | Slabs draw out from their centre, then each column's contents rise, left to right | The columns are "built" |
| Programme | Phases appear in order, sliding 18px from the left | Steps along a path |
| Photos | A curtain lifts; the image settles from 108% (9.7, no parallax) | Reveal, not decoration |
| Facts, FAQ | Quick fade, no movement | Lists: get out of the way |
| Body scan | Fades and lifts last | Invitation after the bio |
| Night orbit | Swings 6° into place (6.6) | The one orbit line |

Only transform and opacity are animated (9.11). Nothing is pinned, scroll-linked or snapped (9.8). Lenis eases the
wheel on desktop fine pointers only (9.9). Under reduced motion none of this runs and content is there at once (9.10, 14.4).

## Measured
- Layout shift: 0.0000 on load and while scrolling, desktop and phone (was 0.0087–0.0235 from late web fonts; fixed by preloading the three main font files).
- After scrolling the whole page: no element left hidden, EN and ES, desktop, phone and reduced motion.
- No horizontal scroll at 390 and 1440.
- Home page JavaScript: about 55 KB gzipped (budget 120 KB, 15.3).
- Try links: Calm → pacer, Sleep → body scan; each scrolls the widget clear of the header, starts it and moves focus to Stop.

## Ten ways it could look generic, and what was done
1. Identical fade-up on every section → entrances differ by purpose (table above).
2. Everything sliding in from below → lists only fade; programme moves sideways; pillars build from the slabs.
3. Bouncy or elastic easing → expo-out and power curves only; no overshoot.
4. Parallax on photos → none.
5. Animated gradients or blobs → none.
6. Typewriter headline → masked line rise instead (and typewriter is forbidden).
7. Scroll-jacking → native distances; Lenis only eases the wheel, and only on desktop.
8. Motion on every hover → only button fill slide and underline draw (9.12).
9. Long staggers that make people wait → total hero sequence about 1.6 s; list staggers 0.025–0.14 s.
10. Animations replaying on every scroll → each entrance runs once.
