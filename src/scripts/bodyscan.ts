import { CYCLE, level, reduceMotion as reduce } from './breath';
const ZONES = ['feet', 'legs', 'hips', 'belly', 'chest', 'arms', 'shoulders', 'face'];
const AMBIENT = 3500, GUIDED = 15000;

document.querySelectorAll<HTMLElement>('[data-scan]').forEach((box) => {
  const section = box.closest('section')!;
  const S = JSON.parse(box.dataset.strings!) as { names: Record<string, string>; count: string; done: string; stopped: string; pause: string; resume: string };
  const svg = box.querySelector('svg')!;
  const groups = ZONES.map((z) => box.querySelector<SVGGElement>(`[data-zone="${z}"]`)!);
  const name = box.querySelector<HTMLElement>('[data-scan-name]')!;
  const count = box.querySelector<HTMLElement>('[data-scan-count]')!;
  const live = box.querySelector<HTMLElement>('[data-scan-live]')!;
  const pauseBtn = section.querySelector<HTMLButtonElement>('[data-scan-pause]')!;
  const stopBtn = section.querySelector<HTMLButtonElement>('[data-scan-stop]')!;
  let start = performance.now(), paused = false, pausedAt = 0, guided = false, last = -1, visible = true;

  const show = (i: number) => {
    if (i === last) return;
    last = i;
    groups.forEach((g, j) => g.classList.toggle('on', j === i));
    name.textContent = S.names[ZONES[i]];
    count.textContent = guided ? S.count.replace('{n}', String(i + 1)) : '';
    if (guided) live.textContent = S.names[ZONES[i]];
  };
  const finish = (msg: string) => {
    guided = false; stopBtn.hidden = true; start = performance.now(); last = -1;
    name.textContent = msg; count.textContent = ''; live.textContent = msg;
  };
  const frame = (now: number) => {
    if (!paused && visible) {
      const run = now - start;
      svg.style.setProperty('--b', reduce.matches ? '.5' : level(run % CYCLE).toFixed(3));
      if (guided) {
        if (run >= GUIDED * ZONES.length) finish(S.done); else show(Math.floor(run / GUIDED));
      } else if (run > 4000 || last >= 0) {
        show(Math.floor(run / AMBIENT) % ZONES.length);
      }
    }
    requestAnimationFrame(frame);
  };
  box.querySelector('[data-scan-start]')!.addEventListener('click', () => {
    guided = true; paused = false; last = -1; start = performance.now();
    pauseBtn.setAttribute('aria-pressed', 'false'); pauseBtn.textContent = S.pause; stopBtn.hidden = false;
  });
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
    pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? S.resume : S.pause;
  });
  stopBtn.addEventListener('click', () => finish(S.stopped));
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(box);
  show(0);
  requestAnimationFrame(frame);
});
