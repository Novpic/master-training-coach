#!/usr/bin/env python3
"""Small arithmetic helper for the running-coach subagent.

Read one JSON object from stdin and emit JSON. The output is bookkeeping only;
it does not recommend training doses or interpret health/injury risk.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
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

    total_minutes = 0.0
    total_distance = 0.0
    distance_unit: str | None = None
    sessions_with_distance = 0
    total_session_load = 0.0
    sessions_with_session_load = 0

    for index, session in enumerate(sessions):
        label = f"sessions[{index}]"
        if not isinstance(session, dict):
            raise ValueError(f"{label} must be an object")

        if "duration_min" in session:
            total_minutes += _positive_number(session["duration_min"], f"{label}.duration_min")

        if "distance" in session:
            distance = _positive_number(session["distance"], f"{label}.distance")
            unit = session.get("distance_unit")
            if not isinstance(unit, str) or not unit.strip():
                raise ValueError(f"{label}.distance_unit must be provided with distance")
            unit = unit.strip()
            if distance_unit is not None and unit != distance_unit:
                raise ValueError("all session distances must use the same distance_unit")
            distance_unit = unit
            total_distance += distance
            sessions_with_distance += 1

        has_rpe = "session_rpe" in session
        has_duration = "duration_min" in session
        if has_rpe != has_duration:
            raise ValueError(f"{label} session load needs both session_rpe and duration_min")
        if has_rpe:
            rpe = _positive_number(session["session_rpe"], f"{label}.session_rpe")
            if rpe > 10:
                raise ValueError(f"{label}.session_rpe must be on the 1-10 scale")
            duration = _positive_number(session["duration_min"], f"{label}.duration_min")
            total_session_load += rpe * duration
            sessions_with_session_load += 1

    if sessions:
        result["session_count"] = len(sessions)
        result["total_running_minutes"] = round(total_minutes, 2)
        result["running_time_note"] = (
            "Sum of supplied session durations; includes only sessions represented in the input."
        )
        if sessions_with_distance:
            result["total_running_distance"] = round(total_distance, 2)
            result["distance_unit"] = distance_unit
            result["distance_note"] = (
                "Sum of supplied distances in one unit; omitted sessions are not estimated."
            )
        if sessions_with_session_load:
            result["session_rpe_load"] = round(total_session_load, 2)
            result["session_rpe_load_sessions"] = sessions_with_session_load
            result["session_rpe_load_note"] = (
                "Sum of session RPE × duration_min for rows with both values; arbitrary tracking units, "
                "not a dose or injury-risk score."
            )

    measurements = payload.get("measurements_cm", {})
    if not isinstance(measurements, dict):
        raise ValueError("measurements_cm must be an object keyed by measurement name")

    changes: dict[str, float] = {}
    for name, values in measurements.items():
        if not isinstance(values, dict) or "baseline" not in values or "current" not in values:
            raise ValueError(
                f"measurements_cm.{name} must contain baseline and current values"
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdin", action="store_true", help="read one JSON object from stdin")
    parser.parse_args()
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(calculate(payload), indent=2, sort_keys=True))
        return 0
    except (json.JSONDecodeError, ValueError) as error:
        print(f"running_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
