# WU R30 이론 연구: 실제 HD 회전선과 화학적 흡수 전 광자-생성물 결합분포

**범위:** 선행 WU R29 원본 SOURCE ZIP `65ed097acb02f8eb91ff6518c26c8ad61e721e3fadd9b904aa2157e3508cb0ea`, Git Draft PR168 HEAD `d0850bd67e20304c566737b7a92bfc45f4849b93`. 실제 연구 산출물은 **새 측정된 선 중심값을 사용한 독립 재계산**이다. 새 실험, 원본 양자 산란 σ(E), 전 우주 진화 결과가 아니다. WU canonical 34/49에서 신규 central promotion 0.

## 1. 입력 근거 및 해석

1. GL2022 JCP157,214302 DOI `10.1063/5.0128598`: H+ + HD(v=0,J=0…4) -> D+ + H2(v'=0,J'=0…9) 열반응률, 350개 양의 인쇄 source 셀; 비반응 HD 하향 rate 70개, 모두 원본 7개 공통 T=(55,105,255,505,1005,2005,3005) K. 자료 출처는 원본 273554 byte SI PDF SHA256 `a65b1cba4208552e7eac6341b462487b23c5afe79f3ba0d2ca009fdee7dd1754`, R29 원본에 중첩 보존. 원본 15 K,1505 K,2505 K를 임의 보간하지 않는다. 출처 의심 J5는 이 모형에 포함하지 않는다.
2. REC161의 Leiden2021 HD Einstein A 전사: \\(A_{1,0},A_{2,1},A_{3,2},A_{4,3}\\)는 상속 원본을 그대로 사용, 2021 원본 `hd.dat` raw byte가 이번 실행에 신규 확보된 것은 아니다.
3. **신규 독립 원전 자료**: Sung et al., *J. Quant. Spectrosc. Radiat. Transfer* 295,108412 (2023 print; online 2022), DOI `10.1016/j.jqsrt.2022.108412`의 296K HD v0 J1→0,2→1,3→2,4→3 **실측 적합 선 중심** 89.22792,177.84141,265.24055,350.85401 cm^-1. 정확한 외부 데이터 주체는 REC Draft PR164 HEAD `e050b97b7d5c6c0929062fafd7333e0164112399`, source file `data/LAB_INPUT.json` Git blob `23626dd9a77aa4e6214f6f9c792ea18270b3940c`. 이 실행의 파일은 위 네 값만 **검증된 재전사**이다. 원본 연구 논문 PDF 바이트, 진정한 공분산·총 systematic uncertainty가 확보되었다고 주장하지 않는다. 괄호의 적합 오차는 총 실험 오차가 아니다.
4. 비교 대조값은 REC162의 *2011* CDMS v2 인쇄 9준위 간격이다. Sung 인접선 네 값을 누적한 *별도* 5준위 측정 적합 사다리 \\(\widetilde E_J^{Sung}=\sum_{r=1}^J\widetilde\nu_r^{Sung}\\)를 새 상세평형 입력으로 사용한다. 이론의 분광 중심에 단순한 Gaussian noise나 미제공 H2 충돌압력 이동을 보정하지 않는다. T=55–3005 K는 반응률 source T이므로 Sung 296K fit centers는 고정된 무압선의 조건부 값으로 쓰는 것이다.

## 2. 유한상태 과정과 자세한 원리

HD의 transient 상태 `J=0,1,2,3,4`; 화학반응 후 최종 H2 `J'=0,...,9`는 absorbing output. 양성자 수밀도 n은 외부 고정 [cm^-3], 온도 T 고정. 방사선 피드백, 자발복사 외 별도의 자극복사, H2/전자 collider, chemical reverse, 다른 진동 생성물, 열역학 Q 및 cosmic expansion 없음.

원본 비반응 하향 \\(k_{J\to I}^{down}\\) (I<J)에 상세평형을 적용한 상향 전이는

\\[ k^{up}_{I\to J}(T)=k^{down}_{J\to I}(T)\frac{2J+1}{2I+1}\exp\left(-\frac{hc(\widetilde E_J^{Sung}-\widetilde E_I^{Sung})}{k_B T}\right). \\]

GL2022 화학 출구 채널 확률은 \\(q_{Jk}(T)\\)이며 `raw_SQM` 또는 저자 Eq.(6)–(7)에 맞는 최종 H2 홀짝 가중 \(w_k=1/4,3/4\) 두 개 *명시적 조건부 정책*을 별도로 계산한다. 각 반응 출구 경로는 \\(r_{Jk}=n w_kq_{Jk}\\) s^-1. 한 상태에서 모든 화학 반응 rate \(r_J=\sum_k r_{Jk}\).

칼럼 생성자 `G(target,source)`에는 충돌 state-to-state 화살표, 자발복사 \\(A_{J\to J-1}\\), 화학 흡수 \(r_J\)가 포함된다. `G0`는 **첫 광자를 흡수 사건**으로 바꿔 복사 항의 off-diagonal을 없애고 원래 diagonal의 복사 사멸률을 보존한다. \\(x(t)=e^{Gt}e_{J_0}\\), 점유시간 벡터 \\(m=(-G)^{-1}e_{J_0}\\), 첫 광자나 반응 전 점유시간 \\(m_0=(-G_0)^{-1}e_{J_0}\\).

**신규 관측량 식:**

\\[\begin{aligned}
\mathbb E[N_{J\to J-1}] &= A_{J,J-1}m_J, \\
P(\hbox{first emitted photon is }J\to J-1) &= A_{J,J-1} (m_0)_J,\\
E_{\rm emitted} &= \sum_{J=1}^4 hc\widetilde\nu_J^{Sung} A_{J,J-1}m_J,\\
P(K=k,\,N_{\rm photon}=0)&=\sum_J r_{Jk}(m_0)_J,\\
P(K=k,\,N_{\rm photon}\ge1)&=\sum_J r_{Jk}(m-m_0)_J.
\end{aligned}\\]

\(K\)는 **제한된 반응 출구에서 형성된 H₂(v'=0,J'=k)**. 위의 마지막 줄은 첫 광자 이후의 Markov 이력을 포함한 사건 결합확률이며, 두 확률의 합은 R29의 생성물 확률을 정확히 재구성한다. 초기 단일 HD 분자의 반응 완료 전 누적 photon energy [J]는 **gas net cooling/heating, photon energy density, observational line luminosity가 아니다**. 초기 HD 밀도를 외부에서 추가 지정해야 방사율 [W/m³]로 변환할 수 있다.

**수학적 검산:** M-matrix의 양의 resolvent와 column 소멸수지에서 \\(\sum_k P(K=k,N=0)+\sum_{J=1}^4 A_J(m_0)_J=1\\), \\(\sum_k P(K=k,N\ge1)=P(N\ge1)\\). 첫 photon과 생성물의 joint distribution으로도 양의 확률과 normalization을 확인한다. Wolfram 2-state 기호 한계의 세 항등식은 PASS; 이는 독립 저자 심사는 아니다.

## 3. 실제 결과, 정확한 수치 영역

7 T × 정책 2 × 명시적 `n/ncrit_J2`=0.1,1,10 × 초기 J=0..4 => **210개 독립 모델 상황**. 각 4개 선에 대해 기대 광자수, 첫 photon 선별 확률, 광자 에너지·파장 => **840개 선별 결과**. 각 10개 H₂ 출구에 `no photon`, `≥1 photon` 공동 확률과 조건부 product probability => **2,100개 결합 결과**. 이는 기존 R29 수치를 출력 모양만 바꾼 것이 아니라 새로운 원전 분광 측정값에 따른 레벨/상향 충돌 재계산과 새 photon/product joint observables를 계산한 것이다.

105 K, J0=2, spin effective, n=3954.4181821071797 cm^-3:
- \\(P(N\ge1)=0.47362861731084116\\), R29 old 2011 ladder 대비 \(+9.98606311×10^{-8}\).
- \\(\mathbb E[N_{ph}]=0.8880279503111301\\), old 대비 \(+3.93561785×10^{-7}\).
- \\(E_{emitted}=2.580602925218754×10^{-21}\\) J/초기 HD = 0.016106856575332843 eV/초기 HD.
- J1→0 (112.072544 μm): 기대 0.355305481 photon/초기 HD; J2→1 (56.229874 μm): 0.493672363; J3→2 (37.701626 μm): 0.038415516; J4→3 (28.501883 μm): 0.000634591.
- H₂ 최종 J' 홀수 비중: photon 없이 반응한 조건에서 0.5994250739850665; photon ≥1 후 반응한 조건에서 0.5849454149276438. 이는 조성 변화의 **조건부 joint-model 예측**, 실측 화학 분기라고 하지 않는다.

## 4. 진척도와 남은 원전 연결

이번 R30 추가 과학 보조단위 **1/1 scoped scientific result**, 중앙 **34/49 유지**, 물리적 core 승격 **0**. R6/C9 distinct-author NOT_RUN, native subagent tools 미제공. 원본 EMAA 2023 171×25 H+ 충돌 ASCII raw bytes 미확보; 실제 browser의 selector로 내려받아 원본 SHA와 ID crosswalk를 구성해야 한다. Velilla2008 E-JCPSA6-129-612834 PES Fortran, 동일 PES 에너지영점과 σ(E), 역반응, source-rate uncertainty, 실제 분자반응 owner ACK 모두 미해결. `PHYSICAL_Q=NULL, PES_NATIVE_THRESHOLD=NULL, OWNER_ACK=NULL, HH_R10=OFF, FULL_A=NULL, L4=false, PRODUCTION=NOT_ISSUED`.

실제 수행·증거는 `README_REPLAY.md`, `results/`, `evidence/`, `stages/`에 있음. 20개 단계 checkpoint는 20개 독립 실험 실행과 다르다. 동일 저자 mpmath75·Wolfram/targeted tests는 독립 저자 R6/C9를 대체하지 않는다.