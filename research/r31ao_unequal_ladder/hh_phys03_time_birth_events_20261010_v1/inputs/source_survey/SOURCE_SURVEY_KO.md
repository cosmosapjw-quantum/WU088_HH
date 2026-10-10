# WU088_HH PHYS03 원 source·시간 geometry 조사

## 판정 범위

**Actual background와 birth/remap chronology는 원 source에 존재한다. 미해결인 것은 새 공통 초기상태의 HH 강도–방출 진폭 family 구현, 그 family의 trusted native root/tube, accepted half1 전체 checkpoint receipt 및 그에 연결된 half2다. 이 결손을 “배경 이력 부재”와 합치면 안 된다.**

조사 시각은 2026-10-10 11:11 UTC 전후다. GPT-6 Astra host 선언에 맞는 research/coding v4.0.0-20260908 하네스의 기존 읽기와 AGENTS 의무를 계승했다. 이 문서는 source intake 및 후보 생성에 속하며 최종 독립 decision review가 아니다. 완료한 PHYS01/02 및 peer 과학을 재실행하거나 재감사하지 않았다. Native, BE root, IVP, NCP, legacy 적분, remote mutation은 각각 0이다.

30개 원본·계승 snapshot의 SHA256/Git blob과 25개 source 구간의 정확 line/byte binding을 확인했다. [SNAPSHOT_INDEX.json](SNAPSHOT_INDEX.json), [SOURCE_LINE_BINDINGS.json](SOURCE_LINE_BINDINGS.json), [SOURCE_IDENTITY_VERIFICATION.json](SOURCE_IDENTITY_VERIFICATION.json)이 기계 판독 가능한 근거다.

## 1. 현재 head와 실제 변경

| 역할 | branch | HEAD | tree |
|---|---|---|---|
| HH 물리 연구 | research/hh-energy06d-birth-tv-20261010 | 0bf109607e51873b6cf44ed8d3eb8f719388fb9b | 35107e42e152c404159d415cb413a6624868cbb1 |
| actual owner | research/ncp-energy06c-owner-birth-20261009 | 569b04cd71e45756e0fd476aef6643bd9434f4fa | 221c84d65f10aa51e993330eef96d54f03a6cb8e |

연구 head는 PHYS02 인계와 같다. Owner는 이전 4071666330d46df1b1965465ae2697c3a10aeb01보다 2 commits 앞섰다. 102개 추가 파일은 모두 ncp_phys01_mixed_contract_20261010_v1 및 detached delivery 패킷 안에 있다. 원 ENERGY06E runtime/source와 root AGENTS/README/RESULTS/IMPLEMENTATION_PLAN/FINAL_VERIFICATION의 blob은 바뀌지 않았다. 따라서 원 완료 과학의 재검산을 새로 요구하는 source 변경은 없다. [REMOTE_STATE.json](REMOTE_STATE.json)에 exact commit·tree·변경 경로를 보존했다.

새 owner 반환의 범위는 four-corner identity 계약과 명시적인 합성 isothermal two-coordinate BE family다. ROOT_PRECONDITIONER_BINDING.json의 합성 인증은 native_trusted=false이며 trusted_native_root, trusted_native_parameter_tube, native_preconditioner는 모두 null이다. MODEL_AND_CORNER_IDENTITY.json은 실제 native parameter/source family 미구현 및 실제 corner receipts null을 명시한다. [최신 RETURN](latest_owner/RETURN_KO.md), [root binding](latest_owner/ROOT_PRECONDITIONER_BINDING.json), [corner identity](latest_owner/MODEL_AND_CORNER_IDENTITY.json)

## 2. 실제 background와 energy law는 무엇인가

원 hh_source_endpoint는 t1=s.time_s+dt를 만들고 ConstantHubbleBackground::new([1.0;3],h)의 두 snapshot을 사용한다. Gas density는 endpoint에서

\[
n_H(t_1)=10^{-4}\exp[-(h_1+h_2+h_3)t_1],\qquad
n_{He}(t_1)=0.083\,n_H(t_1),\qquad
\bar H=(h_1+h_2+h_3)/3
\]

로 조립한다. coupled_primary::model은 실제 n_he_cm3=stage.n_h_cm3*stage.f_he를 전달한다. 배경 scale factor는 \(a_\alpha(t)=\exp(h_\alpha t)\)다. 이는 gas 해를 재적분해야 알 수 있는 미지 입력이 아니라 source에서 주어진 외부 background다. 단, native binary64 식 평가와 그 식을 실함수로 올린 연속 모델은 구분해야 한다. [hh_paired_extension.rs](source/hh_paired_extension.rs) 87–90, 137–139; [bianchi_i.rs](source/bianchi_i.rs) 67–97; [coupled_primary.rs](source/coupled_primary.rs) 60–75.

고정 normalized covariant ray \(q_d\)에 대해

\[
g_d(t)=\sqrt{\sum_{\alpha=1}^{3}q_{d\alpha}^{2}e^{-2h_\alpha t}},
\quad
r_{d,i}=g_d(t_i)/g_d(t_{i-1}),
\quad
E_{j,\mathrm{transported}}=E_j r_{d,i}.
\]

CharacteristicRay::pullback의 energy도 이 비율과 parity 검사된다. Physical-energy **node 자체는 이동하지 않는다.** energy_nodes는 [10, CHI[0], 13.6, 13.7, 20] 각 구간을 8등분한 33개 고정 node를 만든다. 방향은 n_mu=8, n_phi=16의 128개 고정 q-ray다. [paired_runtime.rs](source/paired_runtime.rs) 44–62, 109–132; [hh_paired_extension.rs](source/hh_paired_extension.rs) 94–105.

| 원 member | geometry h [s⁻¹] | HH mode |
|---|---|---|
| 0 | [1e−14, 1e−14, 1e−14] | OFF |
| 1 | [1e−14, 1e−14, 1e−14] | LCS |
| 2 | [1.01e−14, 0.99e−14, 1e−14] | OFF |
| 3 | [1.01e−14, 0.99e−14, 1e−14] | LCS |

이는 owner_birth::cfg의 source 정의다. 새 four-corner 제안은 **모든 corner에 member1의 같은 FLRW config와 같은 seed**를 쓰는 제안이다. 과거 member0과 member1의 서로 다른 누적 ON/OFF history를 그대로 두 corner로 재사용하는 제안이 아니다. [owner_birth.rs](source/owner_birth.rs) 102; [MODEL_AND_CORNER_IDENTITY.json](latest_owner/MODEL_AND_CORNER_IDENTITY.json) 18–49.

## 3. B_i, T_i와 실제 연산 순서

여기서 \(T_i\)는 gas 온도가 아니라 **old photon stock의 transport/remap 선형 연산자**다. Gas 온도와 표기를 혼동하지 않아야 한다. Guard bookkeeping을 잠시 분리하면 source 정의의 point 연산은

\[
(T_iP_{\mathrm{prev}})_{dk}
=\sum_j \phi_k(E_jr_{d,i})P_{\mathrm{prev},dj},
\qquad
B_{i,dk}=(\Delta t_i S_\star)w_d(t_i)\,\mathbf1_{k=24}
\]

형태다. \(\phi_k\)는 hat의 연속 piecewise-linear basis이며, low guard 경계 10eV와 upper guard 20eV 처리가 별도다. Birth의 angular weights는

\[
J_d(t)=e^{-(h_1+h_2+h_3)t}/g_d(t)^3,\qquad
w_d(t)=J_d(t)\Big/\sum_eJ_e(t)
\]

를 source 함수에서 native binary64 및 interval 연산으로 평가한다. 저장된 native weight/product의 합을 사후에 exact 1 또는 \(\Delta tS_\star\)로 강제로 바꾸면 안 된다. 기존 [BIRTH_LEDGER.json](history/BIRTH_LEDGER.json)은 그 작은 product-sum 차이까지 exact rational로 보존한다. 예컨대 FLRW member1 full과 half1의 저장 weights SHA도 서로 다르다. 이것은 새로운 물리 효과를 계산한 주장이 아니라 원 native 수치 의미의 구분이다.

실제 순서는 다음과 같다.

1. 이전 photons와 lower guard energy를 \(r_{d,i}\)로 이동한다.
2. 이동한 energy를 고정 energy nodes의 hat에 remap한다. 10eV 아래는 lower guard로 이동하며 20eV 위는 explicit refusal이다.
3. **Endpoint \(t_i\)** 의 source weights로 13.7eV birth를 더한다.
4. 방향별 photons를 같은 고정 energy node의 packet group으로 합친다.
5. 이전 gas state, 새로 조립된 photon numerator \(N_i=T_iP_{\rm prev}+B_i\), endpoint density를 결합해 implicit BE gas/photon solve를 한다.
6. Gas-dependent opacity에 의해 \(P_i=N_i/(1+\Delta t_i\kappa(y_i))\)를 얻고 원 compensated ledger를 갱신한다.

근거는 [hh_paired_extension.rs](source/hh_paired_extension.rs) 87–179이며, [owner_birth.rs](source/owner_birth.rs) 35–91은 pre-BE 부분만 추출한 compile-only preparation이다. Prebirth라는 type 이름에도 불구하고 반환 photons/groups에는 82–85행에서 이미 birth가 포함되어 있다. 이를 transport-only \(T_iP_{\rm prev}\)로 읽으면 안 된다.

| 경로 | 입력 clock | endpoint | BE dt | birth 위치/역할 |
|---|---:|---:|---:|---|
| full | 160000000000 | 161250000000 | 1250000000 | endpoint, diagnostic |
| half1 | 160000000000 | 160625000000 | 625000000 | 첫 endpoint, linked twohalf |
| half2 | 160625000000 | 161250000000 | 625000000 | 둘째 endpoint, exact accepted half1 필요 |

Full과 half1은 동일 원 seed에서 각각 시작한다. Half2는 half1의 반환 state에서 시작한다. HH accepted events/heat는 half1+half2만 합하고 diagnostic full을 중복 합하지 않는다. 위 schedule은 원 schemes, hh_paired_trial, 저장 SOURCE_LAW_AND_SCHEMES에 명시되어 있다. [scheme record](history/SOURCE_LAW_AND_SCHEMES.json), [birth ledger](latest_owner/BIRTH_SCHEME_LEDGER.json)

**Endpoint birth 뒤 BE dt 전체 노출은 terminal physical delta-kick와 같지 않다.** 연속시간 모델에서 \(t=t_{\rm end}\)에 막 태어난 photon은 그 이전 시간에 흡수될 수 없다. 원 scheme의 birth ordering은 numerical quadrature/operator ordering이며, true continuous source law error를 계산할 때 이를 별도의 객체로 두어야 한다.

## 4. 13.6eV cutoff와 hat switch를 정확히 구별

AtomicProvider::cross_section의 HI threshold는 **13.60eV**이며 energy_ev < eth에서 정확히 0이다. Equality에서는 fit을 평가하므로 selected bin16의 \(E=13.6\)과 \(\sigma=6.346296358990503\times10^{-18}\ \mathrm{cm^2}\)는 active다. \(CHI[0]=13.598434599702\)는 binding energy로서 다른 상수다. 원 source 주석도 fit threshold와 binding energy가 다름을 명시한다. [atomic_provider.rs](source/atomic_provider.rs) 327–353; [selected source](history/SELECTED_SOURCE.json).

Selected 25 scalar bins는 원 33 grid의 활성 packet indices 0…24다. 이 중 bins 0…15는 모든 sigma가 0이며 16…24는 HI sigma가 양수다. 원 128×33 photon state 전체가 25-coordinate state인 것은 아니다.

**Owner gas opacity는 remap 뒤의 고정 nodes[k]에서 평가된다.** Packets를 만드는 136행의 energy_ev:nodes[k], 그리고 153행의 provider.cross_section(...,nodes[k])가 직접 근거다. Transport 중의 \(E_jr\)는 105/115행에서 hat·guard 입력으로만 쓰인다.

따라서 원 owner에는 “개별 characteristic energy가 13.6eV를 통과하는 순간 RHS의 sigma를 직접 전환하는” continuous cutoff event가 없다. 13.6eV는 고정 node의 고정 sigma branch 경계인 동시에 **remap hat knot**다. 처음 bin16에 있던 물리 ray는 expansion에서 곧 13.6eV 아래로 이동하지만, 원 remap은 그 stock을 fixed nodes 15/16에 분배하므로 node16에 배정된 부분은 계속 양의 sigma를 받는다. 이것은 \(\sigma(E_{\rm ray}(t))\)를 직접 평가하는 characteristic continuous model과 동일하지 않다.

Hat knot crossing은 \(E_jr_{d,i}=E_k\), guard crossing은 \(E_jr_{d,i}=10\) 또는 20인 geometry 조건이다. FLRW의 실함수 lift에서는 \(r=e^{-H\Delta t}\)이므로 출발 node \(E_j\)에서 하향 knot \(E_k\)까지의 시간은 \(\Delta t=\log(E_j/E_k)/H\)로 쓸 수 있다. 이는 source 식의 대수적 귀결이며 이번 조사에서 새로운 event trajectory나 numerical crossing campaign을 실행하지 않았다. 원 native binary64 branching의 검증과 이 실함수 표현은 별도 의미를 가진다.

## 5. PHYS03의 a,b와 owner θ는 무엇이 다른가

이번 물리 축은 \(a=\lambda\) (HH strength), \(b=S/S_\star\) (future birth amplitude)다. 원 ENERGY06E의 theta_bits는 **0만 허용되는 fixed-configuration identity tag**다. 이 코드에는 \(\theta\mapsto E\), \(\theta\mapsto h\), source shape 등 연속 물리 변형 map이 구현되어 있지 않다. Geometry 두 선택은 member와 HhRunConfig로 정해진다. 새 owner 문서의 theta도 “same FLRW native configuration for all corners”라고만 구체화한다. Theta를 별도의 energy-shift 또는 shear amplitude라고 단정하거나 PHYS03의 b와 같게 읽을 근거가 없다. [paired_stage_receipt.rs](energy06e/paired_stage_receipt.rs) 16–24; [corner identity](latest_owner/MODEL_AND_CORNER_IDENTITY.json) 24, 43–48.

**같은 clock, fixed h/q/nodes, 같은 emission energy와 source-shape law를 유지하고 a,b만 바꾸는 모델을 명시할 경우**, source에서 background와 transport geometry는 gas 및 HH/S amplitude에 의존하지 않는다. 따라서 다음은 그 premise 아래의 source-backed 조건부 결론이다.

\[
\partial_a n_H=\partial_b n_H
=\partial_a\bar H=\partial_b\bar H
=\partial_aE_{\rm ray}=\partial_bE_{\rm ray}=0,
\qquad
\partial_a T_i=\partial_b T_i=0.
\]

정해진 birth clock 및 geometric cutoff/hat crossing clock의 a,b 미분도 0이다. 새로운 mathematical amplitude extension을 \(N_i=T_iP_{\rm prev}+bB_i^{(1)}\)로 정의하면 \(B_{i,a}=0\), \(B_{i,b}=B_i^{(1)}\)다. 그러나 **이 b-family는 원 native runtime에 아직 구현되지 않았다.** 저장 B를 exact real로 scaling할 것인지 native SOURCE 값을 바꿔 rounded product를 다시 만들 것인지도 수치 계약에서 선언해야 한다.

이 고정 geometry 결론은 이전 gas/photon 민감도를 0으로 만들지 않는다. \(N_{i,a}=T_iP_{{\rm prev},a}\)와 \(N_{i,ab}=T_iP_{{\rm prev},ab}\) 등은 대체로 nonzero이며 half2에서 reset할 수 없다. True theta/geometry family, adaptive accepted-step schedule까지 함께 바꾸는 family 또는 energy-dependent source shape 변화에는 위 zero-time-sensitivity 결론을 옮길 수 없다. 고정 clock에 대해 parameter differentiability가 성립할 수 있다는 사실은 전 구간 time-C⁵를 뜻하지도 않는다.

## 6. Selected old point의 실제 time/source 연결

저장 [OWNER_PREBE_FINAL_BINARY.jsonl](history/OWNER_PREBE_FINAL_BINARY.jsonl) **line5**는 member=1, half1_preBE, initial_time=160000000000, endpoint_time=160625000000이다. 그 33 groups에서 indices0…24를 고른 25개 binary64 값은 PHYS02 SELECTED_SOURCE.old_point_photons와 **전부 bitwise 동일**하다. Line4의 full_preBE와는 다르다. Source bits는 3cf6849b86a12b9b, birth energy bits는 402b666666666666, half1 source_n은 3.125e−6다. 기록은 native_roundtrip=true, root_dispatch=0이다. 새 native 실행 없이 저장 JSON의 binary64 identity만 비교했다.

Selected source는 time=160625000000, dt=625000000, nH=9.951928415493808e−05, nHe=8.26010058485986e−06, Hmean=1e−14를 기록한다. 원 cfg(1)의 FLRW geometry 및 first-half endpoint 조립과 연결된다. 단, 이 조사에서 원 seed 바이너리를 다시 받아 gas4를 독립 decode하지 않았다. Seed의 SHA 678f967f0d50ad1fff47a73e2e63193429b708246cd84ca8ffc72191c31b522b, 108416bytes는 새 owner의 common-initial-checkpoint 기록으로 보존한다.

**중요한 stage 의미:** hh_source_endpoint 137–139행은 gas4/escape를 이전 s.gas에서 가져오고, photons는 transport+birth 뒤 N을 사용하며, density는 t1에서 평가한다. 그러므로 SELECTED_SOURCE의 time label은 BE endpoint의 density/packet-preBE label이다. 모든 좌표가 그 physical instant의 연속해를 이루는 증거가 아니다. 이 조합을 새 연속 모델의 초기점으로 사용할 수는 있지만, 그렇게 선언한 mathematical initial slice와 실제 native continuous trajectory를 구분해야 한다. PHYS02의 frozen result는 이 기존 선언 범위에 남는다.

## 7. 존재와 미해결을 분리한 입력 표

| 입력 또는 certificate | 지금 확인한 상태 | 근거/범위 |
|---|---|---|
| nH/nHe/H background law | 존재 | 원 endpoint 및 ConstantHubbleBackground source |
| fixed energy grid / characteristic redshift law | 존재 | energy_nodes, g_point, pullback |
| full/half1 endpoint clock와 pre-BE photons | 저장 record 존재 | member1 lines4/5, full과 half1 구분 |
| half2 endpoint birth weights | 저장 record 존재 | member1 line6 |
| half2 exact incoming gas/photon/guards/compensation | 새 owner 반환에서는 null | weights-only를 state로 승격할 수 없음 |
| 역사적 ON06G/selected point·carry 기록 | 존재 | 기존 완료 run 및 PHYS02 source; 새 family 인증 아님 |
| 새 accepted half1 typed entire-checkpoint receipt | null | BIRTH_SCHEME_LEDGER 및 future-only issuer |
| 새 actual native root/parameter tube/C | null | ROOT_PRECONDITIONER_BINDING |
| native a,b common-state family | 미구현 | MODEL_AND_CORNER_IDENTITY |
| θ→physical geometry/energy continuous map | 구현되지 않음 | theta_bits=0 fixed identity만 지원 |
| true evolving gas+continuous photon source의 새 수치해/인증 | 이번 패킷에서 제공되지 않음 | background law 존재와 별개 |
| actual native 실행 권한 및 예산 | authorization=null, budget0 | EXECUTION_AUTHORIZATION_RECEIPT |

이미 존재하는 역사적 point/root 자료와 **새 공통-state parameter-family**의 receipt 부재를 같은 뜻으로 쓰지 않았다. 새 root/family gap이 순수 source/time algebra 자체를 막는다고 주장하지도 않는다.

## 8. 관련 peer 변경만 확인한 결과

| repository | 이전→현재 정확 pin | 변화와 HH에 대한 한계 |
|---|---|---|
| rei_bianchi | 718468dc75cb81fdfe0f2792aab5c8d0dbc54607 → faec51259ed26f660cf14568bcaa3d288e54bf9a | PHYS20 문서/작은 연구 패킷 39파일 추가. HH/RCT/CR OFF, directional/shear·threshold cusp 범위. HH root/history를 제공하지 않음 |
| BASS_HE | 81c1dacc1439807d41dc2684619dee499f3e06b0 → 7e82c807c372392b9f48c0ba3d77986e74d71aea | E13C2 패킷 52파일 추가. 제조된 affine gas path의 photon coefficient defect, native HH coupled proof가 아님 |
| bass_cr | 58295e59e1c1815832a26769b05a3b5fcb96b47b 유지 | 변경 없음, 재감사 없음 |

두 변경은 모두 새 docs 연구 패킷 추가이며 기존 scientific source 수정은 없다. 새 handoff와 contract/claim만 읽었다. 수치 evidence나 completed kernels를 수입·재실행하지 않았다. [REI handoff](peers/REI_PHYS20_NEXT_HANDOFF_KO.md), [REI contract](peers/REI_PHYS20_PHYSICS_CONTRACT.json), [HE DAG](peers/HE_E13C2_NEXT_DAG.json), [HE claim ledger](peers/HE_E13C2_CLAIM_LEDGER.json).

## 9. Immutable source identity와 재현

Original-owner source binding SHA256은 265c5cf32db1d6a4e795c0cb383e547bc33697b8827adf9f16fb036d20098cfe다. 표의 source는 owner HEAD 569b04에서 읽었고, PHYS02에서 이미 있던 coupled_primary는 local bytes를 재사용하여 같은 Git blob과 binding SHA256을 확인했다.

| source | bytes | Git blob SHA |
|---|---:|---|
| paired_runtime.rs | 23847 | 094be1d314090380670abd644894eb403589f367 |
| hh_paired_extension.rs | 21319 | c40ff63936afb272820bf96a615a9195885a1d80 |
| bianchi_i.rs | 7902 | 6959baae1b0619120cfc09ccf00cba6b07b98e62 |
| atomic_provider.rs | 12939 | 62211d8910cd332fffa8f94c6989cae77128916e |
| owner_birth.rs | 15697 | e60cf2c148eea9c5a3ea4fb95f7ba65b3730a1d6 |
| paired_stage_receipt.rs | 6532 | 9db0cd4e9f7f50d982cf5c9bac4d732d19f3f685 |
| coupled_primary.rs | 28863 | 99dbc26611852169679b66ef4c74c876dd7add01 |
| OWNER_PREBE_FINAL_BINARY.jsonl | 40991 | 43107e8bdf2f6aad961707a6ecdfdfa0c9ee02d3 |
| SELECTED_SOURCE.json | 6299 | 7c1f9ac466dc100ebdf8a534f5d49824c8cbe6a4 |

전체 SHA256, exact URLs와 다른 snapshots는 SNAPSHOT_INDEX에 있으며 함수별 line 범위·0-based byte start/end-exclusive·해당 segment SHA256은 SOURCE_LINE_BINDINGS에 있다. angular_photons.rs의 일반 packet bin remap과 actual paired endpoint의 hat remap은 별도 함수다. 이 조사에서는 실제 endpoint가 호출하는 paired_runtime::hat을 chronology의 근거로 사용했다. adaptive_history.rs도 immutable snapshot으로 보존했지만 이미 완료한 old solver를 재감사하지 않았다.

표준 Python으로 source identity 검사만 재현할 수 있다.

    python verify_source_intake.py --output SOURCE_IDENTITY_VERIFICATION_FRESH.json

기존 output은 거절한다. 외부 scientific dependency나 native program을 import하지 않는다. 실제 1회 source identity 실행은 exit0, 30 snapshots와 25 source 구간 PASS였다. 이는 source identity·저장 값의 일치 확인이며 물리적 bound나 native acceptance PASS가 아니다.

계승 claim ceiling은 HH ACTIVE, canonical S0 OFF control, C1 24/289·265 unbounded, epsilon_C/R null, B22 OPEN, ON06G256/t=3.2e11s, physical/production HOLD다. 기존 source-law error, mixed I, total HH D, numerical full/twohalf defect를 각각 분리한다. 새 PHYS03의 수치 특수화는 위 actual law·event ordering·선택된 mathematical initial slice를 명시하고 그 범위에서 추가 유도/검증하는 작업이다.
