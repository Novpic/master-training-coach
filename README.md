# Evidence-Based Training Plan

Documentation repository for researching and organizing knowledge about strength,
running, hypertrophy, sports nutrition, and recovery.

## Purpose

The repository separates general evidence from personal plans. Public
documentation serves as an educational foundation and must preserve source
traceability, applicability limits, and access status. Individualized plans,
photographs, measurements, and personal data remain outside Git.

## Structure

```text
.
├── README.md                 # General map and workflow rules
├── AGENTS.md                 # Repository operating instructions
├── docs/                     # Versioned educational documentation
│   ├── README.md             # Collection index and scope
│   ├── metodologia/          # Research, writing, and audit workflow
│   ├── bibliografia.md       # Thematic reference index
│   ├── referencia.bib        # Normalized bibliography
│   └── *.md                  # Published educational topics
├── .agent/                   # Research roles and criteria
├── .agents/                  # Portable instructions and adapter generator
│   └── skills/               # Agent Skills shared across harnesses
├── .coach-kit/               # Coach contract and support, reusable by any harness
├── .opencode/                # Local agent and skill adapters
│   └── agents/               # Agent definitions only: orchestrator, 7 coaches, research
├── .claude/                  # Claude Code subagent adapters
│   └── agents/               # Project subagent definitions
├── .codex/                   # Codex subagent adapters
│   └── agents/               # Project TOML definitions
├── datos/                    # Private datos-<name>.md profiles, ignored by Git
├── planes/                   # Generated plans, private, ignored by Git
└── docs/fotos/               # Private, ignored by Git
```

The `planes/`, `datos/`, and `docs/fotos/` directories are excluded from Git
because they contain plans, profiles, photographs, and other private data.

## How To Work

1. Before researching, define the question, population, intervention or exposure,
   comparator, outcomes, duration, and exclusions.
2. Read `AGENTS.md`, the applicable methodology, and the most recent audit.
3. Use `docs/metodologia/plantilla-investigacion.md` for new research.
4. Prioritize systematic reviews, meta-analyses, consensus statements, guidelines,
   and relevant primary studies. Verify identifiers through an independent source.
5. Always separate source findings, interpretation, and practical application.
6. Add citations next to material claims and synchronize `docs/bibliografia.md`
   with `docs/referencia.bib`.
7. Review links, identifiers, contradictions, legal access, and extrapolations
   before publishing changes.
8. Request a re-audit when a change affects recommendations, figures, safety, or
   the scope of a conclusion.

## Training Plan Agents

The recommended approach is to select `training-plan-orchestrator` with Tab as the
primary agent or invoke it with `@training-plan-orchestrator`. It asks only once
for information missing from the profile, runs coaches in dependency order, and
combines their results into a master plan.

| Agent | Purpose |
| --- | --- |
| `@gym-coach` | General strength plan: one table per day, main exercises, core work, and progression. |
| `@hypertrophy-coach` | New hypertrophy plan or refinement of a `gym-coach` plan. |
| `@running-coach` | Running or run/walk plan around the strength schedule. |
| `@concurrent-training-coach` | Places completed sessions into the week without changing prescriptions. |
| `@sports-nutrition-coach` | Nutrition strategy, daily menus, shopping list, and budget substitutions. |
| `@recovery-health-coach` | Recovery and safety review; also runs first when symptoms are present. |
| `@fat-loss-coach` | Fat-loss implementation using completed plans; always runs last. |

All agents follow the shared contract in `.coach-kit/protocol.md`:

- They read `datos/datos-<name>.md` before asking questions and save new user-
  reported facts there with a date.
- They respond with a header, one table per day with fixed columns, and a final
  `Handoff` block using one of five statuses: `COMPLETE`, `NEEDS_INPUT`,
  `PAUSED_SAFETY`, `BLOCKED_DEPENDENCY`, or `NEEDS_REVISION`.
- They save each result in `planes/<name>/<domain>/<YYYY-MM-DD>.md`; the
  orchestrator combines them into `planes/<name>/master-plan/<YYYY-MM-DD>.md`.
- They do not include citations or references in their responses; evidence in
  `.coach-kit/` is for internal use only.

Dependencies run sequentially, for example `gym-coach` before
`hypertrophy-coach`, with `fat-loss-coach` always last. A safety pause stops the
entire chain. `opencode.json` sets `experimental.subagent_depth: 2` so the
orchestrator can delegate when invoked with `@`; restart OpenCode after modifying
agents or configuration.

## Personal Profiles

The `datos/datos-<name>.md` file is the canonical source for the private profile.
It is read before asking questions and must distinguish current status, history,
preferences, and pending information. Each new or corrected fact is added with a
date and marked as a user report; previous records are not silently deleted. JSON
files with the same name are secondary formats and may be outdated.

To update a profile from the conversation:

```text
Update Camilo's profile: [new fact or correction].
Preserve the history, add today's date, and mark anything unconfirmed as pending.
```

To request a complete plan:

```text
@training-plan-orchestrator
Use Camilo's profile and prepare a complete strength, running, nutrition, and recovery plan.
Ask only for essential missing information and save the results in plans/camilo/.
```

To request a specific domain, use the responsible agent:

```text
@gym-coach Use Camilo's profile to create or review his general strength plan.
@hypertrophy-coach Use Camilo's current plan and specialize it for hypertrophy.
@running-coach Design running sessions around Camilo's strength routine.
@sports-nutrition-coach Design a nutrition strategy compatible with Camilo's schedule.
@recovery-health-coach Review safety, symptoms, and recovery for Camilo's plan.
@concurrent-training-coach Integrate Camilo's completed strength and running plans into one week.
@fat-loss-coach Implement fat-loss tracking after the previous plans are complete.
```

The agent must identify the person before saving data. If the identity is ambiguous,
ask whether this is for Camilo, Susana, a new person, or a request that should not
save anything. To verify that private files remain ignored by Git:

```bash
git status --short --ignored
git check-ignore -v datos/datos-camilo.md datos/fotos/ planes/
```

## Using Personal Plans

Individual plans may be kept locally under `planes/`, but must not be uploaded to
the repository or included in commits. Personal profiles under `datos/` are also
excluded. To share a template, anonymize names, measurements, photographs,
identifying dates, and any health data; place only the general template in `docs/`
or `datos/`.

Before each commit, check the exclusions:

```bash
git status --short --ignored
git check-ignore -v planes/ datos/ docs/fotos/
```

## Evidence Status

The documentation is educational and does not replace medical evaluation. It does
not provide individualized clinical recommendations. Unconfirmed claims must be
marked as `Not verified`, and access to a bibliographic record must not be confused
with access to the full text.
