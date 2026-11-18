# Provenance

The six skills were drafted from the owner-provided design brief and general
domain practices. The brief's named private source skills were not opened.
Their wording, code, private data, and machine-specific details were not used.
No external publications or repositories were used as source material.

- `security-methods`: uses the brief's defensive, evidence-led purpose and
  general secure-review practice. The steps were written as a bounded workflow
  for authorization checks, evidence labels, analysis, and reporting.
- `bug-bounty-recon`: uses the brief's scope-first triage purpose and general
  responsible-disclosure practice. The workflow is limited to scope review and
  organizing user-supplied research and results.
- `craft-and-vibe`: combines the brief's creative-engineering goal with general
  software-development practice. The workflow emphasizes small changes and
  verification without assuming a particular language or toolchain.
- `systems-synthesis`: uses the brief's request for original system design and
  general systems-thinking practice. It separates source functions from new
  rules and requires originality checks.
- `voice-and-edit`: uses the brief's fact-preserving editing goal and general
  editing practice. It checks claims, qualifiers, and figures against the
  supplied source.
- `rea-amplify`: uses the brief's authorized-analysis purpose and general
  evidence handling. It converts user-supplied artifact findings into a
  bounded handoff without reproducing the artifact.

## Enhancement pass, 2026-11-18 (Claude Opus)

The six drafts were reviewed and hardened. `craft-and-vibe` was completed (its
draft was truncated mid-workflow and lacked the stop and verification sections).
Consistent `license` and `metadata` frontmatter (domain, version, status) was
added to the five that lacked it. `systems-synthesis` gained a "Ways in" section
and a fuller description covering combination, cross-domain mapping, genre meta
and from-scratch design, with the originality gate kept.

No private source wording was introduced. The private Dragon source skills were
compared against all six with `tools/provenance.py` (8-word sequences): no shared
sequence was found. That check does not detect paraphrase; the derivations remain
method-level, written fresh.
