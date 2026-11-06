// Every [[PLACEHOLDER: …]] in content or the built site must be listed in PLACEHOLDERS.md (requirement 15.6).
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
const list = readFileSync('PLACEHOLDERS.md', 'utf8').toLowerCase();
const found = [];
const walk = (d) => readdirSync(d).forEach((f) => { const p = join(d, f); statSync(p).isDirectory() ? walk(p) : /\.(md|html)$/.test(p) && found.push(p); });
walk('content'); walk('dist');
const missing = [];
for (const f of found) for (const m of readFileSync(f, 'utf8').matchAll(/\[\[PLACEHOLDER:\s*([^—\]-]+)/g)) {
  const key = m[1].trim().toLowerCase().split(/\s+/).slice(0, 2).join(' ');
  if (!list.includes(key)) missing.push(`${f}: "${m[1].trim()}" not in PLACEHOLDERS.md`);
}
if (missing.length) { console.error(missing.join('\n')); process.exit(1); }
console.log('placeholders ok');
