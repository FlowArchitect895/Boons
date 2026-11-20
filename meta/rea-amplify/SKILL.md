---
name: rea-amplify
description: Turn authorized analysis of a supplied artifact into traceable evidence-based findings that guide another skill without reproducing the artifact.
license: Apache-2.0
metadata:
  domain: meta
  version: "0.2.0"
  status: experimental
user-invocable: true
---

# REA amplify

Analyze an artifact the user supplies or explicitly selects. Produce an evidence-grounded handoff for another skill or decision—not a copy of the artifact or claims beyond what analysis establishes.

## Workflow

1. **Identify authority, artifact and question.** Establish artifact type, user's authority, intended question and downstream consumer. Stop if permission is unclear or output would reproduce protected implementation, assets or secrets.
2. **Inventory coverage.** Record relevant files/components, metadata and portions examined. Distinguish examined, partially examined, unavailable and excluded areas. Do not imply complete coverage from partial inspection.
3. **Check tools and method.** Identify tools actually available and their limits. Use an existing authorized REA setup or tools such as Ghidra only when available and appropriate. Do not assume installation, connectivity, successful parsing or complete analysis. Prefer bounded static or observational methods.
4. **Plan evidence collection.** Gather only what the downstream decision needs. Record method/tool, relevant settings or limitations and artifact location for important observations. Do not access external systems, retrieve additional artifacts or install tools on the user's behalf.
5. **Separate evidence layers.** For each finding distinguish:
   - **Direct observation:** visible in artifact or returned by a tool.
   - **Tool interpretation:** what parser, decompiler or other tool reports.
   - **Analyst inference:** what observations may mean.
   - **Unknown:** what is not established.
   Attach evidence references where possible, calibrate confidence and consider material alternative explanations.
6. **Handle gaps and conflicts.** Note missing symbols, incomplete parsing, stripped metadata, ambiguous control flow, unsupported formats, tool errors and contradictory evidence. Use another bounded method only if available and authorized. Explain what a fallback establishes and what it does not. Absence of tool output is not proof of absence.
7. **Abstract the useful result.** Summarize relevant structure, behavior, constraints, interfaces or hypotheses at the level needed downstream. Do not reproduce source code, secrets, personal data, assets or protected expression.
8. **Produce a downstream handoff.** Include:
   - Question and intended consumer
   - Artifact and coverage
   - Key observations with evidence references
   - Interpretations and confidence
   - Alternative explanations or unresolved behavior
   - Constraints, tool limitations and exclusions
   - Recommended next question or safe follow-up
   The receiving skill must apply its own authorization and safety rules. This analysis does not prove permission for downstream activity.

## Stop or narrow

Do not install tools, access external systems or obtain artifacts on the user's behalf. If no suitable tool is available, ask for user-collected results or provide a high-level explanation. Stop if permission is absent, analysis would expose credentials/personal data, or findings would materially enable unauthorized access.

## Verification

Check artifact and coverage descriptions; traceability of findings to artifact locations or actual tool results; separation of observations, tool interpretations, inferences and unknowns; calibrated confidence; visible alternatives and tool limitations; absence of copied implementation, secrets or unsupported behavior; and downstream recommendations within the receiving skill's own scope. Never claim a tool ran unless this session returned its result.
