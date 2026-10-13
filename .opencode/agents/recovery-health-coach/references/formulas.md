# Permitted Recovery-Review Arithmetic

Use only for transparent bookkeeping when requested or useful. State units, dates, and assumptions. Calculations are not diagnoses, clinical screening, recovery scores, training prescriptions, injury-risk estimates, or predictions. The adjacent `recovery_math.py` implements the allowed arithmetic.

## BMI (only if requested or useful)

`BMI = body mass (kg) / height (m)^2`

Convert height in centimeters to meters. Report only as a height-to-weight ratio; it does not establish body composition, health, recovery, or a training/nutrition target.

## Session-RPE bookkeeping (optional)

`session load = session RPE × session duration (minutes)`

RPE should be user-reported on a 1–10 scale. A sum over supplied sessions is a personal tracking convention, not a standardized physiological dose, cross-person comparison, recovery measure, injury-risk score, or threshold. Include only complete rows with both inputs; never estimate missing values.

## Weight and circumference change (optional)

- `change = current value − baseline value`.
- Compare the same measure, units, scale/site, and reasonably similar conditions; include dates if known.
- A change alone cannot identify tissue, cause, health status, or whether a training/nutrition plan is working. Consumer composition readings are not converted or interpreted.

## Do not calculate or infer

- Energy availability, energy deficit, calorie needs, hydration/sweat status, body-fat/lean mass, sleep debt, recovery/readiness scores, injury probability, tissue capacity/load, or return-to-sport status.
- Acute:chronic workload ratio, “safe” weekly percentage increase, or any threshold from session RPE or weekly load.
- Clinical meaning, RED-S, disease, or risk from a BMI, scale label, circumference, weight change, or one symptom.
