# Permitted Running-Plan Arithmetic

Use these formulas for transparent bookkeeping only. They do not identify an individual's ideal training dose, health status, injury risk, or likely performance improvement. State units and assumptions when reporting derived values. The adjacent `running_math.py` implements the limited calculations below.

## BMI (only if useful or requested)

`BMI = body mass (kg) / height (m)^2`

Convert centimeters to meters first. Report only as a height-to-weight ratio; it is not a body-composition measure or diagnosis and must not set mileage, pace, or training frequency.

## Running exposure totals

- `weekly running time = sum of running-session minutes`
- `weekly running distance = sum of session distances` only when each distance is known and uses the same unit.

These are exposure summaries, not complete measures of internal or tissue-specific load. Do not convert between time and distance unless the user supplies valid session data; do not count walking as running distance unless it is explicitly recorded that way.

## Session-RPE load (optional tracking)

`session load = session RPE × session duration in minutes`

The source concept uses a 1–10 session RPE and reports arbitrary units (RPE × minutes). The value is a personal tracking convention, not a standardized measure, training prescription, injury-risk score, or comparison across people/sports. Calculate only when both inputs and their units are supplied.

## Circumference change (optional trend arithmetic)

`change = current measurement - baseline measurement`

Compare like-for-like sites, units, dates, and measurement conditions. The change alone cannot identify muscle, fat, fluid, or measurement variation. Circumferences do not set a running plan.

## Not operationalized

- The cumulative tissue-load sum in the local injury framework is conceptual: tissue-specific load per stride and tissue capacity have no universal field-ready measurement here. Do not calculate it.
- The acute:chronic workload ratio discussed in the local narrative review is largely derived from team-sport research; no universal safe/unsafe running cutoffs are supported. Do not calculate it or use it for programming decisions.
- No universal weekly percentage progression rule is established. Do not calculate a target mileage increase from a fixed percentage.

## Do not calculate or infer

- Race-time predictions, pace zones, VO2max, heart-rate zones, calories, energy availability, body-fat percentage, visceral fat, hydration, bone health, or running-injury probability from the supplied data.
- Individualized risk or exercise dose from BMI, body mass, BIA outputs, a single session-load value, or a pooled study estimate.
