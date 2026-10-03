# WU088 HH 이론·수치 구현 공백 보완 보고서

이번 loop는 DB v3와 시작 HEAD `393eb882f7fbf160cfb465849d9652c7b026b5be`를 기준으로 G0–G6의 비과학 실행·합성 검증 범위를 진행했다. 과거 미게시 초안을 복구해 실제 source와 대조한 뒤, 구현을 보완하고 별도 artifact review의 재현 가능한 결함을 수정했다. 실제 HH 배열·상수·콜백·적분·certificate는 평가하지 않았다. 모든 B01–B05를 CLOSED라고 보고할 근거는 아직 없다.

같은 브랜치의 최신 remote HEAD/tree와 PR #33(open, draft, unmerged)을 확인했다. 40개 canonical text artifact는 시작 tree의 Git blob 및 SHA256에 맞춰 고정했고, 기존 science source의 수정은 0건이다. Acquisition DB는 68 canonical source, 79 version records, 66 acquired files를 유지했다. 필요한 authority가 확보되어 broad literature search를 반복하지 않았다.

## 완료한 산출물과 근거 범위

| 단계 | 실제 산출물 | 근거 상태와 한계 |
|---|---|---|
| G0 | 36개 sub-obligation의 source/theorem/module/test crosswalk, namespace 분리 | ESTABLISHED source identity; 문헌 존재를 HH closure로 승격하지 않음 |
| G1 | 추가 implementation lemma 12개와 source-bound 미분·domain·assembly 조건 | DERIVED under explicit premises; formal proof assistant/native verification 아님 |
| G2 | NPY1/2/3, binary64/c128, authority-bound x87/binary128, C/Fortran exact decoder | IMPLEMENTATION_VERIFIED synthetic; 역사적 ABI 연결은 BLOCKED |
| G3 | exact Gram, integer-outward sqrt, K/Dmax/gap, direct g−·legacy eta, separate RNE predicate audit | IMPLEMENTATION_VERIFIED synthetic; actual gaps/eta 미평가 |
| G4 | Acb radial/field callback, normalization, donor/orbital contraction, parity/phase, post-integral D assembly | IMPLEMENTED + source/API/static reviewed; native compile/runtime UNVERIFIED |
| G5 | Hermite positive envelope, half-gamma lower tail, algebraic upper tail, Gaussian majorant, disjoint complement | IMPLEMENTATION_VERIFIED synthetic; actual HH endpoint constants 미평가 |
| G6 | exact rectangular range integration와 bounded nested toy pilot, FLINT/Petras native wrapper draft | synthetic width/work measured; actual HH feasibility UNMEASURED |
| 연결부 | Frozen107-shaped NPZ→rational record→native initializer, synthetic G2→G3→epsilon→decision seam, process guard | synthetic/static verification; 생성 fixture를 science evidence로 사용하지 않음 |

정확 제곱근은 G3에 한해 증명된 integer-isqrt rational enclosure를 사용한다. 이를 FLINT/MPFR 실행 결과로 표기하지 않는다. G5의 upper incomplete gamma는 유효한 analytic inequality와 positive recurrence로 감싼다. Decimal/Simpson oracle는 구현을 검산하는 비인증 진단이며 rigorous integration proof를 대신하지 않는다.

## 새로 확인한 결함과 구분

B07은 acquisition catalog와 source-functional map의 bare S01 ID 충돌이다. 새 crosswalk는 namespace-qualified references를 사용한다. B08은 PRIMARY의 `other-local>tol`과 SECONDARY의 `local<other-tol`이 binary64 경계에서 달라진다는 source-bound 반례다. 두 식을 구별해 검증했으며, 실제 archived scalar bits/rounding 환경의 admission은 아직 필요하다.

B09 empty Fortran array의 과다 pool allocation, B10 exact-root/rounding 경로의 work cap 사전 검사 누락, B12 model-only cap의 실패 분류 불일치, B13 leader 이후 child의 실행 지속, B14 self-hashed record의 pinned-loader provenance 위조 경로는 실패를 재현한 뒤 수정·재검증했다. B11 native callback failure slots·setter·resource guards와 B15 nested analytic trial refusal의 불필요한 global abort 등은 native draft를 수정하고 정적으로 재검토했다. C++ 수정의 실행 검증은 host gate에 남긴다.

Raw exact-constructed K=(C−R†)/2, frozen model의 독립 stored K, old comparator의 rounded complex128 K는 별개의 대상이다. Direct gap route는 앞의 두 대상을 사용하고 legacy eta는 published diagnostic과의 차이를 별도 포괄한다. 양쪽 경로의 eta/producer categories를 중복 가산하지 않는다.

## 이번 overlay의 fresh verification

| Suite | 테스트 | Skip | Exit | 해석 |
|---|---:|---:|---:|---|
| G1_exact_theorem | 15 | 0 | 0 | synthetic/exact implementation check |
| G2_exact_decoder | 30 | 0 | 0 | synthetic/exact implementation check |
| G3_exact_gram | 23 | 0 | 0 | synthetic/exact implementation check |
| G4_callback_static_exact | 6 | 0 | 0 | native source/static check |
| G4_assembly_static_exact | 7 | 0 | 0 | native source/static check |
| G4_optional_point_oracle | 3 | 3 | 0 | optional oracle 미실행 |
| G5_endpoint | 17 | 0 | 0 | synthetic/exact implementation check |
| G6_synthetic_pilot | 21 | 0 | 0 | synthetic/exact implementation check |
| G6_Petras_draft_static | 10 | 0 | 0 | native source/static check |
| synthetic_pipeline | 8 | 0 | 0 | synthetic/exact implementation check |
| host_process_guard | 5 | 0 | 0 | synthetic/exact implementation check |
| Frozen107_shaped_synthetic_adapter | 16 | 0 | 0 | synthetic/exact implementation check |

각 suite의 실제 명령·exit·로그·당시 코드 SHA는 `verification/VERIFICATION.json`에 있다. 합성 tests를 과거 science test count에 더하지 않았다. 최초 RED/실패, mpmath 부재, 잘못된 interval-equality oracle, 로그 절단 이상도 원 evidence와 분리된 correction 기록으로 보존했다. Optional mpmath skip은 PASS case가 아니다.

G6 toy의 exact references는 uniform inner z/3와 nested outer 1/6이다. Callback 수·분할·wall·메모리는 `INTERIOR_PILOT_REPORT.md`와 `FEASIBILITY_LEDGER.json`에 있으며 HH 비용으로 외삽하지 않는다. Python integrator wall guard는 cooperative이고 state memory는 추정치다. Host wrapper는 process-group timeout와 프로세스별 address-space hard limit을 제공하지만 process-tree RSS 합계나 zombie의 즉시 재수거를 보장하지 않는다.

## 남은 blocker와 다음 실행

| Blocker | 현재 결론 | 다음 필요한 증거 |
|---|---|---|
| B01 | OPEN | pinned backend build/ABI/binary와 native callback·assembly·integration acceptance |
| B02 | NOT_EVALUATED 실제 HH enclosure | 실제 endpoint/interior/O/G/D balls와 usable epsilon |
| B03 | RAW_ABI_AUTHORITY_BLOCKED | 과거 NumPy serializer/build/layout과 archived output의 연결 |
| B04 | 실제 gaps·eta·machine trace 미평가 | 승인된 exact payload intake와 실제 represented interval |
| B05 | 실제 HH feasibility UNMEASURED | bounded primitive pilot의 실제 width/work/domain/resource 결과 |
| B06 | IRRELEVANT_BY_SELECTED_ROUTE | 현재 continuous-target route에는 stored GL-rule authority 불필요 |

다음 노드는 `HOST_SYNTHETIC_BUILD_AND_HISTORICAL_ABI_EVIDENCE`다. Native 초안을 sidecar에서 빌드·합성 검증하고, 과거 serializer evidence를 회수한다. 실제 HH 수치 실행은 첨부 master prompt §G7/§14의 명시적 승인 경계 때문에 실행하지 않았다. `NUMERICAL_EXECUTION_SCOPE.json`은 exact input pin, 유한 endpoint 후보, precision/work/memory caps와 단일 primitive 목표를 작성한 미승인 제안이다. Binary hash가 없으므로 아직 approval-ready/execution-ready가 아니며 승인 한 번으로 missing runtime/ABI evidence를 대체할 수 없다.

Full G7의 D_col 47×2 및 D_row 2×47, 총188 entries의 실행은 단일 pilot 범위에 포함되지 않는다. Pilot과 backend/ABI 증거가 확보된 뒤 전체 예산과 binary identity를 별도로 고정한다. Existing B128/B160 승인은 재사용하지 않으며 B192 재계산·R31AK 재훈련·새 geometry/order·comparator rerun은 없다.

## 과학 판정과 전달

`B_ORDER_VERDICT_STABLE_OVER_128_160_192`, PRIMARY=`PARETO_SUPPORTED_AT_SELECTED_HOLDOUT`, SECONDARY=`REFINED_PARETO_SUPPORTED_AT_Z075`를 보존했다. `SOURCE_ACCURACY_BOUND_UNAVAILABLE`, `RIGOROUS_REFERENCE_CERTIFICATION_BLOCKED_BY_MISSING_ERROR_BOUND`, epsilon/eta=null, rigorous=false도 유지한다. 0.02856621001324109/t_a는 eta=0 아래의 design budget이며 actual epsilon이 아니다.

별도 agent의 artifact review를 실제 project-admitted scientific decision review로 승격하지 않았다. `independent_review_admitted=false`다. 원본 코드/자료, byte identity, semantic target, synthetic verification, native runtime, actual enclosure, decision admission 및 upload/restore의 근거 층을 구분한다.

보고서·코드·테스트·manifest·receipts는 같은 branch에 additive non-force 게시한다. 제3자 문헌/코드 raw payload는 새 public commit에 포함하지 않는다. 새 ZIP은 지정된 Drive/Dropbox에 create-only로 업로드하고 ACK·object ID·parent/path·metadata size로 검증한다. 실제 확정 Git 및 provider identity는 detached `DELIVERY_RETURN.json`이 기록한다. Remote download 복원 검증은 하지 않으므로 `RESTORE_VERIFIED=false`다.
