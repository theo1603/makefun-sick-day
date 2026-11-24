#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse.

Writes one line (under 200 characters) to /output/entry.txt: a funny,
half-believable reason to call in sick, and nothing else.
"""

import os

EXCUSE = (
    "I knocked coffee over my laptop, then over myself rescuing it, "
    "so today neither of us is coming in."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
