// Breath pacer behaviour. The ambient loop has a visible pause (WCAG 2.2.2); the guided minute is six 10-second breaths.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const IN = 4000, CYCLE = 10000, GUIDED = 60000;
const ease = (x: number) => 0.5 - 0.5 * Math.cos(Math.PI * x);
const level = (t: number) => (t < IN ? ease(t / IN) : 1 - ease((t - IN) / (CYCLE - IN)));

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
  let start = performance.now(), paused = false, pausedAt = 0, guided = false, lastPhase = '', visible = true;
  let doneTimer: number | undefined;

  const finish = (msg: string) => {
    guided = false; fig.classList.remove('guided'); stopBtn.hidden = true; start = performance.now();
    hint.textContent = msg; live.textContent = msg;
    clearTimeout(doneTimer); doneTimer = window.setTimeout(() => { hint.textContent = hintText; }, 8000);
  };

  const frame = (now: number) => {
    if (!paused && visible) {
      const run = now - start, t = run % CYCLE, s = level(t);
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
  });
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
    pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? S.resume : S.pause;
  });
  stopBtn.addEventListener('click', () => finish(S.stopped));
  // Don't animate while off screen
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(fig);
  requestAnimationFrame(frame);
});
