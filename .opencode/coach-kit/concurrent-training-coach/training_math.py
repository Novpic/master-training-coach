#!/usr/bin/env python3
"""Arithmetic helper for weekly schedule bookkeeping only."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from typing import Any


def _duration(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{field} must be finite and zero or greater")
    return number


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    sessions = payload.get("sessions", [])
    if not isinstance(sessions, list):
        raise ValueError("sessions must be a list")

    session_counts: defaultdict[str, int] = defaultdict(int)
    duration_minutes: defaultdict[str, float] = defaultdict(float)
    day_modalities: defaultdict[str, set[str]] = defaultdict(set)

    for index, session in enumerate(sessions):
        field = f"sessions[{index}]"
        if not isinstance(session, dict):
            raise ValueError(f"{field} must be an object")

        modality = session.get("modality")
        if not isinstance(modality, str) or modality not in {"strength", "endurance"}:
            raise ValueError(f"{field}.modality must be strength or endurance")
        session_counts[modality] += 1

        day = session.get("day")
        if day is not None:
            if not isinstance(day, str) or not day.strip():
                raise ValueError(f"{field}.day must be a non-empty string when provided")
            day_modalities[day.strip()].add(modality)

        if "duration_min" in session:
            duration_minutes[modality] += _duration(
                session["duration_min"], f"{field}.duration_min"
            )

    result: dict[str, Any] = {}
    if sessions:
        result["session_counts_by_modality"] = dict(sorted(session_counts.items()))
        result["scheduled_duration_minutes_by_modality"] = {
            modality: round(minutes, 2)
            for modality, minutes in sorted(duration_minutes.items())
        }
        result["note"] = (
            "Counts supplied sessions and durations only; this is not a training-load, "
            "fatigue, interference, or safety estimate."
        )

    if day_modalities:
        result["days_with_both_modalities"] = sorted(
            day
            for day, modalities in day_modalities.items()
            if {"strength", "endurance"}.issubset(modalities)
        )

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdin", action="store_true", help="read a JSON object from stdin")
    parser.parse_args()
    try:
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
