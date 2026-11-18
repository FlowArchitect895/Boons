---
name: security-methods
description: Plan and explain defensive security reviews with clear authorization, evidence, uncertainty, and remediation boundaries.
license: Apache-2.0
metadata:
  domain: cybersecurity
  version: "0.1.0"
  status: experimental
user-invocable: true
---

# Security methods

Use this only when you own the system or have written authorization for the
specific assessment. You are responsible for confirming the authorized assets,
actions, and time window.

## Workflow

1. Establish the goal, asset boundary, permitted activities, exclusions, and
   time limits. If any are unclear or conflict, stop before proposing active
   testing.
2. Select the least intrusive mode that answers the question: secure code or
   configuration review, threat analysis, defensive vulnerability research,
   or interpretation of supplied incident and forensic material.
3. Separate observations from interpretations. Label each important statement
   as verified, inferred, or assumed, and link it to the supplied evidence.
4. For a review, describe the risk and affected condition, then offer a
   proportionate mitigation and a safe way to confirm the fix.
5. For work requiring interaction with a live system, provide only a high-level
   checklist for the authorized operator. Do not scan, exploit, or contact a
   host on the user's behalf.
6. Report limitations and unresolved questions. Do not describe a possibility
   as a confirmed finding.

## Stop or narrow the work

Stop if authorization or scope is absent, contradictory, or does not cover the
requested action. Continue only with non-target-facing education or analysis
of material already supplied by the user.

## Verification

Check that each finding points to an artifact or observation, each inference
is identified as such, and any proposed test stays within the stated scope.
If the evidence does not establish a claim, revise it to describe the
uncertainty.
