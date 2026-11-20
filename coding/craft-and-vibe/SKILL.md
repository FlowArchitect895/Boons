---
name: craft-and-vibe
description: Build code by combining creative intent with disciplined engineering, explicit acceptance criteria, risk-based verification and a clean handoff.
license: Apache-2.0
metadata:
  domain: coding
  version: "0.5.0"
  status: experimental
user-invocable: true
---

# Craft and vibe

Treat the user's description as the brief. Infer what is safe to infer, ask when ambiguity changes the build, and apply engineering standards appropriate to the risk. The loop is **shape, weight, feel, build, prove, exit**.

## Workflow

1. **Read the shape.** Establish function, intended experience, smallest useful scope and output form. Identify users and runtime environment when relevant. In an existing project, inspect instructions, relevant source, tests, dependencies and version-control state before editing. Preserve unrelated and untracked work.
2. **Set the weight.** Match effort to consequence, complexity, lifespan and reversibility. A disposable helper does not need product infrastructure. Software handling accounts, private data, money, safety or security boundaries deserves stronger controls. Prefer the simplest architecture that meets the need; justify dependencies and abstractions. State assumptions and ask when an unresolved choice changes architecture, data handling, security or experience.
3. **Catch the feel.** Identify the few details that matter: interaction pace, visual hierarchy, response behavior, accessibility, tone or a key moment. Translate them into observable acceptance criteria. Keep functional requirements distinct from visual preferences; polish is not proof of correctness.
4. **Define the smallest whole.** Write a compact acceptance checklist for the core journey and constraints. Include expected inputs, outputs, errors and boundary conditions. Build a coherent working slice, follow project conventions, make reversible changes, and preserve unrelated code and data. Handle invalid input and expected failures deliberately.
5. **Build with safeguards.** Validate inputs at trust boundaries. Never hardcode credentials. Consider permissions, data exposure, injection, dependency provenance and destructive side effects where relevant. Minimize data collection. Consider confirmation, rollback or recovery for consequential state changes. Do not install, access external services, deploy, publish or push without authorization.
6. **Prove it.** Choose checks by risk: unit tests for logic, integration tests for boundaries, end-to-end tests for critical journeys, and manual inspection for visual details. Test normal use, invalid input, empty/missing data, boundaries, failure paths and relevant permissions. For fixes, include a regression check. Inspect diffs for unintended changes. Exercise visual/interactive paths, including responsiveness and keyboard access where applicable. If a check cannot run, say why. Never report an unrun test as passing.
7. **Exit clean.** Deliver the result, what changed, how to run it, exact checks and outcomes, assumptions, limitations and unverified areas. Mention operational requirements or migrations. Offer the next useful increment without gold-plating.


## Optional open-source development tools

Prefer the project's existing toolchain. These free, open-source tools can
improve common build and verification workflows:

- [Git](https://github.com/git/git) — version control and reviewable changes.
- [pytest](https://github.com/pytest-dev/pytest) — Python tests.
- [Ruff](https://github.com/astral-sh/ruff) — Python linting and formatting.
- [Playwright](https://github.com/microsoft/playwright) — browser automation
  and end-to-end testing.
- [Godot](https://github.com/godotengine/godot) — open-source game engine for
  2D/3D playable projects.

Choose tools by language, runtime and project needs; do not add all of them to
every project. Check the official repository for current installation and
platform requirements.

**On activation:** inspect the repository, installed runtimes and existing
test/build commands first. If a relevant capability is missing, ask:
"Would you like me to integrate or set up [tool] in this workspace?" Explain
the benefit and any footprint before asking. Do not install packages, modify
configuration or add dependencies without approval. In chat-only clients,
offer copyable setup steps or a handoff to a workspace-connected agent.

## Game creation and iteration

Treat a game as an interactive system, not merely a visual coding task. Use
this focused pass inside the main workflow whenever the output is a game or
playable prototype:

1. **Define the player promise.** State the fantasy or experience, the core
   player action, the short gameplay loop, the intended session length and the
   smallest playable slice. Separate essential mechanics from optional
   content. Do not begin by accumulating features.
2. **Map the game state.** Identify states and transitions such as title,
   playing, paused, upgrade choice, wave transition, victory, defeat and restart.
   Record the state variables that matter: health, resources, cooldowns, score,
   wave, inventory, progression and unlocks. Make one source of truth for each
   value; avoid duplicated state that can drift.
3. **Design mechanics as rules.** For each mechanic, specify trigger, cost,
   effect, duration, limits, interaction with other mechanics and failure or
   cancellation behavior. For resource systems, define sources, sinks, caps,
   costs and whether any loop can generate unlimited resources. For combat,
   define hit rules, damage, invulnerability, enemy roles, projectile behavior
   and readable feedback. Keep tuning values easy to inspect and change.
4. **Build the playable loop first.** Prioritize input, movement, collision,
   one meaningful challenge, feedback, success/failure and restart. Add weapons,
   upgrades, enemies, bosses, effects, progression and polish in increments.
   Each new system must connect to the existing loop rather than exist as a
   disconnected feature.
5. **Protect feel and readability.** Test whether controls respond as expected,
   threats are distinguishable, damage and cooldowns are legible, effects do
   not obscure important information, and the player understands why a state
   changed. Treat animation and visual polish as feedback, not substitutes for
   correct mechanics. Consider keyboard-only use, focus, contrast, scaling and
   reduced-motion needs where relevant.
6. **Balance through evidence.** Inspect time-to-kill, damage received, resource
   income/spending, upgrade frequency, enemy pressure, cooldown uptime and
   viable strategies. Use repeatable scenarios or seeded runs when possible.
   Do not call a game balanced from one successful playthrough; record the
   tested build, conditions and observed strategy. Avoid tuning solely to make
   the game easier or harder without reference to the intended experience.
7. **Keep inspiration transformative.** Borrow high-level functions, design
   principles or genre conventions rather than reproducing protected
   characters, art, text, music, distinctive scenes or named expression.
   Develop original mechanics, names and presentation; disclose inspirations
   when they materially shape the result.

## Game testing and release checks

Use several layers; no single test proves a game works:

- **Rule/unit tests:** damage, collision boundaries, cooldowns, costs, resource
  caps, drop rates, upgrade prerequisites, affinity/path selection, boss phases
  and win/loss conditions.
- **System/integration tests:** weapon + enemy interactions, upgrades + stats,
  abilities + boss states, resource rewards + spending, pause + timers, and
  wave transitions + progression. Test interactions, not only each feature in
  isolation.
- **State and exploit tests:** repeated pause/resume, death during an effect,
  restart after victory/defeat, upgrade selection at the last valid moment,
  insufficient resources, maxed upgrades, simultaneous hits, cooldown boundary
  frames, and any action that could duplicate rewards or bypass a cost.
- **Playable end-to-end tests:** complete the opening loop, survive or lose a
  run, reach upgrades, test each control and ability, trigger a boss or terminal
  state, and restart. Include a fresh run after a long run to detect leaked
  state.
- **Presentation and platform checks:** launch in the intended browser/runtime;
  inspect console errors, viewport scaling, input focus, keyboard and pointer
  controls, pause behavior, readability, frame-rate symptoms and audio behavior
  if audio exists. Test the actual exported deliverable, not only a development
  preview.
- **Balance and usability review:** repeat comparable runs, record outcomes,
  identify dominant or unusable strategies, and distinguish a bug from a tuning
  preference. Have a human play where possible; automated checks cannot fully
  judge fun, clarity or pacing.

For each issue, capture build/version, reproduction steps, expected behavior,
actual behavior, severity, evidence and regression coverage. Fix the rule at its
source rather than patching only the visible symptom. Re-run affected tests and
at least one adjacent gameplay path. If the runtime or browser is unavailable,
label code inspection and static checks as such; do not imply that the game was
played or visually verified.

## Stop or narrow

Pause before proceeding if ambiguity changes architecture or safety; credentials or permissions are missing; the next step installs, publishes, pushes, deploys, overwrites or deletes; an external dependency adds material cost/privacy/security implications; or scope expands beyond the smallest useful whole. Proceed only with a safe, reversible step and stated assumptions.

## Verification and handoff

Report separately:
- **Implemented:** behavior present in the code.
- **Tested:** exact commands, cases or paths actually exercised and results.
- **Not tested:** unavailable environments, integrations or checks not run.
- **Known risks:** unresolved defects, assumptions and operational dependencies.

A preview or written code is not proof. Confirm acceptance criteria, honest test reporting, regression consideration and preservation of unrelated work. If a test fails, report it and do not call the build fully passing.
