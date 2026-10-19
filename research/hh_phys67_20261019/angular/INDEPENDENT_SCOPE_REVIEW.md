# Independent angular scope review of the first Born certificate

Date: 2026-10-19.  Reviewer: the angular subagent, separate from the
first-Born implementation author.  This is a read-only mathematical and
implementation-scope review.  No radial solver or campaign was run for it.

Reviewed files:

- `src/wu088_hh/phys67_first_born.py`, SHA256
  `c4f4c7c6adc72269ead632b3897f21c4cd0068ea3535df691cd1078f2ce7bb11`.
- PR115 `research/hh_phys66_20261018/r5/PROOF.md`, SHA256
  `c0f67c47c36f445494af3df52a9e09e27a853962b8f500ebe1572603febb68ca`,
  remote commit `445d82db9c42b4f2f81e4ac1b107dec3b69b3c24`.
- `src/wu088_hh/phys67_angular_certificate.py`, SHA256
  `43fc3097dddb2d3b15285998fb8895989522df38e35c0350505055427aef399e`.

## 1. The elementary angular identity has the original normalization

For m=0 the two normalized associated basis factors contribute
sqrt((2ell+1)(2ell'+1))/2.  The original radial coefficient V=2S
cancels this factor 1/2.  With d=r+t, reversing the d endpoints in
dmu=-d dd/(rR) gives the exact real-radius identity

\[
 V_{\ell\ell'}(r)=
 \frac{\sqrt{(2\ell+1)(2\ell'+1)}}{R}e^{-2r}
 \int_{-R}^{R}\left(1+\frac{t+1}{r}\right)
 P_\ell(\mu_r(t))P_{\ell'}(\mu_r(t))e^{-2t}\,dt,
 \qquad
 \mu_r(t)=-\frac{t}{R}+\frac{R^2-t^2}{2Rr}.
\]

Thus the Laurent coefficients include the complete potential angular
integral for the chosen pair; neither an angular multipole truncation nor
a Gauss rule is present.  The code's two contributions at powers k and
k+1 correspond to 1 and (t+1)/r.  The independent Coulomb agent's exact
recurrence check covers the actual ell=21, ell'=20 target separately.

The identity extends to Re(r)>R by holomorphy.  Indeed, for real mu in
[-1,1], Im(d^2)=2 Im(r)(Re(r)-R mu), which cannot vanish for nonreal r in
this domain.  On its real part d^2 is positive.  The principal root has no
cut crossing there, so both the original angular integral and the Laurent
expression are holomorphic and agree by the identity theorem.  The
first-Born callback's Re(r)>R guard therefore supports this identity on
the complex test balls used by validated integration.

## 2. The single first-order entry is independent of the projection

Write P(B,r)=diag(H_ell^+(r)/H_ell^+(B)).  The first forcing coefficient is

\[
 [D_1(B)]_{\ell\ell'}=
 \int_B^\infty
 \frac{H_\ell^+(r)H_{\ell'}^+(r)}
      {H_\ell^+(B)H_{\ell'}^+(B)}
 V_{\ell\ell'}(r)\,dr.
\]

There is no intermediate angular index.  Every orthogonal ell<=L
projection containing both external modes has this same entry.  This is
also the unrestricted first-Born forcing element for those modes.  The
claim `all_angular_first_order_entry=true` is therefore valid for the
reported individual m=0 element.  It is not a claim about the complete
nonlinear all-angular DtN response, its full first-order operator norm, or
all entries in an infinite matrix.

PR115's beta1 tail can consequently be applied with any
max(ell,ell')<=L<=64: the finite-projection entry and this exact first-order
entry have the same integrand and hence the same omitted radial tail.
Taking a matrix element of its finite-L operator-norm inequality is
contractive.  This transfer preserves PR114/115's finite-L Coulomb-ratio
premise and does not extend that premise to ell>64.

At order two, an intermediate-channel contraction occurs.  The argument
above then ceases to establish equality between finite-L and unrestricted
coefficients.  Higher-order excluded-angular control and the Born remainder
for the full physical response remain separate obligations.  Adding the
finite-L remainder to this one first-order number would not certify the
full-angular response.

## 3. Relationship with the all-signed-m Gauss certificate

The separate angular certificate proves an exact-rule operator-norm
error bound for all signed m in a chosen finite projection.  It applies
to the original multiplication matrix for Q>=L+1.  The elementary m=0
identity above removes that quadrature component altogether for the
selected element; these are compatible statements about different
evaluation paths.

The measured f64 sampling Gram defects in angular/RESULTS.json are
diagnostics only.  They are not enclosed errors and cannot serve as a
matrix error upper bound.  In particular, the exact-rule coefficient
2.222222...e-147 for L=64,Q=128 is not the error of the NumPy/SciPy matrix.
The angular certificate keeps all floating evaluation and roundoff
entries null.  Its proof and machine scope correctly retain this
distinction.  The first-Born implementation instead encloses the
elementary angular coefficients within its Acb arithmetic; that result
does not retroactively certify existing f64 campaign output.

## Decision

**PASS_SCOPED**: no blocking angular identity or projection-scope error
was found in the reviewed source.  Actual ball integration acceptance is
the root execution's returned-radius test and recorded certificate, not
this read-only review.  The source-driven xi, origin condition, incoming
adjoint, sigma(E), Maxwellian k_HH(T), and higher-order angular response
retain their individual obligations.  PHYS63 qualitative existence is
unchanged and HH_R10 remains OFF.
