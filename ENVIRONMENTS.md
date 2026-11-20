# Boons environment guide

Boons skills are portable instructions. The host AI and its connected tools determine what the user can actually do.

## Choose an environment

| Environment | Best use | What it does not provide by itself |
|---|---|---|
| ChatGPT or Claude chat | Reasoning, writing, research, and analysis of supplied material | Direct access to a local WSL filesystem, terminal, or Docker containers |
| Chat with Agensi MCP | Discovering and using Boons through a connected agent | A local shell or project workspace unless the host separately provides one |
| Codex or Claude Code | Repository work, coding, debugging, tests, and tool-assisted workflows | Unlimited permissions; actions remain subject to client settings and approvals |
| Local model and custom agent | Private or self-managed workflows | MCP, filesystem, terminal, and tool access unless the local application implements them |

Use Agensi where the selected chat or agent supports its MCP connection. For coding and repository work, Codex or Claude Code generally provide a more direct workspace workflow than a chat-only interface. Exact features depend on the product, plan, client version, and permissions.

## Three ways to use Boons

### 1. Chat-first

1. Connect Agensi where supported, or provide the relevant skill from GitHub.
2. Give the assistant the source material: files, code, screenshots, logs, or a clearly scoped question.
3. Ask it to follow the relevant Boon.
4. Perform local actions yourself and return the resulting evidence.

This works well for planning, editing, security reasoning, documentation, and supplied-artifact analysis. It does not imply that the assistant can see your computer or run local tools.

### 2. Workspace-connected agent

1. Open the intended repository in Codex or Claude Code.
2. Connect Agensi or install the relevant Boons skill locally.
3. Confirm the agent can see the intended workspace and only the permissions needed.
4. Ask for a plan before consequential changes.
5. Require tests, diff review, and a clear report of what was and was not run.

This is the recommended route for implementation, debugging, repository maintenance, and repeatable development tasks.

### 3. Local model or personal AI workspace

A local model does not gain Agensi access simply because it can read a skill. The application around the model must implement an MCP client or another supported integration.

A developer can use Claude Code, Codex, or another coding agent to build and test that adapter. A custom integration needs to handle:

- MCP transport and server discovery.
- OAuth or other authentication required by the service.
- Tool discovery and invocation.
- Passing tool results into the model context.
- Permission boundaries, errors, and credential handling.

For a personal system such as Odysseus, this is an engineering integration—not a one-line skill installation. You may also choose another local implementation route.

## WSL and Linux

Use the environment that matches the work:

- **Ubuntu WSL:** general development, coding, local models, and application work.
- **Kali WSL:** security tooling, controlled labs, and authorized assessment work.

They are separate environments unless you deliberately connect them. Verify the current working directory, Git root, active container, network binding, and tool permissions before running commands. Do not assume a chat assistant can access either WSL distribution.

For local labs, bind services to loopback when external access is unnecessary. Keep credentials and session tokens out of screenshots, logs, commits, and shared evidence.

## Capability rules

- A skill supplies a workflow; it does not install tools or grant permissions.
- MCP supplies a connection to tools; it does not automatically provide a terminal or filesystem.
- A coding agent may execute commands only within its configured access and approval boundaries.
- A local model needs an application or agent runtime to use external tools.
- Security skills require authorization for the specific assets and actions. The current Bug Bounty Recon skill is an evidence organizer and does not query targets, scan, exploit, or contact program infrastructure.

## Related guides

- [Install Boons](INSTALL.md)
- [Agensi and external integrations](INTEGRATIONS.md)
- [Trusted references](REFERENCES.md)
- [Testing record](TESTING.md)
