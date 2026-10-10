# WU088_HH 다음 물리 루프 인계 — PHYS03 완료

## 바로 이어갈 물리 목표

PHYS04는 fixed-grid remap과 H/He·thermal feedback을 보존한
full/two-half 혼합 반응의 quartic 및 opacity-weighted defect를 다룬다.
PHYS03의 새 결과를 다시 유도하는 데 한 루프를 쓰지 않는다.

우선 FINAL_REPORT_KO.md, FINAL_STATUS_KO.md, independent/DECISION.json,
NEXT_DAG.json을 읽고, 필요한 증명만 선택해서 확인한다.
Git의 이 패킷 경로는 다음과 같다.

    research/r31ao_unequal_ladder/hh_phys03_time_birth_events_20261010_v1/

실제 publication commit/tree와 archive SHA는 detached
WU088_HH_PHYS03_DELIVERY_RECEIPT.json에 기록한다.
패킷 안에 자기 자신의 commit/ZIP hash를 넣지 않는다.

## 채택된 과학과 제한

1. Smooth source의 \(K_3=H_zJB+2Q(H,B)\)는 explicit-time derivative에
   영향받지 않는다. Quartic 보정은 smooth_theory 문서 식 (4.4)를 쓴다.
   Photon-independent nonphoto coefficient의 explicit-time drift만은
   mixed quartic에서 소거되지만 instantaneous nonphoto 장은 유지한다.
2. Birth 시각 \(s\) 이전의 HH memory를 보존한다.
   \(\mathcal K_x=-Aq[s(t-s)+(3+\Xi)(t-s)^2/2]+O(t^3)\).
   Birth마다 \(U,W\)를 0으로 reset하지 않는다.
3. Repeated frozen birth+BE의 formal cubic은
   \(C_m=(4+\Xi)/6+(3+\Xi)/(2m)+(5+2\Xi)/(6m^2)\)다.
   Actual finite BE root 또는 error로 읽지 않는다.
4. 고정 scheduled map \(R=Lz+bB_e\)는
   \(U^+=LU,\ V^+=LV+B_e,\ W^+=LW\).
   General moving-event 식은 HYBRID_THEORY_KO.md를 사용하되
   regularity/transversality와 공통 시각 동기화 조건을 지킨다.
5. Actual FLRW fixed-grid threshold column:
   full active weight 0.1312180649460370,
   two-half 0.3199120420203140.
   Difference는 \(K(K-1)(1-r)^2>0\)이고
   photon N/E 보존이 opacity 보존을 보장하지 않는다.
   단위 basis column의 real-expression 진단이며 gas trajectory가 아니다.

Finite continuous PHYS02의 부호 정리는 원 선언 범위에서 유지된다.
새 actual finite sign은 KEEP_UNRESOLVED다. Actual source와 reference의
초기 slice, future birth 의미, clock을 맞춘 뒤 augmented error를
제어해야 한다. REMAINDER_TRANSFER_KO.md의 충분조건을 참고한다.

## Source identity에서 다시 혼동하지 말 것

- 연구 parent PHYS02 HEAD: 0bf109607e51873b6cf44ed8d3eb8f719388fb9b.
- Actual owner HEAD: 569b04cd71e45756e0fd476aef6643bd9434f4fa.
- Actual owner branch: research/ncp-energy06c-owner-birth-20261009.
- 연구 branch: research/hh-energy06d-birth-tv-20261010.
- Selected input SHA-256:
  26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494.
- Background가 실제로 존재한다. \(a_i=e^{h_it}\),
  \(n_H=10^{-4}e^{-\sum h_i t}\), \(n_{He}=0.083n_H\)다.
- 실제 순서는 transport → fixed-grid hat remap → endpoint birth →
  old gas + endpoint density를 사용하는 coupled BE다.
- Cross section은 fixed energy node에서 평가한다.
  Moving ray cutoff event로 대체하지 않는다.
- HI fit cutoff 13.60 eV와 binding energy 13.598434599702 eV는 다르다.
- Selected old photons는 member1 half1_preBE line5의 25 groups와 bitwise 같다.
  그 aggregate의 gas는 t0, photon numerator/density는 t1이다.
  Native continuous snapshot이나 raw macro predecessor로 승격하지 않는다.
- PHYS03의 \(b=S/S_*\)는 future source amplitude.
  Owner의 theta_bits=0은 fixed-configuration tag이며 b가 아니다.
- 실제 새 owner의 common-state amplitude family는 미구현이다.
  Synthetic isothermal mixed family의 root 인증은 actual native root가 아니다.

Source snapshot과 구간 hash는 inputs/source_survey에 있다.
원 seed binary의 gas4를 이번 루프에서 독립 decode하지 않았다는
한계가 있다. 필요한 PHYS04 raw input은 원 typed checkpoint와
schema를 정확히 연결해서 얻는다. PreBE aggregate로 대신하지 않는다.

## PHYS04의 구체적인 작업 순서

1. Source/owner HEAD가 바뀌었으면 PHYS03 이후 추가분과 handoff만 읽는다.
   같은 source blob이면 기존 identity와 완료 과학 검증을 그대로 계승한다.
2. 먼저 비교할 raw initial slice와 real amplitude lift를 고정한다.
   기존 owner의 four-corner 계약을 재사용하고 새로운 adapter 문서로
   같은 결손만 반복하지 않는다.
3. \(h\downarrow0\)의 fixed-grid one-sided remap expansion을 구한다.
   Node에서 출발하므로 일반 two-sided \(C^2\) 가정은 쓰지 않는다.
   Guard bookkeeping, cutoff 및 이동 방향을 포함한다.
4. Exact source order를 보존한 formal BE mixed quartic을 도출한다.
   Density sampling, remap과 gas-dependent opacity의 비가환 항,
   H/He와 HH 열 feedback, 이전 \(U,V,W\)의 연결을 분리한다.
5. Source-bound remap/opacity functional은 bounded algebra/interval
   evaluation로 수치화할 수 있다. Native gas trajectory로 표현하지 않는다.
6. Actual common-state root/tube, accepted half1 entire checkpoint와 half2
   incoming state가 제공되면 augmented map bound에 연결한다.
   그 전에는 root가 없다는 이유로 가능한 algebra를 멈추지 않되,
   실제 finite sign/accuracy admission은 하지 않는다.

## 실행과 보존

이 session은 사용자 요청과 기존 인계의 범위에서 이론·코드·bounded
검산, additive non-force 연구 branch push, 지정 Google Drive/Dropbox
create-only backup을 승인받아 진행했다. 이 이미 승인된 범위를 다시
확인 질문으로 멈추지 않는다. Native 실행은 이 승인과 별개다.

새 actual owner의 native authorization은 null, budget0이다.
Native dispatch, nonlinear BE root, IVP, NCP, 완료한 atomic integral,
PHYS01/02 또는 peer의 완료 suite를 재실행하지 않는다.
사용자가 이후 범위를 명시적으로 바꾸면 그 새 지시를 우선 적용한다.

계승 상태:
HH research ACTIVE; canonical S0 HH OFF control;
legacy C1 24/289, 265 unbounded; epsilon_C/R null; B22 OPEN;
ON06G 256 macro, t=3.2e11 s 및 consumed scope 보존;
physical/production HOLD.

Research/coding harness는 host-declared GPT-6 Astra Pro에 맞는
Astra v4.0.0-20260908을 적용했다. 런타임 attestation은 제공되지 않았다.
독립 최종 reviewer는 이번 candidate 생성/검증설계에 참여하지 않은
/root/decision_review다. 실제 판정은 independent/DECISION.json을 확인한다.

## 재현과 산출물

REPRODUCE_KO.md와 reproduce.py는 새 output directory만 사용한다.
기존 evidence를 덮어쓰지 않는다. manifest 확인만으로 충분한 상황에서
완료한 과학 검사를 다시 돌리지 않는다.
문서 저장 형식 오류와 복구는 failures에 남아 있고,
새 과학 checker의 최초 실행은 PASS였다.

Source branch publication과 backup의 증거 수준은 detached receipt에서
확인한다. Upload ACK/metadata 확인과 원격 bytes 복원 검증은 다른 상태다.
R1을 RESTORE_VERIFIED로 바꾸어 읽지 않는다.
