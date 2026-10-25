# WU 원래 19개 target의 실제 공급자 registry 확장 R2

작성일: 2026-10-25 UTC  
작업 단위: `WU_TARGET19_PROVIDER_BINDING_R2`  
과학적 기준선: WU R1 source commit `18a6804d7cbe4879701e83631f7e908bbb84cef1`

## 1. 이번 단위의 결과와 승인 범위

연결된 기존 백업에서 원래 network PNG와 19개 target 계약을 회수하고, 실제 공급자 원행을 추가한 별도 R2 registry를 만들었다. 원래 19개 ID가 선언한 28개 방향 가운데 27개에 실제 공급자 기록 참조가 연결되었다. 새 공급자 변형은 26개이며, 기존 finite event compiler와 R1 adapter를 재사용해 새 수 보존 열 24개를 만들었다. 새 종을 발명하지 않고 R1의 종 정체성 9개를 그대로 사용했다. [방향별 registry](registry/targets.json), [집계](registry/coverage.json), [컴파일 결과](registry/compiled.json)

최종 독립 판정은 **`PASS_SCOPED_SOURCE_REGISTRY_AND_NEW_INTEGER_PROJECTIONS`**이다. 승인 대상은 공급자 수치·출처·상태의 보존, 원래 target 정체성의 복구, 유한 정수 반응 열의 장부 검사이다. **새 rate 승인, 핵 Q 승인, 계수에서 실제 event flux로의 결속, 물리 consumer 활성화는 모두 0**이다. 모든 새 열의 에너지는 `UNQUALIFIED:ENERGY`로 남는다. 27개 방향에 자료 참조가 있다는 수치를 27개 방향의 물리적 rate 승인으로 읽으면 안 된다. [최종 C9 판정](reviews/C9_FINAL.json)

| 항목 | 이번 R2의 실제 결과 | 집계의 의미 |
|---|---:|---|
| 원래 target ID | 19 | 원본 오른쪽 목록의 ID를 보존 |
| 원래 목록의 방향 | 28 | 가역 9개 × 2방향 + 단방향 10개 |
| 실제 공급자 기록 참조가 있는 방향 | 27 | 포괄적 자료와 응답 가중 측정도 포함하는 출처 연결 수 |
| 실제 수치 공급자가 아직 없는 방향 | 1 | ID 6의 ⁴He + γ → D + D |
| 새 공급자 변형 | 26 | 기존 공급자 packet 19 + NNDC 3 + He-4 측정 변형 4 |
| NACRE II 원래 표 / 격자 행 | 10 / 598 | 원래 온도·단위·adopted/low/high 값 유지 |
| ENDF MF3 격자 점 | 246 | 3개 평가 파일의 실제 수치 |
| ENDF MF6 yield product / 격자 점 | 16 / 1,777 | inclusive yield를 branch 확률로 바꾸지 않음 |
| He-4 실제 측정 채널 행 | 20 | Shima 4점 × 2채널 + Murata 6점 × 2채널 |
| 새 수 보존 열 | 24 | 조건부 family의 정방향 18 + 원래 광분해 방향 6 |
| 재사용 종 / 새로 만든 종 | 9 / 0 | 기존 동위원소·전하·상태 정체성을 사용 |
| 새 rate·Q·IVP 평가 | 0 / 0 / 0 | source intake와 수 장부 작업의 경계 |

공급자 변형 수, 원래 수치 행 수, target 방향 수, compiler 열 수는 서로 다른 집계이다. 이를 더해 새 물리 결과의 수로 보고하지 않는다. 재사용한 조건부 계산 결과도 `PRIMARY_SOURCE_ROW`에 합산하지 않는다. [입력 정체성](registry/inputs.json), [실행 장부](EXECUTION_LEDGER.json)

## 2. 원본 network 복구와 권한 기준

고정 인계서의 기준은 WU commit `34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad`의 [HANDOFF_KO.md](https://github.com/cosmosapjw-quantum/WU088_HH/blob/34dd7d1d018abff8a0a4ebd1d3f3579ac46d2fad/research/program_expansion_20261025/HANDOFF_KO.md)이다. R1에서 남아 있던 원본 그림 locator 공백은 연결된 기존 Drive 백업 `REI_RUN19_FINAL_T_RATE_ACCELERATION_LI_BE_20261020.zip`의 실제 member 회수로 해소했다. ZIP의 크기는 25,344,988 bytes, SHA256은 `6421ead745f3e5d298286e13b9515b7f668dcbb72de11b9f86650021c92b4f62`이다. [원본 회수 영수증](sources/recovered_network/ORIGINAL_NETWORK_RECOVERY.json)

회수한 `primordial_target_network.png`는 **1,856,861 bytes**, SHA256 **`472ba6be633d2b5fc05fc1e0e88f965ff3c0311b0697e3c35c05bbca1629e6f9`**이다. 이 바이트 정체성이 pinned REI 계약과 일치하며, 실제 그림을 열어 오른쪽의 19개 식을 확인했다. `source_network.png`라는 기존 alias도 같은 바이트이다. Target 계약은 REI commit `c9deb933761a8d2593d1176aee028cd423bdbc05`의 `research/atomic_nuclear_ssot_20261017/run19/metals/network/TARGET_NETWORK_19.json`과 일치한다. 그림의 모든 보조 화살표를 새로운 target으로 세지 않았다. 그림만으로 beta 붕괴의 전자 배치나 daughter 이온 상태를 결정하지도 않았다. [원래 target 계약](sources/recovered_network/TARGET_NETWORK_19_c9deb93.json), [회수 분석](sources/recovered_network/ARCHIVE_RECOVERY_REPORT_KO.md)

노드 실행 전 AGENTS, HEAD, 병렬 작업, 이전 백업을 확인한 근거는 `authority/`에 보존했다. 과학적 중앙 기준 pin `641a725ada4be27473069c2c35005a94c2ab0248`과 최신 병렬 진행 관측은 구분한다. 마지막 관측 중앙 HEAD `a5db4bac9dafadae29685bbea3cec7f43ab990b2`에는 88개 노드가 있었고, WU의 14개 노드에는 의미 변화가 없었다. 다른 작업의 노드를 이번 단위에서 수정하지 않았다. 이전 AGENTS의 원본 그림 미회수 문구는 당시의 기록이며, 이번 회수 영수증이 그 입력 공백에 대한 후속 근거이다. [동시 작업 관측](authority/CENTRAL_CONCURRENCY_OBSERVATION.json), [입력 동결 AGENTS](authority/AGENTS_AT_INPUT_FREEZE.md), [단계 기록](WORKFLOW_RECORD.json)

## 3. 원래 19개 ID와 방향별 공급자 연결

아래에서 정방향은 원래 식을 왼쪽에서 오른쪽으로 읽은 방향이다. `↔`가 있는 ID에는 역방향을 별도로 기록했다. 단방향 식의 역방향은 원래 28개 방향에 추가하지 않는다. `D=²H`, `T=³H`, `α=⁴He`이다. 표의 핵 기호는 원본 반응 family를 나타내며, 실제 전하·전자·핵 상태는 뒤의 종 장부와 공급자 메타데이터에서 구분한다. 모든 행의 새 physical rate/Q admission은 false이다. [전체 target 행](registry/targets.json), [중복 family 연결](registry/family_aliases.json)

| ID | 원래 반응 | 정방향 공급자·근거 | 원래 역방향 공급자·근거 / 남은 한계 |
|---:|---|---|---|
| 1 | H I + γ ↔ H II + e⁻ | R1 Verner 광이온화 행 | R1 방사 재결합 행. 원소 단위 공급자의 H/D/T 사영이며 동위원소별 실측으로 승격하지 않음 |
| 2 | He I + γ ↔ He II + e⁻ | R1 Verner 광이온화 행 | R1 He I 재결합 fit a와 b를 별도 대안으로 유지. He-3/He-4 사영과 source 상태를 구분 |
| 3 | He II + γ ↔ He III + e⁻ | R1 Verner 광이온화 행 | R1 재결합 행. ground 광이온화와 total Case A 재결합을 정확한 상태별 역반응으로 동일시하지 않음 |
| 4 | ⁴He + γ ↔ ³He + n | Shima·Murata의 채널별 응답 가중 평균 측정 | JENDL-5 ³He MT102 참고 수치. 측정 평균을 monoenergetic σ(E)로 결속하지 않음 |
| 5 | ⁴He + γ ↔ T + p | Shima·Murata의 채널별 응답 가중 평균 측정 | p+T E1 cluster-model S₀. 전체 multipole 또는 direct 광분해 자료로 일반화하지 않음 |
| 6 | ⁴He + γ ↔ D + D | **실제 direct 수치 공급자 null** | NACRE II Table 3의 D(D,γ)⁴He. 역포획 자료로 정방향 값을 추론하지 않음 |
| 7 | ³He + γ ↔ D + p | NNDC MF3 MT5와 MF6 deuteron yield의 **미평가 factorized candidate** | NACRE II Table 2. R1 cold pD 자료는 운동학 근거이며 rate 공급자가 아님 |
| 8 | D + γ ↔ p + n | NNDC H-2 MF3 MT50의 exclusive native channel | R1 ENDF H-1 MT102 153점, NIST H-1 흡수 참고값, 기존 cold 운동학을 구분 |
| 9 | T → ³He + e⁻ + ν̄ₑ | R1 NUBASE·ENSDF 대안 | 단방향. 중성 T의 spectator 전자와 bare-T 사영을 구분 |
| 10 | n → p + e⁻ + ν̄ₑ | R1 NUBASE·ENSDF 대안 | 단방향. half-life·mean lifetime·불확실성의 원래 의미를 보존 |
| 11 | ⁷Li + γ ↔ ⁴He + T | NNDC Li-7 MT5와 MF6의 **inclusive 자료** | NACRE II Table 8. 역포획의 Li-7 ground+first-excited 포함을 ground-only branch로 바꾸지 않음 |
| 12 | p(n,γ)D | ID 8 역방향과 같은 family: R1 MT102, NIST H-1 흡수 참고값 | 원래 단방향 ID 유지. ID 8과 별개의 물리 계수로 중복 활성화하지 않음 |
| 13 | D(p,γ)³He | ID 7 역방향과 같은 NACRE II Table 2 | 원래 단방향 ID 유지. cold pD Q 근거로 rate 공백을 닫지 않음 |
| 14 | D(D,p)T | NACRE II Table 5, Viviani S₀, Li THM S₀의 별도 대안 | 단방향. 방법·불확실성이 다른 값을 평균하거나 기본 공급자로 자동 선택하지 않음 |
| 15 | D(D,n)³He | NACRE II Table 4, Viviani S₀의 별도 대안 | 단방향. 각 모델과 평가의 원래 불확실성 유지 |
| 16 | T(D,n)⁴He | NACRE II Table 7 | 단방향. 원래 T₉ grid와 저온 조건부 모델의 정의역이 다름 |
| 17 | ³He(D,p)⁴He | NACRE II Table 9 | 단방향. 계수·에너지·상태의 consumer 결속은 미승인 |
| 18 | ³He(n,p)T | JENDL-5 MT103 참고 수치 | 단방향. 열중성자 점과 spectrum-averaged 항목을 동일한 에너지 격자로 취급하지 않음 |
| 19 | T(α,γ)⁷Li | ID 11 역방향과 같은 NACRE II Table 8 | 원래 단방향 ID 유지. ground/first-excited의 개별 branch 비율은 미제공 |

ID 쌍 `(7,13)`, `(8,12)`, `(11,19)`는 출처가 겹쳐도 원래 ID를 지우지 않았다. 같은 family에 연결된 표현이라는 사실을 보존한다. 조건부 18-family 계약은 이 목록의 핵·약반응 family 13개와 추가 closure 5개로 이루어진다. 추가 closure는 `d_alpha_gamma`, `p_li6_alpha`, `n_li6_alpha`, `p_li7_alpha`, `d_n_gamma`이며, 원래 19개 목록의 새 ID로 세지 않았다. [조건부 모델 목록](registry/conditional_models.json)

## 4. 실제 공급자 수치와 적용 범위

### 4.1 19개 기본 공급자 변형

기본 packet은 NACRE II 10개, JENDL-5 2개, NIST 3개, Viviani 2개, pT model 1개, Li THM 1개로 구성된다. 모든 레코드는 원래 숫자 문자열, 단위, support, 불확실성, URL, 원본 SHA, 행·표 locator를 보존한다. 실제 공급자라는 분류에는 실험, 평가, 이론 모델이 각각 포함되며, 이 방법론의 차이는 `source_kind`와 원행 메타데이터에 남아 있다. [공개 기본 packet](sources/primary/PROVIDER_ROWS.json), [전체 공급자 registry](registry/primary_providers.json)

| 공급자 | 실제 복구 내용 | 해석상 유지한 경계 |
|---|---|---|
| [NACRE II, Xu et al.](https://arxiv.org/abs/1310.7099), [DOI](https://doi.org/10.1016/j.nuclphysa.2013.09.007) | Tables 2–9, 13, 15의 598개 온도 행과 source S₀·Q | `N_A〈σv〉`는 cm³ mol⁻¹ s⁻¹, 온도는 T₉. adopted/low/high는 평가 범위이며 covariance나 새 신뢰확률이 아님 |
| [JENDL-5 He-3 표](https://wwwndc.jaea.go.jp/jendl/j5/elm/Table/z002/T3.html) | MT102와 MT103의 reference 값 | 0.0253 eV에서 각각 54.02 μb와 5.328 kb. 처리 온도 300 K와 입사 중성자 에너지를 구분 |
| [NIST NCNR 표](https://ncnr.nist.gov/resources/n-lengths/list.html) | 2,200 m/s에서 H-1 0.3326 b, D 0.000519 b, Li-6 `940.(4.)` b의 absorption 값 | **총 흡수** 값을 특정 partial channel로 자동 배정하지 않음. 특히 Li-6의 지배적 nα channel과 total absorption의 등치를 승인하지 않음 |
| [Viviani 원문](https://inspirehep.net/files/fc3a3fe08ab5d1beaa365ec51e2c7565), [DOI](https://doi.org/10.1088/1742-6596/2586/1/012076) | DDp 50.8±1.9, DDn 51.0±1.4 keV b | 이론 계산의 cutoff 변화에 관련된 오차이며 실측 신뢰구간으로 바꾸지 않음 |
| [Dubovichenko pT 원문](https://arxiv.org/pdf/1811.04779), [DOI](https://doi.org/10.1142/S0218301319300042) | E1 model S₀ `0.95(5)` eV b와 keV 부근의 support | 모델의 multipole·전이 선택을 전체 반응의 정확한 branch 승인으로 확장하지 않음 |
| [Li et al. THM](https://arxiv.org/abs/1503.08672), [DOI](https://doi.org/10.1103/PhysRevC.92.025805) | DDp bare S₀ 56.7±2 keV b | THM 추출값을 별도 대안으로 유지. 실험실 screening과 plasma 환경을 자동 동일시하지 않음 |

NACRE II의 여덟 표는 T₉=0.001부터, Dα 및 Tα 표는 T₉=0.002부터 시작하며 상한은 T₉=10이다. 따라서 표의 낮은 끝도 각각 10⁶ K 또는 2×10⁶ K이다. 기존 REI 조건부 모델의 100–10,000 K에 이 표가 직접 수치 support를 제공한다고 주장하지 않았다. 보간·외삽·새 적분·Avogadro 인자 변환을 실행하지 않았다. S₀ 요약값도 원 논문의 저에너지 모델 요약으로 보존했으며, 원하는 저온 전 구간의 직접 실측으로 취급하지 않았다. [공급자 원행](sources/primary/PROVIDER_ROWS.json), [source observable 해설](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md)

NACRE II가 인쇄한 Q는 MeV 단위 원자료로 유지했다. 예를 들어 pD의 +5.493, DDγ의 +23.847, Tα의 +2.467은 source field이며, R2가 새 질량표로 계산하거나 전자 결합·daughter 상태까지 승인한 값이 아니다. T(α,γ)⁷Li 공급자는 ground와 first-excited 상태를 포함하므로, 그 합을 ground-only 수 장부 열의 경험적 branch 값으로 귀속시키지 않았다. 각 branch fraction은 미정 상태로 남는다. [상태·가지·Q의 명시적 경계](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md)

### 4.2 NNDC의 실제 photonuclear 원파일 3개

IAEA PD2019의 git-annex pointer와 공개 archive의 403/error 1010 응답은 실제 단면적 행으로 세지 않았다. 이후 연결된 공식 [NNDC ENDF release](https://www.nndc.bnl.gov/endf-releases/?sublibrary=gammas)의 [ENDF/B-VIII.1 photonuclear archive](https://www.nndc.bnl.gov/endf-releases/releases/B-VIII.1/gammas/gammas-version.VIII.1.tar.gz)에서 필요한 실제 member를 회수했다. 이 회수는 archive stream의 일부 member를 읽은 것이므로 전체 archive checksum을 검증했다고 주장하지 않는다. 각 회수 파일의 바이트 수와 SHA256은 별도 영수증에 고정했다. [H-2 회수](sources/photon_native/NNDC_H2_RECOVERY.json), [He-3/Li-7 회수](sources/photon_native/NNDC_HE3_LI7_RECOVERY.json), [앞선 접근 결과](sources/photon_native/RECOVERY_RECEIPTS.json)

| 핵종·native channel | 실제 자료와 원래 범주 | Target 결속 |
|---|---|---|
| H-2, MAT128, MF3/MT50 | exclusive native channel; 원파일 10,336 bytes | ID 8 정방향의 직접 source channel. 계수의 runtime 활성화는 false |
| He-3, MAT225, MF3/MT5 및 MF6 | deuteron production을 이용할 수 있는 factorized candidate; 원파일 121,904 bytes | ID 7 정방향. MF3 단면적 × MF6 yield는 아직 계산하지 않음 |
| Li-7, MAT328, MF3/MT5 및 MF6 | total absorption와 inclusive product yield; 원파일 2,650,804 bytes | ID 11 정방향의 family 근거. exclusive α+T event ownership은 미확정 |

전체 native 자료는 MF3 246점, MF6 product 16개 및 yield 격자 1,777점이다. 원래 ENDF 숫자 표현, interpolation 구간, ZAP/LIP/LAW와 support를 유지했다. MF6 yield는 생성 수율 또는 multiplicity이므로 합이 1인 branch probability로 재해석하지 않았다. Li-7의 triton 또는 alpha 생성량만으로 모든 생성이 독점적인 α+T 반응에서 나왔다고 결론 내리지 않았다. [NNDC 공급자 packet](sources/photon_native/PROVIDER_ROWS.json), [native 파싱 영수증](sources/photon_native/NATIVE_PARSE_RECEIPT.json)

H-2 MF3/MT50의 source Q 표기는 `-2.224600+6` eV이며, 이를 원문 정밀도로 유지했다. He-3와 Li-7의 MT5에 있는 0 필드는 exclusive channel의 Q=0을 뜻하지 않으므로 해당 exclusive Q는 null이다. 회수한 파일에 covariance section이 없어 수치 불확실성은 null로 기록했다. 이는 불확실성 0이라는 뜻이 아니다. [원래 Q·uncertainty 필드](sources/photon_native/PROVIDER_ROWS.json)

### 4.3 He-4의 두 실험: 4개 변형, 실제 채널 측정 20개

[Shima et al. 2005](https://arxiv.org/abs/nucl-ex/0509017)의 Table II와 [Murata et al. 2023](https://arxiv.org/abs/2307.01474)의 Table II에서 γn과 γp 채널을 각각 추출했다. 두 논문은 각각 [PRC 72, 044004](https://doi.org/10.1103/PhysRevC.72.044004), [PRC 107, 064317](https://doi.org/10.1103/PhysRevC.107.064317)이다. 같은 반응명이어도 빔, 응답, 각도 수용도, 추정 절차가 다르므로 두 자료를 평균하거나 하나로 합치지 않았다. 네 provider는 각각 inactive alternative이다. [He-4 공개 packet](sources/he4_photon/PROVIDER_ROWS.json)

Shima의 실제 숫자는 아래와 같다. 에너지는 MeV, 단면적은 mb이며 `±stat; ±sys`를 분리했다. 이것은 source가 보고한 응답 가중 평균이며 해당 평균 에너지의 monoenergetic 단면적을 새로 결정한 값이 아니다.

| 빔 Emax | 보고 평균 에너지 | ⁴He(γ,n)³He: σ ±stat; ±sys | ⁴He(γ,p)T: σ ±stat; ±sys |
|---:|---:|---|---|
| 22.3 | 21.8 | 0.10 ±0.02; ±0.006 | 0.19 ±0.02; ±0.01 |
| 25 | 24.3 | 0.63 ±0.05; ±0.03 | 0.71 ±0.05; ±0.03 |
| 28 | 26.5 | 0.80 ±0.06; ±0.02 | 0.89 ±0.06; ±0.02 |
| 32 | 29.8 | 1.35 ±0.08; ±0.03 | 1.39 ±0.08; ±0.03 |

Murata에서는 채널별 보고 평균 에너지도 다르다. 비대칭 systematic 오차의 두 방향을 보존했으며 stat과 합성하지 않았다.

| 빔 Emax | γn 평균 에너지 | γn σ ±stat; +sys/−sys | γp 평균 에너지 | γp σ ±stat; +sys/−sys |
|---:|---:|---|---:|---|
| 23.0 | 22.5 | 1.15 ±0.08; +0.13/−0.13 | 22.5 | 1.25 ±0.08; +0.56/−0.40 |
| 24.0 | 23.5 | 1.31 ±0.10; +0.14/−0.15 | 23.3 | 1.41 ±0.07; +0.28/−0.28 |
| 25.0 | 24.5 | 1.66 ±0.12; +0.18/−0.18 | 24.3 | 1.64 ±0.08; +0.25/−0.22 |
| 27.0 | 26.5 | 2.26 ±0.25; +0.25/−0.24 | 25.7 | 1.93 ±0.13; +0.34/−0.42 |
| 28.0 | 27.5 | 1.94 ±0.19; +0.21/−0.24 | 26.5 | 1.59 ±0.09; +0.63/−0.21 |
| 30.0 | 29.4 | 1.26 ±0.11; +0.16/−0.19 | 28.7 | 1.67 ±0.05; +0.19/−0.23 |

두 표의 수치·단위·오차·Q는 source correction 전후 동일하다. 독립 검토에서 보완한 것은 **관측량의 정의**이다. Shima Eq. 2는 검출 효율 ε와 빔 spectrum φ를 함께 가중한다.

\[
\langle\sigma_i\rangle
=\frac{\int \epsilon_i(E)\,\sigma_i(E)\,\phi(E)\,dE}
       {\int \epsilon_i(E)\,\phi(E)\,dE}.
\]

그 논문의 Eq. 3 보고 에너지는 분자와 분모에 σ까지 들어가는 반응 가중 평균이다.

\[
\langle E\rangle_i
=\frac{\int E\,\epsilon_i(E)\,\sigma_i(E)\,\phi(E)\,dE}
       {\int \epsilon_i(E)\,\sigma_i(E)\,\phi(E)\,dE}.
\]

Murata Eq. 3의 빔 함수는 `∫fₖ(E)dE=Nγ,k`이므로 단위 적분이 1인 확률밀도로 바꾸지 않았다. Eq. 4에는 각도 bin의 efficiency가 들어간다. Eq. 9의 보고 평균 에너지는 모델 differential cross section, angular acceptance, efficiency 및 빔 함수로 가중되며, Eqs. 10–12의 총 단면적에는 source angular model에 의존하는 4π 보정이 들어간다. 따라서 이 값들을 일반적인 빔 평균이라는 한 문장으로 축약하거나 consumer의 광자 spectrum에 바로 적용할 수 없다. [응답 정의 addendum](sources/he4_photon/RESPONSE_DEFINITION_ADDENDUM.json), [관측량·가지 해설](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md)

네 공급자의 `source_coverage`는 `EXCLUSIVE_SPECTRUM_AVERAGED_MEASUREMENT`, `source_is_named_exclusive_channel=true`, `exclusive_channel_binding=false`이다. γn·γp라는 관측 채널의 이름은 명확하지만, consumer의 단색 단면적·정확한 branch·runtime hazard로의 결속은 별도라는 뜻이다. 공동 covariance와 신뢰확률은 미제공으로 남겼다. Shima Table I의 γp Q=−19.81 MeV, γn Q=−20.58 MeV도 원자료 필드로만 보존했다. [수치·support·Q 필드](sources/he4_photon/PROVIDER_ROWS.json)

## 5. 동위원소·isomer·전하·상태와 finite event compiler

이번 새 24개 열은 이미 승인 범위가 고정된 `rei_chem_ledger_20261025/chem_ledger.py`와 R1 adapter를 사용했다. compiler SHA256은 `60a502895266b6feb96964abc4b24db61c2faed2344db0f7d12f16bb47ed62af`이다. 기존 249-check 결과를 다시 실행하지 않았으며, 그 합성 정수 장부 승인을 실측 rate·핵 Q 승인으로 확대하지 않았다. [재사용 장부](REUSED_CALCULATIONS.json), [수 사영 계약](theory/NUMBER_PROJECTION_CONTRACT.md)

새 R2 열에서 사용하는 종은 다음과 같다. `ground`와 bare 상태는 이번 수 사영의 명시적 좌표 선택이다. 공급자가 미분해한 상태나 inclusive branch를 이 선택으로 경험적으로 확정하지 않는다.

| 종 | Z | A | isomer 좌표 | 전하 q | 전자·물질 상태 |
|---|---:|---:|---|---:|---|
| p | 1 | 1 | ground | +1 | bare nucleus |
| D | 1 | 2 | ground | +1 | bare nucleus |
| T | 1 | 3 | ground | +1 | bare nucleus |
| ³He | 2 | 3 | ground | +2 | bare nucleus |
| ⁴He | 2 | 4 | ground | +2 | bare nucleus |
| ⁶Li | 3 | 6 | ground | +3 | bare nucleus |
| ⁷Li | 3 | 7 | ground | +3 | bare nucleus |
| n | 0 | 1 | ground | 0 | 기존 neutron 물질 항 |
| e⁻ | 해당 없음 | 해당 없음 | 해당 없음 | −1 | 기존 `electron_fast` 자유전자 항 |

핵 변환의 수 사영과 원자 전자 상태를 분리했다. bare T 사영은 `T⁺ → ³He²⁺ + e⁻ + ν̄ₑ`이며, R1의 중성 T source는 결합전자 하나를 가진 daughter He-3⁺와 방출 자유전자를 포함하는 별도 상태 장부를 갖는다. 중성 원자 질량 차의 Q를 bare 붕괴 Q로 그대로 승인하지 않았다. neutron beta의 `n → p + e⁻ + ν̄ₑ`에도 antineutrino를 외부 lepton 장부에 명시했다. `electron_fast`는 수 장부의 전자 운반 항이며, 에너지 분포·감속·열 침적 모델의 승인이 아니다. [종 registry](registry/species.json), [event registry](registry/events.json)

24개 열에서 baryon 수, 전하, electron-lepton 장부의 잔차는 모두 정확히 0이다. core compiler는 baryon과 charge를 검사하고, electron-lepton 보존은 R1 adapter의 외부 lepton 장부가 검사한다. photon은 선언된 schematic token이며 total cascade photon 수나 에너지 payload를 확정하지 않는다. `ν=products−reactants`인 정수 반응 열과 실제 계수의 정규화는 분리되어 있다. 같은 D 두 개가 반응하는 경우의 event flux 대칭 인자와 D 감소 stoichiometry −2도 서로 다른 항이다. 이 단위에서는 실제 event flux를 평가하지 않았다. [compiler 출력](registry/compiled.json), [source와 event flux의 구분](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md)

원자·분자·음이온의 기존 R1 범위는 그대로 재사용했다. R1의 원소 단위 source isotope-unspecified 표기, He I RR a/b 대안, total RR cascade 수 미정, 분자 isotopologue 후보, HD para/ortho catalyst, UMIST 정의역 공백을 이번 핵 source 연결로 해소했다고 주장하지 않는다. NUBASE 전체 5,843행과 configured 8개 nuclide/isomer 행도 서로 다른 집계이다. R2는 이 source/state 구분을 덮어쓰지 않는다. [R1 결과](../provider_registry_20261025/registry/coverage.json), [R1 재사용 정체성](registry/reused_r1_evidence.json)

## 6. 완료 계산 재사용과 예산

R1의 완료 결과는 **102개 공급자 변형, 125개 열, 92개 종·상태 정체성**, primary 20개 검토군 및 독립 448개 검사이다. R2는 R1의 core JSON 출력 바이트를 보존하고 event 근거 24개를 참조했다. 기존 125개 열의 재컴파일과 R1 전체 검사의 재실행은 각각 0이다. 이번 24개 새 열을 이전 물리 계산의 재수행으로 기록하지 않았다. [재사용 파일 hash 장부](REUSED_CALCULATIONS.json)

REI commit `9620e1fcc4bdda76e0311206f614234926600381`의 완료된 조건부 18-family 계산에서 **82개 저장 background**와 log-rate table, energy ledger, run receipt, summary를 원래 바이트로 회수했다. 모드는 `instantaneously_thermalized_all_bare_nuclei_passive_reservoir_sensitivity`, 역사적 온도 범위는 100–10,000 K이다. 이 결과는 `REUSED_CONDITIONAL_MODEL_OUTPUT`으로 유지한다. 과거의 제한된 `PASS_SCOPED` 역시 그 all-bare·instant-thermal·passive-reservoir 모델에만 적용되며, 새 empirical supplier의 승인이 아니다. [회수 근거](sources/primary/REUSED_OUTPUT_RETRIEVAL.json), [저장 summary](sources/primary/raw_reused/NUCLEAR_NETWORK_SUMMARY.json), [재사용 범위](REUSED_CALCULATIONS.json)

완료 계산의 log-rate table SHA256은 `9b557ccf7f16b2fc20a1af618a486e2795252f2017df28c99f74aec1a00eb88b`, energy ledger SHA256은 `3b291277fa942cd6fb0c246035f4c2f393a8040bebf2dd21a8812bab1eccf049`이다. 새 network sweep과 background IVP 재실행은 0이다. 기존 선택 외부광 5–60 eV에서 사용한 photo-zero 조건은 그 조건부 spectrum의 모델 선택으로 유지했으며, γn·γp·γdd 등을 모든 에너지에서 물리적 0으로 선언하는 근거로 사용하지 않았다. [조건부 출력](sources/primary/raw_reused/NUCLEAR_NETWORK_LOG_RATE_TABLE.npz), [기존 energy ledger](sources/primary/raw_reused/NUCLEAR_NETWORK_ENERGY_LEDGER.json)

PHYS91 primary, reference, Wolfram의 남은 예산은 모두 **0**이며 변경·이체·재설정하지 않았다. PHYS91의 `MT102_B1=OPEN`도 그대로이다. 전체 과거 CPU, 금액, global remaining은 **null**로 남긴다. source 다운로드·준비·review wrapper의 미측정 비용을 0으로 쓰지 않는다. [실행 장부](EXECUTION_LEDGER.json), [PHYS91 재사용 경계](REUSED_CALCULATIONS.json)

현재 실행 장부가 계측한 서로 다른 8개 child의 합계는 CPU **0.737753 s**, wall **0.861847 s**이다. 이 수에는 보존된 실패 checker 2회가 포함된다. 이는 해당 child들의 비용 합계이며 전체 세션이나 과거 연구의 총비용이 아니다. 이번 실행의 제한은 child당 CPU 30 s, wall 120 s, memory 512 MiB, worker/thread 각 1이다. 모든 과거 249/R1/PHYS91/REI 완료 science 재실행은 0이며, source intake와 변경 입력에 필요한 가벼운 구현 검증만 수행했다. [계측 범위와 미측정 비용](EXECUTION_LEDGER.json)

## 7. 검증, 독립 검토, 보존한 실패

첫 build는 성공했고 primary 검증은 **13/13 검토군 PASS_SCOPED**였다. 공급자 packet SHA, 원본 target ID와 방향, source payload의 locator, 실제 수치의 전사, state/branch 구분, 정수 장부, 활성화 금지 및 기존 출력 재사용을 확인했다. [build01 영수증](raw/build01/RECEIPT.json), [primary 결과](raw/PRIMARY_RESULTS.json), [primary 실행 영수증](raw/primary01/RECEIPT.json)

최종 독립 10/10은 **처음 통과한 9개 검토군과 수정 후 표적 검토 1개를 합성한 결과**이다. 전체 독립 suite를 다시 실행한 10/10이라고 표기하지 않는다. 최초 독립 실행은 공개 derivative의 의미 보존 문구 10개와 source가 뒷받침하는 inclusive daughter-state 설명 하나를 checker가 너무 엄격하게 거부해 9/10으로 실패했다. 숫자·단위·원본 출처를 변경해 통과시킨 것이 아니며, 허용되는 메타데이터 경로를 특정한 수정 checker를 별도로 만들었다. [최초 독립 결과](reviews/INDEPENDENT_R2_RESULTS.json), [최종 C9의 실패 분류](reviews/C9_FINAL.json)

첫 표적 수정 실행도 PDF 텍스트의 form-feed를 `splitlines()`가 줄 경계로 세면서 LF 기반 source locator와 충돌해 실패했다. 이 실행과 checker를 보존하고, LF 기준을 쓰는 후속 표적 checker에서 **163개 assertion을 통과**했다. 최종 C9가 승인하는 것은 원래 9개 통과군과 이 수정된 한 군이다. 두 실패 raw 디렉터리를 삭제하거나 성공 영수증으로 덮어쓰지 않았다. [표적 수정 결과](reviews/PUBLIC_DERIVATIVE_CORRECTION_RESULTS.json), [첫 독립 실행](raw/r2_independent01/RECEIPT.json), [표적 실패](raw/r2_independent_publicfix01/RECEIPT.json), [표적 성공](raw/r2_independent_publicfix02/RECEIPT.json)

별도로 He-4 응답 정의의 누락은 실제 source 의미 보완이었다. 효율·단면적·각도 acceptance·4π 모델 보정을 명시한 additive packet을 만들고 앞선 frozen packet을 보존했다. 20개 측정값과 오차·Q는 바꾸지 않았다. 독립 검토는 이 source 의미 수정과 공개 숫자 derivative의 검증 수정도 구분한다. [He-4 addendum](sources/he4_photon/RESPONSE_DEFINITION_ADDENDUM.json), [최종 C9](reviews/C9_FINAL.json)

## 8. 남은 입력 의존성과 후속 승인 요건

### 8.1 ID 6: ⁴He(γ,dd)의 실제 수치 공급자

이 방향은 `INPUT_DEPENDENCY_UNRESOLVED_AFTER_BOUNDED_DIRECT_SOURCE_CHECK`이다. Shima Sec. III.A(iii)의 후보 사건 부재 서술에는 여기서 사용할 수 있는 confidence·exposure를 갖춘 정량 upper limit가 없으므로, 단면적 0이나 임의의 upper limit를 부여하지 않았다. 약 29 MeV의 3.2 μb라는 이차 인용도 primary measurement로 가져오지 않았다. ref. 37을 따라간 검토·이론 및 inverse capture 문헌으로 direct γdd 수치를 만들어내지 않았다. [Target 6의 구체적 의존성](sources/he4_photon/TARGET6_DEPENDENCY.json)

직접 실험인 [Rice et al., PRC 61, 064612](https://journals.aps.org/prc/abstract/10.1103/PhysRevC.61.064612)은 확인했지만, 접근 가능한 abstract에는 150–250 MeV의 두 photon-energy bin과 6개 각도라는 실험 메타데이터만 있고 실제 단면적 표가 없었다. full text는 권한이 필요한 상태였다. 공식 EXFOR landing page는 열렸으나 연결된 form script가 403, Hokkaido interface가 503을 반환해 entry 수치 행을 회수하지 못했다. 이 결과는 접근·입력 공백의 증거이며, 세계적으로 자료가 없다는 주장이나 strong no-go가 아니다. [EXFOR 접근 영수증](sources/he4_photon/EXFOR_INTERFACE_RECEIPT.json), [script 응답](sources/he4_photon/EXFOR_SCRIPT_RECEIPT.json)

다음 입력은 정확한 primary γdd 수치 표 또는 정식 provider export이다. 단위, 에너지·각도 평균 범위, uncertainty, branch/state와 원문 locator가 함께 필요하다. 이번 단위의 figure digitization과 inverse-rate 추론은 각각 0이다. [다음 source intake](NEXT_SOURCE_INTAKE_KO.md)

### 8.2 source reference 이후의 runtime 결속

직접 광분해 여섯 방향 가운데 ID 8만 exclusive native channel source가 있다. ID 4·5는 응답 가중 평균 측정, ID 7은 미평가 factorization 후보, ID 11은 inclusive source, ID 6은 실제 수치 공급자 공백이다. 따라서 exclusive source 결속의 남은 의무는 ID 4·5·6·7·11에 있다. ID 8도 실제 consumer의 flux·energy ledger에 활성화되지는 않았다. [방향별 승인 필드](registry/targets.json), [coverage](registry/coverage.json)

후속 물리 승인은 소비할 photon/particle spectrum, 온도, bare/atomic 상태, branch ownership, coefficient 단위와 event normalization, Q의 원자·핵 질량 및 결합에너지 관례, 불확실성 전파를 명시해야 한다. He-4의 source beam/response 가중치를 consumer spectrum으로 옮길 때의 정보도 별도 입력이다. source 평균 하나와 보고 평균 에너지 하나만으로 임의의 spectrum에 대한 hazard를 유일하게 정할 수 있다는 가정을 두지 않았다. 필요한 자료·계산·검증은 후속 계약에서 범위를 정하며, 이미 소진된 예산을 되살리지 않는다. [관측량과 consumer의 구분](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md), [후속 입력 계약](NEXT_SOURCE_INTAKE_KO.md)

현재도 `HH_R10=OFF`, `production=NOT_ISSUED`, `L4_ready=false`, 전체 물리 완료 상태는 null이다. source registry의 이번 제한된 완료를 전체 연구 프로그램의 물리 완료로 발표하지 않는다. [최종 독립 판정](reviews/C9_FINAL.json)

## 9. 공개 자료 범위와 게시·백업 상태

공개 packet에는 수치 사실, 구조화한 불확실성·support, 필요한 식의 정의, 원본 URL·SHA·locator를 넣었다. 전체 원문 PDF·HTML의 공개 재배포 허가를 확인하지 못한 경우에는 전체 본문을 source ZIP에 넣지 않는다. 명시적 CC BY 3.0을 확인한 Viviani 자료는 attribution과 함께 취급하고, 나머지 논문의 전체 본문 및 장문의 원문 설명은 공개 derivative에서 제외했다. 숫자·단위·원본 정체성은 유지했으며, 원문이 공개 packet에 들어 있지 않다는 사실도 명시한다. [재배포 범위](sources/primary/SOURCE_REDISTRIBUTION.json), [출처 고지](sources/primary/THIRD_PARTY_NOTICES.md), [공개 subset manifest](sources/primary/PUBLICATION_SUBSET_MANIFEST.json)

본 보고서 작성 시점에는 구현 검증과 C9 독립 검토가 끝났으며, **R2 source 게시 및 새 Dropbox/Drive 이중 백업은 진행 중**이다. 따라서 새 source commit, ZIP SHA, cloud readback 완료를 이 문서에서 미리 선언하지 않는다. 기존 R1 source ZIP과 양쪽 readback 증거는 [R1 최종 백업 확인](../provider_registry_20261025/delivery/FINAL_BACKUP_ACK.json)에 남아 있다. R2의 실제 게시 commit, expected-SHA non-force 결과, source ZIP hash, 양쪽 다운로드 재검증 및 DAG 반영 상태는 게시 후 추가되는 이 leaf의 `delivery/` 영수증과 root가 붙이는 실제 전달 절을 기준으로 확인해야 한다. 사용자의 명시적 게시·백업·자동 실행 권한은 유지되며 새 허가 요청으로 대기하지 않는다. [현재 실행·전달 장부](EXECUTION_LEDGER.json), [workflow 단계](WORKFLOW_RECORD.json)

## 10. 근거 파일 안내

| 확인할 사항 | 권위 근거 |
|---|---|
| 원본 19-ID 및 실제 PNG 회수 | [ORIGINAL_NETWORK_RECOVERY](sources/recovered_network/ORIGINAL_NETWORK_RECOVERY.json), [TARGET_NETWORK_19](sources/recovered_network/TARGET_NETWORK_19_c9deb93.json) |
| 각 방향의 source·상태·승인 필드 | [targets](registry/targets.json), [coverage](registry/coverage.json) |
| 모든 새 공급자 원행과 native precision | [기본 19개](sources/primary/PROVIDER_ROWS.json), [NNDC 3개](sources/photon_native/PROVIDER_ROWS.json), [He-4 4개](sources/he4_photon/PROVIDER_ROWS.json) |
| 종 정체성과 정수 반응 열 | [species](registry/species.json), [events](registry/events.json), [compiled](registry/compiled.json) |
| 측정 observable과 branch 경계 | [이론 메모](theory/SOURCE_OBSERVABLES_AND_BRANCHES_KO.md), [응답 정의 수정](sources/he4_photon/RESPONSE_DEFINITION_ADDENDUM.json) |
| 완료 계산 재사용·예산·실패 보존 | [REUSED_CALCULATIONS](REUSED_CALCULATIONS.json), [EXECUTION_LEDGER](EXECUTION_LEDGER.json) |
| 최종 scoped 승인 | [primary](raw/PRIMARY_RESULTS.json), [C9_FINAL](reviews/C9_FINAL.json) |
| 남은 직접 입력과 다음 노드 | [TARGET6_DEPENDENCY](sources/he4_photon/TARGET6_DEPENDENCY.json), [NEXT_SOURCE_INTAKE_KO](NEXT_SOURCE_INTAKE_KO.md) |

