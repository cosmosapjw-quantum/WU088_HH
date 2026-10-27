# R6 일반 finite-n 이론 독립 심사

## 판정

**PASS_SCOPED_GENERAL_N_THEORY.** 아래 명시한 R5 선행 조건과 시간 구간 전체의 coefficient enclosure 조건 아래에서 핵심 유도에 blocking 오류를 발견하지 않았다. 이 판정은 일반 유한 차원에 대한 직접 증명 검토이며, 유한 fixture의 통과를 증명으로 대체하지 않았다.

기여 초안의 작성자와 다른 agent가 검토했다. 이 agent의 앞선 참여는 저장소 목록 조사와 정확한 source/backup metadata 회수뿐이며, 이 단위의 이론 초안과 production core 작성에는 참여하지 않았다. 서로 다른 backend model을 확인한 검토라고 주장하지 않는다.

검토한 초안은 \`THEORY_CONTRIBUTION_KO.md\` SHA256 **2841a91c6f599b423e0658c5a258a409a01df424f1ca59f128737d4babe3314f**다. R6 계약과 R5 \`DYNAMIC_LIFT.md\`, \`HD_GRAPH_BLOCK.md\`, \`THEORY_ADMISSION.json\`, \`CLAIMS.json\`을 전체 읽었다. 정확한 입력 identity는 동봉 JSON에 기록했다.

**수치 실행 0, CAS 0, IVP 0, 과거 과학 재실행 0, 외부 쓰기 0.** Root의 dyadic rounding·production 구현·최종 C9 판정은 이 심사에 포함하지 않는다.

## 1. 반드시 유지해야 하는 전제

R5에서 재사용한 원 모델은 \(x_0\ge0,\ f\ge0,\ h,d\ge0\)이고, \(f\)는 미리 주어진 locally integrable source이다. \(K\)는 column Metzler generator, \(\mathbf1^TK=0\)이다. \(\pi(t)\)는 simplex에 놓인 locally absolutely continuous 함수이다. \(X=\mathbf1^Tx\ge0\)가 성립하며 coarse total은 같은 prescribed \(F=\mathbf1^Tf\)를 사용한다. \(f=f(x,t)\) 같은 상태 의존성은 별도의 coupling bound가 없으면 이번 정리에 포함되지 않는다.

Block에 쓰는 모든 lower/upper bound는 그 block 전체에서 거의 모든 시간에 유효해야 한다. Endpoint sample만으로는 부족하다. Rational comparison은 \(k,b,\kappa\ge0\), 비음수 초기 bound와 forcing/coupling 상한을 사용한다. \(\rho^{\lfloor(t-s)/H\rfloor}\)의 모든 이동창 적용은 같은 generator family bounds가 해당 이동창 모두에 유효한 경우에만 성립한다.

이 조건들은 초안이 명시적으로 재사용한 R5 범위에 포함된다. 독립 문서나 실행 API로 떼어 쓰기 전에는 §5에 비음수 조건을 한 줄로 재명시하는 것이 필요하다.

## 2. Column convention과 zero-sum 투영

\[
X'=-h\,d^Tx+F,\qquad r=x-\pi X
\]

에서 직접 미분하면

\[
r'=\bigl[K+h(\pi d^T-D)\bigr]r+
\bigl[K\pi-\dot\pi-h(D\pi-\pi d^T\pi)\bigr]X+Qf
\]

가 나온다. \(\mathbf1^T\pi=1\), \(\mathbf1^TK=0\), \(\mathbf1^T\dot\pi=0\)로 세 항의 합은 모두 0이다. \(Z=\ker\mathbf1^T\)는 \(\pi(t)\)가 움직여도 고정된 부분공간이다. 따라서 뒤의 common-killing 분리에서 움직이는 좌표계에 대한 추가 \(\dot\pi\) 항을 만들 필요가 없다. 그 항은 이미 \(cX\)에 정확히 포함돼 있다.

물리 source 식의 실제 파괴항과 잔차 식의 수학적 reset generator를 구별한 점도 타당하다. 잔차의 \(L\)에 들어가는 \(\pi v^T\)가 물리적 새 reset event의 존재를 뜻하지 않는다.

## 3. Literal Gibbs enclosure와 상관관계

\(y\in[0,1]\)에 대해 교대 지수급수의 항 크기는 비증가한다. Odd partial sum은 \(m\ge1\)에서 \(S_{2m+1}\ge S_3>0\)이고, even/odd sum은 각각 \(e^{-y}\)의 상·하한이다. 양의 구간을 \(2^s\) 거듭제곱하는 연산은 단조이므로 range reduction 뒤의 enclosure가 성립한다. 초기 Taylor gap을 최종 지수 구간 폭으로 잘못 보고하지 않는다는 조건도 적절하다.

정규화 식 \(w_i/\sum_jw_j\)는 자신의 weight에 단조 증가하고 나머지 weight에 단조 감소한다. 따라서

\[
\frac{\ell_i}{\ell_i+\sum_{j\ne i}u_j}
\le \pi_i\le
\frac{u_i}{u_i+\sum_{j\ne i}\ell_j}
\]

는 독립 weight box에서 좌표별로 sharp하다. 실제 Gibbs family에서는 공통 온도와 gap의 상관관계 때문에 극점들이 동시에 달성되지 않을 수 있다. 초안은 이 구분을 유지한다. \(\pi\in\Delta_{n-1}\)를 버리고 서로 독립인 확률좌표 family를 실제 물리 family로 취급해서는 안 된다.

상향률의 Gibbs ratio는 normalization 없이 직접 감싸야 한다. 정확한 동일 ratio로 양 방향을 구성하면 각 pair에 대해 \(K_{ul}\pi_l=K_{lu}\pi_u\)이고, column diagonal을 출구율의 음수 합으로 정해 \(K\pi=0\)가 정확히 성립한다. 독립 interval 곱셈으로 계산한 \(K\pi\) box의 폭은 dependency loss일 수 있으며 실제 비평형 항으로 해석할 수 없다.

Literal을 정확한 수학 입력으로 취급한다는 것은 측정 오차가 0이라는 주장이 아니다. Source밖 온도에서의 collision rate나 누락된 transition을 생성하는 근거도 아니다.

## 4. 비자율 uniformization과 곱의 순서

Column ODE \(\partial_t\Phi_A=A(t)\Phi_A\)에서 \(A=\lambda(P-I)\)를 대입하고 scalar integrating factor를 적용하면 ordered product는 정확히

\[
P(t_m)\cdots P(t_1),\qquad t_1<\cdots<t_m
\]

순서가 된다. 늦은 시간이 왼쪽에서 작용한다. \(P(t)\)의 induced 1-norm은 1이므로 유한 차원 bounded measurable 계수에서 Picard/Peano–Baker 급수의 norm 절대 수렴이 확보된다. 계수들의 상호 가환성을 가정하지 않았다.

\(0\le P_-\le P(t)\)이면 비음수 행렬곱의 단조성으로 ordered product가 \(P_-^m\) 이상이다. 적분영역 부피는 \(H^m/m!\)이다. 따라서

\[
e_-\sum_{m=0}^N\frac{(\lambda H)^m}{m!}P_-^m
\le\Phi_A(s+H,s)
\]

는 정확한 lower bound다. 생략된 tail은 비음수이므로 이 방향의 증명에 tail upper estimate가 필요하지 않다. 강한 하한을 얻기 위한 수렴/차수 선택과 enclosure의 논리적 타당성은 구별된다.

Diagonal 하한은 실제 full generator의 exit upper bound에서 만들어야 한다. Simplex를 사용한 더 좋은 exit bound를 채택해도 실제 \(P(t)\)에 지배된다는 증명이 유지되면 타당하다. 서로 독립인 off-diagonal 상한의 합과 반드시 같을 필요는 없다.

## 5. Pair overlap, block 분할과 remainder

\(z=z^+-z^-\in Z\)이면 두 부분의 질량은 \(\|z\|_1/2\)로 같다. 각각을 확률분포로 정규화하면 \(Sz\)는 column difference들의 convex combination으로 표현된다. 따라서

\[
\|S\|_{Z,1}
=\frac12\max_{j,k}\|Se_j-Se_k\|_1
=1-\min_{j,k}\sum_i\min(S_{ij},S_{ik}).
\]

두 확률벡터의 공통 질량 항등식으로 두 번째 등식이 성립한다. \(R_N\le\Phi_A\)이므로 \(R_N\)의 최소 pair overlap은 실제 공통 질량의 하한이다. \(\rho=1-\beta_N\)가 zero-sum contraction의 상한이라는 방향이 맞다.

Full block마다 \(\rho\), 짧은 remainder에는 Markov nonexpansiveness 1을 적용하면 floor exponent를 얻는다. 이를 prefactor 1인 순간 gap으로 치환하지 않은 점이 핵심이다. 이동창 family 가정이 없으면 해당 block grid의 개별 certificate만 사용할 수 있다.

\(\beta_N=0\)은 이 certificate의 정보 부족이다. 불가능성 또는 mixing 부재의 정리가 아니다. \(n=1\)은 \(Z=\{0\}\)로 별도 자명하다.

## 6. Full A와 common killing의 정확한 분리

\(v=hd\), \(\tilde v=v-\kappa\mathbf1\ge0\)일 때

\[
A=K+\pi\tilde v^T-\operatorname{diag}(\tilde v),\qquad
L-A=\kappa(\pi\mathbf1^T-I).
\]

\(A\)의 비대각 성분은 비음수이고 column sums는 0이다. 고정된 \(Z\) 위에서는 마지막 차가 \(-\kappa I\)이므로

\[
\Phi_L(t,s)|_Z=e^{-\kappa(t-s)}\Phi_A(t,s)|_Z.
\]

이 논증은 시간가변 \(\pi,K,v\)에도 성립한다. Scalar identity factor만 분리하므로 나머지 행렬끼리의 가환성은 필요하지 않다. 시간가변 \(\kappa(t)\)의 적분 형태도 같은 이유로 성립한다.

\(\rho\)를 full \(A\)의 bounds로 계산해야 한다는 제한이 정확하다. \(K\)만의 finite-block factor에 비가환 reset dynamics를 붙이는 일반 명제는 여기서 증명하지 않았다. 동일 common killing을 \(A\) 내부와 외부에서 두 번 세지도 않았다.

## 7. Forcing의 age와 endpoint/구간 내부의 구별

Duhamel formula의 source는 생성 이후 경과 시간 \(t-s\)만큼의 kernel로 전파된다. 따라서 최근 \(H\)보다 짧은 시간에 생긴 forcing에는 full-block factor \(\rho\)를 일괄 곱할 수 없다.

한 block에서 \(\|u\|_1\le G_n\)이면

\[
U_{n+1}^{\rm exp}
=\rho e^{-\kappa H}U_n^{\rm exp}
+G_n\Psi_\kappa(H)
\]

는 타당한 endpoint upper-envelope recurrence다. 같은 block의 내부에는

\[
\|r(t_n+\tau)\|_1
\le e^{-\kappa\tau}U_n+G_n\Psi_\kappa(\tau)
\le U_n+G_n\tau
\]

가 성립한다. Endpoint bound가 시작값보다 작을 수 있으므로 이를 전체 block의 bound로 삼지 않는 구분이 필요하며 초안은 이를 유지한다.

상수 \(G\)의 convolution에서 lag를 \(kH+[0,H)\)로 분해하면

\[
J(nH+\theta)=\Psi_\kappa(H)\sum_{k=0}^{n-1}q^k
+q^n\Psi_\kappa(\theta),\qquad q=\rho e^{-\kappa H}
\]

가 직접 나온다. 이 공식은 타당하다. 단, 더 보수적인 rational update의 저장값 \(\widehat U_n\)을 이 작은 exact-exponential sequence보다 작다고 결론 내릴 수는 없다. 두 sequence가 모두 실제 residual의 상계라는 것과 서로의 순서는 별도 문제다.

## 8. M, U, E 결합의 적분 방향

\(x\ge0\)로 \(d^Tx\ge d_{\min}X\)를 얻는다. \(M_n\)이 total의 시작 상계이면

\[
M^*=M_n+F_+H,\quad G_n=q_cM^*+g
\]

가 block 전체의 total 및 residual forcing 상계를 준다. \(k\ge0\)의 rational endpoint damping은 scalar variation of constants와 \(e^{-a}\le(1+a)^{-1}\)로 정당화된다.

같은 prescribed total source의 coarse equation과 차를 취하면

\[
D^+|X-\bar X|\le-b|X-\bar X|+s_+\|r\|_1
\]

이다. Zero-sum residual에 대한 \(d^Tr\)의 bound는 \(d\) 범위의 중점을 빼서 얻는다. Within-block residual의 선형 상계를 적분하면

\[
\int_0^H\|r(t_n+\tau)\|_1d\tau
\le HU_n+\frac12G_nH^2.
\]

따라서

\[
E_{n+1}\le\frac{E_n}{1+bH}
+s_+\left(HU_n+\frac12G_nH^2\right)
\]

는 homogeneous term에만 damping을 적용하고 forcing convolution의 damping은 버린 안전한 상계다. 계약이 요구한 endpoint와 적분의 구별을 충족한다. \(U_{n+1}\)을 그대로 \(H U_{n+1}\)로 바꾸면 이 증명은 성립하지 않는다.

Fixed exact Gibbs balance에서 \(q_c\le h\,\operatorname{osc}(d)/2\)의 선택적 개선도 맞다. \([a,b]\) 안의 변수 평균을 \(\mu\)라 두면 convex chord bound로 평균 절대편차가 \(2(\mu-a)(b-\mu)/(b-a)\le(b-a)/2\)이다. \(a=b\)이면 0이다.

## 9. 문서 명확화 두 건

### R6-N1 — 비음수 전제의 재명시

- **대상:** §0, §5.
- **근거:** R5는 비음수 positive-system과 비교계 조건을 명시한다. R6 §5는 lower bound 표기에서 \(0\le k,b\)를 생략한다.
- **영향:** R5 범위를 떼고 음수 lower bound까지 허용하면 rational denominator와 positive comparison이 깨질 수 있다.
- **최소 수정:** \(x_0,f,h,d\ge0\), 같은 prescribed \(F\), \(0\le k\le h\min d\), \(0\le b\le h\bar d\), 비음수 초기/upper bounds를 해당 식 앞에 재명시한다.
- **판정 영향:** 재사용된 R5 조건 아래의 핵심 증명 오류는 아니다. Standalone 계약에는 이 조건을 드러내야 한다.

### R6-N2 — 서로 다른 U sequence의 명칭

- **대상:** §4.1–§4.2.
- **근거:** Exact update는 \(\rho e^{-\kappa H}\), \(\Psi_\kappa(H)\)를 쓰지만 rational replacement는 더 큰 계수 \(\rho/(1+\kappa H)\), \(H\)를 쓸 수 있다.
- **영향:** §4.2의 explicit transient는 실제 residual의 analytical bound이며 보수적인 rational 저장 sequence 자체의 상계로 자동 이전되지 않는다.
- **최소 수정:** \(U_n^{\rm exp}\)와 \(\widehat U_n\)을 구별하거나 §4.2를 rational bookkeeping과 독립인 직접 analytical bound라고 명시한다.
- **판정 영향:** Displayed Duhamel/kernel 식은 정확하며, 의미 혼용만 방지하면 된다.

## 10. 이번 수용이 닫지 않는 의무

실제 native 적용은 **100 K para-H2 supplied-edge graph, \(A=K,\kappa=0\)**이다. 미제공 transition은 missing이며 실제 HD reactive destruction, collider density, REC/REI molecular consumer, source의 물리 불확실성, production은 수용하지 않았다.

Dyadic 계산은 음수가 아닌 lower matrix를 보존하고, overlap lower 방향과 \(\rho\) upper 방향, denominator/zero branch, initial normalization correction, full-A identity를 구현 수준에서 따로 확인해야 한다. 이번 문서는 그 코드 검증의 대체물이 아니다.

정리의 기본 도구는 기존 uniformization, Dobrushin coefficient, elementary interval normalization과 positive comparison이다. 새 기본정리의 발견이나 strong no-go를 주장하지 않는다. 실제 DAG node admission과 stage/backup 공개는 root의 후속 통합에서 판정한다.

