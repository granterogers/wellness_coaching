// Full favicon set from assets/brand/icon.svg (requirement 7.2). Run: node scripts/favicons.mjs
import sharp from 'sharp';
import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from 'node:fs';
mkdirSync('public/brand', { recursive: true });
const svg = readFileSync('assets/brand/icon.svg', 'utf8').replace(/<style>[\s\S]*?<\/style>/, '').replaceAll('currentColor', '#3F5F4A');
const onBg = (size, pad) => Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 64 64"><rect width="64" height="64" fill="#ECEDE4"/><g transform="translate(${pad} ${pad}) scale(${(64 - 2 * pad) / 64})">${svg.replace(/<svg[^>]*>|<\/svg>/g, '')}</g></svg>`);
for (const [n, s, pad] of [['favicon-32.png', 32, 4], ['icon-192.png', 192, 8], ['icon-512.png', 512, 8]]) await sharp(onBg(s, pad)).png().toFile(`public/brand/${n}`);
copyFileSync('assets/brand/icon.svg', 'public/brand/icon.svg');
copyFileSync('assets/brand/icon-180.png', 'public/brand/icon-180.png');
writeFileSync('public/manifest.webmanifest', JSON.stringify({
  name: 'Grant Rogers', short_name: 'Grant Rogers', start_url: '/wellness_coaching/en/', display: 'browser',
  background_color: '#ECEDE4', theme_color: '#3F5F4A',
  icons: [{ src: 'brand/icon-192.png', sizes: '192x192', type: 'image/png' }, { src: 'brand/icon-512.png', sizes: '512x512', type: 'image/png' }],
}, null, 1));
console.log('favicons written to public/brand/');
