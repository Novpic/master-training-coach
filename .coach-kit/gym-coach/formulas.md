# Formula Guide for Gym Plan Arithmetic

Use these only for transparent arithmetic and bookkeeping. None estimates an individual's likely progress, optimal dose, injury risk, or health status. Units and assumptions must be stated. The executable helper beside this file implements BMI arithmetic, assigned direct-set totals, and planned volume load.

## Weekly set count per muscle

`weekly sets for a muscle = sets per session × sessions per week`

This is the operational definition used in Schoenfeld et al. (2017; `schoenfeld2017volume`). If a plan varies exercises/session, sum its actual per-session sets across the week. The helper counts only the muscle explicitly assigned as the row's `primary_muscle`; it does not estimate secondary-muscle contribution or “effective sets.”

## Volume load

`volume load = load (kg) × repetitions × sets`

Tracked for a limited set of barbell exercises in Schoenfeld et al. (2016; `schoenfeld2016rest`). This is an accounting convention, not a complete measure of stimulus or a comparison of exercises. Use only with a single known load and exact repetition count; omit it for ranges, unknown machine settings, or bodyweight work without a measured external load.

## ACSM volume convention

`V = total repetitions × resistance`

ACSM (2009; `acsm2009progression`) labels this as volume in the position stand; it is not the only convention. State which definition is being used. Do not add this to volume-load totals as if they were independent quantities.

## Relative volume load

`relative volume load = repetitions × sets × relative load (%1RM)`

Robinson et al. (2024; `robinson2024rir`) uses this quantity when discussing conditions with different loading. Express relative load consistently as a fraction (e.g. 0.70) or percentage (e.g. 70%), and do not mix the two. This is not an e1RM equation and does not supply an individualized load target.

## BMI arithmetic (non-diagnostic)

`BMI = body mass (kg) ÷ height (m)²`

This calculation is not used to select exercises or training volume. BMI does not measure body composition and is not a diagnosis. If calculated, report only the number and limitations unless the user explicitly asks for general interpretation.

## Muscular power identity

`P = F × v` (power = force × movement velocity)

ACSM (2009; `acsm2009progression`) uses this basic relationship to describe power. It is conceptual here; this agent does not measure force/velocity or use it to prescribe a load.

## Do not calculate or infer

- Do not estimate 1RM from submaximal load/repetitions: no such formula is supported by the local source summaries, and an estimate is unnecessary for most recreational plans.
- Do not infer calorie needs, fat-loss targets, body-fat percentage, visceral-fat status, lean mass, hydration, or bone health from a formula or consumer scale output.
- Do not turn the Schoenfeld et al. volume meta-regression coefficient (0.37 percentage points per additional weekly set) into an individual's expected gain.
- Do not assign fractional secondary-muscle sets unless clearly labeled as a transparent planning convention, not a validated formula. The included helper does not do this.
