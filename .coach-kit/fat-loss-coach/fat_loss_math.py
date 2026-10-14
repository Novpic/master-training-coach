#!/usr/bin/env python3
"""Arithmetic helper for fat-loss progress review; not a prescription tool.

Reads one JSON object from stdin and prints validated arithmetic as JSON. It
does not estimate energy needs, select targets, or assess health/body composition.
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
        raise ValueError(f"{field} must be finite and greater than zero")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}

    has_weight = "weight_kg" in payload
    has_height_m = "height_m" in payload
    has_height_cm = "height_cm" in payload
    if has_height_m and has_height_cm:
        raise ValueError("provide only one of height_m or height_cm")
    if payload.get("body_fat_percent") is not None and not has_weight:
        raise ValueError("body_fat_percent arithmetic requires weight_kg")

    height_m: float | None = None
    if has_height_m or has_height_cm:
        height = _positive_number(
            payload["height_m"] if has_height_m else payload["height_cm"],
            "height_m" if has_height_m else "height_cm",
        )
        height_m = height if has_height_m else height / 100

    if has_weight:
        weight = _positive_number(payload["weight_kg"], "weight_kg")
        if height_m is not None:
            result["bmi_kg_m2"] = round(weight / (height_m * height_m), 2)
            result["bmi_note"] = (
                "Height-to-weight ratio only; not a diagnosis or body-composition measure."
            )

        body_fat = payload.get("body_fat_percent")
        if body_fat is not None:
            percentage = (
                float(body_fat)
                if isinstance(body_fat, (int, float)) and not isinstance(body_fat, bool)
                else math.nan
            )
            if not math.isfinite(percentage) or not 0 <= percentage <= 100:
                raise ValueError("body_fat_percent must be finite and between 0 and 100")
            estimated_fat_mass = weight * percentage / 100
            result["estimated_fat_mass_kg"] = round(estimated_fat_mass, 2)
            result["estimated_fat_free_mass_kg"] = round(weight - estimated_fat_mass, 2)
            result["body_composition_note"] = (
                "Arithmetic from the supplied body-fat estimate; not a verified tissue measurement or clinical assessment."
            )

    trend = payload.get("weight_trend")
    if trend is not None:
        if not isinstance(trend, dict):
            raise ValueError("weight_trend must be an object")
        required = ("baseline_kg", "current_kg", "elapsed_days")
        missing = [field for field in required if field not in trend]
        if missing:
            raise ValueError(f"weight_trend missing required field(s): {', '.join(missing)}")
        baseline = _positive_number(trend["baseline_kg"], "weight_trend.baseline_kg")
        current = _positive_number(trend["current_kg"], "weight_trend.current_kg")
        elapsed_days = _positive_number(trend["elapsed_days"], "weight_trend.elapsed_days")
        absolute_change = current - baseline
        relative_change = absolute_change / baseline * 100
        result["weight_trend"] = {
            "absolute_change_kg": round(absolute_change, 2),
            "relative_change_percent": round(relative_change, 2),
            "descriptive_weeklyized_change_percent": round(relative_change * 7 / elapsed_days, 2),
            "note": (
                "Retrospective arithmetic only, not a target or prediction; short-term body mass also varies with fluid, glycogen, and gut contents."
            ),
        }

    measurements = payload.get("measurements_cm", {})
    if not isinstance(measurements, dict):
        raise ValueError("measurements_cm must be an object keyed by measurement name")
    changes: dict[str, float] = {}
    for name, values in measurements.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("measurement names must be non-empty text")
        if not isinstance(values, dict) or "baseline" not in values or "current" not in values:
            raise ValueError(f"measurements_cm.{name} needs baseline and current values")
        baseline = _positive_number(values["baseline"], f"measurements_cm.{name}.baseline")
        current = _positive_number(values["current"], f"measurements_cm.{name}.current")
        changes[name.strip()] = round(current - baseline, 2)
    if changes:
        result["circumference_change_cm"] = dict(sorted(changes.items()))
        result["circumference_note"] = (
            "Current minus baseline; compare like-for-like sites and conditions; does not identify the tissue or cause of change."
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
        print(f"fat_loss_math: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
