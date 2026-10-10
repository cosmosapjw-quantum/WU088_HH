# PHYS04: Source 순서를 보존한 혼합 quartic

2026-10-10. 직접 유도와 bounded exact algebra 검사. 후보 생성·검증설계에 참여한 작업자의 산출물이며 최종 독립 decision review가 아니다.

## 1. 범위와 convention

상태는 \(z=(x_{\rm HII},x_{\rm HeII},x_{\rm HeIII},w,P)\)이고,
\(w\)는 eV/H, \(P_j\)는 photons/H이다. 시간은 proper seconds,
밀도는 \({\rm cm}^{-3}\), metric은 \((-+++)\)이며 \(c,k_{\rm B}\)를 유지한다.
\(\lambda\)는 HH 강도, \(b\)는 지정된 미래 광원의 무차원 amplitude다.

한 step의 실제 순서를 다음 국소 map으로 표현한다.

\[
\begin{aligned}
 d_\delta(t,z;b)&=R_\delta(t)z+b\delta B(t+\delta),\\
 z^+&=d_\delta(t,z;b)
       +\delta F(t+\delta,z^+;\lambda),\\
 F(t,z;\lambda)&=F_0(t,z)+\lambda H(t,z).
\end{aligned}
\tag{1}
\]

\(B\)는 \(S_*\)를 포함한 photon-only rate vector다. 첫 줄은 transport,
fixed-grid remap, endpoint birth이고, 둘째 줄은 endpoint time/density에서
평가한 coupled BE다. Birth를 \(F\)에 다시 넣지 않는다. Photon absorption,
H/He nonphoto 반응과 heating/cooling은 \(F\) 안에 보존한다.

Geometry, step clock, source shape와 fixed grid는 \((\lambda,b)\)와 독립이다.
HH \(H\)는 photon-independent이고 photon 성분은 0이다. 광화학·광가열은
gas–photon bilinear이며 nonphoto gas 장은 비선형일 수 있다.

여기서 필요한 remap은 \(h\downarrow0\) 한쪽 chart의
\(R_0=I\)이다. 고정 node에서 시작한 실제 remap의 양쪽 매끄러움을
가정하지 않는다. 특히 실제 owner의 최저 에너지 guard는
\(h=0^+\)에서 즉시 projection이 생길 수 있으므로, 전체 원 photon
배열에 \(R_0=I\)를 적용하지 않는다. Gas와 결합하지 않는 inactive photon을
제외한 active quotient는, inactive에서 active로 돌아오는 수송이 없고
모든 gas coupling이 0이라는 조건 아래 별도로 사용할 수 있다.
Guard ledger와 비활성 photon 상태는 그 quotient 밖에 보존해야 한다.

식 (1)은 formal power series 정의로 먼저 사용한다. 충분히 매끄러운
함수에서 \(\delta=0\)의 BE Jacobian은 \(I\)이므로 국소 implicit-function
branch와 연결할 수 있지만, 이 문서에서는 유한 \(\delta\)의 root,
positivity tube, interval preconditioner나 branch uniqueness를 계산하지 않았다.
혼합미분까지 포함한 \(O(\delta^5)\) remainder를 정량화하려면 필요한 joint
derivative의 uniform bound가 추가로 필요하다. Joint \(C^6\)와 compact
parameter/clock/state neighborhood의 bounded derivatives는 충분한
smoothness 가정이며, 그 bound 자체는 제공하지 않는다.

## 2. 한 BE step의 \(a_1,\ldots,a_4\)

Transport의 one-sided expansion을

\[
 R_\delta=I+\delta L+\frac{\delta^2}{2}M
 +\frac{\delta^3}{6}N+\frac{\delta^4}{24}P_4+O(\delta^5)
\tag{2}
\]

로 쓴다. \(P_4\)는 photon 상태 \(P\)와 다른 네 번째 transport derivative다.
모든 transport coefficient는 step 시작시각 \(t\)의 함수다.
Endpoint birth 때문에 preBE increment coefficient는

\[
\begin{aligned}
 d_1&=Lz+bB,\\
 d_2&=\tfrac12Mz+bB_t,\\
 d_3&=\tfrac16Nz+\tfrac12bB_{tt},\\
 d_4&=\tfrac1{24}P_4z+\tfrac16bB_{ttt}.
\end{aligned}
\tag{3}
\]

실제 constant prescribed birth에서는 \(B_t=B_{tt}=B_{ttt}=0\)이다.
Transport를 \(\exp(\delta L)\)로 대체하지 않는다. 일반적으로
\(M\ne L^2\), \(N\ne L^3\), \(R_\delta^2\ne R_{2\delta}\)다.

\[
 \Psi_\delta(t,z;\lambda,b)
 =z+\delta a_1+\delta^2a_2+\delta^3a_3+\delta^4a_4+O(\delta^5)
\tag{4}
\]

라 두고 모든 \(F\) derivative를 \((t,z;\lambda)\)에서 평가한다.
\(J=F_z\), \(Q=F_{zz}\), \(C=F_{zzz}\)이면

\[
\boxed{
\begin{aligned}
a_1={}&d_1+F,\\
a_2={}&d_2+Ja_1+F_t,\\
a_3={}&d_3+Ja_2+\tfrac12Q(a_1,a_1)
              +F_{tz}a_1+\tfrac12F_{tt},\\
a_4={}&d_4+Ja_3+Q(a_1,a_2)+F_{tz}a_2\\
 &+\tfrac16C(a_1,a_1,a_1)
       +\tfrac12F_{tzz}(a_1,a_1)
       +\tfrac12F_{ttz}a_1+\tfrac16F_{ttt}.
\end{aligned}}
\tag{5}
\]

이 식은 직접 Taylor 치환으로 나온다. \(v_1=(1,a_1)\),
\(v_2=(0,a_2)\), \(v_3=(0,a_3)\)와 \(D=D_{(t,z)}\)를 쓰면

\[
a_2=d_2+DF[v_1],\quad
a_3=d_3+DF[v_2]+\tfrac12D^2F[v_1,v_1],\quad
a_4=d_4+DF[v_3]+D^2F[v_1,v_2]+\tfrac16D^3F[v_1,v_1,v_1].
\tag{6}
\]

계산 코드는 식 (6)을 구현한다. \(a_k\)는 raw \(\delta^k\) 계수이며
\(k\)차 시간도함수는 \(k!a_k\)다.

Endpoint density drift는 \(F_t,F_{tz},F_{tt},\ldots\)에 들어간다.
예를 들어 고정 He/H 비에서 \(n_H(t)=n_{H0}e^{-3Ht}\)이면
\(n_{H,t}=-3Hn_H\)이고 HH \(q=n_Hu^2k(T)\) 및
photo opacity \(cn_H\sigma_j\) 모두 변한다. 이 drift를 nonphoto 항의
시간변화로만 취급하면 필요한 항을 누락한다. \(H_z,H_{zz},H_{zzz}\)를
포함한 \(F\)의 tensor를 그대로 유지하므로 HH thermal feedback을 freeze하지 않는다.

## 3. One-full과 two-half의 quartic

시간을 상태에 포함하여 \(X=(t,z)\)라 두고

\[
G_1=(1,a_1),\qquad G_r=(0,a_r)\quad(r=2,3,4)
\]

로 정의한다. 한 step은
\(\widehat\Psi_\delta(X)=X+\sum_{r=1}^4\delta^rG_r(X)+O(\delta^5)\)다.
두 번째 half의 시작시각은 첫 번째 half가 만든 \(t+\delta\)이므로,
\(D_XG_r\)가 transport clock과 endpoint sampling을 함께 처리한다.
\(h=2\delta\)에서

\[
 \widehat\Psi_{h/2}\circ\widehat\Psi_{h/2}(X)
 =X+hC_1+h^2C_2+h^3C_3+h^4C_4+O(h^5)
\]

이며

\[
\begin{aligned}
C_1={}&G_1,\\
C_2={}&\tfrac14\{2G_2+DG_1[G_1]\},\\
C_3={}&\tfrac18\{2G_3+DG_1[G_2]+DG_2[G_1]
                    +\tfrac12D^2G_1[G_1,G_1]\},\\
C_4={}&\tfrac1{16}\{
2G_4+DG_1[G_3]+DG_2[G_2]+DG_3[G_1]
+D^2G_1[G_1,G_2]\\
&\hspace{31mm}
+\tfrac12D^2G_2[G_1,G_1]
+\tfrac16D^3G_1[G_1,G_1,G_1]\}.
\end{aligned}
\tag{7}
\]

식 (7)은 map 합성의 직접 전개다. \(DG_1[G_2]\)와
\(DG_2[G_1]\)는 서로 다른 항이며 교환하지 않는다. \(C_r\)의 gas/photon
성분을 \(c_r\)라 하면 full과 two-half의 raw quartic 차이는 \(c_4-a_4\)다.
원하는 혼합계수는 다음 절의 total mixed derivative를 적용한 값이다.

이 표현은 4차 전체 vector field를 하나의 매우 긴 scalar 식으로 펴는
대신, 실제 RHS와 remap jet을 넣을 수 있는 정확한 computational form을 준다.
H/He, thermal, density drift, old photon과 source order를 제거하는 closure는
들어가지 않았다.

## 4. Old \(U,V,W\)를 보존하는 혼합미분

이전 history가 이미 만들어 놓은 상태를 \(z=z(\lambda,b)\)라 하자.

\[
 U=\partial_\lambda z,\quad V=\partial_bz,\quad
 W=\partial_\lambda\partial_bz.
\]

\(a_r(t,z;\lambda,b)\)의 모든 partial derivative는 \(t,z,\lambda,b\) 중
다른 변수를 고정하여 정의한다. Total derivative는

\[
\begin{aligned}
 \mathcal D_\lambda a_r&=(a_r)_zU+(a_r)_\lambda,\\
 \mathcal D_ba_r&=(a_r)_zV+(a_r)_b,\\
 \boxed{\mathcal M a_r}
 &\boxed{=(a_r)_zW+(a_r)_{zz}(U,V)
 +(a_r)_{z\lambda}V+(a_r)_{zb}U+(a_r)_{\lambda b}.}
\end{aligned}
\tag{8}
\]

따라서

\[
W_{\rm full}(h)=W+\sum_{r=1}^4h^r\mathcal M a_r+O(h^5),\qquad
W_{\rm two}(h)=W+\sum_{r=1}^4h^r\mathcal M c_r+O(h^5).
\tag{9}
\]

\(U,V,W\)가 모두 0인 원래 공통 초기 slice에서만
\(\mathcal M a_r=(a_r)_{\lambda b}\)로 줄일 수 있다.
중간 accepted checkpoint에서 이를 임의로 0으로 reset하면
더 낮은 차수의 항도 누락한다.

같은 내용을 정확한 implicit sensitivity 식으로 확인할 수 있다.
PreBE map에서

\[
\tilde U=R_\delta U,\quad
\tilde V=R_\delta V+\delta B(t+\delta),\quad
\tilde W=R_\delta W.
\]

\(A_+=I-\delta J_+\)라 하면 differentiable branch에서

\[
\begin{aligned}
A_+U^+&=\tilde U+\delta H_+,\\
A_+V^+&=\tilde V,\\
A_+W^+&=\tilde W+
 \delta\{Q_+(U^+,V^+)+H_{z,+}V^+\}.
\end{aligned}
\tag{10}
\]

이 식의 \(A_+^{-1}\)를 유한 step에서 계산하거나 인증한 것은 아니다.
식 (5), (7), (8)은 이 감도식을 bounded formal polynomial로 구현하는
별도의 경로다.

유한 매개변수 four-corner difference는
\(I_z=\int_0^\lambda\int_0^b W(a,c)\,dc\,da\)다. 따라서 특정
parameter base에서의 \(W\)를 유한 \((\lambda,b)\) 차이와 같다고 놓지 않는다.
Old family를 이어받으면 initial \(I_z\)도 일반적으로 0이 아니지만,
full/two-half가 같은 family에서 시작하면 그 공통 initial term은
scheme difference에서 소거된다.

## 5. 물리적으로 읽을 수 있는 zero-photon remap 항

이 절에만 추가로 \(P_0=0\), 초기 \(U=V=W=0\), frozen external
coefficients와 constant \(B\)를 가정한다. \(R_\delta\)는 gas를 그대로
두고 photon에만 작용한다. \(L\)도 photon-only이며
\(F(g,P;\lambda)=N(g)+\lambda H(g)+\mathcal P(g,P)\),
\(\mathcal P\)는 gas–photon bilinear다. Nonphoto \(N\)의 photon 성분도
0으로 두어 \(F_\gamma(g,0;\lambda)=0\)을 요구한다. 재결합 방출 등을
transported photon에 내부 생성하는 closure라면 이 특수화에 추가항이
필요하지만 일반 식 (5), (7), (8)은 그 RHS를 넣어 계속 사용할 수 있다.

One-full에서는 birth 전에 remap할 photon이 없으므로,
mixed quartic에 \(L\) 의존성이 없다. Two-half에서는 첫 birth의 photon이
두 번째 remap을 통과한다. \(L\ne0\)와 \(L=0\)의 mixed quartic 차이를
\(\Delta_L[h^4]W\)로 표기하면

\[
\boxed{
\Delta_L[h^4]W_{\rm two}
=\frac1{16}\left\{
 H_zJ(LB)+2Q(H,LB)+LQ(H,B)
\right\}.
}
\tag{11}
\]

\(LQ(H,B)\)는 photon 성분에만 남으므로 gas에 대해서는

\[
\boxed{
\Delta_L[h^4]W_{{\rm two},\,{\rm gas}}
=\frac1{16}\{H_zJ(LB)+2Q(H,LB)\}_{\rm gas}.
}
\tag{12}
\]

도출에서 \(\delta=h/2\)이다. 첫 half의
\(W_{1,\gamma}=\delta^3Q(H,B)_\gamma+O(\delta^4)\)를 두 번째 remap이
\(\delta^4LQ(H,B)\)만큼 바꾼다. 두 번째 birth 감도는
\(\Delta V=\delta^2LB+\delta^3JLB+O(\delta^4)\)이고
\(U_+=2\delta H+O(\delta^2)\)다. 식 (10)에 넣으면
\(\delta^4\{H_zJ(LB)+2Q(H,LB)\}\)가 추가된다.
\(H_zLB=0\)이므로 이 remap 효과는 mixed cubic에 들어가지 않는다.
\(M,N,P_4\)의 first-birth 효과도 해당 mixed quartic에는 남지 않는다.

기존 photon \(P_0\ne0\)이면 remap이 baseline gas 진화와 Jacobian도
바꾸므로 식 (11)을 전체 quartic 차이로 사용할 수 없다. 그 경우에는
식 (5), (7), (8)을 사용한다.

### HI-only birth의 thermal-weighted opacity 표현

관련 birth와 이웃 node가 모두 HeI photoionization cutoff 아래라면

\[
 A_j=cn_H\sigma_H(E_j),\quad
 \Pi=1+r+x+r(y_1+2y_2),\quad u=1-x,
\]

\[
 T=\frac{2E_{\rm eV}w}{3k_{\rm B}\Pi},\quad
 \nu=\frac{d\ln k}{d\ln T},\quad
 T_{\gamma,j}=\frac{2E_{\rm eV}(E_j-\chi)}{3k_{\rm B}},
\quad
 \Xi_j=\frac{u}{\Pi}\nu\left(1-\frac{T_{\gamma,j}}{T}\right).
\]

\(T_{\gamma,j}\)는 excess energy에 대응하는 온도이며 CMB 온도가 아니다.
직접 상태미분으로

\[
 [H_zJ(LB)]_x=-q\sum_jA_j(2+\Xi_j)(LB)_j,\quad
 [Q(H,LB)]_x=-q\sum_jA_j(LB)_j
\]

이므로

\[
\boxed{
 \Delta_L[h^4]W_{{\rm two},x}
 =-\frac{q}{16}\sum_jA_j(4+\Xi_j)(LB)_j.
}
\tag{13}
\]

이는 단순한 photon 수나 에너지 모멘트보다 thermal-weighted opacity
functional이 직접 관련된다는 것을 보여준다. \((LB)_j\)에는 유입과
유출의 서로 다른 부호가 들어가므로 전체 부호를 일반적으로 정하지 않는다.
실제 spectrum에서 전체 remap opacity defect가 단일 cutoff column의
부호와 달라도 모순이 아니다.

식 (13)은 차원도 맞는다:
\(q\sim{\rm s}^{-1}\), \(A_j\sim{\rm s}^{-1}\),
\(B_j\sim{\rm photons/H/s}\), \(L\sim{\rm s}^{-1}\)이므로
\(qA_j(LB)_jh^4\)는 무차원 이온화 fraction이다.
실제 nonzero photon 초기상태나 유한 \(h\)의 gas 오차에 이 isolated
zero-photon 항을 그대로 대입하지 않는다.

## 6. 검산 방법과 독립성

ordered_be_quartic.py는 표준 라이브러리 fractions.Fraction만 사용한다.
비차원 algebra fixture는 gas 4개와 active photon 2개를 갖는다.
H/He photoionization·photon loss·threshold heating은 gas–photon bilinear,
HH는 photon-independent이고 상태의 비선형 thermal surrogate를 포함한다.
비선형 nonphoto ionization/recombination·cooling, density clock drift,
birth profile과 transport clock drift를 보존한다. 이 surrogate는 실제
LCS rate 근사나 물리 dataset이 아니다.

두 계산 경로는 다음과 같다.

1. Candidate는 sparse multivariate polynomial을 직접 편미분하여 \(F\)의
   tensor를 만든 뒤 식 (5)와 확장시각 map 합성식 (7)을 평가한다.
   Old \(U,V,W\)는 \(\epsilon^2=\eta^2=0\)인 commuting dual algebra로
   보존한다.
2. Oracle은 state의 truncated \(h\)-series를 구성하고 각 BE 단계에서
   미리 정한 네 번의 formal substitution을 수행한다. 시간 convolution으로
   계수를 얻으며 candidate의 \(a_r\)나 map-composition derivative를 쓰지 않는다.
   각 단계의 implicit residual도 \(h^0,\ldots,h^4\)에서 exact zero인지 확인한다.

두 경로는 rational fixture의 RHS 정의와 Fraction 산술을 공유한다.
따라서 서로 다른 계산 경로의 대조이지만, 실제 물리 RHS를 독립 구현하여
검증한 것은 아니다. 이 작업자는 candidate와 검사설계에 모두 참여했으며
최종 decision reviewer의 독립성을 주장하지 않는다.

실행한 6개 case:

| TestID | 구체적 차이 |
|---|---|
| frozen_nonzero_photons | 초기 old photons, frozen 외부계수 |
| density_and_profile_drift | 밀도·birth 시간변화와 양의 parameter base |
| transport_clock_and_density | remap clock 및 density 시간변화 |
| inherited_UVW_all_nonzero | 모든 gas/photon의 old \(U,V,W\)가 0이 아님 |
| zero_photons_frozen | zero-photon \(L\) 특수화 |
| zero_photons_frozen_lambda_base | 같은 특수화, \(\lambda_0=1/3,b_0=2/5\) |

최종 run_02의 모든 case에서 full/two-half, \(h^1,\ldots,h^4\), 6개 상태,
primal/\(U\)/\(V\)/\(W\)의 총 1,152 rational slot이 일치했다.
Zero-initial sensitivity case의 cubic은 상속된 PHYS03 계수
\(\alpha_mH_zJB+\beta_mQ(H,B)\)와 \(m=1,2\)에서 일치했다.
이 cubic 비교는 새 quartic 검사에 포함한 하위 차수 일관성 확인이며,
PHYS03의 완료 suite를 다시 실행한 것이 아니다.
식 (11)은 zero-photon 두 case의 모든 6개 상태에서 exact 일치했다.

## 7. 실행 결과, 상태와 재현

최종 과학 검사 run_02는 exit 0, 6 case PASS였다.
run_02/EXACT_CHECK.json에는 모든 mixed cubic/quartic의 정확한 rational
계수와 full/two-half 차이가 들어 있다. run_02_status.json에는 실행
명령, Python 버전, 시각, 실행한 script SHA와 stdout/stderr 경로가 있다.
run_02.stdout과 run_02.stderr를 원문 그대로 보존한다.

첫 run_01도 candidate/oracle의 algebra 일치는 모두 PASS였으나, 사후
scope 대조에서 frozen label의 fixture에 nonphoto cooling의 t/47 항이
남은 것을 발견했다. 이는 IMPLEMENTATION_FIXTURE_SCOPE_MISMATCH다.
원 script, run_01 및 최초 발견을 FIRST_FIXTURE_SCOPE_CORRECTION.json에
보존했다. 그 coefficient drift를 기존 density-drift switch에 묶어
frozen case에서는 정확히 0이 되도록 고쳤다. 영향받은 6개 fixture만
run_02로 재검사했고 candidate recurrence나 합성식은 변경하지 않았다.
Frozen 특수화의 검사 근거는 수정된 run_02만 사용한다.

사전 dependency probe에서 SymPy가 없다는 ModuleNotFoundError가 한 번
발생했다. FIRST_ENVIRONMENT_PROBE_FAILURE.json에 보존했다.
패키지를 설치하거나 같은 probe를 반복하지 않고 Fraction-only 구현으로
진행했다. 이것은 환경 확인 실패이며 과학 검사의 실패가 아니다.
과학 checker의 최초 실패는 발생하지 않았다.

재현이 필요한 경우 기존 증거를 덮어쓰지 않는 새 경로를 사용한다.

    python3 -B ordered_be_quartic.py --output /absolute/new/output_directory

Native dispatch, IVP integration, nonlinear BE root, NCP,
legacy atomic integral와 부모의 완료 suite 실행 횟수는 모두 0이다.

식 (5), (7), (8), (11)–(13)은 명시된 범위에서 derived이고,
formal fixture의 두 계산 경로 일치는 exactly checked /
implementation-verified다. Actual common-state native family의 유한시간
부호, finite gas error와 production admission은 unresolved/HOLD다.
결론은 root의 독립 decision review와 source-bound 결과에 통합될 후보이며
이 문서가 스스로 PROMOTE를 승인하지 않는다.

