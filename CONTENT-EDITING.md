# Editing the site

Everything below is done on **github.com**, in your browser. Nothing to install. Each change you save to the `main`
branch is checked and published in about 3 minutes. If a check fails, the old version stays live and nothing breaks
(see "If something goes wrong" at the end). You can also ask Claude Code on the web to make any of these changes.

## The basic move: change a file

1. Go to https://github.com/granterogers/wellness_coaching and open the file (folders are links).
2. Click the **pencil** icon (top right of the file). On a phone: the **…** menu, then **Edit file**.
3. Make your change.
4. Click **Commit changes…**, write a few words about what you changed, keep **Commit directly to the main branch**, and click **Commit changes**.
5. After about 3 minutes, reload the page on the site. The **Actions** tab shows progress: yellow is working, green is live.

## Words

| What | File |
|---|---|
| Home page | `content/en/home.md` (Spanish: `content/es/home.md`) |
| Programme, About, Book and the "page not found" page; page titles and Google descriptions | `content/en/pages.md` (Spanish: `content/es/pages.md`) |
| Voice scripts for the breathing and body scan widgets | `content/en/practices.md` (Spanish: `content/es/practices.md`) |
| Privacy and Terms (English only) | `content/en/legal.md` |
| Small interface words (button labels, "Listen", flag names) | `src/i18n/en.json` and `src/i18n/es.json` |

Rules that keep the build happy:

- Keep the `##` and `###` headings and the bold labels (`**Headline:**`, `**Description:**` …). Change only the words after them.
- Text between single asterisks, like `*built around your life.*`, is set in italic.
- If you change the English, change the Spanish to match, or ask Claude to translate it.
- Don't remove `status: approved` at the top of the English files: the build refuses unapproved copy.

## Pillars

The pillars are the `###` items under `## Pillars` in both `home.md` files. The layout works with 3 to 8.

- **Change a pillar:** edit its `**Description:**`, `**Example practice:**` and `**Why:**` lines.
- **Add a pillar:** copy a whole `###` block (from `###` down to its `**Why:**` line), paste it where you want it in the list, and change the words. In the Spanish file, add the same block with an `**ID:**` line matching the English name in lower case (e.g. `**ID:** focus`).
- **Remove a pillar:** delete its whole block in both files.
- **Its photo:** in `content/shared/photos.json`, the photo with `"pillar": "sleep"` (and so on) belongs to that pillar. For a new pillar, set `"pillar"` on one of the unused slots (P09 or P12) to the new ID.
- **Link to a widget:** a `**Try:** pacer` or `**Try:** bodyscan` line turns the example practice into a link that starts that widget (Calm and Sleep have one now).

## Photos

Until a photo exists, the site shows a labelled placeholder in its place. The site uses these:

| Slot | File name | Where |
|---|---|---|
| P03 | `about-portrait` | Home About section and About page |
| P04 | `about-profile-bw` | About page |
| P06 | `work-call` | Home Programme section |
| P07 | `pillar-breathe` | Calm pillar |
| P08 | `pillar-move` | Strength pillar |
| P10 | `pillar-restore` | Sleep pillar |
| P11 | `pillar-vitality` | Energy pillar |
| P16 | `texture-water` | Background of the "Start with a conversation" section |

What each one should show (framing, light, mood): `knowledge/photo-slots.md`.

To add one:

1. Name the photo exactly as above, ending `.jpg`, `.png` or `.webp` (e.g. `about-portrait.jpg`). Use the original, full-size file; the site makes the smaller versions itself.
2. On github.com, open the folder `src/assets/photos/`.
3. Click **Add file → Upload files**, drag the photo in, and click **Commit changes**.
4. To replace a photo later, upload a new one with the same name.

Descriptions for screen readers (alt text) are in `content/shared/photos.json` under `"alt"`, in both languages.

## Your voice in the widgets

1. Approve the scripts: in `content/en/practices.md`, change `status: draft` to `status: approved`. The transcripts then appear under each widget.
2. Record them, following the timings in the file (the breathing script is one minute; the body scan about two).
3. Upload them to `src/assets/audio/` named exactly `pacer-en.mp3` and `bodyscan-en.mp3` (Spanish: `pacer-es.mp3`, `bodyscan-es.mp3`).

The Listen link then plays your recording and the animation follows it. Until then it runs silently and says "Recording to come".

## Client stories

Under `## Proof` in `content/en/home.md` (and the Spanish file), replace the placeholder with up to three stories, first names only and only with written permission:

```
### Anna
**Before:** …
**What we did:** …
**Now:** …
```

A single quote works too: `**Quote:** …` instead of the three lines. Then switch `testimonials` on (next section).

## Switches and settings

All in `content/shared/site.json`. Use `true` or `false` exactly, with no quotes.

| Setting | What it does |
|---|---|
| `"bookingUrl"` | Your Calendly link, in quotes (e.g. `"https://calendly.com/…"`). The Book page then shows your calendar. |
| `"whatsapp"` | Your WhatsApp number, digits only with the country code (`"34603834206"`). |
| `"email"` | Leave as `""` to keep your email address off the site. |
| `"formEndpoint"` | Where the contact form sends messages (e.g. a Formspree form link). The form needs this and `contactForm` on. |
| `testimonials` | Shows the client stories section. |
| `contactForm` | Shows the contact form on the Book page. |
| `spanish` | Shows the flags and the links to the Spanish pages. |
| `indexing` | Lets Google find the site. Leave `false` until launch (`LAUNCH-CHECKLIST.md`). |
| `freePractice`, `voiceClip` | Reserved for later features; no effect yet. |

## If something goes wrong

- A red cross in the **Actions** tab means the change wasn't published, and the previous version is still live. Click the red run to see the reason; it usually names the file and line (often a missing bold label or a stray quote in `site.json`).
- To undo a change: open the file, click **History**, open the earlier version, and copy its text back. Or ask Claude: "undo my last change to home.md".
