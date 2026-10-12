# HH atomic-reuse 재편 계약

2026-10-12 KST. 현재 사용자 요청은 첨부 REI Atomic-Reuse DAG를 사용하여 WU088_HH의 연구계획을 다시 재편하는 것이다.

## 완료조건

1. 첨부 4개 원본을 byte 그대로 보존하고 역할·출처·hash를 연결한다.
2. 실제 PR46/PHYS12를 현재 과학 기준점으로 유지한다. 과거 S14·PHYS11·PR45 계획은 보존한다.
3. 원 global RUX00–16의 dependencies와 PROPOSED_NOT_EXECUTED 상태를 바꾸지 않고 HH local 기여를 매핑한다.
4. 보존 결과·사건 owner·소비 계약·관측량 판정 규칙·작업 카드·DAG·NCP 정책과 인계문을 만든다.
5. RUX14의 준비와 실제 EoR 소비를 나눈다. 생산자 준비는 현재 가능하고 실제 EoR 효과에는 RUX11의 실제 증거가 필요하다.
6. HH strict-native/singlet의 완료를 REI baseline에 요구하지 않는다. 독립 HH 연구에도 REI 완료를 요구하지 않는다.
7. 계획의 의미·참조·cycle·보존 조건을 한 번의 bounded 구조 검사와 독립 noncreator 검토로 확인한다.
8. WU088_HH root 진입점에 반영하고 기존 승인 범위에서 새 branch/PR 및 이중 백업·최종 파일을 남긴다.

## 작업 범위와 근거 상태

이번 작업은 planning/interface 계약 작성이다. source/native solver·과거 과학 suite·PHYS12 endpoint·그림을 재실행하지 않는다. 새 PHYS13 또는 새 global RUX PASS를 선언하지 않는다.

PHYS12의 독립 PROMOTE_SCOPED는 기존 과학 증거다. 첨부 DAG·계획은 사용자 제공 proposed snapshot이다. 첨부에 특정 REI commit/head가 없어 현재 REI 물리입력 채택 상태를 새로 확정하지 않는다. 과거 N2 HOLD를 현재 입력 부재의 증거로 읽지 않는다.

소비자가 정하지 않은 관측량·허용오차·시나리오·callback은 null로 남긴다. 현재 heavy_queue=[]와 launch=false다. 새 공개 대상은 HH 계획과 계약이며 다른 repository의 계획·코드·과학 상태를 수정하지 않는다.

## 변경과 검증의 구분

원본 identity, DAG 구조, 계획상 source/owner 의미, 실제 runtime admission, 과학적 정확성, Git object 게시, provider ACK, 원격 복원은 서로 다른 판정이다. 독립 계획 검토는 새 물리 결과를 인증하지 않는다. 유효한 저장·게시 verification tier가 닫히면 동일 데이터를 반복 다운로드하거나 감사하지 않고 종료한다.
