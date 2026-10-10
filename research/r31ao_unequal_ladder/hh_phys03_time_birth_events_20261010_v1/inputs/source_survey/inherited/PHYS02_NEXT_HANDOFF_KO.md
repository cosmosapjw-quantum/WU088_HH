# 다음 WU088_HH 물리 루프: PHYS03

WU088_HH에서 PHYS02 다음 물리 연구 루프를 이어서 수행하라. 현재 채택 모델에 맞는 physmath-research-loop 하네스를 읽고 적용하되, 이미 완료한 PHYS01/PHYS02를 재시작하지 말라. 이 문서는 새 NCP/native campaign, BE 근 또는 기존 원자 적분의 실행 승인이 아니다. 기존 승인된 이론·대수·경량 검산·문서·비강제 게시·create-only 이중백업은 계속한다.

## 1. 현재 정본과 이미 닫힌 결과

- 저장소: cosmosapjw-quantum/WU088_HH.
- 현재 연구 branch: research/hh-energy06d-birth-tv-20261010. 실제 최신 HEAD를 먼저 읽되, publication receipt에 기록한 PHYS02 commit과 의미상 관계를 보존하라.
- PHYS02 디렉터리: research/r31ao_unequal_ladder/hh_phys02_finite_mixed_remainder_20261010_v1/.
- PHYS01 parent: b91a2716ef0a7f8172fa643ca4d99615e9efa443, tree d654e1349a8f2f4a30fe54bf43b1091f59f3630a.
- PHYS01 원 archive SHA256: 977ac57dc2aadfb15235c6c8e18edd495927ee8f7a68a62592273c7862b4c96c.
- 선택한 old_gas+old_point_photons JSON SHA256: 26a340065a9a99d02903bf0cc008baaf6ade00d2e845beb9d2b0b7d801316494.

PHYS02의 핵심은 같은 전체 초기상태에서 F=F0+lambda*HH+S*B를 쓰는 frozen continuous source이다. 모든 lambda∈[0,1], b=S/Sstar∈[0,1], Sstar=binary64(5e-15), 0<t<=hstar=1.25e9 s에 대해 mixed HII response가 음수임을 포함했다. tau=t/hstar, c3≈−2.0159064162896692e−17이고

    I_x/(lambda*b) ∈ c3*tau³ + [L4,U4]*tau⁴
    [L4,U4] ⊂ [5.1715113,5.4191015]e−20.

t=hstar에서는 I_x/(lambda*b)∈[−2.010735,−2.010487]e−17이며, 나머지/cubic<0.268818%. L4/U4는 전체 augmented tube의 4차 시간미분/4!이므로 모든 고차 나머지를 포함한다. 다시 24로 나누거나 hstar^4를 곱하지 않는다. lambda=0, b=0, t=0은 정확한 zero axis이다.

source의 상태·감도 52좌표가 모두 strict inclusion이며 T∈[49482.0213623,49496.1347657] K이다. 원 25개 scalar photon bin에서 16개 exact zero-sigma constant만 제거하고 활성 9개는 개별 유지했다. H/He CI/RR/두 DR/thermal/−2Hw를 남겼다. binary64 leaf를 정확한 실수로 해석한 수학식이며 native 중간 rounding replay가 아니다.

초기 4차 mixed coefficient는 S에 무관하고 lambda에 affine이다. 네 corner 차이에서는 lambda²S 항은 4차부터 나타날 수 있고 lambdaS²는 아직 없다. 기존 spectrum은 초기 K4_x에서 Gamma0=Σa_jP_j, G0=Σa_j(Ej−chi)P_j 두 가중합으로 나타나지만, 이것으로 finite-time dynamics를 닫지 않는다.

## 2. 필요한 파일만 읽어라

1. WU088_HH_PHYS02_REPORT_KO.md.
2. SCIENTIFIC_CONTRACT.md, INPUT_IDENTITY.json, CLAIM_LEDGER.json, NEXT_DAG.json.
3. results/REMAINDER_256_FINAL.json 및 independent/DECISION.json.
4. independent/HH_PHYS02_REMAINDER_DERIVATION_KO.md의 sensitivity/remainder와 event 한계.
5. 필요한 경우에만 source/frozen_source 및 원 Rust의 관련 함수.

기존 completed science full suite, PHYS01 전체 suite, ON06G history를 의례적으로 반복하지 않는다. 수입 시 manifest와 해당 source identity만 확인한다. 새 finding이나 실제 의존성 변화가 생기면 영향받는 주장만 다시 연다.

## 3. 먼저 구분할 별도 실제 owner 상태

별도 branch research/ncp-energy06c-owner-birth-20261009의 이번 확인 HEAD는 4071666330d46df1b1965465ae2697c3a10aeb01, tree608586e3d43fc725b21cec9bfb761e0eefd25374이다. ENERGY06E typed receipt/source/preconditioner/tangent 계약은 이미 게시되었다. 다음 작업으로 그 계약을 또 구현하지 말라.

실제 accepted half1, coupled root, derivative enclosure와 theta/lambda family certificate는 여전히 OPEN이다. N_i=T_i P_prev+B_i와 photon elimination P_i=N_i/(1+dt_i opacity(y_i))의 full chain을 보존해야 한다. dB/dlambda=0이어도 dP_prev/dlambda, dN/dlambda를 0으로 두면 안 된다. Half2 weights-only를 accepted state로 바꾸지 않는다.

## 4. PHYS03의 구체적인 물리 목표

frozen PHYS02와 실제 time-dependent source 사이의 차이를 정식화하고, event를 포함해 작은 HH×new-photon 혼합 응답을 유지하는 비교식을 산출하라.

### A. Smooth cell

실제 owner가 제공하는 nH(t), nHe(t), H(t), E_j(t), source/birth law를 source-bound로 식별한다. 없는 물리 background·history를 임의의 FLRW 또는 제조 이력으로 대체하지 않는다. 물리 입력이 없더라도 일반 F(t,z;lambda,b)의 sensitivity와 time-dependent Taylor/Volterra 식은 유도할 수 있다.

새 F_t, F_tz 등 explicit-time 항이 어떤 혼합 시간차수에 처음 들어가는지 분리하고, frozen result로의 극한을 보여라. 기존 photon state와 U,V,W의 초기값을 보존하라. 가능하면 작은 원 source cell에서 interval error budget을 갖는 perturbation comparison을 만들어라. time-dependent source를 다시 frozen으로 정의하여 차이를 없애지 않는다.

### B. Threshold와 birth의 event map

원 선택 spectrum에는 13.6 eV의 활성 bin16과 그 아래 zero-sigma branch가 있다. energy redshift를 포함하는 전체 단계에 무조건 global C5를 요구하거나 있다고 가정하지 말라. cutoff/hat-cell/birth/reset을 event로 분리하고 event 시각/상태 의존성에 맞는 tangent 및 mixed jump를 유도하라.

연속시간의 끝점 photon impulse와 '끝점 birth 추가 후 길이dt의 BE source 노출'은 다른 연산이다. photon birth 이전에 축적된 HH sensitivity도 이후 흡수율에 기여한다. 이 chronology를 zero reset으로 제거하지 않는다.

### C. Actual owner 연결의 완료기준

물리 모형·초기조건·네 corner/source law·stage time geometry·rate convention을 먼저 고정한다. 기존 정확한 실행 권한과 accepted state/family가 실제로 확인되는 최소 한 단위에서만 owner-bound 검사를 진행한다. PHYS02의 ~1e−17 숫자를 기준으로 native tolerance를 조정하거나 네 binary64 이력의 직접 뺄셈만으로 승인하지 않는다.

물리 inputs 또는 actual family가 없으면 그 값에 대한 수치 승격을 보류하되, A/B의 실제 유도·구현 가능한 source interface와 남은 입력 목록을 산출하라. 메타 감사/adapter만 반복하여 다음 물리 계산을 대체하지 않는다.

## 5. 계속 유지할 경계

canonical S0 HH OFF control; HH research ACTIVE; legacy accepted24/289,265unbounded; epsilon_C/R null; B22 OPEN_UNDETERMINED; ON06G256 macros/t3.2e11 및 consumed FD1/FD2/six-cell/G256 scopes. 원 native/reference, vendor, 원 checkpoint는 보호한다. BASS_HE, bass_cr, rei_bianchi 저장소는 이 HH 연구에서 수정하지 않는다. 다른 repo의 HH-OFF 결과를 공동 ON physics certificate로 전용하지 않는다.

## 6. 다음 반환물

PHYS03_THEORY_KO.md, SOURCE_AND_CORNER_IDENTITY.json, EVENT_MAPS.json, TIME_DEPENDENT_REMAINDER_OR_GAP.json, CLAIM_LEDGER.json, NEXT_DAG.json, 가능한 lightweight 계산과 원로그/최초 실패, 실제 실행/미실행 ledger 및 다음 handoff를 반환하라. 독립 decision reviewer가 후보 생성·검증 설계와 분리되어 있는지 기록하라.

Git은 기존 연구 branch에 additive non-force 게시한다. Google Drive parent1074Hr5msnAMgIXWU-PmgdMrQvrdV6emM, Dropbox /BASS_DERIVATION_DOSSIERS_20260912/WU088_HH_R31S_NCP_REDESIGN_20260928/에 create-only로 동일 ZIP을 백업한다. 두 provider의 실제 ACK/ID/name/size/path를 확인한 뒤 R1 완료를 기록한다. 실제 복원 없이 RESTORE_VERIFIED를 true로 쓰지 않는다. 완성한 결과를 보존한 뒤 다음 실제 연구를 진행한다.
