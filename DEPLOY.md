# Deploying the site

## The preview (now)

- Live at **https://granterogers.github.io/wellness_coaching/** (English at `/en/`, Spanish at `/es/`, prototypes at `/design/`).
- Every change pushed to the `main` branch is checked and published automatically by GitHub Actions (`.github/workflows/pages.yml`). It takes 2–3 minutes. You can watch it under the repo's **Actions** tab.
- One-time setting (already done): repo **Settings → Pages → Source: GitHub Actions**.
- If a publish fails, the previous version stays live. The Actions tab shows a red cross and the reason.
- While the `indexing` flag in `content/shared/site.json` is `false`, every page tells search engines not to index it.

## Moving to Cloudflare Pages and your own domain (later)

1. Create a Cloudflare Pages project connected to this GitHub repo. Build command `npm run build`, output folder `dist`.
2. In `astro.config.mjs`, change `site` to your domain (e.g. `https://grantrogers.com`) and `base` to `/`.
3. Point the domain at Cloudflare Pages (Cloudflare walks you through it).
4. When you're ready to be found on Google, set `"indexing": true` in `content/shared/site.json` (see `LAUNCH-CHECKLIST.md`).

Nothing else in the code needs to change; every link is built from `site` and `base`.
