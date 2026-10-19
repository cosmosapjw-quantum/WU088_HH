# PHYS68 — 검증된 Born 반경 profile과 finite-L28 2차 성분

## 1. 이번에 완료한 과학 결과

원래 screened Hamiltonian의 outgoing DtN Born 전개에서, **m=0, L=28,
외부 채널 (21,20)**의 2차 계수를 인증했다. 중간 채널은 j=0,...,28 모두다.
필요한 두 외부 행의 57개 서로 다른 D1 profile을 [27,65]의 76개 구간에
구성하여 적분했다. 별도로 수행한 전체 D1 행렬 계산이라고 부르지 않는다.

정확한 중심은 `profiles/run_l28_t65_completed/CERTIFICATE.json`의 dyadic
midpoint이며, 아래 십진수는 읽기용 표시다.

\[
D_{2,21\,20}(27)\simeq
(7.017743632815532786+3.200163222305211742i)10^{-48}\ a_0^{-1}.
\]

| 오차 성분 | 정확한 유리수 상한의 십진 표시 |
|---|---:|
| Coulomb·angular 평가·profile·반경 적분·roundoff를 합친 수치 오차 | 8.2281004544907943e-67 a0^-1 |
| 기존 PR115 정리에 따른 T=65 바깥 beta2 | 4.6211093402500825e-68 a0^-1 |
| 저장한 정확한 중심에 대한 full-radial 복소 절대오차 | **8.6902113885158026e-67 a0^-1 미만의 외향 유리수 상한** |

안전하게 반올림한 보고 상한은 **8.691e-67 a0^-1**이다. 표시용 중심을
추가로 반올림한 뒤 같은 상한을 무조건 붙이지 말고, 정확한 midpoint를
사용하거나 그 반올림 오차를 별도로 더해야 한다.

사전에 고정한 목표는 필요한 D1 57쌍의 B=27 경계 오차 1e-45와 D2 목표
성분의 수치+반경 tail 오차 1e-62였다. 둘 다 통과했다. D1 경계의 최대
수치+beta1 오차는 **8.764e-53 a0^-1 미만**이다. profile은 각 구간의
임의 exact 실수점에서 포함 구간을 반환하지만, 모든 r에 동일한 1e-45
accuracy를 검증한 별도 uniform gate는 이 결과에 포함하지 않는다.

## 2. 먼저 확인한 백업과 GitHub

실제 최신 관련 GitHub는 draft PR117, HEAD
`1a149efeba61a9ffd7ea882bdd86f7ea36c0b78c`, tree
`43885b4b718ee35bcc96ee842645c6e5ac4a0bd6`였다. 최근 PR 20개와 branch
126개를 확인했으며, 그 HEAD의 마지막 변경은 publication JSON 4개인
metadata commit이었다. 새 과학 실행이나 이전 C5–C8의 재게시로 세지 않았다.

Dropbox WU088_HH 직계 23개/재귀 33개와 Drive 직계 24개 및 PHYS66 R5
하위 항목을 확인했다. 조사한 범위에서 새 longtail 결과를 찾지 못했다.
이를 NCP host 전체에 실행이 없었다는 주장으로 확대하지 않는다. 기존
PHYS67 Dropbox ZIP은 같은 ID·revision·4,684,159 bytes를 유지했다.
Drive의 이전 업로드 2건은 성공 ACK를 회수하지 못한 상태를 그대로 보존했다.

PHYS67 source/evidence ZIP을 실제 bytes로 복구하여 SHA256
`f1bec132b7efb5a8f3f938a5848d505c84216f1087be8e39e484ae3ef121234d`를
확인했다. DELIVERY와 기존 PHYS66 longtail runner도 이전 영수증과 일치했다.
이미 검증된 PHYS67 archive payload 전체의 과학 실행을 반복하지 않았다.

사용자가 지정했던 PHYS66 최종 ZIP `993317b1...`와 snapshot `2d08f8da...`의
정확한 버전은 여전히 `BLOCKED_ARTIFACT_ACCESS_EXACT_FINAL_VERSION`이다.
PR117에 통합된 것은 별도로 검증한 이전 `84c29de7...` archive의 84-path
추가분이다. 그 구분과 실제 ancestry를 유지하며, 45-path 최종본을
회수했다고 주장하지 않는다. 최신 PR114/115 proof와 frozen NPZ를 이전
archive로 덮어쓴 경로는 없다.

## 3. 원래 물리와 계수 정의

atomic coordinates에서 B=27, k=7/10, E=49/200 Hartree, R0=7/10을 유지한다.

\[
h=-\Delta/2-1/r-(1+1/d)e^{-2d},\qquad
d=|\mathbf x-R_0\hat z|.
\]

radial equation의 V는 **2(1+1/d)e^{-2d}**다. outgoing convention은
H+=G+iF, Z=+u'u^-1, d_r=k d_rho이며 eta_C=-10/7이다. 원래 eta=Fy,
xi=Fy-phi와 Coulomb eta_C를 구별한다.

원본 frozen1386 complex128 NPZ의 SHA256
`f1bd3074950163960cc2011682d013af60f9b17c471bea72ecbc2ffb19e6855d`를
실행 입구에서 검사했다. 이번 계산은 DtN 계수의 행렬 원소다. NPZ의 byte
guard를 원래 source vector에 연산자를 적용한 실제 xi 계산으로 세지 않는다.

screening 강도 lambda의 전개 Z=Z_C+lambda D1+lambda^2 D2+...를 쓴다.
D2는 이 전개의 계수이며 lambda의 두 번째 ordinary derivative와는 2!
차이가 있다. PHYS66 기존 Born convention을 그대로 사용한다.

## 4. 실제 유도: point certificate에서 검증 profile로

\[
F_l(r)=H_l^+(r)/H_l^+(27),\qquad
q_{lj}(r)=F_l(r)F_j(r)D^T_{1,lj}(r).
\]

Riccati 식 D'+Z_C D+D Z_C=-V-D^2와 terminal D(T)=0으로부터

\[
q_{lj}(r)=\int_r^T F_l(s)F_j(s)V_{lj}(s)\,ds,
\qquad q'_{lj}=-K_{lj},\quad K_{lj}=F_lF_jV_{lj}
\]

를 얻는다. 따라서

\[
D^T_{2,lp}(27)=\sum_{j=0}^{28}\int_{27}^{T}
\frac{q_{lj}(r)q_{pj}(r)}{F_j(r)^2}\,dr.
\]

켤레는 들어가지 않고 D2 convolution에 추가 factor 2가 없다. 정규화
F_l(27)=1을 사용했다. 전체 j 합에 필요한 57개의 symmetric pair를 먼저
만들며, 큰 항 몇 개만 골라 합한 결과는 이 인증으로 통과하지 못한다.

Coulomb Taylor 계수는 원래 ODE

\[
H_l''+Q_l(r)H_l=0,\qquad Q_l=k^2+2/r-l(l+1)/r^2
\]

에서 구한다. 중심 c에서 정확한 Q_n과 계수 h_n은

\[
Q_n=(49/100)\delta_{n0}+2(-1)^n/c^{n+1}
-l(l+1)(n+1)(-1)^n/c^{n+2},
\]
\[
h_{n+2}=-\frac{\sum_{s=0}^nQ_s h_{n-s}}{(n+1)(n+2)}.
\]

초기 h0,h1는 기존 PHYS67 Arb Coulomb 함수와 radial derivative로 감싼다.
radius R의 복소 원판에서는 dimensionless atomic coordinate의 두 성분
(H/H(B),d_(r/a0)H/H(B))에 Gronwall을 적용하여

\[
M_H=\max(|h_0|,|h_1|)
\exp\{R\max(1,k^2+2/(c-R)+l(l+1)/(c-R)^2)\}
\]

를 얻는다. Taylor 나머지는 M_H(h/R)^(N+1)/(1-h/R)로 제어한다.

작은 원판 rho에서

\[
m_j=|h_{j,0}|_{\rm lower}
-\sum_{n=1}^N|h_{j,n}|_{\rm upper}\rho^n-R_{H_j}(\rho)>0
\]

인 것을 실제로 검사한다. 실수축 비영점만으로 복소 원판의 비영점을
가정하지 않았다. 76x29=2,204개 하한이 모두 양수이며 최소값은
0.004395346773909886보다 크다.

각 구간의 q center와 left boundary는 K의 다항식 적분에 각각 h R_K,
2h R_K를 더하여 감싼다. 상수 계수에는 이전 구간에서 온 전체 ball 오차가
남고, q의 나머지 계수는 -K_n/(n+1)이다. K degree80, q degree81을 쓴다.
I_j=q_lj q_pj/F_j^2의 degree80 계수를 구하고, 작은 원판의

\[
M_q\le |q_{\rm right}|+(\rho+h)M_K(\rho),\qquad
M_{I_j}\le M_{q_{lj}}M_{q_{pj}}/m_j^2
\]

로 각 적분 tail 2h M_I (h/rho)^81/(1-h/rho)를 붙인다. 모든 coefficient
ball과 operation roundoff를 유지한다. 구간폭1/2, h1/4, 큰 R2, rho1/2,
working384bits, angular coefficient1024bits가 실제 고정 요청이다.

T를 넘는 복소 원판에서도 K는 원래 analytic kernel이다. q^T를 terminal
value 0인 analytic primitive로 연장하며, 복소 원판 중간에서 K를 0으로
잘라 Cauchy 정리의 가정을 깨뜨리지 않는다.

상세 증명은 `theory/PROOF.md`와 `taylor/PROOF.md`에 있다. DLMF 33.2,
1.9와 FLINT/Johansson의 arbitrary-precision ball integration 문헌을
실제로 조회했고, PHYS68에 필요한 majorant와 model 대응은 직접 유도했다.

## 5. 각도 계산과 최적화

m=0의 angular integral에는 PHYS67의 exact Laurent 식을 사용한다.
d=r+t 치환 뒤 mu=-t/R0+(R0^2-t^2)/(2R0 r)이고 P_l P_j는 유한
다항식이다. monomial별 endpoint pair를 정확한 Fraction으로 한 번
준비한 뒤 Legendre 곱에 선형 결합한다. V=2S와 정규화는 그대로다.

같은 57쌍의 exact preparation+동일 serialization/hash를 별도 cold
process에서 측정한 시간은 이전6.375268초, 새0.702180초였다. 단일 관측
비율은9.079이며 57쌍의 exact 결과 hash는 전부 같다. 전체 L28 symmetric
435쌍을 준비하는 API도 구현됐지만, 그것을 전체435개 radial profile의
완료 실행으로 표시하지 않는다.

새 복소 원판 majorant는 a=c-s-R0>0에 대해

\[
|V_{lj}(z)|\le 2(1+1/a)e^{-2a}
\]

다. w=x+iy,x>0,b^2>=0에서 principal sqrt가 cut을 피하고
|w^2+b^2|^2-(x^2+y^2-b^2)^2=4x^2b^2>=0임을 사용해
Re sqrt(w^2+b^2)>=x를 증명했다. 이어 정규화 angular basis의
Cauchy–Schwarz를 적용한다. 채널 수 배수를 넣을 필요가 없다.

이 정확한 m0 algebra 경로의 평가·roundoff는 이번 Arb 포함 구간에
들어간다. 이전 f64 Gauss nodes/weights/basis로 만든 전체 pipeline의
roundoff를 소급하여 인증한 결과는 아니다.

## 6. 실제 실행과 독립 검증

실제 Rust1.94.1 컴파일러가 작동하여 표준 라이브러리만으로 별도 복소
arithmetic·Gauss96 angular integral·backward RK4를 구현하고 실행했다.
따라서 Rust 접근 차단에 따른 Fortran 전환은 필요하지 않았다. Coulomb
terminal seed의 Arb initializer만 공유하며, angular·ODE·적분 구현은
별도다. f64 refinement 자체를 엄밀한 인증으로 부르지 않는다.

| 독립 Rust 실행 | D2 real | D2 imag | 적분 시간 |
|---|---:|---:|---:|
|2432 steps, h=-1/64|7.017743691499148e-48|3.2001632200665314e-48|0.058214621s|
|4864 steps, h=-1/128|7.017743636578995e-48|3.200163222139536e-48|0.096436988s|

새 Arb certificate와 비교한 fine Rust 결과의 실제 상대오차 상한은
4.885e-10 미만이다. 기존 PHYS66 pilot의 저장된 D2 성분도 다시 실행하지
않고 읽어, 실제 절대오차가 약1.7486685e-59 a0^-1인 것을 감쌌다.
이는 그 저장된 한 성분의 총오차이며 과거 solver의 모든 항에 대한
오차 분해나 전체 인증이 아니다.

새 D1(21,20)의 full-radial rectangle은 기존 PHYS67 rectangle에 포함된다.
기존 D1 integrator는 다시 호출하지 않았다. 저장 profile loader의
r=219/8 두 평가도 실제로 수행했으며, 이 경로는 계수만 재구성하고 기존
Volterra/D2 적분을 반복하지 않는다.

검증은 새 Taylor28, angular35, profile22, Rust driver14, 저장값 비교8,
NCP wrapper21, 총128개의 서로 다른 Python 테스트와 native Rust5개,
합계133개로 구성된다. 이전 PHYS67의 128개와는 별도 신규 집합이다. 상세 실제 실행은 각
단위의 TEST/EXECUTION 기록이 권위다. profile22개는 최초20개의 성공과
새2개 및 영향받은 재개검사5개의 성공을 합친 서로 다른 테스트 수다.
동일 테스트의 재검증을 새 테스트로 중복 세지 않는다. 첫 invalid-input
테스트 fixture의 잘못된 전제와 이후 수정도 보존했다.

독립 reviewer는 프로젝트 모듈이나 Arb를 import하지 않고 exact Fraction
및 저장 JSON만으로 76 payload hash/chain, 17,328개 경계 포함 부등식,
4,332개 pair 기록, 2,204개 비영점 하한과 D2 tail, 모든 j 합과 최종 합,
고정 목표의 실제 충족을 확인했다. 최종 판정은
`theory/FINAL_EXECUTION_REVIEW.json`의 PASS다.

## 7. 성공 구간을 보존한 재시작 수정

첫2패널은3.021초에 성공했다. 첫 재시작은 새 적분0회 상태에서 멈췄다.
Arb radius 복원 시 1 magnitude ulp의 외향 확대가 생길 수 있는데,
재직렬화한 ball과 원래 저장 bytes의 동일성을 요구한 검사 때문이었다.

수정 후 raw predecessor q_left의 저장 hash와 실제 q_right의 exact
포함 관계를 나누어 검사한다. 기존 수학 정의16개와 imports/constants는
그대로이며 run_profiles의 연결 검사와 raw-box helper3개만 바뀌었다.
원래 구현 SHA50878a...와 원래2payload를 모두 보존했고, 정의별 AST 및
다른 engine/runtime/source/request의 동일성을 검증하여 새 envelope에
같은 payload를 채택했다. 이 과정의 적분은0회다.

그 뒤 **2패널 재사용+74패널 신규**로78.469초에 완료했다. 원본 전체
78개 panel JSON bytes는 `profiles/PROFILE_PANEL_PAYLOADS_20261019.zip`에
보존되어 있다. source guard나 fingerprint를 무시하는 force-resume
선택지는 추가하지 않았다.

## 8. NCP에 전달한 완성된 범위와 남은 과학

L64의 모든 j를 포함한 같은 D2 성분을 선택적 다음 numerical extension으로
완성했다. 고정 요청은 T65,N96,768/2048bits,h1/8,rho1/4,R2이며,
runner는 기본 preflight-only다. 실제 critical Coulomb4개와 높은 angular
pair2개의 preflight는 통과했으며 radial panel 실행은0회다. wrapper는
기존 request/fingerprint를 먼저 확인하고 성공 checkpoint를 재사용한다.
정해진 timeout·memory 한도와 실행 로그 수집까지 구현돼 있다.

PHYS66 longtail6의 완성된 기존 runner는 SHA
`34a59dfe3158c454811ed6e6f47c82357e502ef8cdef9ee5f14640b37f73a835`로
별도 유지한다. NCP에서 이미 생긴 결과가 있으면 host와 backup의
영수증부터 검증해야 한다. 이 세션의 NCP 제출·radial 실행은0이다.
solver 설계는 NCP로 넘기지 않는다.

PHYS63의 실제 all-angular qualitative LAP/Poisson/DtN 존재는 확보 상태다.
남은 연구는 finite-L 바깥 higher-order angular response, 아직 다루지 않은
계수·m의 수치 인증, 원래 xi=Fy-phi, regular origin과 incoming adjoint,
sigma(E), Maxwellian k_HH(T)다. 이번 finite-L 한 성분의 성공으로 그
상태를 완료로 바꾸지 않는다. HH_R10은 OFF다.

## 9. 게시·백업·DAG의 권위

과학 완료와 Git 게시·백업은 별도 상태다. `NEXT_DAG.json`은 과학 결과와
NCP 요청을 구분하며 `publication/`의 실제 remote/readback/backup
영수증이 외부 쓰기 성공의 권위다. science commit 이후 metadata commit을
추가하더라도 새 계산으로 세지 않는다. Archive에 포함된 science commit과
나중에 생성한 게시·백업 영수증의 범위를 구별한다.

완료된 PHYS64 20건, PHYS66 pilot/smoke, PHYS67 certificate는 재사용했고
실제 재실행은0회다. Git의 기존 최신 proof와 원래 NPZ는 byte-identical로
유지한다. 이번 branch는 실제 PR117을 부모로 하는 additive stacked draft다.

### 주요 근거

- `theory/PROOF.md`, `theory/FINAL_EXECUTION_REVIEW.json`
- `profiles/run_l28_t65_completed/CERTIFICATE.json`
- `profiles/PANEL_ARCHIVE_RECEIPT.json`
- `validation/SAVED_RESULTS_COMPARISON.json`
- `validation/PROFILE_EVALUATION_WITNESS.json`
- `taylor/WOLFRAM_VERIFICATION.json`, `theory/LITERATURE_RETRIEVAL.json`
- https://dlmf.nist.gov/33.2
- https://dlmf.nist.gov/1.9
- https://flintlib.org/doc/acb_calc.html
- https://arxiv.org/abs/1802.07942
