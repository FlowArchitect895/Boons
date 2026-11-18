# Installing Boons

Each Boon is a folder with a `SKILL.md` file. Installing one means putting that
folder where your assistant looks for skills. You can install all six or only
the ones you want.

| Boon | Folder |
|---|---|
| security-methods | `cybersecurity/security-methods` |
| bug-bounty-recon | `cybersecurity/bug-bounty-recon` |
| craft-and-vibe | `coding/craft-and-vibe` |
| systems-synthesis | `creative/systems-synthesis` |
| voice-and-edit | `creative/voice-and-edit` |
| rea-amplify | `meta/rea-amplify` |

Skills load when a session starts, so start a new session after installing.

## Where assistants look for skills

| Assistant | Personal (all your projects) | Project (one repository) |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| GitHub Copilot (VS Code) | `~/.copilot/skills/` | `.github/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |

Other assistants: check their documentation for their Agent Skills location, or
use the Skills CLI below, which knows the locations of many assistants.

On Windows, `~` is your user folder, for example `C:\Users\you\.claude\skills\`.

---

## Local workspaces

### Option 1: the Skills CLI (easiest)

Needs Node.js 22.20 or later.

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons -g
```

It asks which Boons and which assistants to install for. `-g` installs for all
your projects; leave it off to install into the current project only. To pick
one Boon and one assistant directly:

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons --skill craft-and-vibe -a claude-code -g
```

`DISABLE_TELEMETRY=1` stops the CLI reporting which skills you installed.
Update later with `npx skills update`, remove with `npx skills remove`.

On Windows PowerShell, set the variable first:

```powershell
$env:DISABLE_TELEMETRY = "1"; npx skills add FlowArchitect895/boons -g
```

### Option 2: clone and copy (no Node needed)

```sh
git clone https://github.com/FlowArchitect895/Boons.git
mkdir -p ~/.claude/skills
cp -r Boons/coding/craft-and-vibe ~/.claude/skills/
```

Repeat the `cp` line for each Boon you want, and swap `~/.claude/skills` for
your assistant's folder from the table above.

### Option 3: clone and link (stays up to date)

On Linux, macOS or WSL, a symbolic link means a `git pull` in the clone updates
the installed Boon:

```sh
git clone https://github.com/FlowArchitect895/Boons.git ~/Boons
ln -s ~/Boons/coding/craft-and-vibe ~/.claude/skills/craft-and-vibe
```

On Windows, links need Developer Mode or an administrator shell; use Option 2
there.

### Option 4: download the ZIP

On the repository page choose **Code → Download ZIP**, unzip it, and copy the
Boon folders you want into your assistant's skills folder.

---

## Cloud workspaces

In a cloud workspace your home folder is usually temporary or not yours, so
the reliable route is to install Boons **into the project repository** and
commit them. Every session that opens the repository then has them.

### Into a repository (works for most cloud agents)

From the root of your project:

```sh
DISABLE_TELEMETRY=1 npx skills add FlowArchitect895/boons
```

or copy the folders yourself:

```sh
git clone --depth 1 https://github.com/FlowArchitect895/Boons.git /tmp/Boons
mkdir -p .claude/skills
cp -r /tmp/Boons/coding/craft-and-vibe .claude/skills/
git add .claude/skills && git commit -m "Add Boons skills"
```

Use `.claude/skills/` for Claude Code, `.github/skills/` for GitHub Copilot and
`.agents/skills/` for Codex. You can keep more than one.

- **Claude Code in the cloud** (claude.ai/code and other cloud sessions) loads
  the repository's `.claude/skills/`.
- **GitHub Copilot coding agent** works in your repository, so skills in
  `.github/skills/` travel with it.
- **GitHub Codespaces and dev containers** behave like a local machine, but the
  home folder resets when the container is rebuilt. Use the project folders
  above, or install at creation time with a `postCreateCommand` in
  `.devcontainer/devcontainer.json`:

  ```json
  "postCreateCommand": "DISABLE_TELEMETRY=1 npx -y skills add FlowArchitect895/boons -g -y"
  ```

### Claude apps (claude.ai web and desktop)

Where your plan supports custom skills, you can upload a Boon as a ZIP: zip one
Boon folder so `SKILL.md` sits at the top of the folder, then upload it under
the app's skills settings. Feature names and plan availability change, so check
Claude's current help pages.

---

## Check it worked

Start a new session and ask the assistant which skills it has, or ask for a
task one Boon covers, for example "build me a small CLI that counts word
frequencies" for craft-and-vibe. In Claude Code the installed Boons also appear
in the `/` menu.

## Notes

- Boons are instructions only. They include no programs and need no keys. The
  security Boons and rea-amplify are for systems and artifacts you own or are
  authorized in writing to work on.
- If a Boon does not appear, check that `SKILL.md` is directly inside the Boon's
  folder (for example `~/.claude/skills/craft-and-vibe/SKILL.md`), not one level
  deeper, and that you started a new session.
