---
name: security-methods
description: Plan defensive security reviews with explicit authorization, traceable evidence, calibrated risk reasoning, proportionate remediation and safe verification boundaries.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.2.0"
  status: experimental
user-invocable: true
---

# Security methods

Use only when the user owns the system or has written authorization for the specific assessment. The user is responsible for confirming authorized assets, actions and time window.

## Workflow

1. **Establish authorization and scope.** Record goal, assets, permitted activities, exclusions, time limits and rules of engagement. If authorization/scope is missing, contradictory or insufficient, stop before active testing. Continue only with safe education or supplied material.
2. **Choose the least intrusive method.** Prefer code/configuration review, threat analysis, defensive vulnerability research or interpretation of supplied incident/forensic material. Do not escalate to live interaction without explicit scope and authorization.
3. **Build an evidence record per finding.** Record identifier, affected component/asset, source artifact and location, direct observation, interpretation, preconditions, confidence, evidence gaps and plausible alternatives. Label important claims **verified**, **inferred** or **assumed**. Tool output proves what the tool reported, not automatically the interpretation.
4. **Reason about risk without collapsing dimensions.** Assess separately:
   - **Exploitability:** access, conditions, skill or interaction required.
   - **Impact:** possible effect on confidentiality, integrity, availability or people.
   - **Likelihood:** plausibility in the stated environment.
   - **Confidence:** strength of supporting evidence.
   Explain severity rationale. Do not inflate severity to compensate for weak evidence or treat uncertainty as proof of no risk.
5. **Recommend proportionate remediation.** Describe affected condition, likely consequence and practical mitigation. Prefer root-cause fixes over cosmetic workarounds. Note compatibility, operational and residual-risk trade-offs. Prioritize by risk and exposure.
6. **Define safe confirmation.** For code/configuration, suggest local tests, regression cases or configuration checks. For live systems, provide only a high-level checklist for the authorized operator; do not scan, exploit or contact hosts on the user's behalf.
7. **Report limits.** State what was reviewed, unavailable evidence, unresolved questions and what would change the conclusion. Never describe a possibility as confirmed.

## Stop or narrow

Stop if authorization or scope is absent, contradictory or does not cover the requested action. Do not perform target-facing activity. Continue only with non-target-facing education or supplied-material analysis.

## Verification

Ensure every finding points to evidence; observations, interpretations and assumptions are distinct; alternatives and false-positive possibilities were considered; exploitability, impact, likelihood and confidence are not conflated; severity has rationale; remediation addresses cause and has a safe confirmation path; and proposed tests remain authorized. Narrow unsupported claims and state what remains unknown.
