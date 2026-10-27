# Molecular dynamic lift and an exact rational comparison certificate

## Result and scope

For a declared finite state model, the total number X, the state-lift residual r=x-pi X and the error of the scalar coarse equation admit a triangular, nonnegative comparison system. Its coefficients are explicit functions of the supplied generator, destruction vector, formation vector and reference distribution. The accompanying rational step encloses its endpoint for any nonnegative step length.

The finite model is
\[
 \dot x=Kx-hDx+f,\quad D=\operatorname{diag}(d).
\]
Vectors are columns. K has nonnegative off-diagonal entries and zero column sums. On the time interval, coefficients are locally bounded measurable, f>=0 is prescribed and locally integrable, h,d>=0, and x(0)>=0. These assumptions imply a unique absolutely continuous solution and positivity by the finite positive-system variation-of-constants construction. A fixed interval with constant coefficients is the implemented numerical contract. Piecewise intervals may use valid lower damping and upper forcing bounds.

x,f have units cm^-3 and cm^-3 s^-1; K is s^-1, h is cm^-3 and d is cm^3 s^-1. The proper-time variable is seconds unless the caller supplies an explicit nondimensionalization. No physical consumer or GL2022 destruction vector is supplied in this unit. REC's HD source states keep v=UNSPECIFIED and unlisted channels MISSING_NOT_ZERO. Physical uncertainties, energy and photon transport are separate inputs.

## 1. Exact projection, including a moving reference distribution

Let pi(t)>=0, 1^T pi=1 be locally absolutely continuous. Define
\[
 X=1^Tx,\quad Q=I-\pi1^T,\quad r=Qx,\quad
 \bar d=d^T\pi,\quad b=D\pi-\pi\bar d,
\]
\[
 B=\pi d^T-D,\quad L=K+hB,\quad
 c=K\pi-\dot\pi-hb,\quad F=1^Tf .
\]
Then
\[
 \dot X=-h\bar d X-hd^Tr+F,\qquad
 \dot r=Lr+cX+Qf. \tag{1}
\]
Indeed x=pi X+r, 1^TK=0 and differentiating r=x-pi X gives (1) after collecting all terms. Also 1^Tr=1^Tc=1^TQf=0.

For fixed stationary pi, Kpi=0 and piDot=0, c=-hb. This condition is optional in (1), and the implementation retains the full residual c. The matrix B is a mathematical representation of the residual dynamics: its off-diagonal entries are pi_i d_j>=0 and 1^TB=0. Thus L is a Markov generator. No new physical reset event is inserted in x's equation.

For a finite thermal reference with fixed energies and weights,
\[
 \pi_i(T)=\frac{g_i e^{-E_i/(k_BT)}}{\sum_jg_j e^{-E_j/(k_BT)}},
 \qquad
 \dot\pi_i=\pi_i\frac{E_i-\langle E\rangle_\pi}{k_BT^2}\dot T.
\]
This is an explicitly chosen finite ensemble. It does not assert LTE for an actual consumer.

## 2. A computable zero-sum contraction coefficient

For any finite column generator A and n>=2, define
\[
 \delta(A)=\min_{i<j}\left[
 A_{ij}+A_{ji}+\sum_{k\ne i,j}\min(A_{ki},A_{kj})
 \right]. \tag{2}
\]
It is nonnegative, and for 1^Tz=0,
\[
 \|e^{At}z\|_1\le e^{-\delta(A)t}\|z\|_1. \tag{3}
\]

Proof. For sufficiently small epsilon>0, P=I+epsilon A is column stochastic, and the diagonal terms exceed the cross terms in each pair of columns. Decompose any zero-sum z into positive and negative parts of equal mass. Their normalized parts are convex combinations of coordinate probability vectors. The triangle inequality then bounds the induced zero-sum norm of P by half the maximum distance between two columns. Since the columns sum to one, this equals one minus their minimum overlap. Computing that overlap for I+epsilon A gives exactly epsilon times the bracket in (2). Therefore ||Pz||1 <= (1-epsilon delta(A))||z||1. Taking powers with epsilon=t/m and m->infinity proves (3). For time-varying locally bounded A, the same infinitesimal inequality and Gronwall give the propagator bound with exp(-integral delta(A)).

The stochastic-matrix identity used here is the established Doeblin-Dobrushin formula, reviewed in Gaubert and Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, IEOT81 (2015),127-150, Introduction eqs(1),(2), DOI10.1007/s00020-014-2193-2. Their row convention is transposed here:
https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf

For B,
\[
 \delta(B)=\min_{i<j}\left[
 \pi_i d_j+\pi_jd_i+(1-\pi_i-\pi_j)\min(d_i,d_j)
 \right]\ge d_{\min}. \tag{4}
\]
The direct choice a=delta(L) preserves overlap between K and hB. A bound alpha for K can be added only if it is a prefactor-one L1 zero-sum contraction bound. A spectral gap in another norm is not such an alpha without a justified norm transport.

For d->d+c0*1 with c0>=0, b and osc(d) are unchanged, while L on the zero-sum subspace gains -h*c0*I. Formula(2) also gives delta(L_new)=delta(L_old)+h*c0: every pairwise overlap gains h*c0 sum(pi). This preserves common destruction damping.

A connected sparse graph can have delta(K)=0. This is the one-step coefficient's actual value, not a claim that the finite graph fails to mix. The bound (3) remains valid with that value.

## 3. Triangular continuous comparison theorem

Define
\[
 k=hd_{\min},\quad a=\delta(L),\quad q=\|c\|_1,\quad
 g=\|Qf\|_1,\quad b_0=h\bar d,\quad s=\frac h2\operatorname{osc}(d).
\]
Let the scalar coarse equation share the same prescribed F:
\[
 \dot{\bar X}=-b_0\bar X+F.
\]
Choose nonnegative initial bounds M(0)>=X(0), U(0)>=||r(0)||1 and E(0)>=|X(0)-Xbar(0)|. Solve
\[
 \boxed{
 \begin{aligned}
 \dot M&=-kM+F,\\
 \dot U&=-aU+qM+g,\\
 \dot E&=-b_0E+sU .
 \end{aligned}} \tag{5}
\]
Then, throughout the common interval,
\[
 0\le X\le M,\qquad \|r\|_1\le U,\qquad |X-\bar X|\le E. \tag{6}
\]

Proof. Positivity gives d^Tx>=dmin X, hence X'<=-kX+F. Scalar comparison yields X<=M. The forcing cX+Qf in (1) has zero sum and norm at most qX+g. Variation of constants and (3), or the upper Dini derivative inequality, yield D^+||r||1<=-a||r||1+qX+g. Substitute X<=M and compare to U.

For e=X-Xbar, e'=-b0 e-hd^Tr. The accepted R4 zero-sum estimate follows by subtracting the midpoint of d's range from every component:
|d^Tr|<=osc(d)||r||1/2. Hence D^+|e|<=-b0|e|+sU, giving E. This completes the proof. An f that depends on x needs a separate bound for that dependence; the stated shared prescribed-source assumption cannot be discarded.

For fixed stationary pi, q=h beta with beta=||Dpi-pi dbar||1. The inequality beta<=osc(d)/2 is a useful optional scalar bound; the code uses the actual norm and does not replace it by a worse estimate.

All formulas hold with zero damping, using the integral representation rather than division by a rate. For n=1, r=0 and the code chooses delta=0 for the trivial zero-sum subspace.

## 4. Exact rational endpoint and interval enclosures

On a constant-coefficient interval of duration Delta>=0, suppose nonnegative M,U,E already enclose the comparison solution at its start. Define
\[
 M_* = M+F\Delta,\quad C=qM_*+g,\quad U_*=U+C\Delta,\quad
 E_*=E+sU_*\Delta .
\]
The whole interval is bounded by (M_*,U_*,E_*), and the endpoint is bounded by
\[
 \boxed{
 M_+=\frac{M}{1+k\Delta}+F\Delta,\quad
 U_+=\frac{U}{1+a\Delta}+C\Delta,\quad
 E_+=\frac{E}{1+b_0\Delta}+sU_*\Delta.} \tag{7}
\]

Proof. Dropping each nonpositive damping term bounds M(t) by M+Ft, then U(t) by U+Ct, then E(t) by E+sU_*t. For the endpoint, apply variation of constants and
e^{-z}<=1/(1+z) for z>=0 and integral_0^Delta e^{-a u}du<=Delta. All coefficients multiplying earlier bounds are nonnegative, so an existing overestimate remains an overestimate. Iterating (7) gives certified endpoints of (5), then (6). Endpoint values are not necessarily whole-interval bounds: a decaying M_+ can be smaller than M. The returned interval object therefore uses starred quantities.

Expansion at Delta=0 gives the right derivative of (5) and local error O(Delta^2) for fixed finite coefficients. Thus on finite intervals the method is first-order consistent and convergent. Arithmetic is exact rational; displayed decimals are approximations and are not themselves outward interval endpoints.

For variable coefficients on a segment, the same comparison construction uses certified *lower* bounds on k,a,b0 and *upper* bounds on F,q,g,s. A point sample is not an interval certificate. The general moving-pi identity remains available even when such interval bounds have not yet been supplied.

## 5. Exact limits and a nonzero closure example

If h=0, or d is constant, s=0 and same initial total gives E=0. For constant d, beta=0 as well. Having r(0)=0 and Qf=0 alone is insufficient to preserve the lifted distribution: heterogeneous destruction produces the term -hbX. The exact invariance condition is cX+Qf=0 along the trajectory; c=0 and Qf=0 suffice.

A dimensionless mathematical fixture is
\[
 K=\begin{pmatrix}-1&2\\1&-2\end{pmatrix},\
 \pi=(2/3,1/3)^T,\ d=(1,4)^T,\ h=1,\ x(0)=\pi .
\]
Then k=1,a=6,q=4/3,b0=2,s=3/2. Write r=(z,-z). With f=0,
\[
 X=e^{-4t}\left[\cosh(\sqrt6t)+\frac2{\sqrt6}\sinh(\sqrt6t)\right],
 \quad z=e^{-4t}\frac2{3\sqrt6}\sinh(\sqrt6t),\quad \bar X=e^{-2t},
\]
\[
 M=e^{-t},\quad U=\frac4{15}(e^{-t}-e^{-6t}),\quad
 E=\frac25\left[e^{-t}-\frac54e^{-2t}+\frac14e^{-6t}\right].
\]
With f=(1,0), g=2/3 and F=1, M=1,
\[
 U=(1-e^{-6t})/3,\qquad E=1/4-(3/8)e^{-2t}+(1/8)e^{-6t}.
\]
Its full steady state is (3/5,1/10), so the total error tends to1/5 while E tends to1/4. These are mathematical verification fixtures, not measured HD destruction rates.

## 6. Connection to the reused HD input

The REC adapter source binds nine J-labelled HD states and nine downward pairs per H2 collider at 50/100/200K. Reuse its source and normalization identities. A new supplied-edge generator may be assembled from those named channels and explicitly declared inverse-rate rules, keeping other channels unrepresented. The source does not supply the GL2022 destruction vector d, a consumer pi/x/h/f, chemical Q or complete state coverage outside its finite set.

The new source-conditioned diagnostic uses one native node,100K/para-H2, and records its rational approximation to conditional thermal weights. It evaluates the generator representation and norm geometry, not a physical trajectory or an observed relaxation time. Because pi need not be exact stationary data, the general coefficient c retains Kpi-piDot whenever present. Number-source and energy-source admission remain separate.

## 7. Implementation correspondence and evidence

Equations(1)-(4) map to coefficients, projectedState and contractionRate in src/dynamic_lift.mjs. Equations(5)-(7) map to initialBounds, envelopeStep and envelope. generatorFromEdges constructs the declared graph from explicit directed nonnegative rate records and rejects duplicate edges.

See checkpoints and results for actual executions, reviews and source hashes. The proof is independent of a particular sample count. No new strong no-go or field-wide novelty claim is made; the contribution to this project is the dynamic comparison and its exact-rational implementation.
