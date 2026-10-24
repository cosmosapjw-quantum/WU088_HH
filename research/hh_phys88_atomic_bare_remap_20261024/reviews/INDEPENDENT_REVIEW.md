# PHYS88 독립 C9 검토

## 판정

**PASS_SCOPED_CONDITIONAL_BARE_FINITE_WINDOW. 열린 material finding은0개다.** 원전·R6 유도·동결 코드와 실제 primary, 별도 reference, resume, 두 PNG를 검토했다. 마지막 PDF의 실제 byte mismatch를 발견해 최종 파일 작성을 중단했고, 원본 보존·한정 복구 뒤 원래 전체 SHA로 돌아온 것을 확인한 다음 이 판정을 작성했다. 최초부터 모두 PASS였다고 기록하지 않는다.

Scientific identity는 `2712595494bd9d784539d470c4ad0b178314c1ca55d2b0b9a75cb5dc1e6a2774`이며 계약 revision3을 유지했다. Primary RESULT는421150B/SHA `6f3f1e8d6ce07619502dee8683d8322560fe1c13e70ae27f2eb1381969500104`, independent reference는188804B/SHA `a9f596de2a0d4a15c4bae1bf83ef74bbd9565c203b92f00fb850ad46eef257aa`다. 개별 실제 파일과 실패·복구 receipt의 bytes/SHA는 동반 JSON에 결속했다.

## 실제 계산과 판별 범위

Primary는16full+4FD scalar=20적분, source relabel18·새 bare36사건·owner32행을 한 번 수행했다. **482/482 checks PASS이며36개 refusal guard는 그 안에 포함된다.** 저장된 parent153knots/152convexcells positivity witness는 별도로 재사용했고 새 assertions 또는 새 positivity campaign으로 더하지 않았다.

15개 frozen dependency와6개 primary payload의 실제 identity를 확인했다. 저장 raw의 네 성분·여섯 energy 열을 standard-library 산술로 대조했으며 원 source·integrator를 실행하지 않았다.

| 판별량 | 실제 최대값 | 동결 허용값 | 판정 |
|---|---:|---:|---|
| mapping_roundtrip_relative | 4.04219867e-16 | 3e-15 | PASS |
| GL16_vs32_relative | 2.09450827e-16 | 1e-08 | PASS |
| FD_log_slope_absolute | 6.2714039e-08 | 5e-07 | PASS |
| relabel_4component_absolute_eV | 4.71482053e-07 | 3e-06 | PASS |
| bare_4vector_scaled | 1.56522998e-16 | 2e-15 | PASS |
| mass_shell_scaled | 2.79038863e-16 | 3e-15 | PASS |
| mean_energy_closure_absolute_eV | 7.64330724e-10 | 2e-07 | PASS |
| owner_energy_closure_absolute_eV | 7.64430297e-10 | 2e-07 | PASS |
| independent8fields_relative | 4.28870981e-13 | 1e-07 | PASS |

Centered variance는 모두 유한·비음수다. 저장 covariance의 VarKin=VarGamma+VarD+2Cov identity는 descriptive 최악 절대차1.8204105757535505e−12eV²였으며, 이는 독립 low-T variance oracle이나 새 acceptance 기준이 아니다. GL16/32와 reference의 작은 residual을 continuum certificate로 쓰지 않는다.

Reference는 별도 원 ENDF parser로153행·612numeric fields를 대조했고 실제 SciPy1.17.0 kve/adaptive quad에서1216quad calls·25620callbacks를 기록했다. 두 사상의 최고T=10⁸K rate·세 평균,8개 비교가 모두 PASS다. 최대 상대차는4.2887098119610273e−13이며 energy closure는 각각1.964508555829525e−10eV와−1.0913936421275139e−11eV다.612field audit·8reference comparisons·482primary checks는 서로 구분한다. Physical covariance·tails·charge-state 동등성·연속 온도 정확도는 이 근거의 범위가 아니다.

## 과학적 의미

| T[K] | LAB κ[cm³/s] | COM κ[cm³/s] | COM/LAB−1[%] |
|---:|---:|---:|---:|
| 255 | 7.316996339025e-20 | 7.317992836317e-20 | 0.013618939 |
| 10000 | 7.316879732309e-20 | 7.317876258150e-20 | 0.013619547 |
| 1000000 | 7.303198929011e-20 | 7.304197264341e-20 | 0.013669836 |
| 100000000 | 6.331006282451e-20 | 6.332074877187e-20 | 0.016878750 |

차이는 네 점에서136.189–168.788ppm의 조건부 모형 민감도다. 실제 물리 신뢰구간 또는 결과를 포함하는 경계가 아니다. LAB의 bare support는[1e−5,2e7]eV, FIXED_COM_K는[1.0002723992401612e−5,20005462.392183945]eV이며, 두 경우 모두 원 native Es support와 보간을 유지한다.

Nominal Q 차81.63eV는 binding isotope shift0.003700036867eV와 convention-residual difference81.626299963133eV의 합이다. 이를 전자 하나의 energy나 전체 convention residual만 또는 heat로 치환하지 않는다.

Same-source-event 재표기의 signed C0는18fixture에서−45772.06114214077..554.250601648353eV, 최대 spatial component 절댓값은72307.46500185243eV였다. 모든 reservoir는−C이며 새 bare 사건에는 C를 더하지 않는다. 이 값은 유한 fixture 관측이지 일반 bound가 아니고, C는 on-shell electron이나 일정81.63eV 열원이 아니다.

Owner 회계는 thermal h−2, fast1−h, free electron0과 disjoint rest/thermal/fast/photon 열을 유지한다.255K의 h0 caloric coefficient는 약−7.69e−8eV/event로 작지만 음수다.10⁸K에서는 h0가 LAB1031.459301/COM1031.270360eV/event, h1이2347.818645/2347.629928eV/event다. h1은 instantaneous birth 가정이며 실제 fast stopping이 아니다. 고정T readout은 coupled thermal/xe/geometry history의 bound가 아니다.

Root의 saved readout 및 보고서·다음 consumer handoff의 과학 값과 범위도 저장 raw와 대조했다. 외부 repo/branch/backup inventory는 C9에서 다시 전수조사하지 않았다.

## 실제 resume와 그림

Resume은 실제1회·exit0·SKIP, scientific callbacks0·integrations0·rewrites0이다.6개 payload의 before/after bytes/SHA와 현재 파일이 일치한다. Resume CPU는 별도 계측되지 않아0으로 쓰지 않는다.

conditional_maps.png와 conditional_bare_moments.png를 직접 보았다. 제목·단위·축·범례·caption이 읽히고 clipping이 없다. Map ppm, 네T rate와 저장 parent baseline, h0/h1 caloric 값의 역할이 명확하다. Caption은 연결선을 visual guide로, map difference를 uncertainty가 아닌 조건부 비교로, h1을 instantaneous birth로 표시한다. 선이 거의 겹친다고 수치적 동등성을 주장하지 않는다.

**P88-C9-01**에서 conditional_bare_moments.pdf가 원 receipt의21400B/SHA6389368893663f161be17845fa618d8c8e9348d0a10b6eeccddf9876f18dbde7와 달리4928B/SHA3b9af6e6586797b54c0a20f5e72507faecedcac8d19a55cc1b590146f2b602e5로 짧아져 있었다. 다른3파일과 모든 primary/reference identity는 일치했다. Root는 짧은 원본과 최초 receipt를 보존했다. 짧아진 원인은 **NOT_ESTABLISHED**다.

명시적으로 허가된 saved-only artifact child1회는 완성된 후보 PDF를 만들었지만 원본 byte 비교에서 exit1을 반환했고 실패·비용을 보존했다. 실제 후보의 CreationDate timezone metadata 차이가 관측돼 root가 같은 길이의 metadata 치환을 한 번 허가했다. 이 metadata-only 단계에서는 render0·integration0이었다. 전체 원 SHA가 정확히 복구됐고 fsync/closed staging·atomic placement·directory fsync·reopen 기록이 남았다.

독립 최종 확인에서 해당 원 경로는 **21400B·정확한 원 SHA**, `%PDF-1.4` header와 terminal `%%EOF`를 가졌다. 동결26파일도 모두 그대로였다. 원 FIGURE_RECEIPT는 변경하지 않았다. 따라서 현재2PNG+2PDF는 그 최초 receipt와 모두 일치한다. PDF page를 별도 rendering해 시각 검토했다고 주장하지 않는다. 이 복구로 새 source·primary·reference를 실행하지 않았다.

## 실제 자원과 누적 예산

| Child | 결과 | 실제 CPU[s] | 실행 포함 wall[s] |
|---|---|---:|---:|
|Primary|exit0|0.180113|0.181474277000234|
|Independent reference|exit0|0.838988|0.8405935520022467|
|원 saved-only figures|exit0|3.348951|3.35081246199843|
|추가 affected-artifact recovery|exit1, 보존|2.954885|2.958114809000108|

원3child 합은 CPU4.368052s/wall4.372880291000911s다. 추가 실패까지4boundedchildren은 CPU7.322937s/wall7.330995100001019s다. Metadata-only closure CPU0.0005106s/wall0.0013754300016444176s는 별도다. 추가 artifact child를 누락하거나 원3child가 실패했다고 바꾸지 않는다.

원3child 각각 fresh shared lease·available memory≥2GiB·coordinator CPU8·own lease release·exit0을 확인했다. Primary/reference의 actual child affinity는CPU0이며 renderer의CPU0은 검토한 wrapper preexec enforcement 근거다. 별도 renderer affinity probe를 했다고 주장하지 않는다. Worker/thread1, auto-retry0, 타 process 종료0을 유지한다.

과거 비용과 PHYS87 완료 identity를 보존했다. 기존 symbolic4+1에 이번 최초 실패1+명시적 복구1을 더해 lineage7, 새 symbolic allowance0이다. 실제18scalar CAS zeros와 별도 positive-branch proof를19CASzeros로 쓰지 않는다. R6 metric·residual-scale 수정과 최초 실패를 보존하고 budget을 reset하지 않는다. 전체 과거/원격 비용·금액의 미관측값은null이다.

## DAG와 다음 의무

Root는 **MASS_CONVENTION_COVARIANT_RELABELLING_AND_CONDITIONAL_BARE_KERNEL** child를 scoped 완료로 채택할 수 있다. NUCLEAR_ATOMIC_TO_BARE_CAPTURE_REMAP 및 NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER 부모는PARTIAL이다. 다음 단일 노드는 **NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT**다. 실제 bare/electron-state kernel 적합성·covariance·tails·named consumer·stopping은OPEN이다. HH_R10=OFF, production admission NOT_ISSUED다.

이번 검토는 완결된 과학 C9이며, S2/FINAL expected-SHA 게시·중앙 DAG 및 양쪽 최종 전체 복원은 root의 별도 전달 의무다. Upload ACK와 whole-byte restoration을 구분한다. 검토자의 candidate/numerical import·scientific/evaluator 실행·source edit·Git/provider mutation은0이다.
