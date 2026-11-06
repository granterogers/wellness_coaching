// Shared breath rhythm for the pacer and the body scan: 4 s in, 6 s out.
export const IN = 4000;
export const CYCLE = 10000;
export const ease = (x: number) => 0.5 - 0.5 * Math.cos(Math.PI * x);
/** 0 → 1 over the in-breath, 1 → 0 over the out-breath. */
export const level = (t: number) => (t < IN ? ease(t / IN) : 1 - ease((t - IN) / (CYCLE - IN)));
export const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
