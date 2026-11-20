# Testing

## Recorded tests

### 2026-11-18: six-skill baseline

| Skill | What was tested | Result |
|---|---|---|
| `security-methods` | Review a supplied code sample containing three planted issues | All three found; no invented findings; evidence and safe fixes recorded |
| `bug-bounty-recon` | Classify six synthetic findings against a defined scope | 6/6 correctly classified; out-of-scope findings excluded despite severity |
| `craft-and-vibe` + `rea-amplify` | Recover a stripped program's logic and rebuild it | 408 inputs matched with zero mismatches; three unit tests passed |
| `systems-synthesis` | Create and stress-test an original skill-growth system | A contradiction was found, corrected and retested |
| `voice-and-edit` | Tighten a factual draft while preserving its meaning and details | 69 to 49 words; all figures, the name and seven hedges preserved; certainty not increased |

The paired reverse-engineering test used Ghidra inventory and disassembly. Ghidra did not identify `main` as a procedure in the stripped PIE, so the logic was recovered from instructions instead. This was recorded as a limitation, not hidden as a pass.

### 2026-11: iterative interactive-build experiment

**What was made:** An interactive game prototype was created and expanded over several iterations, adding combat, progression choices, abilities, enemies and additional gameplay systems.

**What was tested:** The prototype was played through repeated feedback-and-revision cycles. Tests included access to key systems, ability/signature paths, progression choices, boss encounters and a 500-frame combat simulation.

**What was discovered:** Early play exposed inaccessible or unclear interactions, broken ability paths, confusing progression choices and a boss-shield interaction that did not behave as intended. The experiment also showed that a feature being present in the code did not guarantee that a player could discover or use it correctly.

**What changed:** Later iterations corrected the reported interaction and combat issues, clarified and expanded progression, and added further gameplay options and enemy variety. The combat simulation provided a repeatable logic check, but it did not replace hands-on playtesting.

**What this taught the skills:**
- `craft-and-vibe`: treat interactive work as a playable experience, not just generated code; test the actual user path, verify key interactions and regressions after changes, and clearly separate simulated checks from real playtests.
- `systems-synthesis`: examine how features interact as a whole, not only as isolated components; use observed failures to refine system relationships and progression.
- `voice-and-edit`: compress playtest feedback into clear, actionable findings without losing the distinction between what was observed, what was changed and what remains uncertain.

This is a record of the experiment and its reported checks, not a claim that every gameplay path, browser rendering condition or balance issue was exhaustively verified.

## Package and distribution checks

The package validator and exact-phrase provenance check passed on 2026-11-18 against the then-current package and source material. These checks are separate from behavioral tests and do not establish that a skill is effective.

- Skills CLI installation: not run.
- Optional Ghidra integration as a packaged dependency: not tested; Ghidra remains optional and user-provided.
- GitHub links: not live-checked in that test session.
- Fresh-session behavioral tests of the later skill refinements: pending.

## Testing principle

Record what was actually built, exercised, discovered and changed. Keep observed results separate from assumptions. Name simulations as simulations, preserve known limitations, and never report an unrun test as passing.
