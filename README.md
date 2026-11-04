# Wellness Coaching — Grant Rogers

Source repository for Grant Rogers' 1:1 wellness coaching website. Preview: GitHub Pages (`granterogers.github.io/wellness_coaching`).

This repo holds two things: the website itself, and the knowledge base the website's content is written from. Any update to the offer, wording or design starts in `knowledge/`, then flows into `content/` and the site.

## Structure

| Folder | What lives here |
|---|---|
| `knowledge/` | Single source of truth: brief, offer, voice, scope. Read `knowledge/brief.md` first. |
| `content/` | The words the website displays, one file per language (English, Spanish). |
| `assets/brand/` | Logo and icon files (see its README). |
| `assets/images/` | Photos not tied to a site slot (site photos go in `src/assets/photos/`). |
| `design/` | The three prototypes and `CHOSEN.md`. |
| `src/` | The website (Astro; built after copy and design are approved). |

## Working with an AI assistant

Start any new chat by pointing it at this repo and asking it to read `knowledge/brief.md` before doing anything else. That file summarises every decision made so far, so nothing depends on earlier chat history.

## Private material

Workbooks, research interviews, client stories and strategy notes are kept in a separate private repository (`wellness_coaching_private`), because this repo is public.
