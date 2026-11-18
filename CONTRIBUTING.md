# Contributing

Contributions are welcome through pull requests. Nobody pushes to `main`
directly: every change is reviewed, and only the maintainer merges.

## How to contribute

1. **Fork** the repository and create a branch for your change.
2. Make the change: fix or improve an existing Boon, or propose a new one.
3. Run the checks (below) and include their output in your pull request.
4. Open a **pull request** against `main`, saying what you changed, why, and how
   you tested it.
5. The maintainer reviews it. Changes may be requested before it is merged, and
   a pull request can be declined if it does not fit the collection.

For a larger idea, such as a new Boon, open an issue first so the direction can
be agreed before you write it.

## What makes a good Boon

Each Boon should be useful on its own, portable across compatible assistants,
and honest about what it can and cannot establish.

- **Format.** A folder containing `SKILL.md`, in the Agent Skills format. The
  `name` uses lowercase letters, digits and hyphens, matches the folder, and is
  at most 64 characters. The `description` says what the Boon does and when to
  use it, in at most 1024 characters.
- **Structure.** A clear workflow, a "Stop or narrow the work" section, and a
  "Verification" section that names a concrete check.
- **Honesty.** Keep observed facts, inferences and assumptions distinct. Never
  present an untested claim as established.
- **Security work.** Security Boons open with the authorization line used by the
  existing two. They require written authorization and a defined scope before
  any target-facing action, and favor analysis of material the user supplies.
  Contributions that help target systems without authorization are declined.
- **Originality.** Write your own instructions. Do not copy wording, code or
  examples from other skills, books or products; if you adapt an idea from an
  openly licensed source, credit it in `PROVENANCE.md`. Material with no clear
  licence, or with share-alike terms, cannot be used.
- **No private data.** No personal paths, names, credentials, or anything not
  meant to be public.

## Checks

```sh
python3 tools/validate.py
python3 tools/provenance.py --source path/to/any/reference/you/drew/on
```

The validator checks the package shape and each Boon's required sections. The
provenance check flags any run of eight or more words shared with the reference
files you supply. It cannot detect paraphrase, so review still matters. If a
check reports a problem, fix the Boon rather than the check.

A new Boon must also be added to the lists in `tools/validate.py` (`EXPECTED`)
and `tools/provenance.py` (`SKILL_FILES`), given a row in `TESTING.md`, and
described in `PROVENANCE.md`.

## Testing

Run one representative task with the Boon in a fresh session of a supported
assistant, and add the task and the result to `TESTING.md`. A Boon stays marked
untested until that row exists.

## Licence

By contributing you agree that your contribution is licensed under the
Apache License 2.0, the same as the rest of the repository.
