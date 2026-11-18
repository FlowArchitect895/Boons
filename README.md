# Boons

Six portable skills for disciplined security work, engineering, creative design,
editing, and artifact analysis.

## Skills

- `cybersecurity/security-methods`: evidence-led defensive security analysis.
- `cybersecurity/bug-bounty-recon`: scope-first bounty research and triage.
- `coding/craft-and-vibe`: creative engineering with deliberate verification.
- `creative/systems-synthesis`: original systems built from high-level patterns.
- `creative/voice-and-edit`: fact-preserving writing and editing.
- `meta/rea-amplify`: authorized artifact analysis that grounds another skill.

Each Boon passed a fresh-session task test on 2026-11-18 (see TESTING.md). The
set is prepared for release but not yet published to a standalone public
repository.

## Checks

Run `python3 tools/validate.py` to check the package shape and metadata.
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
CONTRIBUTING.md.

The skills do not bundle analysis tools. `rea-amplify` adapts to an authorized
analysis capability that is actually available in the user's session. It does
not require a particular REA framework. [Ghidra](https://github.com/NationalSecurityAgency/ghidra)
is one optional analysis environment, not a dependency; use it only when the
user has configured and authorized it.

## License

Apache-2.0. The full license text is in LICENSE.
