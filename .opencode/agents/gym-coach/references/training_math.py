#!/usr/bin/env python3
"""Small, dependency-free arithmetic helper for the gym-coach subagent.

Read one JSON object from stdin and emit JSON. This reports raw bookkeeping
only; it does not recommend training doses or interpret body-composition data.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from typing import Any


def _positive_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a positive number")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{field} must be a finite number greater than zero")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    if "weight_kg" in payload or "height_m" in payload:
        if "weight_kg" not in payload or "height_m" not in payload:
            raise ValueError("BMI arithmetic needs both weight_kg and height_m")
        weight = _positive_number(payload["weight_kg"], "weight_kg")
        height = _positive_number(payload["height_m"], "height_m")
        result["bmi_kg_m2"] = round(weight / (height * height), 2)
        result["bmi_note"] = "Raw height/weight ratio only; not a diagnosis or body-composition measure."

    sessions = payload.get("sessions", [])
    if not isinstance(sessions, list):
        raise ValueError("sessions must be a list")

    weekly_sets: defaultdict[str, float] = defaultdict(float)
    total_volume_load_kg = 0.0
    volume_load_rows = 0
    skipped_volume_load_rows = 0

    for session_index, session in enumerate(sessions, start=1):
        if not isinstance(session, dict) or not isinstance(session.get("exercises", []), list):
            raise ValueError(f"sessions[{session_index - 1}] must be an object with an exercises list")
        for exercise_index, exercise in enumerate(session.get("exercises", []), start=1):
            label = f"sessions[{session_index - 1}].exercises[{exercise_index - 1}]"
            if not isinstance(exercise, dict):
                raise ValueError(f"{label} must be an object")
            sets = _positive_number(exercise.get("sets"), f"{label}.sets")
            if not sets.is_integer():
                raise ValueError(f"{label}.sets must be a whole number")
            if "primary_muscle" in exercise:
                muscle = exercise["primary_muscle"]
                if not isinstance(muscle, str) or not muscle.strip():
                    raise ValueError(f"{label}.primary_muscle must be a non-empty string")
                weekly_sets[muscle.strip()] += sets

            load = exercise.get("load_kg")
            reps = exercise.get("reps")
            if load is None or reps is None:
                skipped_volume_load_rows += 1
                continue
            load_kg = _positive_number(load, f"{label}.load_kg")
            repetition_count = _positive_number(reps, f"{label}.reps")
            if not repetition_count.is_integer():
                raise ValueError(f"{label}.reps must be a whole number; omit volume load for rep ranges")
            total_volume_load_kg += load_kg * repetition_count * sets
            volume_load_rows += 1

    if sessions:
        result["assigned_direct_weekly_sets"] = {
            muscle: int(count) for muscle, count in sorted(weekly_sets.items())
        }
        result["weekly_set_note"] = (
            "Counts each listed work set only for its assigned primary_muscle; "
            "secondary-muscle contribution is not estimated."
        )
        if volume_load_rows:
            result["planned_volume_load_kg"] = round(total_volume_load_kg, 2)
        result["volume_load_rows_included"] = volume_load_rows
        result["volume_load_rows_skipped_missing_load_or_exact_reps"] = skipped_volume_load_rows
        result["volume_load_note"] = (
            "Arithmetic sum of load_kg × exact reps × sets for included rows only; "
            "not a complete measure of training stimulus."
        )

    return result


def main() -> int:
    try:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            "--stdin",
            action="store_true",
            help="read the JSON input object from standard input",
        )
        parser.parse_args()
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(calculate(payload), indent=2, sort_keys=True))
        return 0
    except (json.JSONDecodeError, ValueError) as error:
        print(f"training_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
