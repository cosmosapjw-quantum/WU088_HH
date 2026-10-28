# R15 재사용 정리 — positive B3 forcing의 quartic memory certificate

이 문서는 완성된 `theory/PROOF_KO.md`, `RESULTS_KO.md`, `CONTRACT.json`과 저장된 verification 판정을 재서술한다. 새 유도·실행·CAS·문헌조사·심사를 수행하지 않았다. 작성 기준은 **S08, workflow16/20, DAG29/46**이며 C9의 최종 채택 심사는 진행 중이다. 기존70-file scientific payload SHA256은 `828888e952c15bd94d37d7dd30c0676df9470ca316bb1dbb8334c6c218b0e909`다.

## 1. 재사용 전제

고정 column-conservative Metzler \(K\), \(\pi\ge0\), \(\mathbf1^\top\pi=1\), destruction vector \(d\ge0\)와 비음수 w box에서

\[
H=\pi d^\top-\operatorname{diag}(d),\qquad A_w=K+wH
\]

를 사용한다. 실제 full-A evolution operator U가 **허용된 모든 시작시각과 이력**에서 동일한 \(0\le q\le1,\tau>0\)에 대해

\[
\|U(s+\tau,s)\|_{\mathrm{zero\ mass},1}\le q,
\qquad \|U(s+\delta,s)\|_{\mathrm{zero\ mass},1}\le1
\quad(0\le\delta<\tau)
\]

를 만족해야 한다. Source family·state order·norm·clock와 전체 w domain을 이 certificate에 결속한다. Constant-w certificate의 확인 범위는 해당 constant-w 이력이며, switching histories를 허용하려면 그 이력에 대한 certificate가 필요하다. 입력의 선언 flags와 hash는 결속 조건을 기록한다. Nominal K의 수축률만으로 full-A 전제를 충족시키지 않는다.

Source/observation clocks는 같은 \([t_0,T]\)의 exact rational partitions다. 각 **원래 source cell**에서 \(g_r,g_e\)는 주어진 비음수 rational Bernstein-B3 계수 네 개로 표현되고, 관련 whole fine/coarse-domain forcing을 지배해야 한다. 이것이 현재 입력 원뿔이다. 모든 pointwise-nonnegative cubic으로 범위를 넓히지 않으며, R14의 full nonnegative quadratic 전처리 결과는 별도 유효 범위로 보존한다. Generic cap adapter는 포함하지 않는다.

\(R_0,E_0,c\ge0\), 고정 signed \(d_c\), \(E=|\eta|\), coarse \(l^1=4E\)를 유지한다. c는 비교 결합계수이며 모든 시간과 \(d_c\)는 같은 clock의 단위를 따른다. 근거: `theory/PROOF_KO.md` §1–2, `CONTRACT.json`.

## 2. 재사용 가능한 결론

원래 \(t_0\)에서 정의한

\[
h(a)=q^{\lfloor a/\tau\rfloor},\qquad h(0)=1,
\]
\[
\mathcal R(t)=h(t-t_0)R_0+\int_{t_0}^t h(t-s)g_r(s)\,ds,
\]
\[
\mathcal E(t)=e^{d_c(t-t_0)}E_0+
\int_{t_0}^t e^{d_c(t-s)}[c\mathcal R(s)+g_e(s)]\,ds
\]

를 계산한다. q=0에서도 첫 age block의 h는1이다. Full-A·forcing·초기값·signed scalar comparison 전제가 성립하면 \(\mathcal R,\mathcal E\)는 해당 residual/scalar error의 상계다. Source/observation refinement나 extrema subdivision에서 memory를 재시작하지 않는다.

**Positive B4 구성.** Observation knots와 source knots의 \(k\tau\) 이동을 exact union한 base grid에서 overlap 끝점 L,U와 중점 M은 affine다. Cubic Simpson 항등식

\[
\int_L^U g_r(s)ds=\frac{U-L}{6}\{g_r(L)+4g_r(M)+g_r(U)\}
\]

과 positive B1×B3 product로 각 base cell의 convolution을 비음수 B4로 얻는다. \(q^k\) 가중합 및 초기 memory를 더한

\[
P(u)=\sum_{i=0}^4B_i\mathsf B_i^4(u),\qquad B_i\ge0,
\quad0\le u\le1
\]

를 셀마다 한 번 저장한다. 근거: `theory/PROOF_KO.md` §3–5.

**Zero-aware whole-cell extrema.** Derivative-B3 coefficients는 \(4(B_{i+1}-B_i)\)다. Exact zeros를 제거한 variation V는 midpoint subdivision에서 \(V_L+V_R\le V\)를 만족한다. All-zero derivative는 constant, 한 부호 derivative는 monotone이므로 endpoint maximum이 exact다. Mixed leaves만 depth D까지 분할하고, 남은 leaf에는 coefficient-hull upper와 endpoint/midpoint lower를 사용한다. Shared midpoint zero, repeated roots와 rootless mixed coefficients를 포함하며 terminal leaf를 isolated root로 취급하지 않는다.

한 깊이의 mixed nodes는 최대3이므로 split≤3D, visit≤6D+1이다. D=96에서는 셀당 **288 splits / 577 visits**이고

\[
0\le U_{\rm exact}-L_{\rm exact}
\le M_B2^{-96}\le4C_{\max}2^{-96},
\quad M_B=4\max_i|B_{i+1}-B_i|,\ C_{\max}=\max_iB_i.
\]

Dyadic128 outward conversion의 추가 폭은 최대 \(2\cdot2^{-128}\)다. Observation whole cells는 포함된 base certificates의 max로 집계한다. 근거: `theory/PROOF_KO.md` §6–8.

**Endpoint 규약.** Convolution은 연속이고 초기 staircase term만 하향 jump할 수 있다. P(0)은 실제 왼쪽 값, P(1)은 오른쪽 left limit다. 실제 오른쪽 값에는 해당 시각의 h를 별도로 적용한다. Closed-cell supremum의 left-limit witness는 유효하지만 attained point sample과 구별한다. 출력의 R/E lower endpoints는 제공된 forcing bounds로 만든 **ideal comparison 함수의 하한**이다. Whole-cell lower는 그 supremum의 하한이며 실제 물리 오차의 하한이 아니다. 보편적 raw/capped/physical gain을 결론에 넣지 않는다. 근거: `theory/PROOF_KO.md` §1, §5, §11.

## 3. Signed scalar 전달과 유한 계산 계약

Base cell의 \(cP+g_e\)를 비음수 B4 coefficients Q_i로 표현한다. \(z=d_c\Delta\)에서

\[
W_i(z,\Delta)=\Delta\int_0^1e^{z(1-u)}\mathsf B_i^4(u)du,
\qquad
\mathcal E_{\rm next}=e^z\mathcal E_{\rm left}+\sum_iQ_iW_i.
\]

z≥0의 positive series 계수는

\[
\beta_i(n)=\binom4i\frac{i!(n+4-i)!}{(n+5)!},
\qquad
W_i=\Delta\sum_{n\ge0}\frac{z^n}{n!}\beta_i(n).
\]

z<0은 \(W_i(z)=e^zW_{4-i}(-z)\), z=0은 \(W_i=\Delta/5\)를 사용한다. \(|d_c|(T-t_0)\le16\)에서 Taylor0..96, first omitted index97, 이후 ratio≤16/98의 positive tail와 dyadic outward arithmetic으로 포함성을 유지한다. d_c의 damping sign은 보존한다.

Whole-E는 \(Q_{\max}=cU_R+U_e\)와 incoming E upper에서 출발한 같은 signed-\(d_c\) 상수 forcing majorant Y로 감싼다. Whole upper는 **\(\max(E_{\rm left,upper},Y(\Delta)_{\rm upper})\)**이며, 다음 셀에는 별도의 polynomial-forcing endpoint interval을 전달한다. 근거: `theory/PROOF_KO.md` §9–12.

계약은 states≤13, source≤16, observation≤32, base≤512, full blocks≤8, input components≤256bits, production/saved-derived components≤16384bits를 사용한다. Base당 한 번 조립할 때 overlap precharge≤73728, 전체 splits≤147456, visits≤295424다. Arithmetic/domain 초과는 명시적으로 거부하며 모든 최대-domain 입력의 CPU·memory 완료를 일반화하지 않는다. 근거: `CONTRACT.json`, `theory/PROOF_KO.md` §13–14.

## 4. 저장된 검증과 적용 지위

| 검증 | 실제 저장 결과 | 해석 |
|---|---|---|
| Primary | 302/302, 21 models, 68 rejection guards, 14 depth rows | 고정 산술·구현 캠페인 결과 |
| Independent reference | 302/302 semantic records, 실패0; pure exact238, mixed exact/guarded21 | 원래 J0..J3 적분·독립 power/Sturm 경로와 별도 scalar 계산 |
| Decimal160 부분 | 고정 guard 비교784건 통과; strict 포함 실패59건, 예시50개 보존 | `1e-80*max(1,abs(reference),abs(lower),abs(upper))`에 따른 corroboration; rigorous interval reference로 분류하지 않음 |
| Wolfram | 72/72 unique exact-zero residuals, 이번 batch 관측 경고0 | 명시한 가정 아래 유한 algebraic identities의 corroboration |

근거는 `verification/PRIMARY_ASSESSMENT.json`, `REFERENCE_ASSESSMENT.json`, `CAS_ASSESSMENT.json`과 `RESULTS_KO.md`다. Exact 유리수/Sturm 판정은 tolerance 없이 수행됐으며 Decimal guard는 실행 전에 고정됐다. 모든21 control models는 **ARITHMETIC_CONTROL_PREMISE**에 속한다. q=0을 포함한 경계 대조군의 성공이 새로운 물리 certificate를 공급하지 않는다.

실제 GL2022 HD reactive array와 named physical consumer/state/density/clock는 조사 범위에서 **INPUT_PENDING**이다. Native v **UNSPECIFIED**, **MISSING_NOT_ZERO**, **TIQM/SQM DISTINCT**, **HH_R10 OFF**, **production NOT_ISSUED**, **L4 false**, **central/physical delta0**을 보존한다. 이 문서는 기존 증명·실행 결과의 재사용 진술이며 C9의 최종 채택 판정을 대신하지 않는다.
