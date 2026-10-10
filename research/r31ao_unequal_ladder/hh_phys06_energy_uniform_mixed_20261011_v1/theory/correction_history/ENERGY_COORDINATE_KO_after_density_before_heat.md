# PHYS06: 결합 에너지 좌표와 reduced-BE 혼합 감도의 정확한 제약

## 판정 범위

이 문서는 PHYS04 reduced-BE equality residual과 PHYS05의 affine photo
stoichiometry를 그대로 두고, 기존 energy ledger를 gas 좌표 및 미분 잔차로
표현한다. 새 물리 rate, closure, endpoint 또는 실행 권한을 도입하지 않는다.
아래 정리의 근거 상태는 **derived**다. 읽은 소스의 의미와 연결한 부분은
source inspection이며, 실제 FT03/LCS runtime 또는 uniform physical tube의
**implementation-verified** 판정이 아니다. 최종 독립 promotion은 이 문서의
작성자가 수행하지 않는다.

핵심 결과는 세 가지다. 첫째, 열에너지와 이온화 에너지를 합친 좌표에서는 HH
항의 에너지 row가 항등적으로 0이고 각 photo column의 에너지 row는
\(E_j\kappa_j\)다. 둘째, 고정된 비음수 incoming photon numerator에서
reduced photo energy RHS의 gas Hessian은 음의 준정부호다. 셋째, gas와
photon을 합친 BE 에너지 잔차 및 그 \(U,V,W\) 미분은 정확한 선형
ledger identity를 만족한다. 이 결과들은 실제 mixed endpoint response의
부호나 크기를 결정하지 않는다.

이 좌표의 물리 내용 자체는 새 closure가 아니다. 원본
coupled_primary.rs의 energy 함수가 이미 같은 matter binding energy,
escaped energy 및 primary photon energy를 합산한다. 이번 결과는 그
에너지 조합을 residual, Hessian 및 interval preconditioner의 계약으로
구체화한 것이다. [E-SRC02, E-SRC04]

## 1. 정의, 단위와 고정되는 자료

Gas state를
\[
g=(x,y_1,y_2,w)^{\mathsf T}
\]
라 둔다. \(x=n_{\rm HII}/n_{\rm H}\),
\(y_1=n_{\rm HeII}/n_{\rm He}\),
\(y_2=n_{\rm HeIII}/n_{\rm He}\)다. 이론적으로 일관된 normalization에서는
\(f=n_{\rm He}/n_{\rm H}>0\)다. 실제 source coefficient graph에서는
stage의 \(f\)와 저장된 density leaf의 비율 \(\widehat f\)를 구분해야 하며,
그 차이를 §5.1에서 보존한다. 아래 photo column과 \(S,\ell\)에 들어가는
\(f\)는 stage.f_he다. Helium 두 변수는 H에 대한 분율이 아니다.
\(w\)는 H nucleus 하나당 열에너지로, 단위는 eV/H다.
Packet \(j\)의 에너지 \(E_j>0\)는 eV, \(N_j\)와 \(P_j\)는 photons/H다.
여러 방향의 grouping이 끝난 packet을 쓴다면 그 grouping의 normalization을
그대로 유지한다. [E-SRC01–E-SRC03]

Proper-time step \(d>0\), endpoint의 \(n_{\rm H}>0\), \(c>0\),
\(f\), \(H\), \(E_j\), \(\sigma_{aj}\) 및 binding energies \(\chi_a\)는
이번 \((a,b)=(\lambda,b)\) 미분에서 고정한다. \(c\)는 cm/s,
\(n_{\rm H}\)는 cm\(^{-3}\), \(\sigma\)는 cm\(^2\), \(d\)는 s다.
한 full step과 두 half step 사이에서 endpoint density와 clock이 다를 수
있다는 사실과, 각 endpoint의 \((\lambda,b)\) 미분에서 그 자료를 고정한다는
전제는 별개다. Time-step 미분이나 density-parameter 미분에 아래 식을
그대로 사용해서는 안 된다.

\[
\ell_{\rm abs}(g)=
\bigl(1-x,\ f(1-y_1-y_2),\ fy_1\bigr),
\quad
r_{aj}=c n_{\rm H}\sigma_{aj}\ell_{{\rm abs},a},
\quad
\kappa_j=\sum_a r_{aj},\qquad D_j=1+d\kappa_j .
\tag{1}
\]
\(r_{aj},\kappa_j\)의 단위는 s\(^{-1}\), \(D_j\)는 무차원이다.
Photo stoichiometry column은
\[
K_j(g)=
\begin{pmatrix}
r_{{\rm H},j}\\
(r_{{\rm HeI},j}-r_{{\rm HeII},j})/f\\
r_{{\rm HeII},j}/f\\
\sum_a r_{aj}(E_j-\chi_a)
\end{pmatrix}.
\tag{2}
\]
이를 \(P_j\)에 곱하면 첫 세 row는 fraction/s, 마지막 row는 eV/(H s)다.
Helium row의 \(1/f\)와 에너지 row의 \(f\)는 같은 normalization의 양면이다.
둘 중 하나를 빼면 에너지 항등식이 깨진다. [E-SRC01–E-SRC03]

Binding vector와 row를
\[
\beta=
\begin{pmatrix}
\chi_{\rm H}\\ f\chi_{\rm HeI}\\
f(\chi_{\rm HeI}+\chi_{\rm HeII})
\end{pmatrix},
\qquad
\ell=(\beta^{\mathsf T},1)
\]
로 두고,
\[
e=\ell g
=w+\chi_{\rm H}x+f\chi_{\rm HeI}y_1
  +f(\chi_{\rm HeI}+\chi_{\rm HeII})y_2
\tag{3}
\]
를 정의한다. \(e\)는 중성 ground-state 원자를 기준으로 한 저장
matter energy이며, baryon rest energy나 모든 우주론적 stress-energy를
뜻하지 않는다. \((-+++)\) convention과 모순되지 않지만 이 국소 ledger
항등식은 별도의 GR 에너지 보존 정리를 주장하지 않는다.

소스의 binding energies는
\[
(\chi_{\rm H},\chi_{\rm HeI},\chi_{\rm HeII})
=(13.598434599702,\ 24.587389011,\ 54.41776)\ {\rm eV}.
\tag{4}
\]
AtomicProvider의 단면적 fit cutoff
\((13.60,24.59,54.42)\) eV와 구분한다. Fit cutoff는
\(\sigma_{aj}=0\)가 되는 branch를 결정하며, binding energy는 이온화 및
thermal energy ledger를 결정한다. 식 (3)과 (2)에 같은 \(\chi_a\)를 쓰면
각 cutoff의 차이와 무관하게 아래 cancellation이 성립한다. Cutoff를
binding energy로 치환하는 수정은 허용하지 않는다. [E-SRC02, E-SRC05]

## 2. 좌표 변환과 HH 항의 에너지 row

\[
\xi=(x,y_1,y_2,e)^{\mathsf T}=Sg,\qquad
S=\begin{pmatrix}I_3&0\\ \beta^{\mathsf T}&1\end{pmatrix},
\quad
Q=S^{-1}=\begin{pmatrix}I_3&0\\-\beta^{\mathsf T}&1\end{pmatrix}.
\tag{5}
\]
따라서
\[
w=e-\beta^{\mathsf T}(x,y_1,y_2)^{\mathsf T}.
\]
이는 상수 선형 변환이고 \(\det S=1\)이다. \(e>0\)만 검사해서는
\(w>0\)를 보장할 수 없다.

HH source가
\[
H_{\rm HH}(g)=(q(g),0,0,-\chi_{\rm H}q(g))^{\mathsf T}
\]
이면
\[
SH_{\rm HH}(g)=(q(g),0,0,0)^{\mathsf T},
\qquad \ell H_{\rm HH}\equiv0 .
\tag{6}
\]
이 결과는 \(q\)의 구체적 함수형에 의존하지 않는다. 현재 source의
\(q=n_{\rm H}(1-x)^2 k_{\rm HH}(T)\) 및 그 gas first/second derivatives를
보존한 상태에서도
\[
\ell H_{{\rm HH},g}u=0,\qquad
\ell H_{{\rm HH},gg}[u,v]=0
\tag{7}
\]
다. 현재 HH source에는 별도 \(1/2\)를 넣지 않는다. [E-SRC04]

온도는 여전히 열에너지 \(w\)로 복원한다.
\[
T=
\frac{2\epsilon_{\rm eV}
\left[e-\beta^{\mathsf T}(x,y_1,y_2)^{\mathsf T}\right]}
{3k_B[1+f_T+x+f_T(y_1+2y_2)]}.
\tag{8}
\]
여기서 \(\epsilon_{\rm eV}\)는 eV를 erg로 바꾸는 source의 conversion
constant다. \(k_B\)는 erg/K로 유지한다. 일관된 real-arithmetic model에서는
\(f_T=f\)이고, 현재 source의 stored-density coefficient graph에서는
\(f_T=\widehat f=m.n_{\rm He}/m.n_{\rm H}\)다. 두 값을 동일하다고
반올림하여 처리하지 않는다. \(e\)를 식 (8)의 \(w\) 자리에
그대로 넣으면 다른 열모형이 된다. Source의 HH guard
\(35000\le T/{\rm K}\le60000\)과 기존 gas simplex를 유지해야 한다.
[E-SRC02, E-SRC04]

## 3. Photo column의 정확한 에너지 조합

식 (2)를 식 (3)에 대입하면
\[
\begin{aligned}
\ell K_j
={}&\chi_{\rm H}r_{{\rm H},j}
+\chi_{\rm HeI}(r_{{\rm HeI},j}-r_{{\rm HeII},j})\\
&+(\chi_{\rm HeI}+\chi_{\rm HeII})r_{{\rm HeII},j}
+\sum_a r_{aj}(E_j-\chi_a)\\
={}&E_j(r_{{\rm H},j}+r_{{\rm HeI},j}+r_{{\rm HeII},j})
=E_j\kappa_j .
\end{aligned}
\tag{9}
\]
HeII를 HeIII로 바꾸는 event의 binding 증가가
\(\chi_{\rm HeII}\)라는 점이 helium cancellation의 핵심이다. HeIII의
누적 binding energy는 \(\chi_{\rm HeI}+\chi_{\rm HeII}\)다.

이 항등식은 모든 \(g\)에서 대수적으로 성립하며, 아직 gas root 또는
photon population의 크기를 가정하지 않았다. Fixed branch에서 \(K_j\)와
\(\kappa_j\)는 gas에 affine이므로
\[
\ell K'_j[u]=E_j\kappa'_j[u],\qquad K''_j=0,\quad\kappa''_j=0 .
\tag{10}
\]
Photo source가 gas와 photon 사이에서 교환하는 전체 에너지는
\(E_j\)이고, 열에너지에 들어가는 부분만 \(E_j-\chi_a\)다.

## 4. Reduced photo energy의 concavity와 그 한계

Photon을 BE 식으로 제거하면
\[
P_j=\frac{N_j}{D_j},\qquad
\Phi(g,N)=\sum_j\ell K_jP_j
=\sum_j\frac{E_jN_j\kappa_j(g)}{1+d\kappa_j(g)} .
\tag{11}
\]
입력 \(N_j\ge0\)를 gas 미분에서 고정한다. 고정 단면적 branch에서
\[
\alpha_j=\nabla_g\kappa_j
=cn_{\rm H}
\begin{pmatrix}
-\sigma_{{\rm H},j}\\
f(\sigma_{{\rm HeII},j}-\sigma_{{\rm HeI},j})\\
-f\sigma_{{\rm HeI},j}\\
0
\end{pmatrix}
\tag{12}
\]
이고 \(\kappa'_j[u]=\alpha_j^{\mathsf T}u\)다. 스칼라 함수
\(f_d(k)=k/(1+dk)\)에 대해
\[
f'_d(k)=D^{-2},\qquad f''_d(k)=-2dD^{-3}.
\]
따라서
\[
\boxed{
\nabla_g\Phi=\sum_j\frac{E_jN_j}{D_j^2}\alpha_j,\qquad
\nabla_g^2\Phi=-2d\sum_j
\frac{E_jN_j}{D_j^3}\alpha_j\alpha_j^{\mathsf T}.}
\tag{13}
\]
특히 모든 실수 direction \(u\)에 대해
\[
\Phi_{gg}[u,u]
=-2d\sum_j\frac{E_jN_j}{D_j^3}
(\alpha_j^{\mathsf T}u)^2\le0
\tag{14}
\]
이므로 Hessian은 음의 준정부호다. 유효 tube 전체에서 \(D_j>0\),
\(N_j\ge0\) 및 \(\kappa''_j=0\)가 유지되면 그 tube에서의 정확한 정리다.
이 proof는 Newton convergence나 uniform inverse를 가정하지 않는다.

고정 \(N\)에서의 photo energy RHS는 \(w\)와 \(e\) 자체에는 의존하지
않는다. 에너지 좌표에서는 Hessian이
\(Q^{\mathsf T}(\nabla_g^2\Phi)Q\)로 변하므로 같은 음의 준정부호 성질을
갖는다. 또한 \(\alpha_{j,4}=0\)이므로 이 특정 scalar의 gradient
성분은 \(\xi\) 표현에서도 식 (12)와 같다. Strict concavity는 모든
방향에 대해 성립하지 않는다. \(\alpha_j^{\mathsf T}u=0\)인 공통
null direction, 순수 energy direction, 또는 \(E_jN_j=0\)인 column은
곡률을 주지 않는다.

반면 서로 다른 두 direction의
\[
\Phi_{gg}[u,v]
=-2d\sum_j\frac{E_jN_j}{D_j^3}
(\alpha_j^{\mathsf T}u)(\alpha_j^{\mathsf T}v)
\tag{15}
\]
에는 고정 부호가 없다. \(v=u\)면 비양수지만 \(v=-u\)면 비음수다.
어떤 active opacity direction이 있고 \(N_j>0\)이면 두 부호 모두
가능하다. Interior gas state 주변에서 작은 \(a,b\)에 대해
\(g=g_*+(a-b)u\)를 취하면 서로 반대인 두 tangent도 실제로 admissible한
국소 gas family에서 발생한다. 따라서 Hessian의 음의 준정부호를
\(\partial_\lambda\partial_b e\le0\)의 근거로 사용할 수 없다.

이번에 회수한 archived common seed의 33-node grid는
\(10\le E_j/{\rm eV}\le20\)다. 따라서 현재 provider의 HeI/HeII cutoff
24.59/54.42 eV보다 모든 node가 낮고 두 helium cross section은 그
provider의 zero branch다. 이 grid에 한정하면
\(\alpha_j=(-cn_{\rm H}\sigma_{{\rm H},j},0,0,0)^{\mathsf T}\)이므로
\[
\nabla_g^2\Phi
=-\left[
2d\sum_j
\frac{E_jN_j(cn_{\rm H}\sigma_{{\rm H},j})^2}
     {(1+dc n_{\rm H}\sigma_{{\rm H},j}(1-x))^3}
\right] e_xe_x^{\mathsf T}.
\tag{15a}
\]
즉 photo energy 곡률은 rank at most one이고, 양의 numerator를 가진
active HI column이 하나라도 있으면 rank one이다. 이는 fixed grid/cutoff와
비음수 \(N\)에 관한 구조적 결론이다. 실제 다음 endpoint의 numerator,
root 또는 \(U_xV_x\)의 부호를 얻은 결과가 아니다. 또한 He photo가 꺼져
있어도 full gas의 He ionization/recombination, electron density, 온도 및
HH Hessian은 남는다. [E-SRC05, E-SRC08]

추가 한계는 다음과 같다.

- 이것은 **photo energy RHS**의 gas Hessian이다. Full FT03/nonphoto
  energy RHS의 Hessian이나 full 4-vector RHS의 sign theorem이 아니다.
- \(N\)도 변수로 취한 joint Hessian에는 gas–stock cross block이 있다.
  Fixed-\(N\) concavity는 그 joint Hessian의 준정부호를 뜻하지 않는다.
- \(\kappa\)가 gas에 비선형이면 식 (13)에
  \(\sum_j E_jN_j\kappa_{j,gg}/D_j^2\)가 더해진다. 고정 thermal
  cross section, fixed branch라는 현재 계약을 벗어나면 부호 증명도 바뀐다.
- \(N_j\)가 signed primal 값이면 Gram coefficient의 부호가 깨진다.
  Signed **tangent**를 허용한다는 규칙은 signed primal photon stock을
  허용한다는 뜻이 아니다.

## 5. BE matter–photon energy residual

보존해야 할 nonphoto RHS를 \(F_0(g)\), 그 에너지 row를
\[
Q_0(g)=\ell F_0(g)
\tag{16}
\]
로 쓴다. 여기에는 FT03 collisional ionization, radiative/dielectronic
recombination, kinetic cooling 및 endpoint expansion work가 모두 포함된다.
현재 계산에서 이 항들을 0으로 대체하지 않는다.

결합 BE residual을
\[
G=g-g_0-d\left[F_0(g)+\lambda H_{\rm HH}(g)
                   +\sum_jK_j(g)P_j\right],
\quad
R_{\gamma j}=P_j-N_j+d\kappa_j(g)P_j
\tag{17}
\]
로 두자. 식 (6), (9)로부터 **root 여부와 무관한 residual identity**
\[
\boxed{
R_E\equiv
e-e_0+\sum_jE_j(P_j-N_j)-dQ_0(g)
=\ell G+\sum_jE_jR_{\gamma j}}
\tag{18}
\]
를 얻는다. Photon을 정확히 제거했으면 \(R_{\gamma j}=0\)이므로
\(R_E=\ell G\)다. 실제 BE root에서는
\[
e+\sum_jE_jP_j
=e_0+\sum_jE_jN_j+dQ_0(g).
\tag{19}
\]
Photo absorption과 HH 반응은 여기서 내부 교환으로 소거되지만,
nonphoto loss/work는 남는다. 비영 residual인 후보점에 대해 식 (19)를
exact endpoint identity로 주장할 수 없다. 그 오차는 식 (18)의
gas 및 photon residual에 묶어 보고한다.

### 5.1 Escape와 thermal work를 포함한 현재 controlled ledger

Nonphoto source의 H/He binding energies와 helium density ratio가 각각
식 (4)와 \(f\)에 일치하는 real-arithmetic model에서는 FT03 event ledger로부터
\[
Q_0(g)=-L_{\rm esc}(g)-2Hw
\tag{20}
\]
가 성립한다. \(L_{\rm esc}\)는 escaped energy rate를
\(n_{\rm H}\epsilon_{\rm eV}\)로 나눈 eV/(H s) 단위의 함수다.
[E-SRC02, E-SRC06]

이 cancellation은 각 event에서 확인된다. Per-H collisional
ionization rate \(C_a\), radiative recombination rate \(R_a\), recombination
kinetic energy loss \(J_a\), helium dielectronic rate \(D_k^{\rm DR}\)와
그 thermal loss per event \(\varepsilon_k^{\rm DR}\)를 쓰면
\[
\begin{aligned}
\dot B_{\rm chem}^{(\widehat f)}
 &=\sum_a\chi_a(C_a-R_a)
   -\chi_{\rm HeI}\sum_k D_k^{\rm DR},\\
\dot w_{\rm micro}
 &=-\sum_a\chi_a C_a-\sum_aJ_a
   -\sum_k\varepsilon_k^{\rm DR}D_k^{\rm DR},\\
L_{\rm esc}
 &=\sum_a(\chi_aR_a+J_a)
   +\sum_k(\chi_{\rm HeI}+\varepsilon_k^{\rm DR})D_k^{\rm DR}.
\end{aligned}
\tag{21}
\]
여기서 chemical binding energy는 nonphoto source의 실제 density ratio
\(\widehat f\)로 정상화한다. 따라서
\(\dot B_{\rm chem}^{(\widehat f)}+\dot w_{\rm micro}=-L_{\rm esc}\).
CI thermal loss를 생략하거나 RR/DR binding energy를 escaped ledger에서
빼면 식 (20)을 얻을 수 없다.

현재 NCP candidate snapshot의 HHeModel::controlled_fixture를 추가로
읽어 \(g.{\rm threshold\_ev}\)의 세 literal이 coupled_primary::CHI와
동일함을 확인했다. Ft03Model::controlled는 photon energies, cross sections
및 placeholder alpha/beta arrays를 변경하며 이 thresholds는 바꾸지 않는다.
따라서 현재 source에서 threshold identity 자체는 source inspection으로
닫혔다. 그러나 density normalization에는 별도의 차이가 있다.
model(stage)는 저장될 \(n_{\rm He}\)를 binary64 곱셈
\({\rm fl}(n_{\rm H}f)\)으로 만들고, ft03_interval은 그 저장된 두 density
leaf를 정확한 실수 상수로 취해 \(\widehat f=n_{\rm He}^{\rm stored}/
n_{\rm H}^{\rm stored}\)를 구성한다. 일반적으로
\[
\delta f=f-\widehat f\ne0,\qquad
J_{\rm norm}(g)=\delta f\left[
\chi_{\rm HeI}F_0^{(y_1)}(g)
+(\chi_{\rm HeI}+\chi_{\rm HeII})F_0^{(y_2)}(g)\right].
\tag{21a}
\]
원본 photo/energy row는 stage \(f\)를 쓰므로, 이 coefficient graph에서의
정확한 nonphoto row는
\[
\boxed{Q_0(g)=-L_{\rm esc}(g)-2Hw+J_{\rm norm}(g).}
\tag{21b}
\]
식 (21b)는 \(\ell_f-\ell_{\widehat f}
=(0,\delta f\chi_{\rm HeI},\delta f(\chi_{\rm HeI}+\chi_{\rm HeII}),0)\)
를 \(F_0\)에 곱해 바로 얻는다. \(J_{\rm norm}\)은 원래 물리 model에
새 process를 추가한 것이 아니라 현 source coefficient graph의 서로
다른 normalization을 드러낸 잔차다. [E-SRC02, E-SRC06, E-SRC07, E-SRC09]

여기서 source-exact는 interval source의 저장된 binary64 leaves를
정확한 실수로 올린 coefficient graph에 대한 뜻이다. Primary f64
event evaluator의 곱셈 \(n_{\rm H}\epsilon_{\rm eV}\), event sum,
나눗셈 및 그 evaluation order에는 별도의 반올림이 있다. 식 (21b)는
그 계산들의 bitwise equality나 error-free summation을 주장하지 않는다.

회수한 archived scalar density와 다음 step의 제안 density leaf에 대해
Python binary64 곱셈 뒤 Fraction 비율을 취한 점검은 다음과 같다.
이는 endpoint/root 실행이 아니며 실제 \(J_{\rm norm}\) 값이나 trajectory
error를 계산하지 않는다.

| Density leaf | \(f-\widehat f\), 표시용 근삿값 |
|---|---:|
| Archived clock의 density | \(3.92133772618918\times10^{-18}\) |
| 제안 half endpoint의 density | \(7.325827815283162\times10^{-18}\) |
| 제안 full endpoint의 density | \(3.8057835851302354\times10^{-19}\) |

모든 차이는 exact Fraction 비교에서 비영이다. 정확한 유리수와 hex leaves는
CLAIMS_ENERGY.json의 correction_history에 보존한다. 독립 source 담당도
동일한 세 유리수와 correction 부호를 확인했다. [E-SRC10] 차이가 작다는 사실을
zero equality의 근거로 쓰지 않는다. Source의 density construction,
photo normalization 또는 kernel을 일괄 변경하는 수정은 이 결과에 포함되지
않는다. 실제 source-bound energy exporter는 \(Q_0\) 자체 또는
식 (21b)의 \(J_{\rm norm}\)을 포함하는 형태를 써야 한다.

Escaped ledger \(\zeta\)와 endpoint thermal work increment를
\[
\zeta-\zeta_0=dL_{\rm esc}(g),\qquad
\Delta{\cal W}_{\rm th}=2Hd\,w
\]
로 보존하면 현재 coefficient graph에 대한 식 (19)는
\[
\boxed{
e+\sum_j E_jP_j+\zeta+\Delta{\cal W}_{\rm th}
=e_0+\sum_jE_jN_j+\zeta_0+dJ_{\rm norm}(g).}
\tag{22}
\]
이는 fixed endpoint BE stage에서의 항등식이다. 더 넓은 nonphoto model에
외부 heating 또는 radiation-reservoir exchange \(Q_{\rm ext}\)가 실제
존재하면
\(Q_0=-L_{\rm esc}-2Hw+J_{\rm norm}+Q_{\rm ext}\)로 바꾸고 식 (22)의 우변에
\(dQ_{\rm ext}\)를 남긴다. 현재 source에 없는 항을 새로 추가하라는
지시가 아니라 모델 변경 시 누락을 막는 명시적 일반형이다.

### 5.2 Source ordering과 guard의 적용 범위

식 (19), (22)의 incoming photon은 transport 전 stock이 아니라
실제 BE 직전의 \(N\)이다. Fixed source law가
\[
N=R\,p_{\rm old}+d\,b B
\tag{23}
\]
라면 remap과 birth를 이미 한 번 적용한 것이다. Gas RHS에 같은 birth를
다시 더하지 않는다. \(\sum E_jN_j\)와 \(\sum E_jp_{{\rm old},j}\)의
차이는 birth, redshift/remap 및 boundary/guard ledger에서 따로 닫아야 한다.
Active quotient의 energy를 full photon array와 동일시할 수 없다.
Noninteracting guard는 이 BE stage 동안 일정하더라도 stage 사이의
export/import와 그 derivatives는 보존되어야 한다.

## 6. \(U,V,W\)에 대한 미분 잔차 항등식

\[
U=g_a,\quad V=g_b,\quad W=g_{ab},\qquad (a,b)=(\lambda,b).
\]
\(g_0,N\)은 incoming family의 모든 derivative를 유지한다.
Transformation은 상수이므로
\[
\xi_a=SU,\quad \xi_b=SV,\quad \xi_{ab}=SW;
\qquad e_a=\ell U,\ e_b=\ell V,\ e_{ab}=\ell W .
\tag{24}
\]
특히 \(e_{ab}\)에는 별도 coordinate-Hessian 항이 없다.

\[
\kappa_{j,a}=\alpha_j^{\mathsf T}U,\quad
\kappa_{j,b}=\alpha_j^{\mathsf T}V,\quad
\kappa_{j,ab}=\alpha_j^{\mathsf T}W
\tag{25}
\]
를 쓰면, photon derivatives는 \(N_j\)로 나누지 않고
\[
P_{j,a}=\frac{N_{j,a}-dP_j\kappa_{j,a}}{D_j},\qquad
P_{j,b}=\frac{N_{j,b}-dP_j\kappa_{j,b}}{D_j},
\tag{26}
\]
\[
\boxed{
P_{j,ab}
=\frac{N_{j,ab}-dP_j\kappa_{j,ab}
-dP_{j,a}\kappa_{j,b}-dP_{j,b}\kappa_{j,a}}{D_j}.}
\tag{27}
\]
이는 PHYS04의 full denominator mixed derivative와 같은 식이다.
\(D_j>0\)이면 \(N_j=0\)에서도 정칙이다. [E-SRC01]

Exact root family에서 식 (18)을 미분하면
\[
e_a-e_{0,a}+\sum_jE_j(P_{j,a}-N_{j,a})
=d\,Q_{0,g}U ,
\tag{28}
\]
\[
e_b-e_{0,b}+\sum_jE_j(P_{j,b}-N_{j,b})
=d\,Q_{0,g}V ,
\tag{29}
\]
\[
\boxed{
e_{ab}-e_{0,ab}+\sum_jE_j(P_{j,ab}-N_{j,ab})
=d\{Q_{0,g}W+Q_{0,gg}[U,V]\}.}
\tag{30}
\]
Nonzero candidate residual의 경우에는 각 식의 좌변에서 우변을 뺀 값이
\(\ell\partial_aG+\sum E_j\partial_aR_{\gamma j}\) 또는 대응하는
\(b,ab\) residual과 같다. 검증기는 결과를 강제로 0으로 설정하는 대신
이 양변을 독립적으로 구성해 비교할 수 있다.

식 (21b)의 escape/work/normalization ledger를 포함하면 고정 \(H,d,f,\widehat f\)에서
\[
e_a-e_{0,a}+\sum_jE_j(P_{j,a}-N_{j,a})
+(\zeta_a-\zeta_{0,a})+2Hd\,w_a=dJ_{{\rm norm},g}U,
\tag{31}
\]
\[
e_{ab}-e_{0,ab}+\sum_jE_j(P_{j,ab}-N_{j,ab})
+(\zeta_{ab}-\zeta_{0,ab})+2Hd\,w_{ab}
=d\{J_{{\rm norm},g}W+J_{{\rm norm},gg}[U,V]\}.
\tag{32}
\]
\(b\) first derivative도 식 (31)과 같다. 예를 들어
\(\zeta_{ab}-\zeta_{0,ab}
=d\{L_{{\rm esc},g}W+L_{{\rm esc},gg}[U,V]\}\)를 반드시 포함한다.
실제 \(Q_{\rm ext}\)가 있으면 우변에 각각 그 total first/mixed
derivative에 \(d\)를 곱한 값을 더한다. \(\delta f=0\)인 일관된 real
coefficient graph에서는 \(J_{\rm norm}\)과 그 derivatives가 0으로 환원된다.

### 6.1 Reduced photo의 total mixed forcing

식 (13)만으로는 식 (30)을 구현할 수 없다. Incoming photons도
parameter-dependent이면
\[
\begin{aligned}
\partial_{ab}\Phi
=\sum_j E_j\bigg[
&\frac{N_j\,\alpha_j^{\mathsf T}W}{D_j^2}
-\frac{2dN_j
(\alpha_j^{\mathsf T}U)(\alpha_j^{\mathsf T}V)}{D_j^3}\\
&+\frac{N_{j,a}\,\alpha_j^{\mathsf T}V
       +N_{j,b}\,\alpha_j^{\mathsf T}U}{D_j^2}
+\frac{N_{j,ab}\kappa_j}{D_j}\bigg].
\end{aligned}
\tag{33}
\]
두 번째 항만이 fixed-\(N\) gas Hessian의 contraction이다.
첫 항은 unknown \(W\)의 Jacobian 부분이며, 나머지 항은 signed
old-photon/birth derivatives를 운반한다.

Residual \(A=G_g\)의 mixed equation에서 HH parameter/gas forcing
\(H_{{\rm HH},g}V\), \(\lambda H_{{\rm HH},gg}[U,V]\)는 full vector로
유지한다. 다만 \(\ell\) row로 projection하면 식 (7) 때문에 이
**explicit** HH contribution들이 소거된다. Species equations를 통해
정해지는 \(U,V,W\), 그에 따른 opacity, temperature 및 nonphoto
cooling의 변화는 소거되지 않는다.

### 6.2 Explicit HH energy forcing 0의 잘못된 확대에 대한 반례

다음은 실제 FT03/LCS endpoint가 아닌 정확한 symbolic counterexample다.
Helium photo coupling을 끈 H-only subblock, \(F_0=0\), 상수
\(q_*>0\), 한 packet \(E>\chi_{\rm H}\),
\(\kappa=A_*(1-x)\), \(A_*>0\), \(N=bN_*\), \(N_*>0\)를 취한다.
Common incoming gas를 고정하고 \(b=0\)에서 \(b\ge0\) 방향으로 미분한다.
충분히 작은 \(\lambda\)에서
\[
x=x_0+d\lambda q_*,\quad
w=w_0-d\lambda\chi_{\rm H}q_*,\quad
D_0=1+dA_*(1-x_0-d\lambda q_*)>0 .
\]
Gas simplex와 \(w>0\)를 만족하는 범위로 제한한다.
Energy identity \(e=e_0+E(N-P)\)에 의해
\[
e_b\big|_{b=0}=EN_*\left(1-\frac1{D_0}\right),
\qquad
\boxed{
e_{\lambda b}\big|_{b=0}
=-\frac{EN_*d^2A_*q_*}{D_0^2}\ne0.}
\tag{34}
\]
HH가 neutral abundance를 바꾸어 다음 photon의 흡수 비율을 바꾼 결과다.
이는 \(SH_{\rm HH}\)의 energy row가 0이어도 matter mixed energy
response가 0일 필요가 없음을 보인다. 실제 \(q(T)\), nonphoto terms
또는 actual finite rectangle을 이 fixture로 대체하지 않는다.

Escape/work까지 합친 **전체 stage energy**의 혼합 derivative가 0이
되는 특별한 경우는 존재한다. 공통 초기 상태와 affine-in-\(b\)
numerator 때문에 \(e_{0,ab}=\zeta_{0,ab}=N_{ab}=0\)이고, 식 (32)의
premises와 \(J_{{\rm norm},ab}=0\)가 모두 성립하면 그 선형 energy
combination은 0이다.
그렇더라도 \(e_{ab},P_{ab},\zeta_{ab},w_{ab}\) 각각은 일반적으로 0이
아니다. 반례 (34)에서는 photon energy의 mixed derivative가 matter
energy의 mixed derivative를 상쇄한다.

## 7. Coordinate Jacobian, Hessian 및 preconditioner 계약

Reduced residual을
\[
\widetilde G(\xi;\xi_0,N,\lambda)
=S\,G(Q\xi;Q\xi_0,N,\lambda)
\]
로 정의한다. 동일한 physical point에서
\[
\widetilde A=S A Q,\qquad
\widetilde G_{\xi\xi}[u,v]=S G_{gg}[Qu,Qv].
\tag{35}
\]
Full-vector RHS도 같은 변환 법칙을 따른다. 각 scalar component의
input Hessian에만 \(Q^{\mathsf T}(\cdot)Q\)를 적용한 뒤 output row의
\(S\) 조합을 누락해서는 안 된다. Incoming-stock cross block은
\[
\widetilde F_{\xi N}[u,n]=S F_{gN}[Qu,n],\qquad
\widetilde F_{NN}=S F_{NN}=0 .
\tag{36}
\]
이는 새 Hessian callback을 검증할 수 있는 exact change-of-coordinate
계약이다. Matrix determinant와 singularity는
\(\det\widetilde A=\det A\)로 보존되지만, elementwise signs 또는
일반적인 unweighted matrix norm은 보존되지 않는다.

원본 source-bound centre preconditioner \(C\)가 주어졌다면
\[
\widetilde C=S C Q,\qquad
I-\widetilde C\widetilde A=S(I-CA)Q.
\tag{37}
\]
원본 \(C\)를 값 변경 없이 새 좌표에 재사용하면 다른 연산자다.
원본 centre, source identity, \(S,Q\), units와 scales를 새 binding에
기록해야 한다. 이 변환이 conditioning 또는 Krawczyk contraction
상수를 자동 개선한다는 주장은 하지 않는다.

정확한 transported norm
\(\|\xi\|_{\xi}=\|Q\xi\|_g\)에서는 대응하는 operator bound가 같다.
그러나 gas box \(X_g\)의 정확한 image \(SX_g\)는 일반적으로
axis-aligned box가 아닌 parallelepiped다. 이를 새 interval box로
감싸면 dependency/wrapping이 증가할 수 있다. 기존 strict inclusion을
그대로 상속하려면 정확한 set transformation을 사용해야 하고, 새
coordinate box를 사용한다면 그 box에서 physical domain, root inclusion,
full interval Jacobian 및 contraction을 새로 평가해야 한다.

\(f\) 또는 \(\chi\)가 parameter-dependent라면 \(S\)도 변하므로
\[
\xi_a=SU+S_a g,\qquad
\xi_{ab}=SW+S_aV+S_bU+S_{ab}g
\tag{38}
\]
를 써야 한다. 식 (24), (35)–(37)의 현재 상수-coordinate 계약은 그
확장을 자동으로 포함하지 않는다.

## 8. Domain, zero stock 및 한쪽 tangent

Physical primal domain은
\[
0\le x\le1,\quad y_1,y_2\ge0,\quad y_1+y_2\le1,\quad
w=e-\beta^{\mathsf T}(x,y_1,y_2)^{\mathsf T}>0,\quad N_j\ge0
\tag{39}
\]
이며 source의 온도와 finite/normal-arithmetic guards를 추가한다.
\(\sigma_{aj}\ge0\) 및 고정 branch이면 \(\kappa_j\ge0\)이고 \(D_j\ge1\).
수학적 식은 더 넓은 \(D_j>0\) 영역에서 정칙이지만, 그 사실이 negative
abundance나 negative primal photons의 실제 실행을 허용하지 않는다.

Signed \(U,V,W,N_a,N_b,N_{ab}\)는 clip하지 않는다. 이들은 stock이
아니라 미분 계수다. 다만 formal jet과 physical parameter family의
실현 가능성은 구분한다. 양방향 열린 parameter 근방에서 매끄러운
\(N\ge0\)가 interior point에서 \(N=0\)이면 그 점의 모든 first
derivative는 0이다. 반면 boundary \(b=0\), \(b\ge0\)의
\(N=bN_*\)에는 \(N_b=N_*>0\)인 한쪽 derivative가 존재한다.
이는 식 (34)에서 사용한 경우다. Arbitrary signed jet가 계산 가능하다는
것만으로 physical rectangle 전체에서 그 jet가 실현되었다고 판정하지 않는다.

Fixed-\(N\) photo gas Hessian은 \(N_j=0\)일 때 그 column에서 0이다.
그러나 식 (33)의 \(N_{j,a}\alpha_j^{\mathsf T}V\),
\(N_{j,b}\alpha_j^{\mathsf T}U\), \(N_{j,ab}\kappa_j\) 항은
primal stock이 0이어도 남을 수 있다. 모든 photo derivative가 없어지는
충분조건은 그 incoming family에서
\[
N=N_a=N_b=N_{ab}=0
\]
인 것이다. Old stock \(p_{\rm old}=0\)만으로는 이 조건을 얻지 못한다.
식 (23)의 fixed source-order family에서
\[
N_a=R p_{{\rm old},a},\quad
N_b=R p_{{\rm old},b}+dB,\quad
N_{ab}=R p_{{\rm old},ab}
\tag{40}
\]
를 유지한다. Active quotient 밖의 guard/inactive derivatives도 같은
incoming provenance에 남겨야 한다.

## 9. 극한, 검증 계약과 남은 물리 전제

다음 점검들은 위 유도에서 직접 따른다.

| 점검 | 결과 |
|---|---|
| \(d\to0^+\), fixed \(N,\kappa\) | \(\Phi\to\sum EN\kappa\), \(\Phi_{gg}\to0\). Unsaturated photo energy는 affine이다. |
| \(\sigma_{aj}=0\) for all absorbers | \(\kappa_j=\alpha_j=K_j=0\), 해당 packet의 gas contribution과 그 gas derivatives가 0이다. |
| \(N_j=0\), fixed-\(N\) differentiation | 해당 photo energy와 gas Hessian이 0이며, stock cross derivatives의 소거는 별도 조건이다. |
| \(d\kappa_j\gg1\), \(\kappa_j>0\) | \(\Phi_j\to E_jN_j/d\). Absorbed energy increment \(d\Phi_j\)는 \(E_jN_j\)로 포화한다. |
| \(\kappa_j=0\), \(\alpha_j\ne0\) | Primal absorption이 0이어도 boundary에서 gas curvature가 0일 필요는 없다. |
| \(f\to0\) | 현재 helium-fraction chart의 \(1/f\) 때문에 직접 대입하지 않는다. H-only 모델은 별도 chart/normalization으로 정의한다. |
| \(H=0,\ L_{\rm esc}=0,\ J_{\rm norm}=0\) | BE stage에서 \(e+\sum EP\)가 incoming \(e_0+\sum EN\)와 같다. |
| Nonzero root/tangent residual | 에너지 mismatch는 식 (18), (28)–(30)의 residual 조합으로 남기며 exact conservation으로 승격하지 않는다. |

경량 exact checker가 검증할 대상은 (i) 전체 H/He stoichiometry의
\(\ell K=E\kappa\), (ii) full HH energy first/second cancellation,
(iii) 식 (13)의 Gram Hessian과 energy-coordinate congruence,
(iv) 식 (18) 및 그 value/a/b/ab 잔차 identity,
(v) nonzero old-stock 및 zero-primal/signed-tangent slots,
(vi) 식 (35)–(37)의 coordinate transformation이다. 이러한 checker는
source arithmetic reference를 확인할 수 있지만 actual physical
endpoint를 생성하거나 uniform inverse를 인증하지 않는다.

현재 문서의 실제 수행은 source reading, 직접 유도 및 세 density leaf의
normalization을 대상으로 한 1회 exact scalar arithmetic 점검이다.
Native endpoint, nonlinear BE root, IVP, atomic integral, 과거 scientific
suite의 추가 실행은 모두 0이다. 별도 checker 결과는 owner가 증거
파일에 바인딩한 뒤에만 numerically checked 또는
implementation-verified로 병기할 수 있다.

실제 finite mixed response를 결정하려면 여전히 다음 자료가 필요하다.

1. 같은 initial gas/photon/guard/ledger family, 고정 \((\lambda,b)\)
   rectangle 및 단계별 source/density/clock identity.
2. Full FT03/LCS nonphoto/HH Hessian과 gas–stock cross derivative를
   포함한 actual source-bound callbacks.
3. 그 rectangle 전체의 physical gas domain, \(D_j>0\), common regular
   root family, strict inclusion 및 uniform inverse/contraction 증거.
4. 실제 incoming \(g_0,N,U_0,V_0,W_0,N_a,N_b,N_{ab}\) enclosures.
5. Escape/thermal work와 transport/guard energy의 source-bound ledger;
   현재 확인한 FT03 threshold/binding identity, 두 helium density ratio 및
   필요한 \(J_{\rm norm}\) residual을 실제 callback의 source identity와
   함께 보존하는 계약.

그 전제 없이 concavity만으로 \(W\), finite four-corner interaction,
full-versus-two-half gas error, continuous-time error 또는 production
admission을 채울 수 없다. 이 문서는 그 미결 값을 숫자 0으로 바꾸지 않는다.

## 근거 포인터와 읽은 범위

아래 SHA-256은 읽은 파일의 identity다. 과학적 정리의 증거는 본문의
명시적 유도 및 그 source contract이며, hash 자체가 정리를 증명하지 않는다.
이 문서에서는 외부 literature claim을 추가하지 않았다.

| ID | 근거와 읽은 범위 | SHA-256 |
|---|---|---|
| E-SRC01 | PHYS04 IMPLICIT_MIXED_THEORY_KO.md 전체; src/implicit_mixed.py 전체 | 92e983d35e9688304fd9269d689c2117b7d0c81b95ce67d24fee789ca686cf00 ; ad8043ed6ca07ca1e2e8f8b596481917d34b65084ad64e8f8351ce85a74bc88f |
| E-SRC02 | PHYS04 inputs/source_survey/reused_phys03/source/coupled_primary.rs: state/units/validity, opacity/photo/energy, interval_rhs의 관련 부분 | 6386333c3b9478f7fc486c11adf941a35f811595fa42e6f4653cf0dcdac0706e |
| E-SRC03 | PHYS05 CONTRACT.md 전체; SOURCE_PINS.json의 canonical commit 4ea15a082f9358e28af35e30a392585f4e4383c9 identity | 2b431ce03df7d5ee167024bfc74cf3d5fa3350b8e5f0a54a06f7f8c446a116f3 |
| E-SRC04 | PHYS04 source snapshot hh_primary_extension.rs의 q(T), HH gas/thermal pair, guards, conservative energy update 부분 | 8653f00034189b024759b39ca57d05723430988eaa08047387d12fe8381a676d |
| E-SRC05 | PHYS04 reused_phys03/source/atomic_provider.rs의 cross_section 전체와 provenance header | b0b572d3940a7a1f740e09d5f43c60236ec61511e8bdbcc68e60395ec7e107d3 |
| E-SRC06 | PHYS04 source snapshot ft03_controlled.rs의 controlled model 초기화 및 ft03_rhs 전체 | 61e11471482bb49d99e5d0eb79504d3f67538fbe6361653a0462d1abb0b672db |
| E-SRC07 | 현재 NCP candidate/src/hhe_events.rs의 controlled_fixture 및 candidate/src/coupled_primary.rs의 CHI, ft03_controlled.rs의 controlled 초기화 | c100b08e034089c2d67b2102769ccdd51f1d29a2f388d6bb2dfe7984af93b290 ; 2c528f1e7dcf44622374f8421a192f75ce8cff8b1c311bbff508f9ed863d7dcc |
| E-SRC08 | ARCHIVED_COMMON_SEED_POINT_INPUT.json 전체; 추출된 33-node energy 범위와 provider zero branch만 재사용 | 1f462e7fa7c1d4251c5004194c42b0e471fe5c42303962f1a40d5d5062f1923d |
| E-SRC09 | 현재 NCP candidate/src/ft03_interval.rs의 density ratio, temperature, per-H event 및 He fraction normalization | 886580a810b8ec29c8f0b6199c0e35d82fde1f46d984a5f8f1da304326a42a42 |
| E-SRC10 | 독립 source 담당의 SOURCE_DENSITY_LEAF_CORRECTION.json 전체; 세 density의 exact Fraction 및 normalization 부호 확인 | 259d91f3153dd97b2f0ae50bb566e9d333aaff19af44f96b6c2714fd21a7471d |

E-SRC04–06의 canonical source commit은
569b04cd71e45756e0fd476aef6643bd9434f4fa다.
E-SRC02는 PHYS04가 보존한 PHYS03 snapshot이며 원 source commit
0bf109607e51873b6cf44ed8d3eb8f719388fb9b, Git blob
99dbc26611852169679b66ef4c74c876dd7add01에 바인딩되어 있다.
PHYS04 publication은 36b479d509d28aade8db6c8df6a1f8e9edf1a677이다.
최신 owner code에 적용할 때는 이 immutable baseline과 현재 변경분을
구분한다.

E-SRC07은 현재 NCP source commit
4b9231a0eff113701e7178ad98624233f387dd15의
research/r31ao_unequal_ladder/ncp_phys04_local_20261011_v2/candidate/src
아래 파일이다. E-SRC08의 원 binary checkpoint SHA-256은
678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b다.
이 입력 추출물은 Python source diagnostic과 archived bytes를 구분하여
보존하며, 새 native decode/root 또는 native provider 실행을 뜻하지 않는다.
