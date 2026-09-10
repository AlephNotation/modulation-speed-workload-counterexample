#!/usr/bin/env python3
"""64-state Markov counterexample with every off-diagonal rate positive.

Python 3.10+, standard library only. The certificate uses exact fractions;
decimal formula evaluations are diagnostics and do not establish the sign.
The probability proof and elementary inequalities are in
note/ross_modulation_note.tex. This script is not a formal proof of the
queueing argument or a novelty audit.
"""
from __future__ import annotations

import cmath
import math
from fractions import Fraction as F

N = 64
RESET = F(1, 2000)
EPSILON = F(1, 2000)
M = F(3, 2)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def certify() -> F:
    # tan(pi/64) < u/(1-u^2/2), using pi < 22/7 and u=11/224.
    u = F(11, 224)
    alpha_upper = u/(1-u*u/2) + RESET
    require(alpha_upper < F(1, 20), 'damping bound')
    a = F(1, 20)
    C_lower = (1-a*a)/(1+a*a)**2
    require(C_lower > F(99, 100), 'C bound')
    bracket = F(2, 9)/F(22, 7)**2 - F(1, 72)
    require(bracket > 0, 'bracket positivity')
    delta_I = -F(1, 360)+F(99, 100)*bracket
    require(delta_I == F(91, 15840) and delta_I > F(1, 200), 'integral gap')
    gap = EPSILON**2*(F(1, 1600) - EPSILON*M*F(241, 480)/(1-EPSILON*M))
    require(gap == F(1587, 25580800000000) and gap > 0, 'workload gap')
    print('Full-support 64-state certificate: PASSED')
    print('q[j,j+1 mod 64] = r + 1/128000; all other off-diagonals = 1/128000')
    print('r = 1/sin(2*pi/64); diagonal entries give zero row sums.')
    print('x[j] = 1 + cos(2*pi*(j+1/4)/64)/2; eps=1/2000; service=1.')
    print(f'alpha < {alpha_upper} < 1/20')
    print(f'w(3*pi)-w(2*pi) > {gap} = {float(gap):.15e}')
    return gap


def numerical_display() -> None:
    alpha = math.tan(math.pi/N)+float(RESET)
    ks = []
    for k in (2, 3):
        z = complex(-alpha, 1)*k*math.pi
        K = .5+((cmath.exp(z)-1-z)/z**2).real/8
        ks.append(K)
        print(f'K({k}*pi) approximately {K:.17g}')
    e = float(EPSILON)
    print(f'Sharper numerical display of analytic gap: {e*e*(ks[1]-ks[0]/(1-e*float(M))):.15e}')


if __name__ == '__main__':
    certify()
    numerical_display()
