# NEW_THEOREM_REVIEW — bounded endpoint and enclosure review

This reviews only the new companion theorems, not the closed producer preflight or 19-source audit. Inspected remote HEAD/tree: `a5947d79be0234494873b7201233ac9da4b233da` / `f934cc2e0db7d31b4e5275266ab6d56627f79ad0`; no successor. Source-review RETURN blob: `d1cbf14325d1ad40fb83ab636e042c47343e6cce`. Companion SHA256: `199526b5ed88d722b4f7eac10d00a4466ad6bfe55dbfe3c061a91994c0aa0c5a`. Its REPORT_KO.md, RESULT.json, CERTIFICATE_DESIGN.json and CODEX_HANDOFF_KO.md were read. The companion's semantic extract does not replace canonical source/input/raw bytes.

## Verdict and fixed premises

The algebraic and analytic implications A–E and the end-to-end/Gram formulas are **accepted under the specified premises**. No theorem formula requires correction. Numerical enclosure feasibility is untested. A callback conjugation clarification is required below; it does not invalidate the O/G theorem.

Premises: mu>0 (the source uses exact mu=1); positive real Gaussian a,b; nonnegative integer degrees i,j,k in the finite donor range; real centers and wave numbers; real stored pref, coefficients, phase energies and nonzero real v; fixed z=3/4, transverse displacement 2 and tau=z/v. All input numbers are exact lifts of the same stored Frozen107 bits. Coefficients, normalization formula, phase, active/cusp/parity/adjoint semantics are unchanged. The stored pref is not recomputed from the donor certificate. These statements concern the finite source-defined continuous model, not complete-HH physical adequacy.

## A — finite signed Hermite envelope: ACCEPT

Substitute the physicists' finite expansion of H_(i+1) into the unweighted density U_i. With lambda=mu^2/4,

\[
U_i(t)=e^{-\lambda/t}\sum_{r=0}^{\lfloor(i+1)/2\rfloor}(-1)^r A_{ir}t^{-\nu_{ir}},
\quad A_{ir}=\frac{(i+1)!\mu^{i+1-2r}}{\sqrt\pi\,2^{i+1}r!(i+1-2r)!},
\quad\nu_{ir}=i+3/2-r.
\]

The factor 2^(i+1) follows by combining the Hermite powers with (2sqrt(t))^(-i-1), rather than an additional factorial convention. A_ir>0; all allowed nu>1. Triangle inequality gives the finite monomial envelope. This does not make signed U_i or contracted W positive. Weighted U/W already contain the original Jacobians/base quadrature weights. See [DLMF Hermite expansion](https://dlmf.nist.gov/18.5.E13).

Remaining premise: actual outward evaluation of these symbolic constants and their use in the same input/domain. None is evaluated here.

## B — real Gaussian O/G majorant and pz derivative: ACCEPT

For t,u>0 write A=a+t, B=b+u and translate by real means ad1/A,bd2/B. The attenuation factors are <=1 and the real-wave-number phase has modulus one. Writing s=|y1|,w=|y2|,D1=|d1|,D2=|d2| bounds |r1-d1|<=s+D1, |r2-d2|<=w+D2 and |r1-r2|<=s+w+D1+D2. The companion's nonnegative polynomials P_O,P_G1,P_G2 therefore bound the respective spatial integrands.

In particular,

\[
-\partial_{d_z}[(r_z-d_z)e^{-a|r-d|^2}]
=[1-2a(r_z-d_z)^2]e^{-a|r-d|^2}.
\]

Thus P_G1 retains the pz delta term; p_x has no such polynomial derivative. G2 differentiates the second Gaussian only. The six-dimensional moments factor, and

\[
\int_{\mathbb R^3}|y|^r e^{-A|y|^2}dy
=2\pi\Gamma((r+3)/2)A^{-(r+3)/2}.
\]

Factoring A^(-3/2)B^(-3/2) and using A>=a,B>=b yields precisely C_F=L_(a,b)[P_F] and |I_F|<=C_F/[(a+t)^(3/2)(b+u)^(3/2)]. Compact real-center neighborhoods give common D1,D2 bounds. With A's finite absolute density integrals this provides absolute domination and the first center-derivative interchange for both spatial and Laplace integrals. No numerical size or practicality of C_F is established.

## C — lower/upper endpoints and rectangle complement: ACCEPT

For Phi_i^a=e^(-lambda/t) sum A_ir t^(-nu_ir)/(a+t)^(3/2), bound the denominator by a^(-3/2) at the lower endpoint. Substitution y=lambda/t gives the upper incomplete gamma factor lambda^(1-nu) Gamma(nu-1,lambda/l). At the upper endpoint bound exp<=1 and (a+t)^(-3/2)<=t^(-3/2); integration gives T^(-nu-1/2)/(nu+1/2). The weakest exponent is **T^(-2)**, an endpoint envelope exponent, not quadrature order or p_cond. [Incomplete gamma definitions](https://dlmf.nist.gov/8.2.E2) fix the upper/lower convention.

Whole-domain W and interior J follow from the same substitution; J uses Gamma(nu-1,lambda/T)-Gamma(nu-1,lambda/l), which is nonnegative mathematically. The complement partition (E_t x all_u) disjoint-union (I_t x E_u) gives C_F[S_i W_j+J_i S_j]; corners enter once. Finite coefficient/normalization/orbital absolute-value contractions propagate these bounds without changing the signed source.

Remaining premises: certified evaluation and outward summation, explicit finite endpoints, cancellation-safe gamma differences and certified final entry radii. These remain unevaluated.

## D — joint holomorphy, product ellipses and Chebyshev remainder: ACCEPT WITH DOMAIN CONTRACT

For a compact subset of Re(t),Re(u)>0, the absolute value of the electron integrand is dominated by the real Gaussian integrand with t,u replaced by their real parts. Parameter derivatives insert finite powers of spatial coordinates and preserve Gaussian domination. Integration therefore gives a jointly holomorphic O/G primitive. Principal powers in U_i are holomorphic there. Also Re(a+t),Re(b+u)>0 implies Re(1/(a+t)),Re(1/(b+u))>0, so Re(sigma)>0 for sigma=(1/(a+t)+1/(b+u))/2. This controls the radial powers and nonzero denominators. Unregularized 1F1 is entire in its argument at the fixed positive half-integer denominator parameters.

For [l,T], the ellipse's leftmost real part is (T+l)/2-(T-l)(rho+rho^(-1))/4. Requiring it positive yields

\[
1<\rho<\frac{\sqrt T+\sqrt l}{\sqrt T-\sqrt l}.
\]

Require a positive margin on a neighborhood of each closed ellipse. The real Gaussian bound extends with Re(t),Re(u); |exp(-lambda/t)|<=1 and |t|>=r_min>0 give the stated product-ellipse magnitude M. No global ellipse through 0/infinity is claimed.

Two Cauchy/Chebyshev coefficient bounds yield |c_mn|<=4M rho_t^(-m)rho_u^(-n), conservatively including zero indices. Summing the union m>p or n>q gives the companion's inclusion–exclusion tail exactly. Enclosed coefficient radii must be added once; sampled fits need their own interpolation/aliasing enclosure. The distinction between exact-series and sampled interpolants matters. See [Trefethen's coefficient-bound exposition](https://www.chebfun.org/examples/approx/EntireBound.html).

**Callback clarification:** literal conj(f(t,u)) is antiholomorphic. Integrate/enclose O,G1,G2 over real positive t,u first and perform D_row conjugation afterwards. A future direct complex-domain row callback would require reflected continuation f#(t,u)=conj(f(conj(t),conj(u))) with separately verified target equality. The preferred plan uses post-integral assembly and does not require that extra callback.

## E — restricted original rule and moment defect: ACCEPT

Let Q be a finite positive base measure, partitioned into inside/outside the same rectangle. Adding/subtracting P on the interior and bounding f-P by delta gives

\[
|If-Qf|\le B_{integral,out}+B_{quadrature,out}
+(area(\Omega)+Q_\Omega1)\delta+|I_\Omega P-Q_\Omega P|.
\]

Q_out needs an actual-node finite sum, not the endpoint integral formula. Q positivity is about the base measure; signed donor densities remain inside f. Restricting original GL nodes does not produce an interior GL rule. The exact two-point counterexample defect (3-2sqrt(3))/24 is nonzero despite vanishing fourth derivative. Affine Chebyshev moments are width/(1-m^2) for even m and zero for odd m. No actual OD measure moment is evaluated here.

Remaining authority: actual OD t/u node and positive transformed base-weight bytes, units, tensor ordering and generation-time identity. Neither a JVP frozen grid nor regenerated nodes supplies that authority by itself. This optional route remains blocked on inspected evidence; the primary continuous-target route does not depend on it.

## End-to-end epsilon and Gram eta: ACCEPT, NUMERICAL PREMISES OPEN

If final target entries satisfy |D*_ab-c_ab|<=r_ab, then the archived raw difference has spectral norm at most sqrt(sum_ab (|D192_ab-c_ab|+r_ab)^2), with outward arithmetic. This includes the producer's entire discrepancy. Preserve the old X0..X8 decomposition as a forensic alternative; do not add it to this bound. Final D balls avoid ambiguous double charging of phase/normalization/assembly error. Conditional O/G-to-D propagation in the companion is also correct.

For an exact represented 47x2 error matrix, exact dyadic Gram entries a,d,b give largest eigenvalue (a+d+sqrt((a-d)^2+4|b|^2))/2. The norm is its positive square root; 2x47 uses its adjoint. Certified root intervals yield gap intervals, and eta>=max(|ghat-g_minus|,|ghat-g_plus|) covers discrepancy from the fixed published gap. Dmax needs interval max bounds; it does not need to guess the active block. No raw norms or certificates are evaluated now. Exact decoding, serialization and separate machine-predicate boundary semantics are mandatory.

## Review status and stop

A fresh bounded verifier confirmed the mathematical implications, with the row-callback clarification above. This is not the project's admitted independent final decision review. Companion Wolfram warnings/results and its 36 synthetic assertions are preserved as prior evidence; none is rerun or aggregated with historical tests.

certified_epsilon=null; certified_eta=null; rigorous=false. SOURCE_ACCURACY_BOUND_UNAVAILABLE and RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND remain. The eta=0 common strict budget 0.02856621001324109/t_a is not an acquired epsilon. Source/physical/production gates, frozen R31AK and z075 holdout role are preserved. Stop after A/B/C documents, bounded artifact verification and publication/backup. No numerical authorization scope is issued.
