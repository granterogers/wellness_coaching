// Screenshots at 390px and 1440px, light and dark (requirement 1.7). Usage: npm run shots -- <phase>
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
const phase = process.argv[2] || 'latest';
const pages = (process.argv[3] || 'en/,es/').split(',');
const out = `review/phase-${phase}`;
mkdirSync(out, { recursive: true });
const server = spawn('npx', ['astro', 'preview', '--port', '4329'], { stdio: 'ignore' });
await new Promise((r) => setTimeout(r, 3500));
const browser = await chromium.launch();
try {
  for (const path of pages) for (const scheme of ['light', 'dark']) for (const w of [390, 1440]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: w < 500 ? 844 : 900 }, colorScheme: scheme });
    const page = await ctx.newPage();
    await page.goto(`http://localhost:4329/wellness_coaching/${path}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1200);
    const name = `${out}/${path.replace(/\//g, '') || 'root'}-${w}-${scheme}`;
    await page.screenshot({ path: `${name}.png`, fullPage: true });
    const sw = await page.evaluate(() => document.documentElement.scrollWidth);
    if (sw > w) console.warn(`horizontal scroll on ${path} at ${w}px (${sw}px)`);
    await ctx.close();
  }
} finally { await browser.close(); server.kill(); }
console.log(`screenshots in ${out}/`);
