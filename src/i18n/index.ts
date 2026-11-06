import en from './en.json';
import es from './es.json';

export const languages = ['en', 'es'] as const;
export type Lang = (typeof languages)[number];
const dict = { en, es } as const;

/** UI strings (requirement 3.7). Missing Spanish keys fall back to English. */
export function t(lang: Lang, key: keyof typeof en, vars: Record<string, string | number> = {}): string {
  const s: string = (dict[lang] as Record<string, string>)[key] ?? en[key];
  return s.replace(/\{(\w+)\}/g, (_, k) => String(vars[k] ?? ''));
}

/** Link inside the site, respecting the /wellness_coaching/ base (requirement 2.9). */
export const url = (path = '') => `${import.meta.env.BASE_URL.replace(/\/$/, '')}/${path.replace(/^\//, '')}`;
