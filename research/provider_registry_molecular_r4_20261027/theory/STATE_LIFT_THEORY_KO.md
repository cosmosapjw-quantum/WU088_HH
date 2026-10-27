# R4 LiH·HD의 상태별 반응과 집계 연산자

## 1. 이 문서의 결과와 전제

이 문서는 회수된 LiH·HD 공급자의 화학식에서 정확한 입자수 열을 구성하고, 상태별 파괴율을 하나의 집계 계수로 사용할 수 있는 조건을 증명한다. 유한 상태족의 알려진 계수 벡터와 명시적인 상태 분포가 주어졌을 때 얻는 결과다. 현재 공급자 표만으로 상태 분포나 실제 소비자를 만들었다는 주장은 포함하지 않는다.

기준은 [CONTRACT.json](../CONTRACT.json), source packet SHA256 **40e2fbd73d451c0c8116b4ca9bd4db4d2e43e4cdf8967988a2fea551f99ce35e**, [MOLECULAR_SOURCE_PACKET.json](../sources/MOLECULAR_SOURCE_PACKET.json)이다. source packet의 6개 variant와 77개 인쇄 계수 cell은 재사용한다. scratch 소실 뒤 packet은 같은 SHA로 복구되었으며, 원파일 접근·복구 한계는 [RECOVERY_RECORD.json](../sources/RECOVERY_RECORD.json)에 따로 기록되어 있다. 원 숫자 또는 공급자의 상태 정의를 이 이론 문서에서 교체하지 않는다.

현재 작성 범위는 R3의 전제 명시, R4의 표현 선택, R5의 조건부 유도다. 증명은 저자 작성 완료이며 독립 R6 검토를 기다린다. 이 문서 작성 중 rate/Q 평가, partition function 계산, compiler 실행, IVP, Wolfram 호출은 수행하지 않았다. 기존249·R1·R2·R3·PHYS91·REI 완료 결과의 재실행도 없다.

### 실제 source에서 읽은 서로 다른 관측량

| Source | 이 단위에서 확보한 것 | 그대로 남는 상태 조건 |
|---|---|---|
| Bennett2003 §2.2·§4.1.1·Table3 | Li(2s)+H(1s)의 spontaneous association 총계와 원fit | X¹Σ⁺의 bound/quasi-bound 최종준위와 후속 방사 생존을 가중한 집계; 최종(v,J) 분포 없음 |
| Bovino2009 §2–3·Table1 | LiH+H→Li+ortho/para-H2의 별도14온도 총계 | Table1의 초기 분자 v/j, 두 제품 spin 총계의 population weighting 미결속 |
| Honvault2013 correction Table1 | D⁺+H2(v=0,j=0)→HD+H⁺의 TIQM/SQM 수정 표 | 두 방법은 대안; 생성 HD의 개별 준위 분포를 이 표가 제공하지 않음 |
| González-Lezana2022 §III.A 식(5)–(7) | HD+H⁺ 파괴의 열적 집계fit과 직접 인쇄된 두 SQM 값 | HD(v=0,j=0…8)의 회전 Boltzmann 평균과 H2(v′=0,j′=0…9)의 제품 핵스핀 가중 |

원문의 직접 locator는 각각 [Bennett2003](https://doi.org/10.1046/j.1365-8711.2003.06422.x), [Bovino2009](https://arxiv.org/abs/0911.1281v1), [Honvault2013 정오표](https://doi.org/10.1021/jp4113377), [González-Lezana2022](https://doi.org/10.1063/5.0128598)다. 수치 table은 [sources/public_sources](../sources/public_sources)에 있고, 위 설명의 세부 필드는 source packet에 결속되어 있다.

## 2. source identity와 정수 모델 identity

분자 상태를 합치기 전에 두 종류의 identity를 구분한다. source-native identity는 논문이 명시한 isotope·전하·전자/진동/회전·spin 정보다. compiler용 declared identity는 보존량을 계산할 수 있도록 선택한 유한 모델의 핵 구성과 전하다.

LiH 두 논문의 7Li 지정은 유지한다. source의 H 표기에는 수소 질량수가 별도로 인쇄되어 있지 않다. 아래 정수 표에서는 **H를 1H, D를 2H로 결속한 모델**을 명시적으로 사용한다. 이를 6LiH·LiD·HT·DT의 rate 승인으로 확대하지 않는다. source-native nuclear-isomer 필드는 null이다. compiler 식별자가 nuclear ground g를 요구한다면 g는 이 단위의 모델 convention이며 원 논문에서 isomer별 rate를 측정했다는 뜻이 아니다. 전자 바닥상태, 핵 바닥상태, 분자 회전 바닥상태는 서로 다른 필드다.

아래 AΣ는 질량수의 합이며 질량 에너지가 아니다. ZΣ는 핵 전하수의 합이다. Nbound는 선택한 전하 상태에서 결합된 전자 수다.

| 물질 종 | (N1H,N2H,N7Li) | AΣ | ZΣ | q/e | Nbound |
|---|---|---:|---:|---:|---:|
| H | (1,0,0) | 1 | 1 | 0 | 1 |
| H⁺ | (1,0,0) | 1 | 1 | +1 | 0 |
| D⁺ | (0,1,0) | 2 | 1 | +1 | 0 |
| Li | (0,0,1) | 7 | 3 | 0 | 3 |
| H2 | (2,0,0) | 2 | 2 | 0 | 2 |
| HD | (1,1,0) | 3 | 2 | 0 | 2 |
| LiH | (1,0,1) | 8 | 4 | 0 | 4 |

각 분자의 spin·rovibrational 상태가 바뀌어도 같은 핵 구성과 전하를 가진다면 이 표의 보존량은 같다. 반대로 보존량이 같다는 사실은 서로 다른 상태의 rate를 대체할 근거가 아니다.

## 3. 여섯 supplier variant의 정확한 물질 수 사영

물질 순서를
\[
(H,\ H^+,\ D^+,\ {\rm Li},\ H_2,\ {\rm HD},\ {\rm LiH})
\]
로 둔다. 열 순서는 association A, ortho destruction Do, para destruction Dp, TIQM HD formation FT, SQM HD formation FS, thermal HD destruction R이다. 제품/반응물 상태를 물질 종으로 사영한 선언적 정수 행렬은
\[
S_{\rm mat}=
\begin{pmatrix}
-1&-1&-1&0&0&0\\
0&0&0&1&1&-1\\
0&0&0&-1&-1&1\\
-1&1&1&0&0&0\\
0&1&1&-1&-1&1\\
0&0&0&1&1&-1\\
1&-1&-1&0&0&0
\end{pmatrix}.
\tag{1}
\]

| 열 | 원 화학 방향 | 물질 입자수 변화 |
|---|---|---|
| A | Li+H→LiH, primary radiation 별도 | (−Li,−H,+LiH) |
| Do | LiH+H→Li+ortho-H2 | (−LiH,−H,+Li,+H2) |
| Dp | LiH+H→Li+para-H2 | 같은 물질 열, 다른 source 제품 spin |
| FT | D⁺+p-H2(v0,j0)→HD+H⁺ | (−D⁺,−H2,+HD,+H⁺) |
| FS | 같은 방향의 SQM 대안 | FT와 같은 물질 열 |
| R | H⁺+HD thermal ensemble→D⁺+H2 | FT의 반대 물질 열 |

이는 구현이 재사용할 수 있는 정수 명세다. 이 문서가 compiler를 실행했다는 뜻은 아니다. FT와 FS를 동시에 더하면 같은 물리 반응의 두 방법을 중복 계상한다. Do와 Dp는 원자료에서 분리된 제품 spin 총계지만, 합산하려면 동일 초기 상태 및 통계 정규화가 결속되어야 한다. 현재 그 조건을 추가하지 않는다.

### 보존량의 직접 확인

A열은 1H 하나와7Li 하나를 LiH에 옮긴다. D열은 LiH의1H와 충돌 H의1H를 H2에 옮기고7Li를 보존한다. F열은 D⁺의2H와 H2의1H 두 개를 HD 및 H⁺에 재배치한다. R은 그 반대다. 따라서 각 isotope 핵 개수의 행벡터 c에 대해 cSmat=0이다. 질량수 합
\[
a^T=(1,1,2,7,2,3,8)
\]
도 aTSmat=0을 만족한다.

전하 행은 qT=(0,1,1,0,0,0,0)이다. FT/FS에서 H⁺ 증가와 D⁺ 감소가 상쇄되고, R에서 반대로 상쇄되므로 qTSmat=0이다. 결합 전자 행
\[
e_b^T=(1,0,0,3,2,2,4)
\]
에 대해서도 A는 −1−3+4=0, D는 −1+3+2−4=0, F는 −2+2=0이다. 자유 전자·중성미자·반중성미자의 순 변화는 이 화학식들에서0이다. 따라서 결합/자유 전자를 합친 electron-lepton 수가 보존된다. 보존량을 맞추려고 source에 없는 전자나 광자를 물질 반응물에 추가하지 않는다.

원자·분자·이온 및 자유 전자를 각각 하나의 gas particle로 세고 photon은 제외하는 모델의 계수 행을 gT로 둔다. 이 여섯 열은 자유 전자 변화가 없으므로 여기서는 gT=1T이고
\[
g^TS_{\rm mat}=(-1,0,0,0,0,0).
\tag{2}
\]
association은 두 gas particle을 한 분자로 바꾸므로 ΔNg=−1, 나머지는2→2이므로 ΔNg=0이다. 이 counting identity는 방출/생성물이 즉시 특정 thermal bath에 동화된다는 주장이나 온도 방정식이 아니다.

Bennett의 elementary association에는 primary radiative transition 하나를 별도 ledger에 붙일 수 있다. survival-weighted 집계에서 총 cascade photon 수, photon bin, spectrum, energy partition은 null이다. 따라서 식(2)에 photon을 넣어 ΔNg를0으로 바꾸지 않는다. 모든 열의 채택된 Q와 소비자 energy source는 null이다.

## 4. proper time, 물리 밀도, reference당 사건률

proper time을 τ로 쓰고 단위는 s로 둔다. nA,nB는 동일한 국소 물리 부피 기준 number density, 단위 cm⁻³다. binary 계수 k의 단위는 cm³ s⁻¹이므로
\[
\mathcal R=k\,n_A n_B
\quad [\mathrm{events\ cm^{-3}\ s^{-1}}],
\qquad
\left.\frac{dn_i}{d\tau}\right|_{\rm react}
=\sum_a S_{ia}\mathcal R_a.
\tag{3}
\]
이 여섯 공급자의 입사 반응물은 서로 다르다. H2 내부의 동일한 두 H 또는 final-state spin을 이유로 입사쌍1/2를 추가하지 않는다. 공급자 내부의 전자·핵스핀 가중과 이 사건 pair counting은 별개다.

양의 물리 reference density nref [cm⁻³]를 실제 소비자가 정하고 yi=ni/nref로 정의하면
\[
j_a=\frac{\mathcal R_a}{n_{\rm ref}}
=k_a\,n_{\rm ref}\,y_Ay_B
\quad[\mathrm{s^{-1}}].
\tag{4}
\]
이는 reference particle당 proper-second 사건 수다. k 또는 R를 단위와 정규화 없이 j로 바꿀 수 없다.

reference가 해당 반응에 대해 보존되는 경우에만 반응 부분은
\[
\left.\frac{dy_i}{d\tau}\right|_{\rm react}
=\sum_a S_{ia}j_a
\tag{5}
\]
다. 일반적으로는 정확한 미분식
\[
\frac{dy_i}{d\tau}
=\frac{1}{n_{\rm ref}}\frac{dn_i}{d\tau}
-y_i\,\frac{d\ln n_{\rm ref}}{d\tau}
\tag{6}
\]
를 사용해야 한다. 예컨대 nref를 gas-particle density로 잡으면 association 때문에 그 reaction derivative가0이 아니다. 우주 팽창의 희석항이나 다른 background 항도 식(6)과 일관되게 처리해야 한다. 이 문서는 실제 nref를 선택하지 않는다.

소비자의 좌표 시간이 t라면 reaction contribution에 dτ/dt를, 무차원 시간이 u=τ/t0라면 t0를 곱한다. 현재 dτ/dt, t0, comoving/physical density map은 공급자가 제공하지 않으므로 consumer contract의 필수 입력이다. 현재 rate가 어떤 cosmological clock에 이미 결속됐다는 가정은 없다.

## 5. 집계를 위한 표현 선택

R4에서는 다음 세 표현의 정확한 차이를 사용한다.

| 표현 | 필요한 입력 | 보장되는 것 |
|---|---|---|
| 상태별 벡터 x를 유지 | 각 상태의 계수 di와 collider density h | 주어진 유한 모델의 정확한 상태별 flux |
| 총량 X만 유지하고 π를 명시 | 정규화된 비음수 lift π와 같은 상태족의 d | 선택한 manifold x=πX에서 정확; 실제 x와 다르면 아래 defect를 계산 |
| source의 열적 집계 계수를 직접 유지 | source의 ensemble과 소비자 ensemble이 일치한다는 별도 결속 | 그 결속 범위의 집계 계수만 사용 가능 |

현 입력에는 LiH formation branching b, LiH 파괴의 완전 state vector d, 실제 population lift π가 모두 주어져 있지 않다. 그러므로 구현 명세는 **π를 명시적으로 요구하는 조건부 lift**를 채택한다. 임의 LTE·Boltzmann·ground-only 분포를 default로 생성하지 않는다. González-Lezana의 Boltzmann 평균은 해당 source가 정의한 aggregate를 설명하며, 다른 공급자나 실제 population의 LTE를 증명하지 않는다.

## 6. 비음수 state lift와 정확한 defect

### 정리1: lift의 보존·양성 및 flux 항등식

유한한 상태족 I={1,…,m}, m≥1을 고정한다. 한 temperature 및 외부 parameter 값에서 다음을 가정한다.

- xi≥0는 상태별 물리 밀도 [cm⁻³]이고 X=Σixi다.
- di≥0는 **같은 반응 방향·같은 collider 정의**의 알려진 상태별 계수 [cm³ s⁻¹]다.
- h≥0는 그 collider의 물리 밀도 [cm⁻³]다.
- πi≥0, Σiπi=1이며 모든 수는 유한하다.

lift Lπ(X)=πX는 비음수이며 1TLπ(X)=X다. 집계 계수와 두 flux를
\[
k_\pi=d^T\pi,\qquad
J=h\,d^Tx,\qquad
J_\pi=h\,k_\pi X
\tag{7}
\]
로 정의하면 kπ≥0, J≥0, Jπ≥0이고
\[
\Delta J:=J-J_\pi
=h\,d^T(x-\pi X).
\tag{8}
\]

**증명.** πiX≥0이고 ΣiπiX=X다. 식(7)의 각 합은 비음수 항들의 합이다. dTπX=(dTπ)X를 이용하여 J−Jπ를 전개하면 식(8)을 얻는다. X=0이면 모든 xi=0이므로 두 flux와 defect가 모두0이며 x/X를 계산할 필요가 없다. □

상태별 파괴항을 \(\dot x_i|_{\rm dest}=-h d_i x_i\)로 쓰면 경계 xi=0에서 해당 제거항도0이다. 고정된 비음수 d,h의 유한 model에서 이 제거항은 양성을 보존한다. 이는 현재 표가 그 di를 모두 제공한다는 주장과 구별한다.

### 정리2: zero-sum 잔차의 진폭 bound

dmin=mini di, dmax=maxi di라 두면
\[
\boxed{
|\Delta J|
\le
\frac{h(d_{\max}-d_{\min})}{2}
\|x-\pi X\|_1 .
}
\tag{9}
\]
또한 \(\|x-\pi X\|_1\le2X\)이므로
\[
|\Delta J|\le hX(d_{\max}-d_{\min}).
\tag{10}
\]

**증명.** r=x−πX라 두면
\[
1^Tr=1^Tx-(1^T\pi)X=X-X=0.
\]
따라서 임의의 실수 c에 대해 dTr=(d−c1)Tr다. c=(dmax+dmin)/2를 선택하면
\[
\begin{aligned}
|d^Tr|
&=\left|\sum_i(d_i-c)r_i\right|\\
&\le\sum_i|d_i-c||r_i|\\
&\le\frac{d_{\max}-d_{\min}}{2}\sum_i|r_i|.
\end{aligned}
\]
h≥0를 곱하여 식(9)를 얻는다. x≥0 및 πX≥0에 대해 두 벡터의 L1 norm이 각각 X이므로 삼각부등식에서 \(\|r\|_1\le2X\)다. □

X>0일 때 p=x/X는 실제 state fraction이므로 식(9)는
\[
|\Delta J|\le
hX(d_{\max}-d_{\min})\,{\rm TV}(p,\pi),
\quad
{\rm TV}(p,\pi)=\tfrac12\|p-\pi\|_1
\tag{11}
\]
와 같다. 이것은 실제 알려진 d와 x,π 사이의 **deterministic closure defect bound**다. 계수의 물리 불확실성·source fit residual·covariance를 대신하지 않는다. 현재 미지의 di를 aggregate 표 한 열로 채워 dmax−dmin을0으로 놓을 수 없다.

## 7. 정확한 scalar closure의 필요충분조건

### 정리3: 전체 상태 cone에서의 scalar criterion

고정된 d와 **숨은 x에 의존하지 않는 prescribed π**에 대해, h>0라고 하자. admissible state family의 각 state에 임의의 비음수 밀도를 배정할 수 있어 x가 전체 \(\mathbb R_{\ge0}^m\)를 달린다고 가정한다. 이때 다음 조건은 동치다.

1. 모든 x≥0에 대해 J=Jπ다.
2. 어떤 실수 c≥0에 대해 d=c1이다.
3. dTz=0이 모든 z∈ker(1T)에 대해 성립한다.

**증명.** 2이면 kπ=cΣiπi=c이고 J=hcX=Jπ이므로1이다. 1을 가정하고 임의의 X0>0 및 표준기저 ei에 대해 x=X0ei를 대입하면 hX0di=hX0kπ다. hX0>0이므로 모든 i에 대해 di=kπ이며2를 얻는다. 2이면 1Tz=0인 z에 대해 dTz=c1Tz=0이므로3이다. 3이면 ei−ej가 ker(1T)에 있으므로 di−dj=0이고2다. □

이 필요충분조건에는 범위가 있다.

- h=0이면 d가 비상수여도 모든 flux가0이다. 이 경우로 d의 상수성을 추론하지 않는다.
- 제한된 manifold x=πX 위에서만 exactness를 요구하면 비상수 d도 항상 정확하다.
- 매번 실제 x를 알고 π=x/X로 고르면 exactness는 자명하지만, 총량 X만으로 독립적으로 닫힌 모델을 얻은 것은 아니다.
- 허용될 수 없는 state를 family에 넣거나, 실제 가능한 population을 임의로 줄여 필요조건을 바꾸지 않는다.

따라서 이 결과는 보편적인 물리 불가능성 또는 strong no-go가 아니다. 어떤 상태 정보를 지워도 flux가 보존되는지 판별하는 일반적인 선형 closure criterion이다. 신규성도 주장하지 않는다.

### 일반 선형 사영 P

P가 유한 차원 상태를 집계하는 실수 선형 사영이고 observable이 dTx라고 하자. 전체 비음수 cone에서 dTx가 Px만으로 결정될 필요충분조건은
\[
d^Tz=0\quad(z\in\ker P),
\tag{12}
\]
또는 동치로 어떤 행벡터 \(\bar d^T\)에 대해
\[
d^T=\bar d^TP
\tag{13}
\]
가 존재하는 것이다.

**증명.** 식(13)은 충분하다. 역으로 dTx가 Px만으로 결정된다면, z∈kerP를 양·음 부분 z=z+−z−로 나눈다. z±≥0이고 Pz+=Pz−이므로 dTz+=dTz−, 즉 dTz=0이다. 식(12)가 성립하면 Px라는 값에 \(\ell(Px)=d^Tx\)를 대응시켜도 표현 x에 의존하지 않는다. 이 \(\ell\)은 imP 위의 선형 functional이다. 이를 공역의 기저까지 연장하면 \(\bar d^T\)를 얻는다. □

물리적으로 허용된 domain이 전체 cone의 진부분집합이면 필요한 조건은 같은 Px를 갖는 **허용 상태들의 차이**를 d가 소거하는 것이다. 전체 kerP를 소거해야 한다는 결론은 그 더 작은 domain에 자동 적용하지 않는다. 또한 일반 P가 양의 lift를 항상 갖는다고 주장하지 않는다. 이 단위에서 실제 사용하는 양의 lift는 정리1의 scalar simplex π다.

## 8. formation branch와 전체 RA flux

유한한 LiH 제품 상태족이 동일한 핵 구성과 전하를 갖고, formation branch bi≥0, Σibi=1이 실제로 공급된다고 가정한다. 알려진 aggregate association flux F≥0에 대해
\[
\left.\dot x\right|_{\rm form}=bF
\quad\Longrightarrow\quad
\left.\dot X\right|_{\rm form}=1^TbF=F.
\tag{14}
\]
따라서 total formation number flux는 branch의 세부값과 무관하다. 모든 제품 state가 같은 보존량을 가지므로 −Li,−H,+b라는 상태별 열은 정수 물질 열 A와 같은 핵·전하·전자 ledger로 사영된다. 비음수 bF는 population 양성도 보존한다.

현재 Bennett 총계가 제공하는 것은 F를 구성하는 source coefficient이며, 안정화 뒤의 완전한 유한 branch vector b는 없다. “b가 존재한다고 가정하면 어떤 b에서도 total flux가 같다”는 증명이 b를 회수했다는 뜻은 아니다. 준결합 생존 가중까지 포함한 source aggregate를 어떤 실제 제품 family에 배정할지도 별도 계약이다.

b는 새로 형성된 분자의 product branching이고 π는 이후 전체 population의 state fraction이다. 충돌·복사전이·파괴가 작용하므로 b=π를 자동 가정하지 않는다. 이후 파괴 flux h dTx까지 total X만으로 정확해지려면 정리3의 조건 또는 실제로 결속된 population manifold가 추가로 필요하다.

## 9. 작은 유리수 예: 같은 총량과 다른 파괴 flux

아래는 **대수적 이론 예이며 source data가 아니다**. 두 상태의 계수를 d=(1,3)κ, κ>0 [cm³ s⁻¹], prescribed lift를 π=(1/2,1/2)로 둔다. X0>0 및 h>0를 고정하고
\[
x^{(a)}=(X_0,0),\qquad
x^{(b)}=(0,X_0)
\]
를 택하면 두 총량은 모두 X0지만
\[
J^{(a)}=\kappa hX_0,\qquad
J^{(b)}=3\kappa hX_0,\qquad
J_\pi=2\kappa hX_0.
\tag{15}
\]
각 defect는 −κhX0, +κhX0다. 각 잔차의 L1 norm은 X0이고 dmax−dmin=2κ이므로 식(9)의 우변은 κhX0다. 따라서 이 예에서는 bound가 등호를 이룬다.

이는 총량만 같은 임의의 두 상태를 하나의 계수로 대체할 수 없음을 보여 주는 반례다. 실제 LiH·HD에 d=(1,3)κ를 배정하지 않았으며, source fit을 평가하거나 population을 시뮬레이션하지 않았다.

## 10. native fit의 정확한 함수 정의와 검사 domain

### Bennett association fit

\[
\theta=\frac{T}{1000\,{\rm K}},\qquad
k_{\rm B03}(T)=10^{-20}
\left[
3.22+\frac{1}{0.0657\,\theta^{-2.45}
+0.00631\,\theta^{0.837}}
\right]\ {\rm cm^3\,s^{-1}}.
\tag{16}
\]
입력 십진수는 원문 literal로 유지한다. algebra에서
\[
3.22=\frac{161}{50},\quad
0.0657=\frac{657}{10000},\quad
0.00631=\frac{631}{100000},\quad
-2.45=-\frac{49}{20},\quad
0.837=\frac{837}{1000}
\]
로 정확히 표현할 수 있다. 이는 공급자의 정밀도보다 많은 물리 유효숫자를 얻었다는 뜻이 아니다.

T>0에서 \(\theta^r:=\exp(r\ln\theta)\)로 양의 실수 branch를 정의한다. 두 denominator 항이 양수이므로 분모는0이 아니고 kB03>0이다. 따라서 fractional power를 정수 지수처럼 반올림하거나 T≤0의 복소 branch로 확장할 이유가 없다.

함수의 수학적 domain T>0, 원표 support50–10000 K, 실제 계약의 **27개 native node** 진단은 각각 구분한다. 양의 함수라는 증명은 온도 외삽의 물리 승인과 무관하다. source는 약800 K 이상 약5%, 저온 최대20%의 fit residual을 서술하지만 이것을 엄밀한 전역 오차 bound나 physical covariance로 쓰지 않는다.

### HD destruction fit

\[
k_{\rm GL22}(T)=8.57\times10^{-10}
\exp\!\left(-\frac{405\,{\rm K}}{T}\right)
\ {\rm cm^3\,s^{-1}}.
\tag{17}
\]
T>0이면 양수다. 원 계산의5–3000 K 범위와 별도로 확정된 fit validity interval은 구별한다. 현재 계약의 진단은 원 논문에 직접 인쇄된205 K와295 K 두 SQM 값으로 제한된다. γ=405 K는 원fit의 parameter이며 Q, 상태별 threshold 또는 detailed-balance exponent를 새로 승인하지 않는다.

원fit과 원표의 비교량은 각 native node에서
\[
r_j=\frac{k_{\rm fit}(T_j)}{k_{{\rm table},j}}-1
\tag{18}
\]
로 명확히 정의할 수 있다. 이것은 함수 구현과 인쇄 표의 재현성 진단이다. 이 문서는 rj를 계산하지 않았으며, 검사 결과에 맞추어 공급자가 서술한 정확도를 변경하지 않는다. 후속 문헌의 HD fit30% 평가는 원 두 점의 통계오차가 아니다. [Faure et al.2024 §2.2.6](https://academic.oup.com/mnras/article/531/1/340/7644349)

Bovino의 aT exp(−bT)는 원문 b 단위 K와 차원상 필요한 K⁻¹의 충돌을 보존하고 이번 fit 평가에서 제외한다. Honvault 두 방법은 native 표로만 보존하며 보간·외삽·방법 평균을 추가하지 않는다.

## 11. source와 실제 소비자 사이의 남은 결속

이 정리를 구현 guard로 쓰려면 d,π,b를 서로 다른 의미의 입력으로 유지해야 한다. 각각이 실제로 공급되지 않으면 null을0이나 ground-state delta로 바꾸지 않는다. state-resolved coefficients가 없는 aggregate table에서 임의 d 벡터를 구성해 식(9)를 수치평가할 수 없다. 물리 population x가 없으면 실제 defect도 미지다.

Bennett의 p=1/4는 source에 이미 포함되어 있다. González-Lezana의 even/odd 핵스핀 가중1/4,3/4도 원 집계fit에 포함되어 있다. 두 source의 숫자가 같다고 같은 통계 인자를 뜻하는 것은 아니다. Bovino 두 spin 총계의 원 정규화는 이들로 추측하지 않는다. [Bennett §2.2](https://doi.org/10.1046/j.1365-8711.2003.06422.x), [González-Lezana §III.A](https://doi.org/10.1063/5.0128598)

HD formation의 입사 p-H2(v0,j0)와 HD destruction의 thermal HD(v0,j0…8)는 서로 다른 ensemble이다. 식(1)에서 R=−FT가 성립해도, microscopic state pairing·통계중량·partition function·temperature convention·energy zero가 결속되지 않아 두 공급자를 detailed-balance pair로 승인할 수 없다. LiH RA 제품의 survival-weighted aggregate도 Bovino의 미명시 initial v/j와 자동 동일시하지 않는다.

Bovino의2.258 eV는 source가 추정한 exothermicity라는 provenance를 유지한다. 선택한 최종 H2(v′,j′), bound-electron mass convention, photon/collider/thermal energy ownership이 없는 상태에서는 Q 입력으로 사용할 수 없다. 모든 physical Q·energy partition·named consumer·runtime activation은 현재 null/false다. source의 부분/총합 mismatch와 fit unit 문제는 [AUXILIARY_SOURCE_ISSUES.json](../sources/AUXILIARY_SOURCE_ISSUES.json)에 그대로 남아 있다.

## 12. 구현에 전달하는 조건과 판정 상태

이 문서가 요구하는 최소 interface는 유한 state family와 동일 순서의 d,x,π, collider h, 명시적인 물리 density/clock/reference convention이다. 모든 값은 유한하며 비음수여야 하고 π의 합은1이어야 한다. branch b를 쓰는 연산은 동일한 정규화 조건을 독립적으로 요구한다. 입력 오차를 조용히 clip하거나 재정규화하여 source와 다른 모델을 만들지 않는다. 구현 허용오차를 쓰면 그 수학적 조건과 별도로 명시하고 결과에 기록해야 한다.

현재 채택한 결과는 식(1)의 선언적 물질 수 사영, 식(8)의 defect 항등식, 식(9)의 조건부 bound, 정리3의 scalar criterion, 식(12)–(13)의 일반 선형 factorization, 식(14)의 formation total 보존이다. source missing state는 이 결과를 얻는 데 숨긴 가정이 아니라 적용 전에 채워야 할 명시적 입력이다.

독립 검토와 bounded 구현 검증 전에는 이론 저자의 증명 상태만 기록한다. 그 이후에도 source-fit implementation acceptance는 empirical physical rate, nuclear Q, energy partition, consumer 또는 production 승인을 뜻하지 않는다. PHYS91 remaining0과 global historical budget null은 유지한다.
