# Formula Guide — Sports Nutrition Coach

Use these only for transparent arithmetic after the safety gate, when the user asks for quantitative tailoring and the inputs/context are appropriate. State units and assumptions. A calculation is not a diagnosis, target, or guarantee. The companion script computes only selected arithmetic and does not estimate food composition or daily energy needs.

## Protein arithmetic

- `daily protein (g) = body mass (kg) × selected protein rate (g/kg/day)`.
- A broad exercise-context range in the local summaries is 1.4–2.0 g/kg/day. This is not an automatic target for every person, diet, or health context. Use only when body-mass scaling is appropriate; otherwise give food-based guidance without a numerical target and/or refer to a sports dietitian.
- `per-serving reference amount (g) = body mass (kg) × 0.25 g/kg`. This is one optional planning reference, not a required dose or timing rule. Interpret alongside the 20–40 g range and meal quality/context in the local summaries; do not multiply it into a rigid meal schedule.

## Hydration and exercise arithmetic

- Optional pre-exercise fluid example: `5–7 mL/kg × body mass (kg)` at least 4 hours before exercise, from the local position-stand summary. This is conditional, not a universal requirement; do not apply to people with fluid restrictions or medical concerns.
- Approximate sweat rate: `(pre-exercise mass (kg) − post-exercise mass (kg) + fluid consumed (L) − urine produced (L)) ÷ duration (h)`. Approximate 1 kg mass change as 1 L fluid. This is a noisy, task/environment-specific estimate; clothing, respiratory losses, food, and measurement conditions affect it. Do not turn it into a forced drinking target.
- `BMI = mass (kg) ÷ height (m)²` is an optional height/weight ratio only. It is not body composition, a nutrition prescription, or a diagnosis.

## Do not calculate or infer

- Do not calculate BMR, TDEE, maintenance calories, calorie deficits/surpluses, or exact meal calories/macros from predictive equations or activity multipliers. No such individualized energy equation or food-composition database is supported by this agent's local evidence set.
- Do not infer body-fat percentage, fat-free mass, lean mass, hydration status, visceral fat, bone status, or nutrient adequacy from a consumer scale, waist/circumference, BMI, or appearance.
- Do not use energy-availability arithmetic or proposed cutoffs to assess an individual, diagnose REDs, establish a “safe” intake, or reassure the user. Estimation error and individual context are substantial, and the current local consensus summary rejects a universal diagnostic cutoff.
- Do not convert study-level pooled associations into individual predictions or prescriptions (including a modeled daily deficit, protein breakpoint, or weight-loss rate).
- Do not use one sweat test to prescribe a fixed daily fluid/electrolyte amount or encourage drinking beyond thirst/sweat losses.
