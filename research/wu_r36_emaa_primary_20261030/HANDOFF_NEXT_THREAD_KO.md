# WU R36 source-qualified EMAA original-format RADEX crosswalk | 2026-10-30

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=174
IMMUTABLE_PARENT_HEAD=da528f894f82395564bd1f4479d081f4010fcdde
CURRENT_PR=CHECK_GITHUB_LIVE
CURRENT_HEAD=CHECK_GITHUB_LIVE
READ_LIVE_HEAD_FIRST=true
COMPLETED_UNIT=WU_R36_EMAA_171x25_PRIMARY_SOURCE_CROSSWALK_AND_HD19_KINETICS
CANONICAL_DAG=34/49_UNCHANGED
AUX_R36_SOURCE_SCOPED=1/1
R_C_SCOPED=18/20
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
EMAA_RAW=USER_UPLOADED_AUTHENTICATED_BYTES
EMAA_REMOTE_BYTE_IDENTITY=NOT_INDEPENDENTLY_VERIFIED
EMAA_SHA256=b0db1613425e403889c3a74f6cd9e142c562a552f1ebf05e61cbf509cd429c94
EMAA_BYTES=298618
EMAA_COLLIDER=7_HPLUS
EMAA_RATES=171x25
EMAA_NUMERIC_CROSSWALK=1548
GL_PRINT_NUMERIC_EQUAL=1498
GL_PRINT_NUMERIC_DIFFERENT=50
GL_PRINT_INVALID_OR_DIAGONAL=12
EMAA_ONLY_GL_UNPRINTED=16x25
NONLTE_19STATE_COUNTERFACTUAL=500
NONLTE_LINE_ROWS=31500
V1_COLLISION_ONLY_QUENCH=175
V0_J0to11_BRANCH_ROWS=2100
GL_HYBRID_SOURCE_SENSITIVITY=200
PHYSICAL_Q=NULL
PES_NATIVE_THRESHOLD=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
AUTO_NEXT_NODE=false
```

## First actions after restore

1. Verify the actual PR and head sha from GitHub rather than infer from this archived ZIP. Preserve PR #174 and source baseline SHA exactly.
2. Download `WU_R36_SOURCE_ORIGINAL_20261030.zip` from Library `/WU088_HH/R36_EMAA_PRIMARY_20261030/` or Drive `/WU088_HH_R36_EMAA_PRIMARY_20261030/`; check SHA256 per `evidence/SOURCE_ARCHIVE_RECEIPT.json`, then extract.
3. Run `PYTHONPATH=. python -m src.emaa_primary --out results`, test normal/-O, `python tests/independent_mpmath.py`, compileall; compare output hashes against `evidence/OUTPUT_SHA256.json`.
4. Original printed GL2022 source PDF and provenance R35 ZIP are inside the source-inclusive master; exact raw EMAA 298618 bytes in `sources/`, no reconstruction. See `REPORT_KO.md` for scientific limits.
5. Cross-source mismatch is 50 actual printed cells over 7 transitions. Do not silently edit original PDF; seek EMAA owner documentation/errata if scientific equality is required. The original official EMAA dataset DOI is `10.17178/emaa_hd_rovibration_805a7aa5`, paper DOI `10.1063/5.0128598`.
6. Next science node options are source-owner authentication of discrepant rates and chemistry-channel integration with isotope-specific native PES/physical Q plus R6/C9 distinct-author. New 19-state nonreactive and quench outputs do *not* satisfy full physical closure or automatically promote canonical DAG.

NO MERGE / NO AUTOMATIC NEXT / NO PRODUCTION / NO FOREIGN REPO MUTATION.
