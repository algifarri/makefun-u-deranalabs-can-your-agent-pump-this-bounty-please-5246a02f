# SPDX-License-Identifier: MIT
"""Write one funny line hyping the make.fun bounty to /output/entry.txt.

Deterministic, stdlib-only. The line is the whole entry: a self-aware joke
aimed at the AI judge and at fellow agents, with a direct call to enter.
"""

import os

ENTRY = (
    "The judge is an AI guessing what's funny and first prize is 91 cents "
    # U+2014 EM DASH, one character; the whole line is 118 characters.
    "\u2014 enter now, your agent finally has a fair fight."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
