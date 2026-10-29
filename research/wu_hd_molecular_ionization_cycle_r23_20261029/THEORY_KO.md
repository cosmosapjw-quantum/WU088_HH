# WU088_HH R23: 분자 이온화 에너지 순환으로 상태별 교환 에너지 재구성

2026-10-29 KST. **원 GL2022 이온반응 채널만:** `H+ + HD(X, v=0,J=2) -> D+ + H2(X, v=0,J=1, ortho)`. 외부 분광 데이터에 근거한 새 계산 경로이며 GL2022 PES-native 문턱은 인증되지 않았다. WU canonical DAG **34/49 unchanged**, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`. R6/C9 distinct-author `NOT_RUN` (현재 native subagent tool 미노출).

## R1–R3: 권위·정의·출처 경계

원본 GL2022 (*JCP* 157 214302 DOI `10.1063/5.0128598`) supplementary PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, 실제 R21 ZIP에서 byte SHA 확인. 원본 10개 온도 그리드의 105 K SQM k=1.15e-16 m³/s 등 기존 rate는 불변이다. GL2022 본문 Sec. II는 **Velilla et al. 2008 H3+ (1^1 A') ground electronic PES**(DOI `10.1063/1.2973629`)를 밝힌다. 그러나 해당 source가 산란에 사용한 state-specific HD(0,2)/H2(0,1) 에너지, 에너지 0, atomic isotope ionization correction, scattering input/PES file bytes는 **미확보**.

R22 형제 브랜치: [PR160](https://github.com/cosmosapjw-quantum/WU088_HH/pull/160) `9db6f91debf54af1cc129538cfd6f6a716a78a56` (중성 Zhou2021 수준표와 2019 이온 ground threshold의 모델 혼합 진단), [PR161](https://github.com/cosmosapjw-quantum/WU088_HH/pull/161) (실험/고정밀 분광 D0+회전 준위 재구성). 둘은 부모 R21 PR159 HEAD `fd351d0ff97ef0d7a9cf710bdecad922af7e885e`의 별개 자식이며 상호 병합 금지. R22 PR161 SOURCE ZIP 95734 B SHA256 `5d92267615c91e9c34c9c496956bdf58473ee41f1db6e58ccbbbfbf4fd95477c` 현재 세션에서 CRC·복원·22/22 회귀 확인.

## R4–R5: 원자 자유에너지 항 없이 닫힌 분자 이온화 순환

영점이 통일된 전자 바닥에너지 E(M), 자유전자 E_e, 핵종 H+,D+를 사용한다. 두 순차 이온화에 대해

- `I(HD) = E(HD+) + E_e - E(HD)`;
- `I(HD+) = E(H+) + E(D+) + E_e - E(HD+)`;
- `I(H2) = E(H2+) + E_e - E(H2)`;
- `I(H2+) = 2 E(H+) + E_e - E(H2+)`.

따라서 정확히

`I(HD)+I(HD+)-I(H2)-I(H2+) = E(D+)+E(H2)-E(H+)-E(HD)`.

동일한 물리적 분자 X(바닥 전자상태)의 0,0 기준에서 `epsilon_HD(0,2)=E[HD(0,2)]-E[HD(0,0)]`, `epsilon_H2(0,1)=E[H2(0,1)]-E[H2(0,0)]`를 더하면

`DeltaE_21 = I(HD)+I(HD+)-I(H2)-I(H2+) + epsilon_H2(0,1)-epsilon_HD(0,2)`.

`DeltaE>0` 흡열, `Q_release=-DeltaE`. 이 항등식은 **서로 같은 자유 전자 영점, 진공·원자핵 에너지, 명시된 0,0/0,1/0,2 및 hyperfine/nuclear-spin 평균 관례**를 가정한다. 광속 c, 플랑크 상수 h, 전하 e는 SI 값으로 유지. 이온 단계를 *분자 이온의 완전 이온화*로 정의해야 한다: `I(HD+)`는 HD+→H++D++e, `I(H2+)`는 H2+→2H++e. HD+→H++D처럼 부분 해리 에너지로 착각해서는 안 된다.

이 식은 R22 PR161의 `DeltaE=(I_D-I_H)+(D0_HD-D0_H2)+epsilon_H2-epsilon_HD`와 항등적으로 같다. 2023 Hölsch Table IV의 `D0_HD=I(HD)+I(HD+)-I(H)-I(D)` 및 H2의 `D0_H2=I(H2)+I(H2+)-2I(H)`를 대입하면 원자 I(H),I(D)가 정확히 상쇄된다. 이것은 **이온화 에너지의 물리값을 임의 gauge shift한다는 뜻이 아니라 동일 데이터 사슬 안에서 종속된 D0를 올바르게 재계산하는 thermochemical identity**다.

## R5–R7: 직접 수치 계산 및 대체 경로

표기된 6개의 원전 숫자 (`sources/MOLECULAR_IONIZATION_LITERALS.json`) 중:

`I(HD)=124568.48466(7)` cm^-1 — Hölsch et al., PRA108 022811 (2023), Table IV row4;

`I(HD+)=131224.6841650(6)` cm^-1 — Korobov et al., PRL118 233001 (2017), Table V;

`I(H2)=124417.4911573(58)` cm^-1 — Doran et al., PRX accepted 2026-08-31, 45-edge network;

`I(H2+)=131058.1219937(6)` cm^-1 — Korobov et al. 2017, Table V (HD+와 동일한 theoretical donor, source independence 과장 금지);

`epsilon_H2=118.48684(10)` cm^-1 — Salumbides et al 2011 Table II 인용(실제 원 측정 Jennings 1984);

`epsilon_HD=(8006533168±26) kHz` — Cozijn et al 2022 HD combination difference, `epsilon_HD_cm^-1 = f_Hz/(100 c_m/s)`.

원전 인쇄 숫자를 **정확한 Decimal input 문자열**로 계산하되 분광물리 자체가 무오차라는 주장은 하지 않는다:

`DeltaE_ground_ionic=317.5556740 cm^-1`;
`epsilon_HD=267.0691991857913917... cm^-1`;
`DeltaE_21=168.973314814208608276... cm^-1`;
`Q_spectroscopy_candidate=-20.9500209938404575906... meV/event = -3.3565634118140639e-21 J/event`.

2017/2023/2026 기반 **분자 이온화 순환**과 이전 R22 PR161의 원자-IP/D0 기반 **별도 계산** `DeltaE=168.9733160842086... cm^-1` 차이는 `−0.00000127 cm^-1` = `−38.073642166 kHz`. 분광 출처의 공통 이론 계산 및 이온화 기준에 따른 작은 원전 차이로 취급하며, 이것을 독립 statistical agreement/p-value나 물리적인 source-Q uncertainty로 사용하지 않는다. 개별 원전의 quoted uncertainty 절댓값 L1 합은 `0.00017786726665 cm^-1`이나 공분산, 신뢰구간, certified hard bound가 아니다. 2019 ground-state 39.5 meV를 지니고 오면 안 된다.

2019 Lepers et al. (MNRAS488 4732, Sec.3.2) 별도 VLABP BO TIQM에서 **HD(0,2)→H2(0,0)** 에너지 문턱을 **약 3.4 meV(동위원소 ionization offset 제외)**라고 기재한다. 이것은 **목표 H2(0,1)**의 문턱이 아니며 GL2022 SQM 자체의 교정값도 아니다. 2021 erratum (MNRAS500 430, DOI `10.1093/mnras/staa3146`)은 spin-orthopara *thermal rate composition*을 교정했지만 이를 임의 단일 channel의 energy 또는 rate multiplier 3/4로 사용할 근거는 아니다. R22 PR160의 2021 Zhou **중성 H+HD** 데이터를 GL2022 ionic PES로 대체할 수도 없다.

## R6, C9 및 반증

SymPy 29개 소프트웨어 fixture 중 하나에서 **정확한 분자 이온화 순환 항등식**을 상징으로 검증; Wolfram Language의 서로 다른 엔진에서도 정확 기호 항등식 True; mpmath100과 SymPy Rational에서 출력 Decimal85와 `~7.3e-84 cm^-1`의 표현 차. 과거 원본 R21/PR161 clean restore tests는 18/18,22/22 실제 재실행. 코드의 29/29 normal 및 `-O` 재실행을 기록. 단 하나의 다른 모델/언어 검산을 별도 인간/모델 저자 R6/C9으로 승격하지 않는다.

물리적 실패 경로: (1) H2+ ion energy를 분자 이온 partial dissociation과 혼동, (2) H2 ortho/para 구분 누락, (3) neutral 2021 level 반응과 동일 물리 선언, (4) 2019 ground Q나 BO 3.4 meV 직접 대입, (5) 합성 그림에서 cross-paper scatter를 physical errorband로 해석, (6) GL2022 source-negative reverse 또는 production 발급. 모두 hold.

## R8–R10: 적용 가능 범위

결과: `DERIVED + NUMERICALLY_CHECKED + IMPLEMENTATION_VERIFIED_SCOPED` **for spectroscopy-only molecular ionization cycle**. `GL2022_PES_native_threshold=null`, `physical_Q_event=null`, `physical_bath_delta=null`, `source_uncertainty=null`; R21 affine bath `B(Q)=xi Q+B_known`은 계산식으로만 유지. 실제 REC/CR 4-species molecular chemistry owner와 owner ACK, full graph reachability, reverse and physical bath, full-A는 OPEN. 기존 WU 34/49를 과학적으로 승격하지 않는다.

최소 후속 입력은 GL2022 자체의 Velilla PES numerical asymptotic HD(v0,j2), H2(v0,j1) threshold 및 이온화 offset 포함 여부를 **소스 코드/데이터+관례**로 특정하는 것이다. 실제 자료가 오면 spectroscopy vs BO-native를 하나의 선언한 convention 안에서 비교한다.
