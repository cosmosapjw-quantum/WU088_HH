# WU088_HH 재이온화 한정 수렴 계약

2026-10-02. 상태: DESIGNED_NOT_IMPLEMENTED. 전체 이론 완료·실제 D/epsilon 인증·production admission을 선언하지 않는다.

## 선택

이곳에서 Bianchi 재이온화에 필요한 이론과 portable reference 구현/테스트를 끝내고, NCP/local Codex에는 host-specific build/ABI, bounded heavy execution, Fortran/OpenMPI/SIMD 최적화와 실측을 넘긴다. 원 Frozen107 signed ordered coefficients, 128bit, 고정 기하/순서/오차와 2,592 primitive 계약은 보존한다. 기존20/289셀과 endpoint는 재실행하지 않는다. missing269는 미상계이며 B22는 OPEN_UNDETERMINED다.

HH 인증과 공통 H/He 재이온화 baseline을 불필요한 직렬 의존으로 묶지 않는다. HH의 D/epsilon은 원자 source/근사 판정 입력이며 σ(E), k(T), free-electron source와 같지 않다. 실제 channel/asymptotic/flux/분포 평균의 bridge를 별도로 닫는다. 기하 z와 cosmological redshift, D_HH와 Doppler factor는 이름과 단위를 분리한다.

초기 integration fixture는 기존 BASS R1의 prescribed Bianchi I, non-tilted H/He 수신기다. H-only projection은 부품 검사이며 H/He production을 대신하지 않는다. 국소 matter-frame provider를 연결하고 BASS 수송/Einstein solver를 이 저장소에서 새로 만들지 않는다. 다른 Bianchi 유형/tilt는 기존 adapter를 통해 확장 가능하되 모든 수송기의 재구현은 이 범위 밖이다.

## 닫을 작업

C0 — APPLICATION_CONTRACT와 HH_CHANNEL_CROSSWALK. 실제 state/process/source/threshold/축퇴도/분포/단위/receiver field를 하나로 연결한다. 최신 consumer의 T·energy·redshift·source SED와 observable error budget을 회수한다. 없는 수치는 null+DOMAIN_CONTRACT_REQUIRED이며 임의 기본값을 넣지 않는다. 불필요성은 정량 bound로만 판정한다.

C1 — actual represented model gap과 historical machine predicate bridge. 기존 exact decoder, exact_gram, composition adapter를 재사용한다. R31AK/R31Z/R31AD의 실제 D_col(47×2), D_row(2×47), 독립 K를 source/index/hash로 연결한다. frozen tolerance token 0x3ddb7cdfd9d7bdbb, strict near-tie, conjugation, exact Gram/radical, binary64/exact-real 경계를 검증한다. epsilon 미확보이면 최종 판정은 unresolved다. 이 단계는 새 HH 적분 없이 우선 진행한다.

C2 — portable certificate pipeline. source-bound job/coverage → 같은 primitive/window의 전체 interior → endpoint 단 한 번 → source-prescribed normalization/contraction → D/epsilon → exact gap/고정 판정기. 289 partial을 full로 승격하지 않는다. 모든 필요한 primitive의 적용 정리·error ownership을 닫고 decoder/validator/source pins를 연결한다. 자동 retry·error double counting·callback 안 literal conjugation을 금지한다.

C3 — C0에서 실제 필요한 channel만 scattering/rate bridge로 연결한다. O/H/D·독립 dotO·ionic/full49 authority, fixed-Q/ETFs, admissible propagation, asymptotic projection/flux, σ와 상대속도 평균의 전제를 각각 고정한다. actual propagation은 physical gates 후에만 한다. ionic ion-pair를 free-electron ionization으로 바꾸지 않는다. 없는 source는 UnsupportedChannel/SourceUnavailable로 반환한다.

C4 — 기존 BASS에 국소 process rate/stoichiometry/heat/opacity/source-error를 전달한다. nuclei·charge·free-electron·photon·threshold/heat ownership, double-provider rejection, zero/threshold/FLRW/Maxwell fixture를 검증한다. u_th와 순간 particle count로 온도를 복원한다. 유한 tilt의 bulk energy/frame/proper-time 계약을 생략하거나 anisotropic distribution을 scalar T_eff로 대신하지 않는다.

C5 — theory/portable implementation freeze와 실행 인계. necessary theorem premises와 physical mapping이 실제로 닫히고, entry points/API/schema/실패경로/단일 coordinator one-shot/recovery/source pins가 테스트되어야 한다. 독립 검토가 없으면 자체검토를 독립 과학 검토라 하지 않는다. 가능한 미래 종료 상태는 THEORY_SPEC_FROZEN__PORTABLE_IMPLEMENTATION_VERIFIED__NCP_CERTIFICATION_PENDING이며 현재 이 상태에 도달한 것이 아니다.

DAG: C0→C3→C4, C1→C2, 두 경로가 C5에서 합류한다. 다음 canonical node는 C0_APPLICATION_CONTRACT_AND_HH_CHANNEL_CROSSWALK. 뒤따르는 우선 구현은 C1_ACTUAL_REPRESENTED_GAP_AND_MACHINE_PREDICATE_BRIDGE다.

## NCP에 남길 것

Pinned backend/ABI/upstream tests, 실제 quota/affinity/RAM, 비특권 containment와 B22 synthetic lifecycle, 고정6셀 [275,67,288,272,16,0] 한 번, 그 결과에 따른 별도 finite batch, 전체289와2,592 primitive·D/epsilon·최종 comparator, 필요한 실제 channel/rate/consumer 수치 인증, 독립 과학 검토, Fortran/OpenMPI/SIMD 실측이다. Local Codex가 과학 가정·basis·tolerance·source SED를 새로 결정하지 않는다. Comparable serial workload 없이 speedup을 주장하지 않는다.

## 범위와 오차

범용 all-element atomic engine, 금속/먼지/분자화학 전체, full HyRec, 자체 Einstein backreaction, 새3D 재이온화 radiation-hydrodynamics, CMB likelihood/retraining은 제외한다. 단순 고정밀 가능성이 아니라 선택된 소비자의 conservation/domain/error-budget blocker만 최소 재진입 조건이다.

[HI,HII,Hminus,e]에서 ionization, ion-pair, recombination, aggregate resonant CX의 free-electron delta는 각각 [1,0,-1,0]이다. nuclei/charge delta는 모두0이다. 실제 Wolfram 기호검산을 수행했으나 HH rate를 인증한 것은 아니다. CX의 aggregate species source=0은 momentum exchange=0을 뜻하지 않는다.

비상대론적 drift-free 등방 Maxwell 상대속도에서 theta=k_B*Trel, E=mu*vrel²/2이면 k=sqrt(8/(pi*mu))*theta^(-3/2)*integral(E*sigma*exp(-E/theta)dE). 단위 m³/s, σ 단위 m²다. 임의 비등방 분포에 이 식을 폐쇄로 적용하지 않는다. positive-weight source UQ와 quadrature/tail/interpolation 항을 owner별 합성하고 HH epsilon을 소비자 observable tolerance와 직접 동일시하지 않는다.

## 근거와 durability

원 AGENTS/README, original gap-closure prompt, W3 COVERAGE STAGE_DELTA, T5 composition README, H_ATOMIC_REVISED_RESEARCH_PLAN_20260929, BASS_PRESENT_R1_NONPERTURBATIVE_MULTIFREQUENCY_HHE_REIONIZATION_CONTRACT_20260917을 읽었다. 후자의 오래된 구현 상태를 BASS 최신 상태로 추정하지 않는다. 외부 확인은 기존 C2-Ray(arXiv:1201.0602), Verner(arXiv:astro-ph/9601009), secondary-electron deposition(arXiv:0910.4410) 범위에 한정했다.

RECOVERY_PUBLICATION.json은 원 COVERAGE 다섯 파일의 두 provider ACK/ID/size와 로컬 SHA를 기록한다. old report/receipt의 과거 실패 기록은 byte-preserved다. Cloud RESTORE_VERIFIED=false. 원75개 overlay source/evidence는 두 provider의 content-addressed ZIP에 보존되며 이 Git 계약을 source-tree 전체 전개 게시로 해석하지 않는다. 상세 확장 설계와 machine DAG는 별도 CONVERGENCE_PLAN_KO.md/CONVERGENCE_PLAN.json delivery에 포함한다.
