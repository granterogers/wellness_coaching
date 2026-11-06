# Master prompt for Claude Code

Paste everything inside the block into Claude Code on the web (claude.ai/code), connected to this GitHub repo. Nothing needs installing. The detail lives in `knowledge/requirements.md` (numbered IDs) and the always-on rules in `CLAUDE.md`, so this prompt stays short.

```
You are a senior product designer and front-end engineer building Grant Rogers' bilingual (English/Spanish) 1:1 wellness coaching website in this repo. It must look like a top independent studio made it — never a generic AI template.

Read, in this order: CLAUDE.md, knowledge/brief.md, knowledge/requirements.md, knowledge/design-system.md, then the rest of knowledge/. The numbered requirements are the contract. Approved copy in content/ and the chosen prototype in design/ override any example wording or styling elsewhere.

Process requirements 1.1–1.11 apply throughout every phase.

PHASE 0 — Critique (allowed before the gates are met)
Critique knowledge/requirements.md and this prompt: gaps, contradictions, unclear items, and where you'd be likely to produce generic output. Apply the fixes you're confident about, list them, and list (numbered) anything that needs my decision. Create REQUIREMENTS-STATUS.md listing every requirement ID with status "todo" (or its real status). Stop and wait for my answers.

Then check the gates (1.3 copy approved, 1.4 prototype chosen). If either is unmet, stop and tell me. Copy is drafted and approved per knowledge/copywriting-brief.md (two rounds of edits); prototypes are built and published per design/README.md.

PHASES 1–6 — Build. For each phase: implement the listed IDs; run the visual self-review (1.7) and npm run check; update REQUIREMENTS-STATUS.md with status and evidence for every ID touched; commit with a plain-English summary; then re-read CLAUDE.md and the next phase's IDs before continuing. Stop for my approval only after Phase 3 (the homepage), with the preview link and screenshots; otherwise continue to the next phase on your own. At the end, give me the preview link and a summary of REQUIREMENTS-STATUS.md.

Phase 1 — Scaffold: 2.1–2.6, 2.8–2.12, 3.2, 3.4, 3.5, 3.7, 12.1, 13.8 (noindex from the first deploy), 16.1
Phase 2 — Foundations: 6.1–6.6, 6.9, 7.1–7.4, 5.14, 5.12, 12.2, 12.3, 4.8
Phase 3 — Home content: 3.1, 3.3, 3.6, 5.1–5.6, 5.10, 5.11, 5.13, 8.1–8.4, 12.4, 12.5, 11.1–11.3 (the pacer is drawn statically here and animated in Phase 4) — STOP for my approval
Phase 4 — Motion and signature: 9.1–9.12 (9.13 built early, with the homepage, at Grant's request), 6.6 (motif in motion), 14.4
Phase 5 — Pages and features: 4.1–4.7, 5.7, 5.8, 5.9 (flagged off), 10.1–10.3, 11.4, 11.5, 13.1–13.7, 2.7
Phase 6 — Audit and handover: 6.7, 6.8, 14.1–14.5, 15.1–15.6, 16.2–16.6, 3.8

Finish only when every M requirement is "done" in REQUIREMENTS-STATUS.md and every S is "done" or explained. Ask before adding any dependency (1.9).
```
