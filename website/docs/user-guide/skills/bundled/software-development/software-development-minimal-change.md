---
title: "Minimal Change — Use only when asked for the smallest sufficient code change"
sidebar_label: "Minimal Change"
description: "Use only when asked for the smallest sufficient code change"
---

{/* This page is auto-generated from the skill's SKILL.md by website/scripts/generate-skill-docs.py. Edit the source SKILL.md, not this page. */}

# Minimal Change

Use only when asked for the smallest sufficient code change.

## Skill metadata

| | |
|---|---|
| Source | Bundled (installed by default) |
| Path | `skills/software-development/minimal-change` |
| Version | `0.1.0` |
| Author | Joey Farina (josephfarina), Hermes Agent |
| License | MIT |
| Platforms | linux, macos, windows |
| Tags | `software-development`, `implementation`, `scope`, `simplicity`, `maintenance` |
| Related skills | [`simplify-code`](/docs/user-guide/skills/bundled/software-development/software-development-simplify-code), [`test-driven-development`](/docs/user-guide/skills/bundled/software-development/software-development-test-driven-development) |

## Reference: full SKILL.md

:::info
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
:::

# Minimal Change Skill

Use this opt-in decision skill to keep a coding change no larger than its
verified need. It guides implementation choices after the task and affected
flow are understood; it does not narrow explicit requirements or replace the
project's testing and review practices.

## When to Use

- The user explicitly asks for `minimal-change` or the smallest sufficient
  implementation.
- A coding task has several plausible implementation levels and the user wants
  a disciplined way to choose among them.

Do not activate this skill automatically for ordinary coding work. Do not use
it to reinterpret acceptance criteria, omit requested behavior, or avoid tests.

## Prerequisites

- The requested outcome and explicit acceptance criteria are known.
- Repository instructions and the relevant implementation, callers, and tests
  are available through `read_file` and `search_files`.
- No external services or platform-specific commands are required by this
  prose-only skill.

## How to Run

Invoke the skill explicitly for a coding task. First understand the request,
then trace the affected flow from its entry point through state changes,
boundaries, and observable output before choosing an implementation level.

Use `search_files` to find existing behavior and `read_file` to inspect the
implementation and tests. Use `patch` for focused edits and `terminal` for the
repository's targeted verification commands.

## Quick Reference

Apply the ladder in order and stop at the first level that fully satisfies the
request:

1. **Need** — does the requested change need code at all?
2. **Existing** — is the behavior already present or configurable in the
   codebase?
3. **Stdlib** — can the language standard library provide it clearly?
4. **Native** — can a native capability of the target platform provide it?
5. **Installed** — can an already-installed dependency provide it within its
   intended use?
6. **Smallest change** — otherwise implement the smallest complete change.

## Procedure

1. **Fix the contract.** Record the explicit acceptance criteria and identify
   public contracts, compatibility expectations, and observable behavior that
   must remain intact. Completion: every requested outcome is represented.

2. **Trace the flow.** Follow the relevant entry point through callers,
   validation, state, persistence, and output. Check sibling paths that share
   the mechanism. Completion: the precise place where behavior must change is
   supported by code evidence.

3. **Walk the ladder.** Evaluate each Quick Reference level in order. Prefer an
   existing capability only when it actually meets the contract and fits the
   repository's conventions. Completion: the chosen level is the earliest one
   that satisfies all acceptance criteria.

4. **Implement the complete minimum.** Preserve validation at trust boundaries,
   explicit data-loss handling, security controls, accessibility behavior, and
   public contracts. Do not invent abstractions, dependencies, configuration,
   scaffolding, or speculative extension points. Completion: the implementation
   covers the requested behavior without unrelated surface area.

5. **Verify proportionally.** Run existing targeted tests and add or update
   focused tests for changed, non-trivial logic. Exercise affected boundary and
   failure behavior when relevant. Completion: verification demonstrates the
   acceptance criteria and protects the changed behavior.

## Pitfalls

- **Minimal is not incomplete.** Implement every explicit requirement,
  including error states and accessibility details.
- **Existing is not automatically suitable.** Confirm semantics and supported
  use before reusing an API or dependency.
- **Fewer lines are not the objective.** Clear boundary validation and safe
  data handling may require more code.
- **No abstraction on speculation.** Introduce a seam only when the present
  request or an established repository pattern needs it.
- **No test avoidance.** A small diff can still change non-trivial behavior and
  needs targeted verification.

## Verification

- Each acceptance criterion maps to implemented behavior or a verified
  no-code outcome.
- The affected flow and sibling paths were inspected before editing.
- No new dependency, configuration, abstraction, or scaffolding exists without
  a demonstrated requirement.
- Public contracts, trust-boundary validation, data-loss handling, security,
  and accessibility remain intact.
- Targeted tests cover changed non-trivial logic and pass.
