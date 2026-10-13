# Supported Fat-Loss Progress Arithmetic

The adjacent script performs only arithmetic on explicit inputs. Use only when the user wants quantitative interpretation and the required values, units, and dates are known. Preserve measurement limitations. Outputs never select a goal, prescribe an intervention, assess health, or predict outcomes.

## Weight change

- Absolute change: `current average body mass − baseline average body mass` in kg.
- Relative change: `100 × (current − baseline) ÷ baseline` in percent.
- Descriptive weeklyized change: `relative change × 7 ÷ elapsed days` in percent per week.

Use comparable observations, preferably averages collected over several days and spanning a clearly specified interval. Report the calculation as a retrospective description only, not as an appropriate/required/ideal rate or a forecast. Short-term body-mass change includes water, glycogen, gut contents, and measurement variation.

## Circumference change

`current circumference − baseline circumference`, using the same unit, site, technique, and comparable conditions. A change cannot identify fat versus muscle/fluid or prove a cause. The script accepts values explicitly labeled in centimeters only.

## Optional body-composition arithmetic

If a user supplies current mass and a consumer-device body-fat percentage, the helper may calculate:

- `estimated fat mass = body mass × supplied body-fat percentage ÷ 100`
- `estimated fat-free mass = body mass − estimated fat mass`

Always label these as arithmetic derived from an unverified device estimate. They are not measured tissue masses, clinical measurements, or a basis for an energy-availability calculation or target.

## Optional BMI arithmetic

`BMI = body mass (kg) ÷ height (m)²`. The helper accepts height in meters or centimeters. Label BMI only as a height-to-weight ratio; it does not measure body composition, diagnose health, or set a target.

## Prohibited calculations and inferences

- Do not calculate BMR, TDEE, maintenance energy, a calorie deficit, goal weight, target body-fat percentage, or predicted fat-loss rate.
- Do not calculate energy availability or use a proposed threshold to diagnose, screen, reassure, or determine whether a plan is safe.
- Do not infer visceral fat, water status, bone status, nutrient adequacy, disease risk, or tissue-specific change from a scale or formula.
- Do not convert an average study outcome, training volume, step count, or exercise-calorie estimate into an individual outcome or prescription.
