// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// Preview on GitHub Pages (requirement 2.9). Moving to Cloudflare Pages + a domain later only changes `site` and `base` (see DEPLOY.md).
export default defineConfig({
  site: 'https://granterogers.github.io',
  base: '/wellness_coaching',
  trailingSlash: 'always',
  output: 'static',
  i18n: {
    locales: ['en', 'es'],
    defaultLocale: 'en',
    routing: { prefixDefaultLocale: true, redirectToDefaultLocale: false },
  },
  integrations: [sitemap({ i18n: { defaultLocale: 'en', locales: { en: 'en-GB', es: 'es-ES' } } })],
  vite: { plugins: [tailwindcss()] },
});
