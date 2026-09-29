# R31AA research checkpoint

Parent: `6e34cfec8971cecce4bbe1c663582e2c5658219b`, tree `7410169cf96422f77fa00f9e8513cdf88d802eab`.

R31Z found an existing withheld source-bound direct z=3 mixed node. The global R31Z candidate, fitted only at z=0,2,4, had spectral-norm errors
`E_O=0.13213912310643441`,
`E_dotO=0.07262393465956431/t_a`,
`E_Dcol=0.3073893478614785/t_a`,
`E_Drow=0.3192667733603847/t_a`.
This is one genuine out-of-sample comparison for the frozen R31Z model, not interval admission.

## Connection-sector diagnosis

At both source and candidate nodes,
`dotO=D_col+D_row†`. Define `K=(D_col-D_row†)/2`.
Then
`DeltaD_col=DeltaDot/2+DeltaK`,
`DeltaD_row†=DeltaDot/2-DeltaK`.

Spectral-norm inequalities give
[
0.2829548060306026/t_a le ||Delta K||_2
le 0.3133280606109316/t_a.
]
The lower bound alone is 3.89616463714058 times `||Delta dotO||`. Thus the z=3 D failure is connection-sector dominated at norm level. This is not an elementwise causal attribution.

Wolfram independently reproduced these numeric bounds.

## Local structure-preserving candidate

Rather than raise a global polynomial degree after seeing z=3, R31AA defines a lower-order local candidate on cells [0,2] and [2,4]:

- O: cubic Hermite from the two adjacent O,dotO nodes.
- K: linear interpolation of the two adjacent K nodes.
- D_col=dotO/2+K.
- D_row†=dotO/2-K.

The metric identity is algebraic for all interpolation parameters. O is C1 across z=2 and K/D are continuous there. The right-cell prediction at z=3 depends only on z=2,4 and not z=0.

Fresh sandbox checks: 5 focused tests PASS, py_compile/replay exit0. On the fit nodes, O,dotO,D reproduction and a 65-point metric-identity probe are at binary64 roundoff. No z=3 local comparison has yet been counted as validation.

Wolfram exact checks returned zero endpoint value/derivative residuals and zero compatibility residual; the standard cubic-Hermite midpoint remainder factor is `h^4/384` under the usual fourth-derivative hypothesis. No HH fourth-derivative enclosure is available.

## Validation policy after z=3

Because this local candidate was designed after observing the R31Z z=3 failure, z=3 is now tuning/post-hoc data for R31AA. It may be used to diagnose whether the local model reduces K error, but not as independent confirmation.

A new z=1 mixed-only validation is therefore preregistered but NOT authorized for execution. Required outputs are B192 mixed O, D_col, D_row and independent dotO only. H, neutral47, ionic2, full49 and propagation are excluded.

The z=1 decision rule compares the frozen R31Z global and R31AA local models using primary metrics `E_K` and `E_Dmax=max(E_Dcol,E_Drow)` with tolerance 1e-10. Local or global support requires Pareto dominance in these primary metrics; otherwise the verdict is `TRADEOFF_UNRESOLVED`. O/dotO/D individual errors are mandatory secondary outputs, but no arbitrary cross-unit weighted score is used. A single z=1 point still does not validate interval-wide or transition accuracy.

## Fixed-Q contract

Parent producer evidence says Q is an `s=0 static inversion-sector map`, while full-model and trajectory source consume frozen `model[Q]`; no Q(z)/dotQ producer was found. The next source review should distinguish:

1. `FIXED_Q_MODEL_DEFINITION_ESTABLISHED`: Q is intentionally constant in the represented model, hence dotQ=0 by definition.
2. `Q_DYNAMIC_CONTRACT_MISSING`: Q was intended to vary but its transport source is missing.

Even if case 1 holds, physical invariance of the complete HH dynamics is a separate gate. Pointwise small O/R cross-sector norms do not prove invariant dynamics. The full generator/Hamiltonian coupling and symmetry argument must be source-bound and reviewed.

SciSpace literature used for methodology: Luo–Levesley, DOI 10.1006/JATH.1997.3218 (Hermite error); Chellappa et al., DOI 10.1007/978-3-030-72983-7_5 (adaptive interpolation/error estimation); Kumar–Sarovar, DOI 10.1088/1751-8113/48/1/015301 (quantum invariant subspaces); Yen–Lang–Izmaylov, DOI 10.1063/1.5110682 (exact vs approximate symmetry projectors). These do not validate this HH model by themselves.

Remaining gates: full-cell authority blocked, z4 neutral47 not generated, fixed-Q physical invariance unreviewed, BR01/BR02 open, independent_review_admitted=false, trajectory/production/H-skip false.
