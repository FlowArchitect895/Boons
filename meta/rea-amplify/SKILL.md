---
name: rea-amplify
description: Analyze authorized supplied artifacts or actual tool results, track coverage and uncertainty, and produce traceable handoffs for downstream skills.
license: Apache-2.0
metadata:
  domain: meta
  version: "0.4.0"
  status: experimental
user-invocable: true
---

# REA amplify

Analyze an artifact the user supplies or explicitly selects. Produce an
evidence-grounded handoff for another skill or decision—not a copy of the
artifact or claims beyond what analysis establishes.

REA software is optional. This skill is not the REA engine, does not install
analysis tools and does not grant access to the user's machine. Use only
artifacts and tool results actually available in the session.

## Workflow

1. **Identify authority, artifact and question.** Establish artifact type,
   user's authority, intended question and downstream consumer. Stop if
   permission is unclear or output would expose protected implementation,
   assets or secrets.
2. **Declare the environment.** State whether the artifact was uploaded,
   selected from an available source, or returned by a connected tool. List
   tools actually available. Do not imply access to a local path, browser,
   terminal, network, container or REA installation unless the session exposes
   it and a result confirms access.
3. **Inventory coverage.** Record relevant files/components, metadata and
   portions examined. Distinguish examined, partially examined, unavailable
   and excluded areas. Do not imply complete coverage from partial inspection.
4. **Check tools and method.** Use an existing authorized REA setup or tools
   such as Ghidra only when available and appropriate. Record the actual
   command/action, version or configuration when known, output and errors.
   Do not assume installation, connectivity, successful parsing or completeness.
5. **Plan bounded evidence collection.** Gather only what the downstream
   decision needs. Record method/tool, settings or limitations and artifact
   location for important observations. Do not access external systems,
   retrieve additional artifacts or install tools on the user's behalf.
6. **Separate evidence layers.** For each finding distinguish:
   - **Direct observation:** visible in the artifact or returned by a tool.
   - **Tool interpretation:** what a parser, decompiler or other tool reports.
   - **Analyst inference:** what observations may mean.
   - **Unknown:** what is not established.
   Attach evidence references, calibrate confidence and consider alternatives.
7. **Handle gaps and conflicts.** Note missing symbols, incomplete parsing,
   stripped metadata, ambiguous control flow, unsupported formats, tool errors
   and contradictory evidence. Use another bounded method only if available
   and authorized. Explain what a fallback establishes and what it does not.
   Absence of tool output is not proof of absence.
8. **Adversarially review the handoff.** Ask what observation would disprove the
   leading interpretation, whether the tool output was over-read, whether a
   benign explanation fits, and whether the artifact coverage supports the
   breadth of the conclusion. Keep competing interpretations when evidence
   cannot distinguish them.
9. **Abstract the useful result.** Summarize relevant structure, behavior,
   constraints, interfaces or hypotheses at the level needed downstream. Do
   not reproduce source code, secrets, personal data, assets or protected
   expression.
10. **Produce a downstream handoff.** Include:
    - Question and intended consumer
    - Artifact identity and coverage
    - Actual tools/methods used, or state that none were run
    - Key observations with evidence references
    - Tool interpretations, analyst inferences and confidence
    - Alternatives, unknowns and unresolved behavior
    - Constraints, limitations and exclusions
    - Recommended next question or safe follow-up

    The receiving skill must apply its own authorization and safety rules.
    This analysis does not prove permission for downstream activity.

## Optional open-source analysis tools

REA is a separate, optional MCP toolkit. Its upstream project documents a
setup flow for supported agents:

- [REA](https://github.com/morluto/rea) — agent-facing reverse-engineering
  workflows and MCP tools. Review its current Node.js requirements, supported
  clients and target-specific prerequisites before setup.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) — software
  reverse-engineering suite.
- [radare2](https://github.com/radareorg/radare2) — reverse-engineering
  framework and command-line analysis tools.
- [JADX](https://github.com/skylot/jadx) — Android DEX to Java decompiler.
- [Binwalk](https://github.com/ReFirmLabs/binwalk) — firmware and file
  extraction/analysis.

Do not assume every artifact needs every tool. REA can analyze some formats
without a separate native decompiler; other formats require specific providers.
Check the REA guide for the artifact type and platform. Some commercial tools
may appear in upstream compatibility lists; Boons recommends only the free,
open-source options listed here.

**On activation:** identify the artifact type and the analysis depth required.
Check which tools are already available. Explain the smallest useful optional
setup, then ask:
"Would you like me to help integrate REA or one of these free tools into your
agent/workspace?" Never install REA, Ghidra or other dependencies, modify MCP
configuration, or inspect a local target without approval. If the client has no
workspace/terminal access, request a supplied artifact or user-collected
results instead.

## Stop or narrow

Do not install tools, access external systems or obtain artifacts on the user's
behalf. If no suitable tool is available, ask for user-collected results or
provide a high-level explanation. Stop if permission is absent, analysis would
expose credentials/personal data, or findings would materially enable
unauthorized access.

## Verification

Check artifact identity and coverage; traceability to artifact locations or
actual tool results; separation of observations, tool interpretations,
inferences and unknowns; calibrated confidence; visible alternatives and
tool limitations; absence of copied implementation, secrets or unsupported
behavior; and downstream recommendations within the receiving skill's scope.
Never claim a tool ran unless this session returned its result.
