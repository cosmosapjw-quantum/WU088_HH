$physmath-research-loop $scispace $exa $wolfram
WU088_HH의 R19 이후 실제 named consumer 결속을 재개하라.

REPO=cosmosapjw-quantum/WU088_HH
PARENT_PR=155
PARENT_HEAD=f7371c7c389cac9c1b504f6e741b80ea80d776f1
R19_BRANCH=research/wu-hd-105k-nominal-exact-flow-r19-20261029
R19_PATH=research/wu_hd_nominal_exchange_r19_20261029
SOURCE_PDF_SHA256=a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754
R18_SOURCE_MODULE_GIT_BLOB=be2a845263b215b604f255ffe5deabe55be9dd7b
SOURCE_RATE_105K_SI=23/200000000000000000 m^3/s
CANONICAL_WU_DAG=34/49_UNCHANGED
R19_WORKFLOW=18/20 (R6/C9 distinct-author review NOT_RUN)
HH_R10=OFF
PRODUCTION=NOT_ISSUED
L4=false

## 이번 이론/코딩 결과

원본 DIGITAL.CSIC GL2022 Table2 page6 H+ + HD(v0,j2) -> D+ + H2(v0,j1) SQM 105K 명목 source rate를 R18 source-verifying loader로 취득한다. 외부 고정 등온 bath, 한 방향 4종 모형, 물리 수밀도 n(m^-3), proper time(s), 외부 prescribed volume v=V/V0에 대해 정확한 반응 extent를 구현했다. `tau=int dt/v`, `N=v n`이면 정적 mass-action 정확 해를 사용할 수 있다. H/D 핵수, 양전하 보존, 양성성, isolated rank-one Jacobian, k 민감도와 Q가 별도 공급되는 경우의 형식적 에너지 ledger를 유도했다.

실제 테스트: Python pytest24/24, mpmath80자리160/160, SciPy DOP853 3/3, Wolfram symbolic9/9, 시각검토한 2개 그림. CLI 예제 nH+=nHD=1e6 m^-3, products0, t=1e10s -> reactants465116.27906976745, products534883.7209302326 m^-3. Source uncertainty, reverse reaction, physical Q, full-A, actual Bianchi/REC/CR owner consumer는 미제공이다. Native subagent 도구는 현재 호출에 노출되지 않아 R6/C9 비저자 심사 미실행. 같은 모델의 자체 CAS·별도 알고리즘 검산을 비저자 심사로 재분류하지 마라.

## Clean checkout 재현

1. R19 Git branch의 새 파일들과 부모 R18 source module을 읽고 Git blob SHA를 확인하라.
2. 원본 PDF를 R18 S10 Drive source ZIP의 `ORIGINAL_SOURCES/GL2022_CSIC_supplement.pdf`에서 복원하거나 기관 원문 URL로 받되 SHA/273554 bytes를 확인하라.
3. repo root에서 실행:

   export WU_R19_SOURCE_PDF=/absolute/path/GL2022_CSIC_supplement.pdf
   python -m pytest -q research/wu_hd_nominal_exchange_r19_20261029/tests/test_nominal_exchange.py
   python -m research.wu_hd_nominal_exchange_r19_20261029.tests.independent_mpmath_reference
   python -m research.wu_hd_nominal_exchange_r19_20261029.figures.render_nominal
   python -m research.wu_hd_nominal_exchange_r19_20261029.src.nominal_exchange --source-pdf "$WU_R19_SOURCE_PDF" --initial-m3 1000000 1000000 0 0 --proper-seconds 10000000000 --output /new/output/path.json

Dependencies: Python>=3.10, pdftotext (Poppler), NumPy, SciPy, pytest, mpmath, matplotlib. Re-probe current runtime; do not inherit old failures. CLI output uses exclusive-create. Use new paths and finite budgets; do not rerun R16/R17A/R17B/R18 historical suites without changed dependency.

## 다음 실제 연구 노드 (순서)

1. WU_HD_105K_OWNER_CONSUMER_BINDING: find actual named REC/CR repo/path/function/commit and explicit state order, density units, time coordinate and `dt/ds`, positive volume/thermal history. Source T=105K and states must match; no 100K/300K interpolation without independently qualified model. Owner acknowledgment required before mutation.
2. WU_HD_REACTIVE_STATE_ENERGY_LEDGER: source the actual state-dependent energy/mass defect Q, bath/stopping/thermal electron and photon ledger. Current Q is symbolic only.
3. WU_HD_REACTIVE_RATE_UNCERTAINTY: source-qualified error model for original SQM nominal rate and its impact on full-A and observable. Printed decimal precision is not a physical uncertainty enclosure.

For each new unit do a bounded theory-first then coding loop, publish only to isolated branch/Draft PR, record completed/total canonical DAG with unchanged authority until explicit admission. Every stage must distinguish Git publication, Google Drive binary original ZIP, Dropbox text-only Paper versus actual Dropbox binary original; never claim two-provider binary backup from a text receipt. No main merge or other-owner code mutation without actual owner ACK.
