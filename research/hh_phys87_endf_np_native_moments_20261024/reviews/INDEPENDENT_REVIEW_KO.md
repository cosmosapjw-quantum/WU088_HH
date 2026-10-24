# PHYS87 독립 C9 최종 검토

## 판정

**PASS_SCOPED — NUMERICALLY_CHECKED_SCOPED_SOURCE_NATIVE_FINITE_WINDOW.** 미해결 차단 지적은 0건이다.

독립 R6 유도, S1 동결 코드, 실제 primary/reference/lease/admission/resume raw와 저장 그림을 차례로 검토했다. 검토자는 source module을 import하거나 새 적분·과학 실행·Wolfram 호출·기존 identity 재실행을 하지 않았다. 아래 수치는 저장 결과의 표준 라이브러리 요약과 실제 원문 readback이다. S2 게시·DAG·handoff·양쪽 최종 복원은 별도의 controller 단계이며 이 문서가 그 완료를 대신하지 않는다.

### 확정된 identity

- 실제 로컬 S1 HEAD: `94d3b35bb66df184cf370035f498effbb4534cc6`.
- Primary input/code binding: `bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d`.
- Primary RESULT: 109074bytes, SHA256 `aaf3a145c24a57a467886ad7d6422f04805be50e389c254d2f12d8049a18b874`.
- 독립 reference: 86936bytes, SHA256 `7a5e29167f5f469e32ab0d66fffa0f491fc130f22d7452a68ae4b482c4060fea`.
- CONTRACT revision2: `464df6f83a7ac8bd64813dc9da3ca34f19398a2f970f3d69c706e3d089f6fd38`.

실제 primary dependencies9개, primary output manifest payload6개, figure payload4개 및 세 prelaunch admission 파일의 bytes/SHA를 대조했다. Primary bytes는 reference·resume·figure 이후에도 동일하다. Historical R6 이론과 현재 이론의 설명상 차이는 `CODE_REVIEW_PREEXEC`에 보존했다. 수치 입력과 식은 변경되지 않았다.

## 검증 근거의 구분

| 근거 종류 | 실제 확인 | 의미 |
|---|---:|---|
| Primary scalar assertions | 147/147 PASS, 실패0 | 이 중 guard cases24개가 포함된다 |
| 원자료 절점의 exact positivity witness | 153개 | Fraction으로 저장된 후보값·최소값이 양수 |
| Convex interpolation cell witness | 152개 | 표현된 angular law의 knot 사이 양성성 |
| Wolfram formal residual | 12개 정확히0 | 기존 단일 root symbolic 호출의 저장 근거 |
| Independent rate/mean comparison | 4/4 PASS | T=1e8K에서 별도 parser, kve, adaptive quadrature |
| Independent energy closure | 1 PASS | 같은 reference가 반환한 세 평균 회계 |
| 실제 resume | SKIP1, callback0, 적분0, rewrite0 | 완료된 결과 bytes 재사용 |

**153/152 source witnesses를 147 scalar assertions에 더하지 않는다.** 새로운 primary child는1이고 그 안의 valid thermal integrations는8 full+4 FD scalar=12다. Conditional angular cases18개, adopted owner rows16개를 보존한다. 독립 reference child1, saved-only figure child1은 각각 별도 ledger 항목이다.

## 실제 수치 결과

다음은 order32의 네 고정 sample이다. Rate는 source support `[1e−5, 2e7] eV`에 한정한 값이며 support 밖의 전체 반응률을 뜻하지 않는다. Mean energy 단위는 eV/event다.

| T [K] | κ [cm³/s] | ⟨Kin⟩ [eV] | ⟨Eγ⟩ [eV] | ⟨Kd⟩ [eV] |
|---:|---:|---:|---:|---:|
| 255 | 7.316996332054e-20 | 0.0659226763472 | 2223330.63664 | 1317.42928282 |
| 10000 | 7.316879769765e-20 | 2.58518378749 | 2223331.89626 | 1318.68892149 |
| 1000000 | 7.303202639022e-20 | 258.359321954 | 2223459.70319 | 1446.65613026 |
| 100000000 | 6.331212661681e-20 | 24821.0259767 | 2235226.85375 | 14242.1722255 |

공통 normal frame에서 `⟨Kin⟩+QI=⟨Eγ⟩+⟨Kd⟩`를 확인했다. QI=2224648eV는 source-native effective mass 회계다. Photon AWP=2223300eV metadata를 별도의 energy deposit으로 더하지 않는다. Parent bare-nucleus Q와의81.63eV 차이는 변환 의무로 유지한다.

### Frozen acceptance와 실제 residual

| 항목 | 실제 최대 | 동결 허용값 |
|---|---:|---:|
| Order16–32 rate/mean 상대차 | 1.648189533740267e−16 | 1e−8 |
| FD selected log-rate slope 절대차 | 6.271401387092368e−8 | 5e−7 |
| Conditional angular relative/scaled residual | 1.3446208630370971e−14 | 2e−12 |
| Conditional event energy closure [eV] | 7.82310962677002e−8 | 2e−7 |
| Thermal mean energy closure [eV] | 4.15738887760142e−10 | 2e−7 |
| Six-column owner closure [eV] | 4.15738887760142e−10 | 2e−7 |
| Independent rate/means 상대차 | 7.767841434001767e−13 | 1e−7 |
| Independent closure 절대값 [eV] | 7.275957614183426e−12 | 2e−7 |

255K와1e4K 부근의 near-constant rate는 이 원자료 모델의 저장 결과다. Order16–32가 binary64 수준에서 일치하는 사실을 continuum quadrature certificate나 source confidence interval로 바꾸지 않는다. FD 비교는 지정된 두 온도와 고정 hlog=2^−8에 한정된다.

153개 angular density witness 중 가장 작은 저장값은 knot122, E_lab=6MeV의 `926441/100000000=0.00926441`이다. 이는 표현된 normalized quadratic law의 양성성이며, 원전의 물리적 uncertainty를 좁히는 근거가 아니다. All full rows의 세 variance와 conditional gamma variance는 양수다. Variance의 안정성은 R6의 exact coefficient cancellation, 코드 검토, 실제 양수·centered 계산과 symbolic residual 근거에 의존한다. 별도의 저온 high-precision variance reference를 수행했다고 주장하지 않는다.

### Underflow 기록

Order32의 Boltzmann underflow nodes는 온도 순으로4271,4115,2984,459개/4864이고, sampled cell 전체의 Boltzmann 값이 underflow한 구간은133,128,93,14개다. 코드가 모든152개 native interval을 유지한 상태에서 관측한 binary64 underflow다. 해당 물리적 적분이 정확히0이라고 선언하거나 omitted/source-outside tail에 대한 한계로 쓰지 않는다. 독립 reference에서도 모든152개 구간을 적분했고1215개의 callback에서 exponential underflow0을 기록했다. Callback 수는 고유한 물리적 사건 수가 아니다.

## 독립 reference의 실제 범위

별도 fixed-width Decimal parser가 canonical raw를 읽고153개 절점×4 numeric fields=612개를 frozen table에 대조했다. MF3 interpolation은32개 INT5 cell과120개 INT2 cell이며, MF6 LCT2/LAW2/LAW4/yield1/frame을 확인했다. Table은 대조용이고 kernel input은 별도 raw parser의 결과다.

T=1e8K에서 SciPy1.17.0의 실제 scaled Bessel `kve`와 변수 `x=E_lab/theta`의 adaptive QUADPACK 적분을 사용했다. Primary의 logE Gauss rule 및 finite asymptotic Bessel polynomial을 가져오지 않았다. 전체608개의 scalar quadrature call,12810개의 callback, native cell152개가 저장돼 있고 각 cell 합이 반환 integral과 일치한다.

| 비교값 | Primary/reference 상대차 |
|---|---:|
| κ | 1.9012253727115222e−16 |
| ⟨Kin⟩ | 4.4630086919005057e−13 |
| ⟨Eγ⟩ | 0 |
| ⟨Kd⟩ | 7.767841434001767e−13 |

Reference energy closure는 −7.275957614183426e−12eV다. 별도 mpmath 실행은0이고 저온 variance 차감은 하지 않았다. 반환된 QUADPACK error estimates는 rigorous global bounds로 취급하지 않는다.

## Thermal/fast ownership의 해석

| T [K] | Cv Tdot/R, h=0 [eV/event] | Cv Tdot/R, h=1 [eV/event] |
|---:|---:|---:|
| 255 | -7.68898886297e-08 | 1317.39632144 |
| 10000 | 1.61941232129e-05 | 1317.39633769 |
| 1000000 | 0.160705561006 | 1317.55682947 |
| 100000000 | 1031.27031126 | 2347.36842998 |

h=0은 recoil kinetic energy의 fast ownership을 유지하고, h=1은 명시된 instantaneous caloric-birth model이다. 특히1e8K에서 thermal energy column 자체는 두 모델 모두 음수이지만, reactant와 daughter particle 수 변화에 따른 composition term을 포함한 `Cv Tdot/R`는 양수다. 이는 reaction-selected kinetic energy와 일반 single-species thermal energy가 다른 데서 나온다. Q를 그대로 gas heat로 추가한 결과가 아니다.

R, density, Cv는 외부 consumer의 미정 입력이다. 위 forcing은 실제 시간에 따른 가열률, stopping 완료, coupled T/xe history의 상·하한 또는 두 역사 사이의 causal experiment가 아니다. Raw energy column의 legacy 이름 `nuclear_rest`도 이번 source-native effective mass 규약 안에서만 읽어야 한다.

## 실제 자원·실행·재사용

| Child | 실제 CPU / cap [s] | 실제 launch wall / cap [s] | 실제 prelaunch available bytes | 시도 / 완료 / 실패 |
|---|---:|---:|---:|---:|
| primary | 0.155068 / 12 | 0.156074 / 60 | 2213384192 | 1 / 1 / 0 |
| reference | 0.821026 / 20 | 0.822370 / 60 | 2212503552 | 1 / 1 / 0 |
| figures | 3.388289 / 8 | 3.390605 / 30 | 2156789760 | 1 / 1 / 0 |

세 child 모두 fresh actual memory가 reserve1.5GiB+job0.5GiB=2147483648bytes 이상이었다. Admission 시 peer lease0, own lease1을 기록했고, child CPU0·coordinator CPU8·1 worker/thread·original gate SHA를 유지했다. 모두 own lease를 해제했다. Peer process termination, automatic retry, cache credit 및 기존 PHYS83–86 science 호출은0이다. 실제 primary+reference outer CPU 합은0.976094s, figure까지 포함한 세 local child CPU 합은4.364383s다. 이는 root의 단일 Wolfram 호출 및 이전 단계 누적 비용과 별도 항목이다. 금액은 알려지지 않았으며 allowance를 reset하지 않는다.

실제 resume 원문은 `SKIP`, scientific_callbacks0, thermal_integrations0, files_rewritten0을 반환했다. Source/code/input binding과 완료 output hashes가 일치한다. Runtime 차이만으로 과학을 재실행하지 않았다.

## 그림과 수정 이력

Saved RESULT만 읽는 child1이2PNG+2PDF를 생성했다. 각 bytes/SHA와 input RESULT identity를 확인했다. 검토자는 두 실제 PNG를 직접 보았고, root도 별도로 직접 보았다는 근거를 전달했다. 축·단위·legend가 읽히며 clipping이나 confidence bands는 관찰되지 않았다. Native-knot와 네 온도를 연결한 선은 visual guides라는 문구가 보인다. 별도의 PDF rasterization을 수행했다고 주장하지 않는다.

실행 전 지적 C9-P01은 actual prelaunch admission JSON을 child 전에 쓰도록 고친 후 실행했다. Reference가 소비한 SHA `84cc86128963bee3be674dbefbf80dce897b89aa236a950c1738b048e9416b99`는 wrapper의 실제 prelaunch file과 일치한다. 그 결과 첫 reference child가 정상 완료했으므로 정적 repair뿐 아니라 실제 연결 근거도 확보됐다. Source 또는 tolerance를 결과를 보고 바꾸거나 실패 실행을 지우지 않았다. 새 runtime finding은0이다.

## Claim gate와 남는 의무

이번 판정은 unpolarized ground-state evaluated source, 독립 common-T isotropic driftless classical Jüttner reactants, 고정 finite support, 명시적 source-native mass/Q convention 및 고정 samples에 한정된다. Conditional directed photon law를 보존하면서 COM 입사축을 평균하면 scalar moments의 angular dependence가 소거되는 유도를 사용했다. 이를 원래 microscopic law가 isotropic하다는 가정으로 바꾸지 않는다.

Atomic-equivalent→bare-network remap, physical source covariance/angular uncertainty, source 밖 cross sections와 full-rate/tail bound, 실제 charge-state/population validity, thermal/fast consumer와 fast stopping, photon escape/reabsorption, full spectral backreaction 및 coupled history는 OPEN이다. 고온의 고정 neutral-target 입력은 그 온도에서 중성 원자의 평형 abundance를 주장하지 않는다.

**HH_R10=OFF. Production admission NOT_ISSUED.** Publication·dual-provider final restore·최종 handoff는 controller가 각각 실제 근거를 갖추어 닫아야 한다.
