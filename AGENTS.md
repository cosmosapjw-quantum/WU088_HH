# Current development priority — PHYS12, 2026-10-12

Read CURRENT_DEVELOPMENT_PLAN.json, then research/r31ao_unequal_ladder/hh_phys12_absolute_response_20261012_v1/state/RESEARCH_STATE.json and review/DECISION.json in that folder. The observable-first plan remains active; PHYS12 has now executed its L0–L3 bounded task.

Reuse the fixed-family future HH-on/off x_HII and thermal-w results and the inherited PHYS11 mixed response. Do not replay completed PHYS09/PHYS11/PHYS12 or treat the old plan's PLANNED_NOT_EXECUTED snapshot as the current execution state. Source-inclusion and same-alpha C2 premises remain explicit. Full and first_half are separate first stages; their PreBE coefficients differ.

Current NCP heavy_queue=[] and launch=false. The fixed-family question is answered within its inherited scope; no additional refinement or heavy job is selected. Select new work only for a concrete observable/error requirement or a standalone microscopic HH question, following the existing lane-specific admission. HH LCS and singlet ion-pair physics, and FT03 BE versus frozen107 atomic native, remain distinct.

## Preserved execution contract

# WU088_HH execution contract

Read README_KO.md, docs/research/RESULTS_KO.md, docs/coding/IMPLEMENTATION_PLAN.md, and evidence/FINAL_VERIFICATION.json.
Read exact source and provenance before mutation. Frozen sources under native/reference and vendor/orchestration remain byte-preserved. Archived scientific arrays are not placeholders or synthetic fixtures.
Use local runtime for heavy scientific kernels; sandbox does bounded algebra, convergence, source and implementation checks. Preserve existing checkpoint/ACK history. No automatic full-suite scientific reruns without dependency changes.
Treat byte identity, numerical equivalence, convergence, physical model adequacy, provider admission and upload/restore verification separately.
Never infer full49 readiness from H convergence alone. No symmetrization, precision downgrade, tolerance relaxation, hidden screening, propagation or changed trial basis.
Candidate native code is NOT promoted by component tests. Record compiler/flags/CPU/precision, compare canonical scalar arrays and sumabs, benchmark on target host; request independent decision review before promotion.
