// Body scan behaviour (9.13, 10.4). Guided timeline: settle 10 s, 22 parts × 5 s, whole body 10 s (= the voice script).
// Listen (or a tap on the figure) plays Grant's guided scan; the same button then reads Stop. Otherwise the figure
// walks through the parts on a loop, with no pause control (Grant's decision, D-11 Nov).
import { CYCLE, level, reduceMotion as reduce } from './breath';
const SETTLE = 10000, PART = 5000, WHOLE = 10000, AMBIENT = 2000;

document.querySelectorAll<HTMLElement>('[data-scan]').forEach((box) => {
  const S = JSON.parse(box.dataset.strings!) as {
    zones: string[]; names: Record<string, string>; count: string; done: string; stopped: string;
    listen: string; stop: string;
  };
  const parts = S.zones.filter((z) => z !== 'whole');
  const TOTAL = SETTLE + parts.length * PART + WHOLE;
  const svg = box.querySelector('svg')!;
  const dot = box.querySelector<SVGCircleElement>('[data-scan-electron]')!;
  const TH = (-6 * Math.PI) / 180, RX = 118, RY = 228, CX = 100, CY = 222;
  const groups = new Map(S.zones.map((z) => [z, box.querySelector<SVGGElement>(`[data-zone="${z}"]`)]));
  const name = box.querySelector<HTMLElement>('[data-scan-name]')!;
  const count = box.querySelector<HTMLElement>('[data-scan-count]')!;
  const live = box.querySelector<HTMLElement>('[data-scan-live]')!;
  const listen = box.querySelector<HTMLButtonElement>('[data-listen]')!;
  const soon = box.querySelector<HTMLElement>('[data-voice-soon]');
  const voice = box.querySelector<HTMLAudioElement>('[data-voice]');
  let start = performance.now(), guided = false, last = '', visible = true;

  const show = (z: string, n: number) => {
    if (z === last) return;
    last = z;
    groups.forEach((g, k) => g?.classList.toggle('on', k === z));
    svg.classList.toggle('whole', z === 'whole');
    svg.classList.toggle('settle', z === 'settle');
    name.textContent = S.names[z];
    count.textContent = guided && n > 0 ? S.count.replace('{n}', String(n)) : '';
    if (guided) live.textContent = S.names[z];
  };
  const finish = (msg: string) => {
    guided = false; listen.textContent = S.listen; if (soon) soon.hidden = true;
    if (voice) { voice.pause(); voice.currentTime = 0; }
    start = performance.now(); last = '';
    groups.forEach((g) => g?.classList.remove('on')); svg.classList.remove('whole', 'settle');
    name.textContent = msg; count.textContent = ''; live.textContent = msg;
  };
  const begin = () => {
    guided = true; last = ''; start = performance.now();
    listen.textContent = S.stop; if (soon) soon.hidden = false;
    if (voice) { voice.currentTime = 0; voice.play().catch(() => { /* blocked: runs on its own clock */ }); }
  };
  const at = (run: number): [string, number] => {
    if (run < SETTLE) return ['settle', 0];
    const i = Math.floor((run - SETTLE) / PART);
    return i < parts.length ? [parts[i], i + 1] : ['whole', parts.length + 1];
  };
  const frame = (now: number) => {
    if (visible) {
      const run = guided && voice && !voice.paused ? voice.currentTime * 1000 : now - start;
      svg.style.setProperty('--b', reduce.matches ? '.5' : level(run % CYCLE).toFixed(3));
      if (!reduce.matches) {
        const a = (2 * Math.PI * (run % (CYCLE * 2))) / (CYCLE * 2), x = RX * Math.cos(a), y = RY * Math.sin(a);
        dot.setAttribute('cx', (CX + x * Math.cos(TH) - y * Math.sin(TH)).toFixed(2));
        dot.setAttribute('cy', (CY + x * Math.sin(TH) + y * Math.cos(TH)).toFixed(2));
      }
      if (guided) {
        if (run >= TOTAL) finish(S.done); else show(...at(run));
      } else {
        show(S.zones[Math.floor(run / AMBIENT) % S.zones.length], 0);
      }
    }
    requestAnimationFrame(frame);
  };
  const toggle = () => (guided ? finish(S.stopped) : begin());
  box.querySelector('[data-scan-start]')!.addEventListener('click', toggle);
  listen.addEventListener('click', toggle);
  voice?.addEventListener('ended', () => { if (guided) finish(S.done); });
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(box);
  requestAnimationFrame(frame);
});
