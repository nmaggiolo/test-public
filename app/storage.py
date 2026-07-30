"""Helpers for persisting the current numeric value to a file."""

import os

VALUE_FILE = os.path.join(os.path.dirname(__file__), "..", "value.txt")


def read_value() -> float:
    """Return the current value stored on disk, defaulting to 0 if the file does not exist."""
    try:
        with open(VALUE_FILE, "r") as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0


def write_value(value: float) -> None:
    """Persist *value* to disk."""
    with open(VALUE_FILE, "w") as f:
        f.write(str(value))
