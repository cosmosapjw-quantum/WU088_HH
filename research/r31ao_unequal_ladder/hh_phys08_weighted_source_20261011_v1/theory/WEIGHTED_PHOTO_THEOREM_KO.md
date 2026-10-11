# PHYS08 — 전체 광반응률을 이용한 온도 부호 정리

이 문서는 PHYS07 NCP의 보존된 native-source export에서 `SOURCE_DIRECTIONAL_WITNESS=OPEN`으로 남은 충분조건을 보완한다. 새 source 호출이나 implicit solve를 수행하지 않고, 기존 signed interval을 보존하는 합계 수준의 정리를 유도한다. 정리의 증거 상태는 **derived**다. Root가 보존된 export로 수행한 PHYS08 exact-rational 후처리는 **numerically checked / implementation-verified**이고, 두 stage의 총 photo \(P_N\)와 birth 방향 \(P_M\) 모두에서 엄밀한 냉각·상호 억제 조건을 충족했다. 과거 PHYS07 NCP 수치는 별도로 **archived implementation evidence**라고 표시한다. 최종 채택은 상위 패키지의 독립 판정을 따른다.

## 1. 결론과 적용 범위

광반응 때문에 온도가 내려가는 정확한 조건은 모든 활성 에너지 노드가 개별적으로 낮은 잉여에너지를 갖는다는 조건보다 약하다. 온도는 반응률로 가중한 **전체 열에너지 증가율과 전체 입자 수 증가율**의 차이로 정해진다. 임의의 signed source 방향 (v=(v_x,v_1,v_2,v_w))에 대해

\[
\boxed{\quad
DT_g[v]=\frac{C}{p^2}\,\mathcal B_g(v),\qquad
\mathcal B_g(v)=p v_w-w\{v_x+\widehat f v_1+2\widehat f v_2\}.
\quad} \tag{1}
\]

따라서 동일 domain을 포함하는 구간 확장으로 \(\sup[\mathcal B_g(v)]<0\)를 보이면, 모든 원 signed tail을 유지하면서 온도 방향미분의 엄밀한 음수를 얻는다. 이 조건은 node32의 작은 양의 value tail 또는 양·음의 derivative tail을 지울 필요가 없다.

PHYS07 NCP의 `DIRECTIONAL_VECTORS.json`에는 이미 \(v=P_M\)에 대해 두 stage 모두 음의 `DT_P_M` 포함값이 저장되어 있다. 과거 `OPEN`은 다른 per-node 충분조건을 함께 요구한 집계 predicate의 결과다. PHYS08 후처리에서는 같은 33×3 rate Jets에서 \(P_N,P_M\)를 따로 합산하고 식 (1)의 엄밀한 음수를 확인했다. 과거 판정과 파일은 그대로 보존하고, 이번 가중 정리와 새 근거 상태를 별도 산출물로 추가한다.

이 문서의 부호는 **고정 계수 실수 source의 방향미분**에 대한 것이다. Actual native nonlinear root, root authority, \(U,V,W\), 유한 상호작용 \(I\), full/two-half defect 또는 시간·continuum remainder에 대한 새 주장은 없다.

## 2. 입력, 좌표, 단위와 계수의 의미

상태 좌표는

\[
g=(x,y_1,y_2,w)
 =(x_{\rm HII},y_{\rm HeII},y_{\rm HeIII},w[\mathrm{eV/H}])
\]

이며, 과거 COMMON state를 보존한 첫 stage를 다룬다. 매개변수는 \(\lambda,b\in[0,1]\)이고, \(\lambda\)는 앞으로 적용할 HH source의 세기, \(b\)는 앞으로 추가하는 광자 birth의 세기다. 이미 COMMON에 들어 있는 과거 HH 이력과 primal compensation은 변경하지 않는다. Full과 first-half는 각각 같은 COMMON에서 시작하며, first-half는 carried second-half를 뜻하지 않는다.

실제 domain \(X_{\rm native}\)의 endpoint는 NCP의 `C2_DOMAIN.json` 및 frozen source contract에 있는 binary64 bit pattern이다. 이 domain은 표시상

\[
[0.90,0.93]\times[0.29,0.31]\times[0.59,0.61]\times[13,14]
\]

보다 바깥으로 확장되어 있다. PHYS07 Python reference의 exact-decimal box와 byte identity를 주장하지 않는다. 연산 입력에는 저장된 `lo_bits`, `hi_bits`를 사용해야 하며, 표시된 decimal을 다시 반올림하여 원 endpoint를 대체하지 않는다.

Stage의 저장 상수들을 실수에 정확히 올려서

\[
f=\operatorname{exact}(f_{\rm He}^{\rm stage}),\qquad
\widehat f=
\frac{\operatorname{exact}(n_{\rm He}^{\rm stored})}
     {\operatorname{exact}(n_{\rm H}^{\rm stored})},\qquad
C=\frac{2\operatorname{exact}(e_{\rm V,erg})}{3\operatorname{exact}(k_B)}
\tag{2}
\]

로 둔다. \(C\)의 단위는 K/eV다. 두 helium 비율은 보통 매우 가깝지만 \(f=\widehat f\)라는 정확한 등식을 추가하지 않는다. Source의 온도는

\[
p=1+\widehat f+x+\widehat f(y_1+2y_2),\qquad
T=C\frac{w}{p}. \tag{3}
\]

\(p\)는 수소 핵당 총 입자 수이므로 무차원이다. Source vector의 앞 세 성분은 \(\mathrm{s}^{-1}\), 네 번째는 \(\mathrm{eV/H/s}\)다. 따라서 \(DT[v]\)의 단위는 K/s다. 이 문제에는 metric tensor가 직접 나타나지 않으며, 프로젝트의 기본 signature \((-,+,+,+)\)와 충돌하지 않는다. \(c\)와 \(k_B\)를 1로 두지 않는다.

### 2.1 Incoming stock과 birth 방향의 구분

고정된 transport·angular 계수와 원 COMMON 계수 벡터를 \(\alpha\)로 묶으면, 실제 한 coefficient family의 incoming은

\[
N_j(g,\lambda,b;\alpha)=\overline N_j(\alpha)+bM_j(\alpha),\qquad
M_j=\partial_b N_j. \tag{4}
\]

해당 첫 stage에서는 \(\overline N_j,M_j\)가 gas와 \(\lambda\)에 의존하지 않는다. 원 transport 코드는 이미 계산한 remap 이후 노드24에 birth를 더한다. Fixed-real birth의 구조적 support가 제한된다는 사실과, 저장된 interval의 33개 노드에 작은 signed tail이 있다는 사실은 양립한다. 이번 가중 계산은 이 구조적 support로 원 배열을 축소하는 방식에 의존하지 않는다.

총 birth amount의 scalar leaf는

\[
M_* =\operatorname{exact}(\operatorname{fl}(d S_*)), \tag{5}
\]

이고, 각 \(M_j\)에는 실제 source angular weight와 합산의 포함 의미가 들어 있다. \(M_j\)를 반올림 전의 정확한 \(dS_*\) 또는 PHYS07 reference의 별도 direction sum으로 대체하지 않는다. 필요하면 \(B_{d,j}=M_j/\operatorname{exact}(d)\)를 정의할 수 있다. \(M_j\)는 photons/H, \(B_{d,j}\)는 photons/H/s다.

이하 \(P_N\)은 현재 전체 incoming으로 만든 photo source, \(P_M=\partial_b P_N\)은 birth 매개변수의 source 방향이다. \(P_M\)의 단위도 \(\mathrm{s}^{-1}\) 또는 \(\mathrm{eV/H/s}\)이며, 잔차 미분에서만

\[
G_b=-dP_M
\]

라는 stage 시간 인자가 붙는다. \(P_M\)를 \(P_N\) 또는 \(dP_M\)로 읽으면 안 된다.

## 3. 일반 signed-vector 온도 정리

### 정리 1

\(p>0\), \(w>0\), \(\widehat f,C\)가 상태·매개변수에 대해 고정된 양수라고 하자. \(T\)가 식 (3)으로 정의되면 임의의 signed 방향 \(v\)에 식 (1)이 성립한다. 어떤 집합 \(\mathcal D\) 전체에서 \(v(g,\theta)\)와 \(g\)를 포함하는 구간 입력으로 \(\mathcal B_g(v)\)의 상계가 엄밀한 음수이면, \(DT_g[v]<0\)가 \(\mathcal D\) 전체에서 성립한다.

**증명.** \(p\)는 gas의 affine 함수이므로

\[
Dp[v]=v_x+\widehat f v_1+2\widehat f v_2.
\]

양의 \(p\)에 quotient rule을 적용하면

\[
DT[v]=C\left(\frac{v_w}{p}-\frac{w}{p^2}Dp[v]\right)
      =\frac{C}{p^2}\{pv_w-wDp[v]\}.
\]

\(C/p^2>0\)이므로 부호는 \(\mathcal B\)와 같다. 포함 연산의 결과가 모든 입력의 정확한 실수 값을 포함하면, 상계의 엄밀한 음수는 그 모든 값에 대한 음수를 보증한다. 성분 사이의 dependence를 버린 직사각형 포함은 폭을 넓힐 수 있지만, 유효한 포함을 유지하는 한 엄밀한 음수 판정을 무효화하지 않는다. □

같은 정리를 다음 형태로 평가할 수도 있다.

\[
\nabla_gT=
\left(-\frac{T}{p},-\frac{\widehat fT}{p},
      -\frac{2\widehat fT}{p},\frac{T}{w}\right),
\qquad DT[v]=\nabla_gT\cdot v. \tag{6}
\]

저장된 `T_gradient`와 `P_M`의 네 성분을 이용하는 식 (6)은 새로운 source 값이나 초월함수 평가가 필요 없다. 식 (1)의 더 짧은 computational form과 식 (6)의 기존 export form은 같은 실수 항등식의 서로 다른 포함 표현이다. 두 구간의 단순 overlap은 독립적인 유효성 증명을 대신하지 않는다. 각 표현의 입력과 연산이 각각 같은 함수를 포함한다는 provenance가 먼저 있어야 한다.

## 4. 반응률 가중 형태와 per-node 조건의 한계

Photo 채널 \(a\in\{\mathrm{HI},\mathrm{HeI},\mathrm{HeII}\}\)의 고정 scalar leaf를

\[
\sigma_{ja}\ge0,\qquad
a_{ja}=\operatorname{exact}(\operatorname{fl}(E_j-\chi_a))
\]

로 둔다. \(a_{ja}\)는 source에서 이미 반올림된 heat leaf다. \(E_j-\chi_a\)를 지금 다른 precision으로 다시 계산해 대체하지 않는다. 실제 source는

\[
\ell_{\rm HI}=1-x,\quad
\ell_{\rm HeI}=f(1-y_1-y_2),\quad
\ell_{\rm HeII}=fy_1,
\]

\[
\kappa_j=c n_H\sum_a\ell_a\sigma_{ja},\quad
D_j=1+d\kappa_j,\quad
R_{ja}[Z]=c n_H\ell_a\sigma_{ja}\frac{Z_j}{D_j}. \tag{7}
\]

여기서 \(Z=N\) 또는 \(Z=M\)이고, 후자는 incoming이 gas와 독립인 식 (4)의 방향을 뜻한다. \(c\)는 cm/s, \(n_H\)는 \(\mathrm{cm}^{-3}\), \(\sigma\)는 \(\mathrm{cm}^2\), \(d\)는 s이므로 \(\kappa\)는 \(\mathrm{s}^{-1}\), \(D\)는 무차원이다. 식 (7)의 scalar coefficient는 각각 보존된 binary64 leaf의 정확한 실수 값이며, \(c n_H\sigma\)를 임의의 새 scalar binary64 곱 하나로 먼저 반올림하지 않는다.

채널별 합계를 \(r_a=\sum_jR_{ja}[Z]\), \(Q_Z=\sum_{ja}a_{ja}R_{ja}[Z]\)라 쓰면

\[
P_Z=\left(r_{\rm HI},\frac{r_{\rm HeI}-r_{\rm HeII}}{f},
                  \frac{r_{\rm HeII}}{f},Q_Z\right),
\]

\[
Dp[P_Z]=r_{\rm HI}
   +\frac{\widehat f}{f}(r_{\rm HeI}+r_{\rm HeII}). \tag{8}
\]

따라서 일반 3채널의 정확한 가중 조건은

\[
\boxed{\quad
\mathcal B(P_Z)
=\sum_{j,a}R_{ja}[Z]\{p a_{ja}-w\eta_a\}<0,
\quad
\eta=(1,\widehat f/f,\widehat f/f).
\quad} \tag{9}
\]

Helium 반응의 입자 수 증가 인자에 \(\widehat f/f\)를 남기는 이유는 source의 ion fraction 정규화에는 \(f\), 온도에는 저장 density ratio \(\widehat f\)가 쓰이기 때문이다. 정확히 같다고 가정하여 지울 수 없다.

### 4.1 현재 HI-only fixed-leaf family

현재 native source의 고정 grid는 10–20 eV이며, 보존된 모든 HeI·HeII cross-section leaf는 정확한 0이다. 이 leaf identity 아래 실수 식의 \(P_Z\)는

\[
P_Z=(R_Z,0,0,Q_Z),\quad
R_Z=\sum_jr_j[Z],\quad Q_Z=\sum_ja_jr_j[Z],
\quad r_j[Z]=A_j\frac{uZ_j}{D_j},
\quad A_j=cn_H\sigma_{j\rm HI},\quad u=1-x.
\tag{10}
\]

식 (9)는

\[
\mathcal B(P_Z)=pQ_Z-wR_Z
=\sum_jr_j[Z](pa_j-w) \tag{11}
\]

가 된다. \(R_Z>0\)이면

\[
\bar a_Z=Q_Z/R_Z,\qquad
DT[P_Z]<0\iff\bar a_Z<w/p. \tag{12}
\]

모든 \(r_j\ge0\)인 physical value의 경우 \(\bar a\)는 보통 의미의 반응률 가중 평균이다. Signed derivative interval을 평가할 때는 개별 \(r_j\)가 음수인 값을 포함할 수 있으므로, 양수 weight의 convex average라는 해석을 추가하지 않는다. 식 (11)은 signed 값에도 그대로 성립하고, 식 (12)는 합계 \(R_Z>0\)를 확보한 경우에만 대수적 비율로 쓸 수 있다. 분모가 0을 포함하면 비율을 쓰지 않고 식 (11) 또는 네 성분의 식 (1)을 사용한다.

실제 구현 증거의 He 방향 성분에 \(\pm\)subnormal interval이 남아 있으면 그 배열을 정확한 0으로 고치지 않는다. Fixed-real identity는 별도 정리로 기록하고, 보존된 export의 강건한 부호 평가에는 식 (1)의 네 성분을 모두 넣는다. 이 방식은 소스의 algebraic zero와 구간 연산의 폭을 혼동하지 않는다.

### 4.2 높은 에너지 노드가 있다고 합계 부호가 바뀌지는 않는다

\(a_L<w/p<a_H\)인 두 채널을 생각하자. \(r_L=R_0>0\), \(r_H=\varepsilon R_0\), \(\varepsilon>0\)이면

\[
\mathcal B=R_0\{-L+\varepsilon H\},\quad
L=w-pa_L>0,\quad H=pa_H-w>0.
\]

따라서 \(0<\varepsilon<L/H\)이면 높은 에너지 채널이 실제로 존재하고 개별 \(pa_H<w\)를 위반해도 전체 \(DT[P]<0\)다. 반대로 \(\varepsilon>L/H\)이면 전체가 가열 방향이다. 이것은 논리적 반례이며 현재 입력의 수치 검산을 대신하지 않는다.

PHYS07 NCP의 node32에서는 `physical_incoming`의 상계가 양의 subnormal이고, 그 energy에서 \(a_{32}p-w\)가 일부 gas 영역에서 양수가 될 수 있다. 이 사실로부터 전체 \(\sum_jr_j(a_jp-w)\)의 부호를 추론할 수 없다. Node32를 포함한 전체 합의 상계를 실제 보존 interval로 계산해야 한다. Tail의 크기가 작다는 말만으로 삭제하거나 무시해서도 안 된다.

## 5. HH–photo 경쟁으로 이어지는 source 정리

HH source는

\[
H=qv_H,\quad v_H=(1,0,0,-\chi_H),\quad
q=n_Hu^2 k(T),\quad
k(T)=K T^{\eta}\exp(-T_*/T), \tag{13}
\]

이다. \(K\), \(\eta\), \(T_*\)는 현재 source literal의 exact binary64 lift이며, 특히 \(\eta=\operatorname{exact}(\operatorname{fl}(1.2))\), \(T_*=157800\) K를 유지한다. 여기서 \(T^{\eta}\)는 코드의 Kelvin 수치에 대한 fit이며 \(K\)는 그 convention을 포함한다. 새로운 차원 없는 온도 정규화를 넣지 않는다.

\(u>0\), \(T>0\)에서

\[
\nu(T)=\frac{T k'(T)}{k(T)}=\eta+\frac{T_*}{T}>0.
\]

임의의 gas 방향 \(v\)에 대해 product·chain rule로

\[
Dq[v]=q\left[-\frac{2v_x}{u}
             +\frac{\nu(T)}{T}DT[v]\right]. \tag{14}
\]

### 따름정리 1: photo에 의한 HH 억제

동일 family·domain에서 \(q>0\), \(u>0\), \((P_Z)_x>0\), \(DT[P_Z]<0\)이면

\[
(H_gP_Z)_x=Dq[P_Z]<0. \tag{15}
\]

이는 식 (14)의 두 항이 모두 엄밀한 음수이므로 따른다. 개별 노드의 thermal condition은 필요하지 않다. 첫 항은 중성 H의 감소, 두 번째 항은 온도 감소에 따른 HH 반응률의 감소를 나타낸다. 해당 충분조건은 일반 signed 4-vector 및 helium 성분이 있는 경우에도 식 (14)가 동일 source를 나타내면 성립한다.

\(DT[P_Z]<0\)도 식 (15)의 필요조건은 아니다. 양의 \(DT[P_Z]\)가 있어도 중성 감소 항이 더 클 수 있다. 이번에는 온도·이온화의 물리 해석이 직접 이어지는 가중 충분조건을 사용한다.

### 따름정리 2: HH에 의한 HI photo 억제

HI-only 식 (10)에서 \(Z_j\)가 gas에 독립이면

\[
\partial_xr_j[Z]
=-A_jZ_j\,\frac{D_j-dA_ju}{D_j^2}
=-\frac{A_jZ_j}{D_j^2},\qquad
\partial_wr_j[Z]=0.
\]

따라서

\[
\boxed{\quad
((P_Z)_gH)_x=-q\sum_j\frac{A_jZ_j}{D_j^2}.
\quad} \tag{16}
\]

\(Z=N\ge0\)이고 양의 absorption rate가 하나라도 있으면 오른쪽은 음수다. \(Z=M\)의 보존된 signed interval에는 각 노드의 양수성을 가정하지 않고 \(\inf[\sum_jA_jM_j/D_j^2]>0\)라는 합계 조건을 사용한다. 식 (16)은 광자 잉여에너지의 thermal condition을 전혀 요구하지 않는다.

보존된 AD contracted vector \((P_M)_gH\)는 rate의 `hessian[k][5]`에서 직접 만들어졌다. 총 photo \(P_N\)의 gas Jacobian은 같은 rate의 `gradient[k]`로 얻는다. 실제 signed gas/carry slot의 폭을 그대로 포함한 AD 결과는 식 (16)의 상징적 구조 검산과 구분해 기록한다. \(H_gP\)와 \(P_gH\)의 앞 세 성분은 \(\mathrm{s}^{-2}\), 네 번째와 기체 에너지 projection은 \(\mathrm{eV/H/s^2}\)다. 두 유효 포함의 overlap은 semantic equality 또는 byte identity를 보증하지 않는다.

## 6. 기체 에너지의 정확한 cancellation과 좌표 조건

기체의 열·이온화 에너지 관측량을

\[
e(g)=w+\chi_Hx+f\chi_{\rm HeI}y_1
          +f(\chi_{\rm HeI}+\chi_{\rm HeII})y_2,
\quad
\ell=(\chi_H,f\chi_{\rm HeI},f(\chi_{\rm HeI}+\chi_{\rm HeII}),1)
\tag{17}
\]

로 정의한다. 이 \(e\)는 escaped photon, retained photon, guard 또는 redshift ledger를 포함하는 전체 에너지가 아니다. Projection에는 source의 stage \(f\)를 사용하며 temperature의 \(\widehat f\)와 혼동하지 않는다.

식 (13)의 exact-real source에서는

\[
\ell v_H=\chi_H-\chi_H=0,
\qquad \ell H=0,
\qquad \ell(H_gv)=0 \quad\text{for every }v. \tag{18}
\]

즉 HH의 열에너지 손실과 이온화에너지 증가는 이 기체 projection에서 정확히 상쇄된다. 이것은 동일 \(\chi_H\) leaf가 양쪽에 사용된다는 대수적 identity다. 서로 dependence가 없는 interval로 \(\ell(H_gP_M)\)를 더하면 0을 둘러싼 폭이 생길 수 있으며, 그 폭이 source의 물리적 energy imbalance를 뜻하지 않는다. 원 interval은 보존한다.

HI-only photo의 경우 heat leaf error를

\[
\epsilon_j=a_j-(E_j-\chi_H)
\]

로 정의하면

\[
\ell P_Z=\sum_j(E_j+\epsilon_j)r_j[Z],
\qquad
\ell((P_Z)_gH)
=-q\sum_j(E_j+\epsilon_j)\frac{A_jZ_j}{D_j^2}. \tag{19}
\]

\(\epsilon_j=0\)를 이론적으로 또는 bit 수준으로 확인하지 않은 노드에는 \(E_j\)만 남기지 않는다. 이 항등식은 source heat subtraction의 반올림과 photon energy accounting을 연결한다. Stored signed interval에 식 (19)의 합계 상계가 음수이면 **이 source 방향의 기체 에너지 projection**만 음수라고 말할 수 있다.

식 (18)과 (19)를 더해도 finite gas-energy interaction의 부호는 결정되지 않는다. Implicit root의 선형 resolvent, gas feedback, baseline FT03와 팽창, family carry, 고차항을 거치면 다른 항과 dependence가 생긴다. Source 방향 두 개만으로 actual mixed root \(W_e\)나 유한 \(I_e\)를 발행하지 않는다.

또한 \(z=Sg=(x,y_1,y_2,e)\), \(g=Qz\)라는 exact linear 좌표변환을 사용하면

\[
\widetilde G(z)=S G(Qz),\quad
\widetilde G_z=S G_gQ,\quad
\widetilde G_{zz}[a,b]=S G_{gg}[Qa,Qb]. \tag{20}
\]

State Hessian의 두 입력 인덱스를 모두 \(Q\)로 당겨야 한다. \(S X_{\rm native}\)는 일반적으로 기울어진 평행육면체이고, 그 axis-aligned hull은 더 큰 domain이다. 변환된 energy Jets만으로 기존 thermal-w box가 새 energy box의 근거가 되지는 않는다. Energy-coordinate 조건부 계산을 수행하려면 새 domain을 \(Q\)로 pullback하여 원 source domain 안에 들어가는지 따로 확인해야 한다.

Full nonphoto energy projection에서 유지해야 하는 normalization correction은 기존 exporter의

\[
J_{\rm norm}=(f-\widehat f)
\{\chi_{\rm HeI}F^{\rm nonphoto}_{y_1}
 +(\chi_{\rm HeI}+\chi_{\rm HeII})F^{\rm nonphoto}_{y_2}\}
\]

이며, 전체 photo heat correction은 \(\Psi=\sum_{ja}\epsilon_{ja}R_{ja}\)다. 현재 weighted-temperature 정리를 이유로 이 두 보존 항을 삭제하지 않는다.

## 7. 보존된 NCP 증거만으로 이미 말할 수 있는 것

다음 값은 이번 문서 작성자가 새 계산한 값이 아니라, 현재 NCP head의 `DIRECTIONAL_VECTORS.json`에서 읽은 첫 실행 결과다. 표의 decimal endpoint는 원 bit interval보다 바깥으로 표시했다. 정확한 identity는 원 JSON의 `lo_bits`·`hi_bits`와 intake manifest를 따른다.

| 보존된 source 방향 | Full, K/s | First-half, K/s |
| --- | --- | --- |
| \(DT[H]\) | \([-1.960678\times10^{-14},-5.566020\times10^{-15}]\) | \([-1.960715\times10^{-14},-5.566125\times10^{-15}]\) |
| \(DT[P_M]\) | \([-2.803890\times10^{-13},-1.733005\times10^{-13}]\) | \([-1.403104\times10^{-13},-8.675312\times10^{-14}]\) |

`P_M`의 수소 성분 역시 두 stage에서 양의 하계를 갖는다. Full은 약 \(8.1032621\times10^{-18}\)에서 \(1.1584135\times10^{-17}\ \mathrm{s}^{-1}\), first-half는 약 \(4.0564027\times10^{-18}\)에서 \(5.7968765\times10^{-18}\ \mathrm{s}^{-1}\)다. 이 문장의 근삿값은 표시용이며, 정확한 포함 판단은 bit endpoint로 한다.

원 `P_M[1]`, `P_M[2]`에는 각각 \(\pm\)subnormal interval이 있고, `T_gradient·P_M`는 네 성분을 모두 합산했다. `sourcebox.rs::directional`의 실제 산술 경로는 다음과 같다.

1. 같은 `Phys04DerivativeExport.photo_rates`의 `gradient[5]`를 33개 노드·3개 채널 모두 합쳐 `P_M`를 만든다.
2. 같은 rate의 `hessian[k][5]`를 이용하여 `P_M_g`를 만든다.
3. 같은 whole-source `q`와 `q.gradient`를 이용해 `H`, `H_g_P_M`, `P_M_g_H`를 수축한다.
4. 같은 gas box와 stored density ratio의 `T_gradient`로 `DT_P_M`를 구한다.
5. 별개의 boolean `support`에 모든 nonzero derivative interval 노드와 모든 positive value-support 노드의 per-node \(a_jp<w\) 조건을 누적한다.

따라서 5번이 실패했다고 1–4번의 signed aggregate가 사라지는 것은 아니다. `native_authority=false`라는 scope 역시 유지된다. 기존 독립 판정은 원 predicate 아래 `OPEN`을 유지하라고 명시했다. 새 가중 정리의 채택 여부는 이 과거 파일을 고치는 대신 PHYS08의 독립 판정에서 결정한다.

전체 실제 photo \(P_N\)에 대해서는 위 `P_M` 표를 재사용할 수 없다. `SOURCE_BOX_COMPONENTS.json`의 `photo_rates[*][*].value`를 채널별로 더하고 동일 heat leaf를 곱하거나, `SOURCE_BOX.photons`, `PREBE.groups.value`, denominator와 계수들을 이용해 식 (7)의 저장-export 산술을 수행해야 한다. 후자를 택하면 가정한 실수 식·exact leaf·전체 signed 입력과 원 source AD export의 구분을 결과에 남겨야 한다. 실제 PHYS08 실행은 다음 절처럼 전자의 저장된 rate Jet 합계를 사용하고, closed source 식의 별도 포함과 비교했다.

### 7.1 PHYS08의 새 exact-rational 결과

실제 결과 파일은 `results/weighted_corrected/WEIGHTED_RESULTS.json`이다. `source_stages[*].roles.P_N`은 33개 노드·3개 채널의 `photo_rates.value`, `P_M`은 `photo_rates.gradient[5]`를 사용했다. Gas Jacobian에는 각각 `gradient[k]`, `signed_hessian[k][5]`를 사용했다. 모든 원 signed 성분을 합계에 남겼으며 He 성분과 node32의 subnormal도 제거하지 않았다. Source endpoint의 bit를 exact Fraction으로 해석하고, \(f,\widehat f,C\)의 coefficient 구분을 유지했다.

다음 표는 exact rational 결과를 바깥으로 넓혀 표시한 포함값이다. \(\mathcal B\)의 단위는 \(\mathrm{eV/H/s}\), \(DT\)는 K/s다. 정확한 분자·분모와 표시용 endpoint bit는 결과 JSON에 보존되어 있다.

| Stage와 source 역할 | \(\mathcal B(P)\) 포함 | \(DT[P]=C\mathcal B/p^2\) 포함 |
| --- | --- | --- |
| Full, 총 photo \(P_N\) | \([-9.969964\times10^{-13},-6.407154\times10^{-13}]\) | \([-1.740689\times10^{-9},-1.082374\times10^{-9}]\) |
| First-half, 총 photo \(P_N\) | \([-9.977286\times10^{-13},-6.414618\times10^{-13}]\) | \([-1.741967\times10^{-9},-1.083635\times10^{-9}]\) |
| Full, birth 방향 \(P_M\) | \([-1.604455\times10^{-16},-1.028246\times10^{-16}]\) | \([-2.801270\times10^{-13},-1.737038\times10^{-13}]\) |
| First-half, birth 방향 \(P_M\) | \([-8.028903\times10^{-17},-5.147328\times10^{-17}]\) | \([-1.401793\times10^{-13},-8.695494\times10^{-14}]\) |

네 경우 모두 \(P_x>0\), \(P_w>0\), \(\mathcal B(P)<0\), \(DT[P]<0\)다. 즉 photo는 수소 이온분율과 열에너지를 늘리면서 온도를 낮추는 방향이다. \(C\mathcal B/p^2\), \(T\mathcal B/(wp)\), \(\nabla T\cdot P\)의 세 유효 포함 모두 음수였고, 위 표는 그중 첫 번째 표현만 사용한다. 서로 다른 표현의 endpoint를 임의로 조합하지 않았다.

반응률로 가중한 added-particle당 에너지 \(P_w/Dp[P]\)의 보수적 포함은 총 photo에 대해 full `[0.0557343, 0.1139442]` eV, first-half `[0.0558175, 0.1140140]` eV다. Birth 방향은 각각 `[0.0710463, 0.1451943]`, `[0.0710710, 0.1451439]` eV이고, 네 경우 모두 \(w/p\in[6.0747947,6.6507998]\) eV보다 작다. 이것은 동일 저장된 rate 포함의 ratio bound이며, 그 폭을 독립적인 스펙트럼 폭으로 해석하지 않는다.

저장 Jet를 수축한 다음 source 방향들도 네 경우 모두 엄밀한 음수다. 표에는 읽기 쉽게 바깥 방향의 **상계만** 표시했다. 첫 두 열의 단위는 \(\mathrm{s}^{-2}\), 마지막은 \(\mathrm{eV/H/s^2}\)다.

| Stage와 source 역할 | \((H_gP)_x\) 상계 | \((P_gH)_x\) 상계 | \(\ell(P_gH)\) 상계 |
| --- | --- | --- | --- |
| Full, \(P_N\) | \(-1.251637\times10^{-31}\) | \(-5.893445\times10^{-32}\) | \(-8.061128\times10^{-31}\) |
| First-half, \(P_N\) | \(-1.253130\times10^{-31}\) | \(-5.907374\times10^{-32}\) | \(-8.080230\times10^{-31}\) |
| Full, \(P_M\) | \(-2.017003\times10^{-35}\) | \(-9.507985\times10^{-36}\) | \(-1.302593\times10^{-34}\) |
| First-half, \(P_M\) | \(-1.009710\times10^{-35}\) | \(-4.765208\times10^{-36}\) | \(-6.528335\times10^{-35}\) |

같은 signed 입력에 대한 closed formula 포함도 음수였다. Saved-Jet와 closed-form 간 overlap은 결과에서 `DIAGNOSTIC_ONLY_NOT_IDENTITY_PROOF`로 유지했다. 원 `DIRECTIONAL_VECTORS.P_M`는 이번 exact aggregate의 네 성분을 모두 포함한다. 새 합계의 일부 폭이 줄어든 것은 같은 유한 endpoint를 exact rational로 후처리한 결과이며, source 입력 또는 tail을 좁힌 결과가 아니다.

Node32의 \(\mathcal B\) 기여 포함은 총 photo에서 `[-9e-322,9e-322]`, birth 방향에서 `[-2.5e-321,2.5e-321]` \(\mathrm{eV/H/s}\) 안에 든다. 이 bound는 부호가 있는 원 source-rate tail을 실제로 합산한 것이다. Node32 기여의 절댓값 상계를 전체의 엄밀한 음수 여유로 나눈 비율은 네 경우 모두 \(4.814\times10^{-305}\)보다 작다. 이 정량적 비교는 tail을 버리지 않고도 합계 부호가 닫히는 이유를 보여 준다. 과거 per-node predicate는 계속 false이고 원 `OPEN` 파일도 그대로다.

### 7.2 실행 근거와 첫 실패 보존

새 실행의 owner는 root다. 이 이론 작성자는 저장된 JSON·로그를 읽었고 수치 프로그램을 별도로 실행하지 않았다. 최초 `weighted_first`는 \(\nu=\eta+157800/T\)의 `int / E`에서 Python reflected division이 구현되지 않아 `TypeError`로 종료했다. 분류는 `REFERENCE_SCAFFOLDING_OPERATOR_OMISSION`이며 source 수식의 반례나 물리 실패가 아니다. 원 코드 snapshot·stderr·실행 기록·`FAILURE_CLASSIFICATION.json`을 보존했다. 최초 성공이라고 보고하지 않는다.

계약이 허용한 한 번의 표적 수정은 기존 interval division에 위임하는 `__rtruediv__`의 추가와 create-only corrected output ID의 사용이었다. Scientific input·domain·부호·tolerance·assertion을 바꾸지 않았고, `weighted_corrected`는 2026-10-11 05:24:42 UTC에 exit 0으로 완료됐다. 경과시간은 `0.3678347829991253 s`, Linux max RSS는 `19324 KiB`다. 결박한 코드·입력의 실행 전후 bytes/SHA가 모두 일치했고 stderr는 0 bytes였다.

Corrected run은 **294개 assertions**, **실제 source 4개와 의미 사례 7개를 합한 총 11개 golden fixture**, 두 stage와 두 source 역할을 검산했다. 294는 독립적인 test case 수가 아니며 반복된 shape·domain 확인 등을 포함하는 assertion 수다. Semantic fixtures에는 작은 hot tail의 전체 냉각, 큰 hot tail의 가열, zero·zero-touching, signed He 성분을 버렸을 때 생기는 잘못된 냉각 판정, 양의 scaling, 최소 subnormal signed 값과 invalid input rejection이 포함된다. 이러한 보조 사례는 실제 33×3 source 증거를 대체하지 않는다.

Python exact arithmetic의 성공은 Rust build/run을 뜻하지 않는다. 현재 결과의 Rust 상태는 `NOT_BUILT_NOT_RUN_TOOLCHAIN_ABSENT`다. 새 native binding, PreBE, residual, FT03, HH, provider, nonlinear root, IVP 및 과거 science replay는 없고, 이는 이 offline Python 실행 경로의 관측 범위다. 과거 미계측 counter를 새 0으로 채우지 않는다. Actual native \(U,V,W,I\)와 finite gas-energy sign은 여전히 OPEN이다.

## 8. C² 및 넓은 family 양화사를 유지하는 조건

정리의 양화사는 다음 순서다.

\[
\forall\alpha\in\mathcal A\ \text{fixed},\quad
\forall g\in X_{\rm native},\quad
\forall(\lambda,b)\in[0,1]^2:
\quad DT_g[P_Z(g,\lambda,b;\alpha)]<0. \tag{21}
\]

\(\alpha\)는 원 stored COMMON interval, 고정 angular·geometry chart, source leaf와 stage 상수에서 온 일관된 coefficient vector다. 같은 family를 미분하는 동안 각 노드의 계수나 원 history를 매개변수 점마다 임의로 다시 선택하지 않는다. 큰 interval product를 사용한 pointwise 포함이 이런 비일관 선택도 외부적으로 포함할 수는 있지만, 그 사실이 비일관 배열을 하나의 differentiable family로 만들어 주지는 않는다.

Source를 gas 방향으로 미분할 때는 \(\lambda,b\)를 고정한다. 실제 `phys04_prepare_family`의 transport·remap·angular weight는 전달받은 gas 값으로 계산되지 않는다. COMMON photon·guard의 future Jet은 초기 상수이고, 직접 birth의 유일한 매개변수 slot은 5다. 따라서 해당 실수 family에서는 \(N_g=N_\lambda=M_g=0\)이며, PREBE의 작은 signed gas·mixed slot 폭은 이 0을 포함하는 외부 interval이다. 새 aggregate는 그 폭을 보존한다. \(P_N\)에는 rate의 `value`와 `gradient[k]`, \(P_M\)에는 `gradient[5]`와 `signed_hessian[k][5]`를 각각 사용하면, 두 서로 다른 역할의 source vector와 gas Jacobian을 같은 export에서 읽을 수 있다.

현재 NCP의 C² 증거는 보존된 넓은 \(X_{\rm native}\)와 별도의 열린 gas 이웃에서 분율 simplex, 양의 \(w,p\), HH 온도 구간, 양의 denominator를 확인한다. \(D_j\)는 \(N,\lambda,b\)와 독립이며 열린 gas 이웃에서도 \(D_j\ge1\)인 실수 식을 갖는다. \(N_j\)는 \(b\)에 affine이므로 작은 열린 parameter 이웃에서 대수적 확장을 정의할 수 있다. 그 확장이 native 실행 guard 밖의 실제 source 호출을 허용하는 것은 아니다.

Rounded binary64 프로그램과 interval `nonneg` 또는 outward widening 연산 자체를 C² 함수로 취급하지 않는다. 미분 대상은 저장된 계수를 고정한 실수 source이고, Jet와 구간은 그 값·미분의 포함 증거다. Physical value에 이미 적용된 비음수 cone intersection은 원 의미를 유지한다. Gradient·Hessian에는 같은 cone을 적용하지 않는다.

가중 합계의 부호는 반드시 **동일한 whole gas × whole parameter domain**의 입력에서 나와야 한다. 중심 gas에서 나온 rate와 whole-box gradient를 섞어 `whole-domain`이라고 보고하지 않는다. Full과 first-half의 density/dt/PreBE를 섞지도 않는다. Python point reference의 leaf 또는 root 결과를 native-source family에 끼워 넣지 않는다.

## 9. 필요한 보존 필드와 최소 재산술 계약

| 목적 | 필요한 실제 필드 | 의미와 제한 |
| --- | --- | --- |
| Signed aggregate 온도 부호 | `DIRECTIONAL_VECTORS.P_M`, `T_gradient`, `DT_P_M` | 네 성분 모두 보존; 원 archived 결과의 독립 rational contraction 가능 |
| 식 (1)로 별도 가중 합계 | `C2_DOMAIN.X`, `fhat` 또는 정확한 stored density leaf, `particles`; `P_M` | 원 bit endpoint를 exact rational로 해석; \(f\)로 치환하지 않음 |
| 실제 총 photo | `SOURCE_BOX_COMPONENTS.photo_rates[*][*].value`, `SOURCE_BOX.heat_bits`, `fHe_bits` | 33×3 전체를 포함; \(P_M\)와 구분 |
| Incoming 기반 독립 대수 형태 | `PREBE.groups[*].value` 또는 `gradient[5]`, `SOURCE_BOX.D`, `sigma_bits`, `heat_bits`, `nH_bits`, `NATIVE_CONSTANT_LEAVES.c_bits` | 원 tail·기존 denominator를 유지; source/초월함수 호출 없음 |
| HH에 의한 photo 억제 | 원 `q.value`, \(A_jZ_j/D_j^2\) 전체 합 또는 saved `P_M_g_H` | 실제 source directional result; root mixed response 아님 |
| Energy cancellation | 동일 CHI leaf, `fHe_bits`, `H_g_P_M`, `P_M_g_H`; 실제 \(\epsilon\) 정의 | \(\ell H_gP=0\)를 raw interval width와 구분 |
| Whole-domain provenance | frozen contract, `C2_DOMAIN`, same-object PREBE validator, source/candidate/ABI/binary/input identity, named-first 실행 기록 | Hash 일치만으로 source 의미·C²·실행 범위를 대체하지 않음 |

재산술에서 최소 양의 subnormal \(2^{-1074}\)를 exact rational로 읽으면 작은 signed tail이 보통 binary64 곱에서 다시 underflow되는 문제를 피할 수 있다. 이는 원 interval을 더 좁히거나 원 source 프로그램을 새 precision으로 재실행한다는 뜻이 아니다. 보존된 유한 endpoint와 저장된 source 식에 대한 후처리 산술이다. 결과의 exact rational endpoint를 보존하고, decimal 출력은 별도의 바깥 방향 표시로 둔다.

실제 corrected 산술이 성공했으므로 위 7.1–7.2절의 완료된 exact arithmetic evidence를 가중 정리에 연결한다. 이후 다른 입력의 결과가 0을 포함하면 실패 또는 OPEN을 그대로 보존하고, 임의 tail 삭제나 같은 증거로의 반복 실행을 하지 않는다. 실제 source/native 실행을 허용하는 코드나 gate는 이 이론 문서가 생성하지 않는다.

## 10. 극한, 반례와 남는 범위

- **광원이 0인 경우:** 모든 \(Z_j=0\)이면 \(P_Z=0\), \(DT[P_Z]=0\)다. 엄밀 음수 조건에는 비영 source가 필요하다.
- **평균 잉여에너지의 임계:** \(Q_Z/R_Z=w/p\)이면 온도 변화는 0이다. 작은 잉여에너지라는 정성적 설명만으로 엄밀 부호를 주장하지 않는다.
- **높은 에너지 stock이 충분히 큰 경우:** 식 (11)의 양의 항이 음의 항을 이길 수 있다. 이번 정리는 모든 스펙트럼이 냉각한다는 보편 주장이 아니다.
- **흡수 단면적이 0인 경우:** 해당 exact-real 반응률은 0이다. 원 AD export의 roundoff enclosure 폭은 별도 보존한다.
- **완전 이온화 경계:** 식 (14)의 \(1/u\) 표현은 \(u=0\)에서 사용할 수 없다. 현재 domain은 \(u>0\)이고, 경계 자체는 원 \(q=n_Hu^2k\)를 직접 미분해야 한다. 이 문서는 경계로 무단 연장하지 않는다.
- **Stage 시간 폭:** \(d\to0\)에서 \(D_j\to1\)이지만, 실제 finite birth leaf \(\operatorname{fl}(dS_*)\)를 시간에 대해 매끄러운 함수라고 미분하지 않는다. Fixed-stage 결과와 별도 smooth-source formal limit를 구분한다.
- **같은 C² domain:** Source coefficient·threshold·geometry branch가 달라지면 현재 증명을 자동 이전하지 않는다. 새 같은-domain 증거가 필요하다.
- **전체 물리 모형의 적합성:** Weighted sign은 고정된 HH/FT03/photo 모델 안의 정리다. 원자물리 fit의 외삽, 모든 방사선 스펙트럼, physical production admission에 대한 주장은 아니다.

## 11. 원본·추적성

현재 읽은 authoritative NCP snapshot은 repository `cosmosapjw-quantum/WU088_HH`, head `4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b`, prefix `research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/`이다. 원본 파일별 bytes/SHA256/Git blob과 intake 범위는 PHYS08 입력 manifest를 따른다.

핵심 source는 [native directional producer](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/src/sourcebox.rs), [reduced source](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/candidate/src/phys04_mixed.rs), [transport](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/candidate/src/phys04_transport.rs), [HH Jet](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/candidate/src/hh_primary_extension.rs), [energy projection](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4d5c18b8a6d348e2de42b5e12dc0fd4d753add7b/research/r31ao_unequal_ladder/ncp_phys07_local_20261011_v1/src/energy.rs)다. 새 문헌상 신규성은 주장하지 않는다. 이 문서의 가중 항등식과 따름정리는 위 고정 source 식에서 직접 유도했다.

이론 작성자는 Astra v4 research core와 model routing을 읽었다. Host label은 `GPT-6 Astra Pro`이고 기존 Astra v4 continuation을 따르되 runtime attestation이나 model switch를 주장하지 않는다. 이번 하위작업에서 source/physics 실행, build, test, numerical diagnostic, remote mutation은 수행하지 않았다. 원 파일과 root의 실제 실행 결과를 읽고 이 문서와 동반 claim JSON만 작성했다. 최종 채택은 후보 생성자가 아닌 독립 reviewer의 판정을 따른다.
