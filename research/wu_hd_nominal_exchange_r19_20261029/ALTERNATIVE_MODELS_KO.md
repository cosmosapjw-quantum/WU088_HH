# R19 R4: 실제 방정식이 있는 세 후보

A. 고정 부피·고정 T=105K 한 방향 반응: `dn/dt=nu*k*n_H*n_HD`; 원본 source grid에서 직접 재현 가능한 최소 문제.

B. **채택**: 외부 지정 부피비 `v(t)>0`, `d(v n)/dt=nu*k*(v n_H)*(v n_HD)/v`; `tau=int dt/v`로 A의 정확 flow에 환원. Bianchi/FRW에서 계산된 팽창률을 **추후 입력**받을 수 있지만 실제 기하학 계산은 수행하지 않음.

C. 온도·역반응·전체 HD rotational ladder를 진화시키는 full physical network: 현재 실제 state-resolved reverse rates, thermal source, source uncertainty, external named owner가 없어 보류. A/B의 수치 성공을 C의 과학 승인으로 확대하지 않는다.

판별 기준: source state와 T 정확 일치, H/D/charge 보존, 비음수성, `theta→0` 극한, source-row 재가중치 금지, 원본 SHA 결속.