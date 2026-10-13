# WU088_HH PHYS19 — HH·birth 순수 곡률과 유한 응답

**과학 판정: PROMOTE_SCOPED.** PHYS18의 동일한 fixed-alpha, same-COMMON,
전역 λ,b∈[0,1]²인 C² 계열에서 두 순수 온도 결함 곡률을 실제 계산했다.
F=T(two half)-T(Full), h=625000000 s이며 gas 4좌표와 photon 35개 slot을 보존한다.

| 결과 | 외향 포함 또는 안전한 상계 |
|---|---|
| Fλλ [K] | [-4.510292217171e-14, -3.084478303660e-14] |
| Fbb [K] | [-4.912098573204e-11, -4.450662359403e-11] |
| Fλb [K], PHYS18 재사용 | [-2.668505746423e-12, -2.118796636045e-12] |
| det Hessian [K²] | [-5.748125770240e-24, -2.273799188447e-24] |
| v=(1,-1/24)의 곡률 [K] | [4.618397504729e-14, 1.142622520923e-13] |
| Bilinear corner 재구성 오차 [K] | ≤6.145761081776e-12 |
| 정확한 pure midpoint 보정 오차 [K] | ≤2.892887673208e-13 |
| 명시한 finite-decimal midpoint 사용 [K] | ≤2.892887673216e-13 |
| 계수 반폭까지 포함한 중심값 모델 전체 오차 [K] | ≤0.0001557338140092 |

두 좌표축에서는 각각 엄격히 오목하며, 전체 Hessian은 양·음 고유값을 하나씩 가진다.
고정 방향 v의 양의 곡률은 사각형 내부에 놓인 선분에 적용한다.
현재 첫 도함수가 0이 아니므로 정지점의 존재를 뜻하지 않는다.
작은 재구성 오차는 실제 동일 계열의 corner 계수를 유지한 형상 오차다.
마지막 행은 그 계수도 수치 중심으로 바꿨을 때의 별도 전체 예산이다.

## 읽을 파일

- [13쪽 연구 보고서](report/WU088_HH_PHYS19_THEORY_20261013.pdf): 질문, 주요 결과, source·carry·endpoint 유도, 유한 온도 quotient, 보간 증명, 물리 해석과 다음 질문.
- [정확한 수치 포함](checks/application/run01/results/CURVATURE_RESULTS.json), [Hessian·재구성 읽기](checks/application/readout02/results/CURVATURE_GEOMETRY.json).
- [독립 원식 유도](theory/PURE_CURVATURE_INDEPENDENT_DERIVATION_KO.md), [독립 수치 심사](review/INDEPENDENT_REVIEW_KO.md).
- [최종 채택](review/DECISION.json), [R1–R10/C1–C10 상태](state/RESEARCH_STATE.json).
- [재현 방법](REPRODUCE.md), [다음 실행 인계](HANDOFF_KO.md), [다음 입력 계약](contracts/NEXT_CONSUMER_CONTRACT.json).

## 실제 검증

23개 원 입력의 bytes와 SHA-256을 대조했다.
새 source·reaction fit·root·history 실행은 각각 0이며,
동결된 입력에서 이번 순수 응답만 계산했다.
main wrapper는 1.569 s, 최대 RSS 55,992 KiB였다.

독립 Fraction 구현의 최종 run03에서 362개 검사,
2,057개 스칼라 포함 비교와 3,174개 외향 decimal 검사가 모두 통과했다.
독립 wrapper는 1.870 s, 최대 RSS 52,448 KiB였다.
검사기만 고친 두 앞선 시도의 로그와 snapshot도 보존했다.

실제 Wolfram 15.0.1에서 xTensor 1.3.0·xPerm 1.2.4를 로드하여
6 tensor, 13 scalar, 14 matrix component가 literal 0,
Peano 관련 4개 조건이 True임을 확인했다.
두 번째 Wolfram 호출은 exact rational Hessian·방향 계산을 독립 확인했다.
원 경고와 canonicalizer backend 선택을 포함한 request/response가
checks/wolfram/에 있다.

## 다음 연구 단위

PHYS20은 실제 이름과 identity가 있는 rei_bianchi 소비 구간 하나를 회수해,
기존 HH_DOMAIN_SCREEN와 HH_MATERIALITY에 연결한다.
첫 목표는 HH의 절대 온도 변화율 [K/s]과 전자 생성률 [per H/s]의 source 표다.
현재 consumer binding은 unverified이며 다음 과학 계산은 아직 실행하지 않았다.
기존 RUX 전역 DAG와 HH_STRICT_NATIVE·HH_SINGLET의 독립 lane은 유지한다.

원 producer JSON의 CANDIDATE_COMPUTED 표시는 실행 당시 상태로 보존되어 있다.
현재 scientific adoption은 별도 review/DECISION.json이 결박한다.
원격 게시와 백업의 실제 identity는 publication/의 영수증에 연결된다.
