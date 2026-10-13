# WU088_HH PHYS22: 유한 HH 응답의 직접 포함

2026-10-13. 중단된 실행에서 interval v3와 xAct 출력을 회수하고, 별도 exact-rational 폐쇄 검사와 결과 문서를 완성했다.

**채택 결과:** 같은 IC/source/geometry/closure를 갖는 warm P01의 명시적 실수값 명목 모델에서, 끝점 t=1e11 proper seconds의 HH-ON/OFF 차이는 다음 구간에 포함된다.

\[
\Delta T\in[-5.83789,-5.57637]\,10^{-11}\ {\rm K},\qquad
\Delta e\in[7.60418,8.28307]\,10^{-16}\ {\rm electrons/H}.
\]

전체 gas4 + photon2904 계를 유지한다. 같은 공통 영역이 모든 λ∈[0,1]의 해를 포함하며, 각 λ>0의 응답은 위 구간의 λ배로 제한된다. 이는 균일 포함식이며 정확한 선형 응답을 가정하지 않는다.

## 근거

전체 구간 source·opacity 상계로 광자를 `m_i(0) exp(-κ_i^+ t_f) ≤ m_i ≤ m_i(0)+t_f S_i`에 포함한 뒤, gas의 first-exit 영역을 닫았다. 4개 gas 좌표의 적분 RHS 상계/box 반경 비는 0.03430414, 0.07035527, 0.03333276, 0.62272114이다. T box는 약 49999.63846..50000.36154 K다.

두 비선형 방정식의 차이에서는 실제 공통 외부 source가 소거되고 광자 damping은 diagonal nonnegative 적분인자로 남는다. 양의 비교행렬

\[
P=t_f A^+ +\tfrac12t_f^2 B^+ C^+
\]

에 대해 고정 단위 scaling으로 얻은 norm은 0.03688471538571053<1이다. 따라서 `u=(I-P)^(-1)t_f|ν|q^+`와 `v=Pu`가 각각 유한 gas 변화와 직접 HH 노출량 대비 feedback을 제한한다. 온도는 정확한 quotient `(C_T Δw−T_0 Δe)/(Π_0+Δe)`로 읽었다. 전체 증명은 [8쪽 보고서](report/REPORT_KO.pdf)와 [LaTeX](report/REPORT_KO.tex)에 있다.

Wolfram Engine 15.0.0 / 40자리 Interval 계산을 사용했다. 별도 Python Fraction 계산 24개 검사, xAct를 포함한 11개 항등식 잔차가 모두 통과했다. Fraction 검사는 저장된 Wolfram majorant 이후의 대수 폐쇄를 독립적으로 재계산한다. 같은 assistant의 다른 산술·기호 경로이며 외부 심사자는 참여하지 않았다.

## 모델 및 수 표현

Receiver: `cosmosapjw-quantum/rei_bianchi@a5c958c414dea41216b445c05f58df837f05cacb`.
LRS Bianchi I dust+Λ, test gas/radiation, warm primary HM12, Case A escape. 상수와 source 표는 명시된 십진수를 정확한 실수로 해석하고, NPZ 초기값은 exact binary64 dyadic 값으로 고정한다. `f=3/38`. 원자 fit의 물리적 오차와 native roundoff는 별도 연구 항목이다.

이 결과는 PHYS21의 PL-baseline tangent를 유한 효과로 단순 승격한 것이 아니라, 동일 유한 효과를 **직접 두 해 차이의 포함**으로 닫은 결과다. PHYS21의 숫자를 유한 온도 응답의 근사로 쓰면 절대 오차는 `1.513403708821e-12 K` 이하이다.

## 파일

- `DECISION.json`, `RESEARCH_STATE.json`: 결과 채택, R1–R10, 방법 교체 근거.
- `results/interval_result_v3.json`: exact rational interval majorants와 최종 포함.
- `checks/EXACT_AUDIT.json`, `checks/audit_certificate.py`: 별도 유리수 폐쇄 검사.
- `wolfram/finite_response_interval_v3.wl`, `wolfram/xact_checks_v2.wl`: 실제 실행된 기호·구간 검산 입력.
- `inputs/`: 원 NPZ, HM12 emissivity와 고정 receiver source. `INPUTS.json`에 hash.
- `raw/`: 실패한 v1, v2, v3, 원 xAct, 실제 실행 로그와 복구 inventory.
- `HANDOFF_KO.md`, `REPRODUCE.md`: 다음 실제 연구와 재현 명령.

다음 단위는 **PHYS23_HH_RATE_ENVELOPE_TO_OBSERVABLE_BUDGET**이다. 이미 닫힌 유한 명목 응답을 반복하지 않고, 채널이 일치하는 rate uncertainty와 실제 수신 observable 예산을 연결한다.
