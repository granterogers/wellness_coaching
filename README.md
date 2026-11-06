# Wellness Coaching — Grant Rogers

The website for Grant Rogers' 1:1 wellness coaching, plus the knowledge base its words come from.

**Live preview:** https://granterogers.github.io/wellness_coaching/ (not indexed by search engines yet).

## How it works, in plain terms

- **Nothing to install.** You edit text on github.com (or ask Claude Code on the web to do it). When a change reaches the `main` branch, GitHub builds and publishes the site in about 3 minutes.
- **The words** live in `content/` — one file per language. `content/en/home.md` is the homepage, `content/en/pages.md` the other pages. The site uses them word for word.
- **Settings** (email, WhatsApp, booking link, which features are switched on) live in `content/shared/site.json`.
- **Photos** go in `src/assets/photos/` with the file names listed in `knowledge/photo-slots.md`. Until a photo exists, the site shows a labelled placeholder.
- **Decisions and rules** live in `knowledge/` (start with `knowledge/brief.md`) and `CLAUDE.md`.

How to change text, pillars, photos and switches step by step: `CONTENT-EDITING.md`. Publishing and the later move to your own domain: `DEPLOY.md`. What's built and what's left: `REQUIREMENTS-STATUS.md`. What's still waiting for you: `PLACEHOLDERS.md`.

## The technical bits (for whoever maintains it)

Astro (static site) · Tailwind CSS v4 · GSAP and Lenis for motion · self-hosted fonts (Newsreader, Hanken Grotesk, IBM Plex Mono) · GitHub Actions → GitHub Pages.

Commands: `npm run build` · `npm run check` (types, content, links, placeholders) · `npm run shots -- <phase>` (screenshots).

## Private material

Workbooks, research interviews, client stories and strategy notes are in a separate private repository (`wellness_coaching_private`), because this repo is public.
