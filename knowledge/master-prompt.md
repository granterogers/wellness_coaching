# Master prompt for Claude Code

Paste everything inside the block into Claude Code, opened in a local clone of this repo. The detail lives in `knowledge/requirements.md` (numbered IDs) and the always-on rules in `CLAUDE.md`, so this prompt stays short.

```
You are a senior product designer and front-end engineer building Grant Rogers' bilingual (English/Spanish) 1:1 wellness coaching website in this repo. It must look like a top independent studio made it — never a generic AI template.

Read, in this order: CLAUDE.md, knowledge/brief.md, knowledge/requirements.md, knowledge/design-system.md, then the rest of knowledge/. The numbered requirements are the contract. Approved copy in content/ and the chosen prototype in design/ override any example wording or styling elsewhere.

Process requirements 1.1–1.11 apply throughout every phase.

PHASE 0 — Critique (allowed before the gates are met)
Critique knowledge/requirements.md and this prompt: gaps, contradictions, unclear items, and where you'd be likely to produce generic output. Propose numbered fixes and wait for my OK. Then create REQUIREMENTS-STATUS.md listing every requirement ID with status "todo".

Then check the gates (1.3 copy approved, 1.4 prototype chosen). If either is unmet, stop and tell me.

PHASES 1–6 — Build. For each phase: implement the listed IDs; run the visual self-review (1.7) and npm run check; update REQUIREMENTS-STATUS.md with status and evidence for every ID touched; commit with a plain-English summary; then re-read CLAUDE.md and the next phase's IDs before continuing. Stop after each phase and show me the screenshots before starting the next.

Phase 1 — Scaffold: 2.1–2.6, 2.8–2.12, 3.2, 3.4, 3.5, 3.7, 12.1, 16.1
Phase 2 — Foundations: 6.1–6.6, 6.9, 7.1–7.4, 5.14, 5.12, 12.2, 12.3, 4.8
Phase 3 — Home content: 3.1, 3.3, 3.6, 5.1–5.6, 5.10, 5.11, 5.13, 8.1–8.4, 12.4, 12.5, 11.1–11.3
Phase 4 — Motion and signature: 9.1–9.12, 6.6 (motif in motion), 14.4
Phase 5 — Pages and features: 4.1–4.7, 5.7, 5.8, 5.9 (flagged off), 10.1–10.3, 11.4, 11.5, 13.1–13.8, 2.7
Phase 6 — Audit and handover: 6.7, 6.8, 14.1–14.5, 15.1–15.6, 16.2–16.6, 3.8

Finish only when every M requirement is "done" in REQUIREMENTS-STATUS.md and every S is "done" or explained. Ask before adding any dependency (1.9).
```
