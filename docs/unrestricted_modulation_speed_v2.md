# Working note: a proposed counterexample to the unrestricted modulation-speed question in Leskela (2022)

**Date:** 7 September 2026.  
**Status:** Mathematical derivation produced in this examination, not independently refereed or formally verified. Novelty has not been established. The accompanying script checks arithmetic and evaluates the covariance independently from the finite-state generator; it does not verify all probability arguments.

## 1. Target statement and historical scope

**Scope correction, revision 2.** This note targets the universal inequality in the first part of Problem 1 in Leskela (2022). It does not refute the original two-state Markov-modulation case, does not contradict the established positive theorems under stochastic-monotonicity assumptions, and does not solve the necessary-and-sufficient characterization requested in the second part of Problem 1. An unqualified description as a disproof of Ross's original conjecture would be misleading.

Ross's accessible May 1977 technical report, preceding the 1978 journal article, gives a two-state CTMC as its explicit modulation-speed conjecture. The Shaked-Shanthikumar 1991 review also records the two-state formulation. Leskela's broader Problem 1 allows a stationary ergodic baseline intensity, not only a CTMC. The historical distinction does not alter the mathematical inequality examined below. The full 1978 journal text has not been audited line by line here.

The target is Problem 1 in Lasse Leskela, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems **100** (2022), 213-215, DOI 10.1007/s11134-022-09824-0; author preprint arXiv:2204.11856.

For a stable single-server queue with Cox arrivals of stationary ergodic intensity
\[
\lambda_c(t)=\lambda(ct),\qquad c>0,
\]
and independent identically distributed service times, let \(w(c)\) be the mean stationary workload. The universal monotonicity assertion is
\[
c_1\le c_2\quad\Longrightarrow\quad w(c_1)\ge w(c_2).
\]
The construction below concerns this unrestricted formulation, not subclasses with additional stochastic-monotonicity assumptions. It addresses failure of workload monotonicity itself, not merely failure of a sufficient dependence ordering.

## 2. A finite-load workload bound

Let \(X\) be a stationary nonnegative intensity multiplier with
\[
E X(0)=1,\qquad X(t)\le M.
\]
Fix \(\epsilon>0\) with \(\epsilon M<1\). Conditional on the full environment path, arrivals are Poisson with intensity \(\epsilon X(ct)\). Every job requires exactly one unit of service; the work-conserving server processes one unit of work per unit time. Write \(V_c(t)\) for the stationary workload and \(w_\epsilon(c)=E V_c(0)\).

Define
\[
K(c)=\int_0^1(1-u)E[X(0)X(cu)]\,du.
\]
Then
\[
\boxed{\frac\epsilon2+\epsilon^2K(c)
\ \le\ w_\epsilon(c)\ \le\
\frac\epsilon2+\frac{\epsilon^2K(c)}{1-\epsilon M}.}
\tag{1}
\]

### Stationary construction and integrability

Construct the environment on the whole real line in stationarity. Independently generate a two-sided homogeneous Poisson proposal process with rate \(\epsilon M\), with independent uniform marks. Accept the proposal at time \(t\) when its mark is at most \(X(ct)/M\). Conditional on the entire environment path, the accepted points have the desired Poisson intensity.

For a horizon \(T\), start the queue empty at \(-T\). Equivalently, at zero its workload is the nonnegative reflected net-input supremum over starting times in \([-T,0]\). As \(T\) increases these workloads increase pathwise. They are bounded above by the stationary homogeneous M/D/1 workload driven by all proposal points, whose arrival rate \(\epsilon M<1\). That dominating workload is finite and has finite moments of every order. The monotone limit therefore exists and has these same integrability properties. Applying the construction at every time gives a stationary version, because it is a shift-equivariant function of stationary input. This is a Loynes-type construction; no independence of successive accepted interarrival times is being asserted.

To justify the quadratic balance without a formal differentiation of a stationary law, use the pathwise identity, for any fixed \(t>0\),
\[
V_c(t)^2-V_c(0)^2
=-2\int_0^t V_c(s)\,ds
+\int_{(0,t]}(2V_c(s-)+1)N_c(ds).
\]
The domination just described, together with bounded intensity, makes both integrals integrable. The predictable compensator of \(N_c\) is \(\epsilon X(cs)ds\), with predictable versions at the finitely many environmental jump times. Taking expectations and using stationarity cancels the left side and yields equation (2) below. Thus no unproved interchange between a limiting workload and a derivative is needed.

### Proof of (1)

At an arrival, \(V\) jumps by one; away from arrivals, it decreases at speed one when positive. Stationary balance for \(V^2\) gives
\[
0=-2EV_c(0)+\epsilon E[X(0)(2V_c(0)+1)],
\]
so
\[
w_\epsilon(c)=\frac\epsilon2+\epsilon E[X(0)V_c(0)].
\tag{2}
\]
Here \(X(c\cdot0)=X(0)\). Values immediately before or at time zero agree almost surely. The compensator is \(\epsilon X(ct)dt\); independence between the environment and workload is neither assumed nor used.

Let
\[
Y_c=\sum_{T_i\in(-1,0)}(1+T_i)
\]
be the work remaining at time zero in an infinite-server system that starts each unit-service job immediately. Pathwise,
\[
V_c(0)\ge Y_c.
\tag{3}
\]
Indeed, a job of age \(u<1\) cannot have received more than \(u\) units of service from a unit-speed single server; it therefore contributes at least \(1-u\) residual work. Older jobs contribute nonnegative additional residual work.

Conditional Poisson expectation and stationarity yield
\[
E Y_c=\frac\epsilon2,
\qquad
E[X(0)Y_c]
=\epsilon\int_0^1(1-u)E[X(0)X(-cu)]\,du
=\epsilon K(c).
\tag{4}
\]
The last equality only uses symmetry of the scalar stationary autocorrelation:
\(E[X(0)X(-t)]=E[X(0)X(t)]\). It does not require reversibility.

Put \(D_c=V_c(0)-Y_c\ge0\) and \(d=E D_c=w_\epsilon(c)-\epsilon/2\). Equations (2)-(4) imply
\[
d=\epsilon^2K(c)+\epsilon E[X(0)D_c].
\]
Consequently,
\[
\epsilon^2K(c)\le d\le\epsilon^2K(c)+\epsilon M d.
\]
Rearranging proves (1).

In particular, this is an explicit remainder bound, not a merely formal light-traffic expansion:
\[
w_\epsilon(c)=\epsilon/2+\epsilon^2K(c)+R_\epsilon(c),
\qquad
0\le R_\epsilon(c)\le\frac{\epsilon^3M K(c)}{1-\epsilon M}.
\tag{5}
\]
Since \(K(c)\le M/2\), the remainder is bounded uniformly in \(c\).

A useful general consequence is that if \(K(c_2)>K(c_1)\), then workload monotonicity is reversed whenever
\[
0<\epsilon<\frac{K(c_2)-K(c_1)}{M K(c_2)}.
\tag{6}
\]

## 3. Motivation: an oscillating environment

For intuition, consider a uniform random phase \(\Theta\) and
\[
X(t)=1+\frac12\cos(t+\Theta).
\]
This stationary process has
\[
E[X(0)X(t)]=1+\frac18\cos t,
\qquad
K(c)=\frac12+\frac{1-\cos c}{8c^2}.
\]
Thus \(K(3\pi)>K(2\pi)\). The triangular service-time weighting does not average an oscillating covariance monotonically as the modulation speed increases.

The counterexample used below does not rely on a periodic nonmixing environment: it replaces this sinusoid by an irreducible finite-state continuous-time Markov chain.

## 4. Explicit 64-state Markov environment

Set
\[
n=64,\quad\theta=\frac{2\pi}{64},\quad r=\frac1{\sin\theta}.
\]
Let \(J(t)\) be a continuous-time Markov chain on \(\{0,\ldots,63\}\) with transitions
\[
j\longrightarrow j+1\pmod {64}\quad\text{at rate }r.
\]
Its generator has \(q_{j,j+1}=r\), \(q_{jj}=-r\), and no other off-diagonal entries. Start the chain in its uniform stationary distribution.

Define
\[
x_j=1+\frac12\cos\!\left(\frac{2\pi(j+1/4)}{64}\right),
\qquad X(t)=x_{J(t)}.
\tag{7}
\]
The quarter-step phase shift makes the 64 intensity levels distinct: equality between two cosine values would require either equal indices modulo 64, or an integer \(j+k+1/2\) to be a multiple of 64, which is impossible. Thus \(X\) itself is a finite-state Markov chain, not only a non-Markov observation of one.

We have
\[
E X(0)=1,\qquad \frac12<X(t)<\frac32.
\]
The chain is irreducible and exponentially mixing. The periodicity of its embedded jump chain does not make its continuous-time semigroup periodic: the nonconstant Fourier modes have strictly negative real parts.

Choose
\[
\epsilon=\frac1{2000},\qquad M=\frac32,
\qquad \lambda_c(t)=\epsilon x_{J(ct)}.
\tag{8}
\]
Every queue in the comparison has the same mean arrival rate \(1/2000\), deterministic unit services, and a unit-speed server. The maximal instantaneous intensity is below \(3/4000<1\), ensuring the dominating queue is stable. Speeding the environment from \(c_1\) to \(c_2\) changes its generator from \(c_1Q\) to \(c_2Q\), exactly as required.

### Correlation calculation

For \(t\ge0\), conditional on \(J(0)\), the number of forward jumps is Poisson with mean \(rt\). The first Fourier mode therefore has eigenvalue
\[
r(e^{i\theta}-1)=-a+i,
\qquad
 a=\frac{1-\cos\theta}{\sin\theta}=\tan\frac\pi{64}.
\]
Averaging the product of cosines over the uniform initial state gives
\[
E[X(0)X(t)]=1+\frac18e^{-at}\cos t.
\tag{9}
\]
Consequently,
\[
K(c)=\frac12+\frac18 I_a(c),
\qquad
I_a(c)=\int_0^1(1-u)e^{-acu}\cos(cu)\,du.
\tag{10}
\]
For \(z=(-a+i)c\), elementary integration gives
\[
I_a(c)=\operatorname{Re}\frac{e^z-1-z}{z^2}.
\tag{11}
\]

## 5. Numerical display of the separated bounds

The following values are evaluations of explicit expressions, not simulated queue means:

| Quantity | \(c=2\pi\) | \(c=3\pi\) |
|---|---:|---:|
| \(I_a(c)\) | 0.0144786436389434106 | 0.0234111761893566333 |
| \(K(c)\) | 0.501809830454867926 | 0.502926397023669579 |
| Lower bound for \(w(c)\) in (1) | 0.000250125452457613717 | 0.000250125731599255917 |
| Upper bound for \(w(c)\) in (1) | 0.000250125546617576900 | 0.000250125825968732467 |

The lower bound at \(3\pi\) exceeds the upper bound at \(2\pi\). The difference between these bounds is approximately \(1.8498167901773847\times10^{-10}\).

An independent 64-by-64 matrix-exponential computation evaluated
\[
E[X(0)X(t)]=64^{-1}x^T e^{Qt}x
\]
and integrated it to check (9)-(11). High-precision scalar quadrature also agreed. These are numerical consistency checks; the exact sign certificate follows next.

## 6. An elementary rational sign certificate

This section avoids relying on floating-point evaluation of trigonometric or exponential functions to establish the workload reversal.

First, \(0<a<1/20\). Indeed, with \(x=\pi/64<11/224\),
\[
\tan x<\frac{x}{1-x^2/2}\le
\frac{11/224}{1-(11/224)^2/2}<\frac1{20}.
\]
Define
\[
A=\frac{a}{1+a^2},\qquad
C=\frac{1-a^2}{(1+a^2)^2}.
\]
Then \(A<a\) and \(99/100<C<1\). The lower bound on \(C\) follows by its decrease on \([0,1/20]\) and evaluation at \(1/20\).

At integer multiples of \(\pi\), equation (11) becomes
\[
I_a(k\pi)=\frac{A}{k\pi}
+C\frac{1-(-1)^ke^{-ak\pi}}{(k\pi)^2}.
\]
Hence
\[
I_a(3\pi)-I_a(2\pi)
=-\frac{A}{6\pi}
+C\left[
\frac{1+e^{-3\pi a}}{9\pi^2}
-\frac{1-e^{-2\pi a}}{4\pi^2}
\right].
\]
Using \(e^{-x}\ge1-x\), \(1-e^{-x}\le x\), and \(3<\pi<22/7\), the bracket is bounded below by
\[
\frac{2}{9\pi^2}-\frac{5a}{6\pi}
>\frac{2}{9(22/7)^2}-\frac1{72}>0.
\]
Therefore
\[
I_a(3\pi)-I_a(2\pi)
> -\frac1{360}+
\frac{99}{100}\left[\frac{2}{9(22/7)^2}-\frac1{72}\right]
=\frac{91}{15840}>\frac1{200}.
\]
It follows that
\[
K(3\pi)-K(2\pi)>\frac1{1600}.
\tag{12}
\]
Also
\[
I_a(2\pi)
\le\frac{a}{2\pi}+\frac{2\pi a}{4\pi^2}
=\frac a\pi<\frac1{60},
\qquad
K(2\pi)<\frac{241}{480}.
\tag{13}
\]
Combining (1), (12), and (13) yields
\[
\begin{aligned}
w(3\pi)-w(2\pi)
&\ge \epsilon^2\left[K(3\pi)-\frac{K(2\pi)}{1-\epsilon M}\right]\\
&>\frac1{2000^2}\left[
\frac1{1600}-\frac{(3/4000)(241/480)}{1-3/4000}
\right]\\
&=\boxed{\frac{1587}{25\,580\,800\,000\,000}>0.}
\end{aligned}
\tag{14}
\]
Thus the proposed counterexample is at explicit positive load, with an exact strictly positive lower bound. No limiting interchange or unquantified asymptotic remainder is needed.

## 7. Workload versus customer waiting time

Cox arrivals do not in general see the time-stationary workload distribution. The calculation above does not invoke PASTA.

In the FCFS unit-service example, let \(W_c\) be a typical arrival's waiting time before service. The arrival mean is obtained by intensity weighting:
\[
E^0 W_c=\frac{E[\lambda_c(0)V_c(0)]}{E\lambda_c(0)}
=E[X(0)V_c(0)].
\]
Equation (2) therefore gives
\[
w(c)=\epsilon\left(E^0W_c+\frac12\right).
\]
The mean arrival rate is identical in the two queues, so (14) also implies a reversal of mean customer waiting time. Adding the same unit service requirement preserves the reversal for mean time in system.

## 8. Interpretation, scope, and audit priorities

The mechanism is an oscillatory autocorrelation combined with a fixed service duration. The relevant light-traffic coefficient averages the autocorrelation with a triangular kernel of one service-time width. Faster modulation need not decrease that weighted integral. The finite-load bound makes this mechanism an actual workload comparison.

The claim concerns the unrestricted statement quoted in Section 1. It does not refute positive results proved for stochastically monotone intensity processes; it does not supply a necessary-and-sufficient characterization of all environments with workload monotonicity. The state count is not claimed minimal, and no counterexample with exponential services is claimed here.

The derivation needs independent review, especially of the stationary-workload construction, the infinite-server lower comparison, and the match to the precise conjecture being discussed. A targeted literature search did not locate a later general resolution, but absence from that search is not a novelty certificate. The elementary bound or this oscillatory mechanism could have appeared under other terminology.

The example's effect is deliberately small: the construction chooses a very light load so the sign is easy to certify. Its proposed significance is logical failure of universal monotonicity, not a claim of a large operational performance penalty.

## References for the research context

- L. Leskela (2022). *Ross's second conjecture and supermodular stochastic ordering*. Queueing Systems 100, 213-215. DOI: 10.1007/s11134-022-09824-0. Author preprint: https://arxiv.org/abs/2204.11856 . This is the precise target formulation used here.
- N. Baeuerle and T. Rolski (1998). *A monotonicity result for the workload in Markov-modulated queues*. Journal of Applied Probability 35(3), 741-747. DOI: 10.1239/jap/1032265221. Establishes an increasing-convex workload ordering under monotonicity assumptions on the modulating generator.
- S. M. Ross (1978). *Average delay in queues with non-stationary Poisson arrivals*. Journal of Applied Probability 15(3), 602-609. Original historical source; this examination does not claim a complete line-by-line audit of the original article.

## Original reproduction instructions

From the repository root, run `python3 verify/run_all.py` for the included exact rational certificates and decimal displays. The 64-state verifier checks the full-support refinement in `note/ross_modulation_note.tex`; the cycle construction above is the preceding version. Optional high-precision quadrature and finite-generator semigroup routines are not included.

The script verifies neither the queueing proof in a proof assistant nor novelty. Its default positive certificate is exact rational arithmetic, rather than a floating-point sign test.


## 9. What the literature audit establishes, and what it does not

This is a partial audit, not a novelty certificate. References below are distinct from mathematical verification of the construction.

- **Original scope:** The May 1977 Ross technical report explicitly uses a two-state CTMC for the speed comparison. Shaked and Shanthikumar (1991), *Regular, sample path and strong stochastic convexity: a review*, also presents the two-state version and describes positive resolutions. This note should not be advertised as overturning that result.
- **Exact modern target:** Both the arXiv paper and the accepted-manuscript record for Leskela (2022) allow arbitrary stationary ergodic baselines in Problem 1. Its first part asks whether the workload inequality always holds; its second part asks for a characterization if it does not. Only the first part is addressed here. The discussion floats stochastic monotonicity as a possible characterization, conditionally; a single nonmonotone example does not establish that characterization.
- **Baeuerle and Rolski (1998):** The published abstract establishes positive workload ordering under monotonicity assumptions on the generator. The full article was not obtained for line-by-line inspection in this audit.
- **Miyoshi and Rolski (2004):** The accessible article text was inspected, including Theorem 2 and Remark 2. Theorem 2 proves workload and waiting-time monotonicity under increasing-directionally-convex regularity of the environment. Remark 2 conjectures a converse. No unrestricted continuous-time counterexample was located in that text.
- **Baeuerle (1997), *Inequalities for stochastic models via supermodular orderings*:** The relevant applications were inspected in the author-repository PDF. Application 4.6 gives a positive result for a discrete-time packet queue with specially structured two-state source chains, and Application 4.7 concerns the first claim time in a risk model. This does not establish the alleged earlier discrete-time counterexample to an extended Ross statement. The precise source and statement of that alleged counterexample remain unidentified.
- **Bambos and Walrand (1989), *On queues with periodic inputs*:** The publisher abstract concerns stability and asymptotic periodicity, including extensions to acyclic networks. Only the abstract and bibliographic information were inspected; the paper has not been cleared as prior art.
- **Lemoine (1989), *Waiting time and workload in queues with periodic Poisson input*:** The publisher abstract explicitly gives moment formulas for periodic Poisson input and general service, with exact calculations in certain cases. This is particularly relevant prior art. Only the abstract and bibliographic information were inspected; it remains necessary to inspect the formulas and examples.
- **Light traffic:** Bashtova (2006), *Small work-load mode in a queueing system with random nonstationary intensity*, explicitly studies a doubly stochastic Poisson single-server queue and gives a light-load expansion of the virtual waiting-time distribution. Its abstract alone does not identify the coefficient or settle whether the present finite-load bound or oscillatory example is already known. The older exact source for the claimed triangular-correlation coefficient has not been identified in this audit. No novelty is claimed for the coefficient.

The original random-phase sinusoid is itself stationary and ergodic under the full continuous-time translation action, although not mixing. Thus it already fits the literal unrestricted question once combined with the finite-load bound. The finite-state construction has the additional merit of being an irreducible, mixing CTMC with strictly positive intensities; it is not needed merely to repair a failure of continuous-time ergodicity.

### Additional reference details and access records

1. S. M. Ross, *Average Delay in Queues with Nonstationary Poisson Arrivals*, May 1977 technical report, DTIC ADA041629. Accessible report text: https://archive.org/stream/DTIC_ADA041629/DTIC_ADA041629_djvu.txt . This is the report version, not a claim to have read the entire 1978 journal version.
2. M. Shaked and J. G. Shanthikumar (1991), *Regular, sample path and strong stochastic convexity: a review*, IMS Lecture Notes-Monograph Series 19, 320-333, DOI 10.1214/lnms/1215459864. Accessible article text inspected at https://www.academia.edu/105089230/Regular_sample_path_and_strong_stochastic_convexity_a_review .
3. N. Miyoshi and T. Rolski (2004), *Ross-Type Conjectures on Monotonicity of Queues*, Australian & New Zealand Journal of Statistics 46, 121-131. Accessible article text: https://www.academia.edu/84475651/Ross_Type_Conjectures_on_Monotonicity_of_Queues .
4. N. Baeuerle (1997), *Inequalities for stochastic models via supermodular orderings*, Stochastic Models 13, 181-201, DOI 10.1080/15326349708807420. Repository PDF: https://publikationen.bibliothek.kit.edu/1000043737/3324855 .
5. N. Bambos and J. Walrand (1989), *On queues with periodic inputs*, Journal of Applied Probability 26, 381-389, DOI 10.2307/3214043.
6. A. J. Lemoine (1989), *Waiting time and workload in queues with periodic Poisson input*, Journal of Applied Probability 26, 390-397, DOI 10.2307/3214044.
7. E. E. Bashtova (2006), *Small work-load mode in a queueing system with random nonstationary intensity*, Mathematical Notes 80, 329-338, DOI 10.1007/s11006-006-0144-1.

## 10. Load, service distributions, and limitations of the mechanism

The original sufficient condition (6), using the closed-form values rather than the coarser rational bounds, requires
\[
\epsilon < \frac{K(3\pi)-K(2\pi)}{(3/2)K(3\pi)}
\approx 0.001480092747.
\]
This is a limitation of the current certificate, not a proof that the actual workload reversal disappears at higher load. No moderate-load simulation or certified moderate-load computation is supplied here. The small numerical difference should not be presented as a large operational penalty.

The service distribution matters, but exact determinism is **not** essential. Here is an explicit extension of the same proposed argument to a nondegenerate continuous service distribution.

### Mean-one bounded service times

Let service requirements \(B_i\) be iid, bounded, independent of the environment and arrivals, with \(EB=1\). Write
\[
h_B(u)=E(B-u)_+,\qquad
K_B(c)=\int_0^\infty h_B(u)R(cu)\,du,
\quad R(t)=E[X(0)X(t)].
\]
Assume the dominating homogeneous queue is stable; for the concrete bounded uniform example below this also follows by replacing every service requirement with its maximum.

Quadratic balance for jumps \(V\mapsto V+B\) gives
\[
w_B(c)=\epsilon EB^2/2+\epsilon E[X(0)V_c(0)].
\]
The infinite-server comparison is now
\[
Y_B=\sum_{T_i<0}(B_i+T_i)_+\le V_c(0).
\]
Independence of service marks and conditional Poisson expectation yield
\[
EY_B=\epsilon EB^2/2,\qquad E[X(0)Y_B]=\epsilon K_B(c).
\]
Exactly the same nonnegative-excess argument as in Section 2 therefore proves
\[
\boxed{\epsilon EB^2/2+\epsilon^2K_B(c)
\le w_B(c)\le
\epsilon EB^2/2+\frac{\epsilon^2K_B(c)}{1-\epsilon M}.}
\]
The baseline term \(\epsilon EB^2/2\) is identical at the two speeds and cancels in their comparison.

### An explicit nondegenerate service example

Take \(B\) uniform on \([1-\delta,1+\delta]\), with \(\delta=1/100\), and retain the same 64-state environment and \(\epsilon=1/2000\). By convexity,
\[
h_B(u)\ge (1-u)_+,
\qquad
\int_0^\infty[h_B(u)-(1-u)_+]du
=\frac{EB^2-1}{2}=\frac{\delta^2}{6}.
\]
Also \(0\le R(t)\le M\), because \(X\ge0\), \(X\le M\), and \(EX=1\). Hence, uniformly in \(c\),
\[
0\le K_B(c)-K(c)\le M\delta^2/6.
\]
Applying the original exact certificate then gives
\[
\begin{aligned}
w_B(3\pi)-w_B(2\pi)
&>\frac{1587}{25\,580\,800\,000\,000}
-\epsilon^2\frac{M\delta^2/6}{1-\epsilon M}\\
&=\frac{1427}{25\,580\,800\,000\,000}>0.
\end{aligned}
\]
Thus the proposed reversal survives continuous iid service-time randomness on \([0.99,1.01]\). This is a mathematical extension of the present argument, not a claim of independent verification or novelty.

### Exponential services: the relevant limitation

For mean-one exponential services, \(h_B(u)=e^{-u}\). With
\(R(t)=1+\beta e^{-at}\cos t\),
\[
K_B(c)=1+\beta\frac{1+ac}{(1+ac)^2+c^2}.
\]
If \(a\ge0\) and \(\beta>0\), its nonconstant factor has derivative
\[
-\frac{a+2(a^2+1)c+a(a^2+1)c^2}
{((1+ac)^2+c^2)^2}<0\quad(c>0).
\]
So this particular covariance does not produce the same second-order light-traffic reversal with exponential services. This calculation does not prove workload monotonicity at every positive load, nor for arbitrary exponential-service environments.

## 11. Revised reproduction

`python3 verify/run_all.py` checks the periodic, full-support 64-state, and rational 24-state certificates. The uniform-service perturbation arithmetic described above is not checked by the included scripts. The scripts neither verify the probabilistic argument in a proof assistant nor establish novelty.
