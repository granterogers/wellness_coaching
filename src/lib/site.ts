import { getEntry, getCollection } from 'astro:content';
import type { Lang } from '../i18n';

export async function siteData() {
  const s = await getEntry('site', 'site');
  if (!s) throw new Error('content/shared/site.json is missing');
  return s.data;
}

export async function homeCopy(lang: Lang) {
  const entry = (await getEntry('home', lang)) ?? (await getEntry('home', 'en'));
  if (!entry) throw new Error('content/en/home.md is missing');
  return entry.data;
}

export async function photoSlots() {
  return (await getCollection('photos')).map((p) => ({ id: p.id, ...p.data }));
}

export async function pageCopy(lang: Lang, page: string) {
  const entry = (await getEntry('pages', `${lang}/${page}`)) ?? (await getEntry('pages', `en/${page}`));
  if (!entry) throw new Error(`content/en/pages.md has no "# ${page}" page`);
  const d = entry.data;
  return { ...d, section: (title: string) => d.sections.find((s) => s.title === title) };
}
