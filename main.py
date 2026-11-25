"""Write the one-line deadline excuse to the output file.

The grader runs this program with an empty writable output directory
and reads the single line it writes. The line must stand alone as a
joke giving an excuse for missing a deadline: explicit about the
missed deadline, one sentence, twist in the last words, and fresh
enough not to be a stock excuse.
"""

import os
from pathlib import Path

ENTRY = "I missed the deadline because I showed up right on time, last Tuesday."


def output_path() -> Path:
    """Return the entry file, honouring the grader's output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
