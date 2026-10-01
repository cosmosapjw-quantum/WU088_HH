# T1 — explicit complex-domain bounds for the source O/G route

The compact-domain and Cauchy implications below are proved under the listed symbolic premises. They do not evaluate a Frozen107 parameter, a source integral, a native callback or a certificate. Earlier accepted density algebra, radial continuation and real endpoint theorems are retained. This document supplies the explicit constants that were implicit in their compact-domination statements.

## 1. Fixed premises and source binding

Let `a,b,mu>0` be real, let `d1,d2 in R^3` and `q1,q2 in R`, and let `i,j,k` be nonnegative integers in a finite donor set. Write `lambda=mu^2/4`. The source has degrees at most eight, but finiteness is enough for the theorem. All coefficients, exponents, normalizations and phase data denote exact lifts of the selected stored inputs; no coefficient or stored prefactor is recomputed here. For effective constants, these inputs must be computable with certified positive lower bounds on positive quantities. Exact rational/dyadic inputs satisfy that condition.

The source primitive is

\[
I_O(t,u)=\int_{\mathbb R^6}|r_1-r_2|^k P_\ell(r_1-d_1)
 e^{-a|r_1-d_1|^2-b|r_2-d_2|^2-t|r_1|^2-u|r_2|^2
 +iq_1r_{1z}+iq_2r_{2z}}\,dr_1dr_2,
\]

where `P_s=1`, `P_px=(r1-d1)_x`, `P_pz=(r1-d1)_z`. Define `I_G1=-partial_d1z I_O`, `I_G2=-partial_d2z I_O`, with q fixed, and `f_F=U_i(t)U_j(u)I_F(t,u)`. These are the unweighted continuous integrands: transformed quadrature weights/Jacobians are not multiplied into f again.

The source definitions are pinned by `SOURCE_FUNCTIONAL_MAP.md`, `NEW_THEOREM_REVIEW.md` and G1-01 through G1-11 in `THEOREM_CLOSURE.md`. Exact source bytes reread here are `h0_fused.cpp` (geometry, bilinear s, negative center derivatives), `exact_laplace_weights.py` (signed UU densities), and `od_run.py` (finite coefficients, phase, physical-domain conjugation). Their hashes are recorded in the companion JSON. No source module was imported or executed.

## 2. Rectangle margins without interval dependency

Let

\[
T=[x_-,x_+]+i[y_-,y_+],\quad
V=[v_-,v_+]+i[w_-,w_+]
\]

be finite closed rectangles, possibly degenerate, with ordered real endpoints. Put

\[
\alpha=a+x_->0,\quad X=a+x_+,\quad Y=\max(|y_-|,|y_+|),\quad Q_A=X^2+Y^2;
\]

define `beta=b+v_->0`, `Vmax=b+v_+`, `W=max(|w_-|,|w_+|)` and `Q_B=Vmax^2+W^2` analogously. For every `(t,u) in T x V`, set

\[
A=a+t,\quad B=b+u,\quad \sigma=\tfrac12(A^{-1}+B^{-1}),
\quad s_0=\tfrac12(\alpha/Q_A+\beta/Q_B),
\quad s_1=\tfrac12(\alpha^{-1}+\beta^{-1}).
\]

Then

\[
\alpha\le|A|\le\sqrt{Q_A},\quad
Q_A^{-1/2}\le|A^{-1}|\le\alpha^{-1},\quad
\Re(A^{-1})\ge\alpha/Q_A>0,
\]

and the same bounds hold for B. Indeed `Re(1/A)=Re(A)/|A|^2`. Consequently

\[
\Re\sigma\ge s_0>0,\qquad s_0\le|\sigma|\le s_1,
\qquad s_1^{-1}\le|\sigma^{-1}|\le s_0^{-1},
\qquad \Re(\sigma^{-1})\ge s_0/s_1^2>0. \tag{2.1}
\]

All displayed real-part margins are rational expressions when the input data and box endpoints are rational. They are inequalities for the exact correlated image, independent of how a sequence of interval operations encloses it. Optional sharper bounds are

\[
\Re(A^{-1})\ge\min\!\left\{
\frac{\alpha}{\alpha^2+Y^2},\frac{X}{X^2+Y^2}\right\},\qquad
|\sigma|\ge\frac{\alpha+\beta}{2\sqrt{Q_AQ_B}}.
\]

For the first, minimize over `|Im A|<=Y`, then note that `x/(x^2+Y^2)` has no interior minimum on `[alpha,X]`. For the second use `sigma=(A+B)/(2AB)` and `|A+B|>=alpha+beta`.

The principal logarithms of A, B, sigma are holomorphic on an open neighborhood of this compact product. For a real exponent p and `0<L<=|z|<=U`,

\[
|z^p|\le\begin{cases}U^p&p\ge0,\\ L^p&p<0,\end{cases}
\]

with the reverse endpoint providing a modulus lower bound. Thus every fixed half-integer power and inverse in the source radial expression has an explicit finite bound. This does **not** assert that powers have positive real parts. For example `Re((1+2i)^(3/2))<0`.

The geometry also has explicit finite bounds. With `D_j>=|d_j|`,

\[
|m_1|\le(aD_1+|q_1|/2)/\alpha=:H_1,\quad
|m_2|\le(bD_2+|q_2|/2)/\beta=:H_2,
\]

\[
|s|=|(m_1-m_2)\cdot(m_1-m_2)|\le(H_1+H_2)^2,
\quad |s/(2\sigma)|\le(H_1+H_2)^2/(2s_0).
\]

Norms in these inequalities are Hermitian Euclidean bounds, but the **definition** of s remains the source bilinear dot product. Replacing that definition by a Hermitian norm changes the target and destroys holomorphy. The unregularized 1F1 denominator parameters `3/2,5/2,7/2` do not encounter poles; its global entire-function theorem remains the already accepted G1-03/G1-04 statement.

### Safe use of an independently proved image bound

Suppose a computed outward rectangle `R_raw` encloses every exact sigma image but crosses zero or the negative real axis. The valid repair is the set intersection

\[
R_{\rm raw}\ \cap\ \bigl([s_0,s_1]+i[-s_1,s_1]\bigr). \tag{2.2}
\]

Both sets contain the exact image by independent proofs; hence so does their intersection. One may use certified rational lower/upper approximations to s0,s1 that preserve the containing rectangle. An empty intersection signals inconsistent premises/evidence and must be rejected. Convert the intersection outward to the working ball/rectangle and verify that rounding still leaves a strictly positive real lower bound before calling an operation that requires a branch-safe input ball. A representable margin such as `s0/2>0` is eventually retained at sufficiently high precision because the true interval has a positive margin. The direct proof is **not** permission to pass the old branch-crossing rectangle unchanged to `pow`, or to clamp a midpoint or discard parts of an enclosure without the independent set-inclusion proof. The same intersection construction applies to A and B if their arithmetic enclosures overestimate the known rectangle.

## 3. Signed density bounds and the separate t/u branch condition

The accepted finite expansion is

\[
U_i(t)=e^{-\lambda/t}\sum_{r=0}^{\lfloor(i+1)/2\rfloor}(-1)^r A_{ir}t^{-\nu_{ir}},
\quad
A_{ir}=\frac{(i+1)!\mu^{i+1-2r}}{\sqrt\pi\,2^{i+1}r!(i+1-2r)!}>0,
\quad \nu_{ir}=i+\tfrac32-r>1. \tag{3.1}
\]

The density requires the principal slit domain `t notin (-infinity,0]`; positivity of Re A alone does not guarantee this. A rectangle avoids this cut exactly when `x_->0` or `y_->0` or `y_+<0`. Require that condition separately for T and V. If `d(0,[c,d])` denotes `max(c,-d,0)` for ordered endpoints, then

\[
\tau_T^2=d(0,[x_-,x_+])^2+d(0,[y_-,y_+])^2>0.
\]

Since `|t|>=tau_T` and `Re(1/t)=Re(t)/|t|^2`,

\[
E_i(T):=\exp\!\left(\frac{\lambda\max(0,-x_-)}{\tau_T^2}\right)
\sum_r A_{ir}\tau_T^{-\nu_{ir}}
\quad\Longrightarrow\quad |U_i(t)|\le E_i(T). \tag{3.2}
\]

For the selected positive-halfplane route `x_->0`, an often smaller bound is

\[
E_i^+(T)=e^{-\lambda x_-/Q_T}\sum_r A_{ir}x_-^{-\nu_{ir}},
\qquad Q_T=x_+^2+Y^2, \tag{3.3}
\]

because `Re(1/t)>=x_-/Q_T`. The exponential may be replaced by 1 for a simpler certified upper bound. A sum of the absolute monomial bounds does not change signed U_i into a positive measure; cancellation has only been discarded for the inequality.

## 4. Explicit source-domain Gaussian polynomial majorant

This derivation stays on `r1,r2 in R^3`. There is no complex contour translation of the nonanalytic spatial factor `|r1-r2|^k`.

For a particular `x=Re t`, complete the **real** Gaussian square with `A_R=a+x>0`:

\[
-a|r-d|^2-x|r|^2
=-A_R|r-ad/A_R|^2-\frac{ax}{a+x}|d|^2. \tag{4.1}
\]

Let

\[
h_a=a/\alpha,\quad
\kappa_a=\max\{|x_-/(a+x_-)|,|x_+/(a+x_+)|\},
\quad Z_a=\exp[a\max(0,-x_-)D_1^2/\alpha],
\]

and define `h_b,kappa_b,Z_b` analogously. The function `x/(a+x)` is increasing on `x>-a`; hence its absolute value has its maximum at an endpoint. The attenuation in (4.1) is at most Za. After setting `Xr=sqrt(A_R)|r1-ad1/A_R|`, `Yr=sqrt(B_R)|r2-bd2/B_R|`, write the nonnegative polynomials

\[
L_1=\kappa_aD_1+X_r/\sqrt\alpha,\quad
L_2=\kappa_bD_2+Y_r/\sqrt\beta,
\quad R=h_aD_1+h_bD_2+X_r/\sqrt\alpha+Y_r/\sqrt\beta.
\]

They bound `|r1-d1|`, `|r2-d2|` and `|r1-r2|`, respectively. Put `P=1` for s and `P=L1` for px or pz, and let `e_pz` be 1 only in the pz channel. Then

\[
\mathcal P_O=R^kP,\qquad
\mathcal P_{G1}=R^k(2aL_1P+e_{pz}),\qquad
\mathcal P_{G2}=R^k(2bL_2P). \tag{4.2}
\]

For G1 the derivative of `P_pz` contributes the `+1` absolute bound; it is absent for px and s. Explicitly `-partial_dz[(r_z-d_z)e^{-a|r-d|^2}]=[1-2a(r_z-d_z)^2]e^{-a|r-d|^2}`. G2 differentiates only the second Gaussian. No derivative of q, phase data or `|r1-r2|^k` is introduced by these fixed-q center derivatives.

For a nonnegative finite polynomial `P(Xr,Yr)=sum p_mn Xr^m Yr^n`, define the completely explicit moment functional

\[
\mathcal L[P]=\sum_{m,n}p_{mn}J_mJ_n,\qquad
J_n=\int_{\mathbb R^3}|x|^ne^{-|x|^2}dx=2\pi\Gamma((n+3)/2),
\]

\[
J_{2h}=\pi^{3/2}(2h+1)!!/2^h,\qquad J_{2h+1}=2\pi(h+1)!.
\]

All sums are finite. From the Jacobian and (4.1)–(4.2), uniformly on `T x V`,

\[
|I_F(t,u)|\le Z_aZ_b\alpha^{-3/2}\beta^{-3/2}\mathcal L[\mathcal P_F]=:B_F(T,V). \tag{4.3}
\]

The spatial phases `exp(iq_j r_jz)` have modulus 1 because both q and the integration coordinates are real. Imaginary parts of t,u likewise contribute pure phases before completion. This accounts for **all** such complex phases without asserting that factors of the analytically completed-square formula separately have modulus at most 1.

On the preferred domain `x_-,v_->0`, one may instead reuse the simpler accepted polynomial: `Za=Zb=1`, `L1=D1+Xr/sqrt(a)`, `L2=D2+Yr/sqrt(b)`, `R=L1+L2`. Keep the stronger Jacobian bound `alpha^(-3/2)beta^(-3/2)`. Thus, if `C_F=mathcal L[mathcal P_F]` uses those simpler polynomials,

\[
M_{F,ijk}(T,V)=E_i^+(T)E_j^+(V)
\frac{C_F}{\alpha^{3/2}\beta^{3/2}} \tag{4.4}
\]

is a finite explicit bound for `|f_F|`. On the larger cut-avoiding domain use `E_i(T)E_j(V)B_F(T,V)` instead. The two versions are alternatives; their attenuation/Jacobian factors are not counted twice.

## 5. Fixed domination, holomorphy and finite source contractions

Uniform integrated bounds alone are not being used as a substitute for a pointwise dominating function. On the same rectangle, Young's inequality gives the fixed bound

\[
-a|r-d|^2-\Re(t)|r|^2
\le-\tfrac\alpha2|r|^2+\frac{2a^2D_1^2}{\alpha}. \tag{5.1}
\]

Indeed expand the left side, use `Re(t)+a>=alpha`, discard the nonpositive `-a|d|^2`, and apply `2aD1|r|<=alpha|r|^2/2+2a^2D1^2/alpha`. The same holds for the second electron. Multiplying the resulting fixed decaying Gaussians by the finite polynomials in `|r1|+D1`, `|r2|+D2`, `|r1|+|r2|` bounds O/G pointwise. Any fixed number of t/u derivatives inserts only powers `|r1|^(2m)|r2|^(2n)`, which still have finite Gaussian moments. On a slightly enlarged compact neighborhood the positive alpha,beta and cut distances remain positive. Dominated differentiation therefore gives joint holomorphy of I_F there, and multiplication by the finite holomorphic densities gives joint holomorphy of f_F. This also proves the uniform-parameter version for any compact family with common certified positive a,b/domain margins and finite real-center bounds. Holomorphy in a complexified center or a complexified q is not asserted by the unit-phase argument.

For a finite primitive/donor/orbital sum `F(t,u)=sum_n w_n f_n(t,u)`,

\[
M_F=\sum_n|w_n|M_n \tag{5.2}
\]

is explicit and finite. Here w includes the unchanged donor C, orbital coefficients and `N_l(a,b)=sqrt(2)*pref*(2a/pi)^(3/4)*(2b/pi)^(3/4)` with the source p-channel factor `2sqrt(a)`. Signed parity is a modulus isometry. The assembly phase `exp(i[2kc*cz+(EN-EI)*tau])`, `tau=(3/4)/v`, has modulus 1 under real finite phase data and real `v!=0`. Do not replace tau by a rounded quotient or stored pref by a new normalization.

After integration over positive real t,u and phase/row assembly, source-prescribed conjugation preserves modulus bounds. It is not inserted into f. For example the same finite contraction constants give

\[
M_{Dcol}\le |k_c|(M_{G1}+M_{G2})
 +|k_c(2k_c-k_a-k_b)-E_I|M_O,
\]

\[
B_{Drow}\le |k_a|B_{G1}+|k_b|B_{G2}+|E_N|B_O
\]

for suitable integrated O/G bounds B in the second formula. Drow is a **post-integral** bound, not a claimed holomorphic callback involving literal conjugation. No new row continuation is required.

## 6. Dyadic extended rectangles and Cauchy bounds

Let the real integration rectangle be `[l_t,T_t] x [l_u,T_u]`, with exact finite endpoints `0<l_t<T_t`, `0<l_u<T_u`. Choose explicit dyadic radii

\[
\delta_t=2^{-n_t}\le l_t/4,\qquad
\delta_u=2^{-n_u}\le l_u/4,
\]

where `n_j` is the first nonnegative integer satisfying the inequality. A finite search exists for certified positive rational l_j. Define

\[
K_t=[l_t-\delta_t,T_t+\delta_t]+i[-\delta_t,\delta_t],
\quad K_u=[l_u-\delta_u,T_u+\delta_u]+i[-\delta_u,\delta_u].
\]

Their positive left margins, alpha/beta, s0, density envelopes and `M` follow by the preceding formulas. The polydisc of radii delta_t,delta_u centered at every point of the original real rectangle is contained in `K_t x K_u`. The function is holomorphic on an open neighborhood of that closed product. Therefore the iterated Cauchy formula yields, for all nonnegative integers m,n,

\[
|\partial_t^m\partial_u^n F(t,u)|\le
\frac{m!n!M}{\delta_t^m\delta_u^n}. \tag{6.1}
\]

In particular `L_t=M/delta_t`, `L_u=M/delta_u` are uniform first-derivative bounds for the constructive interior theorem. Any certified rational `Mhat>=M` may replace M. Formula (4.4), finite polynomial expansion, integer/half-integer moment formulas and elementary exp/root/pi operations show exactly which constants must be enclosed; they do not assume an oracle for an unbounded spatial integral.

For an outer compact complex parameter rectangle P, enlarge its real/imaginary endpoints by the desired Cauchy radius, prove that the enlarged product remains in the same admissible domain, and use its M uniformly. One must bound the whole parameter box, not only its midpoint. With `H(t)=integral_[l_u,T_u] F(t,u)du`, the same reasoning gives `|H|<=(T_u-l_u)M` and `|H^(m)|<=(T_u-l_u)m!M/delta_t^m` whenever the corresponding t-polydiscs are covered. Parameter-image width need not approach zero under inner quadrature refinement.

## 7. Limits of the claim and corrected possible overreadings

1. `Re A,Re B>0` alone does not certify the densities: take `a=b=1,t=u=0`. A,B,sigma are positive, but U has a singularity at zero. A negative real t with `-a<t<0` also violates the selected principal slit-domain contract.
2. The completed-square phase `exp(iqa d_z/A)` need not have modulus 1 for complex A. For `a=q=d_z=1,A=1+i`, its modulus is `exp(1/2)>1`. The source-domain modulus-one phase argument, followed by real Gaussian completion, is the valid proof.
3. There is no uniform compact-bound constant for the entire positive halfplane approaching zero: `t_n=n^(-2)+i n^(-1)` gives `Re(1/t_n)=n^2/(n^2+1)` while `|t_n|^(-3/2)` grows as `n^(3/2)`, so `|U_0(t_n)|` is unbounded. Real endpoint decay and compact complex interior bounds address different domains.
4. A mathematical positive margin cannot be inferred from a midpoint, nor may a branch-crossing working ball be passed to a branch-sensitive routine merely because an external theorem holds for a smaller exact image. Use (2.2) with outward representation and a verified working-ball margin.
5. Explicit finite constants prove local boundedness and convergence prerequisites. They do not prove a small M, a fixed resource-cap success, a finite runtime for an arbitrary noncomputable real input, or acceptance of a frozen decision at an irreducible equality boundary.

## 8. Closure and remaining actual-input obligations

The theorem establishes explicit positive margins, source-domain O/G bounds including signed densities and complex phases, finite-contraction bounds, joint holomorphy, safe image intersection and Cauchy derivative constants. No further existential compact-majorant premise is needed for the stated source and domains. T2 may consume `(Mhat,delta_t,delta_u)`; the point-evaluation construction belongs to the separate T4 theorem.

Actual execution must still bind the exact stored input bytes to finite real parameters/positive exponents/nonzero v; enclose the chosen constants and output balls; respect source ordering, normalization and post-integral conjugation; verify code/backend identity and actual numerical results. These are input/implementation/execution checks, not missing implications in this theorem. All old files remain immutable. Exact synthetic checks support algebra/guard transcription only and are not a proof by sampling.

`actual_HH_runs=0; native_builds=0; certified_epsilon=null; certified_eta=null; rigorous=false; independent_review_admitted=false`.
