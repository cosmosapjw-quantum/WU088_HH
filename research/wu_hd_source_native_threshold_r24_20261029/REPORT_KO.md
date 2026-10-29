# WU088_HH R24 연구보고서 | 원본 GL2022 반응률의 양의 Laplace 문턱 제약

2026-10-29 KST. 부모 R23 Draft PR162 HEAD `2f214319ca8600475b1d4e85d1ca21a0249136a8`. R22 PR160은 읽기 전용 형제, PR161은 부모 계보의 분광 입력. **정규 과학 DAG 34/49 변화 없음**, 4-상태 HD 실제 owner ACK 미확보, `HH_R10=OFF`, `production=NOT_ISSUED`, `L4=false`.

## 이번 루프의 구체적인 새 결과

GL2022 (González-Lezana, Hily-Blant, Faure 2022, DOI 10.1063/5.0128598)의 원본 CSIC supplementary PDF(273554 bytes, SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`)에서 R18 원본 Git-blob 인증 파서를 다시 실행했다. 사용 채널은 **H⁺+HD(X,v0,J2)→D⁺+H₂(X,v0,J1)**. 원본 Table 2의 15 K `3.99(14)`와 55 K `2.92(11)`은 각각 **3.99×10⁻²⁰, 2.92×10⁻¹⁷ m³/s**다. 표기 괄호는 오차가 아닌 10의 음수 지수이며, 원자료는 온도 10개 점만 제공한다.

단일 고정 입사상태, 양의 온도 비의존 단면적 σ(E)≥0, 충돌 에너지 E의 공통 영점, 양의 문턱 Δ, 정확한 Maxwell 열평균이라는 명시적 조건 아래, `F(β)=k(T)β^(-3/2)/C`는 Eσ(E)의 양의 Laplace 변환이다. 따라서 모든 T_c<T_h에 대해

    Δ ≤ k_B ln[(k_h T_h^(3/2))/(k_c T_c^(3/2))]/(1/T_c−1/T_h).

**15/55 K의 source nominal 값으로 Δ≤15.186303821758897 meV**. 소수 맨 끝 ±0.005 mantissa 인쇄 반올림만 보수적으로 허용하면 **Δ≤15.191573204773210 meV**다. 이는 source-side 모델 필요조건이지, 개별 rate의 측정/이론 불확실도를 부여하는 것이 아니다. 모든 9개 인접 온도 쌍에서 가장 강한 상한이 이 첫 쌍이다.

R24의 문헌 혼합 BO 진단 Δ≈18.09049588228 meV는 조건부 저온 비를 5.12445518배 초과하고, R23 외부 분광 Δ≈20.95002099384 meV는 25.60830893배 초과한다. 즉 **두 후보값과 GL2022 원본 저온 rate는 선언된 하나의 T-비의존 양의 Maxwellian 단면적으로 동시에 표현할 수 없다**. 이 진단은 실제 GL2022 SQM 계산의 E 정의, PES-native 문턱 또는 저온 수치적분 입력·채널 개방을 직접 검증한 것은 아니므로, 원논문 물리 계산의 오류·물리적 Q 확정·일반 no-go로 승격하지 않는다.

Velilla2008의 37,170 cm⁻¹는 **H₃⁺ 최저점 대비 H₂+H⁺ 전자적 배열 해리값**이며 이종 핵의 (J2→J1) rate 문턱과 같지 않다. Lepers2019의 3.4 meV는 **HD(0,2)→H₂(0,0)** BO/TIQM이며, 원문에 H/D 이온화 전위 차이를 생략했다고 명시한다. 외부 H₂ J1–J0 분광 118.48684 cm⁻¹을 더한 18.090495882... meV는 교차 문헌 **approximate diagnostic**뿐이다. 실제 GL2022 Velilla PES 상태별 E_in/E_out와 동위원소 보정·핵 질량은 아직 미인증이다.

## 코드·검산 상태

- `src/threshold_audit.py`는 R21 immutable ZIP, 원본 PDF SHA, R18 parser Git blob, Table2 10개 데이터와 과학 NULL을 엄격 검증하고 model-free support bound와 p0 toy Arrhenius 진단을 **분리**하여 발급한다.
- 실제 현재 runtime Python 3.13.5: 신규 **42/42 unittest 정상 PASS**, **42/42 `python -O` PASS**, strict source CLI 새 결과 재생 PASS. 이전 34/34 모델 코드는 `R24_PRELIMINARY.json`에 역사적 결과로 남겨두고 새로운 `R24_MOMENT_BOUND.json`이 동작 의미를 확장한다.
- 독립 C++20 compiled long-double 런에서 bound 15.186303821758897272 meV, rounding 15.191573204773209784 meV, 후보 위반 5.124455180255/25.608308931674와 일치. Wolfram exact SI 입력/고정밀 산술로도 상한과 두 위반 계수를 확인했다. **기호 부등식 증명은 위의 양의 적분 argument로 제공**하며, CAS에 임의의 양의 함수를 맡기고 자동증명 PASS로 간주하지 않는다.
- 원본 PDF는 14페이지 렌더링, Table 2 본문·단위 확인. 세 번째 `R24_MAXWELL_SUPPORT.png/svg`과 기존 원본 rate·toy barrier의 합계 세 가지 진단 그림을 실물 렌더링으로 확인했다. 회귀 테스트에 `no physical Q`, `no actual owner`, no production, 34/49 unchanged 포함.

## 최신 브랜치 읽기 범위

2026-10-29 21시 기준 WU PR162, R22 PR160/161, REC PR157(실제 HD 방사 전이 callsite source-policy, 반응 4종 RHS 아님), CR PR124(He 에너지 예산), REI PR267/266 (H/He/동위원소 전자 feedback), BASS PR253 및 BASS_HE PR110을 GitHub로 조회·고정했다. 이 한정된 조사는 전체 native/generated chemistry dynamic call graph 부재 증명이 아니다. **소유자 실제 ACK 없음**, 타 저장소 수정 없음.

## 보존·후속 판단

`PASS_SCOPED_LAPLACE_POSITIVITY_BOUND / HOLD_GL2022_PES_AND_REAL_OWNER`. 이론·수치의 범위는 **확인된 original printed rates의 모델 일관성 필요조건**이며 완전한 source-error 인증이 아님. 아직 물리적 `Q_event`와 bath ΔB의 수치 삽입, 역반응/상세평형, error bars, full-A, L4, production 없음. 다음 최단 경로는 original GL2022 SQM cross-section raw energy arrays / GL2022 Fig1 native entrance/exit channel E / Velilla isotope nuclear-mass and IP prescription을 확보하고 **같은 15/55 K sample quadrature를 별도 재생해** 조건부 불일치를 원인별로 분류하는 것.

### 핵심 원전
- https://doi.org/10.1063/5.0128598 (GL2022 Eq 4 and supplementary Table 2)
- https://doi.org/10.1063/1.2973629 (Velilla2008 PES and electronic limit)
- https://doi.org/10.1093/mnras/stz1797 (Lepers2019 §3.2, separate j′=0 BO channel)
- https://academic.oup.com/mnras/article/500/1/430/5976295 (2020 spin-statistics erratum, thermal-rate aggregate only)
