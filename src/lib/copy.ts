/**
 * Reads the copy documents in content/<lang>/*.md word for word (requirement 3.1).
 * Format: YAML-ish frontmatter, then "## Section" headings, "### Item" headings,
 * "**Label:** value" lines and plain paragraphs. No rewording happens here.
 */
import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

export type Section = {
  raw: string;
  paras: string[];
  labels: Record<string, string>;
  items: { title: string; labels: Record<string, string>; text: string }[];
  list: string[];
  text: string;
};

const ROOT = process.cwd();

function frontmatter(src: string): [Record<string, string>, string] {
  const m = src.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!m) return [{}, src];
  const fm: Record<string, string> = {};
  for (const line of m[1].split('\n')) {
    const kv = line.match(/^([\w-]+):\s*(.*)$/);
    if (kv) fm[kv[1]] = kv[2].trim();
  }
  return [fm, src.slice(m[0].length)];
}

function labels(txt: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const m of txt.matchAll(/^\*\*([^*]+):\*\*\s*(.*)$/gm)) out[m[1].trim()] = m[2].trim();
  return out;
}

function paragraphs(txt: string): string {
  return txt
    .split('\n')
    .filter((l) => l.trim() && !l.startsWith('**') && !l.startsWith('[[') && !l.startsWith('- ') && !l.startsWith('#'))
    .map((l) => l.trim())
    .join(' ');
}

function parseText(body: string, level: '# ' | '## '): Record<string, Section> {
  const sections: Record<string, Section> = {};
  const parts = body.split(new RegExp(`^${level === '# ' ? '#' : '##'}\\s`, 'm')).slice(1);
  for (const part of parts) {
    const nl = part.indexOf('\n');
    const name = (nl < 0 ? part : part.slice(0, nl)).trim();
    const rest = nl < 0 ? '' : part.slice(nl + 1);
    const [head, ...items] = rest.split(/^###\s/m);
    sections[name] = {
      raw: rest,
      labels: labels(rest),
      list: head.split('\n').filter((l) => l.startsWith('- ')).map((l) => l.slice(2).trim()),
      text: paragraphs(head),
      paras: head.split(/\n\s*\n/).map(paragraphs).filter(Boolean),
      items: items.map((it) => {
        const i = it.indexOf('\n');
        const t = i < 0 ? '' : it.slice(i + 1);
        return { title: (i < 0 ? it : it.slice(0, i)).trim(), labels: labels(t), text: paragraphs(t) };
      }),
    };
  }
  return sections;
}

export function readSections(file: string, level: '# ' | '## ' = '## ') {
  const [fm, raw] = frontmatter(readFileSync(file, 'utf8'));
  return { fm, sections: parseText(raw.replace(/<!--[\s\S]*?-->/g, ''), level) };
}

/** content/<lang>/pages.md: "# Page" headings, each with labels and "## Section" blocks. */
export function loadPages(lang: string) {
  const file = join(ROOT, 'content', lang, 'pages.md');
  const { fm, sections } = readSections(file, '# ');
  return Object.entries(sections).map(([name, page]) => {
    const head = page.raw.split(/^##\s/m)[0];
    return {
      id: `${lang}/${slug(name)}`,
      lang,
      page: slug(name),
      status: fm.status,
      translation_status: fm.translation_status,
      labels: labels(head),
      sections: Object.entries(parseText(page.raw, '## ')).map(([title, s]) => ({
        title, labels: s.labels, paras: s.paras, list: s.list,
        items: s.items.map((i) => ({ title: i.title, text: i.text })),
      })),
    };
  });
}

export const pageLanguages = () => ['en', 'es'].filter((l) => existsSync(join(ROOT, 'content', l, 'pages.md')));

const slug = (s: string) =>
  s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

function need(sections: Record<string, Section>, name: string, file: string): Section {
  const s = sections[name];
  if (!s) throw new Error(`${file}: missing "## ${name}" section`);
  return s;
}

/** Maps content/<lang>/home.md onto the shape the home page uses. Missing pieces are caught by the schema. */
export function loadHome(lang: string) {
  const file = join(ROOT, 'content', lang, 'home.md');
  const { fm, sections } = readSections(file);
  const S = (n: string) => need(sections, n, file);
  const hero = S('Hero').labels;
  const prog = S('Programme');
  return {
    id: lang,
    lang,
    status: fm.status,
    translation_status: fm.translation_status,
    hero: {
      headline: hero['Headline'], subhead: hero['Subhead'], primary: hero['Primary button'],
      secondary: hero['Secondary button'], pacerHint: hero['Pacer hint'],
    },
    recognition: {
      heading: S('Recognition').labels['Heading'],
      items: S('Recognition').items.map((i) => i.text),
      closing: S('Recognition').labels['Closing line'],
    },
    pillars: {
      heading: S('Pillars').labels['Heading'],
      intro: S('Pillars').labels['Intro'],
      items: S('Pillars').items.map((i) => ({
        id: i.labels['ID'] || slug(i.title), name: i.title, description: i.labels['Description'],
        practice: i.labels['Example practice'], why: i.labels['Why'],
      })),
    },
    programme: {
      heading: prog.labels['Heading'],
      intro: prog.labels['Intro'],
      phases: prog.items.map((i) => {
        const m = i.title.match(/^(.*?)\s*(\d+)\s*\/\s*(.*)$/);
        return { label: m?.[1] ?? '', num: m?.[2] ?? '', name: m?.[3] ?? i.title, text: i.text };
      }),
      included: (prog.labels['Included'] ?? '').split('·').map((s) => s.trim()).filter(Boolean),
      price: prog.labels['Price line'],
    },
    about: {
      heading: S('About').labels['Heading'], body: S('About').labels['Body'],
      facts: S('About').list, link: S('About').labels['Link'],
    },
    voice: { intro: S('Voice').labels['Intro line'], transcript: S('Voice').labels['Transcript'] },
    proof: { heading: S('Proof').labels['Heading'] },
    faq: { heading: S('FAQ').labels['Heading'], items: S('FAQ').items.map((i) => ({ q: i.title, a: i.text })) },
    finalCta: {
      heading: S('Final CTA').labels['Heading'], body: S('Final CTA').labels['Body'],
      primary: S('Final CTA').labels['Primary button'], email: S('Final CTA').labels['Email label'],
      whatsapp: S('Final CTA').labels['WhatsApp label'],
    },
    footer: { disclaimer: S('Footer').labels['Disclaimer'] },
  };
}

export const homeLanguages = () => ['en', 'es'].filter((l) => existsSync(join(ROOT, 'content', l, 'home.md')));

/** Inline *italic* → <em>. Text is escaped first, so copy can never inject markup. */
export function inline(s: string): string {
  const esc = s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return esc.replace(/\*([^*]+)\*/g, '<em>$1</em>');
}
