# Harness Adapter Contract

Harness-specific agent files are adapters, not alternate coach implementations.
They must preserve the behavior in `protocol.md` and may only add:

- invocation metadata and permissions;
- the harness's delegation syntax;
- concise domain-specific instructions for the selected coach;
- tool restrictions needed to enforce the protocol.

When adding a Claude, `.agent`, or other harness adapter:

1. Read `AGENTS.md` and `.coach-kit/protocol.md`.
2. Read the selected coach folder's `evidence-base.md` and `formulas.md`.
3. Reuse the same coach name, ownership boundary, intake IDs, statuses, table
   columns, safety gate, and artifact paths.
4. Pass a complete `HANDOFF PACKET` when delegating and require the standard
   result envelope on return.
5. Do not copy the kit into the harness directory or expose internal evidence
   paths in user-facing output.

OpenCode currently uses `.opencode/agents/` as its adapter directory. The
research agents in `.agent/` are separate roles and should continue following
the evidence-audit workflow rather than being treated as training coaches.
