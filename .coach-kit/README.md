# Shared Coach Kit

This directory is the harness-neutral source of truth for the training-plan
coaches. It is intentionally outside `.opencode/` and `.agent/` so OpenCode,
Claude, and other repository agent harnesses can reuse the same contract,
evidence digests, formulas, and arithmetic helpers.

## Entry points

- Read `protocol.md` before invoking any coach.
- Read the selected coach's `evidence-base.md` and `formulas.md`.
- Use the coach definition supplied by the current harness as the adapter. The
  adapter must preserve the protocol's intake, safety gate, handoff, artifact,
  and ownership rules.
- Run arithmetic helpers from the repository root with the command form defined
  in `protocol.md`.

## Harness adapters

- `.opencode/agents/` contains OpenCode front matter, permissions, and coach
  prompts. These files may delegate to other coaches through OpenCode's task
  mechanism, but they do not duplicate the kit.
- `.agent/` contains the research auditor and evidence implementer. If a
  harness exposes the training coaches through `.agent/`, it should reference
  this kit rather than copy it.
- `AGENTS.md` is the repository-level operating guidance shared by harnesses
  that support it.

The kit is internal decision support. Coach responses must not expose its
evidence digests, source details, or filesystem paths to users.
