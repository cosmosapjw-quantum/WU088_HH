# R11 코드 설계 — 전체 생성자 블록과 forcing convolution

## 입력·전제와 API

`src/full_generator_blocks.py`는 `generator_certificate`, `bernstein_weights`, `convolution_sweep`, `sweep`를 제공한다. `sweep`는 고정된 exact `K, pi, destruction`, 비음수 전체 `w_box`, 인증된 nominal `tau, rho_K`, 같은 source/state/clock binding, 전체 fine/coarse 영역의 `c,d,g_r,g_e`를 받는다. 생성자 열합은 정확히 0, 비대각은 비음수, pi는 simplex이며 n=1..13이다. 숫자는 int·Fraction·유리수 text로 제한하고 float·bool을 거부한다. 입력 numerator/denominator는 각각 8,192bit 이하, 표본 셀은 1..192, `tau/delta`는 정확한 정수 1..192이다. 현재 forcing 셀과 출력 셀은 같은 균일 exact grid다. `c>=0`, `d`는 signed, forcing은 비음수 scalar 또는 셀별 배열이다.

Nominal 인증은 source SHA·JSON pointer·certificate ID·정확한 K matrix hash·tau·rho·binding과 `fixed_homogeneous_K`, `uniform_all_starts`를 요구한다. 이 구조 검사는 외부 인증의 과학적 진위를 증명하지 않는다. 실제 primary는 동결 R7 입력과 출력 SHA를 확인한 뒤 기존 exact K/tau/rho를 연결한다. 원래 homogeneous K 인증은 시간 차이만으로 모든 시작시각에 적용된다. 실제 HD 반응 배열이나 physical consumer를 생성하지 않는다.

## full-A 인증의 수치화

`H=pi*d^T-diag(d)`, `bH=max_j d_j(1-pi_j)`, `||H||_1=2bH`를 exact arithmetic으로 계산한다. `eps=bH*M_w*tau`에 대해 다음 두 값을 구성한다.

\[
q_{\rm add}=\min(1,\rho_K+2\epsilon),\qquad
q_{\rm minor}=1-e^{-\epsilon}(1-\rho_K).
\]

생산 q는 두 값의 바깥쪽 upper와 1의 최솟값이다. `exp(-eps)` lower를 사용하여 positive gap을 축소하는 방향으로 계산한다. q가 1로 반올림되면 코드의 strict contraction 상태도 false가 된다. 실제 
minorization 정리와 모든 시작시각·모든 가측 w 전제는 이론 문서가 제공한다. 생산 q는 고정된 유리수 upper이므로 이후 lower 배열은 이 **선택된 q의 이상적 비교해**를 둘러싼다.

## 블록 age와 현재 forcing

`m=tau/delta`, `h_n=q^floor(n/m)`, `h_0=1`이다. h는 dyadic128 내림·올림 recurrence로 보존하고, forcing 적분은 양의 합으로 계산한다.

\[
F_n=\Delta\sum_{j=0}^{n-1}h_{n-1-j}g_{r,j},\qquad
R_n=h_nR_0+F_n.
\]

셀 n의 내부에서 R envelope는 다음 두 값 사이의 affine 함수다.

\[
L_n=h_nR_0+F_n,\qquad V_n=h_nR_0+F_{n+1}.
\]

V는 오른쪽 endpoint에서 접근하는 left limit다. 블록 경계의 실제 endpoint envelope는 `h_(n+1)R0+F_(n+1)`로 내려갈 수 있다. 닫힌 셀 whole R은 L,V 및 보고된 오른쪽 outward endpoint의 최댓값을 사용한다. Forcing의 현재 셀 계수는 h0=1이며 q를 미리 곱하지 않는다. Cap 적용 후에도 전역 R age나 forcing memory를 reset하지 않는다.

## signed d의 E 적분

셀 내부 `R(u)=(1-u/Delta)L+(u/Delta)V`를 직접 적분한다.

\[
E_{n+1}=e^{d\Delta}E_n+c(W_0L+W_1V)+\phi g_{e,n},\qquad
\phi=W_0+W_1.
\]

\(x=d\Delta\ge0\)에서 
\[
W_0=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+2)},\quad
W_1=\Delta\sum_{k\ge0}\frac{x^k}{k!(k+1)(k+2)}.
\]

x<0에서는 |x|의 위 두 양의 급수를 서로 교환하고 `exp(x)`를 곱한다. 이 변환은 cancellation 없이 d=0, d>0, d<0를 모두 다룬다. 양의 exp 급수를 96차까지 계산하고, rounded |x|<=16에서
\[
\mathrm{tail}\le \frac{|x|^{97}}{97!}\frac{1}{1-|x|/98}
\]
를 각 moment의 tail에도 적용한다. Moment 분모는 1 이상이므로 같은 tail은 안전하다. 모든 항·곱·합·최종 결과를 dyadic128 바깥쪽으로 반올림한다. Negative exp는 positive exp interval의 reciprocal로 얻는다.

Whole E는 해당 셀 Rwhole을 상수 forcing에 넣은 signed scalar 비교해를 쓴다. 그 해의 미분 부호는 일정하므로 `max(Eleft, exp(dDelta)*Eleft+phi*(cRwhole+ge))`가 닫힌 셀 전체를 덮는다. 보고된 outward endpoint와도 max를 취한다. d의 부호로 endpoint 단조성을 추정하지 않는다.

## source-backed cap

Cap은 R10 `raw/PRIMARY_RESULTS.json` SHA
`1713df54bc3653003614f3deba93212735a345e8d7220f053ab9af2d84677fb1`의 `/hd_cases/i/capped/endpoints_upper` 또는 `/hd_cases/i/capped/whole_cells_upper`만 허용한다. 같은 delta·cell count·binding·case index를 검사한다. Primary가 해당 실제 저장 배열에서 cap을 조립한다.

R point와 whole은 각각 같은 quantity/clock/cell의 valid upper를 min으로 교차한다. Capped E의 셀 전파는 capped Rwhole과 이전 capped E를 쓰는 signed scalar bound로 계산하고, raw E 및 R10의 같은 point/whole cap과 교차한다. 보고된 각 endpoint는 양옆 닫힌 셀에도 속하므로 출력 단계에서 인접 whole cap과 추가 교차한다. 이 마지막 교차는 전역 R convolution의 memory나 미분식을 변경하지 않는다. Capped lower는 반환하지 않는다.

## 검증 범위

Primary는 저장된 HD 네 사례를 192셀로 비교한다. Nominal K 인증·initial invariant class·fine/coarse whole box·forcing coefficients의 동일성을 확인한 뒤 새 full-A q와 convolution만 실행한다. 별도 controls는 q0/q1/near-one, fresh late forcing, 블록 경계 left limit, signed d와 near-zero d, 셀별 forcing을 다룬다. Generator controls는 H0/Mw0, simplex 경계, reducible K, n1/n13, additive saturation와 minorization strict contraction을 구별한다. 잘못된 source·state·clock·cell·cap과 수치 영역 입력은 거부한다. 기존 ODE·native source·predecessor suite는 실행하지 않는다.

이 파일 작성 시 과학 실행은 아직 수행하지 않았다. 실제 freeze, root의 단일 primary 실행, 독립 reference와 C9 결과는 별도 실행 기록이 결정한다.
