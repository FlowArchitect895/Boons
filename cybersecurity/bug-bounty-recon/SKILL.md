---
name: bug-bounty-recon
description: Review written bounty scope, organize user-supplied passive reconnaissance, classify evidence and eligibility, and draft accurate disclosures without target-facing activity.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.2.0"
  status: experimental
user-invocable: true
---

# Bug bounty recon

Use only for systems the user owns or where written authorization covers the specific assessment. Current written program rules are authoritative. This skill organizes supplied information; it does not query targets, scan, exploit or contact program infrastructure.

## Workflow

1. **Establish the program snapshot.** Ask for current rules, source URL or supplied copy, retrieval/effective date, exact asset list, exclusions, testing limits and disclosure requirements. Record version/date. If freshness cannot be confirmed, mark it unresolved.
2. **Classify each asset explicitly.** Compare candidates with supplied scope. Normalize obvious textual differences, but do not infer ownership, DNS relationships or inclusion from similar names. Use:
   - **In scope:** explicitly covered by current supplied rules.
   - **Excluded:** explicitly excluded or prohibited.
   - **Unresolved:** ambiguous, absent, stale or conflicting.
   Do not propose testing excluded or unresolved assets.
3. **Respect scope over severity.** A serious-looking issue on an excluded or unresolved asset does not become eligible because it appears important. Keep technical interest, authorization and potential bounty eligibility separate.
4. **Organize supplied passive results.** Use only user-provided observations and permitted passive research. Do not query targets, scan, exploit or contact program infrastructure. Record source and collection context; distinguish original observations from copied summaries or later interpretations.
5. **Triage candidates.** Record identifier, affected asset, scope state and rules date, evidence/source, observed behavior, prerequisites, likely impact, technical severity rationale if supportable, confidence, alternative explanations, missing evidence and duplicate relationship. Merge duplicates without discarding distinct evidence or conditions.
6. **Identify evidence gaps.** State what would confirm or reject the hypothesis. If validation requires active testing, leave the gap for the authorized user under program rules; do not provide target-facing steps beyond supplied authorization.
7. **Draft careful disclosures.** Use supported facts only. Separate user-supplied reproduction notes from interpretation, impact and remediation. Do not invent exploitability, affected users, business impact, severity or eligibility. Respect reporting format and restrictions.

## Stop or narrow

If scope is missing, stale, contradictory or insufficient, stop that scope decision and ask for the applicable rule. Mark the asset unresolved meanwhile. If validation requires active testing, do not perform it; identify the evidence gap.

## Verification

Confirm every asset has an explicit scope state tied to the supplied rules snapshot; scope is not inferred from naming similarity or severity; findings trace to supplied evidence; observation, interpretation, impact and confidence are distinct; duplicates retain meaningful evidence; technical severity and eligibility are separate; disclosures contain no unsupported claims; and unresolved gaps are visible.
