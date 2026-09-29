# R31AC 승인된 z=1 단일 노드

구조화된 사용자 승인 아래 B192, z=1.0 a0 (tau=2.2358772390338113 t_a)의 기존 mixed OD/JVP producer를 각각 한 번 실행했다. 승인권은 첫 과학 출력 생성 시 소비되었으며 재실행하지 않는다.

원본 복소 배열은 complex256 그대로 `OD_RAW/`, `JVP_RAW/`에 보존한다. OD의 O/D_col/D_row와 독립 JVP의 dotO를 사용했다. OD/JVP 내부의 부가 원시 진단 배열은 보존했고 H, neutral47, ionic2, full49, trajectory 출력은 생성하지 않았다. 모델 비교만 선행 R31Z/R31AA와 같은 complex128에서 수행했다.

고정 1e-10 Pareto 규칙의 결과는 `GLOBAL_SUPPORTED_AT_Z1`이다. 두 primary 지표에서 R31Z의 오차가 더 낮다. z=1 단일 지점의 독립 모델 비교 결과이며 구간 전체 정확도나 production을 승인하지 않는다. 수치와 원본/모델 해시, 실제 명령 및 출구 코드는 `RETURN.json`, `Z1_COMPARISON.json`, `ONE_SHOT_LEDGER.json`과 로그를 참조한다.

선언된 scope ID는 envelope 및 모든 개별 binding과 일치하지만 canonical scope JSON 직렬화 규칙이 명시되지 않아 scope digest 자체는 독립 재도출하지 못했다. 이 한계를 `RETURN.json`에 기록한다.
