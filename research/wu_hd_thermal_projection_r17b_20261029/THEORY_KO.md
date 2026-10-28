# WU088_HH R17B: GL2022 reactive 총율에서의 조건부 sharp state-rate projection

**날짜:** 2026-10-29. **근거:** direct derivation, Wolfram exact 12/12, local Python 6 tests, independent-algorithm SciPy LP 120 cases. **물리적 채택:** 없음. **WU DAG:** 33/48 불변. **REI:** central last observed 28/88, PR257 working 33/88, 별도 DAG.

## 1. Source identity

González-Lezana, Hily-Blant, Faure, J. Chem. Phys. **157**, 214302 (2022), DOI **10.1063/5.0128598**, §III A, Eqs. (5)–(7), Fig. 5. H⁺+HD(v=0,j)→D⁺+H₂(v'=0,r)의 **SQM reactive** channels에 국한. j=0..8, r=0..9. 인쇄된 thermal TOTAL: 205 K에서 1.21, 295 K에서 2.21, 단위 10^-10 cm³/s. 이 두 소수점 인쇄값은 true physical-rate rigorous enclosures가 아니다. 원문 supplementary state-to-state raw ZIP은 확보되지 않았고 원본 SHA도 없다. EMAA/LAMDA HD-H⁺ 비반응성 충돌·분광 자료, EQM/TIQM 또는 별도 Arrhenius fit을 SQM 개별 행으로 대용하지 않는다.

## 2. Exact source prescription

ΔE_j=E_{0j}-E_{00}, b_j(T)=(2j+1)exp[-ΔE_j/(k_B T)]>0,
Z=Σ_{j=0}^8 b_j, p_j=b_j/Z, s_r=1/4 (r even), 3/4 (r odd).

K(T)=Σ_{j=0}^8 Σ_{r=0}^9 p_j(T)s_r k_{jr}(T) = Σ_i w_i k_i,
k_i≥0, w_{jr}=p_j s_r>0.

Σ_j p_j=1, Σ_r s_r=5, 따라서 Σ_{jr}w_{jr}=5 (**1이 아니다**). s_r를 최종 준위에 걸쳐 추가 정규화하면 원문 Eq.(5)–(7)의 total operator를 변경한다. Detailed balance, source uncertainty, temperature coupling은 미도입.

## 3. Theorem A: nonnegative sharp fixed-total bound (conditional)

고정 T에서 w_i>0, k_i≥0, K=Σ_i w_i k_i를 **정확한 입력**으로 가정하면 모든 a에 대해

0≤k_a≤K/w_a.

증명: K-w_a k_a=Σ_{i≠a}w_i k_i≥0. 상한은 k_a=K/w_a, 다른 모든 k_i=0으로 도달. 둘 이상의 양의 가중치에서는 특정 b≠a에 k_b=K/w_b, 나머지 0으로 두면 k_a=0을 도달. 이는 비음수 선형 **수학적 box**에서의 sharpness이며 실제 chemical selection rules/state manifold의 실현성은 보장하지 않는다.

Target HD(v0,j2)→H₂(v'0,r1)의 조건부 상계:

k_{2,1}(T)≤ [4 Z(T) e^{+ΔE_2/(k_B T)} /15] K(T).

에너지·partition sum source 인증 및 총율 rounding enclosure 없이 실제 rate 숫자를 인증하지 않는다.

## 4. Theorem B: sharp projection with joint rate box

주어진 고정 w_i>0와 l_i≤k_i≤u_i (u_i=+∞ 가능), Klo≤Σ_i w_i k_i≤Khi가 feasible이라고 가정. 목표 a에 대해 Slo=Σ_{i≠a}w_i l_i, Shi=Σ_{i≠a}w_i u_i라 두면

k_a ∈ [ max(l_a,(Klo-Shi)/w_a), min(u_a,(Khi-Slo)/w_a) ].

Shi=∞이면 (Klo-Shi)/w_a=-∞로 해석. 증명: 나머지 rate box의 연속 선형상은 정확히 [Slo,Shi]. 고정 k_a에서 [w_a k_a+Slo,w_a k_a+Shi]와 [Klo,Khi]가 만날 필요충분조건을 정리한 것. 각 endpoint에서 중간값 성질로 finite-dimensional box witness를 택할 수 있으므로 conditional sharp. 추가 물리 rate relation이 있으면 다시 평가해야 한다.

## 5. Theorem C: certified supplied Boltzmann-factor enclosures

외부 검증된 입력 0<L_j≤b_j≤U_j가 존재한다고 가정하면,

w^-_{jr}=s_r L_j/(L_j+Σ_{h≠j}U_h),
w^+_{jr}=s_r U_j/(U_j+Σ_{h≠j}L_h).

b_j에 대해서 증가하고 다른 b_h에 대해서 감소하는 비율이므로 정확하고 independent box corner에서 tight. 외부 인증된 K≤Khi와 w≥w^->0이면 k_jr≤Khi/w^-.

본 Python Fraction 모듈 자체는 Boltzmann exp의 rounding proof, 실제 원자·분자 에너지 출처, **물리적 source-total enclosure**를 생산하지 않는다. Fraction exactness는 명시적으로 공급한 **유리수 synthetic/conditional factors**에 한정된다.

## 6. Actual verification and limits

Wolfram 12/12 exact booleans true. 합성 b_j=2j+1 (전부 같은 전이 에너지라는 toy, GL2022 에너지 아님)에서 Z=81, w_{2,1}=5/108, K=121/100을 **printed total exact toy input**으로 가정하면 수학적 cap 3267/125 (printed units). 두 극단 rate vectors가 같은 total을 만듦. 다른 2-component toy w=(1/4,3/4), box ([0,3],[0,1/3]), K=1/2의 sharp target range는 정확히 [1,2]. Local 6 pytest PASS. 별도 SciPy HiGHS 120 finite-case LP vs exact Fraction formula: max absolute difference 4.440892098500626e-16, preset 1e-9 threshold PASS. Saved synthetic theta_rot scan figure visual audit completed. 실행 오류 1건은 wrong working-directory import (environment/path), 수정하고 6/6 PASS. 기존 R16/R17A 고정 시험은 재실행하지 않음.

**PHYS-MATH audit:** sign, positive weights, joint projection, source parity, units reviewed; physical source gap open. **PHYS-MATH-CODE audit:** typed Fraction inputs, target validity, infeasible boxes, endpoint witnesses, SI conversion tested. Independent **different-author** R6/C9 remains NOT_RUN; Wolfram or SciPy alternate algorithms are not that review.

R17B is an enabling mathematical/coding slice and **does not add one of WU's 48 original science nodes**. WU 33/48 unchanged, R17A 19/20 unchanged. HH_R10 OFF, production NOT_ISSUED, L4 false.

## 7. Only DAG-admissible next physical task

Source node **WU_HD_REACTIVE_STATE_SOURCE_NEXT**: fetch **original** GL2022 SQM state-to-state supplement bytes and immutable SHA; verify HD(v0,j2)→H₂(v'0,j'1) source row, temperature support, spin/parity/nuclear identity and uncertainties. Obtain independent energy/source-total enclosures, named REC/CR consumer with actual state-density-clock/full-A mapping, finite new budget and genuine distinct-author source review. Until then block physical parameter injection, temperature-rate extrapolation, physics-based fit and production claims.
