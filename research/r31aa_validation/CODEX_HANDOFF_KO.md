# Codex handoff: R31AA

Repo: cosmosapjw-quantum/WU088_HH
Branch: research/r31aa-validation-design-20260929
Base: research/r31z-source-bound-interp-20260929
Pinned parent: 6e34cfec8971cecce4bbe1c663582e2c5658219b
Parent tree: 7410169cf96422f77fa00f9e8513cdf88d802eab

Goal: reproduce the lightweight R31AA analysis, compare the new local candidate against the already-existing z=3 direct node as POST-HOC diagnostic only, review the fixed-Q source contract, and lock the z=1 preregistration. Do not execute z=1.

## Start
Verify remote HEAD/tree. Read REPORT_KO.md, RESULT.json, Z1_PREREGISTRATION.json, local_candidate.py/test, then parent R31Z RETURN, WITHHELD_Z3_COMPARISON, INTERMEDIATE_NODE_INVENTORY, FULLCELL_EXISTING_AUTHORITY. Preserve existing worktrees/raw/backups. No reset, force push, main merge, PID/cgroup mutation.

## Lightweight replay
Use the existing hash-locked 71,481-byte input:
SHA256 565a9ee6d831f5f9e3e69010270f5319aa3328432950efcfda81cfabf325c079.
Prefer /root/wu088_hh_ncp_work_v2/venv/bin/python. Do not install packages.

Run py_compile, focused pytest, and local_candidate.replay with argv/stdout/stderr/exits/JUnit preserved. Do not rerun historical 11/20/13/33/134 suites.

Reproduce z=3 global error diagnosis:
- E_dotO 0.07262393465956431/t_a
- E_Dcol 0.3073893478614785/t_a
- E_Drow 0.3192667733603847/t_a
- DeltaK lower 0.2829548060306026/t_a
- DeltaK upper 0.3133280606109316/t_a
- lower/E_dotO 3.89616463714058

## Existing z=3 post-hoc comparison
Use the already recovered CP4 z=3 OD/JVP members only. No new node computation.
Compare frozen R31Z global vs R31AA local:
E_O, E_dotO, E_K, E_Dcol, E_Drow, E_Dmax and metric residual.
Write Z3_POSTHOC_MODEL_COMPARISON.json.
Because R31AA was designed after seeing z=3 failure, set independent_validation=false regardless of outcome.

## z=1 preregistration
Hash-lock Z1_PREREGISTRATION.json before any future science run.
Do NOT execute z=1 in this handoff.
Planned minimal future node: z=1 a0, tau=2.2358772390338113 t_a, B192, mixed O/D and independent dotO only. No H/neutral/ionic/full49/trajectory.

Primary future comparison: E_K and E_Dmax, tolerance 1e-10.
Local support requires local <= global+tol in both and >tol improvement in at least one. Reverse dominance supports global; otherwise TRADEOFF_UNRESOLVED. One point never admits interval/trajectory accuracy.

## Fixed-Q source-contract review
Review recovered source to decide:
- FIXED_Q_MODEL_DEFINITION_ESTABLISHED: same frozen Q is intentionally used at all z, so dotQ=0 by represented-model definition; or
- Q_DYNAMIC_CONTRACT_MISSING: z-dependent Q intended but transport missing.

Write FIXED_Q_CONTRACT_REVIEW.json with exact archive member/source lines.
If fixed-Q model definition is established, do NOT promote it to physical invariant symmetry without source-bound proof that the full dynamics preserves the sector. Keep FIXED_Q_PHYSICAL_INVARIANCE_REVIEWED=false unless such proof is actually found.

## Full-cell
Do not execute neutral_worker at z4. Keep FULLCELL_AUTHORITY_INPUT_BLOCKED except any legitimate reclassification of the Q/dotQ sub-gate from source review. z4 neutral generation is a separate science action.

## Return
RETURN.json must separate execution identity, environment, K-bound replay, local fit-node replay, z3 post-hoc comparison, z1 prereg hash/execution_authorized=false, fixed-Q contract verdict, unresolved full-cell/BR01/BR02/reviewer/production gates, and mutation scope.

No native HH evaluation, no new scientific node, no M3 rerun, no trajectory.

Ordinary non-force push and create-only Drive+Dropbox backup are allowed. Record provider ACK/object/size/checksum scope; RESTORE_VERIFIED=false without actual raw restore.

Stop after R31AA replay + z3 post-hoc comparison + fixed-Q contract review + z1 prereg lock. Return to the research thread for the explicit decision whether to authorize the minimal z=1 mixed OD+JVP node.
