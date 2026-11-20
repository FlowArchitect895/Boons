# Boons

Six portable skills for disciplined security work, engineering, creative design,
editing, and artifact analysis.

## Skills

| Skill | Purpose | Version |
|---|---|---:|
| `cybersecurity/security-methods` | Evidence-led defensive security analysis | 0.2.0 |
| `cybersecurity/bug-bounty-recon` | Scope-first bounty research and triage | 0.2.0 |
| `coding/craft-and-vibe` | Creative engineering, game creation and layered verification | 0.4.0 |
| `creative/systems-synthesis` | Original systems built from high-level patterns | 0.2.0 |
| `creative/voice-and-edit` | Fact-preserving editing that preserves authorial character | 0.2.0 |
| `meta/rea-amplify` | Authorized artifact analysis that grounds another skill | 0.2.0 |

`craft-and-vibe` now includes a game-development workflow: player promise, core loop, state and mechanic design, iterative implementation, balance review, and layered gameplay testing. The AURA//ARMORY prototype is documented as a candidate regression-test case in `TESTING.md`; its presence there does not mean those tests have been run.

The skills remain experimental. The original fresh-session tests were run on
2026-11-18 against the versions available at that time. See `TESTING.md`.
Those historical results do not automatically validate the refined versions
in this bundle.

## Checks

Run `python3 tools/validate.py` to check package shape and metadata.

Run `python3 tools/provenance.py --source PATH` with each authorized reference
file to check for exact phrase reuse. That check cannot establish authorship or
detect paraphrase; human review is still required.

## Install

With the [Skills CLI](https://github.com/vercel-labs/skills), which installs into
Claude Code, Codex, Copilot, OpenCode and other supported agents:

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons
```

`DISABLE_TELEMETRY=1` stops the CLI from reporting which skills you installed;
leave it off if you do not mind. For an assistant without installer support,
copy the skill folders you want into its documented Agent Skills location.

## Contributing

Fork the repository, make your change on a branch, and open a pull request.
Changes reach `main` only after the maintainer reviews and merges them. See
`CONTRIBUTING.md`.

The skills do not bundle analysis tools. `rea-amplify` adapts to an authorized
analysis capability that is actually available in the user's session. It does
not require a particular REA framework. [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
is one optional analysis environment, not a dependency; use it only when the
user has configured and authorized it.

## License

Apache-2.0. The full license text is in `LICENSE`.
