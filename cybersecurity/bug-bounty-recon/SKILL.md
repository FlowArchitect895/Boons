---
name: bug-bounty-recon
description: Review written bounty scope, organize passive evidence, plan authorized collection and triage findings without silently crossing into target-facing activity.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.4.0"
  status: experimental
user-invocable: true
---

# Bug bounty recon

Use this only when you own the system or have written authorization for the
specific assessment. You are responsible for confirming the authorized assets,
actions, and time window.

Current written program rules are authoritative. This skill defaults to
evidence review and planning. It does not query targets, scan, exploit, or
contact program infrastructure. Tool availability is not authorization.

## Operating modes

Select and state one mode before work begins:

- **Evidence review (default):** organize user-supplied observations, artifacts
  and permitted passive research. No target-facing requests or scans.
- **Collection plan:** turn unresolved questions into a bounded plan for the
  authorized operator. This is a plan, not execution permission.
- **Tool-assisted execution:** not enabled by this skill version. Do not run
  target-facing requests, scans, exploitation or program contact. A future
  execution capability requires a separate reviewed design, explicit scope,
  per-action permissions, budgets, audit logs and stop controls.

For a local lab, confirm that the user owns or controls the target and that
requested actions are within the stated lab boundary. Do not infer that a
hostname is local or authorized from its name alone.

## Workflow

1. **Establish the program snapshot.** Record rules source, retrieval/effective
   date, exact assets, exclusions, testing limits, rate limits and disclosure
   requirements. If freshness cannot be confirmed, mark it unresolved.
2. **Classify every asset.** Use **In scope**, **Excluded** or **Unresolved**.
   Do not infer ownership, DNS relationships or inclusion from naming
   similarity. Do not plan testing of excluded or unresolved assets.
3. **Respect scope over severity.** Keep technical interest, authorization and
   bounty eligibility separate. A serious-looking issue does not override scope.
4. **Inventory evidence.** For each item record evidence ID, source, collection
   time/context, artifact location, direct observation and any transformation.
   Distinguish original observations from copied summaries and interpretations.
   Redact credentials, cookies, tokens and personal data; preserve only the
   metadata needed for analysis.
5. **Triage hypotheses.** Record affected asset, scope state and rules date,
   observed behavior, prerequisites, possible impact, severity rationale if
   supportable, confidence, alternative explanations, missing evidence and
   duplicate relationship. A lesson description, scanner label or hypothesis
   is not proof of behavior.
6. **Challenge each candidate.** Ask what evidence would falsify it, whether
   the evidence supports the claimed impact, what benign explanation fits, and
   whether a separate issue has been conflated with it. Keep unresolved
   hypotheses unresolved; do not force a severity score.
7. **Plan safe confirmation.** If active validation is necessary, describe the
   question to resolve, required authorization, minimal evidence needed and
   stop conditions for the authorized operator. This skill does not execute
   the test or supply permission to do so.
8. **Draft accurate disclosures.** Separate observation, reproduction evidence,
   interpretation, impact, severity and remediation. Do not invent affected
   users, exploitability, business impact, severity or eligibility.

## Required finding record

- Finding ID and concise hypothesis
- Asset and explicit scope state, tied to rules snapshot
- Evidence IDs and direct observations
- Interpretation and confidence
- Preconditions and plausible alternatives
- Impact and severity rationale, or why these remain undetermined
- Missing evidence and safe next question
- Duplicate relationship and disclosure status

## Optional open-source collection tools

These free, open-source projects can support an authorized operator's
collection workflow. They do not change this skill's default evidence-review
mode or enable target-facing execution:

- [OWASP Amass](https://github.com/owasp-amass/amass) — attack-surface
  mapping and asset discovery.
- [Subfinder](https://github.com/projectdiscovery/subfinder) — passive
  subdomain discovery.
- [httpx](https://github.com/projectdiscovery/httpx) — HTTP service probing.
- [Nuclei](https://github.com/projectdiscovery/nuclei) — template-based
  vulnerability checks; active requests require explicit authorization and
  program-rule review.

Treat collection output as leads, not confirmed findings. Confirm scope,
program rules, rate limits, exclusions and permitted methods before any
operator runs a tool. Do not run these tools from this skill version.

**On activation:** identify whether the task is evidence-only or needs a
collection plan. Check whether the user already has suitable tools. Ask:
"Would you like help setting up any of these free tools for your authorized
workspace?" Never install or launch them automatically. If the host is
chat-only, provide a user-run setup guide or request sanitized output. Never
send secrets, cookies or private program data to third-party services.

## Stop or narrow

Stop scope decisions when rules are missing, stale, contradictory or
insufficient. Mark the asset unresolved. Stop before any target-facing action:
this version is evidence review and collection planning only. Do not treat a
tool's presence, a user's general interest or a prior test as authorization.

## Verification

Confirm that every asset has an explicit scope state tied to a current rules
snapshot; every claim traces to evidence; observations, interpretations and
unknowns remain distinct; alternative explanations and falsifiers were
considered; severity is not inferred from uncertainty; secrets are redacted;
and no target-facing action was performed. State what was not tested.
