# PHYS88 결과의 수신 계약과 다음 물리 노드

## 이번에 전달하는 범위

PHYS88은 원 ENDF H1(n,γ) 자료의 native energy Es와 보간법을 유지하면서, bare n+p→d+γ에 대한 두 명시적 조건부 사상을 구현했다. 같은 source 사건의 질량 재표기에는 signed carrier를 쓰며, 새로 구성한 보존되는 bare 사건에는 그 carrier를 더하지 않는다. 새 수치 결과는 공통 T의 등방·비축퇴·독립 Jüttner n,p 분포와 원 자료의 유한 energy support에 한정된다. 실제 검증된 온도는255,10000,1e6,1e8K의 네 점이다.

Primary identity는 `2712595494bd9d784539d470c4ad0b178314c1ca55d2b0b9a75cb5dc1e6a2774`, RESULT SHA256은 `6f3f1e8d6ce07619502dee8683d8322560fe1c13e70ae27f2eb1381969500104`이다. Primary와 독립 reference의 수치 통과는 실제 bare cross-section/charge-state/source validity나 named consumer의 물리 수용을 대신하지 않는다. 최종 한정 판정은 `SCIENTIFIC_ADMISSION.json`과 독립 검토에 결속한다.

## 수신자가 함께 받아야 하는 식별자와 양

수신자는 다음 필드를 한 묶음으로 보존해야 한다.

| 필드 | 의미와 계약 |
|---|---|
| Source identity | 원 raw/table SHA, MAT/MF/MT,153knots/152cells, 원 native Es 보간법 |
| Map | LAB_ANCHORED 또는 FIXED_COM_K를 명시; `conditional_transport=true`는 모형 가정의 동의 |
| Domain | Native Es=[1e-5,2e7]eV; LAB bare support는 동일, COM bare support는[1.0002723992401612e-5,20005462.392183945]eV |
| Mass convention | 동결 nominal n/p/d/e, AWR, Qsource/Qbare, H/D binding, signed residual; covariance/physicalCI 미제공 |
| State measure | 같은 normal orthonormal frame의 proper volume·proper time; 공통 thermal T와 n_n,n_p |
| Kernel | κ [cm³/s], reaction-selected mean incoming kinetic/photon/daughter energy [eV/event], centered moments, 선택된 유한 support |
| Ownership | thermal/fast/rest/atomic/photon-handoff/photon-escape 각 열, h=0/1, 정확히 하나의 photon route |
| Verification | 실제 네 T,20primaryintegrals, 별도 최고T8fields, residual의 척도와 tolerance, 실제 실행·검토 identity |

정해진 common-frame homogeneous thermal rate를 사용할 때 event rate는 R=n_n n_p κ [cm^-3 s^-1]이다. 입자 수 열은 event당 thermal=h−2, fast=1−h, free electron=0이다. 에너지 열은 다음처럼 서로 겹치지 않는다.

`thermal=h<Kd>−<Kin>; fast=(1−h)<Kd>; nuclear_rest=−Qbare; atomic_binding=0; photon=<Eγ>`.

마지막 photon 에너지는 emissivity_handoff 또는 escape의 한 열에만 들어간다. 총 에너지 합은0이다. Gas temperature의 caloric 식은 입자 수 변화까지 포함하므로 `Cv*Tdot/R=−<Kin>+u_n+u_p+h(<Kd>−u_d)`이다. Thermal kinetic-energy debit 자체와 이 식을 동일시하지 않는다. h=1은 즉시 caloric birth를 가정한 분기이며 stopping을 계산했다는 뜻이 아니다.

표시 nominal Q 차이81.63eV는 bare 사건에 추가할 heat가 아니다. 같은 source 사건의 재표기에 쓰는 C=ΔH U_H−ΔD U_D는 일반적으로 spatial 성분이 있고 C0의 부호도 달라진다. 이 signed internal/convention reservoir를 실제 electron, photon 또는 thermal deposit으로 승격하지 않는다.

## 최신 다른 owner 결과와의 접점

BASS PR187의 photon state weight와 emission event-rate measure는 다른 양이다. 이번에 실제 읽은 BASS B3C S2 backup은 cold/recoil-free/detached f_plus=0 H_LYA_EFFECTIVE_2P,10.198714553953742eV의 manufactured14cohort 사례다. Archived contract SHA는 `2c5c1afb005d3f71894d8291928a9aa0543c2f6f8b01f6f01e26338f198264ed`, implementation SHA는 `1917f49c45cbd637f4d951a21d6e377c3cc3c58798c5e75690317eacabe68044`이다. 이 결과의 proper-clock, X-only debit, newborn midpoint timing은 수신기 설계의 근거로 재사용할 수 있다. PHYS88 capture photon의 약2.2MeV 에너지·recoil·spectrum·rate와 연결된 계약은 아직 없다. B3C가 실제 WU nuclear consumer로 binding되었다고 쓰지 않는다.

REI stock/work의 positive-measure moment 결과는 별도의 conditional stock/work 도구다. 물리 cohort/common-measure/source-history qualification과 L4ready가 남아 있으므로 PHYS88의 열 또는 Einstein backreaction을 이미 활성화한 근거로 쓰지 않는다. REC의 represented response, CR의 finite H1 CE, HE의 shape benchmark 또한 각 source/consumer 범위를 유지한다.

## 다음 단일 노드: NUCLEAR_BARE_KERNEL_SOURCE_AND_CONSUMER_CONTRACT

다음 연구는 다음 입력을 실제 owner와 원전에서 먼저 고정한다.

1. Atomic evaluated kernel을 bare capture에 쓰는 물리적 근거: charge/electron/target state, σ 및 angular law의 에너지 대응, 원 evaluation의 validity와 필요한 covariance.
2. 실제 요청 T와 energy support: 현재 finite window 밖의 입력 또는 필요한 tail 처리. 현재 sampled quadrature agreement를 continuum/tail certificate로 사용하지 않는다.
3. Named thermal/fast/radiation consumer: 같은 normal frame, proper measure, species/count/rest/binding owner, photon route와 spectral/angular 표현을 고정한다. Scalar mean만으로 joint photon distribution이나 실제 cohort history를 만들었다고 주장하지 않는다.
4. Fast daughter의 birth와 thermalization/stopping, 즉시 h=1 분기와 실제 시간 이력을 구별한다. 실제 rates와 stopping 활성화는 이 계약·물리 검토·별도 실행 수용 이후다.

Non-tilted LRS Bianchi I, reacting gasπ=0, collisionless DMπ_m 별도를 유지한다. Matter/radiation의 signed tensor를 같은 normal orthonormal frame에서 합한 뒤 norm을 취하며 Frobenius=√2×half-contraction norm이다. 동일 trajectory 성분 분해는 species-off 인과 실험이 아니다. HH_R10=OFF, production NOT_ISSUED, 전체 목표 완료율null을 유지한다.
