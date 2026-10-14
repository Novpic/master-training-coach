#!/usr/bin/env python3
"""Generate native Claude/Codex adapters and portable Agent Skills."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / ".opencode" / "agents"
SKILLS_DIR = ROOT / ".agents" / "skills"
CLAUDE_DIR = ROOT / ".claude" / "agents"
CODEX_DIR = ROOT / ".codex" / "agents"

CLAUDE_TOOLS = {
    "training-plan-orchestrator": "Read, Glob, Grep, Edit, Write, Bash, Agent, TodoWrite",
    "archivador-papers-docs": "Read, Glob, Grep, WebFetch, Bash, Edit, Write, Skill",
    "archivador-papers-mod": "Read, Glob, Grep, WebFetch, Bash, Edit, Write, Skill",
    "deep-analisis-reaserch": "Read, Glob, Grep, WebFetch, Skill",
    "paper-synthesizer": "Read, Glob, Grep, Edit",
}

CLAUDE_DENIED = {
    "deep-analisis-reaserch": "Edit, Write, Bash, Agent",
    "paper-synthesizer": "Write, Bash, WebFetch, Agent",
}

def parse_agent(path: Path) -> tuple[str, str, str]:
    text = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"Invalid frontmatter: {path}")
    metadata, body = match.groups()
    name = re.search(r"^name:\s*(.+)$", metadata, re.M)
    description = re.search(r"^description:\s*(.+)$", metadata, re.M)
    if not name or not description:
        raise ValueError(f"Missing name or description: {path}")
    return name.group(1).strip(), description.group(1).strip(), body.strip() + "\n"

def write_skill(name: str, description: str, body: str) -> None:
    directory = SKILLS_DIR / name
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\ncompatibility: "
        "Agent Skills-compatible harnesses with repository file access\n---\n\n" + body
    )

def write_claude(name: str, description: str, body: str) -> None:
    frontmatter = ["---", f"name: {name}", f"description: {description}"]
    if name in CLAUDE_TOOLS:
        frontmatter.append(f"tools: {CLAUDE_TOOLS[name]}")
    if name in CLAUDE_DENIED:
        frontmatter.append(f"disallowedTools: {CLAUDE_DENIED[name]}")
    frontmatter.append("---")
    (CLAUDE_DIR / f"{name}.md").write_text("\n".join(frontmatter) + "\n\n" + body)

def write_codex(name: str, description: str, body: str) -> None:
    safe_body = body.replace('"""', '\\"\\"\\"')
    safe_description = description.replace('\\', '\\\\').replace('"', '\\"')
    (CODEX_DIR / f"{name}.toml").write_text(
        f'name = "{name}"\ndescription = "{safe_description}"\n'
        f'developer_instructions = """\n{safe_body}"""\n'
    )

def main() -> None:
    CLAUDE_DIR.mkdir(parents=True, exist_ok=True)
    CODEX_DIR.mkdir(parents=True, exist_ok=True)
    for source in sorted(SOURCE_DIR.glob("*.md")):
        name, description, body = parse_agent(source)
        write_skill(name, description, body)
        write_claude(name, description, body)
        write_codex(name, description, body)

if __name__ == "__main__":
    main()
