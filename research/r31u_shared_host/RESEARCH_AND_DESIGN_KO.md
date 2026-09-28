# R31U: 세 Codex 세션 자원 공유와 theory-first DAG 단축

이것은 연구 결과와 승인 대기 설계다. 실행 중 NCP job, 타 repo, scientific thresholds, production gate를 수정하지 않았다. Live host 접근은 없다.

## 확인한 repository 상태

- WU088_HH PR12: a49a704bf84fa86c34c16cd26a631dfabfbbc5ab. M3A 종료, M3B는 concurrent BASS F1 때문에 유효 측정 없음. M3B_INTERRUPTION은 같은 session-2.scope의 61 child processes를 기록한다. 이는 당시 관측이지 현재 PID inventory가 아니다.
- BASS_HE PR14: ff3035e0d240da53293cb2e15b97050cd5a25c47. 이전42-case 성능시험은16 workers 3.1997cases/s,24 workers 3.2429cases/s. 95% plateau 정책의 선택값16. 현재 live stage는 미확인.
- bass_cr PR4:25ba5e6eb71285d22d06bb884e77b806bb40735a. F1-R2는60worker/3600s/4000KRW/exactly-once/no automatic retry-resume. Frozen execution f1d69165c6d1e799d9474db23166cb665880576f. 이 run을 중도12worker로 줄이거나 다시 시작하면 안 된다.

## 즉시 권고

현재 protected F1-R2가 돌고 있으면 보존한다. 다른 세션은 새 대형 pool을 시작하지 않고, 각자의 정상 checkpoint 경계에서 다음 dispatch만 보류한다. Kill/SIGSTOP/강제taskset/deadline 연장/자동 재시작을 하지 않는다. 세 Codex UI를 닫을 필요는 없다.

F1-R2가 정산되면 HH M3B에 짧은 BENCHMARK_EXCLUSIVE 창을 둔다. 다른 세션은 heavy native/compile/압축을 겹치지 않는다. Shared-production epoch와 exclusive benchmark는 다른 실행 조건이다.

후속 shared 후보 HH32/HE16/CR12/control4는 아직 미승인이고 현재 CR60 계약에 적용하지 않는다. CPU 숫자는 guest logical CPUs다. 모든 job은 같은 host-level reservation을 읽고 actual allocation에 맞게 worker/thread를 제한해야 한다. Memory는1/3 균등분할 대신 measured peak+shared/spool+reserve 기준으로 계산한다.

    sum(P_i*T_peak_i)+control <= C_effective
    sum(M_peak_i)+shared/spool+reserve <= M_effective

새 job은 별도 leaf cgroup에서 시작하고 job-local cpu.stat/memory.events를 기록한다. 기존 parent만 이동해도 children이 따라온다고 가정하지 않는다. Broker/WAL/systemd deployment는 이 연구에서 구현하거나 설치하지 않았다. Lease expiry만 보고 live 작업의 자원을 다시 배정하면 안 된다.

## M3 coding audit와 최소 변경 제안

현재 m3_throughput.py는 measured_task_count(P)=max(24,2P),12-pair cyclic mix를 쓴다. 따라서128/64/32 tasks는 서로 다른 pair-frequency histogram이다. 기존 exactness/CPU engagement는 보존하지만 near-tie 순위를 동일-workload 순위로 과장하지 않는다.

새 co-finalist 비교에서는 같은12pair를11번 반복한132tasks를 모든 layout에 사용한다.132 distinct scientific pairs가 아니라 performance repetitions이다. 이미 완료된 전체M3A를 재실행하지 않고 필요한 finalist만 제한 재측정한다.

현재 runner는 saved host probe의64CPU를 요구하고 그 affinity/cgroup 경로를 재사용한다. 실제32CPU job allocation에서 그대로 실행할 수 없다. Host capability와 granted job budget을 분리하는 additive adapter/테스트가 필요하다. 실제 leaf effective cpuset/quota가 우선이다.

B192 reference12개는 parent에서 직렬 precompute하고 메모리에만 남는다. Source/model/grid/build/precision/rounding/pair identity에 묶인 cache로 저장하면 interruption 후 반복 계산을 줄일 수 있다. Correctness preparation의 cache와 measured native throughput을 혼동하지 않는다. 측정 구간에서 H0/native output memoization은 금지한다. Persistent spawn pool은 이미 있으므로 새로 구현한 성과로 세지 않는다.

HH32x1은 이전64x1 throughput의0.7204948243이었다. 절반CPU로 약72%라는 진단은 공유 후보의 근거이나 pair-histogram 차이와 concurrent memory/cache interference 때문에 실측공유속도 예측은 아니다.

## 이론: H-independent actual metric test

O=Phi†Phi>0,H=H†,D=Phi†dotPhi,physical time t:

    i*hbar*O*dotc=(H-i*hbar*D)c
    A=-i/hbar*O^-1 H-O^-1 D
    d(c†Oc)/dt=c†R c, R=actual(dotO)-D-D†.

O=C†C, y=Cc, G=dotC*C^-1+C*A*C^-1이면

    G+G†=C^-† R C^-1
    |d log N/dt| <= ||C^-† R C^-1||_2.

이 구조 검사에는 expensive H가 없다. 한 점의 defect를 실제 trajectory 누적오차라고 부르지는 않는다.

O,D,dotO를 독립 선형보간할 때 endpoint metric identity만으로 충분하지 않다. 전체 구간에서 actual derivative compatibility의 필요충분조건은

    dotO0=dotO1=(O1-O0)/dt.

## 기존 데이터에서 실제 계산한 결과

새 native calls=0,heavy nodes=0,trajectory=0. CP4 및 stored z2 full49/source seals의 SHA를 확인해 사용했다. [0,4] midpoint2에서 neutral은 기존 target 값을 유지하고 mixed/ionic provider만 보간:

- algebraic metric gap max:5.12384790334138e-15
- actual metric defect max:0.248069740331951
- reduced whitened residual spectral norm:0.6007169417167524 per atomic time
- overlap minimum eigenvalue:0.2258526095454687

대안도 실제 시험했다. Independent endpoint dotO를 이용한 cubic Hermite O와 interpolated skew K=(D-D†)/2에서 Dhat=(dOhat/dt)/2+Khat를 구성했다. 구조 residual은약5.12e-15로 줄었으나 direct midpoint mixed O error0.4938588926,D error0.5700657267,dotO error0.07350487984로 여전히 크다. 따라서 이 단순 Hermite 후보를 해결책으로 승인하지 않는다. 전체구간 SPD도 미증명이다.

## 추가 물리 후보와 gate

Known channel/ETF phase를 분리한 envelope 후보는 유망하지만 별도 연구분기다. 상수envelope pure phase에서 chord error는 |A|*|1-cos(kh/2)|이며 h^2 scaling은 |kh|<<1일 때만 유효하다.

Phi_tilde=Phi U(t)의 unitary gauge에는 D_tilde=U†DU+U†O dotU가 필요하다. H만 dephase하면 다른 dynamics다. 새 후보는 withheld direct data와 원frame 비교가 필요하다.

일정한 reference energy E에 대해 H=EO+r라 두고 |r_j|<=b_j를 독립 증명할 수 있다면

    |Delta H| >= |E| |Delta O|-b_mid-(1-s)b_left-s b_right.

이로 cheap O rejection certificate를 만들 수 있지만 현재 certified residual bound가 없어 H생략권한으로 쓰지 않는다.

유한 node 값/slope만으로 uniform error를 보장하지 않는다: q(s)=A*s^2*(s-1/2)^2*(s-1)^2는0,.5,1에서 값/미분0이나 q(.25)=9A/4096이다. 정확한 derivative 또는 analytic remainder bound가 추가로 필요하다.

## DAG amendment 제안

identity -> cheap O/JVP/actual metric -> cheap rejection/certified bound 또는 unresolved -> 필요한 H -> full49/accuracy -> transport.

일부 entry의 certified FAIL은 conjunction 전체를 기각할 수 있다. 일부 PASS는 전체PASS가 아니다. 같은 조건의 failure probability p와 cost c에 대해 p/c가 큰 검사를 먼저 두는 비용식이 성립하지만 현재 확률을 추정해 채우지 않았다.

M4 async executor는 범용 throughput 기능이지 첫 science discriminator의 수학적 필요조건이 아니다. 별도로 검증/승인된 synchronous checkpoint+dualACK NCP 경로가 있으면 M4를 병행연구로 옮길 수 있다. 그러나 현재 M5 lock은 그대로이며 이 제안이 z1 실행을 허용하지 않는다. Old12pair outstanding을 유지하면64worker활용이 제한될 수 있다.

기존 H<=2e-7Eh,G<=2e-12 및 minimum width1a0를 바꾸지 않았다. Z1,z0.5 미계산; minimum-width failure도 아직 미확정이다.

## 검증/산출물

새 pure research tests15 PASS(exit0),TDD missing-module RED(exit2),Python syntax PASS. Portable stored-array replay는 original probe JSON values와 일치했다. Wolfram에서 scalar conditions와 noncommuting2x2 norm/gauge example을 exact 검산했다. 첫 protected-symbol/conjugate-derivative 실수는 기록하고 최종 clean evaluation으로 교정했다. SciSpace 문헌탐색도 실제 수행했다.

Full code/tests/raw outputs/71KB input snapshot은 conversation artifact WU088_HH_R31U_SHARED_HOST_THEORY_20260928_v1.zip,93,270bytes,SHA25654b91ac6d111d6c3b2358cc143827b030a73d876ec1e3560c14b4e4284d5ebaa에 있다. 이 Git 문서는 그 전체binary package를 포함한다고 주장하지 않는다.

새 NCP benchmark/controller deployment,worker변경,production,trajectory,타repo mutation,새dual-provider backup은 수행하지 않았다. 이전6-10h final-audit ETA를 이 공유상태에서 유지하지 않는다.

## Primary references

https://docs.kernel.org/admin-guide/cgroup-v2.html
https://arxiv.org/abs/1608.05300 (Artacho/O'Regan, evolving Hilbert space)
https://arxiv.org/abs/2312.01115 (Ture/Jang, unitary Magnus propagators)
https://arxiv.org/abs/2503.22365 (Kulagina/Benoit/Meyerhenke, memory-aware workflows)

References motivate structure-aware transport/resource accounting, not a claimed numerical speedup on this VM.
