# PHYS18 실제 혼합 응답 적용

같은 COMMON과 고정 α의 원 C² family, 전역 λ,b∈[0,1]²에서 실제 두 half–Full 온도 결함 F=ΔT의 혼합 도함수를 포함했다. 원 interval 입력만 읽는 `run02`의 결과는

\[
\boxed{F_{\lambda b}\in[-2.668505746423,-2.118796636045]\times10^{-12}\ \mathrm K.}
\]

상한이 음수이며, 부호 margin은 적어도 2.118796636045×10⁻¹² K다. 원 전체 parameter 사각형의 네 꼭짓점 대비에도 같은 포함이 적용된다.

\[
\mathcal I=F(1,1)-F(1,0)-F(0,1)+F(0,0)
=\int_0^1\!\int_0^1F_{\lambda b}\,db\,d\lambda
\in[-2.668505746423,-2.118796636045]\times10^{-12}\ \mathrm K.
\]

이는 저장된 source/root/carry의 uniform mixed derivative를 실제 interval 연산한 뒤 정확한 적분 항등식으로 얻은 유한 대비다. 추가 꼭짓점 root 평가는 0회다. 원 입력과 실제 성공 출력을 보존하고, 독립 검토의 채택 상태는 `review/`에 연결한다.

## 1. 입력과 수학적 대응

`src/mixed_response_application.py`는 PHYS15에 결박된 원 PHYS14의 256-bit outward dyadic Fraction 연산만 import한다. imported module의 `main`과 source 평가 경로를 호출하지 않는다. h=625000000 s, Full 길이 2h를 원 binary64 bit leaf에서 정확히 읽고 확인한다. f₁,f₂는 각각 exact(nHe_stored)/exact(nH)다. 두 source의 Hmean bit leaf는 모두 `3d06849b86a12b9b`다.

| 저장 입력 | 적용 위치 |
|---|---|
| PHYS09 first_half/full `U,V,W` | U₁,V₁,W₁와 UF,VF,WF. W는 ordinary ∂λb이며 factorial 계수가 없다. |
| PHYS14 `gas_response/U,V,W` | carried second-half U,V,W |
| PHYS11 first-half incoming/absorbed/outgoing_joint와 PHYS14 incoming/absorbed/outgoing/guard | mixed 2-jet primitive를 원 signed carry와 교차; 800 scalar 교집합 |
| PHYS15 원 first_half/full nonphoto,q jets | C² value/gradient/Hessian, source 시간차와 공간차 |
| 원 Full `G_gg,G_g_lambda,G_g_b,G_lambdab` | Full residual의 Hessian; gas 0–3, λ 4, b 5 슬롯. G_gg의 −2h 계수를 그대로 유지한다. |
| PHYS16 correlated endpoint와 endpoint remainder | g₁,g₂,gF, d, ΔT, s, QF 및 photon 링크 |
| PHYS17 parameter response | dλ,db,sλ,sb와 Fλ,Fb,T₂λ,T₂b,ΠFλ,ΠFb |
| 원 Full `UNIFORM_ARITHMETIC.json` | 같은 C,B,q,S. q의 원 binary64 값 0.00011736830563768177, S의 원 exact binary64 leaves를 재사용한다. |

각 읽은 파일의 경로·크기·SHA-256은 `run02/results/MIXED_RESPONSE_RESULTS.json/input_identities`에 있다. 원 24개 계약 입력의 검증은 상위 `evidence/intake/INPUT_IDENTITY_CHECK.json`에 연결한다. 실제 원 `G_lambdab`는 작은 subnormal signed 구간이며, 각 구간이 정확한 source identity Hλb=0을 포함함을 확인한 뒤 0과 교차했다.

## 2. 실제 계산 경로

혼합 2-jet은 (value,U,V,W)를 ordinary 편도함수로 저장한다. 곱은

\[
(ab)_{\lambda b}=a_{\lambda b}b+a_\lambda b_b+a_b b_\lambda+ab_{\lambda b}
\]

로, reciprocal은

\[
(a^{-1})_{\lambda b}=2a^{-3}a_\lambda a_b-a^{-2}a_{\lambda b}
\]

로 전파한다. 33개 photon과 number/energy guard를 포함한 35개 좌표에서 PHYS15의 같은 일곱 sector graph를 계산했다. sλb는 원 W−W₁와 stage mixed 식 M13을 교차했고, ΔA₁=ζA₁A₂의 ζ에 그 작은 차이를 넣었다. Photon number와 energy mixed ledger의 residual 두 개가 각각 0을 포함한다.

Gas 혼합 residual은 M8–M11로 평가한다. M9/M11은 PHYS17에서 완결한 density pullback의 첫 방향미분을 W₁,V₁에 각각 적용한다. Stage Hessian 차는 원 두 signed Hessian 범위의 차로 직접 포함한다. Endpoint의 source Hessian 차도 C² signed 범위의 차를 사용한다. HI photon Hessian 차와 birth gradient 차는 M5/M6의 dₓ 인수와 양의 분모를 유지한다. HH gradient 차는 M7의 원 q Hessian 선적분 포함으로 계산한다.

직접 M3와 상관 M4 각각의 RHS를 같은 Full JF로 전달했다. JF는 원 Full centre gradient와 Hessian으로 endpoint box에 제한하고 원 A_Gg와 교차한다. C,B,q,S로 절대 majorant의 4×4 유리수 선형계를 풀고 signed fixed-point 포함을 3회 제한한다. 이후 원 W−WF의 독립 포함까지 교차한다.

## 3. 수치 결과

| 관측량 | 상관식·직접식·원 carry의 최종 교집합 |
|---|---:|
| ∂λb dₓ | [3.428209698898, 4.498894132315]×10⁻¹⁷ |
| ∂λb dᵧ₁ | [−2.296697834724, 0.5758083648551]×10⁻²² |
| ∂λb dᵧ₂ | [−9.420366340430, −2.612148448548]×10⁻²⁴ |
| ∂λb d_w, eV/H | [−4.336773175632, −3.600882004347]×10⁻¹⁶ |
| ∂λb ΔT, K | [−2.668505746423, −2.118796636045]×10⁻¹² |

온도는 M15의 같은 ΠF>0과 nF=CTe_wᵀ−TFℓe를 사용했다. M16에서 T₂λb를 구성하고, 여섯 quotient geometry 항을 별도로 보존했다.

| 비교 경로 | ∂λb ΔT 포함, K |
|---|---:|
| 원 W₂−WF 직접 차 | [−6.545446896199×10⁻¹², 6.907235324700×10⁻¹³] |
| M3 직접 mixed implicit 식 | [−3.819468564815×10⁻¹², −8.533085984866×10⁻¹³] |
| M4 상관식과 최종 교집합 | [−2.668505746423×10⁻¹², −2.118796636045×10⁻¹²] |

최종 폭은 원 carry 차보다 13.16363562486배, M3보다 5.395871944515배 작다. PHYS17의 |I|≤1.958485175177039×10⁻⁹ K와 비교하면 magnitude upper bound를 733.9257851712배 줄였다. 이 비율은 원 결과의 exact interval endpoints로 별도 `readout01`에서 계산했다.

## 4. 같은 inverse와 온도 covector에서의 기여

`readout01`은 원 25개 RHS sector를 세 그룹으로 정확히 나누고, 각 합을 동일한 JF inverse와 온도 row로 전달했다. 관측량의 기여는 특정한 이 정확한 분해를 기준으로 한다.

| 그룹 | 온도 혼합 기여, K |
|---|---:|
| 다섯 HH gradient 항 | [−2.329668009361, −1.928397581837]×10⁻¹² |
| 일곱 photon sector | [−3.024678223968, −1.735793802686]×10⁻¹³ |
| 나머지 gas·endpoint 항 | [2.819648272515×10⁻¹⁶, 1.140914739344×10⁻¹⁵] |
| 유한 온도 분모 geometry | [−3.666218766444, −1.794167181955]×10⁻¹⁴ |

주요 HH 항은 −hDq₂[s_b]νH와 −Hgλ(gF)d_b이며, 각각 약 −1.1×10⁻¹² K다. Photon 내부에서는 birth backward Euler 항이 [−2.162954512589,−1.072305628653]×10⁻¹³ K이고 opacity-change 항이 [−8.543779577136,−6.708098635518]×10⁻¹⁴ K다.

폭의 상위 세 항은 HH_gradient_birth_increment 2.014687686434×10⁻¹³ K, endpoint_HH_birth_defect 1.994124866133×10⁻¹³ K, birth_backward_euler 1.090648883936×10⁻¹³ K다. Endpoint source Hessian 차의 폭은 4.576255016977×10⁻¹⁶ K다. 현재 C² 자료에서 이 공간차를 직접 포함해도 실제 혼합 부호가 닫힌다.

## 5. 유한 parameter 사각형의 귀결

0≤λ₀<λ₁≤1, 0≤b₀<b₁≤1인 임의의 양의 면적 a=(λ₁−λ₀)(b₁−b₀)에 대해

\[
F(\lambda_1,b_1)-F(\lambda_1,b_0)-F(\lambda_0,b_1)+F(\lambda_0,b_0)
\in a\,[-2.668505746423,-2.118796636045]\times10^{-12}\mathrm K.
\]

따라서 온도 결함은 이 사각형들에서 엄격한 submodularity를 갖는다. b가 증가하면 음의 HH 방향 Fλ가 더 작아지고, λ가 증가하면 양의 birth 방향 Fb가 감소한다. 각 1차 도함수의 기존 부호는 PHYS17의 전역 포함으로 유지된다.

## 6. 실제 실행·실패·재현

| 실행 | 종료 | wall s | CPU s | peak RSS KiB | 실제 산출물 |
|---|---:|---:|---:|---:|---|
| run01 | 1 | 0.515569 | 0.475653 | 43700 | 원 guard schema의 정수 key 접근 실패 로그와 FAILED_CODE.py |
| run02 | 0 | 0.967359 | 0.930019 | 43744 | MIXED_RESPONSE_RESULTS.json, SUMMARY.json |
| readout01 | 0 | 0.114273 | 0.070526 | 17568 | FINITE_MIXED_READOUT.json, SUMMARY.json |

run01의 입력 schema 오류는 PHYS14 guard가 각 slot에서 `number`, `energy_eV_per_H`를 갖는 dict라는 원 구조를 확인하고 그 두 이름으로 접근하도록 고쳤다. 원 코드와 PRE_RUN/RUN/STDERR를 보존했다. 두 성공 실행은 새 source callback, 반응률 fit, 비선형 root solve, history replay가 각각 0회다. 실행 환경·명령·code identity는 각 PRE_RUN/RUN.json에 있다.

재현은 성공한 출력 디렉터리를 바꾸지 않고 새 경로에서 실행한다.

```bash
python3 HH_PHYS18_THEORY_20261013_v1/src/mixed_response_application.py \
  --parent15 HH_PHYS15_THEORY_20261012_v1 \
  --parent16 HH_PHYS16_THEORY_20261013_v1 \
  --parent17 HH_PHYS17_THEORY_20261013_v1 \
  --output /absolute/new/phys18_mixed_results
```

결과에는 wall time과 peak RSS가 들어 있으므로 재실행 파일은 같은 과학 구간을 얻어도 byte hash가 달라질 수 있다. `readout01`은 실제 채택 후보 run02의 immutable byte identity에 결박되어 있으며, 원 파일을 입력으로 재현한다.

```bash
python3 HH_PHYS18_THEORY_20261013_v1/src/mixed_response_readout.py \
  --parent15 HH_PHYS15_THEORY_20261012_v1 \
  --result HH_PHYS18_THEORY_20261013_v1/checks/application/run02/results/MIXED_RESPONSE_RESULTS.json \
  --output /absolute/new/phys18_mixed_readout
```

현재 source/result의 정확한 크기·SHA-256과 실행 파일 목록은 `APPLICATION_MANIFEST.json`에 있다.
