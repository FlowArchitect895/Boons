---
name: security-methods
description: Plan and review defensive security work with explicit authorization, traceable evidence, calibrated risk reasoning, adversarial false-positive checks and safe verification boundaries.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.3.0"
  status: experimental
user-invocable: true
---

# Security methods

Use this only when you own the system or have written authorization for the
specific assessment. You are responsible for confirming the authorized assets,
actions, and time window.

A tool being available does not make its use authorized. A skill describes a
method; it does not grant access, permissions or execution capability.

## Workflow

1. **Establish authorization and scope.** Record goal, assets, permitted
   activities, exclusions, time limits, data handling and rules of engagement.
   If authorization or scope is missing, contradictory or insufficient, stop
   before active testing. Continue only with safe education or supplied material.
2. **Declare the working mode.** State whether this is supplied-evidence
   analysis, local code/configuration review, a collection plan, or an
   explicitly authorized operator-led assessment. Identify the actual tools and
   environment available. Never imply access to a terminal, browser, network,
   container or file that is not connected to the session.
3. **Choose the least intrusive method.** Prefer code/configuration review,
   threat analysis, defensive research or interpretation of supplied
   incident/forensic material. Do not escalate from passive analysis to live
   interaction without explicit authorization for that action.
4. **Build an evidence record per finding.** Record identifier, affected
   component/asset, source artifact and location, direct observation,
   interpretation, preconditions, confidence, evidence gaps and alternatives.
   Label important claims **verified**, **inferred** or **assumed**. Tool output
   proves what the tool reported, not automatically the interpretation.
5. **Reason about risk without collapsing dimensions.** Assess separately:
   - **Exploitability:** access, conditions, skill or interaction required.
   - **Impact:** possible effect on confidentiality, integrity, availability
     or people.
   - **Likelihood:** plausibility in the stated environment.
   - **Confidence:** strength of supporting evidence.
   Explain severity rationale. Do not inflate severity to compensate for weak
   evidence or treat uncertainty as proof of no risk.
6. **Challenge the finding.** Construct at least one plausible benign
   explanation, identify evidence that would falsify the hypothesis, check
   whether the observed behavior actually supports the claimed impact, and
   distinguish missing evidence from negative evidence. Preserve disagreement
   between reviewers when it cannot be resolved.
7. **Recommend proportionate remediation.** Describe the affected condition,
   likely consequence and practical mitigation. Prefer root-cause fixes over
   cosmetic workarounds. Note compatibility, operational and residual-risk
   trade-offs. Prioritize by risk and exposure.
8. **Define safe confirmation.** For code/configuration, suggest local tests,
   regression cases or configuration checks. For live systems, provide only
   a bounded checklist for the authorized operator. Do not scan, exploit or
   contact hosts on the user's behalf.
9. **Report limits.** State what was reviewed, tools actually run, evidence
   unavailable, unresolved questions and what would change the conclusion.
   Never describe a possibility as confirmed.

## Stop or narrow

Stop if authorization or scope is absent, contradictory or does not cover the
requested action. Do not perform target-facing activity. If environment access
is unavailable, request user-collected evidence or narrow the task to analysis
of supplied material.

## Verification

Ensure every finding points to evidence; observations, interpretations and
assumptions are distinct; tool availability is not confused with permission;
alternatives and falsifiers were considered; exploitability, impact, likelihood
and confidence are not conflated; severity has rationale; remediation addresses
cause and has a safe confirmation path; and proposed tests remain authorized.
State exactly what was and was not examined or executed.
