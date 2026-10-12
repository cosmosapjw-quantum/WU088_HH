# 고정 소스 계열의 유한 HH ON/OFF 응답

## 1. 정의와 양화사

각 단계 s에서 허용된 고정 계수 묶음을 α_s라 한다. 이 묶음은 COMMON,
기존 기체·광자·guard, source의 저장된 scalar leaves, transport geometry,
단계 길이 d_s와 photon-birth amount의 실제 관계를 유지한다. full과
first_half 사이에는 d_s와 PreBE 계수가 다르다. 같은 COMMON에서 출발한다는
사실은 α_full=α_first_half를 뜻하지 않는다.

기체 좌표와 매개변수는

\[
g=(x_{\rm HII},y_{\rm HeII},y_{\rm HeIII},w),\quad
\theta=(\lambda,b_{\rm amp})\in[0,1]^2
\]

다. λ는 미래 LCS HH 소스의 강도, b_amp는 미래 광자 생성량의 정규화 강도다.
한 stage에서 α_s는 θ가 바뀌어도 고정한다. λ=0에도 COMMON 이전 HH와
장부 보정이 남고, b_amp=0에도 이미 존재하는 광자는 남는다.

\[
G(g,\lambda,b;\alpha_s)=g-g_{\rm old}-d_sF(g,\lambda,b;\alpha_s)=0,
\qquad F=R+\lambda H,
\]

\[
H=q(1,0,0,-\chi_H),\qquad
q=n_H(1-x_{\rm HII})^2k_{\rm LCS}(T).
\]

여기서 n_H는 proper cm⁻³, k는 cm³/s이므로 q는 H핵당 s⁻¹이다.
w는 열에너지 eV/H, χ_H는 eV, d_s는 proper second다. 기존 LCS closure에
새 pair-counting 1/2를 넣지 않는다. 별도 singlet H⁺/H⁻ 생성 모형과도
동일시하지 않는다. c, k_B 및 eV 변환은 원 source 정의를 유지한다.

이 연구에서 사용할 이온화량은 **분율 x_HII**다. 결과 Δx는 순간 반응률
dx/dt가 아니며, 표의 Δw도 시간에 따른 w(t)의 총 변화가 아니다.

## 2. 상속하는 전제와 이번에 새로 유도하는 결론

PHYS09의 기존 정리·판정은 각 고정 α_s에서 다음을 조건으로 삼는다.

1. 실수로 lift한 source G는 X×Θ의 적절한 열린 근방에서 C²다.
2. 보존된 source-box/centre export는 동일 함수와 전체 영역의 값·미분을 포함한다.
3. 보존된 Y⊂X, 고정 preconditioner C, 가중 수축률 γ<1 및 strict
   self-map margins가 유효하다.

그때 Banach 정리로 매개변수마다 Y에 근이 존재하고 X에서 유일하다.
근 Jacobian A=G_g가 가역이므로 implicit-function theorem으로 C² branch를
얻으며, X 내 유일성으로 국소 branch들을 Θ 전체에서 잇는다.
원 interval kernel의 source-inclusion은 상속 전제다. 이 글이 그 kernel을
새로 증명하거나 부동소수점 native 실행 자체를 C² 함수로 선언하지 않는다.

고정 g_old,d_s,α_s에서 한 번 미분하면

\[
A U=-G_\lambda=d_sH,\qquad U=\partial_\lambda g.
\tag{1}
\]

PHYS09는 고정 C와 K=I−CA를 사용하여

\[
A^{-1}s=\sum_{k=0}^3 K^kCs+R_4,
\qquad \|R_4\|_r\le\frac{\gamma^4}{1-\gamma}\|Cs\|_r
\]

의 포함으로 U를 Θ 전체에서 계산했다. PHYS12는 이 계산을 재실행하지 않고
저장된 exact endpoints를 재사용한다. q>0만으로 결합계의 U_x>0를
일반적으로 증명할 수는 없다. A⁻¹의 feedback까지 들어 있는 실제 U 포함의
엄밀한 부호를 사용해야 한다.

**유한 응답 정리.** 위 전제와 균일 포함 U_O(λ,b;α_s)∈[u⁻,u⁺]가
있으면 고정 b=b_*에서 λ₀≤λ₁인 유한 차이는

\[
D_{\lambda_0\to\lambda_1}O(b_*;\alpha_s)
=\int_{\lambda_0}^{\lambda_1}U_O(\lambda,b_*;\alpha_s)d\lambda
\in (\lambda_1-\lambda_0)[u^-,u^+].
\tag{2}
\]

증명은 같은 C¹ branch에 미적분학의 기본정리를 적용하고 적분구간 전체에
u⁻≤U_O≤u⁺를 적분하는 것이다. α_s는 적분 안에서 변하지 않는다.
λ₀=0, λ₁=1, b_*=1이면

\[
\boxed{D_{\rm HH}O(1;\alpha_s)=O(1,1;\alpha_s)-O(0,1;\alpha_s)\in[U_O].}
\tag{3}
\]

이는 finite implicit-stage response를 포함한다. λ=0 근처 선형근사나
corner를 실제 실행했다는 주장은 없다. 일반 길이는 식 (2)의 인자를
유지해야 한다. 경로 길이가 0이면 차이도 정확히 0이다.

## 3. 혼합 응답과 부호 해석

같은 α_s에서 기존 혼합량은

\[
I_O=O(1,1)-O(1,0)-O(0,1)+O(0,0)
=D_{\rm HH}O(1)-D_{\rm HH}O(0)
=\int_0^1\!\int_0^1W_O\,d\lambda\,db,
\quad W=\partial_b\partial_\lambda g.
\tag{4}
\]

저장 U의 부호가 U_x>0, U_w<0이고 저장 W의 부호가 W_x<0, W_w>0이므로,
두 stage 각각에서 허용된 같은 계수 계열에 대해

\[
0<D_{\rm HH}x(1)<D_{\rm HH}x(0),\qquad
D_{\rm HH}w(0)<D_{\rm HH}w(1)<0.
\tag{5}
\]

따라서 HH는 같은 단계의 OFF 대조군보다 추가 이온화를 만들고 열에너지를
낮춘다. 추가 photon birth는 이 추가 이온화와 열에너지 감소의 크기를
줄인다. 이는 현재 source family의 정량적 결과다. 모든 온도·밀도·스펙트럼에서
반드시 같은 부호가 성립한다는 일반 정리는 아니다.

\[
r_x=\frac{-I_x}{D_{\rm HH}x(1)},\qquad
r_w=\frac{I_w}{-D_{\rm HH}w(1)}
\tag{6}
\]

는 b=1의 HH 응답 크기를 분모로 한 상대 보정이다. 분모가 엄밀히 양수이므로
양의 구간 a∈[a⁻,a⁺], d∈[d⁻,d⁺]에 대해
[a⁻/d⁺,a⁺/d⁻]를 사용할 수 있다. 같은 모형의 상관관계를 무시하므로
폭은 보수적일 수 있지만 포함은 유효하다. b=0의 효과를 분모로 한 억제분율
η는 η=r/(1+r)로 다르다. 이번 표는 r만 보고한다.

열에너지 변화와 이온화에너지 변화의 source 항에는 χ_H q의 구조적 상쇄가
있지만, 그 사실로 endpoint의 D_w=−χ_H D_x를 주장하지 않는다. Photo,
nonphoto, He 및 팽창 feedback이 있다. 온도도 T∝w/p에 따라 입자수 p가
바뀌므로 w의 부호만으로 자동 환산하지 않는다.

## 4. 단순 검산과 반례

별도 유리수 예제

\[
x(\lambda,b)=\frac{a+pb+h\lambda}{1+a+pb+h\lambda},
\quad a,p,h>0
\]

에서는 A₀=1+a라 두면

\[
D_x(b)=\frac{h}{(A_0+pb)(A_0+pb+h)}>0,
\quad
I_x=-\frac{ph(2A_0+p+h)}{A_0(A_0+p)(A_0+h)(A_0+p+h)}<0.
\]

분율의 HH 기여와 혼합량이 다른 부호여도 모순이 없음을 정확한 유리수로
검사했다. 비단위 λ 경로와 영길이 경로, 0 포함 구간과 0 분모 거절도 확인했다.

동일 계수 가정의 반례는 g(λ;α)=α+λ/10이다. 같은 α에서 D=1/10>0지만,
λ=0에는 α=0, λ=1에는 α=−1을 고르면 차이는 −9/10이다. 양의
∂λg만으로 서로 다른 α의 두 결과를 비교할 수 없다.

## 5. 정확도와 유효범위

새 구간 이동·비율 산술은 Fraction의 정확 유리수로 실행했다. 표의 십진
끝점은 바깥쪽으로 반올림한 별도 표현이며 정확 끝점도 JSON에 남는다.
기존 구간 폭에는 입력·계수 domain, interval dependency와 원래 포함한
선형 역작용 나머지가 섞여 있다. 이들을 독립적인 오차 성분으로 분해하거나
통계적 신뢰구간으로 읽지 않는다. Zero-containing 구간의 끝점을 잘라
부호를 만들지 않는다.

full과 first_half는 서로 다른 첫 stage의 결과다. 차이·비율로 시간 수렴 차수,
전구간 적분오차 또는 실제 두 half의 조합을 추정하지 않는다. 현재 입력은
Hubble triplet [10⁻¹⁴,10⁻¹⁴,10⁻¹⁴] s⁻¹의 witness이며 일반 Bianchi
비등방성 scan도 아니다. 소비 허용오차와 물리 이력 전체가 지정되지 않았으므로
이 국소 크기로 HH의 우주론적 생략 가능성을 판정하지 않는다.

근거: inputs/phys09/PROJECTED_ENERGY_THEOREM_KO.md §§2,5–6;
inputs/phys09/DECISION.json의 same_family_conditions 및 reviewed_mathematics;
inputs/family/{full,first_half}/COMMON_INPUT_SCOPE.json;
inputs/phys09/PROJECTED_RESULTS.json의 stages/0,1/U 및 W.
