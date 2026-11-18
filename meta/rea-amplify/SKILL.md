---
name: rea-amplify
description: Turn authorized analysis of a supplied artifact into evidence-based findings that can guide another skill without copying the artifact.
license: Apache-2.0
metadata:
  domain: meta
  version: "0.1.0"
  status: experimental
user-invocable: true
---

# REA amplify

## Workflow

1. Identify the artifact, the user's authority to study it, and the question
   the analysis should answer. Use an artifact the user supplies or explicitly
   selects from the current workspace.
2. Confirm that the user's authority covers the artifact and intended analysis.
   If authority is unclear or the request would copy another product's
   implementation or assets, stop and narrow it to a permitted explanation.
3. Check which analysis tools are actually available in this session and what
   they can safely do. Use an existing, authorized REA setup or a tool such as
   Ghidra only when it is available and appropriate; do not assume a tool is
   installed or connected.
4. State which downstream skill or decision the analysis should support.
   Gather only evidence needed for that purpose, using bounded static or
   observational analysis rather than target-facing activity.
5. Separate direct observations from interpretations and assumptions. Attach
   each finding to the supplied artifact or the tool result that supports it.
6. Summarize useful structure, behavior, constraints, or interfaces at an
   appropriate level of abstraction. Do not reproduce source code, assets,
   secrets, or protected expression.
7. Hand off concise findings, confidence, limitations, and follow-up questions
   to the selected skill. Never treat an analysis result as proof of
   authorization.

## Stop or narrow the work

Do not install tools, access external systems, or obtain artifacts on the
user's behalf. If no suitable analysis tool is available, ask for relevant
user-collected results or continue with a high-level explanation. Stop if
permission is absent, the requested analysis would expose credentials or
personal data, or the findings would enable unauthorized access.

## Verification

Check that each finding is traceable to supplied analysis, each inference is
labelled, and no copied implementation or unsupported behavioral claim appears
in the handoff. Do not claim a tool ran unless this session returned its result.
