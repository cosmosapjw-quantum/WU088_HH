# PROOF_OBLIGATIONS_AND_STOP

## Scope and present status

Focus: certify the represented B192 mixed D_col/D_row relative to the same fixed Frozen107 continuous source functional, for the two frozen decisions at z=0.75. This task supplies a proof design and a source map. It executes no numerical certificate, producer, new sample, native compile or old test/postprocessor. No additional authorization scope is issued.

`SOURCE_ACCURACY_BOUND_UNAVAILABLE`

`RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`

rigorous=false; certified epsilon_C/epsilon_R/epsilon_K/epsilon_Dmax=null; diagnostic eta bounds=null. Established below means source/evidence identity or an existing contract, not an end-to-end mathematical certificate. Derived means a mathematical implication under its stated premises. Missing means needed project authority or a quantitative enclosure has not been supplied.

## A telescoping partition that avoids double counting

Define hybrid blocks X0,...,X8 with exact mathematical operations wherever not yet replaced. Each replacement error is charged once and propagated to the final D block in spectral norm; all stages use the fixed input I_F. This is a proposed accounting partition, not implemented computation.

| Hybrid transition | Exclusive ownership | State and evidence |
|---|---|---|
| X0 continuous target -> X1 exact ideal B192 tensor GL | Full-domain quadrature remainder | MISSING numerical derivative/analytic-domain remainder bound |
| X1 -> X2 stored binary64 nodes and base transformed weights, exact integrand evaluation | Node and base-weight representation, map/Jacobian error | ESTABLISHED source path; MISSING enclosures for actual stored/generated bits relative to exact GL |
| X2 -> X3 actual binary64 U/V/W, keeping exact radial/Gaussian evaluation | Density exp/sqrt/Hermite errors, C-weight contraction and its roundoff | ESTABLISHED UU semantics; MISSING certified pointwise weight-error arrays and propagation |
| X3 -> X4 mathematical radial approximation selected by the actual branch/stopping trace | Series truncation and omitted complete-Gamma tails only | DERIVED local exact-arithmetic tail statements; MISSING actual-data outward bounds and contraction propagation |
| X4 -> X5 actual radial evaluation and Gaussian geometry/normalization arithmetic | Binary128/longdouble radial rounding, pi/sqrt/pow/exp errors, geometry arguments and normalization | ESTABLISHED source/precision controls; MISSING certified elementary/special-function and argument bounds |
| X5 -> X6 actual compensated finite t,u,k sums | Weighted primitive summation roundoff and underflow | ESTABLISHED summation algorithm; MISSING outward roundoff/underflow bound |
| X6 -> X7 actual 12x12 orbital contraction | Frozen coefficient products and contraction roundoff | ESTABLISHED registry and coefficients; MISSING outward assembly bound |
| X7 -> X8 actual phase and final D assembly = raw archived bits | Phase arithmetic, multiplying G/O, final D additions and storage | ESTABLISHED source formula; MISSING outward transcendental and final arithmetic bounds |

For each C or R block, ||X8-X0||_2 <= sum_k ||X(k+1)-Xk||_2. Each term must compare fully propagated hybrid blocks, not unscaled local errors. A local entry enclosure M_ab>=|error_ab| yields the safe block bound ||error||_2<=||M||_F, provided M itself is outward bounded. When actual branches depend on rounded arguments, freeze the observed branch/term counts in X4 and include branch-selection/argument perturbation in X4/X5 consistently. Do not treat a rounded stop test as an exact tail enclosure.

The fixed-input target has no input uncertainty by definition: its stored numbers are exact dyadics. This does not certify the physical input. If a later authority asks for a different I_A, add ||F(I_A)-F(I_F)|| with a quantified sensitivity bound; do not silently replace pref/v or restore ideal rational coefficients. Casts before raw storage belong to these source transitions. Complex128 casts after raw storage belong only to diagnostic eta in DECISION_BOUND_DERIVATION.

The binary64 UU contraction's rounding belongs to X2->X3, never charged again to X5->X6. Algorithmic special-function tails belong to X3->X4; floating tail evaluation belongs to X4->X5. Raw producer roundoff is not also diagnostic eta. A detailed implementation would refine this hybrid chain, retaining exclusive ownership.

## Quadrature and endpoint obligations specific to this integral

The active rule integrates two Laplace variables on (0,infinity) via x/(1-x), and already incorporates both Jacobians in U/W. At x=0 the elementary density has exp[-(1-x)/(4x)], with an essential complex singularity. At x=1 the rational transform reaches infinity and the completed-square variance can tend to zero. A globally holomorphic ellipse containing the full closed [0,1] interval cannot simply be asserted from radial_entire's name or finite-node guards. Whether cancellations allow a more regular representation would require a separate proof, not an assumption. Signed high-order Hermite densities and complex phases require absolute domination in an error bound.

For a scalar smooth integrand on a finite interval of width h, the n-point Gauss-Legendre derivative remainder bound is

\[
 |R_n|\le \frac{h^{2n+1}(n!)^4}{(2n+1)((2n)!)^3}
 \sup|f^{(2n)}|.
\]

This follows from the monic orthogonal-polynomial remainder and rescaling; a complex/matrix version needs a positive Peano-kernel/duality argument or separate real/imaginary entry bounds, not a claimed common real xi for every entry. The project has not provided the required derivative bound or endpoint regularity. See [NIST DLMF 3.5, Gaussian quadrature remainder](https://dlmf.nist.gov/3.5.E19).

For a tensor rule, I_x I_y-Q_x Q_y=(I_x-Q_x)I_y+Q_x(I_y-Q_y). Use uniform parameter-dependent bounds and the positive base GL weights to propagate the two errors. This does not make the signed donor weights positive. No derivative constant is inferred from the observed order triplet.

An alternative on a compact interior subrectangle could use analytic ellipse bounds after proving holomorphy and a magnitude bound there: avoid t=-a/u=-b poles, variance zeros, inverse-Laplace singularities and square-root/power branch crossings. Entire dependence on s at fixed positive variance is not joint holomorphy in all transformed variables. [Johansson's Petras/ball integration method](https://arxiv.org/html/1802.07942) requires a valid analytic callback enclosure; a nested two-variable use would need uniform outer-parameter enclosures. None is supplied or executed here. The existing piecewise floating radial program is not an analytic ball callback. A separate validated-integrand implementation/evaluation workload would require separate approval and must preserve the target; it is not an automatic replacement producer.

For a partition into an interior rectangle and endpoint strips, first prove domination and explicitly partition their union without double-counting corner regions. The interior remainder plus strip/corner integral and quadrature-contribution bounds must cover the original full GL error. There is no separate physical hard-cut tail in the current rule. Do not add a purported Laplace tail on top of a remainder already covering the whole domain.

## Special-function tails and finite arithmetic

`completion/radial/DERIVATION.md` lines 52–61 gives an exact-arithmetic geometric series tail when its ratio bound q<1. The floating computed q, terms, compensated sum and stop predicate are not outward bounds. Lines 69–78 give, for a=Re(x)>=64, |F_n(x)-C_n(x)|<=T_n(a), T0<=exp(-a)/(2a), Tn=exp(-a)/(2a)+(2n-1)T(n-1)/(2a), derived from the defining integral tail [1,infinity]. This holds for complex x with that real part. It is a partial analytic ingredient, not a mixed D error certificate.

To use it, propagate through the odd-moment polynomials A/B, their first/second derivatives, inverse powers of variance, Gaussian bases, G derivatives, signed donor coefficients and orbital contractions. The omitted exp(-x) term needs its own contribution within the same special-function approximation category. Even terminating polynomials still have rounded coefficients, argument and evaluation. Bounds on longdouble and binary128 basic arithmetic do not by themselves enclose libm/transcendental calls or argument conditioning. Underflow, phase, normalization and finite sums must be addressed on the actual host/compiler path.

Existing sumabs is formed with ordinary rounding and is not an outward interval. FE_TONEAREST, strict flags, cached-binary identity and scalar control thresholds are implementation facts; none replaces a certified error propagation bound. Historical H convergence anchors do not certify these mixed blocks. The independent dotO analytic source remains distinct; metric compatibility diagnostics are not source-error bounds or a way to manufacture dotO.

## Exact blockers and separately approved future workload

Missing quantitative authority:

1. Full-domain tensor quadrature error for the actual mixed O/G integrands, including endpoint regularity/domination and any interior/tail partition.
2. Exact GL node/base-weight enclosures tied to the actual OD generated arrays and JVP frozen bytes; representation/transform error propagation.
3. Enclosures for U/W generation, Hermite/elementary evaluation and coefficient contraction.
4. Uniform or actual-node radial special-function truncation, omitted tails and floating evaluation enclosures propagated to C/R; finite guards are insufficient.
5. Certified primitive summation, orbital contraction, phase and final D assembly error on the actual numerical path.
6. A separate diagnostic eta enclosure for complex128 cast, K assembly, subtraction, spectral norm and scalar publication/rule arithmetic.
7. Optional input-to-physical-target authority if a target beyond the exact stored Frozen107 model is requested.

Only theoretical design has been performed. Obtaining numerical enclosures, evaluating an interval callback, sampling new integrands, or validating norms is a future workload requiring separate authorization. No numerical scope/envelope is created. Missing evidence is not repaired by increasing order, generating B144, extending B256, changing precision, fitting a tail/order model, modifying the comparator, or rerunning the consumed transaction.

## Preserved evidence and stop

Original four-stage transaction is consumed and complete. All finite-order PRIMARY/SECONDARY verdicts and all conditional p/E/machine labels remain unchanged. The negative-direction argument rejects only the positive-direction single-term interpretation of this represented triplet; it proves neither divergence nor a cause. Finite-order stability can coexist with common implementation bias.

O and independent dotO evidence/metric diagnostics remain preserved. R31AK model/knot/training state is frozen; z0.75 is not consumed as training. Full-cell authority, complete-HH fixed-Q physical invariance, BR01/BR02, independent project/decision review, interval-wide accuracy, transition error, trajectory, H-skip and production remain open gates. A bounded artifact review here does not admit the project's independent scientific decision review gate.

new_science_commands=0; new_science_nodes=0; new_integration_samples=0; native_compile_commands=0; original_postprocessor_invocations=0; historical_test_invocations=0. Raw restore is not performed: RESTORE_VERIFIED=false. Stop after these three artifacts, their bounded evidence verification, ordinary research publication and create-only dual-backup ACK/metadata receipts. No recurring preflight audit or automatic successor follows.
