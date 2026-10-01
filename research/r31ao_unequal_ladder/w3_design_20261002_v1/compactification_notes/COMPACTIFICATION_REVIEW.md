# W3 compactification: derived candidate, deferred implementation

Status: the real changes of variables below are derived from the frozen source;
the transformed kernel is not implemented, tested, or admitted. No HH integration
or callback was executed for this review. The immediate priority is independent
lower/upper endpoint accounting and certified upper-cutoff selection, since that
can remove unnecessary domain width without changing the current callback.

## Source authority

The exact target is the finite Frozen107 continuous source functional in
`source_functional_review_20260930/SOURCE_FUNCTIONAL_MAP.md`. The accepted
conditional endpoint and holomorphy statements are in
`endpoint_enclosure_review_20260930/NEW_THEOREM_REVIEW.md`. Actual expressions are
`gap_closure_20261001_g0_g6_v1/validated_callback/callback.cpp`, imported without
formula duplication by `ncp64_acceleration_20261001_v1/native_cache/cached_callback.cpp`.
`wide_domain_20261001_v1/range_native_driver/log_map.hpp` is the current coordinate
wrapper. The companion JSON records actual file byte identities.

Write the source integrand as

\[
 F(t,u)=\sum_{ijk}C_{ijk}U_i(t)U_j(u)I_{k,\ell}^{a,b}(t,u).
\]

The order and exact values of all 107 signed coefficients, the orbital/field,
Gaussian inputs and all normalization/phase conventions remain fixed. No
normalization or endpoint error is included in this unnormalized primitive.

## Discriminating comparison

| Route | Exact real target equality | Existing kernel reusable | Principal limitation |
|---|---|---|---|
| Current \(t=2^x\) | Yes; \(dt=(\log2)t\,dx\) | Yes | Fixed step-3 full tensor tiling is expensive over [-8,192]^2; 4,489 tiles is a planner outcome, not a theorem lower bound. |
| Naive \(t=r^{-2}\) wrapper | Yes; reversed endpoints and \(2r^{-3}\) | Yes on finite positive intervals | It retains artificial singularities at r=0 and the old whole-image Re(t)>0 proof domain; speedup is unproved. |
| Algebraically normalized \(r=t^{-1/2}\) | Yes on the positive real axis | New density/geometry expressions required | Single-variable upper tails regularize, but the double-tail corner needs its own treatment. |
| Normalized reciprocal square root plus sectors | Yes with the correct sector domain | New scaled radial and derivative kernel | A finite lower r cutoff makes the sector nonrectangular; integrating to r=0 needs an explicit endpoint-inclusion contract. |
| \(t=\tan^2\theta\) or \(t=x/(1-x)\) | Yes on their real domains | Only as naive wrappers | More transcendental/dependency cost or severe near-1 cancellation; no demonstrated advantage over reciprocal square root. |

For \(r=x+iy\ne0\),
\(\Re(r^{-2})=(x^2-y^2)/(x^2+y^2)^2\). Thus the inherited physical-domain
guard requires \(|y|<|x|\). On the positive branch a large complex box near zero
cannot satisfy this. For W3, \(r_{\min}=2^{-96}\) is exact and nonzero, but merely
using that representable endpoint does not give a wide analytic neighborhood.
The naive wrapper may still perform adequately under absolute tolerances; no
runtime failure or speedup is inferred from this domain observation alone.

## Exact reciprocal-square-root formulas

Let \(r=t^{-1/2}>0\), \(s=u^{-1/2}>0\), and \(\lambda=\mu^2/4\). Then

\[
 \int_l^T\!\int_l^T F(t,u)\,dt\,du
 =\int_{T^{-1/2}}^{l^{-1/2}}\!\int_{T^{-1/2}}^{l^{-1/2}}
 4r^{-3}s^{-3}F(r^{-2},s^{-2})\,dr\,ds.
\]

For the upper-tail split at t=256 the inverse coordinate boundary is 1/16.
For W3, l=1/256 and T=2^192 correspond to [2^-96,16] in both inverse coordinates.
All these endpoints are exact dyadics. The transformed density is

\[
 D_i(r):=2r^{-3}U_i(r^{-2})
 =e^{-\lambda r^2}\sum_{m=0}^{\lfloor(i+1)/2\rfloor}
 (-1)^m2A_{im}r^{2i-2m},
\quad
 A_{im}=\frac{(i+1)!\mu^{i+1-2m}}
 {\sqrt\pi\,2^{i+1}m!(i+1-2m)!}.
\]

Every exponent is a nonnegative even integer for i=0,...,8. This is an entire
function of r. The source factor 1/sqrt(pi), Hermite convention, and signs must
be retained; the Jacobian is absorbed exactly once into D_i.

Define \(Q_a(r)=1+ar^2\), \(h_a(r)=r^2/Q_a(r)\), and
\(c_a=ad+iq\hat z/2\). The exact source geometry can be rewritten as

\[
 m_a=c_ah_a,\quad n_a=m_a-d,
\quad
 B_a(r)=\pi^{3/2}r^3Q_a(r)^{-3/2}
 \exp\!\left[-\frac{a|d|^2}{Q_a(r)}
 -\frac{q^2h_a(r)}4+iqad_z h_a(r)\right].
\]

For positive real r these equal the original geometry. Near a real interval
including r=0, a sufficient new whole-box domain is Re(Q_a)>0, with explicit
positive margin, and corresponding bounds for the other coordinate and sigma.
One must use r^3 directly, not infer a global complex identity
\((r^2)^{3/2}=r^3\). Real equality plus holomorphic continuation on a connected
common domain supplies the branch justification.

If the second inverse coordinate stays in a compact positive interval, sigma
remains nonzero at r=0. All radial moments and center derivatives then have a
holomorphic extension to a sufficiently small neighborhood of that edge. The
transformed complete integrand is O(r^3) there. This statement is local; it does
not assert that an arbitrary large product ellipse satisfies the domain guards.

## Double-tail corner and exact scaling

At r=s=0, \(2\sigma=h_a(r)+h_b(s)\) vanishes. For odd k the leading radial
factor resembles \((r^2+s^2)^{k/2}\); in general there is no jointly holomorphic
extension at this point. Powers such as r^3s^3 multiplying it do not establish
joint holomorphy. No cancellation across the actual 107 terms is assumed.

In the real sector r>=s>=0, put r=rho and s=rho*v, 0<=v<=1. Define

\[
 A=1+a\rho^2,\quad B=1+b\rho^2v^2,\quad
 \Sigma=A^{-1}+v^2B^{-1},\quad
 \Delta=c_a/A-v^2c_b/B,\quad S=\Delta\cdot\Delta.
\]

The dot remains bilinear, not Hermitian. Exactly,
\(2\sigma=\rho^2\Sigma\), \(\delta=\rho^2\Delta\), and the hypergeometric
argument is \(-\rho^2S/\Sigma\). For radial derivative order n=0,1,2 define

\[
 K_{kn}=\Sigma^{k/2-n}
 \frac{\Gamma((k+3)/2)}{\Gamma(3/2)}
 \frac{(-1)^n(-k/2)_n}{(3/2)_n}
 {}_1F_1(-k/2+n;3/2+n;-\rho^2S/\Sigma).
\]

Then \(\partial_s^n M_k=\rho^{k-2n}K_{kn}\), where this derivative's s is
the original bilinear scalar, not the inverse coordinate. The implementation
must combine powers analytically before evaluating. It must never evaluate a
negative rho power and multiply by a compensating zero afterward.

For example the p-orbital factor becomes

\[
 E=\rho^k\widehat E,\qquad
 \widehat E=n_{1\alpha}K_{k0}
       +\rho^2\Delta_\alpha A^{-1}K_{k1}.
\]

The source displacement derivatives admit the same factoring. With
\(\eta=a/A\) for G1 and \(\eta=bv^2/B\) for G2, put
\(q_d=+2\eta\Delta_z\) for G1 and \(-2\eta\Delta_z\) for G2. Their common
p-orbital derivative part divided by rho^k is

\[
 \rho^2 n_{1\alpha}q_dK_{k1}
 +\rho^4\Delta_\alpha A^{-1}q_dK_{k2}.
\]

For alpha=z, add \((\rho^2\eta-1)K_{k0}+\rho^2\eta A^{-1}K_{k1}\) for G1,
or \(-\rho^2\eta A^{-1}K_{k1}\) for G2. This retains the pz derivative's
delta term. For an s orbital the derivative part is simply
\(\rho^2q_dK_{k1}\). The remaining log-base derivative is the unchanged
\(2a n_{1z}\) or \(2b n_{2z}\), and the overall negative derivative sign remains.

The Gaussian-base product contributes rho^6*v^3 and the sector Jacobian
\(|\partial(r,s)/\partial(\rho,v)|=\rho\). Each donor term consequently has
rho^(k+7)*v^3 times entire transformed densities and functions holomorphic on a
neighborhood where Re(A), Re(B), and Re(Sigma) have positive margins. Such a
neighborhood exists locally around each real point of the closed sector
rectangle: A,B are positive and Sigma>=1/A there. It is a new domain contract,
not an inference from the old Re(t)>0 guard. The other sector exchanges inverse
coordinates while preserving their physical parameters and donor indices.

## Finite-domain warning and disposition

The sector rectangle rho in [0,b], v in [0,1] describes the triangle
0<=s<=r<=b. For W3's finite epsilon=2^-96 the exact sector is instead
epsilon<=rho<=b and epsilon/rho<=v<=1. Replacing the latter lower limit by zero
includes additional physical tails beyond T=2^192. Those contributions cannot
be silently dropped or charged as zero. An alternative is a certified
infinite-tail integral with a new endpoint-inclusion contract and explicit
partition bookkeeping.

This is a viable future kernel-design route, especially if cutoff refinement
alone is insufficient. It is deferred now because the simpler source-bound
positive-tail polynomial can select a much smaller necessary finite T without
changing radial formulas, complex branch authority, or nested integration.
Required future acceptance includes exact transformed-density checks for every
i, real-axis enclosure overlap against the unchanged callback for all fields
and orbitals, odd-k and pz-derivative tests, whole-complex-box refusal tests,
sector-partition equality, strict ordered-107 aggregation, and actual bounded
integration. None is claimed complete here.
