---
name: craft-and-vibe
description: Build anything in code, from a quick script to a game, dashboard, simulator, visualization or tool, by fusing disciplined engineering (read first, small reversible changes, tests, verification) with creative range (the user describes shape, function and feel, and the build reads that intent instead of demanding a spec). Use when someone says "build me", "make something that", "I want a tool that feels like", hands over a one-line concept, or asks to change, fix or extend existing code.
license: Apache-2.0
metadata:
  domain: coding
  version: "0.2.0"
  status: experimental
user-invocable: true
---

# Craft and vibe

Most people describe software by what it should do and how it should feel, not
by a specification. This skill treats that description as the brief. It reads
the intent, makes the calls that can be inferred, and holds the build to real
engineering standards so creative work is also sound work.

One loop runs every build: **shape, weight, feel, build, prove, exit.**

## Workflow

1. **Read the shape.** Settle four things before writing code:
   - what it does (function);
   - what it should be like to use (experience);
   - the smallest version that delivers both (scope);
   - the output form (script, web page, component, CLI, notebook, game file).
   In an existing codebase, also read the relevant files, the project's
   instructions and its tests first, and note the current state of version
   control so unrelated work is preserved.
2. **Decide the weight.** Ask one question before any visual or structural
   choice: does this need to be solid and plain, or expressive and rich? A
   throwaway check is not a product. Match effort to the answer, and do not add
   a framework, dependency or abstraction the scope does not earn.
3. **Catch the feel.** Name the few details that make the thing feel like what
   the user asked for: the pace of an interaction, the shape of an output, the
   one moment that should land. Carry those into the build deliberately; they
   are the difference between working and good.
4. **Build the smallest whole.** Write the least code that delivers the shape
   and the feel as one working piece, not a stub. Follow the existing patterns
   of the codebase. Make changes small and reversible, and keep unrelated code
   and untracked work untouched.
5. **Prove it.** Run it. Add tests for the logic that would hurt if it broke,
   and run them. For something visual or interactive, exercise the path the
   user described and confirm it behaves. Never report a test as passing
   without having run it, and never call a build done you have not run.
6. **Exit clean.** Hand back working code with a short note: what it does, how
   to run it, what you inferred rather than were told, and what you did not
   build or verify. Offer the next increment rather than gold-plating this one.

## Stop or narrow the work

Stop and ask when the intent is genuinely ambiguous in a way that changes the
build, when a request needs a secret, an install, a push, a deployment or a
destructive change, or when the scope is growing past the smallest whole. State
an assumption and proceed only when a safe, reversible first step is clear.

## Verification

Confirm the code runs, its tests were actually run and pass, the shape and the
feel the user asked for are both present, and unrelated work was preserved.
Report exactly what was run and what was left unverified.
