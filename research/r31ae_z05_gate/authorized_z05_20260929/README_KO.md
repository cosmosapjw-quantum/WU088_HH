# R31AE 승인된 z=0.5 단일 node

현재 사용자의 독립 affirmative structured envelope를 확인하고 canonical scope SHA와 여섯 parent hash를 출력 접근 전에 검증했다. 기존 mixed OD와 독립 JVP producer를 각각 한 번 사용하여 B192 z=0.5 a0, tau=1.1179386195169057 t_a를 계산했다. OD output identity 생성 시 승인권을 소비했으며 같은 envelope로 재실행하지 않는다.

원본 complex256 OD/JVP 배열과 pair checkpoint는 `OD_RAW/`, `JVP_RAW/`에 보존한다. 비교는 기존 R31AD/R31Z와 같은 complex128에서만 수행했다. Frozen 1e-10 Pareto 규칙의 한 점 판정은 `PARETO_SUPPORTED_AT_SELECTED_MIDPOINT`다. S는 지점 선택에만 사용했고 최종 판정에는 사용하지 않았다. 이 결과는 interval-wide/transition/trajectory/full-cell/H-skip/production admission이 아니다.

기존 OD 구현은 fused backend 내부에서 T 등 중간 moment를 평가하지만 `od_run.py`는 O/G1/G2만 선택하여 mixed O/D를 저장한다. Hamiltonian matrix block은 조립하거나 저장하지 않았다.

`RETURN.json`, `Z05_COMPARISON.json`, `ONE_SHOT_LEDGER.json`과 실행 로그를 참조한다.
