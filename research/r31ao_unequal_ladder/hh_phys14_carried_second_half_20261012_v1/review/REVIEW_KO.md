# WU088_HH PHYS14 독립 검토

## 판정

**PROMOTE_SCOPED.** PHYS14는 같은 COMMON에서 출발한 첫 half의 기체·광자 carry를 실제 다음 half의 implicit 식에 넣고, 두 번째 단계의 균일 근 포함과 일차·혼합 응답을 새로 계산했다. 원 FT03/HH source 포함과 첫 단계의 고정 계수 C² 근 계열을 전제로, 현재 등방 기하학 subfamily의 두-half endpoint 결과를 채택한다. 최종 후보 코드와 결과에 차단 항목은 없다.

검토자는 `/root/hh_phys14_review`다. 후보 이론·과학 코드·후보 검증 설계에 참여하지 않았고 후보 파일을 수정하지 않았다. 후보 모듈을 import하거나 `main`을 실행하지 않고, 실제 원 source를 읽은 뒤 별도의 유리수 산술로 저장된 증거를 검토했다. 후보 이론 작성자의 supplemental oracle은 별도 역할의 검증 증거로 확인했다.

## 1. 채택되는 계열과 새 단계

시간은 `t0=1.6e11 s`, `h1=h2=6.25e8 s`, `t2=1.6125e11 s`다. 전역 미래 파라미터 λ와 b를 두 단계에 공통으로 유지한다. 실제 과학 계열은 **연속된 두-half history 하나**, 새 implicit 단계는 그중 두 번째 하나다.

원 `paired_runtime.rs`의 `g_box`는 등방 조건에서 `G_r(t)=exp(-Ht)||q_r||`로 인수분해된다. 따라서 같은 captured q의 norm이 시간비에서 상쇄되어 `rho=exp(-Hh)`가 모든 ray에 공통이다. Source weight의 원 실수 기하학은 `||q_r||^-3`을 그 합으로 정상화한 값이다. Photon group 합과 전체 guard 수·에너지는 공통 선형 transport 및 공통 absorption denominator와 교환한다. Gas residual도 group 합에만 의존하므로, 유일 근 조건 아래 `(gas4, groups33, guard2)`의 **39상태 축약**이 닫힌다. 이는 현재 관측량을 계산하는 정확한 대수적 축약이다.

검토자는 exact Fraction 교대급수로 두 원 단계의 exp(-Hh)를 포함하고, captured q norm은 integer square-root 포함으로 별도 계산했다. 공통 rho가 Full 및 first_half의 각 128개 원 ray ratio 구간에 들어갔고, 정상화한 128개 weight도 모두 원 weight 구간에 들어갔다. 현재 geometric subfamily가 원 포함 증거에 연결된다. 원 native 스칼라 capture graph의 권한은 별도 상태로 유지된다.

## 2. Full source 재사용과 새 근 포함

`phys04_reduced_residual`, `ft03_interval_rhs`, `coupled_primary::model`, `hh_rate_jet`을 읽었다. Nonphoto와 q는 현재 gas 좌표 및 고정 stage/atomic leaves의 함수다. 이전 gas, incoming photons, 시간 길이는 이 두 부분에 직접 들어가지 않는다. 둘째 half의 끝시각은 원 Full과 같고, 이번 계산은 실제 Full의 endpoint leaves를 그대로 사용한다. 새 half 길이와 새 photon incoming에 대한 photo 부분은 PHYS14가 새로 조립했다.

Taylor 기준점도 실제 captured binary64 centre `(0.915,0.3,0.6,13.5)`에 연결돼 있다. 이 기준점과 원 전체 X에서의 gas gradient/Hessian을 이용한 mean-value 교집합은 동일 함수의 포함이다. Hessian의 인덱스와 원 signed endpoint를 유지했다.

독립 고정밀 산술로 다음 사항을 확인했다.

- 원 X에서 `g1 + h F2(X)`가 네 좌표 모두 strict self-map이다.
- 원 X의 scaled infinity contraction 상계는 `[0.0005392100481790, 0.0005392100481791]` 안에 있다.
- 저장된 네 번의 root refinement가 원 포함에서 정당하게 좁혀진다.
- 최종 root에서의 contraction 상계는 `[0.0005045844357587, 0.0005045844357588]` 안에 있다.
- 33개 photon denominator는 모두 양수다.

Banach 정리가 각 고정 계열 성원의 둘째 근 존재·유일성을 준다. Strict interior와 가역 Jacobian, 원 source 및 incoming의 C² 전제를 함께 사용하면 같은 파라미터 rectangle에서 둘째 근의 C² 연속 계열이 이어진다. 첫 단계 근 계열과 FT03/HH kernel의 포함은 이전 증거에서 상속하고, **둘째 단계 self-map·contraction·응답 포함은 이번의 새 증거**로 구별했다.

## 3. 일차·혼합 응답과 물리적 결과

HI photo의 gas Jacobian은 x 열 하나이고, 새 photon memory는 x,w 행에 들어간다. Code의 K, K′, K″와 q·nonphoto의 gas Hessian을 확인했다. Mixed forcing에는 이전 gas W, gas Hessian UV, 두 gas–incoming 교차항, incoming photon W가 모두 들어 있다. 동일한 새 U,V를 사용한 W forcing이며, incoming은 현재 gas unknown에 독립인 전달 입력으로 처리한다.

`A=I-hF_g`에 대한 Neumann 다항식은 차수 8까지 포함하고, 나머지를 `q^9/(1-q)`의 scaled norm 상계로 닫는다. 별도 380+ significant-bit 유리수 구간 계산으로 U,V,W의 RHS, Jacobian, tail 및 저장된 solution 포함을 확인했다. Direct HH·gas memory·photon memory의 세 기여에도 같은 역행렬을 적용했다.

원 source에 맞춘 `fhat=exact(nHe_stored)/exact(nH)`와 `C_T=2 exact(eV)/(3 exact(kB))`를 유지했다. Stage f와 fhat를 구별하며, e와 T의 일차·혼합 체인룰을 검토했다. 실제 포함은 다음과 같다. 모든 유한 차이는 같은 전역 파라미터 계열의 FTC로 전달된다.

| 관측량 | 두-half endpoint의 포함 |
|---|---:|
| HH 추가 자유전자, electrons/H | `[1.343169300092e-10, 2.595287368628e-10]` |
| HH 온도 응답, K | `[-1.893684639279e-5, -9.751531029264e-6]` |
| Birth 추가 자유전자, electrons/H | `[8.548580514394e-9, 9.901746622979e-9]` |
| Birth 열에너지 응답, eV/H | `[8.733265021478e-10, 1.014234750421e-9]` |
| Birth 온도 응답, K | `[-2.278717930823e-4, -1.931735858256e-4]` |
| HH–birth 혼합 온도 응답, K | `[1.966322264584e-12, 3.448057221983e-12]` |
| HH–birth 혼합 자유전자 응답, electrons/H | `[-6.233916429722e-17, -3.439765714258e-17]` |

세 HH 온도 기여도 각각 음수다. 이전 gas 기여는 `[-1.141841000568e-5,-3.729392608696e-6] K`, 둘째 단계 direct HH는 `[-7.518434739815e-6,-6.022137910732e-6] K`, **이전 photon memory는 `[-1.649099651540e-12,-4.924434099674e-13] K`**에 포함된다. 세 값은 동일 λ 미분의 전달 기여로 정의된다. Photon memory 기여는 33개 node의 실제 값 및 signed tail을 모두 유지한 합으로 판정했으므로, 별도의 정확한 `E≤13.7 eV` support 가정을 이 수치 부호 판정에 추가하지 않는다.

## 4. Spectral remap 분할 효과

비균일 원 energy node에 대한 linked polynomial 식과 lower-guard의 j=1 경계식을 검토했다. 첫 half rho에 대해 정리의 branch 조건은 j=2..32에서 모두 성립한다. 각 column의 photon-number 및 energy moment가 정확히 상쇄되고, j=1은 guard 기여를 포함할 때 상쇄된다.

실제 COMMON spectrum에 transport-only 연산자 `R(rho)^2 - R(rho^2)`를 적용한 HI-active group 수 차이는

`[-8.680771077461e-9, -8.680422250484e-9] photons/H`

로 엄밀히 음수다. 최대 column L1 포함은 `[0.7547759083005,0.7547759083006]`이다. 독립 산술에서 j=1 guard boundary column도 이 최대보다 작음을 확인했다. 이 결과는 **같은 입력 spectrum에 대한 remap operator 차이**로 채택한다. 실제 두-half 온도 응답과 이 operator 진단의 물리적 역할을 각각 기록했다.

원 `CHI_H=13.598434599702 eV` leaf와 현재 sigma table의 최초 HI-active sampled node인 `E16=13.6 eV`를 구별한다. 이번 계산은 원 33 energy leaves와 sigma leaves를 그대로 소비했다.

## 5. 검증의 실제 실행과 파일 연결

후보의 과학 실행 `advance01`은 첫 실행에서 exit 0으로 완료됐다. Process wall은 0.666850초, CPU는 user 0.611015초 + system 0.027752초, RSS는 41016 KiB였다. 원 후보 코드와 결과의 실행 연결을 확인했다.

검토자의 `independent_arithmetic.py`는 원 입력 45개 파일, source centre, 실제 PHYS11에서 둘째 incoming으로 가는 33-node·guard 전달, root/source/linear/readout 및 remap 수치를 별도 산술로 검사했다. 최종 실행은 0.621842초였고 2,713개 assertion이 통과했다. 그중 십진 외향 표시와 부호 label 검사는 각각 861개다. `geometry_review.py`의 528개 assertion은 반복 captured q와 원 geometry row의 확인을 포함한다. **이 수들은 독립 물리 실험 수를 나타내지 않는다.** 과학 history 한 계열에 대한 증거 범위와, 다섯 종류의 작은 독립 산술·Jet 의미 검사를 구분해 기록했다.

Outgoing photon의 independent four-slot Jet 표현은 모든 저장 결과와 겹치고 각 node의 absorption 수지 포함은 영을 포함한다. 해당 exact quotient 항등식과 두 mixed 교차항은 코드 및 작은 유리함수 oracle로 확인했다. Source/root/linear/readout 및 remap 항목은 저장 구간이 별도 고정밀 계산을 포함하는 것을 확인했다.

별도로 후보 이론 작성자가 실행한 `evidence/oracles/`도 검토했다. Candidate dyadic 함수를 known-binade Euclidean oracle과 비교한 306개 signed point, 지수 ±16384 및 `2^-100000` tail, zero divisor 처리가 실제 통과했다. 비선형 scalar quadratic root의 closed form을 별도 truncated polynomial algebra에서 계산하고, 두 q 변형에 대한 gas/photon U,V,W 및 누락 교차항을 후보 함수에 대조했다. 이 0.164559초의 supplemental 실행은 과학 history 실행 수에 추가하지 않는다.

## 6. 해결 사항과 완료 조건

Eq.(23)의 bracket 안 쉼표 두 개를 제거하는 편집 수정을 확인했다. 수정 전 이론은 `theory/versions/`에 보존됐고, 과학 코드·결과는 byte-identical이다. 최종 이론 SHA256은 `0eb0a8374470498e9320e0a6191d72d0a5f5e15c0162a7f633b5e3e52f2da125`다.

현재 채택 범위는 지정된 source-aligned 등방 두-half 계열, 그 39상태 관측량 축약, 새 둘째 근 포함·유한 응답, 동일 COMMON의 remap operator 진단이다. 첫 단계 source/C² 전제와 저장 atomic source 포함을 계승한다. Native history, 다른 배경·시간 격자, 실제 소비자 적용은 해당 별도 입력과 계약에 연결하는 후속 작업이다.

**판정에 필요한 위험은 해소됐다.** 추가 과거 suite 재실행 없이 현재 산출물의 상태 갱신·게시·백업·전달로 진행한다. 게시와 백업의 실제 remote identity는 owner의 완료 기록에 연결한다.
