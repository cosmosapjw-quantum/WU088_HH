# WU088_HH | R24 native PES threshold and molecular owner handoff

PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=162
PARENT_HEAD=2f214319ca8600475b1d4e85d1ca21a0249136a8
EXISTING_R24_DRAFT_PR=163
EXISTING_R24_ORIGINAL_HEAD=c63f29fb2b6ede9ebb14b7df6aed91707a0c6d09
R22_SIBLING_PR=160
R22_SIBLING_HEAD=9db6f91debf54af1cc129538cfd6f6a716a78a56
REC_READONLY_HEAD=e209cd0180c8bf199fc476c37e3cbf8d50394b6c
CR_READONLY_HEAD=a6b49b352fed31587955d55b1cad30c0b55a81eb
UNIT=WU_HD_GL2022_PES_NATIVE_THRESHOLD_R24
CANONICAL_DAG=34/49_UNCHANGED
R23_WORKFLOW=18/20
R6=NOT_RUN
C9=NOT_RUN
PHYSICAL_Q=NULL
GL2022_PES_NATIVE_THRESHOLD=NULL
SOURCE_UNCERTAINTY=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
PRODUCTION=NOT_ISSUED
FULL_A=NULL
L4=false

Read THEORY_KO.md, CODE_AND_CALLPATH_KO.md and EVIDENCE_AND_GATES.json in this add-only R24 review directory first. Download original byte-verified standalone ZIP from Library /WU088_HH/R24_native_owner_admission_20261029/WU_R24_NATIVE_OWNER_ADMISSION_SOURCE_ORIGINAL_20261029.zip (SHA256 e88788f629eaf098073ddbc63a7ffdcded3bca5c7bdfc8124fbbabb7f819e1ed, 326174 bytes), which holds executed source, 14/14 Python and 14/14 -O tests, source provenance, original GL2022 supplementary PDF and visual adversarial audit.

Theory next: locate actual Velilla et al. JCP129 084307 (2008) 1^1A' H3+ source PES and obtain native HD(v0,J2) and H2(v0,J1) asymptotic state eigenenergies, isotopologue masses and IP/BO corrections and original energy zero. Derive incoming-kinetic eps=E_total-E_HD(0,2) transformation from GL2022 Eq(3) to Eq(4) and independently re-integrate source-native state-specific cross sections at 15 K and 55 K. The 15.186303821758897 meV upper bound is *CONDITIONAL* on positive fixed entrance-kinetic cross section; the spectroscopic candidate 20.950020993840458 meV is external and is not the native threshold or physical Q. Source Fortran file identified Aguado2000 NOT Velilla2008.

Coding next: preserve exact four typed species H+,HD(v0,J2),D+,H2(v0,J1); do not confuse CR 'HD_CX' atomic D/H charge exchange or REC LAMDA HD rotational collision with source-native GL2022 molecular chemistry. Identify actual reachable molecular-chemistry owner function by runtime import/graph tracing and obtain named owner ACK before foreign edits. Never convert missing channel/null to measured zero or inferred heat. Keep original R24 P01-P04 Git+Library receipts, all original source SHA; do not merge main or sibling R22. No production or full-A or R6/C9 completion without their actual independent evidence.

Next stop condition: native model source lacks any one of same-energy-zero levels, GL2022 cross-section kinetic-axis reconciliation, source uncertainty, or named owner ACK -> HOLD; do not invent Q or reverse rates.
