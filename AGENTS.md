# Repository instructions

## Scope and structure

- This is a documentation repository, not an application: it has no manifest, build, tests, lint, CI, or configured development command.
- `docs/` contains the educational documentation; `docs/metodologia/README.md` is the source of truth for researching and publishing new topics.
- `docs/bibliografia.md` is the subject index and `docs/referencia.bib` is the normalized bibliography; keep them synchronized with citations in the documents.
- `.agent/verificador-verdad-deportiva.md` defines the independent audit, and `.agent/investigador-ejecutor-evidencia.md` defines the research and subsequent editing process.
- `.opencode/agents/` contains the local training-plan agents: `gym-coach`, `hypertrophy-coach`, and `training-plan-orchestrator`.

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

- Use `gym-coach` for general resistance-training plans across goals. It provides the broad intake, schedule, movement coverage, requested lifts, core work, and a separate plan table for each training day.
- Use `hypertrophy-coach` for muscle-growth specialization. Its final plan also uses one table per training day, followed by explanation; it does not emit citations or bibliographic references to the user.
- Use `training-plan-orchestrator` when routing or chaining is useful. For a general plan, delegate to `gym-coach`. For a hypertrophy-only request, delegate directly to `hypertrophy-coach`. For a broad plan that must then be specialized for hypertrophy, invoke `gym-coach` first and wait for its result, then pass the original user context and complete first plan to `hypertrophy-coach`.
- The sequential handoff is intentional: never run the two planning agents in parallel for a chained plan. The second agent must reuse the first intake and preserve its days, session-time limit, equipment, safety constraints, requested lifts, and requested core work unless the user asks for a change or a specific conflict requires one. Do not silently add sessions or extend session time.
- If the first agent requests essential information or pauses at its safety gate, return its questions/guidance to the user and do not invoke the second agent until the user responds and a safe baseline plan is available. Do not use the second agent to bypass a safety restriction.
- If user intent is purely hypertrophy, a general `gym-coach` pass is unnecessary. If intent is unclear between a general routine and hypertrophy specialization, ask one brief clarification before delegation.

## Verification

- No automated validation commands are configured; verification consists of rereading changes against their sources, checking metadata and links, and reviewing documentary consistency.
- The current audit flags concrete recommendations without local citations, extrapolations between beginners and trained athletes, source access status, and BibTeX traceability as areas requiring special care.
- For claims about pain, injuries, pregnancy, illness, medication, supplements, safety, or low energy availability, retain warnings and require human review when appropriate.
