# R31V: post-idle M3 controls와 metric correction 하한

2026-09-28. 기준은 R31U `ff3db87dfbadd5f1eed89b413e5b785baf63a429`이며 기존 실행선/원시 결과/물리 tolerance는 변경하지 않았다. 이 보고서는 새 opt-in adapter 구현과 기존 데이터에 대한 추가 연구를 구분한다.

## 1. 복구와 현황 정정

R31U 원본 ZIP 93,270 bytes, SHA-256 `54b91ac6d111d6c3b2358cc143827b030a73d876ec1e3560c14b4e4284d5ebaa`를 Library에서 복구했다. 내부 manifest 19개를 확인하고 기존 15 tests와 metric replay를 실제 재실행했다. Google Drive의 같은 ZIP을 raw fetch하여 SHA/CRC를 확인했고, Dropbox는 size 및 provider block content hash를 로컬 계산과 대조했다. Dropbox raw restore를 수행한 것은 아니다.

마지막 붙여넣기에는 R31U 이중백업이 미수행이라고 되어 있지만 실제로는 그 뒤 11:17~11:18 UTC에 두 provider에 업로드되어 있었다. 중복 업로드하지 않았다. 이전 assistant의 H0 authority 미주입 요약도 오래된 상태였다. 현 PR12에는 H0 authority 반영, B160 M3A, B192 pilot, 6개 full-pair exactness가 이미 있다. 미완료는 오염 없이 측정한 M3B이다.

세 프로젝트의 idle은 사용자 보고이다. 이 세션에서 NCP VM의 PID/cgroup 목록에 직접 접근하거나 process/affinity/cgroup를 변경하지 않았다.

## 2. 다른 저장소에서 읽은 것과 가져오지 않은 것

- bass_cr `6f4be73104d791011137659fe08c71b6e354aaf3`: CURRENT_STATE 및 MATHEMATICAL_SUPPLEMENT를 읽었다. F1-R2는 297/297 tasks, 60 workers, elapsed 1817.893839 s의 F1_ENGINE_ADMISSION_PASS이며 exactly-once authorization은 소비됐다. 다음은 R3_POSTPASS_CACHE_REUSE_AND_METRIC_AUDIT이다. 이 결과를 여기서 재실행한 것은 아니며 capture/production admission으로 확장하지 않는다.
- BASS_HE `3746aeace488be09d568a0c99935e917f4ef4a91`: R2 REPORT를 읽었다. resume-004의 runtime closure와 CODE-I02 독립 재검수 대기를 구별한다. common-contour의 이산 evaluator에 대한 interpolation bound 및 source/quadrature/interpolation/roundoff 오차 분리가 핵심이다. 14개 trace/7970 withheld comparisons는 해당 저장소의 기존 결과이며 HH 계산으로 집계하지 않는다.

CR에서 numerical-object identity와 output-path provenance의 분리, 준비 계산과 cache-only 소비의 분리를 가져왔다. HE에서 조건부 오차 상계와 원자료 오차를 따로 다루는 방법을 가져왔다. H/O/D 배열, 원자물리 파라미터, contour/homotopy 조건, tolerance와 다른 프로젝트의 PASS는 가져오지 않았다.

## 3. 이번에 실제 작성한 코드

`m3_postidle.py`는 원래 m3_throughput.py를 수정하거나 대체하지 않는 별도 진입점이다. 기존 worker/init/full_pair/compare 함수를 그대로 호출한다. 네 legacy 파일의 정확한 Git blob을 확인하여 interface drift 시 중단한다.

- 모든 layout에 동일한 12 pairs x 11 repeats = 132 tasks를 공급한다. 측정은 configuration당 3회이며 순서 hash와 histogram을 결과에 기록한다. 132개 새 scientific pair/node가 아니다.
- host의 CPU 개수가 아니라 명시적 grant, 현 sched_getaffinity, 보이는 모든 cgroup-v2 조상 quota의 교집합을 사용한다. memory reserve와 B192 private-memory pilot을 적용하여 native 준비와 pool 시작 전에 검사한다. 측정 전후에도 grant/메모리/cgroup를 다시 확인한다.
- reference cache는 numeric source/model/grid/실제 binary bytes/ABI/rounding context와 pair에 결합된다. PID, output directory, worker count는 numerical key에 넣지 않는다. create-only 원자적 JSON, dtype/shape/finite/byte hash 검사, 읽기 중 native 호출 금지를 구현했다.
- `prepare`만 명시적으로 누락된 serial reference를 계산한다. `benchmark`는 누락 cache에서 실패하며, timed batch는 매번 실제 legacy native backend를 호출한다. 매 reference와 측정 repetition의 checkpoint를 남긴다.
- 모든 결과의 production_admitted=false이다. 측정 종료 상태도 REVIEW_REQUIRED이다. 범용 broker, systemd 설치, cgroup partition 설정, continuous process surveillance, M4 async executor를 구현했다고 하지 않는다.

이 adapter는 BENCHMARK_EXCLUSIVE grant만 허용한다. HH32/HE16/CR12 동시 운영은 아직 승인하거나 배포하지 않았다. cpuset/가시적 quota 검사는 독점 cgroup 존재 또는 bandwidth/I/O 비경쟁의 증명이 아니다. NCP root/namespace 및 다른 owner 작업이 없다는 확인은 실제 VM 검토에서 별도로 필요하다. SIGKILL/host loss 후 완료하지 않은 measurement는 IN_PROGRESS checkpoint로 남으며, 이를 PASS나 자동 resume 권한으로 읽으면 안 된다.

## 4. 추가 연구: norm 구조를 맞추는 최소 수정량

물리 시간 t에서 O>0, H=H†, D=Phi† dot(Phi)를 두고

    i hbar O dot(c) = (H-i hbar D)c,
    R = actual(dot O)-D-D†,
    O=C†C, E=C^-† R C^-1, eta=||E||_2

로 정의한다. R31U가 이미 보인 d(c†Oc)/dt=c†Rc에서 H의 소거는 H Hermiticity를 전제로 한다. 이번에는 같은 O와 actual(dot O)를 유지하면서 D*=D+delta D로 metric compatibility를 맞추는 데 필요한 수정량을 정량화했다.

조건은 delta D+delta D†=R이다. X=C^-† delta D C^-1로 쓰면 X+X†=E. 따라서

    ||E||_2 <= ||X||_2+||X†||_2 = 2||X||_2.

X=E/2, 즉 delta D=R/2가 하한을 달성하므로

    min_metric-compatible ||C^-† delta D C^-1||_2 = eta/2.

Frobenius norm에서도 Hermitian/skew-Hermitian 부분의 직교성을 사용하면 최소값은 ||E||_F/2이다. 이것은 물리적 정확성을 보장하는 수선법이 아니라, represented equations를 norm-compatible하게 바꾸는 데 필요한 수정의 크기이다. source arrays는 수정하지 않았다.

## 5. 좌표 불변성과 조건부 원자료 오차 envelope

임의의 가역 basis 변환 T에 대해 Otilde=T†OT, Rtilde=T†RT이면

    eta = sup_(x!=0) |x†R x|/(x†O x)

는 변하지 않는다. 시간 의존 T일 때에도 실제 미분과 Dtilde=T†DT+T†O dot(T)를 함께 변환해야 R의 congruence가 성립한다. 기존 Q로 줄인 25차원 공간 내부에서 이 성질을 검사했다. 임의 basis truncation 자체에 불변이라는 주장은 아니다.

계산된 Oc,Rc에서 실제 행렬이 O*=Oc+delta O, R*=Rc+delta R라 하자. Oc=Cc†Cc와

    ||Cc^-† delta O Cc^-1||_2 <= eps_O < 1,
    ||Cc^-† delta R Cc^-1||_2 <= eps_R

라는 별도 유효 상계가 있을 때만 Rayleigh quotient와 삼각부등식으로

    max(0,eta_c-eps_R)/(1+eps_O) <= eta_*
    eta_* <= (eta_c+eps_R)/(1-eps_O)

를 얻는다. eps_O는 무차원, eta와 eps_R는 시간 역수이다. 따라서 최소 수정량의 보장 하한도 왼쪽 식의 절반이다. 이는 O*의 양의 정부호도 보장하지만, HH 데이터의 eps_O/eps_R를 이번에 산출한 것은 아니다. 노드 차이나 보간 차이를 자동으로 이 상계에 넣어서는 안 된다.

## 6. 실제 계산과 검증 범위

기존 z=0,4 입력과 보존된 z=2 full49 snapshot만 읽었다. R31U의 instantaneous construction과 같은 neutral block을 유지하고, stored complex256 일부를 binary64 diagnostic 행렬로 변환하는 기존 경로를 명시적으로 유지했다.

- eta = 0.6007169417167524 / atomic time.
- 최소 whitened connection correction = 0.3003584708583762 / atomic time.
- 최소 Frobenius correction = 0.38544269467010966 / atomic time.
- Cholesky+SVD와 generalized Hermitian eigenproblem의 eta 차이는 이번 실행에서 0.0.
- 가역 coordinate 변환 64개에서 eta 최대 차이 1.5543122344752192e-15.
- synthetic noncommuting perturbation 1000개에서 conditional-envelope 관측 위반 0.

raw/reduced residual의 Hermiticity는 floating tolerance로 검사했고 whitened gap은 약1.57e-14이다. 위 수치는 interval arithmetic이나 exact-data error enclosure가 아니다. 단일 시각의 eta에 전체 시간폭을 곱해 trajectory 오차라고 보고하지 않는다. norm-compatible Hermite 후보의 큰 withheld direct-value error라는 R31U 판정도 여전히 유효하다.

새 focused tests 67개가 통과했다. 최초 RED 61 failures, driver RED 5 failures를 보존했다. 첫 GREEN의 실패 1개는 scalar Cholesky 결과를 정수 3과 exact equality로 비교한 테스트 assertion 문제였으며, 1 ULP 수준이므로 approx assertion으로 수정했다. 수학/커널 실패로 기록하지 않는다. 추가 path-independence 테스트를 포함한 최종 실행은 67 PASS이다. 별도로 원본 R31U 15 tests가 통과했다. 전체 WU088_HH repository suite, 실제 fork/spawn native integration, NCP timing, 독립 심사는 실행하지 않았다.

## 7. 문헌과 claim ceiling

Artacho–O'Regan, *Quantum mechanics in an evolving Hilbert space*, arXiv:1608.05300은 moving basis의 connection과 gauge 문맥을 제공한다. Auzinger et al., *A posteriori error estimation for Magnus-type integrators*, DOI 10.1051/m2an/2018050은 주어진 skew-Hermitian ODE의 integrator defect와 local error를 다룬다. 그 integrator 결과는 잘못 보간된 generator의 물리 정확성 인증을 대신하지 않는다. 이번 최소 수정 및 조건부 envelope는 위 전제에서 직접 유도한 결과이며 신규 문헌 정리나 새로운 우선권을 주장하지 않는다.

Sources:
- https://arxiv.org/abs/1608.05300
- https://archive.numdam.org/articles/10.1051/m2an/2018050/
- https://docs.kernel.org/admin-guide/cgroup-v2.html
- pinned repo paths/blobs: SOURCE_PINS.json

새 native kernel calls=0, 새 heavy scientific nodes=0, trajectory=0, NCP 설정 변경=0. z1/z0.5/full144/M4 async/M5/production/main merge lock을 해제하지 않았다. 다음은 실제 VM에서 제공된 코드의 집중 검토와 필요한 최소 수정, 기존 source/build/pilot 확인, exclusive grant 아래 prepare 및 제한된 M3B 실행이다.
