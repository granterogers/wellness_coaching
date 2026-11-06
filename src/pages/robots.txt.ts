import type { APIRoute } from 'astro';
import { siteData } from '../lib/site';

// Requirement 13.8: disallow everything while the `indexing` flag is off.
// Note: crawlers read robots.txt only at a domain's root, so on GitHub Pages the noindex meta tag is what counts.
export const GET: APIRoute = async ({ site }) => {
  const { flags } = await siteData();
  const sitemap = new URL(`${import.meta.env.BASE_URL}sitemap-index.xml`, site).href;
  const body = flags.indexing ? `User-agent: *\nAllow: /\nSitemap: ${sitemap}\n` : 'User-agent: *\nDisallow: /\n';
  return new Response(body, { headers: { 'Content-Type': 'text/plain' } });
};
