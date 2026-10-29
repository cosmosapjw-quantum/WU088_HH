# R19 R10 이론→코드 전달

R18 원본 105 K `k=23/200000000000000000 m³/s`를 R18의 검증된 `NativeGrid`에서만 취득한다.

정확 flow: `n=(a-xi,b-xi,c+xi,d+xi)/v`, `xi`는 `tau=int dt/v`에 대한 한 방향 반응해다. `theta=0`에서 `v=1,tau=t`. 양성성·H/D/charge 보존·rank-one Jacobian·rate 민감도를 구현하고 테스트한다.

외부 `Q_event`는 현재 미제공이므로 ledger는 형식적 조건부 식으로만 제공한다. `HH_R10=OFF`, production NOT_ISSUED, L4 false, WU DAG 34/49. R6 비저자 심사 미실행.