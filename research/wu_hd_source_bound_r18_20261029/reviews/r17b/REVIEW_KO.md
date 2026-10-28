# WU088_HH R17B 독립 R6/C9 검토

**판정: PASS_SCOPED. 열린 material finding 0건.** Frozen PR154 HEAD `31d3270ef210ef6659915105358f8fdbf8dae5a0`의 조건부 유리수 수학과 해당 Python 구현에 대해 다른 작성 주체인 `/root/r17b_independent_review`가 원문과 코드를 읽고 독립 유도·실행을 수행했다. 이는 blind review는 아니다. WU 과학 DAG는 **33/48**이고 물리적 source 또는 consumer 채택 수는 늘지 않는다.

## 독립적으로 확인한 수학

양의 고정 가중치 w와 비음수 유한차원 rate box에 대해 나머지 좌표들의 가중합 S는 정확히 [Slo,Shi]를 채운다. 목표 좌표 x를 고정하면 가능한 total은 [w_a x+Slo,w_a x+Shi]이다. 이 구간이 [Klo,Khi]와 교차할 필요충분조건은

    w_a x+Slo <= Khi,
    w_a x+Shi >= Klo.

이를 목표 좌표의 원 box와 교차하면 production의 두 endpoint 식을 얻는다. 합성 box의 연속성과 양의 가중치가 endpoint witness의 존재를 보장한다. 무한 upper의 경우에도 유한 Khi와 rate 비음수성이 각 좌표에 유한 상한을 주므로 같은 결과가 성립한다. 구현의 전체 feasibility 검사도 두 가중합 구간의 교차 조건과 일치한다.

기본 0..K/w_a 상한은 다른 좌표들을 0으로 둔 vertex에서 달성한다. 하한 0의 sharpness는 목표 외에 양의 가중치 좌표가 존재하는 경우를 사용한다. R17B 본문은 이 조건을 명시하며 실제 정의된 source-weight vector는 90개 좌표를 갖는다. n=1의 일반 projection 함수는 K/w로 collapse하는 경우와 비음수 전체 구간을 올바르게 처리한다.

Boltzmann-factor interval은 w=s_r b_j/(b_j+sum_other b)에서 각 변수에 대한 단조성으로 유도된다. 분자는 자기 factor에 대해 증가하고 다른 factor에 대해 감소한다. 공통 분모를 유지한 corner extrema가 R17B 식과 일치한다. 개별 가중치들의 극값을 동시에 하나의 physical factor vector가 달성한다는 주장은 채택하지 않는다.

## 원전 대응

[González-Lezana, Hily-Blant, Faure, JCP 157, 214302 (2022)](https://pubs.aip.org/aip/jcp/article/157/21/214302/2842276/A-statistical-investigation-of-the-rate-constants), DOI `10.1063/5.0128598`, §III A 및 Eqs. (5)–(7)를 Exa로 이번 검토에서 직접 읽었다. 원문의 reactive arrangement와 초기 HD j=0..8, 최종 H2 r=0..9, even 1/4 및 odd 3/4 계수는 코드와 일치한다. 초기 확률은 합이 1이고, 최종 channel 계수는 합이 5이므로 전체 90개 가중치의 합은 5다. 공통 energy-zero shift는 분자와 partition sum에서 소거된다. 원문의 두 printed total과 Arrhenius fit을 state row나 rigorous interval로 승격하지 않은 구분도 적절하다.

이 검토는 원본 reactive supplement bytes, 실제 state row, HD 에너지 interval 또는 consumer density/clock을 확보하지 않았다. 해당 source 결속 의무는 그대로 열린다.

## 독립 실행과 identity

기존 6pytest·120LP 또는 이전 R16/R17A suite를 재실행하지 않았다. 새 `independent_vertex_review.py`는 production projection 식을 oracle로 복제하지 않고 clipped-box의 모든 geometric vertex를 exact Fraction으로 열거했다.

| 항목 | 실제 결과 |
|---|---:|
| Synthetic box/slab cases | 160 |
| Exact target projections 및 endpoint witness | 309 PASS |
| Empty-polytope rejections | 93 PASS |
| Infinite-upper cases | 76 |
| Nonzero-lower cases | 152 |
| Singleton cases | 40 |
| Boltzmann factor corners | 512 |
| Target weight sharp intervals | 18 PASS |
| Invalid-contract rejections | 9 PASS |

현재 Python probe는 PYTHON_PASS다. 최종 실행은 exit 0, CPU 약 0.183초, wall 약 0.183초였다. 실제 실행 증거와 source hash는 `INDEPENDENT_REVIEW_EXECUTION.json`에 있다. Theory/module/tests/LP/stage ledger의 Git blob은 5/5 원격 frozen identity와 일치했다. 실행된 module은 Git blob `4f9889e21444033e079d0f003ca6069d30406c5b`, SHA256 `b9acaee80c857f8f8b6dd97697dafc17004a7ec048bb302f220b0e04f20a7dd9`다.

초기 scratch transfer는 파일 끝 LF를 하나 추가했으며 첫 scratch 실행의 blob이 원격과 달랐다. 이를 identity 검사에서 발견해 LF 한 바이트만 제거했고, 다섯 원문 모두 Git blob 일치를 확인한 뒤 같은 독립 검사를 다시 실행했다. 이전 결과는 `INITIAL_TRANSFER_EXTRA_LF_EXECUTION.json`에 보존했다. 원 저장소 과학 코드의 수정이나 수학적 결과 차이는 없었다.

## 검토 범위와 채택 권고

R6의 조건부 증명 독립 검토와 C9의 frozen 구현 독립 검토는 이 evidence 범위에서 충족된다. 부모가 이 review와 source identity를 결속해 게시하면 R17B workflow의 남은 두 검토 의무를 닫을 수 있다. 원전 state row의 독립 검토, 실제 화학 선택규칙을 포함한 attainable rate manifold, 물리적 full-A 결속은 이 한정된 검토의 수용 범위 밖 의존성이다.

새 strong no-go 결과를 채택하지 않는다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`, physical/central delta=0을 유지한다. 추가 수학·코드 수정 권고는 없다.
