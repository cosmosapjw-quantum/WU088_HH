# PHYS65: a constructive finite-cutoff full-exterior certificate

## 1. Preserved operator and what is bounded

Atomic coordinates are used: r denotes physical radius/a0 and the log derivative is in a0^-1. B=27, k=7/10, E=49/200 Hartree, eta_C=-10/7. The original potential is

V(r,n)=2(1+1/d)exp(-2d), d=|r n-(7/10)zhat|.

For any fixed integer 0<=L<=64, project orthogonally to all ell<=L, including every allowed signed m. V_L is the actual projected multiplication; no central replacement or intermediate-channel deletion is made inside this projection. We prove bounds for the continuum radial problem on B<=r<infinity and for comparison with V_L truncated at r=T. We do NOT bound the excluded ell>L sector, numerical discretization, roundoff, an original driven source, or a cross section.

The source NPZ SHA256 is f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d. It is a provenance guard, not a mathematical proof oracle. Parent PR113 includes new completed NCP data; we do not rerun the old campaign. The exact retrieved L64/T39 RESULT.json was reconstructed and matched to its campaign SHA256 before reuse. Its coefficient NPZ and complete NCP archive were not downloaded here.

## 2. Uniform-in-radius Coulomb ratio lemma

Let h_l(r)=G_l(eta_C,kr)+i F_l(eta_C,kr), with derivatives in r. The DLMF normalization gives Im(conj(h_l)h_l')=k and h_l=exp(i[kr-eta_C log(2kr)+phase]) times an amplitude tending to one. Thus the radial equation and outgoing energy normalization are

h''+nu_l h=0, nu_l=k^2+2/r-l(l+1)/r^2,
E_l=|h'|^2+nu_l|h|^2, E_l(infinity)=2k^2.

The identities E_l'=nu_l'|h|^2 and (E_l/nu_l)'=-nu_l'|h'|^2/nu_l^2 are exact wherever nu_l>0. Write lambda=l(l+1). For l>0, nu_l has its unique maximum at r=lambda; on the decreasing outer part E_l/nu_l increases to2, so E_l<=2nu_l. On any positive-nu interval R<=r<=lambda, E_l increases with r and is bounded by E_l(lambda)<=2nu_l(lambda). For l=0, nu_l is decreasing everywhere. Consequently, if nu_l(R)>0, for ALL r>=R,

nu_min=min(nu_l(R),k^2)>0,
nu_max=nu_l(max(R,lambda)) (or nu_l(R) for lambda=0),
|h|^2+|h'/k|^2 <= C_R=2 nu_max/nu_min.

This uses no global monotonicity assumption on the attractive Coulomb amplitude. Such monotonicity would in general be false.

If nu_l(B)>0, set a=R=B. Otherwise use the exact rational grid a=j/16 with nu_l(a)<=0<nu_l(a+1/16), and choose an allowed R=a+h, h in {1/2,3/4,...,3}. For Y=(h,h'/k), Y'=A Y with A=[[0,k],[-nu_l/k,0]]. Both forward and backward Euclidean logarithmic norms are bounded by

mu(r)=|lambda/r^2-2/r|/(2k).

The maximum on [a,R] occurs among a,R,lambda (the last only if in the interval). Gronwall therefore gives, for every r>=a,

trace G(r)=|h|^2+|h'/k|^2 <= C_R exp(2 mu_max(R-a)) <= C_l,

where the final integer C_l is obtained by an exact upward rational Taylor/geometric remainder for exp, followed by integer ceiling. All search decisions compare exact fractions. The source code and mode table give every rational witness.

Here G is the REAL Gram matrix of the complex pair (h,h'/k). Its determinant is1 by the Wronskian. Hence its eigenvalues obey

1/C_l <= lambda_min(G(r)) <= lambda_max(G(r)) <= C_l, r>=a.

For B<=r<=a (when present), nu_l<=0. With x=a-r, the real backward transfer representation is

h(r)=A_0(x)h(a)-B_0(x)h'(a)/k,
A_0(0)=1, A_0'(0)=0; B_0(0)=0, B_0'(0)=k.

Both solve y_xx=-nu_l(a-x)y. Since -nu_l>=0, A_0,B_0 and their first derivatives are nonnegative. In particular A_0>=1, and A_0(x)^2+B_0(x)^2 is nondecreasing inward. The Gram inequalities at a then imply for B<=r<=t<=a

|h(t)|^2/|h(r)|^2 <= C_l^2 [A_0(a-t)^2+B_0(a-t)^2]/[A_0(a-r)^2+B_0(a-r)^2] <= C_l^2.

If r<=a<=t, the numerator is <=C_l, while the denominator is >=1/C_l; if a<=r<=t, use the Gram inequalities at both points. Thus in ALL cases

|h_l(t)/h_l(r)|^2 <= C_l^2, B<=r<=t<infinity.

Exact finite enumeration of l=0..64 gives max C_l=180, attained at l64. Its selected a=1441/16, R=1465/16, nu_min=134281/8584900, nu_max=10197/20800 and mu_max=5094240/14535367. This is an exact finite angular certificate combined with a continuum radial proof, not a sampled radial maximum. For P(r,t)=diag(h_l(t)/h_l(r)), every signed-m multiplicity obeys ||P(r,t)||_2^2<=Gamma=32400. No L-independent bound is claimed as L tends to infinity.

## 3. Full-exterior Riccati fixed point and ordered Born series

The exact source majorant is ||V_L(r)||<=delta exp[-2(r-B)], delta=3e-23. It follows from d>=r-7/10 and the positive Taylor lower bound for exp(263/5). Projection is a contraction.

The outgoing response D=Z_L-Z_C satisfies the complex-bilinear matrix Volterra equation

D(r)=int_r^infty P(r,t)[V_L(t)+D(t)^2]P(r,t)dt.

No conjugation or commutation is inserted. In the Banach norm ||D||_w=sup_{r>=B} exp[2(r-B)]||D(r)||_2, its forcing has norm <=a=Gamma delta/2 and its bilinear part norm <=b=Gamma/4. Let chi=4ab=Gamma^2 delta/2. If chi<1/2, the ball y=a/(1-chi) is invariant, since a+b y^2<=y, and its Lipschitz constant2by=chi/[2(1-chi)]<1. The resulting decaying Riccati solution yields an outgoing fundamental matrix: factor U=H A, integrate A'=H^-1 D H A with A(infinity)=I. For each finite L the Coulomb factors and their inverses are bounded in the exterior, so the coefficient is integrable. This identifies the small fixed point with the actual projected outgoing Jost logarithmic derivative, not merely a formal power series.

With physical ordered terms D_n=epsilon^n Y_n, epsilon=delta, the exact noncommutative convolution gives

||D_n||_w <= Cat_(n-1) b^(n-1) a^n.

Since Cat_j<=4^j, after N terms the continuum tail obeys

||D-sum_(n=1)^N D_n||_w <= a chi^N/(1-chi).

For L64, chi=19683/1250000000000000000 =1.57464e-14 and the N3 tail is <2e-60 a0^-1. This bounds the exact mathematical terms, not the error in computed floating coefficients.

## 4. Analytic radial-cutoff error

Let D_T be the analogous exact solution with V set to zero beyond T and extended by D_T=0 there. Both D,D_T obey the same weighted ball bound y. In UNWEIGHTED supremum norm the forcing difference is <=a exp[-2(T-B)]. The nonlinear difference is bounded by Gamma y ||D-D_T||_infty; here Gamma y=chi/(1-chi)<1. Therefore

||D-D_T||_infty <= a (1-chi)/(1-2chi) exp[-2(T-B)].

For L64 this is <=1.834716e-29 at T39, <=6.155e-33 at T43, and <=4.789120e-52 at T65. Values in code are exact rational upper endpoints, not nearest decimal rounding. Since the same Born bound applies to D_T,

||D-sum_(n=1)^N D_(n,T)|| <= radial_cutoff_bound + Born_tail_bound.

To compare with FLOATING computed terms one MUST add ODE/Coulomb/angle-quadrature/roundoff errors, still uncertified. Excluded angular modes require a separate bound. A finite-grid self-difference is not that bound. In particular do not mark old NCP fields full_nonlinear_remainder_certified or total numerical certification true retroactively.

## 5. Evidence and attribution

Standard Coulomb ODE, Wronskian and asymptotic normalization: NIST DLMF33.2 and33.11, https://dlmf.nist.gov/33.2 and https://dlmf.nist.gov/33.11. Brune,Hale,Paris (2018), https://doi.org/10.1103/PhysRevC.97.024603 and https://arxiv.org/abs/1708.07554, explicitly distinguishes repulsive monotonicity from the attractive case. Their paper does not establish our finite-cutoff constants. This is a source-specific direct energy/Gram-transfer derivation; no general novelty or full-scattering claim is made.

Exact-Fraction code tests and independent mpmath ratio samples check implementation/ingredients, not a machine proof of every analytic step. Connected Wolfram independently checked energy and Gram identities, l64 rational anchor and C64/Gamma/chi/tail. The first CAS equality was left unexpanded and returned PASS false; the corrected residual was exactly zero. The first Python reference at110 digits could not order exponentially close rationals; independently evaluated at500 digits, no physical tolerance changed. These failures are retained. HH_R10 stays OFF.
