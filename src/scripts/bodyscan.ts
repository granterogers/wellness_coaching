// Body scan behaviour (9.13, 10.4), timed and drawn like the breath pacer so the two read as one family:
// the same 4 s in / 6 s out breath, the dot circling once per breath, and every change a smooth fade.
// Ambient: one part per breath; it glows as you breathe in and fades as you breathe out, then the next.
// Guided (Listen): settle 10 s, 22 parts × 5 s, whole body 10 s (= the voice script); parts cross-fade.
import { CYCLE, ease, level, reduceMotion as reduce } from './breath';
const SETTLE = 10000, PART = 5000, WHOLE = 10000;

document.querySelectorAll<HTMLElement>('[data-scan]').forEach((box) => {
  const S = JSON.parse(box.dataset.strings!) as {
    zones: string[]; names: Record<string, string>; count: string; done: string; stopped: string;
    listen: string; stop: string;
  };
  const parts = S.zones.filter((z) => z !== 'whole');
  const TOTAL = SETTLE + parts.length * PART + WHOLE;
  const dot = box.querySelector<SVGCircleElement>('[data-scan-electron]')!;
  const whole = box.querySelector<SVGGElement>('[data-scan-whole]')!;
  const TH = (-6 * Math.PI) / 180, RX = 118, RY = 228, CX = 100, CY = 222;
  const groups = S.zones.map((z) => box.querySelector<SVGGElement>(`[data-zone="${z}"]`));
  const name = box.querySelector<HTMLElement>('[data-scan-name]')!;
  const count = box.querySelector<HTMLElement>('[data-scan-count]')!;
  const live = box.querySelector<HTMLElement>('[data-scan-live]')!;
  const listen = box.querySelector<HTMLButtonElement>('[data-listen]')!;
  const soon = box.querySelector<HTMLElement>('[data-voice-soon]');
  const voice = box.querySelector<HTMLAudioElement>('[data-voice]');
  const fig = box;
  let start = performance.now(), guided = false, last = '', visible = true;

  const label = (z: string, n: number) => {
    if (z === last) return;
    last = z;
    name.textContent = S.names[z];
    count.textContent = guided && n > 0 ? S.count.replace('{n}', String(n)) : '';
    if (guided) live.textContent = S.names[z];
  };
  // Opacity of every part and of the whole-body glow for this moment: all continuous, no steps
  const paint = (op: number[], wholeOp: number) => {
    groups.forEach((g, i) => { if (g) g.style.opacity = op[i].toFixed(3); });
    whole.style.opacity = wholeOp.toFixed(3);
  };
  const finish = (msg: string) => {
    guided = false; fig.classList.remove('guided'); listen.textContent = S.listen; if (soon) soon.hidden = true;
    if (voice) { voice.pause(); voice.currentTime = 0; }
    start = performance.now(); last = '';
    name.textContent = msg; count.textContent = ''; live.textContent = msg;
  };
  const begin = () => {
    guided = true; fig.classList.add('guided'); last = ''; start = performance.now();
    listen.textContent = S.stop; if (soon) soon.hidden = false;
    if (voice) { voice.currentTime = 0; voice.play().catch(() => { /* blocked: runs on its own clock */ }); }
  };
  const frame = (now: number) => {
    if (visible) {
      const run = guided && voice && !voice.paused ? voice.currentTime * 1000 : now - start;
      const b = level(run % CYCLE);              // the breath, exactly as in the pacer
      const op = S.zones.map(() => 0);
      let wholeOp = 0.18 + 0.12 * b;             // the body itself breathes softly, like the pacer's disc
      if (!reduce.matches) {                     // the dot goes round once per breath, like the pacer's
        const a = (2 * Math.PI * (run % CYCLE)) / CYCLE, x = RX * Math.cos(a), y = RY * Math.sin(a);
        dot.setAttribute('cx', (CX + x * Math.cos(TH) - y * Math.sin(TH)).toFixed(2));
        dot.setAttribute('cy', (CY + x * Math.sin(TH) + y * Math.cos(TH)).toFixed(2));
      }
      if (guided) {
        if (run >= TOTAL) finish(S.done);
        else if (run < SETTLE) { label('settle', 0); wholeOp = 0.2 + 0.3 * b; }
        else if (run >= SETTLE + parts.length * PART) { label('whole', parts.length + 1); wholeOp = 0.3 + 0.4 * b; }
        else {
          // Cross-fade: each part rises over the first second of its 5 s and hands over smoothly to the next
          const p = (run - SETTLE) / PART, i = Math.floor(p);
          for (let k = 0; k < parts.length; k++) {
            const d = p - k;                       // 0..1 while part k is current
            op[k] = d < 0 ? 0 : d < 1 ? ease(Math.min(1, d * 5)) : Math.max(0, 1 - ease(Math.min(1, (d - 1) * 5)));
          }
          for (let k = 0; k < parts.length; k++) op[k] *= 0.7 + 0.3 * b;
          label(parts[i], i + 1);
        }
      } else {
        // Ambient: one part per breath, glowing with the in-breath and fading with the out-breath
        const i = Math.floor(run / CYCLE) % S.zones.length, z = S.zones[i];
        if (z === 'whole') wholeOp = 0.18 + 0.45 * b; else op[i] = b;
        label(z, 0);
      }
      name.style.opacity = guided ? '1' : (0.45 + 0.55 * b).toFixed(3); // the name breathes with its part
      paint(op, wholeOp);
    }
    requestAnimationFrame(frame);
  };
  const toggle = () => (guided ? finish(S.stopped) : begin());
  box.querySelector('[data-scan-start]')!.addEventListener('click', toggle);
  listen.addEventListener('click', toggle);
  voice?.addEventListener('ended', () => { if (guided) finish(S.done); });
  // A pillar's example practice links here (9.3): follow the link, start the session, focus Listen/Stop
  document.querySelectorAll('[data-try="bodyscan"]').forEach((a) => a.addEventListener('click', () => {
    if (!guided) begin();
    setTimeout(() => listen.focus({ preventScroll: true }), 60); // after the browser has handled the link
  }));
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(box);
  requestAnimationFrame(frame);
});
