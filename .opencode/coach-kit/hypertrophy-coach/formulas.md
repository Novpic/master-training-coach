# Permitted plan arithmetic

Use formulas only for transparent bookkeeping. They do not estimate an individual's ideal training dose, health, body composition, injury risk, energy needs, or likely muscle gain. State units and assumptions when reporting a calculated value. The adjacent `training_math.py` script implements a small subset.

## Direct weekly set count

`direct weekly sets for a named muscle = sum of that muscle's planned working sets across all sessions`

Count each working set once, against the exercise's explicitly assigned primary target. Exclude warm-up/ramp-up sets unless intentionally prescribed as work. Do not estimate secondary-muscle fractions or call the total an experimentally validated “effective set” count.

## Volume load

`volume load = external load (kg) × exact repetitions × sets`

Use only when load and exact repetitions are known and comparable. Omit load ranges, unknown machine settings, bodyweight work without measured external load, and any ambiguous per-hand/total-load convention. It is an accounting value, not a complete measure of stimulus or a way to compare different exercises.

## BMI arithmetic (only if useful or requested)

`BMI = body mass (kg) ÷ height (m)²`

Convert centimeters to meters first. Label the result as a height-to-weight ratio only; it neither measures body composition nor diagnoses health. Do not use BMI to select exercises, loads, set counts, or a hypertrophy program.

## Circumference change (optional trend arithmetic)

`absolute change = current measurement − baseline measurement`

Report the supplied unit and dates/conditions when known. Compare only like-for-like measurement sites, technique, and units. A circumference change alone cannot identify whether muscle, fat, fluid, or measurement variation caused the difference.

## Do not calculate or infer

- Do not estimate 1RM from load and repetitions, or prescribe loads from a percentage of an untested 1RM.
- Do not estimate calories, energy availability, protein needs, fat-loss targets, or supplement doses.
- Do not infer body-fat percentage, visceral-fat status, hydration, bone health, lean mass, or local muscle growth from scale labels or a formula.
- Do not predict hypertrophy from weekly sets, volume load, circumference changes, or pooled study averages.
