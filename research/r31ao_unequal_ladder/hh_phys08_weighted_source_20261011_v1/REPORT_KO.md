# PHYS08 연구 보고 — weighted photo 냉각과 source 경쟁 부호

## 결과

**Full과 first-half 모두에서 실제 photo source P_N, birth 미분 P_M의 온도 방향이 엄밀히 음수다.** 두 source 방향의 HH/photo 경쟁 항도 음수다. 이번 결과는 최신 NCP PHYS07 source export가 주는 전체 X × Theta 포함값을 소비한 fixed-coefficient 실수 source 명제다. 실제 native nonlinear root 또는 유한 mixed response를 계산한 결과는 아니다.

현재 광자장과 새 birth의 효과를 구별해야 한다. P_N은 저장된 33×3 `photo_rates.value`를 합한 전체 광자 source다. P_M은 같은 Jet의 `gradient[5]`를 합한 partial_b F_gamma다. 입력 M=partial_b N은 유한 photon amount이고 M/dt가 source-rate 방향이다. 이 둘을 같은 값이나 단위로 바꾸어 넣지 않았다.

## 이전 막힘과 이번 정리

새 NCP07은 full/first-half의 source producer와 fixed coefficient C², conditional uniform arithmetic을 완료했다. 그런데 기존 directional witness는 nonzero interval support에 속하는 모든 node에 대해 각 heat_j*p<w를 요구했다. Node32는 E=20 eV이고 M은 ±128 minsubnormal의 포함폭을 가진다. 이 node의 heat*p가 w보다 작다는 충분조건은 닫히지 않는다. 그 OPEN과 모든 원본 bytes를 보존했다.

온도는 thermal energy 자체와 같지 않다. 고정 density-ratio fhat 아래

\[
p=1+\widehat f+x+\widehat f(y_1+2y_2),\quad
T=\frac{Cw}{p},\qquad C=\frac{2\epsilon_{\rm eV}}{3k_B}>0.
\]

임의의 signed source vector v에 대해 정확히

\[
B(v)=p v_w-w(v_x+\widehat f v_{y_1}+2\widehat f v_{y_2}),
\qquad DT[v]=\frac{C}{p^2}B(v).
\]

따라서 전체 B의 상계가 0보다 작으면 냉각한다. 각 node의 동일한 thermal 조건을 요구할 필요가 없다. 모든 He signed tail과 원 33개 node를 합했다. 단계별 photo conversion에는 captured fHe를 사용하고, 온도에는 captured nHe/nH의 정확 실수 비를 사용했다. 둘의 아주 작은 rounding 차이도 동일시하지 않았다.

## 실제 포함값

아래 표는 가독성을 위해 **바깥 방향으로 반올림한 요약**이다. 정확 유리수 numerator/denominator와 binary64 outward endpoints는 `results/weighted_corrected/WEIGHTED_RESULTS.json`에 있다.

| Stage | 방향 | B 포함구간 | DT 포함구간 [K/s] |
|---|---|---:|---:|
| Full | P_N | [-9.969964e-13, -6.407154e-13] | [-1.740689e-9, -1.082374e-9] |
| First-half | P_N | [-9.977286e-13, -6.414618e-13] | [-1.741967e-9, -1.083635e-9] |
| Full | P_M | [-1.604455e-16, -1.028246e-16] | [-2.801270e-13, -1.737038e-13] |
| First-half | P_M | [-8.028903e-17, -5.147328e-17] | [-1.401793e-13, -8.695494e-14] |

각 역할의 P_x와 P_w는 양수다. 따라서 photo source는 thermal w를 늘리면서도 T를 낮춘다. Full P_N의 thermal 증가율은 약 [4.002607e-15,5.723177e-15] eV/H/s이고, 온도 방향은 위와 같이 음수다. 생성된 입자 수의 상대 증가가 thermal energy의 상대 증가보다 크기 때문이다.

이 관계를 같은 box에서 비교하면, P_N의 P_w/Dp는 full에서 [0.05573432,0.11394412] eV인 반면 기존 w/p는 [6.07479474,6.65079976] eV다. 이것은 signed enclosure를 사용한 비의 포함값이다. 모든 개별 signed rate를 양의 확률 가중치로 해석하는 주장은 하지 않는다. Node32만의 B 기여 절댓값 상계는 전체 strict margin 대비 full P_N에서 1.29e-309 미만, full P_M에서 2.41e-305 미만이다. 이 작은 항도 계산에서 제외하지 않았다.

First-half는 full과 동일한 COMMON에서 시작하는 첫 반단계다. 두 번째 carried half나 full/two-half defect의 결과가 아니다.

## HH와 광이온화의 경쟁

현재 HH source는 H=q(1,0,0,-CHI_H)이고 q=nH*k(T)*(1-x)^2다. 원 source의 exact captured coefficient로

\[
Dq[P]=q\left[-\frac{2P_x}{1-x}+\frac{\nu}{T}DT[P]\right],
\qquad\nu=\operatorname{exact}(\operatorname{fl}(1.2))+\frac{157800}{T}>0.
\]

P_x>0와 DT[P]<0가 동시에 성립하므로 HgP의 x 성분이 음수다. Photo ionization이 중성 수소를 줄이고, 온도 방향도 HH rate를 낮추는 쪽이다. 반대 순서 PgH도 음수다. HI-only 실수 source에서는

\[
((P_Z)_gH)_x=-q\sum_j\frac{c n_H\sigma_j Z_j}{D_j^2},
\]

이며 Z=N 또는 M이다. M은 signed interval이므로 각 node의 양수를 가정하지 않고 전체 합의 하계를 확인했다. 저장된 rate gas gradients/Hessians로 만든 PgH와, q의 저장 gradient를 쓴 HgP도 독립적으로 축약했다.

| Stage·방향 | (HgP)_x 포함구간 [s^-2] | (PgH)_x 포함구간 [s^-2] |
|---|---:|---:|
| Full P_N | [-4.023741e-31,-1.251637e-31] | [-1.796201e-31,-5.893445e-32] |
| First-half P_N | [-4.026821e-31,-1.253130e-31] | [-1.799039e-31,-5.907374e-32] |
| Full P_M | [-6.489990e-35,-2.017003e-35] | [-2.897352e-35,-9.507985e-36] |
| First-half P_M | [-3.247750e-35,-1.009710e-35] | [-1.451080e-35,-4.765208e-36] |

Closed formula와 saved-Jet 축약의 overlap은 정합성 진단일 뿐 동일성의 증명이 아니다. 동일성은 source graph의 gas-independent incoming, fixed coefficients 및 chain rule에서 유도했다. 두 계산 경로가 각각 주는 포함값은 파일에 나란히 남겼다.

## Energy와 유한 interaction의 경계

\[
\ell=(\chi_H,f\chi_{\rm HeI},f(\chi_{\rm HeI}+\chi_{\rm HeII}),1)
\]

를 쓰면 동일 CHI leaf가 만드는 반응 벡터 cancellation으로 ell*HgP=0이다. 이것은 구간 endpoint를 임의로 상쇄한 수치 결과가 아니다. ell*PgH는 네 경우 모두 엄밀히 음수였다. Rounded heat leaf와 정확 threshold leaf의 차이는 원 source 정의대로 보존했다.

이 사실만으로 유한 gas-energy interaction I_e의 부호를 정하지 않는다. 유한 시간 implicit solution map에는 inverse gas Jacobian, mixed derivatives, parameter integrals 및 domain/regularity의 결박이 더 필요하다. Native root authority와 actual U/V/W/I도 아직 발행하지 않았다. 따라서 finite energy, carried half, paired defect, time/continuum remainder, full49 및 production의 OPEN 상태를 유지한다.

## 검증과 재현성

첫 reference 실행은 Python `157800/T`의 reflected division 연산자 누락으로 0.216 s에 실패했다. 원 command·stdout/stderr·코드 snapshot·입력 hash를 보존했다. 동일 exact interval division으로 연결하는 한 가지 표적 수정과 새 create-only output 경로를 적용한 corrected run은 0.368 s에 PASS였다. 최종 source 및 19개 bound 항목의 전후 hash가 일치한다. 수치 gate와 입력·허용오차는 바꾸지 않았다.

정확 산술은 binary64 endpoint bits를 Fraction으로 읽고 +,-,*,/를 유리수로 수행했다. Decimal 표시를 다시 rounded input으로 사용하는 계산은 없다. 소스 초월함수나 native solver를 재실행하지 않았다. 실제 결과에는 294개 assertion, 2개 stage, 11개 golden fixture가 기록돼 있다. 11개 fixture는 4개 실제 source 역할과 작은/큰 고에너지 꼬리, zero, zero-touching, signed He 부호 변화, 양의 scaling, minsubnormal의 7개 의미 사례로 구성된다.

Rust implementation과 standalone harness는 완성했으나, 현재 host에 rustc/cargo가 없어 빌드·실행하지 않았다. NCP는 이 저장 fixture만 소비해 실제 binary 출력이 exact oracle interval을 포함하는지 검증한다. 비교 기준은 endpoint equality나 overlap이 아닌 containment이며 각 출력의 strict sign도 별도로 검사한다. Underflow로 포함폭이 넓어지는 minsubnormal 사례는 안전한 unresolved를 허용한다. 실제 네 source fixture에서는 strict negative가 필요하다.

독립 비생성자 검토와 최종 scope 판정은 `review/DECISION.json`에 있다. 새 코드·입력·보고·실행 계약·NCP prompt는 core archive에 포함하고, core hash와 양쪽 backup의 실제 upload/metadata identity는 detached delivery receipt에 보존한다.
