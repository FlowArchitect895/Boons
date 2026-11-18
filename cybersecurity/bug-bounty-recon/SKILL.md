---
name: bug-bounty-recon
description: Review written bounty scope, organize supplied reconnaissance results, prioritize evidence, and draft careful disclosures.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.1.0"
  status: experimental
user-invocable: true
---

# Bug bounty recon

Use this only when you own the system or have written authorization for the
specific assessment. You are responsible for confirming the authorized assets,
actions, and time window.

## Workflow

1. Ask for the current program rules and the exact asset list, including
   exclusions and any limits on testing. Treat the program's written terms as
   authoritative.
2. Compare each proposed asset with the supplied scope. Normalize obvious
   textual differences, but do not infer ownership, DNS relationships, or
   inclusion from a similar name.
3. If an asset is excluded, ambiguous, or absent from the provided rules, mark
   it out of scope or unresolved. Do not propose testing it.
4. Organize only passive research and results the user provides. Do not query
   targets, run scans, exploit systems, or contact program infrastructure.
5. For each candidate issue, record its source, affected asset, observed
   behavior, likely impact, confidence, and any missing evidence. Merge
   duplicates without discarding distinct evidence.
6. Draft a disclosure using only supported facts. Separate reproduction notes
   supplied by the user from interpretation and recommendations.

## Stop or narrow the work

If the scope text is missing, stale, or contradictory, stop scope decisions and
ask for the applicable rule. If a candidate depends on active testing, leave a
checklist for the authorized user rather than providing target-facing steps.

## Verification

For every triage item, identify the supplied source and confirm that the asset
is explicitly covered by the provided scope. Check the report for unsupported
claims, invented impact, and details not present in the evidence.
