# Repository instructions

## Scope and structure

- This is a documentation repository, not an application: it has no manifest, build, tests, lint, CI, or configured development command.
- `docs/` contains the educational documentation; `docs/metodologia/README.md` is the source of truth for researching and publishing new topics.
- `docs/bibliografia.md` is the subject index and `docs/referencia.bib` is the normalized bibliography; keep them synchronized with citations in the documents.
- `.agent/verificador-verdad-deportiva.md` defines the independent audit, and `.agent/investigador-ejecutor-evidencia.md` defines the research and subsequent editing process.

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

## Verification

- No automated validation commands are configured; verification consists of rereading changes against their sources, checking metadata and links, and reviewing documentary consistency.
- The current audit flags concrete recommendations without local citations, extrapolations between beginners and trained athletes, source access status, and BibTeX traceability as areas requiring special care.
- For claims about pain, injuries, pregnancy, illness, medication, supplements, safety, or low energy availability, retain warnings and require human review when appropriate.
