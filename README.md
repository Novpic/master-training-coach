# Evidence-Based Training Plan

An AI-assisted training workspace for turning scientific evidence into a
coherent, practical plan for strength, hypertrophy, running, nutrition, and
recovery.

## Why This Exists

Training information is often fragmented. A coach may be useful for writing a
routine, while the relevant research is spread across papers, reviews, position
statements, and different websites. Finding a good answer can require searching
trainer by trainer, topic by topic, or paper by paper.

This repository was created to make that process more useful and connected. The
AI agents are designed to help a person:

- Turn a goal, schedule, experience, equipment, and constraints into a practical
  training plan.
- Connect strength training with hypertrophy, running, nutrition, and recovery
  instead of treating each topic as an isolated program.
- Use research as decision support rather than copying a single study into a
  universal rule.
- Keep a dated personal profile so the agent does not ask the same questions in
  every conversation.
- Review symptoms, fatigue, recovery, and scheduling conflicts before adding
  more training.
- Produce local, dated plan files that can be reviewed and updated over time.

The goal is not to replace a qualified coach, physician, dietitian, or other
professional. The goal is to reduce the distance between the evidence and a
well-organized training decision.

## What This Repository Can Do

Given a person's profile and request, the agents can help create or review:

| Area | Possible output |
| --- | --- |
| Strength | Day-by-day resistance plan with exercises, sets, repetitions, rest, effort, core work, and progression. |
| Hypertrophy | Muscle-growth specialization, volume distribution, priority decisions, and plan refinements. |
| Running | Running or run/walk schedule that respects the existing strength plan. |
| Concurrent training | A weekly calendar that places existing strength and running sessions without rewriting them. |
| Nutrition | Nutrition strategy, optional meal plans, shopping list, and practical or budget substitutions. |
| Recovery and safety | Review of sleep, fatigue, pain, symptoms, training stress, and recovery constraints. |
| Fat loss | Implementation and monitoring after the relevant training, nutrition, and recovery plans exist. |
| Research | Traceable evidence reviews with source metadata, limitations, access status, and practical interpretation. |

The system can also identify missing information, ask only essential questions,
pause when a safety concern requires human review, and preserve unknowns instead
of inventing values.

## Quick Start

You can use the repository through an AI coding assistant that supports the
project agents. The simplest workflow is:

1. Identify the person. Use an existing profile or say that this is a new person.
2. Ask the orchestrator for a complete plan, or call one specialist directly.
3. Answer the essential questions it asks.
4. Review the resulting plan and any safety or recovery notes.
5. Ask for updates when the schedule, goal, symptoms, equipment, or performance
   changes.

### Complete Plan

Use the orchestrator when you want the agents to collect the shared intake and
run the necessary specialists in the correct order:

```text
@training-plan-orchestrator
Use the profile of Camilo and prepare a complete plan for strength, running,
nutrition, and recovery. Ask only for essential missing information.
```

You can replace `Camilo` with an existing profile name or explicitly request a
new profile. The orchestrator decides which specialists are needed and saves
the completed artifacts under `planes/<name>/`.

### One Area Only

Use a specialist when the request is limited to one domain:

```text
@gym-coach Use Camilo's profile to create or review his general strength plan.
@hypertrophy-coach Use Camilo's current plan and specialize it for hypertrophy.
@running-coach Design running sessions around Camilo's strength routine.
@sports-nutrition-coach Design a nutrition strategy compatible with Camilo's schedule.
@recovery-health-coach Review safety, symptoms, and recovery for Camilo's plan.
@concurrent-training-coach Integrate Camilo's completed strength and running plans into one week.
@fat-loss-coach Implement fat-loss tracking after the previous plans are complete.
```

### Update a Profile

Tell the agent who the information belongs to and what changed:

```text
Update Camilo's profile: I now run three days per week and have no pain while running.
Preserve the history, add today's date, and mark anything unconfirmed as pending.
```

The agent should save the new user-reported fact in the person's profile during
the same task. It should not silently delete an older report when a status
changes.

## The Agents

The recommended entry point is `training-plan-orchestrator`, selected with Tab
or invoked with `@training-plan-orchestrator`. It reads the profile, asks for
missing essentials, routes the request, and combines completed outputs.

| Agent | Owns |
| --- | --- |
| `@training-plan-orchestrator` | Shared intake, routing, dependency order, and the master plan. |
| `@gym-coach` | General resistance training: split, exercises, sets, repetitions, rest, effort, core, and progression. |
| `@hypertrophy-coach` | Muscle-growth programming or specialization of an existing resistance plan. |
| `@running-coach` | Running and run/walk programming around an existing strength schedule. |
| `@concurrent-training-coach` | Week-level placement of already-written strength and endurance sessions. It does not rewrite them. |
| `@sports-nutrition-coach` | Nutrition strategy, meal plans, shopping lists, and budget substitutions. It does not rewrite workouts. |
| `@recovery-health-coach` | Recovery review, symptom review, and safety boundaries. It may run first when a safety concern appears. |
| `@fat-loss-coach` | Fat-loss implementation and monitoring after the upstream plans are complete. |

Dependencies run sequentially. For example, a hypertrophy refinement may require
`gym-coach` first, concurrent scheduling requires the relevant modality plans,
and `fat-loss-coach` runs last. A safety pause stops the chain rather than being
worked around by another agent.

## What Is Stored

The repository separates public educational material from private personal work:

```text
.
├── README.md                 # User guide and repository map
├── AGENTS.md                 # Operating rules for agents and contributors
├── docs/                     # Versioned educational documentation
│   ├── README.md             # Documentation index and scope
│   ├── metodologia/          # Research, writing, and audit workflow
│   ├── bibliografia.md       # Thematic reference index
│   ├── referencia.bib        # Normalized bibliography
│   └── *.md                  # Published educational topics
├── .agent/                   # Research roles and audit criteria
├── .agents/                  # Portable instructions and shared skills
├── .coach-kit/               # Shared coach contract and internal support
├── .opencode/                # OpenCode agent and skill adapters
├── .claude/                  # Claude Code subagent adapters
├── .codex/                   # Codex subagent adapters
├── datos/                    # Private personal profiles, ignored by Git
├── planes/                   # Private generated plans, ignored by Git
└── docs/fotos/               # Private photos, ignored by Git
```

### Personal Profiles

`datos/datos-<name>.md` is the canonical private profile. It can contain:

- Current goals, schedule, preferences, and available equipment.
- Training background and reported capacities.
- Health, pain, mobility, and recovery information relevant to safe planning.
- Optional measurements and consumer-device readings, clearly labeled with their
  date and source.
- Historical reports that should not be confused with current status.
- A `Pendientes de confirmar` or pending-information section.

The profile is read before questions are asked. Same-name JSON files are secondary
formats and may be outdated; agents must not silently merge them into the Markdown
profile. Profiles are private and excluded from Git.

### Plan Artifacts

Completed outputs are saved locally using this structure:

```text
planes/<name>/<domain>/<YYYY-MM-DD>.md
planes/<name>/master-plan/<YYYY-MM-DD>.md
```

The shared coach contract in `.coach-kit/protocol.md` defines the handoff format,
fixed table columns, dependencies, safety gate, and result statuses:

- `COMPLETE`
- `NEEDS_INPUT`
- `PAUSED_SAFETY`
- `BLOCKED_DEPENDENCY`
- `NEEDS_REVISION`

## Evidence And Research

The repository is also a research workspace. When adding or reviewing educational
content, the process should:

1. Define the question, population, intervention or exposure, comparator,
   outcomes, duration, and exclusions.
2. Prioritize systematic reviews, meta-analyses, consensus statements, guidelines,
   and relevant primary studies.
3. Confirm DOI, PMID, publisher, or another identifier independently.
4. Separate what the source found from its interpretation and practical use.
5. State the population, units, duration, limitations, and access status.
6. Keep `docs/bibliografia.md` and `docs/referencia.bib` synchronized.
7. Request a re-audit when recommendations, figures, safety, or the scope of a
   conclusion changes.

Use `docs/metodologia/README.md` and
`docs/metodologia/plantilla-investigacion.md` for the detailed workflow.

The coaching agents use internal evidence support from `.coach-kit/`. Their
user-facing outputs do not include citations or a bibliography. Research requests
should use the repository's research workflow when source details are needed.

## Privacy And Git

Personal profiles, plans, photos, measurements, and other private data must remain
local. Before committing, verify that private paths are ignored:

```bash
git status --short --ignored
git check-ignore -v planes/ datos/ docs/fotos/
```

To share a template, anonymize names, measurements, photographs, identifying dates,
and health information. Put only the general template or educational material in
`docs/` or another intentionally public location.

## Scope And Safety

This project is intended for general education and planning for healthy adults and
recreational populations. It does not diagnose, treat, rehabilitate, or replace a
qualified professional.

Mention pain, injury, illness, pregnancy, medication, disordered-eating concerns,
or other safety-relevant information directly in the request. The recovery and
safety workflow may pause the plan and recommend appropriate human review.

The agents should not infer health, goals, capacity, or nutritional needs from
appearance, sex, gender, BMI, a consumer-scale label, or one isolated performance
value. Unknown loads, paces, calories, and targets should be calibrated rather than
invented.

Unconfirmed research claims must be marked `Not verified`. A bibliographic record
must not be confused with access to the full paper, and a paper must not be turned
into a universal prescription without considering its population and limitations.

## Repository Status

This is a documentation and agent-workflow repository, not a packaged application.
It currently has no automated build, test suite, linter, or CI command. Verification
is performed by reviewing the changed documents, checking identifiers and links,
and confirming that private paths remain ignored.
