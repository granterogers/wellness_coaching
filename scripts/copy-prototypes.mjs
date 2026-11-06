// Keeps the design prototypes published at /design/ after the build (requirement 2.9).
import { cpSync, mkdirSync, readdirSync } from 'node:fs';
mkdirSync('dist/design', { recursive: true });
for (const f of readdirSync('design')) if (/^prototype-.*\.html$/.test(f)) cpSync(`design/${f}`, `dist/design/${f}`);
cpSync('design/fonts', 'dist/design/fonts', { recursive: true });
cpSync('design/assets', 'dist/design/assets', { recursive: true });
console.log('prototypes copied to dist/design/');
