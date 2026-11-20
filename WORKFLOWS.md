# Boons team workflow

Use this guide when several Boons contribute to one task. The skills are
independent instructions, not autonomous agents. The host assistant coordinates
their work and must have access to any files or tools the task requires.

## Default sequence

1. **Brief and boundaries** — define the user's goal, deliverable, constraints,
   audience, authorization and available environment.
2. **REA Amplify** — when artifacts are supplied, inventory coverage and extract
   evidence with source references. If no artifact or tool is available, say so;
   do not invent an analysis stage.
3. **Systems Synthesis** — model relevant components, dependencies, feedback,
   assumptions and failure cases. Separate observations from interpretations
   and proposed design.
4. **Domain skill** — use the relevant specialist, such as Security Methods or
   Bug Bounty Recon, to apply its own scope and evidence rules.
5. **Craft and Vibe** — implement only when code or a working artifact is
   requested. Inspect the existing project, set acceptance criteria, preserve
   unrelated work and test the actual user journey.
6. **Voice and Edit** — revise the user-facing writing and documentation to the
   requested intensity. Preserve facts, qualifications, authorial expression
   and the distinction between verified results and proposals.
7. **Cross-review** — ask each relevant skill to challenge the others' strongest
   assumptions, evidence gaps, failure modes and unsupported claims. Resolve
   contradictions or record them as unresolved.
8. **Handoff** — report what changed, what was actually tested, what was not
   tested, risks and the next decision.

## Rules for collaboration

- Do not invoke every skill mechanically. Select only those that add a distinct
  function to the task.
- Do not let one skill's conclusion become another skill's evidence. Preserve
  source references and evidence IDs through handoffs.
- The specialist skill retains its own safety and authorization rules.
- A tool call is not proof of the interpretation drawn from its output.
- Do not claim skills ran as separate agents unless the host actually launched
  separate agents. A coordinated single assistant can apply their workflows,
  but that is not multi-agent execution.
- Record disagreement rather than forcing false consensus.
- A proposed architecture, written plan or generated preview is not proof of a
  working implementation.

## Completion checklist

- [ ] User goal and output format are clear.
- [ ] Authorization and tool/environment boundaries are explicit where relevant.
- [ ] Evidence, inference, assumption and proposal are distinguishable.
- [ ] Alternatives and likely failure cases have been challenged.
- [ ] Changes are limited to the requested scope.
- [ ] Tests are listed with exact results; unrun checks are marked not tested.
- [ ] Writing preserves facts, meaning, certainty and intended voice.
- [ ] Remaining risks and next decision are visible.
