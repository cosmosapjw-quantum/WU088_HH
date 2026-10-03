# Independent source/theory review of endpoint cutoff selection

Verdict: the source-bound positive-majorant decomposition and fixed finite
candidate selection are accepted for the stated component scope. This is a
pre-execution review; it does not assert any actual new endpoint value, complete
interior integral, normalized primitive, final D error, or production admission.

Reviewed implementation SHA-256:
`7a8a4d9fc10d79ba08d7c9eb015bd814559d9c970ec008404b7e45d1a055a759`
for `tail_bound/select_cutoff.py`. The owner supplied nine pure arithmetic/source
tests; this reviewer inspected them but did not rerun them or count them as
independent scientific evaluations. No callback or endpoint engine execution
was performed by this reviewer.

## Derived implication

For a fixed donor term, let L_i be the existing certified nonnegative bound on
the lower tail [0,l), W_i a bound on the entire positive density-envelope mass,
and U_i(T) the existing upper-tail bound. The source theorem first partitions
the rectangle complement as

\[
 (E_t\times\mathbb R_+)\;\dot\cup\;(I_t\times E_u).
\]

Its term bound is C_F[(L_i+U_i)W_j+J_i(L_j+U_j)]. Since the interior envelope
mass J_i <= W_i, a safe replacement is

\[
 C_F(L_iW_j+W_iL_j)+C_F(U_i(T)W_j+W_iU_j(T)).
\]

The larger factors may overcount positive bounds; they do not alter the
disjoint integral partition or lose any region. The exact original upper-tail
formula is

\[
 U_i(T)\le\sum_{m=0}^{\lfloor(i+1)/2\rfloor}
 \frac{A_{im}}{i+2-m}T^{-(i+2-m)}.
\]

Every coefficient is nonnegative and every integer degree p=i+2-m is in 2..10
for i=0,...,8. Multiplication by |C_ijk|C_F and summation therefore produce
\(B_L+\sum_{p=2}^{10}A_pT^{-p}\). Upper bounding all positive coefficients and
positive partial sums by upward rounding preserves the inequality. This
includes the implementation's additional upward rounding of |C_ijk|C_F before
it is used. No signed cancellation is used for the endpoint bound; the actual
signed continuous source target is unchanged.

The nonnegative polynomial is monotone nonincreasing in real T>0. Candidate
selection uses exact rational predicates and reports the first passing member
of {2^32,2^40,2^48,2^56,2^64}, explicitly not a globally optimal cutoff. A failure
of this computed majorant to meet budget would be inconclusive about the true
tail error, not a proof that the true error exceeds budget.

## Accuracy comparison and source binding

The old W3 certified endpoint radius is exactly

\[
 R_{\rm old}=\frac{90690421389980920232708863295172494873}
 {178405961588244985132285746181186892047843328}.
\]

The new declared budget is 2^-21, strictly smaller, with exact difference

\[
 R_{\rm old}-2^{-21}
 =\frac{5619829659746304366865211437230442009}
 {178405961588244985132285746181186892047843328}>0.
\]

Thus an actually computed new bound <=2^-21 necessarily improves the prior
actual endpoint ceiling. The budget ratio is approximately 0.938032820075.
Moving l from 1/256 to 1/512 expands the auxiliary interior lower range and
reduces the true lower-tail region. Reducing T contracts its upper range. These
are separate endpoint-design changes to a finite auxiliary window, not a
change to the infinite-domain source target. They do not establish a final D
accuracy goal or relax the current interior tolerance.

The selector pins the old plan/result/input/planner bytes and delegates complete
plan/result validation to that unchanged planner. The planner in turn verifies
the endpoint engine, input adapter/decoder/spec, assembly and callback source
pins. Its result validator checks complete term count/order and the old rounded
arithmetic, so the selector's zip over terms cannot silently truncate an
otherwise accepted old record. The new code also recomputes each distinct C_F
once and requires exact agreement with the old W3 recorded majorant.

The root must retain actual execution/source/result identities and enforce the
declared hard process caps externally; the imported selector API's wall checks
are cooperative. Its CLI output is create-only, but its final file is created
after calculation, so concurrent invocations of the same output name are not a
general duplicate-execution lock. The declared single root-owned invocation
avoids that issue in this campaign. This observation is not a blocker for the
current contract and is not a claim of a resumable production scheduler.

The old engine's exponential evaluator uses absolute rational quantization
internally. At lambda/l=128 this may leave a positive floor much larger than
the mathematical exp(-128). Therefore the achieved lower contribution must be
reported from the actual outward calculation; asymptotic intuition alone must
not be used as its numerical certificate.

## Required result readback

Before a numerical conclusion is stated, verify the new result's selector and
input/source identities; all positive terms and their aggregate coefficients;
all five exact candidate predicates; selected candidate minimality within the
declared finite set; and the strict old-radius comparison. An independently
computed original-engine endpoint result for that same selected window is a
useful separate cross-check, not a rerun of an already completed interior.
That result still supplies no W3/new-window interior or D certificate.
