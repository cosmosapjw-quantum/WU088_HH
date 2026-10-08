# Separated endpoint budget and finite cutoff selection

Status: derived source-bound bound, implemented with exact rational outward arithmetic. No HH callback, compact-interior integration, archived B192 computation, normalization, final D/epsilon decision, or production admission is implied. Actual execution evidence is a separate root-owned result.

## Fixed target and reason for the change

The pinned endpoint planner and Gaussian callback define a continuous positive-domain integral of the signed stored 107-term Frozen107 expansion. Primitive index 0 fixes active=0, field=O, orbital=s, ia=ib=0 and all stored parameters. The immutable W3 record uses lower cutoffs 1/256 and upper cutoffs 2^192; its actual positive endpoint bound is between 2^-21 and 2^-20. It is not a final D error budget.

A single simultaneous enlargement of both lower and upper ranges did not identify which side dominated. Inspection of that existing record shows the (i,j,k)=(0,8,1) and (8,0,1) terms contribute about 1.842e-7 each. This is only an explanatory decimal rendering of already stored rational evidence, not a new HH evaluation.

The selected design fixes lower cutoffs to 1/512, allocates the stricter endpoint-component budget 2^-21, and tests only T=2^32,2^40,2^48,2^56,2^64. The budget is strictly below the existing W3 exact bound; therefore passing it does not relax this component's previous accuracy. A successful smaller upper cutoff will require a new interior covering that exact chosen rectangle; neither old W1 nor a cutoff certificate alone supplies this interior.

## Weight and spatial bounds

Write the exact signed density in the pinned callback as

\[
\rho_i(t)=e^{-\lambda/t}\sum_{r=0}^{\lfloor(i+1)/2\rfloor}(-1)^r h_{ir}t^{-\nu_{ir}},\quad
\lambda=\mu^2/4,\quad\nu_{ir}=i+3/2-r,
\]
\[
h_{ir}=\frac{(i+1)!\,\mu^{i+1-2r}}{2^{i+1}r!(i+1-2r)!\sqrt\pi}>0.
\]

The engine's `hermite_coefficient` encloses exactly h_ir. The source Gaussian majorant supplies

\[
|F_k(t,u)|\le C_{F,k}(a+t)^{-3/2}(b+u)^{-3/2},\qquad t,u>0.
\]

All parameters, geometry, phase input and units retain the existing source conventions. This is a real positive-domain absolute-value inequality; it makes no holomorphy claim for a new compactified variable. In particular, the upper Gaussian mass decay was **already present** in the old engine; the problem is not a missing factor of t^-3/2.

Define positive majorant weights

\[
w_i^{(a)}(t)=e^{-\lambda/t}\sum_r h_{ir}t^{-\nu_{ir}}(a+t)^{-3/2}.
\]

Then, because exp(-lambda/t)<=1 and (a+t)^(-3/2)<=t^(-3/2),

\[
\int_T^\infty w_i^{(a)}(t)\,dt
\le U_i(T)=\sum_r\frac{h_{ir}}{p_{ir}}T^{-p_{ir}},\quad p_{ir}=i+2-r\ge2.
\]

For i=0,...,8 the powers lie in 2,...,10. Every coefficient is positive. At mu=1 this is exactly the expression in the existing `upper_mass_bound` before outward rounding; it is not a new asymptotic approximation. The inequality is valid at every positive T, so no unproved large-T threshold is used.

The existing engine provides L_i^(a)(l)>=integral_0^l w_i^(a) and

\[
W_i^{(a)}=L_i^{(a)}(1)+U_i(1)\ge\int_0^\infty w_i^{(a)}(t)\,dt.
\]

The pivot 1 is only a positive mass partition and preserves the source formula. The lower bound formula is an upper bound on omitted lower-domain mass, despite the label L.

## Disjoint two-dimensional complement

Partition the rectangle complement as `(outside_t x all_u)` disjoint union `(inside_t x outside_u)`. Let J_i^(a)(l,T) bound the inside-t mass. The prior result uses

\[
(L_i^{(a)}+U_i)W_j^{(b)}+\min(J_i^{(a)},W_i^{(a)})(L_j^{(b)}+U_j).
\]

Since min(J,W)<=W, a sufficient bound is

\[
(L_i^{(a)}+U_i)W_j^{(b)}+W_i^{(a)}(L_j^{(b)}+U_j).
\]

The original physical integration partition remains disjoint. Replacing inside mass by a larger whole mass is a conservative estimate; it must not be described as exact complement evaluation.

Multiplying by |c_ijk| C_F,k and summing the original stored term order gives

\[
B(l,T)\le B_{\rm lower}(l)+\sum_{p=2}^{10}A_pT^{-p},
\]
\[
B_{\rm lower}=\sum_{ijk}|c_{ijk}|C_{F,k}
 (L_i^{(a)}W_j^{(b)}+W_i^{(a)}L_j^{(b)}),
\]
\[
A_p=\sum_{ijk}|c_{ijk}|C_{F,k}
 \left[W_j^{(b)}\sum_{r:p_{ir}=p}\frac{h_{ir}}p
 +W_i^{(a)}\sum_{r:p_{jr}=p}\frac{h_{jr}}p\right]\ge0.
\]

Taking absolute coefficients only constructs a positive error majorant; all original signed input coefficient strings are preserved in term evidence. No coefficient is removed, altered, fitted, screened or silently cancelled.

## Certified computational form

At 128 bits, `up(q)` uses only integer comparisons, shifts and ceiling division to satisfy q<=up(q), with relative excess strictly below 2^-127 for positive q. Exact zero stays zero. The selector reproduces the pinned planner's upward-grid formula and tests it against that original function's AST without executing actual data.

The engine first encloses C_F,k, L_i, W_i, and h_ir. Their upper endpoints are rounded upward. Positive term products, positive sums, polynomial coefficients, each candidate polynomial and final lower-plus-upper sum are also rounded upward. Since every operation after absolute-value formation is monotone on nonnegative inputs, successive rounding preserves the inequality. Division is solely by positive integer p or the exact positive power T^p. The finite powers do not use host floating-point conversions.

The selector recomputes each distinct C_F,k once and requires exact equality with the immutable W3 term record after the same 128-bit relative rounding. The planner validates all canonical task/input/source identities before any new engine evaluation. All three pinned baseline files and the NPZ archive are byte-bound; the planner in turn binds the endpoint engine, input decoder and actual callback/assembly sources.

The chosen result is the **first passing member of the five fixed candidates**. Positivity implies monotonicity in T; nevertheless, the result makes no claim of global optimality among untested real or dyadic cutoffs. A lower-only bound above budget returns `LOWER_BUDGET_EXCEEDED`. Failure of all five candidates returns `NO_TESTED_CUTOFF_MEETS_BUDGET` without expanding the campaign.

## Implementation and validation limits

`select_cutoff.py` contains pure exact aggregation/selection functions and an explicitly enabled pinned evaluator. Default evaluator invocation refuses execution. The fixed actual campaign uses lower=1/512, bits=128, endpoint budget=2^-21, task=0 and the five stated upper exponents. Engine calls are cooperatively capped at 128 and 60 seconds; the root-owned executor must enforce the stated hard 512 MiB/wall isolation. Output is create-only and bounded at 2 MiB. No child launches or numerical HH callback are included in this module.

`test_select_cutoff.py` performs nine synthetic test functions: rounding enclosure/idempotence/error, direct expansion, non-dyadic outward arithmetic, candidate ordering/monotonicity, impossible lower/candidate budgets, invalid exact types, unplanned exponents, invalid powers/disabled actual execution, and comparison against the pinned rounding implementation. These establish implementation properties at the new algebraic boundary, not correctness of all source physics or final matrix decisions.
