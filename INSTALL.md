# Installing Boons

Each Boon is a folder containing `SKILL.md`. Install all six or select only
the skills you need.

| Boon | Folder |
|---|---|
| security-methods | `cybersecurity/security-methods` |
| bug-bounty-recon | `cybersecurity/bug-bounty-recon` |
| craft-and-vibe | `coding/craft-and-vibe` |
| systems-synthesis | `creative/systems-synthesis` |
| voice-and-edit | `creative/voice-and-edit` |
| rea-amplify | `meta/rea-amplify` |

## Choose an installation route

### Option 1: Agensi (recommended quick connection)

[Open Boons on Agensi](https://www.agensi.io/skills/boons). Sign in, follow the
current MCP setup for your agent, complete authorization, and ask the connected
agent to use Boons.

Agensi is useful when you want marketplace distribution and on-demand access
without manually copying skill folders. The host agent still controls workspace,
terminal and tool access. See [INTEGRATIONS.md](INTEGRATIONS.md) for account
connection behavior, supported-client caveats and local-agent integration.

### Option 2: Skills CLI (GitHub)

The [Skills CLI](https://github.com/vercel-labs/skills) installs skills into
supported agents. It requires Node.js; check the CLI's current requirements.

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons
```

For a global install:

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons -g
```

To install one skill for Claude Code:

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons --skill craft-and-vibe -a claude-code -g
```

The CLI can report installation telemetry unless disabled. Update and remove
skills using the CLI's current commands. Verify its current agent list and
installation destination before relying on it.

### Option 3: clone and copy (no Node required)

```sh
git clone https://github.com/FlowArchitect895/Boons.git
mkdir -p ~/.claude/skills
cp -r Boons/coding/craft-and-vibe ~/.claude/skills/
```

Repeat the copy command for each selected skill and use the documented skill
directory for your agent.

### Option 4: clone and link (Linux, macOS or WSL)

A symbolic link lets a `git pull` in the clone update the installed skill.

```sh
git clone https://github.com/FlowArchitect895/Boons.git ~/Boons
mkdir -p ~/.claude/skills
ln -s ~/Boons/coding/craft-and-vibe ~/.claude/skills/craft-and-vibe
```

Use the equivalent skill directory for your agent. On Windows, links may
require Developer Mode or an administrator shell.

### Option 5: download ZIP

On GitHub choose **Code → Download ZIP**, extract it, and copy the selected
skill folders into the agent's documented skills directory.

## Common skill locations

| Agent | Personal | Project |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| GitHub Copilot (VS Code) | `~/.copilot/skills/` | `.github/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |

Agent support and skill discovery behavior can change. Check the current
documentation for your specific client. Other assistants may use different
directories or support skills through MCP instead of local files.

## WSL and Linux workspaces

Use Ubuntu WSL for general development, coding and local-model work; use Kali
WSL for security tooling and controlled labs when appropriate. These are
separate environments unless you deliberately connect them.

Before running commands, verify the working directory, Git root, active
container, network binding and permissions. A chat assistant does not gain
access to WSL merely because WSL is running on your computer.

For local labs, bind services to loopback when external access is unnecessary.
Keep credentials and session tokens out of screenshots, logs, commits and
shared evidence.

## Cloud and project workspaces

For a project-specific install, place skills in the agent's documented project
directory and commit them with the project only when appropriate. For example,
Claude Code uses `.claude/skills/`; Codex uses `.agents/skills/`.

Cloud home directories may be temporary. Prefer project-level installation or
the provider's documented setup hook. Confirm the current client behavior
before adding automated install commands to a development container.

## Local models and custom agents

A local model can follow skill instructions when its application supplies them.
It cannot use Agensi MCP unless the surrounding application implements a
compatible MCP client and authentication flow.

For a custom workspace such as Odysseus, use a coding agent or implement your
own adapter to handle MCP transport, authentication, tool discovery/invocation,
context passing, permissions and errors. This is a software integration, not
a skill-only installation. See [INTEGRATIONS.md](INTEGRATIONS.md).

## Optional REA integration

The `rea-amplify` Boon does not require REA software. To add REA's independent
MCP tools and workflows, follow the official
[REA repository](https://github.com/morluto/rea) and its current setup guide.
The upstream quick start currently documents:

```sh
npx rea-agents setup
```

Review proposed configuration changes before approving them. REA, Ghidra and
other analysis engines have their own requirements and permissions.

## Verify installation

Start a new agent session and ask it to identify the installed Boons or perform
a representative task. In a coding agent, confirm that it can see the intended
project before asking it to edit files or run commands.

## Notes

- Boons are instructions; they do not bundle programs, credentials or tool
  permissions.
- Security skills require ownership or written authorization for the specific
  assessment.
- If a local skill does not load, confirm that `SKILL.md` is directly inside
  the skill folder and that the agent supports that location or format.
