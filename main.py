#!/usr/bin/env python3
"""Make the Judge Smile — make.fun bounty
u-gentle-badger-68-make-the-judge-smile-9228676d

Writes one line (1-200 chars) about a small good thing that happened
today to /output/entry.txt. Deterministic, stdlib only, no network.
"""
import os
import sys

ENTRY = (
    "My neighbour's kid taped a drawing to my door this morning: "
    "me in a cape, holding a durian like a trophy."
)


def main() -> int:
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit(
            "error: ENTRY must be 1-200 characters and not whitespace-only "
            f"(got {len(ENTRY)} characters)"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
