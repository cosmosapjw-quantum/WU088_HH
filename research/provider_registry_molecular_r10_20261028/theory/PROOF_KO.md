# R10 독립 구성: HD 파괴항의 Markov 생성자 흡수와 삼각형 비교

## 범위와 실제 읽기

이 문서는 `/root/r10_theory_review`의 R3–R6 구성·검토 산출물이다. 사용자 제공 physmath-research-loop 1.0.0의 RESEARCH_POLICY.md와 THEORY_LOOP.md를 실제 읽었다. R7 원전 `theory/NONLINEAR_FEEDBACK_PROOF_KO.md` (Git blob `1e22dbb051f10ffad6971f41461ae612bedc79b3`, R9 FINAL commit `7a1430afb21736804286ca5284e0d8243016f2f4`)의 식 (R7.20)–(R7.29), R7 구현 `src/nonlinear_feedback.py:hd_feedback_coefficients`, R9 `theory/PROOF_KO.md`와 `src/causal_resolvent.py`를 확인했다. 이전 과학 실행은 재실행하지 않았다.

채택할 새 단위는 `WU_FULL_GENERATOR_TRIANGULAR_R10`이다. 직접 유도의 범위는 지정된 HD 공유 저장고 모형, 같은 불변량의 fine/coarse 초기값, 실제 fine/coarse 궤도를 포함하는 whole-domain box다. 기존 g_r,c,d,g_e를 유지해 생성자 처리의 차이만 분리한다. 물리 HD consumer·밀도·시계·반응 배열의 입력 상태는 바뀌지 않는다.

## 1. 정확한 잔차식

HD 상태벡터 x, 총량 X=1^T x, simplex lift pi에 대해 r=x−pi X, 1^T r=0이다. 열벡터 관례로 K는 conservative Metzler이고, D=diag(d_1,...,d_n), d_i≥0, P_pi=I−pi1^T다. pi는 국소 절대연속이고 q=Kpi−pi'이다.

R7 식 (R7.26)은 정확히
```math
r' = [K + w(pi d^T−D)] r + q X + k_f u v (alpha−pi) − w X (Dpi−pi d^T pi)
   = A(t) r + f_r(t)
```
이다. 1^T q=0, 1^T(alpha−pi)=0, 1^T(Dpi−pi d^T pi)=0이므로 forcing도 zero-sum이다.

H(pi,d)=pi d^T−D에 대해 i≠j이면 H_ij=pi_i d_j≥0이고 각 열의 합은 0이다. 따라서 A=K+wH는 w≥0에서 conservative Metzler다. 이 부호 구조를 보존하면 R7의 절댓값 비용 aR을 사용할 필요가 없다. 다만 새 전파 연산자는 A이므로 K만의 유한 블록 수축률을 그대로 붙이지 않는다.

## 2. 생성자의 zero-sum 수축률

n≥2인 conservative Metzler 열 생성자 M에 대해
```math
L_ij(M)=M_ij+M_ji+sum_{k≠i,j} min(M_ki,M_kj),
lambda(M)=min_{i<j} L_ij(M).
```
모든 항이 비음수라 lambda(M)≥0이다.

충분히 작은 h>0에서 T=I+hM는 열 확률행렬이다. 두 열 i,j의 겹침은 대각 교차의 min 가지가 고정되는 h에서
```math
sum_k min(T_ki,T_kj)=h L_ij(M).
```
확률행렬의 Dobrushin 공식
```math
||T|_{1^T z=0}||_1
 = (1/2)max_{i,j} sum_k |T_ki−T_kj|
 = 1−min_{i,j}sum_k min(T_ki,T_kj)
```
에서 ||T|_Z||_1=1−h lambda(M)를 얻는다. 즉 zero-sum 공간의 l1 logarithmic norm은 −lambda(M)이다. 이 미소시간 식은 전체 l1 공간의 logarithmic norm 0과 구별된다.

M(t)가 유한 구간에서 유계 가측이면 fundamental propagator는 존재하고, z'=M(t)z의 절대연속 해에 거의 모든 시각에서
```math
D^+||z(t)||_1 <= −lambda(M(t))||z(t)||_1
```
를 적용할 수 있다. 적분형 Grönwall로
```math
||Phi_M(t,s)z||_1 <= exp(−integral_s^t lambda(M(u))du)||z||_1
```
이다. M(t)의 Euler approximation을 쓰는 경우에는 계수의 단순함수 근사와 유계성에 따른 propagator 수렴으로 같은 결과를 얻는다. 함수의 값을 임의의 표본점에서 고르는 Euler법이 모든 가측 함수에 수렴한다고 가정할 필요가 없다.

n=1이면 Z={0}이다. API는 lambda=0, 빈 pair 목록을 쓰는 convention을 채택할 수 있다. 정확한 one-state HD 잔차와 forcing은 0이고, 비음수 초기 상계가 느슨해도 유효성은 유지된다. pi의 0 성분, d_i=0, reducible K도 위 증명에 허용된다.

## 3. reset 생성자의 명시적 계수

H=pi d^T−D에 대해서
```math
L_ij(H)=pi_i d_j+pi_j d_i+(1−pi_i−pi_j)min(d_i,d_j).
```
예를 들어 d_i≤d_j이면 이 값은 d_i+pi_i(d_j−d_i)이다. 따라서 lambda(H)≥min_i d_i다. n=2에서는 lambda(H)=pi_1 d_2+pi_2 d_1이며 Z가 1차원이어서 정확한 decay rate다.

각 off-diagonal entry가 w에 대해 비감소하므로 L_ij(K+wH)와 lambda(K+wH)는 w≥0에서 비감소다. fixed K,pi,d와 w∈[m_w,M_w]이면
```math
lambda_* = inf_w lambda(K+wH) = lambda(K+m_w H).
```
또한 각 min의 concavity에서 lambda(K+wH)는 w에 대해 concave하다. 따라서 양 끝점 최소로 구하는 방법도 정확하며, lambda(K+M_w H)≥lambda_*가 추가 exact guard가 된다.

min(x+x',y+y')≥min(x,y)+min(x',y')를 각 pair에 적용하면
```math
lambda(K+wH) >= lambda(K)+w lambda(H).
```
직접 full-generator pair 계산은 이 분리된 lower bound보다 작아지지 않는다. 양의 차이는 K와 H가 서로 다른 열 쌍의 겹침을 보충하는 효과다.

K,pi,d가 실제 시간에 의존하는 일반 이론에서는 각 t의 lambda(A(t))≥lambda_*를 따로 보장하면 된다. fixed-input API의 w 끝점 계산을 시간 변화하는 pi/d의 인증으로 쓰지 않는다. 실제 상태에 의존하는 K에는 선언된 전체 계열의 lower bound가 필요하다.

## 4. forcing의 fine-state box 경계

R7 §9의 box는 fine/coarse를 함께 포함한다:
0≤u,ubar≤M_u, 0≤v,vbar≤M_v, 0≤w,wbar≤M_w, 0≤X,Xbar≤M_X.
q_*,theta_*,v_*가 각각 ||q||_1,||alpha−pi||_1,||Dpi−pi d^Tpi||_1의 구간 전체 상계이면
```math
||f_r(t)||_1 <= q_* M_X + k_f^+ M_u M_v theta_* + M_w M_X v_* = g_r.
```
R7 구현의 v_*=Delta_d/2를 그대로 사용한다. 이 상계는 F_0(bar y)뿐 아니라 F_0(y)도 덮는다. 따라서 F_0(y)−F_0(bar y)를 다시 bE로 분해할 필요가 없다.

R7의 a=M_w h_*와 bE는 일반적인 명목-K 비교의 유효한 선택이었다. 이 단위에서는 정확한 HD 잔차의 full-generator와 fine-state box를 사용하여
```math
D^+R <= −lambda_* R + g_r
```
를 얻는다. 이것은 일반 질량작용계의 모든 b를 제거하는 정리가 아니다.

## 5. scalar coarse error와 삼각형 정리

같은 H,D,charge 불변량에서 coarse error는 e=(-eta,-eta,eta,eta), E=|eta|다. R7 식 (R7.22)의 eta'와 zero-sum dual bound를 재사용하면
```math
D^+E <= c R + d_c E + g_e,
c=M_w Delta_d/2,
d_c=−[k_f^- (m_u+m_v)+dbar^- (m_w+m_X)] <= 0.
```
coarse defect가 있으면 invariant-compatible scalar defect와 g_e의 결속을 유지한다. 전역 coarse l1 error는 4E다.

R0≥R(0), E0≥E(0), lambda_*≥0, c,g_r,g_e≥0인 상수에서
```math
R(t) <= Rbar(t) = e^(−lambda_* t) R0 + phi(−lambda_*,t) g_r,
E(t) <= Ebar(t) = e^(d_c t) E0
 + c J(−lambda_*,d_c,t)R0
 + c Q(−lambda_*,d_c,t)g_r
 + phi(d_c,t)g_e.
```
여기서
```math
phi(a,t)=integral_0^t e^(a s) ds,
J(a,b,t)=integral_0^t e^[b(t−s)]e^(a s)ds,
Q(a,b,t)=integral_0^t e^[b(t−s)]phi(a,s)ds.
```
각 함수는 실수 a,b와 t≥0에서 비음수이며 전체함수다. 유도는 첫 scalar 비교를 푼 뒤 두 번째 Duhamel 적분에 대입하는 것으로 닫힌다. initial whole-horizon error envelope나 implicit determinant 조건은 필요하지 않다. whole-domain coefficient/box 증명은 계속 필요하다.

## 6. 소거식의 연속 극한과 양의 계산법

a≠b이면 J=(e^(at)−e^(bt))/(a−b), a=b이면 J=t e^(at).
a≠0이면 Q=[J(a,b,t)−phi(b,t)]/a다. a=0, b≠0이면 Q=[phi(b,t)−t]/b, a=b=0이면 Q=t²/2다. phi(0,t)=t다.
lambda_*=0, d_c+lambda_*=0, 둘 다0인 경우가 모두 정칙하다. 부동소수점에서 작은 차이를 나누는 닫힌식을 그대로 계산할 필요가 없다.

M=[[-lambda_*,0,g_r],[c,d_c,g_e],[0,0,0]], sigma=max(lambda_*,-d_c,0)를 두면 C=t(M+sigma I)≥0이다. 따라서
```math
exp(tM)=exp(−sigma t) sum_{j=0}^infty C^j/j!.
```
유한 양의 행렬합과 geometric exponential tail을 쓰면 exact rational outward enclosure를 구성할 수 있다. n+2>z=||C||_infty이면
```math
tail_n <= z^(n+1)/(n+1)! / [1−z/(n+2)]
```
가 induced infinity norm에서 유효하며, 각 entry에 같은 scalar tail을 더하는 것은 안전한 상계다. 모든 series 항은 비음수이므로 signed cancellation이 없다. exp(−sigma t)의 유효한 양의 upper를 곱한다. 이는 pole-free 구현의 한 선택이며, 정확한 혼합 moment series나 재사용된 인증 scalar primitive도 같은 계약을 만족할 수 있다.

cell-by-cell 구현에서는 각 cell의 endpoint upper를 다음 초기값으로 전달한다. 양의 삼각형 semigroup 때문에 귀납이 닫힌다. 같은 exact clock의 R9 endpoint cap과 성분별 min은 유효하다. sample trajectory를 cap으로 사용하지 않는다.

whole-cell용으로 Rbar의 scalar 해는 constant forcing에서 단조이므로 max(left bound,right bound)가 유효하다. E에는 Rwhole을 constant forcing에 넣은 scalar bound의 양 끝값 최대를 사용할 수 있다. d_c≤0일 때 단순하고 안전한 식은 Ewhole≤max(Eleft,exp(d_c delta)Eleft+phi(d_c,delta)(cRwhole+g_e))이다. 어떤 선택이 실제 구현되는지는 코드 계약에 명시한다.

## 7. K block 인증 이전의 경계

R7/R9 K-only block rho를 full A에 그대로 넣는 연산은 일반적으로 성립하지 않는다. 확인 가능한 구성은 세 상태 0→1→2에서 각 rate1이고 상태2는 흡수인 K다. 추가 H는 pi=e_0, destruction=(0,L,0), L>0로 state1→state0 reset이다. 기존 K의 상태0 대 상태2 total-variation distance는 e^(−t)(1+t)다. 추가 reset은 absorption을 늦춘다. L=1에서 full A의 해당 distance는
```math
e^(−3t/2)[cosh(sqrt(5)t/2)+(3/sqrt(5))sinh(sqrt(5)t/2)].
```
두 함수의 0차–2차 Taylor 계수는 같고 full−nominal의 t³ 계수는 +1/6이다. 따라서 충분히 작은 양의 t에서 old block bound보다 크다. 이는 특정 잘못된 certificate transfer에 대한 구성적 반례이고 새 strong no-go 성과로 등록하지 않는다.

각 destruction에 epsilon>0을 더하면 H의 common reset 부분은 Z에서 −epsilon I다. 이 부분은 commute하여 e^(−epsilon t)를 인수로 뽑을 수 있지만, 남은 reset이 K의 유한시간 수축을 유지한다는 결론은 여전히 나오지 않는다. 본 단위의 full-generator pair coefficient가 이 문제를 직접 해결한다.

## 8. 검증에 전달할 최소 항목

1. 정확한 H 열합0, offdiagonal≥0, residual identity, E=|eta| 및 coarse l1=4E.
2. pair formula, n1/n2, pi 경계, d_i=0, w interval ends, full lambda≥split lambda.
3. fixed-input scope guard: state ordering/clock/physical source bindings, full-generator family, invalid negative or nonconservative K rejection.
4. triangular matrix/reference, a=b, a=0, b=0, all-zero, positive forcing controls.
5. 지정된 saved R7 input과 R9 cap byte identity; source와 sample의 역할 구분.
6. 실제 bound 결과를 R9와 비교: raw 개선 여부는 실제값으로 판단하고 capped no-worse는 pointwise min의 정리로 기록.
7. 새 1회의 primary/reference + 1회의 symbolic check 등 부모가 고정한 bounded 실행 계약만 사용. 기존 exhausted 과학 allowance는 그대로 보존.

## 9. 문헌 비교와 근거 상태

문헌 담당 agent는 Gaubert–Qu, DOI10.1007/s00020-014-2193-2, arXiv1307.4649v3의 원 PDF 46,949자를 실제 읽고 §1 식(1)–(2), Theorem6.2 및 Example6.3의 stochastic Dobrushin 공식을 확인했다. 해당 문헌은 위 discrete zero-sum formula를 뒷받침한다. 이 문서의 continuous generator bridge와 HD 적용은 위에서 직접 유도했다. 문헌의 기본 수축 원리를 새로운 우선권 주장으로 등록하지 않는다.

결과 상태: projected-sink/full-generator/forcing/triangular comparison은 위 가정 아래 derived. 수치 구현·실제 테스트와 C9 verdict는 별도 실행/검토 근거가 생긴 뒤 갱신한다. 원 HD physical data/consumer input 의무를 닫지 않는다.


## 실제 whole-cell 구현의 대응 (DOC01 종료)

## 실제 구현의 whole-cell majorant

증강 비교행렬 M=[[-lambda,0,g_r],[c,d,g_e],[0,0,0]]에 대해 Mplus=[[0,0,g_r],[c,max(d,0),g_e],[0,0,0]]를 사용한다. lambda>=0이므로 Mplus>=M이며 Mplus의 모든 원소는 비음수다. 비음수 초기 증강벡터 z=(R_left,E_left,1)에 대해 양의 비교 원리로 exp(s M)z<=exp(s Mplus)z이고, 0<=s<=delta에서 exp(s Mplus)z는 성분별 비감소이므로 exp(delta Mplus)z가 닫힌 셀 전체를 덮는다. 코드의 directed matrix/state rounding은 이 상계를 바깥쪽으로 넓힌다. raw 모드에서 보고된 outward endpoint와 max를 취하는 연산은 반올림된 endpoint까지 포함한다. capped 모드에서는 같은 닫힌 셀의 R9 인증 whole cap과 min을 취하고, endpoint는 같은 exact clock의 R9 cap 및 현재 whole cap과 min을 취한다. 각각 동일한 물리량에 대한 유효한 상계의 교차이므로 이후 셀의 초기 상계로 사용할 수 있다.
