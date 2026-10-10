# WU088_HH PHYS02 — 광자–HH 비가산성의 유한시간 부호

2026-10-10 · 직접 유도, 구간 계산, 독립 소스·대수 검토

## 1. 결론

HH-PHYS01에서 얻은 음의 3차 혼합항을, **같은 초기 전체 상태와 같은 고정 source 모형의 유한 시간 구간**으로 확장했다. 기존 광자 재고, H/He의 충돌이온화·복사재결합·두 유전재결합 경로, 열에너지 변화와 팽창 일 항을 함께 유지했다. 계산 대상은 원 코드의 binary64 입력·상수를 정확한 실수로 읽고 함수·연산식을 실수에서 평가한 frozen source이다.

\[
\Delta_*=1.25\times10^9\ {\rm s},\qquad
S_*=5\times10^{-15}\ {\rm photons/(H\,s)},\qquad
b=S/S_*,\quad \tau=t/\Delta_*.
\]

기록된 binary64의 정확한 값은 결과 JSON에 보존했다. 모든 \(0<\lambda\le1\), \(0<b\le1\), \(0<t\le\Delta_*\)에 대해

\[
\boxed{\mathcal I_x(t;\lambda,S)<0}
\]

를 얻는다. \(\lambda=0\), \(S=0\), \(t=0\)에서는 정의에 의해 혼합 차이가 정확히 0이다. 이 결과는 HH가 총 이온화를 줄인다는 주장이 아니다. **HH와 새 광자 방출을 함께 켰을 때의 증가량이, 각각 따로 켰을 때 증가량의 합보다 작다**는 뜻이다.

\(t=\Delta_*\)에서 계산한 구간을 바깥쪽으로 짧게 반올림하면

\[
\boxed{
\frac{\mathcal I_x(\Delta_*;\lambda,S)}{\lambda b}
\in[-2.010735,\,-2.010487]\times10^{-17}.}
\]

3차 항 뒤의 **모든 고차 나머지**는 그 3차 항 크기의 **0.268818% 미만**이다. 실제 변화하는 Bianchi background, photon birth/remap chronology, BE full/two-half 근, 전체 source history 또는 LCS 물리율의 정확도를 인증한 결과는 아니다.

## 2. 비교하는 물리계와 입력

물질의 국소 zero-tilt frame, proper time, metric signature \((-+++)\)를 사용한다. 기체는 공통온도의 H/He이며

\[
z=(x,y_1,y_2,w,P_0,\ldots,P_{24}),\quad
x=x_{\rm HII},\quad y_1=x_{\rm HeII},\quad y_2=x_{\rm HeIII},
\]

\(w\)는 eV/H, \(P_j\)는 photons/H이다. \(n_H,n_{He}\)는 \({\rm cm^{-3}}\)이며 \(c,k_B\)를 유지한다. source 단계에서는 밀도, 에너지, 단면적과 \(H_{\rm mean}\)을 고정한다.

\[
\dot z=F_0(z)+\lambda\mathcal H(z)+S B,\qquad
\mathcal H=q\eta,\quad
\eta=(1,0,0,-\chi_H,0_{\rm photon}),
\]

\[
q=n_H(1-x)^2 k_{\rm LCS}(T),\qquad
k_{\rm LCS}(T)=1.2\times10^{-17}(T/{\rm K})^{1.2}
 e^{-157800\,\mathrm{K}/T}\ {\rm cm^3s^{-1}}.
\]

\(\lambda\)는 동일한 LCS provider의 수학적 세기이다. KS/LCS 혼합이나 물리율의 확률오차로 해석하지 않는다. 별도 쌍계수 \(1/2\)는 추가하지 않았다. \(B\)는 \(E_*=13.7\) eV의 마지막 광자 bin에 photon number를 넣는 상수 방향이다.

네 해의 초기 상태는 완전히 같다.

\[
\mathcal I_x=x(t;\lambda,S)-x(t;\lambda,0)
 -x(t;0,S)+x(t;0,0).
\]

특히 \(S=0\)에서는 **앞으로의 새 방출만 0**이고, 이미 존재하는 광자는 남는다. 서로 다른 과거를 가진 ON/OFF 이력이나 Bianchi/FLRW 이중차이를 이 정의로 바꾸지 않았다.

정본 입력은 PHYS01의 `inputs/SELECTED_SOURCE.json`이다. SHA-256은

    26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494

이며 `old_gas`와 `old_point_photons`를 사용했다. 저장된 과거 endpoint 또는 parent interval을 새 초기값으로 대입하지 않았다. 선택된 값은 다음과 같다.

| 양 | 값 |
|---|---:|
| \(x_0\) | 0.9131385026926517 |
| \(n_H\) | \(9.951928415493808\times10^{-5}\ {\rm cm^{-3}}\) |
| \(n_{He}\) | \(8.260100584859861\times10^{-6}\ {\rm cm^{-3}}\) |
| \(T_0\) | 49,489.0775134 K |
| \(\chi_H\) | 13.598434599702 eV |
| \(E_*-\chi_H\) | 0.101565400298 eV |
| \(q_0\) | \(1.59724160718\times10^{-19}\ {\rm s^{-1}}\) |
| \(A_*=cn_H\sigma_H(E_*)\) | \(1.85650714446\times10^{-11}\ {\rm s^{-1}}\) |

H/He의 비광자 반응은 `ft03_rates.rs`, `ft03_controlled.rs`의 CI/RR/두 DR와 RR kinetic cooling을 그대로 실수식으로 옮겼다. 기체 열식의 \(-2H_{\rm mean}w\)도 유지했다. 입력의 25개 photon bin 중 16개는 모든 단면적이 정확히 0이고 새 방출도 없다. 이 16개 좌표는 정확히 상수라서 대수적으로 제거했다. 나머지 9개는 **각 bin의 독립적인 소멸식**을 유지했다. 평균 opacity를 넣는 closure는 사용하지 않았다.

### 상수의 의미

기록된 숫자와 Rust leaf 상수는 exact binary64 real이다. 거듭제곱, 지수함수와 대수식은 실수에서 평가하고 Arb로 포함한다. 예컨대 DR prefactor의 중간 곱을 native binary64에서 반올림한 값과 이 실수식은 일반적으로 byte/연산 의미가 다르다. 본 증명은 **명시된 실수 모형**의 증명이며 native per-operation rounding 또는 별도 owner의 근 발급을 검증한 것이 아니다.

## 3. 왜 3차의 억제가 생기는가

이 절의 3차 결과는 PHYS01에서 계승한다. \(u=1-x\), \(r=n_{He}/n_H\),

\[
\Pi=1+r+x+r(y_1+2y_2),\quad
T=\frac{2\epsilon_{\rm eV}}{3k_B}\frac{w}{\Pi},\quad
T_\gamma=\frac{2\epsilon_{\rm eV}(E_*-\chi_H)}{3k_B},
\]

로 놓는다. \(\epsilon_{\rm eV}\)는 eV→erg 변환상수이다. 광이온화 한 사건에 대해

\[
\frac{dT}{dJ_{\rm photo}}=\frac{T_\gamma-T}{\Pi}.
\]

현재 \(T_\gamma\simeq785.745\) K이고 \(T_0\simeq49489.078\) K이다. 광자 excess energy의 가열은 양수지만, 새 자유전자가 늘리는 입자수 때문에 이 사건 방향의 온도 변화는 음수다. 따라서 HH율은 중성수소 target 감소와 온도 감소 양쪽에서 억제된다. 이것은 모든 기체 열항을 합한 전체 온도 진화의 부호와 구별해야 한다.

\[
\nu=T\frac{d\ln k}{dT},\qquad
\Xi=\frac{u}{\Pi}\nu\left(1-\frac{T_\gamma}{T}\right)
\]

에 대해 \(\Xi_0=0.176902468411\)이고, 계승한 결과는

\[
\mathcal I_x=-\frac{\lambda S A_*q_0(4+\Xi_0)t^3}{6}
 +O(\lambda S t^4).
\]

PHYS01에서는 여기의 \(O(t^4)\)가 실제 \(t=1.25\times10^9\) s에서 얼마나 큰지 남아 있었다. 이번 작업은 이 부분을 채운다.

## 4. 네 해를 빼지 않는 유한시간 증명

\(b=S/S_*\)를 사용하고

\[
U=\partial_\lambda z,\quad V=\partial_b z,\quad
W=\partial_\lambda\partial_b z,\quad
J=F_z,\quad Q=F_{zz}
\]

로 정의하면 정확한 민감도 방정식은

\[
\dot U=JU+\mathcal H,\qquad
\dot V=JV+S_*B,\qquad
\dot W=JW+Q[U,V]+\mathcal H'V.
\]

공통 초기조건 때문에 \(U(0)=V(0)=W(0)=0\)이다. 혼합항은

\[
\mathcal I_x(t;\lambda,b)
=\int_0^\lambda\!d\alpha\int_0^b\!d\beta\,
W_x(t;\alpha,\beta)
\]

와 정확히 같다. 따라서 작은 HH·source 응답을 독립된 미분 좌표로 보존할 수 있다. \(x\simeq0.9\)인 네 binary64 값의 직접 차분으로 \(10^{-17}\) 신호를 추출하지 않는다.

### 4.1 모든 매개변수 경로를 함께 포함하는 영역

활성 상태 13개와 \(U,V,W\)를 합치면 52개 좌표이다. \(\tau=t/\Delta_*\)의 augmented RHS를 \(G\)라 하고 공통 상자 \(\mathcal Y\)에 대해

\[
Y_0+[0,1]G(\mathcal Y,[0,1]^2)
\subset\operatorname{int}\mathcal Y
\]

를 확인했다. 구현은 \([0,1]G\)보다 넓은 대칭 절댓값 상자를 사용했다. 4번의 대수적 폭 조정 뒤 **52개 좌표 모두 strict inclusion**을 만족했다. 이것은 trajectory time stepping이나 BE nonlinear solve가 아니다.

왜 이 검사로 충분한가? 해가 \(\mathcal Y\)를 처음 나가는 시간이 있다고 가정하면, 그 시각까지 RHS는 \(G(\mathcal Y)\) 안에 있으므로 적분된 변화도 위 포함관계에 들어가야 한다. 이는 처음 도달한 점이 경계라는 가정과 모순이다. compact 영역에서 RHS가 매끄러우므로 존재와 유일성도 해당 시간까지 연장된다. 여기서 별도의 수축계수 \(<1\)는 필요하지 않다.

모든 기체 분율과 photon number가 물리 영역에 남았으며 온도 상자는

\[
49482.0213623<T<49496.1347657\ \mathrm{K}
\]

로 포함됐다. HH의 35000–60000 K guard, FT03의 30000–110000 K guard와 양의 EOS 분모를 모두 만족한다. 따라서 필요한 상태 미분이 정의되지 않는 floor나 온도 경계를 지나지 않는다.

### 4.2 4차 미분으로 모든 고차 나머지를 제한한다

시간 Taylor 계수는 이미 factorial로 나눈 값으로 정의한다. 위 **전체 상자**에서

\[
\frac{1}{4!}\frac{d^4W_x}{d\tau^4}
\in[L_4,U_4]
\subset[5.1715113,5.4191015]\times10^{-20}
\]

를 얻었다. 초기점 한 곳의 4차 계수만 구한 결과와 다르다.

초기 혼합 계수는 \(W_x(0)=W_x'(0)=W_x''(0)=0\)이고

\[
c_3=-\frac{S_*A_*q_0(4+\Xi_0)\Delta_*^3}{6}
=-2.0159064162896692\ldots\times10^{-17}.
\]

Taylor 적분 나머지의 가중치가 양수이므로

\[
\boxed{
\frac{\mathcal I_x(t;\lambda,S)}{\lambda b}
\in c_3\tau^3+[L_4,U_4]\tau^4,
\qquad0<\tau\le1.}
\]

이 식에는 **4차, 5차 및 그 이후의 모든 시간 차수**가 포함된다. 필요한 조건은 source의 충분한 매끄러움과 방금 검증한 전체 경로의 영역 잔류이다. 초기 4차 항만 더해서 오차를 무시한 식이 아니다. \(L_4,U_4\)에 \(1/24\)나 \(\Delta_*^4\)를 다시 곱하지 않는다.

\[
\frac{U_4}{|c_3|}<0.002688172
\]

이므로 모든 \(0<\tau\le1\)에서 음의 3차 항이 유지된다. 또한 \(L_4>0\)이므로 나머지는 이 구간에서 억제의 크기를 조금 줄인다. cubic만 쓴 값보다 실제 frozen-flow 혼합항은 약간 덜 음수다.

| 양, \(t=\Delta_*\), \(\lambda=b=1\) | 구간 또는 값 |
|---|---:|
| 계승한 cubic 항 | \(-2.01590641629\times10^{-17}\) |
| 4차 이상 전체 나머지 | \([5.1715113,5.4191015]\times10^{-20}\) |
| 혼합 응답 \(\mathcal I_x\) | \([-2.010735,-2.010487]\times10^{-17}\) |
| 나머지 / cubic 크기 | \(<0.268818\%\) |

정확한 dyadic endpoint와 outward decimal endpoint는 `results/REMAINDER_256_FINAL.json`에 있다. 표시된 짧은 구간은 그 구간보다 바깥으로 반올림했다.

## 5. 이번에 추가로 분리한 4차의 물리

초기점에서 \(C=JB\), \(Q=F''\), \(K_3=\partial_\lambda\partial_S z^{(3)}(0)\)라 하면 독립 유도로

\[
\begin{aligned}
K_4={}&JK_3+3Q(B,J\mathcal H+\mathcal H'F)
 +3Q(\mathcal H,C)\\
&+\mathcal H'[JC+2Q(F,B)]+3\mathcal H''(F,C)
\end{aligned}
\]

를 얻었다. photo 항이 gas–photon에 bilinear이고 HH가 photon-independent라는 원 모형의 구조를 사용했다. 비광자 H/He 반응과 열·팽창항의 도함수는 4차에 남는다.

이 계수는

\[
K_4(\lambda,S)=K_{40}+\lambda K_{41}
\]

로 \(S\)에 무관하고 \(\lambda\)에 affine이다. 따라서 유한 사각차이의 4차부터 \(\lambda^2 S\)가 나타날 수 있으며, \(\lambda S^2\)는 아직 없다. 매개변수 적분을 하면 \(\lambda K_{41}/2\)가 들어간다. 큰 \(\lambda\)에서 단순히 mixed derivative endpoint만 곱하는 방법과 이 적분은 구별해야 한다. 본 상계는 전체 \([0,1]^2\)를 직접 포함해 이 비선형성을 이미 보존했다.

현재 HI-only support에서 초기 \(K_{4,x}\)의 기존 photon 재고는 정확히

\[
\Gamma_0=\sum_j a_jP_{j,0},\qquad
G_0=\sum_j a_j(E_j-\chi_H)P_{j,0},\quad
a_j=cn_H\sigma_H(E_j)
\]

두 가중합으로 나타난다. \(\Gamma_0\)는 \({\rm s^{-1}}\), \(G_0\)는 eV/s이다. 이것은 **초기 4차 계수의 식을 줄이는 항등식**이다. 전체 동역학을 두 변수로 닫는 closure는 아니다.

\[
\dot\Gamma=-u\sum_j a_j^2P_j+A_*S
\]

에서 다른 순간이 필요하므로, finite-time 상계는 활성 9개 bin을 그대로 유지했다. 전체 tensor 유도와 경계·단위 검사는 `independent/HH_PHYS02_REMAINDER_DERIVATION_KO.md`에 있다.

## 6. 검증과 근거의 구분

본 작업의 수학 정리는 직접 유도(derived), Arb 상계는 numerically checked, 전사와 미분 연산 검사는 implementation-verified 범위이다. Arb는 midpoint–radius 표현으로 연산 오차를 포함하는 ball arithmetic을 제공한다. 실제 사용 버전은 Python의 `python-flint 0.8.0`, backend FLINT 3.3.1이며 256 bit와 384 bit의 동작 환경을 각각 결과에 기록했다. 일반적 산술 의미는 [FLINT Arb 문서](https://flintlib.org/doc/arb.html)를 참조한다. 형식증명기에서 검증한 정리는 아니다.

- 새 단위 시험 14개: 비선형 hyperdual, 정확히 아는 scalar flow, factorial/time recurrence, 분모·로그 guard, HH 에너지 방향, source 삽입 위치, bin 제거, 매개변수 구조, 52좌표 포함관계 및 outward 출력.
- 독립 유도 경로: 유리수 다항식 fixture의 6개 매개변수 조합에서 4차 tensor식과 별도 time/parameter series가 모든 성분에서 정확히 일치.
- 독립 소스 전사 검사: FT03 per-cm3 경로와 정규화한 구현을 별도 고정밀 산술로 비교했다. 상세 범위와 원로그는 `independent/SOURCE_AUDIT.md` 및 JSON에 수록한다.
- 256 bit에서 닫힌 상계는 384 bit의 한 차례 점검에서도 유지됐고, 384 bit의 구간은 256 bit 구간 안에 들었다. 이것은 한 번의 반올림·포함관계 점검이며 물리적 수렴시험을 뜻하지 않는다.
- 부모의 완료 과학 suite, ON06G 이력, 원자 적분, native 실행, BE 근 풀이, NCP dispatch를 새로 실행하지 않았다. 새 계산은 대수적 parametric tube enclosure와 도함수·계수 검사이다.

초기 JSON은 내부 Arb 구간을 40자리 표시문자열로 내보냈으나 그 endpoint 문자열의 outward rounding을 보장하지 않았다. 내부 포함관계와 부호 결과는 유지됐지만, 이 문자열을 인증값으로 쓰지 않도록 **exact dyadic endpoint와 directed 42자리 decimal endpoint**를 추가했다. 첫 출력과 수정 기록을 보존하고 `_FINAL`을 정본으로 지정했다. 실패를 삭제하거나 처음부터 모두 통과했다고 기록하지 않았다.

독립 최종 decision reviewer의 허용 주장과 판단은 `independent/DECISION.json`에 기록한다. 이 판단도 본 고정 source 구간에 한정한다.

## 7. 무엇이 닫혔고 무엇이 남았는가

| 의무 | 이번 상태 |
|---|---|
| PHYS01의 local cubic coefficient | 계승, 부모 full suite 재실행 없음 |
| 동일 초기 상태의 전체 \(\lambda\times S\) 가족 | 현재 frozen interval에서 포함 |
| 목표 \(1.25\times10^9\) s의 4차 이상 나머지 | 구간 상계 확보 |
| 목표 구간에서 음의 비가산성 | 부호 확보 |
| 최대 허용 시간 또는 전역 부호정리 | 미계산 |
| 원 initial-history 불확실성에 대한 가족 | 미계산; 선택한 old point가 기준 |
| 실제 time/angle/energy-dependent macro | 미해결 |
| BE full/two-half의 실제 coupled root와 family | ENERGY06E owner 의무, 미해결 |
| LCS율의 물리적 오차/실험 검증 | 이번 연구 대상 아님 |
| 물리·production 전역 승인 | HOLD 유지 |

특히 실제 redshift를 넣을 때는 threshold 문제를 먼저 다뤄야 한다. 선택 spectrum에는 **13.6 eV에 놓인 활성 bin 16**이 있고 그 아래에는 zero-sigma branch가 있다. 따라서 에너지 이동을 포함하는 전체 단계에 무조건 \(C^5\) Taylor 공식을 적용하면 안 된다. 이번에는 에너지·단면적을 고정했으므로 상태 미분이 매끄럽다.

canonical S0의 HH OFF 대조군, HH research ACTIVE, legacy 24/289와 265 미상계, \(\epsilon_C=\epsilon_R=\mathrm{null}\), B22 OPEN, ON06G 256 macros / \(3.2\times10^{11}\) s 및 consumed execution scope를 모두 보존한다. 다른 저장소의 HE/CR 결과를 공동 ON 물리로 합치지 않았다.

## 8. 다음 물리 루프와 구현 인계

다음 물리 단위는 **PHYS03: threshold와 birth를 구분한 실제 chronology의 혼합 응답**으로 둔다. 먼저 frozen PHYS02와 실제 stage 사이의 차이를 source identity에 결속하고, smooth cell과 event map을 분리한다. 기존에 완성된 ENERGY06E receipt/계약을 다시 만드는 단계는 넣지 않는다.

1. smooth cell에서 실제 \(n_H(t),E_j(t)\), source law에 의한 \(F_t\) 항과 mixed remainder를 유도한다. 모르는 background나 photon history를 새로 만들어 넣지 않는다.
2. bin 16을 포함한 cutoff/hat-cell, discrete birth와 reset을 event로 분리하고, event 전후의 상태·감도 전달을 정의한다. 기존 photon 감도를 0으로 재설정하지 않는다.
3. 실제 owner의 동일 \(\theta,\lambda\) family와 source insertion 순서를 확인한다. accepted half1 및 full-chain Jacobian/preconditioner가 없는 상태에서는 PHYS02의 부호를 실제 macro 인증으로 전용하지 않는다.
4. 필요한 정확한 실행 승인이 이미 존재하는 최소 단위에서만 actual owner 검사를 이어간다. 이번 물리 패키지는 새 NCP/native campaign 승인이 아니다.

구체적인 입력·출력·금지 재실행·반환 파일은 `WU088_HH_PHYS02_NEXT_HANDOFF_KO.md`와 `NEXT_DAG.json`에 있다. 현재 결과를 다시 처음부터 감사하기보다 이 남은 물리 차이를 해소하는 것이 다음 연구의 목적이다.

## 9. 원본과 재현 경로

- PHYS01 정본: [commit b91a2716의 게시 문서](https://github.com/cosmosapjw-quantum/WU088_HH/blob/b91a2716ef0a7f8172fa643ca4d99615e9efa443/research/r31ao_unequal_ladder/hh_phys01_photo_hh_competition_20261010_v1/START_HERE_KO.md). 전체 원문 ZIP의 SHA-256은 `INPUT_IDENTITY.json`에 고정했다.
- 별도 실제 owner: [ENERGY06E return, 40716663](https://github.com/cosmosapjw-quantum/WU088_HH/blob/4071666330d46df1b1965465ae2697c3a10aeb01/research/r31ao_unequal_ladder/ncp_energy06e_certificate_20261010_v1/RETURN_KO.md). 이 상태는 새 실제 root/family가 없다는 source obligation을 확인하기 위해 읽었다.
- 재현: `REPRODUCE_KO.md`; 계산: `bound_remainder.py`; 결과: `results/REMAINDER_256_FINAL.json`; 정확한 유도: `independent/HH_PHYS02_REMAINDER_DERIVATION_KO.md`.
- 새 물리 식과 구간 증명은 이번 직접 유도다. 외부 문헌에 이 HH mixed coefficient 또는 이 수치 상계가 실려 있다고 주장하지 않는다.
