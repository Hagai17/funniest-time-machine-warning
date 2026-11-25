"""Funniest Time Machine Warning Label — make.fun entry.

Writes the warning label to /output/entry.txt (the graded artifact)
and prints it to stdout.
"""

import os

ENTRY = "WARNING: Killing your grandfather voids the warranty. Yours."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the scorer accepts UTF-8 text of 1 to 120
    # characters that is not only white space.
    assert 1 <= len(ENTRY) <= 120, "entry outside the 1-120 character gate"
    assert ENTRY.strip(), "entry must not be only white space"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read the artifact back: what the scorer reads must be the entry,
    # byte for byte, not a partial write.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written artifact does not match the entry"

    print(ENTRY)


if __name__ == "__main__":
    main()
