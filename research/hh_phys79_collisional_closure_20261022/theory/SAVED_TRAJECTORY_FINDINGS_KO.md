# PHYS79: PHYS78 저장 궤적에 대한 순간 충돌 연산자 진단

## 범위와 핵심 결과

P013·P030의 저장 상태를 그대로 사용한 조건부 순간 연산자 진단이다. source가 허용하는 온도 구간에서 H I CI/PI event ratio는 각각 1.1354623922269576, 1.4819964467172575에 도달하고, CI threshold cooling/기존 PI excess heating은 각각 1.88689969277666, 2.4553164819502027까지 커진다. 이 구간에서 누락된 충돌항을 일률적으로 작은 항으로 취급할 근거는 없다. 보정된 궤적의 변화량은 이 계산으로 정해지지 않는다. 수치 원본은 [SUMMARY.json](../analysis/saved_operator/SUMMARY.json)과 각 case의 NPZ·CSV이다.

**고유 저장 표본은 322개 = 161 × 2, analyzer 후처리 실행은 2회, 새 ODE는 0회이다.** 두 번째 실행은 C9 검토 뒤 dependency가 변경되어 수행했다. 새 입력·새 궤적·추가 표본을 만든 실행으로 세지 않는다. 기존 PHYS78 입력의 SHA256을 확인했고, 원래의 species·온도·UV·proper-time 이력은 변경하지 않았다.

| Case | UV source scale | 저장 표본 | 중성 CI 허용 / 제외 | 저장 T 범위 [K] |
|---|---:|---:|---:|---:|
| P013 | 1 | 161 | 66 / 95 | 275.9795687821955–24036.204970922598 |
| P030 | 2 | 161 | 63 / 98 | 292.7993088821724–25370.66308424773 |

H I·He I·Li I의 CI fit 하한은 1 eV이다. He II·Li II·Li III의 하한은 각각 3·4·5 eV이며, 두 이력의 모든 저장점은 이 세 비중성 row의 source domain 밖이다. 여섯 row 전체가 동시에 허용된 표본은 0개다. 허용되지 않은 rate는 **NaN + false validity mask**이고, 0으로 두거나 잘라내어 fit을 외삽하지 않았다. 기존 PI/RR 비교항은 각 저장점의 실제 UV 평균 에너지와 photon density를 byte-pinned atomic RHS에 넣어 평가했다.

## 저장점 최대값

아래 epoch는 0부터 시작하는 저장 배열 인덱스다. 최대값·z·T는 최종 JSON에 저장된 float 표현을 그대로 옮겼다. 표의 최대값은 source-admitted 저장점 집합 위의 최대값이며 연속시간 최대값의 인증이 아니다.

### CI event / PI·RR event

각 원소 row는 그 row에 해당하는 isotope event를 합한 값이다. PI는 해당 하위 charge의 광이온화, RR은 대응하는 상위 charge의 재결합 event이다.

| Case | Row | 비율 | 최대값 | epoch | z | T [K] |
|---|---|---|---:|---:|---:|---:|
| P013 | H I | CI/PI | 1.1354623922269576 | 73 | 7.642578123396062 | 21801.062505963266 |
| P013 | He I | CI/PI | 0.0007616127959771082 | 75 | 7.434893208142313 | 22807.247245821818 |
| P013 | Li I | CI/PI | 3132.7018826733206 | 70 | 7.9637328012431645 | 20106.3023690665 |
| P013 | H I | CI/RR | 7.5977797129931375 | 72 | 7.748330399251117 | 21259.613483395504 |
| P013 | He I | CI/RR | 0.0024537666236860824 | 74 | 7.5381042107644 | 22317.38265221544 |
| P013 | Li I | CI/RR | 61443.88120731203 | 70 | 7.9637328012431645 | 20106.3023690665 |
| P030 | H I | CI/PI | 1.4819964467172575 | 62 | 8.879701067384955 | 22562.393258403285 |
| P030 | He I | CI/PI | 0.0012853514797079289 | 64 | 8.642287549148117 | 24079.39079223325 |
| P030 | Li I | CI/PI | 3405.2571765752 | 60 | 9.122960208701828 | 20929.819710234966 |
| P030 | H I | CI/RR | 10.999890288214765 | 62 | 8.879701067384955 | 22562.393258403285 |
| P030 | He I | CI/RR | 0.004546449347185938 | 63 | 8.760272465016094 | 23337.32731750298 |
| P030 | Li I | CI/RR | 73034.99430787071 | 60 | 9.122960208701828 | 20929.819710234966 |

### CI threshold cooling / 기존 energy rate

분자는 허용된 중성 CI의 양의 threshold cooling이며, 분모는 각각 기존 PI excess heating 또는 RR kinetic cooling이다. RR binding-energy radiation 전체를 kinetic cooling으로 센 값이 아니다.

| Case | 분모 | 최대값 | epoch | z | T [K] |
|---|---|---:|---:|---:|---:|
| P013 | PI excess heating | 1.88689969277666 | 73 | 7.642578123396062 | 21801.062505963266 |
| P013 | RR kinetic cooling | 62.67473306404041 | 72 | 7.748330399251117 | 21259.613483395504 |
| P030 | PI excess heating | 2.4553164819502027 | 62 | 8.879701067384955 | 22562.393258403285 |
| P030 | RR kinetic cooling | 85.7271630540413 | 61 | 9.000591021485022 | 21758.6634908787 |

## 큰 Li ratio의 절대량

다음은 각 case의 Li I CI/PI 최대점이다. Li I local binding defect 5.392 eV를 사용했으며, Li6·Li7에 같은 defect가 적용된다. 큰 Li ratio는 작은 PI 분모와 미량 Li abundance의 맥락에서 읽어야 한다. 이 표본들에서 Li CI가 전체 CI cooling을 지배한다는 결론은 성립하지 않는다. 계산과 dependency 비교 기록은 [DEPENDENCY_REBUILD_COMPARISON.json](../analysis/saved_operator/DEPENDENCY_REBUILD_COMPARISON.json)에 보존했다.

| Case / epoch | Li CI event [per H/s] | Li PI event [per H/s] | 전체 CI cooling [eV per H/s] | Li cooling / 전체 CI cooling |
|---|---:|---:|---:|---:|
| P013 / 70 | 1.1648528941769267e-22 | 3.7183649699309677e-26 | 1.4793512342756157e-15 | 4.2457035623980876e-07 |
| P030 / 60 | 1.9363978276632797e-22 | 5.686495108163286e-26 | 2.964863460971792e-15 | 3.5215979501930065e-07 |

## D charge exchange

D CX detailed-balance closure는 forward D I + H II → D II + H I에 대해 k_forward/k_reverse = exp(−43 K/T)를 사용한다. 두 case 모두 161점에서 적용 domain 안이다. raw-fit 두 방향의 비율을 이 detailed-balance 비율로 나눈 값의 범위는 P013에서 0.9749921668809408–1.017595849242198, P030에서 0.9749926351110535–1.017595666458352다. 다음은 그 ratio 및 local CX/기존 atomic-event ratio의 저장점 최대값이다.

| Case | 지표 | 최대값 | epoch | z | T [K] |
|---|---|---:|---:|---:|---:|
| P013 | raw-fit ratio / DB ratio | 1.017595849242198 | 81 | 6.841306177545836 | 22966.575589682383 |
| P013 | forward CX / D PI | 31892.30106258753 | 0 | 20.0 | 299.99999999999994 |
| P013 | reverse CX / D RR | 1993131.306524488 | 1 | 19.746146099700773 | 294.8253457264333 |
| P030 | raw-fit ratio / DB ratio | 1.017595666458352 | 72 | 7.748330399251117 | 23205.983775527246 |
| P030 | forward CX / D PI | 31892.30106258753 | 0 | 20.0 | 299.99999999999994 |
| P030 | reverse CX / D RR | 1743828.2627335188 | 1 | 19.746146099700773 | 296.8596340032258 |

초기 D II = 0인 표본에서는 reverse CX/DRR이 0/0이므로 NaN이다. 이 비율은 case마다 160개 유효 표본을 가진다. DB ratio의 최대 절대 부동소수점 잔차는 두 case 모두 2.220446049250313e-16이다. 이 값은 산술적 일치 진단이다. 43 k_B isotope shift는 새 local collision energy ledger에만 적용되었으며, 기존 isotope-blind PI/RR energy ledger와 통합된 자기일관적 이력은 아직 계산하지 않았다.

## 의존성·검증·해석 경계

첫 실행의 collisional.py SHA256은 `6da20f80f8c7097372d1c984c1ba1f8fead6ef36334204566fe0706c7cf60837`, C9 안정화 후 두 번째 실행은 `7fca190029597888692d770f9641c6c325c921b0fb67da927f5f06db75f2f2cd`이다. 첫 실행 source bytes는 [보존본](../analysis/history/pre_C9_stability_patch/source/collisional.py)에 있으며 해당 SHA256을 확인했다. 첫 결과·receipt·preview도 같은 history 아래 보존했다. 두 실행의 event rate, heat, electron, mask, ratio 배열은 정확히 같다. 변경된 binding derivative와 local energy residual 배열의 최대 차이는 1.5777218104420236e-30 eV per H/s이다.

최종 local collision energy residual = 0은 heat와 binding derivative를 같은 event-defect sum으로 정의한 결과다. 독립적 보존 검증으로 세지 않는다. 직접적인 state-dot-product와의 차이 및 기존 PI/RR의 작은 sampled residual 역시 continuum certificate가 아니다. 별도 QA 보조 명령의 잘못된 Li 인덱스 assertion은 결과 작성 전에 중단됐고, [실패 기록](../analysis/history/qa_trace_context_index_failure.json)을 보존한 뒤 named event로 수정했다. analyzer 실행 자체는 두 번 모두 성공했다.

이 결과는 동일 저장 궤적 위의 성분·연산자 분석이다. species-off 인과 실험, 수정된 trajectory, 수렴한 cosmological correction, 전체 thermal closure 또는 production admission으로 읽지 않는다. fit domain 밖의 CI, He/Li CX의 상태별 branching·energy closure, D isotope-shift와 PI/RR의 일관된 연결, recombination→z20 초기 charge contract는 별도 해결이 필요하다. HH_R10=OFF, Production admission NOT_ISSUED를 유지한다.

그림은 [온도와 fit domain](../figures/01_temperature_and_fit_domains.png), [local CI/PI·cooling 비교](../figures/02_instantaneous_CI_PI_RR_comparison.png)이며 각 PDF도 같은 figure에서 생성했다. 최종 PNG 시각 검토 범위는 [VISUAL_REVIEW.json](../figures/VISUAL_REVIEW.json)에 명시했다.
