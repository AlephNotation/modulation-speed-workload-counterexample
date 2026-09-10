#!/usr/bin/env python3
"""Exact arithmetic audit for the periodic Cox/D/1 counterexample.

Python 3, standard library only. This verifies numerical certificates,
not the probability proof, novelty, or simulated stationary workloads.
See docs/upper_bound_audit.md for the probabilistic derivation.
"""
from fractions import Fraction


def certificate(rho: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return the slow upper bound, fast strict lower bound, and their gap."""
    if not 0 < rho < Fraction(1, 2):
        raise ValueError("Expected 0 < rho < 1/2 for the dominating queue.")
    slow_upper = rho / 2 + rho**2 / (2 * (1 - 2 * rho))
    # K(3*pi) = 1/2 + 1/(9*pi^2) > 1/2 + 1/90.
    fast_lower = rho / 2 + rho**2 * (Fraction(1, 2) + Fraction(1, 90))
    gap = fast_lower - slow_upper
    closed_gap = rho**2 * (1 - 92 * rho) / (90 * (1 - 2 * rho))
    if gap != closed_gap:
        raise AssertionError("Algebraic identities disagree.")
    return slow_upper, fast_lower, gap


def main() -> None:
    expected = {
        Fraction(1, 100): Fraction(1, 11025000),
        Fraction(1, 1000): Fraction(227, 22455000000),
    }
    for rho, expected_gap in expected.items():
        slow, fast, gap = certificate(rho)
        if gap != expected_gap or gap <= 0:
            raise AssertionError(f"Certificate failed at rho={rho}.")
        remainder = rho**3 / (1 - 2 * rho)
        print(f"rho = {rho}")
        print(f"  w(2*pi) <= {slow}")
        print(f"  w(3*pi) >  {fast}")
        print(f"  workload increase > {gap} = {float(gap):.15e}")
        print(f"  slow remainder <= {float(remainder):.15e}")
    # This tests only the threshold of this certificate, not the true phenomenon.
    if certificate(Fraction(1, 92))[2] != 0:
        raise AssertionError("Unexpected certificate threshold.")
    print("Exact arithmetic checks: PASSED")


if __name__ == "__main__":
    main()
