# PHYS81 C7/C8 saved-result review

## Decision

**CONFIRMED_SCOPED_FROM_SAVED_EVIDENCE.** The saved fresh cohort reports three completed new ODEs, zero observed failed attempts in this cohort, and passing frozen comparison gates. The current source/data bytes match the identities bound into those results and the earlier static review. The profile run is complete, and its CSV hash matches the final JSON receipt. The subsequent parent-run resume reports three verified skips and zero new ODEs.

This postflight used saved JSON receipts, schema/identity inspection and file hashes only. It did not import numerical modules, evaluate rates, call an RHS/Jacobian/integrator, recompute a completed test, perform NPZ-array arithmetic or create another reviewer agent. NPZ files were read as bytes for SHA256 only. The parent had already rechecked the two saved-array comparisons under the shared lease; that existing resume evidence was reused.

The review confirms the recorded finite-model computation and its declared sampled acceptance. It does not issue production admission, a complete physical collision-rate result, a uniform trajectory error bound or a speedup claim. Plot scientific claims and visual review remain with the parent.

## Identity and execution evidence

The following identities were actually read and checked against the saved bindings:

| Artifact | SHA256 |
|---|---|
| `results/parcel/SCIENCE_SUMMARY.json` | `752a09bfb1445c12a36766f4a9512e0900caa8835cb9f95d55246102a9174c84` |
| `results/parcel/PLAN.json` | `8296c8a7ceecea9073dfee08ffe40d7d373694542cb5af31573321f6a5a70612` |
| `results/RATE_PROFILES.json` | `131de5ea39834a3a3a3dbf4a15ebfe196d1980ebabd69bebcf3e69100e7b2d33` |
| `results/RATE_PROFILES.csv` | `e4d17ffeb92c80d6a0035f9104557a85810068af31cc7125725f2beb356cd5a9` |
| `verification/RUNNER_STATIC_REVIEW.md` | `de7faadb3ad216b3a45af560c9db52556836353c28679fe037dad1c85e2773d5` |

The canonical plan-binding digest is `8ae4a4d18b625742c7f966b21596ce24f904be83e1ac5123541df5aa188a291b`. All eleven distinct source/data files listed across the cohort and profile bindings still match their recorded hashes. In particular, the executed runner is the statically reviewed corrected version `f7b7443c80fef386e070bbcd4019c59c16143c0b9b285e83c076c04d70eae4f4`, and the profile implementation is `54063b5feb68851816535ae0aca3adceef423004524900ff1093d08eb864a936`.

For all three ODE cases, the canonical identity hashes to the reported science ID, the CLAIM and COMPLETE identities agree, and the current trajectory bytes hash to the value recorded in both COMPLETE and SCIENCE_SUMMARY. The three trajectory hashes are:

| Case | Trajectory SHA256 |
|---|---|
| Hazard base | `4407d66a8750d8fc6e27f23d2ba3769b97f5fe2a39e7c599bcbe411caff91ab7` |
| Hazard refined | `d8626e65c2e3f77df674abbca770fc05678093b45311245df3e33075f649e6ba` |
| Original seven-state reference | `8746483030433d6b5ff8ae04c58538779479701b32b7fd34de71829163310112` |

The structured companion `SAVED_RESULT_REVIEW.json` preserves the full science IDs, CLAIM/COMPLETE hashes, bound source/data hashes and principal values. These hashes identify the observed evidence; they do not replace the scientific scope qualifications below.

### Shared-lease receipts

| Operation | Actual exit | Recorded result | Receipt SHA256 |
|---|---:|---|---|
| Rate profiles | 0 | COMPLETE_SCOPED; 27 finite evaluations, 27 new Bell64 evaluations using reused kernel code, 27 new Bell-window integrals, zero ODEs | `328982350e26801cd55b6ce64991558ccfccf100c4aa2f31f89608d8ad90f107` |
| Fresh parcel cohort | 0 | PASS_SCOPED; three new ODEs completed | `decf9d5420e992bc9f83cc53b430220b0b6e70d263c0a24142c2c3caab9eab50` |
| Resume readback | 0 | RESUME_VERIFIED; three verified skips, zero new ODEs, two saved comparisons rechecked | `ef6c27dbe06c577eabdd59fd14dfcc4f2c33a0d6908bc4546229182fdf05f23e` |

Each wrapper records one thread, a 0.5 GiB job reservation, the shared lease implementation hash `76ff57ba687fd9830b84c3fcff69eb8ed0e9f6ceab4551e61c67c84d3ea65124`, empty stderr and zero other-process terminations. The resume stdout binds the unchanged science-summary hash listed above. This reviewer did not execute any of these commands.

## Model and principal saved state

The frozen scenario is the explicit fixed-density, homogeneous common-temperature H1/He4/Li7 finite-window CI model. Its inputs are

\[
B=(1,0.083,4.6\times10^{-10}),\qquad
X_0=(2\times10^{-4},0,0),
\]

with nref = 0.001 cm^-3, initial T = 25370.66308424773 K and physical end time 10^14 s. The rate kinematics remain stationary-target electron Maxwell averages. Expansion, PI, RR, CX, bound-bound collisional excitation and radiative losses are absent by the selected model contract. These choices are not a physical validation of their omission from a general plasma.

The refined hazard receipt gives the following endpoint, read directly from COMPLETE:

| Quantity | Stored result |
|---|---:|
| T | 25266.558216164776 K |
| Electron abundance per reference H | 0.0010642158051694301 |
| H1 ion fraction X/B | 0.001064059898723147 |
| He4 ion fraction X/B | 0.0000018773392812632518 |
| Li7 ion fraction X/B | 0.18975204005937182 |

The ion fractions are normalized by each species' own B. In particular, the Li7 fraction is not a Li abundance of that magnitude per reference H; the declared Li7 total abundance is 4.6e-10. The initial thermal state, the chemical energy defects and all source identities are part of the frozen plan/API contract.

## Stored comparison gates

No comparison maximum was recomputed by this reviewer. The saved summary reports:

| Comparison against refined hazard | Maximum normalized seven-state difference | Maximum T difference / T0 | Frozen limits | Result |
|---|---:|---:|---|---|
| Base hazard | 3.266791559486393e-10 | 6.451973914971298e-12 | 1e-7 for each metric | PASS |
| Original raw seven-state reference | 7.286526937377857e-11 | 1.35578205058459e-12 | 1e-7 for each metric | PASS |

The corrected runner compares all seven normalized components `[N/B, X/B, u/u0]`. For the original seven-state solve, the saved comparison state is the raw normalized integrator state, without reconstructing an invariant or projecting conservation. The parent resume has checked that the sample grids agree and that the saved comparison results match the passing cohort summary.

These are meaningful refinement and independent-coordinate/different-solver checks for the selected model. They remain sampled agreement evidence, not rigorous errors against an exact solution. The compared integrations share the same admitted rate implementation and source data, so shared source or model error is not independently tested by their agreement.

## Conservation and sampling must remain separate

The COMPLETE receipts report the following accepted-mesh diagnostics:

| Case | Accepted mesh points | Accepted steps | Max nuclei fraction residual | Max relative total-energy residual |
|---|---:|---:|---:|---:|
| Hazard base | 55 | 54 | 2.220446049250313e-16 | 1.2492035952546755e-16 |
| Hazard refined | 165 | 164 | 2.220446049250313e-16 | 0 |
| Original seven-state | 6 | 5 | 1.1102230246251565e-16 | 0 |

The frozen accepted-mesh limits are 1e-10 for the nuclei fraction residual and 2e-10 for relative total energy. All recorded accepted and sampled minimum fractions are zero, consistent with initially neutral He4/Li7 ion slots; none is negative. All accepted/sample neutral-underflow counts are zero. The recorded accepted temperatures remain inside the admitted 255–50000 K interval.

**Reconstructed hazard energy is not independent accuracy evidence.** The hazard lift defines

\[
u(z)=u_0-\sum_s I_s\,\Delta X_s(z).
\]

Therefore the thermal-plus-chemical energy identity is satisfied by construction for any admissible supplied hazard vector, including a numerically inaccurate trajectory. A zero energy residual cannot establish that the ODE was integrated accurately. The full7 energy diagnostic evaluates independent energy coordinates, but preservation of a linear invariant alone still does not determine the trajectory along its invariant manifold. The separate refinement and raw-seven-state comparisons supply the relevant additional numerical evidence.

Every run saves **161 common dense-output sample times**. These are distinct from accepted solver mesh points or integration steps. The seven-state solve, for example, has six accepted mesh points and five accepted steps, followed by 161 dense-output readouts. The conservation gates above are accepted-mesh gates; positivity is additionally checked at saved samples. Neither this distinction nor the sampled comparison should be recast as a uniform-in-time error certificate.

## No speedup inference

The solver receipts contain:

| Case | Method / dimension | RHS evaluations | Jacobian evaluations | LU decompositions | Single recorded wall time |
|---|---|---:|---:|---:|---:|
| Hazard base | Radau / 3 | 386 | 2 | 16 | 0.7089417639945168 s |
| Hazard refined | Radau / 3 | 1156 | 2 | 18 | 2.0984197439975105 s |
| Original reference | DOP853 / 7 | 89 | 0 | 0 | 0.1812924749974627 s |

The exact reduction decreases the number of state coordinates from seven to three. This cohort does **not** establish a runtime speedup from that reduction. The seven-state explicit solver used fewer RHS evaluations here than either implicit three-state run; method, tolerance, step-control and callback/linear-solve costs differ. The recorded times are single executions, not a controlled repeated benchmark. No speedup ratio, universal efficiency claim or performance promotion is supported.

## Profile evidence and interpretation

The profile science ID is `ce0c382952674e0da985d768654f1b0f1253d671ed475f26cc00d7f47eb5e014`. Its nine temperatures for each of H1, He4 and Li7 produce the 27 saved rows and 27 quadrature receipts. All stored warning lists are empty. The largest stored reported relative finite-window quadrature error is 1.1613197816350031e-12, at He4/3000 K, below the declared 1e-8 reported-error gate. This is an adaptive-quadrature diagnostic, not a certified physical or numerical enclosure. The full Bell result is order64 Gauss–Laguerre and has no new uniform convergence certificate here.

At the parcel's initial temperature, the saved rate rows are:

| Species | Finite K (cm^3/s) | Mean incoming energy (eV) | Bell-model window fraction | CCC / Bell in the same window |
|---|---:|---:|---:|---:|
| H1 | 1.6896167676316183e-11 | 18.20986091959254 | 0.9999965981812716 | 0.9272527745565898 |
| He4 | 3.7079880419624424e-14 | 29.543935701774554 | 0.9999979496478227 | 0.7937276129636713 |
| Li7 | 4.077941060608214e-9 | 9.40034398240508 | 0.9231367126146738 | 0.7340960656962464 |

The incoming-energy mean remains a diagnostic. It is not an additional event heat loss on top of the chemical ionization defect.

Two observed numerical details should remain explicit:

- He4 at 255 K and 300 K has stored binary64 K = 0 with the underflow flag set, while log10 K remains finite at -495.69828218412414 and -422.78345015523087. These zeros do not establish a physically zero rate. Log-rate plots can preserve the saved finite logarithms without inventing a positive floor.
- The He4/300 K Bell-model window fraction is stored as 1.0000000000001137. This is a tiny floating quadrature/logarithm approximation overshoot, not physical support exceeding the full Bell model. The raw result should be retained and described with that numerical qualification, not silently clipped or promoted to an exact probability.

Finite support remains the main physical scope boundary. For example, the Li7/255 K saved same-window CCC/Bell ratio is 0.9994992523362651, while the Bell-model window fraction is only 4.255644038244163e-11. Agreement inside a selected window therefore does not establish complete low-temperature rate coverage. The Bell fraction is a statement inside the comparison model, not a certified physical missing-support bound. The source-window, interpolation, stationary-target and thermal-pool assumptions retain their previously declared limits.

## Remaining scope and audit trail

The review confirms the passing saved finite-model cohort, profile outputs, current input identity and successful no-ODE resume. It does not establish a full physical CI rate, omitted-support/interpolation error bounds, finite-mass double-Maxwell kinematics, a cosmological history, a nuclear reaction rate, stopping closure, normal-frame transport, uniform trajectory error, or a general performance advantage.

The observed read/hash/schema commands completed with exit 0. The existing-result inventory was read once; no failure receipt was present among the inspected parcel cohort files. All new scientific execution counts in this document come from the parent's saved receipts. This review added **zero** rate evaluations, RHS/Jacobian calls, ODE attempts, completed-test reruns, NPZ numerical comparisons, process terminations or remote writes.

`HH_R10=OFF`; `production_admission=NOT_ISSUED`. Plot visual QA and publication/backup receipts are separate parent-owned obligations.
