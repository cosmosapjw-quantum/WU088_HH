# PHYS07 — 소스의 C² 영역과 HH–광이온화 혼합 메커니즘

2026-10-11. 후보 생성자가 작성한 직접 유도 문서다. 최종 채택 범위는 별도 독립 판정에 따른다. 이 문서는 수치 실행 로그를 대신하지 않는다.

## 1. 무엇의 매끄러움과 포함을 주장하는가

이번 대상은 NCP PHYS06 implementation core
`927019cff541e8a4a1f0d2c8846f1466d6b70533`, 전달 head
`65a36e255aa6d9911e23a9b5ced18d8a9f507606`의 고정 소스다.
`SOURCE_INTAKE_MANIFEST.json`은 해당 head/tree와 각 파일의 byte identity를 연결한다.
이 문서의 `candidate/src/...`, `src/...`는 그 NCP dossier 내부 경로다.

다음 세 대상을 구별한다.

1. **Source-derived exact-real family:** source의 binary64 상수를 명시된 실수 상수로 올리고, 고정 에너지·밀도 leaf 및 지정된 transport chart에서 같은 반응식을 실수 연산으로 읽은 함수다. C², Hessian, 매개변수 미분은 이 함수에 대한 진술이다.
2. **Outward interval evaluation:** 위 함수의 값·미분을 실제로 포함하는 계산이다. 실행 성공 외에 elementary function remainder, leaf map, 정의역 및 전체 입력 영역의 포함이 필요하다.
3. **Native 반환·인증:** native point 코드의 반올림, 방향별 leaf, preBE tuple, 내부 solver와 실제 반환 상태다. 위 두 대상만으로 native 실행·실제 root/tube·실제 혼합응답이 확인되지는 않는다.

Root가 계산하는 PHYS07 transport는 **isotropic analytic transport reference family**다. COMMON seed의 고정 `h_i=10^-14 s^-1`에서 정확한 실수 비율은 `r=exp(-H d)`이고, 방향 정규화의 합은 1이다. Native `qhat`, `g_point`, `source_weights`, `widened`와 그 결과 tuple의 bitwise 동일성은 별도 OPEN이다. 이 구분은 기존 모델이나 closure를 교체하는 허가가 아니다.

물리 좌표는

\[
g=(x,y_1,y_2,w),\qquad
x=x_{\rm HII},\quad y_1=x_{\rm HeII},\quad y_2=x_{\rm HeIII},
\]

이며 `w`의 단위는 eV/H, 시간은 proper s, 핵 밀도는 cm⁻³다. `c`, `k_B`, eV–erg 변환을 유지한다. Metric convention은 \((-+++ )\)이지만 이번 국소 반응 계산에는 새 metric 미분을 사용하지 않는다.

연구 매개변수 \(\theta=(\lambda,b)\in\Theta=[0,1]^2\)는 각각 미래 HH 강도와 미래 광원 강도다. NCP `FamilyIdentity.theta_bits:[u64;3]`는 **Hubble triplet**이며 이 두 매개변수와 다른 필드다. 기존 COMMON 상태의 HH ON 이력은 \(\lambda=0\)에서 지워지지 않는다.

## 2. 실제 소스의 정의역과 분기

| 소스 | 실제 제약 또는 구조 | C² 주장에 주는 의미 |
|---|---|---|
| `candidate/src/ft03_interval.rs::ft03_interval_rhs` | 7개 입력의 lower endpoint가 양수, \(x_{hi}<1\), \(y_{1,hi}+y_{2,hi}<1\), \(30000\le T\le110000\) K | 현재 reduced callback은 마지막 3개 dummy photon을 1로 놓고 sigma를 0으로 만든다. 이 positivity guard는 물리 incoming photon이 0일 때의 미분을 금지하지 않는다. |
| `candidate/src/hh_primary_extension.rs::hh_rate_jet` | 닫힌 H/He simplex, \(w_{lo}>0\), \(35000\le T\le60000\) K | FT03와 결합하면 더 엄격한 FT03 simplex와 더 좁은 HH 온도 영역을 모두 만족해야 한다. |
| `candidate/src/phys04_mixed.rs::phys04_reduced_residual` | \(d>0\), \(\lambda\in[0,1]\), incoming \(N_j\ge0\), 모든 \(D_j>0\) | \(\lambda=0\)이어도 HH jet을 먼저 평가하므로 HH 온도 guard는 사라지지 않는다. |
| `candidate/src/coupled_primary.rs::model` | finite \(n_H>0,f>0,H\ge0\), stored \(n_{He}=\operatorname{fl}(n_Hf)>0\) | \(n_{He}/n_H\)를 \(f\)와 동일하다고 치환하면 안 된다. |
| `candidate/src/paired_runtime.rs::temp_box` | \(f\)를 \([FHE(1-8\epsilon),FHE(1+8\epsilon)]\)로 감싸고 모든 thermal product를 interval로 평가 | paired guard는 `FHE` 한 점만 사용하는 것이 아니다. 고정 stage의 정확한 밀도비가 이 source blanket 안에 드는지도 확인한다. |
| `candidate/src/atomic_provider.rs::cross_section` | fixed \(E_j\), Verner cutoff 13.60, 24.59, 54.42 eV; \(E\le50000\) eV | \(E_j\)가 \((g,\lambda,b)\)에 독립인 leaf이면 cutoff를 포함하는 노드도 이 변수들에 대해서는 상수다. 에너지를 변수로 삼는 새 문제에는 이 결론을 전용할 수 없다. |
| `candidate/src/phys04_transport.rs::phys04_prepare_family` | 고정 33개 노드, 128개 방향; guard/hat interval crossing 검사; 0 stock의 signed jet 보존 | transport coefficient가 \((\lambda,b)\)에 상수인 현재 chart에서는 hat knot 자체가 이 매개변수의 비매끄러움을 뜻하지 않는다. interval branch 검사는 별도로 충족해야 한다. |
| `src/uniform.rs::Domain::require` | whole coverage, strict simplex, positive denominator, 35–60 kK, conditional C² premise | 문자열·boolean은 증명을 생성하지 않는다. `x[3]`은 실제 gas thermal coordinate라는 현재 API 의미도 보존해야 한다. |

`exp`, `powf`, division 자체는 아래 양의 정의역에서 매끄럽다. FT03 rate의 `a==1` 분기는 고정 species index이며 온도에 따른 분기가 아니다. HH의 \((1-x)^2\)에는 neutral fraction이나 electron density로 나누는 연산이 없으므로 \(x=1\)에서 생기는 물리적 소멸은 수학적 특이점이 아니다. 다만 현재 전체 FT03 callback은 그 경계를 입력으로 받아들이지 않는다.

실제 native endpoint의 point iteration, 반환 여부, tolerance gate, packet compaction, underflow rejection을 합친 프로그램을 \(\mathbb R^n\to\mathbb R^n\)의 C² 함수라고 주장하지 않는다. 미분 대상은 지정된 source-real residual이고, native 반환과의 연결은 따로 필요하다.

## 3. 온도와 밀도비: 정확한 상자 극값과 미분

Stage에 저장된 상수를 다음과 같이 둔다.

\[
f=\operatorname{exact}(\texttt{stage.f\_he}),\qquad
\widehat f=\frac{\operatorname{exact}(n_{He}^{\rm stored})}
                   {\operatorname{exact}(n_H^{\rm stored})},\qquad
\mathcal C=\frac{2\epsilon_{\rm eV}}{3k_B}.
\tag{1}
\]

\(\epsilon_{\rm eV}\)는 고정 erg/eV 변환 leaf이고 \(k_B\)의 단위는 erg/K다. Source의 scaled 단위에서 \(\mathcal C\)는 \(w\)를 입자/H로 나눈 값을 K로 변환한다. `nHe`는 원 곱셈의 저장 결과이며, \(\widehat f\)를 정의할 때 새 정확실수 곱으로 재계산하지 않는다.

Thermal source는 다음 식을 사용한다.

\[
p(g)=1+\widehat f+x+\widehat f(y_1+2y_2),\qquad
n_e=n_H[x+\widehat f(y_1+2y_2)],\qquad
T(g)=\mathcal C\frac{w}{p(g)}.
\tag{2}
\]

물리 simplex 안에서 \(g_i\in[g_i^-,g_i^+]\)라 하면 \(p\)는 세 이온 분율 모두에 증가하고 \(w\)에 독립이다. 따라서 정확실수 극값은 다음과 같다.

\[
\begin{aligned}
p_-&=1+\widehat f+x_-+\widehat f(y_{1,-}+2y_{2,-}),\\
p_+&=1+\widehat f+x_++\widehat f(y_{1,+}+2y_{2,+}),\\
T_-&=\mathcal C w_-/p_+,\qquad
T_+=\mathcal C w_+/p_- .
\end{aligned}
\tag{3}
\]

이는 gas rectangle의 실제 corner에서 달성되는 극값으로, sampling 추론을 사용하지 않는다. 양의 density-ratio interval이 주어지면 같은 단조성에 따라 그 상한을 \(p_+\)에, 하한을 \(p_-\)에 사용한다. Native outward 구현은 이보다 조금 넓은 결과를 반환할 수 있다.

\(a=(1,\widehat f,2\widehat f,0)\), \(v=(0,0,0,1)\)라 두면 source port에 필요한 미분은 다음과 같다.

\[
T_i=\mathcal C\left(\frac{v_i}{p}-\frac{wa_i}{p^2}\right),\qquad
T_{ij}=\mathcal C\left[-\frac{v_i a_j+v_j a_i}{p^2}
                       +\frac{2wa_i a_j}{p^3}\right].
\tag{4}
\]

임의의 scalar rate \(R(T)\)의 gas 미분은 다음 chain rule로 얻는다.

\[
\partial_iR=R'T_i,\qquad
\partial_{ij}R=R''T_iT_j+R'T_{ij}.
\tag{5}
\]

이 식은 고정 stage leaves를 사용한다. 시간이나 Hubble 미분에서는 밀도 및 leaf 생성 경로를 추가로 미분해야 하며, 그것은 현재 \((\lambda,b)\) chart 밖의 작업이다.

### Energy coordinate의 상관관계

PHYS06의 에너지 좌표는

\[
e=w+\beta\cdot z,\quad z=(x,y_1,y_2),\quad
\beta=(\chi_H,f\chi_I,f(\chi_I+\chi_{II})).
\tag{6}
\]

여기에는 stage의 \(f\)가 들어가고, 온도의 \(p\)에는 저장 밀도비 \(\widehat f\)가 들어간다. Energy rectangle \(Y\)에서는

\[
w=e-\beta\cdot z,\qquad
T(Y)=\mathcal C\frac{e-\beta\cdot z}{1+\widehat f+x+\widehat f(y_1+2y_2)}.
\tag{7}
\]

\(w>0\)와 \(\beta_i>0\)이면 \(T\)는 \(e\)에 증가하고 각 \(z_i\)에 감소한다. 따라서 같은 corner를 공유하는 exact extrema는

\[
T_-^Y=\mathcal C\frac{e_- -\beta\cdot z_+}{p(z_+)},\qquad
T_+^Y=\mathcal C\frac{e_+ -\beta\cdot z_-}{p(z_-)}.
\tag{8}
\]

식 (4)의 \(v\)를 \((-\beta_1,-\beta_2,-\beta_3,1)\)로 바꾸면 energy-coordinate gradient와 Hessian도 얻는다.

Gas rectangle의 선형상 \(S(X_g)\)는 일반적으로 직사각형이 아니라 평행체다. 그 집합에서 \(w\in[13,14]\)라는 제약을 보존하면 식 (3)의 온도 범위를 그대로 사용한다. `hull(S(X_g))`를 새 energy rectangle로 취하면 원래 없던 조합이 들어오므로 식 (8)로 새 영역을 검사해야 한다. 반대로 `Domain.x[3]`에 \(e\)를 직접 넣고 이를 thermal \(w\)로 검사하면 다른 정의역을 검사하게 된다. 현재 gas-domain adapter는 gas pullback과 coordinate tag를 명시한 뒤 사용해야 한다.

## 4. 보관 상태를 포함하는 구체적 물리 영역

보관 COMMON 상태는 아래 exact binary64 값이다. 새 endpoint 관측이 아니다.

\[
g_0=(0.9131385026926517,\ 0.300035085528747,\
     0.5999927594007611,\ 13.565646600651332).
\tag{9}
\]

PHYS07의 주 후보는

\[
\boxed{X_g=[0.90,0.93]\times[0.29,0.31]\times[0.59,0.61]
                 \times[13,14]\ {\rm eV/H\ in\ the\ last\ coordinate}.}
\tag{10}
\]

표기의 십진 끝점은 이론에서 정확한 유리수다. 실제 입력 artifact가 binary64 끝점을 고정한다면 그 두 실수를 사용한 식 (3)을 다시 평가한다. 동일한 십진 출력만으로 exact decimal과 binary64를 동일시하지 않는다. Root의 최종 input manifest가 계산에 사용한 endpoint convention을 지정한다.

이 후보의 명시적 물리 여유는 다음과 같다.

| 경계 | 식 (10)의 여유 |
|---|---:|
| \(x>0\) | 0.90 |
| neutral H, \(1-x>0\) | 0.07 |
| \(y_1>0\) | 0.29 |
| \(y_2>0\) | 0.59 |
| neutral He, \(1-y_1-y_2>0\) | 0.08 |
| \(w>0\) | 13 eV/H |

입자수와 온도의 극값은 source leaf의 유리수 계산으로 환원된다.

\[
p_-=1.90+2.47\widehat f,\qquad
p_+=1.93+2.53\widehat f,
\]

\[
T_-=\frac{26\epsilon_{\rm eV}}{3k_B(1.93+2.53\widehat f)},\qquad
T_+=\frac{28\epsilon_{\rm eV}}{3k_B(1.90+2.47\widehat f)}.
\tag{11}
\]

각 fixed stage에서

\[
m_T=\min(T_--35000,60000-T_+)>0
\tag{12}
\]

를 직접 평가한다. 보관 \(t_0\), first-half \(t_0+d/2\), full \(t_0+d\)의 density leaves는 서로 다른 고정 입력이다. PHYS06의 이전 점 진단은 approximately 49.489 kK였으나, 이번 전체 상자의 수치적 여유는 PHYS07의 새 계산 기록을 사용해야 한다.

Open-neighborhood witness로는 예를 들어

\[
U_g=(0.899,0.931)\times(0.289,0.311)\times(0.589,0.611)
      \times(12.9,14.1)
\tag{13}
\]

을 사용할 수 있다. 그 closure에 식 (3), simplex margin 및 \(D_j>0\) 검사를 적용해 양의 여유를 얻으면 \(X_g\Subset U_g\)가 된다. 이는 root가 그 상자 안에 있다는 증명이 아니라, **그 상자에서 source가 정의되고 매끄럽다는 증명**이다.

정밀 온도 계산과 별도로 다음 넓은 여유의 유리수 witness를 사용할 수 있다. 고정 leaf에서 \(0.082\le\widehat f\le0.084\), \(7700<\mathcal C<7800\)가 확인되면 식 (13)의 closure 전체에서 \(2.10<p<2.15\)다. 따라서

\[
T>7700\frac{12.9}{2.15}=46200\ {\rm K},\qquad
T<7800\frac{14.1}{2.10}<52372\ {\rm K}.
\tag{13a}
\]

이 두 coarse leaf 조건은 같은 input의 정확 산술로 확인할 수 있고, 별도의 whole-source callback 실행이 필요하지 않다. 정밀 margin과 식 (13a)의 보수적 margin을 같은 수치로 보고하지 않는다.

\(\lambda\)는 residual에 affine으로, incoming \(N_j\)는 reduced photon quotient의 numerator에 선형으로 들어간다. 따라서 \(\Theta\)의 바깥으로 작은 열린 구간을 두어 동일 real formula를 연장할 수 있다. 예를 들어 \((-\eta,1+\eta)^2\)에서 일부 \(N_j\)가 음수가 되어도 \(D_j>0\)이면 식의 매끄러움은 유지된다. 이 연장은 경계점에서 C²를 정의하는 수학적 장치이며, 물리적 음의 photon을 허용하거나 native guard를 우회하는 실행 절차가 아니다. 물리적 포함·positivity는 여전히 \(X_g\times[0,1]^2\)에서만 주장한다.

## 5. Opacity와 reduced photo source의 전체 영역 포함

Fixed stage와 고정 단면적 leaf에서

\[
\kappa_j=c n_H\{\sigma_{Hj}(1-x)
        +f\sigma_{Ij}(1-y_1-y_2)+f\sigma_{IIj}y_1\}
       =\kappa_{0j}+a_j\cdot g,
\tag{14}
\]

\[
\kappa_{0j}=c n_H(\sigma_{Hj}+f\sigma_{Ij}),\quad
a_j=c n_H(-\sigma_{Hj},f(\sigma_{IIj}-\sigma_{Ij}),-f\sigma_{Ij},0).
\]

각 \(a_{ji}\)의 부호에 따라 선택한 상자 corner가 exact affine 최솟값·최댓값을 준다.

\[
\kappa_j^- =\kappa_{0j}+\sum_i\min(a_{ji}g_i^-,a_{ji}g_i^+),\quad
\kappa_j^+ =\kappa_{0j}+\sum_i\max(a_{ji}g_i^-,a_{ji}g_i^+).
\tag{15}
\]

HeI와 HeII의 lower populations를 독립적으로 최대화해 더하는 대신 이 affine extrema를 쓰면, 동일 \(y_1\)의 상관관계를 보존한다. 전체 닫힌 H/He simplex에서도

\[
0\le\kappa_j\le c n_H\{\sigma_{Hj}+f\max(\sigma_{Ij},\sigma_{IIj})\}
\tag{16}
\]

가 성립한다. He 세 분율의 합이 1이라는 조건이 이 상계를 준다.

\(d\ge0\)이면

\[
D_j=1+d\kappa_j\ge1.
\tag{17}
\]

따라서 photo elimination은 neutral abundance가 0인 경계에서도 특이하지 않다. 작은 양의 \(D_j\)를 실험적으로 추정해야만 얻는 결론이 아니다. 단, 물리 simplex 밖으로 과도하게 확장한 상자에는 식 (16)을 사용할 수 없으므로 식 (15)로 다시 검사한다.

Source photo column \(K_j(g)\)는 gas에 affine이다. 열 행은 source의 미리 반올림된 excess leaf를 그대로 쓰며, PHYS06에서 밝혀진 \(\Psi\) 보정과 직접 \(\ell G\) projection을 보존한다. \(k_j=K_j/D_j\)에 대해

\[
\begin{aligned}
k_{j,i}&=K_{j,i}/D_j-dK_j a_{ji}/D_j^2,\\
k_{j,il}&=-d(K_{j,i}a_{jl}+K_{j,l}a_{ji})/D_j^2
           +2d^2K_j a_{ji}a_{jl}/D_j^3.
\end{aligned}
\tag{18}
\]

이 식과 affine extrema는 whole box에서 계산 가능하다. \(\sigma\)의 고정 leaf를 native Rust provider로부터 받지 않았다면 이것은 선언된 reference leaf에 대한 포함이며, native provider의 값까지 포함한다는 주장은 추가 증거가 필요하다.

현재 고정 격자는 10–20 eV여서 HeI/HeII photo cross sections가 모두 0이다. 활성 HI에서는 \(A_j=c n_H\sigma_{Hj}\ge0\), \(u=1-x\), \(D_j=1+dA_ju\)이므로 \(\kappa^-_j=0.07A_j\), \(\kappa^+_j=0.10A_j\)이다. 모든 단면적이 0인 비활성 그룹은 \(D_j=1\)이고 gas photo column도 정확히 0이다. 단지 primal stock이 0인 경우와 column 자체가 0인 경우는 다르다.

## 6. 실제 rate fit의 양성·미분 상계

아래 식은 `ft03_interval.rs`, `ft03_rates.rs`, `hh_primary_extension.rs`에서 읽은 계수에 대한 것이다. `AtomicProvider`의 별도 raw Grackle coefficient를 FT03 Case A fit 대신 쓰지 않는다. Source의 모든 소수 상수는 해당 binary64 leaf가 나타내는 실수로 해석하며, 결합 상수를 native에서 새로 반올림하는 대신 원 연산 graph를 유지한다.

### 로그 기울기로 전체 온도 구간을 감싸는 방법

양의 함수

\[
R(T)=A T^s e^{-B/T}(1+u)^{-q},\qquad u=K T^{-r},
\]

에 대해 \(\mathscr D=T\partial_T\)와 \(L=\mathscr D\ln R\)를 정의하면

\[
L=s+B/T+qr\frac{u}{1+u},\qquad
\mathscr DL=-B/T-qr^2\frac{u}{(1+u)^2},
\tag{19}
\]

\[
R'=\frac{R}{T}L,\qquad
R''=\frac{R}{T^2}\{L^2-L+\mathscr DL\}.
\tag{20}
\]

이 표현은 source를 새 prefactor로 재정의하라는 뜻이 아니다. 원 source 식으로 \([R]\)를 감싼 뒤 식 (19)–(20)으로 독립적인 derivative bound를 만드는 방법이다. \(u\ge0\)이면
\(u/(1+u)\in[0,1]\), \(u/(1+u)^2\in[0,1/4]\)이며,
작은 온도 구간에서는 \(u(T_+)\le u\le u(T_-)\)를 이용해 더 좁힐 수 있다.
내부 변수 \(v=u/(1+u)\)를 쓰면 두 번째 함수는 \(v(1-v)\)이므로
\(1/2\) 포함 여부를 검사해 exact extremum을 구한다.

| Source coefficient | 식 (19)의 실제 구조 | 양성·단조성 |
|---|---|---|
| HI·HeII radiative recombination \(\alpha\) | \(\alpha=C(\Lambda/T)^{1.503}[1+(\Lambda/(0.522T))^{0.470}]^{-1.923}\) | \(\alpha>0\), \(s_\alpha=-1.503+1.923(0.470)u/(1+u)<0\)이므로 감소 |
| HeI radiative recombination | \(3\times10^{-14}(570670/T)^{0.654}\) | 양수, 감소; \(\alpha''=0.654(1.654)\alpha/T^2>0\)인 정확실수 형태. Source exponent leaf의 \(1+0.654\)는 interval 합으로 유지 |
| Collisional ionization \(\beta_a\) | \(A_aT^{-1.5}e^{-\Lambda_a/(2T)}(\Lambda_a/T)^{P_a}/[1+(\Lambda_a/(C_aT))^{R_a}]^{D_a}\) | 양수; \(L_\beta=-1.5-P_a+\Lambda_a/(2T)+D_aR_a u/(1+u)>0\) in 35–60 kK |
| Dielectronic terms | \(A_kT^{-1.5}e^{-b_k/T}\), source frozen \(b_k\)와 prefactor | 양수. \(L=-1.5+b_k/T\), \(\mathscr DL=-b_k/T\) |
| HH coefficient | \(k=1.2\times10^{-17}T^{1.2}e^{-157800/T}\) | 양수, \(k_T>0\), \(k_{TT}>0\) for \(T>0\) |

FT03의 \(\Lambda_a\)는 \((315614,570670,1263030)\) K,
\(P_a=(-1.089,-1.146,-1.089)\),
\(C_a=(0.354,0.416,0.553)\),
\(R_a=(0.874,0.987,0.735)\),
\(D_a=(1.101,1.056,1.275)\)이며 원 배열 순서는 HI, HeI, HeII다.
\(L_\beta>0\)은 마지막 양의 항을 버리고 \(T\le60000\)을 넣은 하한만으로도 확인할 수 있다. 온도 guard를 넘는 임의 영역에 이 단조성을 자동 확장하지 않는다.

HH에서 \(a=1.2\), \(z=157800/T>0\)라 두면

\[
\frac{k'}k=\frac{a+z}{T}>0,\qquad
\frac{k''}k=\frac{a(a-1)+2(a-1)z+z^2}{T^2}>0.
\tag{21}
\]

### RR kinetic cooling은 별도로 검사한다

Source의 kinetic coefficient는

\[
K_{\rm rr}=k_BT\alpha(T)h(T),\qquad h=1.5+s_\alpha.
\tag{22}
\]

HeI에서는 \(h=1.5-0.654>0\)이다. HI·HeII에서는
\(h=1.5-1.503+1.923(0.470)u/(1+u)\)다.
현재 온도 영역에서는 \(\Lambda/(0.522T)>1\)이므로 \(u>1\)이고,

\[
h>1.5-1.503+\tfrac12(1.923)(0.470)>0.44.
\tag{23}
\]

마지막 0.44는 source binary64 잎의 오차보다 훨씬 넓은 여유를 둔 유리수 하한이다. 반대로 \(T\to\infty\)에서 이 fit을 무제한 연장하면 \(h\to1.5-1.503<0\)이므로 `alpha>0`만으로 모든 온도에서 kinetic cooling이 양수라고 주장할 수 없다. 수학적 매끄러움과 물리적으로 허용한 source fit 범위의 차이다.

\(s=s_\alpha\), \(\dot s=\mathscr Ds\), \(\ddot s=\mathscr D^2s\)이면

\[
\begin{aligned}
K'_{\rm rr}&=k_B\alpha\{(1+s)h+\dot s\},\\
K''_{\rm rr}&=\frac{k_B\alpha}{T}
 \{s(1+s)h+(h+1+2s)\dot s+\ddot s\},\\
\dot s&=-qr^2\frac{u}{(1+u)^2},\qquad
\ddot s=qr^3\frac{u(1-u)}{(1+u)^3}.
\end{aligned}
\tag{24}
\]

따라서 RR energy Hessian은 \(\alpha''\)만 계산해서 얻을 수 없다. 이 식은 source Jet path를 점검하는 독립적인 닫힌 형태다. \(\ddot s\)를 누락하거나 native `log_slope_derivative` 값이 \(d/dT\)인지 \(d/d\ln T\)인지 혼동하면 결과가 달라진다. 현재 `ft03_rates.rs`의 `gp`는 \(d s/d\ln T\)다.

Dielectronic \(A,b_1,b_{12}\)는 interval source에 `from_bits`로 고정돼 있다. `ft03_rates.rs`의 원 실수 곱을 새로운 고정밀 값으로 다시 생성해 이 leaf를 덮어쓰지 않는다. 각 event rate는 양의 핵 분율·양의 \(n_e\)·양의 계수의 곱이고, source의 He fraction normalization은 \(\widehat f\)로 유지한다.

## 7. HH와 실제 저에너지 광자의 온도 효과

직접 HH source를

\[
H(g)=q(g)(1,0,0,-\chi_H),\qquad
q=n_H(1-x)^2 k(T)
\tag{25}
\]

로 쓴다. \(X_g\)에서는 \(q>0\), \(k_T>0\)이고

\[
q_x<0,\quad q_{y_1}<0,\quad q_{y_2}<0,\quad q_w>0.
\tag{26}
\]

첫 부호는 neutral factor 감소와 \(T_x<0\)가 함께 기여하고, 다른 두 이온 분율은 입자수 증가를 통해 온도를 낮춘다. 식 (4)로 실제 source 방향을 미분하면

\[
\boxed{DT[H]= -\mathcal C\,q\frac{\chi_Hp+w}{p^2}<0.}
\tag{27}
\]

HH는 이온화 에너지로 열에너지를 이동시키고 입자수를 늘린다. PHYS06의 \(\ell H=0\)와 이 온도 감소는 양립한다.

HI photo event rate를 \(R_j\ge0\), stored excess energy를
\(a_j^{\rm heat}=\operatorname{fl}(E_j-\chi_H)\)라 하면 그 gas source는

\[
F_{\gamma j}=R_j(1,0,0,a_j^{\rm heat}),
\]

\[
\boxed{DT[F_{\gamma j}]=\mathcal C R_j
       \frac{a_j^{\rm heat}p-w}{p^2}.}
\tag{28}
\]

따라서 \(a_j^{\rm heat}>0\)라는 thermal heating 부호만으로 \(T\) 증가를 결론낼 수 없다. 온도가 증가하는 임계조건은

\[
a_j^{\rm heat}>w/p=\frac{3k_BT}{2\epsilon_{\rm eV}}
\tag{29}
\]

이다. 새 전자가 운동에너지를 나누어 갖는 효과가 오른쪽에 나타난다.

이번 archived support는 \(E_j\le13.7\) eV이며, \(13.7\) eV보다 높은 8개 노드의 stock은 0이다. Isotropic reference transport는 redshift만 하고 fixed hat remap은 해당 support 밖의 높은 노드에 양의 수를 만들지 않으며, birth도 13.7 eV에만 들어간다. 따라서 이 reference family의 full/first-half input은 \(b\in[0,1]\) 전체에서 같은 상한을 유지한다. 이는 native widened interval의 zero support를 대신 확인한 진술은 아니다.

활성 HI 채널에서는 PHYS06의 exact subtraction 확인에 따라 \(a_j^{\rm heat}=E_j-\chi_H\)이고

\[
0<a_j^{\rm heat}<0.102\ {m eV},\qquad
\frac{w}{p}\ge\frac{13}{1.93+2.53\widehat f}>6\ {m eV}
\tag{30}
\]

가 source density leaves에서 확인할 수 있는 넓은 여유의 부등식이다. 따라서 실제로 stock이 있는 활성 광자와 새 birth 모두 **\(w\)를 증가시키면서 \(T\)를 감소시키는 방향**을 준다. 비활성/zero-stock 채널은 해당 방향이 0이다. 단위 eV/H인 \(w\)와 입자/H인 \(p\)의 비는 particle당 eV다.

물리적 경쟁은 두 경로로 나뉜다. HH와 photoionization은 neutral H를 함께 소모하므로 서로의 반응률을 줄인다. 열에너지 \(w\)에서는 HH의 음의 항과 photo의 양의 항이 경쟁하지만, 이 저에너지 입력의 온도 방향은 둘 다 음수다. 온도 감소는 \(k_{HH}(T)\) 및 현재 영역의 collisional ionization coefficient를 낮추고 radiative recombination coefficient를 높이는 방향이다. 전체 \(W\)나 finite interaction의 부호는 이 국소 방향만으로 결정하지 않는다.

## 8. Whole-Θ source partial과 cubic의 정확한 범위

### 첫 source stage의 직접 parameter cross derivative

COMMON seed의 gas·photons·guard는 미래 \((\lambda,b)\)에 독립이다. Geometry/time/grid가 고정된 full stage와 first-half stage의 **유한 stage source leaf**를 먼저 정의한다.

\[
M_j=\operatorname{exact}(\operatorname{fl}(dS_*))\,\delta_{j,24},\qquad
(B_d)_j=M_j/\operatorname{exact}(d),\qquad
N_j(b)=\bar N_j+bM_j=\bar N_j+b\,d(B_d)_j.
\tag{31}
\]

\(M_j\)는 photon amount [photons/H], \((B_d)_j\)는 그 fixed stage의 effective rate [photons/H/s]다. 원 source rate는 \(S_*=5\times10^{-15}\) photons/H/s지만 PHYS07 port는 `dt * SOURCE`의 source 순서에 따른 binary64 결과를 birth leaf로 고정한다. 따라서 \((B_d)_j=S_*\delta_{j,24}\)를 exact leaf identity로 두지 않는다. 정규화된 isotropic angular weights의 합은 1이고 이 amount를 소스에 한 번만 넣는다. \(d\)가 다른 두 stage는 각각 자신의 \(M,B_d\)를 갖는다.

\[
P_{B_d}^{(d)}(g)=\sum_j(B_d)_j\frac{K_j(g)}{D_j(g)},
\quad
F(g;\lambda,b)=F_0(g)+\lambda H(g)
       +\sum_j\bar N_j\frac{K_j(g)}{D_j(g)}+bdP_{B_d}^{(d)}(g),
\]

\[
G(g;\lambda,b)=g-g_0-dF(g;\lambda,b)
\tag{32}
\]

에서는 전체 \(X_g\times\Theta\)에서

\[
\boxed{
G_\lambda=-dH,\quad
G_b=-d^2P_{B_d}^{(d)},\quad G_{\lambda b}=0,
\quad G_{g\lambda}=-dH_g,\quad
G_{gb}=-d^2(P_{B_d}^{(d)})_g.}
\tag{33}
\]

이는 실제 model structure에서 온 source partial이다. \(G_{\lambda b}=0\)은 \(W=0\)을 의미하지 않는다. 충분히 정칙한 root family가 있다면

\[
A U=dH,\qquad A V=d^2P_{B_d}^{(d)},\qquad A=I-dF_g,
\]

\[
\boxed{A W=dH_gV+d^2(P_{B_d}^{(d)})_gU+dF_{gg}[U,V].}
\tag{34}
\]

Actual \(A\)의 역작용과 \(U,V\)의 방향·포함값이 필요하다. PHYS05의 conditional propagation 식은
\(N_\lambda=0,N_b=M=dB_d,N_{\lambda b}=0,g_{0,\lambda b}=0\)인 이 경우 식 (34)로 정확히 환원된다. 이를 확인하기 위해 이전 checker를 재실행하지 않았다.

두 번째 half에는 첫 half에서 생성된 gas/photon/guard의 \(U,V,W\)와 their joint parameter dependence가 들어온다. 따라서 식 (31)–(34)의 COMMON-input 단순화를 그 단계에 복사하지 않는다.

### 실제 방향미분으로 확인하는 source interaction

HI-only birth에서 \(A_j=c n_H\sigma_{Hj}\), \(u=1-x\)이고

\[
P_{B_d,j}^{(d)}=(B_d)_jA_juD_j^{-1}(1,0,0,a_j^{\rm heat}).
\]

\[
\nu_T=\frac{d\ln k}{d\ln T}=1.2+157800/T,\qquad
\Xi_j=\frac{u\nu_T}{p}\left(1-\frac{a_j^{\rm heat}p}{w}\right)>0
\tag{35}
\]

를 사용하면

\[
\begin{aligned}
[H_gP_{B_d}^{(d)}]_x
 &=-q\sum_j\frac{A_j(B_d)_j}{D_j}(2+\Xi_j),\\
[(P_{B_d}^{(d)})_gH]_x
 &=-q\sum_j\frac{A_j(B_d)_j}{D_j^2}.
\end{aligned}
\tag{36}
\]

둘은 각각 neutral substrate 및 HH thermal feedback, 그리고 opacity의 neutral substrate 감소를 나타내며, 비영 birth에서는 각각 음수다. Energy row에서는

\[
\ell H_gP_{B_d}^{(d)}=0,\qquad
\ell(P_{B_d}^{(d)})_gH=-q\sum_j
 \frac{(\chi_H+a_j^{\rm heat})A_j(B_d)_j}{D_j^2}<0.
\tag{37}
\]

현재 active heat leaf에서는 \(\chi_H+a_j^{\rm heat}=E_j\)다. 일반 grid에서는 \(E_j+\varepsilon_{Hj}\)를 보존한다. 이 두 source directional witnesses는 실제 \(U,V\)를 넣은 식 (34)와 다른 대상이며, 그 부호를 finite \(W\)에 직접 대입하지 않는다.

### Endpoint birth 때문에 시작되는 혼합 cubic

아래는 고정 leaf 또는 명시적으로 smooth한 time-source chart의 formal \(h\downarrow0\) 계수다. Raw binary64 \(h\mapsto n_H(h)\) 및 native libm 결과를 매끄러운 함수로 간주하지 않는다. Fixed-grid remap의 \(h=0^+\) chart와 inactive quotient는 PHYS04에서 규정한 의미로 사용하고, lower guard ledger를 삭제하지 않는다.

이 **formal rate family**에서는 \(B_j=S_*\delta_{j,24}\)를 \(h\)에 독립인 rate로 정의하고 born amount를 \(hB\)로 둔다. 또는 선택한 effective rate를 고정한 별도의 formal family를 정의할 수 있지만 어느 경우인지 명시해야 한다. 식 (31)의 finite \(B_d\)와 이 smooth \(B\)는 다른 정의이며, 여러 native `fl(h*S_*)` 결과를 미분해서 smooth \(B\)를 얻었다고 해석하지 않는다. 아래 cubic 식은 원 source 순서의 formal 계수를 설명하고 finite-stage 숫자는 식 (31)의 실제 leaf를 사용한다.

\(U=O(h)\), gas \(V=O(h^2)\)이므로 혼합 gas 응답은 \(h^2\)에서 소멸하고

\[
[h^3]W_{\rm full}=H_gP_B+(P_B)_gH,
\quad P_B=\sum_jB_jK_j.
\tag{38}
\]

Constant \(B\)와 \(m\)개의 같은 BE substeps \(\delta=h/m\)에서는

\[
\boxed{[h^3]W_m=\alpha_mH_gP_B+\beta_m(P_B)_gH,}
\qquad
\alpha_m=\frac{(m+1)(m+2)}{6m^2},\quad
\beta_m=\frac{(m+1)(2m+1)}{6m^2}.
\tag{39}
\]

계수의 짧은 유도는 다음과 같다. \(k\)번째 substep의 leading gas \(U_k=k\delta H\), photon \(V_{k,\gamma}=k\delta B\), gas \(V_{k,g}=k(k+1)\delta^2P_B/2\)다. Mixed forcing은 그 단계에서

\[
\delta^3\left\{\frac{k(k+1)}2H_gP_B+k^2(P_B)_gH\right\}
\]

를 추가한다. \(k=1,\ldots,m\)을 합하고 \(\delta^3=h^3/m^3\)를 대입하면 식 (39)를 얻는다. Nonphoto background, 기존 photon stock, prescribed smooth density drift와 remap은 이 leading mixed coefficient에 추가항을 만들지 않는다. HH가 photon-independent이고 photo source가 gas–photon bilinear라서 \(H_zB=0\), \(J B\)의 gas part가 \(K B\), \(F_{zz}[H,B]\)의 gas part가 \(K_g[H]B\)이기 때문이다. 이 요소들은 다음 \(h^4\) 차수와 유한 \(h\)에서 중요해진다. 기존 입력에 이미 signed \(U,V,W\)가 있거나 source가 transported photon에 다른 내부 방출을 생성하면 이 COMMON-input 유도는 다시 해야 한다.

식 (39)는 PHYS04 ordered quartic의 기존 cubic formula와 일치한다. One-full은 \((\alpha_1,\beta_1)=(1,1)\), two-half는 \((\alpha_2,\beta_2)=(1/2,5/8)\)다. Source-specific thermal form은

\[
[h^3]W_{m,x}=-q\sum_jA_jB_j(2\alpha_m+\beta_m+\alpha_m\Xi_j)<0,
\]

\[
\ell[h^3]W_m=-\beta_m q\sum_j E_jA_jB_j<0
\tag{40}
\]

이다. 두-half minus full의 leading coefficients는

\[
[h^3](W_2-W_1)_x=q\sum_jA_jB_j(11/8+\Xi_j/2)>0,
\]

\[
\ell[h^3](W_2-W_1)=\frac38q\sum_jE_jA_jB_j>0.
\tag{41}
\]

이것은 유한 step에서 실제 defect의 부호를 계산했다는 결과가 아니다. 식 (38)–(41)을 \(W(h)=h^3C+O(h^4)\)라는 분석적 근사로 사용할 때에는 해당 한쪽 source chart의 충분한 joint smoothness와 remainder control이 필요하다. 현재 C² gas/parameter 영역만으로 수치적인 \(h^4\) 나머지가 주어지지 않는다. PHYS04의 remap-specific quartic과 PHYS05의 old-family remap \(h^2\) coefficient는 각각 다른 조건의 항이며 여기의 cubic을 대체하지 않는다.

차원은 \(q\sim s^{-1}\), \(A_j\sim s^{-1}\), \(B_j\sim photons/H/s\)이므로 \(h^3qA_jB_j\)가 ion fraction이고 energy row에는 eV/H가 붙는다.

## 9. C² open-neighborhood의 구성과 전체 source 포함의 남은 조건

소스 실수 함수의 정칙성 증명은 다음 구성으로 닫힌다.

1. Fixed stage에서 \(n_H,n_{He},f>0\)이고 모든 coefficient leaf가 유한하다. 식 (13)의 closure에서 strict simplex·\(w>0\)·35–60 kK의 양의 margin을 확인한다. 그러면 그 안의 \(p>0\), \(T>0\), \(1+u(T)>1\), \(D_j\ge1\)이다.
2. FT03 nonphoto, HH, photo의 원 식은 그 영역에서 다항식·양의 거듭제곱·exp·양의 denominator의 합성이다. 따라서 고정 leaf의 real graph는 \(C^\infty\), 특히 C²다. \(J_{\rm norm}\)은 같은 nonphoto source의 선형 조합이며 \(\Psi\)도 같은 photo rational source의 선형 조합이므로 별도 특이점이 없다.
3. 첫 source stage의 \(\bar N+bM=\bar N+d bB_d\)는 parameter에 affine이고 기존 gas는 상수다. Guard/transport coefficient를 fixed clock과 fixed geometry에 결박하면 \(\lambda,b\)의 작은 열린 연장에서도 동일 합성식이 존재한다. 실제 코드의 입력 guard는 물리 영역에서 유지한다.
4. 닫힌 \(X_g\times\Theta\)를 이 열린 영역에 넣었으므로 그 compact 집합의 값·1차·2차 미분에는 유한한 상계가 존재한다. 실제 수치 상계는 해당 전체 집합을 외향 interval로 계산해 얻어야 한다. 유한성의 추상적 존재를 계산된 숫자와 혼동하지 않는다.

이것으로 **지정된 reference source family의 C² 도메인**을 얻는다. 이어서 root가 실제로 계산한 \([G(g_c,\Theta)]\), \([G_g(X_g,\Theta)]\), 모든 partial/Hessian이 있으면 PHYS06의 충분조건에 넣을 수 있다. 그 충분조건의 arithmetic margin이 양수라면 정확히 어느 reference residual의 root 존재를 보였는지 판정할 수 있다. Native source tuple/leaf의 동일성이나 허용된 native producer는 이 순수 수학 계산에서 생성되지 않는다.

특히 아래 자료는 서로 다른 의무다.

| 의무 | 이번 도메인 결과가 제공하는 것 | 별도 필요 사항 |
|---|---|---|
| C² chart | 실제 식·분기·양의 denominator·open margin의 구성 | 실제 계산에 사용한 reference leaf와 input identity |
| Whole-box arithmetic | 평가 가능한 scalar/derivative 공식 | 실행된 외향 연산의 결과, tail·rounding 증거 |
| Source identity | 현재 NCP 파일 identity, 읽은 분기 | native stage·direction·preBE tuple와 exact-real reference의 대응 |
| Uniform root | 충분조건을 적용할 물리 영역 | 해당 residual의 strict inclusion 계산·해석 |
| 실제 full/two-half 비교 | first-stage parameter partial 구조 | second-half incoming joint carry, 동일 family의 실제 데이터 |
| Finite \(I_h\) | uniform W라면 이중적분 경로 사용 가능 | 실제 whole-Θ W와 native/source 해석, 필요하면 시간 나머지 |

### 어떤 경우에 subdivision을 하는가

현재 \(\lambda,b\)만 변하는 fixed-geometry chart에서 kinetic fit과 atomic leaf의 분기는 바뀌지 않는다. 따라서 관성적으로 parameter subdivision을 추가하지 않는다. 다음 중 실제 실패 원인이 확인될 때만 필요한 축을 나눈다.

- 온도·simplex·\(D>0\)의 **실제 물리 조건**을 상자가 침범하면 후보 상자를 줄이거나 admissible intersection을 명시해야 한다. 같은 침범을 더 작은 interval 조각으로 덮는 것만으로 원래 전체 상자가 물리적이 되지는 않는다.
- 실제 함수는 admissible이지만 coordinate hull이나 interval dependency 때문에 온도 guard 또는 source derivative 상계가 넓어졌다면 correlated energy relation을 유지하거나 해당 gas 축을 나눈다. 어떤 bounding expression이 실패했는지 먼저 기록한다.
- Fixed geometry의 `eb` enclosure가 hat knot/guard를 가로질러 native source adapter가 거부하면 그 **coefficient enclosure와 branch identity**를 다룬다. \(\lambda,b\) subdivision은 그 고정 `eb`를 바꾸지 않으므로 일반적으로 해결책이 아니다.
- 이후 \(H_i\), 시간, grid energy 자체를 variable로 확장한다면 transport hat knot, 10/20 eV guard, Verner cutoff가 실제 variable-domain boundary가 된다. 이때에는 branch subdivision 또는 명시적인 piecewise/one-sided 이론이 필요하며 현재 C² claim을 그대로 사용하지 않는다.
- 식 (34)의 mixed forcing나 root 충분조건에서만 폭 문제가 생기면 그때의 원인에 맞게 parameter/state 영역을 나눈다. 각 조각의 root가 같은 family에 속한다는 overlap·uniqueness 연결을 보존해야 한다. 실제 충분조건의 실패가 곧 물리적 해의 부존재를 의미하지는 않는다.

## 10. 구현에 넘기는 검산 계약

이 문서 작성 agent는 새 과학 수치 코드를 실행하지 않았다. Root가 관리하는 PHYS07 bounded run에 다음 입력과 관측을 넘겼다. 이는 과거 PHYS04/05/06 checker의 재실행 요청이 아니다.

| 새 관측 | 입력 | acceptance |
|---|---|---|
| Gas/open-domain margin | 식 (10), 선택하면 식 (13), source constants와 고정 stage leaves | source endpoint convention을 기록하고 simplex·\(T\)·\(p\)·\(D\) margin을 정확/외향 산술로 저장 |
| Source temperature consistency | exact \(\widehat f\), paired source blanket | 지정된 density ratio가 blanket에 포함되고 온도 guard가 양의 여유로 닫힘 |
| Low-energy thermal mechanism | 실제 input support, \(a_j^{heat}\), 식 (28)–(30) | support/zero를 검증한 reference family에서 \(a_j^{heat}p-w<0\); zero rate와 strict negative rate를 구별 |
| Whole-Θ source partial | full 및 first-half \(\bar N+bM=\bar N+d bB_d\), \(X_g\), \([0,1]^2\) | 식 (33)의 직접 \(G_{\lambda b}=0\), 다른 signed source partial과 Hessian을 보존 |
| Kinetic derivatives | 실제 FT03·HH leaf, positive interval \([T_-,T_+]\) | 원 graph의 AD와 식 (19)–(24)의 독립 관측을 구별해 기록; 작은 source-leaf 차이를 숨기지 않음 |
| Source interaction witness | 식 (35)–(37), 실제 birth source | 부호의 적용 범위를 source directional derivative로 유지, \(W\)나 \(I_h\)로 승격하지 않음 |
| Uniform inclusion arithmetic | 실제 \([G_c],[A]\), 고정 \(C\), 선언된 radius | 실제 strict margin·실패를 기록; native authority와 분리 |

예정한 새 source-box 호출은 최대 2개 named stage이고 실제 command·wall/memory/output ceiling과 첫 실행 기록은 `SCIENTIFIC_CONTRACT.md` 및 root의 `RUN_LEDGER`가 관리한다. 이 문서가 command 수행이나 성공을 선언하지 않는다. `C=I`를 쓰는 경우에도 실제 행렬 \([A]\), component radius와 \(\beta+Br\)를 평가해야 한다.

## 11. 근거 상태와 source identity

본 문서에서 새로 유도한 식 (1)–(41)과 C²/open-chart 논증은 **derived**다. 현재 source 경로·상수·guard를 읽은 사실은 **implementation-inspected**이며 새 native 실행 검증을 뜻하지 않는다. 보관 gas/stock 값은 이전 실행 artifact에서 읽은 **archived input**이다. 새 수치 포함·부호·margin은 PHYS07 실행 증거가 연결된 범위에서만 **numerically checked / implementation-verified**를 추가한다. Actual native \(W,I_h\), second-half carry, full/two-half defect와 time/continuum remainder는 별도 증거가 없으면 **unresolved**다.

소스 고정:

- Repository: `cosmosapjw-quantum/WU088_HH`
- NCP head: `65a36e255aa6d9911e23a9b5ced18d8a9f507606`
- NCP tree: `f823df8c95defcaba737139859cd9eeeda4ef133`
- Source intake manifest SHA256: `fdecbf0c21d90cae761899d75442b14211f99c56cb45b9f153fe44a36d8ea48b`
- COMMON seed SHA256: `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b`

| 읽은 핵심 파일 | SHA256 |
|---|---|
| `candidate/src/ft03_interval.rs` | `886580a810b8ec29c8f0b6199c0e35d82fde1f46d984a5f8f1da304326a42a42` |
| `candidate/src/ft03_rates.rs` | `1a97cd7a3555deeb4d8700376cd84580c5102127773bc3a235a29c33b0c1542f` |
| `candidate/src/hh_primary_extension.rs` | `f47d910abb096f96b829e3392fdfbf55d079ba2fbb09a45416c97c76a4f4a647` |
| `candidate/src/phys04_mixed.rs` | `95c1ecb757b32abd1fd5d5e7ef5195cc8a3ee67ca54de0b1f6e5b87bb58d3cd8` |
| `candidate/src/phys04_transport.rs` | `566a68cf4111d8586b5fee7bd0750f39ec98b2e3f2b6217a656b270deda5ce78` |
| `candidate/src/paired_runtime.rs` | `5cfa65e67e4843ae6ae3ae3eb3d1d5a47e23c01db14eaf26feceb4692fe2e4db` |
| `candidate/src/atomic_provider.rs` | `b0b572d3940a7a1f740e09d5f43c60236ec61511e8bdbcc68e60395ec7e107d3` |
| `src/energy.rs` | `c3bbe3c7b0a4428d01877ee9d4e67501e86a12bda16f388ceb70e5d93b767c85` |
| `src/adapter.rs` | `7fbe814c2ae0b863fb90f57a43363242d987a02cd3df3faf78273cd6551c3442` |
| `src/uniform.rs` | `b152616d6f5188497316d296f0181638ee89acd4fac31cb8343fecf05f30b6a2` |

Source intake가 확인한 이전 v2와의 byte parity는 kinetics와 기존 transport에 적용된다. `phys04_mixed.rs`에는 source metadata export가 추가됐고 원 수식은 유지돼 있다. 해당 변경은 NCP `evidence/CANDIDATE_DELTA.patch`에 보존돼 있다. 이전 PHYS04의 cubic/quartic 유도와 PHYS05의 `CONTRACT.md`는 필요한 식만 읽어 비교했으며 이전 검산 프로그램은 실행하지 않았다.

독립 검토에서 finite `born_leaf=fl(d*S_*)`와 formal \(dS_*\)의 표기 혼동을 발견해 식 (31)–(37)을 수정했다. 원 문서와 claim JSON의 전체 bytes·hash 및 수정 이유는 `theory/corrections/BIRTH_LEAF_CORRECTION.json`과 그 snapshot들에 보존했다. Source code나 수치 결과는 이 수정으로 바뀌지 않았고 과학 검산을 다시 실행하지 않았다.

Host label은 `GPT-6 Astra Pro`이며 기존 Astra v4 연구·코딩 지침을 이 작업에 이어 적용했다. 프로그램이 raw `Pro` suffix를 별도 등록 model alias로 수락했다거나 native 실행 권한을 부여했다는 주장은 하지 않는다. 본 문서는 creator 산출물이며 최종 independent promotion을 자체 발행하지 않는다.
