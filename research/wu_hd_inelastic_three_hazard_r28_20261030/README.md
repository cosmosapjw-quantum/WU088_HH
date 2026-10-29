# WU R28 | Original GL2022 inelastic 1560-cell atlas & three-clock conditional physics

**Real research unit** of WU PR166 at `0505e978b31f976015d7ed8d12c4a5dc4fe42989`. Source GL2022 JCP157 214302 DOI 10.1063/5.0128598. Original institutional supplementary PDF sha256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, size 273554. Preserved R27 physical data SHA256 `b72af2990fbddbc46a496238d9d0d50ad8eb26e61b8e810f27228222e3814339`.

Reproduce *only from* complete original archive (includes original source PDF and immutable prior R27 zip). From extracted `R28` directory:

```bash
PYTHONPATH=. python -m src.three_hazard --pdf sources/GL2022_CSIC_supplement.pdf --r27 sources/R27_SOURCE_REACTIVE_RADIATIVE.json --out results
PYTHONPATH=. python -m unittest discover -s tests -p test_r28.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r28.py -q
python -m compileall -q src tests
PYTHONPATH=. python tests/independent_mpmath.py
```

Source tokens are source-printed *computed SQM values*, not experiments. The `1560` numbers in original PDF tables 12–28 and R27 tables 1–10 make physically distinct reaction tensors. The R28 model compares only source-present downward HD(0,J)->HD(0,J'<J) with source R27 Eq6–7 forward chemical reaction and REC161 J->J−1 Einstein A at exactly 10 source T nodes. It excludes upward transitions, full nonLTE, reverse, physical Q, native PES, cosmic density history.

Central DAG **34/49 unchanged**, scoped R28 data 1/1, R6/C9 distinct-author NOT_RUN. `physical_Q=null`, `owner_ACK=null`, `HH_R10=OFF`, `full_A=null`, `L4=false`, `production=NOT_ISSUED`. Git text source atlas and validation, raw PDF in complete source ZIP/Library, no main/foreign edits.