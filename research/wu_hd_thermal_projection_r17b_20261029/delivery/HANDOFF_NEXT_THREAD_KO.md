# WU088_HH R17B 다음 스레드 재개 | 2026-10-29

## 고정 출처와 실제 게시

PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=153
PARENT_VERIFIED_HEAD=d08683a50a57c7bebc8a871e0021c2f8b5520fa9
THIS_BRANCH=research/wu-hd-thermal-projection-r17b-20261029
THEORY_COMMIT=5e224f7e4945a0c6e6ec602adad07d0c76df9ccd
IMPLEMENTATION_COMMIT=d9ded96255695db4a8c81da94fa9dab5a6f28615
TESTS_COMMIT=ead86605a80315d0dc46c41bf1e20cb455d7385c
REFERENCE_COMMIT=dea1e0f1d6ee5ad8d77a4de4530e14846d4bbc79
PLOT_SCRIPT_COMMIT=4251fa00bd6d92864d30c581a3447d65648b5270
REFERENCE_RECEIPT_COMMIT=d56da35e9456fa61c0cced952abe48c6fa88391d
STAGE_LEDGER_COMMIT=55a6275bf795062050b3077ff4ff6374ea0c0596

R16 parent PR150 HEAD=40281b24d79afaa3dc7f842ccd92f677bd87977f
H–Li registry PR151 HEAD=ded0fa1590da39efa9ed8a449d93d191aaa0dbf8
R17 input PR152 HEAD=7bfe9bd0694c3a8a989ff7d11040c665fe392f74
REI prior PR222 pin=4824eec8526185b6b866a5e7e0dabdc624b5543c
WU_DAG=33/48 ; REI_CENTRAL_LAST_OBSERVED=28/88 ; REI_WORKING_PR257=33/88.
NEW_WU_PHYSICAL_NODES=0; HH_R10=OFF; PRODUCTION=NOT_ISSUED; L4=false.
PARENT_R17A_SCOPED_WORKFLOW=19/20, independent C9 NOT_RUN.
THIS_R17B_SCOPED_WORKFLOW=18/20, nonauthor R6 PARTIAL and C9 NOT_RUN.

## 실제 R17B 결과

GL2022 JCP157 214302 DOI10.1063/5.0128598 Eq(5)-(7) reactive SQM (NOT EMAA or LAMDA nonreactive): K(T)=Σ_{j=0}^8Σ_{r=0}^9 p_j(T)s_r k_jr(T). p_j=(2j+1)exp[-ΔE_j/(k_B T)]/Z, s_r=1/4 even,3/4 odd. Σ_jr w=5, not 1.

Theorem A: for nonnegative k and fixed positive w, sharp k_a∈[0,K/w_a], assuming at least two positive weights for lower endpoint zero. For target HD(v0,j2)→H₂(v'0,j'1), k_21≤4 Z exp[ΔE_2/(k_B T)]K/15.
Theorem B: for supplied rate-box l≤k≤u, aggregate-box Klo≤w·k≤Khi, sharp target projection [max(l_a,(Klo−Σ_{i≠a}w_i u_i)/w_a), min(u_a,(Khi−Σ_{i≠a}w_i l_i)/w_a)], with infinite-upper convention.
Theorem C: for *externally certified* positive b_j intervals [L_j,U_j], exact monotone weight enclosure w^-_jr=s_r L_j/(L_j+Σ_{h≠j}U_h) and w^+ analog. No certificate of actual b, K or state k acquired here.

Verification: Python pytest 6/6 PASS; external Wolfram exact 12/12 True; alternative-algorithm scipy.optimize.linprog 120/120 PASS max error4.440892098500626e-16 against frozen1e-9 criterion; 90-channel and 2-channel exact toy examples; synthetic-only sensitivity PNG/SVG generated and visually inspected. Repo source code, pytest, LP probe, and figure renderer Git blob SHA matched exact executed local bytes. One initial wrong-cwd import error resolved by correct working directory; not a science discrepancy. Current Python runtime PYTHON_PASS; g++ CPP_PASS. Native subagents not exposed: NOT_RUN; no independent different-author claim.

Original GL2022 state-resolved supplementary ZIP HTTP403, source SHA null, actual selected HD row/rate/T null, physical E_j/certified Boltzmann interval null. Printed thermal TOTAL only: 205K 1.21, 295K 2.21 units10^-10 cm³/s; these are not certified upper bounds on real physical K. Their experimental ±0.2 is a **printed halfwidth**, not declared σ. Do not treat the conditional toy as a rate provider or continuous temperature fit.

Read THEORY_KO.md + src/thermal_projection.py + tests/*.py + delivery/STAGE_LEDGER.json + delivery/INDEPENDENT_LP_CHECK.json. To replay in clean checkout, cd to research/wu_hd_thermal_projection_r17b_20261029, then:

    python -m pytest -q tests/test_thermal_projection.py
    PYTHONPATH=. python tests/independent_lp_probe.py
    python figures/render_sensitivity.py

Dependencies: Python3.10+, pytest, scipy, numpy, matplotlib. Treat package/runtime availability as current-turn dependent.

## 백업의 엄격한 층위

Local frozen original SOURCE ZIP= WU088_HH_R17B_20261029_SOURCE.zip, 119817 bytes, 12 members, SHA256=7c7fa69482adf455a929f64ff0a140c5a355bb2c3809c71cd7f8123d66a55627 (local CRC and per-file manifest SHA verified). Git source and stage ledger published in isolated branch with SHA readback, no main merge or other repo mutation. **This new ZIP was NOT uploaded to Drive or Dropbox; dual original backup is NOT_COMPLETE.** Old R17A S10 original ZIP remains Drive GET/SHA verified per frozen PR153, but its Dropbox binary ZIP 0/10. Do not relabel Dropbox Paper textual handoff a binary-source backup.

## 딱 다음에 수행할 노드

WU_HD_REACTIVE_STATE_SOURCE_NEXT: independently acquire native original GL2022 supplementary bytes, immutable SHA256, selected j=2→r=1 rate row and state and temperature support, spin convention, physical level energy provenance; separately specify *named REC/CR consumer* including densities, clock, full-A and same-state energy ledger, plus a new bounded compute budget and distinct nonauthor review. Only after satisfying dependencies do a source-qualified numerical coupling. Don't re-run frozen R16/R17A science for reassurance, transfer rates by interpolating author fit, read EMAA inelastic as reactive, backfill energy from unrelated REC spectroscopy, or turn HH_R10/production/L4 on.

No proposed strong universal no-go; theorem is conditional elementary finite geometry. Source identity, physical attribution and release readiness remain independent gates.

