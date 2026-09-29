# R31AF six-node read-only 재현

기존 z={0,0.5,1,2,3,4} mixed OD와 독립 dotO를 source hash로 묶어 R31AD interpolation engine을 수정 없이 재사용했다. z=0.5는 R31AF training에 소비되어 R31AF construction-time independent validation 지점은 없다.

원본 complex256/complex128 dtype은 `SIX_NODE_INPUT_MANIFEST.json`에 기록했고, interpolation 진단만 complex128에서 수행했다. 여섯 node 재현, 내부 O C1/K/D 연속성, dense-grid metric identity는 `R31AF_MODEL_REPLAY.json`에 있다. z=0.5 direct residual로 얻은 derivative 필요 하한은 source-error certified enclosure가 아니다.

z=3.5 a0의 R31AF 예측은 R31AD pre-output 예측과 동일하다. frozen separation과 선택은 `Z35_PREDICTION_SELECTION.json`, 미래 검증 lock은 `NEXT_VALIDATION_PREREGISTRATION.json`에 있다. `execution_authorized=false`이고 이번 science node 수는 0이다.
