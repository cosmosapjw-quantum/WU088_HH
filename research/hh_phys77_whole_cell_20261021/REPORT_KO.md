# PHYS77 연구 결과: 실제 finite owner의 첫 whole-cell 포함 증명

## 1. 이번에 닫은 의무

PHYS76은 `S'=-A S+Pm+Pr`의 조건부 interval transport를 이미 갖고 있었다. 그러나 그 입력 `A,Pm,Pr`가 **실제 coupled solution의 cell 전체**를 포함한다는 producer는 DAG에서 미완료였다. PHYS77은 고정된 finite coefficient table을 읽는 outward RHS와 first-exit tube를 구현하고 실제 첫 cell 하나에 대해 이 입력 의무를 닫았다.

판정은 `SCOPED_FINITE_OWNER_FIRST_CELL_PASS`다. 완료한 대상은 finite-L8, massive 24×12 cells/Gauss3, 72×36=2592 packet, mass30 모델에서 저장된 정확한 초기 float vector로 정의한 실수 IVP다. 전체 1231개 history와 continuum의 완료 판정은 아니다. 실제 결과는 [LOCAL_CELL_SUMMARY.json](results/LOCAL_CELL_SUMMARY.json), 원래 receipt는 [FIRST_CELL_AFTER_RADIUS_FIX_RECEIPT.json](verification/FIRST_CELL_AFTER_RADIUS_FIX_RECEIPT.json)에 있다.

## 2. 연구 전 최신 결과 대조

접근 가능한 GitHub branch/PR, 다른 repo, provider backup, 대화 검색을 먼저 조사했다. 목록과 제한은 [INVENTORY_S0_KO.md](evidence/INVENTORY_S0_KO.md) 및 [INVENTORY_S0.json](evidence/INVENTORY_S0.json)에 있다. 특정 대화 검색에서 새 일치 항목이 없었다는 결과를 모든 비공개 대화에 새 결과가 없다는 주장으로 확대하지 않았다.

| 대상 | 실제 관측 HEAD | 채택 |
|---|---|---|
| HH PR128 | `92f5ab9dba531ebe05909dcb77d3740d2c68c580` | 과학적 기준 유지 |
| HH PR129 | `b76fd4b5d0dfe4850ebde66a8a10f78402d36c00` | standalone 보충 도구의 한계 유지 |
| HH PR130 | `535d24dbccf4fab40fd11f36330a63c4e288e24c` | 완료된 z20→2 자료·그림·조건부 transport 재사용 |
| HH PR131 | `ec28299fe7e81aab184b93aff787cb00a185dd2e` | 실제 remote 조상으로 선택 |
| REI PR199 | `eb8042b729051f4700bd5d88d6781c4620009bcb` | D8 완료 sidecar와 실제 result 채택 |
| REI PR215 | `d669298f05286728453840da46cae958a3709456` | ACCEL02 warm owner 범위로 분리 |
| REI PR216 | `1f32cc442ebde284bbb944455ba96066c9e0e055` | 같은 D8 case/raw/index/z/sign identity 대조 |
| BASS PR178 / BASS_HE PR83 | inventory에 전체 SHA 수록 | 관련 재사용 경로·backup 증거 대조 |

REI199의 오래된 main DAG에는 D8가 `ready_not_run`으로 남아 있지만, 최신 결과·검토·backup 및 완료 DAG sidecar가 존재했다. HH131·REI199·REI216의 4개 case에 대해 raw SHA, saved index, redshift, signed shear가 일치했다. 따라서 D8는 metadata reconcile 대상으로 채택했고 재실행하지 않았다. Saved adjacent sign bracket은 연속 root proof와 구분했다.

PHYS75 final delivery, handoff, DAG와 backup 기록도 읽었다. 당시 Dropbox supplement BLOCKED는 후속 PHYS76에서 복구돼 있었고 그 이력을 지우지 않았다. PR128 자체의 별도 FULL archive 보완 의무는 이 supplement 복구와 같은 것으로 취급하지 않는다.

## 3. 물리량과 정규화

공통 comoving normal orthonormal frame에서

\[
\sigma_{\hat a\hat b}=\operatorname{diag}(-s,-s,2s),\qquad
\pi^{(A)}_{\hat a\hat b}=\operatorname{diag}(-p_A,-p_A,2p_A),\quad A=m,r.
\]

원본의 질량밀도 convention에 맞춰 `kappa=8 pi G/c²`를 사용한다. Signed half-contraction 좌표는 `S=sqrt(3)s/H`, `P_A=sqrt(3) kappa p_A/H²`다. 크기는

\[
\Sigma_F=\sqrt2|S|,\quad \Pi_{A,F}=\sqrt2|P_A|,\quad
\Pi_{\mathrm{tot},F}=\sqrt2|P_m+P_r|.
\]

Half norm은 `sqrt(T_ab T^ab /2)`, Frobenius는 `sqrt(T_ab T^ab)`이므로 둘 사이가 sqrt2다. Matter와 radiation tensor를 부호를 유지해 합한 뒤 total norm을 취한다. `|Pm|+|Pr|`로 total을 만들지 않는다.

같은 coupled trajectory에서

\[
I(x)=\exp\!\int_{x_0}^x A(u)du,\qquad
S(x)=S_0/I(x)+J_m(x)+J_r(x)
\]

를 계산한다. 다른 species를 제거하면 H, state, source가 함께 변하므로 이 분해는 조건부 기여 분석이다. 이번 계산에 species-off causal 실험은 없다.

## 4. 구성적 유도와 코드 연결

전체 증명은 [THEOREM_KO.md](theory/THEOREM_KO.md)에 있다. 양의 packet moment를 미분해 `rho'=-3(rho+pbar)-6w*pi`를 얻었다. 실제 captured radiation matrix의 첫 행을 남기고 `delta0=(M E)0+2E2`를 정의하면

\[
A=\frac{h_0^2}{H^2}\left[\frac32d+\frac32\mu(\rho-\bar p)+rE_0+3\Omega_\Lambda+\frac12rw\delta_0\right].
\]

`rho-pbar`는 양의 packet 합으로 직접 계산한다. Captured monopole row의 작은 nonzero 원소는 그대로 남긴다. 이를 `(0,-2,0,0,0)`으로 바꾸면 다른 coefficient IVP가 된다. Wolfram algebra residual `{0,0}`와 독립 dimensional reference 검토를 따로 보존했다.

실제 상태를 `y=p+e`로 쓰고 affine predictor의 명시적 range `P(X)`와 후보 error box `R`에서

\[
D\supset F^\#(X,P(X)+R)-p',\qquad
E_{init}+[0,h]D\subset\operatorname{int}R
\]

를 확인했다. Smooth regular tube에서 first-exit contradiction으로 solution의 whole-cell 존재·유일성과 포함성을 얻는다. Endpoint는 `p(x1)+Einit+hD`다. Whole-time `[0,h]D`와 endpoint `hD`를 구분한다. 다음 cell은 이 endpoint box를 운반한다.

저장된 두 node는 predictor를 정하는 데만 쓴다. Nearest Decimal slope 자체를 정확한 affine coefficient로 정의하고 실제 `p0+h*slope`를 outward 평가한다. 저장 sample의 최소·최대나 quadrature residual을 whole-cell certificate로 사용하지 않았다.

## 5. 실제 첫 cell 결과

Case는 `mixed_s+0_m+1`, frozen table canonical SHA는 `c13b5305e83e9b3a249847e0461dfa271eb43138862a5762640f1c7a03ccef47`이다. Exact saved initial state에서 x=0→0.0224231957076456676902775910775744705460965633392333984375, z≈20→19.53435304695를 감쌌다. 원본 aref도 binary64 capture이므로 정확한 초기 redshift의 극소 차이는 summary에 기록한다.

아래 표는 원래 interval을 **바깥쪽으로 반올림해 표시한** 값이다. 전체 endpoint 문자열은 JSON에 있다.

| 양 | 포함 구간 | 범위 |
|---|---|---|
| A | [1.39910, 1.60104] | cell 전체 |
| signed Pm | [3.2980, 4.5998] ×10^-4 | cell 전체 |
| signed Pr | [−4.2790, −3.6568] ×10^-4 | cell 전체 |
| Jm | [7.2640, 10.1541] ×10^-6 | cell endpoint |
| Jr | [−9.4460, −8.0543] ×10^-6 | cell endpoint |
| total signed S | [−2.1819, 2.0997] ×10^-6 | cell endpoint |

8개 상태의 strict inclusion margin이 모두 양수였다. 성분별 단위·스케일이 다르므로 가장 작은 margin 하나를 universal error tolerance로 해석하지 않는다. Matter source는 양, radiation source는 음으로 cell 전체에서 확정되지만, total endpoint enclosure는 0을 포함한다. Total S의 부호 또는 부호 반전 시각은 이번 bound로 판정하지 않는다.

이 결과는 PHYS76 transport에 whole-cell producer를 붙인 첫 실제 finite-owner 사례다. Physical angular/momentum truncation error, 과거 machine integration 전체의 오차, nominal 초기 target의 exact 실현을 동시에 인증하지 않는다. 특히 원래 archive가 constructor table을 저장하지 않았으므로 현재 고정한 table과 과거 알 수 없는 library/runtime에서 만든 table의 bitwise 동일성은 열린 관계다.

## 6. 실패를 보존하고 변경된 의존성만 검토

첫 actual attempt는 `NOT_CERTIFIED_REQUESTED_PREFIX`였다. 모든 component radius를 매번 두 배로 키워 이미 통과한 q bound도 넓어지고, 그 coupling을 따라 다른 component가 계속 넓어지는 heuristic 문제였다. 이미 strict인 component의 radius를 유지하고 실패한 것만 키우도록 수정했다. 각 candidate에서 full coupled box는 다시 평가한다. Precision, 최대 inflation 수, strict criterion은 완화하지 않았다. 수정 후 4회 candidate 평가에서 첫 cell이 통과했다. 첫 failure와 첫 success는 서로 다른 result/receipt로 남아 있다.

독립 generic 검산에서는 reversed initial interval을 public `certify_cell`이 거부하지 않는 문제가 나왔다. 최초 15 PASS/1 FAIL을 보존하고 finite Decimal·ordering guard를 추가했다. 동일 16개 control이 통과했다. 정상 입력의 실제 성공 cell을 반복하지 않기 위해 변경 전후 AST의 계산 본문 동일성과 저장된 interval 134개의 guard 만족을 확인했다. 성공 source를 새 hash로 소급 표시하지 않았다. 저장되지 않은 중간 RHS는 재평가하지 않았으며 그 부분은 outward arithmetic의 finite/ordered invariant에 근거한다.

| 검증 | 결과 | 해석 |
|---|---|---|
| Export contract | 9 PASS | exact binary64 capture, hash/shape/domain 거부 |
| Independent arithmetic/cell | 16 PASS | 알려진 해, interior forcing, error carry, rounding 및 fail 조건 |
| Shared runner | 17 PASS | fake worker만 사용, 실제 engine 0 |
| Independent dimensional reference | 46 scalar comparisons PASS | 120-digit reference 대 50-digit interval, 2개 state |
| Original binary64 RHS 비교 | 2 point calls | 가장 큰 차이 약 2.19×10^-16; inclusion 판정 기준에 사용하지 않음 |
| Guard validation bridge | PASS | 실제 성공 cell 재실행 0 |
| Final staged preflight | PASS, eligible3 | source/input identity 확인, engine import 0 |

42개는 distinct control의 합이다. Guard retest와 portable retest를 새 독립 테스트 수로 중복 계산하지 않았다. Point 비교 46개도 unit-test 개수와 따로 기록한다.

## 7. NCP에 넘기는 실행 가능한 상태

3개 새 request는 다른 case의 첫 4개 cell만 요청한다. 모두 `READY_NOT_RUN`이다. 각각 frozen table, exact original initial state, saved predictor node 5개, source/raw identity를 포함한다. NCP에서 원본 constructor나 raw history를 다시 취득할 필요가 없다. Python/NumPy와 상위 repo의 고정 PHYS74/76 helper를 사용한다.

실행기는 request/source/runtime을 case identity로 묶고, 완료한 결과는 seal과 모든 artifact hash가 맞을 때 skip한다. 실패·비봉입은 별도 immutable attempt로 남으며 자동 재시도하지 않는다. Engine JSON은 post-call 검증 전에 `RESULT_UNVERIFIED.json`으로 보존한다. 입력 변경이 감지되면 최초 결과를 남긴 채 채택을 거부한다.

공유 lease, CPU affinity/quota, load/busy sample, RAM availability를 함께 읽고 최대64CPU/128GiB, 최소16GiB 여유를 적용한다. Worker당 nested thread는1이고 자리를 얻은 뒤에만 process를 만든다. Lease의 child PID/start tick이 연결된 뒤 engine gate를 연다. 같은 host/PID namespace의 advisory protocol이며 kernel resource reservation은 아니다.

최종 local preflight는 quota8CPU/RAM8GiB를 관측했다. source lock과 3개 입력은 통과했고 16GiB reserve 때문에 admissible slot은0이었다. 이 시점 own PID liveness는 관측됐다. 별도 agent의 이전 sandbox 관측에서 liveness가 없었던 이력도 보존한다. 둘 다 NCP 관측으로 표시하지 않는다. 이번 PHYS77에서 NCP 접속·실행은 없으며 NCP의 실제 preflight가 다음 환경 의무다.

## 8. 연구 DAG와 후속 판단

현재 child node `LOCAL_CELL_WITNESS`와 producer implementation은 scoped complete다. Parent whole-cell 의무는 `PARTIAL_SCOPED`이며 `FULL_HISTORY_ENCLOSURE`와 physical continuum 노드는 OPEN이다. 다음 실행은 준비된 세 prefix의 포함 증명 시도다. 실패하면 해당 cell·radius·defect를 보존하고 subdivision 또는 더 정밀한 predictor의 필요를 판단한다. 성공한 cell이나 기존 ODE는 다시 실행하지 않는다.

이 단위는 새 preliminary ODE campaign을 만들지 않았다. 기존 PHYS76의 z20→2 time evolution 및 sweep plot을 그대로 재사용한다. PR213 warm/HH74 control과 비교할 때 owner·closure·범위를 분리한다. Standalone `shear_attribution.py`는 명시적 source mapping을 요구하는 보충 도구로 남고 PR128의 기준 구현을 대체하지 않는다.

유도·코드·검증·과학 계산·게시·백업·DAG는 별도 파일과 단계 receipt로 관리한다. `HH_R10=OFF`, production admission `NOT_ISSUED`를 유지하며 draft PR을 merge하지 않는다.
