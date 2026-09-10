# Upper-bound audit for the periodic modulation-speed counterexample

Date: 9 September 2026.

Status: Self-contained mathematical argument and exact arithmetic certificates.
Not independently refereed or formally verified. Novelty remains unresolved.
The target is the universal inequality in Problem 1 of Leskela (2022), not
Ross's original two-state Markov case or the characterization requested in the
second part of Problem 1.

## 1. Model and stationary construction

Let X be a jointly measurable stationary process with E[X(0)] = 1 and
0 <= X(t) <= M. Given its entire path, let arrivals be Poisson with rate
lambda_c(t) = rho X(ct). Each job requires exactly one unit of service,
provided by a work-conserving, unit-speed, single server. Assume rho M < 1.

Construct a two-sided homogeneous Poisson process with rate rho M, independent
of X, carrying independent uniform marks. Keep a proposal at t precisely when
its mark is at most X(ct)/M. This constructs the conditional Poisson arrivals.

Start the single-server queue empty at -T and let T increase. Its workload at
zero increases to the reflected net-input supremum and is bounded above by
the stationary homogeneous M/D/1 workload driven by all proposal points.
This dominating queue has load rho M < 1 and finite moments of every order.
For example, for small positive theta the exponent
rho M (exp(theta)-1)-theta is negative; the associated exponential
supermartingale bounds the net-input supremum by an exponential tail.
The monotone limit therefore exists with finite first and second moments.
Shift-equivariance of this construction gives joint stationarity with X.

We use V_c(t) for this stationary workload and w_rho(c) = E[V_c(0)].
No independence between X and V is assumed.

## 2. Exact quadratic workload balance

For t > 0, the pathwise identity is

\[
V_c(t)^2-V_c(0)^2
=-2\int_0^t V_c(s)\,ds
 +\int_{(0,t]} (2V_c(s-)+1)N_c(ds).
\]

Use a filtration containing the entire exogenous environment and the arrival
history up to the current time. Conditional Poisson compensation then gives
intensity rho X(cs). The moment bounds above justify expectations and
compensation. Stationarity cancels the left-hand side, yielding

\[
w_\rho(c)=\rho/2+\rho E[X(0)V_c(0)]. \tag{1}
\]

This is an arbitrary-time workload identity, not an application of PASTA.

## 3. The excess over an infinite-server system

Define

\[
Y_c=\sum_{T_i\in(-1,0]}(1+T_i).
\]

This is the residual work if every job started service immediately on its own
unit-speed server. A job of age u < 1 cannot have received more than u units
of service in the actual single-server queue. Summing over jobs proves

\[
0\le Y_c\le V_c(0).
\]

Conditional Poisson expectation gives

\[
E Y_c=\rho/2,
\qquad E[X(0)Y_c]=\rho K(c),
\]

where

\[
K(c)=\int_0^1(1-u)E[X(0)X(cu)]\,du.
\]

Here stationarity and commutativity of scalar multiplication imply
E[X(0)X(-t)] = E[X(0)X(t)]; reversibility is unnecessary.

Let D_c=V_c(0)-Y_c >= 0 and d_c=E D_c=w_rho(c)-rho/2.
Substitution in (1) gives the exact identity

\[
d_c=\rho^2K(c)+\rho E[X(0)D_c]. \tag{2}
\]

Since 0 <= X(0) <= M and D_c >= 0,

\[
\rho^2K(c)\le d_c\le\rho^2K(c)+\rho M d_c.
\]

Solving the last inequality proves

\[
\boxed{\rho/2+\rho^2K(c)
\le w_\rho(c)\le
\rho/2+\frac{\rho^2K(c)}{1-\rho M}.} \tag{3}
\]

In particular, if

\[
R_\rho(c)=w_\rho(c)-\rho/2-\rho^2K(c),
\]

then all higher-order corrections, together, satisfy

\[
\boxed{0\le R_\rho(c)\le
\frac{\rho^3 M K(c)}{1-\rho M}.} \tag{4}
\]

There is no assumed cancellation between remainders at two speeds. To lower
bound w_rho(c2)-w_rho(c1), use R_rho(c2) >= 0 and the upper bound for R_rho(c1).
Equations (2)-(4) are the upper-bound derivation requested in the critique.

## 4. Specialization to the random-phase sinusoid

Let

\[
X(t)=1+\cos(t+\Theta),\qquad
\Theta\sim\operatorname{Uniform}[0,2\pi),\qquad M=2.
\]

Uniform phase gives stationarity. The continuous-time shifts act as every
rotation of the phase circle, so any event invariant under all shifts has
probability zero or one: the intensity is ergodic. It is not mixing.
The service law is degenerate iid and independent of arrivals.

Direct integration gives

\[
E[X(0)X(t)]=1+\tfrac12\cos t,
\qquad
K(c)=\tfrac12+\frac{1-\cos c}{2c^2}.
\]

At c1=2*pi and c2=3*pi,

\[
K(c_1)=\tfrac12,\qquad
K(c_2)=\tfrac12+\frac1{9\pi^2}>\tfrac12+\frac1{90}.
\]

The strict elementary estimate uses pi^2 < 10, for example from pi < 22/7.
Consequently, (3) yields

\[
\begin{aligned}
w_\rho(3\pi)-w_\rho(2\pi)
&>\rho^2\left(\frac1{90}-\frac{\rho}{1-2\rho}\right)\\
&=\boxed{\frac{\rho^2(1-92\rho)}{90(1-2\rho)}}.
\end{aligned} \tag{5}
\]

In particular, every 0 < rho < 1/92 is certified by this coarse bound.
This is a sufficient range, not a necessary range for the reversal itself.

### Original load: rho = 1/100

\[
w_{1/100}(2\pi)\le\frac{99}{19600},\qquad
w_{1/100}(3\pi)>\frac{2273}{450000},
\]

so

\[
w_{1/100}(3\pi)-w_{1/100}(2\pi)
>\frac1{11025000}>0.
\]

The slow-speed remainder bound is
rho^3/(1-2*rho) = 1.020408163265306e-6. The coarse second-order gain is
rho^2/90 = 1.111111111111111e-6. Their difference is the certified margin,
9.070294784580498e-8. The remainder has already been subtracted.

### Lower load: rho = 1/1000

\[
w_{1/1000}(2\pi)\le\frac{999}{1996000},\qquad
w_{1/1000}(3\pi)>\frac{22523}{45000000},
\]

so

\[
w_{1/1000}(3\pi)-w_{1/1000}(2\pi)
>\frac{227}{22455000000}>0.
\]

The slow-speed remainder bound is now about 1.0020e-9, while the coarse
second-order gain is 1.1111e-8. This is a wider relative separation, although
the absolute workload gap is smaller. Lowering the load simplifies presentation;
it is not required to repair the proof at rho=1/100.

## 5. Limited literature audit

These are access and inspection results, not a novelty certificate.

- Leskela (2022), Problem 1: inspected the actual PDF statement on page 2.
  It permits stationary ergodic intensity, without a mixing or CTMC requirement.
  https://arxiv.org/pdf/2204.11856
- Miyoshi and Rolski (2004), Section 4.1, Theorem 2 and Remark 2:
  inspected the accessible transcription of the primary paper. The theorem
  establishes increasing-convex speed ordering under idcx regularity; the
  remark proposes a converse. No periodic reversal appears in that section.
  This inspection alone does not clear all related literature.
  https://www.academia.edu/84475651/Ross_Type_Conjectures_on_Monotonicity_of_Queues
- Rolski (1989), Queues with nonstationary inputs, Queueing Systems 5, 113-129:
  inspected publisher abstract and references only. It explicitly discusses
  Ross's conjectures. Full text was not obtained; unresolved prior-art lead.
  https://doi.org/10.1007/BF01149189
- Rolski (1987), Approximation of periodic queues, Advances in Applied
  Probability 19, 691-707: bibliographic details checked against the references
  in the Rolski (1989) and Lemoine (1989) publisher records. Full text not
  obtained; unresolved prior-art lead.
  https://doi.org/10.1017/S0001867800016827
- Lemoine (1989), Waiting time and workload in queues with periodic Poisson
  input, Journal of Applied Probability 26, 390-397: publisher abstract and
  references inspected. The abstract advertises moment formulas and exact
  computations in some cases. Full text not obtained; unresolved prior-art lead.
  https://doi.org/10.2307/3214044

The audit establishes neither novelty nor prior publication of this reversal.
The probability proof and the historical originality question must be assessed
separately.
