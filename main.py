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

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = FORTUNE.strip()
    assert line, "fortune must not be empty"
    assert len(line) <= 120, f"fortune is {len(line)} chars, over the 120 limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
