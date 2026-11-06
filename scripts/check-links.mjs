// Internal link check over the built site (requirement 2.11, 15.6). No dependencies.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';
const BASE = '/wellness_coaching';
const files = [];
const walk = (d) => readdirSync(d).forEach((f) => { const p = join(d, f); statSync(p).isDirectory() ? walk(p) : p.endsWith('.html') && files.push(p); });
walk('dist');
const bad = [];
for (const f of files) {
  const html = readFileSync(f, 'utf8');
  for (const m of html.matchAll(/(?:href|src)="([^"#?]+)[^"]*"/g)) {
    const u = m[1];
    if (/^(https?:|mailto:|tel:|data:|\/\/)/.test(u)) continue;
    if (!u.startsWith('/')) continue; // relative links (prototypes) are checked by eye
    if (!u.startsWith(BASE + '/') && u !== BASE) { bad.push(`${f}: ${u} (missing ${BASE} base)`); continue; }
    let p = join('dist', u.slice(BASE.length));
    if (u.endsWith('/')) p = join(p, 'index.html');
    if (!existsSync(p)) bad.push(`${f}: ${u}`);
  }
}
if (bad.length) { console.error('Broken internal links:\n' + bad.join('\n')); process.exit(1); }
console.log(`links ok (${files.length} pages)`);
