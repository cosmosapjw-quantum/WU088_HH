# T3 — Exact certificates and the frozen binary64 predicates

**Result.** The source expressions have exact rational threshold preimages, including every equality case in the protected finite domain below. An exact mathematical Pareto certificate alone does not certify either archived machine verdict. It can certify a machine expression when separately established scalar operand identities or forward-error bounds satisfy the stronger, source-specific tests proved here. Nothing here establishes correctly rounded norms, historical execution, ABI admission, or an actual scientific margin.

## 1. Source binding and premises

Paths are relative to the repository root. The following exact source bytes were read; none of the scientific comparators was executed.

| ID | Source and lines | SHA256 | Binding |
| --- | --- | --- | --- |
| T3-S1 | `research/r31ao_unequal_ladder/ncp_preflight_20260930/B192_REPLAY_EXECUTED_COMPARATOR.py:93–105` | `43c3edac4d6f32ecb0ebd68619db76d447d40627610e63ec4000c3d5983732c8` | PRIMARY expressions; secondary helper call |
| T3-S2 | `research/r31al_z075_gate/refinement_gain.py:40–48` | `a81a386f5aa5138012a26e833d468606a91ce4857dcc94311d878ae7976875c3` | SECONDARY expressions, float conversion, finite/nonnegative checks |
| T3-S3 | `research/r31al_z075_gate/compare_secondary_refinement.py:25–36,71–81` | `f8fb529fe4f2d6413f34372580e69bc4b7919e2a4e7c6ef2320949d7ca9c430f` | `float(norm(...,2))`, Dmax, rounded truth K, stored prediction K |
| T3-S4 | `research/r31ao_unequal_ladder/gap_closure_20261001_g0_g6_v1/exact_gram/engine.py:309–438` | `e10f206d63be1a99a441780108619574605014a9b01b3b327e21fecb18c5b9cc` | Immutable exact scalar audit and separate real-gap rule |
| T3-S5 | `research/r31ao_unequal_ladder/gap_closure_20261001_g0_g6_v1/REPRESENTED_GAP_CONTRACT.json` | `f71febdab692f93208ef6339adb965e633ec7d22ff71753f0c3178da8acd078a` | Existing B08 distinction and claim ceiling |

For each of the two metrics, write `a` for local/R31AK and `b` for the competing model's **machine scalar**, interpreted as its exact binary64 dyadic value. PRIMARY uses R31Z; SECONDARY uses R31AD. Let

\[
\tau=\operatorname{value}(\mathtt{3ddb7cdfd9d7bdbb})
=\frac{7737125245533627}{77371252455336267181195264}.
\]

This is the exact frozen `1e-10` binary64 token, not the distinct real number \(10^{-10}\). Let \(R\) mean correctly rounded binary64 round-to-nearest, ties-to-even **for the indicated scalar addition/subtraction only**. The source bindings are

\[
W(a,b): a\le R(b+\tau),\quad
P(a,b): R(b-a)>\tau,\quad
S(a,b): a<R(b-\tau).
\]

Local support is \(W_1\land W_2\land(P_1\lor P_2)\) for PRIMARY and \(W_1\land W_2\land(S_1\lor S_2)\) for SECONDARY. Reverse support is obtained by exchanging `a,b`; its protected-domain checks must be made again after exchange. The theorem preserves these expressions rather than algebraically rewriting the source before rounding.

**Explicit premises.** Operands are finite nonnegative binary64 numbers; signed zeros compare as the same real zero. Scalar operations use the stated rounding mode with gradual underflow, no flush-to-zero, no alternate precision/double rounding, and no reassociation. Let \(F\) be the largest finite positive binary64 number. The applied sufficient tests require exact \(b+\tau\le F\); then \(b-a\) and \(b-\tau\) also lie in \([-F,F]\). This deliberately conservative protection refuses even some additions above \(F\) that might round back to \(F\). Nonfinite operands, unsupported modes, and unproved scalar semantics are outside the implication. No premise about the rounding accuracy of `norm`, SVD, matrix arithmetic, or array casts is smuggled into `R`.

## 2. Exact rounding preimage lemma

Merge the two zero encodings for real comparisons. For a finite representable threshold `q`, let \(q^-<q<q^+\) be its adjacent **distinct real** binary64 numbers and define

\[
m_-(q)=\tfrac12(q^-+q),\qquad m_+(q)=\tfrac12(q+q^+).
\]

Let \(E(q)\) mean that the least significant bit of its stored significand is zero; equivalently, the finite encoding's low bit is zero. Zero is even. Use a row only if its required neighbor is finite.

| Rounded comparison | Exact preimage for real `x` | Equality at the cut |
| --- | --- | --- |
| \(R(x)\ge q\) | \(x>m_-(q)\), or \(x=m_-(q)\land E(q)\) | Accepted iff `q` even |
| \(R(x)>q\) | \(x>m_+(q)\), or \(x=m_+(q)\land\neg E(q)\) | Accepted iff `q` odd |
| \(R(x)\le q\) | \(x<m_+(q)\), or \(x=m_+(q)\land E(q)\) | Accepted iff `q` even |
| \(R(x)<q\) | \(x<m_-(q)\), or \(x=m_-(q)\land\neg E(q)\) | Accepted iff `q` odd |

**Proof.** In the real ordering, the closest representable number changes from \(q^-\) to \(q\) at their midpoint and from \(q\) to \(q^+\) at theirs. Adjacent significands have opposite low-bit parity, including at a binade boundary and the subnormal/normal boundary. At a midpoint the even endpoint wins. Thus the cell rounding to `q` has both endpoints included if `q` is even and both excluded if odd. All lower/higher cells are ordered, yielding the four rows. For zero the adjacent values are \(\pm2^{-1074}\), so its real rounding cell is \([-2^{-1075},2^{-1075}]\); signed-zero choices do not alter any comparison. Negative thresholds follow from the same real ordering, not from unsigned encoding order. This proves the lemma directly from the specified rounding rule.

The table uses exact dyadic midpoints, not a relative-error approximation or a blanket `nextafter` adjustment. At \(q=\pm F\), a missing-neighbor row is refused. The application needs only the lower neighbor at `a=F`; SECONDARY strict is then explicitly false since \(R(b-\tau)\le F=a\). Overflow is not silently represented by a finite endpoint.

## 3. The exact point-scalar theorem

Put \(g=b-a\), \(h_-(a)=(a-a^-)/2\), and \(h_+(a)=(a^+-a)/2\). The lemma gives:

| Actual source predicate | Exact gap condition | Equality rule |
| --- | --- | --- |
| Common weak \(W\) | \(g>-\tau-h_-(a)\) | Also accepted at equality iff \(E(a)\) |
| PRIMARY strict \(P\) | \(g>\tau+h_+(\tau)\) | Also accepted at equality iff \(\neg E(\tau)\) |
| SECONDARY strict \(S\) | \(g>\tau+h_+(a)\) | Also accepted at equality iff \(\neg E(a)\) |

For the frozen tolerance, \(E(\tau)\) is false and \(\operatorname{succ}(\tau)-\tau=2^{-86}\). Consequently,

\[
\boxed{P(a,b)\iff b-a\ge \tau+2^{-87}.}
\]

This equality is accepted because the exact midpoint rounds to the even successor of the odd tolerance. It is not accepted merely because an inequality was weakened by convention.

**Proof.** Substitute `x=b+τ,q=a` into the first row of the lemma for weak support. Substitute `x=b−a,q=τ` into its second row for PRIMARY; substitute `x=b−τ,q=a` into its second row for SECONDARY. Subtract `a` exactly to obtain the displayed gap conditions. The source expressions themselves remain unchanged. At `a=F`, SECONDARY strict is false as specified above.

It follows at once that \(g\ge-\tau\) is sufficient for the common machine weak predicate: it places \(b+\tau\ge a\), and monotonicity gives \(R(b+\tau)\ge R(a)=a\). The converse fails. A merely strict real improvement \(g>\tau\) does not generally imply either machine strict predicate. Machine strict implies \(g>\tau\), but complete machine Pareto support need not imply the real weak condition in the other metric.

## 4. Three exact synthetic counterexamples

These are invented scalar examples. They are not scientific errors or gaps.

1. **Real support does not imply PRIMARY; SECONDARY does not imply PRIMARY.** Let \(u=2^{-86}\), \(b=\tau+u=\operatorname{succ}(\tau)\), and \(a=3u/4\), all finite representable operands. Then \(g=\tau+u/4>\tau\), but \(R(g)=\tau\), so PRIMARY strict is false. In contrast, \(R(b-\tau)=u>a\), so SECONDARY strict is true. Give the second metric `a=b=0` to obtain full Pareto verdicts: real and SECONDARY true, PRIMARY false.
2. **Real support and PRIMARY do not imply SECONDARY.** Let \(b=1\) and \(a=R(1-\tau)\). Here \(b-a>\tau+2^{-87}\), hence PRIMARY strict is true, while SECONDARY strict is `a<a`, hence false. The exact Fraction check verifies the displayed inequality without a host floating calculation. A second zero metric again gives full verdicts. Moving `a` one representable step down makes SECONDARY strict true.
3. **Machine support does not imply real weak nonworsening.** Let \(b=1\), \(a=R(1+\tau)\). Exact dyadic comparison gives \(a>1+\tau\), hence \(g<-\tau\), but machine weak is true by equality. With second metric `a=0,b=1`, both machine Pareto rules support the local model although real Pareto nonworsening fails.

Thus neither strict machine rule implies the other globally, and neither full machine rule is interchangeable with the source-ideal real rule. The failures occur with finite representable operands and the unchanged tolerance.

## 5. Robust scalar-enclosure sufficient tests

Suppose separate valid evidence establishes machine operand enclosures
\(a_j\in[L_{a,j},U_{a,j}]\), \(b_j\in[L_{b,j},U_{b,j}]\), with exact rational endpoints and finite nonnegative binary64 operands. Intersect each closed interval with that finite lattice. Let \(a_j^{\max}\) be its greatest admissible local scalar and \(b_j^{\min}\) its least admissible other scalar. Empty intersections are inconsistent premises and are refused. Require the entire other-scalar box to satisfy \(b+\tau\le F\).

Evaluate the **point theorem** at \((a_j^{\max},b_j^{\min})\). If both weak predicates and at least one corresponding strict predicate hold there, the actual source expression holds for every scalar pair in the box. Equality is handled by the point theorem, including the parity of the endpoint, rather than discarded or relaxed.

**Proof.** `R` is monotone. Each of `a≤R(b+τ)`, `R(b−a)>τ`, and `a<R(b−τ)` becomes no easier when `a` increases or `b` decreases. The selected endpoint pair is therefore a worst case for each predicate. Conjunction and disjunction preserve this implication. For an unconstrained Cartesian product of the two metric boxes, the endpoint criterion is also necessary for universal support, since the combined worst corner is itself admissible. Correlations can make it conservative when the true feasible set is smaller. An inconclusive endpoint test means unresolved, not that the actual verdict is false.

The lattice endpoints are constructible by integer bisection over finite nonnegative binary64 encodings (at most 63 bisection steps per endpoint). Their computation requires no norm or SVD. This is only a finite theorem-check construction, not a new production certificate pipeline.

**How an exact error interval can supply a premise.** If \(e_a\in[A_l,A_u]\) is an exact mathematical error and independently proved \(|a-e_a|\le\rho_a\), then use \([\max(0,A_l-\rho_a),A_u+\rho_a]\) as a machine operand enclosure, and similarly for `b`. The bound \(\rho\) must include every relevant cast, matrix construction/subtraction, norm, and Dmax step; no such bound is supplied by this theorem. Alternatively, if the much stronger premise \(a=R(e_a)\) has separately been proved, monotonicity supplies \([R(A_l),R(A_u)]\). Source code containing `float(norm(...,2))` does **not** establish that stronger premise.

For a gap-only bridge, if \(g^*=e_b-e_a\ge G\) and the two independently established scalar errors are \(\rho_a,\rho_b\), then
\[
b-a\ge B:=G-\rho_a-\rho_b.
\]
Both \(B_j\ge-\tau\) and at least one \(B_j\ge\tau+2^{-87}\) suffice for PRIMARY. For SECONDARY, an additional finite representable local upper bound `A<F` allows the simpler conservative test
\[
B_j>\tau+h_+(A_j),
\]
for at least one metric, with the same weak tests. This is sufficient because \(h_+(a)\) is nondecreasing on the nonnegative finite lattice: constant in the subnormal range and each binade, nondecreasing across all boundaries, and doubling at normal binade boundaries above the minimum normal. This conservative formula intentionally excludes equality; the exact box test above retains all certifiable equality cases. A gap alone has no scale information from which to determine the SECONDARY local half-spacing.

## 6. What the exact target certificate establishes

For fixed, correctly bound model matrices, a common target perturbation bounded by \(\epsilon_j\) changes each spectral-norm model error by at most \(\epsilon_j\), and the difference of two such errors by at most \(2\epsilon_j\). The same conclusion holds for Dmax by the 1-Lipschitz property of `max` in the componentwise sup norm. Thus an exact represented gap enclosure \([g_j^-,g_j^+]\) implies the source-ideal target gap lower bound
\[
G_j=g_j^- - 2\epsilon_j.
\]
If \(G_j\ge-\tau\) for both metrics and \(G_j>\tau\) for one, the **mathematical target** obeys that exact-tolerance Pareto rule. Exact decimal tolerance requires a separately named rule. This statement needs the fixed-model and common-target premises; it is not permission to replace archived model K, rounded source K, or cast matrices by different mathematical objects.

There are three separate routes, none automatically admitting another:

1. Exact gap plus target bound proves a source-ideal mathematical relation under its matrix bindings.
2. Authenticated frozen scalar bit patterns plus the point theorem proves the scalar source decision on those bits, under the scalar execution premises.
3. Independently certified bounds tying mathematical errors to machine scalars plus the enclosure theorem transfer a mathematical certificate to the machine expression.

Route 1 supplies no SVD forward-error theorem and does not establish route 2 or 3. Route 2 does not establish an exact continuous target. Source/byte identity, ABI, correctly bound matrices and scalar outputs, arithmetic behavior, and historical execution remain distinct obligations. No archived scalar trace or actual matrix was evaluated here.

## 7. Finite termination and boundary cases

Known representable point operands admit a finite exact decision, including midpoint equality, because all cuts and parity bits are exact. For a sequence of shrinking analytic enclosures, finite acceptance is a **semidecision** guarantee only when every necessary weak guard and at least one strict guard has a positive separation from its acceptance cut, or an exact equality/cell-isolation argument supplies the missing boundary information. Convergence alone does not imply that a lower bound ever reaches a weak equality: bounds \(-\tau-1/n\) approach an accepted real weak boundary from below forever. Likewise, an exact quantity on a rounding midpoint can leave both neighboring rounded outputs in interval images indefinitely unless its tie is resolved exactly. Replacing a strict test by a weak one would change the theorem and is forbidden.

If the relevant positive guard margin is `d>0` and enclosure widths tend to zero with a constructive accuracy schedule, requesting widths sufficiently below `d` yields a finite successful stage. The unknown margin, unresolved operand bindings, fixed residual forward-error bounds, or a fixed resource cap may prevent acceptance. There is no unconditional finite acceptance, fixed-budget closure, or numerical scientific margin claim.

## Verification and claim ceiling

`theory_checks/t3_GREEN.log` records 12 passing tests under a 20-second/256 MiB guard. The checks cover all four preimages at and around both midpoints for positive and negative thresholds, signed zero, subnormals, the normal boundary, binade transitions, tolerance parity, the three counterexamples, scalar-source agreement, exhaustive small operand boxes, and explicit overflow/nonfinite refusals. Midpoint tests use exact Fractions and compare with the immutable scalar-only integer rounding oracle T3-S4; they do not run its matrix or scientific paths. The proof is the derivation above, not the test count.

`T3_FROZEN_PREDICATE_THEOREM.json` binds source hashes, evidence, assumptions, and remaining obligations. Status: conditional mathematical implication established for the stated domain; actual source-operand linkage unverified. `rigorous=false`, `certified_epsilon=null`, `certified_eta=null`, `independent_review_admitted=false`; no actual HH run, native build, historical trace admission, or physical promotion.
