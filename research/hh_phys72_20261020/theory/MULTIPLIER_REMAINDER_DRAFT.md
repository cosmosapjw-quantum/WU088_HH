# PHYS72 — explicit all-angular weighted Coulomb inverse and Born remainder

Constructive derivation, 2026-10-20. This document is the independent weighted
operator lane, for integration into the final PHYS72 proof. The premises from
PHYS63, PHYS65, PHYS69 and PHYS71 are reused with their original identities.
No inherited radial panels or profiles are evaluated in this derivation.

## 1. Fixed operator, spaces and normalization

Use the inherited dimensionless atomic radius r = r_phys/a0, B=27,
k=7/10, E=(k²/2) Eh=49 Eh/200 and eta_C=-1/k=-10/7. The reduced radial
wave u has already absorbed the three-dimensional r factor; its measure is
dr dΩ. The original operator is

    A_λ = -∂r² + J/r² - 2/r - k² - λ V,
    J = -Δ_(S²),
    V(r,μ) = 2 (1+1/d) exp(-2d),
    d² = r²+(7/10)²-2r(7/10)μ.

A0 has the homogeneous Dirichlet boundary u(B)=0 when used as a Green inverse,
and the actual outgoing Coulomb condition at infinity. H_j^+=G_j+iF_j^C,
f_j(r)=H_j^+(r)/H_j^+(B), and Z=+u'(B)u(B)^-1 are unchanged. A0 is twice
the physical dimensionless h_C-E; its inverse must not be multiplied by an
additional factor two. Physical DtN values below are the displayed atomic
values times a0^-1. The source variables eta=Fy, xi=Fy-phi and the Coulomb
parameter eta_C remain distinct.

For the bulk Hilbert space H=L²([B,∞)×S²,dr dΩ) define

    ||f||_+ = ||r f||_H,
    ||u||_- = ||u/r||_H.

These spaces are equivalent to the inherited (1+r²) weighted spaces because
r≥27. We derive an explicit inverse constant; the existence and uniqueness
identification is the already established PHYS63 outgoing LAP result.

## 2. A shifted radial multiplier controls every angular mode

First let f be smooth, compactly supported in radius and contain finitely
many spherical harmonics, and let u=R0^+f. These are a dense source class.
Write β(r)=r-B/2 and p=u'-iku. Integration by parts in the exact differential
equation A0u=f gives, on [B,R],

    2 Re ∫_B^R ⟨f, β p⟩ dr
      = ∫_B^R [ ||p||² + B ||u||²/r²
                 +(1-B/r)||∇Ωu||²/r² ] dr
        +(B/2)||u'(B)||²
        -β(R)||p(R)||²
        +β(R)[||∇Ωu(R)||²/R²-2||u(R)||²/R].       (2.1)

Here ⟨f,p⟩ means f times conjugate p, summed/integrated over angles; only
its real part is used. For a single angular eigenvalue L=j(j+1), the volume
coefficient follows directly from

    q(r)=L/r²-2/r-k²,
    -(βq)' - k² = B/r² + L(1-B/r)/r².

All angular terms are nonnegative for r≥B, including every j,m. No maximum
angular degree, and no replacement of a growing C_j, appears in (2.1).
The Dirichlet boundary term has positive sign because β(B)=B/2>0.

For this finite-harmonic compact-source class, outside the support each
channel is a multiple A_jm H_j^+. The inherited outgoing Coulomb asymptotic
and Wronskian give

    H_j^+(r) = exp(i[kr+(1/k)log(2kr)+phase_j])(1+O(r^-1)),
    p(r) = O(r^-1),
    Im ∫_(S²) u'(r) conjugate(u(r)) dΩ → k ||A||².

Consequently the last two terms of (2.1) tend to -2||A||². This Coulomb
boundary contribution is retained, rather than omitted as for the free
Helmholtz problem. The imaginary part of the original equation also gives

    Im ∫_B^∞ ⟨f,u⟩ dr = -k ||A||².              (2.2)

Let

    X=||p||_H, W=||u/r||_H, F=||r f||_H,
    Y²=∫_B^∞ (1-B/r)||∇Ωu||²/r² dr.

Using (2.2) to eliminate the outgoing amplitude from the R→∞ limit yields

    X²+B W²+Y²+(B/2)||u'(B)||²
      =2 Re ∫_B^∞ ⟨f, βp - (i/k)u⟩ dr.        (2.3)

Equivalently the scalar integrand on the right is
f[β(conjugate(u')+ik conjugate(u))+(i/k)conjugate(u)]. This form records
the conjugation and the Coulomb-flux sign unambiguously.

Because 0<β(r)≤r, Cauchy–Schwarz gives

    X²+B W² ≤ 2F X+(2/k)F W.

Completing the square in X gives

    B W²-(2/k)F W-F² ≤ 0.

Thus the actual outgoing Dirichlet inverse obeys

    ||R0^+ f||_- ≤ C_R ||f||_+,
    C_R = [1/k+sqrt(B+1/k²)]/B
        = [1+sqrt(1+B k²)]/(B k).               (2.4)

At B=27,k=7/10,

    C_R = 0.2525009112577779329385329803… < C_* = 253/1000.

This final rational upper endpoint is certified without floating arithmetic:

    27 C_*²-(20/7)C_*-1 = 37701/7000000 > 0,

and the quadratic is increasing at and above its positive root. The proof is
uniform in all j,m. Density extends the inverse bound to the full weighted
source space; PHYS63 outgoing uniqueness identifies the bounded extension
with the actual R0^+ already used to define the Taylor coefficients.

An explicit radial/angular energy bound is also available. Put

    E=X²+B W²+Y²+(B/2)||u'(B)||².

Equation (2.3) implies

    E ≤ 4[1+1/(B k²)] F² = (5692/1323) F².      (2.5)

Indeed X+W/k≤sqrt(1+1/(Bk²))sqrt(X²+B W²)≤sqrt(1+1/(Bk²))sqrt(E).
The angular weight in (2.5) is (r-B)/r³ times j(j+1). Its vanishing at B
is part of the exact estimate, and is not replaced by a positive constant.

## 3. The original noncentral multiplier and the sandwiched Green operator

The inherited whole-exterior screen bound is

    0<V(r,μ)≤δ exp[-2(r-B)],    δ=3/10^23.

The exact original V is used throughout. Multiplication by it couples all
permitted angular degrees. On the weighted bulk spaces,

    ||V||_{-→+}=ess sup_(r,μ) r² V(r,μ)
       ≤B²δ = 2187/10^23 =: M.

The last inequality follows because r² exp[-2(r-B)] decreases for r≥27.
There is no angular quadrature or channel-count factor: this is the norm
of multiplication on L²(S²), before any harmonic representation.

Therefore K=R0^+V on the minus weighted space obeys

    ||K||≤q=C_* M=553311/10^26=5.53311×10^-21.   (3.1)

A more convenient Hilbert-space form for the boundary remainder is

    S=√V R0^+ √V : H→H.

Set T=r^-1 R0^+ r^-1. Equation (2.4) states ||T||≤C_* on H, and

    S=(r√V) T (r√V),    ||r√V||²≤M.

Consequently ||S||≤q with exactly the same q. This factorization is valid
for the actual angular multiplier; it requires no commutation of V with J
or with R0^+. S is generally complex and is not asserted positive or self
adjoint. Norm estimates use Hermitian Hilbert norms; the fixed-m matrix
coefficients below retain the original complex bilinear convention.

The Neumann inverse exists in operator norm for |λ|q<1. In particular λ=1
is admitted. The explicit sufficient radius is

    1/q = 10^26/553311 > 1.8073×10^20.

This is a sufficient radius for the exterior Dirichlet/Poisson problem at
B=27. No claim about the interior source-driven problem follows from this
radius alone.

## 4. An explicit angular boundary norm retains the growing C_j

For a full spherical-harmonic boundary field g define

    ||g||_C² = Σ_(j,m) C_j² |g_jm|²,
    C_j = 77                         (0≤j≤28),
          (800/189)(j+1)             (j≥29).

The inherited PHYS65/69 whole-radial ratio estimates give |f_j(r)|≤C_j.
This angular space H_C is equivalent to H¹(S²); it is a specified, stronger
boundary regularity than the natural H^(1/2) trace space. We claim this
explicit weighted norm, not a new sharp natural-trace constant.

Let B_±=√V P0^±. The incoming ratio has the same modulus as the outgoing
one. Since the central Poisson operator is diagonal in spherical harmonics,

    ||B_±g||_H²
       ≤δ∫_B^∞ exp[-2(r-B)] ||P0^±g(r)||² dr
       ≤(δ/2)||g||_C².                         (4.1)

This is a full-angular boundary-to-bulk bound. The polynomial C_j growth
is retained in the boundary norm rather than replaced by Γ64. In particular
for one normalized basis vector of degree a≤28,

    ||B_± e_a||_H ≤ C_a sqrt(δ/2),   C_a=77.

No m multiplicity is lost or inserted; orthonormality already sums it.

## 5. Actual DtN Taylor series and every order ≥4

The already established outgoing Green/boundary identity, with the current
explicit inverse bound, gives

    √V P_λ^+ = (I-λS)^-1 B_+,
    Z_λ-Z_0 = λ B_-^* (I-λS)^-1 B_+,
    D_n = B_-^* S^(n-1) B_+,      n≥1.          (5.1)

The star is the incoming Poisson adjoint under the natural boundary duality.
For the real fixed-m polar basis, conjugating the incoming radial factor
produces the outgoing f_a, so (5.1) is exactly the inherited complex
bilinear coefficient convention. D_3 is Z'''(0)/6 and contains S²; no extra
factorial or factor two occurs.

After retaining D1,D2,D3, the exact remainder is

    R_≥4(λ)=λ^4 B_-^* S³(I-λS)^-1 B_+.         (5.2)

The full-angular weighted boundary estimate is

    ||R_≥4(λ)||_(H_C→H_C*)
       ≤(δ/2) |λ|^4 q³/(1-|λ|q).              (5.3)

For the original entry (a,b,m)=(21,20,0), multiply by C_a C_b=77²=5929:

    |R_≥4(λ)_(21,20)|
       ≤(5929 δ/2) |λ|^4 q³/(1-|λ|q) a0^-1.  (5.4)

At λ=1 the exact rational endpoint is

    R4 = (5929 δ/2) q³/(1-q)
       = 1.506539843783884230906835850675039…×10^-80 a0^-1
       < 1.50654×10^-80 a0^-1.

This bound is all angular and all radial, with the actual outgoing Green
operator and original noncentral screen. It is independent of the completed
D3 numerical campaign; those 76 accepted panels and 152 inherited profiles
are reused without integration. More generally, after exact orders 1…N,

    ||R_≥N+1(λ)||_(H_C→H_C*)
       ≤(δ/2) |λ|^(N+1) q^N/(1-|λ|q).

## 6. Incorporating computed coefficients and preserving their status

If z_n is a stored certified center with |D_n-z_n|≤ε_n for n=1,2,3,
then the original entry at λ=1 satisfies

    |(Z_1-Z_0)_(21,20) - (z_1+z_2+z_3)|
       ≤ε_1+ε_2+ε_3+R4,

plus any newly introduced rounding of the combined displayed center. Exact
rational addition of the stored centers adds no arithmetic error.

PHYS71's final corrected D3 certificate SHA is
f75d082e1966dd61a326c37b6ff14e8f330e010341a59a88eb4ca8d4734e6173. Its radius
7.121295358370×10^-79 a0^-1 remains unchanged. If only the third-order
correction plus higher orders is wanted, the same center z_3 encloses it
with radius ε_3+R4; this is an actual consequence of (5.4), not a rerun.

This derivative/remainder result does not apply the frozen NPZ driving
source. Original source-driven xi, origin/incoming adjoint matching,
sigma(E), Maxwellian k_HH(T) keep their distinct DAG nodes. HH_R10 remains
OFF. A failed optional sharper sufficient estimate would not negate the
valid bound above or constitute a strong no-go result.

## 7. Direct checks required for the implementation contract

1. Verify the general single-channel integration-by-parts identity before
   substituting β=r-B/2, including the boundary and flux signs.
2. Check the free-screen λ=0 limit and V=0 remainder exactly.
3. Check the rational C_* root residual and q<1 by integer arithmetic.
4. Check λ powers: n=1 uses S^0 and the order≥4 remainder uses λ^4 S³.
5. Evaluate the final rational remainder and outward decimal conversion.
6. Verify that any native implementation reports a weighted norm certificate,
   not a numerical integration of inherited panels or a source-driven rate.

The first rational evaluation in this lane used Python standard-library
Fraction and Decimal (80 digits) and returned the residual 37701/7000000,
q=5.53311e-21, and the R4 value displayed above. It performed zero radial
integrations and zero Coulomb function evaluations. The Decimal display is
informational; the rational formulas are authoritative.

### Independent manufactured outgoing-field diagnostic

A new lightweight identity check used

    u(r)=(1-exp[-(r-B)]) exp(i[kr+(1/k)log r]) Y_jm,

with f=A0u evaluated analytically. It has u(B)=0, u'(B) of modulus one,
outgoing amplitude of modulus one, and f=O(r^-2); therefore the nonzero
Coulomb boundary-flux contribution is exercised. This is a manufactured
source for the identity check, not the frozen HH source or an inherited
Born profile. After canceling the common phase, the implementation used

    w=1-exp(-x), w'=exp(-x), x=r-B,
    exp(-iθ)f = w'+[j(j+1)+1/k²]w/r²
                -i[2(k+1/(kr))w'-w/(kr²)],
    exp(-iθ)p = w'+i w/(kr).

SciPy 1.17.0 `quad` on x∈[0,∞), with epsabs=2e-10, epsrel=5e-13,
limit=300, checked (2.3) and (2.2). The outputs were:

| j | LHS including B/2 trace | RHS including Coulomb flux | Relative identity residual | Flux integral + k |
|---:|---:|---:|---:|---:|
| 0 | 15.0204598228583 | 15.0204598228583 | 0 | 0 |
| 20 | 22.76814733693236 | 22.768147336932362 | 1.5603876882145876e-16 | 0 |
| 64 | 91.75945996225852 | 91.75945996225853 | 1.5487073181388658e-16 | 0 |
| 1000 | 18480.342368366033 | 18480.34236836604 | 3.937133560165064e-16 | 0 |

These are binary64 diagnostics with the quadrature routine's estimated
absolute errors between 2.38e-11 and 7.79e-9, not interval certificates.
The symbolic integration-by-parts derivation supplies the continuum
all-angular proof. Four manufactured fields, twelve scalar quadratures,
zero inherited physical integrations and zero Coulomb function evaluations
were used by this diagnostic, in one successful Python invocation.

### Third and higher orders at λ=1

For the inherited certified third-order center

    z3=(2.14300135468641834333042543662
        +1.71865149630238869433259719024 i)×10^-71 a0^-1,

(5.4) gives the all-angular/all-radial statement

    |[(Z1-Z0)-D1-D2]_(21,20),m0 - z3|
      ≤7.121295358370×10^-79+R4
      =7.2719493427483884230906835850675039…×10^-79 a0^-1
      <7.271949342749×10^-79 a0^-1
      <10^-78 a0^-1.

The existing goal 10^-78 is thereby also met for the sum of the third and
all higher orders about the same D3 center. This statement subtracts the
exact D1 and D2. A certificate for the full numerical Z1-Z0 approximation
must separately add the inherited ε1, ε2 and any combined-center rounding.
No such error terms are discarded or inferred from native binary64 output.

The manufactured diagnostic's exact executed stdin source, raw tool stdout
and receipt are preserved as `../verification/manufactured_morawetz.py`,
`../verification/manufactured_morawetz.stdout.json` and
`../verification/MANUFACTURED_MORAWETZ_EXECUTION.json`. The script was saved
after its one successful stdin invocation; the saved replay command was
not run again.
