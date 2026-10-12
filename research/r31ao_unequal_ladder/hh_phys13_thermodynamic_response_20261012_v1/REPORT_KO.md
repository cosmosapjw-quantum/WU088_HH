# WU088_HH PHYS13 — 유한 온도·전자 응답과 냉각 기여

2026-10-12. 같은 소스 계열의 PHYS12 결과를 실제 source 온도와 총 자유전자 수로 옮겼다. **HH는 두 보존된 첫 단계 모두에서 온도를 낮추며, 선택한 HH 강도 경로의 냉각 가운데 약 31.7–32.0%는 입자 수 증가의 기여다.** 원 소스와 coefficient tuple을 유지한 조건부 유한 응답이다. 최종 과학 판정은 `review/DECISION.json`을 따른다.

## 1. 실제 새 결과

미래 HH 강도 λ를 0에서 1로 바꾸며 미래 birth 진폭은 b=1로 고정한다. 과거 HH ON 이력과 기존 광자는 같은 COMMON에 남는다.

| 관측량 | Full 첫 단계, 1.25e9 s | first_half 첫 단계, 6.25e8 s |
|---|---:|---:|
| 자유전자 응답 Δe, electrons/H | [1.027763740e-10, 3.128554646e-10] | [5.142175993e-11, 1.565039294e-10] |
| 전자 밀도 응답 Δn_e, cm^-3 | [1.022803939e-14, 3.113456811e-14] | [5.117456738e-15, 1.557515902e-14] |
| 온도 응답 ΔT, K | [-2.283422272e-5, -7.460984727e-6] | [-1.141949741e-5, -3.731834011e-6] |
| 열에너지 기여 C_w, K | [-1.553390448e-5, -5.093789058e-6] | [-7.767364121e-6, -2.547526610e-6] |
| 입자 수 기여 C_e, K | [-7.300318249e-6, -2.367195668e-6] | [-3.652133288e-6, -1.184307400e-6] |
| 입자 수 기여 비중 | [31.67901824%, 31.98634497%] | [31.71088123%, 31.98927331%] |
| 추가 전자당 열에너지 감소, eV | [13.60117523, 13.63954074] | [13.59981015, 13.61901334] |
| 열+이온화 기체 에너지 응답, eV/H | [-4.224385304e-12, -8.590455955e-13] | [-1.058106258e-12, -2.156864302e-13] |

표는 `results/thermo_v2/THERMO_RESULTS.json`의 정확한 유리수 끝점을 바깥쪽으로 표시했다. 두 단계는 같은 COMMON에서 따로 출발한다. 두 half를 이어 계산한 시간 이력 또는 시간 수렴 결과로 읽지 않는다.

## 2. 실제 source 온도를 사용했다

기체 상태는 g=(x_HII,y_HeII,y_HeIII,w), w의 단위는 eV/H다. 실제 `ft03_interval.rs`와 `coupled_primary.rs`의 저장 밀도와 단위 상수를 읽어

\[
\widehat f=\frac{\operatorname{exact}(n_{He,stored})}{\operatorname{exact}(n_H)},
\quad e=x+\widehat f(y_1+2y_2),\quad \Pi=1+\widehat f+e,
\]
\[
C_T=\frac{2\operatorname{exact}(\epsilon_{eV})}{3\operatorname{exact}(k_B)},
\quad T=C_Tw/\Pi,\quad n_e=n_H e
\]

로 정의했다. Stage의 f=exact(f_He)와 fhat는 정확히 같지 않으며, source 온도에는 fhat가 들어간다. 새로 반올림한 kB_eV quotient나 source coefficient를 대입하지 않았다. 이 정의에서 e는 He 전자를 포함하므로 1을 넘을 수 있다.

같은 고정 α에서 U=∂λg라 하면

\[
U_e=U_x+\widehat f(U_{y_1}+2U_{y_2}),\qquad
U_T=C_T\left(U_w/\Pi-wU_e/\Pi^2\right).
\]

원 source/C² 전제와 균일 포함 아래 ΔT=∫₀¹U_T dλ다. 실제 Ue>0, Uw<0, w>0, Π>0를 확인하여 두 온도 항의 음수를 얻었다. λ=0 근처 선형근사를 사용하거나 corner 근을 새로 계산하지 않았다.

## 3. 약 32%라는 비중을 얻은 방법

같은 λ 경로에서 C_w=∫C_TU_w/Π dλ, C_e=−∫C_TwU_e/Π² dλ로 두면 ΔT=C_w+C_e다. 이는 정해진 좌표와 경로의 chain-rule 분해다. 두 개의 별도 물리 실험으로 소스를 켜고 끈 결과가 아니다.

독립적으로 넓어진 Δw와 Δe 구간을 나누면 상관관계를 잃는다. 대신 PHYS09가 저장한 projected source energy ℰ=ℓ_fF를 사용하여 새로운 **일차** 에너지 응답

\[
U_{E_g}=d(\mathcal E_gU+\mathcal E_\lambda)
\]

을 계산했다. ℓ_f=(χH,fχHeI,f(χHeI+χHeII),1)이며, HH의 직접 thermal/binding 상쇄를 먼저 적용한 소스식이다. He 보정까지 유지하여

\[
\mathcal R=U_w+\chi_HU_e
=U_{E_g}+(\chi_H\widehat f-f\chi_{HeI})U_{y_1}
+\{2\chi_H\widehat f-f(\chi_{HeI}+\chi_{HeII})\}U_{y_2}
\]

와 χ_eff=−Uw/Ue=χH−R/Ue를 포함했다. χ_eff에는 photo/nonphoto/He/팽창 feedback이 들어가므로 원 HH 문턱과 정확히 같다고 놓지 않았다.

양의 냉각 크기 A=−C_TUw/Π, B=C_TwUe/Π²에 대해

\[
\frac{B}{A+B}=\frac{w}{\chi_{eff}\Pi+w},\quad
\frac{\int B}{\int(A+B)}
=\frac{\int [B/(A+B)](A+B)}{\int(A+B)}.
\]

따라서 유한 입자 기여 비중은 점별 비중의 양의 가중평균이며, 점별 상·하한으로 감쌀 수 있다. 기존 Banach 자료의 근 영상 상자 g_c±(β+Br)도 사용해 w/Π의 폭을 줄였다. 새로운 inverse나 source 호출은 필요하지 않았다.

## 4. 열에너지가 늘면서 온도가 내려가는 photon birth

원 birth node는 13.7 eV다. 같은 고정 λ에서 b를 바꾸면 Vw>0, Ve>0이지만 VT<0를 얻는다.

\[
\epsilon_b=V_w/V_e,\qquad
V_T=C_T(V_e/\Pi)(\epsilon_b-w/\Pi).
\]

Full에서 ε_b∈[0.07144046346,0.1476359577] eV, w/Π∈[6.324371351,6.396537324] eV다. 새 전자당 열에너지 증가가 기존 입자당 평균 열에너지보다 작으므로 T는 내려간다. ε_b는 implicit feedback을 포함한 응답 비율이며 단순 heat leaf 13.7−χH와의 exact identity가 아니다. 실제 birth-only 유한 ΔT는 Full [-3.338036516e-4,-2.276063273e-4] K, first_half [-8.356646695e-5,-5.700670497e-5] K다.

PHYS09의 기존 WT>0는 그대로 재사용했다. 이를 새 UT<0와 연결하면 D_HH T(0)<D_HH T(1)<0다. HH와 birth가 각각 온도를 낮추면서 서로의 추가 냉각을 약화하는 것은 양립한다. Full에서 I_T/[-D_HH T(1)]∈[1.134223612e-7,1.185971103e-6], first_half에서는 [2.841886810e-8,2.968671289e-7]다. 이 상대 보정의 분모는 전체 우주론 온도 변화가 아니라 선택된 HH 응답이다.

## 5. 정규화 차이를 같은 근에서 전달한 결과

같은 g(λ,b)에 f 또는 fhat로 정의한 온도를 읽는 차이를 먼저 인수분해했다. 이 차이식의 λ 미분을 포함하고 적분하면 HH 온도 응답의 두 readout 차이는 Full 1.353096441e-23 K, first_half 1.302727274e-22 K 이하다. 작은 coefficient 차이도 상관된 같은 경로에서 계산했다.

이 결과는 같은 근의 출력 변환이다. 원 source의 fhat를 f로 바꾼 뒤 달라지는 근의 오차까지 포함하지 않는다. 원 저장 계수를 변경하지 않는다.

## 6. 실행, 독립 검토 및 후속 계획

표준 Python Fraction 후처리의 최종 process wall은 약 0.115 s, exit 0이다. 첫 성공 이후 birth의 두 energy readout과 부호 판별만 추가했고 기존 계산 항목은 정확히 동일했다. 원 입력 26개의 실행 전후 hash는 유지됐다. 정확 endpoint 관계, 등온 상쇄, 입자 감소의 온도 반례, readout 차이식, 같은 정규화 극한과 영 포함 분모 거절을 실행했다.

후보 모듈을 import하지 않는 별도 유리수 구현과 source 대조로 독립 reviewer가 주요 exact endpoints를 확인했다. 최종 판정과 실제 읽은 범위는 `review/DECISION.json`과 `review/REVIEW_KO.md`에 있다. Hash는 자료 identity를 확인하며 원 구간 kernel의 정확성을 새로 증명하는 것은 아니다.

기존 source inclusion 및 같은 C² root family 전제를 유지한다. 새 native/source/root 호출, NCP 작업 및 과거 과학 suite replay는 모두 0이다. Actual native root, ray/guard carry, 실제 second_half, 시간·연속체 오차, 소비자 적용성 또는 전체 REI 관측량은 이번 결과에 포함되지 않는다.

`NEXT_DAG.json`은 기존 8개 HH 노드와 의존관계를 유지하고 PHYS13 provider 관측량 노드 하나를 추가한다. 원 첨부 global DAG의 새 완료 노드는 없다. 실제 소비 요청이 결박되면 전체 source/COMMON/계수/연산자 관계를 대조해 이 ΔT/Δn_e 포함을 사용할 수 있다. 다음 실제 이력 확장은 PHYS11의 gas·photon 공동 carry와 새 단계의 유효한 source/root 포함을 요구한다.

## 원문과 재현

- `inputs/phys09/PROJECTED_RESULTS.json`, `PROJECTED_ENERGY_THEOREM_KO.md`: source 조건, 정확한 U/V/W·energy Jet·기존 WT.
- `inputs/phys12/`: finite switch 의미와 이전 absolute 결과.
- `inputs/ncp07/`: 실제 온도 source와 scalar leaf/box; Git blob identity는 `evidence/SOURCE_IDENTITY.json`.
- `theory/THERMODYNAMIC_RESPONSE_THEOREM_KO.md`: 상세 유도, 경로 분해, 양의 가중평균 및 제안/실행 구분.
- `results/thermo_v2/THERMO_RESULTS.json`, `SUMMARY.json`: 새 결과; 모든 구간의 정확한 분자·분모와 단위.
- `src/thermo_response.py`: 후처리 구현. 재현 시 새 출력 디렉터리를 선택한다: `python3 src/thermo_response.py --out /absolute/path/new_output`.
- `evidence/thermo_first/`, `evidence/thermo_v2/`, `review/`: 실제 실행과 독립 판정.
