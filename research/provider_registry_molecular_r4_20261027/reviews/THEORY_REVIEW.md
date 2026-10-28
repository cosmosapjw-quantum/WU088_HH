# R4 R6 독립 physics review

## 판정과 입력

**판정: ACCEPT_CONDITIONAL_THEORY.** 실제 이론 문서와 13개 claim을 읽고 핵심 수학적 전이를 독립적으로 유도했다. Blocking defect와 필수 수정은 없다. 이 판정은 명시된 유한 상태 모델과 가정 아래의 조건부 수학에 대한 것이다. 실제 상태 population, rate/Q, consumer 또는 production의 결속을 요구하거나 승인하지 않는다.

| 입력 | SHA256 |
|---|---|
| STATE_LIFT_THEORY_KO.md | eb62a104974a278211c77fb5037bffd00ef4f157acd6911b6e2c46f0bd3fef68 |
| CLAIMS.json | e04353625155ca0f5fab09ef638d63ae96d3ebc84f6ede3b4a2326d3cca634f1 |
| MOLECULAR_SOURCE_PACKET.json | 40e2fbd73d451c0c8116b4ca9bd4db4d2e43e4cdf8967988a2fea551f99ce35e |
| CONTRACT.json | 6a40c43c04aa4506281f2021a6879e76e94d560ea3cc8af3c7cdfeffb15eb8bc |

검토자는 /root/molecule_sources이고 이론 저자 /root/provider_rows 및 구현 작성자와 구별된다. Source packet의 현재 SHA를 직접 재확인했으므로 기존 77개 셀 source 검토를 재사용한다. 그 77개 셀을 다시 대조하지 않았다. 원래 source-review 파일의 정확한 바이트가 유실되어 복원 receipt를 사용하는 사실, Bennett 원 raw 파일의 현재 미복구, Honvault 원 PDF의 미확보도 유지된다. 이론의 숫자·source 정의를 새로 만들지 않았다.

이번 node에서는 최신 AGENTS의 R4 지침, 실제 local HEAD e9276ea2ba8af2d73197a6852931fcafbf39ddf5, authority/S03_PREFLIGHT.json의 2026-10-27T06:03:48.748Z 원격·병렬 SHA 관측, delivery/S02.json을 읽었다. S02 source ZIP의 SHA는 91d94753261582fcf03d9f1ef6056c1cd3de180326fb0c608c07776d9adf816f이고 Dropbox/Drive actual upload ACK가 있다. Final full-source 원격 byte readback은 별도 절차다. 외부 미게시 작업의 상태를 안다고 주장하지 않는다.

## 1. 화학식에서 다시 구성한 수 보존 행렬

행 순서를 \((H,H^+,D^+,Li,H_2,HD,LiH)\), 열 순서를 \((A,D_o,D_p,F_T,F_S,R)\)로 두고, 각 반응의 반응물에 −1, 생성물에 +1을 배정하여 독립 재구성했다.

\[
S=
\begin{pmatrix}
-1&-1&-1&0&0&0\\
0&0&0&1&1&-1\\
0&0&0&-1&-1&1\\
-1&1&1&0&0&0\\
0&1&1&-1&-1&1\\
0&0&0&1&1&-1\\
1&-1&-1&0&0&0
\end{pmatrix}.
\]

이는 검토 대상의 행렬과 일치한다. 동위원소 핵 수를 세는 행렬은

\[
C=
\begin{pmatrix}
1&1&0&0&2&1&1\\
0&0&1&0&0&1&0\\
0&0&0&1&0&0&1
\end{pmatrix},
\]

이며 행들은 각각 \(^{1}H,{}^{2}H,{}^{7}Li\)이다. 각 화학 방향에서 이 세 핵 수를 직접 세면 \(CS=0\)이다. 이 결과에서 질량수 행은 \(a^T=C_{1H}+2C_{2H}+7C_{7Li}=(1,1,2,7,2,3,8)\), 핵 전하수 행은 \(Z^T=C_{1H}+C_{2H}+3C_{7Li}=(1,1,1,3,2,2,4)\)로 얻는다.

전하 행 \(q^T=(0,1,1,0,0,0,0)\)은 formation에서 \(+H^+\)와 \(-D^+\)가 상쇄되어 \(q^TS=0\)이다. 결합 전자 수는 \(e_b^T=Z^T-q^T=(1,0,0,3,2,2,4)\)이다. 대표 세 방향의 직접 검산은 다음과 같다.

| 방향 | 질량수 합 변화 | 결합 전자 수 변화 | gas-particle 수 변화 |
|---|---|---|---:|
| RA | \(-1-7+8=0\) | \(-1-3+4=0\) | −1 |
| LiH destruction | \(-1+7+2-8=0\) | \(-1+3+2-4=0\) | 0 |
| HD formation | \(1-2-2+3=0\) | \(-2+2=0\) | 0 |

두 spin-labelled destruction 열은 같은 물질 사영이며, 두 formation 방법도 같은 물질 사영이다. HD destruction 열은 formation 물질 열의 음수다. 자유 전자·중성미자 순 변화가 없으므로 결합/자유 전자를 포함한 electron-lepton 수가 보존된다.

이는 H=1H, D=2H, Li=7Li로 선언한 모델에 대한 정확한 결과다. Source-native H 질량수와 nuclear-isomer 미명시를 물리적 isotope/isomer rate 승인으로 바꾸지 않는다. 또한 같은 물질 열이라는 사실로 spin channel 정규화, 방법 중복 합산, source ensemble의 detailed balance를 승인하지 않는다.

\(\mathbf1^TS=(-1,0,0,0,0,0)\)이다. Photon은 gas-particle count에서 제외한다. RA의 elementary primary transition 하나와 survival-weighted 성공 사건 뒤의 전체 cascade photon 수는 별개다. 후자의 수·spectrum·energy partition은 현재 미지라는 문서의 경계가 타당하다.

## 2. Lift, defect와 bound의 독립 유도

고정된 유한 상태족에서 \(x_i,d_i,h,\pi_i\)가 유한·비음수이고 \(\sum_i\pi_i=1\), \(X=\sum_i x_i\)라 하자. 그러면 \(\pi X\ge0\)이고 합은 \(X\)다. 따라서

\[
J=h\,d^Tx,\qquad J_\pi=h(d^T\pi)X,\qquad
\Delta J=h\,d^T(x-\pi X)
\]

는 부호와 차원이 일관된다. \(X=0\)에서는 비음수성 때문에 \(x=0\)이며 \(x/X\)를 계산할 필요가 없다. 고정된 비음수 \(h,d_i\)의 제거항 \(-hd_ix_i\)도 경계에서 0이 되어 양성을 보존한다.

저자의 midpoint proof와 다른 방식으로 half-spread bound를 확인했다. \(r=x-\pi X\)이면 \(\mathbf1^Tr=0\)이다. 양·음 부분으로 \(r=r^+-r^-\)를 쓰면

\[
M:=\mathbf1^Tr^+=\mathbf1^Tr^-=\frac12\|r\|_1.
\]

각 \(d^Tr^\pm\)는 \([d_{\min}M,d_{\max}M]\)에 있으므로 그 차이는 \([-M(d_{\max}-d_{\min}),M(d_{\max}-d_{\min})]\)에 있다. 따라서

\[
|\Delta J|
\le \frac{h(d_{\max}-d_{\min})}{2}\|x-\pi X\|_1.
\]

또한 \(\|x\|_1=\|\pi X\|_1=X\)이므로 \(\|r\|_1\le2X\)이다. \(X>0\)에서의 total-variation 표현도 이에 정확히 동치다. 이 bound는 알려진 \(d,x,\pi,h\)의 deterministic closure defect에 관한 것이며, 공급자 covariance·fit residual·물리적 불확실성의 대체물이 아니다. Aggregate 표로 미지의 \(d_i\)를 일괄 동일하게 채워 spread를 0으로 만들 수 없다.

## 3. Scalar exactness와 일반 선형 사영

전체 비음수 cone, \(h>0\), 숨은 \(x\)와 독립적으로 prescribed된 \(\pi\)라는 가정 아래, 같은 \(X_0>0\)를 갖는 pure populations \(X_0e_i\)와 \(X_0e_j\)를 비교한다. 둘 모두 하나의 scalar coefficient에 정확해야 하므로 \(hX_0d_i=hX_0d_j\), 따라서 모든 \(d_i\)가 같다. 역으로 \(d=c\mathbf1\)이면 \(d^T\pi=c\)이고 두 flux는 \(hcX\)로 같다. \(e_i-e_j\)가 zero-sum subspace를 생성하므로 \(\ker(\mathbf1^T)\) 소거 조건도 동치다.

\(h=0\)에서는 이 필요조건을 추론할 수 없다. 제한된 manifold \(x=\pi X\)에서는 임의의 \(d\)에도 정확하며, \(\pi=x/X\)를 사용하면 숨은 상태를 이미 알고 있는 것이므로 독립적인 scalar closure가 아니다. 이 예외들이 실제 문서와 CLAIMS에 모두 있어 명제의 범위가 적절하다.

일반 \(P\)에서도 필요성의 핵심은 전체 cone이다. \(z\in\ker P\)에 대해 \(z=z^+-z^-\), \(z^\pm\ge0\)로 두면 \(Pz^+=Pz^-\)다. Observable이 \(Px\)만으로 정해지면 \(d^Tz^+=d^Tz^-\), 즉 \(d^Tz=0\)이다. 이 소거 조건은 \({\rm im}P\) 위의 well-defined linear functional을 만들고, 유한 차원에서 이를 공역에 연장하여 \(d^T=\bar d^TP\)를 얻는다. 역방향은 이 factorization에서 즉시 따른다.

제한된 물리 domain에는 같은 \(P\)-값을 갖는 허용 상태들의 차이만 소거하면 된다. 일반 \(P\)에 항상 positive lift가 있다는 추가 주장은 없다. 따라서 보편적 물리 불가능성이나 strong no-go, 신규성 주장을 만들지 않는다.

## 4. Formation branch의 의미와 작은 예

\(b_i\ge0,\sum_i b_i=1,F\ge0\)가 실제 제공된 조건에서는 \(\dot x|_{\rm form}=bF\)를 합하여 \(\dot X|_{\rm form}=F\)를 얻는다. 제품 상태들이 같은 물질 보존량을 갖는다는 가정도 충분하다. 현재 source가 \(b\)를 주었다거나 이후 population \(\pi\)와 \(b\)가 같다는 뜻은 아니다.

**비차단 명확화 한 건:** 문서 §8의 \((-Li,-H,+b)\)는 평균 flux 계수로 읽어야 한다. 각 개별 state-channel 사건은 제품 분자 하나와 정수 stoichiometry를 갖고, \(b_i\)가 그 채널을 가중한다. 즉

\[
\sum_i b_i F\,s_i
\]

가 평균 influx이고, 그 물질 사영이 \(F S_A\)다. 개별 사건의 생성물 수를 \(b_i\)라는 분수로 compiler에 전달하는 해석은 허용하지 않는다. 현 정리의 오류는 아니며 원문 수정이 acceptance의 선행 조건도 아니다. 후속 코드에서는 branch-lift와 integer event column을 구별해야 한다.

두 상태 예는 \(d=(1,3)\kappa,\pi=(1/2,1/2)\), \(x^{(a)}=(X_0,0)\), \(x^{(b)}=(0,X_0)\)에서 flux가 각각 \(\kappa hX_0,3\kappa hX_0\), prescribed flux가 \(2\kappa hX_0\)이다. 각 residual의 L1 norm이 \(X_0\)이고 spread가 \(2\kappa\)이므로 defect 크기와 bound는 모두 \(\kappa hX_0\)다. 등호 성립이 대수적으로 확인되며 실제 LiH·HD 계수를 지정하거나 수치 실행한 예가 아니다.

## 5. Density, time과 fit 정의

\([k]={\rm cm^3\,s^{-1}}\), \([n_A]=[n_B]={\rm cm^{-3}}\)에서 \(\mathcal R=kn_An_B\)의 단위는 사건수 \({\rm cm^{-3}\,s^{-1}}\)다. \(n_{\rm ref}>0\), \(y_i=n_i/n_{\rm ref}\)를 대입하면

\[
j=\mathcal R/n_{\rm ref}=k n_{\rm ref}y_Ay_B,\qquad
\frac{dy_i}{d\tau}
=\frac1{n_{\rm ref}}\frac{dn_i}{d\tau}
-y_i\frac{d\ln n_{\rm ref}}{d\tau}
\]

가 된다. Reaction-only denominator 항을 버릴 수 있는 조건이 명시되어 있다. Gas-particle reference는 RA에서 변하고, 보존된 핵 수를 reference로 잡는 경우는 다르다. Clock factor, comoving/physical density map을 consumer에 남긴 것도 타당하다. 여섯 공급자의 입사쌍은 서로 다른 종이므로 입사쌍 \(1/2\)를 더하지 않는다.

Bennett fit의 십진수와 유리수 표현 \(161/50,657/10000,631/100000,-49/20,837/1000\)은 정확히 대응한다. \(T>0\)에서 \(\theta^r=\exp(r\log\theta)>0\)이고 분모가 양수라는 증명도 맞다. HD fit의 양성 역시 같은 domain에서 성립한다. 이는 source의 실제 지원 온도, fit validity 또는 물리적 외삽 승인과 별개다. 진단 범위 27+2 nodes를 넓히지 않았으며, 이번 리뷰에서 함수값이나 residual을 계산하지 않았다.

Bennett의 기존 electronic \(1/4\), HD aggregate의 기존 even/odd \(1/4,3/4\) 가중은 다시 적용하지 않는다. Bovino 단위 문제와 auxiliary discrepancy, HD의 405 K가 fit parameter라는 경계도 기존 source 검토에 맞게 유지된다. HD formation의 p-H2 입사 ensemble과 destruction의 thermal HD ensemble을 물질 역반응 관계만으로 detailed-balance pair로 묶지 않는다.

## 6. Claim별 결론

| Claim | 독립 판정 |
|---|---|
| C01 material stoichiometry | 선언된 isotope 모델에서 보존량과 7×6 행렬 일치 |
| C02 thermal-particle count | counting identity 승인; thermal assimilation·Q는 제외 |
| C03 event normalization | density·clock·reference 조건 아래 정확 |
| C04 positive lift | 유한·비음수·정규화 가정 아래 정확 |
| C05 defect identity | 정확한 대수 항등식 |
| C06 zero-sum bound | 독립 유도로 half-spread와 zero cases 확인 |
| C07 scalar exactness iff | \(h>0\), full cone, fixed lift 가정 및 예외 적절 |
| C08 general projection | kernel 소거와 row-space factorization 동치 확인 |
| C09 formation total | 조건부 평균 flux identity 승인; integer-channel 해석 유지 |
| C10 rational example | 대수적 반례와 bound 등호 성립 확인 |
| C11 native fit functions | literal algebra·positive domain 정의만 승인 |
| C12 weights and Q guards | 이전 source 의미 재사용; 중복 가중·Q 승격 없음 |
| C13 ensemble compatibility | 현재 미결속 입력을 적절히 분리 |

## 7. 실행·승인의 경계

이번 reviewer의 native fit/rate 평가, 새 native-cell 비교, Q/partition function 평가, compiler, Wolfram, IVP, 기존249·R1·R2·R3·PHYS91·REI 재실행은 모두 0회다. 문서 읽기와 SHA 확인, 리뷰 파일 작성·JSON 문법 확인만 수행한다. 도구 및 준비 비용은 측정하지 않았으며 0이라고 주장하지 않는다. Root가 별도 preflight 뒤 수행할 단 한 번의 Wolfram 요청을 이 리뷰가 대신 실행하거나 선승인하지 않는다.

후속 구현 검토와 계산 진단은 별도 상태다. 조건부 이론의 독립 검토를 통과해도 empirical physical rate, Q, energy partition, population lift의 consumer 결속, named runtime consumer, activation은 false다. HH_R10=OFF, production=NOT_ISSUED, L4_ready=false와 기존 예산을 유지한다.
