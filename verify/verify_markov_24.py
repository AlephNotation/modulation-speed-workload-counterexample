#!/usr/bin/env python3
"""Exact arithmetic certificate for a 24-state Markov-modulated queue.

Python 3.10+, standard library only. No simulation, floating-point sign test,
or external input. The CTMC jumps j -> j+1 (mod 24) at rate c. Its stationary
law is uniform. Arrival intensity in state j is eps*x[j]; services are
deterministically 1. This verifies finite matrix-series bounds and the
resulting workload certificate. The probabilistic workload inequality is
proved in note/ross_modulation_note.tex and docs/upper_bound_audit.md.
No global minimality or novelty is claimed.
"""
from fractions import Fraction as F
from math import factorial

# These integers DEFINE the intensities exactly (they are not computed cosines).
LEVELS = (
    1499, 1473, 1416, 1330, 1221, 1098, 967, 839, 722, 624, 552, 510,
    501, 527, 584, 670, 779, 902, 1033, 1161, 1278, 1376, 1448, 1490,
)
SCALE = 1000
EPSILON = F(1, 1_000_000)
M = F(3, 2)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def kernel_interval(c: int, terms: int = 240) -> tuple[F, F]:
    """Enclose K(c) = (x^T/n) integral_0^1 (1-u) exp(cQu) x du.

    Q = S-I, with (Sv)[j] = v[j+1]. Thus ||Q||_infinity = 2.
    Integrating the matrix exponential gives sum_m c^m Q^m/(m+2)!.
    v below is Q^m * LEVELS, computed using integers.
    Since sum(x)/n=1, the omitted tail has absolute size at most
      M * (2c)^(terms+1)/(terms+3)! / (1 - 2c/(terms+4)).
    """
    if c <= 0 or terms < 0 or 2*c >= terms+4:
        raise ValueError('Require c > 0, terms >= 0, and 2*c < terms+4.')
    n = len(LEVELS)
    v = list(LEVELS)
    coefficient = F(1, 2)
    total = F(0)
    for m in range(terms+1):
        product = F(sum(x*y for x, y in zip(LEVELS, v)), n*SCALE**2)
        total += coefficient*product
        v = [v[(j+1) % n] - v[j] for j in range(n)]
        coefficient *= F(c, m+3)
    tail = M*F((2*c)**(terms+1), factorial(terms+3)) / (1-F(2*c, terms+4))
    return total-tail, total+tail


def main() -> None:
    require(len(LEVELS) == 24 and len(set(LEVELS)) == 24, '24 distinct levels')
    require(sum(LEVELS) == len(LEVELS)*SCALE, 'mean multiplier must be 1')
    require(all(0 < F(x, SCALE) <= M for x in LEVELS), 'intensity bound')
    require(EPSILON*M < 1, 'dominating queue must be stable')

    slow = kernel_interval(29)
    fast = kernel_interval(30)
    # Round OUTWARDS to small rational bounds, checked against the full intervals.
    k_slow_upper = F(503796, 1_000_000)
    k_fast_lower = F(503798, 1_000_000)
    require(slow[1] < k_slow_upper, 'slow kernel enclosure failed')
    require(fast[0] > k_fast_lower, 'fast kernel enclosure failed')
    gap = EPSILON**2*(k_fast_lower - k_slow_upper/(1-EPSILON*M))
    require(gap > F(1, 10**18), 'positive workload gap not certified')

    print('24-state Markov workload certificate: PASSED')
    print('All comparisons establishing the sign use exact fractions.')
    print('Q[j,j+1 mod 24] = 1; Q[j,j] = -1. Actual generator = c*Q.')
    print('eps = 1/1000000; compare c=29 with c=30; service = 1.')
    print(f'K(29) < {k_slow_upper} = {float(k_slow_upper):.6f}')
    print(f'K(30) > {k_fast_lower} = {float(k_fast_lower):.6f}')
    print(f'w(30)-w(29) > {gap} > 1/10^18')
    print(f'Decimal display of rational gap: {float(gap):.15e}')
    print('Not a proof of novelty, smallest possible state count, or formal verification.')


if __name__ == '__main__':
    main()
