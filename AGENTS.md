# Repository instructions

## Scope and structure

- This is a documentation repository, not an application: it has no manifest, build, tests, lint, CI, or configured development command.
- `docs/` contains the educational documentation; `docs/metodologia/README.md` is the source of truth for researching and publishing new topics.
- `docs/bibliografia.md` is the subject index and `docs/referencia.bib` is the normalized bibliography; keep them synchronized with citations in the documents.
- `.agent/verificador-verdad-deportiva.md` defines the independent audit, and `.agent/investigador-ejecutor-evidencia.md` defines the research and subsequent editing process.
- `.opencode/agents/` contains only agent definitions: `training-plan-orchestrator`, its seven coaches (`gym-coach`, `hypertrophy-coach`, `running-coach`, `concurrent-training-coach`, `sports-nutrition-coach`, `recovery-health-coach`, `fat-loss-coach`), and the research agents. OpenCode registers every Markdown file under `.opencode/agents/` as an agent, so coach support files live in `.opencode/coach-kit/`: the shared contract `protocol.md` plus one folder per coach with its internal evidence digest, formula guide, and arithmetic helper.

## Required workflow

- Define the question, population, intervention, comparator, outcomes, and exclusions before searching for evidence.
- Prioritize primary sources, systematic reviews, meta-analyses, consensus statements, and official organizations; confirm DOI, PMID, or another identifier using an independent source.
- Always separate a source's findings, their interpretation, and their practical application; treat ranges, examples, and heuristics as guidance, not universal protocols.
- Do not use blogs, social media, Wikipedia, search snippets, or AI-generated content as final evidence.
- Distinguish a bibliographic record, legally accessible full text, and a verified download; never add unauthorized copies.
- If a fact cannot be confirmed, write `Not verified` or leave it pending instead of inferring it.
- Every material claim must have a traceable inline citation and context for population, units, duration, and limitations.
- Do not make individualized clinical recommendations; keep the scope to healthy adults and recreational populations unless explicitly delimited otherwise.
- After editing, review links and identifiers, synchronize `docs/bibliografia.md` and `docs/referencia.bib`, check for contradictions between documents, and request a re-audit.

## Training-plan agent workflow

- `.opencode/coach-kit/protocol.md` is the shared contract for every coach: intake field IDs, handoff packet, result envelope and statuses (`COMPLETE`, `NEEDS_INPUT`, `PAUSED_SAFETY`, `BLOCKED_DEPENDENCY`, `NEEDS_REVISION`), day keys and table columns, artifact paths, and the shared safety gate. Coaches behave the same whether the user or the orchestrator invokes them.
- No coach emits citations, references, or source details to the user; the evidence digests in `.opencode/coach-kit/` are internal decision support only.
- Use `gym-coach` for general resistance-training plans across goals. It provides the broad intake, schedule, movement coverage, requested lifts, core work, and a separate plan table for each training day.
- Use `hypertrophy-coach` for muscle-growth specialization. Its final plan also uses one table per training day, followed by explanation.
- Use `running-coach` for running and run/walk plans; a current resistance plan is a scheduling constraint for it, not something to rewrite.
- Use `concurrent-training-coach` only after the relevant modality specialists have finished. It integrates the already-programmed gym/running/endurance sessions into a clear week-level day schedule; it does not prescribe or replace those specialist workouts.
- Use `sports-nutrition-coach` after the exercise schedule it supports is settled, `recovery-health-coach` after the requested plans (or first, when a safety concern appears), and `fat-loss-coach` last, once resistance, running (or an explicit "no running"), and nutrition plans exist.
- Use `training-plan-orchestrator` when routing or chaining is useful; it is also selectable with Tab as a primary agent. For a general plan, delegate to `gym-coach`. For a hypertrophy-only request, delegate directly to `hypertrophy-coach`. For a broad plan that must then be specialized for hypertrophy, invoke `gym-coach` first and wait for its result, then pass the original user context and complete first plan to `hypertrophy-coach`.
- For a coordinated concurrent-training week, the orchestrator collects shared intake, invokes the priority modality specialist first, then the other specialist with the first plan as a scheduling constraint, and invokes `concurrent-training-coach` last for the high-level weekly layout. Running/endurance performance priority means `running-coach` first; general strength priority means `gym-coach` first; explicit hypertrophy priority means `hypertrophy-coach` first unless a broad general resistance plan was also requested. If no modality has priority or an established schedule anchors it, ask which goal should anchor the calendar.
- The sequential handoff is intentional: never run the two planning agents in parallel for a chained plan. The second agent must reuse the first intake and preserve its days, session-time limit, equipment, safety constraints, requested lifts, and requested core work unless the user asks for a change or a specific conflict requires one. Do not silently add sessions or extend session time.
- If the first agent requests essential information or pauses at its safety gate, return its questions/guidance to the user and do not invoke the second agent until the user responds and a safe baseline plan is available. Do not use the second agent to bypass a safety restriction.
- If user intent is purely hypertrophy, a general `gym-coach` pass is unnecessary. If intent is unclear between a general routine and hypertrophy specialization, ask one brief clarification before delegation.
- Completed coach outputs are saved as `planes/<first-name>/<domain>/<YYYY-MM-DD>.md` (Git-ignored), and the orchestrator merges the current ones into `planes/<first-name>/master-plan/<YYYY-MM-DD>.md` without altering any prescription.

## Personal training profile persistence

- When a user supplies or corrects personal training-profile information, save the user-reported facts in a matching private profile file under `datos/` during the same task, before finishing. Profiles follow `datos/datos-<first-name>.md` (for example `datos/datos-camilo.md` and `datos/datos-susana.md`).
- Date each update and identify it as a user report. Preserve earlier dated facts when a status changes; distinguish current status, preferences, and plans from historical information. Keep unknowns explicit and do not add inferences, diagnoses, or calculated claims as user facts.
- Never mix one person's details into another person's profile. If the person's identity or profile destination is unclear, ask before saving; otherwise use a separate matching profile file. Keep entries limited to details relevant to the requested training support.

## Verification

- No automated validation commands are configured; verification consists of rereading changes against their sources, checking metadata and links, and reviewing documentary consistency.
- The current audit flags concrete recommendations without local citations, extrapolations between beginners and trained athletes, source access status, and BibTeX traceability as areas requiring special care.
- For claims about pain, injuries, pregnancy, illness, medication, supplements, safety, or low energy availability, retain warnings and require human review when appropriate.
