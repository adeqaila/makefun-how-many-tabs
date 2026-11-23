#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — slot 1.

Writes one number (digits only) to /output/entry.txt: an honest count
of open browser tabs. Deterministic, no network, no arguments.
"""

import os

ENTRY = "2"


def build_entry() -> str:
    """Return the honest tab count as digits only."""
    return ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
