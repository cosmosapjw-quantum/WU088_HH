# Constructive choice of a finite-block certificate

We use the exact R5 projection variables and choose a finite positive lower polynomial for the full Markov reset generator A. This retains the source graph and makes the forcing convolution computable with only nonnegative operations. The partial sum has a mathematical lower-bound meaning even if it is coarse.

## A three-state calculation that distinguishes the alternatives

Consider the declared column generator

\[
A=\begin{pmatrix}-1&0&0\\1&-1&0\\0&1&0\end{pmatrix},
\qquad P=I+A.
\]

The instantaneous Dobrushin lower coefficient is zero. However, \(P^2\) sends every coordinate basis vector to the third state. The degree-two lower propagator is

\[
R_2(H)=e^{-H}\left(I+HP+\frac{H^2}{2}P^2\right),
\quad \beta_2(H)=\frac{H^2}{2}e^{-H}>0\quad(H>0).
\]

Thus a finite block contracts on the zero-sum space. The exact propagator gives

\[
\|e^{tA}(e_1-e_3)\|_1=2e^{-t}(1+t),
\]

whose initial decay slope is zero. This explicit control separates a finite block statement from a prefactor-one positive instantaneous gap. It is a familiar finite-chain calculation, used here as a method control.

## Method decision

The instantaneous coefficient remains useful when its lower bound is positive. The R5 single padded path supplies one nonnegative term and remains valid historical evidence. The R6 partial polynomial accumulates all retained matrix-power paths and can improve overlap without a new physical closure. Directed downward matrix multiplication, Poisson weights and term accumulation preserve the same order relation. The omitted terms are nonnegative, so no uncomputed tail can invalidate the lower bound.

For time-dependent coefficients, one common Pminus and one full-generator exit bound are required throughout every certified block. Ordered products are bounded below termwise; a remainder interval is merely nonexpansive. The forced response retains this remainder and integrates the age-dependent kernel. The selected implementation stores a conservative rational bound with factor rho/(1+kappa H), plus a separate whole-block envelope for the aggregate error integral.

The code fixture and independent Wolfram check will exercise the distinguishing identities within the fixed new allowance. No previous source calculation is rerun for this choice.
