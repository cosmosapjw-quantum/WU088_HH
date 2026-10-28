# R2 독립 검토 — 실제 공급자 자료와 원 19개 반응의 정수 사상

## 판정

**PASS_SCOPED_SOURCE_REGISTRY_AND_NEW_INTEGER_PROJECTIONS.** 원 그림의 19개 ID와 28개 명시 방향, 실제 공급자 자료 26개 변형, 새 finite number column 24개의 연결을 수용한다. 이 단위의 독립 검토에서 남은 blocking finding은 없다. 물리 반응률·핵 Q·에너지 침적·소비자 결합의 승인은 0이며, 전체 원래 방향의 수치 공급자 자료 회수는 target 6의 정방향 의존성을 남긴다.

검토자는 `/root/authority_survey`이다. 구현 작성자와 별도로 원자료, source-native 숫자와 줄 위치, 원 19개 선언, 조건부 18-family 계약, 실제 빌드 출력과 보존량을 대조했다. 상세 입력·출력 SHA256, 실행 영수증, 수정 이력은 같은 디렉터리의 `C9_FINAL.json`에 고정했다.

실제 primary 검사는 **13/13 그룹 PASS**다. 독립 수용은 첫 실행에서 통과한 9개 그룹과 교정된 공개 자료 메타데이터 그룹을 합친 **10/10 그룹**이다. 전체 10개를 다시 실행한 결과로 표시하지 않는다. 아래의 두 checker 실패와 그 첫 파일·출력을 모두 보존했다.

## 1. 원래 대상과 조건부 모형의 구별

회수한 원 PNG는 1,856,861 bytes, SHA256 `472ba6be633d2b5fc05fc1e0e88f965ff3c0311b0697e3c35c05bbca1629e6f9`이다. 그림 오른쪽의 19개 식을 직접 확인했고, 고정된 `TARGET_NETWORK_19` 전사와 연결했다. 따라서 R1 당시의 그림/원 목록 미회수 관찰은 이전 시점의 기록으로 남고, 현재의 해당 locator 의존성은 해소되었다.

ID 1–3은 전자 PI/RR 방향이다. 나머지 16개 핵·약반응 ID는 조건부 계약의 13개 계열에 대응한다. 이후 계약의 `d_alpha_gamma`, `d_n_gamma`, `n_li6_alpha`, `p_li6_alpha`, `p_li7_alpha`는 별도의 5개 closure다. 조건부 18-family 계약이 원 19개 목록을 대체하지 않는다.

ID (7,13), (8,12), (11,19)는 겹치는 물리 방향을 참조하지만 각각의 사용자 ID를 유지한다. 원 목록의 가역 화살표를 세면 28개 명시 방향이다. 원래 단방향인 12·13·19에 새로 회수한 역방향 source evidence는 별도 필드에 남아 이 28개 의무 수를 늘리지 않는다. Photo ID 4–8·11의 정방향은 광분해이므로 capture 자료는 해당 ID의 역방향으로 연결된다.

근거: `sources/recovered_network/TARGET_NETWORK_19_c9deb93.json`, `REI18_NUCLEAR_NETWORK_CONTRACT_9620e1f.json`, `primordial_target_network.png`, `reviews/PREINTAKE.md`.

## 2. 실제 원문 수치의 검토

| 자료 | 이번에 대조한 내용 | 수용 범위 |
|---|---:|---|
| NACRE-II | 10개 표의 598개 native grid record | 각 $T_9$, adopted/low/high 문자열, 단위, 표/페이지/줄 locator |
| JENDL-5 He3 표 | MT102·MT103의 2개 선택 행 | 개별 에너지 단면적, Maxwell 평균, 공명 적분, fission-spectrum 평균의 구별 |
| NIST NCNR | H1·D·Li6의 3개 total-absorption 행 | 2200 m/s 기준, native 수치와 Li6 괄호 불확실성 |
| Viviani·Dubovichenko·Li | 4개 S-factor source 변형 | 모형·외삽·실험 방법, 단위와 원래 오차 의미 |
| NNDC photonuclear ENDF | MF3 246 knots, MF6 16개 product yield table의 1,777 knots | MAT/MF/MT, 헤더, NR/NP, interpolation 필드, ZAP/LIP/LAW, 원 줄·필드 문자열 |
| Shima·Murata He4 | 4개 채널별 source 변형, 20개 측정값 | 서로 다른 평균 에너지, 통계 오차, 대칭/비대칭 계통 오차와 원 응답 정의 |

독립 검사는 프로젝트의 parser·builder·adapter·compiler를 import하지 않았다. NACRE 표는 원 PDF에서 얻은 고정 텍스트의 실제 해당 페이지를 독립적으로 읽어 좌우 열을 대조했다. Table 6과 8의 59개 행은 그대로 유지되며 빠진 `T9=0.001` 행을 만들지 않았다. 나머지 8개 표는 60개 행이다. ENDF 숫자는 실제 11-character field와 source line을 직접 대조했고, MF6 LAW payload를 끝까지 건너가며 다음 product selector와 section 종료를 확인했다. 표 보간, 두 표의 곱셈, 속도 평균이나 Q 계산은 실행하지 않았다.

NACRE의 관측량은 $N_A\langle\sigma v\rangle$, 단위는 $\mathrm{cm^3\,mol^{-1}\,s^{-1}}$이며 $T_9=T/(10^9\,\mathrm K)$이다. 원 표의 온도 구간과 이전 조건부 100–10000 K 모형을 구분했다. low/high는 평가자가 제시한 범위로 보존되며 공분산·특정 confidence probability를 추가하지 않았다. Source의 $S(0)$ 이름은 보통 0.5–1.0 keV 부근의 값을 가리킨다는 정의도 남는다.

NIST의 total absorption을 특정 부분 반응의 측정값으로 바꾸지 않았다. Viviani의 DD 값은 두 interaction cutoff에서 얻은 이론 범위다. Dubovichenko의 오차는 영에너지와 1 keV 사이 모형 외삽 추정이고, Li의 별도 DDp 값은 THM 실험을 바탕으로 한 외삽이다. DDp의 여러 대안은 서로 더할 활성 계수가 아니다.

NACRE `t_alpha_gamma` 표는 Li7 ground와 first-excited 전이를 inclusive하게 취급한다. 원문 §3.7의 LF 기준 1764–1765행이 그 주석을 직접 뒷받침한다. 이 source 사실은 선언된 ground-coordinate 정수 열에 실제 source branch fraction이나 cascade를 배정하지 않는다.

## 3. 여섯 광분해 정방향의 현재 상태

| 원 ID | 방향 | 실제 자료 관계 | 남은 결합 |
|---:|---|---|---|
| 4 | He4 + γ → He3 + n | Shima·Murata의 named-channel 실험값 | efficiency·acceptance·모형 보정을 포함한 관측량에서 소비자 표현으로의 연결 |
| 5 | He4 + γ → T + p | Shima·Murata의 named-channel 실험값 | 위와 동일하며 두 실험은 별도 대안 |
| 6 | He4 + γ → D + D | 정방향 primary 수치행 미회수 | 직접 실험 수치표/공급자 export가 필요 |
| 7 | He3 + γ → D + p | ENDF MT5 × deuteron MF6 yield의 인수 형태 후보 | 각 native grid·product identity의 실제 결합 |
| 8 | D + γ → p + n | ENDF MF3/MT50의 실제 배타 채널 | 상태·입사 광자 분포·rate normalization·Q/에너지 소비자 |
| 11 | Li7 + γ → He4 + T | ENDF의 inclusive particle/residual yield | 배타 alpha+T branch에 대한 추가 자료 |

He3의 MF1 설명은 deuteron production을 `He3(g,p)D`에 연결한다. 따라서 전체 MT5 단면적과 D yield를 인수 형태로 보존할 근거가 있다. 서로 다른 native 격자 위의 곱은 실행하지 않았다. Li7의 포괄 수율은 특정 최종 쌍의 배타 branch를 정하지 않는다. MF6 수율은 생성물 multiplicity이며 자동으로 합이 1인 branch probability가 아니다.

H2의 QI/QM 문자열 `-2.224600+6` eV는 원 평가의 수치 필드로 남는다. He3·Li7 MT5 헤더의 0 필드는 배타 반응 Q가 아니므로 exclusive Q는 null이다. 실제 원파일에 covariance section이 없다는 관찰은 불확실성이 0이라는 뜻으로 사용하지 않았다.

Target 6의 no-candidate 관찰에서 단면적 0이나 수치 upper limit을 만들지 않았다. 직접 실험 문헌과 EXFOR 접근 결과는 `sources/he4_photon/TARGET6_DEPENDENCY.json`에 있다. 공개 abstract에 필요한 수치가 없고 일부 full-text/interface 접근이 막혔다는 기록은 데이터의 전역적 부재를 입증하지 않는다. 이 의존성은 전체 source coverage를 제한한다.

## 4. He4 관측량에 대한 실제 finding과 교정

초기 He4 packet은 관련 식 번호를 가지고 있었으나 detector response와 모형 의존성을 충분히 명시하지 않았다. 독립 원문 검토에서 다음을 확인하고 metadata-only v2로 닫았다.

Shima Eq.2는 $\epsilon_i(E)\phi(E)$로 가중한 채널 단면적이며 Eq.3의 reaction mean energy는 여기에 $\sigma_i(E)$도 들어간다. Eq.6–7의 source fit 과정도 명시해야 한다. Murata Eq.3은 $\int f_k(E)dE=N_{\gamma,k}$이며, Eq.4는 angular-bin efficiency를 사용한다. Eq.9의 평균 에너지는 fitted differential cross section·선택 acceptance·efficiency를 포함한다. Eq.10–12는 그 검출량을 fitted angular model로 $4\pi$까지 보정한다.

이 정의는 `sources/he4_photon/PROVIDER_ROWS.json`의 `response_and_energy_definition`에 보존되었다. 20개 수치, uncertainty, Q와 units는 이전 packet과 동일하다. Earlier packet과 correction addendum도 남아 있다. 수정된 theory 문서는 일반적인 response-weighted 평균과 소비자 광자 hazard를 구분하고 이 두 실험의 차이를 설명한다.

## 5. 새 24개 정수 열과 기존 계산의 재사용

빌드는 조건부 forward 18개와 명시된 photodisintegration 6개에만 기존 finite compiler를 호출했다. R1의 24개 event/compiled/provider 참조는 저장된 identity로 연결했으며 재컴파일하지 않았다. R1의 125개 결과, 기존 synthetic 249-check, PHYS91 및 이전 REI background 계산을 재실행하지 않았다.

새 정수 좌표는 R1의 n, H1, D, T, He3, He4, Li6, Li7 bare ground label 8개와 `electron_fast` 1개를 그대로 재사용한다. **9개는 재사용한 identity 수이며 새로운 evolved population 수가 아니다.** 실제 source가 inclusive daughter state나 미분해 electronic/isomer state를 갖는 경우 그 의무가 남는다.

독립 계산에서는 product-minus-reactant 정수 계수를 직접 합산하여 24개 모두에서 바리온·전하·전자 렙톤수 잔차 0을 얻었다. 전자 렙톤수는 material의 $\sum ZN-q$와 외부 neutrino sidecar를 함께 센다. Bare beta 열은 $n\to p+e^-+\bar\nu_e$, $T^+\to{}^3\!He^{2+}+e^-+\bar\nu_e$다. 중성 T의 bound spectator electron을 유지하는 R1 projection은 별도 참조로 남는다.

Core compiler는 바리온·전하를, 그 주위의 R1 adapter는 외부 입자를 포함한 전자 렙톤수 원장을 검사한다. 이 차이를 최종 theory 문서에 반영했다. 모든 새 열은 `UNQUALIFIED:ENERGY`, activation false다. Native normalization, 물리 Q, branch fraction, total cascade photon count 및 소비자 ACK도 별도 미결합 상태다.

## 6. 공개 자료와 실패 기록

공개 subset은 원 수치·단위·uncertainty·locator·원본 hash를 유지한다. 일반 재배포 허가를 확인하지 못한 논문 PDF·전체 추출 텍스트·full-paper HTML은 공개 packet에 없다. Viviani PDF는 첫 페이지의 명시적 CC BY 3.0 허가를 확인했으며 저자·논문·journal·DOI·license attribution을 동반한다. NNDC는 회수한 세 archive member의 실제 bytes를 검증했으며 전체 archive checksum을 검증했다는 주장은 없다.

첫 독립 실행의 공개 derivative 그룹은 S0 정의의 의미를 유지한 paraphrase와 source-supported inclusive-state annotation까지 동일 bytes라고 기대해 실패했다. 이 두 경로만 허용하도록 검사 계약을 바로잡았다. 첫 targeted 교정은 `splitlines()`가 form-feed도 줄로 세어 LF 기반 원문 locator와 어긋났다. 새 v2 checker는 newline-only 분할로 한 줄을 교정했다.

| 실행 | 결과와 범위 | CPU / wall |
|---|---|---:|
| `r2_independent01` | 9개 그룹 PASS, 공개 derivative expectation FAIL 보존 | 0.163793 / 0.165395 s |
| `r2_independent_publicfix01` | 공개 derivative 비교 후 LF/form-feed locator FAIL 보존 | 0.042178 / 0.065963 s |
| `r2_independent_publicfix02` | 같은 공개 metadata 그룹 PASS, 163개 assertion | 0.043025 / 0.066323 s |

소스·registry·native grid·24개 열은 이 교정 과정에서 바뀌지 않았고 다시 계산되지 않았다. 세 child의 합계 CPU는 0.248996 s다. source retrieval 및 문서 준비의 미측정 비용은 null로 남으며 0으로 치환하지 않는다. 각 실행의 30 s CPU / 120 s wall / 512 MiB / 1 worker·thread cap은 이전 예산을 이전하거나 초기화하지 않는다.

## 7. 인계 범위

이 C9는 현재 실제 공급자 registry와 선언된 정수 projection의 source/구조적 수용을 제공한다. Target 6의 직접 수치 자료, 상태·가지별 source binding, native 온도/에너지 정의역, 소비자 분포와 normalization, mass convention·Q covariance 및 에너지 분배는 후속 연구 의무다. `HH_R10=OFF`, `production=NOT_ISSUED`, `L4_ready=false`, global physical completion null을 유지한다.

새 source commit·expected-SHA update·source ZIP·Dropbox/Drive ACK·DAG closeout은 root의 별도 operational receipt로 확정한다. 이 검토 이후 필요한 것은 해당 metadata의 범위 일관성 검토이며 완료된 수치 검사의 선택적 반복은 필요하지 않다.
