# PHYS11 — 실제 소스에서 joint carry로 가는 대응

작성 범위: creator-side 읽기 조사와 유도 제안. 후보 과학 프로그램·Rust·기존 gate·source callback을 실행하지 않았다. 이 문서는 최종 독립 판정이 아니다.

## 결론

현재 보존된 실제 자료로 33개 photon group의 값과 \(U,V,W\), 흡수 광자 수, 팽창 thermal work, 미래 source number/energy, HH event/heat의 첫 단계 carry를 계산할 수 있다. 입력은 같은 COMMON에서 시작하는 Full과 first_half 각각의 완전한 incoming group Jet, 99개 흡수율 Jet, \(q\) Jet, PHYS09의 기체 응답이다. 새로운 native root나 source 호출은 필요하지 않다.

다음 시간 단계에 실제로 들어가는 4,224개 ray·node 광자 상태와 128개 guard 상태의 출력 배열은 현재 JSON에 없다. 기존 원 반환은 그 배열을 `prebe_words.bin`에 저장했고 해당 크기·SHA256은 원 MANIFEST에 있지만, 현재 workspace에는 그 바이너리가 materialize되어 있지 않다. Group carry와 ray scalar lift 정리는 이 결손을 분명히 표시해야 한다. 이는 계산량 때문에 NCP에 보낼 의무가 아니다.

원 source-family에서 가능한 유도와 실제 native 반환 권한을 분리한다. `phys04_native_dispatch_requested()`는 지금도 `PHYS04_AUTHORIZATION_NULL_BUDGET_ZERO`를 반환한다. 이 조사는 해당 코드나 권한을 바꾸지 않았다.

## 1. 실제 상태와 정규화

`candidate/src/paired_runtime.rs::PairedState`의 구성은 다음과 같다.

| 상태 | 실제 필드 | 의미와 carry 의무 |
|---|---|---|
| 시간 | `time_s` | 실제 입력 시간을 이어받아야 한다. |
| 기체 | `gas: PrimaryState`, `gas_box:[Interval;4]` | HII, HeII, HeIII 분율과 thermal \(w\), escape scalar, node packets를 포함한다. |
| ray·node 광자 | `photons`, `photon_boxes` | 128 rays × 33 energy nodes = 4,224개. 단위 photons/H. |
| 하단 guard | `lower_guard_n/u`, 각 `*_box` | ray별 128개 number/H와 eV/H. 원 spectral support 아래로 이동한 광자를 저장한다. |
| redshift work | `redshift_work_ev_per_h` | transport 전후 photon+guard energy 차이의 누적값. |
| thermal work | `thermal_work_ev_per_h` | 각 단계 \(2 H_{\rm mean}d\,w^+\)의 누적값. |
| source ledger | `source_photons_per_h`, `source_energy_ev_per_h` | 미래 birth 누적 number/H와 eV/H. |
| absorption ledger | `absorbed_photons_per_h` | 각 단계 \(d\sum_{j,a} R_{ja}\). |
| 보상합 | `ledger_comp:[f64;5]`, `energy_comp:f64` | 실제 유한정밀도 누적·thermal 업데이트의 correction 상태. |

`PrimaryState`는 `candidate/src/coupled_primary.rs`에서 정의된다. 원 `paired_runtime.rs` 첫 문장은 모든 population이 fixed physical-energy nodes와 fixed q rays의 counts per hydrogen nucleus임을 명시한다. 따라서 \(e_\gamma=\sum_j E_jN_j\)는 그대로 eV/H이며 추가 \(n_H\) 나눗셈을 하지 않는다.

`src/family.rs::CommonFamily`는 위 primal 상태를 통째로 보존하고 별도 `gas`, `photons`, `guard_n`, `guard_u` Jet와 `ledger_derivatives:[Jet;5]`, `energy_comp_derivative`, `hh_derivatives:[Jet;2]`를 둔다. 초기화는 과거 HH ON 이력과 primal correction을 보존하면서 미래 \((\lambda,b)\) derivative ledger만 0으로 시작한다. 이 타입에 실제 joint advance 메서드는 없다.

과거 HH 데이터는 두 단계가 동일하다.

| 항목 | 저장값 |
|---|---:|
| historical HH events/H | 3.0081635116590555e-08 |
| historical HH heat eV/H | -4.0906314778505567e-07 |
| HH compensation event | 3.0243791146470074e-24 |
| HH compensation heat | -2.0265925007549178e-23 |
| primal energy compensation | -8.70804079886045e-16 |

`ledger_comp`는 `[0.0, -2.710505431213761e-19, 0.0, 0.0, -4.54009659728305e-19]`이다. 이것을 새 실수-family derivative로 해석하거나 0으로 덮어쓰면 안 된다.

## 2. 시간과 source call

`src/sourcebox.rs::source_stage`는 \(h=[10^{-14},10^{-14},10^{-14}]\,s^{-1}\), \(t_0=1.6\times10^{11}\,s\), 같은 저장 COMMON을 선택한다. `run_cli`의 두 이름은 다음과 같다.

| 이름 | \(d\), s | 종료 시각, s | 입력 |
|---|---:|---:|---|
| `phys07_sourcebox_full_first` | 1.25e9 | 1.6125e11 | 원 COMMON |
| `phys07_sourcebox_first_half_first` | 6.25e8 | 1.60625e11 | 같은 원 COMMON |

따라서 first_half가 두 half 연속 진화의 두 번째 입력을 뜻하지 않는다. 이 자료는 일반 비등방 배경의 실제 실행 결과도 아니다. 선택된 Hubble triplet은 등방이다.

`candidate/src/phys04_transport.rs::phys04_prepare_family`의 순서는 기존 ray·node stock의 redshift 및 hat remap → guard 이동 → 종료 시각의 angular birth weights → node 24에 birth → ray 합으로 33 group 구성이다. `stage.n_h_cm3 = 1e-4*exp(-sum(h)*(time+dt))`, `stage.f_he=0.083`, `stage.h_mean_per_s=sum(h)/3`이다. Full과 half의 실제 \(n_H\)는 각각 `9.951741818585369e-05`, `9.951928415493808e-05` cm^-3이다.

geometry·clock·node energies는 \((\lambda,b)\)에 대해 고정된다. 동일한 coefficient vector를 rectangle 전체에서 고정한다는 inherited source-family 조건을 유지한다. guard/hat branch crossing은 `phys04_prepare_family`가 반환 전에 명시적으로 거절한다. 실제 native floating-point 프로그램과 cone clipping 전체를 \(C^2\)라고 부르지 않는다.

## 3. 현재 자료의 derivative coverage

모든 Jet는 `value`, `gradient[7]`, `signed_hessian[7][7]`이다. gas slots는 0–3, \(\lambda\)는 4, \(b\)는 5이며 slot 6은 이 연구의 입력 forcing으로 쓰지 않는다.

| 저장 항목 | 가용량 | 사용할 수 있는 정보 |
|---|---:|---|
| `PREBE.json::groups` | 33 full Jets | 들어오는 group의 값과 모든 partials. |
| `PREBE.json::source_n/source_u` | 2 full Jets | \(b\,\operatorname{fl}(dS)\), 그 에너지 ledger. |
| `PREBE.json::source_weights` | 128 intervals | ray별 birth 계수의 포함. |
| `SOURCE_BOX_COMPONENTS.json::photo_rates` | 33 × 3 full Jets | 잔존 광자 및 absorption carry의 모든 항. |
| `SOURCE_BOX_COMPONENTS.json::nonphoto` | 4 full Jets | 기체 NP projection 및 source-derived radiative bookkeeping 유도. |
| `SOURCE_BOX.json::q` | 1 full Jet | HH event/heat의 source-family derivatives. |
| `SOURCE_BOX.json::photons` | 33 value intervals | full photon Jet라고 읽으면 안 된다. |
| `SOURCE_BOX.json::D` | 33 value intervals | positive denominator 포함. |

`PREBE.json::groups[j].gradient[5]`가 실제 저장 incoming birth slope이다. Full node 24의 저장 포함은 `[6.249999999998571e-06, 6.2500000000014445e-06]`, half는 `[3.124999999999286e-06, 3.125000000000717e-06]`이다. 다른 node와 다른 partials에는 signed subnormal tail이 있으므로 원 derivative 배열을 그대로 처리할 경우 보존해야 한다.

소스의 구조로 유도하는 정확한 실수-family birth slope는 ray \(r\), node \(j\)에 대해

\[
\partial_b N^-_{rj}=\widehat{dS}\,w_r\,\delta_{j,24},\qquad
\partial_\lambda N^-_{rj}=\partial_{\lambda b}N^-_{rj}=0.
\]

여기서 \(\widehat{dS}\)는 `fl_dt_SOURCE_bits`로 저장된 leaf이며, 단순히 새로 계산한 Python float `d*5e-15`의 bits로 대체할 필요가 없다. source weights에 대해 JSON 끝점의 독립 합을 곧바로 정확히 1이라 두지 않는다. 각 native 또는 실제 geometry coefficient vector의 정규화 관계를 주장하려면 그 관계의 source premise를 명시해야 한다.

## 4. 새 경량 계산의 정확한 형태

\(g^+(\lambda,b)\)의 inherited responses를 \(U=\partial_\lambda g^+\), \(V=\partial_b g^+\), \(W=\partial_{\lambda b}g^+\)라 하자. saved source Jet \(J(g,\lambda,b)\)에 대해

\[
D_\lambda J=J_gU+J_\lambda,\qquad
D_bJ=J_gV+J_b,
\]

\[
\mathscr L[J]=J_gW+J_{gg}[U,V]+J_{g\lambda}V+J_{gb}U+J_{\lambda b}.
\]

\(A_j=\sum_aR_{ja}\)를 같은 full Jet로 먼저 구성하면,

\[
N_j^+=N_j^- -dA_j,
\quad U_{N_j}=D_\lambda N_j^- -dD_\lambda A_j,
\quad V_{N_j}=D_bN_j^- -dD_bA_j,
\quad W_{N_j}=\mathscr L[N_j^-]-d\mathscr L[A_j].
\]

첫 단계 incoming이 affine source임을 식에서 먼저 이용하는 선택도 가능하다. 그 경우 정확히 0인 구조와 signed outward export tail을 구분해 기록해야 한다. `groups`의 raw Jet contraction을 그대로 쓰면 tail을 자동 보존한다.

\(N^+=N^- -dA\)의 단순 interval 값이 0 아래로 넓어지는 것과 실제 광자 수 음수는 다르다. 원 quotient의 `SOURCE_BOX.json::photons`를 같이 사용하는 교집합은 동일 family 포함이라는 전제 아래 값 구간을 좁힐 수 있다. Derivative interval에 physical nonnegative clipping을 적용해서는 안 된다.

흡수 누적량의 새 증분은 \(d\sum_j A_j\)이며 위와 같은 일차·혼합 contraction을 적용한다. Thermal work 증분은 \(2H_{\rm mean}d\,w^+\)이다. Source N/U는 `source_n/source_u` full Jets를 읽는다. HH event는 \(d\lambda q\), HH heat는 \(-\chi_H\)배이다. `SOURCE_BOX.json::q`가 있으므로 이 역시 새 source 평가 없이 가능하다.

Guard와 redshift work는 첫 단계에서는 birth가 transport 뒤에 들어오고 기존 COMMON이 \((\lambda,b)\)에 독립이므로 실수-family의 새 derivatives가 0이다. 그러나 guard primal 값을 담은 배열이 현재 JSON에 없으므로 complete native carried state를 만들었다고 주장할 수 없다.

### Escape coverage

실제 endpoint는 `raw(m,s).escaped_energy_rate/(nH*ev)`로 escape scalar를 업데이트한다. 저장된 `ft03_interval_rhs`는 gas4와 photon3만 반환하며 escape 채널의 Jet가 없다. 따라서 native escape derivatives를 새로 확보했다고 할 수 없다.

동시에, 이론 owner가 \(\widehat f=n_{He}^{stored}/n_H\)와 FT03 reaction decomposition으로 증명하는 source-derived \(\Gamma_*=-\ell_{\widehat f}F^{np}\)는 별도 observable로 계산 가능하다. 이것은 실제 native `raw.escaped_energy_rate` Jet와의 identity를 자동으로 증명하지 않는다. 실제 escape 값과 compensation 상태를 덮어쓰지 않아야 한다.

## 5. Ray lift가 보장하는 것과 보장하지 않는 것

고정 node의 residual-aligned denominator는

\[
D_j=1+d\sum_a c\,n_H\,\sigma_{ja}\,l_a(g),
\quad l=(1-x_{HII},f_{He}(1-y_{HeII}-y_{HeIII}),f_{He}y_{HeII}).
\]

이 식은 ray index에 독립이다. 따라서 같은 denominator family를 선택한 경우

\[
N_{rj}^+=\frac{N_{rj}^-}{D_j},\qquad
\sum_r N_{rj}^+=\frac{\sum_rN_{rj}^-}{D_j}=N_j^+.
\]

\(N_j^->0\)이면 node 내부의 angular fraction \(N_{rj}/N_j\)가 absorption 단계에서 보존된다. \(N_j^-=0\)에서는 비율을 정의하지 않고 각 ray의 quotient를 그대로 쓴다. Signed forcing이 남을 수 있으므로 0 값 node를 제거하지 않는다. \(C^2\) 조건에서 일차·혼합 derivative에 대해서도 유한합과 미분이 교환된다.

이 정리는 group compression이 absorption만 통과할 때 충분하다는 뜻이다. 다음 anisotropic transport는 ray별 geometry ratio를 쓰므로 33 group 값으로 4,224개 ray 분포를 복원할 수 없다. 동일 group이면서 다른 angular pattern인 상태는 다음 transport에서 다른 결과를 낼 수 있다. 따라서 group carry를 complete ray carry로 승격하지 않는다.

### Existing distribution helper의 coefficient ordering

`phys04_reduced_residual`은 `ic(c)`, `ic(nH)`, `lower`, `ic(sigma)`를 Jet 곱으로 취한다. 따라서 여기서 고정한 실수 source의 opacity coefficient는 exact captured leaf 곱 \(a=c\,n_H\,\sigma\)다.

`phys04_distribute_after_be`는 `sigma[a]*29979245800.0*pre.stage.n_h_cm3`를 scalar f64로 먼저 계산하고 이를 하나의 Jet constant로 넣는다. 그 coefficient는 \(a'=\mathrm{fl}(\mathrm{fl}(\sigma c)n_H)\)다. 현재 captured `c_bits`는 해당 c literal과 같고 `fHe_bits`는 `FHE=0.083`과 같다. 하지만 \(a'\) 자체의 실행 bits는 현재 export에 없으며, 두 product graph의 byte·semantic identity를 선언할 수 없다.

조건부 값 포함은 유도할 수 있다. IEEE round-to-nearest binary64의 유한 정상수 곱이고 contraction이나 reassociation이 없다고 하자. \(u=2^{-53}\), \(\gamma_2=2u/(1-2u)\)이면

\[
|a'-a|\le\gamma_2a.
\]

실제 positive sigma 범위는 약 \(2.2111\times10^{-18}\)–\(6.3463\times10^{-18}\) cm²이고 \(c\), \(n_H\)와의 두 곱은 overflow/underflow 영역에서 멀다. 0인 sigma는 정확히 0인 scalar 곱을 유지한다. 물리 영역에서 \(l_a\ge0\), \(\tau_j=d\sum_a l_a a_{ja}\ge0\)이므로

\[
|D'_j-D_j|\le\gamma_2\tau_j,
\quad
\left|\frac{D'_j}{D_j}-1\right|\le\frac{\gamma_2\tau_j}{1+\tau_j},
\]

\[
\left|\frac{N'_{rj}}{N_{rj}}-1\right|
\le\frac{\gamma_2\tau_j}{1+(1-\gamma_2)\tau_j},
\]

마지막 식은 \(N_{rj}>0\)일 때이며 0 입력은 양쪽 출력이 0이다. 이는 coefficient 변경으로 인한 값 차이의 조건부 상계다. Gas root의 변경, native nonlinear solve, compensation, derivative 부호 또는 native-authority 등가성을 보장하지 않는다.

또한 `paired_runtime.rs::endpoint`는 분배 factor 안에 `p(dt*29979245800.0*stage.n_h_cm3)`를 넣는 별도의 scalar capture order를 갖는다. 이를 `phys04_distribute_after_be`와도 같은 graph라고 간주하지 않는다.

## 6. 독립 analytic 검사 제안

각 사례는 실제 자료를 대체하지 않는 의미 검증이다. 수를 늘리기 위한 반복 suite는 필요 없다.

1. **두 단계 carry 교차항:** 첫 map이 \(x_1=\lambda\), \(P_1=1+b\), 둘째 map이 \(N_2=P_1/(2-x_1)\)인 닫힌 유리함수를 사용한다. 첫 map의 두 mixed responses는 모두 0인데 둘째 mixed response는 \((2-\lambda)^{-2}\)이다. \((\lambda,b)=(1/3,2/5)\)에서 \((U,V,W)=(63/125,3/5,9/25)\), 단위 rectangle finite interaction은 \(1/2\)이다. 기체 carry나 photon birth carry를 지우면 mixed effect가 사라져, joint carry 필요성을 직접 검출한다.
2. **Ray sum과 denominator의 교환:** 서로 다른 affine incoming ray 두 개와 같은 양의 denominator를 exact rational로 선택하고 ray quotient의 합·group quotient·각 mixed derivative의 일치를 확인한다. 다른 ray denominator를 넣으면 교환이 깨지는 반례를 함께 둔다.
3. **Subthreshold node와 zero-stock forcing:** sigma=0인 node는 residual-aligned exact denominator가 1이므로 모든 derivative가 incoming과 같아야 한다. 입력 값이 0인 corner에서도 \(b\) forcing은 남아야 한다.
4. **Group만으로 다음 transport를 정할 수 없는 반례:** 두 ray 총량은 같고 분포만 뒤집은 두 상태에 서로 다른 redshift ratio를 적용하면 energy나 remapped group이 다르다. 이는 group compression을 full carry로 잘못 승격하는 것을 방지한다.

## 7. 실제 identity 및 가용성

`SOURCE_MAP_EVIDENCE.json`에 읽은 파일 22개의 bytes/SHA256와 기존 NCP07 MANIFEST 대조를 저장했다. 22개 모두 기존 MANIFEST와 일치했다. 이 검사는 byte identity이며 과학 정리의 증명을 대신하지 않는다.

| 핵심 소스 | SHA256 |
|---|---|
| `candidate/src/phys04_mixed.rs` | `0fa10fdea11cb24aa1a191a2ea81cf4c8442299fde7278a191553b42a26585d3` |
| `candidate/src/phys04_transport.rs` | `aa7b7ebc83ce1c191fdfbf7039f2a1810caff22ec0744d9802f53832770f6b97` |
| `candidate/src/paired_runtime.rs` | `ffd0cd31bd8b350ecd68f6debf08cd21eaea65c93b0ce94959f62cdf617db11b` |
| `src/family.rs` | `52fc20bb0fb51d93d6c3d72860f8356f978ecea49708f1e7af58a32b08887cd9` |
| `src/sourcebox.rs` | `d771968e9c12c0cce5a9e3ec5fa7311d0040ac63d1f4f4a6f54f048972f674ae` |
| Full `PREBE.json` | `966fe63bbb1e886f3a85ec38bf69ed05920623407b847df19be30b1c21b9c7aa` |
| half `PREBE.json` | `bb293bb9b915f1093bacf5a9878583993f96897ee277e73a445350ea5c3eb3f7` |
| Full components | `29e73ac3518cd4cb5f11ee24c7237a43442d6615a1dba1e710d0206f319ad610` |
| half components | `4272aa6aa49e836eacfdcccddf30e7b5c77fd2e5d8e1846beb0f16af741cf63c` |

다음은 원 MANIFEST에 기록됐으나 현재 materialize되지 않은 실제 출력이다. 새 다운로드도 하지 않았다.

| 파일 | bytes | 원 SHA256 |
|---|---:|---|
| Full `prebe_words.bin` | 4,123,688 | `44519317341ef588d009feaec89ddf7278d3163d1519bb6c1683d376fdb82f78` |
| half `prebe_words.bin` | 4,123,688 | `10f97267c6348c3735102c9c76a8c43e342fdeef7bcffc63ff818764a6bad1cc` |
| Full `prebe_input_words.bin` | 4,090,360 | `cd54a183bba2e7c2a15f7fa83f5734f6818232d20b76e395824a3fdb97c4a71c` |
| half `prebe_input_words.bin` | 4,090,360 | `c9be883901fb0f21247146d65adf83562cf643b63c5883f9051946e0e1b5e78b` |

`prebe_words.bin` layout은 u64 little-endian이며 header 6 words, gas4, photons4224, guardN128, guardU128, groups33, sourceN/U2의 4,519 Jets ×114 words, energy33 words, sourceweights128×2 words이다. 합계 515,461 words =4,123,688 bytes다. 필요하면 이후 새 실제 자료 intake에서 이 binary를 읽을 수 있다. 해당 수량은 높은 계산량이 아니므로 availability를 NCP heavy job으로 분류할 이유가 없다.

본 조사: scientific runtime 호출 0, 원 과학 실행 replay 0, remote fetch 0, remote mutation 0. 최종 후보와 판정은 root owner 및 별도 비창작 reviewer가 결정한다.
