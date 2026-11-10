// Audio slots (requirement 10.3): a widget's voice switches on once its file exists in src/assets/audio/.
import { loadPractices } from './copy';
const files = import.meta.glob<string>('/src/assets/audio/*.{mp3,m4a}', { eager: true, query: '?url', import: 'default' });

export function voiceFor(widget: 'pacer' | 'bodyscan', lang: string) {
  const hit = Object.entries(files).find(([k]) => /\/(pacer|bodyscan)-(en|es)\.(mp3|m4a)$/.test(k) && k.includes(`/${widget}-${lang}.`));
  return hit?.[1] ?? null;
}

/** Transcript lines, only once the English scripts are approved (copy gate, 1.3). */
export function transcriptFor(widget: 'pacer' | 'bodyscan', lang: string) {
  const en = loadPractices('en');
  if (!en || en.status !== 'approved') return null;
  const p = loadPractices(lang) ?? en;
  return p[widget].map((l) => l.text);
}
