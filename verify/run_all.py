#!/usr/bin/env python3
"""Run every arithmetic certificate using Python 3.10+ and its standard library."""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer is required.", file=sys.stderr)
        return 1

    directory = Path(__file__).resolve().parent
    certificates = (
        "audit_upper_bound.py",
        "verify_markov_64.py",
        "verify_markov_24.py",
    )
    failed = False
    for name in certificates:
        print(f"=== {name} ===", flush=True)
        result = subprocess.run(
            [sys.executable, "-I", "-B", "-u", str(directory / name)],
            cwd=directory.parent,
            check=False,
        )
        if result.returncode != 0:
            print(f"FAILED: {name} (exit {result.returncode})", flush=True)
            failed = True

    print("CHECKS FAILED" if failed else "ALL CHECKS PASSED", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
