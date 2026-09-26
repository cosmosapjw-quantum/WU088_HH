# R31K-B: exact structure, numerical stability, and scheduling

## Protected model and units

The nonrelativistic two-electron, prescribed straight-line H-H model, 47 neutral plus two fixed ionic channels, frozen107 Hylleraas donor, exponents, complex electron-translational factors and 49-to-25 projection are unchanged. Kernel coordinates use a0 and energy uses Eh. The ETF wave number is q = m_e v_rel / hbar; its numerical atomic-unit value is the stored velocity. The letter v in the radial scalar code denotes a **variance**, not this velocity. Below it is written sigma². The nuclear impact parameter is 2 a0; beta below is a Gaussian exponent, not the impact parameter.

All optimizations are subordinate to the existing source domains and numerical budgets. The underlying frozen special-function implementation has its own asymptotic approximations; caching and parallelism do not turn those into exact integral evaluations.

## 1. Gaussian separation actually implemented

For t_i,u_j>0, alpha,beta>0, define A_i=alpha+t_i, B_j=beta+u_j and R²=(2 a0)²+z². Completing the square in the two-electron Gaussian integral gives the factor

C_ij = (pi/A_i)^(3/2) (pi/B_j)^(3/2)
       exp[-beta*u_j*R²/B_j - q²/(4 B_j) - i*q*z*beta/B_j].

To obtain this expression rather than assume it, put R=(2 a0,0,z) and factor the six-dimensional Gaussian integral as

integral d³x exp[-A_i x²] × integral d³y exp[-beta(y-R)²-u_j y²-iq y_z].

The second exponent is -B_j y²+(2 beta R-iq e_z)^T y-beta R². Applying the convergent Gaussian identity

integral d³y exp[-B y²+b^T y]=(pi/B)^(3/2) exp[b^T b/(4B)], Re B>0,

first for real b and then by analytic continuation for complex b, gives beta²R²/B-beta R²=-beta*u_j R²/B and the two q terms displayed above. The complex square uses transposition, not conjugate transposition. A_i,B_j have dimension length^-2, q has dimension length^-1, the exponent is dimensionless and C_ij has dimension length^6. This does not alter any external donor/weight normalization.

Set p_i=(pi/A_i)^(3/2), r_j=(pi/B_j)^(3/2), e_j=exp[...]. Then C_ij=(p_i*r_j)*e_j. This is separation of existing Gaussian integrals, not a Gaussian fit to the ionic trial state and not removal of the cusp.

The previous packing loop evaluated two real powers and one complex exponential at every i,j. The candidate evaluates 2n powers and n exponentials, instead of 2n² and n². At n=192 this removes 73,344 repeated power evaluations and 36,672 repeated complex exponentials from this packing section. It does not remove the much larger odd-power special-function workload.

The code deliberately keeps `(p_i*r_j)*e_j`, the original multiplication association. On the tested compiler/ABI with round-to-nearest, cached and repeated calls produce exactly equal numerical arrays. This is not a proof of archive-byte identity or cross-platform bitwise reproducibility. Long-double padding bytes and NPZ metadata must not be confused with numerical data.

## 2. Why even powers should remain analytic

For sigma²>0 and integer m>=0, first consider a real Gaussian relative coordinate, then analytically continue its mean delta to complex values. Let s=delta^T delta, **without complex conjugation**. Finite moments are entire polynomials in delta; the generating function below is expanded near lambda=0 (for example |2 sigma² lambda|<1 on its analytic branch). Here lambda has dimension length^-2 and M_m has dimension length^(2m). Its polynomial radial moments are

M_m = E[(r^T r)^m]
    = (2 sigma²)^m Gamma(m+3/2)/Gamma(3/2)
      1F1(-m;3/2;-s/(2 sigma²)).

The first argument is a non-positive integer, so this is a terminating polynomial. Its exponential generating function is

G(lambda)=(1-2 sigma² lambda)^(-3/2)
          exp[s lambda/(1-2 sigma² lambda)].

Differentiating gives

(1-2 sigma² lambda)² G' = [s+3 sigma²-6 sigma⁴ lambda] G.

Comparison of coefficients proves

M_(m+1) = [s+(4m+3)sigma²] M_m
          -2m(2m+1)sigma⁴ M_(m-1),
M_0=1, M_1=s+3 sigma².

For m=0..4 this gives 1; s+3v; s²+10sv+15v²; s³+21s²v+105sv²+105v³; s⁴+36s³v+378s²v²+1260sv³+945v⁴, with v=sigma². Wolfram independently simplified the first three recurrence residuals to zero. The general result follows from the generating function, not from checking finitely many cases.

The frozen `fg_even` implementation already uses this structure. R31K-B preserves it instead of claiming a new optimization or adding gamma integration back to the even sector. The odd r12 powers remain present; no donor coefficient or physical channel is deleted.

## 3. Rejected fast path: one high-order Boys seed in a wide complex strip

F_n(x)=integral_0^1 u^(2n) exp(-x u²) du is entire in complex x.
Integrating the derivative of u^(2n+1) exp(-x u²) proves

2x F_(n+1)=(2n+1)F_n-exp(-x),   dF_n/dx=-F_(n+1).

These are exact identities. However an error in F_m propagated downward obeys

Delta F_0 = [(2x)^m/(2m-1)!!] Delta F_m

before adding roundoff from subsequent operations. At m=9,x=32i the magnitude of this amplification factor is 5.22771303046e8. This makes a one-seed implementation dangerous even though it saves special-function calls.

Actual 80-decimal mpmath comparisons of the frozen independent-seed implementation and an order-9 downward reconstruction gave, at x=32i, absolute F0 errors 1.12289e-20 and 3.86005e-13 respectively. This is a **scalar-domain counterexample**, not a claim that physical H has the latter error. The candidate therefore preserves independent wide-strip seeds and binary128 cancellation control. No precision is silently reduced for SIMD/GPU use.

## 4. Parallel evaluation with the original reduction order

Write an odd-sector component as

I_c = I_even,c + sum_h g_h P_h,c,
P_h,c = CompensatedSum_(i,j,p)[ f_hijp,c ].

Distinct h planes have no shared scientific state. The candidate evaluates each P_h,c and its sumabs in a private buffer. Within a plane, i,j,p,c iteration order is the original order. After all workers finish, the master applies the original compensated summation over h in ascending order. There is no OpenMP floating-point reduction. The only OpenMP reduction computes an integer diagnostic, the observed team size.

Exact-zero weight masks are cached once in canonical i,j order. This repeats the original `weight != 0` decision; it is not magnitude screening. Errors are stored per h, and the first failed h in canonical order is returned before reducing that side. Exceptions do not escape OpenMP regions. The old sidewise output-commit semantics are retained, not relabelled as whole-call transactional behavior.

## 5. Optimal grouping under the existing durability boundary

For N independent pair jobs with known costs c_(1)>=...>=c_(N), P worker slots, and a barrier after each group of at most P jobs, the compute makespan is the sum of group maxima. The j-th largest group maximum is at least c_((j-1)P+1): otherwise the first (j-1)P+1 jobs would need to fit in only j-1 groups of capacity P. Consecutive groups in descending order attain every one of these lower bounds. Thus sorting by descending exact cost minimizes compute time **for this wave/barrier model**.

The implemented scheduler uses measured/predicted costs, not an oracle. Correctness does not depend on a good prediction: the same independent pair files are computed, and assembly uses canonical pair order. Performance does depend on prediction quality, frequency/cache interactions, and service latency. Held-out B160-to-B192 timing-trace simulations are reported as simulations, never actual optimized runtime.

The <=12-new-pair boundary and two-provider ACK fence remain intact. Provider transports run concurrently with each other, but computation never overlaps an unacknowledged wave. This is intentionally narrower than a fully asynchronous rolling task queue; removing that durability barrier requires a separate explicit policy revision.

## 6. Physically motivated future candidate: exact phase separation

For P(t)=diag exp[-i E_a t/hbar], write O=P† O_bar P. Direct differentiation gives

dot O = P† [dot O_bar + i[E,O_bar]/hbar] P,
D = P† D_bar P + P† O_bar dot P.

The known channel phase can therefore be evaluated exactly while interpolating a slower envelope. Omitting the commutator would break the independent metric identity. Wolfram verified the elementwise derivative residual is zero. This candidate is **not deployed**: R31J's interpolation rule is not silently replaced, and no midpoint or trajectory is admitted. Same-z independent dotO, ionic blocks and direct midpoint error evidence remain prerequisites.

## Literature status

SciSpace was used for discovery, not as numerical authority. Fedorov 2017 (arXiv:1702.06784v2, abstract inspected) and Fedorov et al. 2024 (arXiv:2407.17221v1, HTML sections 2–4 inspected) support shifted-Gaussian analytic overlaps, Coulomb integrals and parameter differentiation. Their formulas do not certify this frozen107 two-centre implementation or its wide-complex floating-point domain. The derivations and numerical counterexample above are separately reproducible project work.
