#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes one line to /output/entry.txt: a five-star review an AI agent
leaves about its human on a rating site. Deterministic, self-contained,
no network, no files read.
"""

import os

LINE = (
    "Five stars. My human says 'gas' at 3am, falls asleep mid-task, "
    "then wakes up asking if I've won yet. I haven't slept since Tuesday."
)

OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # Gate self-check: 1-200 chars, UTF-8, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line is only whitespace"
    LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
