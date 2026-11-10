// Body scan behaviour (9.13, 10.4). Guided timeline: settle 10 s, 22 parts × 5 s, whole body 10 s (= the voice script).
import { CYCLE, level, reduceMotion as reduce } from './breath';
const SETTLE = 10000, PART = 5000, WHOLE = 10000, AMBIENT = 2000;

document.querySelectorAll<HTMLElement>('[data-scan]').forEach((box) => {
  const section = box;
  const S = JSON.parse(box.dataset.strings!) as {
    zones: string[]; names: Record<string, string>; count: string; done: string; stopped: string;
    pause: string; resume: string; voiceOn: string; voiceOff: string;
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
  const pauseBtn = section.querySelector<HTMLButtonElement>('[data-scan-pause]')!;
  const stopBtn = section.querySelector<HTMLButtonElement>('[data-scan-stop]')!;
  const voice = box.querySelector<HTMLAudioElement>('[data-voice]');
  const voiceBtn = section.querySelector<HTMLButtonElement>('[data-voice-toggle]');
  let voiceOn = !!voice;
  let start = performance.now(), paused = false, pausedAt = 0, guided = false, last = '', visible = true;

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
    guided = false; stopBtn.hidden = true; start = performance.now(); last = '';
    if (voice) { voice.pause(); voice.currentTime = 0; }
    groups.forEach((g) => g?.classList.remove('on')); svg.classList.remove('whole', 'settle');
    name.textContent = msg; count.textContent = ''; live.textContent = msg;
  };
  const at = (run: number): [string, number] => {
    if (run < SETTLE) return ['settle', 0];
    const i = Math.floor((run - SETTLE) / PART);
    return i < parts.length ? [parts[i], i + 1] : ['whole', parts.length + 1];
  };
  const frame = (now: number) => {
    if (!paused && visible) {
      const run = guided && voice && voiceOn && !voice.paused ? voice.currentTime * 1000 : now - start;
      svg.style.setProperty('--b', reduce.matches ? '.5' : level(run % CYCLE).toFixed(3));
      if (!reduce.matches) {
        const a = (2 * Math.PI * (run % (CYCLE * 2))) / (CYCLE * 2), x = RX * Math.cos(a), y = RY * Math.sin(a);
        dot.setAttribute('cx', (CX + x * Math.cos(TH) - y * Math.sin(TH)).toFixed(2));
        dot.setAttribute('cy', (CY + x * Math.sin(TH) + y * Math.cos(TH)).toFixed(2));
      }
      if (guided) {
        if (run >= TOTAL) finish(S.done); else show(...at(run));
      } else {
        const i = Math.floor(run / AMBIENT) % (S.zones.length);
        show(S.zones[i], 0);
      }
    }
    requestAnimationFrame(frame);
  };
  box.querySelector('[data-scan-start]')!.addEventListener('click', () => {
    guided = true; paused = false; last = ''; start = performance.now();
    pauseBtn.setAttribute('aria-pressed', 'false'); pauseBtn.textContent = S.pause; stopBtn.hidden = false;
    if (voice && voiceOn) { voice.currentTime = 0; voice.play().catch(() => { /* blocked: runs on its own clock */ }); }
  });
  pauseBtn.addEventListener('click', () => {
    paused = !paused;
    if (paused) pausedAt = performance.now(); else start += performance.now() - pausedAt;
    pauseBtn.setAttribute('aria-pressed', String(paused)); pauseBtn.textContent = paused ? S.resume : S.pause;
    if (voice && guided && voiceOn) { if (paused) voice.pause(); else voice.play().catch(() => {}); }
  });
  stopBtn.addEventListener('click', () => finish(S.stopped));
  voiceBtn?.addEventListener('click', () => {
    voiceOn = !voiceOn;
    voiceBtn.setAttribute('aria-pressed', String(voiceOn)); voiceBtn.textContent = voiceOn ? S.voiceOn : S.voiceOff;
    if (!voiceOn && voice) { start = performance.now() - voice.currentTime * 1000; voice.pause(); }
    else if (voiceOn && voice && guided && !paused) { voice.currentTime = (performance.now() - start) / 1000; voice.play().catch(() => {}); }
  });
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(box);
  requestAnimationFrame(frame);
});
