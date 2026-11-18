# Testing

Status: all six skills passed a fresh-session test on 2026-11-18.

| Skill | Fresh-session task | Result |
|---|---|---|
| `security-methods` | Review a supplied snippet with 3 planted issues; evidence-labeled findings | Pass (2026-11-18): all 3 found, none invented, labeled, non-target-facing |
| `bug-bounty-recon` | Triage 6 synthetic findings against a synthetic scope | Pass (2026-11-18): 6/6 classified, scope held over severity, no out-of-scope proposed |
| `craft-and-vibe` | Rebuild a stripped binary's transform from rea-amplify findings; tests + 408-input differential sweep | Pass (2026-11-18, paid Claude Code) |
| `systems-synthesis` | Synthesize an original skill-growth system (tide + compounding) and stress-test it | Pass (2026-11-18): stress test caught a real contradiction, fixed, re-run consistent |
| `voice-and-edit` | Tighten a factual draft and verify preservation | Pass (2026-11-18): 69->49 words, all figures/name/7 hedges kept, no certainty raised |
| `rea-amplify` | Recover an owner-authored stripped ELF's algorithm (Ghidra inventory + objdump), hand findings to craft-and-vibe | Pass (2026-11-18, paid Claude Code) |

The package validator passes and the exact-phrase provenance check is clean
(run 2026-11-18 against the private Dragon source skills: no 8-word overlap).
These are separate from the behavioral tests below. Passing either does not mean
a skill is effective; each still needs a fresh-session task test.

## Distribution checks

- GitHub install through the Skills CLI: Not run. This draft has no standalone
  public repository URL.
- Optional Ghidra integration: Not run. Ghidra is documented as an optional
  user-provided tool, not a package dependency.
- GitHub links in `README.md`: Not live-checked in this session.

## 2026-11-18 paired test: rea-amplify + craft-and-vibe

An owner-authored C program (a 32-bit integer transform) was compiled and
stripped. With no access to the source, `rea-amplify` recovered its algorithm
from the stripped ELF: REA/Ghidra gave the procedure and import inventory and
the entry-to-main pointer, and objdump disassembly of main (file offset 0x10a0)
showed the logic (FNV-1a over four little-endian bytes, a final xor-shift, mod
100000). `craft-and-vibe` rebuilt it as a clean, documented Python module with
tests. The rebuild reproduced the real binary's output on all 408 inputs tested
(8 edge values plus 400 random), zero mismatches, and 3 unit tests pass.

Honest limitation found: Ghidra's default analysis did not define `main` as a
procedure in this stripped PIE, so the decompiler returned no body for it; the
logic was recovered at the instruction level instead. The skill handled this by
falling back to disassembly, as its workflow intends.

Artifacts (scratch, not committed): the C source, binary and the Python rebuild
live under the session scratchpad and `~/projects/python/vibe-test/`.

## 2026-11-18 tests for the other four

- **voice-and-edit:** a 69-word factual draft was tightened to 49 words in a direct voice. A token check confirmed all six figures (12, 3, 420, 15, 30, 2024), the name (Mensah), and all seven hedges survived, and no certainty word was added.
- **bug-bounty-recon:** six synthetic findings were triaged against a synthetic scope. All six matched the known-correct in/out answer. A critical (default creds on an excluded internal host) and a high (XSS on an excluded blog) were both correctly excluded, so scope held over severity, and no out-of-scope asset was proposed for testing.
- **security-methods:** a supplied Python snippet with three planted issues (command injection, hardcoded secret, SQL injection) was reviewed. All three were found at the right lines, none invented, each labeled verified/inferred/assumed with a proportionate fix and a local confirmation step, and nothing target-facing was proposed.
- **systems-synthesis:** an original skill-growth system was synthesized from the functions of a tide and of compounding, with original terminology. Its stress-test step surfaced a real internal contradiction (the retained floor could exceed the recorded peak); the design was corrected and the re-run was consistent, with the steady builder ending far above the all-push sprinter, matching the intent. References stayed at the function level; no protected work was reproduced.

All four are judgment-assisted tests run by paid Claude Code; voice-and-edit and bug-bounty-recon were checked mechanically against a known answer, security-methods against planted issues, systems-synthesis against a runnable model of its own rules.
