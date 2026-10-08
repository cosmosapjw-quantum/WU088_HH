# Independent bounded review of T3

**Result: no material mathematical defect found in the stated protected
domain.** The author corrected one wording point about the minimum-normal
spacing boundary. This review approves the conditional theorem, not actual
scalar provenance, SVD accuracy, historical execution, or a scientific verdict.

Reviewed final documents:

- T3_FROZEN_PREDICATE_THEOREM.md:
  f623a3ce0580505e5a687673d1103582aac4901fb42e87b0b2ba7e7b3e4da0a1.
- T3_FROZEN_PREDICATE_THEOREM.json:
  e1e2bed3d4008172f83dee2b9931184d45141520d962454e6b4ecae10a48ff71.

The reviewer is the separate T2 author, /root/g2_decoder, not the T3 author.
The five source identities listed by T3 were rehashed successfully. The exact
PRIMARY and SECONDARY source expressions and the float(norm(...,2))/Dmax
path were read as text; no scientific comparator or array loader was run.

## Mathematical assessment

1. The rounding-preimage table follows from the adjacent representable
   midpoint cells and the parity of their endpoints. It correctly uses
   distinct real neighbors for negative thresholds, merges signed zeros
   only for comparisons, and distinguishes the two half-spacings at a binade
   boundary. Missing finite neighbors are refused.
2. For the common weak guard, substitution into the lower midpoint yields
   \(g>-\tau-h_-(a)\), with equality accepted exactly for even \(a\).
   The sufficient condition \(g\geq-\tau\) follows independently from
   monotonicity of rounding. It is correctly not asserted necessary.
3. The frozen tolerance has odd significand. PRIMARY therefore accepts
   exactly \(g\geq\tau+2^{-87}\), including the tie that rounds to its even
   successor. SECONDARY instead uses \(\tau+h_+(a)\), accepting its boundary
   exactly for odd \(a\); the largest-finite local operand is handled
   separately. The two source expressions are not interchanged.
4. All three synthetic nonimplication examples are valid with represented
   finite operands. A true exact-tolerance mathematical gap alone need not
   pass PRIMARY or SECONDARY; a machine weak equality can fail ideal weak
   nonworsening.
5. Every guard is antitone in the local scalar and monotone in the other
   scalar. The worst-corner sufficient test follows. Its necessity for
   universal support is correctly limited to unconstrained Cartesian
   operand boxes. Correlations can only make that test conservative.
6. The forward-error bridge does not manufacture scalar error bounds.
   Source code calling a norm or an SVD is not treated as proof of a
   correctly rounded mathematical norm. Fixed models, common-target
   perturbations, stored versus constructed K, actual scalar bits, and
   historical execution remain separately stated premises.
7. Finite decision of authenticated point operands is distinguished from
   acceptance based on shrinking analytic enclosures. Positive guard margins
   or exact boundary/cell information are needed for the stated semidecision
   argument. The theorem does not promise success under a fixed resource
   cap or a nonvanishing unresolved forward-error bound.

## Resolved wording point

T3-R1 concerned the phrase that half-spacing increases at a power of two.
At the minimum normal number the spacing is the same as the subnormal
spacing. The needed fact is nondecrease everywhere, with doubling at normal
binade boundaries above the minimum normal. The author made this change
before the final hashes above. The original wording did not affect the
sufficient inequality, and no formula or executable helper changed.

## Independent exact checks

A separate exact Fraction implementation rounds by binary search over the
finite nonnegative binary64 value lattice, compares distances to adjacent
values, resolves ties by endpoint parity, and reflects negative arguments.
It imports neither the T3 helper nor the author's earlier rounding oracle.

It passed 784 rounding-preimage comparisons, 816 point-predicate comparisons,
32 universal small-box comparisons, the three counterexamples, and five
explicit source-operand midpoint equalities. The latter include the odd
tolerance PRIMARY tie and even/odd SECONDARY and weak ties. All arithmetic
was exact and synthetic; no host float norm or scientific value was used.

The complete standalone check code, its actual successful execution result,
and final source hashes are embedded in T3_INDEPENDENT_REVIEW.json for
reproduction. Tests corroborate the stated algebra; the proof is the
rounding-cell and monotonicity derivation, not the test count.

This bounded review leaves no open material finding within its scope.
Actual HH runs, actual arrays, and native builds: zero.
Historical ABI/trace admission, norm-correct-rounding admission and project
scientific decision admission remain false. No certified epsilon/eta is
issued.
