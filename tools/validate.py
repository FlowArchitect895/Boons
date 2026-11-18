#!/usr/bin/env python3
"""Validate the expected Boon package shape and required skill metadata."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "cybersecurity/security-methods": "security-methods",
    "cybersecurity/bug-bounty-recon": "bug-bounty-recon",
    "coding/craft-and-vibe": "craft-and-vibe",
    "creative/systems-synthesis": "systems-synthesis",
    "creative/voice-and-edit": "voice-and-edit",
    "meta/rea-amplify": "rea-amplify",
}
AUTHORIZATION_LINE = (
    "Use this only when you own the system or have written authorization for the\n"
    "specific assessment. You are responsible for confirming the authorized assets,\n"
    "actions, and time window."
)
PRIVATE_PATH = re.compile(r"(?:/home/|/Users/|~/|[A-Za-z]:\\)")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            return None
        fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    errors = []
    security_contents = []

    for relative, expected_name in EXPECTED.items():
        skill_path = ROOT / relative / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"missing {relative}/SKILL.md")
            continue

        text = skill_path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(text)
        if metadata is None:
            errors.append(f"{relative}/SKILL.md has invalid frontmatter")
            continue
        if metadata.get("name") != expected_name:
            errors.append(f"{relative}/SKILL.md name does not match its folder")
        description = metadata.get("description", "")
        if not description or len(description) > 1024:
            errors.append(f"{relative}/SKILL.md needs a description of 1-1024 characters")
        if "## Stop or narrow the work" not in text:
            errors.append(f"{relative}/SKILL.md needs a stop condition")
        if "## Verification" not in text:
            errors.append(f"{relative}/SKILL.md needs a verification section")
        if PRIVATE_PATH.search(text):
            errors.append(f"{relative}/SKILL.md contains a machine-specific path")
        if expected_name in {"security-methods", "bug-bounty-recon"}:
            security_contents.append(text)

    if len(security_contents) == 2:
        for content in security_contents:
            if AUTHORIZATION_LINE not in content:
                errors.append("both security skills must use the same authorization opening")

    testing = ROOT / "TESTING.md"
    if not testing.is_file():
        errors.append("TESTING.md is missing")
    else:
        testing_text = testing.read_text(encoding="utf-8")
        for expected_name in EXPECTED.values():
            if expected_name not in testing_text:
                errors.append(f"TESTING.md must record a status for {expected_name}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(EXPECTED)} skills and required package metadata.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
