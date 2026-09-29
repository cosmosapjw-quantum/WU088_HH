# R31AD 기존 다섯 node 재현

z=0,1,2,3,4의 저장된 mixed OD와 독립 dotO를 읽기만 하여 unit-cell cubic O/linear K 후보를 재현했다. z=1과 z=3은 R31AD의 training으로 소비되므로 R31AD 독립 validation 지점은 0개다. 원본 dtype과 모델 진단 dtype은 `FIVE_NODE_INPUT_MANIFEST.json`에 분리했다.

후보 중 z=1.5에는 기존 OD 단독 출력이 있으므로 fresh selection에서 제외했다. 나머지 후보의 frozen-model separation은 `MIDPOINT_SELECTION.json`에 기록했고, 최대 S인 z=0.5 a0를 다음 검증 후보로 선택했다. `NEXT_VALIDATION_PREREGISTRATION.json`은 해당 선택과 E_K/E_Dmax Pareto 판정, 1e-10 tolerance를 잠갔으며 `execution_authorized=false`다. S는 지점 선택용이고 모델 승패 점수가 아니다.

이번 실행의 science node 수는 0이다. `RETURN.json`에 실행, 원본 결합, 미완료 gate를 기록했다.
