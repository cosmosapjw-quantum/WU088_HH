# 새 적분 구간의 재사용·부분 집계 계약

고정 표적은 기존 Frozen107의 primitive 0이다. source의 좌표·위상·단위·107개 signed coefficient와 저장 순서는 바꾸지 않는다. 양쪽 변수의 전역 직사각형은 `[1/512,2^40]^2`이고 정밀도는 128bit다. 원 endpoint 결과를 재계산하지 않는다.

## 정의와 유도

log2 축 `[-9,-6,-4,-1,2,5,8,11,14,17,20,23,26,29,32,35,38,40]`의 Cartesian product는 289개 셀을 만든다. 셀 내부는 서로 겹치지 않으며 공통 경계는 적분 측도 0이다. accepted index 집합을 S, 셀 적분의 실수·허수 구간을 각각 `[a_{s,p},b_{s,p}]`로 쓰면, 유한 가법성과 포함관계에 의해

`I_p(union_{s in S} C_s) in [sum_{s in S} a_{s,p}, sum_{s in S} b_{s,p}]`

이다. 모든 endpoint는 정확한 dyadic 유리수이고 합산은 Fraction으로 실행한다. 따라서 합산 과정에서 새로운 부동소수점 반올림 오차가 생기지 않는다. 합산 radius는 `sum_s (b_{s,p}-a_{s,p})/2`와 정확히 같다.

중복 cell ID와 중복 native receipt를 거절한다. 동일 셀을 두 번 더하거나 다른 window의 기록을 끼워 넣을 수 없다. source binding, primitive index, 실제 window, precision, 원 native plan/receipt hash를 모두 확인한다. Hash는 바이트 동일성 근거이며 계산 진위·물리 타당성 자체의 증명은 아니다. native output의 신뢰는 기존 검토된 source와 backend의 계약에 조건부다.

## 기존 W1 16타일의 재사용

기존 W1의 `[1/16,256]^2` 16개 셀은 새 partition에 그대로 포함된다. 기존 validator의 원 raw receipt·stdout·host receipt·dispatch/return과 전체 집계를 다시 읽어 검증한다. 입력 archive와 canonical record, 같은 primitive, kernel/build/backend, window 동일성이 유지되는 경우에만 새 전역 계획에 연결한다. 기존 수치 적분을 재실행하지 않는다.

원 native request의 radius 지수 `-52`는 그대로 보존한다. 새 할당 `2^-57`에 대한 통과 여부는 원본 serialized interval의 실제 radius로 판단한다. 작은 실제 radius를 얻었다고 원래 요청값을 `-57`로 고쳐 쓰지 않는다.

## 이번 실제 실행 범위

새 실행은 다음 4개 셀까지만 허용한다.

| 새 cell ID | log2 t | log2 u | 위치 |
|---|---|---|---|
| 20 | `[-6,-4]` | `[-1,2]` | W1 인접 하단 t strip |
| 52 | `[-1,2]` | `[-6,-4]` | W1 인접 하단 u strip |
| 105 | `[8,11]` | `[-1,2]` | W1 인접 상단 t strip |
| 57 | `[-1,2]` | `[8,11]` | W1 인접 상단 u strip |

두 변수 방향을 따로 실행하며 전치·복소켤레 대칭을 가정하지 않는다. 먼 tail이나 corner까지 대표한다고 주장하지 않는다. 새 타일당 radius `2^-57`를 요구하며, 예전 실제 W1 최대 component radius `r_W1`에 대해 `r_W1 + 273*2^-57 < 2^-48`인 조건부 전체 예산을 유지한다. 이번 4타일 통과만으로 나머지 269타일의 통과를 추론하지 않는다.

실행 계약은 동시 2개 Python worker, worker당 180초·1GiB, native당 120초 요청/125초 hard wall·1GiB·200,000 evaluation·1,024 integration calls다. source를 확인한 기존 host의 부모 종료 시 SIGKILL과 native 자식 생성 금지를 유지한다. 첫 관측 거절 이후 새 작업 배치를 중단하고 이미 시작한 작업은 회수한다. 자동 재시도와 성공한 이전 작업의 재실행은 없다.

## 결론의 범위

집계값의 domain은 **accepted 셀들의 합집합**이다. 누락된 내부 영역의 기여를 0으로 두거나 radius에 암묵적으로 흡수하지 않는다. `missing_domain_contribution=NOT_BOUNDED_OR_INCLUDED`로 기록한다. 전체 직사각형 바깥에 대한 기존 endpoint 상계를 이 부분 적분에 더해 전체 양의 영역 적분으로 선언할 수 없다.

이 구현이 받아들이는 신규 셀은 위의 4개로 고정된다. 289개 전체 실행·집계로 확장하려면 별도의 명시적 실행 계약이 필요하다. 정규화와 source-prescribed contraction, 전체 2,592 primitive, 최종 D/epsilon, physical/scientific/production admission은 이 단계의 결론이 아니다.
