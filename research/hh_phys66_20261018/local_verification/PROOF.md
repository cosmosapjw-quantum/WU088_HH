# PHYS66 R5: coefficient-wise full-radial versus cutoff errors

## Definitions and authority

Existing atomic coordinates are retained: radius r/a0, B=27, k=7/10,
E=49/200 Hartree, original V=2(1+1/d)exp(-2d), d=|r n-0.7 zhat|.
The original source hash f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d is a provenance guard, not proof of an operator inequality.
For a fixed full angular cutoff 0<=ell<=L<=64, include every allowed m and every intermediate angular channel within that projection. There is no assertion uniform as L tends to infinity.

Upstream PR114 commit bad80f7729015c84c8dde27f1b1dec3a1f8b2c9f proves the real-radius Coulomb ratio bound ||P(r,t)||_2^2<=Gamma for all 27<=r<=t<infinity, with P=diag(H_l^+(t)/H_l^+(r)), H+=G+iF. It does NOT assume attractive-Coulomb modulus monotonicity. Exact byte-pinned upstream code evaluates all mode certificates; Gamma64=32400. The upstream real-Gram determinant and energy/turning-point derivation is a prerequisite, not replaced with numerical samples.

Reference conventions: NIST DLMF33.2 and33.11. Related bounds on coupled integral equations exist in A.Weinmann, Proc.Phys.Soc.75 (1960),510, doi10.1088/0370-1328/75/4/305; no priority or general novelty claim is made here.

## Norms and existing coefficient majorants

Let D=Z_S-Z_C, with Z=+u'(B)u(B)^(-1), opposite the exterior outward normal convention. The outgoing bilinear Volterra map is

D(r)=int_r^infty P(r,t)[V(t)+D(t)^2]P(r,t)dt.

No conjugation or commutation is inserted in the matrix square.
The physical nth Born contributions D_n include powers of the original V. Thus D1 is physical order1, not the normalized O(1) Y1 used in code.
Define ||A||_w=sup exp[2(r-B)]||A(r)||_2 and ||A||_0=sup||A(r)||_2.
The upstream source bound ||V(r)||<=delta exp[-2(r-B)], delta=3e-23, gives

a=Gamma delta/2, b=Gamma/4, chi=4ab=Gamma^2 delta/2<1/2,
alpha_n=Cat_(n-1) b^(n-1) a^n,
||D_n||_w<=alpha_n.

These bounds also hold for D_(n,T), the exact mathematical coefficients for V restricted to [B,T], extended with D_(n,T)=0 beyond T.

## New coefficient-wise radial comparison

Let E_n=D_n-D_(n,T), beta_n an unweighted bound. The forcing tail directly gives

beta_1(T)=a exp[-2(T-B)].

For the bilinear operator B(A,C)(r)=int_r^infty P A C P dt,

||B(E,A)||_0, ||B(A,E)||_0 <= (Gamma/2)||E||_0||A||_w.

The factor is Gamma/2, NOT Gamma/4: just one factor is controlled in the exponential-weighted norm. Expanding the ordered products,

D_j D_(n-j)-D_(j,T)D_(n-j,T)
 = E_j D_(n-j)+D_(j,T) E_(n-j).

This identity remains valid without commuting the matrices. Summing the two positive scalar norm estimates and reindexing yields the induction

beta_n(T)=Gamma sum_(j=1)^(n-1) alpha_j beta_(n-j)(T), n>=2.

Let h0=1 and h_n=sum_(j=0)^(n-1) Cat_j h_(n-1-j)/4^j. Then

beta_n(T)=a h_(n-1) chi^(n-1) exp[-2(T-B)],
sum_(n>=0) h_n x^n=1/(2sqrt(1-x)-1).

This last generating function is only for positive scalar majorants, not a commutative replacement of matrix dynamics. Its first coefficients are 1,1,5/4,13/8,137/64. The finite-n recurrence proves the required statement without an exchange of infinite sums. The generating function converges for |x|<3/4, and the inherited chi<1/2 is safely inside this region.

In particular beta2=a chi exp[-2(T-B)] and beta3=(5/4)a chi^2 exp[-2(T-B)]. For L64 at T65 the exact-rational upward bound has numerical display beta3=1.4843223148855876e-79 a0^-1. The implementation uses a reciprocal positive Taylor sum as a rational upper enclosure of exp[-2(T-B)], not a nearest-rounded float.

## Application and strict exclusions

Each fixed normalized spherical-harmonic boundary matrix entry has absolute radial error <=beta_n. The bound is for the exact coefficient of the full-radial finite-L problem minus the exact cutoff coefficient, NOT its computed f64 approximation. It includes every intermediate channel inside the chosen L; it excludes ell>L.

An error ledger for numerical data must keep at least: per-order analytic radial error; higher-Born truncation; angular omission; Coulomb numerical error; angular quadrature; ODE and floating roundoff. Missing components are UNKNOWN, never0. In particular the upstream whole-response tail after3 (~1.90e-60 at L64) need not be smaller than the very tiny third-order numerical value (~1e-71). No total accuracy or actual source-driven scattering rate follows from choosing T65.

Selected planning goals beta1<=1e-30, beta2<=1e-54, beta3<=1e-78 are analyst-selected absolute RADIAL-component goals. They are not user-specified total tolerances. Exact integer search returns T65; T64 fails the third component. These choices do not authorize production HH_R10.

## Verification status

One genuine behavioral red test of h0,h1,h2 failed with a zero placeholder, followed by the same passing test after implementation. Twenty-five proportionate regressions were then added (tests-after, not relabeled as independent red cycles). All26 pass. Independent SymPy power-series coefficients, mpmath500 exponential evaluations, source/code hash gates, invalid domains, and exact large rational hex roundtrip are checked. Connected Wolfram independently returned {1,1,5/4,13/8,137/64} and the T64/T65 third-order comparison. Native subagent execution NOT_RUN.

PHYS63 qualitative all-angular real-axis LAP remains established in the project. The present estimates provide additional finite-L quantitative components, not a replacement all-angular theorem. HH_R10 remains OFF.

## Late upstream synchronization
Before closeout, PR115 commit445d82db9c42b4f2f81e4ac1b107dec3b69b3c24 was read. It independently publishes the SAME coefficient-wise theorem with hbar_n=4^n h_n and generating function1/(2sqrt(1-4x)-1). This file is a local verification/supporting derivation, NOT a replacement for the upstream r5/PROOF.md or a claim that this session published PR115. All local reports were moved to local_verification to avoid collision. For L<64 this implementation also uses the tighter inherited mode-wise Gamma_L instead of the common Gamma64; no new asymptotic claim follows.
