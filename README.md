## What this is

Explicit finite-state Markov-modulated Poisson arrival processes, and a random-phase periodic one, for which speeding up the environment strictly increases mean stationary workload in a single-server queue with unit deterministic service. This answers the universal-validity question in Problem 1 of Leskelä (2022) in the negative.

## Main statement

Let a stationary 64-state chain have generator $Q=r(S-I)+(\Pi-I)/2000$, where $S$ advances around the cycle, every entry of $\Pi$ is $1/64$, and $r=1/\sin(2\pi/64)$. Set $x_j=1+\cos(2\pi(j+1/4)/64)/2$ and arrival intensity $x_{J(ct)}/2000$, with unit service requirements and server speed. Every off-diagonal transition rate and every intensity level is positive. The [note](note/ross_modulation_note.pdf) proves $w(3\pi)-w(2\pi)>1587/25\,580\,800\,000\,000>0$ for this process. This counterexample is for Markov-modulated environments outside the stochastically monotone class.

## Reproduce

```sh
python3 verify/run_all.py
```

Python 3.10+; standard library only. Expected runtime: under one second on a laptop. Each certificate prints its result; success ends with `ALL CHECKS PASSED` and exit status 0.

## What is and is not verified

The scripts check the arithmetic of the certificates. All comparisons establishing them use integers or exact fractions; floating-point values are diagnostics. The probabilistic argument is in [the derivation](docs/upper_bound_audit.md) and [the note](note/ross_modulation_note.pdf). The [Markov construction note](docs/unrestricted_modulation_speed_v2.md) records the cycle construction preceding the full-support refinement. These checks are not formal verification or independent peer review. Novelty relative to Rolski (1987, 1989), Lemoine (1989), Heyman (1982), and Miyoshi–Rolski (2004) is not established.

## Citation

Tynan Daly (2026). *Modulation-speed workload counterexamples for Cox/D/1 queues*. Version 1.0.0. See [CITATION.cff](CITATION.cff). Licensed under [CC-BY-4.0](LICENSE).

DOI: [10.5281/zenodo.22686842](https://doi.org/10.5281/zenodo.22686842)

[![DOI](https://zenodo.org/badge/1363809067.svg)](https://doi.org/10.5281/zenodo.22686842)

## Acknowledgment of AI assistance

AI tools assisted with the mathematical derivation, writing, and verification code; the author is responsible for the content.
