# Cross-Harness Agent Sources

`.agents/skills/` contains the portable instruction layer shared by supported
agent harnesses. Native execution definitions live in `.opencode/agents/`,
`.claude/agents/`, and `.codex/agents/`.

Run `python3 .agents/generate-adapters.py` after changing an OpenCode agent.
The generated Claude and Codex definitions contain the full prompt, so each
harness can execute the agent in its own native context instead of asking the
model to load another agent file at runtime.
