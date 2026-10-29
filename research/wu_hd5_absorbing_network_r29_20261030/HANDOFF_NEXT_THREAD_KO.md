# WU088_HH R29 | 새 대화 재개 지침 (source frozen)

`$physmath-research-loop $scispace $exa $wolfram`

```text
PROJECT=cosmosapjw-quantum/WU088_HH
PARENT_PR=167
PARENT_HEAD=cd85b157fdfdf6be0bbe372ff5c282c20a4ca07e
CURRENT_UNIT=WU_R29_HD5_SQM_THERMAL_COLLISION_ABSORBING_REACTION
CURRENT_PR=READ_FINAL_DETACHED_RECEIPT
CURRENT_HEAD=READ_FINAL_DETACHED_RECEIPT
CANONICAL_DAG=34/49_UNCHANGED
R29_AUXILIARY_SCIENCE=1/1_SCOPED
R29_PHYSICAL_CASES=210
R29_PRODUCT_BRANCHING_CELLS=2100
R29_ORIGINAL_RATE_INPUTS=350_REACTIVE_70_INELASTIC_DOWN
R6_DISTINCT_AUTHOR=NOT_RUN
C9_DISTINCT_AUTHOR=NOT_RUN
PES_NATIVE_THRESHOLD=NULL
PHYSICAL_Q=NULL
OWNER_ACK=NOT_OBTAINED
HH_R10=OFF
FULL_A=NULL
L4=false
PRODUCTION=NOT_ISSUED
THEORY_FIRST=true
PHYSICAL_DATA_FIRST=true
NO_MAIN_MERGE=true
NO_FOREIGN_REPO_MUTATION=true
AUTO_NEXT_NODE=false
```

## 불변 원본과 실행

전체 immutable R29 SOURCE ZIP의 SHA-256/bytes는 *source publication 후 detached receipt*에서 확인하라. 원래 R28 전체 ZIP SHA256 `58cb66e566c2481603933f2ee6894f7fe3b05864847285c458ba8cbebadfb8ea`. 원본 GL2022 PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 2011 CDMS v2와 2021 LAMDA는 **원문 출력 전사 소스**로 고정돼 있으며 원본 바이트를 새로 획득한 것이 아니다. 1984 HD J4→3 실측 검산은 source-genealogy 독립성을 보장하지 않는다.

```bash
PYTHONPATH=. python -m unittest discover -s tests -p test_r29.py -q
PYTHONPATH=. python -O -m unittest discover -s tests -p test_r29.py -q
python -m compileall -q src tests
python -m src.network --out results
python -m src.counterfactual
python tests/independent_mpmath.py
```

Expected 20/20 normal, 20/20 -O, 210 full absorbing 5-level source-derived cases, 2100 H2(v'0,J'0..9) branching probabilities, 14 transparent nonthermal down-only sensitivity cases, independent mpmath75 210/210 to approximately 5.3e-14 relative to numpy double. Source SHA, PDF and zip CRC checks included. Original first test regex one-digit exponent error repaired; no altered source data.

## 물리 범위

J=0..4 only, T=[55,105,255,505,1005,2005,3005] K. Source-positive chemical sink q from GL2022 2022 printed SQM rates plus downward inelastic k from R28 original GL2022 PDF; upward detailed balance is a **derived** rate using REC162 2011 CDMS v2 printed energies; Einstein A transcribed from REC161. All other sources (extra HD vibrational levels, different collision partners, full chemistry/nuclear species, original PES-native σ(E), H2(v'>0), actual cosmic bath) are absent. Output is a transparent finite-time-independent tracer conditional model. Never promote Q, reverse, production or F4 owner integration from these coefficients.

## 다음 과학 과제

1. Acquire source-native original 2008 Velilla H3+ ionic PES FORTRAN EPAPS E-JCPSA6-129-612834 and actual energy-resolved σ(E) for same 2022 state and isotope conventions. Reconcile R24 Laplace support bound and R23 spectroscopic candidate without inventing PES Q.
2. Original EMAA HD/H+ 2023 **171 rotational-vibrational transitions, 25 source temperatures**, physical source bytes not yet acquired. Download actual native file and check quantum labels, direction, collision-partner and source units before using; not equivalent to reactive D++H2 channel.
3. Obtain original CDMS2011 v2 raw .egy/.fit/.par/.lin/.cat covariance or other source-owned energy input; preserve REC162 source status.
4. Acquire native complete H2(v'>0), other HD collision partners or owner-acknowledged coupled physical species/bath for real astrochemical kinetics. Trace actual molecular REC/CR owner and request explicit ACK before any foreign mutation.
5. Genuine different-author theory R6/code C9 review; original 49 canonical DAG node-object identity must remain unchanged unless source-authoritative admission conditions are met.

## 보존의 분리

Per-stage ZIPs and 4 actual phase archive uploads are retrospective source evidence records; not 20 independent science runs. Git text commit, Library binary original, independent whole-byte remote readback, Dropbox/Drive provider status are separate. Do not write a backup-verified success without actual receipts.