#!/usr/bin/env python3
"""For running it in Command Line Interface execute as follows: ./extractor.py <type> "text"  or( ./extractor.py all "text")"""
import sys

from patterns import PATTERNS, extract


def main() -> None:
    if len(sys.argv) != 3 or (sys.argv[1] not in PATTERNS and sys.argv[1] != "all"):
        print(f"Usage: {sys.argv[0]} <{'|'.join(PATTERNS)}|all> \"text\"")
        sys.exit(1)

    kind, text = sys.argv[1], sys.argv[2]
    kinds = PATTERNS if kind == "all" else [kind]
    for k in kinds:
        for match in extract(k, text):
            print(f"{k}: {match}" if kind == "all" else match)


if __name__ == "__main__":
    main()
