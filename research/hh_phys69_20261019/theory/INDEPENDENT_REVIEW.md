# PHYS69 independent mathematical review and coefficient identification

Reviewer: `/root/phys69_github_intake`, separately assigned after completing
the read-only GitHub intake. Date: 2026-10-19 UTC.

**Verdict: PASS_SCOPED_MATHEMATICS.** The proposed polynomial Coulomb-mode
bound and excluded-intermediate second-Born bound are valid in the scope
below. This review supplies the all-angular DtN Taylor-coefficient
identification and the exact old-block/new-band composition. It does not
review a future band integrator or declare that integrator executed.

## 1. Exact object and fixed conventions

Use atomic coordinates, B=27, k=7/10 and E=49/200 Hartree. Set

\[
 h_j(r)=G_j(-10/7,kr)+iF_j(-10/7,kr),\qquad
 f_j(r)=h_j(r)/h_j(B),\qquad
 \nu_j(r)=k^2+2/r-j(j+1)/r^2.
\]

The symbol f here is a normalized outgoing Coulomb mode, not the original
source variable eta=Fy or xi=Fy-phi. The radial derivative is k times the
DLMF rho derivative, and the DtN convention is Z=+u'(B). The source
Hamiltonian is retained through

\[
 V(r,\mu)=2(1+1/d)e^{-2d},\qquad
 d^2=r^2+(7/10)^2-2r(7/10)\mu.
\]

Fix a signed integer m and external ell,p with
|m|<=min(ell,p), 0<=ell,p<=64. The coefficient V^m_{ell,j} is the exact
m-block matrix element of multiplication by V in an orthonormal
spherical-harmonic basis. Its reduced polar basis is real, so this matrix
is symmetric as well as Hermitian at real radius.

Write A_0=2h_C-k^2 in the radial Hilbert space, and let lambda be a
dimensionless strength multiplying the original V. Then A_lambda=A_0-lambda V.
For the outgoing boundary map near lambda=0 define

\[
 Z_\lambda-Z_0=\lambda D_1+\lambda^2D_2+O(\lambda^3).
\]

Thus D_2=Z''_lambda(0)/2. It is the second Born coefficient for the original
potential. All radial integration in the theorem extends to infinity.
The finite-angular coefficient D_{2,L} uses every intermediate mode
|m|<=j<=L and the unchanged corresponding entries of V.

## 2. All-j polynomial Coulomb ratio bound

For every integer j>=20, define

\[
 a_j=(j-1)/k,\quad R_j=(j+1)/k,\quad \Lambda_j=j(j+1),
 \quad C_j=\frac{800}{189}(j+1).
\]

Then

\[
 \boxed{|h_j(t)/h_j(r)|\le C_j\quad(B\le r\le t<\infty).}
 \tag{2.1}
\]

### 2.1 Allowed exterior and transfer interval

Exact substitution gives

\[
 \nu_j(a_j)=-\frac{7j+91}{100(j-1)^2}<0,
 \qquad \nu_j(R_j)=\frac{189}{100(j+1)}>0.
\]

For j>=20, a_j>=190/7>27, R_j<Lambda_j/2, and

\[
 \nu_{\max}=k^2+1/\Lambda_j<1/2,\qquad
 \nu_{\min}=\nu_j(R_j)<k^2.
\]

The inherited energy identities are E'=nu'|h|^2 and
(E/nu)'=-nu'|h'|^2/nu^2, with
E=|h'|^2+nu|h|^2 and E(infinity)=2k^2. Here
nu'=2(Lambda_j-r)/r^3. On r>=Lambda_j, E/nu increases to 2, so
E<=2nu. On R_j<=r<=Lambda_j, E increases with r, hence
E(r)<=E(Lambda_j)<=2nu_max. It follows on the entire r>=R_j interval that

\[
 |h_j|^2+|h'_j/k|^2
 \le\frac{2\nu_{\max}}{\nu_{\min}}
 \le\frac{100(j+1)}{189}=:C_R.
\]

For Y=(h,h'/k), Y'=[[0,k],[-nu/k,0]]Y. The Euclidean logarithmic norms
of the forward and backward systems are both bounded by

\[
 \mu(r)=|\Lambda_j/r^2-2/r|/(2k).
\]

On [a_j,R_j] the expression inside the absolute value is positive and
decreasing: R_j<Lambda_j/2 and its derivative is
2(r-Lambda_j)/r^3<0. Hence the maximum is at a_j. Its trace-growth
exponent is exactly

\[
 2\mu(a_j)(R_j-a_j)
 =2+\frac{14j+182}{49(j-1)^2}\le\frac{41}{20}.
\]

This is an all-integer inequality, not a scan. The positive numerator of
41/20 minus this expression, after multiplication by 980(j-1)^2 and
writing j=t+20, is

\[
 49t^2+1582t+8449>0\qquad(t\ge0).
\]

The positive Taylor sum through degree 16, with the remaining terms
bounded by the first omitted term times 1/(1-(41/20)/18), gives
exp(41/20)<8 using exact rational arithmetic. Consequently

\[
 |h_j(r)|^2+|h'_j(r)/k|^2\le C_j\qquad(r\ge a_j).
 \tag{2.2}
\]

The argument uses fixed-j outgoing asymptotics only to set E(infinity).
It never assumes a uniform asymptotic expansion in j.

### 2.2 Wronskian and the forbidden region

The DLMF normalization yields Im(conj(h)h')=k. Therefore the real Gram
matrix of the two complex numbers (h,h'/k) has determinant 1. Equation
(2.2) bounds its trace by C_j, so its eigenvalues lie in [1/C_j,C_j].
The same Wronskian ensures h_j(r) is nonzero for every real r>0.

For B<=r<=a_j, nu_j(r)<=0 because
k^2 r^2+2r-Lambda_j is strictly increasing on r>0 and is negative at a_j.
Set x=a_j-r. The real backward fundamental functions A(x),B_0(x)
satisfy y''=-nu_j(a_j-x)y, with data
A(0)=1,A'(0)=0,B_0(0)=0,B_0'(0)=k. Their Volterra integral equations
have nonnegative kernels. Successive approximation therefore gives
A>=1, B_0>=0 and nonnegative derivatives. In particular A^2+B_0^2 is
nondecreasing inward.

Since h(r)=A(x)h(a_j)-B_0(x)h'(a_j)/k, the Gram inequalities imply

\[
 \frac{|h(t)|^2}{|h(r)|^2}
 \le C_j^2\frac{A(a_j-t)^2+B_0(a_j-t)^2}
                    {A(a_j-r)^2+B_0(a_j-r)^2}
 \le C_j^2
\]

when B<=r<=t<=a_j. For r<=a_j<=t, the numerator is at most C_j and
the denominator at least 1/C_j; for a_j<=r<=t, use (2.2) and the Gram
lower bound at r. Taking square roots proves (2.1) in every radial case.

This construction gives polynomial growth with j. It does not introduce
an all-j uniform constant Gamma_infinity.

## 3. Exact angular selection and geometric off-diagonal decay

Reuse the PHYS67 whole-exterior E_10 estimate for the original screen S=V/2:

\[
 |S(r,z)|\le M e^{-2(r-B)},\qquad M=1/(4\,10^{19}).
\]

Its degree-N Chebyshev projection S_N obeys
||S-S_N||_infinity <=(2M/9)10^{-N}e^{-2(r-B)}. The multiplier
polynomial of degree N maps a spherical harmonic of angular degree ell
into degrees at most ell+N, for every signed m. One direct proof iterates
the exact cos(theta) recurrence, which changes ell only by +1 or -1 while
preserving m. Thus for j>ell and N=j-ell-1,
<Y_jm,S_N Y_ell,m>=0.

The L2 norm of each harmonic is one, so multiplication by the remainder
has norm at most its scalar sup norm. Including V=2S gives

\[
 \boxed{|V^m_{\ell j}(r)|\le v_{\ell j}e^{-2(r-B)},\qquad
 v_{\ell j}=\frac{4M}{9}10^{\ell+1-j}\quad(j>\ell).}
 \tag{3.1}
\]

There is no angular-quadrature approximation in (3.1), and no factor for
the number of channels. Negative m changes the spherical-harmonic phase
but not this norm argument. Axial symmetry means that the intermediate
sum for the fixed external m contains that same m only.

## 4. Identification with the actual all-angular DtN coefficient

### 4.1 Precise function spaces and local coupling analyticity

The accepted PHYS63 construction uses

\[
 \mathcal H_s=L^2([B,\infty), (1+r^2)^s dr;L^2(S^2)),
 \qquad X=H^{1/2}(S^2).
\]

For the original central exterior problem at k^2, its Dirichlet outgoing
limiting resolvent R_0^+ maps H_1 boundedly to H_-1, with a finite
uncomputed norm. Its Poisson map P_0^+ maps X to H_-1 and local H1. These
are reused PHYS63 results, with AIIS Theorem 1.7 and Corollaries 1.9--1.10
providing the applicable real-axis LAP and radiation uniqueness.

The exact original screen bound V<=delta exp[-2(r-B)], delta=3e-23,
gives the bounded multiplication map

\[
 V:\mathcal H_{-1}\longrightarrow\mathcal H_1,\qquad
 \|V\|\le \sup_{r\ge B}(1+r^2)\|V(r)\|\le730\delta.
\]

Therefore K=R_0^+V is bounded on H_-1. For |lambda|||K||<1,

\[
 P_\lambda^+=(I-\lambda K)^{-1}P_0^+
 \tag{4.1}
\]

is analytic in lambda, has the required boundary trace, and satisfies
(A_0-lambda V)P_lambda^+=0. Its correction is a central outgoing
resolvent applied to an exponentially decaying forcing. Uniqueness in
this outgoing class follows from w=lambda K w and the inverse above.
Local elliptic regularity and the weak normal trace used by PHYS63 make
Z_lambda analytic as a map X to X*. Only a neighborhood of lambda=0 is
needed. No numerical convergence radius reaching lambda=1 is asserted.

For clarity, V is not a compact multiplication operator between these
weighted L2 spaces. The *composition* K is compact, although this extra
property is unnecessary for (4.1). To see it, first truncate V to a
compact source region. For any fixed s0 in (1/2,1), LAP gives a uniform
H_-s0 bound on the truncated-source output, while elliptic regularity
gives a local H2 bound, including the smooth Dirichlet sphere. Rellich
compactness controls any fixed bounded output annulus. The remaining
H_-1 tail is uniformly suppressed by the factor
(1+R_out^2)^(-(1-s0)/2) from the H_-s0 bound. Finally the removed source
tail tends to zero in operator norm because
sup_(r>R_src)(1+r^2)V(r) tends to zero. This proves compactness of K
without assigning compactness to V itself.

The PHYS63 outgoing bilinear boundary identity, or equivalently its
Hermitian form with the incoming Poisson adjoint, now gives

\[
 Z_\lambda-Z_0
 =\lambda(P_0^-)^*V(I-\lambda R_0^+V)^{-1}P_0^+,
\]

and hence the actual operator coefficient

\[
 D_2=(P_0^-)^*V R_0^+V P_0^+.
 \tag{4.2}
\]

For a reduced fixed-m entry, conjugating the incoming Coulomb mode in
(P_0^-)^* yields f_ell^+, so both radial outer factors in (4.2) are
outgoing and there is no complex conjugation in the radial product.
The use of this known auxiliary Coulomb adjoint does not solve the
separate original-source incoming-adjoint research node.

### 4.2 The exact Dirichlet Green kernel and its sign

For the j-channel A_0,j=-d^2/dr^2-nu_j(r), let

\[
 w_j(r)=f_j(r)\int_B^r f_j(t)^{-2}\,dt.
\]

Then w_j(B)=0, w'_j(B)=1 and W(w_j,f_j)=w_j f'_j-w'_j f_j=-1.
The outgoing Dirichlet Green kernel is therefore

\[
 G_j(s,t)=w_j(\min(s,t))f_j(\max(s,t))
 =f_j(s)f_j(t)\int_B^{\min(s,t)} f_j(r)^{-2}\,dr.
 \tag{4.3}
\]

Its derivative jump is -1, as required for -d^2/dr^2, and its increasing-r
boundary derivative is d_s G_j(B,t)=f_j(t). Thus the plus sign in
A_0 u=lambda V u and in both Born coefficients agrees with Z=+u'(B).
There is neither an extra radial k factor nor a minus sign in (4.3).

Define the full-radial primitive

\[
 q_{\ell j}(r)=\int_r^\infty f_\ell(s)f_j(s)V^m_{\ell j}(s)\,ds.
\]

Expanding (4.2) in the central angular basis and inserting (4.3) gives

\[
 \boxed{(D_2)^m_{\ell p}
 =\sum_{j=|m|}^{\infty}\int_B^\infty
       \frac{q_{\ell j}(r)q_{pj}(r)}{f_j(r)^2}\,dr.}
 \tag{4.4}
\]

The expansion agrees with the Hilbert-space expression because angular
projections commute with the central resolvent and converge strongly
in all the radial weighted spaces. Section 5 supplies absolute bounds
on the omitted mode sum and on the triple integral after (4.3), so
Fubini and the infinite angular sum are justified quantitatively.
The finitely many low-j terms are integrable by the retained finite-mode
Coulomb bounds and the same exponential screen decay.

Equation (4.4) identifies the result with the original all-angular
Taylor coefficient; it is not merely a formal limit of numerical
Galerkin values. It also explains why an ordinary second derivative
would equal twice the displayed coefficient.

## 5. Excluded-intermediate estimate and exact infinite sum

Let Gamma_ext bound C_ell C_p, equivalently the product of the two
external normalized-mode bounds. The retained certificate permits
Gamma_ext=5929 for ell,p<=28, or 32400 for ell,p<=64. These are inherited
finite external-mode constants; no new ratio enumeration is needed.

For j>L>=max(ell,p,19), equation (2.1) and (3.1) give

\[
 \left|\frac{q_{\ell j}(r)}{f_j(r)}\right|
 \le\int_r^\infty |f_\ell(s)|
         \left|\frac{h_j(s)}{h_j(r)}\right||V_{\ell j}^m(s)|\,ds
 \le\frac{C_\ell C_jv_{\ell j}}2 e^{-2(r-B)}.
\]

Multiplying the corresponding p estimate and integrating yields

\[
 \int_B^\infty
 \left|\frac{q_{\ell j}q_{pj}}{f_j^2}\right|dr
 \le\frac{\Gamma_{\rm ext}C_j^2v_{\ell j}v_{pj}}{16}.
 \tag{5.1}
\]

The factor 1/16 is (1/2)^2 from the two inner radial integrals times
1/4 from the outer integral of exp[-4(r-B)]. It is not the Riccati
coefficient convention factor. The same estimate holds if both inner
integrands are replaced by their absolute values before applying Fubini
to (4.3); thus there is no conditional cancellation hidden in the
identification.

With x=1/100, the exact elementary identity

\[
 S_L(x):=\sum_{j=L+1}^{\infty}(j+1)^2x^j
 =x^{L+1}\left[
 \frac{(L+2)^2}{1-x}+\frac{2(L+2)x}{(1-x)^2}
 +\frac{x(1+x)}{(1-x)^3}\right]
\]

follows by setting j=L+1+n and using the geometric series and its first
two derivatives. It applies for |x|<1, in particular at the exact
rational x=1/100. Therefore

\[
 \boxed{|(D_2-D_{2,L})^m_{\ell p}|\le\mathcal A_{\ell p,L}:=
 \frac{\Gamma_{\rm ext}}{16}
 \left(\frac{800}{189}\right)^2
 \left(\frac{4M}{9}\right)^2
 10^{\ell+p+2}S_L(1/100).}
 \tag{5.2}
\]

All factors in (5.2) are exact rationals. This proves absolute
convergence of the full-radial excluded-intermediate sum at every fixed
allowed m,ell,p. As an operator statement, (4.2) is bounded from X to X*
by the reused qualitative LAP maps; (5.2) gives a new explicit entrywise
angular error, not a numerical operator-norm error for the entire DtN.

For ell=21,p=20 and Gamma_ext=5929, the independent exact calculation gives:

| L | Approximate decimal value of the exact rational bound, a0^-1 |
|---:|---:|
| 28 | 7.4565417590638954189501976870032151e-49 |
| 35 | 1.1340740046780165375958072920984451e-62 |
| 36 | 1.1961860526549112237206807754933825e-64 |
| 64 | 3.6076087484741816392303777858649738e-120 |

These displayed decimals are nearest displays of exact bounds, not
replacement outward endpoints. The authoritative numerators and
denominators are in INDEPENDENT_EXACT_CHECKS.json. The all-j Coulomb
constant was intentionally chosen for an elementary closed proof;
optimality or sharpness is not claimed.

## 6. Exact reuse of the old L28 block and a new 29..36 band

For a common physical radial cutoff T=65 define

\[
 q^T_{\ell j}(r)=\int_r^T f_\ell(s)f_j(s)V^m_{\ell j}(s)\,ds,
 \qquad q^T_{\ell j}(T)=0.
\]

For every L containing the external channels,

\[
 (D^T_{2,L})_{\ell p}
 =\sum_{j=|m|}^{L}\int_B^Tq^T_{\ell j}q^T_{pj}/f_j^2\,dr.
\]

Neither a retained matrix element V_ell,j nor the scalar Coulomb f_j
depends on the Galerkin cutoff L. Consequently, for the actual old
m=0,ell=21,p=20 request,

\[
 D^T_{2,36}=D^T_{2,28}+
 \underbrace{\sum_{j=29}^{36}\int_B^T
          q^T_{21,j}q^T_{20,j}/f_j^2\,dr}_{B^T_{29:36}}.
 \tag{6.1}
\]

This identity requires only the sixteen new q profiles for the eight
new j values. It reuses the old 57 profiles and their D2 result by
identity, with zero old-panel recomputation. The new profiles must use
the same original V, B,k, Coulomb outgoing normalization and q(T)=0.

Let z28 be the exact stored cutoff midpoint in the completed PHYS68
certificate, and zband the exact midpoint of a validated new band
calculation. Let e28 and eband be their *numerical* complex absolute
error bounds about those cutoff quantities. Then

\[
 |D_{2,\infty}-(z28+zband)|
 \le e28+e_{\rm band}+e_{\rm add}
   +\beta_2(\Gamma_{64},T)+\mathcal A_{21,20,36}.
 \tag{6.2}
\]

Here e_add is zero when the two dyadic complex midpoints are added with
exact rational arithmetic. If rounded addition is used, its error must
be retained. The old scalar e28 is
`D2_numerical_absolute_error_l1`, approximately 8.22810045449e-67; the
historical full-radial total is a different field.

For L=36, the inherited PR115 finite-L<=64 theorem permits the
conservative Gamma64=32400. Its exact beta2=a*chi*exp[-2(T-B)] bounds
the *whole* D2,36 radial cutoff. At T=65 its displayed size is about
7.541139e-66 a0^-1. Equation (6.2) adds this radial term once. The old
beta2 for L28 is not also added: z28 was already the midpoint of the
cutoff computation, even though the old certificate additionally
reported a full-radial enclosure about that midpoint.

Thus a successful new band numerical enclosure can combine with the
unchanged PHYS68 certificate and (5.2) to certify an all-angular second
Born entry at the fixed original physical energy. This conclusion is
conditional on the actual new numerical certificate until that run
and its source-bound verification complete.

## 7. Findings, adoption scope and independent evidence

The following material issues were resolved in this review:

| Finding | Resolution |
|---|---|
| A growing-j bound could accidentally become a uniform Gamma_infinity claim. | Equations (2.1) and (5.2) retain C_j proportional to j+1 and perform the infinite sum explicitly. |
| The convergent angular sum might be only a formal Galerkin limit. | Section 4 constructs the local analytic all-angular boundary family and identifies its exact lambda^2 coefficient using the signed Green kernel. |
| Compact multiplication might be presumed from exponential decay. | V is used as a bounded weighted-space multiplier; only R_0^+V is compact by smoothing and weighted tail control. |
| The radial Green sign, outgoing conjugation or a factor two could be lost. | W=-1, derivative jump=-1, d_B G=+f, incoming-adjoint interpretation and D2=Z''(0)/2 fix all three. |
| Old and new radial tails could be combined inconsistently. | Equation (6.2) uses the old numerical radius, exact band sum and one full finite-L36 beta2. |

No mathematical blocker remains for (2.1), (4.4), (5.2) or the
composition contract (6.2). The independent arithmetic program imports
only Python's standard library, verifies the retained certificate hash
and Gamma28, certifies exp(41/20)<8 exactly, checks the j=20 anchor and
the positive all-j polynomial witness, and compares each closed tail
formula to 64 exact terms plus its exact remaining tail. It performs
zero Coulomb function evaluations, radial integrations or old tests.
Its actual output is INDEPENDENT_EXACT_CHECKS.json.

The scientific advance is an explicit summable angular bound for the
second Born coefficient and a useful missing-band computation strategy.
Numerical certification of the new band is a separate implementation
and execution obligation. Higher-order all-angular nonlinear remainder,
the original source-driven xi, origin and original incoming-adjoint
construction, sigma(E), and Maxwellian k_HH(T) retain their own nodes.
PHYS63 qualitative all-angular LAP/Poisson/DtN remains established, and
HH_R10 remains OFF.

This is a constructive result, with no new impossibility theorem. The
NG1--NG7 review checks were nevertheless applied to the stated scope:
the quantified objects are explicit; the nontrivial mode and sum proofs
are complete; the fixed original model meets the assumptions; the
controlling mechanism is polynomial Coulomb growth overcome by geometric
angular decay; the bound selects the useful new 29..36 band; comparison
with primary sources is scoped below; and the root candidate has this
separate independent derivation. No novelty claim about general LAP,
Chebyshev approximation, or optimal Coulomb asymptotics is made.

## 8. Read sources and fixed evidence identities

Primary sources inspected on 2026-10-19 UTC:

- [NIST DLMF 33.2](https://dlmf.nist.gov/33.2), equations 33.2.1,
  33.2.11 and 33.2.12: Coulomb ODE, outgoing convention and Wronskian.
- [NIST DLMF 33.11](https://dlmf.nist.gov/33.11), fixed-j outgoing
  large-radius expansion, used only for the energy normalization.
- [Adachi--Itakura--Ito--Skibsted, arXiv:1804.07874v1](https://arxiv.org/html/1804.07874v1),
  Theorem 1.7 and Corollaries 1.9--1.10: applicable hard-core weighted
  limiting resolvent and radiation uniqueness. The already accepted
  source-specific mapping is copied from the exact PHYS63 report below.
- [Trefethen, ATAP chapter 8](https://github.com/chebfun/ATAP/blob/development/chap8.m),
  Theorems 8.1--8.2: analytic Chebyshev coefficient and projection bounds.

Inherited source identities actually read:

- PHYS63 PR109 commit `13a9d2cacedc84d9d23cd1193837de2c75f781b5`,
  `research/hh_phys63_20261018/r5/REPORT_KO.md`, Git blob
  `df68533dd0d04f466df9d08714fd4e218261c534`. A faithful read-only copy
  and retrieval identity are in `inputs/PHYS63_REPORT_KO.md` and
  `inputs/PHYS63_REPORT_SOURCE.json`.
- PHYS65 original PR114 `r5/PROOF.md` SHA256
  `00a1f86a8f8d132d53f2e8ea274a26948fd80420ac1c2e943d7036910ef41959`.
- PHYS67 `angular/PROOF.md` SHA256
  `68a1b3e4b7839ebfe9d54210c6e608526c8b9f1254801cc4a3ef853aafa6a650`.
- PHYS68 `theory/PROOF.md` SHA256
  `7f6b2f9543975924e1c500c23b15b609aff20dc1438866340b8fd95e18bfff25`.
- PHYS68 completed `profiles/run_l28_t65_completed/CERTIFICATE.json`
  SHA256 `ddaae206009a276def281af5526851ceb717baf2e0de5f8472552a9db340de9a`.

No inherited scientific evidence was overwritten or recomputed by this
review. Git publication and cloud backup of these new files are root
delivery tasks and are not asserted by the mathematical verdict.
