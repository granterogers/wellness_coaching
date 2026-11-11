// Social-share images, one per page and language, drawn at build time (requirements 2.7, 13.3).
// Text comes from content only; sexual wellbeing never appears here (13.7) because only headings are used.
import type { APIRoute } from 'astro';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { homeCopy, pageCopy } from '../../../lib/site';
import { t, type Lang } from '../../../i18n';

export const SHARE_PAGES = ['home', 'programme', 'about', 'book'] as const;
export function getStaticPaths() {
  return (['en', 'es'] as const).flatMap((lang) => SHARE_PAGES.map((page) => ({ params: { lang, page } })));
}

const font = (f: string) => readFileSync(join(process.cwd(), 'src/assets/og-fonts', f));
const fonts = [
  { name: 'Newsreader', data: font('newsreader-400.ttf'), weight: 400 as const, style: 'normal' as const },
  { name: 'Newsreader', data: font('newsreader-400-italic.ttf'), weight: 400 as const, style: 'italic' as const },
  { name: 'Hanken', data: font('hanken-grotesk-500.ttf'), weight: 500 as const, style: 'normal' as const },
];
// Palette A (light): design/CHOSEN.md
const C = { bg: '#ECEDE4', ink: '#1F2A24', accent: '#3F5F4A', muted: '#56615A', warm: '#E3A63E', rule: '#7D877E' };
type Node = { type: string; props: Record<string, unknown> };
const h = (type: string, style: Record<string, unknown>, children?: unknown): Node => ({ type, props: { style, children } });

export const GET: APIRoute = async ({ params }) => {
  const lang = params.lang as Lang, page = params.page as string;
  let roman = '', italic = '';
  if (page === 'home') {
    const c = await homeCopy(lang);
    const m = c.hero.headline.match(/^(.*?)\s*\*(.*)\*\s*$/);
    [roman, italic] = m ? [m[1], m[2]] : [c.hero.headline, ''];
  } else {
    roman = (await pageCopy(lang, page)).labels['Heading'] ?? '';
  }
  const tree = h('div', { width: 1200, height: 630, boxSizing: 'border-box', display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
    padding: '72px 80px', background: C.bg, color: C.ink, position: 'relative', fontFamily: 'Newsreader' }, [
    // The one orbit line (6.6), quiet, top right
    h('div', { display: 'flex' }),
    h('div', { display: 'flex', fontFamily: 'Hanken', fontSize: 28, color: C.accent, letterSpacing: 0.2 }, 'Grant Rogers'),
    h('div', { display: 'flex', flexDirection: 'column', fontSize: italic ? 86 : 96, lineHeight: 1.04, letterSpacing: -1.5, maxWidth: 900 }, [
      h('div', { display: 'flex' }, roman),
      ...(italic ? [h('div', { display: 'flex', fontStyle: 'italic', color: C.accent }, italic)] : []),
    ]),
    h('div', { display: 'flex', alignItems: 'center', fontFamily: 'Hanken', fontSize: 24, color: C.muted }, [
      h('div', { display: 'flex', width: 14, height: 14, borderRadius: 7, background: C.warm, marginRight: 16 }),
      h('div', { display: 'flex' }, t(lang, 'share.tagline')),
    ]),
  ]);
  // The orbit: an absolutely placed ellipse, top right, clear of the text
  (tree.props.children as Node[])[0] = h('div', { display: 'flex', position: 'absolute', right: -260, top: -170, width: 820, height: 330,
    border: `2px solid ${C.rule}`, borderRadius: '50%', transform: 'rotate(-14deg)', opacity: 0.45 });
  const svg = await satori(tree as never, { width: 1200, height: 630, fonts });
  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};
