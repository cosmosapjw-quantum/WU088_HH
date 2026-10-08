# NCP local Codex handoff: HH-ENERGY06B → ENERGY06C

**역할:** `WU088_HH_NCP_ENERGY06_COMMON_SOURCE_LAW_AND_PAIRED_CANDIDATE_IMPLEMENTER`.

**목표:** 이번에 검증한 full/two-half **공통 source-law, 상이한 이산 birth 시각, 정확한 scalar BE paired-defect 항등식**을 현재 owner의 실제 128방향×33노드 H/He+HH source 진입점에 결속한다. 필요 시 `C1 272/0` 후속 프로포절은 **독립 분기**에서 정교화한다. 이미 완료된 NCP 산출물과 과거 scope를 다시 실행하지 않는다.

## 0. 맨 먼저 읽어야 할 authority와 변경금지 경계

1. GitHub `cosmosapjw-quantum/WU088_HH`의 branch `research/ncp-master-execution-20261008`, 정확한 반환 HEAD `d8aeaec783c143600e38cbb1b48d1fa5cdb3799e`, 다음 본 연구의 Git 새 경로, `research/r31ao_unequal_ladder/ncp_master_execution_20261008_v1/DELIVERY_RECEIPT.json`을 read-only로 읽는다. 브랜치가 전진했으면 델타를 정합하게 검토하고 **과거 HEAD로 reset/rebase/force하지 않는다**.
2. 현재 NCP durable workspace `/root/WU088_HH_MASTER_EXEC_20261008/runs/master_20261008`, source-cache, 기존 `registry`, 완료 generation을 먼저 확인한다. 현지 데이터가 정상이고 해시가 맞으면 다운로드/과학 suite를 반복하지 않는다.
3. 현지 자료가 없으면 기존 연결된 Drive file ID `1pGl_SrlJGebBNrXJZPdJ_Q4_zZbOGH48`, 파일 `WU088_HH_NCP_MASTER_RETURN_20261008_sha_c0cb24b95a06.zip` (bytes=3,079,967; sha256=`c0cb24b95a06471b427b310eedd929ff2e0a1650fdaf248122f55a5faf05b9f6`)를 필요할 때 하나의 provider에서만 회수한다. 모든 payload hash를 확인한다.
4. NCP 원본 `ENERGY06_SOURCE_MEASURE.json`, `ENERGY06_SUCCESSOR_PROPOSAL.json`, `TWO_CELL_NEW_SCOPE_PROPOSAL.json`, `FD2_STATUS.json`, `BLOCKERS.json`, `NEXT_HANDOFF_KO.md`, `RUN_DAG.json`을 원 bytes로 회수한다. **새 exact science dispatch는 기본 0회**. 과거 6cell, FD1, FD2 approvals/registries는 consumed 상태다.
5. ON06G 고정 소스 `paired_runtime.rs` sha256=`8322d79609cc535b046b6000dd27bfdfd8859ddbffb5c3adac90ba396d6d2718`; `hh_paired_extension.rs` sha256=`f47958a8e185ab02cd7d6c00cb7760be583eb769147ca4ed04ef7b1404e87830`. 기존 ON06G 총256macro/t=3.2e11s checkpoint 불변. 최신 REI 본류에는 이 HH include가 없을 수 있으니 **명시적 opt-in source 후보**를 별도 경로에 구성하고 old root certificate를 새로운 source identity에 자동 전용하지 않는다.
6. 현재 교차 owner refs는 REI `40ea171d6be12275f9ee8b4f50f68b9dad59ed0a` (BRIDGE15), HE `54d99a3af01ac7eabb907be05c634bcc06570357` (E9), CR `58295e59e1c1815832a26769b05a3b5fcb96b47b` (R14). 수행 전 live refs를 재확인하되 이 연구용 codepath에 무단 merge/import하지 않는다.

## 1. 이번 수학·코드 연구의 재현 (비과학 작업, 즉시 시행)

원봉인 `WU088_HH_ENERGY06B_20261009_v1.zip`과 동일 경로의 `THEORY_KO.md`, `REPORT_KO.md`, `results/ANALYSIS.json`, `src/birth_contract.py`, `tests/test_birth_contract.py`를 확인한다.

새 output 경로에서:

```bash
python -B -m unittest discover -s tests -v
python -B research_loop.py --output /path/to/new-empty-output
```

예상 결과: scoped test **15개 통과**, 18개 synthetic direct case 및 5개 tangent case, 저장 source의 dyadic moment `-72057594037927939453125/36893488147419103232`, 120자리 crosscheck. 이 숫자는 물리 구간/실행 횟수가 아니다. input 해시가 다르거나 actual owner source의 call order가 달라지면 fail-closed하고 가능한 최신 버전의 차이를 보고한다. 사용자에게 과거 파일을 재업로드하도록 먼저 요구하지 않는다. `mpmath`가 없으면 별도 numerical crosscheck만 환경 문제로 보류하고 stdlib Fraction 및 15개 시험은 시행한다. 승인 없는 시스템 전역 설치 금지.

### 핵심 수학적 의무

`P'=S-kappa P`의 constant-opacity 보조 BE 모델에서

`F=(P+W)/(1+x)`, `H=(P+W/2)/(1+x/2)^2+(W/2)/(1+x/2)`, `H-F=x*(W-x*P)/[4*(1+x)*(1+x/2)^2]`, `x=kappa*h`, `W=S*h`.

**동일 source-law / 동일 초기 state**를 보존하되 **full과 refined의 discrete birth measure가 동일해야 한다고 강제하지 않는다**. 실제 `endpoint`는 시각별 `source_weights`, `source_n=dt*SOURCE`, packet 생성 후 BE를 사용한다. 이를 literal endpoint delta-injection with no absorption으로 바꾸지 않는다. 위 항등식/부호는 nonlinear angular HH source의 물리오차 추정이 아니다.

평형 `P=W/x`이면 서로 다른 birth times여도 defect=0, `W=0,P>0`에서는 birth measure가 같아도 homogeneous BE 분할차이가 남는다. 이 두 반례를 하나의 regression으로 유지한다. **원 NCP preflight의 ENERGY05_NO_BIRTH_OWNER_BIRTH_MISMATCH 차단은 그대로 유효**하다.

## 2. 실제 ENERGY06 owner에 필요한 opt-in 최소 구현

- `BirthLaw`: 원 `SOURCE`, `BIRTH=13.7eV`, 방향별 source weight 함수 및 고정 입력/clock/source hashes. `Scheme`: full/half/two-half의 **원 native schedule**, 각 단계의 신규 birth, operator order와 acceptance ledger ownership. 두 정책을 분리해 직렬화하고, 같은 underlying source law에서 서로 다른 quadrature measures가 나오도록 한다. 원 과학 함수의 기본 설정은 바꾸지 않는다.
- 실제 ON06G initial H/He gas·25packet/128directions×33grid와 한 macro의 원 시각을 정확하게 결속한다. aggregate-only ENERGY03–05 projected data에는 방향 분포가 없으므로 이를 억지로 128방향으로 재구성하지 않는다. 유효한 실제 native member를 원 저장 checkpoint에서 읽는다.
- 기존 `source_weights(c,h,t_end)`, redshift/hat mapping, per-direction photon transport, endpoint birth+BE order, gas nonphoto, `q_HH`, `J_HH` 및 `Q_HH=-chi_H J_HH`를 보존한다. extra1/2·extra1/n_e 금지. `13.6eV` fit cutoff와 `13.598434599702eV` binding energy는 구별한다.
- 각각 동일한 `theta,lambda`의 초기점에서 `(full)` 및 `(half1 -> half2)`를 수행하며, `birth_count_lambda`는 물리적 source law가 lambda-independent일 때만 0이다. 입력 photon/state tangent·energy-dependence·angular weights 및 transport/remap derivative를 초기화하지 않는다. 한 BE 단계의 선형 source 식에서 `M_i v_i=v_previous+birth_lambda+Delta t F_photon*N_lambda+Delta t c_H q_HH` 및 위 source-law에 필요한 실제 미분항을 포함한다. Exact preconditioner/Krawczyk 범위가 지원되지 않는 입력이면 거절한다.
- full-state는 defect diagnostic, accepted state/HH ledger는 **두 half source의 누적 합**만 등록한다. `full + half1 + half2`로 accepted event/heat를 기록하지 않는다. 전 구간의 광자 number, absorbed energy, chemical+thermal, escaping, redshift work 및 charge/nuclei ledger를 원 owner's owner policy대로 한 번만 계상한다. Static `N/U` closure는 direct Γ/heat rate accuracy와 별도다.
- `Energy05`의 no-birth local λ certification은 그 원래 scope에서 유지하되 **실제 birth-included root/paired acceptance로 전용하지 않는다**. Bianchi-I directional/tilt 범위도 원 frozen source 지원보다 넓혀 주장하지 않는다.

### 구현 직후의 최소 수행 증거

1. 소스·ABI·physics hash gate, wrong-origin/clock/birth-law ID/λ/energy/angle label·retry/duplicate rejected path를 test-first로 확인한다. 명시적 테스트 변경 시 어떤 RED를 관측했는지 기록한다. 기존 통과된 suite를 관례적으로 재실행하지 않는다.
2. toy/zero-source/source-only/opacity=0/equilibrium/threshold singleton/one-sided boundary/nuclei-energy-owner test. 비교법의 두 다른 discretization을 **같은 born packet으로 강제하는 잘못된 path**도 거절한다.
3. 기존 동일 source policy로 실제 owner macro의 full/twohalf를 비교할 때 반드시 native point와 새 parameter family enclosing roots를 구분한다. 본문 근·전용 HH counter·photo rate·state difference의 동일 입력을 인증하고 수치 admissibility가 실제로 통과한 범위만 반환한다.
4. Gate는 원 owner `local<2e-4`, `public_width<2e-3`, `ledger<=1e-12`, positivity/domain 및 구간 포함/수축을 그대로 사용한다. Full/half `source_n` bit 연산, angular weights, endpoint event과 accepted half sum을 모두 감사한다. 아직 계승 증명이 부족하면 `SCOPED_IMPLEMENTATION_VERIFIED__SCIENTIFIC_ACCEPTANCE_OPEN`으로 보고한다.
5. 실제 과학 native root/trajectory 추가 dispatch가 새 authorization 범위를 요구하면 구체적인 `OWNER_PAIRED_NEW_SCOPE_PROPOSAL.json`을 생성하고 **여기서는 dispatch0**으로 종료한다. 비과학 build/코드·fixture·source-bound exact audit를 멈추지 않는다.

## 3. 독립 C1: 272/0 두 미완료 H–H 원자 셀

원 pilot coverage는 24/289, 265 unbounded, epsilon_C/R=null, B22=OPEN_UNDETERMINED. FD2 finite 107 source-bound four field call은 종료됐지만 whole physical complex box에서의 integration admissibility·holomorphic derivative·sign/rank는 미증명이다. `TWO_CELL_NEW_SCOPE_PROPOSAL.json`은 준비안이고 과학 승인 기록이 아니다.

- 먼저 기존 candidate/worker/FD2 field records를 확인하고 **서로 다른 candidate integration worker**를 새 source identity로 작성·빌드한다. 원 code/box를 변경하지 않으며 kernel proof의 256-term tail·L1<=64 등 적용영역을 검사한다.
- 원 physical/log boxes의 full-domain inclusion, complex holomorphic derivatives, signed ordered107, fieldO/orbitalS, primitive0, precision128, radius2^-57, FLINT3.4.0/GMP6.3.0/MPFR4.2.2 ABI, cgroup identity를 확인한다.
- 실제 finite cgroup/CPU quota/effective memory·host free/ancestor cap, UID/cap/NoNewPrivs, loader를 실행 직전 확인한다. 기존 종료된 service의 finite memory 설정을 현재 live science binding으로 재사용하지 않는다. host-wide 설치/권한 상승/가짜 resource file 금지.
- 원 proposal의 제한(272/0, 두 native invocation 한 번씩, concurrency1, 최대120s each, evaluation200000, integration_calls1024, queue64, degree64, memory1024MiB/worker, reserve 조건, no-retry)을 **정확한 새 source/binary/run ID**에 결속한다. 조건이 모두 닫혀야 human exact authorization 원문을 새 파일로 별도 받는다. 기존 소비된 6셀·FD1·FD2 승인을 새 run에 재사용하지 않는다.
- 이 프롬프트는 **272/0 적분 허가가 아니다.** 과학 코드를 실행해 해시를 얻는 식의 one-shot registry 선소비, force retries, resource/precision/tolerance 완화 금지. 미충족 조건은 자격 미달의 정확 원인으로 남긴다.

## 4. 중복계산 방지와 기타 owner 결과

REI BRIDGE15의 conditional IEEE ledger, HE E9 OFF-only native prefix, CR R14 conditional optical first cell은 각 소유자의 결과다. 다른 owner의 과학 인증/연속오차/physical source를 HH에 자동 적용하지 않는다. 새 일이 이 변화와 맞닿을 때만 최신 ref·해시·구간을 selective import한다. REI BRIDGE16/HE KF·GM/CR R15 작업은 해당 owner에게 남긴다.

기존 256 macro·ENERGY05 실제 2-source nonlinear roots·1/2worker checkpoint validation·이전 native/old 40/TH01–TH05 suites·FN2/FD2 original callbacks는 **필요한 변경의 영향을 받지 않으면 재실행하지 않는다**. 속도 향상은 동일 원 native input·검증/benchmarks에서 동일한 과학 output이 나온 뒤에만 실험한다. 64CPU/128GiB를 실제 할당량이라고 선가정하지 않는다.

## 5. 반환 파일·백업·검증 수준

매 단계 root:

- `INVENTORY.json`, `SOURCE_BINDING.json`, `RUN_DAG.json`, `RUN_LEDGER.jsonl`, `CLAIM_LEDGER.json`, `AUTHORIZATION_AUDIT.json`, `INPUT_SHA256SUMS`, `COMMANDS.jsonl`, `BLOCKERS.json`.
- ENERGY06C scoped results: `SOURCE_LAW_AND_SCHEMES.json`, `BIRTH_LEDGER.json`, `PARAMETER_TANGENT.json`, `PAIRED_DEFECT.json`, `ROOT_AND_GATE_RESULTS.json`, 독립 `INDEPENDENT_CHECKS.json`, 실제 gate의 stdout/stderr exit, source-target regression.
- C1 준비: `FULL_BOX_FEASIBILITY.json`, `CANDIDATE_WORKER_IDENTITY.json`, `CGROUP_BINDING.json`, `TWO_CELL_NEW_SCOPE_PROPOSAL_V2.json`(근거가 모두 있는 경우), `authorization_record=null` unless actual separately issued authorization.
- `REPORT_KO.md`, `NEXT_HANDOFF_KO.md`, machine-readable `NCP_LOCAL_CODEX_RETURN.json`, 재현 command, SHA-256 manifest, 에러 증거와 checkpoint/status.

새 연구 브랜치에 force 없이 추가 경로로 게시하고, 기존 Drive parent `1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM`, Dropbox `/BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/`에 **create-only 이중백업**을 수행한다. provider ACK/ID/name/size와 full remote restore + SHA를 구분한다. 연결이 안 되면 로컬 번들·manifest를 남기고 `BACKUP_PENDING`을 정확히 보고하라. 공유 credentials 로그/ZIP 삽입 금지. 원 G checkpoint/old DB/registry/source 또는 타 원자 저장소를 변경하지 않는다.

최종 claim은 `hh-scoped-toy`, `source-bound-static`, `new-coupled-root`, `new-paired-accepted`, `continuous-true-error`, `physical-admission`, `production-admission`을 각각 분리해 표기한다. 24/289·265unbounded·epsilonC/Rnull·B22OPEN·canonical S0 OFF·HH_ACTIVE/productionHOLD는 실제 새 authority가 없으면 보존한다.

**착수:** 위 반환 소스와 본 연구 파일을 먼저 읽어 환경·authority를 검증하라. 정확한 과학 scope가 아직 없는 상태에서 할 수 있는 코드 구현/테스트/preflight/proposal은 실제 수행하되, 무승인 native scientific dispatch를 강행하지 마라.
