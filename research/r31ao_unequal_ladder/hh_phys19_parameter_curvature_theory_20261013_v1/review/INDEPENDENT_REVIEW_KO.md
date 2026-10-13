# WU088_HH PHYS19 — 순수 곡률 application의 독립 심사

## 판정

**`PASS_SCOPED` — 현재 fixed-alpha, same-COMMON, 전역 (lambda,b) rectangle, 원 C2 계약 안에서 PHYS19 순수 곡률 결과와 readout02의 채택을 권고한다.** 미해결된 producer 수식·포함 계산 결함을 발견하지 않았다. 이 판정은 아래 SHA-256으로 결박한 application, 실제 실행 snapshot, 결과, geometry readout에 적용한다. Root의 최종 scientific adoption 또는 게시 영수증을 대신하지 않는다.

실제 독립 계산은 producer를 import하거나 producer main을 다시 실행하지 않았다. 별도로 작성한 `fractions.Fraction` 구간 클래스, ordinary pure jet의 이항계수 convolution, Gaussian elimination을 사용하여 동결된 원 입력과 저장된 중간값으로 포함을 다시 계산했다. 외부 source callback, 새 reaction fit, nonlinear root solve, history replay는 모두 0이다.

| 최종 독립 실행 | 확인값 |
|---|---:|
| 실행 | `run03` |
| 상태 / 종료 코드 | `pass_scoped` / 0 |
| 검사항목 | 362 |
| 구간 비교 묶음 | 265 |
| exact scalar endpoint 포함 비교 | 2,057 |
| 저장된 outward decimal 구간 검사 | 3,174 |
| adopted contract 입력 SHA/bytes 일치 | 23 / 23 |
| 계산 본문 경과 시간 | 1.752876122 s |
| wrapper wall time | 1.869888170 s |
| 최대 RSS | 52,448 KiB |
| stderr | 0 bytes |

## 1. 심사한 과학적 범위와 실제 근거

한 admissible 물리 계수 선택 alpha를 고정하고, 같은 COMMON과 같은 전역 lambda,b가 [0,1]^2를 움직이는 함수 계열을 심사했다. Gas 4성분과 photon 35성분, 즉 33 active와 number/energy guard 2개를 유지한다. 첫 half, Full, carried 둘째 half의 순수 ordinary second derivative는 Taylor coefficient의 2배이며, 순수 jet 자체에 1/2!를 넣지 않는다. 기존 U,V는 각각 첫 lambda,b 응답이고 W는 기존 mixed 응답이다.

보존된 독립 유도 `PURE_CURVATURE_INDEPENDENT_DERIVATION_KO.md`를 producer보다 먼저 읽고 D5–D67의 식과 구현을 대조했다. 별도 하위 심사 `/root/curvature_audit/formula_source`가 source bridge, Full 잔차, endpoint 차이, seven-sector photon 식, guard 및 finite temperature quotient를 읽기 전용으로 다시 검토했다. 이 하위 심사도 producer·검사기·기존 suite를 실행하지 않았다.

본 심사는 기존 atomic/source enclosure 및 root branch certificate의 과학적 기원을 재실행하지 않는다. 채택된 입력들의 bytes와 SHA를 모두 확인하고 그 계약 위의 새 PHYS19 미분, 전송, 포함, readout을 독립적으로 검사했다. 결과 파일의 exact endpoints를 비교 기준으로 사용했으며, decimal 표시의 일치는 별도로 확인했다.

## 2. 역연산자와 ordinary second derivative

첫 half의 J, E=I-J는 원 first-half source export와 연결했다. B,S,q는 원 preflight에 연결하고 B>=0, S>0, |E|<=B 및 weighted row sum<=q<1을 exact Fraction으로 확인했다. 둘째 half의 E는 PHYS14의 `L_hFg`와 일치하며 원 scale 및 refined contraction을 사용한다.

Full과 endpoint에는 원 `UNIFORM_ARITHMETIC.json`의 같은 C,B,S,q가 사용된다. Full JF의 source-box/centre Taylor 포함 및 signed E=(I-CJF) intersect [-B,B]도 다시 계산했다. Direct와 correlated endpoint의 certificate는 모두 이 Full inverse에 연결된다.

각 theta에서 K1, KF, K2, direct Kd, correlated Kd의 5개 certificate, 합계 10개를 독립 Gaussian elimination으로 검산했다. 각 stored RHS 또는 C*RHS가 실제 RHS에 연결됨을 확인하고,

\[
m=(I-B)^{-1}\operatorname{mag}(Cf),\qquad
m-Bm=\operatorname{mag}(Cf),\qquad m\ge0
\]

를 exact Fraction으로 확인했다. 초기 enclosure `Cf+[-Bm,Bm]`와 signed E를 이용한 3회 포함 교차를 다시 계산했으며 저장된 응답이 모두 이 독립 포함을 담았다.

순수 implicit 식은

\[
JK=-H_{gg}[p,p]-2H_{g\theta}p
\]

로 확인했다. First-half `G_gg`, `G_g_theta`는 이미 duration과 잔차 부호가 들어 있는 export이므로 시간 인수를 다시 곱하지 않는다. Full source Hessian에는 -2h, Full HH column에는 -2h가 들어가고, Full birth column에는 QF,b=2Jgamma가 들어간다. 바깥 순수 product factor 2와 결합하여 필요한 Full factor 4가 보존된다.

둘째 half source Hessian RHS의 h와 HH factor 2도 독립 재계산했다. Photon forcing graph에서 K2만 0으로 두고 carried Q2''는 보존한다. 이 처리로 unknown linear K2 항은 J2에만 들어간다. 실제 P2''와 stage increment를 만들 때는 K2 항이 복원된다.

## 3. Carried photon과 일곱 sector

독립 pure jet graph는 각 35-slot Q1,Z1,Q2의 value, first, second 응답을 재구성하고 원 value/first enclosure와의 교차까지 확인했다. P1,P2,Z2의 새 pure slot과 둘째 half의 photon forcing도 포함 비교를 통과했다. 독립적으로 전개한

\[
A''=haA^2K_x+2(ha)^2A^3p_x^2,
\quad
Z_1''=A_1''Q_1+2\delta_bA_1'J_\gamma,
\quad Q_2''=RZ_1''
\]

의 모든 35개 slot이 양쪽 theta에서 producer 포함 안에 들어갔다.

아래 일곱 sector의 pure derivative도 각각 35개 성분을 다시 계산했다.

| Sector | 검토한 핵심 |
|---|---|
| `opacity_change` | factored Delta A1와 stage pure increment, 모든 product factor 2 |
| `absorption_transport_commutator` | R와 A의 순서, active-to-active denominator 차이 |
| `stock_intermediate_redshift` | L(I-R)RZ0의 부호 |
| `stock_backward_euler` | tau^2 A^2 AF의 ordinary pure jet |
| `remap_composition` | R(rho)^2-R(rho^2), j=1 특수 열 및 guard 전송 |
| `birth_redshift` | b(LA)''+2 delta_b(LA)' |
| `birth_backward_euler` | -b C1''-2 delta_b C1' |

Producer의 `commQ`는 raw commutator의 active-to-guard 성분을 명시하지 않는다. 사용되는 실제 sector는 L*commQ이며 guard에는 L=L'=L''=0이므로 이 생략은 정확하다. 이를 raw 35-vector commutator의 잘못된 누락으로 판정하지 않았다. 둘째 incoming/outgoing guard의 carried curvature는 유지되고 P1/P2 absorption guard의 pure slot만 정확히 0이다.

독립 Full survival jet은 QF,b=2Jgamma를 사용하여 A_F''QF+4 delta_b A_F'Jgamma를 구성했다. 이 값과 저장된 Z2'', 일곱 sector 합을 사용하여 number 및 energy row를 별도로 계산했다. 모든 residual 구간이 0을 포함한다.

| theta | Number ledger residual | Energy ledger residual |
|---|---|---|
| lambda | [-1.816122247024919, 1.816215700463215]e-21 | [-2.484118464587787, 2.484246289998357]e-20 |
| b | [-3.927293390570897, 3.927105707070325]e-16 | [-5.380378094755118, 5.380120967415427]e-15 |

이 수치 검사는 정확한 보존식의 interval consistency 검사다. 보존식 자체의 증명은 독립 유도 D39와 전송 연산의 원식 대조에서 제공한다. Birth energy의 원 affine 항은 같은 theta의 두 번째 미분에서 0이 된다.

## 4. Source bridge와 endpoint 결함

원 nonphoto source를 추가로 대조한 결과,

\[
\mathscr U=(F_w^{np}+\chi_HF_x^{np})/(n_2e_2)
=xk_H(T)+f_2k_{He}(y,z,T)
\]

이다. 방향 xi=e_x+(w/Pi)e_w가 T를 고정하므로 kHe=(U-x DU[xi])/f2가 성립한다. 이 식의 첫 방향미분은 source Hessian까지로 닫힌다. Producer는 inherited kHe value bound를 미분하지 않고 원 함수 identity를 미분한다. 두 stage의 Hmean binary leaf가 동일함도 확인되어 expansion term의 source-time 차이가 소거된다.

독립 Fraction 계산은 K1 및 p1 방향에서 pullback, density ratio derivative, gstar/vstar, helium projector와 그 derivative, nonphoto 및 HH time derivative를 다시 평가했다. 저장된 bridge의 해당 포함들과 8개 gas residual sector가 모두 통과했다. 따라서 correlated curvature의 작은 결과가 source Hessian보다 높은 정칙성을 암묵적으로 가정하지 않는다.

Endpoint에서는 다음 8개 보정 sector를 독립 계산했다: linear movement, source Hessian difference, rational photo Hessian difference, balanced tangent defect, HH gradient difference/defect, birth gradient difference/defect. Source Hessian 차이는 같은 signed Hessian 범위의 두 값 차이이며 C3 또는 Hessian Lipschitz bound를 사용하지 않는다. HI rational 항의 분모 차이는 d_x 인수를 유지한다.

Direct RHS `JF*K2 + forcingF`, correlated RHS, 그리고 별도 `K2-KF`가 모두 재계산되었다. 세 Kd enclosure의 최종 교집합은 저장된 exact endpoints와 일치한다. Balanced tangent `p2-dtheta/2`는 같은-family `(p2+pF)/2`이며, 같은 Full JF를 모든 endpoint 항에 적용한다.

## 5. 정확한 유한 온도 quotient와 최종 순수 구간

원 binary leaves에서 CT와 최종 f2=nHe_stored/nH를 exact Fraction으로 복원했다. Electron row, Pi2, PiF=Pi2-le*d, 양의 denominator, goal row를 확인했다. 양 끝점의 T''와 다음 유한 quotient를 독립 계산했다.

\[
F''=\frac{(C_Te_w^T-T_F\ell_e)K_d
-T_2''d_e-2T_2'\ell_ed_\theta
-2F'\Pi_F'-F\ell_eK_2}{\Pi_F}.
\]

두 product factor 2, Full particle-count response PiF', 그리고 마지막 K2가 모두 올바르다. Quotient 포함과 별도의 T2''-TF'' 포함을 교차한 최종 결과가 통과했다.

| Quantity | 채택 가능한 outward 표시 |
|---|---|
| F_lambda_lambda [K] | [-4.510292217171e-14, -3.084478303660e-14] |
| F_b_b [K] | [-4.912098573204e-11, -4.450662359403e-11] |
| F_lambda_b [K], inherited pointwise | [-2.668505746423e-12, -2.118796636045e-12] |

두 순수 곡률은 전역 같은-family rectangle에서 엄격히 음수다. 두 축 방향 concavity가 판정된다.

## 6. Hessian과 유한 재구성 readout

Readout02는 PHYS18 mixed 파일의 `DeltaT_mixed_intersection_K`를 pointwise Hessian에, `four_corner_interaction_K`를 corner coefficient에 각각 결박한다. 이번 입력에서 두 구간의 exact endpoints가 같지만 두 quantity의 의미는 다르다. Geometry의 source-file SHA와 두 field 이름을 실제로 검증했다.

독립 Fraction 계산에서

\[
\det\nabla^2F\in[-5.748125770239212,-2.273799188447636]\times10^{-24}\;\mathrm{K}^2<0
\]

이고, v=(1,-1/24)에 대하여

\[
v^T\nabla^2Fv\in[4.618397504729307\times10^{-14},
1.142622520922812\times10^{-13}]\;\mathrm K>0.
\]

따라서 각 parameter point의 Hessian은 하나의 양의 eigenvalue와 하나의 음의 eigenvalue를 가진다. 이는 stationary saddle point 주장과 구별된다. 상속된 첫 derivative 구간은 F_lambda<0, F_b>0이며, 같은 방향의 첫 derivative도 [-3.003985803609359e-6,-2.831616000076853e-6] K로 음수다. Directional claim은 rectangle 안에 머무는 line segment에 적용한다.

순수 C2 interpolation 식은

\[
F-\mathcal LF\in-\tfrac12\lambda(1-\lambda)[F_{\lambda\lambda}]
-\tfrac12b(1-b)[F_{bb}]
\]

이며 두 곡률이 음수이므로 이 signed error는 비음수다. Exact same-family corner coefficients를 사용할 때의 경계와 finite decimal midpoint 보정 경계를 따로 확인했다.

| Readout | 검증된 upper bound |
|---|---:|
| Bilinear reconstruction remainder | 6.145761081776e-12 K |
| Exact pure-curvature midpoint correction remainder | 2.892887673208e-13 K |
| 표시된 finite decimal coefficients를 쓰는 correction remainder | 2.892887673216e-13 K |
| Bilinear / exact-midpoint remainder ratio | 약 21.2443820017437 |

위 작은 경계는 exact same-family corner representation에 대한 곡률 reconstruction error다. Anchor 및 chord 계수 자체의 inherited resolution을 포함하는 고정 수치 다항식의 전체 오차와 혼동하지 않는다. 모든 corner가 원 global F enclosure에 속한다는 조건을 이용한 F00 교집합은 대략 [-0.001585959249675372,-0.001278583452911096] K다. Anchor/chord/interaction midpoint radii와 finite decimal correction remainder를 모두 합친 deterministic model의 uniform upper bound는 **0.0001557338140092 K**다. 이 값도 exact Fraction으로 재현되었다.

## 7. 실행 기록, 검사기 수정 및 결박

각 실행 전에 검사기 snapshot, 코드 SHA, Python/platform, 입력 SHA, budget을 PRE_RUN.json에 기록했다. Budget은 wall 60 s, CPU soft 52 s / hard 56 s, address space 1.5 GiB이며 매 실행은 frozen enclosure 계산 1회로 제한했다.

| 실행 | 결과 | 원인과 조치 |
|---|---|---|
| run01 | 검사기 assert 종료, wall 0.216 s | 원 PHYS09 약 1,941-bit rational endpoint와 producer의 outward 256-bit 정규화 endpoint에 exact equality를 요구한 검사기 오류. 실제 lower/upper 차이는 안전한 outward 방향이었다. 요구를 exact containment로 수정했다. |
| run02 | 검사기 TypeError 종료, wall 1.871 s | lambda ledger의 scalar `ell`이 다음 b-loop의 vector 이름을 가리는 검사기 변수 shadowing. scalar를 `ellj`로 바꾸었다. |
| run03 | 전체 PASS, wall 1.870 s | 362 checks 및 모든 exact endpoint 비교 통과. |

이 두 실패에서 producer 또는 scientific inputs를 수정하지 않았다. 세 PRE_RUN, EXECUTED_CODE, RUN, STDOUT/STDERR와 실패 정보는 그대로 보존한다. 최종 검사기와 run03 snapshot의 SHA는 같다. 본문·결정 파일 작성은 새 scientific execution으로 세지 않는다.

| 결박 파일 | SHA-256 |
|---|---|
| Producer `src/curvature_application.py` 및 run01 snapshot | `c02af6b7b79a5be64b900c7bcaa1a37566e99e95dc15383e2b364bdb83e5aeaf` |
| `CURVATURE_RESULTS.json` | `0cf533a6a766f97ca3905113d2922f28dadd6c80f4b355dc0e81aa91c0b8d0fa` |
| `src/curvature_geometry.py` 및 readout02 snapshot | `35a6beab3b672f795d3d795ddf61302f3fe7e0122bcc4545b9e7db0f9724cdf7` |
| Independent final checker 및 run03 snapshot | `ea5064b4beb1310b488cba4b1b12525d9285ad6e5244f7ca88d327b508d0d87f` |
| run03 `PRE_RUN.json` | `39b4919eae793b6c5e4d8922872b947d876d5f7022fcda7193e53ec02df47405` |
| run03 `INDEPENDENT_FRACTION_AUDIT.json` | `b032ebc337d810dfc11403dfd42f192df0d0824ba7185e21666d04bd34416778` |

`INDEPENDENT_REVIEW.json`과 `VERDICT.json`은 위 파일 외에도 geometry 결과, adopted contract, original mixed 결과, 원식 검토 입력을 현재 bytes/SHA로 결박한다. `REVIEW_MANIFEST.json`에는 전체 심사 산출물의 hash가 있다. Wolfram/xAct 검사는 root의 별도 실제 실행 근거이며, 이 independent Fraction 실행의 검사 개수에 더하지 않았다.

## 채택 범위

현재 source/result/readout bytes에 대해 PHYS19 순수 응답, stage/carry/endpoint certificate, 유한 온도 quotient, 양 축 concavity, indefinite Hessian 및 같은-family interpolation/model error 경계의 채택을 권고한다. Higher source regularity, 새 source/root/history 계산, 임의로 독립 선택된 corner samples, consumer의 실제 materiality 또는 stationary saddle를 추가로 주장하지 않는다. Consumer 적용은 별도의 실제 interval identity와 원 source/COMMON/clock 계약 결박을 따라야 한다.
