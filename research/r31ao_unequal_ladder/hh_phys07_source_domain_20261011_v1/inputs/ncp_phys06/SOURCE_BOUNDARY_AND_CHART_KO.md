# PHYS07 source map: C² chart와 whole-domain 산술의 실제 경계

이 문서는 2026-10-11 UTC에 고정 Git source를 읽어 얻은 source-localization 결과다. 수치 source callback, endpoint, point solver, root, IVP, 과거 science suite를 실행하지 않았다. 실제 chart 판정과 영역 전체의 수치 포함값은 PHYS07 연구 산출물이 별도로 제시해야 한다.

## 1. 고정된 구현과 바뀐 부분

Repository는 `cosmosapjw-quantum/WU088_HH`다. 새 NCP branch `codex/hh-phys06-ncp-20261011`의 관측 head는 `65a36e255aa6d9911e23a9b5ced18d8a9f507606`, tree는 `f823df8c95defcaba737139859cd9eeeda4ef133`이다. 구현 core `927019cff541e8a4a1f0d2c8846f1466d6b70533`의 tree는 `f156e72d5e58d4c6efa840606af28e43aa014e6f`, parent는 기존 NCP v2 head `4b9231a0eff113701e7178ad98624233f387dd15`다. 현재 연구 PHYS06 branch head `baf23360627bc1c6d10aac5317052f23edafd1b1`은 그대로다.

새 구현 prefix는 `research/r31ao_unequal_ladder/ncp_phys06_local_20261011_v1/`다. `CANDIDATE_V2_PARITY.json`은 현재 head의 v2/v6 경로를 같은 Git tree에서 비교한다. FT03 interval, HH rate Jet, remap/birth, paired runtime, primary source, AtomicProvider, interval AD/math와 FT03 coefficients는 v2와 Git blob가 같다. `candidate/src/phys04_mixed.rs`만 기존 계산에 `nonphoto`, `photo_rates`, stage, energies, stored nHe, dt의 metadata 수집을 추가했다. `evidence/CANDIDATE_DELTA.patch`에 정확한 차이가 있다. 새로운 PHYS06 모듈은 `src/energy.rs`, `src/uniform.rs`, `src/adapter.rs` 등이며 물리 source kernel의 규격을 바꾸지 않는다.

현재 main/root 문서의 frozen107 heavy pair·full49 이력은 별도 과학 lane이다. 이 intake에 필요한 보존 규칙을 읽었지만 그 오래된 root 문서를 PHYS06의 최신 physical result로 해석하지 않는다.

## 2. source-wide exporter의 진입점

`candidate/src/phys04_mixed.rs::phys04_reduced_residual(stage, old, gas, incoming, energies, lambda, dt)`는 public source arithmetic이다. gas는 4개의 7-slot Jet, old와 incoming도 전체 Jet이므로 이전 gas/photon의 U/V/W가 전달될 수 있다. 함수는 nonphoto FT03 Jet, HH Jet, eliminated photo quotient와 source-leaf residual을 평가한다. 반환 residual Jet에서 G, G_y, G_lambda, G_b, G_lambdab, G_ylambda, G_yb, G_yy를 추출할 수 있다. 함수 자체는 endpoint/BE point/root solver를 부르지 않으며 private permit도 요구하지 않는다. 호출할 때마다 별도 source arithmetic counters가 증가한다. 이것은 native operation counters와 다른 계수다.

반면 `phys04_mixed_at_box`는 위 callback을 여러 번 부르고 `inverse4`와 조건부 tangent 포함 계산까지 수행한다. whole-domain source data를 먼저 확보하려면 direct residual callback이 더 좁은 진입점이다. Gc는 gas 값을 고정한 center box와 전체 parameter rectangle에서, A/mixed partials는 전체 X×Theta에서 각각 얻어야 한다. 한 점에서 얻은 Gc/A를 같은 field에 넣어 whole-domain으로 표시할 수 없다.

`src/certificate.rs::export_derivatives`는 실제 family와 PreBE를 연결해 `phys04_mixed_at_box`를 부르는 기존 경로다. `src/adapter.rs::bind`는 이 연결의 exact words/clock/density/source ABI를 검사하되, 항상 `WholeSourceEnclosure::Unresolved`를 반환한다. 현재 source-wide Gc/A/mixed data 및 실제 C² domain의 증거가 없다는 의미다. 이 typed unresolved를 source-derived result로 채우는 작업은 새 generic validator를 다시 만드는 일과 다르다.

`src/uniform.rs`의 Domain/Regularity/Coverage 및 supplied partials는 현재 조건부 전제다. private RootBounds/LinearBounds/MixedBounds는 이미 판정된 payload의 교체를 막지만, 문자열·hash·flag를 actual source의 진실성 증거로 바꾸지는 않는다.

## 3. 열역학 좌표, 고정 leaf, source chart

가스 좌표는 `(x_HII, y_HeII, y_HeIII, w_eV_per_H)`다. `coupled_primary.rs::model`은 `nHe = fl(nH*fHe)`를 저장한다. FT03와 HH의 온도는 정확한 실수로 들어 올린 source graph에서

\[
\hat f=\operatorname{exact}(n_{He})/\operatorname{exact}(n_H),\quad
p=1+\hat f+x+\hat f(y_1+2y_2),\quad
T=\frac{2\,\mathrm{ev}_{erg}\,w}{3 k_{B,erg/K}p}
\]

다. `hhe_events.rs::controlled_fixture`의 leaf는 `c=29979245800.0 cm/s`, `kB=1.380649e-16 erg/K`, `ev=1.602176634e-12 erg/eV`, CHI `[13.598434599702,24.587389011,54.41776] eV`다. NCP `src/energy.rs::transform`는 exact-real sums/products를 outward interval로 감싼 S와 Q를 만들고 두 gas derivative indices를 `diag(Q,I3)`로 pull back한다. 좌표의 물리 box는 기존 gas chart에 남는다. transformed energy e의 box를 기존 w-domain에 그대로 넘길 수 없다.

`ft03_interval.rs::ft03_interval_rhs`의 입력 gas chart는 모든 scalar interval의 lower>0, x.hi<1, y1.hi+y2.hi<1이며, 온도 enclosure가 `[30000,110000] K` 안에 있어야 한다. reduced source가 dummy photon slots=1과 zero sigma로 FT03 nonphoto를 호출하므로 이 함수의 엄격한 photon positivity는 실제 incoming N=0을 배제하는 근거가 아니다.

`hh_primary_extension.rs::hh_rate_jet`은 nonnegative simplex와 w>0에서 정의되며 온도 enclosure `[35000,60000] K`를 요구한다. source algebra는

\[
q=n_H(1-x)^2\,(1.2\times10^{-17})T^{1.2}\exp(-157800/T)
\]

형태다. 실제 결합 callback의 허용 온도 구간은 더 좁은 HH 구간이다. 원래 coefficients의 단위와 fit 지원 범위를 바꾸지 않는다. T>0 및 p>0에서 이 식과 FT03의 exp/power/rational 식은 매끄럽다. 코드의 admissibility guard와 수식의 열린 정의역은 구분해야 한다. 소스가 허용하는 열린 이웃 안의 C² proof를 만들려면 compact X의 physical/temperature margins를 명시하는 경로가 충분하다.

`paired_runtime.rs::temp_box`는 단순히 fHe를 상수로 넣는 것이 아니다. `f ∈ [FHE*(1−8*EPSILON), FHE*(1+8*EPSILON)]`을 만들어 저장 nHe/nH의 곱셈·나눗셈 rounding을 감싸고 모든 thermal constant product를 interval 처리한다. paired guard도 35000–60000 K를 요구한다. 새 chart의 수치 검사는 FT03/HH의 실제 fhat formula와 paired guard의 넓어진 f interval을 모두 포함해야 한다.

고정 leaf corrections는 그대로 유지한다. `Jnorm=(f−fhat)*(chiI F^0_y1+(chiI+chiII)F^0_y2)`. Photo excess energy는 native source에서 `ic(E−CHI[a])`를 만들기 전에 binary64 subtraction이 일어나므로 `Psi=sum eliminated_rate*epsilon`을 포함한다. 직접 `ell*G`가 source-consistent baseline이다. C² 여부와 에너지 상쇄 여부는 별개의 주장이다.

## 4. photo denominator와 threshold

Fixed stage/energy grid에서 HI/HeI/HeII lower population은 `(1−x, f(1−y1−y2), f*y1)`다. Fixed nonnegative sigma, nH>0, d>0와 physical simplex에서 opacity≥0이므로 exact denominator `D=1+d*kappa`는 적어도 1이다. Source interval evaluation의 lower bound도 양수인지 별도로 확인해야 한다. N은 denominator에 들어가지 않는다. 따라서 N=0에서도 quotient N/D와 전체 signed derivatives는 algebraically regular하다.

`AtomicProvider::cross_section`의 fit thresholds는 `(13.60,24.59,54.42) eV`이며 binding energies CHI와 다르다. `E<eth`이면 0, 아니라면 Verner 식을 binary64로 계산해 fixed leaf로 넣는다. Gas/λ/b에 대해 E와 sigma를 고정하면 이 threshold branch는 해당 매개변수에 따라 움직이지 않는다. Gas/λ/b C² proof에 threshold-distance를 불필요하게 추가하지 말아야 한다. Energy 또는 geometry 자체를 미분 매개변수로 삼는 새로운 문제에서는 별도 piecewise analysis가 필요하다.

여기서 AtomicProvider의 f64 결과를 고정 leaf로 받는 것은 fit의 exact-real 값 자체를 rigorous하게 감싼다는 뜻이 아니다. source law/leaf identity와 fitting/model error를 구분한다. 기존 `interval_math.rs`의 exp/ln/pow는 libm 오차를 가정해 한 ulp 늘리는 구현이 아니라 positive series와 explicit geometric tail을 사용한다. Basic finite arithmetic은 next representable number로 outward 처리한다. 이 intake에서는 해당 기존 numerical suite를 다시 돌리지 않았다.

## 5. remap/birth와 C² regularity를 가르는 변수

`phys04_transport.rs::phys04_prepare_family`의 h_i, clock, dt, 33 energy nodes, 128 directions는 λ,b에 대해 고정이다. 에너지 비 r_d와 hat weights, birth angular weights는 따라서 이 가족에서 constant coefficients다. Remap은 photon/guard Jet에 대한 linear map이고 birth는 `b * fl(dt*SOURCE)`에 fixed weights를 곱해 추가하는 affine source다. full half의 다음 clock과 density leaf는 서로 다르지만 각각의 λ,b family 안에서는 고정이다.

기존 구현은 `eb.hi>20`, guard straddling 10 eV, hat knot의 엄격 내부 straddling에 대해 reject한다. 이는 frozen geometric interval을 하나의 source branch에 연결하는 요건이다. h/time을 미분하지 않는 이 연구에서 fixed hat knot 자체를 λ,b의 nonsmoothness로 오해하면 안 된다. Geometry interval crossing이 없다면 단일 분기의 coefficient proof가 가장 간단하고, crossing을 허용하려면 별도의 piecewise coefficient coverage가 필요하다.

`nonneg`는 physical value enclosure를 알려진 비음수 cone과 교차시키며 signed gradient/Hessian을 clip하지 않는다. 고정 zero stock에도 nonzero forcing Jet을 남긴다. source에 실제 `max(0,N(λ,b))`라는 물리 law를 새로 넣어 C²를 주장해서는 안 된다. b=0 및 λ=0,1은 physical rectangle의 경계지만 식은 λ에 polynomial, b에 affine이고 D>0인 open neighborhood로 algebraic extension을 만들 수 있다. 이 extension은 theorem의 C² 전제에 관한 것이며 code guard 밖의 실제 호출이나 native dispatch 권한이 아니다.

FamilyIdentity의 `theta_bits:[u64;3]`는 Hubble triplet h_i다. `uniform::Domain.theta:[Interval;2]`는 `(λ,b)`다. notation 차이를 identity binding에서 보존한다.

## 6. native point/permit 경계

`candidate/src/phys04_receipt.rs`의 `Phys04ExactPermit`은 private struct이고 public issuer가 없다. private `accepted_half1_amplitude_producer`는 `hh_source_endpoint_returned`를 호출한다. 후자는 실제 conservative point, root/certificate, same-execution carry를 생성한다. 이 경로는 source-only callback과 구분되는 actual native 실행이다. public `phys04_native_dispatch_requested()`는 현재 `PHYS04_AUTHORIZATION_NULL_BUDGET_ZERO`로 항상 실패한다. `src/certificate.rs`와 `src/uniform.rs`의 native authority wrapper도 생성 경로가 없다.

따라서 새 source-wide arithmetic을 설계·작성하는 일은 private issuer를 새로 만드는 일이 아니다. 실행할 때에도 새 source arithmetic budget와 counter를 명시하고 endpoint/conservative/internal-point/root ceiling0를 유지해야 한다. 여기서는 모든 scientific/native invocation이 0이다. NCP 반환에 기록된 과거 실행값은 읽은 증거이며 이 intake의 실행값이 아니다.

## 7. 다음 최소 물리 산출물

다음 productive gap은 실제 frozen source의 admissible C² chart와 그 X×Theta에 대한 source-derived Gc/A/full mixed partial enclosure다. Gas chart의 physical/thermal/denominator margins와 frozen geometry branch 범위를 수식 및 bounded source arithmetic으로 제시한다. 검증 가능한 whole-domain source result를 기존 UniformData에 연결하되, root 충분조건을 평가하기 전까지 root existence/U/V/W/I를 만들지 않는다. 두half의 첫 half에서 오는 U/V/W carry는 실제 predecessor family bound가 있을 때만 다음 half에 이어 붙인다. 연속시간 source law/time remainder는 이 작업만으로 닫히지 않는다.

증거 포인터: `SOURCE_INTAKE_MANIFEST.json`, `CANDIDATE_V2_PARITY.json`, `candidate/src/*`, `src/*`, `review/DECISION.json`, `delivery/NCP_RETURN_FINAL.json`, `delivery/ACK_INDEX.json`. 이 문서는 final independent decision이 아니며 source 조사자가 작성한 localization/설계 제안이다.
