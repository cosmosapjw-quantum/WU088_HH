# WU088_HH R24 결과 보고서 (2026-10-29)

**선택된 기여:** 원본 10개 상태별 k(T)의 양의 Laplace support 필요상한 도출, 35개 회귀/오류 처리 테스트, 분광학적 에너지 후보와의 조건부 불일치, 합성 양의 measure 역문제 비유일성. Production/physical energy admission 없음.

## 1. 근거와 최신 소유권

WU PR162 HEAD `2f214319ca8600475b1d4e85d1ca21a0249136a8`에서 분기. R22 PR160 `9db6f91debf54af1cc129538cfd6f6a716a78a56`은 형제 브랜치로 핀만 유지. R22 PR161 `4a9cc6f701aacbb8d09bbf4a169d5edd4c4fed47`은 상속된 spectroscopy ancestor. R18 Git 원문 row `08fdadd5dc366c00b8b546fcc9820bf030f3ae6c`, Table2 PDF SHA `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`. 소유자 직접 GL2022 cross sections 파일은 아직 미획득.

최신 REC #157 HEAD `e209cd0180c8bf199fc476c37e3cbf8d50394b6c`은 `lamda_hd.py` (radiative line physics) source policy firewall, 본 반응의 네 종 화학 소비자 아님. CR #124 HEAD `a6b49b352fed31587955d55b1cad30c0b55a81eb`는 helium energy-bin exact allocation, 이 반응 소유자 아님. REI #267 HEAD `779192ec55daf21e006b34bbc859681c9d2643ab`는 electron Jacobian, BASS #254 HEAD `8a56d15947435fe7dd83cc1b11347c145136321c`는 Bianchi-I MPFR source certificate, BASS_HE #110 HEAD `57d2de80bb192c4358c773cc327b9fad5b1e2ed2`는 DD angular bound. **각각 read-only context**, 교차 repo 이동·이식 없음. 실제 각 전체 동적 call graph 해석 및 ACK는 미실행.

## 2. 신규 과학 결과

기본 계약 A1–A3는 THEORY_KO §1에. 
`k(T)=sqrt(8 beta^3/(pi mu))∫_0∞ σ(E) E e^(−beta E)dE`, `beta=1/(k_B T)`에서 `sigma>=0`, source threshold theta면

`theta <= [ln(k(Tj)/k(Ti)) + 1.5 ln(beta_i/beta_j)]/(beta_i-beta_j)` for `Ti<Tj`.

15K k=3.99e−14, 55K k=2.92e−11 cm³/s로 조건부 θ≤**15.186303821758897 meV**. 인쇄 mantissa 반올림만 반영 시 ≤**15.191573204773210 meV**. R23 외부 spectroscopic θ≈**20.950020993840458 meV**와의 차 **5.76371717208156 meV**; strict same-energy-axis Maxwell model이면 15K rate 최대치는 source nominal의 **약 0.03904982569배**, 즉 source가 약 25.6083배 큼. 이것은 physical GL2022 native Q에 대한 사실 판정이 아니라 **source/model compatibility falsifier**임.

모든 45쌍에서 가장 낮은 상한은 (15,55)이며, 9개 인접 secant는 log convex necessary ordering을 충족. 이것만으로 physical positivity 또는 source-consistent energy zero가 확인되지 않음.

추가 합성 증인: 에너지 가중 양의 원자분포 두 개가 동일한 10개 Laplace 값을 갖지만 support onset은 20 meV 및 12 meV로 다름. mpmath125에서 sample 상대 잔차 <1e−125; 이는 실제 scattering cross section 추정이나 GL2022 rates fitting이 아님.

## 3. 코드 경로와 검증

`src/threshold_bound.py`: original rate token/상수/SHA/channel/가중치/열에너지 조건보호, 모든 pair 필요상한, log-convexity diagnostic, 비교만 출력; 물리 Q/bath null 강제. `src/positive_witness.py`: synthetic positive Laplace sample noninjectivity. `tests/test_bound.py`: source 계약과 변조/무단 승격 negative controls 및 양의 증인. `tests/independent_high_precision.py`: 구현 import 없이 mpmath85 부호/로그 재유도. `figures/render_diagnostics.py`: 실제 표본으로 그래프 3개 생성, 수동 시각 검사 완료.

실행: **35/35 unittest PASS**, **35/35 python -O PASS**, mpmath85 vs Decimal70 ≤5.2e−67 meV, Wolfram35 significant-digit agreement. 앞선 다른 대화의 R24 34/34 local quick analysis는 별도 증거이며 본 35/35 검산으로 자동 합쳐 세지 않음. 현재-turn native subagent capability NOT_EXPOSED; R6/C9 distinct author NOT_RUN.

## 4. 현재 불확실성 및 다음 작업

P0: GL2022 Eq3 E_total과 Eq4 collisional E가 실제 산란·평균화 코드에서 어떻게 연결되는지, original GL2022/Velilla native state energy basis 값과 H/D 이온화 보정을 확보해야 함. P1: R18 15K/55K numerical integration (실제 underlying σ data)가 있을 경우 독립 재적분과 threshold onset 재계산. P1: REC/CR 네 종 chemistry owner 경로를 실제 동적으로 열거한 다음 owner ACK를 받아야 함. 물리 소스 열방출, 역반응/상세평형, 실제 bath, full-A, production 모두 여전히 열림.

**판정** `PASS_CONDITIONAL_LAPLACE_BOUND_AND_NONINJECTIVITY_EXAMPLE / HOLD_PES_NATIVE_THRESHOLD_AND_PHYSICAL_Q`, 중앙 DAG **34/49**, 제한 workflow **18/20**, R6/C9 NOT_RUN, HH_R10 OFF, L4=false, production NOT_ISSUED.
