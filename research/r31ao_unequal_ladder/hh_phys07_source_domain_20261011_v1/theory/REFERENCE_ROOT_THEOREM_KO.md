# PHYS07 — 고정 reference family의 균일 근과 유한 혼합 상호작용

2026-10-11. 이 문서는 고정된 PHYS07 source export와 최초 `source_analysis_first` 결과를 읽어, 계산된 부등식이 어떤 수학적 결론을 주는지 증명한다. 작성자는 이론 creator이며 최종 독립 판정자는 아니다. 새 source, 초월함수, point/root 또는 corner 계산은 이 문서를 작성하면서 실행하지 않았다.

## 1. 결론과 수학적 대상

고정 COMMON 입력에서 시작하는 **full stage**와 **first-half stage** 각각에 대해, 선언한 reference residual은 \(\Theta=[0,1]^2\) 전체에서 아래 gas 상자 안에 유일한 근을 갖는다. 이 근은 매개변수에 대해 C²이고, 계산된 uniform mixed derivative의 포함값은 유한한 네 모서리 상호작용도 포함한다. Endpoint나 corner 값을 실제로 구할 필요 없이 이 결론을 얻었다.

두 결과는 서로 다른 길이의 첫 stage에 대한 것이다. First-half의 출력을 실제 입력으로 사용하는 second-half는 아직 계산하지 않았으므로, 이 문서는 one-full versus two-half defect를 포함하지 않는다. Native source tuple·native root·native \(W,I\)의 동일성도 미해결이다.

### Reference family의 고정

Gas 좌표와 단위는

\[
g=(x,y_1,y_2,w),\qquad
[x]=[y_1]=[y_2]=1,\quad [w]={\rm eV/H}
\tag{1}
\]

이고 \(\lambda,b\)는 미래 HH와 미래 birth의 무차원 강도다. 각 stage의 duration은

\[
d_{\rm full}=1.25\times10^9\ {\rm s},\qquad
d_{\rm first\ half}=6.25\times10^8\ {\rm s}.
\tag{2}
\]

Source constants, density, energy grid, cross-section leaves, COMMON gas와 과거 photon/guard 이력은 해당 `family.json`에 결박돼 있다. Transport는 선언된 isotropic analytic reference이고, stage scalar leaves는 source의 연산 순서와 유일한 correctly-rounded reference 값을 사용한다. Native libm·방향별 연산·실제 preBE tuple와의 동일성은 여기서 가정하지 않는다.

Fixed stage의 born amount는

\[
M_j=\operatorname{exact}(\operatorname{fl}(dS_*))\delta_{j,24},\qquad
N_j(b)=\bar N_j+bM_j,
\tag{3}
\]

다. \(dS_*\)의 반올림 전 값으로 \(M_j\)를 치환하지 않는다. \(\bar N\)는 고정 geometry와 고정 COMMON photons에서 얻은 exact-real remap 값이며, 실제 계산은 이를 외향 interval로 감싼다.

이를 엄밀하게 양화하면 \(\xi\)를 허용된 고정 remap coefficient vector라 쓰고,

\[
G_d(g,\theta;\xi)=g-g_{\rm old}-dF_d(g,\theta;\xi),\qquad
\theta=(\lambda,b)\in\Theta
\tag{4}
\]

를 연구한다. 아래 모든 포함 부등식은 실제 reference의 \(\xi\)를 감싸는 coefficient enclosure 전체를 포함한다. 따라서 각 허용된 \(\xi\)를 **\(\Theta\) 전체에 고정한** family마다 결론이 성립한다. 네 corner마다 \(\xi\)를 독립적으로 골라 서로 다른 family를 빼는 것은 이 정리의 대상이 아니다.

`source_centre.json`의 실제 중심과 전체 상자는 정확한 유리수로

\[
g_c=(183/200,3/10,3/5,27/2),\qquad
r=(3/200,1/100,1/100,1/2),
\]

\[
X=g_c+[-r,r]=[.90,.93]\times[.29,.31]\times[.59,.61]\times[13,14].
\tag{5}
\]

마지막 radius만 eV/H이며 나머지는 무차원이다. \(g_c\)는 선언된 상자의 중심이고 관측된 nonlinear root가 아니다. `source_centre.json`은 이 gas 중심에서 **전체 \(\lambda,b\in[0,1]\)**를 넣은 export다.

## 2. 실제 계산이 제공한 전제

### C² 영역

`theory/SOURCE_C2_DOMAIN_KO.md`는 실제 FT03·HH·reduced-photo 식과 source의 분기를 읽어 열린 gas 이웃을 구성했다. 새 분석에서는 각 stage에서 다음을 실제 정확/외향 산술로 확인했다.

- \(n_H\), stored \(n_{He}\)는 양의 고정 point leaves다.
- \(\widehat f=n_{He}^{stored}/n_H^{stored}\)가 source의 paired blanket 안에 들고, \(.082\le\widehat f\le.084\)다.
- \(7700<2\epsilon_{\rm eV}/(3k_B)<7800\).
- \(U=(.899,.931)\times(.289,.311)\times(.589,.611)\times(12.9,14.1)\)의 closure에서 strict simplex와 양의 thermal energy를 유지한다.
- \(\overline U\)의 온도는 보수적인 \(46200<T<52372\) K 안에 있고, source의 35–60 kK guard에 양의 여유가 있다.
- \(X\)의 모든 photo denominator는 \(D_j\ge1\)이다.

원 source graph의 positive-base powers, exp, rational quotients 및 affine \(\lambda,b\) 의존성은 이 열린 영역에서 C²다. \(\lambda,b\) 경계 밖의 작은 수학적 연장은 동일 실수 식으로 정의한다. 이 연장은 음의 physical stock을 실행하도록 native guard를 수정한다는 뜻이 아니다.

실제 `source_T_K` 포함값의 근사 표시는 두 stage에서 모두

\[
T(X)\simeq[46996.710445734505,\ 51452.88421486554]\,\mathrm{K}
\tag{6}
\]

이고, 열린 이웃 closure의 근사 표시는
\([46607.994644843806,51851.170519165804]\) K다. 이 소수들은 JSON의 `display_float`이며 인증 endpoint는 JSON의 정확한 분자·분모다.

### Whole-box export

`source_box.json`은 \(X\times\Theta\)에서 residual value, 6개 변수 \((g,\lambda,b)\)의 gradient와 Hessian을 포함한다. `source_centre.json`은 같은 \(\Theta\)와 같은 고정 family에 대해 \(g_c\)에서 residual을 포함한다. 분석은 이 파일들을 읽기만 했으며 새 source callback을 호출하지 않았다.

\[
[A]=[G_g(X,\Theta)],\qquad
[Q]=I-[A],\qquad
\beta_i=\operatorname{mag}[G_i(g_c,\Theta)]
\tag{7}
\]

를 정의한다. 이번에는 preconditioner \(C=I\)다. 아래 \(Q\)는 시간적분의 다른 기호와 무관한 residual Jacobian defect다.

가중 최대 노름은

\[
\|v\|_r=\max_i\frac{|v_i|}{r_i},\qquad
\|Q\|_r=\max_i\sum_j|Q_{ij}|\frac{r_j}{r_i}
\tag{8}
\]

이며 서로 다른 gas 성분의 단위를 radius로 정규화한다. 실제 계산은

\[
q_i=\sum_j\operatorname{mag}[Q_{ij}]r_j,\quad
\gamma=\max_i q_i/r_i,\quad m_i=r_i-\beta_i-q_i
\tag{9}
\]

의 exact rational 값과 부호를 기록했다.

| Stage | \(\gamma\)의 근사 표시 | \((m_x,m_{y_1},m_{y_2},m_w)\)의 근사 표시 |
|---|---:|---|
| full | 0.0011531881192975576 | (0.013203889271364342, 0.009964442451287673, 0.009992695906967185, 0.43470855089219) |
| first-half | 0.0005772958701028138 | (0.013171223731727341, 0.009964678456845096, 0.009992727653268899, 0.43453097130376966) |

두 경우 모두 정확한 데이터에서 \(\gamma<1\), 모든 \(m_i>0\)가 성립했다. 마지막 margin의 단위는 eV/H이며 다른 세 margin은 fraction이다. Approximate table의 반올림에 의존해 부호를 판정하지 않았다.

## 3. 정리 1 — \(\Theta\) 전체의 유일한 내부 근

**정리.** 위 고정 reference family와 C² source 영역, whole-box 포함을 사용하면 각 \(\theta\in\Theta\)에 대해 \(G_d(g,\theta;\xi)=0\)인 근 \(g_d(\theta;\xi)\)가 \(X\) 내부에 유일하게 존재한다. \(X\) 밖의 다른 근은 이 정리에서 배제하지 않는다.

**증명.** \(\theta,\xi\)를 고정하고

\[
\mathcal T_{\theta,\xi}(g)=g-G_d(g,\theta;\xi)
\tag{10}
\]

를 정의한다. \(X\)는 닫힌 convex 상자다. \(g\in X\)와 중심 \(g_c\)를 잇는 선분에 적분형 평균값 정리를 적용하면

\[
\mathcal T(g)-g_c=-G_d(g_c,\theta;\xi)
 +\int_0^1\{I-G_g(g_c+t(g-g_c),\theta;\xi)\}(g-g_c)\,dt.
\]

모든 적분점이 \(X\)에 있으므로 성분별로

\[
|\mathcal T_i(g)-g_{c,i}|\le\beta_i+q_i=r_i-m_i<r_i.
\tag{11}
\]

따라서 \(\mathcal T\)는 \(X\)를 그 strict interior로 보낸다. 같은 평균값 표현을 두 점 \(g,z\in X\)에 적용하면

\[
\|\mathcal T(g)-\mathcal T(z)\|_r\le\gamma\|g-z\|_r,
\qquad\gamma<1.
\tag{12}
\]

완비 공간 \(X\)의 수축사상이므로 유일한 fixed point가 존재한다. \(C=I\)에서 fixed-point 방정식은 곧 \(G_d=0\)이다. 식 (11)에 fixed point를 넣으면 그 근의 각 면까지의 거리가 적어도 \(m_i>0\)임을 얻는다. 모든 상계가 \(\Theta\)와 허용된 고정 \(\xi\) 전체에 균일하므로 같은 결론이 각각에 성립한다. □

이 증명은 Banach 정리를 사용했지만 \(\mathcal T\)의 nonlinear point iteration을 실제로 실행하지 않았다. 근의 존재를 증명하는 계산과 근의 좌표를 point solver로 구하는 계산은 서로 다른 작업이다.

## 4. 정리 2 — 유일한 근의 C² 매개변수 의존성

근 위에서도

\[
\|I-A(\theta)\|_r\le\gamma<1,\qquad
A(\theta)=G_g(g_d(\theta),\theta;\xi),
\tag{13}
\]

이므로 \(A(\theta)\)는 모든 \(\theta\)에서 invertible이다. C² implicit-function theorem을 각 근에 적용하면 그 근 근방에 C² parameter branch가 존재한다.

이 국소 branch들이 서로 다른 해를 선택하는 문제는 식 (11)의 strict interior margin과 \(X\) 안의 유일성으로 해결된다. 각 parameter 근방을 충분히 작게 잡으면 branch가 계속 \(X\) 안에 있고, 두 근방의 겹침에서 두 branch는 같은 residual의 \(X\) 안 근이므로 일치한다. 따라서 모든 국소 branch가 하나의 C² family \(g_d(\theta;\xi)\)로 이어진다.

\(\Theta\)의 경계에서는 source formula의 열린 parameter 연장을 사용한다. \(X\times\Theta\)의 compactness, \(m_i>0\), \(1-\gamma>0\), source derivative의 연속성 때문에 충분히 작은 parameter thickening에서 strict inclusion과 contraction을 유지할 수 있다. 그 열린 집합에서 위 논증을 적용한 후 \(\Theta\)로 제한하면, 경계에서의 미분도 같은 C² extension에서 정의된다. 실제 native의 \(\lambda,b\in[0,1]\) 입력 제한은 그대로 유지된다.

## 5. 정리 3 — 네 항 Neumann 합과 검증된 나머지

\(A=I-Q\), \(\|Q\|_r\le\gamma<1\)이므로 임의의 선형계

\[
Az=s
\]

의 해는

\[
z=(I-Q)^{-1}s=\sum_{k=0}^3Q^ks+R_4,
\qquad
\|R_4\|_r\le\frac{\gamma^4}{1-\gamma}\|s\|_r.
\tag{14}
\]

마지막 부등식은 \(k=4\)부터의 기하급수를 합한 것이다. 분석 코드는 interval \([Q]\), \([s]\)를 반복 곱해 첫 네 항을 포함하고,

\[
R_{4,i}\in[-r_i\rho_4,r_i\rho_4],\qquad
\rho_4=\frac{\gamma^4}{1-\gamma}
       \max_i\frac{\operatorname{mag}[s_i]}{r_i}
\tag{15}
\]

를 더했다. Interval 곱에서 같은 \(Q\)의 dependency를 잃어 구간이 넓어질 수 있지만, 각 실제 \(Q(\theta)^ks(\theta)\)의 포함은 유지된다. \(Q\)와 \(s\)가 서로 독립이라는 가정은 필요하지 않다.

이 나머지는 선형 Neumann 급수의 truncation tail이다. 시간 이산화 나머지나 parameter Taylor 나머지가 아니다. 근의 선형응답을 계산하는 algebra가 nonlinear native root certificate를 발행하지도 않는다.

실제 weighted tail 상한의 근사 표시는 다음과 같다.

| Stage | \(\rho_U\) | \(\rho_V\) | \(\rho_W\) |
|---|---:|---:|---:|
| full | \(3.6962552352\times10^{-20}\) | \(1.7091654365\times10^{-18}\) | \(1.7303509636\times10^{-26}\) |
| first-half | \(1.1600666491\times10^{-21}\) | \(2.6842774058\times10^{-20}\) | \(1.3595120724\times10^{-28}\) |

이들은 \(r\)-norm 상한이므로 성분 tail은 식 (15)처럼 radius를 곱해야 한다. Exact values는 `linear_Neumann_tails`에 보존돼 있다.

## 6. 전체 mixed derivative의 포함

\[
U=\partial_\lambda g_d,\quad V=\partial_b g_d,\quad
W=\partial_{\lambda b}g_d
\tag{16}
\]

라 두고 \(G(g_d(\theta),\theta)=0\)을 미분한다. 첫 미분은

\[
AU=-G_\lambda,\qquad AV=-G_b.
\tag{17}
\]

첫 식을 \(b\)로 한 번 더 미분하면

\[
\boxed{
AW=-\{G_{\lambda b}+G_{g\lambda}V+G_{gb}U+G_{gg}[U,V]\}.}
\tag{18}
\]

Hessian contraction은 각 residual 성분의 4×4 gas Hessian에 대해
\(\sum_{ij}(G_k)_{g_i g_j}U_iV_j\)다. 분석은 \(U,V\)를 먼저 식 (14)–(15)로 포함한 뒤, 그 포함값과 source의 모든 gas/parameter Hessian 성분을 식 (18)에 넣고 \(W\)의 선형계에 같은 tail 처리를 적용했다.

이번 COMMON-input first stages에서는 fixed gas에서 \(G_{\lambda b}=0\)이 실제 export에 정확히 나타났다. 이 0 때문에 식 (18)의 다른 세 항이 사라지는 것은 아니다. 이전 HH 역사, nonphoto kinetics, photo elimination과 source의 density normalization은 residual 안에 유지돼 있다. 첫 stage의 식을 second-half carry에 복사하지 않는다.

### 온도와 에너지 관측량

고정 stage에서 \(\phi(g)=T(g)\)인 경우

\[
\boxed{\partial_{\lambda b}T(g_d)
       =T_gW+T_{gg}[U,V].}
\tag{19}
\]

분율 증가에 따른 입자수 효과 때문에 두 번째 항을 생략하면 다른 온도 상호작용을 계산한다. 분석은 source가 제공한 전체 gas \(T\) gradient와 Hessian을 사용했다. 이 fixed stage의 \(\widehat f\)는 \(\lambda,b\)에 독립이므로 explicit parameter derivative는 없다.

에너지 좌표는

\[
e=\ell g,\qquad
\ell=(\chi_H,f\chi_I,f(\chi_I+\chi_{II}),1)
\]

로 선형이며

\[
W_e=\ell W.
\tag{20}
\]

Source의 저장 밀도비 \(\widehat f\)와 stage \(f\), \(J_{norm}\), rounded heat leaf의 차이는 이미 residual에 보존돼 있다. \(\ell\)은 exact-real 선형 관측량이고 native `energy()`의 bitwise 실행 결과로 대체하지 않는다.

### 계산된 포함값

아래는 `SOURCE_ANALYSIS.json`의 exact rational endpoint를 포함하도록 바깥쪽으로 넓힌 십진 구간이다. 각 표의 십진 숫자는 그 자체로 유리수이며 `display_float`를 그대로 인증 endpoint로 사용하지 않았다. \(\lambda,b\)가 무차원이므로 \(W_x,W_{y_1},W_{y_2}\)는 fraction, \(W_w,W_e\)는 eV/H, \(W_T\)는 K다.

| 성분 | Full stage 포함값 | First-half stage 포함값 |
|---|---|---|
| \(W_x\) | \([-1.46553\times10^{-16},-4.61150\times10^{-17}]\) | \([-1.83470\times10^{-17},-5.78948\times10^{-18}]\) |
| \(W_{y_1}\) | \([-7.95465\times10^{-23},6.51665\times10^{-22}]\) | \([-4.96720\times10^{-24},4.07791\times10^{-23}]\) |
| \(W_{y_2}\) | \([5.84861\times10^{-25},2.55991\times10^{-23}]\) | \([3.74038\times10^{-26},1.60210\times10^{-24}]\) |
| \(W_w\) | \([4.22891\times10^{-16},1.37651\times10^{-15}]\) | \([5.29916\times10^{-17},1.72269\times10^{-16}]\) |
| \(W_e\) | \([-1.57000\times10^{-15},7.49420\times10^{-16}]\) | \([-1.96499\times10^{-16},9.35407\times10^{-17}]\) |
| \(W_T\) | \([2.58591\times10^{-12},8.85376\times10^{-12}]\) | \([3.24279\times10^{-13},1.10819\times10^{-12}]\) |

따라서 지정된 reference family에서 \(W_x<0\), \(W_w>0\), \(W_T>0\)가 \(\Theta\) 전체에 성립한다. 이 포함은 \(W_e\)의 부호를 결정하지 못한다. Energy의 구간이 0을 포함한다는 것은 실제 energy interaction이 0이라는 뜻이 아니며, 음수 formal leading coefficient만으로 그 구간을 잘라내지 않는다.

## 7. 정리 4 — corner 실행 없이 유한 상호작용을 포함

위 C² root family의 관측량 \(\phi_d(\lambda,b)=\phi(g_d(\lambda,b))\)에 대해

\[
\mathcal I_{\phi,d}=
\phi_d(1,1)-\phi_d(1,0)-\phi_d(0,1)+\phi_d(0,0)
\tag{21}
\]

를 정의한다. 먼저 \(\lambda\), 다음 \(b\)에 적분의 기본정리를 적용하면

\[
\boxed{\mathcal I_{\phi,d}
 =\int_0^1\!\int_0^1
   \partial_{\lambda b}\phi_d(\lambda,b)\,db\,d\lambda.}
\tag{22}
\]

단위 사각형의 넓이가 1이고 scalar interval은 convex이므로, integrand의 uniform 포함값은 적분의 포함값이기도 하다. Gas component에는 식 (18)의 \([W]\), energy에는 식 (20), temperature에는 식 (19)의 포함값을 사용한다. 따라서 위 표는 같은 reference family의 **유한 \(\mathcal I_x,\mathcal I_w,\mathcal I_e,\mathcal I_T\)**도 포함한다.

이 식은 정확한 discrete family의 항등식이므로 별도의 parameter Taylor remainder가 필요하지 않다. Pointwise mixed derivative 한 값이나 formal cubic 한 항을 적분 대신 사용하는 것도 아니다. \(G_g\)의 역작용은 finite \(d\)에서 Neumann tail과 함께 포함됐고, source Hessian은 전체 \(X\times\Theta\)에서 계산됐다.

네 corner의 근이 존재한다는 사실은 정리 1로 확보했지만 그 좌표를 실제로 평가하지 않았다. 여기의 \(g_d(0,0)\)는 미래 HH와 미래 birth가 꺼진 **stage 이후의 baseline 근**이다. 과거의 photo·HH 이력을 가진 COMMON input \(g_{old}\) 자체로 이 corner를 바꾸지 않는다.

## 8. 물리 해석과 범위

\(\mathcal I_x<0\)는 동일 COMMON history에서 두 미래 작용을 함께 켠 이온화 증가가, 각각을 켰을 때의 증가를 더한 값보다 작다는 뜻이다.

\[
g_{d,x}(1,1)-g_{d,x}(0,0)
 <[g_{d,x}(1,0)-g_{d,x}(0,0)]
  +[g_{d,x}(0,1)-g_{d,x}(0,0)].
\tag{23}
\]

이는 HH와 photo가 같은 neutral substrate를 소모하고, 낮아진 온도가 HH rate를 줄이는 방향과 일치한다. 그 해석을 뒷받침하는 source directional signs와 실제 root-family mixed inclusion은 서로 다른 증거이며 이번 결과에서 함께 연결됐다.

\(\mathcal I_T>0\)는 결합 온도가 각 switch의 단순 가산 예측보다 높다는 뜻이다. 두 source 방향이 각각 온도를 낮춘다는 앞선 결과와 모순되지 않는다. 중복된 냉각 작용이 서로의 반응률을 낮추면 결합된 냉각량은 단순 합보다 작아질 수 있다. **양의 온도 상호작용을 결합 상태의 절대 온도 증가 또는 전체 시간 진화의 heating이라고 읽지 않는다.**

\(\mathcal I_w>0\)도 동일한 additive comparison에 관한 결과다. 반면 \(e\)에는 이온화에너지와 열에너지의 상쇄가 들어가며 현재 전체 포함값은 부호를 결정하지 못했다. 선형 결합에서 생긴 폭을 감추거나 tiny positive/negative 값을 골라 보고하지 않는다.

이번 mixed quantities는 매우 작다. 그것을 직접 계산하지 않은 네 endpoint의 차이로 관측했다고 주장하지 않으며, source derivative와 포함 정리를 통해 얻은 수학적 reference 결과로 보고한다.

다음 범위는 여전히 별도다.

- **Native source identity:** 실제 Rust libm·direction·density/σ·preBE tuple가 선언한 reference의 대상에 포함되는지 또는 동일한지 미확인이다.
- **Native root·W·finite I:** 해당 native 물리 family의 실제 값은 `null`이다. 여기의 reference root 증명이 native certificate issuer나 실행 권한을 생성하지 않는다.
- **Two-half full path:** first-half의 실제 joint gas/photon/guard carry를 전달한 second-half는 미실행이다. 표의 first-half와 full을 빼서 full-versus-two-half defect라고 부르지 않는다.
- **연속시간·시간 오차:** 이 정리는 두 고정 \(d\)의 discrete reference에 관한 것이다. 연속시간 오차, time-step remainder, 실제 history trajectory는 계산하지 않았다.
- **모델·closure·fit:** source의 물리 모델이나 원자 fit 정확도에 관한 새 문헌 검증을 수행한 결과가 아니다. 보존된 모델 내부의 계산을 검증했다.

## 9. 실제 실행 기록과 재현 포인터

이 정리가 읽은 분석 실행은 `source_analysis_first` 하나다. `diagnostics/analyze_source_exports.py`는 두 stage의 고정 export를 읽고 rational interval algebra를 수행했다.

| 관측 | 기록 |
|---|---|
| 최초 실행 exit | 0 |
| Assertion | 122개 통과 |
| 경과시간 | 0.16604778199689463 s |
| 최대 RSS | 18,264 KiB |
| 실행 제한 | 30 s, 256 MiB, stdout/stderr 각 8 MiB |
| 새 source callback | 0 |
| 새 초월함수 평가 | 0 |
| Nonlinear point iteration / corner 계산 | 0 |
| Native 호출 / 과거 suite replay | 0 |
| 이 문서 작성 중 과학 재실행 | 0 |

Source-box export를 생산한 이전 PHYS07 최초 실행들과 이 후처리 실행은 별도 기록이다. 이 표의 0을 전체 PHYS07의 새 source reference 계산이 없었다는 뜻으로 사용하지 않는다.

| 파일 | SHA256 |
|---|---|
| `results/SOURCE_ANALYSIS.json` | `d29bcc94b55e2b795520f09412aab4ababb7b7dfe48075c36cb39139526b19c3` |
| `diagnostics/analyze_source_exports.py` | `6c4719bcf4b0b27dcfd615b34ce7b687a9e865100f25d0a701e38b824bc8810c` |
| `evidence/source_analysis_first/stdout.txt` | `879cf14e6519532b2be2ad682ce5374230da9e6288a244ca34293c04dfd75092` |
| `evidence/source_analysis_first/stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `evidence/source_analysis_first/EXECUTION.json` | `0fa9ec8791b7b456b8088a4f295c5cbb7e9860547e3cc123d5168bae381e3f55` |

`EXECUTION.json`은 실제 command, start/end, 원 stdout/stderr, 사용한 source/input의 전후 hash와 변경 없음 확인을 담고 있다. `SOURCE_ANALYSIS.json::stages[*].input_exports`는 각 `family.json`, `source_box.json`, `source_centre.json`, `run_summary.json`의 exact identity를 연결한다.

근 존재·C²·적분 항등식은 **derived**, 위 전제 부등식·Neumann tail·source mixed 포함값은 고정 reference에 대해 **numerically checked / implementation-verified**인 계산 증거다. 최종 claim 승격은 이 문서와 증거를 읽는 별도 독립 판정에 따른다. Native 실제 값과 second-half 및 continuum 항목은 **unresolved**다.
