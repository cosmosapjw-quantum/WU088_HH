# WU088_HH R27 | GL2022 × REC161 실제 출처 기반 HD 복사·반응 경쟁 척도

2026-10-30 KST. **Theory first, physical-data first.** 본 보고서의 새로운 물리적 계산 산출물은 `results/R27_CRITICAL_DENSITIES.csv`의 온도별 회전준위별 자료 60행(44행 수용, 6행 원문 인쇄영 미확정, 10행 원문 의심)이다. 기존 R26 700셀 원본을 수치 근사로 대체하지 않고, REC #161의 실제 출처 전사 Einstein A 값을 병치한다. 원본 고정: WU PR #165 `fa5d50561b001ae173e8bd038e3a18fdb1b65202` (parent PR164 `24302ab37ecc3b1220fb90a705ed375fe431b54e`).

## R1–R3: 정의, source provenance, 가정

- 2022 GL: González-Lezana, Hily-Blant & Faure, *JCP* 157 214302, DOI `10.1063/5.0128598`; 원 보충 PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`; 원본 토큰 tensor SHA256 `1258b1150577e732a8e175a16a7a78b09e69bc5a02407ed6e351f7e31eb3d7c8`. 10 T × 7 초기 HD J=0...6 × 10 최종 H2 J'=0...9의 계산된 state-to-state 반응률. 산란 계산(SQM), 실험 관측 수치 아님.
- 2021 Leiden HD `hd.dat`를 2026 REC PR #161에서 *가시 텍스트 전사*한 `LAMDA_HD_SOURCE_TRANSCRIPTION.json` Git blob `bd5a7f0e29ff6dd228cd8e927d6932b74d8cb4b9`; 8개 J→J−1의 전자기 자연 방출률 `A_J` [s^-1]. 원본 2289바이트가 **이번 R27에서 재취득/바이트 검증되지 않았음**. REC PR161 `5bf22a4258ba571e8aebb1cfedab9cafe7ac6481`, REC 2011 line-frequency 35Hz gate의 J≥2 실패는 이 A 전사의 byte-identification과 별개.
- Velilla et al. (2008) H3+ PES `10.1063/1.2973629`, 원 Fortran EPAPS `E-JCPSA6-129-612834`: 원 바이너리 미취득. Lepers, Guillon & Honvault (2019) `10.1093/mnras/stz1797`의 근사 BO `HD J2 -> H2 J'0 ≈ 3.4 meV`에는 isotope ionization 차이가 빠짐. R23 외부 분광 cycle 약 20.95002meV; **둘 다 GL2022 PES native threshold 확정 값 아님**.

## R4–R5: 후보 관측량과 실제 유도

외부로부터 상태 j의 HD 분자 한 개를 정해 놓고, 다른 경쟁 경로 없이 동일한 j에서 첫 사건으로 `H+ + HD(j) -> D+ + H2` 또는 `HD(j)->HD(j-1)+photon`을 관측한다고 가정한다. 일정 온도 T, 일정 양성자 수밀도 n_p에서 다음 두 사건의 위험률은

\[
\lambda_{\rm rxn,j}=n_p K_j(T),\qquad \lambda_{\rm rad,j}=A_{j\to j-1}.
\]

여기서 `n_p`는 cm^-3, `K`는 cm^3/s이므로 두 λ는 모두 s^-1. 논문 원본 Eqs.(6–7)의 선언된 최종 H2 핵스핀 정책을 한 번만 적용해

\[
K_j^{\rm spin}(T)=\sum_{j'=0}^{9}w_{j'}k_{jj'}(T),\quad
w_{j'}=\begin{cases}1/4 & j'\ \mathrm{even},\\ 3/4 & j'\ \mathrm{odd}.\end{cases}
\]

`k`는 원시 인쇄 SQM 상태별 속도계수, 가중의 재적용 금지. 별도 `raw_SQM`의 전량 단순합을 diagnostic으로만 남긴다. 두 독립 exponential 최초 사건모형이라면

\[
P(\mathrm{first\;event=photon}\mid j,T,n_p)
=\frac{A_j}{A_j+n_pK_j},\qquad
n_{p,\mathrm{crit}}(j,T)=\frac{A_j}{K_j(T)}.
\]

따라서 `n_p=ncrit`에서 복사 사건과 반응 사건이 각 1/2이다. 밀도-시간의 임의 시나리오 없이, 원출처 rate로 결정되는 **물리적 밀도 눈금**이다. 단, 여러 번 연쇄 복사·역반응·H2/전자 충돌·CMB 점유율·non-LTE stationary nine-level은 포함하지 않는다. `ncrit`는 원시 관측량이 아닌 **독립 출처 기반 파생 수치**다.

`J=0`은 자발 `0->-1` 선이 없어 제외. `J=7,8`은 GL2022 700셀 표에 초기 상태 반응률이 없으므로 제외. `J=5` 원본 Table1/Table2에 10T 전부 문자 동일한 행 복제 의심으로 부적격; `J=3,T=2505K` Table8의 `6.72(16)` 지수 의심으로 부적격. 인쇄 영이 포함된 J/T는 합산 diagnostics만 표시하고 ncrit는 NULL. 원시 rate의 임의 보정·온도 보간·외삽은 없음.

## R5 대안 검산: 2019 BO와 R24 positive Laplace 조건의 정량적 충돌

목표 **다른** 채널 `HD(0,2)->H2(0,1)`의 GL2022 인쇄 rate는 15K `3.99(14)`, 55K `2.92(11)` (단위 cm^3/s). 충돌에너지 `E_c`가 entrance-relative이며 온도 독립 `σ(E)≥0`이 `E≥θ`에만 지지되고 Maxwell 적분식의 prefactor만 T에 의존하면

\[
\frac{k(15)}{k(55)}\le\left(\frac{55}{15}\right)^{3/2}\exp\left[-\theta\left(\frac1{k_B15}-\frac1{k_B55}\right)\right].
\]

각 β는 meV^-1, θ는 meV. 결과는 R24의 조건부 상한 `θ≤15.186303821758897... meV`를 재현한다. 2019 BO 출처의 J'=0 조건부 `3.4 meV`에 독립 분광 H2 J'=1−J'=0 간격 `118.48684 cm^-1 ≈14.69049588 meV`를 결합하면 **18.09049588 meV**, 이 가정 아래 15K `k` 상한은 `7.7862e-15 cm^3/s` (원문 인쇄 `3.99e-14`의 1/5.124). R23 외부 분광 `20.95002 meV`를 가정하면 상한은 `1.55809e-15 cm^3/s` (1/25.608). 이는 **cross-paper conditional inconsistency diagnostic**이지 실제 native PES 단면적/threshold 측정값이나 원문 오류 증명이 아니다. 2019는 3.4meV 자체가 반올림 값이고 서로 같은 PES isotope correction/energy zero를 공유한다고 인증되지 않았다.

## R6–R10: 검증, 판정, 계산 연결

- Wolfram independent algebra *tool check*는 `J2 105K ncrit=3954.41818... cm^-3`, θ=15.18630, 두 15K 상한·인쇄율 대비 5.124/25.608을 재현. 이는 별도의 기호/수치 도구 검산이고 다른 저자의 blind science review는 아님. **R6 distinct-author=NOT_RUN**.
- Python Decimal75 `44`개의 source-positive/unsuspected `ncrit`를 생산, 6 printed-zero-censored, 10 suspect로 처리. 진단하는 출처 전사와 science gate를 분리한다. `C9 distinct-author=NOT_RUN`.
- 모델이 계산한 rate와 `ncrit`는 제한된 상태별 첫 사건 모형에 한해 **derived + numerically_checked**. 실제 cosmic history, `physical_Q`, bath heat, Boltzmann hierarchy, 9-level non-LTE owner, reverse rate, native PES cross section은 **unresolved**.
- 중앙 **34/49_UNCHANGED**, 이번 새로운 보조 물리 자료 노드 `R27_SOURCE_REACTIVE_RADIATIVE_CROSSOVER=1/1_SCOPED`. canonical node promotion=0. `OWNER_ACK=NULL`, `PES_NATIVE_THRESHOLD=NULL`, `PHYSICAL_Q=NULL`, `FULL_A=NULL`, `HH_R10=OFF`, `L4=false`, `PRODUCTION=NOT_ISSUED`.

자료 재현 및 코딩 연결은 `src/reactive_radiative.py`, `tests/test_reactive_radiative.py`, `results/R27_SOURCE_REACTIVE_RADIATIVE.json`, `results/R27_CRITICAL_DENSITIES.csv`를 사용한다.
