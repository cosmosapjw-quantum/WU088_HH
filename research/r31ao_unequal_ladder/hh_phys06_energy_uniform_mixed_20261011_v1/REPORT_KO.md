# WU088_HH PHYS06 — 에너지 구조와 유한 혼합 차이의 조건부 상계

작성일: 2026-10-11 KST. 최종 독립 판정은 `review/DECISION.json`과
`review/REVIEW_KO.md`에 기록한다. 물리/production 상태는 **HOLD**다.

## 1. 이번 루프의 결론

PHYS06은 에너지 좌표에서 reduced H/He 광흡수의 정확한 곡률 구조를 얻고,
실제 저장 상태로 그 구조를 경량 검산했다. 또 **매개변수 사각형 전체의
implicit root와 혼합 미분을 포함할 수 있으면, 유한한 네 모서리 interaction을
별도 parameter Taylor 나머지 없이 제한할 수 있다**는 연결을 증명하고
실행 가능한 exact rational reference로 만들었다.

동시에 실제 소스의 두 가지 산술 차이를 발견해 보존했다. 하나는
`fl(nH*fHe)/nH`와 `fHe`의 차이, 다른 하나는 `fl(E-chi)`의 excess-energy
leaf 차이다. 이들을 지워야만 성립하는 보존량이라고 보고하지 않는다.
직접적인 residual 좌표변환을 기본으로 두고, 축약식에는 필요한 잔차를 남긴다.

이번에 실제 새 native endpoint, BE point/root solver, IVP 또는 과거 연구
suite를 실행한 횟수는 모두 **0**이다. 따라서 actual W, finite I_h, mixed
scheme defect 또는 continuous-time error의 수치/부호를 얻었다고 주장하지 않는다.

## 2. 어디에서 이어받았는가

| 항목 | 확인한 상태 | 이번 루프에서의 처리 |
|---|---|---|
| PHYS05 연구 | PR #34, head `4ea15a082f9358e28af35e30a392585f4e4383c9` | source/report/review와 checker snapshot을 읽고 결과를 계승 |
| PHYS05 대수 검산 | 보관 기록상 18,817 exact equalities, scoped review | 실행을 반복하지 않음; 5.5 MB full result를 새로 검산한 것으로 표시하지 않음 |
| 최신 NCP PHYS04 v2 | head `4b9231a0eff113701e7178ad98624233f387dd15`, core `892eca446ce23815d103f162dbd71c198a1e6198` | actual source와 반환 계약을 읽음 |
| 이미 구현된 NCP 항목 | FT03/LCS Jet 조합, N/D mixed quotient, U/V/W 선형 포함, λ/b receipt, 공통 seed/history | 재구현/재실행 작업으로 되돌리지 않음 |
| 아직 열린 NCP 항목 | 실제 family/tube root issuer, trusted producer 연결, finite observable와 continuous error | OPEN 유지; 이번 정리의 적용 전제로 명시 |

출처: [PHYS05 PR #34](https://github.com/cosmosapjw-quantum/WU088_HH/pull/34),
[PHYS05 고정 commit](https://github.com/cosmosapjw-quantum/WU088_HH/commit/4ea15a082f9358e28af35e30a392585f4e4383c9),
[NCP v2 고정 commit](https://github.com/cosmosapjw-quantum/WU088_HH/commit/4b9231a0eff113701e7178ad98624233f387dd15).
상세 원문과 blob/SHA256 bindings는 `inputs/phys05/`, `inputs/ncp_v2/`에 있다.

## 3. 이온화 에너지까지 합치면 드러나는 구조

기체 좌표를 g=(x,y1,y2,w)로 둔다. x는 HII 분율, y1/y2는 각각 HeII/HeIII
분율, w는 eV/H 단위 열에너지다. 다음의 **명시적으로 정의한 exact-real 좌표**를 쓴다.

\[
e=w+\chi_H x+f_{\rm He}\chi_{\rm HeI}y_1
       +f_{\rm He}(\chi_{\rm HeI}+\chi_{\rm HeII})y_2.
\]

이는 기존 물리 ledger가 계산하려는 열에너지+이온화 에너지 조합이다.
Native `energy()`의 binary64 합·곱과 bitwise 동일한 값이라는 주장은 아니다.
Interval 구현은 S의 계수와 그 구성 연산까지 outward하게 포함해야 한다.

### HH direct energy row

HH source가 H_HH=(q,0,0,−χ_H q)이므로 이 좌표에서

\[
\ell H_{\rm HH}=0,\qquad
\ell H_{{\rm HH},g}=0,\qquad
\ell H_{{\rm HH},gg}=0.
\]

HH 이온화가 열에너지에서 빼는 양을 이온화 에너지로 옮긴다는 뜻이다.
전체 implicit mixed response W_e는 여전히 escape, expansion, 다른 반응,
광자 교환, incoming derivatives와 inverse Jacobian을 통해 달라질 수 있다.

### Photo energy와 음의 준정부호 Hessian

그룹 j의 total opacity를 κ_j=Σ_a r_aj, reduced photon을
P_j=N_j/(1+dκ_j)로 둔다. 고정 grid/밀도에서 κ_j는 gas에 affine이다.
Excess energy가 정확한 E_j−χ_a일 때 모든 H/He photo column의 energy row는
E_jκ_j가 되고,

\[
\Phi(g,N)=\sum_j\frac{E_jN_j\kappa_j(g)}{1+d\kappa_j(g)}.
\]

α_j=∇κ_j라 두면 고정 d,E,N에서

\[
\nabla_g\Phi=\sum_j\frac{E_jN_j\alpha_j}{(1+d\kappa_j)^2},
\qquad
\nabla_g^2\Phi
=-2d\sum_j\frac{E_jN_j\alpha_j\alpha_j^{\mathsf T}}
                    {(1+d\kappa_j)^3}.
\]

d>0, E_j>0, N_j≥0, 분모>0이면 각 항은 rank가 최대 1인 음의 준정부호 행렬이다. 따라서
uᵀΦ_gg u≤0이다. 서로 다른 signed U,V에 대한 UᵀΦ_gg V의 부호와
전체 W의 부호는 이 결과로 고정되지 않는다. N의 λ/b derivatives도 별도로 남는다.
자세한 유도와 모든 incoming 항은 `theory/ENERGY_COORDINATE_KO.md`를 따른다.

## 4. 실제 저장 상태에서 얻은 새 수치

NCP v2의 원본 `COMMON_SEED_MEMBER1.bin`을 read-only로 해석했다.
SHA256은 `678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b`이다.
복원한 archived gas는

\[
g=(0.9131385026926517,\ 0.300035085528747,
0.5999927594007611,\ 13.565646600651332).
\]

물리 시간은 t0=1.6×10^11 s, frozen nH≈9.952115015900972×10^-5 cm^-3,
fHe=0.083이다. 정의한 exact-real matter energy는
e≈30.5296073383134 eV/H다. 이 숫자의 많은 표시 자릿수는 저장된 입력 leaf를
정확한 유리수로 옮긴 계산 정밀도이며 원래 물리 입력의 정확도를 높이지 않는다.

**아래 N은 저장된 old primary packet stock을 그대로 고정한 것이다.** 다음
step의 remap/birth를 적용한 pre-BE incoming이 아니다. d 두 값도 비교를 위한
산술 매개변수이며 실제 해당 시간만큼 진화시키거나 실행 승인을 받은 값이 아니다.
단면적은 실제 provider 식의 Python binary64 전사본으로 만들었고, NCP Rust
libm 출력과 bitwise 같다는 attestation은 하지 않았다.

| Frozen-stock 광흡수 성분 | d=6.25×10^8 s | d=1.25×10^9 s |
|---|---:|---:|
| Φ [eV/(H·s)] | 8.53668034384×10^-13 | 8.52805700127×10^-13 |
| ∂Φ/∂x [eV/(H·s)] | −9.81798443022×10^-12 | −9.79815914060×10^-12 |
| ∂²Φ/∂x² [eV/(H·s)] | −2.28586494785×10^-13 | −4.55788931946×10^-13 |
| dΦ [eV/H] | 5.33542521490×10^-4 | 1.06600712516×10^-3 |
| Hessian rank | 1 | 1 |

33개 에너지 node는 10–20 eV에 있다. Provider의 HI 단면적이 양수인 것은
17개(index 16–32), 그중 archived N도 양수여서 이번 Φ에 기여하는 것은
**9개(index 16–24)**다. HeI/HeII 단면적은 모두 0이다. 따라서 나머지 Hessian
성분은 이 고정 입력에서 정확히 0이고, x 방향의 음수 성분 하나만 남는다.

수소가 더 이온화되어 중성 수소가 줄면 이 고정 stock에서 흡수되는 에너지
율이 감소한다는 해석이 ∂Φ/∂x<0와 일치한다. 이 정량 결과를 full/twohalf
endpoint 차이나 HH×birth interaction으로 해석하지 않는다.

근거: `diagnostics/archived_energy_point.py`,
`evidence/archived_energy_point_results.json`, `evidence/archived_energy_run01.*`.
Closed-form derivative와 독립 formal quotient coefficient division을 비교했다.
198개 group equality, 6개 aggregate equality, 2개 energy balance 및 2개
rank factorization case가 기록되어 있다. 최초 실행 exit 0, 약 0.115 s다.

## 5. Source의 반올림 차이를 보존한 에너지식

### 밀도 leaf의 정규화 차이

실제 source는 nHe=fl(nH·fHe)를 저장한다. Nonphoto FT03 interval source의
헬륨 정규화는 fhat=nHe/nH인 반면, photo 및 정의한 energy coordinate에는
stage fHe가 들어간다. 따라서 exact-real stored-leaf graph에서도

\[
\delta f=f_{\rm He}-\widehat f
\]

가 일반적으로 0이 아니다. 원래 t0에서
δf≈3.92133772619×10^-18>0임을 확인했다. 비광자 energy row는 단순한
−L_escape−2Hw로 줄이지 않고

\[
\ell F_{\rm np}=-L_{\rm escape}-2Hw+J_{\rm norm},
\qquad
J_{\rm norm}=\delta f\,[\chi_{\rm HeI}F^0_{y_1}
 +(\chi_{\rm HeI}+\chi_{\rm HeII})F^0_{y_2}]
\]

로 보존한다. 여기서 F^0는 해당 nonphoto normalization의 성분이다.
Jnorm의 실제 whole-family 수치/미분 bound까지 계산한 것은 아니다.
온도 계산에서도 source의 fhat와 stage fHe를 혼동하지 않는다.

### `E−χ` excess-energy leaf

NCP mixed source에는 `ic(E-CHI[a])`가 있어 뺄셈을 먼저 binary64로 수행한다.
ε_aj=fl(E_j−χ_a)−(E_j−χ_a)라 두면 일반 source energy column은

\[
\ell K_j^{\rm source}=E_j\kappa_j+\delta_j(g),\qquad
\delta_j=\sum_a r_{aj}\varepsilon_{aj}.
\]

따라서 필요하면 Ψ=Σ_j N_jδ_j/(1+dκ_j)와 그 미분을 추가한다. 이를 생략한
Gram/concavity 정리는 arbitrary high-energy H/He native coefficient graph에
자동 적용되지 않는다. 예를 들어 100 eV의 HI excess leaf에서는
ε=−1/281474976710656 eV라는 작은 비영 값이 있다.

이번 archived 33-node에서는 99개 channel을 확인했고, 모든 σ가 양수인
channel의 ε는 정확히 0이었다. σ=0인 channel의 차이는 광흡수에 기여하지
않는다. 따라서 이번 고정 격자의 활성 photo 부분에는 이 보정이 남지 않는다.
근거는 `evidence/archived_energy_photo_leaf_check.json`과
`evidence/archived_energy_photo_leaf_addendum.json`에 있다.

이 둘을 원래 코드에서 조용히 바꾸지 않았다. NCP에서 G_E=ℓG를 직접
구성하는 경로와 compact energy ledger를 비교할 때 필요한 잔차로 전달한다.
초기 과도한 exact-source 문구와 정정 과정도 `FAILURE_LOG.md` 및
`theory/correction_history/`에 보존했다.

## 6. Uniform W에서 finite I_h로 가는 정리

G(y,λ,b)=0, Θ=[0,1]², X={|y−yc|≤r}를 둔다. G가 해당 영역을 포함하는
admissible C² domain에 있고, actual source를 포함하는 uniform bounds
gc=[G(yc,Θ)], [A]=[G_y(X,Θ)]가 있다고 가정한다. 고정 C에 대해

\[
B=\operatorname{mag}(I-C[A]),\quad
\beta=\operatorname{mag}(C g_c),\quad
\beta+Br<r
\]

이면 X 안에 각 θ의 유일한 root가 있으며 하나의 C² family로 이어진다.
증명은 Tθ(y)=y−CG(y,θ)의 strict invariance와 weighted-norm contraction이다.
이는 X 바깥까지 유일하다는 전역 정리가 아니다.

같은 source의 모든 parameter/old-state 항을 포함하면

\[
AU=-G_\lambda,\quad AV=-G_b,\quad
AW=-\left(G_{\lambda b}+G_{y\lambda}V+G_{yb}U+G_{yy}[U,V]\right).
\]

Θ 전체의 W bound가 있으면

\[
\boxed{I_h=y_h(1,1)-y_h(1,0)-y_h(0,1)+y_h(0,0)
       =\int_0^1\!\int_0^1 W_h(\lambda,b)\,db\,d\lambda.}
\]

이 때문에 **실제 discrete family 전체를 포함한 W**를 사용하면 별도의
parameter Taylor remainder가 필요 없다. 한 점의 W나 PHYS05의 formal
h-coefficient만으로는 이 결과를 적용할 수 없다. Continuous-time error와
h-expansion remainder는 여전히 별도다.

Full/twohalf의 차이에도 같은 식을 쓰되, 독립적인 넓은 두 W box를 빼는
대신 source-bound한 같은 θ의 차이를 보존할 수 있다.

\[
A_T\Delta W=\Delta f-\Delta A\,W_F,\qquad
\Delta I=\int_\Theta\Delta W.
\]

Actual ΔA/Δf bounds가 없이 작은 cancellation을 가정하는 방법은 아니다.
두 half-step의 old U,V,W carry도 함께 포함해야 한다.

근거와 전체 증명: `theory/UNIFORM_MIXED_RECTANGLE_KO.md`.
검증 수치계산의 일반 문헌 맥락은
[S. M. Rump, Acta Numerica 19 (2010), DOI 10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X)
의 publisher abstract/metadata를 확인했다. 접근하지 못한 full PDF의 특정
정리를 읽었다고 주장하지 않으며, 이번 specialized proof는 전달본 안에 있다.

## 7. 구현과 검산의 실제 범위

`src/uniform_mixed.py`는 Python 표준 라이브러리의 Fraction으로 interval
산술, uniform root 충분조건의 산술 부분, 선형 comparison enclosure, mixed
forcing, nonlinear observable chain, rectangle integral 및 paired difference를
구현한다. Domain과 source fields는 **전제의 선언**이며 native authority를
발급하는 기능이 아니다. 실제 physical RHS/BE solver는 포함하지 않는다.

최초 reference 실행에서 **275개 assertions와 17개 expected rejection**을
통과했다. 약 0.116 s, exit 0이었다. 독립 경로에는 radical로 표현한 nonlinear
implicit family, 별도 sparse polynomial derivative engine, formal quotient
division, non-diagonal interval matrix의 명시적 역행렬 비교가 포함된다.

점의 부호를 finite 부호로 바꾸지 못한다는 반례 y=λb−2λ²b도 포함했다.
여기서는 W(0,0)=1이지만 finite I=−1이다. Manufactured examples는 수학적
검증을 위한 것이며 HH physical surrogate로 사용하지 않았다.

과거 PHYS04/05 checker 및 NCP Decimal100 189-slot oracle를 다시 돌리지
않았다. 이 host에는 cargo/rustc가 없어 Rust build를 했다고 보고하지 않는다.
일시적인 실행 서버 연결 오류는 파일 읽기/문서 편집 중 발생했고, 접속 회복
후 실제 파일 상태를 확인해 이어갔다. 완료한 과학 검산을 재실행하지 않았다.

## 8. 다음 NCP 작업과 남는 조건

NCP handoff의 목표는 기존 actual source Jet에 energy-row export를 추가하고,
Jnorm/heat-leaf correction과 uniform parameter-domain contract를 명시하며,
source에 연결된 bounds를 받아 식의 충분조건을 평가할 수 있게 하는 것이다.
이미 완료된 receipt, seed/history, FT03/LCS composition을 다시 시작하지 않는다.

같은 parameter family의 half1→half2 jets, common initial state, endpoint time,
energy grid, source revision을 포함해 paired delta export를 준비한다. Actual
root/tube producer 또는 live native 실행이 여전히 필요한 부분은 정확한
입력·issuer gap·call graph·자원 계획으로 반환한다. 기존 미래 실행 제안의
12 endpoint/12+12 point/12 root 등의 숫자를 실행 승인으로 바꾸지 않는다.

| 결과 | 상태 |
|---|---|
| Energy/photo 대수 및 source 산술 보정 | 이번 유도·경량 검산 대상 |
| Uniform implicit-family → finite rectangle 정리 | 전제가 명시된 수학 결과 |
| Exact rational reference 구현 | 기록된 신규 검사 범위에서 검증 |
| Actual native W / I_h / mixed scheme defect | null / OPEN |
| Continuous source-law error / time remainder | null / OPEN |
| 물리 및 production 승격 | HOLD |

기존 24/289 admission, 265 unbounded cases, epsilon_C/R=null, B22 OPEN,
canonical S0 OFF, ON06G의 256-macro t=3.2e11 prefix도 그대로 유지한다.

전체 NCP prompt, task JSON, return template은 `handoff/`에 있다. ZIP 밖의
delivery receipt와 backup 시작 안내는 실제 publication commit/tree와
archive hash, Google Drive/Dropbox file identity를 제공한다. 사용자에게
새 전달 파일을 요청하지 않고 그 위치에서 회수해 시작하도록 구성한다.
