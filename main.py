#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun bounty entry (program/v1).

Writes one sentence, at most 200 characters, about the best meal ever had
to /output/entry.txt. Pure standard library; the output is fixed, so every
run produces byte-identical text.
"""

import os

# One sentence about the best meal ever had: a named dish, a place, a
# texture and one specific moment, told as one person's memory.
SENTENCE = (
    "The best meal I ever had was my grandmother's chicken soup, steam "
    "fogging my glasses at her kitchen table as she ladled a second bowl "
    "and told me to eat before it got cold."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the sentence.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
