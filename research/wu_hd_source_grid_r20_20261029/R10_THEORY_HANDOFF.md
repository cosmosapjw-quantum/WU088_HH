# R20 이론→코딩 연결

정리 A: `N=v n`, `dN/dt=[k(T)/v] ν N_H N_HD`, `A=∫k/v dt`, `N=Φ_A(N0)`. 정리 B: source-grid segment i에서 `A_i=k(T_i) Δt_i/v_i * (1-e^{-θ_iΔt_i})/(θ_iΔt_i)`. 정리 C: `dξ/dk_i=I_i(a-ξ)(b-ξ)`.

코드는 원본 PDF SHA 확인 뒤 R18 NativeGrid lookup만 사용. R19의 수치안정 `expm1` 해를 exposure 입력으로 재사용한다. source-grid 밖의 T, 다른 상태, 외부 spin/thermal reweight, actual Q-event, 역반응, full-A는 금지. CR `proper_dt`는 소스-핀된 formula/signature 비교만 하며 실제 owner state binding은 하지 않는다.

Wolfram 9/9 True, R6 비저자 심사 NOT_RUN. WU DAG 34/49 유지.
