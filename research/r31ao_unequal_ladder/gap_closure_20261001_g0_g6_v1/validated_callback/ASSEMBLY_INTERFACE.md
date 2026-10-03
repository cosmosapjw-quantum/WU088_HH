# Post-real-domain assembly interface

Implementation: `assembly.cpp` / `assembly.hpp`. Status: source-bound native draft, not compiled or executed. This module performs no callback or integral evaluation and does not admit a certificate.

## Exact input boundary

`AssemblyInputs` receives exact rational lifts from the separately verified decoder. The loader must verify the Frozen107 archive/member identities in `EXACT_INPUT_AND_CALLBACK_BINDING.json` and supply semantic indices, not raw memory-order indices. In particular, s_C and p_C are stored Fortran-order arrays; the semantic value `[primitive, orbital_column]` goes to `array[primitive*12+orbital_column]`. Scalar and coefficient conversion must use exact integers/rational strings, never host floating intermediates or shortened decimal strings.

| Member | Native semantic shape | Authority |
|---|---:|---|
| exponents | 12 | archived exact positive represented values |
| s_C, p_C | 12×12 | archived orbital coefficient values, signed |
| donor_C | 9×9×9 | archived C values, direct monomial coefficients |
| phase_E | 49 | archived represented phase energies |
| pref, v | scalar | archived values; no recomputation |
| z | scalar | exact 3/4 |

The objects do not themselves prove the archive identity. An actual execution must bind these values to decoder/provenance output; that executable loader remains open. The algebra functions are usable for synthetic data without claiming a Frozen107 binding.

`stored_donor_terms` preserves all supplied nonzero signed coefficients and their i,j,k indices. It does not read the donor rational polynomial and does not regenerate C. The 1..107 term guard permits small synthetic fixtures; the real input loader must separately establish the pinned full payload and expected nonzero pattern. `canonical_parameters` implements source active=0/1 with real q held fixed under center derivatives, transverse displacement 2, z=3/4, mu=1 and a,b from the selected stored exponents.

## Integral boundary and normalization ownership

`RealDomainPrimitiveIntegrals::unnormalized_real_domain_integrals` contains 2×3×3×12×12 complex balls indexed by `(active,field,orbital,ia,ib)`. Fields are O,G1,G2; orbitals are s,px,pz. Every entry must enclose the whole real-positive dt du integral of `polynomial_field`, including the chosen interior plus disjoint endpoint complement **before** orbital normalization. No source quadrature weights, Jacobians, phase, parity or coefficient contraction belongs in this array.

This is a mathematical precondition, not inferred from a finite ball or a caller-supplied boolean. Interior/endpoint proof artifacts, ball radius convention, method caps and array provenance must accompany an actual use. A caller must not feed already normalized primitive balls: the assembly multiplies each primitive exactly once by

\[
N_\ell(a,b)=\sqrt2\,\mathrm{pref}\,(2a/\pi)^{3/4}(2b/\pi)^{3/4}
\times\begin{cases}1,&\ell=s,\\2\sqrt a,&\ell=p_x,p_z.\end{cases}
\]

`normalization_factor` uses Arb/Acb outward operations on exact input values. This is the ideal mathematical normalization in the source-functional target, not the old adapter's binary64-rounded normalization. Thus the old adapter's rounding discrepancy remains within the eventual target-to-B192 error; no extra old producer error is added.

## Source-prescribed assembly

Rows are `(active=0,j=0..23)` followed by `(active=1,j=1..23)`. Angular channel is j//8, orbital column j%8. The ground contraction coefficient is always `s_C[ib,0]`. Each term is multiplied by `C_neutral[ia,j%8]*s_C[ib,0]`; signed coefficients remain signed. The raw active arrangement is `active XOR cusp`.

At cusp=1, p orbitals receive a minus sign and G1/G2 receive another minus sign. The source phase is evaluated outward as `exp(i*(2*kc*cz+(E_N-E_I)*(z/v)))`; kc and cz each reverse sign with cusp. The exact rational ratio is evaluated through a containing ball, never substituted by a printed tau. After this phase, the original D formulas apply. Only this final assembly translation unit contains literal `acb_conj`; the analytic callback has none.

Output shapes and storage:

| Output | Semantic shape | Flattened index |
|---|---:|---|
| components_OG | 3×47×2 | `(field*47+row)*2+cusp` |
| O, D_col | 47×2 | `row*2+cusp` |
| O_row, D_row | 2×47 | `cusp*47+row` |

No symmetrization, fitted phase, independent dotO reconstruction, H field, or model promotion occurs. Source normalization and source assembly are entirely separate from the analytic callback, preserving the post-real-integral conjugation boundary.

## Execution and remaining obligations

The draft rejects invalid indices, a changed exact z, nonpositive Gaussian exponents, zero v, nonfinite primitive/result balls and precision outside 32..4096 bits. Any assembly failure invalidates every output. A future bounded workload may choose a smaller precision/work cap; this hard draft bound is not a demonstrated usable precision budget. Call `assemble_real_domain` only after the integration proof and exact input binding have closed.

`test_assembly.py` checks exact synthetic signed contraction, registry order, all 18 orbital/field/cusp reflection combinations, exact tau/phase arguments, and final complex D algebra against separately written source formulas. Native tests in `native_synthetic.cpp` additionally cover normalization ratios, canonical geometry, one-hot tensor contraction, phase/cusp relations, adjoint placement and rejection; those tests remain uncompiled and unexecuted.

Remaining: actual decoder-to-native loader and sealed parameter identity; pinned native compilation/ABI/runtime tests; integration/endpoint evidence with the declared unnormalized ownership; rigorous serialization and final epsilon aggregation; authorized real workload. This source-only implementation does not provide actual O/G/D balls or a numerical certificate.
