"""Fortune Cookie Wisdom for Developers.

Writes a single original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Deterministic, stdlib-only: the line is
a constant, chosen once, and written verbatim.
"""

import os

FORTUNE = (
    "The comment you skip today is the mystery "
    "your future self will solve at 2 a.m."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = " ".join(FORTUNE.split())
    assert line, "fortune must not be empty"
    assert "\n" not in line, "fortune must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"fortune is {len(line)} chars, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
