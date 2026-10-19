# PHYS68: exact error certificates for saved values and inherited D1 consistency

## Fixed comparison objects

The completed PHYS68 certificate fixes the original atomic source,
B=27, T=65, k=7/10, eta_C=-10/7, m=0, external modes (21,20), and every
internal mode j=0,...,28.  Its cutoff D2 rectangle includes the validated
integration, Coulomb, exact angular evaluation and arithmetic errors.
The separate PR115 beta2 controls its difference from the infinite-radial
second Born coefficient in this same finite block.  It does not control
excluded angular modes or higher Born terms.

This unit reads that completed certificate, the two already completed
Rust outputs, the original stored PHYS66 pilot NPZ/JSON, and the inherited
PHYS67 first-Born certificate.  It launches no Rust executable and no
Volterra, quadrature, or D2 integration.

The original frozen source SHA256 is checked, the requested finite block
and complete status are checked, and the profile engine source hashes
are required to equal the executed binding.  Every consumed source/result
file and the comparison program itself is SHA256-bound in
SAVED_RESULTS_COMPARISON.json.  NPZ and JSON must encode the same pilot
binary64 value before the pilot comparison is admitted.

## Exact rectangle distance and radial remainder

Let the validated cutoff rectangle be

    C = [m_x-r_x,m_x+r_x] + i[m_y-r_y,m_y+r_y].

All m and r are decoded from the serialized integer mantissa/exponent
pairs into exact Fractions.  No informational decimal display is used.
Likewise, a stored binary64 approximation p=p_x+i p_y is decoded with
`as_integer_ratio` on each actual float.  Thus the comparison point is
the stored machine value, not a chosen decimal approximation to it.

Define d_x=|p_x-m_x| and d_y=|p_y-m_y|.  Elementary rectangle geometry
gives the exact squared extrema

    d_min^2 = max(0,d_x-r_x)^2 + max(0,d_y-r_y)^2,
    d_max^2 = (d_x+r_x)^2 + (d_y+r_y)^2.

The square roots are evaluated as Arb balls at 512 bits.  Their exact
downward and upward dyadic endpoints give L<=d_min and U>=d_max.  Since
the exact cutoff coefficient z_T belongs to C and
|z_infinity-z_T|<=beta2, the triangle inequalities prove

    max(0,L-beta2) <= |p-z_infinity| <= U+beta2.

The beta2 addition/subtraction uses exact Fractions.  It is added once.
For an exact modulus bound on the target, repeat the same rectangle
distance construction with p=0 and include beta2.  If 0<S_L<=|z_infinity|
<=S_U, the relative error satisfies

    E_L/S_U <= |p-z_infinity|/|z_infinity| <= E_U/S_L.

The code refuses a relative bound when S_L is not positive.  Every
reported interval endpoint is an exact stored rational; decimal strings
are labeled as approximate displays.  The recorded full radial Acb box
is also checked, by exact rational rectangle containment, to enclose the
cutoff rectangle enlarged by beta2 in each coordinate.  The numerical
L1 radius and numerical-plus-beta2 budget are checked exactly.

## Actual saved-value results

The following bounds include the finite-L28 radial beta2.  Rounded bounds
below are deliberately widened; exact endpoints are in the JSON.

| Stored complex value | Certified absolute-error interval [a0^-1] | Certified relative-error upper |
|---|---|---:|
| Rust RK4, 2432 steps | [5.87263006959e-56, 5.87263006970e-56] | 7.613975909e-9 |
| Rust RK4, 4864 steps | [3.76710724685e-57, 3.76710724782e-57] | 4.884125765e-10 |
| Existing PHYS66 L28,T65 pilot | [1.74866851127e-59, 1.74866862831e-59] | 2.267181936e-12 |

All three certified relative upper bounds are below 1e-6.  This promotes
the total error of each specific stored complex D2 value.  It does not
produce a uniform error bound for the Rust RK4 method, the PHYS66 solver,
or every element of a matrix.  The earlier two-resolution refinement
comparison is retained as a separate numerical diagnostic.

The PHYS66 pilot remains the earlier independently recovered C5-C8
artifact.  Reading its stored NPZ does not change the unresolved identity
of the separately requested final PHYS66 9933... archive.  The NPZ SHA is

    c5908fea305f07d4eda920fd6ce8bb6b6b2590a6055e39adf16b3652669ab25a.

## D1 consistency without an old integration rerun

The inherited PHYS67 certificate SHA is

    c3e8640db5296c3a522397780ce74f09e0e5db334a11b671cecc7ada07758f95.

Its full-radial rectangle for D1_(21,20)(B),m=0 is decoded from its older
`mid/rad` serialization.  The new PHYS68 cutoff rectangle for the same
entry uses `midpoint/radius`; beta1 is then added as an exact enclosing
Cartesian square.  Exact endpoint comparisons prove that the whole new
full-radial rectangle lies inside the inherited full-radial rectangle.

This is stronger than mere overlap and confirms consistency of the two
saved certificates.  No old PHYS67 integral or PHYS66 solver was rerun.
D1 has no intermediate angular sum, so this same external entry is
unchanged by a finite projection containing the two external modes.

## New profile reuse witness

The recorded panel 75 is centered at 109/4=27.25 and covers [27,27.5].
The profile loader validates source, engine/runtime fingerprint, panel
payload hash, manifest membership, pair coverage and full intermediate
sum.  It restores the saved Volterra primitive at the panel center and
regenerates the exact coefficient formulas, without integrating again.

Two new point outputs were computed at r=219/8=27.375, offset 1/8:

    D1_(20,21)^T(r), D1_(21,28)^T(r).

Both returned finite Acb enclosures.  For each pair, the decoded q-center
ball exactly contains the saved dyadic q-center rectangle, and a center
evaluation overlaps the original stored D1-center ball.  The latter
comparison permits harmless widening from outward ball deserialization.
It is not mislabeled as byte equality.  These are two cutoff-profile
evaluations with no radial tail added; they are not a new claim about a
global uniform profile error.  Exact output rectangles and identities
are in PROFILE_EVALUATION_WITNESS.json.

## Validation and invalidation

Eight focused arithmetic tests pass.  They verify exact 3-4-5 rectangle
geometry, outward square-root inequalities as rational inequalities,
radial-tail addition, relative-error refusal at zero scale, exact
binary64 subnormal decoding, and old/new serialization containment.
The actual comparison execution and new profile evaluations exited 0.

Changed result bytes, source/engine bindings, finite block, external
indices, radial cutoff, or arithmetic program invalidate the associated
comparison receipt.  The minimal response is to recheck and recompute
the affected comparison; it is not to rerun every underlying campaign.
All algorithm-wide, excluded-angular, original source-driven xi,
origin/incoming-adjoint and physical-rate obligations retain their own
scope.  PHYS63 remains ESTABLISHED and HH_R10 remains OFF.
