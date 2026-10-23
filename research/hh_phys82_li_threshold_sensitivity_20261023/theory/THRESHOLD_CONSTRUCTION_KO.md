# PHYS82 R4–R5: Li7 source-gap의 구성적 Maxwell closure

## 0. 이 문서의 결과와 범위

기존 CCC 6–15 eV piecewise-linear(PL) source를 그대로 두고, 그 첫 knot와 chemical threshold 사이만 양의 함수족으로 연결한다. 이 구성은 불완전 감마함수로 닫히며, 양의 scaled moments, logarithmic rate, 반응 가중 입사 에너지, 온도 도함수, 조건부 함수족 envelope와 고정 노출의 관측량 경계를 동시에 준다.

이 문서에서 실제 수행한 일은 R4 후보식 구성과 R5 해석적 유도다. 수치 적분, rate 계산, ODE, 과거 테스트, 과학 코드 실행은 하지 않았다. 수치 도메인·오차 허용치·최종 모델 채택은 parent가 결정한다. 문헌 원전 상태와 새로운 유도 상태를 구별한다.

보호 입력:

| 기호 | 값 또는 정의 | 지위 |
|---|---|---|
| \(I\) | \(5.39172060034581\ {\rm eV}\) | PHYS81에서 교정한 Li7 chemical defect를 재사용 |
| \(E_0\) | \(6\ {\rm eV}\) | 변경하지 않는 첫 CCC incident-energy knot |
| \(\sigma_0\) | \(5.18148\,10^{-17}\ {\rm cm^2}\) | 변경하지 않는 첫 CCC cross-section literal |
| \(b\) | \(15\ {\rm eV}\) | 기존 finite-source 상한 |
| \(\Delta\) | \(E_0-I>0\) | gap 폭 |
| \(\theta\) | \(k_B T\), eV로 표현 | 기존 Maxwell convention |
| \(C\) | \(100\sqrt{8\,{\rm eV_J}/(\pi m_e)}\) | \(\sigma\)가 cm²일 때 K가 cm³/s가 되는 기존 상수 |

입력 근거는 PHYS81의 theory/ATOMIC_DERIVATION_KO.md, source/finite_ci.py, source_data/PHYS81_CI_FINITE_WINDOW_LITERAL_DATA.csv 및 source_data/NEUTRAL_ISOTOPE_PROVENANCE.md다. 초기 source registry에 남아 있는 elemental Li I 값과 교정 후 Li7 chemical defect를 혼동하지 않는다. 전자의 isotope별 source 이동은 도입하지 않는다.

계산 convention은 PHYS81의 stationary-target/electron-mass Maxwell closure를 유지한다. \(I\)를 이 closure의 incident threshold로 쓰며, finite-mass laboratory kinematic threshold와 chemical defect의 정밀 차이는 별도 recoil convention의 대상이다.

## 1. R4: 비교할 네 가지 실제 후보

\[
t=\frac{E-I}{\Delta},\qquad
\sigma_{g;p,q}(E)=
\sigma_0 t^p\left(\frac{E_0}{E}\right)^q,\qquad
I\leq E\leq E_0,
\tag{1}
\]

\[
p>0,\qquad q\in\{0,1\}.
\]

전체 선택 연산자는

\[
\sigma_{p,q}^{\rm fin}(E)=
\begin{cases}
\sigma_{g;p,q}(E),& I\leq E<E_0,\\
\sigma_{\rm PL}(E),&E_0\leq E\leq b,\\
0,&\text{그 밖의 선택 연산자 영역}.
\end{cases}
\tag{2}
\]

구간 밖의 0은 유한 연산자의 정의다. 표본 밖 실제 물리 단면적에 대한 판정은 별도다.

Parent가 제안한 네 모서리는 다음과 같다.

| 이름 | \(p\) | \(q\) | 비교하는 구조 |
|---|---:|---:|---|
| L0 | \(1\) | \(0\) | threshold zero-knot를 추가한 정확한 한 PL cell |
| L1 | \(1\) | \(1\) | 선형 excess numerator와 보존한 \(1/E\) factor |
| W0 | \(p_W\) | \(0\) | Wannier exponent를 gap 전체에 적용한 matching 가설 |
| W1 | \(p_W\) | \(1\) | 같은 exponent와 추가 smooth \(1/E\) factor |

\[
p_W=\frac{\sqrt{91/3}-1}{4}.
\tag{3}
\]

모든 후보는 \(\sigma(I)=0,\ \sigma(E_0)=\sigma_0\)를 만족한다. 첫 knot를 이용한 normalization은 새로운 측정값이 아니라 후보를 지정하는 matching 조건이다. \(E_0\)에서 연속성이 보장되며, 기존 PL cell의 기울기와 일치한다는 조건은 두지 않는다.

\[
\sigma'_{g;p,q}(E_0^-)=
\sigma_0\left(\frac p\Delta-\frac q{E_0}\right).
\tag{4}
\]

기존 source interpolation의 첫 기울기를 정확한 물리 도함수로 간주해 C¹ matching을 강제할 근거는 없다. \(p\geq1,\ 0\leq q\leq1\)에서는 (1)의 E에 대한 기울기도 양수다. 일반 \(p>0\)에서 양성은 유지되지만 q=1의 E-단조성은 별도 조건이다.

## 2. 후보의 물리적 근거와 matching 가정

Wannier 원논문은 neutral atom의 threshold excess에 대한 exponent 약 1.127을 제시한다. 공개 원문 abstract는 ergodicity를 이용한 유도가 엄밀한 증명은 아님을 직접 명시한다. 후속 primary paper Friedrich, Ihra, Meerwald (1999), printed p.323 Eq.(2)는

\[
\nu_W(Z)=\frac14\left[
\sqrt{\frac{100Z-9}{4Z-1}}-1\right]
\tag{5}
\]

을 적는다. 같은 논문의 p.324는 infinitely heavy Coulomb center와 두 outgoing electron을 사용한다. Li에 \(Z=1\)을 대입하는 것은 잔여 Li+의 장거리 순전하를 이용하는 frozen-core/asymptotic 적용이다. \(Z=3\)이라는 nuclear charge 대입과 구별한다. Source 담당 agent가 primary PDF의 web-extracted text를 보존했고, 본 작성자도 sources/WEB_WANNIER_FORMULA_PRIMARY_RAW.json의 Eq.(2)와 p.324 조건을 readback했다. PDF 원본 bytes를 확보했다는 뜻은 아니다. Wannier 공개 abstract와 Peterkop–Tsukerman 원문도 별도로 읽었다. [S1–S3]

Wannier exponent는 \((E-I)\to0^+\)의 형태를 제약한다. 그 법칙만으로 threshold amplitude 또는 \(I<E<6\) eV 전 구간의 오차가 결정되지는 않는다. 식 (1)의 W0/W1은 이 asymptotic 구조를 첫 CCC knot까지 이어 붙인 명시적 가설이다.

Zapesochnyi–Aleksakhin의 primary alkali 실험은 Li의 resolved linear interval과 slope를 보고한다. Source 담당 agent가 확인한 Li table은 linear interval 3.4 eV와 slope \(0.9\,10^{-16}\ {\rm cm^2/eV}\)다. 이 보고에는 absolute normalization 약 ±15%, energy-axis 약 0.1–0.2 eV, electron energy spread가 함께 존재한다. 이들은 isotope chemical \(I\)의 spectroscopic uncertainty와 다른 입력이다. Peterkop–Tsukerman은 alkali의 실제 비선형 구간이 실험 resolution보다 좁을 수 있음을 논한다. 따라서 resolved interval의 선형 경향과 엄밀한 threshold 극한의 exponent를 같은 관측량으로 취급하지 않는다. [S3,S4]

L0와 L1의 threshold slope는 각각

\[
\left.\frac{d\sigma_{\rm L0}}{dE}\right|_{I^+}
=\frac{\sigma_0}{\Delta},
\qquad
\left.\frac{d\sigma_{\rm L1}}{dE}\right|_{I^+}
=\frac{\sigma_0E_0}{I\Delta}.
\tag{6}
\]

반면 \(p_W>1\) 후보의 strict threshold slope는 0이다. 실제 데이터와 비교할 때는 beam convolution과 finite energy interval을 맞춰야 한다.

Bell Eq.(1)의 source threshold를 \(I_B\)로 따로 쓰면

\[
\sigma_B(E)=\frac{
A\log(E/I_B)+\sum_{j\geq1}B_j(1-I_B/E)^j}{I_B E}.
\tag{7}
\]

\(x=E-I_B\to0^+\)에서 직접 전개하면

\[
\sigma_B(I_B+x)
=\frac{A+B_1}{I_B^3}x+O(x^2).
\tag{8}
\]

검토한 Bell Li I literal은 \(A+B_1=(0.0854-0.0040)10^{-13}>0\ {\rm eV^2cm^2}\)여서 이 fit의 leading power는 1이다. q=1은 이러한 smooth \(1/E\) factor를 분리해서 비교하는 후보지만 Bell 전체 식·coefficient를 재현하는 모델은 아니다. Bell의 printed \(I_B=5.39\) eV와 교정 chemical \(I\)는 서로 다른 source 객체다. Bell p.894는 tabular reliability보다 threshold uncertainty가 크다고 명시한다. 따라서 Bell의 Li ±10%를 이번 gap의 pointwise 오차로 이전하지 않는다. [S5]

## 3. Maxwell 적분과 반응 가중 에너지의 정의

온도와 무관한 finite cross section에 대해

\[
M_n(T)=\int E^n\sigma(E)e^{-E/\theta}\,dE,\qquad
K(T)=C\theta^{-3/2}M_1(T),
\tag{9}
\]

\[
\mu(T)=\frac{M_2(T)}{M_1(T)}.
\tag{10}
\]

\(M_n\)의 단위는 \({\rm cm^2\,eV^{n+1}}\), \(K\)는 cm³/s, \(\mu\)는 eV다. 반응 조건부 incident-energy density는

\[
\rho(E;T)=\frac{E\sigma(E)e^{-E/\theta}}{M_1(T)}.
\tag{11}
\]

따라서 \(\mu\)는 단순 Maxwell 전자 평균 \(3\theta/2\)가 아니라 실제 반응 event에 조건을 건 평균이다. Gap과 기존 table을 각각 g와 tab으로 표기하면

\[
K_{\rm fin}=K_{\rm tab}+K_g,\qquad
w=\frac{K_g}{K_{\rm fin}},\qquad
\mu_{\rm fin}=(1-w)\mu_{\rm tab}+w\mu_g.
\tag{12}
\]

Endpoint 한 점의 중복 표기는 적분값을 바꾸지 않는다. 구현에서는 식 (2)의 한쪽 소속을 명시해 source 행 수와 지원 구간의 의미를 유지한다.

## 4. R5: q=0의 불완전 감마함수 유도

\(x=E-I\), \(z=\Delta/\theta\)로 바꾸면

\[
M_{n,g}^{(q=0)}
=\sigma_0\Delta^{-p}e^{-I/\theta}
\sum_{j=0}^{n}{n\choose j}
I^{\,n-j}\theta^{p+j+1}
\gamma(p+j+1,z),
\tag{13}
\]

\[
\gamma(a,z)=\int_0^z u^{a-1}e^{-u}du.
\]

실제로 \((I+x)^n\)을 유한 이항 전개하고 각 항에 \(u=x/\theta\)를 대입한 결과다. \(p>0\)에서 모든 항은 양수다. 필요한 두 moment는

\[
M_{1,g}^{(0)}
=\sigma_0\Delta^{-p}e^{-I/\theta}
\left[
I\theta^{p+1}\gamma(p+1,z)
+\theta^{p+2}\gamma(p+2,z)
\right],
\tag{14}
\]

\[
M_{2,g}^{(0)}
=\sigma_0\Delta^{-p}e^{-I/\theta}
\left[
I^2\theta^{p+1}\gamma(p+1,z)
+2I\theta^{p+2}\gamma(p+2,z)
+\theta^{p+3}\gamma(p+3,z)
\right].
\tag{15}
\]

각 항의 차원이 각각 \(M_1:{\rm cm^2\,eV^2}\), \(M_2:{\rm cm^2\,eV^3}\)로 같다. Cancellation을 만들 signed polynomial coefficient는 필요하지 않다.

## 5. q=1의 flux-factor 상쇄

q=1에서는 Maxwell flux의 E와 cross section의 \(1/E\)가 정확히 상쇄된다.

\[
M_{n,g}^{(q=1)}
=\sigma_0 E_0\Delta^{-p}e^{-I/\theta}
\sum_{j=0}^{n-1}{n-1\choose j}
I^{\,n-1-j}\theta^{p+j+1}
\gamma(p+j+1,z),\quad n\geq1.
\tag{16}
\]

특히

\[
M_{1,g}^{(1)}
=\sigma_0E_0\Delta^{-p}e^{-I/\theta}
\theta^{p+1}\gamma(p+1,z),
\tag{17}
\]

\[
M_{2,g}^{(1)}
=\sigma_0E_0\Delta^{-p}e^{-I/\theta}
\left[I\theta^{p+1}\gamma(p+1,z)
+\theta^{p+2}\gamma(p+2,z)\right].
\tag{18}
\]

이 상쇄는 계산식을 단순화하지만 두 후보를 같은 단면적으로 만들지는 않는다. q=1은 gap 안에서 q=0보다 큰 단면적을 주고, threshold amplitude를 \(E_0/I\)배 바꾼다.

## 6. 양의 scaled moments와 log 평가식

\[
F_j(p,z)=\int_0^1t^{p+j}e^{-zt}dt
=z^{-(p+j+1)}\gamma(p+j+1,z),\qquad j\geq0.
\tag{19}
\]

그러면

\[
\begin{aligned}
M_{1,g}^{(0)}
&=\sigma_0\Delta e^{-I/\theta}(I F_0+\Delta F_1),\\
M_{2,g}^{(0)}
&=\sigma_0\Delta e^{-I/\theta}
(I^2F_0+2I\Delta F_1+\Delta^2F_2),\\
M_{1,g}^{(1)}
&=\sigma_0E_0\Delta e^{-I/\theta}F_0,\\
M_{2,g}^{(1)}
&=\sigma_0E_0\Delta e^{-I/\theta}(I F_0+\Delta F_1).
\end{aligned}
\tag{20}
\]

특히 작은 excess energy를 \(\mu-I\)라는 두 큰 수의 차로 계산할 필요가 없다. \(r_1=F_1/F_0,\ r_2=F_2/F_0\)를 쓰면

\[
\mu_g^{(0)}
=I+\Delta\frac{I r_1+\Delta r_2}{I+\Delta r_1},
\qquad
\mu_g^{(1)}=I+\Delta r_1.
\tag{21}
\]

\[
\begin{aligned}
\log K_g^{(0)}
={}&\log C+\log\sigma_0+\log\Delta-\frac32\log\theta
-\frac I\theta+\log F_0+\log(I+\Delta r_1),\\
\log K_g^{(1)}
={}&\log C+\log\sigma_0+\log\Delta-\frac32\log\theta
-\frac I\theta+\log F_0+\log E_0.
\end{aligned}
\tag{22}
\]

로그는 지정 단위에 대한 수치의 natural log, 예를 들어 \(\log[K/(1\ {\rm cm^3\,s^{-1}})]\)다. 차원 있는 물리량 자체의 로그 convention을 새로 만들지 않는다.

Special-function branch는 \(a=p+j+1\), regularized lower gamma \(P(a,z)\)에 대해

\[
\log F_j=\log\Gamma(a)+\log P(a,z)-a\log z
\tag{23}
\]

로 구현할 수 있다. \(P\)를 0으로 underflow시킨 뒤 로그를 취하면 정보가 사라진다. 작은 z의 보완식은

\[
F_j=e^{-z}\sum_{k=0}^{\infty}
\frac{z^k\Gamma(a)}{\Gamma(a+k+1)}
=\frac{e^{-z}}a
\left[1+\frac z{a+1}
+\frac{z^2}{(a+1)(a+2)}+\cdots\right].
\tag{24}
\]

이것은 \(e^{-zt}=e^{-z}e^{z(1-t)}\)의 전개와 beta 적분에서 얻는 양의 급수다. 항 \(v_0=1/a\), \(v_{k+1}=v_k z/(a+k+1)\)를 쓰면 된다. N번째 항 뒤 \(r=z/(a+N+1)<1\)이면 남은 양의 합은 \(v_N r/(1-r)\) 이하이다. 이 경계는 급수 절단 경계이며, floating-point 오차 인증과는 구별한다. 매우 큰 z에서 급수 전체를 무작정 합하면 중간 overflow가 생길 수 있으므로 log-sum 또는 gamma branch를 택한다.

검산 가능한 엄밀한 moment 성질:

\[
0<F_{j+1}<F_j,\qquad
F_1^2\leq F_0F_2,\qquad
\frac{e^{-z}}{p+j+1}\leq F_j\leq\frac1{p+j+1},
\tag{25}
\]

\[
(p+j+1)F_j-zF_{j+1}=e^{-z}.
\tag{26}
\]

식 (26)은 적분 부품검사에 쓸 수 있지만 작은 z에서 두 비슷한 수를 빼는 forward recurrence는 불안정할 수 있다. 기본 평가식은 (23) 또는 (24)다.

전체 rate는 logaddexp로 합하고, \(w=\exp(\log K_g-\log K_{\rm fin})\)로 조합한다. binary64의 K가 0으로 underflow해도 \(\log K\), \(w\), \(\mu\)가 유효할 수 있다. underflow flag와 물리적 rate 0은 다른 상태다.

## 7. 온도 도함수, 부호, 확률적 해석

모든 모델 parameter와 energy 경계가 T에 무관할 때 적분 미분으로

\[
\frac{dM_1}{dT}
=\frac{M_2}{\theta T},
\qquad
\boxed{\frac{d\log K}{dT}
=\frac1T\left(\frac{\mu}{\theta}-\frac32\right)}.
\tag{27}
\]

따라서 \(dK/dT=K\,d\log K/dT\). K가 underflow하면 이 곱을 곧바로 0으로 만들기보다

\[
\operatorname{sgn}\!\left(\frac{d\log K}{dT}\right)
\exp\!\left[\log K+
\log\left|\frac{d\log K}{dT}\right|\right]
\tag{28}
\]

을 평가하고 도함수 0을 별도 처리할 수 있다. 이 식이 수치 범위 밖이면 계산 상태를 보고해야 한다.

양의 support로부터

\[
I<\mu_g<E_0<\mu_{\rm tab}<b,\qquad
\mu_g<\mu_{\rm fin}<\mu_{\rm tab}.
\tag{29}
\]

따라서 gap 추가는 rate를 늘리며, 같은 T에서 \(d\log K/dT\)를 낮춘다. dK/dT 자체의 순서는 rate와 logarithmic derivative의 곱으로 판정한다.

\[
\frac{I/\theta-3/2}{T}
<\frac{d\log K_{\rm fin}}{dT}
<\frac{b/\theta-3/2}{T}.
\tag{30}
\]

예를 들어 \(\theta<2I/3\)이면 도함수는 양수, \(\theta>2b/3\)이면 음수다. 후자의 감소는 finite upper support를 가진 선택 연산자의 고온 거동이다.

\[
\frac{d\mu}{dT}
=\frac{\operatorname{Var}_\rho(E)}{\theta T}>0
\tag{31}
\]

도 직접 따른다. 이는 moment와 도함수 사이의 추가 검사량이며, 새로운 ODE 또는 물리적 source 오차 검증이 아니다.

## 8. p–q rectangle의 조건부 envelope와 민감도

이 절에서는 envelope를 위해 \(q\in[0,1]\)의 함수족 (1)을 연속적으로 정의한다. 내부 q에 대한 구현을 요구하지 않으며, rate 극값은 모서리만으로 정해진다.

\[
\partial_p\log\sigma_g=\log t\leq0,\qquad
\partial_q\log\sigma_g=\log(E_0/E)\geq0.
\tag{32}
\]

따라서 \(p\in[p_{\min},p_{\max}],\ q\in[q_{\min},q_{\max}]\)이면

\[
\sigma_{g;p_{\max},q_{\min}}
\leq\sigma_{g;p,q}
\leq\sigma_{g;p_{\min},q_{\max}},
\tag{33}
\]

그리고 양의 Maxwell kernel를 적분하여 같은 순서가 K에 전달된다. 지정 rectangle에서는

\[
\boxed{K_{\rm tab}+K_{g;p_W,0}
\leq K_{\rm fin;p,q}
\leq K_{\rm tab}+K_{g;1,1}.}
\tag{34}
\]

이것은 명시한 함수족에 대한 엄밀한 envelope다. 실제 Li 단면적이 그 rectangle 안에 있다는 추가 전제가 없으므로 물리 confidence interval로 표기하지 않는다.

Gap의 반응 조건부 평균을 사용하면

\[
\partial_p\log K_g=\langle\log t\rangle_g<0,\quad
\partial_q\log K_g=\langle\log(E_0/E)\rangle_g>0,
\tag{35}
\]

\[
\partial_p\log K_{\rm fin}
=w\langle\log t\rangle_g,\quad
\partial_q\log K_{\rm fin}
=w\langle\log(E_0/E)\rangle_g.
\tag{36}
\]

같은 p에서 q-factor만 바꾸는 영향에는 T에 무관한 경계가 있다.

\[
1<
\frac{K_{g;p,1}}{K_{g;p,0}}
<\frac{E_0}{I},
\tag{37}
\]

\[
1<
\frac{K_{\rm fin;p,1}}{K_{\rm fin;p,0}}
<1+w_{p,0}\left(\frac{E_0}{I}-1\right).
\tag{38}
\]

Parameter \(p\)에 대한 두 번째 log derivative는 \(\operatorname{Var}_g(\log t)\geq0\)다. 전체 finite operator에서는 table 구간의 score를 0으로 연장한 분산이 된다.

평균 에너지의 순서도 직접 증명할 수 있다. \(\partial_\lambda\mu=\operatorname{Cov}_\rho(E,s_\lambda(E))\)이며, p-score는 gap의 \(\log t\), table의 0으로서 E에 대해 증가한다. q-score는 gap의 \(\log(E_0/E)\), table의 0으로서 감소한다. 두 독립 E 표본에 대한

\[
\operatorname{Cov}(E,s(E))
=\frac12\left\langle
(E-E')[s(E)-s(E')]
\right\rangle
\tag{39}
\]

을 쓰면 p 증가가 \(\mu_{\rm fin}\)을 높이고 q 증가가 낮춤을 알 수 있다. 따라서 rectangle의 mean-energy 순서는 K 순서의 반대다.

단면적 amplitude의 일반적인 조건부 오차도 양의 적분으로 전파된다. Gap 안에서 \(|\delta\sigma|\leq\epsilon\sigma_g\)가 실제로 확보되면

\[
|\delta K_g|\leq\epsilon K_g,\qquad
\frac{|\delta K_{\rm fin}|}{K_{\rm fin}}\leq\epsilon w.
\tag{40}
\]

현재 CCC 첫 knot의 literal은 고정하므로 임의 multiplier를 gap에 붙여 \(\sigma(E_0)=\sigma_0\)를 깨뜨리지 않는다. 장래 endpoint를 고정한 amplitude 탐색이 필요하면

\[
\sigma_{g;p,q,\alpha}
=\sigma_{g;p,q}\,[\alpha+(1-\alpha)t],\qquad\alpha>0,
\tag{41}
\]

가 가능한 구성이다. 이는 \(\sigma(E_0)\)를 보존하면서 strict threshold coefficient만 \(\alpha\)배 한다. \(\alpha\)의 범위가 주어지면 추가 envelope를 만들 수 있으나 이번 네 모델 실행에는 포함하지 않는다.

## 9. 저온 극한: relative enhancement와 절대량의 분리

\(a=p+1,\ z=\Delta/\theta\)라 두고 \(\theta/\Delta\to0\)을 취한다. 상한을 무한대로 확장한 보조 적분에서 \(\gamma(a,z)\to\Gamma(a)\)이므로

\[
K_g^{(0)}
\sim C\sigma_0I\Gamma(p+1)\Delta^{-p}
\theta^{p-1/2}e^{-I/\theta}
\left[1+\frac{(p+1)\theta}{I}\right],
\tag{42}
\]

\[
K_g^{(1)}
\sim C\sigma_0E_0\Gamma(p+1)\Delta^{-p}
\theta^{p-1/2}e^{-I/\theta}.
\tag{43}
\]

여기서 \(\sim\)의 생략항은 finite upper limit의 exponentially small correction이다. q=0의 표시된 선형 bracket과 q=1의 상수 factor는 무한 상한 보조 적분에서 각각 정확하다. 이 보조 적분은 실제 source 상한을 늘리는 조작이 아니다.

q=0에서 그 상대 tail correction은 정확히

\[
\varepsilon_0=
\frac{I\Gamma(a,z)+\theta\Gamma(a+1,z)}
{I\Gamma(a)+\theta\Gamma(a+1)},
\tag{44}
\]

q=1에서는 \(\varepsilon_1=\Gamma(a,z)/\Gamma(a)\)다. 실제 gap rate는 각각 해당 무한상한 보조식에 \(1-\varepsilon_q\)를 곱한 값이다.

\[
\mu_g^{(0)}
\sim I+a\theta\frac{I+(a+1)\theta}{I+a\theta}
=I+a\theta+\frac{a\theta^2}{I+a\theta},
\tag{45}
\]

\[
\mu_g^{(1)}\sim I+a\theta.
\tag{46}
\]

따라서 leading logarithmic derivative는

\[
\frac{d\log K_g}{dT}
\sim\frac1T\left(\frac I\theta+p-\frac12\right).
\tag{47}
\]

q=0에는 \(a\theta/[T(I+a\theta)]\)의 다음 항이 더해진다.

같은 q에서 두 exponent를 비교하면 leading ratio는

\[
\frac{K_{g;p,q}}{K_{g;r,q}}
\sim
\frac{\Gamma(p+1)}{\Gamma(r+1)}
\left(\frac{\theta}{\Delta}\right)^{p-r}.
\tag{48}
\]

q=0의 다음 correction은 \([I+(p+1)\theta]/[I+(r+1)\theta]\)다. 저온의 exponent 민감도는

\[
\partial_p\log K_g
=\log(\theta/\Delta)+\psi(p+1)+o(1).
\tag{49}
\]

반면 q-factor의 효과는 식 (37)처럼 유한하다. 따라서 q는 smooth-amplitude 차이, p는 threshold power 차이를 분리하는 판별량이다.

기존 table은 \(E_0\)에서 \(\sigma_0>0\)으로 시작한다. 첫 cell의 PL slope가 유한하므로

\[
K_{\rm tab}\sim C E_0\sigma_0
\theta^{-1/2}e^{-E_0/\theta},
\qquad
\mu_{\rm tab}\sim E_0+\theta.
\tag{50}
\]

그러므로

\[
\frac{K_{g;p,q}}{K_{\rm tab}}
\sim
\Gamma(p+1)
\left(\frac I{E_0}\right)^{1-q}
\left(\frac{\theta}{\Delta}\right)^p
e^{\Delta/\theta}\longrightarrow\infty.
\tag{51}
\]

각 rate 자체는 0으로 간다. 큰 enhancement는 source가 시작되는 exponential scale을 \(E_0\)에서 I로 바꾸었기 때문에 생긴다. Gap/total fraction \(w\to1\)과 gap/table enhancement \(\to\infty\)를 다른 지표로 기록해야 한다.

함수족의 upper/lower ratio도

\[
\frac{K_{g;1,1}}{K_{g;p_W,0}}
\sim
\frac{E_0/I}{\Gamma(p_W+1)}
\left(\frac{\Delta}{\theta}\right)^{p_W-1}
\tag{52}
\]

로 커질 수 있지만, 양쪽 rate의 절대값은 모두 \(e^{-I/\theta}\)로 작아진다.

## 10. 고온·parameter 극한의 자체 검산

\(z\to0\)에서 \(F_j\to1/(p+j+1)\). 따라서

\[
K_g^{(0)}\sim
C\sigma_0\Delta
\left[\frac I{p+1}+\frac{\Delta}{p+2}\right]\theta^{-3/2},
\tag{53}
\]

\[
K_g^{(1)}\sim
\frac{C\sigma_0E_0\Delta}{p+1}\theta^{-3/2}.
\tag{54}
\]

유한 support의 고온 rate는 \(\theta^{-3/2}\)이다. q=1의 high-T mean은

\[
\mu_{g,\infty}^{(1)}
=I+\Delta\frac{p+1}{p+2},
\tag{55}
\]

q=0에서는 식 (20)에 \(F_j=1/(p+j+1)\)를 넣은 양의 비가 된다.

\(p\to0^+\)에서 적분은 유한한 limit을 가지나 pointwise limiting cross section은 threshold의 연속 onset을 잃는다. \(p\to\infty\)에서는 각 \(I<E<E_0\)의 gap cross section이 0으로 가고 \(K_g\to0,\ \mu_g\to E_0\)다. 선택된 \(p\in[1,p_W]\)의 검증으로 이 극단 parameter 영역까지 floating-point 지원을 주장하지 않는다.

## 11. 고정 exposure에서 관측량 경계

외부에서 일정한 T와 electron density \(n_e\)를 주고 시간 \(\tau\) 동안 한 neutral의 이온화 확률을 관측한다. \(\Lambda=n_e\tau\)의 단위는 cm⁻³ s다.

\[
P(K;\Lambda)=1-e^{-\Lambda K}.
\tag{56}
\]

Gap 없는 원래 연산자와 gap을 더한 연산자의 차이는 정확히

\[
\Delta P
=e^{-\Lambda K_{\rm tab}}
\left(1-e^{-\Lambda K_g}\right),
\tag{57}
\]

\[
0\leq\Delta P
\leq e^{-\Lambda K_{\rm tab}}\min(1,\Lambda K_g)
\leq\min(1,\Lambda K_g).
\tag{58}
\]

이는 \(1-e^{-x}\leq\min(1,x)\), \(x\geq0\)에서 바로 나온다. 수치적으로는 작은 \(\Lambda K\)에서 -expm1을 쓴다.

같은 식은 두 ordered 후보 \(K_+\geq K_-\)에 대해 \(\delta K=K_+-K_-\)로 적용된다. 따라서 envelope (34)는 P에도 전달된다. \(\Lambda\)가 유한하게 고정되어 있으면 \(\theta\to0\)에서 \(\Delta P\to0\)이다. 식 (51)의 큰 relative enhancement만으로 유의한 절대 이온화량을 결론 내릴 수 없는 이유를 이 bound가 직접 표현한다.

동일하게 외부에서 정한 \(T(t),n_e(t)\)라면 hazard \(H=\int n_e(t)K(T(t))dt\)와 \(\Delta H\)를 써서 같은 증명이 된다. 하지만 rate를 바꾸면 T와 \(x_e\)가 함께 변하는 coupled parcel에서는 두 해가 같은 histories를 지나지 않는다. 그 경우 (58)은 coupled trajectory의 오차 경계가 아니며, 변한 vector field에 대한 별도 비교·안정성 분석이나 허용된 직접 적분이 필요하다. 이 문서는 그 추가 계산을 수행하지 않는다.

## 12. Reaction bias와 chemical thermal sink의 분리

Event energy balance를 shared thermal pool에 대해 쓴다. 반응 전에 들어온 electron kinetic energy는 E이고, 반응 뒤 ion의 internal energy는 I만큼 증가한다. 두 outgoing electron과 recoil의 kinetic energy가 전부 같은 pool에 남으면, 그 합은 \(E-I\)다.

\[
E=\underbrace{I}_{\text{chemical storage}}
+\underbrace{E_{\rm out,kin}}_{\text{thermal pool에 잔류}},
\qquad
E_{\rm out,kin}=E-I.
\tag{59}
\]

반응 ensemble에 평균을 취하면

\[
\langle E\rangle_{\rm events}=\mu,\qquad
\langle E_{\rm out,kin}\rangle_{\rm events}=\mu-I,
\tag{60}
\]

\[
\Delta u_{\rm thermal,event}
=-\mu+(\mu-I)=-I.
\tag{61}
\]

따라서 \(\mu\)나 \(\mu-I\)를 chemical loss에 추가하면 outgoing kinetic energy를 잘못 제거한다. \(\mu\)의 역할은 반응 bias, rate 온도 미분, 비열적 분포 또는 일부 입자 escape를 따로 모델링할 때의 진단이다.

CI event는 neutral −1, ion +1, free electron +1이다. 최종 thermal particle 수가 하나 증가하므로, same-pool 이상기체 EOS에서

\[
u_{\rm th}=\frac32 k_BT N_g,\qquad
du_{\rm th}=-I\,dX,\qquad dN_g=dX
\]

를 미분하면

\[
\frac{dT}{dX}
=-\frac{I+\frac32 k_BT}{\frac32 k_B N_g}.
\tag{62}
\]

두 항은 chemical sink와 particle-number 증가에 따른 온도 dilution이다. PHYS81의 hazard Jacobian map과 같은 구조이며, threshold rate family를 바꾸어도 event energy bookkeeping 자체는 바뀌지 않는다. Separate electron/ion temperatures, photon escape, excitation loss 또는 입자 escape를 도입하면 새로운 에너지 closure가 필요하다.

## 13. 구현 인계: 실제 오류를 구별하는 최소 검사

아래는 실행 결과가 아니라 parent의 R7/C 단계에 전달하는 판별식이다.

| 검사 | 비교 대상 | 검출하는 구체적 오류 |
|---|---|---|
| gamma 대 transformed quadrature | (22)와 아래 (63)–(64)의 별도 적분 | gamma normalization, \(\theta\) power, q-factor 오류 |
| 정확 p=1,q=0 PL identity | 새 knot \((I,0)\) 추가된 기존 FiniteWindowCI와 gap+원 table | source join, endpoint weight, gamma index 오류 |
| q=1 상쇄 | (17)와 직접 \(E\sigma\) 적분 | q=0 branch를 실수로 재사용하는 오류 |
| first-knot identity | 모든 후보의 \(\sigma(E_0)=\sigma_0\) | normalization 또는 source mutation |
| positivity·mean bounds | (25), (29), (34), (37) | 음수 moment, 잘못된 가중 합, rectangle 순서 오류 |
| 도함수 | (27)과 \(\log K\)의 독립 symmetric difference | 에너지 moment index, T/eV/K 혼동 |
| 저온 ratio | (42)–(51), 엄밀 tail correction (44) | 잘못된 reference exponential 또는 underflow 판단 |
| 고온 scaled limit | \(K\theta^{3/2}\)와 (53)–(54) | prefactor power·finite-support 처리 오류 |
| 노출 확률 | (57)와 (58), 작은 hazard의 -expm1 | rate 비율과 절대 관측량 혼동 |

독립 적분 좌표로 \(u=t^{p+1}\), \(t=u^{1/(p+1)}\), \(E(u)=I+\Delta u^{1/(p+1)}\)를 쓰면 \(t^pdt=du/(p+1)\)이므로

\[
\frac{M_{1,g}}{\sigma_0\Delta e^{-I/\theta}}
=\frac1{p+1}
\int_0^1E(u)\left[\frac{E_0}{E(u)}\right]^q
e^{-z\,u^{1/(p+1)}}du,
\tag{63}
\]

\[
\mu_g-I=
\Delta\,
\frac{\int_0^1u^{1/(p+1)}E(u)
[E_0/E(u)]^q e^{-z\,u^{1/(p+1)}}du}
{\int_0^1E(u)
[E_0/E(u)]^q e^{-z\,u^{1/(p+1)}}du}.
\tag{64}
\]

이 quadrature는 incomplete gamma library를 호출하지 않고, 같은 순간값의 양의 정규화된 integral을 계산한다. Production과 reference의 변수 변환·수치 알고리즘이 분리된다. Root가 선택한 finite T-domain 안에서 계산 비용과 목적에 맞는 별도 error estimate를 사용한다.

p=1,q=0에서는 \(F_0=J_1,\ F_1=J_2,\ F_2=J_3\), \(J_j=\int_0^1t^je^{-zt}dt\)다. 따라서 기존 positive right-endpoint cell의 \(I J_1+\Delta J_2\), \(I^2J_1+2I\Delta J_2+\Delta^2J_3\)와 (20)이 항별로 동일하다. 이것이 원래 PL 구현과 연결하는 exact identity다. p=1,q=1의 \(\sigma\)는 rational function이므로 같은 PL identity를 주장하지 않는다.

구체적인 수치 실패 모드는 다음과 같다.

- \(e^{-I/\theta}\)를 먼저 계산해 0으로 만든 뒤 mean과 derivative를 잃는 경우: common exponential을 제거한 moments와 logK를 유지한다.
- P(a,z)의 underflow, \(\theta^{p+1}\) 또는 \(z^{p+1}\)의 중간 overflow: (22)–(24)의 logarithmic/scaled form으로 바꾼다.
- 작은 z에서 lower-gamma recurrence의 소거: positive series 또는 독립 special-function branch를 쓴다.
- q=1에서 \(E_0\) normalization을 빠뜨리는 경우: first-knot와 (17)을 검사한다.
- 매우 작은 excess를 \(\mu-I\)로 계산하는 소거: (21) 또는 (64)를 쓴다.
- derivative가 0에 가까울 때 상대오차만 비교하는 경우: 절대 또는 물리적 scale 기반 기준을 미리 정한다.
- p 또는 q를 T에 따라 바꾸면서 (27)만 쓰는 경우: 고정 parameter 계약을 지키거나 parameter 미분 항을 추가한다.
- \(\log K\), gap/table ratio, probability를 float64 K 자체로부터 복구하는 경우: 각 log 표현과 -expm1을 먼저 쓴다.
- source closure의 모델 오차와 gamma numerical error를 같은 error bar로 쓰는 경우: 관측량과 전제를 각각 기록한다.

## 14. 근거·상태와 다음 작업

**직접 유도 완료:** positive gamma moments, q=1 cancellation, log formula, reaction-weighted mean과 derivative, p–q conditional envelope, parameter sensitivity, 저온·고온 limit, 고정 prescribed-exposure bound, same-pool chemical sink.

**문헌에 근거한 후보:** neutral residual-charge Wannier exponent, resolved linear finite-range 실험 경향, Bell analytic linear leading term. 실제 Li gap의 shape 및 amplitude 오차와 full physical Maxwell rate 오차는 이들만으로 수치 경계가 생기지 않는다.

**이 worker의 실행 상태:** 과학 수치 실행 0; ODE 0; 과거 suite 실행 0; source 데이터 수정 0; remote mutation 0. 독립 검토는 이후 parent가 다른 context에 맡긴다. 이 문서의 self-check는 구성자 자신의 해석적 차원·부호·극한 검사다.

**적용 skill context:** PhysMath Research Loop 1.3.0의 SKILL.md, STAGE_SELECTION.md, references/POLICY_INTEGRATION.md, THEORY_LOOP.md의 R4/R5 definition, SUBAGENT_MODE.md를 실제 읽었다. 한 번의 bounded 구성 pass로 수행했고 recursive delegation은 하지 않았다. 다른 stage의 완료를 이 문서로 선언하지 않는다.

**다음 실행:** parent가 선택한 4개 corner와 온도 도메인에 대해 새 변경분만 검사한다. (63)–(64)의 독립 적분과 p=1 PL identity를 주된 두 판별 경로로 삼는다. 원 source와 별개인 closure status를 결과에 보존한다.

## Primary source pointers

- [S1] G. H. Wannier, “The Threshold Law for Single Ionization of Atoms or Ions by Electrons,” Physical Review 90, 817 (1953), [DOI 10.1103/PhysRev.90.817](https://doi.org/10.1103/PhysRev.90.817). 공개 abstract 실제 확인: [APS](https://journals.aps.org/pr/abstract/10.1103/PhysRev.90.817). Fulltext를 읽었다고 주장하지 않는다.
- [S2] H. Friedrich, W. Ihra, P. Meerwald, “Threshold Behaviour of (e, 2e) Reactions in Classical and Quantum Mechanics,” Australian Journal of Physics 52, 323–339 (1999), [DOI 10.1071/PH98091](https://doi.org/10.1071/PH98091), [primary PDF](https://www.publish.csiro.au/ph/pdf/PH98091), Eq.(2), printed pp.323–325. Source 담당 agent가 보존한 primary web-extracted text의 exact exponent와 infinitely heavy center 조건을 본 worker도 직접 readback했다. 본 worker의 direct web fetch는 redirect 오류였으며 original PDF bytes를 확보했다고 주장하지 않는다.
- [S3] R. K. Peterkop, P. B. Tsukerman, “Threshold Behavior of the Cross Section for the Ionization of Atoms by Electrons,” Soviet Physics JETP 31, 374–377 (1970), [primary PDF](https://jetp.ras.ru/cgi-bin/dn/e_031_02_0374.pdf), 특히 printed pp.375–376. 본 worker가 원문을 직접 읽었다.
- [S4] I. P. Zapesochnyi, I. S. Aleksakhin, Soviet Physics JETP 28, 41–45 (1969), [primary PDF](https://jetp.ras.ru/cgi-bin/dn/e_028_01_0041.pdf). Table와 실험 precision은 source 담당 agent가 실제 원문·기존 extraction에서 확인. 본 worker의 PDF direct fetch는 timeout이었다.
- [S5] K. L. Bell et al., “Recommended Data on the Electron Impact Ionization of Light Atoms and Ions,” JPCRD 12, 891 (1983), [DOI 10.1063/1.555700](https://doi.org/10.1063/1.555700), [NIST primary PDF](https://srd.nist.gov/jpcrdreprint/1.555700.pdf), Eq.(1)/Table 5 printed p.910; threshold uncertainty printed p.894. 본 worker는 primary text와 보존된 PHYS81 visual transcript를 읽었다.
