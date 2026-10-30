# WU088_HH | R31 reaction-conditioned HD rotational energy | 다음 스레드 인계

## 실행 기준 및 통제

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=169
PARENT_HEAD=72d189752d81febe48292e7532d0e96beac51f7f
CURRENT_BRANCH=research/wu-hd-reaction-conditioned-energy-r31-20261030
CURRENT_PR=RESOLVE_FROM_GITHUB_AT_RESUME
CURRENT_HEAD=RESOLVE_FROM_GITHUB_AT_RESUME
CURRENT_UNIT=WU_HD_REACTION_CONDITIONED_ENERGY_R31_20261030
NEXT_UNIT=WU_HD_EMAA_171x25_NATIVE_SOURCE_CROSSWALK
AUTO_NEXT_NODE=false
THEORY_FIRST=true
PHYSICAL_DATA_FIRST=true
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
CANONICAL_DAG=34/49_UNCHANGED
R29_AUXILIARY=1/1_SCOPED
R30_AUXILIARY=1/1_SCOPED
R31_AUXILIARY=1/1_SCOPED
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
NATIVE_SUBAGENT=NOT_EXPOSED
PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
```

## 불변 원본과 실제 검증

- R31 complete SOURCE ZIP: `WU_R31_SOURCE_ORIGINAL_20261030.zip`, Library `/WU088_HH/R31_REACTION_ENERGY_20261030/`, 4,286,496 bytes, SHA-256 `3286e22a7663ab3114685698e7653b00ac3ea1ec439af466b5c4ae5483e42078`. ZIP CRC PASS; 72/72 manifest-file SHA-256 PASS (73 ZIP entries, one is manifest itself). `evidence/PACKAGE_METADATA.json` is an empty placeholder and not a verification receipt.
- Nested original R30 ZIP SHA-256 `d1aa63fedb6527d6aab59df447f1f2b4aa557fab98789b962464a2b86bb5bf16`; nested R29 SHA-256 `65ed097acb02f8eb91ff6518c26c8ad61e721e3fadd9b904aa2157e3508cb0ea`.
- R30 was used unchanged. New original external PES/EMAA raw data were **not** acquired, no reaction Q or threshold inferred.
- Clean fresh extraction, Python 16/16 normal and 16/16 `-O`, compileall PASS, same-author algorithm mpmath75 210 cases × 3 energy metrics = 630/630, max scaled difference `9.9581495611029228e-13`; recomputed 6 main outputs SHA-256 identical to original archived bytes.
- New physical output counts: 210 energy balances, 2,100 collision edge transfers, 1,050 reaction terminal HD energy records, 840 photon energy rows, 35 matched-density spin-policy comparisons. Max |energy balance residual| = `2.02373107437565e-34 J`.
- 105 K, initial J2, `n(H+)=3954.4181821071797 cm^-3`, spin effective: initial `5.3051876415004004e-21 J`; proton bath gain `-8.507972699776604e-22 J`; photon `2.580602925218754e-21 J`; terminal HD `3.575381986259306e-21 J`. Eq: epsilon_initial = B_bath + R_photon + F_HD_at_reaction. At matched density, raw SQM bath gain `+7.483131835456486e-22 J`: sign differs under two explicit spin policies. This is a model-policy sensitivity, not uncertainty interval.

## Scope 및 백업

R31 models only transient HD(v=0,J=0..4), fixed T and n(H+), original GL2022 350 reactive + 70 downward rate cells (7 native T), REC161 A and REC164 transcription of four Sung fitted line centers. `B` is energy per initial HD, **not** volumetric heating rate; `F` excludes product-side energy and chemical Q. Full astrophysical cooling, full non-LTE and cosmic abundance dynamics are not validated.

20 R/C retrospective stage evidence records were published as individual Git files and corresponding stage ZIPs received Library upload ACK; four phase ZIPs and the complete SOURCE ZIP also received Library ACK. Previous Git CSV transport corruption was repaired, and the five main physical result CSVs were verified to match original byte-identical Git blob SHA. Other independent cloud mirrors (Google Drive, Dropbox) and per-stage ZIP remote-byte full readback are not certified. Do not interpret upload ACK as an independently verified scientific replication.

## 재현 명령

```bash
mkdir -p clean_r31 && cd clean_r31
unzip /path/to/WU_R31_SOURCE_ORIGINAL_20261030.zip
sha256sum archive/WU_R30_SOURCE_ORIGINAL_20261030.zip
PYTHONPATH=. python -m src.energy_ledger
PYTHONPATH=. python -m unittest discover -s tests -p test_r31.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r31.py -q
PYTHONPATH=. python tests/independent_mp.py
python -m compileall -q src tests
```

## 다음 실행 조건

1. Check fresh WU and REC/CR PR heads; never assume this handoff contains a future head. If R31 Draft is already published, avoid duplicate PR.
2. Retrieve original EMAA HD–H+ native RADEX ASCII, authenticate 171 collision transitions × 25 T nodes, identify dataset DOI, state labels, units and original bytes/hash. Crosswalk with GL2022 without presupposing scientific independence or exact numerical identity.
3. Separately seek Velilla2008 EPAPS E-JCPSA6-129-612834 Fortran and true native sigma(E) and isotope-specific asymptotic energy zero; seek 2011 CDMS v2 raw fit covariance and real REC/CR chemistry owner acknowledgement.
4. Distinct-author R6/C9 remain NOT_RUN; canonical 34/49 remains HOLD until existing admission gates are genuinely satisfied. No merge or full-A/production claim.
