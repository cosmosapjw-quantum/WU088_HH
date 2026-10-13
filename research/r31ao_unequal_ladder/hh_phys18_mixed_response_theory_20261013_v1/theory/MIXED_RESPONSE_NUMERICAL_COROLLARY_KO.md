# PHYS18 수치 따름정리 — 음의 HH–birth interaction

원 PHYS15–17과 같은 고정 계수·COMMON·전역 매개변수의 C² 계열에서 다음 전역 포함이 성립한다. 아래 값은 run02 결과의 외향 decimal 표시이며 정확한 rational endpoint는 MIXED_RESPONSE_COROLLARIES.json과 원 결과 JSON에 있다.

## 1. 기체 혼합 결함

| 좌표 | ∂λb(g₂−gF) 포함 | 단위 |
|---|---|---|
| x_HII | [3.428209698898E-17, 4.498894132315E-17] | 1 |
| y_HeII | [-2.296697834724E-22, 5.758083648551E-23] | 1 |
| y_HeIII | [-9.420366340430E-24, -2.612148448548E-24] | 1 |
| w | [-4.336773175632E-16, -3.600882004347E-16] | eV/H |

## 2. 온도 혼합 응답과 교차항

| 경로 | ∂λb ΔT 포함 (K) |
|---|---|
| 원 carry를 각각 빼기 | [-6.545446896199E-12, 6.907235324700E-13] |
| 직접 implicit 식 | [-3.819468564815E-12, -8.533085984866E-13] |
| 상관식·전체 교집합 | [-2.668505746423E-12, -2.118796636045E-12] |

상관식의 위끝점은 −2.118796636045×10⁻¹² K보다 작거나 같다. 모든 admissible fixed α에서 음의 부호가 닫힌다. PHYS17의 interaction magnitude 경계 1.958485175177039×10⁻⁹ K는 이번 2.668505746423×10⁻¹² K로 약 733.93배 줄었다.

같은 음의 interval을 모든 양의 면적 rectangle의 면적에 곱하면 해당 네 모서리 contrast를 포함한다. 따라서 ΔT는 λ,b에 대해 strictly submodular다. Birth 증가에 따라 음의 HH marginal response가 더 작아지고, HH 증가에 따라 양의 birth marginal response도 더 작아진다. 이는 현재 전역 1차 부호와 함께 성립한다.

## 3. 현재 완결된 축 보존 재구성

\[
F_{\mathrm{ax}}=F(\lambda,0)+F(0,b)-F(0,0),\qquad
F-F_{\mathrm{ax}}\in\lambda b[-2.668505746423,-2.118796636045]\times10^{-12}\ {\rm K}.
\]

\[
F=F_{\mathrm{ax}}-2.393651191234\times10^{-12}\lambda b+R_m,\qquad
|R_m|\le2.748545551890\times10^{-13}\lambda b\ {\rm K}.
\]

같은 fixed α의 축 함수값은 그대로 남겼다. 이 두 식은 현재 mixed 응답 포함을 적분한 완료된 결과다. 다음 pure curvature는 축 자체를 직선으로 바꿀 때의 오차를 다룬다.

## 4. 실제 기여와 정칙성

같은 Full inverse와 온도 covector를 거친 HH gradient 묶음은 [−2.329668009361,−1.928397581837]×10⁻¹² K, 일곱 photon chronology 묶음은 [−3.024678223968,−1.735793802686]×10⁻¹³ K다. 나머지 gas·endpoint 기여는 [2.819648272515,11.40914739344]×10⁻¹⁶ K이며 온도 geometry는 [−3.666218766444,−1.794167181955]×10⁻¹⁴ K다.

혼합 폭의 가장 큰 두 항은 −h Dq₂[s_b] ν_H와 −H_gλ(gF)d_b다. 원 C² source Hessian 공간차의 기여 폭은 약 4.57626×10⁻¹⁶ K로 작다. 원 signed Hessian 범위만으로 이번 mixed 부호를 결정했다.

## 5. 재사용 근거와 실제 실행

주 application은 src/mixed_response_application.py, 결과는 checks/application/run02/results/MIXED_RESPONSE_RESULTS.json이다. 유한 rectangle·기여 묶음은 checks/application/readout01/results/FINITE_MIXED_READOUT.json에 있다. 새 tensor·scalar 검산은 checks/wolfram, 독립 수용 판정은 review/INDEPENDENT_REVIEW.json 및 review/DECISION.json에 결박한다.

주 application 기록의 wall time은 0.853057 s, peak RSS는 43600 KiB다. 새로운 source callback, 비선형 root solve, physical history replay는 모두 0회다.

다음 HH_DEFECT_PARAMETER_CURVATURE의 pure 응답은 not_run이다. 첫 half Jacobian의 유한 inverse readiness만 CURVATURE_INPUT_PREFLIGHT.json에서 실제 exact Fraction 계산으로 준비했다.
