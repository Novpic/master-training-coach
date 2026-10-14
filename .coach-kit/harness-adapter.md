# Harness Adapter Contract

Harness-specific agent files are adapters, not alternate coach implementations.
They must preserve the behavior in `protocol.md` and may only add:

- invocation metadata and permissions;
- the harness's delegation syntax;
- concise domain-specific instructions for the selected coach;
- tool restrictions needed to enforce the protocol.

When adding a Claude, Codex, `.agent`, or other harness adapter:

1. Read `AGENTS.md` and `.coach-kit/protocol.md`.
2. Read the selected coach folder's `evidence-base.md` and `formulas.md`.
3. Reuse the same coach name, ownership boundary, intake IDs, statuses, table
   columns, safety gate, and artifact paths.
4. Pass a complete `HANDOFF PACKET` when delegating and require the standard
   result envelope on return.
5. Do not copy the kit into the harness directory or expose internal evidence
   paths in user-facing output.

OpenCode uses `.opencode/agents/` as its native agent directory. The research
agents in `.agent/` are separate repository roles and should continue following
the evidence-audit workflow rather than being treated as training coaches.

Claude Code project subagents use `.claude/agents/` and require `name` and
`description` frontmatter. Codex uses `.codex/agents/*.toml` with
`name`, `description`, and `developer_instructions`. Both directories contain
full generated prompts and therefore execute through their native separated
context mechanisms.

Portable instructions are generated under `.agents/skills/`. Run
`python3 .agents/generate-adapters.py` after changing an OpenCode prompt.
