# R31AE z=0.5 authorization gate 후속

현재 사용자 지시는 structured envelope를 실행 조건의 예시로 제시했으며 affirmative authorization을 제공하지 않았다. 따라서 `Z05_EXECUTION_STATUS=AWAITING_STRUCTURED_AUTHORIZATION`, science producer command 0, science node 0으로 종료한다.

명시된 JSON canonicalization으로 scope digest를 재계산했고 모델·manifest·selection·rule·prereg 개별 해시와 z/time/order/tolerance가 모두 일치했다. 검증 결과와 실제 argv/stdout/stderr/exit는 `GATE_PREFLIGHT.*`에 있다. z=0.5 직접 출력을 읽거나 생성하지 않았다.
