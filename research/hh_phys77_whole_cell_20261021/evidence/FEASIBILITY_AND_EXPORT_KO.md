# PHYS77 finite-owner whole-cell 의무: 독립 검토 및 계수 export

## 범위와 실제 산출물

이 작업은 PHYS76의 미완료 노드 `FINITE_OWNER_WHOLE_CELL_SOURCE_OR_RESIDUAL_ENCLOSURE`를 위한 **유한 계수 모델의 입력 고정과 box-extension 설계**다. 기존 1,231개 이력이나 PHYS76 tail을 재적분하지 않았다. 실제 owner의 constructor와 `set_amplitude`로 계수를 만들었고, RHS 호출·ODE solve·benchmark는 모두 0회다.

`source/export_owner.py`는 지정된 PHYS76 loader와 그 loader가 검증하는 원본 owner만 import한다. 고정된 source/index/manifest SHA를 확인한 뒤 한 사례의 저장 receipt에서 matter amplitude를 읽는다. 초기 조건은 원본 raw history의 `x=0` 첫 상태를 정확히 사용한다. 임의의 중간 저장 endpoint를 정확한 IVP 초기 조건으로 바꾸지 않는다.

9개 manufactured exporter contract test가 첫 실행에서 모두 PASS했다. 원본 source의 table 구성 1회와 정확한 JSON readback도 PASS했다. 기록은 `verification/EXPORT_CONTRACT_FIRST_TESTS.json`, `verification/ACTUAL_ONE_CASE_EXPORT_FIRST.json`에 있다.

실제 첫 사례는 `mixed_s+0_m+1`이다. 파일은 `exports/mixed_s0_mplus1_owner.json` 및 `exports/REQUEST_FIRST_CELL.json`이다. 후자는 첫 두 저장 node를 선형 predictor 후보로 제공할 뿐, 이 exporter가 enclosure 성공을 주장하지 않는다.

## 모델, 실제 packet 수와 identity

원본 경로는 `upstream_inputs/rei198_verified/repo_payload/research/rei_bianchi_sigma_pi_pilot_20261021`이다. 핵심 파일은 `pilot.py`, `matter_radiation_20261021/component_pilot.py`, `vendor/canonical_fv.py`, `vendor/lrs_boltzmann.py`다. 개별 SHA는 실제 export의 `provenance.owner_files`에 모두 보존했다.

- PHYS76 loader SHA: `959952f9d347bcc515410ef90b3b8dc4b36388ad4bfd2acc2bac356fafd6d97b`
- PHYS75 OWNER_LOCK SHA: `85991ae90de5041bb1ff967b3abaf426a4787874ba71a3b1290a111317acdd1c`
- 원본 REI198 archive SHA: `2c1433a92ae68c328436852b2842c9b7c51d30b9ff84a22fe2dffbd04ee4246d`
- terminal index SHA: `62f5d96fd323b1ed60c61f4b51e35ab80eb3498d2800c6c04addc1e5e2483115`

`kinetic24x12`는 radial/angular cell 수다. 각 축의 Gauss order 3 때문에 실제 표는 radial 72개, angular 36개, 총 **2,592 packet**이다. 표는 `q[72]`, `mu2[36]`, `numbers[72][36]`, `M[5][5]`를 담는다. `q`는 radial canonical momentum이며 state의 shear 변수 `q=s/h_ref`와 다르다. 원본 q를 보존하고 float로 q²를 먼저 만들지 않는다.

각 수치는 `str(Decimal.from_float(original_binary64))`로 정확히 직렬화한다. array마다 shape, canonical Decimal JSON SHA, 원래 little-endian binary64 byte SHA를 남긴다. 최상위 `table_sha256`은 그 필드 자체를 제외한 canonical compact sorted JSON의 SHA다.

이것은 **현재 기록된 runtime에서 고정 source constructor가 만든 binary64 계수의 exact-real 모델**이다. 표를 저장하지 않았던 과거 runtime과의 bit identity나 원래 NumPy reduction의 각 반올림을 포함한다는 주장이 아니다. 실제 export runtime은 Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0이다.

## Whole-cell box extension을 구성할 실제 식

상태를 \(y=(\tau,b,q,E_0,E_2,E_4,E_6,E_8)\), \(s=h_{ref}q\), \(a=a_{ref}e^x\), \(r=\Omega_r/a^4\), \(D=(1-f_m)\Omega_m/a^3\)라 놓는다. 상수와 M은 모두 frozen table의 값이다.

packet마다

\[
p_\perp^2=e^{-2x}q_i^2e^{2b}(1-\mu_j^2),\qquad
p_\parallel^2=e^{-2x}q_i^2e^{-4b}\mu_j^2,
\]

\[
\epsilon_{ij}=\sqrt{m^2+p_\perp^2+p_\parallel^2},\quad
w_{ij}=e^{-3x}N_{ij}/N_{ref}.
\]

\[
\rho=\sum w\epsilon,\quad
p_\perp=\sum w\frac{p_\perp^2}{2\epsilon},\quad
p_\parallel=\sum w\frac{p_\parallel^2}{\epsilon},\quad
\bar p=\frac{2p_\perp+p_\parallel}{3},\quad
\pi_s=\frac{p_\parallel-p_\perp}{3}.
\]

모든 packet population은 음수가 아니고, mass와 normalization은 양수다. interval 연산으로 `exp`, `sqrt`, division과 위 유한합을 outward rounding하면 직접 box extension을 얻는다.

\[
F=H^2=h_0^2(D+m_{pref}\rho+rE_0+\Omega_\Lambda)+s^2,
\qquad v=s/H.
\]

\[
\tau'=h_{ref}/H,\quad b'=v,\quad
q'=-3q+\frac{3h_0^2}{h_{ref}H}
  (m_{pref}\pi_s+rE_2/3),\quad E'=vME.
\]

물리/수치 domain은 forward \(x\ge0\), \(|b|\le1\), \(E_0>0\), \(H>0\)이다. 고정 mass, normalization과 source amplitude의 positivity도 전제다. 이 domain에서 RHS는 smooth하므로 국소 uniqueness가 있다. \(E_0>0\)만으로 모든 방향의 truncated radiation brightness가 양수라는 결론은 내리지 않는다.

동일 normal frame의 signed half-contraction source는

\[
P_m=\frac{3\sqrt3 h_0^2m_{pref}\pi_s}{F},\qquad
P_r=\frac{\sqrt3 h_0^2rE_2}{F}.
\]

각 sector를 signed 상태로 보존하고 합산한 뒤 Frobenius norm을 취한다. LRS에서는 full-Frobenius norm이 half-contraction norm의 \(\sqrt2\)배다. 같은 trajectory의 attribution이며 species-off 인과 실험이 아니다.

## Alpha의 full matrix-row 보정은 필수

원본 `legendre_matrix`는 monopole row를 `[0,-2,0,0,0]`에 가깝다고 검사하지만 정확히 그 값으로 대입하지 않는다. 실제 현재 frozen M의 첫 row는 다음과 같다.

```
[ 1.111610803405938e-14,
 -1.9999999999999525,
  7.599476603559197e-14,
  6.383782391594650e-14,
  2.758904216193514e-14 ]
```

따라서 exact continuum identity \(E_0'=-2vE_2\)를 직접 넣으면 고정 계수 모델을 바꾸게 된다. 유한 packet 항등식

\[
\rho'=-3(\rho+\bar p)-6v\pi_s
\]

과 원본 full row \(E_0'=v(ME)_0\)를 사용하면 matter work가 정확히 소거되어

\[
F'=h_0^2[-3D-3m_{pref}(\rho+\bar p)-4rE_0
  +rv((ME)_0+2E_2)]-6s^2,
\qquad \alpha=3+\frac{F'}{2F}.
\]

즉 `((M @ E)[0] + 2*E2)`를 작은 값이라는 이유로 버리지 않는다. 이 식을 full-state box에 직접 적용하면 \(\alpha\) enclosure를 얻을 수 있다.

## Direct-defect first-exit 방식의 가능한 증명 범위

한 cell \([x_0,x_0+h]\)에서 predictor \(p\)와 error box \(R\)를 정한다. 실제 초기 오차 enclosure를 \(e_0\)라 하고

\[
\mathcal D\supseteq F([x_0,x_0+h],p([x_0,x_0+h])+R)-p'([x_0,x_0+h])
\]

를 계산한다. whole-cell domain 검사를 통과하고

\[
e_0+[0,h]\,\mathcal D\subset\operatorname{int}R
\]

이면 첫 이탈 시각에서의 적분식과 모순되므로 오차가 전체 cell에서 R 안에 남는다. 끝점은 \(e_0+h\mathcal D\)로 둘 수 있다. 다음 cell에 이 endpoint enclosure를 정확히 전달해야 한다. 원래 저장 endpoint를 오차 0으로 리셋하면 증명이 끊긴다.

이 접근은 Jacobian 없이 가능하지만 wrapping 때문에 긴 cell에서는 실패할 수 있다. 실패는 `NOT_ENCLOSED`이지 실제 궤적의 비존재나 발산 증명이 아니다. 기존 sampled node 잔차는 predictor 선택에만 쓴다. whole-cell enclosure 성공 여부는 위 outward-rounded 포함 검사가 별도로 결정한다.

## 안전한 경량화 및 재사용

로컬 파일명 조사에서 재사용 가능한 interval Python 코드는 PHYS76 `source/interval_transport.py`가 확인되었다. 다른 branch의 독립 구현까지 전수 검증했다는 주장은 하지 않는다. 그 코드는 Decimal의 directed arithmetic, exp를 nearest result의 양쪽 neighbor로 감싼 구간, fail-closed exponent/subnormal 처리를 이미 갖고 있다. PHYS77에 필요한 sqrt에도 해당 계약을 명시해야 한다.

가장 안전한 최적화는 coefficient 검증을 model 생성 시 한 번 하고, 고정 precision에 대해 q², 1−mu², packet coefficient, M을 cache하는 것이다. 이때 q²와 곱은 원래 q를 읽은 뒤 directed interval 연산으로 만든다. `table_sha256 + precision`을 cache key로 사용하면 다른 matter amplitude의 numbers/norm 혼입을 막을 수 있다. 음수 또는 작은 M 성분을 제거하는 sparse cutoff는 허용되지 않는다.

각 case는 독립적이므로 자원이 허용하는 범위에서 case 단위 병렬화가 자연스럽다. 이 exporter는 single-thread constructor와 작은 표 준비만 수행했다. 처리 속도나 HPC scaling의 benchmark 주장은 하지 않는다.

## 후속 독립 검토 대상

root가 작성하는 interval owner core 및 cell certifier에서 확인할 것은: full-row alpha, 정확한 predictor slope enclosure, `[0,h]`와 endpoint h의 구분, strict interior 검사, 실제 initial-state binding, 다음 cell error carry, domain 실패 처리, 연산 overflow/subnormal의 fail-closed 처리다. 현재 export와 request는 그 검토에 필요한 입력을 제공한다.

`HH_R10=OFF`, production admission은 발급하지 않는다.
