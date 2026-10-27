# S08 최종 physics·figure 독립 검토

## 판정

**ACCEPT_V2_FIGURE_AND_CONDITIONAL_CLAIM_PRESENTATION.** 동결된 v2 PNG를 실제로 열어 확인했고, 그림·manifest·기존 이론 및 독립 reference가 같은 범위를 표현하고 있다. Blocking finding과 필수 수정은 없다. 이 판정은 v2 그림과 조건부 주장 표현의 승인이다. 실제 rate/Q, consumer 또는 production의 승인은 포함하지 않는다.

| 선택된 산출물 | SHA256 |
|---|---|
| source_fit_diagnostics_v2.png | 5c837359c5a6c045ffd5e458471bff4790c2c565696fdb1ffcdc71b9dbcb44db |
| source_fit_diagnostics_v2.svg | ec12aec6cdd32caa9e33c5c56926ad7e95d41e01eb6617a2b5a9402f71ce94d8 |
| source_fit_diagnostics_v2_MANIFEST.json | 96bfefda72aac9a504d48d646cbf4fdf235148128df077cbb35b20ce56a56272 |
| 저장된 fit_diagnostics.json | 5f687fac3c21dc8a9747c45ac6558a4b9d7c107577d6d9eb9285bc13a9c7f599 |
| 저장된 INDEPENDENT_RESULTS.json | ac42d76bcb5471b32c4b635bb20998256181bc3227ed39855e889c505790bf56 |

PNG는 original detail로 직접 보았다. SVG는 동결 manifest와 실제 hash를 확인했으며, 별도로 렌더링하지 않았다.

## 1. 실제 그림에서 확인한 내용

500 K의 LiH 잔차 피크와 두 분모의 marker가 모두 보인다. 최대 잔차 설명은 data axes 밖의 panel title로 이동하여 피크를 가리지 않는다. HD residual legend도 비어 있는 center-right 영역에 놓여 205 K와 295 K 점을 가리지 않는다. 제목, 축, 단위, legend와 footer에 clipping 또는 data occlusion을 발견하지 않았다.

상단 panel은 인쇄된 source 값과 출판된 formula sample을 다른 marker로 구분한다. LiH는 27개 원표 node, HD는 두 개의 인쇄 SQM 비교점임을 제목에 명시한다. 실험 측정값이라고 잘못 표시하지 않는다. 온도 단위는 K, coefficient 단위는 \({\rm cm^3\,s^{-1}}\)이다. LiH에는 log 축, HD에는 linear 축이 사용되며 온도별 marker가 명확하다.

하단 panel은 signed numerator를 formula minus printed value로 표시하고, printed-value 분모와 formula 분모를 구분한다. 최대 잔차 설명은 table 기준임을 명시한다. 그림은 두 상대오차 정의를 혼합하지 않으며, footer에서 두 값 모두 물리적 불확실성 상계가 아니라고 설명한다. 저장된 27+2 node만 marker로 보여 주며 source curve를 새로 fit하거나 보간한 표현을 만들지 않는다.

## 2. 첫 그림 보존과 변경 범위

첫 PNG와 SVG가 원 manifest의 hash 그대로 남아 있음을 확인했다. 첫 그림의 occlusion 관측은 보존된 VISUAL_QA.json에 기록되어 있고, 선택된 v2와 구분되어 있다. 이 reviewer는 첫 그림을 다시 렌더링하거나 덮어쓰지 않았다.

실제 첫 plot code snapshot과 현재 plotting code의 diff도 읽었다. 변경은 별도 output stem과 파일 보존 guard, 세로 크기 조정, 최대값 annotation의 title 이동, HD legend 위치 변경, 별도 manifest 이름과 exclusive creation이다. 데이터 선택 또는 source formula의 변경은 없었다.

v1과 v2 manifest가 같은 diagnostic SHA와 같은 independent reference SHA를 가리킨다. 두 manifest 모두 29 samples, 새 source formula 평가 0, interpolation/extrapolation false를 기록한다. 이 layout 수정 때문에 과학 계산을 재실행할 필요는 없다.

## 3. 수치 결과가 지지하는 범위

저장된 독립 결과는 8/8 groups, 80-digit Decimal reference의 29 nodes, 구현 상대오차 최대

\[
1.942018822568154\ldots\times10^{-16}
\]

을 기록한다. 해당 검사의 사전 허용 한계는 \(2\times10^{-14}\)다. 이는 **같은 출판 formula의 sampled implementation 재현성**을 뒷받침한다. 원표에 대한 fit 잔차, 물리적 rate 정확도, 전체 온도 구간, interpolation 또는 model discrepancy의 상계가 아니다. 이번 reviewer는 그 수치 검사를 다시 실행하지 않았다.

Bennett의 500 K에서 table 분모의 최대 상대잔차는 저장된 reference에서 약 0.2481021851, formula 분모에서는 약 0.1987835516이다. 두 값은 같은 formula/table 쌍의 다른 정규화다. 원 source의 fit-error 분모가 명시되지 않았다는 BENNETT500_SOURCE_NOTE의 결론을 유지하며, 이를 논문 모순이나 수치 구현 실패로 단정하지 않는다. 원 formula와 첫 primary 출력은 그대로다.

## 4. 조건부 이론과 Wolfram 근거

THEORY_ADMISSION.json은 기존 독립 R6 검토와 고정된 proof/CLAIMS SHA를 참조하여 13개 조건부 claim을 승인한다. \(h>0\), 전체 비음수 cone, hidden state와 독립적인 prescribed \(\pi\)가 scalar iff의 가정이고, \(h=0\) 및 제한된 manifold의 예외가 별도다. Formation \(b\)는 정수 state-channel 사건의 가중이며 개별 사건의 분수 생성물이 아니라는 해석도 반영되어 있다.

실제 Wolfram request, raw receipt와 parsed result를 읽었다. 저장된 한 번의 호출은 선언된 finite matrix의 36개 zero entries, finite symbolic identities 5개, 작은 예 2개를 확인한다. 이 수는 유한 명세에 대한 결과다. 임의 상태 차원의 일반 정리를 finite examples만으로 증명했다고 주장하지 않으며, 일반 증명의 근거는 별도 R6 analytical review다.

실제 source가 완전한 state-resolved \(d,\pi,b\)를 제공한 것은 아니다. 물리적 closure defect의 수치값도 null이다. Wolfram 호출로 source rate/Q 또는 상태 population을 추가 승인하지 않았다. 기존 PHYS91 Wolfram remaining=0은 보존되고 old-budget transfer가 없다는 receipt도 일관된다.

## 5. DAG와 물리적 승인 경계

검토 시점 DAG SHA는 e2dd85b94cb9fd2ca0696e2fbcb1e4560cf0205e2c8f2022d02a4b2dd102dc99이며, scoped completion은 **8/24**다.

| 분류 | 기록된 수 |
|---|---:|
| 보존된 original 20 중 strict complete | 5 |
| 추가한 4개 중 scoped complete | 3 |
| 전체 local scoped complete | 8/24 |
| Complete에 합산하지 않는 implementation-only PASS | 2 |

추가된 완료 셋은 LiH source, HD source, 조건부 state-lift theory다. Code node의 최종 admission은 이 좁은 figure 검토에서 변경하지 않는다. 저장된 구현·reference 결과와 후속 C9/final admission은 구별한다. 이 수를 physical consumer 8개 또는 전체 분자·동위원소·음이온 registry의 완료로 해석하지 않는다. 중앙 DAG의 새 완료도 추가하지 않는다.

Physical rate, nuclear Q, energy partition, consumer state binding, named runtime consumer와 activation은 false다. HH_R10=OFF, production=NOT_ISSUED, L4_ready=false를 유지한다.

## 6. Preflight와 이번 검토의 실행 범위

최신 AGENTS, local HEAD ffed56b979b2ddc7cd278579f884e1a5a2067b69, S08 preflight의 2026-10-27T06:24:34.657Z 원격·병렬 관측, S07 delivery receipt를 읽었다. S07 source ZIP SHA f2c57dc5902a67ad61340322be5c1285586f7020c1b6167d10c6e098133d7598의 실제 Dropbox/Drive upload ACK는 있으며, final full-source 원격 byte readback은 별도다.

이번 작업은 actual PNG 보기, 저장된 문서·결과·manifest·code diff 읽기와 hash 확인, 리뷰 파일 작성에 한정된다. 새 source 추출·native cell 확인·fit/residual 평가·reference 평가·compiler·Wolfram·plot generation·기존 science suite 재실행은 모두 0회다. 도구 및 준비 비용은 측정하지 않았으며 0이라고 주장하지 않는다.
