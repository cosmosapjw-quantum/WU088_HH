# Codex 인계 — PHYS86 완료 참조의 재사용

## 실행을 다시 하지 않고 시작할 것

실제 실행 source는 S1 280ef5094dd56b76ce4f5dc8f8aad7bc36172728다. 현재 최종 containing commit은 PR143와 외부 final-delivery receipt로 확인한다. 동일 입력/source/수용 범위에 대한 reference 재실행은 하지 않는다.

- Scientific identity: 270d59879327809203beb5f272527724ba85ceba7b3a54989b4417d02219eaa7
- Evidence identity: 90a2ca12e69fa11e13acb83e78093b35b3c51a38533b3866253ceb1568f02cbc
- Contract SHA256: ed8bb9f3aeef380b8ffcd5f190e9938b19f44bf9726fb87d1523dd423da52abd
- Freeze manifest SHA256: 194e948efd03baee8fe28475a222a156fe94e87d13937a8e11e535a43651f8d2
- Recovery request SHA256: 3db65d4d22e610b6f8d7b1903ebaf2108a73499de6cdaa44312470cfa4c237e9
- Moments request SHA256: 41e06202ad710758187c8f771e460c5b29e28a740c91f86f64ec27e44597230d

Actual whole raw와 certificate는 results/attempt_recovery 및 attempt_moments다. 독립 ACTUAL_RAW_REVIEW와 ROOT_SCIENTIFIC_DECISION이 범위를 정한다. 검사1099/1099, 새 참조2, 누적 evaluator4, 현재 추가허용0. 원문 경고를 정리하려는 목적으로 완료 identity를 재실행하지 않는다.

## 코드의 정확한 의미

source/phys85_repair01_core.wl은 부모 repaired core25893bytes를 그대로 보존한다. Original counts/guard/source 기준을 바꾸지 않고 complete compact projection으로 출력 전달을 닫았다. 이전 verbose raw를 복구한 것은 아니다.

source/reaction_moments.wl은 finite positive ensemble의 mean/variance/joint moments를 계산한다. verification/verify_reaction_moments.wl의 독립 oracle은 partition polynomial을 직접 미분한다. Constructed2×2 입력은 nuclear cross section, actual Jüttner continuum quadrature, physical EOS/rate가 아니다. C_V, R, u_c를 formal source 계수로 유지한다.

N=κ=0의 normalized moments undefined와 density 때문에 R=0인 경우를 구별한다. Nonpositive C_V를 우선 거부한다. T-dependent kernel에는 별도 A_T가 필요하며 qG witness의 잘못된 식은-1, 수정식은0이었다. 큰-z floating Bessel cancellation/production implementation은 미해결 별도 의무다.

## 다음 코드 전에 필요한 물리 입력

NUCLEAR_PHYSICAL_FINITE_T_EVENT_SUPPLIER의 source contract를 먼저 닫는다.

1. 원전의 isotope/target state, mass convention, energy/temperature domain, normalization/units, branch·angle support, uncertainty와 명시적 plasma/T 의존성을 고정한다.
2. 같은 normal-frame 사건 measure가 R, incoming energy, daughter thermal/fast count, photon/recoil/rest-energy columns를 함께 공급하게 한다.
3. PHYS86 selection/variance/covariance/joint-retention 식과 explicit-kernel correction에 입력을 대응한다.
4. 실제 source·정확도·failure disposition·비용/lease·resume identity를 고정한 뒤 최소 구현과 독립 검증을 수행한다.
5. Physical rate와 fast stopping 활성화는 source 및 energy/count ownership 검토 뒤에만 판단한다.

총 rate fit만으로 full angular joint law 또는 stopping을 만들지 않는다. 같은 frame의 signed tensor 합과 gas pi=0/DM pi_m 별도 조건을 유지한다.

## 실행·전달 정책

실제 중앙 AGENTS의 Astra contract → lower-tier implementation/bounded execution → fresh Astra actual diff/raw review 역할을 따른다. Requested model과 observed backend를 구별한다. 기존 비용·unknown 잔액·실패를 누적한다. Local reserve1.5GiB+job0.5GiB, 공유 lease와1worker/thread를 임의로 낮추지 않고 다른 process를 종료하지 않는다.

S0/S1 새 dual-ACK 선행 조건은 Drive 응답 장기 대기를 진단한 뒤 process-only로 한 번 교정했다. 원래 gate와 독립 보정 검토를 보존했고 과학 기준은 그대로였다. 백업 ACK/whole restore 완료를 이 교정으로 주장할 수 없다. 미완료 Drive/최종 JSON/PR readback이 있으면 먼저 해당 전달 상태를 실제 receipt로 확인해 마무리한다.

현재 새 단위의 바깥 파일은 변경하지 않는다. 다음 새 연구는 actual final descendant에서 additive Draft로 게시하고 expected SHA를 사용한다. Main merge0, HH_R10=OFF, production NOT_ISSUED.
