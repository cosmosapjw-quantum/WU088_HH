# WU088 HH G0–G6 재개 계약

같은 브랜치 `research/r31ao-unequal-order-ladder-20260930`에서 이어간다. 이 폴더를 포함한 실제 remote HEAD/tree와 PR #33부터 읽고, 과거 `393eb882`로 reset하지 않는다. 새 브랜치·force·merge·rebase·main 변경은 금지다. 게시 커밋과 백업 객체의 확정값은 전달된 detached `DELIVERY_RETURN.json`을 따른다.

먼저 `RESULT.json`, `GAP_CLOSURE_SSOT.json`, `OPEN_OBLIGATION_LEDGER.json`, `RESEARCH_REPORT_KO.md`, `NUMERICAL_EXECUTION_SCOPE.json`, `verification/VERIFICATION.json`을 읽는다. 새 구현의 source identity는 `MANIFEST.sha256.json`에 있다. 과거 원본·실패 로그·과학 결과는 변경하지 않는다. G0의 40개 canonical artifact는 원격 시작 tree와 일치한다.

## 현재 구현과 claim ceiling

Exact NPY decoder, rational Gram/gap engine, endpoint evaluator, synthetic uniform range integration, synthetic certificate seam은 합성·정확 검증을 거쳤다. C++ Acb callback·normalization·orbital/phase/D assembly·Petras wrapper는 source/API/static 검토를 거친 **native 미실행 초안**이다. Frozen107-shaped adapter의 생성 fixture는 실제 Frozen107 값이 아니다.

`RAW_ABI_AUTHORITY.json`은 여전히 `RAW_ABI_AUTHORITY_BLOCKED`다. x86_64, GCC와 NumPy source만으로 B192 serializer의 정확한 wheel/build/layout을 확정하지 않는다. 현재 host에서 새 probe를 실행해도 과거 producer 증거가 되지 않는다. Decoder의 `LayoutAuthority` 객체가 구조적으로 유효하다는 사실도 historical authority 승인이 아니다.

`certified_epsilon=null`, `certified_eta=null`, `rigorous=false`를 유지한다. `B_ORDER_VERDICT_STABLE_OVER_128_160_192`, PRIMARY/SECONDARY의 기존 finite-order verdict와 z=0.75 holdout은 그대로다. B128/B160 승인은 소진되었고 B192는 기존 출력 재사용만 허용된다.

## 다음 노드: host synthetic build + historical evidence

1. FLINT 3.4.0, GMP 6.3.0, MPFR 4.2.2의 `BACKEND_IDENTITY.json` source SHA를 지킨다. 별도 sidecar prefix를 사용하며 기존 scientific runtime을 교체하지 않는다. 원 archive는 DB v3가 가리키는 v2 raw archive에 있다. 제3자 원본은 이 코드 패키지에 중복 수록하지 않았다.
2. 실제 compiler·flags·ABI·build log·linked shared libraries·binary SHA를 수집한다. `verified_build_provenance=true`를 적는 행위 자체가 build authority가 되는 것은 아니다. `verify_build_inputs.py`는 bytes와 구조를 확인하는 보조 gate다.
3. `validated_callback/build_host.sh`로 native synthetic executable만 빌드한다. 새로운 output directory를 지정한다. ldd 경로가 검증한 prefix/binary와 일치하는지 확인한 뒤 `host_guard/run_guarded.py`로 synthetic acceptance를 실행한다. `interior_pilot/PETRAS_HOST_README.md`의 별도 native integration fixture도 같은 방식으로 검증한다.
4. `frozen_input/` adapter가 생성하는 exact rational records와 native setter의 연결은 먼저 생성 fixture로 검증한다. 실제 Frozen107 파일을 로드하거나 실제 HH parameter로 callback을 호출하지 않는다.
5. `exact_raw_decoder/HISTORICAL_LAYOUT_CAPTURE_PLAN.md`에 따라 **과거** serializer/binary/config와 archived outputs의 연결 증거를 회수한다. evidence 부족이면 ABI blocker를 그대로 반환한다. 근거 없는 layout fallback은 하지 않는다.
6. host return에는 명령, exit, stdout/stderr, compiler/version/flags, CPU/ABI, source/binary/linked-library hashes, native synthetic 결과, actual-HH count=0, 실패 분류를 포함한다. 두 provider 백업의 ACK와 metadata를 기록하되 restore는 실제 검증 전 false다.

수행 가능한 이 단계는 native software verification이며 실제 HH 수치 인증 승인을 대신하지 않는다. 원래 science full suite나 comparator는 실행하지 않는다.

## 실제 HH 작업 경계

`NUMERICAL_EXECUTION_SCOPE.json`은 **미승인·미실행·아직 execution-ready가 아닌 제안**이다. binary hash가 null인 상태로 실제 실행 승인서라고 사용하지 않는다. Host/native/ABI 증거가 채워지면 다음의 bounded scope를 다시 고정해 별도 명시적 승인을 받는다.

- frozen z=3/4, active=0, a_index=b_index=0, s angular의 O/G1/G2 primitive pilot.
- endpoint 후보는 양 축 `[1/16,16]`, precision 128→256→512bit, 총 callback dispatch 20,000, wall 300초, single process/thread, address-space 2 GiB. 이는 미측정 설계 후보이며 HH 적합성 주장이 아니다.
- 실제 represented-array decode/gap은 별도 60초·512 MiB 범위로 분리한다. B192 D_col/D_row와 세 모델의 stored K/D만 사용하고 JVP/새 geometry/order/훈련은 추가하지 않는다.
- full G7의 188개 D entries는 이 pilot 승인에 포함되지 않는다. 실제 pilot 결과와 binary identity를 검토한 뒤 전체 certificate 예산을 별도로 확정한다. 무한 adaptive escalation은 금지다.

Endpoint→interior→assembly의 error radius는 한 번씩만 계상한다. X0…X8를 end-to-end epsilon에 재가산하지 않는다. D_row conjugation은 real-domain integration 이후에만 한다. Direct represented gap과 legacy eta는 분리하며, raw exact-constructed K·model stored K·legacy rounded K를 혼동하지 않는다.

PRIMARY의 `other-local > tol`과 SECONDARY의 `local < other-tol`은 binary64에서 다를 수 있다. 두 source expression과 tolerance bit를 그대로 보존한다. 합성 real-rule 충분조건 통과를 original machine predicate·continuous target·science promotion의 완료로 표기하지 않는다.

Artifact review와 프로젝트 수준 독립 decision review는 별개다. 현재 `independent_review_admitted=false`다. Native 또는 actual HH gate가 열리지 않으면 해당 blocker를 정확히 기록하고, 가능한 코드/증거 산출물은 같은 브랜치에 ordinary non-force 게시 및 create-only 이중백업한다.
