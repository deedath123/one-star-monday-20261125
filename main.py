#!/usr/bin/env python3
"""One Star for Monday — make.fun bounty entry.

Writes one line of plain text: a one-star review of Monday
as if Monday were a restaurant.
Standard library only; no network.
"""

import os

ENTRY = "One star. Seated at 9:04, waited 47 minutes for coffee, and the waiter handed me Tuesday's menu with Monday's prices. Still hungry. Never again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
