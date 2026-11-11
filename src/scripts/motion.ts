// The one motion utility (9.10). Every entrance on the site is declared here, by purpose (9.6), and nothing runs under
// prefers-reduced-motion: the content is simply there (14.4). Only transform and opacity are animated (9.11); nothing
// is pinned or scroll-linked and scroll distance is never changed (9.8). Lenis smooths the wheel on desktop fine
// pointers only (9.9).
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';
import Lenis from 'lenis';
import 'lenis/dist/lenis.css';

const root = document.documentElement;
(window as unknown as { __motion: boolean }).__motion = true; // tells the head fallback that this loaded
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

if (reduce.matches) {
  root.classList.remove('motion');
} else {
  gsap.registerPlugin(ScrollTrigger, SplitText);
  const EASE = 'expo.out';
  const $ = <T extends Element = HTMLElement>(s: string, el: ParentNode = document) => [...el.querySelectorAll<T>(s)];
  // Elements already on screen when the script runs (e.g. after a language switch) are left alone: no flicker.
  const onScreen = (el: Element) => { const r = el.getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0; };
  const when = (trigger: Element, build: () => gsap.core.Timeline | gsap.core.Tween) => {
    if (onScreen(trigger) && !trigger.closest('[data-hero]')) return;
    const anim = build(); anim.pause();
    ScrollTrigger.create({ trigger, start: 'top 92%', once: true, onEnter: () => anim.play() });
  };
  const lines = (el: HTMLElement, opts: gsap.TweenVars = {}) => {
    const split = SplitText.create(el, { type: 'lines', mask: 'lines', linesClass: 'm-line' });
    return gsap.from(split.lines, { yPercent: 110, duration: 1.1, ease: EASE, stagger: 0.09, ...opts,
      onComplete: () => split.revert() });
  };

  // Hero: the headline rises line by line out of its mask, once per page load (9.5); then the rest settles in.
  const hero = document.querySelector<HTMLElement>('[data-hero]');
  if (hero) {
    const h1 = hero.querySelector<HTMLElement>('h1')!;
    const tl = gsap.timeline({ delay: 0.1 });
    gsap.set(hero, { autoAlpha: 1 });
    tl.add(lines(h1, { duration: 1.3, stagger: 0.12 }))
      .from($('.lede, .ctas', hero), { autoAlpha: 0, y: 14, duration: 0.9, ease: EASE, stagger: 0.08 }, 0.45)
      .from(hero.querySelector('.hero-pacer'), { autoAlpha: 0, scale: 0.94, duration: 1.6, ease: 'power2.out' }, 0.3);
  }
  // Inner pages: the page title rises the same way
  $('.page-head .display').forEach((h) => when(h, () => lines(h)));

  // Section headings rise out of a mask; the intro beside them follows quietly
  $('main .h2').forEach((h) => when(h, () => {
    const tl = gsap.timeline();
    tl.add(lines(h, { duration: 1 }));
    const intro = h.parentElement?.querySelector('.sec-intro');
    if (intro) tl.from(intro, { autoAlpha: 0, duration: 1, ease: 'power1.out' }, 0.25);
    return tl;
  }));

  // Pillars are built: the slab at the top and bottom of each column draws out from its centre, then the column's
  // contents come up, left to right
  const row = document.querySelector('.pillar-row');
  if (row) when(row, () => gsap.timeline()
    .from($('.col-capital, .col-base', row), { scaleX: 0, duration: 1, ease: EASE, stagger: 0.06 })
    .from($('.pillar > :not(.col-capital):not(.col-base)', row), { autoAlpha: 0, y: 18, duration: 0.9, ease: EASE, stagger: 0.025 }, 0.2));

  // Programme: the phases appear in order, like steps along a path
  const steps = $('.timeline .step');
  if (steps.length) when(steps[0], () => gsap.from(steps, { autoAlpha: 0, x: -18, duration: 0.9, ease: EASE, stagger: 0.14 }));

  // Photos open like a curtain lifting (9.7); the image inside settles from a slight zoom. No parallax.
  $('main .photo').forEach((ph) => {
    if (ph.closest('.final-bg')) return;
    when(ph, () => {
      const curtain = document.createElement('span');
      curtain.className = 'curtain'; curtain.setAttribute('aria-hidden', 'true'); ph.append(curtain);
      return gsap.timeline({ onComplete: () => curtain.remove() })
        .fromTo(curtain, { scaleY: 1 }, { scaleY: 0, duration: 1.2, ease: 'expo.inOut' })
        .from(ph.firstElementChild, { scale: 1.08, duration: 1.6, ease: EASE }, 0);
    });
  });

  // About: facts are a list, so they come in as one, quickly; the body scan fades up last
  $('.facts').forEach((f) => when(f, () => gsap.from(f.children, { autoAlpha: 0, duration: 0.6, ease: 'power1.out', stagger: 0.05 })));
  $('.about-widget').forEach((w) => when(w, () => gsap.from(w, { autoAlpha: 0, y: 24, duration: 1.4, ease: EASE })));

  // FAQ: questions fade in quickly; nothing slides
  const faq = $('.faq-item');
  if (faq.length) when(faq[0], () => gsap.from(faq, { autoAlpha: 0, duration: 0.6, ease: 'power1.out', stagger: 0.05 }));

  // Night section: the one orbit line swings gently into place (6.6)
  const orbit = document.querySelector<SVGElement>('.final-orbit');
  if (orbit) when(orbit, () => gsap.from(orbit, { autoAlpha: 0, rotation: -6, transformOrigin: '50% 50%', duration: 2.2, ease: 'power2.out' }));

  // Lenis: desktop fine pointers only (9.9); same distance per wheel step as native, just eased
  if (matchMedia('(pointer: fine) and (min-width: 1024px)').matches) {
    const lenis = new Lenis({ lerp: 0.14, anchors: true, autoRaf: true, prevent: (n) => !!n.closest?.('[data-lenis-prevent]') });
    lenis.on('scroll', ScrollTrigger.update);
  }
}
