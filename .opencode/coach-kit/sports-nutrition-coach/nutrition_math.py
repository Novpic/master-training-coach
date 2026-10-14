#!/usr/bin/env python3
"""Small arithmetic helper for sports-nutrition planning.

Reads one JSON object from stdin and emits JSON. It reports arithmetic only;
it does not estimate calorie needs, choose targets, or assess health/safety.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Any


def _number(value: Any, field: str, *, allow_zero: bool = False) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    number = float(value)
    if not math.isfinite(number) or number < 0 or (number == 0 and not allow_zero):
        qualifier = "non-negative" if allow_zero else "greater than zero"
        raise ValueError(f"{field} must be finite and {qualifier}")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    has_height_m = "height_m" in payload
    has_height_cm = "height_cm" in payload
    if has_height_m and has_height_cm:
        raise ValueError("provide only one of height_m or height_cm")
    if (has_height_m or has_height_cm) and "weight_kg" not in payload:
        raise ValueError("BMI arithmetic needs weight_kg and one height unit (height_m or height_cm)")

    if "weight_kg" in payload:
        weight = _number(payload["weight_kg"], "weight_kg")

        protein_range = payload.get("protein_g_per_kg_range")
        if protein_range is not None:
            if (
                not isinstance(protein_range, list)
                or len(protein_range) != 2
            ):
                raise ValueError("protein_g_per_kg_range must contain [low, high]")
            low = _number(protein_range[0], "protein_g_per_kg_range[0]")
            high = _number(protein_range[1], "protein_g_per_kg_range[1]")
            if low > high:
                raise ValueError("protein range low value must not exceed high value")
            result["protein_g_per_day_range"] = [round(weight * low, 1), round(weight * high, 1)]
            result["protein_note"] = "Arithmetic only; use this range only when body-mass scaling is appropriate."

        if payload.get("include_optional_pre_exercise_fluid_example") is True:
            result["pre_exercise_fluid_ml_example"] = [round(weight * 5), round(weight * 7)]
            result["pre_exercise_fluid_note"] = (
                "Conditional 5–7 mL/kg position-stand example at least 4 h before exercise; "
                "not a universal target or suitable for every medical context."
            )

        # Accept both units so every coach helper shares the same BMI input contract.
        if has_height_m or has_height_cm:
            height_m = (
                _number(payload["height_m"], "height_m")
                if has_height_m
                else _number(payload["height_cm"], "height_cm") / 100
            )
            result["bmi_kg_m2"] = round(weight / (height_m * height_m), 2)
            result["bmi_note"] = "Height/weight ratio only; not body composition, a diagnosis, or a nutrition target."

    sweat_test = payload.get("sweat_test")
    if sweat_test is not None:
        if not isinstance(sweat_test, dict):
            raise ValueError("sweat_test must be an object")
        required = ("pre_mass_kg", "post_mass_kg", "fluid_drunk_l", "urine_l", "duration_h")
        missing = [field for field in required if field not in sweat_test]
        if missing:
            raise ValueError(f"sweat_test missing required field(s): {', '.join(missing)}")
        pre = _number(sweat_test["pre_mass_kg"], "sweat_test.pre_mass_kg")
        post = _number(sweat_test["post_mass_kg"], "sweat_test.post_mass_kg")
        drank = _number(sweat_test["fluid_drunk_l"], "sweat_test.fluid_drunk_l", allow_zero=True)
        urine = _number(sweat_test["urine_l"], "sweat_test.urine_l", allow_zero=True)
        duration = _number(sweat_test["duration_h"], "sweat_test.duration_h")
        result["estimated_sweat_rate_l_per_h"] = round((pre - post + drank - urine) / duration, 2)
        result["sweat_rate_note"] = (
            "Approximate, task/environment-specific estimate with measurement error; "
            "not a fixed drinking prescription. A negative result can indicate measurement/input issues or mass gain."
        )

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdin", action="store_true", help="read a JSON object from standard input")
    parser.parse_args()

    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(calculate(payload), indent=2, sort_keys=True))
        return 0
    except (json.JSONDecodeError, ValueError) as error:
        print(f"nutrition_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
