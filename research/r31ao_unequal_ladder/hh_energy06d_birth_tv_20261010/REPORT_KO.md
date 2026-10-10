# HH-ENERGY06D 연구 보고: 실제 directional birth correlation와 FD2 조건부 tail

- 기준: 2026-10-10 KST
- 판정: **STORED_DIRECTIONAL_BIRTH_MEASURE_AND_SELECTED_C1_TAIL_CHECKED__ACTUAL_COUPLED_ROOT_AND_FULL_BOX_OPEN**
- 실행 유형: ENERGY06C 원 native 출력 **읽기 전용** exact Fraction·Decimal 연구, 새로운 native science dispatch 0회

## 입력 검증과 중복 작업 배제

2026-10-09 NCP `HH-ENERGY06C` 봉인 파일 `WU088_HH_ENERGY06C_NCP_RETURN_20261009_sha_a9917ff75377.zip` (3,600,493 bytes / SHA `a9917ff7537701168e6130bac1ed536cbb621539332ca7688acf39ac08578394`)의 CRC를 확인하고 정확한 11개 소스·근거 파일만 선별 회수했다. 패키지의 전체 구현·로그·일부 source가 영구 인증된 과학 전체 해라는 뜻은 아니다. 원 `FINAL_SOURCE_BINDING_V4`의 `paired_runtime.rs`·`hh_paired_extension.rs`가 원 bytes와 일치함을 검사했다.

기존 ON06G의 256 macro, 기존 ENERGY05, NCP 34 시험, 과거 FD1/FD2/6cell은 재실행하지 않았다. NCP의 원 native preBE 12행(4 member×full/half1/half2-weight-only)의 128 방향 가중치를 직접 소비했다. Half2는 **weights-only** 자료이며 원 gas/photon state와 endpoint root를 의미하지 않는다.

## 실제 신규 결과

원 binary64의 12개 `source_n * weight` 방향별 산술값을 Fraction으로 정확히 합산한 결과 기존 NCP BIRTH_LEDGER의 exact rationals **12/12 byte-interpretation checks PASS**. 원 로그의 nominal-source와의 미소 차이도 일치했다. 이것은 새로 만든 ideal normalization이 아닌 **원 native f64 제품**을 대조한 결과다.

그와 별도로 **분석 전용** exact rational normalization을 취해 total birth W를 맞춘 후 time/angle birth difference를 계산했다. Full과 half2는 종료시각의 같은 128방향 weight arrays를 사용하며, two-half의 half1은 중간시각의 다른 weight array를 사용한다.

|member|geometry|TV_birth/W|P2(mu) birth moment/W|native f64 count defect photons/H|
|---|---|---:|---:|---:|
|0|FLRW|3.2200804523e-17|-1.3335686722e-17|-5.2939559203e-22|
|1|FLRW|3.2200804523e-17|-1.3335686722e-17|-5.2939559203e-22|
|2|Bianchi-I|2.0574538879e-08|+1.8607552023e-13|+2.3690452744e-21|
|3|Bianchi-I|2.0574538879e-08|+1.8607552023e-13|+2.3690452744e-21|

Moments use nominal `mu_i=-1+2(i+1/2)/8`, 16 phi bins/row; these are **input-grid P2 projections, not observer CMB multipoles**. Exact same-mass signed birth difference sums to zero. Native f64 count defect is separate from angular redistribution. The analytic total-variation inequality for any bounded *angular-only* kernel is proved, but nonlinear BE source error/continuous error cannot be inferred from it.

Centered birth-time first moment is `-1953.1250000000000935... s photons/H` for all four members after ideal rational normalization (exact Fraction stored in outputs). Birth schedule matching is **not** a prerequisite for two time schemes to represent the same physical emission law; the laws/authority/clock/initial state must match. Birth scheduling cannot be silently erased in a paired comparison.

## C1 별도 수학 결과

FD2 selected family k∈{1,3,5,7}, r∈{0,1,2}, N=256, whole complex input |z|≤64에 대해 `q≤64/257`, tail-factor `≤257/193`을 더 간단한 ratio proof로 얻었다. 이는 원 `6656/26471`, `26471/19815`보다 **강한 scalar 조건부 상계**다. 기존 `finite_m.hpp`, frozen interval source, queue, precision, rank/order, original accepted 24cells는 하나도 변경하지 않았다.

실제 두 셀의 whole complex physical/log box mapping, positive margin, σ≠0, holomorphic derivative and 107 signed ordered terms 검증은 **OPEN**. C1 candidate field 107 finite observation을 native integration radius proof로 승격하지 않았다.

## 검증 규모와 실패 기록

새 단위시험 18개 통과. 최초 born-product 검사는 stub에서 assertion **RED→GREEN**, C1 selected-tail 검사와 P2 moment 검사도 각각 의도된 assertion RED를 관측한 뒤 GREEN. 다른 15개는 후속 coverage; 3개 대표 RED 중 하나는 test file 공유 setup을 통한 scoped assertion임을 분명히 한다. 원본 half2-weight-only 레코드에는 `source_bits`, `energy_bits`, `endpoint_time` 필드가 없으므로, 초기 분석 코드의 'half2 source_bits 필수' 가정이 fail-closed로 거절된 뒤 **필드 부재를 그대로 인정하도록 수정**했다. 이를 산출물 조작이나 root 결손의 보정이라고 하지 않는다.

독립 Decimal 160자리 검산은 4member × 4항목 **16개** 비교에서 Fraction 결과와 일치하며, 최대 Decimal 차이는 `5.60565e-167` (수치 산술 대조에만 해당)이다. Native derived inputs/가중치/clock/source는 기존 소스와 공유한다. 별도 외부 전문가 리뷰나 formal proof assistant 검증은 없음.

기존 결과는 수정하지 않으며 새 source/ledger/checkpoint/new paired root 과학 실행·원격 owner adoption을 시도하지 않았다. Git/백업 상태는 배포 후 detached delivery receipt를 따른다. **과학 수락 상태는 변하지 않는다.**

## 남은 작업

1. `HH-ENERGY06E_CORRELATED_OWNER_ROOT_PROVENANCE`: source/pair origin, same θ·λ, full/half1→half2 gas/photon/guard state와 signed derivatives의 증명 객체를 별도 resolver에서 강제 검증한다. BE implicit photon elimination을 포함한 `M_i`와 original preconditioner의 source hash·조건수를 결속한다. 실제 유일근 Krawczyk 포함이 없으면 abort/fail closed.
2. `HH-ENERGY06F_ACCEPTANCE_AND_DISCRETE_DEFECT`: owner의 동일 source law, 서로 다른 discrete birth schedules 및 native ledgers를 보존한 채 새 과학 실행 *사전 승인 scope*가 실제 봉인된 경우에만 수행. 기존 256 macro를 replay하지 않는다.
3. `C1_272_000_FULL_BOX_PROOF`: 선택 1F1 scalar tail 검증을 full-box/holomorphic/cgroup exact proof와 독립시킨다. 기존 consumed approvals를 재사용하지 않는다.

별도 REI/HE/CR owner의 science gates도 무단 대체하지 않는다.
