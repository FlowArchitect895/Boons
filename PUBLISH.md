# Publishing checklist

The repository is prepared. Publishing is the owner's action: creating the
public GitHub repository and pushing are not done automatically.

## Pre-publish gates (all currently met)

- [x] `python3 tools/validate.py` passes (shape, names, descriptions, stop and
      verification sections, no machine paths, security authorization line).
- [x] `python3 tools/provenance.py --source <private sources>` clean: no 8-word
      overlap with the private Dragon source skills (run 2026-11-18).
- [x] All six Boons have a passing fresh-session test row in TESTING.md.
- [x] LICENSE holds the full Apache-2.0 text (verbatim).
- [x] No personal data, paths, names, or private frameworks in any file
      (deny-list grep clean).
- [x] No em dashes.

Re-run the first two before publishing:

```sh
cd ~/projects/boons
python3 tools/validate.py
python3 tools/provenance.py \
  --source ~/TagzAuthor-Sandbox/architecture/dragon-skills/claws/security-methods/original/SKILL.md \
  --source ~/TagzAuthor-Sandbox/architecture/dragon-skills/claws/bounty-hunt/skill.md \
  --source ~/TagzAuthor-Sandbox/architecture/dragon-skills/fangs/scan-triage/skill.md \
  --source ~/TagzAuthor-Sandbox/architecture/dragon-skills/claws/vibe-coder/original/SKILL.md \
  --source ~/TagzAuthor-Sandbox/architecture/dragon-skills/fangs/authenticity-filter/original/SKILL.md
```

## Publish (owner runs this, only when ready)

The folder is currently tracked inside the TagzAuthor-Sandbox home repository. To
publish it as its own public repository without disturbing that history, publish
a fresh copy:

```sh
cp -r ~/projects/boons /tmp/boons-release && cd /tmp/boons-release
rm -rf .git
git init -b main
git add -A
git commit -m "Boons: six portable agent skills (initial public release)"
gh repo create FlowArchitect895/boons --public --source . --push
```

Publishing is public and may be cached by others even if later deleted. Confirm
the repository name and account before running the last line.

## After publishing

- Update README's install example with the real `<owner>/<repository>`.
- The cross-agent install path is `npx skills add FlowArchitect895/boons`
  (vercel-labs/skills). Audited on 2026-11-18 (skills 1.9.0): integrity matches
  the registry, no install hooks, token only to GitHub, no exfiltration. It has
  telemetry on by default to skills.sh (sends CLI version, agent name, and the
  installed skill slugs, nothing private). Recommend documenting
  `DISABLE_TELEMETRY=1` alongside the install command. Re-audit on any version
  bump. Full note: TagzAuthor-Sandbox/notes/planning/skills-cli-rea-audit-2026-11-18.md
- Record the public URL and the release date in this file.
