#!/usr/bin/env python3
"""Flag exact word-sequence reuse against explicitly supplied reference files."""

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = (
    ROOT / "cybersecurity/security-methods/SKILL.md",
    ROOT / "cybersecurity/bug-bounty-recon/SKILL.md",
    ROOT / "coding/craft-and-vibe/SKILL.md",
    ROOT / "creative/systems-synthesis/SKILL.md",
    ROOT / "creative/voice-and-edit/SKILL.md",
    ROOT / "meta/rea-amplify/SKILL.md",
)
SEQUENCE_LENGTH = 8


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:['-][a-z0-9]+)*", text.lower())


def sequences(tokens: list[str]) -> set[tuple[str, ...]]:
    return {
        tuple(tokens[index:index + SEQUENCE_LENGTH])
        for index in range(len(tokens) - SEQUENCE_LENGTH + 1)
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        action="append",
        type=Path,
        required=True,
        help="authorized reference file; repeat for each source",
    )
    args = parser.parse_args()

    sources = []
    for source in args.source:
        if not source.is_file():
            parser.error(f"reference file does not exist: {source}")
        sources.extend(sequences(words(source.read_text(encoding="utf-8"))))
    source_sequences = set(sources)

    overlaps = []
    for skill in SKILL_FILES:
        if not skill.is_file():
            print(f"ERROR: missing skill file {skill.relative_to(ROOT)}", file=sys.stderr)
            return 1
        matches = sequences(words(skill.read_text(encoding="utf-8"))) & source_sequences
        if matches:
            overlaps.append((skill.relative_to(ROOT), len(matches)))

    if overlaps:
        for skill, count in overlaps:
            print(f"OVERLAP: {skill} has {count} shared {SEQUENCE_LENGTH}-word sequences")
        return 1
    print(
        f"No exact shared sequences of {SEQUENCE_LENGTH} words or longer "
        f"found across {len(SKILL_FILES)} skills."
    )
    print("This check does not evaluate paraphrase, authorship, or source suitability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
