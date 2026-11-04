# Design prototypes

Three static HTML prototypes, one per palette in `knowledge/design-system.md` (A Field Notes, B Night Practice, C Tidal), all using the same approved copy and the real logo:

- `prototype-a.html`, `prototype-b.html`, `prototype-c.html`
- Each shows: header, hero (with breath pacer), pillars, programme timeline, final CTA, footer — at desktop and mobile widths
- Each passes the anti-default test in `knowledge/design-system.md`

## Publishing

- Each prototype is one self-contained HTML file: fonts and logo copied next to it under `design/`, no CDN, no tracking, `noindex, nofollow` (requirement 13.8).
- Published on GitHub Pages at `granterogers.github.io/wellness_coaching/design/prototype-a.html` (and `-b`, `-c`) so Grant can open them on phone and laptop. They stay there after the build (requirement 2.9).
- Photos are descriptive placeholders (requirement 8.2), so the comparison is about palette, type, layout and motion.

When Grant picks one, create `design/CHOSEN.md` containing the file name and any changes he asked for. The build matches it (requirement 1.4).
