export {};
// Site-wide behaviour. Everything works without it; this only adds polish.
const root = document.documentElement;

// Header condenses on scroll (5.14)
const header = document.querySelector<HTMLElement>('[data-header]');
if (header) {
  const onScroll = () => header.classList.toggle('condensed', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// Light / dark (6.9): device setting first, the visitor's choice wins and is remembered on this device
const btn = document.querySelector<HTMLButtonElement>('[data-theme-toggle]');
const darkMq = matchMedia('(prefers-color-scheme: dark)');
const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : darkMq.matches);
const syncTheme = () => {
  const d = isDark();
  root.classList.toggle('is-dark', d);
  if (!btn) return;
  btn.querySelector('[data-theme-label]')!.textContent = d ? btn.dataset.lLight! : btn.dataset.lDark!;
  btn.setAttribute('aria-label', d ? btn.dataset.aLight! : btn.dataset.aDark!);
};
btn?.addEventListener('click', () => {
  const next = isDark() ? 'light' : 'dark';
  root.dataset.theme = next;
  try { localStorage.setItem('theme', next); } catch { /* private mode: choice lasts for this page */ }
  syncTheme();
});
darkMq.addEventListener('change', syncTheme);
syncTheme();

// Email assembled here so bots can't read it from the page source (11.1)
document.querySelectorAll<HTMLAnchorElement>('[data-mail]').forEach((a) => {
  const addr = `${a.dataset.u}@${a.dataset.d}`;
  a.href = `mailto:${addr}${a.dataset.subject ? `?subject=${encodeURIComponent(a.dataset.subject)}` : ''}`;
});
document.querySelectorAll<HTMLElement>('[data-mail-text]').forEach((s) => { s.textContent = `${s.dataset.u}@${s.dataset.d}`; });

// Sticky mobile CTA (5.13): appears after the hero, hides when the final CTA is in view
const bar = document.querySelector<HTMLElement>('[data-mobile-cta]');
const hero = document.querySelector('[data-hero]');
const fin = document.querySelector('#book');
if (bar && hero && fin) {
  let pastHero = false, atEnd = false;
  const upd = () => { const off = !pastHero || atEnd; bar.classList.toggle('off', off); bar.inert = off; };
  new IntersectionObserver(([e]) => { pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; upd(); }).observe(hero);
  new IntersectionObserver(([e]) => { atEnd = e.isIntersecting; upd(); }).observe(fin);
}

// Switching language keeps your place (12.2): remember which section is at the top of the screen and how far into it
// you are, then restore that position on the other language's page (the text lengths differ, so pixels alone won't do).
const KEY = 'lang-pos';
document.querySelectorAll<HTMLAnchorElement>('.flags a, .foot-meta a[hreflang], .foot-meta a[lang]').forEach((a) => {
  a.addEventListener('click', () => {
    const secs = [...document.querySelectorAll<HTMLElement>('main > section[id]')]; // same ids in every language
    const here = secs.filter((s) => s.getBoundingClientRect().top <= 80).pop();
    const pos = here
      ? { id: here.id, f: (80 - here.getBoundingClientRect().top) / Math.max(1, here.offsetHeight) }
      : { id: '', f: scrollY / Math.max(1, document.documentElement.scrollHeight - innerHeight) };
    try { sessionStorage.setItem(KEY, JSON.stringify(pos)); } catch { /* ignore */ }
  });
});
try {
  const saved = sessionStorage.getItem(KEY);
  if (saved) {
    sessionStorage.removeItem(KEY);
    const { id, f } = JSON.parse(saved) as { id: string; f: number };
    const el = id ? document.getElementById(id) : null;
    const y = el ? el.getBoundingClientRect().top + scrollY + f * el.offsetHeight - 80
                 : f * (document.documentElement.scrollHeight - innerHeight);
    window.scrollTo({ top: Math.max(0, y), behavior: 'instant' as ScrollBehavior });
  }
} catch { /* ignore */ }
