# PHYS80 reduced.py — bounded core-equation review

## 판정과 범위

**PASS_SCOPED — 검토한 core physics 식에 science launch를 막는 결함은 발견하지 않았다.** PHYS79의 선언된 neutral-CI/D-CX 부분망에 대한 4D/1D reduction의 식을 검토했다. full cosmological admission이나 아직 수행하지 않은 solver 실행의 성공을 승인한 판정이 아니다.

- 대상: `/tmp/hh_phys79_work/WU088_HH/research/hh_phys80_sandbox_reduction_20261022/source/reduced.py`.
- 검토 시 SHA256: `2029eac4b5e23e25158742ae79ba47bb9dcacaf95faba59237c7518195b201a9`.
- Model: `PHYS80_EXACT_CONSERVATIVE_REDUCTION_STRICT_V1`.
- 독립 기준: `EXACT_REDUCTION_AND_JACOBIAN_KO.md` 및 이미 완료된 Wolfram algebra receipt 두 개.
- 방법: 실제 source를 읽어 유도식과 비교했다. 이번 review에서 ODE, finite algebra run, numerical test, 과거 trajectory 재실행을 하지 않았다. SHA256 조회는 review identity 기록이다.
- 일반 API/입력 guard 검토는 별도 검토자 범위다. 이 검토는 core physics의 식과 적용 조건을 다룬다.

## Source–유도 대응

| 대상 | Source에서 확인한 내용 | 판정 |
|---|---|---|
| Physics admission | neutral CI rows `(0,1,3)` 또는 D-CX-only; constant proper density, expansion0, PI/RR0, bath0, D DB closure | 이론 전제와 일치 |
| Zero slots | charge>1, T/neutron의 비영 초기값을 거부; 복원 시 해당 슬롯0 | 원래 invariant subspace |
| H/D coordinates | H ion 변화 `(Q−Q0)−(v−v0)`, D ion 변화 `v−v0`; neutral/ion에 반대 부호 적용 | isotope 보존·원래 IC 보존 |
| He/Li lift | 초기 neutral inventory를 `1−h0`, `1−l0`로 나눈 lift를 고정 | 동일 rate의 invariant neutral ratio |
| Electron/particles | `xe=Q+B*h+L*l`, `N=nuclei+xe` | common/weighted fraction 모두와 일치 |
| Energy | actual parent potential 대조, `delta=eps[DII]−eps[HII]`, grouped `u0−fsum(bgrad·Δq)` | F2 상쇄를 재도입하지 않는 anchor |
| CI derivative | `k/T*(U−K+U/(X+U)−P*sqrt(U)/(2*(1+P*sqrt(U))))` | 유도식과 일치 |
| Reverse CX derivative | `r1*(0.396/T+33/T²)−0.332*r2/T` | 부호·지수 일치 |
| Forward CX derivative | `exp(−43/T)*(rprime+43*r/T²)` | 선택된 DB closure와 일치 |
| Q RHS | `nH*kH*xe*(H+D−Q)` | CX가 Q에서 상쇄됨 |
| v RHS | `nH*(kH*xe*(D−v)+kf*(D−v)*(Q−v)−kr*v*(H−Q+v))` | parent event 방향과 일치 |
| h/l RHS | `nH*k_element*xe*(1−fraction)` | 원소 rate 공유와 일치 |
| Temperature gradient | `−(bgrad+CV*T*xgrad)/(CV*N)` | particle-number·D thermal term 포함 |
| Full Jacobian | fixed-T M + `outer(w,gradT)`, 전체 nH factor | 독립 symbolic 유도와 일치 |
| Scaled Jacobian | `J_raw*S_j/S_i/clock` | diagonal·time chain rule과 일치 |
| CX-only | Q,h,l은 q0에 고정, v만 active; CI rates/derivatives0, J의 v-v 성분 사용 | exact scalar reduction |
| Source domains | derivative 값도 parent rate 호출에 연결; D-only에서 CI domain을 요구하지 않음 | C01/C02 조건과 일치 |
| Lifted RHS | scale·clock을 되곱해 proper-time full species/thermal tangent 복원 | 시간·에너지 단위 일치 |

## Jacobian의 CX 부호

`M[1,0] += kf*(D−v)+kr*v`는 Q 증가에 따른 forward reactant HII 증가와 reverse reactant HI 감소를 모두 반영한다.

`M[1,1] += kf*(2*v−D−Q)−kr*(H−Q+2*v)`는

\[
-f\{(D-v)+(Q-v)\}-r\{(H-Q+v)+v\}
\]

와 같다. 두 항의 부호와 v dependence가 정확하다. w의 CX 온도항도 `kfprime*(D−v)*(Q−v)−krprime*v*(H−Q+v)`로 일치한다. 온도 피드백을 뺀 fixed-T Jacobian만 구현한 것이 아니다.

## Anchored isotope lift

He의 `L_i=Y_iI(0)/(1−h0)`에 대해 구현은

\[
Y_{iI}=Y_{iI}(0)-L_i(h-h_0)=L_i(1-h)
\]

를 쓴다. 따라서

\[
\dot Y_{iII}=L_i\dot h=n_H k_{He}x_eL_i(1-h)=n_H k_{He}x_eY_{iI}
\]

이며 parent의 isotope별 CI equation과 같다. 저장된 초기 isotope fraction이 미세하게 달라도 동일 neutral-rate의 고정 ratio를 보존한다. Li도 같은 증명이다. 각 isotope의 합은 anchored neutral/ion 변화가 상쇄되어 일정하다.

이상적인 실수식에서 `sum(he_lift)=B`, `sum(li_lift)=L`이므로 aggregate electron/energy 계수도 같다. 실제 binary aggregate sum/division의 roundoff까지 bitwise identity라고 주장해서는 안 된다. constructor의 initial lift/temperature 대조와 별도 parent-operator/trajectory comparison은 이 수치 차이를 다루는 근거다. 이번 검토에서는 numerical comparison을 추가 실행하지 않았다.

## Energy와 D-only scalar

`bgrad=(IH,delta,IHe*B,ILi*L)`은 actual parent potential에 대응한다. D-only에서 q0를 고정하므로

\[
u=u_0-\delta(v-v_0),\qquad T_v=-\delta/(CV\,N)
\]

가 복원된다. 구현의 scalar Jacobian은

\[
n_H[-\gamma r'(T)G+r(T)G'],\qquad \gamma=\delta/(CV\,N)
\]

와 같고 v/D scaling은 diagonal Jacobian에서 상쇄된다. Q,h,l을 고정하는 구현이 초기 고정 온도를 쓰는 구현으로 바뀌지 않았다.

## 해석 한계와 다음 단계

1. **Real-equation equivalence와 bitwise trajectory equality는 다르다.** parent의 독립 u 적분을 conserved anchor로 대체하고 solver도 바꾸므로 동일 bit pattern은 요구하지 않는다. 기존 saved parent state에 대한 고정 정확도 gate와 별도 정련으로 비교한다.
2. **Reduced energy conservation은 construction의 성질이다.** 작은 `u+binding` 잔차만으로 독립 검증 완료를 주장하지 않는다. parent22-state 저장값, parent operator, D scalar thermal relation 등 독립 경로를 연결한다.
3. **Strict guard는 Radau trial positivity 보장이 아니다.** 실제 Newton trial 실패가 나면 attempt를 보존한다. trial extension은 별도 version·계약으로 다룬다. 현재 source는 extension·clipping·projection을 숨겨 넣지 않았다.
4. **Source domain의 전역 불변성은 별도다.** source는 평가 시 parent domain을 강제한다. 이로부터 domain 밖의 해가 정당화되지는 않는다.
5. **성능은 실제 실행에서 판단한다.** analytic Jacobian과 작은 상태 수는 설계이며 nfev/njev/nlu/wall-time 및 같은 정확도 조건이 기록되어야 speedup 주장을 할 수 있다.

이 review의 scientific code execution=0, ODE=0, completed-identity rerun=0이다. 별도 검토자의 numerical algebra/guard 검사를 중복 실행하지 않았다. source를 읽고 review 파일을 저장하는 orchestration에서 한 번 JS 구문 오류가 발생했으나 tool/물리 계산은 시작되지 않았고, 문서 저장 방식만 바꾸었다. 현재 발견된 concrete core-physics 잔여 결함은 없다. 새로운 식 변경 또는 실패가 있을 때 그 영향 부분만 다시 검토한다.

새 reduced solver의 science 실행·acceptance는 부모의 plan과 공유 lease 아래에서 별도 판정한다. 유도/구현 검토, 실제 science 실행, 게시·backup·DAG 상태를 분리한다. **HH_R10=OFF. Production admission NOT_ISSUED. Full collisional cosmological closure OPEN.**
