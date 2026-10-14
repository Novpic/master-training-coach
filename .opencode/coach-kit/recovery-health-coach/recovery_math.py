#!/usr/bin/env python3
"""Arithmetic-only helper for recovery-health reviews; no health interpretation."""

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
        raise ValueError(f"{field} must be finite and greater than zero")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    if any(key in payload for key in ("weight_kg", "height_m", "height_cm")):
        if "weight_kg" not in payload:
            raise ValueError("BMI arithmetic needs weight_kg and one height unit")
        if ("height_m" in payload) == ("height_cm" in payload):
            raise ValueError("provide exactly one of height_m or height_cm")
        weight = _positive_number(payload["weight_kg"], "weight_kg")
        height_key = "height_m" if "height_m" in payload else "height_cm"
        height = _positive_number(payload[height_key], height_key)
        if height_key == "height_cm":
            height /= 100
        result["bmi_kg_m2"] = round(weight / (height * height), 2)
        result["bmi_note"] = "Height-to-weight ratio only; not a diagnosis or body-composition measure."

    sessions = payload.get("sessions", [])
    if not isinstance(sessions, list):
        raise ValueError("sessions must be a list")
    duration_total = 0.0
    rpe_load_total = 0.0
    rpe_load_count = 0
    for index, session in enumerate(sessions):
        field = f"sessions[{index}]"
        if not isinstance(session, dict):
            raise ValueError(f"{field} must be an object")
        has_duration = "duration_min" in session
        has_rpe = "session_rpe" in session
        if has_duration:
            duration_total += _positive_number(session["duration_min"], f"{field}.duration_min")
        if has_duration != has_rpe:
            raise ValueError(f"{field} session-RPE arithmetic needs both duration_min and session_rpe")
        if has_rpe:
            rpe = _positive_number(session["session_rpe"], f"{field}.session_rpe")
            if rpe > 10:
                raise ValueError(f"{field}.session_rpe must be on the 1–10 scale")
            rpe_load_total += rpe * _positive_number(session["duration_min"], f"{field}.duration_min")
            rpe_load_count += 1
    if sessions:
        result["session_count"] = len(sessions)
        result["total_session_minutes"] = round(duration_total, 2)
        result["time_note"] = "Sum of supplied session durations only; no missing sessions were estimated."
        if rpe_load_count:
            result["session_rpe_load"] = round(rpe_load_total, 2)
            result["session_rpe_load_sessions"] = rpe_load_count
            result["session_rpe_note"] = "Within-person bookkeeping only; not a recovery or injury-risk score."

    if "weight_change" in payload:
        data = payload["weight_change"]
        if not isinstance(data, dict) or "baseline_kg" not in data or "current_kg" not in data:
            raise ValueError("weight_change must contain baseline_kg and current_kg")
        baseline = _positive_number(data["baseline_kg"], "weight_change.baseline_kg")
        current = _positive_number(data["current_kg"], "weight_change.current_kg")
        result["weight_change_kg"] = round(current - baseline, 2)
        result["weight_change_note"] = "Current minus baseline; does not identify cause or tissue change."

    measurements = payload.get("measurements_cm", {})
    if not isinstance(measurements, dict):
        raise ValueError("measurements_cm must be an object keyed by measurement name")
    changes: dict[str, float] = {}
    for name, values in measurements.items():
        if not isinstance(values, dict) or "baseline" not in values or "current" not in values:
            raise ValueError(f"measurements_cm.{name} must contain baseline and current values")
        baseline = _positive_number(values["baseline"], f"measurements_cm.{name}.baseline")
        current = _positive_number(values["current"], f"measurements_cm.{name}.current")
        changes[name] = round(current - baseline, 2)
    if changes:
        result["circumference_change_cm"] = dict(sorted(changes.items()))
        result["circumference_note"] = "Current minus baseline; does not identify tissue or cause of change."

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
        print(f"recovery_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
