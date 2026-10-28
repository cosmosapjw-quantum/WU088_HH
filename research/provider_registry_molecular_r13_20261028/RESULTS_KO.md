# R13 과학 결과: 비정렬 affine forcing의 정확한 기억 적분과 유한 구현

## 결과와 현재 판정

R13은 비음수 piecewise-affine whole-domain forcing을 받아, R11의 full-A block certificate와 R12의 정확한 비정렬 clock 위에서 전역 residual 비교함수 R을 계산하고 scalar 비교함수 E를 감싸는 방법을 완성했다. 새 계산 경로는 **양의 overlap 1차 moment → 구간별 quadratic R → rational vertex 분할 → 양의 quadratic Bernstein exponential 적분 → 닫힌 셀 상계**다.

실제 primary는 **24개 유효 사례와 38개 거절 사례, 311/311 검사 PASS_SCOPED**, 독립 reference는 **125/125 검사 PASS, 8,408 component comparisons, 실패 0**을 기록했다. 새 과학 Python은 primary/reference 각각 한 번 실행되었다. 독립 검토는 PASS_SCOPED_FINAL_C9, 열린 중대·경미 지적 모두 0이다. 이 수치는 [primary 원출력](raw/PRIMARY_RESULTS.json), [reference 원출력](raw/REFERENCE_RESULTS.json), [C9 결과](reviews/C9_FINAL_REVIEW.json)에 근거한다.

이 문서는 과학 결과와 유효범위를 설명하는 R8/C8 시점의 결과 문서다. 작성 때 실제 DAG는 **25/42**이며, 기존 40개 node와 이번 두 pending node를 포함한다. C9는 새 조건부 이론·유한 코드의 채택 적격성을 판정했다. 실제 두 node의 채택 및 완료 수 변경은 root의 후속 admission delta와 해당 시점 [DAG](DAG.json)에 기록한다. 이 문서가 node 상태를 변경하지 않는다.

## 1. 보존한 전제와 새로 허용한 forcing

Generator는

\[
H=\pi d^{\mathsf T}-\operatorname{diag}(d),\qquad A_w=K+wH
\]

를 유지한다. K, pi, destruction d는 고정이고, certificate는 전체 허용 w box의 모든 경로와 모든 시작시각에 대해 동일 family/state/clock의 zero-mass l1 propagator를 감싼다. 길이 tau의 block 수축 상계 q와 짧은 remainder의 nonexpansiveness로

\[
h(a)=q^{\lfloor a/\tau\rfloor},\qquad h(0)=1,\qquad 0\le q\le1
\]

를 사용한다. q=0에서도 fresh forcing의 계수 \(q^0=1\)을 보존한다. Nominal K의 rho를 full A로 직접 이식하는 단계는 없다.

Norm convention은 \(R=\|r\|_1\), \(E=|\eta|\), coarse l1 \(=4E\)다. Scalar coupling \(c\ge0\)와 signed \(d_c\)는 sweep 전체에서 고정이다. 여기의 c는 비교방정식의 coupling coefficient이며 광속 c의 재정의가 아니다. 시간과 tau는 동일 source clock을 쓰고, 정규화된 변수에서 forcing은 error/time, c와 \(d_c\)는 inverse-time 차원을 갖는다.

R12의 상수 forcing 대신 각 source cell \([a_j,a_{j+1}]\)에서

\[
g_r(s)=r_{j,0}
 +(r_{j,1}-r_{j,0})\frac{s-a_j}{a_{j+1}-a_j},
\qquad r_{j,0},r_{j,1}\ge0
\]

를 받는다. \(g_e\)도 같은 형식이다. 입력의 두 값은 **whole fine/coarse domain에서 유효한 affine 상계함수의 endpoint**다. 두 개의 관측 sample을 연결했다는 사실만으로 이 전제가 성립하지는 않는다. Source cell 사이의 one-sided endpoint 값은 다를 수 있으며 적분에서 개별 경계점의 값은 결과를 바꾸지 않는다. 전제와 정확한 API는 [정리·API 계약](theory/THEOREM_AND_API_KO.md), [고정 계약](CONTRACT.json)에 있다.

## 2. 정확한 overlap과 전역 memory

Raw ideal residual 비교함수는

\[
\mathcal R(t)=h(t-t_0)R_0+F(t),\qquad
F(t)=\int_{t_0}^t h(t-s)g_r(s)\,ds
\]

다. Source cell과 age strip의 교집합 끝점을

\[
L_{jk}(t)=\max(a_j,t-(k+1)\tau),\quad
U_{jk}(t)=\min(a_{j+1},t-k\tau)
\]

로 두면 \(U>L\)인 항은 정확히

\[
I_{jk}(t)=\frac{U-L}{2}\,[g_r(L)+g_r(U)]
\]

이고, 나머지 항은 0이다. 따라서

\[
F(t)=\sum_j\sum_k q^k I_{jk}(t)
\]

를 전부 exact rational로 계산한다. 이 식은 affine 함수의 정확한 적분이며 시간 quadrature를 도입하지 않는다. 모든 항이 비음수라 production 경로에서 두 큰 primitive 값을 빼는 연산도 피한다.

각 평가 시각은 원래 \(t_0\)부터의 source history를 계속 사용한다. Observation knot, source knot, vertex에서 R memory를 초기화하지 않는다. 실제 global_memory 사례는 \(q=1/2,\tau=1,g_r=1,R_0=0\)에서

\[
F(5/4)=R(5/4)=9/8,\qquad E(5/4)=49/64
\]

를 저장했다. \(t=1/2\)에서 이전 forcing을 하나의 새로운 초기값으로 대체하면 같은 ideal 함수가 보존되지 않는다. [Primary 사례](raw/PRIMARY_RESULTS.json)의 global_memory와 [독립 reference](raw/REFERENCE_RESULTS.json)가 이 전역 memory 의무를 검증한다.

독립 reference는 production overlap을 import하지 않고

\[
J_0(x)=\int_0^{x_+}h(v)\,dv,\qquad
J_1(x)=\int_0^{x_+}v h(v)\,dv
\]

의 유한 합을 직접 구성했다. \(g_j(s)=\alpha_j+\beta_j(s-a_j)\)에 대해

\[
F_j(t)=[\alpha_j+\beta_j(t-a_j)]
 [J_0(t-a_j)-J_0(t-a_{j+1})]
 -\beta_j[J_1(t-a_j)-J_1(t-a_{j+1})]
\]

로 같은 비교값을 얻었다. Production과 reference는 이 계산식과 코드 경로가 구별된다.

## 3. Quadratic R, 내부 vertex와 supremum

Source/observation knots, 초기 block knots, translated source knots \(a_j+k\tau\)를 exact rational equality로 합치면 각 base cell 안에서 모든 overlap 끝점의 affine 선택이 고정된다. 따라서 R은 그 안에서 차수 2 이하의 polynomial이다. 양끝과 midpoint의 세 exact 값으로 coefficient를 복원하는 과정은 이미 증명된 quadratic의 대수적 복원이다.

내부 vertex가 있으면 그 rational 시각을 한 번 더 넣는다. 최종 subcell에서는 R이 단조이고 비음수다. Local 시간 \(u\in[0,\Delta]\)에서

\[
P(u)=B_0(1-u/\Delta)^2
 +2B_1(u/\Delta)(1-u/\Delta)
 +B_2(u/\Delta)^2
\]

의 계수는

\[
B_0=P(0),\quad
B_1=P(0)+\frac{\Delta P'(0)}2
     =P(\Delta)-\frac{\Delta P'(\Delta)}2,\quad
B_2=P(\Delta)
\]

다. 증가 구간에서는 \(B_1\ge B_0\ge0\), 감소 구간에서는 \(B_1\ge B_2\ge0\)이므로 세 계수가 비음수다. 단순히 polynomial이 비음수라는 사실만으로 모든 Bernstein 계수가 비음수라고 가정하지 않았다.

### 실제 내부 최대 사례

triangle_q0는 \(q=0,\tau=1\), \(g_r(s)=s\) on \([0,1]\), \(g_r(s)=2-s\) on \([1,2]\)인 산술 사례다. \([1,2]\)에서

\[
R(t)=3t-t^2-\frac32
\]

이며 실제 출력은 다음과 같다.

| 시각 | Exact R | Ideal E |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 1/2 | 1/6 |
| 3/2 | 3/4 | 1/2 |
| 2 | 1/2 | 5/6 |

관찰 시각은 0, 1, 2지만 실제 refined grid는 0, 1, 3/2, 2다. \([1,2]\)의 whole-R 상계는 3/4이며, 관찰 endpoint 두 값을 잇는 선만으로는 이 내부 최대를 포함하지 못한다. 마지막 observation cell의 정확한 scalar majorant는 7/8이고, 실제 outward whole-E upper는

\[
\frac78+2^{-127}
\]

이다. E endpoint enclosure와 whole-cell 상계는 서로 다른 출력이다. [Saved-output 요약](analysis/SAVED_OUTPUT_SUMMARY.json)에 해당 rational 값이 보존되어 있다.

### 실제 달성되지 않는 supremum 사례

initial_jump_unattained는 \(q=0,\tau=1,R_0=1,g_r=1\), 구간 \([0,1]\)이다. \(t<1\)에서는 \(R(t)=1+t\), 실제 \(R(1)=1\), 왼쪽 극한은 2다. 따라서 닫힌 셀의 supremum은 2지만 실제 함수가 그 값을 달성하지 않는다. E endpoint는 3/2다.

R13-F01은 이 차이에 맞춰 closed-cell maximum 표현을 supremum으로 교정한 지적이다. 수식의 상계 계산은 유지했고, 원래 초안 bytes를 [보존 기록](reviews/history/F01_CORRECTION.json)에 남겼다. 해당 실제 control이 통과했으며 독립 R6/C9에서 지적이 닫혔다.

## 4. Signed scalar 전파와 outward enclosure

Affine \(g_e\)를 degree 2로 올리면 계수는 \([e_0,(e_0+e_1)/2,e_1]\)이다. 따라서 \(cP+g_e\)의 Bernstein 계수 \(Q_i\)도 비음수다. \(z=d_c\Delta\)에 대해

\[
W_i(z,\Delta)=
\Delta\int_0^1 e^{z(1-x)}
\binom2i x^i(1-x)^{2-i}\,dx>0
\]

를 쓰면 정확한 ideal endpoint는

\[
\mathcal E_{\rm next}
=e^z\mathcal E_{\rm left}+\sum_{i=0}^2W_iQ_i
\]

다. \(d_c\)의 부호를 제한하지 않는다. \(z\ge0\)에서는 양의 beta-moment Taylor series를 사용하고, \(z<0\)에서는

\[
W_i(z,\Delta)=e^zW_{2-i}(-z,\Delta)
\]

를 쓴다. Taylor degree 96에서 첫 누락항과 이후 항의 비율 상계로 합리수 tail을 감싼 뒤 dyadic128로 바깥쪽 반올림한다.

Whole-E는 별도로 \(Q_{\max}=cR_{\sup}+\max(g_e)\)를 사용한 constant-majorant

\[
Y(u)=e^{d_cu}E_{\rm left}^{\rm upper}
+Q_{\max}\int_0^u e^{d_c(u-v)}\,dv
\]

로 인증한다. \(Y'(u)=e^{d_cu}(d_cE_{\rm left}^{\rm upper}+Q_{\max})\)의 부호가 고정되어 양끝 majorant를 비교할 수 있다. 실제 E가 항상 cell 안에서 단조라고 가정한 것은 아니다. Shared endpoints를 포함한 subcell upper들을 최대화하여 observation closed-cell upper를 얻는다.

**Raw lower는 chosen-rational-q ideal comparison의 lower다.** 실제 physical error의 lower라는 의미를 갖지 않는다. Raw upper가 physical error를 감싸는 결론은 앞서 명시한 generator·forcing·초기값 전제가 같은 실제 source에 결속될 때 사용한다.

독립 reference는 Decimal160의 monomial \(\phi_1,\phi_2,\phi_3\) 적분을 사용했다. 작은 \(|z|<10^{-12}\)에서는 cancellation을 피하는 직접 series를 쓰며 stop \(10^{-150}\), 최대 512항을 실행 전에 고정했다. 비교 guard는

\[
10^{-80}\max(1,|\mathrm{reference}|,|\mathrm{lower}|,|\mathrm{upper}|)
\]

다. 이 guard를 쓰는 Decimal 비교는 수치 corroboration이며 interval reference가 아니다. \(d_c=0\) 사례는 별도로 exact rational E도 비교했다.

Dyadic128은 rounding grid다. 모든 enclosure 폭이 \(2^{-128}\) 이하라는 주장은 하지 않는다. 실제 24개 사례의 가장 큰 refined E endpoint 폭은 argument_minus16에서

\[
\frac{955653}{170141183460469231731687303715884105728}
\approx5.6168235142318576192642348900302537\times10^{-33}
\]

이었다. 이 값은 저장 출력의 upper-minus-lower이며 물리 모델 오차나 reference 오차 추정치가 아니다. zero_singleton의 E 폭은 정확히 0이고, 해당 0/0 relative-width 비율은 null이다. [Saved-output 요약](analysis/SAVED_OUTPUT_SUMMARY.json)

## 5. Affine bound와 cell supremum의 판별

같은 q/tau/초기값/c/\(d_c\)에서 \(g_r^{\rm affine}\le g_r^{\rm sup}\), \(g_e^{\rm affine}\le g_e^{\rm sup}\)이면 양의 kernel과 양의 scalar exponential로

\[
\mathcal R_{\rm affine}(t)\le\mathcal R_{\rm sup}(t),\qquad
\mathcal E_{\rm affine}(t)\le\mathcal E_{\rm sup}(t)
\]

가 따른다. 이는 동일한 source bound 함수를 cell supremum으로 바꾸는 두 ideal comparison의 비교다.

실제 ramp_q1와 ramp_supremum_constant는 \([0,1]\), \(q=1,\tau=1,c=1,d_c=0,R_0=E_0=0,g_e=0\)를 공유한다.

| Quantity at t=1 | Affine \(g_r(s)=s\) | Constant \(g_r=1\) | Ideal affine/constant | Ideal 감소율 |
|---|---:|---:|---:|---:|
| R | 1/2 | 1 | 1/2 | 50% |
| E | 1/6 | 1/2 | 1/3 | 66⅔% |

R 값은 exact rational이며 E 값은 사전에 고정한 analytic control로서 실제 outward enclosure 안에 들어갔다. 저장된 E upper 비율을 정확히 1/3으로 둔 것이 아니라, ideal ratio와 outward interval ratio를 [요약 JSON](analysis/SAVED_OUTPUT_SUMMARY.json)에 각각 기록했다.

두 감소율은 **synthetic arithmetic control의 ideal 비교값 감소율**이다. Native HD 계산이나 R11/R12 capped endpoint의 개선률로 바꾸지 않는다. Strict 개선은 공급된 affine 함수에 따라 달라지며, constant forcing이면 동등한 경우가 생긴다. Source/observation refinement 사례는 같은 ideal F/R/E를 보존하는지를 확인했고, 반올림된 배열의 bitidentity를 요구하지 않았다.

## 6. 실제 finite-domain 및 검증 범위

수학적 forcing 확장은 piecewise-affine이지만, 이번 코드의 유한 domain은 다음과 같이 별도로 고정했다. R12의 모든 유한 입력 크기를 그대로 수용한다는 의미는 없다.

| 항목 | R13 유한 계약 |
|---|---|
| 상태 수 | 1..13; singleton zero-mass residual에서는 \(R_0=0\), 모든 \(g_r\) endpoint=0 |
| Source cells / observation cells | 각각 1..64 |
| Base cells | 최대 2,048 |
| Vertex refinement 이후 cells | 최대 4,096 |
| Full kernel blocks | 최대 8 |
| Exact input numerator/denominator | 각각 최대 256 bits |
| Derived rational numerator/denominator | 각각 최대 16,384 bits |
| Scalar exponential argument | \(|d_c|(T-t_0)\le16\) |
| Production rounding / Taylor degree | dyadic128 / 96 |
| Overlap work | 선행 상한 200,000 이하 |

Base cell 수 N, source cell 수 \(N_s\), full-block 수 B에 대해 구현은

\[
(3N+1)N_s(B+1)\le200000
\]

을 첫 overlap 평가 전에 검사한다. 개별 최대값의 모든 조합이 자동 수용되는 것은 아니다. 실제 dense_aligned_resource는 source 64 cells, base/refined 64 cells를 사용했고 선행 overlap 상한 111,168, 실제 74,304 terms를 기록했다. 잘못된 source/clock/certificate, float/bool/null, 음수 forcing, 65개 cell, 아홉 block, argument 초과, 비트수 초과, stale forcing hash 및 generic cap 요청 등 38개 거절 사례도 모두 기대한 경로를 통과했다. [Primary 검증 출력](raw/PRIMARY_RESULTS.json)

이번 단위는 generic physical cap adapter를 제공하지 않는다. 실제 raw 결과의 cap_application은 NONE이고, R11 saved cap을 새 affine 입력에 결속하지 않았다. R12의 degree-zero 식은 이 확장의 수학적 특수형으로 이어지며, 기존 R11/R12 과학 실행·ODE·완료 심사를 다시 수행하지 않았다.

### 독립 reference 구성별 비교 수

| 구성 | Component comparisons |
|---|---:|
| Metadata·배열 구조·identity | 1,590 |
| Exact rational 계산 | 4,525 |
| Decimal 비교 | 350 |
| Closed-cell·coverage·aggregation | 1,943 |
| 합계 | **8,408** |

125개 검사 group 전부 통과했고 component 실패 및 failure log가 0이다. Exact R/F, translated/vertex grid, local coefficient, d=0 E, signed/near-zero E, closed-cell majorant 및 내부 quarter 점, source/observation refinement를 실제 저장된 결과와 대조했다. 유한 내부점 검사는 전구간 증명을 대신하지 않으며 whole-cell의 수학적 근거는 [직접 증명](theory/PROOF_KO.md)에 있다.

## 7. CAS·실행 자원·identity

Wolfram evaluator 한 번에서 frozen 25 symbolic residual 모두 0이 반환되었다. 동시에 Power::infy가 세 번 및 General::messages가 반환되었다. 실제 상태는 **QUALIFIED_SYMBOLIC_CORROBORATION**, warning cause는 **NOT_ESTABLISHED**다. 제출 코드는 frozen script와 동일한 1,900 bytes이며 실제 제출 SHA256은 아래와 같다.

**d5a342330d34a015e9617c3054f1c14d3ffa82af294df5a4005bc747f0d8ed4e**

이 CAS는 확인한 25 식을 메시지와 함께 corroborate한다. 경고 원인을 이전 단위에서 가져오거나 추가 실행으로 추정하지 않았다. 전체 수학적 근거는 직접 증명과 독립 manual R6다. [실제 CAS 응답](raw/CAS_TOOL_RESPONSE.json), [평가 기록](raw/CAS_ASSESSMENT.json)

| 실행 | 실제 횟수 | 전체 OS process CPU | Wall | 종료 |
|---|---:|---:|---:|---|
| Primary | 1 | 0.793311 s | 0.794483043 s | returncode 0 |
| Independent reference | 1 | 0.541438 s 표시값 | 0.545079357 s | returncode 0 |
| 합계 | 2 | **1.334749 s** 표시값 | 별도 process 기록 | 실패·timeout 0 |

Reference 원 CPU 문자열은 0.5414380000000000003이고 합계 원 문자열은 1.3347490000000000003이다. 위 표는 여섯 소수자리 표시다. CPU는 두 child OS process의 import와 serialization을 포함하며 CAS, 게시·백업·그림 후처리 CPU 및 전체 역사 비용을 포함하지 않는다. [실행 원장](EXECUTION_LEDGER.json), [primary process](raw/PRIMARY_PROCESS.json), [reference process](raw/REFERENCE_PROCESS.json)

Primary/reference/CAS remaining은 **0/0/0**이다. R12/R11/R10/R9/R8/R7/R6/PHYS91 allowance 증가 0, 기존 과학 재실행 0, 새 ODE 0이다. Global remaining과 full historical CPU는 null을 유지한다.

동결 파일 14/14의 실행 후 bytes/SHA256이 일치한다. 이 확인은 [POSTEXEC_FROZEN_IDENTITY](raw/POSTEXEC_FROZEN_IDENTITY.json)의 실제 local identity 검사 범위이며, provider original GET이나 다른 remote blob 검증을 대신하지 않는다.

| 실제 결과 파일 | SHA256 |
|---|---|
| Primary 619,926 bytes | 6b65d7d3d521eb670d42c51cc43140e9ed8db8d6d67825c6975401d531deda28 |
| Reference 41,943 bytes | a3cfc588b0265173dc2e405ff2ea62f7df168238d2ab63fb1f9290490e7f1bdc |
| Frozen cases | 9eaa99dd372da9d242fb57891791502929cfeaf0c74841766a9a3ee2f7806daf |
| Independent reference source | 4525be66370e724bff6aae3f901a92c9a45d69361c1afaa4a0e0301d0f02ec8d |

R13-F02는 실행 전 primary adapter의 root 인수와 exclusive output 처리를 교정한 기록이다. 원래 source hash는 남아 있고 원래 bytes는 보존되지 않았다는 사실을 그대로 유지한다. 실제 과학 실행은 교정·동결 뒤 한 번 성공했다. 이 authoring 교정과 과학 실패 수 0을 구별한다. 과거 R8·R10·R11·R12의 실패·qualified 결과는 [원장](EXECUTION_LEDGER.json)의 역사 항목을 유지한다.

## 8. 문헌의 실제 기여와 현재 physical 경계

SciSpace 검색 1회, Exa 검색 1회와 3 URL fetch 1회로 다항 forcing의 exponential integration을 대조했다. Hochbruck–Ostermann의 [Exponential integrators](https://na.math.kit.edu/download/papers/acta-final.pdf), §2.2 식 2.8–2.11에서 variation-of-constants, exponential quadrature와 \(\phi_k\) 적분 정의를 실제로 읽었다. Al-Mohy–Higham의 [Computing the Action of the Matrix Exponential, with an Application to Exponential Integrators](https://eprints.maths.manchester.ac.uk/1591/1/alhi11.pdf), §2에서는 다항 inhomogeneity와 \(\phi_k\) 급수·augmented representation을 확인했다. 읽기 범위는 가져온 manuscript 앞부분으로 한정하며 논문 전체를 검토했다고 표시하지 않는다.

기존 다항 exponential integration을 재사용하면서, WU의 staircase memory kernel·exact nonaligned event·rational vertex·양의 signed quadratic moment·유한 outward implementation을 연결한 것이 이번 프로젝트 내 기여다. 문헌 전반의 독창성이나 새로운 strong no-go를 주장하지 않는다. Blanes–Iserles–Macnamara 자료는 positivity의 배경 문맥으로만 사용했고 그 논문의 일반 order-barrier 결론을 이번 정리로 채택하지 않았다. 실제 source URL·read scope·raw-response hashes는 [문헌 기록](authority/literature/LITERATURE.json)에 있다.

Actual HD reactive array와 named WU physical consumer/density/clock은 조사한 source 범위에서 INPUT_PENDING이다. HH_R10=OFF, production=NOT_ISSUED, L4=false, central/physical delta=0을 유지한다. Native v=UNSPECIFIED, MISSING_NOT_ZERO, TIQM/SQM 구별도 그대로다. 새 actual input이 오면 original bytes·state/channel·units·density/clock·full-A certificate·whole-domain forcing을 우선 결속한다. 그때 새 source-backed cap이 필요하면 해당 실제 certificate의 별도 adapter 계약을 세운다.

이번 결과가 제공하는 것은 **공급된 whole-domain affine bounds를 시간상수 suprema로 잃지 않고 적분하는 검증된 조건부 방법과 유한 코드**다. 실제 물리 입력의 발급 상태와 과학 방법의 완료 상태를 각각 유지한다.
