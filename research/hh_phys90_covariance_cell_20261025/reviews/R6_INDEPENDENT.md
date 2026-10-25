# PHYS90 독립 이론 검토 — 대칭 formatting cell과 공통 소비자 경계

## 판정과 검토 범위

검토자 `/root/independent90`는 root의 제안식에서 독립적으로 아래 유도를 수행했다. 이 기록은 **제안된 유한 정리의 검토**이며, 아직 받지 않은 최종 계약·구현·실행 결과를 승인하지 않는다. 실제 실행, source decode, eigensolve, 원 PHYS89 반례의 재계산은 모두 0이다.

PHYS89의 정확한 표시 행렬 반례, source decoding 결과, 소비자 정규화·공통 사건 보존식은 완료 근거로 재사용했다. 원 자료를 수정하거나 물리적 공분산을 새로 발행하지 않는다. 선택 부모 `NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT`의 실제 mass/state/kernel/tail/owner-ACK 의무는 유지된다.

검토한 문서:

- `/tmp/hh89_recovery/WU088_HH/AGENTS.md`
- `research/hh_phys89_bare_kernel_contract_20261025/FINAL_REPORT_KO.md`
- `theory/DISPLAYED_COVARIANCE_WITNESS_KO.md`
- `theory/BARE_KERNEL_CONSUMER_KO.md`
- root가 전달한 PHYS90 제안식과 유한 실행 범위

## 1. 정의역과 정확한 sharp support

실수 대칭행렬 F, 실수 대칭 성분별 비음수 H, t≥0에 대해 닫힌 집합

\[
\mathcal B_t=\{F+\Delta:\Delta=\Delta^T,\ |\Delta_{ij}|\le tH_{ij}\}
\]

를 사용한다. 원 ENDF의 half-ULP에서 H를 얻는 것은 명시적인 조건부 formatting 모형이다. 실제 formatter가 nearest rounding이라는 source 보증이나 통계적 신뢰수준은 이 정의에 포함되지 않는다. Half-ULP 양끝을 모두 포함하는 닫힌 cell은 실제 tie-to-even 등의 반열린 cell을 포함하는 보수적 집합이다. 닫힌 cell의 경계에만 있는 구성으로 실제 formatter의 정확한 역상을 인증하면 안 된다.

고정 실수 벡터 u,v에 대해 독립 좌표는 i≤j인 Δij이며

\[
u^T\Delta v=\sum_i u_i v_i\Delta_{ii}
+\sum_{i<j}(u_i v_j+u_j v_i)\Delta_{ij}.
\]

따라서

\[
\sup_{\Delta\in\mathcal B_t-F}|u^T\Delta v|
=t\left[\sum_iH_{ii}|u_i v_i|
+\sum_{i<j}H_{ij}|u_i v_j+u_j v_i|\right].
\]

각 독립 좌표를 해당 계수의 부호에 맞춘 ±tHij로 놓으면 양의 상한을 달성하며, 반대 부호로 음의 하한을 달성한다. 계수 0인 좌표는 자유롭게 0으로 둔다. H 또는 t가 0인 경계도 같은 식에 포함된다. 대칭 off-diagonal을 두 독립 오차로 취급한 |u|ᵀH|v|는 일반적으로 더 큰 경계다.

실수 대칭 Y에 대해서는

\[
h_H(Y)=\sum_iH_{ii}|Y_{ii}|+2\sum_{i<j}H_{ij}|Y_{ij}|,
\qquad\sup_\Delta\operatorname{tr}(Y\Delta)=t h_H(Y).
\]

위 sharpness는 **대칭 성분 box 전체**에 대한 결과다. 추가 제약 C≽0 또는 실제 evaluator의 구조·정규화가 들어간 부분집합에서도 유효한 상계지만, 그 부분집합에서 달성된다는 주장은 별도 구성 없이는 성립하지 않는다.

## 2. 2×2 PSD 가능성의 필요충분조건

쌍 (i,j)에 대해

\[
a=F_{ii}+tH_{ii},\quad b=F_{jj}+tH_{jj},\quad
d=\operatorname{dist}(0,[F_{ij}-tH_{ij},F_{ij}+tH_{ij}])
=\max(|F_{ij}|-tH_{ij},0).
\]

해당 2×2 principal block의 interval cell 안에 PSD 행렬이 존재할 필요충분조건은

\[
a\ge0,\quad b\ge0,\quad d^2\le ab.
\]

필요성: PSD block의 실제 대각 x,y는 0≤x≤a, 0≤y≤b이며 실제 off-diagonal z는 |z|≥d이다. 따라서 d²≤z²≤xy≤ab다. 충분성: 대각을 upper endpoint a,b로, off-diagonal을 해당 구간에서 0에 가장 가까운 값으로 선택하면 비음수 대각과 비음수 determinant를 갖는다. a=0 또는 b=0에서는 반드시 d=0이어야 한다. 실제 구간에 0이 들어가는 경우 이 선택은 정확히 0이다.

모든 쌍이 통과하면 같은 upper diagonal들과 각 off-diagonal의 nearest-zero 값을 한 행렬에 동시에 배치할 수 있다. 그러므로 모든 1×1·2×2 principal minor가 비음수인 **한 공통 행렬**이 존재한다. 이 사실은 n≥3에서 전체 PSD를 보장하지 않는다.

Standalone 1×1 검사를 포함하면 n=1 입력과 단일 대각 오류도 명료하다. n≥2와 모든 쌍의 완전 검사를 계약으로 고정하면 각 대각이 쌍 검사에 포함된다.

## 3. 정확한 이분법과 threshold 의미

\(\mathcal B_s\subseteq\mathcal B_t\) for 0≤s≤t이므로 pairwise feasibility는 t에 대해 단조다. 대각이 비음수인 영역에서는 a,b가 증가하고 d가 감소한다는 직접 증명도 가능하다.

실수 threshold τpair를 모든 1×1·2×2 검사의 최초 통과 반경으로 정의한다. 유한 bracket l,u를 사용하려면 최초에 `fail(l)`과 `pass(u)`를 실제 정확한 판정으로 확보해야 한다. 중점 m=(l+u)/2가 pass면 u=m, fail이면 l=m으로 갱신한다. 각 단계에서 l<τpair≤u가 보존된다. τpair=0인 경우에는 baseline pass를 별도 표시해 [0,0]으로 종료한다. Equality는 닫힌 cell의 pass다. 유리수 연산이면 sign 판정에 tolerance를 넣을 이유가 없다.

최대 doubling 횟수 또는 명시적 upper radius를 미리 정한다. 상단 pass를 얻지 못하면 `UNBRACKETED_WITHIN_FROZEN_RANGE`를 반환해야 하며 유한 threshold나 full-precision 배제를 추론하지 않는다. H의 대각이 0인 일반 입력에서는 임의의 유한 t에서도 불가능한 경우가 있다.

전체 PSD threshold τPSD에 대해 τPSD≥τpair다. 따라서 이분법의 l은 τPSD에 대한 하한이다. **u는 τpair의 상한이며 τPSD의 상한이 아니다.** 두 threshold를 서로 다른 필드에 기록해야 한다.

## 4. 공통 소비자와 보존식

고정 실수 L에 대해 K(C)=LCLᵀ다. 두 row ℓa,ℓb의 covariance 변화에는 1절의 sharp box 식을 적용한다. 여러 entry의 모든 marginal endpoint를 동시에 선택할 수 있다는 주장은 나오지 않는다. 행렬 출력은 `L \mathcal B_t Lᵀ`라는 한 공통 Δ의 image다.

어떤 q가 qᵀL=0을 만족하면 qᵀK=0, Kq=0 및 qᵀKq=0가 모든 C에서 정확히 성립한다. 이는 source uncertainty가 event-wise 보존식을 보존한다는 대수 결과이며 C의 PSD에도 의존하지 않는다. 서로 다른 소비자의 공분산을 독립 표본으로 바꾸면 이 식이 일반적으로 깨진다.

정규화된 모멘트의 sensitivity B=(a−Mr)/Z는 PHYS89 결과를 재사용한다. BCBᵀ는 같은 고정 finite coefficients에서의 일차 source covariance다. 새 식은 비선형 ratio의 정확한 분포나 coupled thermal history를 발행하지 않는다. 미지의 물리적 group weights를 옛 scalar total로 대체하지 않는다.

## 5. 실제로 구별되는 제조 fixture

아래 값은 유도된 유한 예이며 PHYS89 source 값이나 실제 nuclear rate가 아니다. 검토자는 실행하지 않았다.

### 5.1 공유 off-diagonal과 동시 endpoint

F=4I₂, H의 모든 성분=1, t=1, u=(1,1), v=(1,−1)로 둔다. 모든 C∈B₁은 대각≥3, |off|≤1이므로 positive definite다.

- uᵀΔv=Δ11−Δ22이므로 정확한 반경은 2다. off-diagonal을 독립으로 계산한 단순 absolute-product 식은 4를 준다.
- 각각 uᵀCu와 vᵀCv는 최대 12에 도달할 수 있다.
- 그러나 합은 16+2Δ11+2Δ22≤20이다. 따라서 두 marginal maximum (12,12)는 함께 달성되지 않는다.
- L의 세 번째 row를 −u−v=(−2,0)로 두면 q=(1,1,1)에 대해 qᵀL=0이다. 모든 공유 C에서 qᵀKq=0이다.

### 5.2 모든 pair 통과와 전체 PSD의 차이

n=3, Fii=1, Fij=−1(i≠j), Hij=1/10, t=1로 둔다. 모든 pair는 a=b=11/10,d=9/10이므로 통과한다. 그러나 w=(1,1,1)에 대해 wᵀFw=−3이고 hH(wwᵀ)=9/10이므로

\[
\sup_{C\in\mathcal B_1}w^TCw=-21/10<0.
\]

따라서 이 cell에는 전체 PSD 행렬이 없다. 이는 pairwise 통과를 전체 PSD 수용으로 잘못 표시하는 mutation을 잡는 exact fixture다.

## 6. 전체 compatibility를 닫을 수 있는 다음 의무

Y≽0인 정확한 행렬이

\[
\operatorname{tr}(YF)+t h_H(Y)<0
\]

를 만족하면 모든 C∈Bₜ에 대해 tr(YC)<0이므로 Bₜ∩S₊=∅다. Y=wwᵀ는 root가 제안한 quadratic-form certificate다.

이 separator 조건은 전체 closed box의 비양립성과 동치다. 증명은 유한차원에서 box의 compactness를 쓴다. Disjoint인 box와 PSD cone 사이의 최소 거리 pair C₀,P₀를 잡는다. Z=C₀−P₀라 두면 projection 최적성으로 ⟨Z,P−P₀⟩≤0 for all P≽0이다. P=0 및 P=2P₀를 대입하면 ⟨Z,P₀⟩=0이고 Z≼0이다. Box 쪽 최적성은 ⟨Z,C−C₀⟩≥0이다. 따라서 Y=−Z≽0에 대해 모든 C∈Bₜ에서

\[
\langle Y,C\rangle\le\langle Y,C_0\rangle=-\|Z\|_F^2<0.
\]

역방향은 PSD 행렬들의 trace product가 비음수라는 사실로 즉시 따른다. 이 존재 증명은 실제 153군 데이터의 Y를 공급하지 않는다. 차후 정확한 PSD dual separator 또는 interval cell 내부의 정확한 Gram/LDLᵀ primal 구성을 받으면 전체 compatibility를 닫을 수 있다. 그것도 실제 evaluator 승인·nominal binding과는 별도의 유한 수학 결과다.

## 7. 최소 반영 사항과 상태

1. Sharpness의 정의역을 full symmetric box로 명시하고 PSD intersection에서의 attainment를 미발행한다.
2. Consumer marginal bounds와 공통 matrix image를 구분하고 동시 endpoint 검사를 넣는다.
3. τpair와 τPSD의 필드를 분리하며 pairwise upper bracket을 global upper bound로 표시하지 않는다.
4. t≥0, H≥0, real symmetric input, closed endpoints, exact rational sign, baseline/bracket/zero-diagonal 처리 규칙을 계약에 고정한다.
5. Actual153 결과가 오기 전 `all_pairs_pass`, `global_PSD_compatible`, threshold 숫자를 예상값으로 기록하지 않는다.

이 사항을 반영한 최종 root 이론·계약의 actual bytes를 받은 뒤 R6 최종 판정을 덧붙인다. 현 시점 범위는 `PASS_SCOPED_PROPOSED_LEMMAS_PENDING_FINAL_DRAFT_READBACK`이다. 새로운 source claim, strong no-go의 보편적 신규성, 물리 covariance 수용, nuclear 활성화, fast stopping, HH_R10 또는 production admission은 없다.

## 8. 최종 이론·계약 actual readback과 R6 판정

앞 절의 pending 상태는 최초 제안식 검토 시점의 기록이다. 이후 다음 두 실제 파일을 읽고 SHA-256을 확인했다.

| 대상 | SHA-256 |
|---|---|
| `theory/COVARIANCE_CELL_AND_CONSUMER_KO.md` | `979b8f12a69cefd332a225ccce322802d2c94550cda77db4428fd96a0e65492e` |
| `CONTRACT.json`, revision 1 | `45d7b94544cf801619aa723c79be35c05e3ca2b023e2e94e8985f4c20758a20c` |

두 파일은 `/tmp/hh89_recovery/WU088_HH/research/hh_phys90_covariance_cell_20261025/` 아래에 있다. 최종 이론은 §1에 box-only sharpness와 nonjoint endpoints, §2에 exact 2×2 판정·대각/zero-H·최대4096 bracket·40회 이분법과 pair/global threshold 구분, §3에 all-pairs/global 구분, §4에 공통 source 보존과 normalized first-order 범위를 명시한다. 계약은 153 singletons/11628 pairs/11781 upper entries, 두 제조 fixture, source SHA, scientific/remote 실행 한계 및 불변 조건을 고정한다. 최초 검토의 네 정밀화 요청은 모두 이 문서들에서 닫혔다.

추가된 옛 0,10 block의 새 radius 식도 기호 유도로 검토했다. a>d>0, h=d/2에서

\[
(a+th)(a-d+th)-(a-th)^2=-ad+t(d/2)(4a-d).
\]

영점 t*=2a/(4a-d)는 0<t*<2a/d를 만족하므로 사용한 positive-off branch 안에 있다. 이 branch에서 두 upper diagonal은 양수이고 determinant는 t에 대해 엄격히 증가한다. 따라서 해당 block의 최초 compatible radius라는 해석이 맞다. 이 검토는 이전 t=0 source 반례를 재실행한 것이 아니라 새 radius 식의 독립 대수 검토다.

**최종 R6 판정: `PASS_SCOPED_COVARIANCE_CELL_THEORY_AND_FROZEN_CONTRACT`.** 이론의 유한 조건부 결론과 구현 계약에 남은 blocking finding은 없다. Actual153의 새 pair 결과·threshold·원자료 source claim 및 C5–C9 구현/실행 결과는 이 판정에 포함되지 않는다. 독립 reference가 Decimal을 선택하면 실제 고정 입력·40-step dyadic arithmetic에서 exact sign을 보장하는 precision 근거를 구현 검토에서 확인해야 한다. 별도 exact integer/Fraction 경로는 이 위험을 직접 제거한다. 이는 수용 오차를 새로 바꾸는 요구가 아니라 계약의 exact scientific comparison을 구현하는 확인 사항이다.

이 readback에서도 scientific child/source decode/eigensolve/적분/ODE/benchmark/원격 변경은0이다. 원 PHYS89 scientific identity와 소진 허용량을 재사용하며 budget reset=false다.
