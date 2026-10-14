#!/usr/bin/env python3
"""Arithmetic helper for the hypertrophy-coach subagent.

Reads one JSON object from stdin and emits raw bookkeeping as JSON. It does not
recommend a training dose or interpret health/body-composition measurements.
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
        raise ValueError(f"{field} must be finite and greater than zero")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    has_weight = "weight_kg" in payload
    has_height_m = "height_m" in payload
    has_height_cm = "height_cm" in payload
    if has_height_m and has_height_cm:
        raise ValueError("provide only one of height_m or height_cm")
    if has_weight or has_height_m or has_height_cm:
        if not has_weight or not (has_height_m or has_height_cm):
            raise ValueError("BMI arithmetic needs weight_kg and one height unit")
        weight = _positive_number(payload["weight_kg"], "weight_kg")
        height = _positive_number(
            payload["height_m"] if has_height_m else payload["height_cm"],
            "height_m" if has_height_m else "height_cm",
        )
        if has_height_cm:
            height /= 100
        result["bmi_kg_m2"] = round(weight / (height * height), 2)
        result["bmi_note"] = (
            "Height-to-weight ratio only; not a diagnosis or body-composition measure."
        )

    sessions = payload.get("sessions", [])
    if not isinstance(sessions, list):
        raise ValueError("sessions must be a list")

    direct_sets: defaultdict[str, int] = defaultdict(int)
    volume_load_kg = 0.0
    volume_rows_included = 0
    volume_rows_skipped = 0

    for session_index, session in enumerate(sessions, start=1):
        if not isinstance(session, dict) or not isinstance(
            session.get("exercises", []), list
        ):
            raise ValueError(
                f"sessions[{session_index - 1}] must contain an exercises list"
            )
        for exercise_index, exercise in enumerate(session.get("exercises", []), start=1):
            label = f"sessions[{session_index - 1}].exercises[{exercise_index - 1}]"
            if not isinstance(exercise, dict):
                raise ValueError(f"{label} must be an object")
            sets = _positive_number(exercise.get("sets"), f"{label}.sets")
            if not sets.is_integer():
                raise ValueError(f"{label}.sets must be a whole number")

            muscle = exercise.get("primary_muscle")
            if muscle is not None:
                if not isinstance(muscle, str) or not muscle.strip():
                    raise ValueError(f"{label}.primary_muscle must be non-empty text")
                direct_sets[muscle.strip()] += int(sets)

            load = exercise.get("load_kg")
            reps = exercise.get("reps")
            if load is None or reps is None:
                volume_rows_skipped += 1
                continue
            load_kg = _positive_number(load, f"{label}.load_kg")
            repetition_count = _positive_number(reps, f"{label}.reps")
            if not repetition_count.is_integer():
                raise ValueError(
                    f"{label}.reps must be exact whole reps; omit it for rep ranges"
                )
            volume_load_kg += load_kg * int(repetition_count) * int(sets)
            volume_rows_included += 1

    if sessions:
        result["direct_weekly_sets"] = dict(sorted(direct_sets.items()))
        result["weekly_sets_note"] = (
            "Counts each listed work set only for its assigned primary muscle; "
            "secondary-muscle contribution is not estimated."
        )
        result["volume_load_rows_included"] = volume_rows_included
        result["volume_load_rows_skipped_missing_load_or_exact_reps"] = (
            volume_rows_skipped
        )
        if volume_rows_included:
            result["planned_volume_load_kg"] = round(volume_load_kg, 2)
        result["volume_load_note"] = (
            "Arithmetic load × exact reps × sets for included rows only; "
            "not a complete measure of training stimulus."
        )

    measurements = payload.get("measurements_cm", {})
    if not isinstance(measurements, dict):
        raise ValueError("measurements_cm must be an object keyed by measurement name")
    changes: dict[str, float] = {}
    for name, values in measurements.items():
        if not isinstance(values, dict):
            raise ValueError(f"measurements_cm.{name} must contain baseline and current")
        if "baseline" not in values or "current" not in values:
            raise ValueError(
                f"measurements_cm.{name} needs baseline and current values"
            )
        baseline = _positive_number(values["baseline"], f"measurements_cm.{name}.baseline")
        current = _positive_number(values["current"], f"measurements_cm.{name}.current")
        changes[name] = round(current - baseline, 2)
    if changes:
        result["circumference_change_cm"] = dict(sorted(changes.items()))
        result["circumference_note"] = (
            "Current minus baseline; does not identify the tissue or cause of change."
        )

    return result


def main() -> int:
    try:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            "--stdin", action="store_true", help="read one JSON object from stdin"
        )
        parser.parse_args()
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(calculate(payload), indent=2, sort_keys=True))
        return 0
    except (json.JSONDecodeError, ValueError) as error:
        print(f"hypertrophy_training_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
