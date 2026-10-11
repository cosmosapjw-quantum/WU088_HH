# PHYS09 — 에너지 행을 먼저 계산한 유한 HH–photo 상호작용

2026-10-11. 이 문서는 보존된 NCP07 source export에서 실제 수행한 PHYS09 포함 계산을 수학적 결론으로 연결한다. 새 최초 실행 `projected_first`는 두 first-stage family 모두에서 **에너지 혼합응답과 유한 상호작용의 엄밀한 음수**를 얻었다. 이 결과는 원 source-inclusion 전제에 조건부이며 native root 실행·권한을 뜻하지 않는다.

이론 작성자는 과학 코드·source·수치 프로그램을 실행하지 않았고, 실행 owner가 보존한 코드·JSON·로그를 읽었다. 아래 항등식과 조건부 정리는 **derived**, §9의 exact rational 결과는 **numerically checked / implementation-verified**이며 최종 채택은 별도 독립 판정을 따른다. 이론 작성자는 최종 독립 판정자가 아니다.

## 1. 새 의무와 핵심 식

기체의 열·이온화 에너지

\[
e(g)=\ell g,
\qquad
\ell=(\chi_H,f\chi_{\rm HeI},f(\chi_{\rm HeI}+\chi_{\rm HeII}),1)
\tag{1}
\]

를 연구한다. HH는 같은 반응에서 열에너지를 잃고 이온화에너지를 얻으므로 이 선형 에너지에 직접 기여하지 않는다. 그렇다고 HH와 photo의 유한 상호작용이 0이 되는 것은 아니다. HH가 바꾼 gas 상태는 photo 흡수, nonphoto 반응 및 팽창 손실을 바꾸며 이 변화는 implicit stage 안에서 피드백된다.

PHYS07 reference 계산에서 각각 포함한 \(W_x\)와 \(W_w\)를 마지막에 더한 \(\ell[W]\)는 0을 포함했다. PHYS09의 새 의무는 source 수준에서 정확한 HH cancellation을 먼저 사용하고, 유한 stage의 모든 혼합 응답 항을 다시 포함하는 것이다. 현재 대상은 PHYS07 analytic-reference tuple과 구별되는 **NCP07이 실제로 보존한 고정 scalar leaves와 COMMON coefficient family의 실수 source**다.

\[
G(g,\lambda,b)=g-g_{\rm old}-dF(g,\lambda,b)=0,
\qquad \mathcal E=\ell F
\tag{2}
\]

로 놓고 동일 근 family에서

\[
U=\partial_\lambda g,\quad V=\partial_b g,
\quad W=\partial_{\lambda b}g
\]

를 정의하면, 새로 평가할 정확한 식은

\[
\boxed{
W_e=d\left\{
\mathcal E_g W+
\mathcal E_{gg}[U,V]+
\mathcal E_{g\lambda}V+
\mathcal E_{gb}U+
\mathcal E_{\lambda b}
\right\}.}
\tag{3}
\]

\(W\) 자체는 원 residual의 모든 signed 항을 사용하여 먼저 포함한다. 식 (3)은 별도 근사나 leading-order 식이 아니다. 같은 실수 implicit 방정식의 scalar energy 행을 두 번 미분한 항등식이다. 원 thermal-\(w\) 상자에서만 평가하므로 새 energy-coordinate 상자의 source coverage를 요구하지 않는다.

## 2. 대상 family, 단위와 고정 계수 양화사

### 2.1 좌표와 입력

\[
g=(x,y_1,y_2,w)
=(x_{\rm HII},y_{\rm HeII},y_{\rm HeIII},w[\mathrm{eV/H}]),
\quad (\lambda,b)\in\Theta=[0,1]^2.
\tag{4}
\]

\(\lambda\)는 미래 HH source의 강도이고 \(b\)는 미래 photon birth의 강도다. 과거 HH ON 이력과 COMMON의 primal compensation은 그대로 유지한다. Full과 first-half는 각각 동일 COMMON에서 시작하는 첫 stage다. First-half 결과를 다음 단계에 전달한 carried second-half는 이 문서의 대상이 아니다.

Stage별 duration은 보존된 `dt_bits`의 정확한 binary64 실수 값으로, full은 \(1.25\times10^9\) s, first-half는 \(6.25\times10^8\) s다. \(\lambda,b\)는 무차원이므로 \(U,V,W\)의 첫 세 성분은 fraction, 네 번째 성분은 eV/H다. \(W_e\)와 유한 \(I_e\)의 단위는 eV/H다. \(F\)의 앞 세 성분은 \(\mathrm{s}^{-1}\), 열 성분과 \(\mathcal E\)는 \(\mathrm{eV/H/s}\)다.

Source 온도는

\[
\widehat f=
\frac{\operatorname{exact}(n_{\rm He}^{\rm stored})}
     {\operatorname{exact}(n_H^{\rm stored})},
\quad
p=1+\widehat f+x+\widehat f(y_1+2y_2),
\quad
T=\frac{2\operatorname{exact}(\epsilon_{\rm eV})}{3\operatorname{exact}(k_B)}\frac{w}{p}.
\tag{5}
\]

여기서 \(f=\operatorname{exact}(f_{\rm He}^{\rm stage})\)와 \(\widehat f\)는 서로 다른 계수다. 에너지 식 (1)과 photo ion fraction의 정규화에는 \(f\), FT03 및 HH 온도에는 저장 밀도비 \(\widehat f\)가 들어간다. \(f=\widehat f\)라는 추가 등식을 사용하지 않는다. \(c,k_B\), eV-to-erg 변환 계수를 보존하며 자연단위를 도입하지 않는다. 이 계산에 metric tensor는 나타나지 않으며 기본 signature \((-,+,+,+)\)와 충돌하지 않는다.

### 2.2 같은 계수 family를 유지한다는 뜻

\(\alpha\)를 COMMON의 허용된 고정 gas/photon/guard 값, transport·angular coefficient, 저장 scalar leaves 등으로 구성한 한 coefficient tuple이라고 쓰자. 물리적 첫 stage의 incoming은

\[
N_j(b;\alpha)=\overline N_j(\alpha)+bM_j(\alpha),
\qquad M_j=\partial_bN_j
\tag{6}
\]

이며 \(g,\lambda\)에는 의존하지 않는다. \(M_j\)는 photons/H 단위의 유한 amount이고 source rate가 아니다. 그 scalar birth leaf는 \(\operatorname{exact}(\operatorname{fl}(dS_*))\)에 결박된다. 원 angular 포함 및 모든 signed tails를 유지하며 \(M_j\)를 \(dS_*\), \(M_j/d\), 또는 다른 reference의 direction sum으로 바꾸지 않는다.

아래 정리는 **source의 실제 관계들과 보존된 포함에 허용되는 각 고정 \(\alpha\)**에 대해 성립한다. \(\alpha\)는 \(\Theta\) 전체에서 같은 값이다. 매개변수가 변할 때 interval 안에서 입력 또는 source 계수를 임의로 다시 고르는 함수는 연구 대상이 아니다. 특히 네 corner마다 서로 다른 COMMON이나 transport tuple을 선택하여 빼는 것은 유한 상호작용의 정의를 바꾼다. Interval extension이 여러 종속량을 독립적으로 감싸 폭이 넓어진다는 사실은 이러한 family 일관성을 포기한다는 뜻이 아니다.

실제 scalar native program 전체의 반올림·guard·clipping이 C²라고 주장하지 않는다. 미분 대상은 고정된 leaf들을 실수에 정확히 올린 source 식이며, 보존된 native interval kernel이 그 값·미분을 포함한다는 사실은 이 루프에서 **상속하는 source-inclusion 전제**다. PHYS09의 rational 후처리는 이 전제 위의 새 산술을 검증한다. 원 초월함수 kernel, transport trace와 provider 정확성을 처음부터 다시 증명한 결과가 아니다.

## 3. source와 저장 slot의 직접 대응

이 패키지에서 `RAW`는 `inputs/ncp07/raw`를 뜻한다.

| 수학적 대상 | 원 source·보존 자료 |
| --- | --- |
| \(G=g-g_{old}-dF\), nonphoto clone, HH·photo·팽창의 합 | `RAW/candidate/src/phys04_mixed.rs::phys04_reduced_residual` |
| stored \(n_{He}=\operatorname{fl}(n_Hf)\) | `RAW/candidate/src/coupled_primary.rs::model` |
| FT03의 \(\widehat f\), \(p,T\), collisional/recombination/dielectronic 식 | `RAW/candidate/src/ft03_interval.rs::ft03_interval_rhs` |
| source energy leaf, \(J_{norm}\), rounded-heat 보정 | `RAW/src/energy.rs::{transform,export,heat_epsilon}` |
| 같은 COMMON PreBE 및 whole-box/centre export | `RAW/src/sourcebox.rs::{source_stage,export,source_components}` |
| \(X\), 열린 gas chart 및 계수 guard | `RAW/results/{full,first_half}/C2_DOMAIN.json`, `RAW/theory/NATIVE_SOURCE_C2_KO.md` |
| 정확한 native \(X\), 중심·radius의 bit words | `RAW/inputs/FROZEN_SOURCE_CONTRACT.json::frozen_words` |
| \(A,G_\lambda,G_b,G_{\lambda b},G_{g\lambda},G_{gb},G_{gg}\) | `RAW/results/{full,first_half}/SOURCE_BOX.json` |
| whole \(\Theta\)를 사용한 \(G(g_c,\Theta)\) | 같은 stage의 `SOURCE_CENTRE.json` |
| 저장된 고정 preconditioner \(C\) | 같은 stage의 `UNIFORM_ARITHMETIC.json::fixed_C` |
| \(\mathcal E\) 조립용 nonphoto 및 33×3 rate Jets | 같은 stage의 `SOURCE_BOX_COMPONENTS.json` |

Source의 일반 Jet는 `value`, `gradient[7]`, `signed_hessian[7][7]`를 갖는다. Gas slot은 0–3, \(\lambda\)는 4, \(b\)는 5다. 이 계산의 6개 독립 변수에 속하지 않는 slot 6을 매개변수로 재해석하지 않는다. 보존 파일에는 원 7-slot 배열 전체가 남는다. 예를 들어

\[
G_{g_k\lambda}\leftrightarrow\texttt{signed\_hessian[k][4]},
\qquad
G_{g_kb}\leftrightarrow\texttt{signed\_hessian[k][5]}.
\tag{7}
\]

혼합 Hessian은 저장된 signed 값을 그대로 사용한다. 양수 부분만 선택하거나 대칭화를 통해 서로 다른 endpoint를 대체하지 않는다. Interval의 `lo_bits`, `hi_bits`가 정확한 입력이며 decimal display와의 bit roundtrip을 확인한다.

## 4. 정리 1 — HH를 제거한 정확한 source energy 행

HH source를

\[
H(g)=q(g)h,\qquad h=(1,0,0,-\chi_H)
\tag{8}
\]

라 하자. 동일 \(\chi_H\) leaf가 source 양쪽에 사용되므로

\[
\ell h=0,\quad \ell H=0,\quad
\ell H_gv=0,\quad \ell H_{gg}[u,v]=0
\tag{9}
\]

가 임의의 \(u,v\)에 정확히 성립한다. 이는 원 interval을 0으로 편집해서 얻는 결과가 아니라 source reaction vector의 대수적 항등식이다.

흡수 채널 \(a\in\{\mathrm{HI},\mathrm{HeI},\mathrm{HeII}\}\)와 노드 \(j\)의 보존된 rate를 \(r_{ja}\), heat leaf를

\[
a_{ja}=\operatorname{exact}(\operatorname{fl}(E_j-\chi_a))
\]

라 두자. 각 채널의 gas 방향은

\[
v_{jH}=(1,0,0,a_{jH}),\quad
v_{jI}=(0,1/f,0,a_{jI}),\quad
v_{jII}=(0,-1/f,1/f,a_{jII}).
\]

따라서 \(f\)를 정확히 같은 계수로 사용하면

\[
\ell v_{ja}=a_{ja}+\chi_a.
\tag{10}
\]

Source 분해는

\[
F=F^{np}+\lambda H+
\sum_{ja}r_{ja}v_{ja}-2H_{mean}w\,e_w
\tag{11}
\]

이므로 식 (9)–(10)을 적용하면

\[
\boxed{
\mathcal E(g,\lambda,b)=\ell F
=\ell F^{np}
+\sum_{j,a}(a_{ja}+\chi_a)r_{ja}
-2H_{mean}w.}
\tag{12}
\]

이것이 먼저 구성할 energy Jet다. HH의 실제 상태 피드백은 \(U,V,W\)와 전체 \(G\) 미분 안에 남아 있다. 식 (12)에서 사라지는 것은 동일 gas에서의 HH 직접 energy 기여다.

### 4.1 계수 보정을 자동으로 보존하는 방식

\(a_{ja}+\chi_a\)는 두 captured leaf의 **정확한 실수 합**이다. \(\epsilon_{ja}=a_{ja}-(E_j-\chi_a)\)라 쓰면 \(a_{ja}+\chi_a=E_j+\epsilon_{ja}\)다. 모든 노드의 \(\epsilon=0\)을 가정하여 \(E_j\)로 바꾸지 않는다. 이는 원 `energy.rs::heat_epsilon`과 연결되는 algebra다.

Nonphoto는 \(\ell F^{np}\)를 그대로 투영한다. 그 성분은 FT03가 사용한 stored-density 비율로 정규화되어 있으므로

\[
J_{norm}=(f-\widehat f)
\{\chi_{\rm HeI}F^{np}_{y_1}
+(\chi_{\rm HeI}+\chi_{\rm HeII})F^{np}_{y_2}\}
\tag{13}
\]

라는 normalization 차이가 이미 식 (12)에 포함된다. \(f=\widehat f\)라고 두어 지우지 않고, 동일 \(J_{norm}\)을 별도 항으로 다시 더하여 이중 계수하지도 않는다. 저장 nonphoto의 collisional·recombination·dielectronic 및 kinetic-loss 항은 모두 유지된다.

### 4.2 구조적 zero와 numerical tail의 분리

실제 첫-stage source에서 식 (12)의 실수 함수는 fixed gas에서 \(\lambda\)에 독립이다. 따라서 그 실제 \(\mathcal E_{g\lambda}\)와 \(\mathcal E_{\lambda b}\)는 0이다. 그러나 저장된 nonphoto/rate Jets에는 원 구간 연산으로 생긴 signed tails가 남아 있다. PHYS09의 수치 계산은 식 (12)의 **모든 33×3 rate와 네 nonphoto 성분의 원 gradient·Hessian**을 사용해 energy Jet를 만든다. \(\lambda\) 관련 포함이 0을 감싸더라도 scalar 식 (3)에 실제로 더한다.

He cross-section leaf가 정확히 0인 현재 grid에서도 저장 He rate의 작은 signed 폭을 버리지 않는다. Node32를 포함한 전체 rates를 합산한다. Drift \(-2H_{mean}w\)는 별도로 알려진 affine 실수 항으로 정확히 미분하며, 원 input 배열을 변경하는 일이 아니다.

## 5. 정리 2 — 고정 source family의 균일 C² 근

### 5.1 두 상자의 구분과 상속 전제

\(X\)는 `C2_DOMAIN.json`의 보존된 native endpoint 상자다. 표시상 \([.90,.93]\times[.29,.31]\times[.59,.61]\times[13,14]\)이지만 실제 끝점은 밖으로 넓어진 binary64 words다. 원 `frozen_words`의 정확한 중심과 radius를 \(g_c,r\)라 하고

\[
Y=g_c+\prod_i[-r_i,r_i]
\tag{14}
\]

로 정의한다. \(Y\subseteq X\)를 정확한 bit-lift 산술로 확인한다. Native source producer는 외향 `centre±radius`도 \(X\)가 덮도록 첫 source 호출 전에 \(X\)를 확장했다. 따라서 \(X\)를 이상적인 십진 상자로 바꾸거나 \(Y=X\)라고 생략하지 않는다.

고정 \(\alpha\)에서 다음 source 전제를 상속한다.

1. \(G\)는 \(X\times\Theta\)를 포함하는 적절한 열린 실수 chart에서 C²다.
2. `SOURCE_BOX`의 모든 미분은 전체 \(X\times\Theta\)의 실제 미분을 포함한다.
3. `SOURCE_CENTRE`는 같은 coefficient family 및 \(\Theta\) 전체에 대한 \(G(g_c,\Theta)\)를 포함한다.
4. 구성한 energy Jets는 식 (12)의 같은 함수와 미분을 포함한다.

C²의 source 근거는 양의 \(w,p,T\), strict simplex, 양의 photo denominator, HH와 FT03의 positive-base power·exp·rational 식, 고정 provider threshold chart 및 gas와 독립인 고정 transport geometry다. 원 `C2_DOMAIN`은 \((.899,.931)\times(.289,.311)\times(.589,.611)\times(12.9,14.1)\) 주변의 엄밀한 source guard 여유를 기록한다. \(\lambda,b\)의 작은 열린 수학적 연장은 affine source 식과 양의 denominator로 정의할 수 있다. 이때 native runtime의 입력 gate를 수정하거나 범위 밖 호출을 실행하지 않는다.

### 5.2 실제로 확인해야 할 부등식

보존된 고정 matrix를 exact binary64 lift한 \(C\)와 \([A]=[G_g(X,\Theta)]\)를 사용하여

\[
[K]=I-C[A],\quad
\beta_i=\operatorname{mag}[(CG(g_c,\Theta))_i],
\quad B_{ij}=\operatorname{mag}[K_{ij}],
\tag{15}
\]

\[
\gamma=\max_i\sum_jB_{ij}\frac{r_j}{r_i},
\qquad
m_i=r_i-\beta_i-\sum_jB_{ij}r_j
\tag{16}
\]

를 정의한다. \(r_i>0\), \(\gamma<1\), 모든 \(m_i>0\)를 확인한다. \(C\)는 source-center Jacobian의 저장된 한 representative에서 만들어진 상수이며 parameter-dependent inverse로 교체하지 않는다. PHYS09는 원 floating-point inverse를 다시 계산할 필요가 없다. \(\det C\ne0\)의 exact 확인을 사용할 수 있고, 이론상으로도 \(CA=I-K\)의 가역성에서 정사각 \(C,A\)의 가역성이 따른다.

**정리.** 위 source 전제와 부등식이 성립하면, 각 \(\theta\in\Theta\)에서 \(G(g,\theta;\alpha)=0\)인 근이 \(Y\) 내부에 존재한다. 이 근은 전체 \(X\) 안에서 유일하며 \(\theta\)에 대해 C²다.

**증명.** \(\alpha,\theta\)를 고정하고 \(\mathcal T(g)=g-CG(g,\theta;\alpha)\)라 하자. \(g\in Y\)이면 중심과 \(g\)를 잇는 선분은 \(X\)에 포함된다. 적분형 평균값 정리로

\[
|\mathcal T_i(g)-g_{c,i}|
\le\beta_i+\sum_jB_{ij}r_j=r_i-m_i<r_i.
\tag{17}
\]

따라서 \(\mathcal T\)는 닫힌 완비 상자 \(Y\)를 strict interior로 보낸다. 가중 norm

\[
\|z\|_r=\max_i|z_i|/r_i
\]

에서 같은 평균값 정리는 \(\mathcal T\)의 Lipschitz 상수를 \(\gamma<1\)로 제한한다. Banach 정리에 의해 \(Y\)에 유일한 fixed point가 존재하며, \(C\)가 가역이므로 이 점은 \(G=0\)의 근이다. 전체 \(X\)도 convex이고 같은 derivative bound가 적용되므로, \(X\)의 다른 근이 있으면 두 fixed point의 거리가 그 자신의 \(\gamma\)배 이하가 되어 일치해야 한다.

근에서 \(CA=I-K\)는 \(\|K\|_r<1\)이므로 가역이다. C² implicit-function theorem은 각 근 근처에서 C² parameter branch를 준다. Strict interior margin으로 branch를 \(X\) 안에 유지할 수 있고, 겹치는 parameter 근방의 branch는 \(X\) 안의 유일성에 의해 일치한다. 각 고정 \(\alpha\)에서 compact \(\Theta\)를 덮는 이러한 근방을 붙이면 하나의 C² family를 얻는다. 경계에서도 source의 열린 수학적 연장을 사용하므로 동일 미분이 정의된다. □

이 결론은 nonlinear point iteration이나 corner root 실행을 요구하지 않는다. 동시에 실제 native certificate issuer, BEpoint 결과 또는 floating-point solver의 root를 발행하지도 않는다.

## 6. 정리 3 — 전체 signed implicit 혼합 응답의 포함

\(G(g(\theta),\theta)=0\)의 미분으로

\[
AU=-G_\lambda,\qquad AV=-G_b,
\tag{18}
\]

\[
\boxed{
AW=-\{G_{\lambda b}+G_{g\lambda}V+G_{gb}U+G_{gg}[U,V]\}.}
\tag{19}
\]

각 residual 성분 \(k\)의 마지막 수축은

\[
(G_{gg}[U,V])_k=\sum_{i,j=0}^3(G_k)_{g_i g_j}U_iV_j
\tag{20}
\]

다. PHYS09는 원 \(G_{\lambda b}\)의 signed tail을 포함한 네 종류의 모든 forcing 항을 실제로 사용한다. Fixed-gas 실수 항등식 \(G_{\lambda b}=0\)만으로 mixed response를 0으로 만들거나 저장 항을 생략하지 않는다.

### 네 항 합과 엄밀한 선형 나머지

\(Az=s\)를 고려하자. \(K=I-CA\)이면

\[
z=(I-K)^{-1}Cs
=\sum_{k=0}^3K^kCs+R_4,
\tag{21}
\]

\[
\|R_4\|_r\le
\frac{\gamma^4}{1-\gamma}\|Cs\|_r.
\tag{22}
\]

증명은 \(k=4\)부터의 기하급수 상계를 더하는 것이다. 실제 계산에서는 \([K]\), \([Cs]\)로 첫 네 항을 interval 포함하고, 식 (22)의 exact rational 상한 \(\rho\)를 사용해 성분 \(i\)에 \([-r_i\rho,r_i\rho]\)를 더한다. \(K\)와 \(s\)가 같은 \(g,\theta,\alpha\)에 의존해도 각 실제 항을 감싸므로 유효하다. Dependency를 버린 포함은 폭을 넓힐 수 있지만 independent coefficients라는 물리 전제를 추가하지 않는다.

먼저 식 (18)로 \([U],[V]\)를 얻고, 이를 원 전체 Hessian과 식 (19)에 넣어 \([W]\)를 얻는다. Source \(F\)의 HH와 nonphoto, photo elimination, 팽창은 이 전체 \([G]\) 안에 유지된다. 이 Neumann 나머지는 유한 \(d\)에서의 선형 역작용 나머지다. 시간 이산화 오차, parameter Taylor remainder 또는 continuum error와 동일하지 않다.

## 7. 정리 4 — 먼저 투영한 에너지 식의 포함

고정 \(\alpha\)에서 \(g_{old}\)와 \(d\)는 \(\theta\)와 독립이다. 식 (2)에 \(\ell\)을 곱하고 식 (12)를 쓰면

\[
e(\theta)=e_{old}+d\mathcal E(g(\theta),\theta).
\tag{23}
\]

두 번 미분하면 chain rule에 의해 식 (3)이 그대로 나온다. 예를 들어 첫 미분은 \(U_e=d(\mathcal E_gU+\mathcal E_\lambda)\)이고, 여기에 \(\partial_b\)를 적용하면 \(\mathcal E_gW\), \(\mathcal E_{gg}[U,V]\), \(\mathcal E_{gb}U\), \(\mathcal E_{g\lambda}V\), \(\mathcal E_{\lambda b}\)의 다섯 항을 얻는다. \(e_{old}\)가 고정이라는 첫-stage 전제는 여기서 사용되며 carry derivative가 있는 다음 stage에는 해당 식을 그대로 복사하지 않는다.

**정리.** 정리 2–3의 \([U],[V],[W]\)와 식 (12)에서 각각 유효하게 조립한 전체 energy derivative 포함을 사용하면

\[
[W_e]_{row}=d\left(
[\mathcal E_g][W]+[\mathcal E_{gg}][[U],[V]]
+[\mathcal E_{g\lambda}][V]
+[\mathcal E_{gb}][U]+[\mathcal E_{\lambda b}]
\right)
\tag{24}
\]

는 모든 동일-family \(W_e(\theta;\alpha)\)를 포함한다. 특히 그 상계가 엄밀한 음수이면 전체 \(\Theta\)에서 \(W_e<0\)다.

이는 interval의 기본 포함 보존성과 식 (3)으로 바로 따른다. 원 component별 \([W]\)로 만든

\[
[W_e]_{direct}=\sum_i\ell_i[W_i]
\tag{25}
\]

도 유효한 포함이다. 두 표현은 일반적으로 endpoint가 다르다. Direct 포함이 0을 감싸면서 row 포함이 음수일 수 있다. Source identity를 먼저 사용하면 서로 같은 HH amplitude에서 생기는 cancellation을 보존하기 때문이다. 두 구간의 overlap은 identity의 증명이 아니며, 서로 다른 입력 tuple이나 domain을 연결해도 된다는 뜻도 아니다. 같은 family와 source identity를 이미 확보한 뒤 비교하는 진단값이다.

### 물리적 source 기여와 유한 피드백

Fixed-gas 실수 식에서 \(\mathcal E_{gb}=\ell(P_M)_g\), \(P_M=\partial_bP_N\)다. 같은 첫-stage family에서 \(U=dA^{-1}H\)이므로 \(\Delta U=U-dH\)라 놓으면 고정된 유한 \(d\)에서도

\[
d\mathcal E_{gb}U
=d^2\ell(P_M)_gH+d\ell(P_M)_g\Delta U
\tag{26}
\]

가 정확히 성립한다. \(AU=dH\)이므로 \(\Delta U=(I-A)U\)라는 정확한 표현도 쓸 수 있다. 실제 코드는 서로 독립인 \([U]-d[H]\)를 빼는 대신 \((I-[A])[U]\)로 이 feedback을 포함했다. PHYS08은 첫 source projection \(\ell(P_M)_gH\)의 엄밀한 음수를 확인했다. 이것은 HH가 neutral H를 감소시켜 이후 photo absorption의 gas-energy 전달을 줄이는 방향이다. 이 식은 rounded duration·birth leaf를 \(d\)에 대해 미분하거나 \(M\)을 unrounded source rate로 치환하는 전개가 아니다.

그러나 PHYS09의 유한 판정은 leading 항의 부호를 채택하는 방식이 아니다. \(\mathcal E_gW\), \(\mathcal E_{gg}[U,V]\), \(U-dH\)를 포함한 전체 implicit 응답, nonphoto 및 팽창, numerical parameter tails와 Neumann tail을 실제로 모두 포함한 식 (24)의 부호로 결정한다. 어떤 나머지가 음의 여유를 넘으면 결과는 OPEN이며, 허용 precision·원 상자·source 값을 바꾸어 부호를 강제하지 않는다.

### 온도 관측량

같은 계산에서 온도를 보고한다면

\[
W_T=T_gW+T_{gg}[U,V]
\tag{27}
\]

의 두 항이 모두 필요하다. \(a=(1,\widehat f,2\widehat f,0)\), \(e_w=(0,0,0,1)\), \(C_T=2\epsilon_{eV}/(3k_B)\)로 쓰면

\[
T_g=C_T\left(\frac{e_w}{p}-\frac{wa}{p^2}\right),
\quad
T_{gg}=C_T\left(
-\frac{e_wa^\mathsf T+ae_w^\mathsf T}{p^2}
+\frac{2waa^\mathsf T}{p^3}\right).
\tag{28}
\]

이는 원 thermal-\(w\) 상자에서의 rational 식이므로 source 초월함수를 다시 평가할 필요가 없다. \(T\)에 explicit \(\lambda,b\) dependence는 없고 stage \(\widehat f\)는 고정이다.

## 8. 정리 5 — corner 실행 없이 유한 energy 상호작용

동일 C² root family의

\[
I_e=e(1,1)-e(1,0)-e(0,1)+e(0,0)
\tag{29}
\]

에 적분의 기본정리를 두 번 적용하면

\[
\boxed{
I_e=\int_0^1\!\int_0^1W_e(\lambda,b)\,db\,d\lambda.}
\tag{30}
\]

단위 사각형의 넓이는 1이고 interval은 convex다. 따라서 \([W_e]_{row}\)의 uniform 포함은 같은 \(I_e\)의 포함이기도 하다. 엄밀한 음의 상계는 \(I_e<0\)를 뜻한다. Corner를 실제 계산하지 않았다는 사실은 이 적분 항등식을 약하게 만들지 않지만, 미계산 corner 값이나 native nonlinear root를 관측했다는 주장도 허용하지 않는다.

일반 rectangle의 경우 넓이를 곱해야 하며, 다른 COMMON·coefficient tuple 또는 다른 terminal stage를 섞으면 식 (30)을 적용할 수 없다. 여기의 \(e(0,0)\)는 두 미래 switch가 꺼진 **stage 이후의 근 에너지**다. 이것을 stage 이전의 COMMON \(e_{old}\)로 바꾸지 않는다.

\(I_e<0\)의 물리적 뜻은 결합된 미래 HH와 birth의 기체 에너지 변화가 각 작용을 따로 켰을 때의 단순 합보다 작다는 것이다. 이것만으로 결합 상태의 절대 에너지 감소, total photon+gas+escape conservation, 장시간 냉각, 두-half/full defect 또는 continuum sign을 말할 수는 없다. \(e\)는 thermal 및 ionization gas energy이며 escaped/retained photon, guard 및 redshift ledger 전체 에너지와 구별된다.

## 9. 수치 결과와 실행 근거

### 9.1 최초 실행과 증거 identity

`diagnostics/analyze_projected_exports.py --run-id projected_first`의 최초 새 실행은 2026-10-11 06:37:01.943571 UTC에 시작해 06:37:02.821933 UTC에 exit 0으로 끝났다. 사용한 source/input 21개는 실행 전후 byte·SHA가 모두 같았다. 보존된 실행 근거는 `evidence/projected_first/EXECUTION.json`이다. 이론 작성자는 이 결과를 읽었으며 과학 프로그램을 별도로 재실행하지 않았다.

| 관측 | 실제 기록 |
| --- | --- |
| 최초 실행 상태 | PASS, exit 0; 실패·수정 실행 없음 |
| 경과시간 / Linux 최대 RSS | 0.8762889720092062 s / 26,184 KiB |
| 실행 한도 | 45 s / 384 MiB / 각 로그·파일 16 MiB |
| 원 interval records의 bit/display 검사 | stage마다 7,096개; 고유 물리 표본 수라는 뜻은 아님 |
| Assertions / 의미 사례 | 48 / 8; 48을 고유 test 수로 세지 않음 |
| 후속 consumer의 입력 rows | 총 12,594개, 원 endpoint bits로 구성 |
| stdout / stderr | 3,127 bytes / 0 bytes |
| 새 native source callback / native solver | 0 / 0, 이번 Python 경로의 실행 범위 |
| 실제 source corner root / 새 source 초월함수 / 과거 science replay | 0 / 0 / 0 |

이 표의 0은 이 Python 후처리 경로에 대한 기록이다. 과거 NCP07에서 계측하지 않은 counter를 0으로 덮어쓰지 않는다. 8개 의미 사례에는 비자명한 Neumann tail, 같은 반응벡터의 exact cancellation과 독립 interval의 차이, 음수·양수·0-touch, signed 최소 subnormal, 해석적으로 풀리는 두 좌표 HH/photo 모델의 유한 항등식, contraction/radius domain 거부가 들어 있다. Toy의 명시적 해 평가를 실제 source corner root 실행으로 세지 않는다.

| 파일 | SHA256 |
| --- | --- |
| `results/projected_first/PROJECTED_RESULTS.json` | `c6329fed8c411e1592bd1a0c63ebd9ca6151e81500ed1f46fb6b40f4b7758444` |
| `results/projected_first/GOLDEN_ORACLE.json` | `df7b7f88b99764c4c54ae2e3ffac79e23e27cd6b01abba040f4a01cb1e406752` |
| `results/projected_first/GATE_INPUTS.tsv` | `a371d7f54ee4eb57bcb5095e928e6d9647e8dc2bcd7a9d3e5f5eca6225ef05da` |
| `diagnostics/analyze_projected_exports.py` | `51c933ca4f85db4dc4874623e6ee8978d9cc6ce4b743cfc6594473e5d4d3d56e` |
| `evidence/projected_first/EXECUTION.json` | `5fc4d717766f9df23822bcd231858e85c5601795e0cf139b0dadc10c23c7b92f` |
| `evidence/projected_first/stdout.txt` | `6c93354f372f96616f04f2718ec53c7075ac5ac95bcd419bd5976203213bbbc4` |

### 9.2 Root·선형 역작용의 실제 여유

새 exact-rational 산술은 원 `fixed_C`, 원 \(X\), 같은 center/radius와 source exports를 사용해 \(Y\subseteq X\), nonsingular \(C\), strict self-map과 contraction을 확인했다. 아래 소수 상계·하계는 저장된 exact rational 값보다 바깥쪽으로 넓힌 표시다.

| Stage | \(\gamma\) 상계 | \(\det C\)의 양의 하계 | \((m_x,m_{y_1},m_{y_2},m_w)\)의 양의 하계 |
| --- | --- | --- | --- |
| Full | 0.000117368306 | 0.99897337 | (0.0132212759, 0.0099645317, 0.0099927001, 0.4347537869) |
| First-half | 0.000058538715 | 0.99948556 | (0.0131799520, 0.0099647231, 0.0099927297, 0.4345536146) |

따라서 정리 2의 모든 strict 산술 조건이 실제로 성립한다. 이 값은 새 native root 호출이 아니라 기존 source 포함에 대한 exact rational 재표현이다. 같은 입력을 갖는 NCP07의 외향 binary64 표시와 마지막 자리까지 같을 필요가 없다.

네 항 Neumann 합 뒤의 가중 tail 상한은 다음과 같다. 성분 \(i\)의 실제 tail 반경은 각 값에 \(r_i\)를 곱한 것이다.

| Stage | \(\rho_U\) 상계 | \(\rho_V\) 상계 | \(\rho_W\) 상계 |
| --- | --- | --- | --- |
| Full | \(3.958106\times10^{-24}\) | \(1.830261\times10^{-22}\) | \(1.852216\times10^{-30}\) |
| First-half | \(1.225244\times10^{-25}\) | \(2.835102\times10^{-24}\) | \(1.435617\times10^{-32}\) |

### 9.3 에너지의 0-containing 포함이 엄밀한 음수로 좁아진 결과

다음 표는 결과 JSON의 exact endpoints를 포함하도록 바깥쪽으로 넓힌 십진 유리수 구간이다. \(W_x,W_{y_1},W_{y_2}\)는 fraction, \(W_w,W_e\)는 eV/H, \(W_T\)는 K다. 같은 표의 uniform bounds가 정리 5에 의해 해당 finite unit-square interactions도 포함한다.

| 관측량 | Full 포함 | First-half 포함 |
| --- | --- | --- |
| \(W_x\) | \([-1.464016\times10^{-16},-4.625587\times10^{-17}]\) | \([-1.833750\times10^{-17},-5.798310\times10^{-18}]\) |
| \(W_{y_1}\) | \([-1.855750\times10^{-22},6.511630\times10^{-22}]\) | \([-1.161413\times10^{-23},4.076338\times10^{-23}]\) |
| \(W_{y_2}\) | \([-4.994538\times10^{-24},2.557653\times10^{-23}]\) | \([-3.123793\times10^{-25},1.601392\times10^{-24}]\) |
| \(W_w\) | \([4.231222\times10^{-16},1.376122\times10^{-15}]\) | \([5.300612\times10^{-17},1.722442\times10^{-16}]\) |
| \(W_T\), 전체 Hessian chain term 포함 | \([2.589911\times10^{-12},8.848513\times10^{-12}]\) | \([3.245291\times10^{-13},1.107859\times10^{-12}]\) |
| 독립 성분 합 \([W_e]_{direct}\) | \([-1.567710\times10^{-15},7.471155\times10^{-16}]\) | \([-1.963552\times10^{-16},9.339629\times10^{-17}]\) |
| **에너지 행을 먼저 계산한 \([W_e]_{row}\)** | **\([-6.192853\times10^{-16},-2.012354\times10^{-16}]\)** | **\([-7.759699\times10^{-17},-2.535731\times10^{-17}]\)** |

두 stage 모두 \(W_x<0\), \(W_w>0\), \(W_T>0\), 새 \(W_e<0\)가 엄밀하다. Helium mixed components는 0을 포함하므로 부호를 정하지 않는다. Direct energy 포함은 두 경우 모두 0을 포함한 원래 계산 결과로 그대로 보존했다. 새 row 포함의 엄밀한 음수는 원 상자를 줄이거나 음수 endpoint를 골라서 얻은 것이 아니다.

이 새로운 captured-source 결과가 과거 PHYS07 analytic-reference energy OPEN을 소급 변경하지 않는다. Family의 물리·수학적 정의와 입력 tuple은 서로 구별되며, 향후 그 reference의 energy도 같은 방법으로 별도 분석하려면 해당 작업이 따로 필요하다.

### 9.4 유한 피드백과 모든 signed tails의 항별 크기

다음 항들은 식 (24)의 실제 합이다. 모든 행의 단위는 eV/H다. 작은 numerical \(\lambda\) tails도 계산에 포함되어 있다. 아래 표시는 exact 포함보다 바깥으로 넓혔다.

| 항 | Full 포함 | First-half 포함 |
| --- | --- | --- |
| \(d\mathcal E_gW\) | \([4.246836\times10^{-19},1.964183\times10^{-18}]\) | \([2.671001\times10^{-20},1.231868\times10^{-19}]\) |
| \(d\mathcal E_{gg}[U,V]\) | \([-7.780629\times10^{-20},7.263218\times10^{-20}]\) | \([-4.789754\times10^{-21},4.626792\times10^{-21}]\) |
| \(d\mathcal E_{g\lambda}V\), numerical tail | \([-1.049\times10^{-318},1.049\times10^{-318}]\) | \([-1.311\times10^{-319},1.311\times10^{-319}]\) |
| \(d\mathcal E_{gb}U\) | \([-6.196322\times10^{-16},-2.032723\times10^{-16}]\) | \([-7.761891\times10^{-17},-2.548512\times10^{-17}]\) |
| \(d\mathcal E_{\lambda b}\), numerical tail | \([-6.568\times10^{-311},6.568\times10^{-311}]\) | \([-3.284\times10^{-311},3.284\times10^{-311}]\) |

앞서 유도한 고정-\(d\) source/feedback 분해도 독립 표현으로 저장했다. 코드의 `source_leading_energy`는 \(L=d^2\mathcal E_{gb}H\), `birth_feedback_remainder`는 \(d\mathcal E_{gb}(I-A)U\)다. `finite_remainder_energy`는 이 birth feedback에 다른 네 scalar 항을 더한 \(R\)이며, 실제 함수에는 \(W_e=L+R\)가 정확히 성립한다. 이 별도 포함과 row 포함의 overlap은 진단일 뿐 identity의 대체 증명이 아니다.

| Stage | \([L]\) | \([R]\) | \(\operatorname{mag}[R]/(-\sup[L])\)의 상계 |
| --- | --- | --- | --- |
| Full | \([-6.202143\times10^{-16},-2.035303\times10^{-16}]\) | \([5.410865\times10^{-19},2.701364\times10^{-18}]\) | 0.013273 |
| First-half | \([-7.7655441\times10^{-17},-2.550130\times10^{-17}]\) | \([3.412139\times10^{-20},1.694898\times10^{-19}]\) | 0.006647 |

즉 포함한 전체 나머지의 절댓값 상한은 source 항의 엄밀한 음수 여유보다 각각 약 1.3273%, 0.6647% 이하로 작다. Source 항의 부호만 채택한 것이 아니라, 유한 feedback 전체가 그 부호를 뒤집지 못한다는 여유를 실제 계산했다. 이 비율은 두 duration 사이의 convergence order 또는 time error 추정치가 아니다.

### 9.5 해석적 의미 사례

저장된 의미 사례 `analytic_HH_photo_finite_identity`는 차원 없는 두 좌표 모델

\[
F=\lambda q(1,-\chi)+b(r-sx)(1,a)
\]

에서 같은 cancellation과 유한 상호작용을 손으로 풀 수 있게 만든다. Implicit 식의 해는

\[
x=\frac{x_0+d\lambda q+dbr}{1+dbs},\qquad
w=w_0-d\chi\lambda q+dba(r-sx),
\]

이며 \(e=\chi x+w\)에 대해

\[
\partial_{\lambda b}e
=-\frac{d^2sq(\chi+a)}{(1+dbs)^2},
\qquad
I_e=-\frac{d^2sq(\chi+a)}{1+ds}.
\]

선택된 정확한 유리수 계수에서 네 명시적 해의 유한 차이와 마지막 식이 같고, uniform mixed 포함이 그 차이를 포함함을 실제 의미 검산에서 확인했다. 이는 현재 33×3 source의 수치 증거를 대신하는 물리 모델이 아니라, cancellation과 finite FTC를 함께 검사하는 별도 작은 사례다.

## 10. 채택 범위와 남는 의무

이 문서가 제공하는 것은 고정 source-inclusion 전제 아래의 수학적 정리와 새 포함 산술의 해석이다. PHYS09의 최초 exact-rational 실행은 두 stage의 \(I_e<0\)를 뒷받침하는 모든 부등식을 충족했다. 최종 채택은 별도 독립 review를 따른다. 원 source kernel을 처음부터 재검증하거나 native trusted uniform certificate를 발행한 결과로 승격하지 않는다.

| 항목 | 이 문서의 상태·범위 |
| --- | --- |
| 동일 HH leaf의 exact energy cancellation 및 식 (12) | Derived source identity |
| 원 source에서 energy 행을 먼저 미분한 식 (3) | Derived exact identity |
| C², 원 whole-box source Jet 포함과 same-family provenance | Inherited source premises; 새 kernel formalization 없음 |
| Uniform root, Neumann U/V/W 및 finite FTC | 명시한 전제·strict 부등식 아래 derived |
| PHYS09 row 포함과 유한 energy 부호 | 두 stage 모두 strict negative; derived 및 numerically checked, 최종 독립 판정 별도 |
| PHYS07 analytic-reference의 과거 energy OPEN | 기존 판정 그대로 보존; 소급 변경하지 않음 |
| Actual native root/U/V/W/I 및 native authority | `null` / false / OPEN 유지 |
| Carried second-half, paired defect, 시간·continuum remainder | OPEN 유지 |
| Full49·production·물리 fit의 새 문헌 검증 | 이 결과의 범위 밖 |

최종 claim 목록은 `theory/CLAIMS_PROJECTED_ENERGY.json`, 실제 독립 판정은 `review/DECISION.json`을 따른다. 이론 creator의 파일 작성은 독립적인 PROMOTE 판정이 아니다.
