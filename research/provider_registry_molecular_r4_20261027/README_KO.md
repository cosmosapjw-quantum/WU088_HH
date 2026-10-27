# LiH·HD 공급자 상태 연결 R4

고정 인계서와 R1/R2/R3 실제 입력을 재사용하여, 분자 생성·파괴 공급자 행과 상태별 사건 수 연산자를 구성한다. 현재 계약은 `CONTRACT.json`, 원본 재사용 identity는 `REUSED_CALCULATIONS.json`이다.

## 완료 수의 뜻

원20 DAG 노드 중 literal COMPLETE 상태는5개다. 구현/PASS2개는 별도로 표시한다. 이번에4개의 정확히 한정된 자식 노드를 추가하여 시작 표기는 **5/24**다. 이 분자는 scoped source/정수 산출물 완료이며 물리 consumer 완료율이 아니다. 중앙88노드는 별도이며 현재 엄격 COMPLETE는18/88, 기존 선언 scoped gate집계는27/88, 미병합 PR236의 작업 집계는32/88이다. 이 셋을 합산하지 않는다.

각 R1–R10과 C1–C10 단계는 같은 번호의 공유 체크포인트 S01–S10으로 게시·양쪽 백업한다. 과학 단계별 결과·근거와 실제 게시/백업 영수증은 분리하여 기록한다.

## 물리 입력

Bennett2003의 LiH 자발 방사결합은 최종 bound/quasi-bound 상태 합과 방사 생존 weighting을 포함한다. 전자 통계 인자1/4는 이미 공급자 계수에 있다. Bovino2009의 ortho/para 행은 원 상태·스핀 가중치가 미결인 채 보존한다. HD 생성의 TIQM/SQM은 대체 계산이며 합산하지 않는다. HD 파괴의 thermal initial ensemble과 생성의 para-H2(v=0,j=0)는 자동 역반응 pair가 아니다.

과거 합성249검사, source availability, native fit 구현, 물리 rate/Q, state lift 및 실제 소비자는 서로 다른 수용 범위를 가진다. 새 명령이 없는 이전 성공 계산은 재실행하지 않는다.
