# R12 이전 GitHub 전체 head 조사와 변경 원문 종합

## 결론과 시간 경계

이 조사는 다음 연구 단위를 정하기 위한 읽기 전용 intake다. **접근 가능한 51개 저장소의 2,385개 head를 실제 pagination 종단까지 읽었다.** 공개 branch에서 R10 census 이후 새 head 10개와 이동 head 6개를 확인했다. 그중 R11 때 이미 읽은 동일 immutable source 4개를 재사용하고, 새로 읽어야 할 **12개 branch의 관련 handoff·계약·결과 원문을 모두 읽었다.** 모든 branch의 모든 파일 본문이나 과거 이력을 읽었다는 뜻은 아니다.

이번에 읽은 변경 원문과 V8 원본 백업 교차대조 범위에서 **새 actual HD reactive array 또는 named WU physical consumer/state/density/clock 결속은 공급되지 않았다.** 이 결론은 조사 범위에 한정된다. 다른 자료가 전역적으로 없다는 주장은 하지 않는다.

- 최초 WU HEAD 확인: 2026-10-28 **13:38:12 KST**.
- branch census 읽기 구간: **13:39:30.837–13:39:41.723 KST**. 동시 atomic snapshot이 아니다.
- 선택한 immutable source 본문 읽기 종료: **13:48:01.266 KST**.
- WU HEAD 마지막 재확인: **13:48:14 KST**, R11 FINAL `c0b97999b928acb04a805bf3e5283af73aff9831` 그대로다.
- 기준 FINAL tree: `503d048cc83b5813f15cd5996277403f16166db4`. 이번 두 ref GET은 HEAD identity 재확인이며 tree의 모든 member를 다시 검증한 것은 아니다.

권위 있는 기계 기록은 [PUBLIC_CENSUS.json](PUBLIC_CENSUS.json), [PUBLIC_HEAD_DELTA.json](PUBLIC_HEAD_DELTA.json), [R11_SEVEN_REF_DELTA.json](R11_SEVEN_REF_DELTA.json), [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json), [CONTENT_READ_SCOPE.json](CONTENT_READ_SCOPE.json), [IDENTITY_READS.json](IDENTITY_READS.json)이다.

## 전체 census와 이전 기준의 차이

| 범위 | 저장소 | heads | branch pages |
|---|---:|---:|---:|
| 공개 | 35 | 1,902 | 48 |
| 비공개 집계 | 16 | 483 | 18 |
| 접근 가능한 전체 | 51 | 2,385 | 66 |

저장소 목록은 limit100, offset0에서51건, offset100에서0건을 실제 반환했다. 저장소 목록2페이지와 branch66페이지를 합쳐 **68 provider page reads**, branch 종단51/51, 실패 페이지0이다. 이름 필터로 head를 제외하지 않았다. 공개 결과에는 비공개 이름·branch·SHA를 넣지 않았다. 비공개 현재 identities는 비공개 작업 파일에만 남기며 게시 대상이 아니다.

R10 기준은 공개35/1,892 + 비공개16/483 =51/2,375 heads, branch65pages였다. 공개 head는 신규10·이동6·삭제0·불변1,886이다. 공개 저장소 집합은 동일하다. 비공개 count483이 같다는 사실만으로 비공개 head identities가 불변이라고 말할 수 없다. 기존 공개 census에는 비공개 상세 baseline이 없으며 이 한계를 유지한다.

R11의 지정7ref와 비교하면 **REI causal prefix만 이동1**, 나머지6불변이다. REI는 `66878795aa14f79b32be0cd532c31b3a4a036985`에서 `7d1cf19e61c372ecda7964e50991685f006dc1ee`로 이동했다. R10 이후 움직였으나 현재 R11에서 이미 읽은 immutable source와 같은 WU FINAL, BASS restart `f834101d…`, CR event-union `729cb951…`, REI central `3d8bcdb7…`는 완료 근거를 재사용했다. 이들 중 CR의 조건부 consumer를 WU physical binding으로 승격하지 않았다.

## 실제로 바뀐 source 12개

아래 SHA는 census에서 고정한 source identity다. G 번호는 SOURCE_MANIFEST의 실제 읽기 기록이며, 저장한 본문과 정확 Git blob/bytes/SHA-256을 찾을 수 있다.

| branch / immutable SHA | 새로 확인한 상태와 WU에 대한 의미 | 읽은 근거 |
|---|---|---|
| REC native path / `38d543bac481f537b940f0c18f85ff2cf2cfbd2d` | 과거 capture 원본의 **실제 복구와 실행 source의 lossless 재현**이 새 정보다. 과거 “원 archive bytes 미복구” 상태를 현재 상태로 반복하면 안 된다. Git 현재 C10 IN_PROGRESS, physical0/313·오차 필드 null·H6/H7 OPEN 유지. | G06,G08–G10,G22,G23 |
| REI causal prefix / `7d1cf19e61c372ecda7964e50991685f006dc1ee` | 고정 BASS source와11-field packet을 실제 소비한 C7 caloric validation, **12/20**. actual temperature update/native25/physical radii null. WU HD/consumer binding 미공급을 직접 명시한다. | G05,G11 |
| HE harmonic10 / `a73773a9e1056bf18405453a0e88b9d12a15e9ac` | 조건부 second-harmonic Fourier–Bernstein reference20/20, local10 complete+1 partial+3 physical open/14. 실제 flux/history·birth/deposition/thermalization은 미결. WU의 반응 입력으로 대체할 수 없다. | G19,G27 |
| BASS Lyα dual / `fed29a0195ca9bec270971abe4ed60c7d23cff29` | 같은 source law/cell의 상수 비음수 dual witness로 finite reward 상계를 조임. **18/20**, distinct-author R6/C9 미완. 새 HD 물리 입력이 아니다. | G12,G24 |
| BASS QSS enclosure / `5c3623cb06280561853b00b33d74ae638ab24c82` | source-literal exactdyadic QSS 대표의 산술 enclosure, **18/20**, 독립 R6/C9 대기. 원 미저장 QSS와 E_QSS_old는 null. source/physical uncertainty로 바꾸지 않는다. | G13,G25 |
| BASS BF1 / `30b229ed99337ed2f846badf75538abf8b4c3c8e` | 고정 common observer/coframe의 물리 carrier 공간 projection. 시간 의존 measure의 covariance 항과 ADM 평균의 variance 잔차를 분리했다. scoped7/15, 독립 model review 미실행. | G16 |
| BASS BF2 / `10bba48833a3a3ea20b7596b61c90a67003126e5` | opacity·velocity·carrier의 공간 collision correlation, prescribed bath의 에너지 교환을 분리했다. exact bookkeeping이며 closed mean-state solver가 아니다. scoped8/15. | G17 |
| BASS BF3-A / `201231f0918727ae4de6b27bf85c91bdc34ef8fd` | 고정 Bianchi-I 배경의 periodic Fourier-Galerkin 편광 수송 및 별도 characteristic history. 같은 grid의 일치는 continuum accuracy와 다르다. upper BF3 PARTIAL,8/15 유지. | G18 |
| BASS BF3-B / `24db3ea928c476e6cbaa94553307cde773a65832` | **독립 retarded spatial source-memory solve**를 구성. finite Fourier propagator와 연속 attenuation의 투영을 구별한다. full history가 필요하고 nine-state Markov closure가 아니다. | G07,G26 |
| REC background jet / `9378119c483c8163e7b5b3aa1cd8ed89fcba559e` | 동일313 기하 cell의 non-CAMB background jet R1 계약. 계획과 실행 결과를 구별한다. source background의 derivative bound이며 physical H5 M2가 아니다. | G14 |
| REC QSS regularity / `5438f2a082f7ed204603e441866ca63d1e0bf9de` | 실제 저장313×313 QSS matrix의 exact weighted inverse/relative coefficient box에 대한 R1 계약. 비특이 coefficient-domain을 time/state/physical tube로 바꾸지 않는다. | G15 |
| VigilODE polyalgorithm / `384dba091a3d9e1aac0ecddec264958298239253` | exact-rational 이론 보충3lane. fused distinct5-vector 연산수5m→m, 특정 fixture의 dyadic N512→256, causal residual·variable-step transfer. runtime/native test/benchmark 변경은 없음. | G20,G21 |

### REC 복구: 과거 장애와 최신 복구를 구분

G08은03:02UTC recovery 당시의 C10 PARTIAL_DELIVERY 및 원본 bytes 미복구를 보존한 문서다. 이후 G22/G23은 사용자 첨부 원본 SOURCE를 실제 확보하여 **110,654,069 bytes,332members,331 manifest payloads,CRC PASS**를 기록한다. SHA-256은 `94b454c75b51f7c7af38126510cec609f5d7cfb2eb69ca78a491def54b31791c`이다.

Drive에는 원 byte stream의 part00167,108,864bytes와 part00243,545,205bytes, companion64,863bytes의 실제 ACK·별도 크기 readback이 있다. 원 ZIP을 재포장한 것이 아니다. 기존 C5 source45/46blob의 일치와 runner의 후속 PID-domain repair 차이를 따로 기록했고, 실제 실행 runtime6개 파일은 원 절대 경로를 유지하는 lossless line edits로 보존했다. 이 intake는 그 과학 계산이나 재구성을 실행하지 않았다. 원 과학 판정19/20와 성공 capture·18/18 controls는 source-reported history이며 현재 Git C10 IN_PROGRESS를20/20로 바꾸지 않는다.

### REI의 새 실행은 실제 source 검증이나 WU 물리 결속은 아니다

C7는 source commit `634c3046ffccc5d00f1ab7588b5834a6eb8053ad`의3,554,206byte 결과와 기존8,281byte literal packet을 1회 소비했다. 저장 검사45/45, exact decomposition residual0, CAS3zero를 보고하며 independent author review는 NOT_RUN이다. 표시된 caloric endpoint3003.417482286276822K와 prescribed right driver3003.492794789281561K의 차이는−0.07531250300473922K다. 이 차이와 saved-event 재구성 차이−6.297256911088516e−67K를 혼동하지 않는다. 공통 reference volume, gas-owned integrated Q/W, He count·stored free electron의 source 모델 검증이다. actual REI thermal update와 WU physical consumer는 여전히 결속되지 않았다.

### 후속 WU 연구에 재사용할 수 있는 교훈

BASS BF3-B의 source-memory는 forcing의 위치·history와 finite projection을 명시해야 함을 뒷받침하는 별도 사례다. 하지만 그 loss generator `-ik v_q - V`는 complex Fourier 표현이다. 이 source를 WU의 column-Markov full-A l1 nonexpansiveness로 직접 이전할 근거는 없다. BF1의 measure derivative나 BF2의 correlation 항도 실제 WU state/clock을 새로 공급하지 않는다.

BASS QSS와 dual witness는 exact directed arithmetic, 동일 source law/닫힌 cell, 부호 정보를 보존한 reward bound의 구현 사례로 참고할 수 있다. 원 물리 불확실성을 산술 반경으로 대신하거나 독립 작성자 검토가 미완인18/20을 완료로 세지 않는다.

VigilODE polyalgorithm의 causal residual·clock/endpoint budget 분리는 새 convolution 계약의 논리 점검에 참고할 수 있다. 그 operation-count/특정 planning fixture 결과를 WU wall-time·물리 오차 개선으로 채택하지 않는다.

## Git에 없는 최신 V8 백업의 교차대조

백업 조사 agent가 **VIGILODE_V8_MATRIX_BOUNDS_20261028_B_RESULTS.zip** 원본을 실제 확보했다. 이 조사 agent는 그 안의 UNIT_INTAKE, SCIENTIFIC_CONTRACT, PUBLISH_PLAN, STAGES 상태 필드, EXECUTION_SUMMARY를 직접 읽었다. 전체 원본 검증과 provider 식별자는 백업 intake 기록이 권위다. 교차대조는 [V8_BACKUP_GIT_CROSSWALK.json](V8_BACKUP_GIT_CROSSWALK.json)에 있다.

- 원본9,285,519bytes,299members,CRC PASS, SHA-256 `2be53029a19c48e2e68e393d0a0c74626ba9b3632b6fcf90769230ad1f2c4a64`.
- archive workspace이며 자신의 Git commit은 없다. 새 Git mutations0, publication HOLD.
- 원문 target은 REI의 `research/vigilode-v6-return-20261025`, expected SHA `78f7ac5864d5817ceb79b48cb5e298cc30006510`. 이번 census의 실제 target HEAD와 일치한다.
- snapshot은 **15/20(R1–R7,C1–C8)**. Python10pass와 Wolfram25True를 보고하지만 final admission/C9는 pending.
- source는 고정 physical33 metric에서 supplied reduced30 interval matrix family의 operator/logarithmic norm 인증이다. actual model enclosure/owner provenance 검증은 false이며 계약은 WU l1 certificates의 이전을 명시적으로 제외한다.

따라서 Git target 불변으로 새 V8 결과 부재를 추론하지 않는다. 동시에 이 archive 결과를 actual WU model enclosure나 named physical consumer로 승격하지 않는다.

## 자료 보존·한계·다음 입력

SOURCE_RESPONSES는 실제 connector 응답을 보존한다. 성공25회 중23개는 저장 UTF-8 bytes로 Git blob을 정확 재계산해 일치했으며, 두 AGENTS 읽기는1–150행 요청에 대한 반환 텍스트로 남겨 전체 blob byte 동일성은 주장하지 않는다. AGENTS.md404 두 건은 REC native와 BASS Lyα의 path-specific 결과다. 저장소 자체와 실제 연구 leaf 원문은 정상 읽었다. 모든 공개 원문 copy와 hash는 SOURCE_MANIFEST에서 추적한다.

현재 GitHub head census의 완전성과 선택 content 조사의 깊이를 별개로 보고한다. personal conversation·Drive·Dropbox의 범위는 별도 backup/personal-context intake를 따르며 이 문서가 그 조사를 대신하지 않는다. metadata 수집 중 parser/patch/display 문제와 복구는 INTAKE_OPERATION_NOTES에 남겼다. 과학 실패나 전역 접근 실패로 일반화하지 않는다.

R11의 완료 과학·C9·50-file payload·ledger·AGENTS는 바꾸지 않았다. 새 primary/reference/CAS/ODE/scientific import0, 외부 mutation0, 모든 이전 scientific allowance 증가0이다. 이 intake는 후속 계약을 정할 근거이며 새 과학 채택이나 실행 허가는 아니다. 실제 새 HD 배열 또는 WU physical consumer가 이후 들어오면 그 입력 결속을 우선하고, 그렇지 않으면 root가 별도 nonaligned forcing convolution/closed-cell cap 단위의 proof/code/resource 계약을 정할 수 있다.
