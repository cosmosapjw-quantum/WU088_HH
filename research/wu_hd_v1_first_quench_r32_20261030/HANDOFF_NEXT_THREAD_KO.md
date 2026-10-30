# WU088_HH R32 | 다음 대화 인계

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=170
PARENT_HEAD=d359a8d2ecfb68c17657ba30b41c5796d3bde89c
CURRENT_UNIT=WU_HD_V1_SOURCE_RESTRICTED_FIRST_QUENCH_R32
CANONICAL_DAG=34/49_UNCHANGED
R32_AUXILIARY_PHYSICS=1/1_SCOPED
NATIVE_SOURCE_V1_CELLS=890
QUALIFIED_SOURCE_CELLS=801
SOURCE_TEMPERATURES_K=15,55,105,255,505,1005,1505,2505,3005
HELD_ORIGINAL_CELL=2005K_V1J2_TO_V0J5_MALFORMED_1.58(10
CASES=126
V0_TERMINAL_BRANCH_ROWS=1386
ROTATIONAL_EXPECTED_EVENT_ROWS=3969
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
EMAA_171x25_RAW=NOT_ACQUIRED
CDMS2011_V2_ORIGINAL_FIT_AND_COVARIANCE=NOT_ACQUIRED
PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
AUTO_NEXT_NODE=false
```

SOURCE original R31 ZIP = `WU_R31_SOURCE_ORIGINAL_20261030.zip`, SHA-256 `3286e22a7663ab3114685698e7653b00ac3ea1ec439af466b5c4ae5483e42078`. R32 complete original ZIP and new PR identity are in `evidence/FINAL_RECEIPT.json` and the PR description after publication.

### Source and physics contract

The reused GL2022 JCP157,214302 original CSIC supplementary PDF is byte-locked SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. Source CSV SHA256 `58c252a1c3f62995ed748c7620e342bc98d8aabb307271bff48f7711e4f1cd7c`. 890 original v=1 state rates /10 native T; exclude 2005 K entire model because one malformed token. 9 valid T × 7 v1J × 2 named policy =126. Detailed-balance policy uses **official CDMS 2011 v2 rendered text**, explicitly not raw bytes. Interpret first-passage to v0 only for a collision-only restricted source network. No claim of full radiative/reactive state system.

### Reproduce

```bash
unzip -q WU_R32_SOURCE_ORIGINAL_20261030.zip -d R32_RESTORE
cd R32_RESTORE
PYTHONPATH=. python -m src.quench --out results
PYTHONPATH=. python -m unittest discover -s tests -p test_r32.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r32.py -q
python tests/independent_mp.py
python -m compileall -q src tests
```

### Next source-first action

Actually acquire EMAA DOI `10.17178/emaa_hd_rovibration_805a7aa5` official HD–H+ 171×25 RADEX ASCII, save original bytes+SHA, parse H+ collider ID7, original energy state labels and 25 temperatures, determine intersection with GL2022 without assuming independent numerical experiments. If download remains blocked, first obtain source-qualified v=1 vibrational Einstein A / reactive rate bytes, compare hazards and extend *only* from authenticated source. Obtain explicit REC/CR owner ACK and distinct-author R6/C9 before canonical promotion. Never silently start next DAG unit from this handoff.
