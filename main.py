#!/usr/bin/env python3
"""One line from the dog, written to /output/entry.txt.

The excuse below is the whole entry: a single line, no trailing
newline, well under the 200-character cap the bounty sets. The dog
owns the cliché: he ate it to be part of it."""

import os
from pathlib import Path

EXCUSE = "I ate it because 'the dog ate my homework' was the only excuse you'd ever believe, and I wanted to be part of something."

# One line, 120 characters of plain ASCII, so the character count and
# the byte count are the same number and both sit inside the cap.
assert "\n" not in EXCUSE and 1 <= len(EXCUSE) <= 200

DESTINATION = Path("/output") / "entry.txt"


def main():
    os.umask(0o022)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(EXCUSE, encoding="utf-8")
    DESTINATION.chmod(0o644)


main()
