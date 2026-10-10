# PHYS06: uniform implicit family에서 유한 혼합 차이까지

## 1. 이번에 닫는 연결과 닫지 않는 값

PHYS05는 remap/photo 항의 정확한 계수와 대수적 미분식을 제공했고, NCP
PHYS04 v2는 실제 FT03/LCS source를 조합한 residual/Jacobian/Hessian 및
혼합 선형 포함식을 구현했다. 그러나 supplied box에서 미분식을 계산하는
것만으로 그 box 안에 실제 BE 해가 존재하거나, 매개변수 사각형 전체에서
같은 해의 가족이 이어진다고 결론 낼 수는 없다.

PHYS06의 결과는 다음 조건부 연결이다.

1. 실제 source에 대해 상태·매개변수 영역 전체를 덮는 residual/Jacobian
   구간이 주어지고 아래 수축·불변 조건이 성립하면, 그 영역 안의 유일한
   implicit root family가 존재한다.
2. 같은 영역의 모든 미분항을 포함한 U, V, W 구간을 얻으면, W의 적분으로
   유한 네 모서리 차이를 바로 제한한다.
3. 따라서 **이 경로에는 별도의 매개변수 Taylor 나머지가 필요 없다.**
   필요한 것은 whole-rectangle root/derivative 포함이다. 시간 이산화 나머지,
   연속시간 source-law 해와의 차이, 실제 native authority는 별개의 문제다.

현재 actual source-bound root/tube와 W/I_h 수치는 없다. 이 문서의 정리와
실행한 manufactured reference checks를 actual HH 관측값으로 승격하지 않는다.

## 2. 잔차, 매개변수, 공통 초기 상태

매개변수를 θ=(λ,b), 직사각형을
Θ=[λ0,λ1]×[b0,b1]로 둔다. λ는 미래 HH 반응 amplitude, b는 미래 photon birth
amplitude다. 모든 θ는 **동일한 물리적 초기 checkpoint와 과거 HH ledger**에서
출발한다. λ=0이나 b=0이라는 이유로 과거 이력을 지우지 않는다.

한 BE stage의 reduced gas residual은

\[
G(y,\theta)=y-y_0(\theta)-dF\big(y,\lambda,N(\theta);t^+,d\big)=0.\tag{1}
\]

여기서 reduced photon은 P_j=N_j/(1+dκ_j(y)). Old gas/photon의 U,V,W와
remap/birth 순서는 G의 parameter dependence에 포함한다. 두 half-step에서는
half1의 값과 U,V,W를 half2의 old state/incoming으로 전달한다. 마지막 gas
box만 맞추고 첫 half의 mixed carry를 지우면 다른 문제를 푸는 것이다.

이 절의 d, 시간, 밀도, 고정 에너지 grid는 λ,b와 독립이다. 이들까지
미분 매개변수로 바꾸면 아래 G의 partial derivatives에 해당 항을 추가해야 한다.

## 3. Uniform root 존재·유일성의 충분조건

X={y: |y−yc|≤r}, r_i>0인 닫힌 convex box를 택한다. G는 X×Θ를 포함하는
열린 영역에서 C²라고 가정한다. 경계 θ에서 source의 C² extension이 없다면
해당 one-sided regularity를 별도로 증명해야 하며, 코드가 경계값을 받는다는
사실만으로 이를 대체할 수 없다. X의 기체분율, 온도, 양의 광자 분모와
모든 source branch가 이 가정의 domain 안에 있어야 한다.

**유효한 uniform enclosure가 주어졌다는 가정 아래**

\[
g_c=[G(y_c,\Theta)],\quad [A]=[G_y(X,\Theta)]\tag{2}
\]

를 만들고, 전체 box에서 고정한 수치 행렬 C를 택한다. C는 근사 역행렬이어도
된다. 단 C가 state나 θ와 함께 바뀌는 함수로 사용되면 아래 고정-C 증명이
그대로 적용되지 않는다. Exact rational reference에서는 C의 수를 정확한
유리수로 고정한다. NCP에서는 저장된 binary64 C의 bit pattern을 leaf로 고정하고
행렬 곱·합과 bounds는 outward arithmetic로 처리해야 한다.

\[
B=\operatorname{mag}(I-C[A]),\qquad
\beta=\operatorname{mag}(C g_c).\tag{3}
\]

mag는 구간의 성분별 절댓값 상한이다. 다음을 확인한다.

\[
\beta+Br<r\quad\text{성분별}.\tag{4}
\]

이는 q_r=max_i (Br)_i/r_i<1도 함의한다. 별도의 scale s를 사용하면
q_s=max_i(Bs)_i/s_i<1을 직접 보고해도 된다. r을 사용하는 구현에서 두
조건을 출력하는 이유는 불변성과 수축의 실패 원인을 구분하기 위해서다.

### 증명

고정 θ에 대해 Tθ(y)=y−CG(y,θ)라 하자. 선분 적분으로

\[
T_\theta(y)-y_c=-CG(y_c,\theta)
 +\int_0^1 [I-CG_y(y_c+t(y-y_c),\theta)](y-y_c)\,dt.
\]

따라서 |Tθ(y)−yc|≤β+Br<r이다. Tθ는 X를 그 내부로 보낸다. 같은
선분 적분은 weighted maximum norm에서
||Tθ(y)−Tθ(z)||_r≤q_r||y−z||_r을 준다. X는 완비이므로 Banach
고정점 정리에 따라 각 θ마다 X 안의 유일한 고정점이 있다.

또한 ||I−CA||_r<1이므로 실제 CA는 Neumann 급수로 가역이다. 정방행렬인
C와 A 각각도 가역이며, Tθ의 고정점은 실제 G=0의 해다. 이는 X 밖의
다른 root를 배제하는 전역 유일성 정리가 아니다.

각 root는 X 내부에 있고 A가 가역이므로 implicit function theorem의 local
C² family가 있다. X 안의 유일성이 겹치는 local family들을 붙여 Θ 전체의
같은 y(θ)를 만든다. 이 논증은 whole-box G와 그 미분 enclosures가 실제
source를 포함한다는 가정에 의존한다. Caller가 `admissible=true`라고 쓴
JSON, source hash 또는 scalar residual의 작은 값만으로 그 가정이 증명되지는 않는다.

## 4. U,V,W의 포함

U=y_λ, V=y_b, W=y_λb라 두면

\[
A U=-G_\lambda,\qquad A V=-G_b,\tag{5}
\]

\[
A W=-\{G_{\lambda b}+G_{y\lambda}V+G_{yb}U+G_{yy}[U,V]\}.\tag{6}
\]

모든 partial derivative는 y를 고정한 잔차 G의 미분이다. Old-state jets와
incoming N jets는 (1)의 G에 이미 포함되어 있다. PHYS04 code가 gas W를
0으로 넣고 source Jet의 λb slot에서 forcing을 추출하는 방법은 (6)을 구현하는
방법이며, 새로운 physical surrogate를 만들 필요가 없다.

행렬 [A], 고정 C와 right hand side [f]가 주어졌을 때 임의의 중심 zc를 두고

\[
\eta=\operatorname{mag}\{C([f]-[A]z_c)\},\qquad
\rho=(I-B)^{-1}\eta.\tag{7}
\]

q<1이므로 (I−B)^{-1}=Σ B^k는 성분별 비음수가 된다. 실제 해 Az=f에 대해
e=z−zc는 e=(I−CA)e+C(f−Azc)를 만족하므로 |e|≤ρ. 따라서

\[
z\in[z_c-\rho,z_c+\rho].\tag{8}
\]

Reference의 `linear_enclosure`는 작은 비교행렬 I−B를 **exact rational**
Gaussian elimination으로 풀어 ρ를 계산한다. 이것은 실제 nonlinear BE root
solver가 아니다. NCP의 이미 구현된 strict linear-image inclusion도 유효한
대체 방법이다. Reference 방법으로 기존 NCP 방식을 불필요하게 교체할 의무는 없다.

먼저 (5)로 [U],[V]를 구하고, (6)의 전 항을 포함한 [f_W]를 만든 뒤 (8)로
[W]를 구한다. Source derivative bound가 point-only이거나 Hessian의 일부
source term을 빠뜨리면 uniform W bound가 아니다. Conditioning이 나쁘거나
dependency가 크면 결과가 넓거나 조건이 실패할 수 있다. 실패는 native
비존재나 불안정을 뜻하지 않고 이 충분조건으로 결론 내리지 못했다는 뜻이다.

## 5. 유한 네 모서리 interaction: 정확한 적분 항등식

같은 family의 terminal output y_h(λ,b)에 대해

\[
I_h=y_h(\lambda_1,b_1)-y_h(\lambda_1,b_0)
       -y_h(\lambda_0,b_1)+y_h(\lambda_0,b_0).\tag{9}
\]

미적분학의 기본정리를 두 번 적용하면

\[
\boxed{I_h=\int_{\lambda_0}^{\lambda_1}\int_{b_0}^{b_1}
                  W_h(\lambda,b)\,db\,d\lambda.}\tag{10}
\]

따라서 Θ 전체에서 W_h∈[Wlo,Whi]이면 면적 a=(λ1−λ0)(b1−b0)>0에 대해

\[
I_h\in a[W_{lo},W_{hi}].\tag{11}
\]

한 성분의 하한이 양수이면 그 finite interaction이 양수이고, 상한이 음수이면
음수다. 구간이 0을 포함하면 이 검증으로 부호가 결정되지 않는다. NCP 실제
source에서 (2)–(8)이 아직 없는 현재에는 (11)의 **실제 숫자도 null**이다.

### 점 계수로 대신할 수 없는 이유

순수 수학 반례 y(λ,b)=λb−2λ²b를 생각하자. W(0,0)=1이지만 단위 사각형의
네 모서리 차이는 −1이다. 전체 W=1−4λ의 범위 [−3,1]를 쓰면 (11)이
올바르게 −1을 포함한다. 이 반례는 HH 물리 모델이 아니며, 점에서의 계수나
부호를 finite observable로 승격하는 논리만 반박한다.

PHYS05/PHYS04의 h²/h⁴ 계수는 시간 step의 formal coefficient다. 식 (10)은
그 시간 계수들의 나머지를 저절로 없애지 않는다. Actual discrete family의
**정확한 W_h 전체**를 포함한 경우에만 parameter Taylor remainder 없이 (9)를
제한한다. Formal h-expansion으로 W_h를 근사한다면 여전히 h-remainder가 필요하다.

### 관측량

선형 관측량 O(y)=ℓy에는 W_O=ℓW를 쓴다. x_HII와 e 좌표가 여기에 해당한다.
고정 nonlinear observable에는

\[
\partial_{\lambda b}O(y)=O_yW+O_{yy}[U,V].\tag{12}
\]

예를 들어 y=λ+b의 W는 0이어도 O=y²의 mixed derivative는 2다. 관측량 자체가
λ,b에 명시적으로 의존하면 O_λb, O_yλ V, O_yb U도 추가한다.

## 6. Full-step과 two-half-step의 혼합 defect

동일한 시작 상태·최종 시간·source history·매개변수에서

\[
\Delta I=I_{\rm two}-I_{\rm full}
 =\int_\Theta(W_{\rm two}-W_{\rm full}).\tag{13}
\]

각각의 [W]를 빼도 포함 자체는 유효하지만 common-parameter correlation을
잃어 넓어질 수 있다. 마지막 reduced stage를 포함해 각 scheme의 mixed system을
A_T W_T=f_T, A_F W_F=f_F로 쓰면 정확한 식

\[
\boxed{A_T\Delta W=(f_T-f_F)-(A_T-A_F)W_F}\tag{14}
\]

을 얻는다. 같은 θ에서 source-bound한 [ΔA],[Δf],[W_F]를 만들고 (8)을 적용하면
ΔW를 직접 포함할 수 있다. **작은 차이를 기대한다는 이유로 ΔA,Δf를 작게
선언하면 안 된다.** Source subtraction graph, shared inputs, rounding 및
full/twohalf carry를 반영한 실제 bounds가 있어야 한다. Δf에는 half1의
parameter dependence가 포함된다.

참조 검산의 순수 수학 witness는 A_T=A_F=1,
W_F=10^6+θ, W_T=10^6+θ+10^-6이다. Independent range subtraction은
[−1+10^-6,1+10^-6]지만 동일 θ의 exact Δf=10^-6를 사용하면 singleton
{10^-6}를 얻는다. 이는 actual HH에서 같은 폭의 개선을 보장하지 않는다.

## 7. Energy coordinate와 결합할 때의 주의

에너지 좌표 S는 고정 선형변환이다. Residual은 Gtilde=SG(S^-1 ytilde),
Jacobian은 Atilde=SAS^-1, Ctilde=SCS^-1로 변환한다. Hessian은
S G_yy[S^-1u,S^-1v]이다. State boxes와 U,V,W도 이 변환과 단위 scale을
일관되게 포함해야 한다. S가 axis-aligned box를 일반 평행체로 보내므로
새 axis box를 취하는 순간 enclosure가 넓어질 수 있다. Exact spectrum이나
eigenvalue similarity는 interval contraction q의 개선을 보장하지 않는다.

에너지식에서 HH direct row가 0이고 photo Hessian이 음의 준정부호여도
식 (6)의 다른 forcing, U/V 부호, N_λ/N_b/N_λb, inverse A, nonphoto escape,
expansion 및 density-leaf normalization residual이 남는다. W_e=0 또는
I_h의 부호를 이 구조만으로 정할 수 없다. 상세식과 source caveat는
`ENERGY_COORDINATE_KO.md`를 따른다.

## 8. 검산과 NCP 적용의 경계

`src/uniform_mixed.py`는 supplied uniform intervals에 대한 충분조건의 산술
부분을 구현한다. `tests/check_reference.py`는 다음 독립 경로로 확인한다.

- Nonlinear analytic root y=4(sqrt(1+λb/16)−1)에 대한 integer-square-root
  rational enclosure와 정확한 U,V,W formula.
- 별도 sparse polynomial engine으로 만든 두 성분 implicit family의
  G_yλ, G_yb, G_yy 및 전체 mixed chain identity.
- H/He 세 흡수 채널을 모두 가진 photo ledger와 quotient-series 계수 oracle.
- Point-sign 반례, nonlinear observable chain, paired-cancellation witness.
- 불충분한 root image, contraction, domain/coverage/identity 입력의 거부.

이 reference는 physical FT03/LCS RHS를 대체하지 않으며 native root issuer를
제공하지 않는다. NCP는 기존 source Jet를 사용해 domain과 parameter coverage가
명시된 exports를 만들고, energy row의 직접 선형변환과 compact formula의
normalization remainder가 정합적인지 검사해야 한다. 실제 native run 예산은
현재 0이다. 구현과 비native 검증을 먼저 완료하고 필요한 실제 실행이 남으면
정확한 identity·call graph·자원 계획을 반환한다.

## 9. 문헌 위치

검증 수치계산의 일반 배경은 S. M. Rump, *Verification methods: Rigorous results
using floating-point arithmetic*, Acta Numerica 19 (2010), 287–449,
[DOI 10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X)를
참고했다. 이번 접근은 고정 preconditioner와 interval enclosure를 사용하는
일반적인 검증 계산의 맥락에 있다. 위 HH-specific coordinate, mixed-chain 및
finite-rectangle 결론은 이 문서에서 전제와 증명을 직접 제시한 것이다.
Publisher abstract/metadata는 확인했지만 author-hosted full PDF는 timeout으로
읽지 못했으며, 읽지 않은 본문의 특정 정리를 인용한 것으로 표시하지 않는다.
