# Testing

This file records experiments, checks, results and limitations. It is not a
catalogue of external links; see [REFERENCES.md](REFERENCES.md) for sources.

## Recorded tests

### 2026-11-18: six-skill baseline

| Skill | What was tested | Result |
|---|---|---|
| `security-methods` | Review a supplied code sample containing three planted issues | All three found; no invented findings; evidence and safe fixes recorded |
| `bug-bounty-recon` | Classify six synthetic findings against a defined scope | 6/6 correctly classified; out-of-scope findings excluded despite severity |
| `craft-and-vibe` + `rea-amplify` | Recover a stripped program's logic and rebuild it | 408 inputs matched with zero mismatches; three unit tests passed |
| `systems-synthesis` | Create and stress-test an original skill-growth system | A contradiction was found, corrected and retested |
| `voice-and-edit` | Tighten a factual draft while preserving its meaning and details | 69 to 49 words; all figures, the name and seven hedges preserved; certainty not increased |

The paired reverse-engineering test used Ghidra inventory and disassembly.
Ghidra did not identify `main` as a procedure in the stripped PIE, so the
logic was recovered from instructions instead. This was recorded as a
limitation, not hidden as a pass.

### 2026-11: iterative interactive-build experiment

**What was made:** An interactive game prototype was created and expanded over
several iterations, adding combat, progression choices, abilities, enemies and
additional gameplay systems.

**What was tested:** The prototype was played through repeated feedback-and-
revision cycles. Tests included access to key systems, ability/signature paths,
progression choices, boss encounters and a 500-frame combat simulation.

**What was discovered:** Early play exposed inaccessible or unclear
interactions, broken ability paths, confusing progression choices and a
boss-shield interaction that did not behave as intended. A feature being
present in code did not guarantee that a player could discover or use it.

**What changed:** Later iterations corrected reported interaction and combat
issues, clarified progression, and added gameplay options and enemy variety.
The simulation provided a repeatable logic check, not a replacement for
hands-on playtesting.

**Lessons:** `craft-and-vibe` should test real user paths; `systems-synthesis`
should inspect interactions between features; `voice-and-edit` should
compress feedback without losing the distinction between observation, change
and uncertainty.

This is a record of the reported experiment, not proof that every gameplay
path, browser condition or balance issue was exhaustively verified.

### 2026-11-20: WebGoat evidence-boundary benchmark

**Environment reported by the user:** A local WebGoat/WebWolf deployment in
Docker, with ports bound to loopback. The user supplied screenshots and
startup-log excerpts from that environment.

**Evidence reviewed:** Login and registration screens, WebWolf login screen,
container startup messages, and a WebGoat lesson description referring to a
`hijack_cookie` and a cookie-prediction objective.

**Hypotheses retained, not confirmed:**
- The lesson may involve a predictable session identifier. No actual cookie
  value, entropy, cookie attributes, authentication effect or exploitability
  was inspected.
- A credential-like value appeared in startup logs. Its validity, privilege,
  accessibility and security impact were not established. The raw value is
  intentionally not recorded here.

**Custom auxiliary validator:** A small standalone validator was written and
run outside this repository against a structured evidence record. Five checks
passed: cautious hypothesis accepted; unsupported certainty rejected;
severity/eligibility assertion without confirmed scope rejected; unknown
evidence reference rejected; and missing unknowns rejected.

**Important limitation:** This validator was not part of Boons, did not execute
any of the Boons skills as software, and did not test a live HTTP session. No
HTTP traffic, cookie values, Nmap scan, Burp capture, source review of the
running container or autonomous recon was performed. This was an evidence-
reasoning benchmark, not a live reconnaissance test.

**What the benchmark changed in this branch:**
- Bug Bounty Recon now separates evidence review and collection planning from
  target-facing execution, which remains disabled in this version.
- Security Methods now requires an explicit working mode and adversarial
  challenge of findings.
- REA Amplify now records environment/tool access and coverage more explicitly,
  and adversarially reviews downstream handoffs.
- Systems Synthesis now includes an opposing-view and falsification pass.

These are design changes motivated by the benchmark. They have not yet passed
fresh-session behavioral tests.

### 2026-11-20: ecosystem documentation review

Updated the README, installation guide, environment guide, integration guide
and reference directory. External documentation was reviewed for Agensi MCP,
REA upstream setup and Claude Code MCP guidance.

**Not tested:** live Agensi authentication or MCP connection; Skills CLI
installation; REA installation; Codex/Claude Code/local-model integration; or
Kali/WSL command execution from this ChatGPT session. Documentation review is
not an integration test.

## Package and distribution checks

The package validator and exact-phrase provenance check passed on 2026-11-18
against the package state at that time. They are separate from behavioral tests
and do not establish that a skill is effective.

- Skills CLI installation: not run.
- Optional Ghidra integration as a packaged dependency: not tested.
- Fresh-session behavioral tests of the revised skills in this branch: pending.
- The custom five-case evidence validator described above is not integrated
  into this repository.

## Testing principle

Record what was actually built, exercised, discovered and changed. Keep
observed results separate from assumptions. Name simulations as simulations,
preserve known limitations, and never report an unrun test as passing.
