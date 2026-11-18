# Contributing

Keep each skill useful on its own, portable across compatible assistants, and
clear about what it can and cannot establish.

1. Read the applicable skill-authoring guidance and the existing draft.
2. Derive a workflow from authorized material; write new instructions rather
   than reusing source phrasing.
3. Keep facts, assumptions, and proposals distinct. Include a stop condition
   and a concrete verification step.
4. For security work, require written authorization and a defined scope before
   suggesting any target-facing action. Prefer analysis of user-supplied
   material and results.
5. Add the source and derivation method to `PROVENANCE.md`. Do not include
   private data, personal paths, or material that is not approved for release.
6. Run `python3 tools/validate.py` and the provenance checker against authorized
   reference files. Review any reported overlap instead of weakening a check.
7. Test a representative task in a fresh session. Mark the skill untested until
   that evidence exists.

Do not install, publish, or present a draft as effective without the owner's
separate approval.
