# R25 이론 P01 보강: 총 반응 진행량의 온도 순서 불변성과 상태별 생성량의 순서 기억

고정 부피, 외부가 고정한 두 source 온도 노드 `T_a`, `T_b`, 각 지속시간 `t_a,t_b>0`, 초기 두 반응물 밀도 `n0>0`, 10개 보고된 최종 H₂(v'=0,J') 이온 교환 채널만을 가정한다. 같은 소스의 상태별 rate를 `k_{a,j}`, `k_{b,j}`라고 정의하고, `K_a=sum_j k_{a,j}>0`, `K_b=sum_j k_{b,j}>0`, `b_{a,j}=k_{a,j}/K_a`, `b_{b,j}=k_{b,j}/K_b`, `a=n0 K_a t_a`, `b=n0 K_b t_b`라 한다. 표기 a,b는 속도·온도·불확실성이 아니라 양의 무차원 exposure다.

단일구간 반응 extent `X(z)=n0 z/(1+z)`이다. 총 반응물 감소는 두 exposure의 합만 보므로 두 온도 순서와 관계없이 `X_total=X(a+b)`이고, 최종 반응물은 `n0/(1+a+b)`다. 그러나 최종 상태별 H₂ 생성량은

`P_j^(ab)=b_{a,j} X(a) + b_{b,j} [X(a+b)-X(a)]`,
`P_j^(ba)=b_{b,j} X(b) + b_{a,j} [X(a+b)-X(b)]`.

따라서 **정확하게**

`P_j^(ab)-P_j^(ba)=(b_{a,j}-b_{b,j}) [X(a)+X(b)-X(a+b)]`
`=(b_{a,j}-b_{b,j}) n0*a*b*(2+a+b)/[(1+a)(1+b)(1+a+b)]`.

양의 a,b에서 괄호 계수는 양수다. 두 온도에서 특정 product branching 비율이 다르면 최종 상태별 양은 온도 이력 순서를 기억하지만, 총 진행량은 같다. `sum_j(b_aj-b_bj)=0`이므로 차이벡터는 전체 생성물 보존과 양립한다. 같은 `K_total`만 저장하는 scalar reactant integrator는 이 state-composition 정보를 버린다. **이 결론은 10개 reported channels의 restricted forward model에 대한 exact statement**이지 일반적인 HD,H₂ 내부 재분배, 실제 냉각 계측, full astrophysical chemical integration을 다룬 정리가 아니다.

GL2022 105 K/255 K, 각 5e9 s, 초기 n0=1e6 m^-3 (모두 외부 scenario)에서 source 그대로 계산한 `X_total=806695.105463136768... m^-3`. `P_1^(105->255)=341530.071535... m^-3` 대 `P_1^(255->105)=398784.805321... m^-3`, 차이는 `-57254.733786... m^-3`. 점별 source 데이터가 있는 다른 T 조합에서도 같은 식을 적용할 수 있지만 interpolation/역반응/열방출은 넣지 않는다.

**Scientific label:** 직접 유도 + source printed numeric check; 새 보편적 no-go/novelty 없음. `GL2022_PES_NATIVE_THRESHOLD=null`, `physical_Q=null`, `owner_ACK=null`, canonical `34/49` unchanged, R6/C9 `NOT_RUN`, production `NOT_ISSUED`.
