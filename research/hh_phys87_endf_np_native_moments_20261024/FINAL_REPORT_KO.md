# PHYS87 최종 과학 보고서 — source-native ENDF H1 유한 온도 사건 moments

판정: **NUMERICALLY_CHECKED_SCOPED_SOURCE_NATIVE_FINITE_WINDOW / PASS_SCOPED**. Canonical ENDF/B-VIII.1 n+H1 포획 원자료를 원래 에너지·질량·각분포 규약으로 묶고, 공통 온도의 Jüttner 사건 measure에서 반응률·입사 운동에너지·광자·잔류핵 에너지 및 thermal/fast 입자 회계를 구현했다. 독립 C9의 미해결 차단 항목은0이다. 실제 network rate activation, fast stopping, 새 ODE와 완료 identity replay는0이다.

이 문서는 S2 시점의 최종 과학 결과다. 실제 containing commit, 이후 문서 HEAD, 단계 ACK와 FINAL 양쪽 복원은 delivery/ 및 외부 PHYS87_FINAL_DELIVERY_20261024.json에서 구별한다. 과학 판정으로 미래 게시·백업 성공을 선언하지 않는다.

## 1. 연구 위치와 재사용

부모는 PHYS86 최종 HEAD f4a6d5505c845a046e3b81d33a2992a239ab4c8b, Draft PR143이다. 이번 branch는 research/hh-phys87-endf-np-native-moments-20261024, Draft PR144이며 실제 원격 부모의 additive descendant다. PHYS83 owner completion, PHYS84 prepared adapter, PHYS85 사건 소유권 및 PHYS86 Jüttner moments/theorem을 재사용했다. PHYS84 numerical admission WAIT는 바꾸지 않았다.

사용자 고정 중앙 인계0f9d9df825be1dac9ca9bdf73cdc2e8908bcba17와 actual refs를 대조했다. 초기51repo/2234branch-SHA inventory와 최근6repo×10PR을 종합하고, 실행 말미6repo×5PR 및 actual AGENTS/HEAD delta를 추가 확인했다. 메타데이터 전체 페이지 완료와 선택 원문의 실제 읽기를 구별한다. 비공개 대화는 UNAVAILABLE, 외부 runtime/lease는 UNOBSERVED이며 모든 branch 본문·백업 payload·대화를 읽었다고 주장하지 않는다. 자세한 결과는 SURVEY_SYNTHESIS_KO.md와 LATE_SURVEY_ADDENDUM_KO.md에 있다.

PHYS86 전달은 기존 과학을 실행하지 않고 복원했다. 최종 ZIP 양쪽 whole GET/CRC332/payload331/Git82/extraction332와 두 원 JSON 원문 readback을 확인했다. 첫 Drive S2의 short object와 변경된 local copy, downloader 완료 전 restore 실패를 보존하고, 원 Dropbox canonical S2를 새 경로로 복구해 새 Drive 객체의 전체 bytes를 대조했다. 원인은 UNRESOLVED다. 새 completion supplement는21137bytes/SHA3e78e87ab001bab70844c52dfbd896183aefda0fc832a6ef484c9356b1c44aee이며 양쪽 실제 raw readback PASS다. 과거 JSON의 당시 dual=false를 덮어쓰지 않았다.

## 2. Canonical source와 물리 규약

원전은 [NNDC ENDF/B-VIII.1 n-001_H_001.endf](https://www.nndc.bnl.gov/endf-data/ENDF/ENDF-B-VIII.1/n-001_H_001.endf)와 [ENDF-102 manual](https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf)이다. 원본671232bytes의 SHA256은3024d8f0db604b074e33ed8b05027eb9f5a738614041ba44c83f048e0d0bc1af이다. Canonical 원본 bytes와 LF8832개/CRLF0개의 행 끝을 그대로 보존했다. ENDF source table은 literal153행이며 raw parser와 독립 parser 모두 원문을 확인했다.

| 항목 | 채택한 규약 |
|---|---|
| 채널 | n + H1 atomic-equivalent target → effective ²H(D) atomic-equivalent residual + photon |
| 입사 에너지 | target rest LAB E, 1e−5…2e7 eV |
| 단면적 | MF3/MT102, 153knots; NBT33까지 INT5 log-log, 이후 NBT153까지 INT2 lin-lin |
| 각분포 | MF6/MT102 LCT2 COM, LAW2 LANG0 NL2의 a1/a2; 계수 INT2 |
| 생성물 | photon yield1, recoil LAW4 yield1 |
| 기준 질량 | 명시한 neutron rest energy939565421.94eV, source AWR0.9991673 |
| source QI | 2224648eV; effective residual rest energy=εn+εH−QI |
| thermal model | independent common-T isotropic classical Jüttner; no drift/screening/stimulated emission/internal-state evolution |
| covariance | MF33 원문 보존·미전파; angular covariance 공급 없음 |

ENDF atomic AWR와 light-particle AWP를 섞어 독립 잔류핵 질량을 만들지 않았다. Photon AWP2223300eV는 원전 primary-photon metadata이며, 실제 사건 에너지는 같은 W/QI 질량 관계로 계산한다. Parent bare-nucleus Q=2224566.37eV와 차이81.63eV를 보존한다. 이는 이 연구가 추정한 오차 막대가 아니다. Source-native→bare-network remap은 OPEN이며 코드가 bare-network convention 요청을 거부한다.

Bound electron은 composite 내부에 남으므로 free-electron incidence는0이다. 사건별 핵자수1+1=2, 핵전하0+1=1, bound-electron count1=1을 유지한다. 여기의 rest ledger는 source-native composite 질량 회계이며 parent bare-mass ledger의 숫자를 변경하지 않는다.

GNDS advertised/actual checksum mismatch는 보존하고 canonical 입력에서 제외했다. heated_000293.15K 데이터에 다시 thermal convolution을 적용하지 않았다. Exa402 credit-limit 응답, JAEA human-check 중단, SciSpace 실제1검색과 원전 선택을 보존한다. SciSpace의 별도 EFT 불확실성을 ENDF의 confidence interval로 옮기지 않았다.

## 3. 유도에서 구현으로

θ=kBT, M=εn+εH, W는 COM 총에너지, K=W−M이다. 차감 손실을 피하기 위해 다음 동치식을 쓴다.

```text
W = sqrt(M² + 2 εH E_lab)
K = 2 εH E_lab / (W+M)
λ = K(2M+K)(4 εn εH + 2MK + K²)
q = Q+K
e* = q(2W−q)/(2W)
kD* = q²/(2W)
ED* = W−e*
```

원전 COM 법칙 f(μ)=1/2[1+3a1μ+5a2P2(μ)]는 dμ에 정규화되어 있다. Incoming COM axis와 boost axis의 cosine을 η, photon/boost cosine을 ν라 두면 E[ν]=a1η, E[ν²]=(1−a2+3a2η²)/3이다. 고정 β에서 Eγ=γe*(1+βν), KD=kD*+(γ−1)ED*−γβe*ν, Kin=K+W(γ−1)이다. 같은 사건에서 Kin+Q=Eγ+KD가 성립한다.

공통 T의 등방 Jüttner 입력은 fixed W,total P에서 incoming COM axis를 균일하게 만든다. 이 축에 대해 정규화된 비등방 원전 법칙을 평균하면 절대 photon 방향은 균일해진다. 미시적 a1/a2를 없애거나 고정 축에서 등방으로 대체한 것이 아니다. Unequal T, drift 또는 방향 선택에는 이 환원을 그대로 적용하지 않는다.

Fixed W의 boost marginal은 sqrt(γ²−1)exp(−zγ), z=W/θ에 비례한다. G=E[γ]=K2(z)/K1(z), G2=E[γ²]=1+3G/z를 사용한다. 유한 source window의 반응률 계수는

```text
κ(T) = c/[4 εn² εH² θ K2(εn/θ)K2(εH/θ)]
       × ∫source σ(E(K)) λ(W) K1(W/θ) dK
dK/dlogE = εH E/W
```

이다. e^zKν의 0…6차 asymptotic coefficient를 exact Fraction으로 만들고 P2−P1 및 variance numerator P1²+3tP2P1−P2²를 먼저 정확히 소거한다. 그 뒤 floating 평가를 한다. 허용 숫자 입력은255…101000000K 및 모든 z≥1e5이며, 이 범위 전체에 대한 수치 인증을 의미하지 않는다.

평균은 ⟨Kin⟩=⟨K+W(G−1)⟩, ⟨Eγ⟩=⟨e*G⟩, ⟨KD⟩=⟨kD*+ED*(G−1)⟩이다. 분산은 조건부 분산과 (조건부 평균−전체 평균)²의 양의 합으로 계산한다. Photon/recoil covariance도 같은 사건 measure를 공유한다. PHYS86의 정확한 온도 미분 관계 θ dlogκ/dlogT=⟨Kin⟩−un−uH를 재사용했다.

실제 유도와 원전 규약은 theory/NATIVE_FINITE_T_MOMENTS_KO.md, 구현은 source/native_moments.py, 동결 식–코드 관계는 CONTRACT.json 및 implementation/에 있다.

## 4. 네 온도의 실제 결과

다음은 order32 결과다. κ는 원전의 유한 에너지 창에 대한 cm³/s이며, source 밖의 σ를0으로 확장하지 않았다. Population, density, 실제 cosmological abundance를 지정하거나 evolution을 실행하지 않았다.

| T[K] | κ[cm³/s] | ⟨Kin⟩[eV] | ⟨Eγ⟩[eV] | ⟨KD⟩[eV] |
|---:|---:|---:|---:|---:|
| 255 | 7.316996332053735e−20 | 0.0659226763472 | 2223330.636639856 | 1317.42928282050 |
| 10000 | 7.316879769764634e−20 | 2.58518378749 | 2223331.896262297 | 1318.68892149083 |
| 1000000 | 7.303202639021920e−20 | 258.359321954 | 2223459.703191694 | 1446.65613025958 |
| 100000000 | 6.331212661680925e−20 | 24821.025976721 | 2235226.853751180 | 14242.1722255408 |

높은 T의 표도 고정된 source-native target model의 조건부 평가다. 고온에서 중성 H target population이 실제 열평형으로 존재한다는 결론은 포함하지 않는다. 많은 고에너지 노드에서 floating Boltzmann exponential이 underflow했고 그 개수를 raw에 남겼다. 이는 해당 단면적이나 continuum tail이 정확히0이라는 증명이 아니다.

## 5. 입자 수·열적 에너지·온도의 구별

잔류핵을 fast pool에 두면 h=0, 명시적 instantaneous caloric birth를 가정하면 h=1이다. 사건당 thermal count는 h−2, fast count는1−h이고 free electron 변화는0이다. Photon은 emissivity_handoff 또는 immediate_escape 중 정확히 한 경로만 소유한다. Six-column energy sum은

```text
[h⟨KD⟩−⟨Kin⟩, (1−h)⟨KD⟩, −Q, 0, Eγ_handoff, Eγ_escape]
```

이며0이다. Photon 재흡수, spectral feedback 또는 fast stopping law를 추가하지 않았다.

일종의 등온 비열을 가정해 Q만 Tdot로 바꾸지 않는다. Single-species kinetic mean ui=εi(K1/K2−1)+3θ를 사용하면 실제 density/Cv가 주어졌을 때의 temperature equation은

```text
Cv Tdot / R = −⟨Kin⟩+un+uH+h(⟨KD⟩−uD).
```

이번 코드는 오른쪽 eV/event를 공급한다. 실제 R이나 Cv를 임의로 정하지 않았다.

| T[K] | h=0: Cv Tdot/R[eV/event] | h=1: Cv Tdot/R[eV/event] |
|---:|---:|---:|
| 255 | −7.68898886297e−8 | 1317.39632144388 |
| 10000 | 1.61941232129e−5 | 1317.39633769489 |
| 1000000 | 0.160705561006 | 1317.55682946702 |
| 100000000 | 1031.27031126418 | 2347.36842997718 |

특히1e8K에서 thermal energy column은 h0일 때−24821.0259767eV, h1일 때−10578.8537512eV로 둘 다 음수다. 그러나 temperature forcing은 각각+1031.2703113eV와+2347.3684300eV다. 반응으로 제거되는 입자들의 kinetic mean이 기존 thermal 평균과 다르고, thermal 입자 수도 줄기 때문이다. 이 차이를 반영하지 않으면 에너지 ledger가 닫혀 있어도 temperature source를 잘못 구성할 수 있다. h1은 지정한 즉시 caloric birth 모형이며 실제 stopping 시간이나 물리적 thermalization 경계가 아니다.

## 6. 검증과 판정의 범위

| 근거 | 실제 결과 | 동결 기준 |
|---|---:|---:|
| Primary scalar assertions | 147/147 PASS, 실패0 | 전부 통과 |
| Negative guards | 24/24, 위147에 포함 | domain/nonfinite/owner/route/bare 요청 거부 |
| Exact angular source witnesses | 153knots +152convex cells | represented law의 strict positivity |
| GL16–32 최대 상대차(rate/means) | 1.648189533740267e−16 | 1e−8 |
| FD slope 최대 절대차 | 6.271401387092368e−8 | 5e−7 |
| Conditional angular 최대 scaled residual | 1.3446208630370971e−14 | 2e−12 |
| Conditional event closure 최대 | 7.823109626770020e−8eV | 2e−7eV |
| Thermal/owner closure 최대 | 4.157388877601420e−10eV | 2e−7eV |
| Independent κ/means 최대 상대차 | 7.767841434001767e−13 | 1e−7 |
| Wolfram formal residuals | 12/12 exact0, evaluator1회 | 원 유도 항등식 |
| Resume | 실제1 SKIP, scientific callback0 | no replay/no rewrite |
| 그림 | saved render1회,2PNG+2PDF, 실제 시각 검토 PASS | source 재계산0 |

각분포 최소 density witness는6MeV에서926441/100000000이며 양수다. Exact quadratic endpoint/vertex 계산과 lin-lin 계수의 convex combination으로 선택된 represented law의 전체 cell positivity를 설명한다. 이 증명과 sampled thermal/energy residual의 범위는 다르다.

독립 reference는 production module을 import하지 않고 raw MF3/MF6를 다시 파싱했다. 원문 numeric fields612개,153knots를 확인했고, T=1e8K에서 실제 SciPy kve 및 x=E_lab/θ의 adaptive quad를 썼다. Native152cells 전체의608quad calls,12810callbacks이며 독립4관측량과 energy closure가 통과했다. 저온 variance에 대한 별도 high-precision reference 또는 mpmath 실행은 없었다. QUADPACK error estimate, GL 비교, floating residual을 rigorous continuum certificate나 physical CI로 채택하지 않는다.

R6 및 실행 전 검토에서 T guard 문구를 명확히 했고, 실제 admission 파일이 reference 시작 전에 존재하도록 wrapper timing을 교정했다. 둘 다 새 과학 실행 전에 끝났다. Historical R6 source hash와 S0 문구 변경은 실제 diff로 결속했다. 그 뒤 scientific code/input은 불변이며 처음 주 계산·reference·figure 모두 성공했다. Independent final decision은 reviews/INDEPENDENT_REVIEW.json 및 _KO.md, root 결정은 SCIENCE_ADMISSION.json이다.

## 7. 실제 실행·누적 예산

| Child | CPU[s] | launch-inclusive wall[s] | cap CPU/wall[s] |
|---|---:|---:|---:|
| Primary1 | 0.155068 | 0.156074173 | 12/60 |
| Independent reference1 | 0.821026 | 0.822369514 | 20/60 |
| Saved figures1 | 3.388289 | 3.390604982 | 8/30 |

세 child CPU 합4.364383s다. 이는 측정한 child 합이며 전 대화·provider·orchestration의 total CPU가 아니다. Python3.12.14/NumPy2.3.5/SciPy1.17.0, Linux6.18.55를 실제 결과에서 읽었다. 버전만 달라졌다는 이유로 재실행하지 않는다.

매 child 직전에 pinned shared lease와 actual memory를 확인했다. Reserve1.5GiB+job0.5GiB,1worker/thread, scientific CPU0/coordinator CPU8을 지켰다. 최소 prelaunch available2156789760bytes는 요구2147483648bytes 이상이었다. Peer lease0을 관찰했고 own lease를 모두 해제했다. Other process termination/cache credit/autoRetry는0이다. Job0.5GiB는 gate의 allocation이며 별도 peak RSS 측정값으로 꾸미지 않는다.

PHYS85/86 cloud evaluator4회와 해당 추가 allowance0을 보존했고 PHYS87은 symbolic1회만 썼다. 이 계수 범위의 합은5이며 프로젝트 전체 과거 지출을 뜻하지 않는다. PHYS87 cloud bodywall1.043754s/toolwall9.957s, cloud CPU와 금액은unknown/null이다. 세 child 허용 횟수는 모두 사용했으며 남는 초를 새 campaign 예산으로 이전하지 않는다. 전체 EXECUTION_LEDGER와 inherited ledger를 보존했다.

## 8. 과학 identity와 실제 전달

- Primary input/code identity: bc8a07546cab87dc79de5efee1e0d1917f7e88e851cdd8d5e7856f50f8c1c53d
- Primary RESULT: aaf3a145c24a57a467886ad7d6422f04805be50e389c254d2f12d8049a18b874
- Independent RESULT: 7a5e29167f5f469e32ab0d66fffa0f491fc130f22d7452a68ae4b482c4060fea
- S0: b4e606c433bc0d7969227635b62f33e67a56c705
- S1 code checkpoint: 94d3b35bb66df184cf370035f498effbb4534cc6

S0/S1은 양쪽 실제 ACK+metadata가 있고, stage whole GET으로 표시하지 않는다. S2와 FINAL은 발생 뒤 delivery/ 및 external final JSON에 실제 식별자·SHA·원문 readback을 추가한다. Git blob bytes, numerical agreement, source adequacy, provider ACK와 whole restoration은 다른 판정이다. Native Git commit message의 trailing newline serialization 불일치는 local reconstruction 문제로 진단·보존한 뒤 실제 advertised SHA와 일치시켰으며 과학 오류로 승격하지 않았다.

## 9. 다음 DAG와 종료 조건

완료된 child는 ENDF_H1_NATIVE_FINITE_WINDOW_JOINT_MOMENTS다. NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER 부모는 PARTIAL이다. 다음 이론 의무는 NUCLEAR_ATOMIC_TO_BARE_CAPTURE_REMAP: native lab/COM energy, atomic/bare masses/Q, bound electron과 residual identity 및 원전의 에너지 원점을 정합하는 source contract다. 원전 정확도·각분포 covariance·밖의 support/tails와 named consumer를 닫은 뒤 rates/fast-stopping 활성화를 판정한다. 현재 activation은 NOT_ISSUED다.

HE_LI_CX_STATE_AND_PHOTON_ENERGY, D_PI_RR_MATCHED_SOURCE_MOMENTS, Li instrument/deconvolution/isotope/target-state uncertainty, LI_HARD_UV_INNER_SHELL_SPECTRAL_CONTRACT, RECOMBINATION_TO_Z20_INITIAL_CHARGE_CONTRACT, FULL_GEOMETRY_SPECTRAL_BACKREACTION을 OPEN으로 유지한다. 최신 HE/BASS/REC/REI 결과가 이 선행을 모두 닫는다고 해석하지 않는다.

Non-tilted LRS Bianchi I, reacting gas pi=0, collisionless DM pi_m 별도를 유지한다. 같은 normal orthonormal frame의 signed matter/radiation tensor를 합한 뒤 norm을 취하며 Frobenius=sqrt(2)*half-contraction norm이다. 동일 trajectory의 성분 분석은 species-off 인과 실험이 아니다. HH_R10=OFF, production NOT_ISSUED, 전체 목표 완료율null이다.

R1–R10/C1–C10의 단계별 유도·코드·검증·실행·게시·백업 축은 RESEARCH_LOOP_MAP_KO.md와 STAGE_PROGRESS.json에 있다. 최종 사용자는 FINAL HEAD와 외부 delivery receipt를 함께 읽어야 한다. 완료 identity는 복원·reuse하고 새로운 source/consumer 계약만 다음 연구로 진행한다.

최신 HE97/REC133/BASS187/REI pressure 수신의 실제 채택 범위와 발표·백업 상태는 LATE_SURVEY_ADDENDUM_KO.md 및 10/10 Git blob readback으로 보완한다. 이 부록은 원래 조사 시점의 기록을 현재 상태로 오인하지 않게 한다.
