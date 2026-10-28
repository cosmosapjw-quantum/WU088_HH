# R7 유한 비선형 반응 피드백 구현

## 적용 범위와 현재 상태

이 구현은 `theory/NONLINEAR_FEEDBACK_PROOF_KO.md`의 유한 질량작용 반응식, HD 보존량으로 축약한 오차 비교계, 인과적인 블록 끝점 재귀를 계산한다. 원천 상태별 반응률, 실제 기체 밀도와 시계, TIQM/SQM 선택, 공통 반응물 풀의 물리적 동일성을 새로 추정하지 않는다. 입력과 출력의 `source_scope`, `common_pool_binding`, `clock` 필드에 조건을 명시한다.

작성 단계의 검증은 AST 구문 분석이다. 작성 에이전트는 모듈을 import하거나 과학 함수, 테스트, ODE를 실행하지 않았다. 실제 검증 결과와 비용은 부모 작업이 계약에 따라 한 번 실행하는 `raw/PRIMARY_RESULTS.json`에 기록한다. 이 파일의 구현 설명은 실행 성공을 주장하지 않는다.

## 파일과 공개 API

| 파일 또는 API | 역할 |
|---|---|
| `src/nonlinear_feedback.py` | 표준 라이브러리만 사용하는 생산 구현 |
| `verification/run_primary.py` | 고정 SHA 입력에 대한 한 번의 유한 검증 및 결과 보존 |
| `Q`, `rational_text`, `export` | 정확한 수 입력, 큰 정수의 안전한 문자열 변환, JSON 출력 |
| `Interval`, `interval` | 순서와 비음성·확률 범위를 검사하는 닫힌 유리수 구간 |
| `Event`, `ReactionNetwork` | 정수 반응물·생성물 계수, 정확한 보존량 행, 질량작용 RHS |
| `mass_action_jacobian_upper` | 비음수 상자에서 반응률 Jacobian의 성분별 상계 |
| `hd_network`, `hd_rhs`, `hd_coarse_rhs` | 명시적인 HD 반응 채널과 주어진 명목 생성자 결합 |
| `hd_aggregate`, `hd_lift`, `hd_invariants` | HD 총량·리프트·H/D/전하 보존량 |
| `hd_scalar_error` | 동일 보존량류 확인 및 정확한 `R`, `E`, `eta` 계산 |
| `hd_lift_defect_norm` | 주어진 `K`, `pi`, `pi_dot`의 정확한 리프트 결함 norm |
| `hd_feedback_coefficients` | 상자와 원천 조건에 따른 `B`, `g`의 바깥 방향 계수 |
| `exp_neg_enclosure` | `exp(-x)`의 양방향 유리수 포함구간 |
| `interior_feedback_upper` | 주어진 블록 내부 시각의 비수축 비교 상계 |
| `block_feedback_upper` | 인과적 끝점 `T`, `q`와 별도의 블록 전체 상계 |

모든 과학 스칼라는 `int`, `Fraction`, 십진 또는 유리수 문자열이다. 이진 `float`와 `bool` 입력은 거부한다. 입력에 소수점 표기가 필요하면 `"0.125"`처럼 문자열로 전달한다. 실행 시간 등 비과학 메타데이터만 부동소수점으로 기록한다.

## 일반 반응식과 경계 처리

`Event`의 열은 `products - reactants`이다. 각 반응의 비음수 속도상수와 비음수 정수 지수로 질량작용률을 구성한다. 모든 선언된 보존량 행이 모든 반응 열을 정확히 소거해야 `ReactionNetwork`를 생성할 수 있다. 소비되는 종의 밀도가 0이면 해당 소비 항의 반응률도 0이므로 비음수 직교체의 경계를 보존한다.

`mass_action_jacobian_upper`는 반응별·상태별 행렬을 반환한다. 미분하는 변수의 지수가 0인 항은 거듭제곱을 계산하기 전에 정확히 0으로 처리한다. 지수가 1이고 해당 밀도가 0이면 남은 거듭제곱은 0승이며 1이다. 따라서 0 밀도에서 음수 지수나 `0/0`을 만들지 않는다.

유한 구현 한계는 일반 종 수 1–16, 채널 수 최대 64, 각 정수 계수 0–4, 총 반응 차수 최대 4이다. HD 계열은 저장소 3개를 함께 세므로 HD 상태 수 1–13이다. 이 한계는 물리 법칙의 제약이 아니라 이 연구 단위의 코드·비용 계약이다.

## HD 채널과 정확한 보존량

HD 미세 상태 순서는 `(u,v,w,x_0,...,x_(n-1))`이고, 각 채널은 다음과 같다.

\[
u+v\ \rightleftarrows\ w+x_j,
\qquad a_j^+=k_f\alpha_j u v,
\qquad a_j^-=d_j w x_j.
\]

`alpha`는 정확한 simplex 입력이어야 한다. TIQM과 SQM은 한 번에 하나만 선택하는 원천 대안이다. `TIQM+SQM` 같은 결합 표기는 거부한다. 합성 검증은 `SYNTHETIC`을 명시한다.

집계 상태 `y=(u,v,w,X)`, `X=sum_j x_j`의 보존량은

\[
H=2u+w+X,\qquad D=v+X,\qquad Q=v+w.
\]

`hd_scalar_error`는 미세 집계와 coarse 상태의 이 세 보존량을 정확히 비교한다. 같을 때만

\[
y-\bar y=(-1,-1,1,1)\eta,\quad E=|\eta|,
\quad R=\lVert x-\pi X\rVert_1
\]

를 반환한다. `hd_invariants`에는 집계 4벡터를 전달한다. 미세 벡터는 먼저 `hd_aggregate`로 변환한다.

`hd_invariant_box`는 보존량으로부터 얻는 일반적인 안전 상자를 제공한다. 고정 검증기는 동일 보존량류의 정확한 선분

\[
u=A-X,\quad v=D-X,\quad w=Q-D+X,
\quad A=(H-Q+D)/2
\]

및 `max(0,D-Q)<=X<=min(D,A)`를 별도로 구성해 고정 입력 상자가 두 ODE의 모든 비음수 궤적을 포함하는지 확인한다.

## 비교 계수의 바깥 방향

입력 상자와 속도 구간에서 `Delta_d=max(d_hi)-min(d_lo)`, `v_star=Delta_d/2`, `h_star=2 max_j d_hi_j(1-pi_lo_j)`를 사용한다. `pi` 구간의 성분 범위가 `[0,1]`에 있고 하한 합이 1 이하, 상한 합이 1 이상인지 확인한다. 실제 `q_star>=||K pi-pi_dot||_1`, `theta_star>=||alpha-pi||_1`, coarse scalar defect 상계와 상자 유효성은 호출자의 명시적인 증거이다. 고정 검증기는 해당 값들을 정확히 계산하거나 보존량으로 증명하여 입력과 대조한다.

`B=[[a,b],[c,d]]`, `g=(g_r,g_e)`의 `a,b,c,g_r,g_e`에는 상한, 감쇠 `d`에는 더 약한 감쇠를 주는 하한을 사용한다. `d`는 음수일 수 있다. `kf>=0`, `d_j>=0`, `q_star>=0`, `0<=theta_star<=2`를 검사한다. `g_e`를 암묵적으로 0으로 두지 않는다. coarse 반응률이 다른 고정 대조군은 `coarse_kf_offset`과 `|offset| M_u M_v`를 명시한다.

## 지수행렬과 forcing 적분의 유리수 상계

명시한 오차 좌표 scale `s_0,s_1>0`에 대해 3×3 확대 행렬을 구성한다.

\[
M=\begin{pmatrix}
a & b s_1/s_0 & g_r/s_0\\
c s_0/s_1 & d & g_e/s_1\\
0&0&0
\end{pmatrix},\qquad
\gamma=\max(0,-d),\qquad C=H(M+\gamma I)\ge0.
\]

`C`와 양의 Taylor 항을 `2^-bits` 격자로 위쪽 반올림한다. 이전 항의 정수 행렬에 위쪽 `C`를 곱한 뒤 정확한 정수 올림 나눗셈을 적용하므로 항별 상계가 귀납적으로 유지된다. 꼬리 상계에 쓰는 `z`는 원래 행렬의 근사 norm이 아니라 **실제로 위쪽 반올림한 `C`의 유도 무한 norm**이다. `z<=16`, `N+2>z`, `0<=N<=256`, `128<=bits<=512`를 검사한다.

\[
\sum_{k=N+1}^{\infty}\frac{z^k}{k!}
\le \frac{z^{N+1}}{(N+1)!}\frac1{1-z/(N+2)}.
\]

스칼라 항과 기하급수 꼬리도 정확한 정수 올림으로 상계한다. 이 꼬리 상계는 각 행렬 원소에 적용한다. `exp(-gamma H)`는 양의 `exp(gamma H)` Taylor 다항식의 아래·위 포함값을 역수로 바꾸어 얻는다. 최종 곱도 위로 반올림한다. 따라서 구현의 분모 크기는 원천의 큰 유리수 분모와 반복 Taylor 곱 때문에 무한히 증가하지 않는다. 과학 값 자체는 끝까지 정확한 유리수이다.

상단 2×2 블록은 `W_upper>=exp(BH)`, 상단 마지막 열은 `q>=integral_0^H exp(Bs)g ds`를 준다. 좌표 scale을 원래 좌표로 되돌린다. `B`의 역행렬을 사용하지 않으므로 특이 행렬에서도 유효하다. `B^2=0`이면 `W=I+HB`, `q=Hg+H^2 Bg/2`를 정확히 반환한다. `u=0`은 정확한 항등 행렬과 0 forcing으로 처리한다.

## 끝점과 블록 전체의 구분

블록 끝점은 다음을 반환한다.

\[
T=W_{\rm upper}-(1-\rho)e_1e_1^T,\qquad
w_{\rm next}=T w_0+q.
\]

`a>=0` 및 비음수 교차항 때문에 `exp(BH)[0,0]>=1`이고 `T>=0`이다. 코드도 `T`의 비음성을 확인한다. `rho`는 초기 residual 항에만 적용한다. forcing 전체에 `rho`를 곱하지 않는다. binding에는 인증서 identity, 정확한 `H/rho`, 시계, `l1_on_kerP`, `nominal_K`, 피드백을 계수에 포함했다는 명시값이 필요하다. 이 메타데이터는 물리적 원천 결합을 자동으로 증명하지 않는다.

`d<0`일 때 두 번째 오차 좌표는 감소할 수 있으므로 끝점 값으로 전체 블록을 덮지 않는다. 점별 API는 실제 `B`를 사용한다. 전체 블록 상계는 `Bplus=[[a,b],[c,max(d,0)]]`의 비수축 비교계 끝점을 사용한다. `Bplus>=0`인 비교계는 비음수 초기값과 forcing에서 시간에 대해 증가하고 원래 비교계를 지배한다.

## 한 번의 고정 검증

`verification/PRIMARY_INPUT.json`의 SHA256을 코드에 고정한다. 다른 입력이나 이미 존재하는 출력 파일은 실행 전에 거부한다. 부모가 실행하는 검증의 범위는 다음과 같다.

- 고정 affine 대조군 5개: 0 행렬, 상수 forcing, 특이 nilpotent, 음의 대각 감쇠, 교차 결합과 음의 감쇠.
- 고정 HD 대조군 4개: 2상태 무반응, 2상태 비선형, coarse source defect, 저장된 9상태 명목 `K`에 합성 반응을 결합한 조건부 대조군.
- HD별 3블록, 블록별 내부 시각 `0,H/4,H/2,3H/4,H`. 같은 `B,g,H,degree,bits,scales`의 커널을 재사용하고 초기 오차만 갱신한다.
- 정확한 H/D/전하, 채널 RHS, 경계 비음성, 초기 scalar compatibility, `q/theta` 상계, 전역 보존량 상자, 구간 확대 방향, 정의역 거부 동작.
- 저장 R6 결과의 SHA, 원천 hash, `H/rho` 문자값 및 저장된 `K` 구간에 대한 현재 입력의 소속만 확인한다. R6 코드를 import하거나 이전 과학 실행을 반복하지 않는다.
- 고정 late-forcing 대조군: `gamma=H=J=1`, `epsilon=1/4`. 전체 입력에 `rho`를 곱하는 식보다 실제 끝점이 크다는 엄밀한 양의 간격을 기록한다.

CPU 제한은 60초이다. 결과에는 함수 출력 전체, 모든 check, 실패와 traceback, 입력·코어·검증기·계약·증명·재사용 원천 hash, CPU 및 wall time을 보존한다. 검증기는 결과를 생성 전용으로 저장하며 실패를 PASS로 바꾸거나 숨기지 않는다. 독립 reference는 별도 작성자가 별도 구현으로 수행한다.

## 결과 JSON 구조

`affine_cases[]`는 원래 입력과 `certificate`, `queries`를 가진다. `hd_cases[]`는 원래 입력, `coefficients`, `initial_error`, `binding`, `requested_blocks`, `blocks[]`를 가진다. 각 블록에는 `index`, 전역 시작 시각 `t0`, `w0`, `certificate`, `queries`가 있다. `queries[].t`는 블록 내부의 지역 시각이다.

`certificate.W_upper`는 2×2, `T`는 2×2, `q`, `w_next_upper`, `whole_block_upper`는 각각 2벡터이다. 확대 3×3 행렬을 `W_upper`라고 저장하지 않는다. `queries[].bound`도 `(R,E)` 순서의 2벡터이다. 모든 유리수는 정확한 문자열로 직렬화한다.

## 물리적 한계

이 결과는 새로운 반응별 source array나 물리적 소비자를 제공하지 않는다. 저장된 R6 생성자 구간과 `H/rho` 재사용은 명목 `K`의 수학적 입력을 고정한다. 새로 선언한 유리수 `pi`는 저장된 Gibbs 구간을 대체하는 물리적 재추정이 아니며, 그 차이는 새 비교계의 명시적 `q_star`로 처리한다. 실제 공통 저장소, 밀도, 시계, branch, 원천 상태 정렬을 결합하기 전에는 `production=NOT_ISSUED`와 기존 물리적 미승인 상태를 유지한다.
