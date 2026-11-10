// Breath pacer behaviour. The ambient loop has a visible pause (WCAG 2.2.2); the guided minute is six 10-second breaths.
import { IN, CYCLE, level, reduceMotion as reduce } from './breath';
const GUIDED = 60000;

document.querySelectorAll<HTMLElement>('[data-pacer]').forEach((fig) => {
  const S = JSON.parse(fig.dataset.strings!) as Record<string, string>;
  const ring = fig.querySelector<SVGGElement>('.pacer-ring')!;
  const el = fig.querySelector<SVGCircleElement>('.pacer-electron')!;
  const label = fig.querySelector<HTMLElement>('[data-pacer-label]')!;
  const live = fig.querySelector<HTMLElement>('[data-pacer-live]')!;
  const hint = fig.querySelector<HTMLElement>('[data-pacer-hint]')!;
  const pauseBtn = fig.querySelector<HTMLButtonElement>('[data-pacer-pause]')!;
  const stopBtn = fig.querySelector<HTMLButtonElement>('[data-pacer-stop]')!;
  const hintText = hint.textContent ?? '';
  const voice = fig.querySelector<HTMLAudioElement>('[data-voice]');
  const voiceBtn = fig.querySelector<HTMLButtonElement>('[data-voice-toggle]');
  let voiceOn = !!voice;
  // While Grant's recording plays, the animation follows its clock (requirement 10.4)
  const voiceClock = () => (guided && voice && voiceOn && !voice.paused ? voice.currentTime * 1000 : null);
  let start = performance.now(), paused = false, pausedAt = 0, guided = false, lastPhase = '', visible = true;
  let doneTimer: number | undefined;

  const finish = (msg: string) => {
    guided = false; fig.classList.remove('guided'); stopBtn.hidden = true; start = performance.now();
    if (voice) { voice.pause(); voice.currentTime = 0; }
    hint.textContent = msg; live.textContent = msg;
    clearTimeout(doneTimer); doneTimer = window.setTimeout(() => { hint.textContent = hintText; }, 8000);
  };

  const frame = (now: number) => {
    if (!paused && visible) {
      const run = voiceClock() ?? now - start, t = run % CYCLE, s = level(t);
      if (reduce.matches) {
        fig.classList.add('reduced'); ring.style.transform = ''; ring.style.opacity = (0.45 + 0.55 * s).toFixed(3);
      } else {
        fig.classList.remove('reduced'); ring.style.opacity = ''; ring.style.transform = `scale(${(0.62 + 0.38 * s).toFixed(4)})`;
        const a = 2 * Math.PI * (t / CYCLE);
        el.setAttribute('cx', (186 * Math.cos(a)).toFixed(2)); el.setAttribute('cy', (76 * Math.sin(a)).toFixed(2));
      }
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
    requestAnimationFrame(frame);
  };

  fig.querySelector('[data-pacer-start]')!.addEventListener('click', () => {
    guided = true; paused = false; pauseBtn.setAttribute('aria-pressed', 'false'); pauseBtn.textContent = S.pause;
    fig.classList.add('guided'); stopBtn.hidden = false; start = performance.now(); lastPhase = ''; clearTimeout(doneTimer);
    if (voice && voiceOn) { voice.currentTime = 0; voice.play().catch(() => { /* blocked: animation runs on its own clock */ }); }
  });
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
    if (voice && guided && voiceOn) { if (paused) voice.pause(); else voice.play().catch(() => {}); }
    pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? S.resume : S.pause;
  });
  stopBtn.addEventListener('click', () => finish(S.stopped));
  voiceBtn?.addEventListener('click', () => {
    voiceOn = !voiceOn;
    voiceBtn.setAttribute('aria-pressed', String(voiceOn)); voiceBtn.textContent = voiceOn ? S.voiceOn : S.voiceOff;
    if (!voiceOn && voice) { start = performance.now() - voice.currentTime * 1000; voice.pause(); }
    else if (voiceOn && voice && guided && !paused) { voice.currentTime = (performance.now() - start) / 1000; voice.play().catch(() => {}); }
  });
  // Don't animate while off screen
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(fig);
  requestAnimationFrame(frame);
});
