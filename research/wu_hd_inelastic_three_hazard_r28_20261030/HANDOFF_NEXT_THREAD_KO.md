# WU088_HH R28 | 후속 연구·재현 계약

```text
$physmath-research-loop $scispace $exa $wolfram
PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=166
PARENT_HEAD=0505e978b31f976015d7ed8d12c4a5dc4fe42989
R28_BRANCH=research/wu-hd-inelastic-three-hazard-r28-20261030
R28_PR=SET_FROM_LIVE_GITHUB_AFTER_PUBLICATION
R28_HEAD=SET_FROM_LIVE_GITHUB_AFTER_PUBLICATION
CANONICAL_DAG=34/49_UNCHANGED
R28_AUXILIARY_PHYSICAL_SOURCE=1/1_SCOPED
INELASTIC_SOURCE_CELLS=1560
THREE_HAZARD_ADMITTED_ROWS=43/60
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
NATIVE_SUBAGENT=NOT_RUN
PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
```

Immutable original GL2022 SI PDF: 273554 bytes, SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. Original R27 result SHA256 `b72af2990fbddbc46a496238d9d0d50ad8eb26e61b8e810f27228222e3814339`. Original R27 full ZIP SHA256 `a2b7810035fadf8edfe1821660582bec820bcf5aed0d57a636b01321a3ab7aa0`. Every current physics source cell is copied literal from original GL2022 Table12–28 with cross-engine PDF text check, not invented or fitted. R27 parent remains immutable.

**New scientific result:** 1560 printed inelastic-transition source cells, 210 ground-vibrational J1..6 downward cells, 43 source-qualified three-event crossover probabilities (at R27's ncrit). At 105K J2 source: K_ex=1.30461670021225166825e-10 cm3/s, K_down=1.143e-9 cm3/s, A=5.159e-7/s, P_first_exchange=0.09292649128354858. This is conditional on specified one-step competing exponential hazards and the R27 Eq6-7 spin-effective reaction policy; no full nonLTE, no cosmological population output.

**Reproduction:** extract original R28 full SOURCE ZIP; `PYTHONPATH=. python -m unittest discover -s tests -p test_r28.py -q`; repeat with `python -O`; `python -m compileall -q src tests`; `PYTHONPATH=. python tests/independent_mpmath.py`; `PYTHONPATH=. python -m src.three_hazard`. Inspect full data and original suspect literals. Expected 15/15 normal and 15/15 -O, original 1560/1560, independent 43 rows; retain actual logs. **Future runs must not assume tests were run in their new environment.**

**Next:** authenticate Velilla2008 original EPAPS E-JCPSA6-129-612834 binary and same-PES native sigma(E), energy zero, isotope offset; reconcile JCP2022 Eq5 j0..8 versus Table11 SI description j0..6; independently qualify R6/C9 and obtain named actual REC/CR 4-molecular-species owner ACK; only then consider canonical DAG promotion and Q/production gating. No invented new threshold from thermal rates, no main merge, no foreign mutation. Prefer new genuine source data over metadata loops.
