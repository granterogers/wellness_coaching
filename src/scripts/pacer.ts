// Breath pacer behaviour. Listen (or a tap on the circle) plays Grant's guided minute, six 10-second breaths;
// the same button then reads Stop. Otherwise the circle breathes on a loop, with no pause control (Grant's decision, D-11 Nov).
import { IN, CYCLE, level, reduceMotion as reduce } from './breath';
const GUIDED = 60000;

document.querySelectorAll<HTMLElement>('[data-pacer]').forEach((fig) => {
  const S = JSON.parse(fig.dataset.strings!) as Record<string, string>;
  const ring = fig.querySelector<SVGGElement>('.pacer-ring')!;
  const el = fig.querySelector<SVGCircleElement>('.pacer-electron')!;
  const label = fig.querySelector<HTMLElement>('[data-pacer-label]')!;
  const live = fig.querySelector<HTMLElement>('[data-pacer-live]')!;
  const hint = fig.querySelector<HTMLElement>('[data-pacer-hint]')!;
  const listen = fig.querySelector<HTMLButtonElement>('[data-listen]')!;
  const soon = fig.querySelector<HTMLElement>('[data-voice-soon]');
  const hintText = hint.textContent ?? '';
  const voice = fig.querySelector<HTMLAudioElement>('[data-voice]');
  // While Grant's recording plays, the animation follows its clock (requirement 10.4)
  const voiceClock = () => (guided && voice && !voice.paused ? voice.currentTime * 1000 : null);
  let start = performance.now(), guided = false, lastPhase = '', visible = true;
  let doneTimer: number | undefined;

  const draw = (t: number) => {
    const s = level(t);
    if (reduce.matches) {
      fig.classList.add('reduced'); ring.style.transform = ''; ring.style.opacity = (0.45 + 0.55 * s).toFixed(3);
    } else {
      fig.classList.remove('reduced'); ring.style.opacity = ''; ring.style.transform = `scale(${(0.62 + 0.38 * s).toFixed(4)})`;
      const a = 2 * Math.PI * (t / CYCLE);
      el.setAttribute('cx', (186 * Math.cos(a)).toFixed(2)); el.setAttribute('cy', (76 * Math.sin(a)).toFixed(2));
    }
  };
  const finish = (msg: string) => {
    guided = false; fig.classList.remove('guided'); start = performance.now();
    listen.textContent = S.listen; if (soon) soon.hidden = true;
    if (voice) { voice.pause(); voice.currentTime = 0; }
    label.textContent = S.in; hint.textContent = msg; live.textContent = msg;
    clearTimeout(doneTimer); doneTimer = window.setTimeout(() => { hint.textContent = hintText; }, 8000);
  };
  const begin = () => {
    guided = true; fig.classList.add('guided'); start = performance.now(); lastPhase = ''; clearTimeout(doneTimer);
    listen.textContent = S.stop; if (soon) soon.hidden = false;
    if (voice) { voice.currentTime = 0; voice.play().catch(() => { /* blocked: animation runs on its own clock */ }); }
  };

  const frame = (now: number) => {
    if (visible) {
      const run = voiceClock() ?? now - start;
      {
        const t = run % CYCLE; draw(t);
        const phase = t < IN ? 'in' : 'out';
        const n = t < IN ? Math.floor(t / 1000) + 1 : Math.floor((t - IN) / 1000) + 1;
        label.textContent = guided ? `${S[phase]} · ${n}` : S[phase];
        if (guided && phase !== lastPhase) live.textContent = phase === 'in' ? S.breathIn : S.breathOut;
        lastPhase = phase;
        if (guided) {
          hint.textContent = S.progress.replace('{n}', String(Math.min(6, Math.floor(run / CYCLE) + 1)))
            .replace('{s}', String(Math.max(0, Math.ceil((GUIDED - run) / 1000))));
          if (run >= GUIDED) finish(S.done);
        }
      }
    }
    requestAnimationFrame(frame);
  };

  const toggle = () => (guided ? finish(S.stopped) : begin());
  fig.querySelector('[data-pacer-start]')!.addEventListener('click', toggle);
  listen.addEventListener('click', toggle);
  voice?.addEventListener('ended', () => { if (guided) finish(S.done); });
  // A pillar's example practice links here (9.3): follow the link, start the session, focus Listen/Stop
  document.querySelectorAll('[data-try="pacer"]').forEach((a) => a.addEventListener('click', () => {
    if (!guided) begin();
    setTimeout(() => listen.focus({ preventScroll: true }), 60); // after the browser has handled the link
  }));
  // Don't animate while off screen
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(fig);
  requestAnimationFrame(frame);
});
