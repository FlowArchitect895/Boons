# Boons

Six portable skills for disciplined security work, engineering, creative design,
editing, and artifact analysis.

Boons separates **method from capability**: skills provide instructions and
guardrails; the host agent and connected tools determine what can actually run.

## Get Boons

- **[Agensi marketplace](https://www.agensi.io/skills/boons)** — recommended quick
  connection through an MCP-compatible agent.
- **[GitHub repository](https://github.com/FlowArchitect895/Boons)** — inspect,
  fork, install, modify, and self-manage the open-source skills.

Agensi is a distribution and connection route, not a requirement. GitHub remains
available for manual installation and custom integrations.

## Skills

| Skill | Purpose | Version |
|---|---|---:|
| `cybersecurity/security-methods` | Evidence-led defensive security analysis | 0.3.0 |
| `cybersecurity/bug-bounty-recon` | Scope-first bounty research and triage | 0.3.0 |
| `coding/craft-and-vibe` | Creative engineering, game creation and layered verification | 0.4.0 |
| `creative/systems-synthesis` | Original systems built from high-level patterns | 0.3.0 |
| `creative/voice-and-edit` | Fact-preserving editing that preserves authorial character | 0.2.0 |
| `meta/rea-amplify` | Authorized artifact analysis that grounds another skill | 0.3.0 |

`craft-and-vibe` includes a game-development workflow: player promise, core
loop, state and mechanic design, iterative implementation, balance review, and
layered gameplay testing. See `TESTING.md` for recorded experiments and limits.

## Choose your environment

| Environment | Best use |
|---|---|
| ChatGPT or Claude chat | Reasoning, writing, research and analysis of supplied material |
| Codex or Claude Code | Repository work, coding, debugging and tests |
| Local model / personal agent | Custom, self-managed workflows after tool integration |

Chat interfaces can use Boons for meaningful work without local terminal access.
Workspace-connected agents are better suited to editing files and running
commands. A local model needs an application or agent runtime to connect MCP,
filesystems and tools.

## Start here

1. **[Environment guide](ENVIRONMENTS.md)** — choose chat, coding agent, WSL/Linux
   or a local workspace.
2. **[Integrations](INTEGRATIONS.md)** — connect Agensi, Codex, Claude Code and
   optional REA.
3. **[Installation](INSTALL.md)** — install selected skills from GitHub.
4. **[Reference directory](REFERENCES.md)** — primary project and tool links.
5. **[Team workflow](WORKFLOWS.md)** — how to coordinate the skills without blurring their roles.
6. **[Testing record](TESTING.md)** — what has been tested and what remains open.

### Agensi quick start

Open [Boons on Agensi](https://www.agensi.io/skills/boons), sign in, and follow
the current MCP connection instructions for your agent. Complete the requested
authorization, then ask the connected agent to use Boons. See
[INTEGRATIONS.md](INTEGRATIONS.md) for connection boundaries and client notes.

### GitHub installation

With the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons
```

Or follow [INSTALL.md](INSTALL.md) to copy selected skill folders manually.
The CLI supports multiple agents; confirm the current supported-client list
and the destination it selects before relying on an installation.

## Checks

Run `python3 tools/validate.py` to check package shape and metadata.

Run `python3 tools/provenance.py --source PATH` with each authorized reference
file to check for exact phrase reuse. That check cannot establish authorship or
detect paraphrase; human review is still required.

## Development status

The skills remain experimental. The original fresh-session tests were run on
2026-11-18 against the versions available at that time. Historical results do
not automatically validate later refinements. See `TESTING.md`.

The skills do not bundle analysis tools. `rea-amplify` can work from supplied
artifacts and available tool results without REA software. REA is an optional,
independently maintained integration; Ghidra and other analysis engines are
separate dependencies. See [INTEGRATIONS.md](INTEGRATIONS.md).

## Contributing

Fork the repository, make changes on a branch, run the checks, and open a pull
request. Changes reach `main` only after maintainer review. See
`CONTRIBUTING.md`.

## License

Apache-2.0. The full license text is in `LICENSE`.
