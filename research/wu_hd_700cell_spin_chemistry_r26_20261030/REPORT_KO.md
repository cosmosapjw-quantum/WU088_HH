# WU088_HH R26 | 원 GL2022 700셀 반응률과 2-회전상태 비가환 반응 이력

**기준:** R25 PR #164 HEAD `24302ab37ecc3b1220fb90a705ed375fe431b54e`, R24 PR #163 (직계 선행), R22 PR #160 read-only sibling. GL2022 Gonzalez-Lezana, Hily-Blant, Faure, *JCP* **157, 214302** (2022), DOI https://doi.org/10.1063/5.0128598. Supplementary PDF **273554 B** SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754` 원본 bytes 고정. 연구 시작일 2026-10-30 KST.

## 범위와 실제 원전 수치

Supplementary Tables **1–10**: H⁺ + HD(X, v=0, J=0..6) -> D⁺ + H₂(X, v′=0, J′=0..9), 온도 T=[15,55,105,255,505,1005,1505,2005,2505,3005] K. 이 표는 양자역학적 statistical scattering(SQM) **논문 계산값**이지 관측 측정값이나 physical PES Q가 아님. `m(xx)`는 rate 단위 `cm³/s`의 `m×10⁻xx`, `(xx)`는 표준편차 오차가 아님. 따라서 10×7×10 = **700개 셀** 전부 original literal 보존. 원문 독립 텍스트 추출기로 700/700 일치 (pdftotext-layout versus PyMuPDF 원본 페이지텍스트). R25 (초기 J2) 100셀 원문 토큰 SHA256 `f1b8e438a0117688e2497af1434227a42c8c158bab9f810b536b3ad2c36e4174` 동일, 기존 연구를 깨지 않음.

- 양의 인쇄 수치 **678셀**, `0.00(00)` 또는 `.000(00)` 인쇄 영 **22셀**. 해당 영은 `UNKNOWN_PRINTED_ZERO`, 물리적으로 정확한 0이 인증된 것이 아님. 포함한 `(J,T)`에서 complete rate/branching claim 보류.
- 원문 **의심 21셀**(양의 값): Table 1 J5/J′0과 Table 2 J5/J′1의 각 10개 온도 토큰이 동일(20 flag), Table 8 `(HD J3,H2 J′7,T2505 K)` 문자 그대로 `6.72(16)` 한 개. 원본 페이지 그림과 두 PDF 텍스트엔진으로 대조. 2505 K 인접 2005 K `4.71(11)`, 3005 K `8.36(11)`과 5차수 불연속. **임의로 6.72(11)로 교체하거나 전량 신뢰하지 않음**. 유효한 나머지 셀은 유지. 온도 보간/외삽은 하지 않음.

원 논문 본문 Eq. (5)는 HD J=0..8의 Boltzmann population, Eqs. (6–7)는 최종 H₂ J′ 짝수에 **1/4**, 홀수에 **3/4** 핵스핀 가중을 사용. 원본 SI Tables 1–10은 HD J=0..6만 제공하므로 **Table 11 전체 열평균은 이 700셀만으로 정확히 재현 불가**. Table 11 원전 열평균 10셀도 보존하되, 7상태로 renormalize해서 같은 숫자로 만들지 않음. 원시 SQM rate와 Eq6–7 effective rate는 서로 다른 이름·출력 객체.

## 실제 수치: 초기 HD 회전상태에 따른 생성 계수

다음은 J′=0..9의 원문 rate 합. **모두 원전 계산값의 합이며 관측 예측의 불확실성 범위가 아님.**

| Initial HD J | Raw K at 105K [cm³/s] | Raw K at 255K [cm³/s] | Eq6-7 effective K at 105K [cm³/s] | Gate |
|---|---:|---:|---:|---|
| 0 | 1.22190960205e-11 | 1.80972882825e-10 | 4.17557401538e-12 | source positive |
| 1 | 3.47407600235e-11 | 2.44558208078e-10 | 1.36010950176e-11 | source positive |
| 2 | 2.91803080028e-10 | 5.42831870521e-10 | 1.30461670021e-10 | source positive |
| 3 | 6.74332146015e-10 | 8.31986623994e-10 | 3.75248319504e-10 | 2505K J′7 separately suspect |
| 4 | 8.97788200024e-10 | 9.98318690632e-10 | 4.16947650006e-10 | source positive |
| 5 | 9.32134845014e-10 | 1.00083388823e-9 | 4.72300761261e-10 | **source duplicate flag**, no physical integration |
| 6 | 1.19830131002e-9 | 1.20843877134e-9 | 5.53625327518e-10 | source positive |

## 새로운 동역학: J=2, J=4 공동 H⁺ 자원과 온도 순서

이론 입력은 명시적 `n_H+(0)=1.3×10^6 m^-3, n_HD,J2(0)=6×10^5 m^-3, n_HD,J4(0)=4×10^5 m^-3`, 나머지 초기 species 0, 이론적으로 **외부 고정온도 105 K, 255 K를 각각 5×10^9 s 유지**, 고정부피, 오직 forward ion-exchange 채널. 역반응, HD 내부 재분배, photon transport, 팽창, 기체 냉각/반응열 없음. 각 온도에서 원문 10채널 rate를 m³/s로 변환한 양의 질량작용계를 구성. exact collision-clock 축약으로 2구간 적분 후 독립 full coupled ODE DOP853과 비교했다.

| 서로 다른 선언 정책 | 105→255 K 총 extent m^-3 | 255→105 K 총 extent m^-3 | 순서 차이 m^-3 |
|---|---:|---:|---:|
| raw SQM | 933144.0064547455 | 936568.2358469048 | -3424.2293921593 |
| Eq6–7 spin-weighted | 831246.2991579813 | 836068.6688582008 | -4822.3697002195 |

이 차이는 모델별 numerical trajectory result이며 실제 우주론 HD abundance와 혼동 금지. 물리적 출처는 rate SQM이고 초기 밀도·온도/기간은 **synthetic**이다. 출처 의심 J5와 2505 K J3를 사용하지 않아 이상 셀을 우회하는 것이 아니라, 출처가 검증된 채널에 적용 가능한 범위를 명시했다. 모든 이력의 H/D 핵수, 전하, 총 화학적 입자수 보존 절대 잔차 10^-6 m^-3 이하. 대조 `solve_ivp` 전체 상태 최대 오차 2×10^-4 m^-3 미만(제한 허용 기준), 온도별 정확한 계산율 동일. 분광학적 Boltzmann HD 초기 점유율은 사용하지 않았다.

**이론적 비가환성:** `F_A,F_B`를 (p,y2,y4) 반응 벡터장으로 두고 `[F_A,F_B]=DF_A F_B−DF_B F_A`로 정의하면 `[F_A,F_B] = p y2 y4 (K_A2 K_B4 − K_A4 K_B2)(0,1,−1)`. 서로 다른 J의 온도의존 K 벡터가 비례하지 않으면 O(t_A t_B) composition term이 존재한다. 반면 그 단계에서 total mass 및 proton bracket은 0으로, 총 진척량은 더 높은 order에서 차이를 보일 수 있다. Wolfram + SymPy exact Jacobian cross-check로 검산. 이 식은 생리학적/실측 법칙이 아니라 지정 2-state mass-action 모형의 유도다.

## 실제 구현·검증

`src/native_atlas.py`: SHA-locked PDF, 700셀 source-token, old R25 100셀 digest, Table11, 22 unqualified printed zeros, 21 source suspect flags, source status, distinct nuclear-spin policy, seven initial J and exact printed ten temperatures만 허용. Tampered token+recalculated self-digest를 **원본 hardcoded source SHA로 거부**. CLI exclusive-create. `src/finite_species.py`: 2-J example, collision clock scalar quadrature/root, conservation, policy separation, no Q. `tests/test_r26.py`: **38/38 normal and 38/38 Python -O**. 독립 PyMuPDF 추출 **700/700 same literal**, source-affine mutation guard, direct DOP853 independent implementation/4 scenarios and exact symbolic Lie bracket result. Figure 3개를 생성해 실제 확인했고 anomalous 2505 K cell을 plot에서 수리하지 않았다. Smoke/unit pass ≠ PES-native physical validation.

## DAG·권한·다음 연구

**WU canonical 34/49 unchanged**. 이번 R26 auxiliary production data-grid/conditional forward-science 1/1 scoped; P01 theory, P02 implementation/source data, P03 verification, P04 handoff. Distinct-author R6/C9 `NOT_RUN` (native subagent capability current turn unexposed). `GL2022_PES_native_threshold=null`, `physical_Q=null`, `physical_bath=null`, `source_rate_uncertainty=null`, `reverse_rate=null`, `owner_ACK=null`, `HH_R10=OFF`, `L4=false`, `full_A=null`, `production=NOT_ISSUED`. REC PR160 rotational source is nonreactive; CR PR126 exact He event solver no owner acknowledgment of molecular ion exchange; no foreign mutations. New R26 experiments are additive WU-only Draft, no main merge.

Next scientific unit: use a full source-qualified HD J=0..8 rate/cross-section source and same-PES rovibrational energies + original isotope BO convention to reconcile Table11 and GL2022 native threshold; optional contact with authors for actual scattering input and correction. Only then attach owner-acknowledged REC/CR four-species molecular forward source and scientifically qualify physical Q/rate uncertainties. Do not substitute unrelated neutral PES or inferred rate-to-Q values.
