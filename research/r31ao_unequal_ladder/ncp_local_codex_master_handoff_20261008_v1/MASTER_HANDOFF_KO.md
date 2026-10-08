# NCP local Codex 종합 실행 handoff (2026-10-08 KST)

## 역할과 최종 목표

너는 사용자의 **NCP(NAVER Cloud) Ubuntu 계산 노드에 Remote-SSH로 접속된 local Codex**다. 실제 소스 읽기, 빌드, 대형 native 수치 작업, 재시작, 자원 관측, 병렬 최적화, 원본 증거 보존, 제한된 원격 연구 게시·이중 백업을 수행한다. ChatGPT 별도 cloud runtime에서 계산하거나 NCP 경로를 추정하지 마라.

목표는 WU088_HH의 미완료 고정밀 H–H 인증과 선택적 HH의 fastest-track 계산을, `rei_bianchi`·`BASS_HE`·`bass_cr`의 실제 최신 결과에 맞춰 **의존성과 승인 범위 안에서 가능한 데까지 실행**하는 것이다. 중복된 합성 검산 또는 역사적 성공 재실행이 목표가 아니다. 단계별 결과를 완결된 durable artifact로 남기고, 승인·과학적 증명·구현 검증·환경 검증을 반드시 분리하라.

이 요청은 기존에 승인된 비파괴적 개발·검증·백업의 실행 지시다. 과거의 **exact authorization이 필요한 NCP scientific dispatch/consumed registry, 관리자 권한, 과금 증설, 전체 생산 모드, PR merge**의 새로운 포괄 승인은 아니다. 요구되는 exact scope authorization이 없다면 그 과학 배치를 실행하지 말고 proposal과 정확한 blocker를 기록한 다음 다른 독립 허용 작업을 계속하라. 사용자가 이미 승인한 scope를 다시 묻지 마라.

## A. 첫 실행 전에 고정할 출처와 당시의 알려진 상태

소스의 기준은 최신 실제 원격 Git HEAD, 로컬 상태, 해시 검증된 sealed archive와 해당 논문의 원전이다. 아래 commit은 **2026-10-08 기준 수신 스냅샷**이며 절대 reset 대상이 아니다. 시작 시 HEAD/tree, diff, working tree, PR/branch, 원 source blob 및 이전 상태를 다시 읽어 `SOURCE_SNAPSHOT.json`에 고정하라.

- `cosmosapjw-quantum/WU088_HH`, `research/r31ao-unequal-order-ladder-20260930`: 관측 HEAD `649ecb06321d3f7956fc13902666f062dfcde50c`, Draft PR #33. 연구용 Kummer/NCP 원본, R31AO primitive certificate, HH-ON06 및 ENERGY 계보는 각각 별도 authority다.
- `cosmosapjw-quantum/rei_bianchi`, `forward/rust-reion-kernels-20260922`: 마지막 확인된 BRIDGE12 HEAD `9e1bad4daacbe9e313d34b1b645391b90b32b606`; 다음 REI 소유 과제는 BRIDGE13의 piecewise continuous defect chain이다.
- `cosmosapjw-quantum/BASS_HE`, `research/shared-c64-crossrepo-20260928`: RCT03E7 HEAD `6c398585257d23541bbbed125acb81630b97abd4`; E6 finite 9/9은 **절대허용 `1e-22 s^-1`** 계약이며 옛 E3의 더 엄격한 `2.5e-23 s^-1` 실패를 동일 기준 PASS로 고쳐 쓰지 마라.
- `cosmosapjw-quantum/bass_cr`, `research/r4q-gap-closure-20261001`: R12 HEAD `890916f8c9e75d82eb0f9523608cb2bf4500feb3`; two-state photo source decomposition은 증명된 산술 귀속이며 전체 nonphoto RHS, true source error, continuous tau는 열려 있다.

NCP 역사:
- Readiness v2의 `20/289, missing269`는 pilot **이전**의 상태다. 2026-10-03 여섯 셀 `[275,67,288,272,16,0]`을 실행했고 275,67,288,16만 `RADIUS_MET`, 272와0은 `INTEGRATOR_NO_CONVERGENCE`였다. 소비 scope를 유지한다. 이후 유효한 coverage는 **`24/289`, missing265 unbounded**로 기록됐다. 어느 항목도 전체289 완료를 뜻하지 않는다.
- 두 실패는 FLINT 외부 대기열 `depth_limit=64` 종료라는 **종료 경로**가 확인됐으며, 처음 HH callback의 nonfinite 원인은 Kummer `M(a,b,z)` 자동 점근 route가 0을 포함한 복소 상자에서 부적합하다는 것으로 FD2에서 진단했다. `src/finite_m.hpp`의 제한된 직접 `1F1` 급수 후보, 256항 꼬리 경계, 33개 scalar 검사는 검증됐다. 뒤따른 별도 FD2 field 4회에 대해 finite/107 complete/overlap 반환이 수신됐다는 보고가 있으나, 실제 최신 `RETURN`, 승인기록, raw/registry와 일치하는지는 NCP 현장에서 먼저 확인해야 한다. **이미 소비된 FD1/FD2/6-cell scope는 절대로 재실행하지 마라.** 후보가 원본과 source identity가 다름을 유지한다.
- `epsilon_C=null`, `epsilon_R=null`, `B22=OPEN_UNDETERMINED`, scientific/physical/production admission=false. 부분 셀·합성 시험과 LCS/KS fit 차이를 ab-initio 전체 H–H 인증으로 승격하지 마라.
- 최신 HH fastest-track 저장 checkpoint는 `ON06G`의 **총 256 macro-step, `t=3.2e11 s`**, OFF/LCS × FLRW/Bianchi-I, T0 grid(에너지33·방향128)이다. Canonical S0의 HH 선택은 **OFF 대조군**으로 보존한다. 위 G history는 ENERGY01~05의 단일 선택 source 실험과 다른 scope다.
- 가장 최근 sealed HH 연구자료: `WU088_HH_ENERGY05_CORRELATED_TWO_SOURCE_TANGENT_20261008_v1.zip`, 1,334,251 bytes, SHA-256 `45710e72221ab8c4711e6ff5f9eb688fad32e7ac9944eda09edc924c7224c717`, 136 entries/134 payloads. 해당 ZIP은 마지막 보고 시 Drive/Dropbox **미업로드**였으므로 NCP에 자동 존재한다고 가정하지 마라. 이 handoff에 동봉됐으면 hash를 확인해 사용하라. ENERGY04 및 그 이전 archive는 별도 sealed inputs이며 이전 receipt/원시 실패기록을 바꾸지 않는다.
- ENERGY05의 두-stage **같은 θ의 실수 이산근** 응답 `Delta h in [1.9916504780243373e-10,1.9916506272398572e-10]`; 원 저장된 두 binary64 점의 뺄셈은 `1.9916479576664869e-10`으로 매우 좁은 위 구간 밖이었다. 별도 80자리 근 차이 `1.9916505570231716e-10`은 안에 있었다. 이를 실패 은폐, tolerance 완화, 기존 interval proof의 실패 또는 물리적 부호 반전으로 재분류하지 말고 근 오차·상관 차이·점 산술을 분리하라.

우선 확인할 기존 파일/위치:
- 현지 기록이 남았다면 `/root/WU088_NCP_EXEC_20261003_v2`를 읽기 전용 inventory하라. 누락되면 verified cache → 기존 Drive/Dropbox 하나에서 hash 기준 복구 → 공식 Git 원본 순서다. 사용자의 재업로드를 우선 요구하지 마라.
- NCP readiness `WU088_HH_NCP_READINESS_20261003T063359Z_v2.zip` SHA-256 `0d19eee26eb71dbdce5d95b2d62fddcc32913516f24087d15df03b0b8715b2d3`, Drive ID `1fCQH6bcJVR1iJAe8-8YPvkbHfPDDcQfM`.
- 6셀 pilot `WU088_HH_NCP_SIX_CELL_PILOT_20261003T133901Z.zip` SHA-256 `ca151554eeda797359c91af1f613f5ab938b789c560df376e881a61d72982c3f`, Drive ID `14ie4f_ZdR6Q-V137jL4NE6G7Ks9tmfkf`.
- FD2 candidate root cause `WU088_HH_FD2_ROOT_CAUSE_DELIVERY_20261004_v1.zip` SHA-256 `21289a6cc78b1c172815c97b4053eb9990a26d048b0410ac1dee6b22bbcb66a1`, Drive ID `1OiAs1b0G-ot7PJ-bdCwYmevN5xZGTmx2`.
- FD2 candidate preparation `WU088_HH_FD2_NCP_CANDIDATE_PREPARATION_20261004T074747Z.zip` SHA-256 `cdde98085605babf968348e611b6a62e0cf49fe437d32b739c3d0be31a4b55be`, Drive ID `12aEsnLRCQ9VJDo8jkzR_auJ5lUrlUU4s`.
- 기존 NCP 출처에는 `WU088_HH_FD2_CANDIDATE_AUTHORIZATION_DRAFT_KO.md`도 있다. **초안은 승인 원문이 아니다.** 최신 NCP registry/authorization record를 회수해 실제 수행 여부부터 결론내라.
- 주요 handoff 원문: `WU088_HH_FD1_DIAGNOSTIC_PREPARATION_PROMPT_KO_20261003.md`, `WU088_HH_NCP_PREP_REMEDIATION_PROMPT_KO_20261003.md`, `CONVERGENCE_PLAN_KO.md`, 저장소 AGENTS/SSOT.

## B. 작업방식 및 강제 안전 조건

1. 실제 NCP 터미널에서 실행하라. `hostname`, `pwd`, `git status --porcelain`, `git rev-parse HEAD^{tree}`, `nproc`, `lscpu`, `taskset -pc $$`, `cat /proc/self/cgroup`, `/proc/self/mountinfo`, cgroup leaf/ancestor의 `cpu.max`, `memory.max`, `memory.current`, `free -b`, `df -h`, `ulimit -a`, compiler/MPI/library version, PID/PGID/capabilities/NoNewPrivs, 실제 프로세스/worker를 관측해 `RECOVERY_INVENTORY`에 남겨라. NCP 64코어/128GB는 목표 구성이지 실측 quota/여유 메모리 증거가 아니다.
2. 기존 실패 tree, ORIGINAL SOURCE_LOCK, consumed registry, PREPARED, database, raw/return, checkpoint, 이전 공개 artifact는 **불변**이다. 새 실행은 고유한 worktree/branch와 `runs/<UTC_ISO8601>_<taskid>/` 같은 새 작업공간에서 시작하라. source+input+compiler+library+plan+scope의 byte SHA와 semantic identity를 각각 기록한다. symlink tar/ZIP 복구는 링크 대상·경로 탈출을 검사하고 무조건 추출하지 마라.
3. 현지 설치/비특권 작업으로 충분한 경우에만 실행한다. sudo 시스템 전역 apt 설치, mount/cgroup 전역 변경, 새 사용자·VM·과금 증설, 비인가 관리자 권한/credential 변경, 저장소 force-push·merge·원본 삭제는 금지한다. 이미 위임된 cgroup과 로컬 prefix는 사용할 수 있다. 신뢰되지 않는 output proof를 인증된 입력인 양 역수입하지 않는다.
4. 한 논리적 batch는 **exact source/input/parameter/scope/budget/authorization**을 seal한 후 단일 coordinator에서 one-shot으로 실행한다. science dispatch 전에는 `BINDING_PROPOSAL`과 실제 `AUTHORIZATION_RECORD`를 별도로 비교한다. `run()`이 scope registry를 consume하는 경우 승인 hash 추출용으로 절대 호출하지 않는다. 없는 승인/오래된 승인/이미 소비된 scope에서는 dispatch=0, 대신 다음 준비/다른 독립 작업을 계속한다.
5. failure를 THEORY, DOMAIN, NUMERICAL_CONVERGENCE, IMPLEMENTATION, ABI, RUNTIME_ENVIRONMENT, WALLTIME, PROVENANCE, AUTHORIZATION, POLICY로 분리한다. 무한 재시도·새 이름으로 동일 scope 재실행·허용오차 완화·clipping/projection·fast-math 도입·실패 증거 삭제를 금지한다. 첫 실패 시 신규 science dispatch 정지, 이미 실행 중인 worker는 원 계약대로 drain/회수한다.
6. 허용된 단계는 질문하지 말고 완료하라. 막힌 단계에서는 원인·선행 전제·최소 재개행동·필요하면 정확한 승인/관리자 명령 한 건을 `BLOCKERS.json`에 명시하고, 독립적으로 실행 가능한 단계는 계속 진행하라. 옛 인증/테스트를 새로운 과학 성과로 중복 합산하지 마라.

## C. 의존 DAG와 실제 수행할 무거운 작업

### C0. NCP native host/ABI 상태 복구 (먼저 실행, 비과학)

기존 준비 R1의 `makeinfo`/cgroup 문제는 과거 기록이다. 후속 R2에서 backend build, worker link/ABI, binding proposal을 성공했다는 반환도 있으므로 **성공 기록을 먼저 찾아 현재 동일 host/build/view인지 검증**하라. 실제로 달라졌을 때만 필요한 재확인을 수행하라. GMP 6.3.0, MPFR 4.2.2, FLINT 3.4.0 및 원 Arb/FLINT ABI, `-O2 -fno-fast-math -ffp-contract=off`, 원 소스와 makeinfo clean-PATH smoke를 보존한다. 가짜 makeinfo, `MAKEINFO=true`, `touch gmp.info`, 유한 cgroup limit을 가짜 파일로 주입하는 조치를 금지한다. 실측 affinity/quota·finite effective memory·cgroup namespace·UID/capabilities·NoNewPrivs, pinned loader와 worker binary가 실제 동일한지 확인하라.

산출: `HOST_READY.json`, `BACKEND_ABI.json`, `SOURCE_AND_BUILD_LOCK.json`, 빌드/링크/필요한 focused-test 원 로그. Host/ABI가 동일하고 유효하면 과거 full build를 반복하지 말고 `INHERITED_VERIFIED`로 연결한다.

### C1. 소비된 NCP pilot/FD2 최종 상태 확인 및 실패 2셀의 새 후보 (선행)

원 6셀에서 성공한 4셀과 기존 20셀을 다시 적분하지 마라. `272`, `0`의 원 raw·부호·log-domain·첫 failed callback·FD1 diagnostic·FD2 finite-1F1 후보 출처를 비교하라. FD2 4개 callback의 finite, 107-term 완료, cached/reference physical/mapped interval overlap이 **원 반환과 현재 authority에 실제 닫혀 있는지** 확인한다. 이미 닫혔으면 다시 호출하지 않는다. FD2는 field-level 성공이지 새로운 셀 enclosure가 아니다.

필요한 새 scientific scope는 **원문을 복사한 pilot 재실행이 아닌**, source-bound 새 후보를 이용한 실패 셀 `272,0`의 별도 integration plan이다. 먼저 진단에서 유효한 전체 box margin과 rank/order/signs를 결속하고 필요한 신규 승인기록을 생성·검증하라. 정확 승인 없이는 계획·비과학 시험까지만 진행한다. 최초 새 유한 배치는 저렴하고 엄격하게 제한하며 실패 시 폭/last_error/quadrature reason을 보존한다. FLINT queue limit을 무작정 늘리거나 128bit/radius `2^-57` 및 source coefficient를 바꾸지 않는다.

산출: `FD2_STATUS.json`, `TWO_CELL_NEW_SCOPE_PROPOSAL.json`, 새로 **실행된 경우에만** `RETURN_272_000.json`, raw balls/workerlogs/coverage delta. 성공해도 총 coverage의 정확한 원천별 변화만 기록한다.

### C2. R31AO full certification 고정밀 대형 계산 (엄격한 전단계 gate 이후)

성공한 source+backend+scope와 C1의 수치 feasibility를 만족한 경우에만 단계적으로 수행한다. 기존 성공 셀은 재사용하고 새 289-window interior의 미계산 셀을 **충분히 작은 유한 shard**로 실행하되 각 shard마다 원본 cell ID, 정확한 로그/물리 영역, primitive ID, source order, radius/width/CPU·memory·timeout·raw SHA를 남겨라. 계수는 signed ordered 107-term, 정확한 outward Arb/FLINT enclosure다. Radius `2^-57`, precision128 및 원 289 partition/tolerance를 바꾸지 않는다. `289*2^-57 < 2^-48`은 **모든 셀이 실제 포함될 때만** 유효하다는 점을 지켜라.

289개가 완료되기 전에는 부분 합을 whole-domain 인증으로 부르지 않는다. 성공 시에만 primitive0 endpoint 및 normalization을 **한 번** 결합한 뒤 2,592 primitive의 ordered streaming contraction을 수행하고, 정확한 `D_col(47x2)`, `D_row(2x47)`, 독립 K, model gap의 interval과 `epsilon_C/R`을 실제 계산하라. 정확한 dyadic/radical/machine predicate bridge, frozen tolerance token 및 strict inequality gate를 실행한다. `epsilon=null`, `B22 OPEN`, missing cells가 있으면 자동 FAIL/PASS가 아니라 각 의미의 `UNRESOLVED`로 남겨라.

비공개 대량 계산을 한 번에 `289×2592`로 발사하지 말라. resource caps와 원 계약에 따라 고정된 finite batches → exact reducer 순서로 실행하고, 실패 뒤 retry 없이 원인분류를 끝낸 다음 별도 successor로 넘어간다. 분산 MPI/Fortran 최적화는 아래 C5의 검증 전에는 이 결과를 대체하지 않는다.

산출: `COVERAGE_289.json`, `PRIMITIVES_2592.jsonl`, `D_EPSILON_RESULT.json`, `EXACT_GAP_AND_MACHINE_GATE.json`, `CONTRACTION_RECEIPT.json`, 실패별 원 raw, source-bound width/ratio, actual task count와 claim status.

### C3. 충돌 물리·관측량에 필요한 무거운 후속 계산 (conditional)

C0/C2의 source-channel crosswalk를 읽어 HI+HI→HI+HII+e, HI+HI→HII+Hminus (ionic pair), elastic/exchange, H+ + HI의 resonant CX가 **서로 다른 channel authority**인지 확인하라. 47+2 finite basis의 ionic Hminus를 free-electron ionization과 혼합하거나, 행렬 D/epsilon을 단면적·rate로 직접 치환하지 마라.

선택된 채널의 channel projector 및 asymptotic normalization/flux가 인정되고 full49·BR gate가 통과했을 때만 actual O/H/D propagation, 필요한 angular `l>0`/rearrangement 개선, 충돌 에너지·impact parameter·trajectory·b-grid·부분파 수렴, 확률·flux·unitarity/positivity/상세균형의 유효 조건, `sigma(E)`와 분포평균 `k(T,distribution)`의 수치/오차를 실행하라. 기존 W1 5-keV two-centre lane에서 A3 basis N10→N12 약22% 변화가 2% gate를 넘은 문제는 별도 연구 lane이다. 이 결과를 고정된 HH 289 셀 수렴과 섞거나, W1의 N16 runtime walltime을 수학 실패로 처리하지 마라. 현재 authority가 불충분하면 구현 fixture와 정확한 missing-premise만 제출하라. Born/isotropic/Maxwell/straight-line을 무언의 fallback으로 삼지 않는다.

Bianchi 재이온화 수신기에는 local proper-frame source·charge/nuclei/electron/thermal/radiative-ledger와 가정/단위/오차를 제공한다. Hminus pair와 직접 HH ionization이 다르면 서로 다른 stoichiometric ledger를 유지한다. `HH-LCS`·`corrected-KS` fit은 독립된 경험적 **연구 시나리오**이지 위 ab-initio 계산의 rigorous error band가 아니다.

### C4. HH fastest-track 대형 crate/수치 실행 (C1과 독립적으로 가능한 경로)

우선 sealed `ON06G` 완료 checkpoint와 `ENERGY01...05` 계보의 SOURCE_BINDING/MANIFEST/RETURN을 해시로 복구한다. ON06G archive는 Drive ID `15oFfNmXs6hMv5N71rMQDQFz1rc_wTd8Q`, SHA-256 `35e38e66181fe56d75fa8ac24881b6e2496dd77a0bc596fc529a4e3d2ee80b1a`다. ENERGY04의 Drive ID는 `18Z1dyYbUzNpfJ2hT8zj6TiK_Pi63z77p`다. Git 최신과 충돌하는 작업 파일은 별도 worktree에서 3-way 비교하고, **combined patch를 이미 일부 적용한 checkout에 중복 적용하지 마라**. Rust 1.94.1과 실제 dependency pins를 확인한다. 전 과학 suite를 습관적으로 반복하지 말고 실제 crate에 반영하는 변경의 영향범위에서 `cargo test --locked --offline --all-targets`와 focused integration/CLI 검증을 수행하라. dependency 준비가 안 되었으면 정확한 toolchain blocker로 기록한다.

핵심 다음 노드 `HH-ENERGY06_LINKED_CHAIN_ACCEPTANCE_AND_PAIRED_DEFECT`:
- ENERGY05의 같은 `theta`·`lambda` 반환(`v1`, photon `P'`, remap 후 `N'`, `v2`)과 root/point/carry 구간을 actual owner `paired_trial`의 **한** source/transport/birth/ledger 호출 경계에 연결한다. 원 G의 방향 자료가 필요한 Bianchi에는 실제 방향별 stored state를 가져오고, 25 aggregate packet으로 가상 등방 방향을 만들지 않는다.
- 원 `t0=1.6e11`, `t1=1.60625e11`, `t2=1.6125e11 s`의 no-birth split과 원 proper density/energy/source identity를 유지한다. **다음 원본 history에 실제 birth가 있다면**, 동일한 birth times/weights/geometry를 따르는 새 명시적 run contract 없이는 한 매크로의 물리실행이라고 주장하지 마라. source마다 photon redshift/remap/gas thermal work/HH chemical source를 한 번만 계수한다.
- full vs two-half, 가능한 event-aligned 비교를 **동일한 birth measure** 위에서 구성해 예전 local `<2e-4`, public width `<2e-3`, ledger `<=1e-12`를 유지한다. `(accepted half1+half2)`의 HH 사건수/열만 누적하고 full은 진단으로 분리한다. 전 단계의 모든 interval·compensation·identity·checkpoint와 old source uncertainty를 운반한다.
- Krawczyk `K(Y,P) subset interior(Y)`와 scaled contraction `<1`이 새 에너지 및 source parameter family 전체를 포함해야 한다. Point와 전 구간 proof를 구분한다. 시각·mode·energy radius·packet labels·old gas 1-ULP 차이·ABI·source identity가 바뀐 반환은 fail-closed. cutoff `13.6 eV`와 binding `13.598434599702 eV`는 구분하고 crossing family는 branch partition 또는 거절한다. 같은 광자군의 alternatives를 새 광자 두 개로 세지 않는다.
- `Delta h`, `Delta T`, `Delta ne`, `Gamma_HI`(per absorber), `R_HI=(1-h)Gamma_HI`(per H), photoheat, `N,U`, escape/work, HH counters를 같은 시각·model·parameter로 반환한다. HE/CR의 저장 output/error 기준을 HH에 무단 전용하지 않는다. HII 양수 점 비교만으로 비등방 이중차이의 부호를 승인하지 않는다.
- 별도 고정밀 scalar/root와 interval/sensitivity 검사, 시간·spectral·angular refinement, 실제 중단·rollback·restart·byte identity 검사. 연속시간 오차는 REI BRIDGE12에서 **한 실제 셀만 조건부로 닫혔고 31셀은 미완료**였으므로 새 continuous defect/regularity 검증 없이 `continuous_error=null`로 둔다.

그다음 단계 `HH-ON_FULL_HORIZON`은 온도 `35000..60000 K`, cutoff/domain, step/time/event/angle/energy 수렴과 original canonical full-S0 plan이 실제 전 시간동안 유효하다는 증거를 얻은 경우에만 3.2e11 s checkpoint에서 이어나간다. 앞 256 macro를 반복하지 않는다. canonical OFF를 유지하고 LCS/KS와 각각 분리된 opt-in 이력을 실행한다. 원 F09 전체 campaign과 owner DAG는 허가 없이 대리 변경하지 않는다. 단계별 중간 checkpoint만으로 full `1e13 s`나 물리적 rate 정확도를 승인하지 않는다.

### C5. NCP 64-core/128-GB native 최적화 (정확성 gate 후)

정확히 같은 pinned problem/inputs/result width와 scalar reference가 가능한 경우에만 후보별 OpenMPI·Fortran/OpenMP·SIMD·벡터화·캐시·스레드 affinity·NUMA·chunk 크기를 조절하라. 기존 deterministic source order, outward rounding, radius, ABI/flags, atomic/event/ledger semantics를 보존하고 `-ffast-math` 같은 의미 변경 금지. 단일-worker/2-worker/실측 NCP quota 내 병렬 후보를 비교한다. 원 20/24 셀 및 기존 source 결과를 무효화하지 않으며 speedup만으로 과학 PASS를 올리지 않는다.

각 후보의 동일 task parity, enclosure 포함, runtime, RSS, CPU, MPI ranks/threads, topology, worker leak/zombie, disk IO, resource cap, crash/restart resume을 계측하고 최선 구성이 없으면 `selected_configuration=null`로 남겨라. 별도 host에 기록한 시간을 같은-host speedup이라고 부르지 않는다.

### C6. 다른 세 연구 스레드와의 결합, 단일 owner 원칙

`rei_bianchi`: BRIDGE12는 실제 첫 continuous cell만 완료, 이후 BRIDGE13 piecewise 31-cell chain과 source quadrature/escape ledger/open criteria는 REI 담당이다. 수신된 최신 artifact를 import하되 기존 실험을 반복하지 마라. NCP가 위임받은 범위에서만 BRIDGE13의 실제 cell/root/continuum 계산을 실행하고 source/clock/FFT/geometry를 고정해 결과를 REI에 반환하라.

`BASS_HE`: RCT03E6의 9/9 finite target과 RCT03E7의 read-only opt-in receiver 결과를 소비하되 `1e-22 s^-1`가 참오차 인증/옛 strict target과 동등하다고 선언하지 마라. 대형 30M+ characteristic/node 계산 또는 더 엄격한 spectroscopy는 **새 실제 target·owner 승인**이 있을 때만 별도 NCP job으로 실행한다.

`bass_cr`: R12의 stored 96 snapshots/two-state photo-source decomposition은 소비하되 history 96개를 또 계산하지 마라. 진짜 total source error/continuum optical depth/observer tail의 실측 입력과 구간 정칙성이 들어오면 정밀 계산을 수행한다. CR 기본 `OFF_FASTEST`와 b-grid `NO_GO`를 임의 변경하지 마라.

각 repo는 버전·계산 소유자·소스·기준을 별도 원장에 둔다. HH의 sigma/ε 결과가 없어도 기존 공통 H/He baseline이 독립 진행 가능한 것은 유지한다. 서로 다른 epoch·temperature·photon grid·energy family의 검증 결과를 산술적으로 합쳐 단일 joint physics 인증으로 선언하지 않는다.

## D. 완료 조건, 증거 패키지, 반환 방법

각 task에 `TASK_ID`, `AUTHORITY`, `PARENT_HASH`, `INPUT_SHA256`, `SOURCE_SHA`, `TREE_SHA`, `BINARY_SHA`, `TOOLCHAIN_ABI`, `HOST/CGROUP/UID`, `PARAMETER_SCOPE`, `RESOURCE_BUDGET`, `APPROVAL_SCOPE`, `DISPATCH_COUNT`, `EXIT_CODE`, `ELAPSED/RSS`, `RAW_IDS`, `COVERAGE`, `ERROR_DECOMPOSITION`, `BACKUP_RECEIPTS`, `CLAIM_GATE`, `STOP_REASON`을 기록한다.

최소 파일:
- `RECOVERY_INVENTORY.json`, `SOURCE_SNAPSHOT.json`, `RUN_DAG.json`, `RUN_LEDGER.jsonl`, `COMMANDS.jsonl`, `ENVIRONMENT_AND_ABI.json`, `FILE_MANIFEST.json`, `SHA256SUMS`.
- task별 원 raw/stdout/stderr/registry·PID·partial/error·normalized 결과, `TEST_RESULTS.json`, `INDEPENDENT_CHECKS.json`, `INTERVAL_ROOTS.json`, `LEDGER.json`.
- `NCP_MASTER_RETURN.json`, `CLAIM_LEDGER.json`, `BLOCKERS.json`, `REPORT_KO.md`, `NEXT_HANDOFF_KO.md`, 소스 diff/patch와 **원본을 바꾸지 않는** sealed ZIP 및 detached delivery receipt.

각 노드를 `VERIFIED_EXISTING`, `NEW_IMPLEMENTATION_VERIFIED`, `NEW_NATIVE_EXECUTION_VERIFIED`, `DERIVED`, `PARTIAL`, `FAIL_PHYSICS`, `FAIL_NUMERICAL`, `BLOCKED_ENVIRONMENT`, `BLOCKED_PROVENANCE`, `BLOCKED_AUTHORIZATION`, `NOT_RUN`으로 분류하라. 실측 출력 없이 PASS라고 하지 마라. 원본 범위와 다음 최소 구현 및 그에 필요한 정확한 입력·권한·실험을 매 단계 적는다.

허용된 기존 연구 브랜치 또는 별도 연구 브랜치에 **non-force, additive** 게시하며 merge는 금지다. 이전에 특정 Git 게시가 안전성 판정으로 차단됐다면 그것을 우회하려고 다른 경로/변형 payload를 쓰지 말고 독립 파일·실제 차단 기록을 남겨라. 기존 백업 폴더는 Google Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`와 Dropbox `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/`이다. 쓰기가 허용되면 새 이름 create-only로 양쪽에 저장하고 실제 성공 응답·remote ID·name·size를 대조하라. `R1 UPLOAD_VERIFIED`와 remote byte restore 검증, science validation, owner adoption을 결코 혼동하지 마라. Upload action이 없다면 결과 파일만 제공하고 성공 영수증을 만들지 마라.

**실행 시작:** source/runtime/이미 소비된 scope/현재 실행 중인 프로세스부터 실제 NCP에서 inventory하고 `RUN_DAG`와 모든 ready 작업을 수행하라. 권한 없는 science scope만 별도 blocked로 두고, 가능한 고정밀 reference·구현·host readiness·focused regression·독립 입력 검증·패키징을 순서대로 처리하라. 작업 종료 때 사용자에게 완료된 실험/컴파일/검증의 실제 수치, 아직 미완료인 각 의무, repo/commit와 remote 백업 receipt, 새 재개 지점을 **한국어**로 반환하라. 전 단계 반복 감사로 작업을 무한히 지연시키지 마라.